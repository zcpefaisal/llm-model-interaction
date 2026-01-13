import os
from dotenv import load_dotenv
from openai import OpenAI

# Load the variables from .env into the environment
load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY")) # Retrieve the key using os.getenv

prompt="""Summarize the customer support chat in three concise key points: 
        Customer: Hi, I’m trying to log into my account, but it keeps saying my password is incorrect. I’m sure I’m entering the right one.  

        Support: I’m sorry to hear that! Have you tried resetting your password?  

        Customer: Yes, I clicked on "Forgot Password" and entered my email, but I haven’t received the reset link.  

        Support: Let me check that for you. Can you confirm the email address associated with your account?  

        Customer: Sure, it’s john.doe@email.com.  

        Support: Thanks, John. I see that the reset email was sent 15 minutes ago. Could you check your spam or promotions folder? Sometimes emails get filtered there.  

        Customer: Just checked—nothing there either.  

        Support: Got it. I’ll go ahead and resend the reset email. Let me know if you receive it in the next couple of minutes.  

        Customer: Okay, waiting.  

        Support: Also, can you confirm if you signed up using Google or Apple login? Sometimes users have multiple accounts and try logging in with the wrong method.  

        Customer: Oh! I think I might’ve used Google sign-in.  

        Support: That could be the issue! Try clicking "Sign in with Google" instead of entering your password manually.  

        Customer: That worked! I was using the wrong login method. Thanks so much!  

        Support: No problem at all, happy to help! Let us know if you need anything else. Have a great day! 
        """

max_completion_tokens = 400

response = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[{"role": "user", "content": prompt}],
    max_completion_tokens=max_completion_tokens
)

input_token_price = 0.15 / 1_000_000
output_token_price = 0.6 / 1_000_000

# Extract token usage
input_tokens = response.usage.prompt_tokens # get token count form user given prompt
output_tokens = max_completion_tokens

# Calculate cost
cost = (input_tokens * input_token_price + output_tokens * output_token_price)
print(f"Estimated cost: ${cost}")