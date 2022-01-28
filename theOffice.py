import requests # package needed to get access to requesting the office api
BASE_URL = "https://officeapi.dev/api/" # the base url for the office api


def main(): 
    print("Welcome to the Office")
    mainMenu()

    option = int(input("Please Select an Option: ")) # casting the input as an integer
    checkUserOption(option)

    print("")
    while (option != 5) :
        if(option == 1):
            print("Here's your random quote: \n")
            optionOne()
        elif(option == 2):
            print("Here's your random character: \n")
            optionTwo()
        elif(option == 3):
            print("Here are all the characters from The Office: \n")
            optionThree()
        elif(option == 4):
            print("You may want to check out this episode: \n")
            optionFour()
        
        mainMenu()
        option = int(input("Please Select an Option: "))
        checkUserOption(option)
        print("")

    print("Thank you for using this program! \n")



##MAIN MENU-----------------------------------------------------------------------------------------------------------------------
def mainMenu():
    print("---------------------------------------------------------------------")
    print("1. Get a random quote from a character from The Office.")
    print("2. Show a random character.")
    print("3. Show all characters from the Office.")
    print("4. Pick a random episode for you to watch.")
    print("5. Quit \n")


##USER VALIDATION FUNCTION-----------------------------------------------------------------------------------------------------------------------
def checkUserOption(option):
    if (option < 1) or (option > 6):
        print("That is an invalid option, please select a valid option!")


##OPTIONS FUNCTIONS-----------------------------------------------------------------------------------------------------------------------
def optionOne(): 
    request_url = f"{BASE_URL}quotes/random"
    response = requests.get(request_url) #response gained from the RANDOM QUOTE api

    if(response.status_code == 200):
        data = response.json()
        quote = data['data']['content']
        character = f" - {data['data']['character']['firstname']} {data['data']['character']['lastname']}"
        print(f"\"{quote}\"")
        print(character, "\n")
    else:
        print("An error occured!")

def optionTwo():
    request_url = f"{BASE_URL}characters/random"
    response = requests.get(request_url) #response gained from the RANDOM CHARACTER api

    if(response.status_code == 200):
        data = response.json()
        character = f"{data['data']['firstname']} {data['data']['lastname']}"
        print(character, '\n')
    else: 
        print("An error occured!")


def optionThree():
    request_url = f"{BASE_URL}characters/"
    response = requests.get(request_url) #response gained from the GET ALL CHARACTERS api

    if(response.status_code == 200):
        data = response.json()
        characters = data['data'] #list of characters 
        ##print(characters[1]['firstname'])
        for i in characters:
            firstName = i['firstname']
            lastName = i['lastname']
            print(firstName, lastName, "\n")
  
    else:
        print("An error occured!")

def optionFour():
    request_url = f"{BASE_URL}episodes/random"
    response = requests.get(request_url) #response gained from the RANDOM EPISODES api

    if(response.status_code == 200):
        data = response.json()
        episode = f"Episode: {data['data']['title']}"
        description = f"Description: {data['data']['description']}"
        print(episode)
        print(description, "\n")
    else:
        print("An error occured!")
main() #running the main function