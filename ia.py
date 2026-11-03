from getpass import getpass
from openai import OpenAI
#kwargs : keys with arguments
x = ""
client = OpenAI(api_key=x)

response = client.responses.create(
    model="gpt-4.1-mini",
    input="País más grande del mundo",
    max_output_tokens=50,
)

print(response.output_text)