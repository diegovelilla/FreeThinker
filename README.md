# FreeThinker: Your own free of charge AI agent

FreeThinker is an AI agent that uses free of charge API open source LLMs in order to automatize tasks. That meaning that you don't required pay-per-token API keys to run it.

## Index
1. [Overview](#overview)
2. [Features](#features)
3. [Files](#files)
4. [Installation](#installation)
5. [Configuration](#configuration)
6. [Usage](#usage)
7. [Toolbox](#toolbox)
8. [Models](#models)
9. [Learnings](#learnings)
10. [License](#license)
11. [Contact](#contact)

---

## Overview
Welcome to the **FreeThinker** documentation. This AI agent is designed to automatize tasks via natural language. It leverages a pool of multiple advanced LLMs to choose from in order to run the agent. The model uses free open source model's APIs in order to run so there are no costs per token.

## Features
- No cost API usage.
- Multiple LLMs to choose from in order to run the agent.
- Easy to use as it uses natural language to communicate with the user.
- Automatize various tasks.

## Files

### `requirements.txt`
This file lists all the Python packages required to run the project. It ensures that all necessary dependencies are installed for the project to function correctly.

### `agent.py`
This is the main file of the project and is the one that needs to be run in order to use FreeThinker.

### `__init__.py`
This files exist in every folder in order to use imports from other folders.

### `config`
This folder contains the .env file with all API keys.

### `models`
This folder contains one file per available model.

### `prompts`
This folder contains prompting files, one for formatting and another one with an initial system prompt.

### `tools`
This folder contains one file per available tool and another one for the toolbox that agglutinates all tools and its docs.

## Installation
To install the FreeThinker, follow these steps:
   ```bash
   git clone https://github.com/diegovelilla/FreeThinker
   cd FreeThinker
   pip install -r requirements.txt
   ```

## Configuration:
Set up your API keys in the **.env** file inside the config model:

    GROQ_API_KEY=your_api_key_here
    SERPER_API_KEY=your_api_key_here

## Usage:
To use FreeThinker just run the following command:
```bash
python3 -m agent
```
In order to quit, just type **exit**.

## Toolbox:
Here are all the tools supported:
- Basic_calculator: Performs basic binary math operations.
- Weather_forecaster: Retrieves weather information on a given location. 
- Reddit_scrapper: Scrapes a given subreddit for a number of posts.
- Search_tool: Searches a given query on Google.
- Scrape_tool: Scrapes a given webpage.

## Models
The models used for this project are:

- [Llama 3.1 70B](https://console.groq.com/docs/models) - Groq.
- [Mistral Nemo Instruct 2407](https://huggingface.co/mistralai/Mistral-Nemo-Instruct-2407) - Hugging Face.

## Learnings
This is what I learned from this project:

- Most of small/old models act poorly on this task (gpt2, gemma 2B...) being mistral-nemo-instruct-2407 one of the exceptions.
- When using small models, good prompting becomes key. There were big improvements after splitting the answer method in first_answer and second_answer.
- Also the usage of examples of wrong outputs or a forbidden words part in the prompt improved the results.
- Easing the answer by asking for a list instead of a dictionary since the models had problems formatting it correctly.
- Using markdown instead of plain text for instructions really felt like an upgrade.

## License
This project is licensed under the **Apache 2.0 License**. See the [LICENSE](https://github.com/diegovelilla/FreeThinker/blob/main/LICENSE) file for more details.

## Contact
For any questions or feedback please reach out to:

- **Email**: [diegovelillarecio@gmail.com](mailto:diegovelillarecio@gmail.com)
- **GitHub Profile**: [diegovelilla](https://github.com/diegovelilla)
- **Hugging Face Profile**: [diegovelilla](https://huggingface.co/diegovelilla)
- **LinkedIn**: [Diego Velilla Recio](https://www.linkedin.com/in/diego-velilla-recio/)

Feel free to open an issue on GitHub or contact me in any way if you have any queries or suggestions.





