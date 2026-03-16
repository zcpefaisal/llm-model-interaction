import os
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate

# It is better to set the API key as an environment variable
os.environ["OPENAI_API_KEY"] = "your-actual-openai-api-key"

# Ensure 'rag_vs_fine_tuning.pdf' is in the same folder as this script
loader = PyPDFLoader('rag_vs_fine_tuning.pdf')
data = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=50)
docs = splitter.split_documents(data)

# Create Vector Database
# We use OpenAIEmbeddings to turn text into searchable vectors
embedding_function = OpenAIEmbeddings(model='text-embedding-3-small')
vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_function,
    persist_directory="./chroma_db" # Saves the database locally
)

# Initialize Retriever and LLM
retriever = vectorstore.as_retriever(
    search_type="similarity", 
    search_kwargs={"k": 3}
)

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0)

# Define the Prompt Template
message = """
Answer the following question using the context provided:

Context:
{context}

Question:
{question}

Answer:
"""
prompt_template = ChatPromptTemplate.from_messages([("human", message)])

# Build and Invoke the RAG Chain
# The '|' operator pipes the output of one step into the next
rag_chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt_template
    | llm
)

# Run the query
query = "Which popular LLMs were considered in the paper?"
response = rag_chain.invoke(query)

print("--- AI Response ---")
print(response.content)