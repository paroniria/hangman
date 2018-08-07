def hangman():
    word = 'caat'
    stage = 0
    wrong_guesses = ['','_________    ','|     |   ','|     0',
    '|    /|\      ','|    / \     ','|        ']
    letters_left = list(word)
    score_board = ['_']* len(word)
    win = False
    print('Welcome to Hang Man')
    for i in wrong_guesses:
        print(i)
    while stage < len(wrong_guesses)-1:
        print('\n')
        guess = input('Guess a letter')
        if guess in letters_left:
            score_board[letters_left.index(guess)] = guess
            letters_left[letters_left.index(guess)] = '$'
        else:
            stage += 1
        print(''.join(score_board))
        print('\n'.join(wrong_guesses[0:stage+1]))
        if '_' not in score_board:
            print('You win! The word is ')
            print(''.join(score_board))
            win = True
            break
    if not win:
        print('\n'.join(wrong_guesses[0:stage]))
        print('You lose')


hangman()