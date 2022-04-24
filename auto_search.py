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
		print("Beginning search number {}".format(i))
		click(values["bar_x"], values["bar_y"])
		print("Clicked on search bar")
		# enter random words
		search = random_search()
		print("Entering search: {}".format(search))
		autopy.key.type_string(search, wpm=2000)
		print("Typed Search")
		autopy.key.tap(autopy.key.Code.RETURN)
		print("Pressed Enter")

		time.sleep(1)

	print("Searches complete. Minimizing Browser")
	click(values["icon_x"], values["icon_y"])
	

def random_search():
    # List of random words to search
    words = ["movies", "best", "worst", "and", "actors", "games", "top 10",
             "of 2000s", "shows","tv shows","songs","singers","artists",
             "shaimus", "recipes", "food", "2010s", "1990s", "funny",
             "cats","dogs","hamsters","video games"]

    search_count = random.randint(1,5)
    ran_search = ""
    for i in range(search_count):
        ran_word = words[random.randint(1,len(words)-1)]
        ran_search = ran_search + " " + ran_word

    return ran_search

def click(x,y):
	print("Moving mouse to {},{}".format(x,y))
	autopy.mouse.move(x,y)
	print("Moved")
	autopy.mouse.click()
	print("Clicked")


if __name__ == "__main__":
    main()
