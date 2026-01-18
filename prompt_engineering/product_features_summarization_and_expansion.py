import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the variables from .env into the environment
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Retrieve the key using os.getenv

# Create a function which take my prompt and will give response
def get_response(prompt):
  # Create a request to the chat completions endpoint
  response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}], 
    temperature = 0)
  return response.choices[0].message.content

product_description = """The Smartphone XYZ-5000 is a device packed with innovative features to enhance the user experience. Its sleek design and vibrant display make it visually appealing, while the powerful octa-core processor ensures smooth performance and multitasking capabilities.
The XYZ-5000 boasts a high-resolution triple-camera system, combining a 48MP primary lens, a 12MP ultra-wide lens, and a 5MP depth sensor, enabling users to capture stunning photos and videos in various shooting scenarios. The device also supports 4K video recording and comes with advanced image stabilization features.
With a generous 128GB of internal storage, expandable up to 512GB via microSD, users can store a vast collection of media files and apps without worrying about running out of space. The smartphone runs on the latest Android OS and offers seamless integration with various Google services.
In terms of security, the XYZ-5000 features a reliable fingerprint sensor and facial recognition technology for quick and secure unlocking. Additionally, it supports NFC for contactless payments and has a dedicated AI-powered virtual assistant to simplify daily tasks.
The device's long-lasting 4000mAh battery ensures all-day usage, and it supports fast charging, providing hours of power with just a few minutes of charging. The XYZ-5000 is also water and dust resistant, giving users peace of mind in various environments.
Overall, the Smartphone XYZ-5000 offers a fantastic combination of style, performance, and advanced features, making it an excellent choice for tech enthusiasts and everyday users alike.
"""
# Craft a prompt to summarize the product description
prompt_summarize = f"""summarizes the product description delimited by triple backtricks in no more then five bullet points'''{product_description}''' """

# Craft a prompt to expand the product's description
prompt_expansion = f"""writes a one paragraph comprehensive overview delimited with triple backtricks cupturing the key information of the product: unique features, benefits, and potential applications. ```{product_description}```
"""

# summarization
response_summarize = get_response(prompt_summarize)


# expansion
response_expansion = get_response(prompt_expansion)


print("Original description: \n", product_description)
print("Summarized description: \n", response_summarize)
print("Expansion description: \n", response_expansion)