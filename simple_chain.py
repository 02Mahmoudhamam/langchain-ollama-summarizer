from langchain_core.prompts import PromptTemplate
from langchain_community.chat_models import ChatOllama


def build_summarizer_chain():
    """Build a simple summarization chain using a local Ollama model."""
    # Initialize the local LLM served by Ollama
    llm = ChatOllama(
        model="llama3.2",  # Make sure this model exists: `ollama pull llama3.2`
        # base_url="http://localhost:11434",  # Default Ollama endpoint
    )

    # Define the prompt template
    prompt = PromptTemplate.from_template(
        "Summarize the following text in 2-3 sentences:\n\n{text}\n\nSummary:"
    )

    # Runnable pipeline: prompt → LLM
    chain = prompt | llm
    return chain


def main():
    """Entry point for running the summarization chain."""
    long_text = """
    LangChain is a powerful framework designed to help developers build applications
    powered by large language models. Instead of just sending a single prompt and
    getting a response, LangChain lets you connect LLMs with external tools, memory,
    and custom workflows.
    """

    # Build the chain
    chain = build_summarizer_chain()

    # Invoke the chain with the input text
    summary = chain.invoke({"text": long_text})

    print("\n=== SUMMARY ===\n")
    print(summary)


if __name__ == "__main__":
    main()
 