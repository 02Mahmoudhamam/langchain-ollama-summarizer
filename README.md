# 📄 LangChain + Ollama Text Summarizer

A simple practical assignment demonstrating LangChain's Runnable Pipeline with a local LLM

## 📌 Overview

This project is a text summarization pipeline built using:

- **LangChain** (v0.2+ Runnable API)
- **Ollama** (local LLM runtime, no API keys required)
- **Python 3.10+** and virtual environments

The goal of the assignment is to show the theoretical + practical understanding of:

- How Large Language Models (LLMs) are used inside LangChain
- How prompts are structured using `PromptTemplate`
- How to pipe components together using the `|` (Runnable) operator
- How to run a fully local LLM via Ollama
- How to build a small but real LLM-powered application

This implementation summarizes text from a file (`data/input.txt`) and saves the output to `outputs/summary.txt`.

## 🎯 Learning Objectives

This assignment demonstrates:

- The structure of a LangChain application (model → prompt → chain → output)
- The use of Runnable pipelines instead of deprecated classes like `LLMChain`
- How to build a local AI workflow without external API keys
- How to integrate LangChain with Ollama as a local LLM backend
- File I/O for reading and saving generated text
- A clean, reusable project layout

## 🧠 Why Ollama?

Ollama allows you to run LLMs locally on your machine, such as:

- `llama3.2`
- `mistral`
- `phi3`
- many others…

Unlike OpenAI or Groq:

- ❌ No API keys
- ❌ No billing
- ❌ No internet required
- ✅ Runs fully offline
- ✅ Works perfectly with LangChain

This makes it ideal for assignments, prototypes, and privacy-focused workflows.

## 🏗 Project Structure

```
langchain-ollama-summarizer/
│
├── data/
│   └── input.txt          # Text to summarize
│
├── outputs/
│   └── summary.txt        # Generated summary
│
├── task_langchain_summarizer.py   # Main script for the assignment
│
├── requirements.txt       # Dependencies
└── README.md              # This file
```

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/langchain-ollama-assignment.git
cd langchain-ollama-assignment
```

### 2. Create and Activate Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/Mac
# .venv\Scripts\activate       # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Install & Prepare Ollama

Make sure Ollama is installed:

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

Pull the model used in this assignment:

```bash
ollama pull llama3.2
```

Test that it is running:

```bash
ollama list
```

## 🚀 Running the Summarizer

1. Ensure you have text inside `data/input.txt`

2. Run the main script:

```bash
python task_langchain_summarizer.py
```

3. You should see:

```
=== SUMMARY (TERMINAL OUTPUT) ===
<model-generated summary here>
```

4. A file `outputs/summary.txt` will also be created containing the summary.

## 🧩 How It Works (Theoretical Overview)

LangChain applications are built using 3 main components:

### 1. Model

The LLM generating the output.  
Here we use:

```python
ChatOllama(model="llama3.2")
```

This connects to Ollama locally at `localhost:11434`.

### 2. Prompt

A template describing what we want from the model:

```python
PromptTemplate.from_template(
    "Summarize the following text in 3-5 concise sentences:\n\n{text}\n\nSummary:"
)
```

`{text}` is filled dynamically at runtime.

### 3. Runnable Chain

LangChain v0.2+ introduces the `|` operator to connect components:

```python
chain = prompt | llm
```

This means:

```
input → prompt formatting → model → output
```

A clean, modern, and elegant design used across LangChain now.

## 📚 Example Output

```
LangChain is a framework that helps developers build applications powered by LLMs.
It connects prompts, memory, and external tools into reusable pipelines.
Running locally with Ollama provides an offline, fast, and private solution.
```

## 🔮 Possible Extensions

This project can be expanded into:

- Multi-file summarization
- CLI arguments for input/output paths
- Auto-generated report summaries
- RAG (Retrieval Augmented Generation) pipeline
- GUI or web interface
- Integrating embeddings with local vector stores (e.g., ChromaDB)

## ✔️ Final Notes

This assignment demonstrates both:

- **Understanding of LangChain concepts** (theory)
- **Correct practical implementation using local LLMs** (practice)

The project is:

- Clean
- Reproducible
- API-free
- Fully local
- Ready for review / submission / GitHub

## ✨ Author

**Prepared by:** Mahmoud A Hamam
**Instructor / Reviewer:** Eng.Mohammed Khalifeh - Cyber Robot Group (Thanks for Internship  Opportunity)
**Course / Assignment:** LangChain Project – Text Summarization