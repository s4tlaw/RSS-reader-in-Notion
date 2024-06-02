from datetime import datetime


def check_published_format(entry):
    format1 = "%a, %d %b %Y %H:%M:%S %z"
    #format2 = "%a, %d %b %Y %H:%M:%S %Z"

    try:
        datetime.strptime(entry, format1)
        return entry
    except ValueError:
        if entry.find("GMT") != -1:

            entry = entry.replace("GMT", "+0000")
        elif entry.find("EST") != -1:

            entry = entry.replace("EST", "-0400")
        elif is_iso_date(entry) is True:

            entry = datetime.fromisoformat(entry)
            entry = entry.strftime("%a, %d %b %Y %H:%M:%S %z")
        return entry


def is_iso_date(date_string):
    try:
        datetime.fromisoformat(date_string)
        return True
    except ValueError:
        return False

