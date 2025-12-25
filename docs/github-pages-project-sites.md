# GitHub Pages Setup for Project Sites

This document explains how to configure GitHub project repositories to work as subdirectories under `andrewbolster.info`.

## The Problem

GitHub Pages can host project sites at `username.github.io/repo-name/`, but routing them through a custom domain like `andrewbolster.info/repo-name/` requires specific configuration.

### Common Issues

1. **Jekyll Processing**: By default, GitHub Pages processes repos with Jekyll, which can fail if no Jekyll config exists
2. **Stuck Builds**: Broken builds get stuck in "building" status indefinitely
3. **Missing Landing Page**: Without an `index.html`, visitors get a 404 even if the build succeeds
4. **CNAME Conflicts**: Project repos should NOT have their own CNAME file (only the main user site should)

## The Solution

### Minimum Required Files

1. **`.nojekyll`** - Empty file that tells GitHub Pages to skip Jekyll processing
2. **`index.html`** - Landing page for the project site

### Step-by-Step Setup

#### 1. Disable Jekyll Processing

```bash
cd ~/src/your-repo
touch .nojekyll
```

This tells GitHub Pages to serve your files as-is without trying to build them with Jekyll.

#### 2. Create a Landing Page

Create an `index.html` at the repository root. This can be:
- A simple directory listing (like this repo)
- A redirect to your main content
- A full landing page

See `index.html` in this repo for a complete example.

#### 3. Verify No CNAME File

```bash
# Should NOT exist in project repos
ls CNAME  # Should return "No such file or directory"
```

Only the main user site (`andrewbolster.github.io`) should have a CNAME file.

#### 4. Configure GitHub Pages Settings

Via GitHub API or web UI:
- **Source**: Deploy from `master` branch, root directory (or `gh-pages` branch)
- **Custom Domain**: Should be blank (inherited from main user site)

```bash
# Check current Pages config
gh api repos/andrewbolster/YOUR_REPO/pages --jq '{html_url, custom_domain, source}'
```

#### 5. Commit and Push

```bash
git add .nojekyll index.html
git commit -m "Configure GitHub Pages for custom domain routing"
git push
```

#### 6. Monitor Build Status

```bash
# Check build status
gh api repos/andrewbolster/YOUR_REPO/pages/builds/latest --jq '{status, created_at}'

# Wait for "built" status (not "building")
```

### Verification

After the build completes (usually 1-2 minutes):

1. Test the github.io URL:
   ```
   https://andrewbolster.github.io/YOUR_REPO/
   ```

2. Verify redirect to custom domain:
   ```bash
   curl -I https://andrewbolster.github.io/YOUR_REPO/
   # Should show 301 redirect to andrewbolster.info/YOUR_REPO/
   ```

3. Test the custom domain:
   ```
   https://andrewbolster.info/YOUR_REPO/
   ```

## Technical Details

### How Custom Domain Routing Works

1. Main user site (`andrewbolster.github.io`) has CNAME file with `andrewbolster.info`
2. GitHub automatically redirects `username.github.io/repo/*` → `custom-domain.com/repo/*`
3. Project sites inherit the custom domain from the user site
4. Each project becomes a subdirectory under the custom domain

### Why `.nojekyll` Matters

- GitHub Pages defaults to Jekyll processing for all repos
- Jekyll ignores files/folders starting with `_` or `.` (except `.nojekyll`)
- Jekyll requires specific directory structure and config
- For static HTML or non-Jekyll sites, `.nojekyll` bypasses this completely
- Fixes "stuck building" issues when no Jekyll config exists

### Build Pipeline

Without `.nojekyll`:
```
Push → Jekyll Build (fails if no config) → Stuck "building" → 404
```

With `.nojekyll`:
```
Push → Copy files as-is → Deploy → Success
```

## Templates

### Minimal index.html

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Project Name</title>
</head>
<body>
    <h1>Project Name</h1>
    <ul>
        <li><a href="presentation/">Presentation</a></li>
        <li><a href="docs/">Documentation</a></li>
    </ul>
</body>
</html>
```

### Redirect index.html

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="refresh" content="0; url=./main.html">
    <title>Redirecting...</title>
</head>
<body>
    <p>Redirecting to <a href="./main.html">main content</a>...</p>
</body>
</html>
```

## Troubleshooting

### Site Still Returns 404

1. Check build status: `gh api repos/andrewbolster/REPO/pages/builds/latest`
2. Verify `.nojekyll` exists: `ls -la | grep nojekyll`
3. Verify `index.html` exists at root
4. Wait for build to complete (check status every 30 seconds)
5. Clear browser cache or test in incognito mode

### Build Stuck in "building"

This usually indicates the old issue this fix addresses. The new commit with `.nojekyll` should trigger a fresh build that completes successfully.

### Links Don't Work

- Use relative paths: `./subdir/file.html` not `/subdir/file.html`
- Absolute paths should include base: `/repo-name/subdir/file.html`
- Or use the `<base>` tag: `<base href="/repo-name/">`

## Example Repositories

- `nb_presentations` - Directory listing style (this repo)
- Future: `presentations` - Slidev-based presentations

## References

- [GitHub Pages Documentation](https://docs.github.com/en/pages)
- [Custom Domain Configuration](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)
- [Bypassing Jekyll](https://github.blog/2009-12-29-bypassing-jekyll-on-github-pages/)

---

**Last Updated**: 2025-12-25
**Status**: Active configuration for andrewbolster.info project sites
