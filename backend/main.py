from fastapi import FastAPI
from agent import process_query
from scheduler import check_availability, book_appointment
from memory import get_session, set_session
from services.language import detect_language, get_response
from services.speech_to_text import transcribe_audio
from services.text_to_speech import speak_text

app = FastAPI()

@app.post("/query")
def handle_query(data: dict):
    user_input = data.get("text")

    session_id = "123"

    # 🌍 Detect language
    lang = detect_language(user_input)

    session = get_session(session_id)

    agent_response = process_query(user_input)

    intent = agent_response.get("intent") or session.get("intent")
    doctor = agent_response.get("doctor") or session.get("doctor")
    date = agent_response.get("date") or session.get("date")
    time = agent_response.get("time") or session.get("time")

    # 🧠 Save session
    set_session(session_id, {
        "intent": intent,
        "doctor": doctor,
        "date": date,
        "time": time,
        "lang": lang
    })

    # 🟢 Conversation flow
    if not doctor:
        return {"message": get_response("ask_doctor", lang)}

    if not date:
        return {"message": get_response("ask_date", lang)}

    if not time:
        slots = check_availability(doctor, date)
        return {
            "message": get_response("ask_time", lang),
            "available_slots": slots
        }

    appointment = book_appointment(doctor, date, time)

    if appointment is None:
        slots = check_availability(doctor, date)
        return {
            "message": "Slot already booked",
            "available_slots": slots
        }

    return {
        "message": get_response("success", lang),
        "appointment": appointment
    }


# 🎤 Voice endpoint
@app.post("/voice")
def voice_query():
    audio_path = "input.wav"

    user_text = transcribe_audio(audio_path)
    print("User said:", user_text)

    response = handle_query({"text": user_text})

    speak_text(response["message"])

    return {
        "user_text": user_text,
        "response": response
    }