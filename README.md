# Emerald Unicorn - AI-Powered Discord Bot

Emerald Unicorn is a friendly and intelligent AI assistant integrated into Discord. It can chat with users, analyze uploaded images using vision AI, and respond contextually. The bot uses Groq's LLaMA 3 for natural conversation and Google's Gemini 1.5 for image understanding.

## Features
- **Conversational Chatbot** with a warm, human-like tone
- **Image Understanding** using Gemini 1.5
- **Real-time Interaction** with Discord users
- **Dynamic Context Switching**
- **Simple Reset Command** to refresh the conversation

---

## Tech Stack
- Python
- Discord.py
- Groq (LLaMA 3)
- Google Gemini API
- PIL (Pillow)

---

## Prerequisites
- Python 3.8+
- Google Gemini API Key
- Groq API Key
- Discord Developer Account

---

## Setup Guide

### 1. Clone the Repository
```bash
https://github.com/yourusername/emerald-unicorn-bot.git
cd emerald-unicorn-bot
```

### 2. Install Requirements
```bash
pip install -r requirements.txt
```
Packages needed:
```bash
pip install discord.py google-generativeai pillow groq
```

### 3. Set Up Environment Variables (Optional but recommended)
You can hardcode your API keys or set them as environment variables:
```bash
export GROQ_API_KEY='your_groq_api_key'
export GEMINI_API_KEY='your_gemini_api_key'
export DISCORD_BOT_TOKEN='your_discord_token'
```

Update in the code:
```python
groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
bot.run(os.getenv("DISCORD_BOT_TOKEN"))
```

---

## How to Create and Add the Bot to Your Discord Server

### Step 1: Create a Bot on Discord Developer Portal
1. Go to [Discord Developer Portal](https://discord.com/developers/applications)
2. Click on **New Application**
3. Give your app a name (e.g., *Emerald Unicorn*) and create it
4. Go to **Bot** tab > Click on **Add Bot** > Confirm
5. Under **Bot Token**, click **Reset Token** and copy it (save securely)

### Step 2: Enable Privileged Intents
- Under the **Bot** settings:
  - Enable `MESSAGE CONTENT INTENT`

### Step 3: Invite Bot to Your Server
1. Go to **OAuth2 > URL Generator**
2. Select:
   - **scopes**: `bot`
   - **bot permissions**: `Send Messages`, `Read Message History`, `Attach Files`
3. Copy the generated URL and open it in your browser
4. Choose your server and authorize the bot

---

## How to Run the Bot
```bash
python bot.py
```
Once the bot is running, you will see:
```
Emerald Unicorn#0000 has connected to Discord!
```

---

## Bot Commands
- `!chat <message>` - Start a conversation with Emerald Unicorn
- `!detect <question>` - Ask a question about the last uploaded image
- `!reset` - Resets the chat history for a fresh start

---

## Using the Image Analysis Feature
1. Upload an image to the chat
2. Use `!detect <your question>` command
   - Example: `!detect What is in this image?`

---

## Contribution
Feel free to fork and improve. Pull requests are welcome!


---

## Author
Made with ❤️ by Debanga Dutta - "Emerald Unicorn"
