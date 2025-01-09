import requests

api_url = "https://random-word-api.herokuapp.com/word?length=5"

response = requests.get(api_url)

if response.status_code == 200:
    word = response.json()[0]
else:
    print(f"Failed to fetch word. Status code: {response.status_code}")


def hanger(word):
    guessed = ['_'] * len(word)
    score = 0
    
    while score < 5:
        print(' '.join(guessed)) # Combines the seperate strings into one string
        userword = input("Choose a letter from a-z: ")
        
        if userword in word:
            for i in range(len(word)):
                if guessed[i] == userword:
                    score += 1
                    print(f'Incorrect! Score: {score}')
                if word[i] == userword:
                    guessed[i] = userword                    
            if '_' not in guessed:
                print(f"Congratulations! You guessed the word: {''.join(guessed)}, You get to stay alive!")
                return
            
        else:
            score += 1
            print(f'Incorrect! Score: {score}')
    
    print(f"You lost! The word was: {word}, the user is now dead X( ")


hanger(word)