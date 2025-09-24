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

def start_log(topic, agents, moderator_after):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    filename = f"apod_log_{timestamp.replace(' ', '_').replace(':', '-')}.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(f"# APOD Session Log\n\n")
        f.write(f"**Topic**: {topic}\n")
        f.write(f"**Agents**: {', '.join(agents)}\n")
        f.write(f"**Moderator**: {'User joins after turn ' + str(moderator_after) if moderator_after else 'None'}\n")
        f.write(f"**Timestamp**: {timestamp}\n\n---\n")
    return filename

def log_turn(filename, speaker, message, tags):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"### 🧠 {speaker}\n")
        f.write(f"> {message}\n\n")
        if tags:
            f.write(f"**Tags**: {tags}\n")
        f.write("\n---\n")

def log_summary(filename, topic, agents):
    with open(filename, "a", encoding="utf-8") as f:
        f.write("## 🧩 Summary\n")
        f.write(f"- Topic explored: {topic}\n")
        f.write(f"- Agents involved: {', '.join(agents)}\n")
        f.write("- This log may be used to refine agent prompts and improve future simulations.\n")
        