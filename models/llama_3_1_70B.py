from groq import Groq
from dotenv import dotenv_values

CONFIG = dotenv_values("./config/.env")


class llama_3_1_70B:

    def __init__(self, model_name, system_prompt):
        """
        Initializes the llama-3.1-70B with the given parameters.

        Parameters:
        model_name (str): The name of the model to use.
        system_prompt (str): The system prompt to use.
        """
        self.model_name = model_name
        self.system_prompt = system_prompt
        self.client = Groq(api_key=CONFIG["GROQ_API_KEY"])

    def first_answer(self, prompt):
        """
        Generates a response from the model based on the provided prompt.

        Parameters:
        prompt (str): The user query to generate a response for.

        Returns:
        str: The response from the model as a string formatted as a list.
        """
        response = self.client.chat.completions.create(
            messages=[
                {
                    "role": "system",
                    "content": f"{self.system_prompt}"
                },
                {
                    "role": "user",
                    "content": f"{prompt}"
                }
            ],
            model=self.model_name
        )

        return response.choices[0].message.content

    def second_answer(self, prompt, format_prompt):
        """
        Generates a response from the model based on the provided prompt and a format prompt.

        Parameters:
        prompt (str): The user query to generate a response for.

        Returns:
        str: The response from the model as a string formatted as a list.
        """
        response2 = self.client.chat.completions.create(
            messages=[{"role": "system", "content": format_prompt},
                      {"role": "user", "content": f"{prompt}"}],
            model=self.model_name)

        return response2.choices[0].message.content
