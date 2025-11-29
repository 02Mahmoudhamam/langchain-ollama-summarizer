"""
LangChain + Ollama Text Summarizer

This script is an implementation of a simple text summarization pipeline using:
- LangChain (Runnable pipeline API)
- Ollama as the local LLM provider (no API keys required)

High-level flow:
1. Read input text from data/input.txt
2. Build a LangChain pipeline: PromptTemplate → ChatOllama
3. Invoke the chain to generate a summary
4. Print the summary to the terminal and save it to outputs/summary.txt
"""

from pathlib import Path

from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama


# === Paths and directories configuration ===

BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = BASE_DIR / "outputs"

INPUT_FILE = DATA_DIR / "input.txt"
OUTPUT_FILE = OUTPUT_DIR / "summary.txt"


def load_text(file_path: Path) -> str:
    """Read plain text from a file."""
    if not file_path.exists():
        raise FileNotFoundError(f"Input file not found: {file_path}")
    return file_path.read_text(encoding="utf-8")


def save_text(text: str, file_path: Path) -> None:
    """Save text content to a file."""
    file_path.parent.mkdir(parents=True, exist_ok=True)
    file_path.write_text(text, encoding="utf-8")


def build_summarizer_chain():
    """
    Build a summarization chain using a local Ollama model.

    LangChain components:
    - Model: ChatOllama (local LLM served by Ollama)
    - PromptTemplate: defines the summarization instructions
    - Runnable pipeline: prompt → model
    """
    # Initialize the local LLM served by Ollama
    llm = ChatOllama(
        model="llama3.2",  # Ensure this model is available in Ollama: `ollama pull llama3.2`
        # base_url="http://localhost:11434",  # Default Ollama endpoint, change only if needed
    )

    # Prompt template for summarization
    prompt = PromptTemplate.from_template(
        "Summarize the following text in 3-5 concise sentences:\n\n{text}\n\nSummary:"
    )

    # Runnable pipeline: input → prompt formatting → LLM
    chain = prompt | llm
    return chain


def main():
    """
    Main entry point for the assignment:

    - Loads input text from data/input.txt
    - Builds the LangChain + Ollama summarizer
    - Runs the chain to generate a summary
    - Prints and saves the summary
    """
    print(f"Loading text from: {INPUT_FILE}")
    text = load_text(INPUT_FILE)

    print("Building summarization chain...")
    chain = build_summarizer_chain()

    print("Running summarization...")
    summary_msg = chain.invoke({"text": text})

    # The result is a message-like object; we only need its content
    summary_text = summary_msg.content

    print("\n=== SUMMARY (TERMINAL OUTPUT) ===\n")
    print(summary_text)

    print(f"\nSaving summary to: {OUTPUT_FILE}")
    save_text(summary_text, OUTPUT_FILE)

    print("\nDone ✅")


if __name__ == "__main__":
    main()
