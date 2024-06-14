#Editor Tool using local llama3.0 8B
import ollama
from crewai_tools import tool

@tool("NewsWriterTool")
def NewsWriterTool(topic: str, details: dict) -> str:
    """
    Generates an article about the 2024 European Championship using a locally deployed Llama model.

    :param topic: The topic or title of the article.
    :param details: A dictionary with key points to cover in the article.
    :return: The generated article as a string.
    """
    # Initialize the Llama model
    model = ollama.Ollama(model="llama3")  # Replace with the actual model name if different

    # Construct the prompt for the Llama model
    prompt = f"Write an engaging and informative article about the 2024 European Championship on the topic '{topic}'.\n"
    prompt += "Cover the following points:\n"

    for point, detail in details.items():
        prompt += f"- {point}: {detail}\n"

    prompt += "\nArticle:\n"

    # Generate the article using the Llama model
    response = model.generate(
        prompt=prompt,
        max_tokens=1000,  # Adjust based on the required length
        temperature=0.7  # Adjust the creativity level as needed
    )

    return response["text"].strip()  # Assume the response is a dictionary with "text" as the generated content