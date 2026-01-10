from langchain_experimental.text_splitter import SemanticChunker
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

text = """
Cricket is a game of skill, strategy, and teamwork that tests both physical endurance and mental strength.Artificial Intelligence enables machines to learn, think, and make decisions like humans using data and algorithms.

The gym is a place where consistency and dedication turn effort into strength and confidence.
Regular workouts improve physical fitness, mental health, and overall discipline.
"""

splitter = SemanticChunker(
    OpenAIEmbeddings(
        base_url="https://openrouter.ai/api/v1",
        model="openai/text-embedding-3-large",
    ),
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=0.1
)


chunks = splitter.split_text(text)

print(len(chunks))
print(chunks)