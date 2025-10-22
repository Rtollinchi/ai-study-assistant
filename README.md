# AI Study Assistant

An intelligent study companion leveraging AI/NLP technologies and LangChain to provide personalized learning support, interactive quizzes, and detailed explanations for students across any subject.

## 🌟 Features

- **Conversational Learning**: Natural chat interface for studying any subject
- **Conversation Memory**: Remembers context across the entire study session
- **Interactive Quizzes**: Generate custom quiz questions based on your study topics
- **Detailed Explanations**: Get simple, clear explanations with real-world examples
- **Teaching Persona**: Patient, encouraging AI tutor designed for effective learning
- **Session Summaries**: Review your study session and conversation history

## 🎓 Why This Project?

This AI Study Assistant demonstrates practical application of:
- **LangChain Framework** for building conversational AI
- **Memory Management** for context-aware conversations
- **Chain Orchestration** with specialized chains for different tasks
- **Prompt Engineering** for educational effectiveness

## 🛠️ Technologies Used

- **Python 3.7+**
- **OpenAI GPT-3.5-turbo API** - Conversational AI model
- **LangChain** - Framework for building AI applications
- **LangChain Memory** - Conversation history management
- **Python-dotenv** - Environment variable management

## 📋 Prerequisites

Before you begin, ensure you have:

- Python 3.7 or higher installed
- An OpenAI API key ([Get one here](https://platform.openai.com/api-keys))
- pip package manager
- Basic command line knowledge

## 🔧 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Rtollinchi/ai-study-assistant.git
   cd ai-study-assistant
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**

   Create a `.env` file in the root directory:
   ```bash
   touch .env
   ```

   Add your OpenAI API key:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## 🎮 Usage

1. **Run the application**
   ```bash
   python app.py
   ```

2. **Start studying**

   The assistant will greet you and wait for your input.

### Available Commands

- **Natural Conversation**: Just chat about what you're studying
  ```
  You: Can you help me understand photosynthesis?
  ```

- **Quiz Mode**: Test your understanding
  ```
  You: quiz me
  ```

- **Detailed Explanations**: Get in-depth explanations
  ```
  You: explain photosynthesis
  ```

- **Exit**: End your study session
  ```
  You: exit
  ```

## 💡 Example Study Session

```
🎓 Welcome to Your AI Study Assistant!
========================================
I can help you study any subject!
Commands:
  - Just chat naturally about what you're studying
  - Type 'quiz me' to get quiz questions
  - Type 'explain [topic]' for detailed explanations
  - Type 'exit' to quit
============================================================

✅ Study Assistant initialized with memory!

🧐 You: I'm studying the water cycle for my science test

🤖 Study Assistant: Great! The water cycle is a fundamental concept in Earth science.
Let me help you understand it better. The water cycle describes how water moves
between Earth's surface and the atmosphere through evaporation, condensation,
and precipitation...

🧐 You: quiz me

🤖 Study Assistant:
Q1: What are the three main processes in the water cycle?
Q2: What happens to water during evaporation?
Q3: Where does condensation occur in the water cycle?

🧐 You: exit

👋 Good luck with your studies!

📊 Session Summary:
Conversation history:
[Your study session summary...]
```

## 🏗️ Technical Architecture

### Core Components

1. **ConversationChain**: Main conversation handler with memory
2. **Memory System**: Tracks conversation history for context
3. **Specialized Chains**:
   - **Quiz Chain**: Generates relevant quiz questions
   - **Explanation Chain**: Provides detailed topic explanations
4. **Command Processor**: Handles special commands and routing

### Key Features

- **Temperature Setting (0.7)**: Balanced between creativity and accuracy
- **Token Limit (300)**: Optimized for concise, focused responses
- **Context Preservation**: Maintains full conversation history
- **Error Handling**: Graceful error management with user feedback

## 📁 Project Structure

```
ai-study-assistant/
├── app.py                 # Main application file
├── requirements.txt       # Python dependencies
├── .env                  # Environment variables (not in repo)
├── .gitignore           # Git ignore file
└── README.md            # This file
```

## 🔐 Security Note

**Important**: Never commit your `.env` file or expose your OpenAI API key. The `.gitignore` file should include:

```
.env
__pycache__/
*.pyc
.venv/
venv/
```

## 📦 Requirements

Create a `requirements.txt` file with:

```
langchain
langchain-openai
openai
python-dotenv
```

## 🚀 Future Enhancements

Potential improvements for this project:

- [ ] Add Gradio/Streamlit web interface
- [ ] Implement topic-specific study plans
- [ ] Add flashcard generation
- [ ] Include progress tracking and analytics
- [ ] Support multiple languages
- [ ] Add voice input/output capabilities
- [ ] Integrate with note-taking apps

## 👤 Author

**Rubin Tollinchi**

- GitHub: [@Rtollinchi](https://github.com/Rtollinchi)
- LinkedIn: [Your LinkedIn](https://www.linkedin.com/in/rubintollinchi/)
- Portfolio: [Your Website](https://rubintollinchi.info/)

## 🙏 Acknowledgments

- OpenAI for providing the GPT-3.5-turbo API
- LangChain team for the excellent AI framework
- The education technology community

## 📚 Learning Resources

If you're interested in building similar projects:

- [LangChain Documentation](https://python.langchain.com/docs/get_started/introduction)
- [OpenAI API Documentation](https://platform.openai.com/docs/introduction)
- [Prompt Engineering Guide](https://www.promptingguide.ai/)

## 📞 Support

If you have any questions or run into issues, please open an issue in the GitHub repository.

---

⭐ If you found this project helpful for learning, please consider giving it a star!
