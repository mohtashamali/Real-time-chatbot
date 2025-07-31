# 🤖 AI Agent – Your Voice-Driven, Camera-Aware Chat Assistan
An intelligent AI-powered assistant that listens to your voice via microphone, watches via webcam, and responds using a powerful LLM backend. This project uses **Groq + Claude + LangChain + LangGraph**, integrates with **Gradio** for UI, and speaks responses using **gTTS (Google Text-to-Speech)**.

---

## 🔥 Features

- 🎤 **Voice Input** using `SpeechRecognition` and `pydub`
- 💬 **Natural Language Understanding** powered by **Groq LLMs** (e.g. LLaMA, Mixtral)
- 🧠 **LangChain + LangGraph** for memory and tool-driven reasoning
- 🎥 **Camera Feed** with `OpenCV` in Gradio
- 🔊 **Voice Output** with `gTTS` (Google Text-to-Speech)
- 🖥️ **Interactive Gradio Interface**
- 🤖 Modular agent behavior with Claude, Groq, and LangChain tools
- 🌿This project runs in a [UV] environment for lightweight and fast Python package management.

---

## 📁 Modules Overview

| Module | Purpose |
|--------|---------|
| `user_voice.py` | Records audio from microphone and transcribes using Groq |
| `response_voice.py` | Converts AI response to speech using gTTS |
| `ai_agent.py` | Handles agent response via LangChain / Claude / Groq |
| `main.py` | Runs the Gradio interface, integrates all components |


---
<!-- USE THE command for run of the program : uv run main.py -->