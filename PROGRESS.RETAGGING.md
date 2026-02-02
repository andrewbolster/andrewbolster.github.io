# Tag Consolidation Progress

## Summary

| Metric | Value |
|--------|-------|
| Starting tags | 1751 |
| Target tags | <150 |
| Final tags | **195** (89% reduction) |
| Tags with 3+ uses | 141 |
| Status | **Migration Complete** |

---

## Finalized Tag Mappings

### Tags to DELETE (no replacement)

```
# Years (round to decade - keep 1960s, delete specific years)
1963 → DELETE (post already has 1960s)
2009 → DELETE
2010 → DELETE
(etc - all specific years)

# Version numbers
10.04 → Ubuntu
8.04 → Ubuntu
8.10 → Ubuntu
64-bit → DELETE

# Meaningless/too generic (DELETE)
a, see, doing, general, info, value, warn, fun, funny,
experience, explore, new-content, uncategorized, index.html,
obsoletet, assessment_test, job_application, click (generic),
update, system

# Typos (MERGE to correct spelling)
hackersapce → Hackerspace
progamming → Programming
```

### Tags to KEEP (user requested)
- `personal` ✓
- `project` ✓
- `event` ✓
- `data_management` → `Data Management` ✓
- `click` (NS-3 router) → `Click Router` ✓

---

## AI & Machine Learning

```
ai, ai-bubble, ai-ethics, ai-hype, ai-winter, aiops,
artificial-intelligence, bias-in-ai, ethical-ai,
generative-ai, robopsychologist → AI

machine-learning, ml, mlops, fine-tuning, gans, rlhf → Machine Learning

chatgpt, claude, claude-code, deepseek, github-copilot,
large-language-model, llm, llms, mcp, model-context-protocol,
openai, rag → LLM

data-science, data-scientists → Data Science
natural-language-processing → NLP
```

---

## Cybersecurity (with sub-categories + parent tag)

All get `Cybersecurity` as additional parent tag:

```
# Application Security (+ Cybersecurity)
application-security-posture-management, vulnerability,
sql-injection, exploit → Application Security

# Data Security (+ Cybersecurity)
data-breach, data-breaches, data-protection,
passwords, password-security → Data Security

# Network Security (+ Cybersecurity)
firewall, network-security, authentication → Network Security

# Cryptography (+ Cybersecurity)
encryption, tls, traffic-encryption → Cryptography

# Privacy (+ Cybersecurity)
anonymity, digital-rights, internet-freedom, internet-privacy,
net-neutrality, surveillance → Privacy

# Hacking (+ Cybersecurity)
aircrack, backtrack-4, backtrack-linux, hacker, hackers,
nmap, password-cracking, phishing, social-engineering,
wireshark → Hacking

# Generic → just Cybersecurity
cyber-security, information-security, security → Cybersecurity
```

---

## Programming Languages

```
python, python3, python-3, oo-python → Python
javascript, js, node, nodejs → JavaScript
c, c++, cpp → C/C++
csharp → CSharp
java → Java
scala → Scala
groovy → Groovy
ruby → Ruby
perl, perl-scripting → Perl
bash, bash-scripting → Bash
shell, shell-script, shell-scripting → Shell
html → HTML
css → CSS
php → PHP
r-programming → R
matlab, octave → MATLAB
sql → SQL
```

---

## Operating Systems

```
# Ubuntu
ubuntu, ubuntu-9.10, ubuntu-10.04, ubuntu-hardy-heron,
ubuntu-linux, ubuntu-server, lucid, lucid-lynx,
hardy-heron, jaunty, 10.04, 8.04, 8.10 → Ubuntu

# Linux distros (kept separate)
linux, linux-distros, linux-servers → Linux
debian → Debian
fedora → Fedora
mint, linux-mint → Linux Mint

# Windows
windows, windows-7, windows-vista, vista, winxp → Windows

# Android
android, android-api, android-development,
android-market, cyanogenmod → Android

# Desktop environments
gnome, gnome-shell, gnome-do → Gnome
kde → KDE
```

---

## Community & Location

```
# Farset Labs
farset, farset-labs, farsetlabs → Farset Labs

# Hackerspace
hackerspace, hackerspaces, hackersapce → Hackerspace

# Locations (kept separate)
belfast → Belfast
dublin → Dublin
liverpool → Liverpool
northern-ireland, ni, ulster → Northern Ireland
ireland → Ireland
uk → UK

# Universities
qub, queens-university-belfast, university-belfast → QUB
ecit → ECIT (kept separate)
university-of-liverpool → University of Liverpool
```

---

## Academic & Research

