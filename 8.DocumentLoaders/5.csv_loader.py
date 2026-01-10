from langchain_community.document_loaders import CSVLoader



loader = CSVLoader(
    file_path="8.DocumentLoaders/Social_Network_Ads.csv"
)

docs = loader.load()



# print(docs)
# print()
print(len(docs))
# print()
print(docs[0])
# print()
# print(docs[0].metadata)



