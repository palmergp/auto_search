import autopy
import random
import time
import pickle
from configure_auto_search import configure

SEARCHES = 50


def main():

	# Load configuration
	try:
		with open("configuration.pckl", "rb") as f:
			values = pickle.load(f)
		print("Configuration successfully loaded!")
	except FileNotFoundError:
		print("Unable to find configuration file. Running configuration now...")
		values = configure()

	# Move mouse to wake up laptop
	autopy.mouse.move(100,100)
	autopy.mouse.move(200,200)
	time.sleep(1)
	print("Starting searches")

    # Click on Microsoft Edge
	result = click(values["icon_x"], values["icon_y"])
	print("Clicked on Browser")
	if result == 1:
		print("Ending")
		return
		
	time.sleep(1)

	for i in range(0,SEARCHES):

        # Click on search bar
		click(values["bar_x"], values["bar_y"])

		# enter random words
		autopy.key.type_string(random_search(), wpm=2000)
		autopy.key.tap(autopy.key.Code.RETURN)

		time.sleep(20)

	print("Searches complete. Minimizing Browser")
	click(values["icon_x"], values["icon_y"])
	

def random_search():
    # List of random words to search
    words = ["movies", "best", "worst", "and", "actors", "games", "top 10",
             "of 2000s", "shows","tv shows","songs","singers","artists",
             "shaimus", "recipes", "food", "2010's", "1990's", "funny",
             "cats","dogs","hamsters","video games"]

    search_count = random.randint(1,5)
    ran_search = ""
    for i in range(search_count):
        ran_word = words[random.randint(1,len(words)-1)]
        ran_search = ran_search + " " + ran_word

    return ran_search

def click(x,y):
	autopy.mouse.move(x,y)
	autopy.mouse.click()


if __name__ == "__main__":
    main()
