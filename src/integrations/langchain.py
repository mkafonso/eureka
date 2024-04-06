import os
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

def initialize_langchain_model(openai_api_key, data_directory):
    os.environ["OPENAI_API_KEY"] = openai_api_key

    loader = TextLoader(data_directory)
    index = VectorstoreIndexCreator().from_loaders([loader])

    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    return chain

def process_langchain_query(chain, query, chat_history):
    result = chain({"question": query, "chat_history": chat_history})
    return result['answer']

def update_chat_history(chat_history, query, answer):
    chat_history.append((query, answer))

    return chat_history
