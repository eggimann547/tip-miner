# tip-miner
Python script for grabbing tips for better racing


Sim Racing Tip Miner User Guide
Version: 1.0.0
Date: November 18, 2025
Overview
The Tip Miner is a simple Python script that automatically scans r/simracing and r/simracingstewards for recent incident discussions and uses Grok-3 to extract actionable prevention tips. These tips are formatted for direct addition to your tips2.txt knowledge base, making your thesimracingstewards.com tool smarter every day.
What it does in 20 seconds:

Fetches the latest 40 posts from the subreddits (past 24 hours)
Sends the text to Grok-3
Extracts 4–8 new tips in format: Tip text | category | (Reddit)
Saves them to tips2.txt in the same folder

Why it's valuable: Your website's fault % comes from historical data (28K CSV). These tips add fresh, community-sourced wisdom that matches modern incidents, turning verdicts into personalized coaching.
Requirements

OS: Linux (Ubuntu/Debian/Mint/Pop!_OS recommended)
Python: 3.8+ (usually pre-installed)
Internet: For Reddit and Grok API calls
xAI API Key: Free axi- key from x.ai/api (up to 10K tokens/day free until Dec 15, 2025)

Installation (5 Minutes)
Open a terminal and run these commands one by one:
Bash# 1. Update your system
sudo apt update

# 2. Install Python and pip (if not already there)
sudo apt install -y python3 python3-pip python3-venv

# 3. Create project folder
mkdir ~/tip-miner && cd ~/tip-miner

# 4. Create a virtual environment (keeps everything clean)
python3 -m venv venv

# 5. Activate the virtual environment
source venv/bin/activate

# 6. Install the two packages we need
pip install requests
That's it. You're ready.
Setup (One-Time – 1 Minute)

Download or copy the script below into ~/tip-miner/tip_miner.py
Open the file: nano tip_miner.py (or use any editor like VS Code)
Find line 8: GROK_KEY = "axi-your-real-key-here"
Replace with your real key: GROK_KEY = "axi-XXXXXXXXXXXXXXXXXXXXXXXXXXXX"
Save and exit (Ctrl+O → Enter → Ctrl+X in nano)

Running the Script (20 Seconds)
In the terminal (make sure you're in ~/tip_miner and venv is activated):
Bashsource venv/bin/activate  # if not already active
python tip_miner.py
What happens:

Fetches fresh posts from r/simracing and r/simracingstewards (last 24 hours)
Sends the text to Grok-3
Extracts 4–8 new tips
Saves them to tips2.txt in the same folder
Prints them in the terminal for review

Sample Output:
textSim Racing Tip Miner — 2025-11-18 14:30

Fetching latest incidents from Reddit...
Asking grok-3 for fresh tips...

==================================================================
FRESH TIPS
==================================================================
Brake 10m earlier when no overlap by apex | braking | (Reddit)
Only one defensive move per straight — no weaving | defense | (Reddit)
Wait for 2-second gap before rejoining | rejoin | (Reddit)
Mirror check every straight to avoid punts | vision | (Reddit)

==================================================================
TIPS AUTOMATICALLY SAVED → tips2.txt (same folder)
==================================================================
Press Enter to exit...
Copying Tips to Your Website

Open tips2.txt in the terminal: cat tips2.txt
Copy the new lines (everything after the # line)
Paste them into your website's public/tips2.txt (via GitHub web editor or FTP)
Commit/push → your website instantly gets smarter (no redeploy needed)

Troubleshooting


ProblemCauseFix"pip: command not found"pip not installedRun sudo apt install python3-pip"venv: command not found"venv not installedRun sudo apt install python3-venv"Grok error 401"Bad API keyDouble-check your axi- key at x.ai/api"Grok error 429"Rate limitWait 1 minute, run again (free tier: 60/min)"Reddit fetch failed"Network issueCheck internet; try again in 5 mins"No tips found"Quiet subredditNormal—run every 24 hours for fresh ones
Advanced Usage

Run automatically daily: Edit crontab (crontab -e) → add:text0 9 * * * cd /home/yourusername/tip_miner && source venv/bin/activate && ./tip_miner.py(Runs at 9 AM every day)
Scan more subreddits: Change line 10 to SUBREDDITS = "simracing+simracingstewards+iracing" (adds r/iracing)
Custom search terms: Line 15 — change the query for different incident types (e.g., "braking OR trailbrake")

License & Credits

This script is free for personal use (MIT license).
Credits: Powered by Grok-3 from xAI and community posts from r/simracingstewards.
Always credit the community in your tool (e.g., "Tips from r/simracingstewards").

Happy mining! Run ./tip_miner.py any time you want fresh wisdom for your stewards tool.
