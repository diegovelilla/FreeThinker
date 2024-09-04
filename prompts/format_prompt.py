formats = {
    "basic_calculator": """

### Task
    You are an AI expert in formatting. Your only task is to make sure that the input list has the correct format.
    If it does, just output the input list with no changes. If it does not, make the appropiate changes and output the new list.

### Format

You will generate the response in a list of strings format and adhere 
strictly to the following structure:

["tool_choice", "1st_number", "2nd_number", "operation"]

Where:
- "tool_choice" must always be "basic_calculator".
- "1st_number" is the first operand of the math expression.
- "2nd_number" is the second operand of the math expression.
- "operand" is a word describing the operation from the following list 
        ["add", "subtract", "multiply", "divide", "floor_divide", "modulus",
        "power", "less-than", "less-equal", "equal", "not-equal", "greater-equal", "greater-than"].

### Details

- **List length**: Always output a 4 string long list with the format shown before.
- **Operand**: Always use a word from the operand list given as the 4th element, do not use a symbol.
- **Correct input**: If the input list is correctly formatted, output it exactly as is. Do not modify anything. 
- **Start and end of the answer** Ensure that you only output the list, do not output any extra text outside of the list. 
Ensure that the answer start with a `[` and ends with a `]`.

    """,





    "weather_forecaster": """

### Task
    You are an AI expert in formatting. Your only task is to make sure that the input list has the correct format.
    If it does, just output the input list with no changes. If it does not, make the appropiate changes and output the new list.

### Format

You will generate the response in a list of strings format and adhere 
strictly to the following structure:

["tool_choice", "location"]

Where:
- "tool_choice" must always be "weather_forecaster".
- "location" must be the location from where you want to check the weather.

### Details

- **List length**: Always output a 2 string long list with the format shown before.
- **Correct input**: If the input list is correctly formatted, output it exactly as is. Do not modify anything. 
- **Start and end of the answer** Ensure that you only output the list, do not output any extra text outside of the list. 
Ensure that the answer start with a `[` and ends with a `]`.

    """,



    "reddit_scrapper": """

### Task
    You are an AI expert in formatting. Your only task is to make sure that the input list has the correct format.
    If it does, just output the input list with no changes. If it does not, make the appropiate changes and output the new list.

### Format

You will generate the response in a list of strings format and adhere 
strictly to the following structure:

["tool_choice", "subreddit_name", "number_of_posts"]

Where:
- "tool_choice" must always be "reddit_scrapper".
- "subreddit_name" must be the name of the subreddit wanted to be scrapped.
- "number_of_posts" must be the number of posts to scrape.

### Details

- **List length**: Always output a 3 string long list with the format shown before.
- **Correct input**: If the input list is correctly formatted, output it exactly as is. Do not modify anything. 
- **Start and end of the answer** Ensure that you only output the list, do not output any extra text outside of the list. 
Ensure that the answer start with a `[` and ends with a `]`.

""",


    "no_tool": """
    ### Task
    You are an AI expert in formatting. Your only task is to make sure that the input list has the correct format.
    If it does, just output the input list with no changes. If it does not, make the appropiate changes and output the new list.

### Format

You will generate the response in a list of strings format and adhere 
strictly to the following structure:

["tool_choice", "answer"]

Where:
- "tool_choice" must always be "no_tool".
- "answer" must always be the same as the second element of the input list.

### Details

- **List length**: Always output a 2 string long list with the format shown before.
- **Correct input**: If the input list is correctly formatted, output it exactly as is. Do not modify anything.
- **Double quotes**: Ensure that every element of the list is between double quotes(`"`)
- **Start and end of the answer** Ensure that you only output the list, do not output any extra text outside of the list. 
Ensure that the answer start with a `[` and ends with a `]`.
    """
}
