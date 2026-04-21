appointments = []

def check_availability(doctor, date):
    all_slots = ["10:00 AM", "2:00 PM", "4:00 PM"]

    booked = [
        a["time"] for a in appointments
        if a["doctor"] == doctor and a["date"] == date
    ]

    return [s for s in all_slots if s not in booked]


def book_appointment(doctor, date, time):
    for a in appointments:
        if a["doctor"] == doctor and a["date"] == date and a["time"] == time:
            return None

    appointment = {
        "doctor": doctor,
        "date": date,
        "time": time
    }

    appointments.append(appointment)
    return appointment