# یک رشته را از کاربر بگیرید و تعداد جملات، تعداد کلمات، تعداد کل کارکترها و تعداد حروف انگلیسی را چاپ کند
s = input("Enter string: ")
sentences = s.count(".") + s.count("?") + s.count("!")
words = s.count(" ") + 1
characters = len(s)
letters = characters - (s.count(".") + s.count("?") + s.count("!") + s.count(";") + s.count(":") + s.count("-") + s.count(" "))
print("number of sentences: ", sentences)
print("number of words: ", words)
print("number of characters: ", characters)
print("number of letters: ", letters)
# یک کارکتر از کاربر بگیرید و یونیکد آن را چاپ کنید
char = input("Enter char: ")
print(ord(char))