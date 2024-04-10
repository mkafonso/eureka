import os
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator

def initialize_langchain_model(openai_api_key, data_directory):
    # Set the OpenAI API key in the environment variable
    os.environ["OPENAI_API_KEY"] = openai_api_key

    # Load text data from the specified directory using TextLoader
    loader = TextLoader(data_directory)

    # Create a vector store index from the loaded data using VectorstoreIndexCreator
    index = VectorstoreIndexCreator().from_loaders([loader])

    # Initialize a ConversationalRetrievalChain with ChatOpenAI model and retriever
    chain = ConversationalRetrievalChain.from_llm(
        llm=ChatOpenAI(model="gpt-3.5-turbo"),
        retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
    )

    return chain

def process_langchain_query(chain, query, chat_history):
    # Process a query using the language chain model
    result = chain({"question": query, "chat_history": chat_history})
    return result['answer']

def update_chat_history(chat_history, query, answer):
    # Update the chat history with the latest query and its corresponding answer
    chat_history.append((query, answer))
    return chat_history
