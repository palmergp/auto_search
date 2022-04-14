import pickle
import autopy
import time

def configure():
    print("Welcome to auto search configuration!")
    print("\tFor this script to work, you must give the x,y coordinates of your web browser icon and its search bar")
    print("\tThis configuration process will take some guess and check to get those values")
    while True:
        print("Beginning configuration...")
        # Browser Icon Configuration
        while True:
            icon_x = int(input("Please provide an x-value for your browser icon: "))
            icon_y = int(input("Please provide a y-value for your browser icon: "))
            input("Press Enter to move your mouse to the supplied value")
            try:
                autopy.mouse.move(icon_x, icon_y)
                reconfigure = input("Did your mouse move to the center of your browser icon? y/n: ")
                if reconfigure.lower() == "y" or reconfigure.lower() == "yes":
                    print("Success! Moving to search bar configuration")
                    break
                else:
                    print("Restarting configure loop for browser icon...")
            except ValueError:
                print("Value was out of bounds! Try a smaller number")

        # Search Bar Configuration
        while True:
            bar_x = int(input("Please provide an x-value for your browser's search bar: "))
            bar_y = int(input("Please provide a y-value for your browser's search bar: "))
            input("Press Enter to move your mouse to the supplied value")
            try:
                autopy.mouse.move(bar_x, bar_y)
                reconfigure = input("Did your mouse move to the center of your browser's search bar? y/n: ")
                if reconfigure.lower() == "y" or reconfigure.lower() == "yes":
                    print("Success! Moving to trial...")
                    break
                else:
                    print("Restarting configure loop for search bar...")
            except ValueError:
                print("Value was out of bounds! Try a smaller number")

        # Attempt test search
        input("Press Enter to attempt a trial browser search")
        autopy.mouse.move(icon_x, icon_y)
        autopy.mouse.click()
        time.sleep(1)
        autopy.mouse.move(bar_x, bar_y)
        autopy.mouse.click()
        autopy.key.type_string("Shaimus Band", wpm=2000)
        autopy.key.tap(autopy.key.Code.RETURN)
        reconfigure = input("Was the search successful?")
        if reconfigure.lower() == "y" or reconfigure.lower() == "yes":
            print("Success! Your values will be saved to a file for future use")
            print("\tIcon X,Y: {},{}".format(icon_x,icon_y))
            print("\tSearchbar X,Y: {},{}".format(bar_x, bar_y))

            # Save to pickle file
            values = {"icon_x": icon_x,
                      "icon_y": icon_y,
                      "bar_x": bar_x,
                      "bar_y": bar_y}
            with open("configuration.pckl", 'wb') as f:
                pickle.dump(values, f)

            return values
        else:
            print("Restarting reconfiguration process...")


if __name__ == "__main__":
    configure()