```
# Academia
academic, academic-conferences, academic-references,
academic-videos, college, university → Academia

# PhD
phd, phd-research, thesis, thesis-writing,
dissertation, viva → PhD

# Research
research, research-methodologies, lit-review,
literature-review → Research

# Trust (kept separate - PhD topic)
trust, trust-management-frameworks,
multi-vector-trust-management → Trust

# Robotics
robotics, robots, rov → Robotics

# Autonomous Systems
autonomous-systems, autonomous-vehicles, autonomy,
collaborative-autonomy, unmanned-systems → Autonomous Systems

# AUV/Maritime (DUPLICATE to all three)
auv, auvs, maritime-autonomy → Autonomous Systems + Maritime + Robotics
```

---

## Media & Entertainment

```
# Film
film, movie-trailer, animation, trailer → Film
star-wars → Star Wars (kept separate)

# TV
tv, iptv → TV
doctor-who → Doctor Who (kept separate)

# Music
music, music-video, musicians, live-performance, remix → Music

# Gaming
video-games, videogames, video-game, games, gaming,
steam, xbox, portal → Gaming

# Books
book, books, kindle, ebook-reader → Books
science-fiction → Science Fiction (kept separate)

# Podcasts
podcast, podcasts → Podcasts

# Social Media
facebook, twitter, linkedin, youtube, reddit → Social Media
```

---

## Hardware & Networking

```
# Computers
laptop, laptops, thinkpad-x61s → Laptop
desktop, pc → Desktop
server → Server

# Single-board (DUPLICATE + Microcontrollers)
raspberry-pi → Raspberry Pi + Microcontrollers
arduino → Arduino + Microcontrollers

# GPU (kept separate)
gpu, graphics-card → GPU
nvidia → NVIDIA
cuda → CUDA (when specifically discussed)

# CPU
intel → Intel
amd → AMD

# Networking
router, dd-wrt, wrt54g, wrt54gl, linksys → Router
wifi, wi-fi, wireless → WiFi

# Storage
usb → USB
ssd, hdd, nas → Storage

# Mobile networks
3g, 4g, lte → Mobile Network
```

---

## Politics & Society

```
democracy, elections, ni-assembly, dup → Politics
banking, economy, economic-development, taxation,
investment, algorithmic-trading → Finance
covid, pandemic, lockdown → Health
global-warming, climate → Environment
```

---

## Cloud & DevOps (with parent tags)

```
# Cloud providers (+ Cloud)
aws → AWS + Cloud
azure → Azure + Cloud
google-cloud, gcp → Google Cloud + Cloud
rackspace, dreamhost → Cloud

# DevOps tools (+ DevOps)
docker → Docker + DevOps
kubernetes, k8s → Kubernetes + DevOps
terraform → Terraform + DevOps
ansible → Ansible + DevOps
jenkins → Jenkins + DevOps

# Version control (NO DevOps parent)
git → Git
github, github-migration → GitHub
bitbucket → Bitbucket
mercurial, subversion → Version Control
```

---

## Data Science & Analytics

```
data-science, data-scientists → Data Science
pandas → Pandas
numpy → NumPy
scipy → SciPy
jupyter, jupyter-notebooks, jupyterlab, ipython,
ipython-notebook → Jupyter
matplotlib → Matplotlib
seaborn → Seaborn
plotly, plotly-express → Plotly
anaconda, conda → Anaconda
statistics, statistical-analysis → Statistics

# Databases
mysql, postgresql, sqlite → SQL
mongodb, redis → NoSQL
database, databases → Database
```

---

## Web & APIs

```
html, css → Web Development
wordpress, wordpress-plugins, wordpress-security → WordPress
drupal, drupal-6 → Drupal
jekyll → Jekyll
jquery → jQuery

api, rest, restful → API
graphql → GraphQL
json → JSON
xml → XML

apache → Apache
nginx → Nginx
```

---

## Education & STEM

```
# Education
education, e-learning, elearning, learning,
learning-resources, programming-education, teaching,
google-courses, google-code-university → Education

# CoderDojo (kept separate)
community-education, code-club, coder-dojo → CoderDojo

# STEM
stem, stem-education, stem-outreach-activities,
stem-subjects → STEM

# Conferences (kept separate)
conference, conferences → Conferences
nidc → NIDC
tedx, tedxbelfast → TEDx
pycon, pyconie → PyCon
bsides → BSides

# Speaking/Meetups
speaking, speaker, talks → Speaking
meetup, meetups → Meetups
```

---

## Open Source & Maker

```
open-source, opensource, foss, floss → Open Source
open-data → Open Data (kept separate)
creative-commons → Creative Commons

maker, makers, making → Maker
3d-printing, 3d-printer → 3D Printing (kept separate)
diy → DIY (kept separate)
electronics, soldering → Electronics
```

---

## Misc Tech

