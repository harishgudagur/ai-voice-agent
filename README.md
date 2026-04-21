# 🎤 Real-Time Multilingual Voice AI Agent (Healthcare)

## 🚀 Overview

This project implements a **real-time voice AI agent** for clinical appointment booking.
The system supports **natural voice conversations**, multilingual interaction (English, Hindi, Tamil), and handles the full appointment lifecycle including booking, rescheduling, and conflict resolution.

---

## 🎯 Key Features

### 🧠 AI Agent

* Extracts intent using LLM (Groq - LLaMA 3.1)
* Supports booking, rescheduling, cancellation
* Handles incomplete and noisy input

### 🎤 Voice Interface

* Speech-to-Text: Faster Whisper
* Text-to-Speech: pyttsx3
* End-to-end voice conversation support

### 🌍 Multilingual Support

* Language detection (English, Hindi, Tamil)
* Language-aware responses
* Context maintained across turns

### 🧩 Conversational Memory

* Session-based memory (in-memory / Redis-ready)
* Multi-turn conversations supported

### 📅 Scheduling System

* Slot availability checking
* Conflict detection (no double booking)
* Alternative slot suggestions

---

## ⚙️ Tech Stack

* Backend: FastAPI (Python)
* AI Model: Groq (LLaMA 3.1)
* STT: Faster Whisper
* TTS: pyttsx3
* Memory: In-memory (Redis-ready design)
* Language Detection: langdetect

---

## 🏗️ Architecture

```
Voice Input
   ↓
Speech-to-Text (Whisper)
   ↓
AI Agent (Groq LLM)
   ↓
Intent + Entity Extraction
   ↓
Scheduler Logic
   ↓
Response Generation
   ↓
Text-to-Speech
```

---

## ⚡ Latency Breakdown

| Component     | Time        |
| ------------- | ----------- |
| STT (Whisper) | ~150–250 ms |
| LLM (Groq)    | ~100–150 ms |
| Logic + API   | ~50 ms      |
| TTS           | ~100 ms     |

👉 Total: **~350–450 ms**

---

## 🧪 API Endpoints

### `/query`

Text-based interaction

```json
{
  "text": "Book appointment with dentist tomorrow"
}
```

---

### `/voice`

Voice-based interaction

* Uses `input.wav`
* Converts speech → response → speech

---

## 🧠 Design Decisions

* Used Groq for **low latency inference**
* Modular architecture (agent, scheduler, memory)
* Stateless API with optional Redis memory
* Conversational fallback for missing info

---

## ⚠️ Known Limitations

* Whisper base model may mishear noisy speech
* Fixed slot system (can be extended)
* No real database (in-memory used)

---

## 🚀 Future Improvements

* Live microphone input
* Database integration
* Real-time streaming (WebSockets)
* Advanced multilingual translation

---

## 🎉 Conclusion

This system demonstrates:

* Real-time AI reasoning
* Voice interaction
* Multilingual support
* Robust conversational handling

👉 Designed with **low latency and modular architecture**.
