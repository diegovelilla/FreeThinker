class Toolbox:
    def __init__(self):
        self.toolbox = {}

    def store_tools(self, functions_list):
        """
        Stores the name and docstring of each function in the list.

        Parameters:
        functions_list (list): List of function objects to store.

        Returns:
        dict: Dictionary with function names as keys and their docstrings as values.
        """
        for func in functions_list:
            self.toolbox[func.__name__] = func.__doc__
        return self.toolbox

    def output_tools(self):
        """
        Returns the dictionary created in store as a text string.

        Returns:
        str: Dictionary of stored functions and their docstrings as a text string.
        """
        tools_str = ""
        for name, doc in self.toolbox.items():
            tools_str += f"{name}: \"{doc}\"\n"
        return tools_str.strip()
