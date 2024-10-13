
def no_space(text):
    nuevo_text=""
    for char in text:
        if char !=" ":
            nuevo_text+=char
    return nuevo_text

def reverse(text):
    text_reverse=""
    for char in text:
        text_reverse =char + text_reverse
    return text_reverse

def palindromo(text):
    text =no_space(text)
    text_reverse = reverse(text)
    return text == text_reverse

print(palindromo("adda cancion"))