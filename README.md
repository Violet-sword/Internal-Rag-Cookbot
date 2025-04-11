## Local RAG Q&A Bot

A lightweight internal retrieval-augmented generation (RAG) assistant that answers your questions using a local Embedding model and LLM model via [Ollama](https://ollama.com), powered by LangChain and FAISS.

This version is trained on community-sourced cooking tips, but you can customize it to your own content easily.

## Features

- Fully local RAG setup (no cloud APIs!)
- Uses Ollama-compatible models for both embedding and generation
- Built with LangChain, FAISS, and Python
- Interactive terminal interface
- Fallback to general knowledge if answer isn’t found in local data

## Requirements

- Python 3.11+
- [Ollama](https://ollama.com) installed and running
- pull LLM model and Embedding model from Ollama (change line 18 and 22 of the code accordingly)

Install Python library dependencies:
```bash
pip install langchain langchain-community langchain-ollama faiss-cpu
```

Check if the knowledge base file is in the same directory as "internal-rag-cookbot.py". I have named mine "cooking-tips-comments.txt", the name and contents of the file can be changed. 

## Usage

Run the following command in the directory of the python file. 
```bash
python internal-rag-cookbot.py
```

Type in what you want to ask when the prompt "Your question: " shows up. 

Example use of the code:
```bash
<some-user-directory>:~$ python internal-rag-cookbot.py
    Internal RAG Q&A Bot    
Ask questions about cooking hacks and kitchen tips.
This assistant is powered by a local language model and a custom knowledge base built from community-sourced cooking advice.
Type 'exit' to quit.

Your question:
```

Here we enter our question:
```bash
Your question: i am trying to bake some chocolate chip cookies, any tips?
```

The answer printed out is:
```bash
Answer: Based on the provided context, here's a tip for your chocolate chip cookies:

**Brown the butter!** The speaker's wife browns the butter before adding it to the dough, and he says they're the best cookies he's ever had.



The context also suggests being organized by getting all your ingredients and containers ready beforehand. 

Your question: 
```

now we can type "exit" to close this chatbot: 

```bash
Your question: exit
Goodbye!
```




