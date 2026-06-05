# 🤖 AI Chatbot

## Description

A lightweight terminal-based chatbot built in Python that responds to common greetings and basic questions about AI. It uses a dictionary-driven response engine to match user input and reply instantly — no internet connection or external libraries required.

**Features:**
- Responds to greetings (`hello`, `hi`)
- Answers basic questions (e.g., *"What is AI?"*)
- Built-in `help` command to guide users
- Clean exit with the `exit` command

## How to Run

**Requirements:** Python 3.x

1. **Clone or download** the project files into a folder.

2. **Navigate** to the project directory:
   ```bash
   cd your-project-folder
   ```

3. **Run** the chatbot:
   ```bash
   python chatbot.py
   ```

4. **Start chatting!** Type any of the following to get started:

   | Input            | Response                                      |
   |------------------|-----------------------------------------------|
   | `hello` / `hi`   | Greeting response                             |
   | `how are you`    | Bot status reply                              |
   | `what is ai`     | Short definition of Artificial Intelligence   |
   | `what can you do`| Lists bot capabilities                        |
   | `help`           | Usage guide                                   |
   | `bye`            | Farewell message                              |
   | `exit`           | Ends the session                              |

## Example Session

```
Chatbot is running. Type 'exit' to quit.

Say something : hello
Bot: Hi there! How can I help you?

Say something : what is ai
Bot: AI stands for Artificial Intelligence — machines simulating human thinking.

Say something : exit
Bot: Goodbye! Session ended.
```

## Project Structure

```
your-project-folder/
│
├── chatbot.py      # Main chatbot script
└── README.md       # Project documentation
```

---

> 💡 **Want to extend it?** Add more key-value pairs to the `responses` dictionary in `chatbot.py` to teach the bot new answers instantly.
