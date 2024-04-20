import re


text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

email_pattern = r"\b[A-Za-z0-9._%+-]+@(?!exclude\.com)\w+\.\w+\b"

matches = re.findall(email_pattern,text)

print(matches)

