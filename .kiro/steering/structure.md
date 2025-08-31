# Project Structure

## Root Files
- `agent.py`: Main entry point and Agent class implementation
- `requirements.txt`: Python dependencies
- `README.md`: Project documentation
- `LICENSE`: Apache 2.0 license
- `__init__.py`: Package initialization

## Directory Organization

### `/config`
- `.env`: Environment variables and API keys (not tracked in git)

### `/models`
- Model wrapper classes for different LLM providers
- Each model implements `first_answer()` and `second_answer()` methods
- Files: `llama_3_1_70B.py`, `mistral_nemo_instruct_2407.py`
- `__init__.py`: Package initialization

### `/prompts`
- `system_prompt.py`: Agent system prompt template with tool descriptions
- `format_prompt.py`: Tool-specific formatting prompts
- `__init__.py`: Package initialization

### `/tools`
- Individual tool implementations as functions
- `toolbox.py`: Tool management and documentation system
- Each tool follows standard interface: `function_name(input_list) -> str`
- Tools: `basic_calculator.py`, `weather_forecaster.py`, `reddit_scrapper.py`, `search_tool.py`, `scrape_tool.py`
- `__init__.py`: Package initialization

## Code Organization Patterns

### Tool Interface
- All tools accept `input_list` parameter (list of strings)
- Return formatted string responses
- Include comprehensive docstrings for tool discovery
- Handle errors gracefully with descriptive messages

### Model Interface
- Constructor takes `model_name` and `system_prompt`
- `first_answer(prompt)`: Initial tool selection
- `second_answer(prompt, format_prompt)`: Tool input formatting

### Import Structure
- Relative imports within packages
- All tools imported in main `agent.py`
- Models imported by name in main file