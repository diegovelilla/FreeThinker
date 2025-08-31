# Technology Stack

## Core Technologies
- **Python 3.x**: Primary programming language
- **Groq API**: Fast inference for Llama models
- **Hugging Face Hub**: Access to Mistral models
- **JSON**: Data interchange format for tool communication

## Key Dependencies
```
termcolor      # Colored terminal output
groq          # Groq API client
python-dotenv # Environment variable management
huggingface-hub # Hugging Face model access
praw          # Reddit API wrapper
bs4           # BeautifulSoup for web scraping
```

## Environment Setup
- Configuration stored in `config/.env`
- API keys required: GROQ_API_KEY, SERPER_API_KEY, CLIENT_ID, CLIENT_SECRET, WEATHER_API_KEY
- Uses `dotenv_values()` for secure credential loading

## Common Commands

### Installation
```bash
git clone https://github.com/diegovelilla/FreeThinker
cd FreeThinker
pip install -r requirements.txt
```

### Running the Agent
```bash
python3 -m agent
```

### Exit Command
Type `exit` in the interactive prompt to quit

## Architecture Patterns
- **Two-stage inference**: First determines tool choice, then formats tool inputs
- **Modular tool system**: Each tool is a separate function with standardized interface
- **Template-based prompting**: System prompts use string formatting for dynamic content
- **JSON-based communication**: All tool inputs/outputs use JSON list format