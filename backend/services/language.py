from langdetect import detect

def detect_language(text):
    try:
        return detect(text)
    except:
        return "en"

def get_response(key, lang):
    responses = {
        "ask_doctor": {
            "en": "Which doctor do you want?",
            "hi": "आप किस डॉक्टर से मिलना चाहते हैं?",
            "ta": "நீங்கள் எந்த மருத்துவரை பார்க்க விரும்புகிறீர்கள்?"
        },
        "ask_date": {
            "en": "Which date?",
            "hi": "कौन सी तारीख?",
            "ta": "எந்த தேதி?"
        },
        "ask_time": {
            "en": "Choose a time slot",
            "hi": "समय चुनें",
            "ta": "நேரத்தை தேர்வு செய்யவும்"
        },
        "success": {
            "en": "Appointment booked successfully",
            "hi": "अपॉइंटमेंट बुक हो गया",
            "ta": "நியமனம் பதிவு செய்யப்பட்டது"
        }
    }

    return responses.get(key, {}).get(lang, responses[key]["en"])