import gradio as gr
from langchain.agents import initialize_agent, AgentType
from langchain_groq import ChatGroq
from langchain.memory import ConversationBufferMemory
from tools import websearch_tool
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# ======================
# LLM
# ======================
llm = ChatGroq(model="llama-3.1-8b-instant")

# ======================
# Tools
# ======================
tools = [
    websearch_tool
]

# ======================
# Memory
# ======================
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# ======================
# Agent
# ======================
agent = initialize_agent(
    tools                 = tools,
    llm                   = llm,
    agent                 = AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose               = True,
    handle_parsing_errors = True,
    memory                = memory,
    max_iterations        = 10
)

# ======================
# Chat function
# ======================
def chat(message):
    try:

        prompt = f"""
            You are an AI assistant. 

            - If the user greets you (e.g., "Hi", "Hello", "Hey"), respond with a short humanize friendly greeting.
            - If the user asks a question or provides a query, answer professionally and concisely.
            - If information is not available, say "I don't have that information."
            - Keep responses clear and helpful.

            User Input:
            {message}
            """

        response = agent.invoke({"input": prompt})
        return response["output"]
    except Exception as e:
        return f"❌ Error: {str(e)}"

# ======================
# Gradio UI with Theme
# ======================
with gr.Blocks(theme=gr.themes.Soft()) as ui:
    gr.Markdown("## 🤖 AI Chat Bot")
    gr.Markdown("AI-powered assistant with greeting and web search")

    # Chat display
    chatbot = gr.Chatbot()

    # User input
    user_input = gr.Textbox(
        placeholder="Type your message here...",
        label="Your Message",
        lines=1
    )

    # Clear chat button
    clear_btn = gr.Button("Clear Chat")

    # Response function
    def respond(message, history):
        if not message:
            return history

        response = chat(message)
        
        history.append({"role": "user", "content": message})
        history.append({"role": "assistant", "content": response})

        return history, ""

    # Bind submit and clear
    user_input.submit(respond, [user_input, chatbot], [chatbot, user_input])
    clear_btn.click(lambda: [], None, chatbot)

if __name__ == "__main__":
    ui.launch()
