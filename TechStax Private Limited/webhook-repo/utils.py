from datetime import datetime

def format_utc(iso_timestamp):
    dt = datetime.fromisoformat(iso_timestamp)
    return dt.strftime("%d %B %Y - %I:%M %p UTC")
