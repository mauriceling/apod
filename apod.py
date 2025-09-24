"""!
APOD: Agent Panel On-Demand

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
from simulator import run_simulation
from utils import load_personas, select_agents
import os

def main():
    print("🧠 Welcome to APOD: Agent Panel On Demand")

    # Get OpenRouter API key
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        # Try to read from api key file
        api_key_path = os.path.join(os.path.dirname(__file__), "openrouter.api_key")
        try:
            with open(api_key_path, 'r') as f:
                api_key = f.read().strip()
                print("✓ API key loaded from file")
        except FileNotFoundError:
            api_key = input("Please enter your OpenRouter API key: ").strip()
            if not api_key:
                print("Error: OpenRouter API key is required")
                return
            # Optionally save the key for future use
            save = input("Save API key for future use? (y/n): ").lower()
            if save == 'y':
                with open(api_key_path, 'w') as f:
                    f.write(api_key)
                print("✓ API key saved to file")
        
        os.environ["OPENROUTER_API_KEY"] = api_key

    # Load personas
    personas = load_personas("persona.ini")
    
    if not personas:
        print("Error: No personas loaded!")
        return

    # Interactive setup
    topic = input("Enter the topic of discussion: ").strip()
    
    # Get agent selection
    agent_names = select_agents(personas)
    turns = int(input("How many turns should the panel run? "))
    moderator_after = int(input("After how many turns should you join as moderator? (0 for no moderation): "))

    while True:
        try:
            # Run simulation 
            continue_program = run_simulation(topic, agent_names, turns, moderator_after, personas)
            if not continue_program:
                break
            
            # If continuing, get new topic and settings
            topic = input("\nEnter new topic of discussion: ").strip()
            agent_names = select_agents(personas)
            turns = int(input("How many turns should the panel run? "))
            moderator_after = int(input("After how many turns should you join as moderator? (0 for no moderation): "))

        except Exception as e:
            print(f"Error running simulation: {e}")
            break

if __name__ == "__main__":
    main()