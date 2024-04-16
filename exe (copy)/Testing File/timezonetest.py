from datetime import datetime, timezone, timedelta

a = "Tue, 16 Apr 2024 10:08:11 +0800" # 2024-04-16 00:41:57.104089+00:00, Tue, 16 Apr 2024 00:46:36 +0000
b = "Tue, 16 Apr 2024 02:08:11 +0000"
c = "Tue, 16 Apr 2024 02:08:11 GMT"
d = c.replace("GMT", "+0000")

a_fm = datetime.strptime(a,"%a, %d %b %Y %H:%M:%S %z")
b_fm = datetime.strptime(b,"%a, %d %b %Y %H:%M:%S %z")
c_fm = datetime.strptime(d,"%a, %d %b %Y %H:%M:%S %z")

print(datetime.now(timezone.utc))

print(a_fm)
print(b_fm)
print(c_fm)

print(b_fm-a_fm)
print(c_fm-a_fm)
