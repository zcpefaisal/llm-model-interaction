import os
from openai import OpenAI
from pinecone import Pinecone

# Initialize Clients
pc = Pinecone(api_key="pcsk_<TOKEN>rMv9V")
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
index = pc.Index('new-pinecone-index')

# Helper: Prompt Builder
def prompt_with_context_builder(query, docs):
    delim = '\n\n---\n\n'
    prompt_start = 'Answer the question based on the context below.\n\nContext:\n'
    prompt_end = f'\n\nQuestion: {query}\nAnswer:'
    # Combines the retrieved texts into one large string for the AI
    prompt = prompt_start + delim.join(docs) + prompt_end
    return prompt

# Helper: Retrieve Function
def retrieve(query, top_k, namespace, emb_model):
    query_response = client.embeddings.create(input=query, model=emb_model)
    query_emb = query_response.data[0].embedding
    docs = index.query(vector=query_emb, top_k=top_k, namespace=namespace, include_metadata=True)
    
    retrieved_docs = [doc['metadata']['text'] for doc in docs['matches']]
    sources = [(doc['metadata']['title'], doc['metadata']['url']) for doc in docs['matches']]
    return retrieved_docs, sources

# THE FINAL TASK: Question Answering Function
def question_answering(query, chat_model="gpt-4o-mini"):
    # Retrieve the top 3 most relevant documents
    docs, sources = retrieve(
        query=query, 
        top_k=3, 
        namespace='youtube_rag_dataset', 
        emb_model="text-embedding-3-small"
    )
    
    # Build the prompt with the retrieved context
    prompt = prompt_with_context_builder(query, docs)
    sys_prompt = "You are a helpful assistant that answers questions based ONLY on the provided context."

    # Generate response using the Chat model
    response = client.chat.completions.create(
        model=chat_model,
        messages=[
            {"role": "system", "content": sys_prompt},
            {"role": "human", "content": prompt}
        ]
    )
    
    return response.choices[0].message.content, sources

# Run for executions
user_query = "How to build next-level Q&A with OpenAI"
answer, source_list = question_answering(user_query)

print(f"--- ANSWER ---\n{answer}\n")
print("--- SOURCES ---")
for title, url in source_list:
    print(f"- {title}: {url}")