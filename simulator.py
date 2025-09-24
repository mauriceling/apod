"""!
APOD: Agent Panel On-Demand - Simulation System

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
import openai
import time
from logger import start_log, log_turn, log_summary
from utils import moderator_prompt
import os

def setup_openrouter():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OpenRouter API key not found in environment variables")
    
    # Configure OpenAI client for OpenRouter
    openai.api_base = "https://openrouter.ai/api/v1"
    openai.api_key = api_key

def generate_response(agent_name, prompt):
    try:
        print(f"\n👤 {agent_name} is thinking...")
        response = openai.ChatCompletion.create(
            model="openai/gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            headers={
                "HTTP-Referer": "https://github.com/mauriceling/apod",
                "X-Title": "APOD: Agent Panel On Demand"
            }
        )
        reply = response.choices[0].message.content.strip()
        print(f"\n{agent_name}: {reply}\n")
        return reply
    except Exception as e:
        print(f"\n❌ Error when {agent_name} tried to respond: {str(e)}")
        print("Debug info:")
        print(f"API Base: {openai.api_base}")
        print(f"API Key present: {'Yes' if openai.api_key else 'No'}")
        print(f"Prompt length: {len(prompt)} characters")
        raise

def run_simulation(topic, agent_names, turns, moderator_after, personas):
    try:
        setup_openrouter()
        print(f"\n🎯 Starting discussion on: {topic}")
        print(f"Participants: {', '.join(agent_names)}")
        
        log = start_log(topic, agent_names, moderator_after)

        previous_message = topic
        for i in range(turns):
            current_agent = agent_names[i % len(agent_names)]
            persona = personas[current_agent]
            prompt = f"{persona}\n\nRespond to this idea:\n\"{previous_message}\""

            reply = generate_response(current_agent, prompt)
            log_turn(log, current_agent, reply, "")

            previous_message = reply

            # Moderator injection
            if moderator_after and i + 1 == moderator_after:
                moderator_input = input("\n🧑 Moderator: Enter your reflection or guidance:\n").strip()
                log_turn(log, "Moderator", moderator_input, "moderator")
                previous_message = moderator_input

            # After each turn, ask if user wants to continue
            if i < turns - 1:  # Don't ask on the last turn
                continue_chat = input("\nContinue the discussion? (y/n): ").lower().strip()
                if continue_chat != 'y':
                    print("\n💫 Ending discussion early...")
                    break

        log_summary(log, topic, agent_names)
        
        # Ask if user wants to continue discussion
        continue_discussion = input("\nContinue this discussion with more turns? (y/n): ").lower().strip()
        if continue_discussion == 'y':
            additional_turns = int(input("How many more turns? "))
            moderator_after = int(input("After how many turns should you join as moderator? (0 for no moderation): "))
            return run_simulation(previous_message, agent_names, additional_turns, moderator_after, personas)
        else:
            print("\n👋 Thanks for using APOD!")
            return False
            
    except Exception as e:
        print(f"Error during simulation: {e}")
        raise