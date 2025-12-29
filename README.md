# 🤖 AI Chat Bot with DuckDuckGo Search

A **Gradio-based AI Chat Bot** using **LangChain** and **Groq LLM**, with integrated **web search** functionality via a custom DuckDuckGo tool. The bot also detects greetings and responds in a friendly, human-like manner.

---

## Features

- 💬 **Conversational AI** using Groq LLM (`llama-3.1-8b-instant`)
- 🌐 **DuckDuckGo Web Search** integrated for answering queries
- 🤝 **Greeting Detection** for friendly human-like responses
- 🧠 **Conversation Memory** keeps track of chat history
- 🎨 **Modern UI** using Gradio with built-in themes
- 🧹 **Clear Chat Button** to reset conversation
- 🔒 **Environment Variables** for secure API keys (`.env` support). Add `GROQ_API_KEY`

---

## Requirements

- Python 3.10+
- Install dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

- How to run:

```bash
python app.py
```

## Demo Video

Check out the AI Chat Bot in action:

<video width="600" controls>
  <source src="demo.mp4" type="video/mp4">
  Your browser does not support the video tag.
</video>