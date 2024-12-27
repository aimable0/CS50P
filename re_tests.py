import re

email = input("What's your email? ").strip()

if re.search(r"\w+@(\w+\.)?\w+\.(edu|gov|rw|net|org|com)", email, re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")

# match's pattern starts "matching" at the beginning of a given text
# returns something like <re.Match object; span=(0, 7), match='aimable'> or none
print(re.match(r"aimable", "aaimablenkurikiye"))

# fullmatch matches from the beginning to the end
# returns something like <re.Match object; span=(0, 7), match='aimable'> or none
print(re.fullmatch(r"aimable", "aimable"))