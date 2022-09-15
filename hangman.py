import random

def checkWord(word):
    guessed = []
    numTrys = 8
    oString = []
    gotem = len(word)
    alpha = 'A B C D E F G H\nI J K L M N O P\nQ R S T U V W X Y Z\n'
    word = word.upper()

    for i in word:
        oString.append(' _ ')

    while gotem != 0 and numTrys > 0:
        print(''.join(oString) + '\n' + alpha)
        guess = input('Enter a letter guess: ')
        guess = guess.upper()
        alpha = alpha.replace(guess, '_')

        if guess in word:
            numApps = 0
            word2 = word
            for i in word2:
                if i == guess:
                    j = word2.index(guess)
                    oString[j] = ' ' + guess + ' '
                    word2 = word2.replace(word[j], '-', 1)
                    numApps += 1
            if gotem == 1:
                print('Good job, you won!\n')
                print(''.join(oString) + '\n' + alpha)
            gotem -= numApps

        else:
            if guess in guessed:
                print('You already guessed that letter!')

            elif numTrys == 1:
                print('Out of guesses. Game over!')

                for i in range(len(oString)):
                    oString[i] = ' ' + word[i] + ' '

                print(''.join(oString) + '\n' + alpha)
                numTrys -= 1

            else:
                print('Incorrect, try again.')
                numTrys -= 1
            guessed.append(guess)


if __name__ == '__main__':
    doc = open('Words.rtf', 'r')

    words = []

    for i in doc:
        if '\n' in i:
            i = i.replace('\n', '')
        words.append(i)

    index = random.randrange(6)

    word = words[index]

    checkWord(word)

    doc.close()