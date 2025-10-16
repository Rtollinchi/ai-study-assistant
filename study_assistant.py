#  Your Smart Study Assistant

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

#Setup

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
print("🎓 Welcome to Your AI Study Assistant!")
print("=" * 40)
print("I can help you study any subject!")
print("Commands:")
print("  - Just chat naturally about what you're studying")
print("  - Type 'quiz me' to get quiz questions")
print("  - Type 'explain [topic]' for detailed explanations")
print("  - Type 'exit' to quit")
print("=" * 60)


# Initialize the smart LLM
llm = ChatOpenAI(
  model="gpt-3.5-turbo",
  temperature=0.7,
  max_tokens=300
)

# Create memory
memory = ConversationBufferMemory(
  return_messages=False
)

# Create the study assitant with a teaching persona
study_chain = ConversationChain(
  llm=llm,
  memory=memory,
  verbose=False  # Set to True for debugging
)

# Give it a teaching personality
system_message = """You are a helpful study assitant.  Your goal is to:
1. Help students understand complex topics.
2. Remember what they're studying across the converstaion.
3. Provide clear, concise explantions and examples.
4. Quiz then to test understanding.
5. Be encouraging and patient.

When student asks to be quizzed, create 3 relevant questions based on what they've been studying.
"""
# Intialize with system message
memory.save_context(
  {"input": "System: " + system_message},
  {"output": "I understand! I'm ready to help you study!"}
)

print("\n✅ Study Assistant initalized with memory!\n")

# Main conversation loop

def chat_with_assistant(user_input):
  """Process user input and return assistant response."""
  response = study_chain.invoke({"input": user_input})
  return response["response"]

def main():

  while True:
    #Get user input
    user_input = input("🧐You: ").strip()

    if user_input.lower() in ["exit", "quit", "q"]:
      print("👋 Goodluck with your studies!")
      print("\n📊 Session Summary:")
      print(f"Total conversation length: {len(memory.buffer)} characters")
      break

    # Skip empty input
    if not user_input:
      continue

    # Get response from assistant
    try:
      response = chat_with_assistant(user_input)
      print(f"🤖 Study Assistant: {response}\n")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please try again.\n")

if __name__ == "__main__":
  main()
