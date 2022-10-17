import random

with open("word.txt") as f:
    word = list(f.read().split("\n"))

item = 0


def guesstheno(user_message, n, number):
    if (n == 0) and int(user_message) != number:
        return "You Lost :(\nThe number is {}".format(number)
    if int(user_message) == number:
        return "You Won!\nThe number is {}".format(number)
    elif int(user_message) > number:
        return "High"
    return "Low"


def hangman(user_message, m, wordchosen, hangmanword):
    for i in range(0, len(wordchosen)):
        if user_message == wordchosen[i]:
            hangmanword[i] = user_message
    # for word comparison
    hangmanwrd="".join([str(i) for i in hangmanword])
  
    if hangmanwrd == wordchosen:
        return "You Won!\nThe word is {}".format(wordchosen)

    elif (m == 0):
        return "You Lost :(\nThe word is {}".format(wordchosen)

    return str(hangmanword)


def rockpaperscissor(bot_chosen, user_message):
    res = "You win"
    if user_message in ("rock", "paper", "scissor"):
        if user_message == bot_chosen:
            res = "It's a tie"

        elif user_message == "scissor":
            if bot_chosen == "rock":
                res = "You Lost"

        elif user_message == "rock":
            if bot_chosen == "paper":
                res = "You Lost"

        else:
            if bot_chosen == "scissor":
                res = "You Lost"

        return "{}\n{}".format(bot_chosen, res)
    else:
        return "You gave wrong input :( Try again"


def responses(input_text):
    global item
    global n
    global number
    global wordchosen
    global hangmanword
    global m
    user_message = str(input_text).lower()

    if user_message.split()[0] in ("hello", "hey", "hi", "sup"):
        return "Hi, I am Gamer Bot.\n Type 'game' to start the new game"

    if user_message == "game":
        item = 0
        return """You can only play the game once!
To restart the game or play a new game
Type your response:
    rock paper scissor
    hangman 
    guess the number
    """
    if user_message == "rock paper scissor":
        item = 1
        return """Type your response:
    rock
    paper
    scissor
    """
    if user_message == "hangman":
        item = 2
        wordchosen = random.choice(word)
        hangmanword = list('*' * len(wordchosen))
        m = len(wordchosen) + 5
        return "You will be given the length of the word +5 chances to guess the word correctly! Only enter letter\n Your word is {}".format(str(hangmanword))

    if user_message == "guess the number":
        item = 3
        number = random.randint(0, 100)
        n = 5
        return "You will be given 5 chances to guess the number correctly. Hint: The number lies between 0 and 100."

    if item == 1:
        l = ['rock', 'paper', 'scissor']
        bot_chosen = l[random.randint(0, 2)]
        item = 0
        return rockpaperscissor(bot_chosen, user_message)

    if item == 2:
        if (user_message.isalpha() and (len(user_message) == 1)):
            while (m > 0):
                m -= 1
                respnse = hangman(user_message, m, wordchosen, hangmanword)
                if "You Won!" in respnse:
                    m = 0
                return respnse
        else:
            return "Enter only character !"

        if (m == 0):
            item = 0

    if item == 3:
        while (n > 0):
            n -= 1
            return guesstheno(user_message, n, number)
        if (n == 0):
            item = 0

    if item == 0:
        return "Enter the name of the game correctly !"
