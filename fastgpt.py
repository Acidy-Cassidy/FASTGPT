import openai
import tkinter as tk
from tkinter import scrolledtext

# Replace this with your OpenAI API key
OPENAI_API_KEY = 'your-api-key-here'

# Initialize the OpenAI API
openai.api_key = OPENAI_API_KEY

def submit_query():
    prompt = input_field.get()
    input_field.delete(0, tk.END)

    chat_history.insert(tk.END, f'You: {prompt}\n')
    chat_history.see(tk.END)

    response = openai.Completion.create(
        engine='davinci-codex',
        prompt=f'{prompt}\n',
        temperature=0.5,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    generated_text = response.choices[0].text.strip()
    chat_history.insert(tk.END, f'GPT-3: {generated_text}\n')
    chat_history.see(tk.END)

# Create the main application window
root = tk.Tk()
root.title('Chat with GPT-3')

# Create a scrolled text widget for the chat history
chat_history = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=20)
chat_history.grid(row=0, column=0,
