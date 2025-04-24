from datetime import datetime

def generate_time_key():
    now = datetime.utcnow()
    return now.strftime("%Y%m%d%H")

def is_valid_key(key):
    return key == generate_time_key()