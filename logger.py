"""!
APOD: Agent Panel On-Demand - Logger System

Date created: 24th September 2025

License: GNU General Public License version 3 for academic or 
not-for-profit use only

SiPy package is free software: you can redistribute it and/or 
modify it under the terms of the GNU General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
from datetime import datetime

def start_log(topic, participants, moderator_after, log_file=None):
    log = {
        "topic": topic,
        "participants": participants,
        "moderator_after": moderator_after,
        "turns": [],
        "file": log_file
    }
    return log

def log_turn(log, speaker, message, tags):
    if not log.get("file"):
        return
        
    with open(log["file"], "a", encoding="utf-8") as f:
        f.write(f"### 🧠 {speaker}\n")
        f.write(f"> {message}\n\n")
        if tags:
            f.write(f"**Tags**: {tags}\n")
        f.write("\n---\n")
    
    # Store in memory too
    log["turns"].append({
        "speaker": speaker,
        "message": message,
        "tags": tags
    })

def log_summary(log, topic, agents):
    if not log.get("file"):
        return
        
    with open(log["file"], "a", encoding="utf-8") as f:
        f.write("## 🧩 Summary\n")
        f.write(f"- Topic explored: {topic}\n")
        f.write(f"- Agents involved: {', '.join(agents)}\n")
        f.write("- This log may be used to refine agent prompts and improve future simulations.\n")
