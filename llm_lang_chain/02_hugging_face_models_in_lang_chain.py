from langchain_huggingface import HuggingFacePipeline

# Define the LLM
# .from_model_id() handles the downloading and setup automatically
llm = HuggingFacePipeline.from_model_id(
    model_id="crumb/nano-mistral",
    task="text-generation",
    pipeline_kwargs={
        "max_new_tokens": 20,
        "repetition_penalty": 1.1 # Helps prevent the model from looping words
    }
)

# Define the prompt
prompt = "Hugging Face is"

# Invoke the model
# Note: Local models return the full text including your prompt
response = llm.invoke(prompt)

print("Model Output")
print(response)