from fastapi import FastAPI
from agent import process_query
from scheduler import check_availability, book_appointment
from memory import get_session, set_session
from services.language import detect_language, get_response

app = FastAPI()


@app.get("/")
def health():
    return {"message": "Voice AI Agent Running 🚀"}


@app.post("/query")
def handle_query(data: dict):
    user_input = data.get("text")

    session_id = "123"  # static session (can improve later)

    # Detect language
    lang = detect_language(user_input)

    # Load previous session
    session = get_session(session_id)

    agent_response = process_query(user_input)

    # Extract values (fallback to session memory)
    intent = agent_response.get("intent") or session.get("intent")
    doctor = agent_response.get("doctor") or session.get("doctor")
    date = agent_response.get("date") or session.get("date")
    time = agent_response.get("time") or session.get("time")

    #  Save updated session
    set_session(session_id, {
        "intent": intent,
        "doctor": doctor,
        "date": date,
        "time": time,
        "lang": lang
    })

    # Conversation Flow

    # Ask for doctor
    if not doctor:
        return {"message": get_response("ask_doctor", lang)}

    # Ask for date
    if not date:
        return {"message": get_response("ask_date", lang)}

    # Ask for time
    if not time:
        slots = check_availability(doctor, date)
        return {
            "message": get_response("ask_time", lang),
            "available_slots": slots
        }

    # Try booking
    appointment = book_appointment(doctor, date, time)

    # Handle conflict
    if appointment is None:
        slots = check_availability(doctor, date)
        return {
            "message": "Slot already booked. Choose another time.",
            "available_slots": slots
        }

    # Success
    return {
        "message": get_response("success", lang),
        "appointment": appointment
    }