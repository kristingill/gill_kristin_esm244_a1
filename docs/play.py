def play():
  name = input("What's your name?")
  print("Hi " + name + " let's play some hangman!")

  import random
  f = open("words_alpha.txt", "r")
  text = f.read()
  words = text.split()
  num_words = len(words)
  random_index = random.randint(0, num_words-1)
  random_word = random.choice(words)
  f.close()
  num_letters = len(random_word)
  letters = list(random_word)
  print("The number of letters in the phrase is " + str(num_letters) + ".")
  print("""
          |-------|
          |
          |
          |
       __ |__
       """)
  blanks = "_ " * num_letters
  print(blanks)
  
  guess_remain = 6
  response_list = []
  
  while guess_remain > 0:
    remain = "Guesses remaining: " + str(guess_remain)
    print(remain)
    guess = input("Guess a letter!")
    
    if not guess.isalpha():
      print("This is not a letter.")
    
    if guess in response_list:
      print("You already guessed that!")
    
    if guess not in letters:
      if guess.isalpha():
        if guess not in response_list:
          guess_remain -= 1
          print("Wrong!")
      else:
        print("")
        
    if guess not in response_list:
      response_list.append(guess)
    print(response_list)
    
    hidden_word = ""
    for letter in letters: 
      if letter in response_list:
        hidden_word += letter
      else:
        hidden_word += "_ "
      print(hidden_word)
      
    if guess_remain == 0:
      print("You ran out of guesses. You lose!")
      print("The word is " + random_word + ".")
      
    if hidden_word == random_word:
      print("You Win! The word is " + random_word + ".")
      break
    
play()
