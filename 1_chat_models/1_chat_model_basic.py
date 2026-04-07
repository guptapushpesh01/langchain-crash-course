# Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/
# OpenAI Chat Model Documents: https://python.langchain.com/v0.2/docs/integrations/chat/openai/

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_ollama import ChatOllama

# Load environment variables from .env
load_dotenv()

# Create a ChatOpenAI model
# model = ChatOpenAI(model="gpt-4o-mini")

# Create a ChatAnthropic model
# model = ChatAnthropic(model_name="claude-sonnet-4-20250514")

# Create a ChatGoogleGenerativeAI model
# model = ChatGoogleGenerativeAI(model="gemini-pro")

# Create a ChatOllama model (requires Ollama running locally)
# Popular models: llama3.2, llama3.1, mistral, phi3, gemma2
model = ChatOllama(model="mistral") 

# Invoke the model with a message
result = model.invoke("What is 81 divided by 9?")
print("Full result:")
print(result)
print("Content only:")
print(result.content)
