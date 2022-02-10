                #It's a simple Guessing game engine made with while loop and if, else conditionals.

the_number  = 8
input_count = 0
input_limit = 3
while input_count < input_limit :
    guess = int(input('Guess any number 1-10:   '))
    input_count += 1
    if guess == 8 :
        print("Yeah, You guessed the right number")
        print("You Won !")
        break
else:
    print("Sorry you failed !, Better luck next time !!!")