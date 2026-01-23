from random import *

word_list = [
    "КЛЮЧ",
    "КНИГА",
    "ЕНОТ",
    "МАШИНКА",
    "КОРОВА",
    "ТЕЛЕЖКА",
    "ШЛЕМ",
    "КНОПКА",
    "ШНУР",
    "ЧЕРНЫЙ",
    "ВЛАСТЕЛИН",
    "СКАЙП",
    "ДУБ",
    "ЧАСЫ",
    "ТРУБА",
    "ЕЛКА",
    "ИНСТИТУТ",
    "КОРОБКА",
    "ТАБЛИЧКА",
    "ВОДА",
    "СКОВОРОДА",
    "МНОГОНОЖКА",
    "ЕВРЕЙ",
    "ТЕРМИТ",
    "КАЧЕК",
    "РУЛОН",
    "МАГНИТОФОН",
    "НОГА",
    "СЛОН",
    "МИКРОВОЛНОВКА",
    "ТОРТ",
    "МАК",
    "ДЫМ",
    "ЧАЙКА",
    "ВАЛЕТ",
    "ПЛИНТУС",
    "ШАПКА",
    "ДИНОЗАВР",
    "ТОРШЕР",
    "БАЛАЛАЙКА",
    "БАНКА",
    "ЯХТА",
    "ОВЦА",
    "БАНАН",
    "ДУБ",
    "АНИМЕ",
    "РАДУГА",
    "БУКВА",
    "ВЕЛОСИПЕД",
    "БАНДЖО",
    "ГОЛУБЬ",
    "ВИНТОВКА",
    "КУБОК",
    "ЖАСМИН",
    "ТЕЛЕФОН",
    "АНДРОИД",
    "ГОРА",
    "ХАЛАТ",
    "ЖЕТОН",
    "ОБОД",
    "МЫЛО",
    "ЙОГ",
    "ШИШКА",
    "ДОЛЛАР",
    "КОЛОНКА",
    "КУБИК",
    "ОМАР",
    "РАКЕТА",
    "МОРКОВКА",
    "ЗЕРКАЛО",
    "МОЛОТ",
    "ВОЗДУХ",
    "ЗМЕЙ",
    "ЁЖ",
    "ПАЛЬМА",
    "МАСЛО",
    "ДИДЖЕЙ",
    "МЕШОК",
    "ТЮБИК",
    "МОЗГ",
    "ПОЕЗД",
    "РОЗЕТКА",
    "ПАРАШЮТИСТ",
    "БЕЛКА",
    "ШПРОТЫ",
    "САМОСВАЛ",
    "ПАЗЛ",
    "БУТЫЛКА",
    "КРЕМЛЬ",
    "ПИЦЦА",
    "МАКАРОНЫ",
    "КОВЕР",
    "ЗУБЫ",
    "ЯРЛЫК",
    "КАШАЛОТ",
    "МАРС",
    "ШАКАЛ",
    "ПОМАДА",
    "ДЖИП",
    "ЛЕЩ",
    "КАМЕНЬ",
    "ДИСК",
]


def check(word, guessed_letters, guessed_words):
    while not (word.isalpha()):
        if word not in guessed_letters or word not in guessed_words:
            print("Уже было")

        else:
            print("Пожалуста введите букву или слово")

        word = input().upper()

    return word


def get_word():
    return choice(word_list)


def display_hangman(tries):
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
        # голова, торс, обе руки, одна нога
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
        # голова, торс, обе руки
        """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
        # голова, торс и одна рука
        """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
        # голова и торс
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # голова
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # начальное состояние
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    print(stages[tries])


def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print("Давай играть в угадайку слов!")
    display_hangman(tries)
    print(word_completion)

    while tries > 0:
        if word_completion == word:
            guessed = True

        if guessed == False:
            anwser = check(input().upper(), guessed_letters, guessed_words)
            if len(anwser) > 1:
                if anwser == word:
                    display_hangman(tries)
                    print(word)
                    guessed = True

                else:
                    tries -= 1
                    display_hangman(tries)
                    print(word_completion)
                    guessed_words.append(anwser)

            else:
                if anwser in word:
                    guessed_letters.append(anwser)
                    new_word = ""
                    for i in range(len(word)):
                        if anwser == word[i]:
                            new_word += anwser

                        else:
                            new_word += word_completion[i]

                    word_completion = new_word
                    display_hangman(tries)
                    print(word_completion)

                else:
                    guessed_letters.append(anwser)
                    tries -= 1
                    display_hangman(tries)
                    print(word_completion)

        else:
            print("Поздравляем, вы угадали слово! Вы победили!")
            break

    else:
        print(f"Вы проиграли загаданое слово было: {word}")

play(get_word())
while True:
    anwser = input("Хотите сыграть ещё раз (да = д нет = н) ")
    if anwser == "д":
        play(get_word())
        continue

    break
