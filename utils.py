"""!
APOD: Agent Panel On-Demand - Utility Functions

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
import configparser

def load_personas(path):
    config = configparser.ConfigParser()
    try:
        with open(path, 'r', encoding='utf-8') as f:
            config.read_file(f)
        
        personas = {}
        for section in config.sections():
            personas[section] = config[section]['prompt']
        return personas
    except FileNotFoundError:
        print(f"Error: Could not find {path}")
        return {}
    except Exception as e:
        print(f"Error loading personas: {e}")
        return {}

def select_agents(personas):
    print("\nAvailable agents:")
    for idx, name in enumerate(personas.keys(), 1):
        print(f"{idx}. {name}")
    
    indices = input("Select agents by number (comma-separated): ")
    try:
        selected = [list(personas.keys())[int(i.strip()) - 1] for i in indices.split(",")]
        return selected
    except (ValueError, IndexError) as e:
        print(f"Error selecting agents: {e}")
        print("Please enter valid numbers separated by commas (e.g., 1,2,3)")
        return select_agents(personas)  # Retry selection

def moderator_prompt(previous_dialogue):
    return f"""
You are the moderator of this APOD session. Reflect on the last few turns and guide the agents toward synthesis or deeper insight.

Recent dialogue:
{previous_dialogue}
"""