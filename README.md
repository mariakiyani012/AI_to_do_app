# AI-Powered To-Do Application

This is a Streamlit-based to-do application enhanced with AI features. It allows users to add tasks, automatically generate subtasks, and translate tasks into different languages using Groq's LLM API.

# Deployed Link

https://mariakiyani012-ai-to-do-app-app-um3dx7.streamlit.app/

## Features

- Add new to-do tasks
- AI-generated subtasks for each task
- Mark tasks as completed
- Translate tasks into any language using AI
- Persistent storage with SQLite

## Project Structure

```
.
├── app.py                # Main Streamlit app
├── db/
│   └── database.py       # Database functions (SQLite)
├── services/
│   └── groq_service.py   # AI subtask and translation services
├── data/
│   └── todo_app.db       # SQLite database file
├── .env                  # API keys for OpenAI and Groq
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

## Setup

1. **Clone the repository**  
   ```
   git clone <repo-url>
   cd to-do-app
   ```

2. **Install dependencies**  
   ```
   pip install -r requirements.txt
   ```

3. **Set up API keys**  
   - Copy `.env.example` to `.env` or create a `.env` file with:
     ```
     GROQ_API_KEY="your-groq-api-key"
     ```
   - Replace with your actual API key.

4. **Run the app**  
   ```
   streamlit run app.py
   ```

## Usage

- Enter a new task in the input box and click "Add Task".
- View all tasks and their AI-generated subtasks.
- Mark tasks as completed.
- Translate any task into your desired language.

## Dependencies

See [requirements.txt](requirements.txt).

## License

MIT