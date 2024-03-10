def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":(": "🙁",
        ":)": "🙂"
    }

    new_message = ""
    for word in words:
        new_message += emojis.get(word, word) + " "

    return new_message

message = input("Enter message here: ")
print(emoji_converter(message))