# RAG Chatbot - Text to Speech

## 📌 Overview
This **RAG (Retrieval-Augmented Generation) Chatbot** enhances chatbot responses by retrieving relevant information before generating an answer. It integrates **text-to-speech (TTS)** to convert responses into audio, making interactions more engaging.

## 🚀 Features
- **Retrieval-Augmented Generation**: Fetches relevant data before generating responses.
- **LLM Integration**: Uses OpenAI's GPT models for intelligent conversations.
- **Text-to-Speech (TTS)**: Converts chatbot responses into speech using elevenlabs tts model.
- **Streaming Responses**: Provides real-time response generation.
- **Gradio UI**: Simple and interactive web interface.

## 🛠️ Installation
### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-repo/rag-chatbot.git
cd rag-chatbot
```
### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate    # On Windows
```
### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables
Set up your API keys in an `.env` file:
```
OPENAI_API_KEY=your_openai_api_key
```

## 🎙️ How to Run the Chatbot
```bash
python app.py
```
Then, open **http://127.0.0.1:7860/** in your browser to chat with the bot.

## ⚙️ How It Works
1️⃣ User inputs a query via the **Gradio UI**.
2️⃣ The chatbot retrieves relevant data using **RAG**.
3️⃣ The **LLM generates a response**.
4️⃣ The response is **streamed** in real-time.
5️⃣ The chatbot converts text into **speech using OpenAI’s TTS API**.
6️⃣ The audio is played directly without saving it.

## 🔧 Troubleshooting
- If the app crashes after one response, **check the logs** by running:
  ```bash
  python app.py --debug
  ```
- If `playsound` fails to install, use `pydub` with `ffmpeg` instead:
  ```bash
  pip install pydub
  ```
  Ensure `ffmpeg` is installed on your system.
  ffpeg download link : https://ffmpeg.org/download.html

  Installation Steps
   1. Windows
   2.  Download the latest Windows build from Gyan.dev.

    Extract the folder and add the bin directory to the system PATH variable.

## 📜 License
This project is licensed under the **MIT License**.

---
Made with ❤️ by Aviral

