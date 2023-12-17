#1
p = input("Введіть слово : ")
p.lower()
p1 = p[::-1]
if p == p1:
    print("Слово є паліндромом")
else:
    print("Слово не є паліндромом")

#2
user_text = input("Введіть текст: ")
reserved_words = input("Введіть список зарезервованих слів через пробіл: ")
reserved_words1 = reserved_words.split()
def change_case(text, reserved_words1):
    words = text.split()
    for i in range(len(words)):
        word = words[i].lower()  
        if word in reserved_words1:
            words[i] = words[i].upper()
    modified_text = ' '.join(words)
    return modified_text
modified_text = change_case(user_text, reserved_words1)
print(modified_text)

#3
text1 = input("Введіть текст : ")
print(text1.count("."))