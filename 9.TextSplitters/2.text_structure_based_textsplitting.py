from langchain_text_splitters import RecursiveCharacterTextSplitter


text = """
Artificial Intelligence (AI) refers to the simulation of human intelligence in machines that are designed to think, learn, reason, and make decisions like humans. AI systems are built using algorithms, data, and computational models that enable machines to perform tasks such as problem-solving, speech recognition, image analysis, decision-making, and language understanding. Over the years, AI has evolved from simple rule-based systems to advanced models capable of learning from large amounts of data and improving their performance over time.

AI can be broadly classified into three types: Narrow AI, General AI, and Super AI. Narrow AI is designed to perform a specific task, such as voice assistants, recommendation systems, or facial recognition. This is the most common form of AI used today. General AI refers to machines that can perform any intellectual task that a human can do, while Super AI surpasses human intelligence. Currently, General and Super AI remain theoretical concepts, with research still ongoing.
"""

splitter = RecursiveCharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0
)

chunks = splitter.split_text(text)

print(chunks)
print(len(chunks))