```
# IoT
iot, internet-of-things → IoT
smart-home, home-automation → Smart Home (kept separate)

# VR/AR
vr, virtual-reality, ar, augmented-reality → VR/AR

# Blockchain
blockchain → Blockchain
cryptocurrency, bitcoin, ethereum → Cryptocurrency

# GPS
gps, gps-iii → GPS
navigation, geolocation → Navigation

# Simulation
simulation, simulator, ns-3 → Simulation
```

---

## Personal & Lifestyle

```
# Content types
tutorial, how-to, guide → Tutorial
review, reviews → Review
opinion, commentary → Opinion
rant → Rant + Opinion (duplicated)

# Personal
travel → Travel
food, cooking, recipe → Food
whiskey, whisky, coffee, beer → Drinks

# Productivity
productivity, workflow → Productivity
automation → Automation
```

---

## Estimated Final Tag List (~130 tags)

### Technology (~45)
AI, Machine Learning, LLM, Data Science, NLP, Cybersecurity, Application Security, Data Security, Network Security, Cryptography, Privacy, Hacking, Python, JavaScript, C/C++, CSharp, Java, Bash, Shell, HTML, CSS, SQL, Ubuntu, Linux, Debian, Fedora, Linux Mint, Windows, Android, Gnome, KDE, Git, GitHub, Version Control, Docker, Kubernetes, DevOps, Cloud, AWS, Azure, Google Cloud, IoT, Smart Home, VR/AR, Blockchain, Cryptocurrency

### Data & Analytics (~15)
Pandas, NumPy, SciPy, Jupyter, Matplotlib, Seaborn, Plotly, Anaconda, Statistics, Database, NoSQL, Visualization, Data Management

### Hardware (~20)
Laptop, Desktop, Server, Raspberry Pi, Arduino, Microcontrollers, GPU, NVIDIA, CUDA, Intel, AMD, Router, WiFi, USB, Storage, Mobile Network

### Research & Academia (~15)
Academia, PhD, Research, Trust, Robotics, Autonomous Systems, Maritime, Simulation, ECIT, QUB, University of Liverpool

### Community & Events (~20)
Farset Labs, Hackerspace, Belfast, Dublin, Liverpool, Northern Ireland, Ireland, UK, Conferences, NIDC, TEDx, PyCon, BSides, Speaking, Meetups, Education, CoderDojo, STEM

### Media & Entertainment (~15)
Film, Star Wars, TV, Doctor Who, Music, Gaming, Books, Science Fiction, Podcasts, Social Media

### Web & Tools (~15)
Web Development, WordPress, Drupal, Jekyll, API, JSON, XML, Apache, Nginx, Open Source, Open Data, Maker, 3D Printing, DIY, Electronics

### Personal & Other (~15)
Tutorial, Review, Opinion, Rant, Travel, Food, Drinks, Productivity, Automation, Politics, Finance, Health, Environment, GPS, Navigation, Click Router

---

## Migration Complete

1. ✅ Review complete - mappings finalized
2. ✅ Generate Python migration script (`scripts/migrate_tags.py`)
3. ✅ Run migration on all posts (multiple passes)
4. ✅ Rebuild site and verify tag count
5. ✅ Final cleanup and commit

### Final Results

- **Starting tags**: 1751
- **Final tags**: 195 (89% reduction)
- **Tags with 3+ uses**: 141 (core taxonomy)
- **Key consolidations**:
  - AI: 19 posts
  - Cybersecurity: 33 posts (with sub-categories)
  - Ubuntu: 43 posts
  - Python: 19 posts
  - Linux: 53 posts
  - Technology: 42 posts

### Migration Features

The migration script (`scripts/migrate_tags.py`) includes:
- Simple 1:1 tag mappings (e.g., `python3` → `Python`)
- Multi-mappings for parent tags (e.g., `docker` → `Docker` + `DevOps`)
- Frequency threshold filtering (tags used < 3 times removed)
- Long tag cleanup (removes tags > 50 chars or containing URLs)
- Case normalization (e.g., `technology` → `Technology`)

---

## Processing Log

### 2026-02-02: Initial Analysis
- Analyzed 1751 tags using subagents
- Created initial mapping proposals

### 2026-02-02: Interactive Review Complete
- Reviewed 16 batches with user
- Key decisions:
  - Keep detailed cybersecurity sub-categories with parent tag
  - Keep cloud/devops tools with parent tags
  - Keep specific conference names (NIDC, TEDx, BSides, PyCon)
  - Duplicate AUV tags to Autonomous Systems + Maritime + Robotics
  - Duplicate Raspberry Pi/Arduino to include Microcontrollers
  - Keep drinks separate initially, then merged to Drinks
  - Rant gets both Rant + Opinion tags
