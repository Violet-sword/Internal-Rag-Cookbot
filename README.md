## Local RAG Q&A Bot

A lightweight internal retrieval-augmented generation (RAG) assistant that answers your questions using a local Embedding model and LLM model via [Ollama](https://ollama.com), powered by LangChain and FAISS.

This version is trained on community-sourced cooking tips, but you can customize it to your own content easily.

## Features

- Fully local RAG setup (no need for cloud api)
- Uses Ollama-compatible models for both embedding and generation
- Built with Python, using LangChain and FAISS library
- Interactive terminal interface
- Fallback to general knowledge if answer isn’t found in local data

## Requirements

- Python 3.11+
- [Ollama](https://ollama.com) installed and running
- pull LLM model and Embedding model from Ollama to local (after pulling, update line 18 and 22 of the code accordingly)

Install Python library dependencies:
```bash
pip install langchain langchain-community langchain-ollama faiss-cpu
```

Check if the knowledge base file is in the same directory as "internal-rag-cookbot.py". I have named mine "cooking-tips-comments.txt", the name and contents of the file can be changed. 

## How It Works

This project uses Retrieval-Augmented Generation (RAG), which combines a embedding vector database created from your content, along with a language model to answer questions more accurately and contextually.

### Embedding the Content

- The text file (cooking-tips-comments.txt) is our knowledge base file.

- The contents of the file is converted by projecting the **high-dimensional space of initial data vectors** into a **lower-dimensional space** using a local embedding model (in the code provided, we used 'snowflake-arctic-embed:335m' from Ollama).

- These vectors capture the semantic meaning of the text — two similar tips will have similar embeddings. 

### Storing in a Vector Database

- The vectors are stored in FAISS, a fast, in-memory vector store that supports efficient similarity search.

- This lets the system quickly find the most relevant chunks of text when a new question is asked.

### Retrieving and Generating Answers

- When you ask a question, it is also embedded into a vector on the spot for the LLM model to actully understand your question.

- FAISS compares this vector to the ones in the vector database and returns the top matching text chunks, and the specific phrase we use is **"top-k"**.

- **top-k** is the number of top matching entries we retrieve from the embedding. If the number is too small, we might miss out on some relevant information; if it's too large, we're likely getting too much unrelated content. In the code provided we are using **"top-k 3"**, which is a recommended good default option.

- These relevant texts are passed to the LLM (in the provided code we used 'gemma3:12b') along with our question.

- The LLM uses this context to generate a more accurate, grounded, and helpful response.

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

The answer responded is:
```bash
Answer: Based on the provided context, here's a tip for your chocolate chip cookies:

**Brown the butter!** The speaker's wife browns the butter before adding it to the dough, and he says they're the best cookies he's ever had.



The context also suggests being organized by getting all your ingredients and containers ready beforehand. 

Your question: 
```

Now we can type "exit" to close this chatbot: 

```bash
Your question: exit
Goodbye!
```




