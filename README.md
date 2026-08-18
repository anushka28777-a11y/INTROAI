#  INTROAI — Simple AI Agent

A beginner-friendly **rule-based AI agent** developed as part of the **AI-Augmented Workflow assignment (Week 1–3 deliverable)**.

INTROAI is a lightweight command-line chatbot that can understand a few basic conversational commands and solve simple mathematical expressions safely without using `eval()`.

##  Features

* Responds to greetings such as `hello` and `hi`
*  Identifies itself when asked about its name
*  Provides basic help
*  Solves simple mathematical expressions
*  Addition
*  Subtraction
*  Multiplication
*  Division
*  Power operations using `^` and `**`
*  Handles division-by-zero errors
*  Uses safe operator functions instead of `eval()`
*  Exits when the user enters `bye`

##  Example

```text
Simple AI Agent (now with math!)
Try things like: 5 + 3, 12 * 7, 9 / 2, 2 ^ 10
Type 'bye' to exit.

You: hello
Agent: Hello! Nice to meet you.

You: 5 + 3
Agent: 5 + 3 = 8

You: 12 * 7
Agent: 12 * 7 = 84

You: 2 ^ 10
Agent: 2 ^ 10 = 1024

You: bye
Agent: Goodbye!
```

##  Technologies Used

* **Python 3**
* `re` — pattern matching for mathematical expressions
* `operator` — safe mathematical operations

No external Python libraries are required.

##  Project Structure

```text
INTROAI/
│
├── main.py
├── README.md
├── ContributionLog.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

### `main.py`

Contains the complete AI agent, including:

* Chatbot interaction
* User input handling
* Mathematical expression detection
* Mathematical calculation
* Error handling

### `ContributionLog.md`

Contains the development/contribution record for the project.

##  How to Run

### 1. Clone the repository

```bash
git clone https://github.com/anushka28777-a11y/INTROAI.git
```

### 2. Open the project directory

```bash
cd INTROAI
```

### 3. Run the agent

```bash
python main.py
```

##  Supported Commands

| Input    | Agent Response                 |
| -------- | ------------------------------ |
| `hello`  | Greeting                       |
| `hi`     | Greeting                       |
| `name`   | Information about the agent    |
| `help`   | List of supported interactions |
| `5 + 3`  | `5 + 3 = 8`                    |
| `12 * 7` | `12 * 7 = 84`                  |
| `9 / 2`  | `9 / 2 = 4.5`                  |
| `2 ^ 10` | `2 ^ 10 = 1024`                |
| `bye`    | Exits the agent                |

##  Safety

The mathematical solver intentionally avoids Python's `eval()` function for processing user input.

Instead, supported operators are mapped to functions from Python's built-in `operator` module.

This limits calculations to the operations explicitly supported by the agent.

##  Project Objective

The objective of this project is to demonstrate the development of a simple AI-style conversational agent with basic natural-language pattern recognition and mathematical problem-solving capabilities.

The project also demonstrates fundamental concepts such as:

* Conditional logic
* Regular expressions
* Functions
* Dictionaries
* Exception handling
* User input processing
* Safe mathematical operations

##  Future Improvements

Possible future versions could include:

* More natural-language understanding
* Support for multi-step calculations
* More conversational responses
* Memory of previous interactions
* Additional mathematical functions
* A graphical or web interface
* Integration with a modern LLM/API
* Voice input and output

##  Author

**Anushka**

GitHub: `anushka28777-a11y`

##  License

This project is intended for educational and learning purposes.
