import random

def intro_screen():
    intro_art = r'''                                  
                                   # #### ####
                                ### \/#|### |/####
                               ##\/#/ \||/##/_/##/_#
                             ###  \/###|/ \/ # ###
                           ##_\_#\_\## | #/###_/_####
                          ## #### # \ #| /  #### ##/##
                           __#_--###`  |{,###---###-~
                                     \ }{
                                      }}{
                                      }}{
                                      {{}
                                , -=-~{ .-^- _
                                      `}
                                       {






                  &&& &&  & &&
              && &\/&\|& ()|/ @, &&
              &\/(/&/&||/& /_/)_&/_&
           &() &\/&|()|/&\/ '%" & ()
          &_\_&&_\ |& |&&/&__%_/_& &&
        &&   && & &| &| /& & % ()& /&&
         ()&_---()&\&\|&&-&&--%---()~
             &&     \|||
                     |||
                     |||
                     |||
               , -=-~  .-^- _         `
        '''
    print("Welcome to the forest.")
    print(intro_art)

# Function to validate player input
def get_valid_input(prompt, options):
    """Prompt the user for valid input until they provide it."""
    while True:
        player_input = input(prompt).strip()
        if player_input in options:
            return player_input
        print("Invalid input. Please try again.")

# Function to calculate score based on chance
def apply_chance_event(score, event):
    """Randomly adjust the score based on a chance event."""
    outcome = random.choice(["positive", "negative"])
    if outcome == "positive":
        print(f"Good luck! {event['positive_message']}")
        return score + event['positive_points']
    else:
        print(f"Bad luck! {event['negative_message']}")
        return score + event['negative_points']

# Game functions for specific paths
def path_forest(score):
    """The forest path where the player makes decisions."""
    print("\nYou are in a dense forest. You hear a sound nearby.")
    choice = get_valid_input("Do you (1) investigate the sound or (2) stay on the trail? ", ["1", "2"])
    if choice == "1":
        print("\nYou find a hidden treasure chest!")
        score += 10
    else:
        print("\nYou safely continue on the trail but miss out on potential treasure.")
        score += 2
    
    print(f"Your current score is {score} points.\n")
    
    print("You encounter a river blocking your way.")
    choice = get_valid_input("Do you (1) swim across or (2) build a raft? ", ["1", "2"])
    event = {
        "positive_message": "You safely make it across the river.",
        "positive_points": 5,
        "negative_message": "You lose your supplies in the water.",
        "negative_points": -5
    }
    score = apply_chance_event(score, event)

    print(f"Your current score is {score} points.\n")

    print("You see a bear in the distance.")
    choice = get_valid_input("Do you (1) climb a tree or (2) run? ", ["1", "2"])
    if choice == "1":
        print("\nThe bear doesn't notice you. You rest safely.")
        score += 5
    else:
        print("\nThe bear chases you, but you manage to escape with some scratches.")
        score -= 3

    print(f"Your final score is {score} points.")
    return score

def path_cave(score):
    
    """The cave path where the player makes decisions."""
    print("\nYou enter a dark cave and find a fork in the path.")
    choice = get_valid_input("Do you (1) go left or (2) go right? ", ["1", "2"])
    if choice == "1":
        print("\nYou discover a beautiful crystal.")
        score += 8
    else:
        print("\nYou fall into a shallow pit but manage to climb out.")
        score -= 2

    print(f"Your current score is {score} points.\n")
    
    print("A giant spider blocks your way.")
    choice = get_valid_input("Do you (1) fight the spider or (2) run away? ", ["1", "2"])
    event = {
        "positive_message": "You defeat the spider and find gold in its web.",
        "positive_points": 15,
        "negative_message": "You escape but lose some gear.",
        "negative_points": -5
    }
    score = apply_chance_event(score, event)

    print(f"Your current score is {score} points.\n")

    print("You see light at the end of the tunnel.")
    choice = get_valid_input("Do you (1) move towards the light or (2) explore deeper? ", ["1", "2"])
    if choice == "1":
        print("\nYou find the exit and leave with treasure!")
        score += 10
    else:
        print("\nYou explore deeper but find nothing more.")
        score += 2

    print(f"Your final score is {score} points.")
    return score

# Main game function
def main():
    print(intro_screen())
    """Main function to run the text adventure game."""
    print("Welcome to the Adventure Game!")
    print("You start with 0 points.")
    score = 0

    print("\nYou stand at a crossroads.")
    choice = get_valid_input("Do you (1) take the forest path or (2) enter the cave? ", ["1", "2"])
    if choice == "1":
        score = path_forest(score)
    else:
        score = path_cave(score)

    print("\nGame Over!")
    print(f"Your final score is {score} points. Thanks for playing!")

# Run the game
if __name__ == "__main__":
    main()
