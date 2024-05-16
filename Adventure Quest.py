import random

def start_adventure():
    print("Welcome to the tropical island of Bimomba!")
    name = input("What is your name, explorer? ")
    print(f"Hello, {name}. Your journey begins near the shore of the Bimomba. You come across two converging paths; one through a dense jungle, the other through a dark chasm. ")
    first_choice()

def first_choice():
    choice = input("Which path would you like to take? (jungle/chasm) ")
    if choice.lower() == 'jungle':
        jungle()
    elif choice.lower() == 'chasm':
        chasm()
    else:
        print("Unknown choice, please type 'jungle' or 'chasm'")
        first_choice()


# Jungle Subplot
def jungle():
    print("While deep into the junge, night wanes and you lose your sense of direction.")
    jungle_choice = input("Make your choice (sleep/continue)")
    if jungle_choice.lower() == 'sleep':
        sleep()
    elif jungle_choice.lower() == 'continue':
        jungle_continue()
    else:
        print("Unknown choice, please type 'sleep' or 'continue'")
        jungle()

def sleep():
    print('While sleeping an anaconda cyborg injects you with a paralyzing agent and hauls you to their habitat. ')

def jungle_continue():
    print('Further into the jungle darkness falls. Luckily a bioluminescent cyborg bird approaches and offers to guide you. ')
    bird_choice = input("Take the bird up on their offer or stay on your own.Please type (bird/alone)")
    if bird_choice.lower() == 'bird':
        bird()
    elif bird_choice.lower() == 'alone':
        alone()
    else:
        print("Unknown choice, please type 'bird' or 'alone'") 

def bird():
    print("The bird guides you all night. By dawn you encounter a civilization where a intricate network of bridges, boardwalks and causeways lead to highly advanced cabanas.")
    village_choice = input("The bird briefs you on the customs of the village. If you would like to stay in the village for any amount of time, you must be approved by the customs counsel at the embassy. Otherwise you must continue on past the village, The birds informs you there is another, more welcoming village ahead called 'Rundah' but that it can only guide you part of the way.")
    if village_choice.lower() == 'embassy':
        embassy()
    elif village_choice.lower() == 'rundah':
        rundah()
        
def embassy():
    print("At the embassy you undergo a rigorous series of tests and interviews. You are told that you can never leave and are given a new identity")

def rundah():
    print("")

def alone():
    print("You continue into the jungle alone. You cannot see well and your foot gets trapped in larges vines that constrict you and pull you into a")

#Chasm subplot
def chasm():
    print("The chasm opens to a waterfall with a desolate sancuary at the basin. You discover mysterious inscriptions carved into the walls. Suddenly a droning sound emanates from inside the sancuary.")
    chasm_choice = input("To go into the sancuary type temple. To continue along the chasm river type river")

def temple():
    print("After you enter the sancuary you are confronted by a wall with shimmering inscriptions that change shape every few seconds. You accidentally step on a stone and the inscriptions light up to reveal 3 sets of numbers. You discover this is a minigame.")

    pass_code = False

    while not pass_code:

        num1 = random.randint(1, 100)
        num2 = random.randint(1, 100)
        num3 = random.randint(1, 100)

        sum_numbers = num1 + num2 + num3

        if sum_numbers % 5 == 0:
            pass_code = True
            print(f"The numbers {num1}, {num2}, {num3} are the keys, The wall sinks into the ground and steps leading down into the sancuary are revealed.")

        else:
            print(f"The numbers {num1}, {num2}, {num3} are not the keys. Please try again.")
temple()

def river():
    print('')
   
#Rundah Final Desination


def save_outcome(outcome):
    with open("adventure_outcomes.txt", "a") as file:
        file.write(outcome + "\n")

def read_outcomes():
    with open("adventure_outcomes.txt", "r") as file:
        outcomes = file.readlines()
        print("Previous adventure outcomes:")
        for outcome in outcomes:
            print(outcome.strip())

if __name__ == "__main__":
    start_adventure()
