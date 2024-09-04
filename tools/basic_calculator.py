import json
import operator


def basic_calculator(input_list):
    """
    Perform a numeric operation on two numbers based on the provided list of inputs.

    The supported operations are: ["add", "subtract", "multiply", "divide", "floor_divide", "modulus",
        "power", "less-than", "less-equal", "equal", "not-equal", "greater-equal", "greater-than"].

    Parameters:
    input_list (list): A list containing the operands and the operation. The list must have three elements:
        - The first element is the first operand (numeric value as a string).
        - The second element is the second operand (numeric value as a string).
        - The third element is the operation to perform (one of the supported operations).

        Example format: ["100", "5", "divide"]

    Returns:
    (str): The formatted result of the operation or an error message if something goes wrong.
    """
    # Clean and parse the input string
    try:
        num1 = input_list[0]
        num2 = input_list[1]
        operation = input_list[2]
    except (json.JSONDecodeError, KeyError) as e:
        return str(e), "Invalid input format. Please provide a valid input."

    operations = {
        "add": operator.add,
        "subtract": operator.sub,
        "multiply": operator.mul,
        "divide": operator.truediv,
        "floor_divide": operator.floordiv,
        "modulus": operator.mod,
        "power": operator.pow,
        "less-than": operator.lt,
        "less-equal": operator.le,
        "equal": operator.eq,
        "not-equal": operator.ne,
        "greater-equal": operator.ge,
        "greater-than": operator.gt
    }

    if operation in operations:
        try:
            if operation == "modulus":
                i_num1, i_num2 = int(num1), int(num2)
            else:
                i_num1, i_num2 = float(num1), float(num2)
            result = operations[operation](i_num1, i_num2)
            result_formatted = f"\nThe answer is: {result}.\n"
            return result_formatted

        except Exception as e:
            raise Exception(f"Error during operation execution: {e}")

    else:
        return "\nUnsupported operation. Please provide a valid operation."
