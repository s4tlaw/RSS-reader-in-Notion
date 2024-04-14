from datetime import datetime

def check_published_format(entry):
    format1 = "%a, %d %b %Y %H:%M:%S %z"
    format2 = "%a, %d %b %Y %H:%M:%S %Z"
    #format3 = "%a, %d %b %Y %H:%M:%S %z"

    try:
        datetime.strptime(entry, format1)
        return entry
    except ValueError:
        try:
            datetime.strptime(entry, format2)
            entry_with_offset = entry.replace("GMT", "+0800")  # Adding the UTC offset manually
            return entry_with_offset
        except ValueError:
                yt_entry=datetime.fromisoformat(entry)
                yt_out = yt_entry.strftime("%a, %d %b %Y %H:%M:%S %z")
                return yt_out

