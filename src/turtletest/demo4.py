text = input()
result = ""
for ch in text:
    if 'a' <= ch <= 'z':
        print(str(ord(ch)) + " ==>> " + chr(ord(ch) + 3));
        result += chr((ord(ch) + 3) % 26)
    elif 'A' <= ch <= 'Z':
        result += chr((ord(ch) + 3) % 26)
    else:
        result += ch
print(result)