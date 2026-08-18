"""
Simple AI Agent (rule-based chatbot + math solver)
Week 1-3 deliverable for the AI-Augmented Workflow assignment.
"""

import re
import operator

# Supported operators, mapped to safe functions (no eval() on user input)
OPERATORS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "x": operator.mul,
    "/": operator.truediv,
    "^": operator.pow,
    "**": operator.pow,
}

# Matches things like "5 + 3", "12*7", "9 / 2", "2^10"
MATH_PATTERN = re.compile(
    r"^\s*(-?\d+(?:\.\d+)?)\s*([\+\-\*/x\^]|\*\*)\s*(-?\d+(?:\.\d+)?)\s*$"
)


def try_solve_math(text):
    """Return a result string if the input looks like a simple math expression,
    otherwise return None."""
    match = MATH_PATTERN.match(text)
    if not match:
        return None

    left, op, right = match.groups()
    left, right = float(left), float(right)
    func = OPERATORS[op]

    try:
        result = func(left, right)
    except ZeroDivisionError:
        return "Error: division by zero."

    if result == int(result):
        result = int(result)

    left_disp = int(left) if left == int(left) else left
    right_disp = int(right) if right == int(right) else right

    return f"{left_disp} {op} {right_disp} = {result}"


def chatbot():
    print("Simple AI Agent (now with math!)")
    print("Try things like: 5 + 3, 12 * 7, 9 / 2, 2 ^ 10")
    print("Type 'bye' to exit.\n")

    while True:
        user = input("You: ")

        if user.lower() == "bye":
            print("Agent: Goodbye!")
            break

        elif "hello" in user.lower() or "hi" in user.lower():
            print("Agent: Hello! Nice to meet you.")

        elif "name" in user.lower():
            print("Agent: I am a simple AI agent that can also do basic math.")

        elif "help" in user.lower():
            print("Agent: Say hello, ask my name, give me a math expression "
                  "like '5 + 3', or say bye to exit.")

        else:
            math_result = try_solve_math(user)
            if math_result is not None:
                print(f"Agent: {math_result}")
            else:
                print("Agent: Sorry, I don't understand.")


if __name__ == "__main__":
    chatbot()
