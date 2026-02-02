---
layout: post
title: 'Bolstering Claude Code: A Personal Development Environment Configuration Guide'
description: A comprehensive guide to configuring Claude Code with Model Context Protocols
  (MCPs) for enhanced AI-assisted development workflows
tags:
- AI
- Automation
- Configuration
- LLM
- Productivity
categories:
- AI
- Development
date: 2025-12-01T12:21:00+00:00
---
## Introduction

This guide walks through my personal Claude Code configuration, enhanced with multiple Model Context Protocol (MCP) servers that integrate with various tools and data sources. While this represents my specific setup, it's designed to be adaptable for any developer who wants to boost their AI-assisted development workflows.

Yes, it was authored largely by Claude, but reviewed by me.

### What You'll Learn

- How to configure Claude Code for enterprise use
- Setting up essential MCPs (Memory, Filesystem, Tavily)
- Integrating enterprise-specific MCPs (Atlassian, cloud cost management)
- Practical examples of using MCPs together for real workflows
- My dotfiles and configuration management approach with YADM

### Prerequisites

- Claude Code installed ([official installation guide](https://docs.anthropic.com/en/docs/claude-code))
- Basic terminal/command-line proficiency
- Node.js/npm installed (for some MCPs)

---

## Part 1: Claude Code Installation & Configuration

### Installing Claude Code

```bash
# Install Claude Code via npm
npm install -g @anthropic-ai/claude-code
```

If you're using an enterprise LLM gateway or proxy, add the following to your shell configuration (e.g., `~/.zshrc`):

```bash
# Configure for your API endpoint (if using a proxy/gateway)
export ANTHROPIC_BASE_URL="https://your-llm-gateway.example.com"
export ANTHROPIC_AUTH_TOKEN="your_api_key"
```

### First Run

```bash
# In your project directory
claude

# You'll be prompted to authenticate
# If switching API endpoints, run:
claude /logout
```

### Configuration Files

[Claude Code uses two main configuration files](https://docs.anthropic.com/en/docs/claude-code/settings):

- `~/.claude/settings.json` - Global settings (permissions, model, hooks)
- `<projectrepo>/.claude/settings.json` - Project-specific MCP servers (typically version-controlled)

---

## Part 2: Essential MCP Setup

### What are MCPs?

Model Context Protocols extend Claude's capabilities by connecting it to external tools and data sources. Think of them as plugins that give Claude access to:

- Your filesystem
- Memory and knowledge graphs
- Web search capabilities
- Enterprise systems (Jira, Confluence, databases)
- Cloud cost management
- And much more

### MCP Server Types

MCPs come in three transport types:

1. **stdio** - Local command-line tools (npx, python scripts)
2. **SSE** (Server-Sent Events) - Remote HTTP servers
3. **http** - Standard HTTP APIs

### Global MCPs: The Foundation

These MCPs are available in standard Claude Code installations and should be your starting point:

> **Note:** MCPs are by default scoped to 'local', i.e. `<cwd>/.claude/settings.local.json` or a similar location. [See here for an explanation of Scopes](https://docs.anthropic.com/en/docs/claude-code/mcp#choosing-the-right-scope), but I generally experiment with the default scope and then manually add new MCPs to my global `~/.claude/settings.json` scope once I understand/trust it.

#### 1. Memory MCP - Persistent Knowledge Graphs

**Purpose:** Maintains context and relationships across conversations

```bash
# Install via CLI
claude mcp add memory npx @modelcontextprotocol/server-memory
```

**What Memory MCP Does:**

- Stores entities (people, projects, concepts) and their relationships
- Remembers your preferences and coding patterns
- Builds institutional knowledge over time
- Enables questions like "What did I decide about authentication last week?"

**Example Usage:**

```
You: "Remember that we decided to use JWT tokens for the API authentication"
Claude: [Creates entity: API Authentication, adds observation: Uses JWT tokens]

Later...
You: "What authentication method are we using?"
Claude: [Queries memory] "You're using JWT tokens for API authentication"
```

#### 2. Filesystem MCP - Direct File Access

**Purpose:** Allows Claude to read and write files in specified directories

```bash
# Install via CLI
claude mcp add filesystem npx -y @modelcontextprotocol/server-filesystem /Users/yourusername
# You can specify multiple directories
```

**Security Note:** Only grant access to directories you're comfortable having Claude modify!

**What Filesystem MCP Does:**

- Read file contents
- Write and edit files
- List directory structures
- Batch file operations

**Example Usage:**

```
You: "Review all Python files in the src/ directory for security issues"
Claude: [Reads multiple files via filesystem MCP, analyzes, reports findings]
```

#### 3. Tavily MCP - Web Search & Content Extraction

**Purpose:** Enables web search and content extraction (preferred over built-in WebSearch for reliability)

**Getting your Tavily API key:**

1. Sign up at [tavily.com](https://tavily.com)
2. Navigate to your [API Keys dashboard](https://app.tavily.com/home)
3. Generate a new API key for Claude Code
4. Set it as an environment variable in your shell configuration:

```bash
export TAVILY_API_KEY="your_tavily_key"
```

```bash
# Install via CLI
claude mcp add tavily -e 'TAVILY_API_KEY=${TAVILY_API_KEY}' -- npx -y @modelcontextprotocol/server-tavily
```

Or add to your `~/.claude/settings.json`:

```json
{
  "tavily": {
    "type": "stdio",
    "command": "npx",
    "args": ["-y", "@modelcontextprotocol/server-tavily"],
    "env": {
      "TAVILY_API_KEY": "${TAVILY_API_KEY}"
    }
  }
}
```

**What Tavily MCP Does:**

- Web search with AI-optimized results
- Extract content from URLs
- Crawl and map websites
- Answer questions using current web information

---

## Part 3: Enterprise MCPs

These MCPs integrate with enterprise systems and may require specific access.

### 1. Atlassian MCP - Jira & Confluence Integration

**Purpose:** Native integration with Jira and Confluence

**Configuration:**

```bash
# Install via CLI
claude mcp add atlassian --transport sse https://mcp.atlassian.com/v1/sse
```

Or in your settings:

```json
{
  "atlassian": {
    "type": "sse",
    "url": "https://mcp.atlassian.com/v1/sse"
  }
}
```

**Requirements:**

- OAuth authentication (browser-based, one-time setup)
- Appropriate Jira/Confluence permissions

**Important Notes:**

- Atlassian queries can return very large outputs - use Task/Agent tools for searches when possible
- When creating Confluence pages via MCP, consider adding an `ai-generated` label for transparency

**What Atlassian MCP Provides:**

- Search Jira issues using JQL
- Create, read, update Jira issues
- Search and read Confluence pages
- Create and update Confluence content
- Comment on issues and pages
- Manage Jira workflows and transitions

**Example Use Cases:**

```
You: "Find all critical bugs assigned to me that are still open"
Claude: [Searches Jira with JQL: assignee = currentUser() AND priority = Critical AND status != Closed]

You: "Create a Confluence page documenting our new API authentication flow"
Claude: [Creates page in your space, adds content]

You: "What were the main discussion points in the last team meeting notes?"
Claude: [Searches Confluence, retrieves page, summarizes]
```

### 2. Vantage MCP - Cloud Cost Management

**Purpose:** FinOps analytics and cloud cost optimization (At Black Duck we use Vantage, but YMMV)

**Configuration:**

```bash
# Install via CLI
claude mcp add vantage --transport sse https://mcp.vantage.sh/sse
```

```json
{
  "vantage": {
    "type": "sse",
    "url": "https://mcp.vantage.sh/sse"
  }
}
```

**Requirements:**

- Vantage account access
- OAuth authentication (browser-based)
- Appropriate workspace permissions

**What Vantage MCP Provides:**

- Multi-cloud cost analytics (AWS, Azure, GCP, 50+ SaaS providers)
- Budget creation and monitoring
- Cost optimization recommendations
- VQL (Vantage Query Language) for advanced filtering
- Anomaly detection for cost spikes
- Forecasting and planning

**Important:** Vantage cost queries can return very large outputs - use Task/Agent tools for analysis

**Example Use Cases:**

```
You: "What was our total AWS spend last month broken down by service?"
Claude: [Queries Vantage, returns cost breakdown with trends]

You: "Show me cost optimization recommendations for rightsizing EC2 instances"
Claude: [Lists recommendations with potential savings]

You: "Create a budget for $10k/month for our production AWS account"
Claude: [Creates budget with alerts]
```

---

## Part 4: Complete Configuration Example

Here's my `~/.claude/settings.json` configuration (with sensitive tokens removed):

```json
{
  "model": "claude-sonnet-4-5-20250929",
  "verbose": true,
  "permissions": {
    "allow": [
      "Bash(find :*)",
      "Bash(git :*)",
      "Bash(rg :*)",
      "Bash(uv :*)",
      "Bash(uvx :*)",
      "Bash(grep :*)",
      "Read",
      "Edit",
      "Write",
      "WebFetch",
      "Bash(make:*)",
      "Bash(gh act:*)",
      "Bash(curl:*)"
    ],
    "deny": [
      "WebSearch"
    ]
  },
  "statusLine": {
    "type": "command",
    "command": "input=$(cat); cwd=$(echo \"$input\" | jq -r '.workspace.current_dir // .cwd'); user=$(whoami); host=$(hostname -s); if [[ \"$cwd\" == \"$HOME\"* ]]; then dir=\"~${cwd#$HOME}\"; else dir=\"$cwd\"; fi; if git -C \"$cwd\" --no-optional-locks rev-parse --git-dir >/dev/null 2>&1; then branch=$(git -C \"$cwd\" --no-optional-locks branch --show-current 2>/dev/null || echo \"detached\"); git_info=\" ($branch)\"; else git_info=\"\"; fi; printf \"\\033[1;32m%s@%s\\033[0m:\\033[1;34m%s\\033[0m%s\" \"$user\" \"$host\" \"$dir\" \"$git_info\""
  }
}
```

**Key configuration choices:**

- **Model**: Using Claude Sonnet 4.5
- **Verbose mode**: Enabled for detailed tool execution logging
- **Permissions**: Explicitly allow safe commands (git, grep, find, rg, etc.) and deny WebSearch (use Tavily instead)
- **Status line**: Custom command showing user@host:dir (git-branch) - similar to a traditional shell prompt

---

## Part 5: Practical Multi-MCP Workflows

### Workflow 1: Weekly Notes Creation

**Scenario:** Automatically compile weekly team updates from multiple sources

```
You: "Help me create this week's notes. Check Jira for what I worked on and draft a summary in my WEEKNOTE.md file"

Claude's approach:
1. [Atlassian MCP] Search Jira for issues updated by me this week
2. [Memory MCP] Recall note format preferences
3. [Filesystem MCP] Read existing WEEKNOTE.md to match style
4. [Filesystem MCP] Write draft content
```

### Workflow 2: Cost Optimization Investigation

**Scenario:** Investigate unexpected AWS cost spike and document action items

```
You: "Our AWS costs jumped 30% last week. Investigate and create Jira tickets for the top issues"

Claude's approach:
1. [Vantage MCP] Query cost anomalies for last week
2. [Vantage MCP] Get detailed breakdown by service and resource
3. [Vantage MCP] Retrieve cost optimization recommendations
4. [Memory MCP] Recall team's cost optimization priorities
5. [Atlassian MCP] Create Jira issues for top 3 optimization opportunities
6. [Filesystem MCP] Document findings in local cost-analysis.md
```

### Workflow 3: Documentation Synchronization

**Scenario:** Keep code documentation in sync with Confluence

```
You: "Our authentication code has changed. Update the API documentation in Confluence to match"

Claude's approach:
1. [Filesystem MCP] Read current authentication code
2. [Memory MCP] Recall documentation standards
3. [Atlassian MCP] Find existing API documentation page
4. [Atlassian MCP] Update page with current implementation details
5. [Memory MCP] Record documentation update for future reference
```

---

## Part 6: Tips, Tricks, and Best Practices

### MCP Management

**Don't enable too many MCPs at once:**

- Start with 3-4 MCPs and add more as needed
- Disable unused MCPs to reduce overhead
- Use project-specific configurations for different workflows

**Security considerations:**

- Only give filesystem access to specific directories
- Never commit `.claude.json` with API keys to version control
- Use environment variables for sensitive credentials
- Regularly review MCP permissions

**Permission Management Philosophy:**

Claude Code has a permission system that prompts you to approve tool usage. While this is great for safety, I prefer a more streamlined workflow:

```bash
# My Claude Code function (in ~/.config/zsh/aliases.zsh)
# Uses -c to continue existing conversations, falls back to fresh session if none exists
claude() {
    local err
    err=$(command claude -c --dangerously-skip-permissions "$@" 2>&1)
    if [[ $? -ne 0 && "$err" == *"No conversation found"* ]]; then
        command claude --dangerously-skip-permissions "$@"
    else
        echo "$err"
    fi
}
```

The `--dangerously-skip-permissions` flag bypasses permission prompts, but I still:

- Keep verbose mode enabled to watch what's happening in real-time
- Carefully monitor tool usage through the detailed output
- Maintain a well-defined allowlist in `settings.json` for safe commands
- Stay present during Claude's work rather than walking away

**This approach works for me because:**

- I actively supervise Claude's work
- My permissions allowlist already restricts dangerous commands
- I value workflow speed over confirmation dialogs
- I trust the model with my explicit supervision

**Warning:** This isn't recommended for everyone! Only use `--dangerously-skip-permissions` if you:

- Understand what tools Claude has access to
- Actively monitor Claude's actions
- Have a well-configured permissions allowlist
- Are comfortable with the responsibility

### Performance Optimization

**For large queries:**

```
You: "Use a Task agent to search Confluence for all pages mentioning 'microservices'"
# This prevents the large output from consuming your context window
```

(You can also use this to your own 'CLAUDE|AGENTS.md')

**Memory MCP maintenance:**

- Periodically review and clean up stored entities
- Use specific entity types for better organization
- Delete outdated observations

### Debugging MCP Issues

```bash
# Check MCP server status
claude /mcp

# View verbose logging
claude --verbose

# Test individual MCP
# Memory MCP: Try creating/reading entities
# Filesystem MCP: List files in allowed directory
# Atlassian MCP: Should show authentication status
```

### MCP Inspector: Interactive Server Testing

The [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) is an invaluable tool for exploring and debugging MCP servers before integrating them into Claude Code. It provides an interactive web interface to test tools, resources, and prompts.

**Launching the Inspector:**

```bash
# Test a local MCP server
npx @modelcontextprotocol/inspector node server.js

# Test an npm-based MCP server
npx @modelcontextprotocol/inspector npx @modelcontextprotocol/server-memory

# Test with environment variables
npx @modelcontextprotocol/inspector --env API_KEY=test123 node server.js

# Use CLI mode to test specific tools
npx @modelcontextprotocol/inspector --cli list-tools node server.js
npx @modelcontextprotocol/inspector --cli call-tool tool_name '{"param": "value"}' node server.js
```

**What the Inspector provides:**

- **Interactive Web UI** (default port 6274) for testing MCP servers
- **Tools tab** to explore available tools and test them with different inputs
- **Resources tab** to browse available resources
- **Prompts tab** to test prompt templates
- **Message log** showing all MCP protocol communication
- **Export configurations** for Claude Code, Cursor, or other clients

**Typical workflow:**

1. Launch Inspector with your MCP server
2. Explore available tools and resources in the web UI
3. Test tool calls with sample inputs
4. Review the MCP protocol messages to understand server behavior
5. Export the working configuration to your Claude Code settings

**Documentation:** [modelcontextprotocol.io/docs/tools/inspector](https://modelcontextprotocol.io/docs/tools/inspector)

---

## Part 7: Configuration Management with YADM

### Why YADM?

I use YADM (Yet Another Dotfiles Manager) to version-control my Claude Code configuration alongside my other dotfiles. This provides:

- Git-based versioning of configurations
- Easy synchronization across machines
- Bootstrap scripts for automated setup
- Separation of public and private configs

### My YADM Structure for Claude Code

```
~/.claude/
├── CLAUDE.md              # Tracked: Main configuration docs
├── settings.json          # Tracked: Global settings
├── settings.local.json    # Not tracked: Local overrides
├── .claude.json           # Not tracked: Project MCPs with secrets
└── agents/                # Tracked: Agent configurations
    ├── shared/
    │   ├── professional-context.md
    │   ├── data-analytics.md
    │   └── development-environment.md
    └── ...
```

**Public repository:** [github.com/andrewbolster/dotfiles](https://github.com/andrewbolster/dotfiles)

### Setting Up YADM for Claude Code

```bash
# Install YADM
brew install yadm  # macOS
# or
sudo apt install yadm  # Linux

# Initialize
yadm init

# Add Claude Code configs (without secrets!)
yadm add ~/.claude/CLAUDE.md
yadm add ~/.claude/settings.json

# DO NOT track files with API keys
echo ".claude/.claude.json" >> ~/.yadm/.gitignore
echo ".claude/settings.local.json" >> ~/.yadm/.gitignore

# Commit and push
yadm commit -m "Add Claude Code configuration"
yadm remote add origin git@github.com:yourusername/dotfiles.git
yadm push
```

### Bootstrap Script for New Machines

Create `~/.config/yadm/bootstrap.d/claude.sh`:

```bash
#!/bin/bash
# Claude Code setup bootstrap

echo "Setting up Claude Code configuration..."

# Install Claude Code if not present
if ! command -v claude &> /dev/null; then
    echo "Installing Claude Code..."
    npm install -g @anthropic-ai/claude-code
fi

# Create directories
mkdir -p ~/.claude/agents/shared

echo "Claude Code setup complete!"
echo "Run 'claude' to start, then configure your MCPs in ~/.claude/.claude.json"
```

---

## Part 8: Integrations with Other Tools

One of the major 'superpowers' of Claude (and other assistants) is that they can operate within your own existing environments, so (with your supervision) can run all the same CLIs and commands that you can.

Like all good super-powers, they come with super-responsibilities.

For me, this means 'nudging' Claude to use my `az` or `databricks` or whatever other CLIs I use on a regular basis.

I've spun up entire (temporary) environments and CI pipelines just by telling claude to 'spin up the requisite azure resources to deploy this to a new environment under `<SUBSCRIPTIONNAME>`'

You can take this to an extreme, where, if I have regular 'chains' or 'orchestrations' of other activities (like lots of API calls to update services), I can walk Claude through a particular interaction, and then turn around and say 'make an MCP tool using `fastMCP` and `uv` to replicate the flow we've made'. This way you can build up capabilities as _non-llm_ actions. You can do the same thing with 'use `uv` and `click` to make a command line to do X' and then Claude can reuse that capability (this is how I manage 90% of our internal LLM Gateway requests for new budgets and new models etc.)

## Part 9: Doing actual work

One of my favourite applications of LLM assistants is in iteratively improving the Data Product landscape that we operate in Black Duck. We build Data Products based on source data sets like SQL servers and blob stores, and (after an approval process) we publish the relevant transformations along with ownership and descriptive metadata, which is then made available through our internal MCP.

So, the best way I've found to generate new Data Products based on a 'new' source is to have a 'scratch' repository for each new source, use native `psql` or other tools to have the AI explore the datastore _with_ me, have the assistant _query the existing Data Products_ to understand what the conventions of those products are, have it propose mapping identities and relevant naming conventions etc, and then push those 'new' Data Products to the DataBricks instance using the `databricks` CLI as private data sources / notebooks / [asset bundles](https://docs.databricks.com/aws/en/dev-tools/bundles/), share them among my team and other stakeholders, and get them approved for inclusion in the 'real' pipelines.

## Part 10: Claude as a tool itself

Finally, you can also use `claude` as a tool itself in other tools to prototype new 'fuzzy' workflows (but be careful what environment these are running in...).

I don't do this very often because by the time you actually want to _commit_ something to a CI, I'd like to think we've come up with a better answer than 'let the AI do it'...

**Claude Code + GitHub Actions:**

```yaml
# Example: Use Claude Code in CI for code review
- name: AI Code Review
  run: |
    claude "Review this PR for security issues and code quality" --files $(git diff --name-only origin/main)
```

**Claude Code + Pre-commit Hooks:**

```bash
# .git/hooks/pre-commit
#!/bin/bash
claude "Check these changes for common mistakes" --files $(git diff --cached --name-only)
```

---

## Conclusion

This configuration represents my personal Claude Code setup tailored for development workflows. Key takeaways:

1. **Start simple:** Begin with Memory, Filesystem, and one enterprise MCP
2. **Add incrementally:** Don't enable all MCPs at once - add them as you find use cases
3. **Secure properly:** Never commit secrets, use environment variables
4. **Document everything:** Your future self (and teammates) will thank you
5. **Share knowledge:** Contribute improvements back to community docs

### Next Steps

- **Try it yourself:** Start with Memory MCP combo
- **Experiment:** Find workflows that save you time
- **Share:** Document your own useful MCP combinations
- **Contribute:** Help improve this guide and related documentation

### Questions or Feedback?

- Check my public dotfiles for updates: [github.com/andrewbolster/dotfiles](https://github.com/andrewbolster/dotfiles)
- The [MCP documentation](https://modelcontextprotocol.io/) is an excellent resource

---

*This guide was created with assistance from Claude Code itself, using the very MCPs described herein. Meta!*
