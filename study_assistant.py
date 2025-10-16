#  Your Smart Study Assistant

from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain import LLMChain
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

# Create specialized chains for different tasks

# Quiz Chain
quiz_template= PromptTemplate(
  input_variables=["topic", "conversation_history"],
  template="""Based on this conversation about {topic}:
{conversation_history}

Create 3 quiz questions that test understadning of the key concepts discussed.
Format:
Q1: [question
Q2: [question]
Q3: [question]

Quiz Questions:"""
)

quiz_chain = LLMChain(llm=llm, prompt=quiz_template)

# Explanation Chain
explain_template = PromptTemplate(
  input_variables=["topic"],
  template="""Explain {topic} in the simple terms for a student.

  Include:
  1. Simple definition
  2. Real-world example
  3. Why it's important

  Explanation:"""
  )

explain_chain = LLMChain(llm=llm, prompt=explain_template)

def process_special_commands(user_input):
  """Handle special commands like 'quiz me' and 'explain [topic]'."""

  # Quiz Command
  if "quiz me" in user_input.lower():
    #Extract what they want to be quizzed on from memory
    history = memory.buffer

    # Get the last mentioned topic (simple approach)
    response = quiz_chain.invoke({
      "topic": "the subject we've discussed",
      "conversation_history": history[-500:]  # Last 500 chars
    })

    return response["text"]

  # Explain command
  elif user_input.lower().startswith("explain "):
    topic = user_input[8:].strip() # Remove "explain " prefix

    response = explain_chain.invoke({"topic": topic})
    return response["text"]

  # Regular conversation
  else:
    return None

# Update the main() function
def main():
  print("💬 Start chatting! (Type 'exit' to quit)\n")

  while True:
    user_input = input("🧐You: ").strip()

    if user_input.lower() in ['exit', 'quit', 'bye']:
       print("\n👋 Good luck with your studies!")
       print("\n📊 Session Summary:")
       print(f"Conversation history:\n{memory.buffer[:200]}...")
       break

    if not user_input:
        continue

    try:
      # Check for special commands first
      special_response = process_special_commands(user_input)

      if special_response:
        print(f"🤖 Study Assistant: {special_response}\n")
      else:
        # Regular conversation with memory
        response = chat_with_assistant(user_input)
        print(f"🤖 Study Assistant: {response}\n")

    except Exception as e:
        print(f"❌ Error: {e}")
        print("Please try again.\n")

if __name__ == "__main__":
  main()
