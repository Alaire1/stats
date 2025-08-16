# GitHub Coding Stats Generator

This project automatically generates a **live coding stats card** (SVG file) that you can embed directly in your GitHub profile README.  
It shows your total commits, projects, and lines of code — updated **daily** using GitHub Actions. 

---

##  Features
- ✅ Fetches data from the GitHub API
- ✅ Counts commits, repositories, and lines of code
- ✅ Automatically generates an SVG stats card
- ✅ Updates daily via GitHub Actions
- ✅ Can be embedded anywhere (README, websites, etc.)

---

##  How It Works
1. A GitHub Action runs every day at midnight UTC.
2. It executes `generate_stats_svg.py`:
   - Fetches data about your repos and contributions
   - Generates a new `coding_stats.svg` file
3. The action commits the updated SVG back into the repo.

---


