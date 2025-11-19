#!/usr/bin/env python3
"""
Sim Racing Tip Miner
Version: 1.0.0 (November 18, 2025)
Author:  Your Name / thesimracingstewards.com
License: MIT License

Description:
    Daily agent that scans r/simracing + r/simracingstewards for the newest incident
    discussions and uses xAI's Grok-3 to extract 4–8 fresh, actionable prevention tips.
    Tips are saved in the exact format required by thesimracingstewards.com:
        "Tip text here | category | (Reddit)"

    These tips are the "live brain" that makes your website feel current and
    hyper-relevant — no other steward tool in the world updates itself every day.

Credits:
    • Powered by Grok-3 from xAI[](https://x.ai/api)
    • Community wisdom from r/simracing and r/simracingstewards
    • Built for thesimracingstewards.com — the only steward tool that learns daily
"""

import requests
from datetime import datetime
import requests
import sys
import os

# ===================================================================
# CONFIGURATION — EDIT ONLY THESE LINES
# ===================================================================
GROK_KEY = "axi-your-real-key-here"          # ←←←←← REPLACE WITH YOUR REAL KEY
SUBREDDITS = "simracing+simracingstewards"   # Add more with + if desired
# ===================================================================

def print_banner():
    print("\n" + "="*80)
    print("    SIM RACING TIP MINER — v1.0.0")
    print("    thesimracingstewards.com live knowledge agent")
    print(f"    {datetime.now():%Y-%m-%d %H:%M:%S}")
    print("="*80 + "\n")

def get_reddit_text():
    url = f"https://www.reddit.com/r/{SUBREDDITS}/new.json"
    params = {
        "limit": 50,
        "t": "day"          # last 24 hours only
    }
    headers = {
        "User-Agent": "tip-miner-linux/1.0.0 (by u/yourusername; thesimracingstewards.com)"
    }
    
    print("Fetching newest posts from r/simracing + r/simracingstewards...")
    try:
        r = requests.get(url, params=params, headers=headers, timeout=20)
        r.raise_for_status()
        posts = r.json()["data"]["children"]
        if not posts:
            return "No posts in the last 24 hours."
        
        text_parts = []
        for p in posts:
            data = p["data"]
            text_parts.append(data["title"])
            if data.get("selftext"):
                text_parts.append(data["selftext"])
        return "\n\n---\n\n".join(text_parts)
    
    except Exception as e:
        print(f"Reddit fetch error: {e}")
        return "Reddit temporarily unavailable — using fallback mode."

def get_grok_tips(text):
    url = "https://api.x.ai/v1/chat/completions"
    payload = {
        "model": "grok-3",
        "messages": [{
            "role": "user",
            "content": f"""Extract 4–8 NEW actionable sim-racing prevention tips from the Reddit posts below.

Rules:
- One tip per line
- Exact format: Tip text | category | (Reddit)
- Allowed categories only: braking, overtaking, defense, rejoin, vision, netcode, mental, general
- Do NOT invent anything — only use content actually present in the posts

Posts:
{text}"""
        }],
        "temperature": 0.35,
        "max_tokens": 900
    }
    headers = {
        "Authorization": f"Bearer {GROK_KEY}",
        "Content-Type": "application/json"
    }
    
    print("Sending posts to Grok-3 for tip extraction...")
    try:
        r = requests.post(url, json=payload, headers=headers, timeout=40)
        if r.status_code == 200:
            return r.json()["choices"][0]["message"]["content"].strip()
        else:
            return f"Grok error {r.status_code}: {r.text[:300]}"
    except Exception as e:
        return f"Grok connection failed: {e}"

def save_tips(tips):
    filename = "tips2.txt"
    with open(filename, "a", encoding="utf-8") as f:  # append mode
        f.write(f"\n# Tip Miner run — {datetime.now():%Y-%m-%d %H:%M}\n")
        f.write(tips.strip() + "\n")
    print(f"\nTips successfully appended to → {os.path.abspath(filename)}")

# ===================== MAIN =====================
if __name__ == "__main__":
    if GROK_KEY == "axi-your-real-key-here":
        print("ERROR: You forgot to add your real Grok API key!")
        print("Edit the script and replace line with your axi- key.")
        sys.exit(1)

    print_banner()

    reddit_text = get_reddit_text()
    tips = get_grok_tips(reddit_text)

    print("\n" + "═"*80)
    print("FRESH TIPS")
    print("═"*80)
    print(tips)
    print("═"*80)

    save_tips(tips)

    print("\nDone! Copy the new lines from tips2.txt into your website.")
    input("\nPress Enter to exit...")
