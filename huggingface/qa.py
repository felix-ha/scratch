from newspaper import Article

urls = [
    "https://www.tagesschau.de/inland/innenpolitik/steuerschaetzung-154.html",
    "https://www.tagesschau.de/wirtschaft/finanzen/ezb-rat-leitzins-100.html",
    "https://www.zeit.de/gesundheit/2023-09/corona-comirnaty-biontech-angepasst-impfstoff",
]

articles = []

for url in urls:
    article = Article(url)

    article.download()
    article.parse()

    articles.append(article.text)


from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=20,
    length_function=len,
    is_separator_regex=False,
)


texts = text_splitter.create_documents(articles)

print(len(texts))

# print(articles[0])
# print("------------------")
# print(texts[0])
# print(texts[1])
