# Tiny Chatbot with Memory 🤖

A simple chatbot that remembers your last input and can reference it in future responses!

## 🎯 What This Script Does

This Python script creates an interactive chatbot with memory capabilities. It remembers what you said previously and can reference it when you ask, creating a more natural conversational experience. Perfect for learning about basic AI concepts and conversation management!

## ✨ Features

- **No External Dependencies**: Uses only Python's standard library (`random`, `re`)
- **Memory System**: Remembers your last input and references it
- **Intent Detection**: Recognizes greetings, farewells, thanks, and memory queries
- **Pattern Matching**: Uses regex for intelligent response selection
- **Conversation Counter**: Tracks number of exchanges
- **Natural Responses**: Varied responses prevent repetition

## 🚀 Usage

Simply run the script:
```bash
python tiny_chatbot_memory.py
```

The chatbot will start and you can begin chatting immediately!

## 💡 Example Conversation

```bash
python tiny_chatbot_memory.py
```

**Output:**
```
============================================================
🤖 Tiny Chatbot with Memory 🤖
============================================================

I remember what you say! Try asking me to recall it later.
Type 'bye' or 'quit' to exit.

You: Hello!
Bot: Hi there! What's on your mind?

You: I love programming in Python
Bot: That's interesting! Tell me more.

You: Do you remember what I said?
Bot: Earlier you mentioned 'I love programming in Python'. Tell me more about that!

You: Thanks for remembering!
Bot: You're welcome!

You: Bye
Bot: Goodbye! Have a great day!

We had 5 exchanges. Thanks for chatting!
```

## 🧠 How Memory Works

The chatbot stores your last input in memory. When you use trigger words like:
- "remember"
- "earlier"
- "before"
- "previous"
- "you said"

The bot will recall and reference what you previously said!

## 🎭 Intent Categories

### 1. Greeting
**Triggers**: hello, hi, hey, greetings  
**Responses**: Friendly welcomes

### 2. Farewell
**Triggers**: bye, goodbye, see you, farewell, exit, quit  
**Responses**: Polite goodbyes (also exits the program)

### 3. Thanks
**Triggers**: thanks, thank you, thx, appreciate  
**Responses**: Acknowledgments

### 4. Memory Recall
**Triggers**: remember, earlier, before, previous, you said  
**Responses**: References your last input

### 5. Default
**Triggers**: Everything else  
**Responses**: Encouraging continuation

## 🛠️ How It Works

1. **Initialize**: Creates chatbot with empty memory
2. **User Input**: Receives and processes your message
3. **Intent Detection**: Uses regex to identify what you're asking
4. **Memory Check**: If you ask about previous input, recalls it
5. **Response Generation**: Selects appropriate response template
6. **Store Memory**: Saves your input for next interaction
7. **Loop**: Continues until you say goodbye

## ⚙️ Customization

### Add More Response Types
Edit the `RESPONSES` dictionary:
```python
RESPONSES = {
    'your_intent': [
        "Response 1",
        "Response 2"
    ]
}
```

### Add New Patterns
Update the `PATTERNS` dictionary:
```python
PATTERNS = {
    'your_intent': r'\b(keyword1|keyword2)\b'
}
```

### Extend Memory
Modify the `TinyChatbot` class to store more:
```python
def __init__(self):
    self.last_inputs = []  # Store multiple inputs
    self.conversation_count = 0
```


## 💡 Tips for Better Conversations

- **Be specific**: The more detailed your input, the more interesting the recall!
- **Ask about memory**: Use trigger words to test the memory feature
- **Try variations**: Test different greetings and phrases
- **Keep chatting**: The bot stores your most recent input


## 🎯 Example Use Cases

### Teaching Tool
```
You: I'm learning about functions
Bot: That's interesting! Tell me more.
You: What did I say before?
Bot: Earlier you mentioned 'I'm learning about functions'. Tell me more about that!
```

### Personal Assistant
```
You: I need to buy groceries
Bot: I see. What else is on your mind?
You: Can you remember what I need to do?
Bot: You were talking about 'I need to buy groceries' before. Interesting!
```

## 🤝 Contributing

Issue #838 Tiny Chatbot with Memory

## ⚠️ Note

The chatbot only remembers your **last** input. Each new message overwrites the previous memory. This is intentional to keep the code simple and under 100 lines!
