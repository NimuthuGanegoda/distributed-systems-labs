# GitHub Setup Guide

## Current Status

Your repository is already initialized with git and committed. The remote `origin` is already configured.

## Check Your Remote

```bash
git remote -v
```

This will show your GitHub repository URL.

## If You Haven't Created a GitHub Repository Yet

### 1. Create Repository on GitHub

1. Go to [github.com](https://github.com)
2. Click **New** (top left)
3. Repository name: `distributed-systems-labs`
4. Description: "Distributed systems assignments, labs, and projects"
5. Choose **Public** or **Private**
6. Do **NOT** initialize with README (we already have one)
7. Click **Create repository**

### 2. Add GitHub as Remote

After creating the repo, GitHub will show commands. Run:

```bash
git remote add origin https://github.com/YOUR-USERNAME/distributed-systems-labs.git
git branch -M main
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username.

## Working with the Repository

### After Initial Setup

You only need to push/pull:

```bash
# Push your local commits to GitHub
git push

# Pull updates from GitHub
git pull

# Push specific branch
git push origin branch-name
```

### Daily Workflow

1. Make changes to your code
2. Stage changes: `git add .`
3. Commit: `git commit -m "Your message"`
4. Push to GitHub: `git push`

### Pulling Latest Changes

If you make changes on GitHub (web interface):
```bash
git pull origin main
```

## Configure Git (If Not Done)

```bash
# Set your identity globally (one-time)
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"

# Verify
git config --global user.name
git config --global user.email
```

## SSH vs HTTPS

### HTTPS (Recommended for beginners)
- Simpler setup
- Uses username/password or personal access token
- Command: `https://github.com/USERNAME/distributed-systems-labs.git`

### SSH (More secure)
- Requires SSH key setup
- No password needed after setup
- Command: `git@github.com:USERNAME/distributed-systems-labs.git`

[SSH Setup Guide](https://docs.github.com/en/authentication/connecting-to-github-with-ssh)

## Common Commands

```bash
# Check status
git status

# View commit history
git log --oneline

# View changes
git diff

# Create new branch
git checkout -b feature-name

# Switch branch
git checkout branch-name

# Merge branch
git merge branch-name

# Push new branch
git push -u origin feature-name

# Delete branch
git branch -d branch-name
```

## Important Files

- `.gitignore` - Files to exclude from version control (Python cache, etc.)
- `README.md` - Main repository documentation
- `CONTRIBUTING.md` - Guidelines for organizing new work

## Backup & Sync

Your code is now:
- ✅ Tracked locally with git
- ✅ Connected to GitHub
- ✅ Backed up in the cloud

Always push regularly:
```bash
git push
```

---

**Note**: Once set up, you can work locally and sync with GitHub anytime without cloning again. Your `e:\distributed-systems-labs` folder is your working directory.
