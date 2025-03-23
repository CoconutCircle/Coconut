import uuid

# ID generation functions
def generate_user_id() -> str:
    return "u" + str(uuid.uuid4())

def generate_trip_id() -> str:
    return "trip" + str(uuid.uuid4())

def generate_trip_member_id() -> str:
    return "tm" + str(uuid.uuid4())

def generate_itinerary_id() -> str:
    return "it" + str(uuid.uuid4())

def generate_expense_id() -> str:
    return "ex" + str(uuid.uuid4())

def generate_media_id() -> str:
    return "me" + str(uuid.uuid4())

def generate_chat_id() -> str:
    return "msg" + str(uuid.uuid4())

def generate_friendship_id() -> str:
    return "f" + str(uuid.uuid4())

def generate_invite_id() -> str:
    return "tinv" + str(uuid.uuid4())

def generate_usertrip_id() -> str:
    return "ut" + str(uuid.uuid4())