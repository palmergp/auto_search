import autopy
import random
import time

SEARCHES = 50

def main(): 

	# Move mouse to wake up laptop
	autopy.mouse.move(100,100)
	autopy.mouse.move(200,200)
	time.sleep(10)
	print("Starting searches")

    # Click on Microsoft Edge
	result = click_on_edge()
	print("Clicked on Edge")
	if result == 1:
		print("Ending")
		return
		
	time.sleep(25)

	for i in range(0,SEARCHES):

        # Click on search bar
		click_on_searchbar()

		# enter random words
		autopy.key.type_string(random_search(), wpm=2000)
		autopy.key.tap(autopy.key.Code.RETURN)

		time.sleep(3)

	print("Searches complete. Minimizing Edge")
	click_on_edge()
	

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

def click_on_edge():
	print("In click on edge function")
	autopy.mouse.move(355,745)
	autopy.mouse.click()

def click_on_searchbar():
    autopy.mouse.move(500,50)
    autopy.mouse.click()
    

if __name__ == "__main__":
    main()
        
