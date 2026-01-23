def encryption(language_lower, language_upper, step_shift):
    n = len(language_lower)
    line = input("Напишите предложение для шифрование: ")
    new_line = ""
    for i in line:
        if not (i.isalpha()):
            new_line += i

        elif i.isupper():
            if language_upper.find(i) + step_shift > n:
                new_line += language_upper[language_upper.find(i) + step_shift - n]
            else:
                new_line += language_upper[language_upper.find(i) + step_shift]
        else:
            if language_lower.find(i) + step_shift > n:
                new_line += language_lower[language_lower.find(i) + step_shift - n]
            else:
                new_line += language_lower[language_lower.find(i) + step_shift]
    print(new_line)


def decryption(language_lower, language_upper, step_shift):
    n = len(language_lower)
    line = input("Напишите предложение для шифрование: ")
    new_line = ""
    for i in line:
        if not (i.isalpha()):
            new_line += i

        elif i.isupper():
            if language_upper.find(i) - step_shift < 0:
                new_line += language_upper[n + (language_upper.find(i) - step_shift)]
            else:
                new_line += language_upper[language_upper.find(i) - step_shift]
        else:
            if language_lower.find(i) - step_shift < 0:
                new_line += language_lower[n + (language_lower.find(i) - step_shift)]
            else:
                new_line += language_lower[language_lower.find(i) - step_shift]
    print(new_line)


route = input("Шифрование или дешифрование (ш = шифрование д = дешифрование): ")
language = input("Русский или английский (рус = русский язык анг = английский): ")
step_shift = int(input("Наскойлько сдвиг: "))
eng_lower_alphabet = "abcdefghijklmnopqrstuvwxyz"
eng_upper_alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
rus_lower_alphabet = "абвгдежзийклмнопрстуфхцчшщъыьэюя"
rus_upper_alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
if route == "ш":
    if language == "рус":
        encryption(rus_lower_alphabet, rus_upper_alphabet, step_shift)
    elif language == "анг":
        encryption(eng_lower_alphabet, eng_upper_alphabet, step_shift)

elif route == "д":
    if language == "рус":
        decryption(rus_lower_alphabet, rus_upper_alphabet, step_shift)
    elif language == "анг":
        decryption(eng_lower_alphabet, eng_upper_alphabet, step_shift)
