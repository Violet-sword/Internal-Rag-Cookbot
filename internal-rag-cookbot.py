
# Import necessary libraries
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_ollama import OllamaEmbeddings, OllamaLLM
from langchain_community.vectorstores import FAISS

# Read comments from the file
file_path = "cooking-tips-comments.txt"

with open(file_path, "r", encoding="utf-8") as file:
    all_texts = file.readlines()

# Split content into chunks
text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
all_chunks = [chunk for text in all_texts for chunk in text_splitter.split_text(text)]

# Initialize Ollama embeddings and FAISS vector store
embeddings = OllamaEmbeddings(model="snowflake-arctic-embed:335m")
vector_store = FAISS.from_texts(all_chunks, embeddings)

# Initialize Ollama LLM
llm = OllamaLLM(model="gemma3:12b", temperature=0.3)

# Question-answering function with fallback
def ask_question_with_fallback(query):
    docs = vector_store.similarity_search(query, k=3)

    if not docs:
        return use_general_knowledge(query)

    context = "\n\n".join([doc.page_content for doc in docs])

    rag_prompt = f"""
    Use the following context to answer the question:
    
    Context:
    {context}

    Question: {query}
    """

    rag_answer = llm.invoke(rag_prompt)

    if "NO_ANSWER_FOUND" in rag_answer or "don't know" in rag_answer.lower():
        return use_general_knowledge(query)

    return {"answer": rag_answer}

# General knowledge fallback
def use_general_knowledge(query):
    general_prompt = f"Answer using general knowledge: {query}"
    general_answer = llm.invoke(general_prompt)
    return {"answer": general_answer}

# Continuous interaction loop
print("    Internal RAG Q&A Bot    ")
print("Ask questions about cooking hacks and kitchen tips.")
print("This assistant is powered by a local language model and a custom knowledge base built from community-sourced cooking advice.")
print("Type 'exit' to quit.\n")


while True:
    query = input("Your question: ").strip()
    if query.lower() == "exit":
        print("Goodbye! ")
        break

    result = ask_question_with_fallback(query)
    print("\nAnswer:", result["answer"], "\n")
