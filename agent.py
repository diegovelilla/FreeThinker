import json
import re
from termcolor import colored
from tools.toolbox import Toolbox

from prompts.system_prompt import agent_system_prompt_template
from prompts.format_prompt import formats
from models.mistral_nemo_instruct_2407 import mistral_nemo_instruct_2407
from models.llama_3_1_70B import llama_3_1_70B
from tools.basic_calculator import basic_calculator
from tools.weather_forecaster import weather_forecaster
from tools.reddit_scrapper import reddit_scrapper
from tools.scrape_tool import scrape_tool
from tools.search_tool import search_tool


class Agent:
    def __init__(self, tools, model, model_name):
        """
        Initializes the agent with a list of tools, a model and the model name.

        Parameters:
        tools (list): List of tool functions.
        model_service (class): The model service class with two methods (first_answer and second_answer).
        model_name (str): The name of the model to use.

        """
        self.tools = tools
        self.model = model
        self.model_name = model_name

    def prepare_tools(self):
        """
        Stores the tools in the toolbox and returns their descriptions.

        Returns:
        str: Descriptions of the tools stored in the toolbox.

        """
        toolbox = Toolbox()
        toolbox.store_tools(self.tools)
        str_tools = toolbox.output_tools()
        return str_tools

    def think(self, prompt):
        """
        Runs the answer methods on the model using the system prompt template and tool descriptions.

        Parameters:
        prompt (str): The user query to generate a response for.

        Returns:
        final_answer (list): The response from the model as a list.
        """
        # print("\nPreparing tools...")
        str_tools = self.prepare_tools()
        agent_system_prompt = agent_system_prompt_template.format(
            tools=str_tools)
        # print("Tools prepared.")

        model_instance = self.model(
            model_name=self.model_name,
            system_prompt=agent_system_prompt
        )

        agent_response_str1 = model_instance.first_answer(prompt)
        agent_response_str1 = agent_response_str1.replace("'", '\'')
        #print(f"My first answer is: {agent_response_str1}.")
        try:
            agent_response_list = json.loads(agent_response_str1)
        except json.JSONDecodeError as e:
            print(f"JSON decoding failed: {e}")
        tool_choice = agent_response_list[0]
        format_prompt = formats[tool_choice]

        agent_response_str2 = model_instance.second_answer(
            agent_response_list, format_prompt)
        agent_response_str2 = agent_response_str2.replace("'", '\'')
        corrected_json_string = re.sub(
            r"(?<!\w)'|'(?!\w)", '"', agent_response_str2)
        #print(f"My second answer is: {corrected_json_string}.")
        try:
            agent_response_list = json.loads(corrected_json_string)
        except json.JSONDecodeError as e:
            print(f"JSON decoding failed: {e}")

        return agent_response_list

    def execute(self, prompt):
        """
        Parses the list returned from the think method and executes the appropriate tool.

        Parameters:
        prompt (str): The user query to generate a response for.

        Returns:
        The response from executing the appropriate tool or the tool_input if no matching tool is found.
        """

        # Choose the correct tool
        agent_response_list = self.think(prompt)
        tool_choice = agent_response_list.pop(0)
        tool_input = agent_response_list

        # Debugging prints
        print(f"My tool choice is: {tool_choice}.")
        print(f"My tool input is: {tool_input}.")

        for tool in self.tools:
            if tool.__name__ == tool_choice:
                response = tool(tool_input)

                print(
                    colored(f'\n{response}', 'green'))
                print(colored(f'Tool used: {tool_choice}\n', 'yellow'))

                return

        # Answer by model
        print(
            colored(f'\n{tool_input[0]}', 'green'))
        print(
            colored(f'Model used: {model_name}\n', 'yellow'))


if __name__ == "__main__":

    tools = [basic_calculator, weather_forecaster,
             reddit_scrapper, search_tool, scrape_tool]
    model = llama_3_1_70B
    model_name = "llama-3.1-70b-versatile"

    # model = mistral_nemo_instruct_2407
    # model_name = "mistralai/Mistral-Nemo-Instruct-2407"

    agent = Agent(tools=tools, model=model,
                  model_name=model_name)

    while True:
        prompt = input(colored("Ask me anything: ", 'cyan'))
        if prompt.lower() == "exit":
            break

        agent.execute(prompt)
