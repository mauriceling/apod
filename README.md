# APOD: Agent Panel On-Demand

APOD creates moderated panel discussions between AI agents on any topic. It leverages OpenRouter's API to enable multi-agent conversations with unique personas.

## Features

- Create discussions with multiple AI agents
- Each agent has a unique persona and perspective
- Optional human moderation during discussions 
- Conversation logging in Markdown format
- Flexible turn management and continuation
- OpenRouter API integration for reliable AI responses

## Installation

1. Clone the repository:
```bash
git clone https://github.com/mauriceling/apod.git
cd apod
```

2. Install dependencies:
```bash
pip install openai
```

3. Set up your OpenRouter API key:
   - Get an API key from [OpenRouter](https://openrouter.ai)
   - Either:
     - Set environment variable: `OPENROUTER_API_KEY=your_key`
     - Or save in `openrouter.api_key` file

## Usage

1. Run the program:
```bash
python apod.py
```

2. Enter discussion details:
   - Topic for discussion
   - Select participating agents
   - Number of conversation turns
   - Moderation preferences

3. The discussion will proceed with:
   - Agents taking turns responding
   - Optional moderation at specified intervals
   - Conversation logging to `chatlogs` directory
   - Option to continue or end discussion

## File Structure

- `apod.py` - Main program entry point
- `simulator.py` - Core discussion simulation logic
- `utils.py` - Utility functions and agent selection
- `logger.py` - Conversation logging system
- `persona.ini` - Agent persona definitions
- `chatlogs/` - Directory for conversation logs

## Current Version

- Release: 0.1.0 "Cashew Nut Butter"
- Date: 24th September 2025

## License

GNU General Public License v3 (GPL-3.0) for academic or not-for-profit use only.

## Contributing

Contributions are welcome! Please feel free to submit pull requests.

## Authors

- Maurice Ling
- Project URL: https://github.com/mauriceling/apod
