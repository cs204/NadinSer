text = input("Приветсвие: ")
if "Привет" in text:
    print("100$")
elif "Здравствуйте" in text:
    print("$0")
elif "з" in text:
    print("$20")
else:
    print("$0")