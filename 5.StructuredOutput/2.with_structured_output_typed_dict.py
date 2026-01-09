from langchain_openai import ChatOpenAI
from typing import TypedDict,Annotated,Optional,Literal

model = ChatOpenAI(
    api_key="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",
    base_url="https://openrouter.ai/api/v1",
    model="openai/gpt-4o-mini",
    temperature=0.5
)

# schema
# class Review(TypedDict): 
#     summary:str
#     sentiment:str

class Review(TypedDict): 
    summary:Annotated[str,"A brief summary of review"]
    sentiment:Annotated[Literal["pos","neg"],"Return sentiment of review either negative,positive or neutral"]
    key_themes : Annotated[list[str],"Write down all the key themes discussed in review in a list"]
    pros : Annotated[Optional[list[str]],"Write dowm all the pros inside list"]
    cons : Annotated[Optional[list[str]],"Write dowm all the cons inside list"]
    name : Annotated[Optional[str],"Write the name of reviewer"]


structured_model = model.with_structured_output(Review)

result = structured_model.invoke("""

I recently upgraded to the Samsung Galaxy S24 Ultra, and I must say, it’s an absolute powerhouse! The Snapdragon 8 Gen 3 processor makes everything lightning fast—whether I’m gaming, multitasking, or editing photos. The 5000mAh battery easily lasts a full day even with heavy use, and the 45W fast charging is a lifesaver.

The S-Pen integration is a great touch for note-taking and quick sketches, though I don't use it often. What really blew me away is the 200MP camera—the night mode is stunning, capturing crisp, vibrant images even in low light. Zooming up to 100x actually works well for distant objects, but anything beyond 30x loses quality.

However, the weight and size make it a bit uncomfortable for one-handed use. Also, Samsung’s One UI still comes with bloatware—why do I need five different Samsung apps for things Google already provides? The $1,300 price tag is also a hard pill to swallow.

Pros:
Insanely powerful processor (great for gaming and productivity)
Stunning 200MP camera with incredible zoom capabilities
Long battery life with fast charging
S-Pen support is unique and useful
                                 
Review by Harshad

            """)

print(result)


