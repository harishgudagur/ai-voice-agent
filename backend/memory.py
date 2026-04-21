session_store = {}

def set_session(session_id, data):
    session_store[session_id] = data

def get_session(session_id):
    return session_store.get(session_id, {})