from github import Github
import os

USERNAME ="Alaire1"
SVG_FILE = "coding_stats.svg"

token = os.getenv("GH_STATS_TOKEN")
if not token:
    raise Exception("GH_STATS_TOKEN not found. Set the token in Developer Settings")

github_var= Github(token)
user = github_var.get_user(USERNAME)
repos = user.get_repos()


total_lines = 0
projects = 0
total_commits = 0


for repo in repos:
    if repo.fork:
        continue
    projects += 1
    languages = repo.get_languages()
    total_lines += sum(languages.values())
    
    try:
        total_commits += repo.get_commits(author=user).totalCount
    except Exception as e:
        if "Git Repository is empty" in str(e):
            continue 
        else:
            raise Exception("Something went wrong")


svg_content = f"""
<svg width="400" height="150" xmlns="http://www.w3.org/2000/svg">
    <style>
        .title {{ font: bold 18px sans-serif; fill: #ff79c6; }}
        .label {{ font: 14px sans-serif; fill: #f8f8f2; }}
        .value {{ font: bold 16px sans-serif; fill: #50fa7b; }}
        rect {{ fill: #282a36; rx: 10; ry: 10; }}
    </style>
    <rect x="0" y="0" width="400" height="150"/>
    <text x="20" y="30" class="title">My Coding Stats</text>
    <text x="20" y="70" class="label">Lines of Code:</text>
    <text x="200" y="70" class="value">{total_lines}</text>


  <text x="20" y="100" class="label">Projects Completed:</text>
  <text x="200" y="100" class="value">{projects}</text>
  
  <text x="20" y="130" class="label">Commits:</text>
  <text x="200" y="130" class="value">{total_commits}</text>
</svg>
"""

with open(SVG_FILE, "w") as f:
    f.write(svg_content)

print(f"SVG generated: {SVG_FILE}")
