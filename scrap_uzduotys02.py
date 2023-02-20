from bs4 import BeautifulSoup
import requests
import random


url = "http://quotes.toscrape.com/"
response = requests.get(url)

soup = BeautifulSoup(response.content, "html.parser")
quotes = soup.find_all(class_="quote")
game_material = []

def get_author_info(author):
    url = f"http://quotes.toscrape.com/author/{author.split()[0]}-{author.split()[1]}/"
    respnse = requests.get(url)
    soup = BeautifulSoup(respnse.content, "html.parser")
    author = {
        "date": soup.find(class_="author-born-date").get_text(),
        "location": soup.find(class_="author-born-location").get_text()
    }
    return author

for quote in quotes:
    quote_obj = {
        "quote": quote.select_one(".text").get_text(),
        "author": quote.select_one('.author').get_text()
    }
    game_material.append(quote_obj)

while True:
    guess_counter = 0
    quote_index = random.randint(0,len(game_material)-1)
    print(game_material[quote_index]["quote"])
    guess = input("Guess quotes autohor: ")
    if guess == game_material[quote_index]["author"]:
        print("You winn")
        ask_for_continue = input("Do you wanna continue y/n? ")
        if ask_for_continue == 'n'
            break
        continue
    guess_counter += 1
    if guess_counter == 1:
        print(game_material[quote_index]["author"].split()[0][0] + game_material[quote_index]["author"].split()[1][0])
        guess = input("Guess quotes autohor: ")
        if guess == game_material[quote_index]["author"]:
            print("You winn")
            break
    guess_counter += 1
    if guess_counter == 2:
        author = get_author_info(game_material[quote_index]["author"])
        print(f"Born date: {author['date']}\nLocation: {author['location']}")
        guess = input("Guess quotes autohor: ")
        if guess == game_material[quote_index]["author"]:
            print("You winn")
            break
    guess_counter += 1
    if guess_counter == 3:
        print(f"You guessed {guess_counter} times")
        print("You losse")
        ask_for_continue = input("Do you wanna continue y/n? ")
        if ask_for_continue == 'n':
            break
        

       

