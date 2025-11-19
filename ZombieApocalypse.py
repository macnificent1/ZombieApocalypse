import random
import time

def game_over(reason, player_name):
    print(f"\n--- GAME OVER ---")
    print(f"{player_name}, {reason}")
    print("The world falls to the undead.")
    exit()

def win_game(player_name):
    print(f"\n--- CONGRATULATIONS ---")
    print(f"{player_name}, you made it to the evacuation site! You are safe, for now.")
    print("Humanity has a chance thanks to survivors like you.")
    exit()

def play_game():
    player_name = input("What is your name, survivor? ")
    print(f"\nWelcome, {player_name}. The world has fallen. Zombies roam the streets.")
    print("Your mission: reach the evacuation site at the old military base, 20 miles north.")
    print("Good luck. You'll need it.\n")
    
    # Define the locations in order as a list for progression tracking
    locations_order = ["abandoned house", "deserted street", "grocery store", "forest path", "cabin", "trail", "shack", "dirt road", "general store", "city street", "office building", "highway"]
    current_location_index = 0
    current_location = locations_order[current_location_index]
    
    supplies = {"food": 20, "water": 20, "medkit": 2, "ammo": 5}
    has_car = False
    bitten = False

    # Game Loop with at least 10 prompts
    prompt_count = 0
    while prompt_count < 100:
        prompt_count += 1
        print(f"\n--- Location: {current_location.capitalize()} ---")
        print(f"\nSupplies: Food: {supplies['food']}, Water: {supplies['water']}, Medkits: {supplies['medkit']}, Ammo: {supplies['ammo']}")
        
        if bitten:
            if random.random() < 0.3: # 30% chance to turn each turn if bitten
                game_over("\nthe infection took hold, and you turned into one of them.", player_name)
            else:
                print("\nYou feel the bite wound throbbing. Time is running out.")
        
        if supplies["food"] <= 0 and supplies["water"] <= 0:
            game_over("\nyou succumbed to starvation and dehydration.", player_name)

        # Main location logic with added locations
        if current_location == "abandoned house":
            print("\nYou are in an abandoned house. Dust covers everything.")
            choice = input("Do you (search) for supplies, or (leave) the house? ").lower()
            if choice == "search":
                print("\nYou cautiously search the house...")
                if random.random() < 0.9:
                    found_item = random.choice(["food", "water", "ammo"])
                    supplies[found_item] += 1
                    print(f"\nYou found some {found_item}!")
                else:
                    print("\nYou found nothing useful.")
                if random.random() < 0.1:
                    print("\nA zombie shuffles out of a dark corner! You barely escape with a scratch.")
                    if not bitten:
                        bitten = True
                        print("\nYou've been bitten!")
            elif choice == "leave":
                current_location_index += 1
                current_location = locations_order[current_location_index]
            else:
                print("\nInvalid choice. You waste precious time.")
                
        # New location: deserted street
        elif current_location == "deserted street":
            print("\nYou are on a deserted street. Cars are abandoned, and the silence is eerie.")
            choice = input("Do you (check) the cars for loot, or (move) towards the next area? ").lower()
            if choice == "check":
                print("\nYou cautiously check the nearest cars...")
                if random.random() < 0.5:
                    found_item = random.choice(["food", "water", "ammo"])
                    supplies[found_item] += 1
                    print(f"\nYou found some {found_item} in a glove compartment!")
                else:
                    print("\nMost cars are empty or locked tight.")
                if random.random() < 0.2:
                    print("\nA horde of zombies shambles into view at the end of the street! You hide behind a car until they pass.")
            elif choice == "move":
                current_location_index += 1
                current_location = locations_order[current_location_index]
            else:
                print("\nInvalid choice. You should decide quickly.")
        
        # New location: grocery store
        elif current_location == "grocery store":
            print("\nYou stand before a ransacked grocery store. The doors are broken, but supplies might still be inside.")
            choice = input("Do you (enter) the store to scavenge, or (avoid) the risk and move on? ").lower()
            if choice == "enter":
                print("\nYou step inside the dark store, careful where you tread...")
                if random.random() < 0.8:
                    print("You find several cans of food and some bottled water.")
                    supplies["food"] += 3
                    supplies["water"] += 2
                else:
                    print("The shelves are completely bare. Only trash remains.")
                if random.random() < 0.4:
                    print("A single zombie lunges from behind the checkout counter! You have to fight it off, losing precious time and getting scratched.")
                    if not bitten:
                        bitten = True
                        print("You've been bitten!")
            elif choice == "avoid":
                current_location_index += 1
                current_location = locations_order[current_location_index]
            else:
                print("\nInvalid choice. The danger is real.")
        
        # New location: forest path
        elif current_location == "forest path":
            print("\nYou are on a narrow forest path. The trees block out most of the light, making it feel isolated.")
            choice = input("Do you (follow) the path deeper, or (rest) for a moment? ").lower()
            if choice == "follow":
                print("\nYou continue down the path...")
                if random.random() < 0.2:
                    print("You stumble upon a hunter's old backpack.")
                    found_item = random.choice(["food", "water", "ammo"])
                    supplies[found_item] += 2
                    print(f"You find extra {found_item} inside!")
                    current_location_index += 1
                    current_location = locations_order[current_location_index]
                else:
                    print("The path is long and uneventful.")
                    current_location_index += 1
                    current_location = locations_order[current_location_index]
            elif choice == "rest":
                if supplies["food"] > 0:
                    supplies["food"] -= 1
                    print("You eat some food and rest. You feel slightly refreshed.")
                else:
                    print("You rest, but the hunger makes it difficult to relax.")
                # After resting, prompt to continue
                input("Press Enter to continue your journey down the path...")
                current_location_index += 1
                current_location = locations_order[current_location_index]
            else:
                print("\nInvalid choice.")        

        elif current_location == "cabin":
            print("\nYou find a small, isolated cabin in the woods.")
            choice = input("Do you (check) inside for shelter or supplies, or (continue) on the trail? ").lower()
            if choice == "check":
                print("\nThe cabin is old, but surprisingly untouched.")
                if random.random() < 0.6:
                    print("You find a small stash of food and a hunting knife (ammo +1).")
                    supplies["food"] += 2
                    supplies["ammo"] += 1
                else:
                    print("It's empty, save for dust and cobwebs.")
            elif choice == "continue":
                current_location_index += 1
                current_location = locations_order[current_location_index]
            else:
                print("\nInvalid choice. The quiet here is unnerving.")

        elif current_location == "trail":
            print("\nYou are on a narrow forest trail. It's overgrown in places.")
            choice = input("Do you move (stealthily) or (hurry) through? ").lower()
            if choice == "stealthily":
                if random.random() < 0.8:
                    print("\nYou move silently, avoiding detection.")
                else:
                    print("\nA zombie spots you! You manage to escape, but lose some energy (food).")
                    supplies["food"] -= 1
            elif choice == "hurry":
                print("\nYou rush through the undergrowth. You're tired, but cover ground.")
                supplies["water"] -= 1
                if random.random() < 0.4:
                    print("\nYou encounter a small group of zombies. You use some ammo to clear the path.")
                    supplies["ammo"] -= random.randint(1, 2)
                    if supplies["ammo"] < 0:
                        game_over("\nyou ran out of ammo and were overwhelmed by the zombies.", player_name)
            else:
                print("\nInvalid choice. The forest seems to watch you.")
            
            # Allow progress after actions in trail
            if choice in ["stealthily", "hurry"]:
                 if random.random() < 1:
                    print("You feel you've made significant progress.")
                    current_location_index += 1
                    current_location = locations_order[current_location_index]

        elif current_location == "shack":
            print("\nYou come across a dilapidated shack next to the trail.")
            choice = input("Do you (search) the shack, (rest) for a bit, or (push) on? ").lower()
            if choice == "search":
                if random.random() < 0.5:
                    print("You find a dusty medkit under a floorboard!")
                    supplies["medkit"] += 1
                else:
                    print("The shack is empty and unsafe.")
            elif choice == "rest":
                print("You rest for a while, recovering some stamina (food and water -1, but health feels better).")
                supplies["food"] -= 1
                supplies["water"] -= 1
                if bitten:
                    print("Rest does little to stop the infection.")
            elif choice == "push":
                current_location_index += 1
                current_location = locations_order[current_location_index]
            else:
                print("\nInvalid choice.")

        elif current_location == "dirt road":
            print("\nYou leave the trail and find a dirt road, likely leading north.")
            choice = input("Do you (follow) the road, or (look) for a vehicle? ").lower()
            if choice == "follow":
                print("You follow the road. It's slow going on foot.")
                # Allow progress
                if random.random() < 1:
                    current_location_index += 1
                    current_location = locations_order[current_location_index]
            elif choice == "look":
                if not has_car:
                    if random.random() < 0.4:
                        print("\nYou found an old, but functional car! It's low on gas.")
                        has_car = True
                    else:
                        print("\nNo working vehicles here.")
                else:
                    print("\nYou already have a car.")
            else:
                print("\nInvalid choice.")

        elif current_location == "general store":
            print("\nYou find a small general store off the road. The windows are broken.")
            choice = input("\nDo you (look) for food/water, (check) the back room, or (leave)? ").lower()
            if choice == "look":
                if random.random() < 0.7:
                    supplies["food"] += random.randint(1, 3)
                    supplies["water"] += random.randint(1, 2)
                    print("\nYou found a decent amount of food and water!")
                else:
                    print("\nThe shelves are mostly empty. Only scraps remain.")
                if random.random() < 0.3:
                    print("\nA horde of zombies bursts in! You fight your way out, using some ammo.")
                    supplies["ammo"] -= 1
                    if supplies["ammo"] < 0:
                        game_over("\nyou ran out of ammo and were overwhelmed by the horde.", player_name)
            elif choice == "check":
                if random.random() < 0.5:
                    supplies["medkit"] += 1
                    print("\nYou found a medkit in a locked cabinet!")
                else:
                    print("\nThe back room is completely looted.")
            elif choice == "leave":
                current_location_index += 1
                current_location = locations_order[current_location_index]
            else:
                print("\nInvalid choice. The smell of decay is strong.")

        elif current_location == "city street":
            print("\nYou've reached the outskirts of a nearby city. Streets are dangerous.")
            choice = input("Do you move (cautiously) through the streets, or (stick) to the alleys? ").lower()
            if choice == "cautiously":
                if has_car:
                    print("Driving cautiously through the wreckage.")
                    if random.random() < 0.2:
                         print("You attract a large horde with engine noise! You speed away, but use some gas.")
                else:
                    print("Moving carefully, avoiding major threats.")
                # Allow progress
                if random.random() < 1:
                    current_location_index += 1
                    current_location = locations_order[current_location_index]
            elif choice == "stick":
                print("Alleys are quieter but might be dead ends.")
                if random.random() < 0.3:
                    print("You are ambushed by a few zombies! You use ammo to escape.")
                    supplies["ammo"] -= 1
                    if supplies["ammo"] < 0:
                         game_over("\nyou ran out of ammo and were overwhelmed by the zombies.", player_name)
                # Allow progress
                if random.random() < 1:
                    current_location_index += 1
                    current_location = locations_order[current_location_index]
            else:
                print("Invalid choice. The city groans with the undead.")

        elif current_location == "office building":
            print("\nYou take shelter in a large, abandoned office building.")
            choice = input("Do you (search) the floors, (look) for a vantage point, or (leave)? ").lower()
            if choice == "search":
                if random.random() < 0.4:
                    print("You find a first aid station with a medkit and some water bottles.")
                    supplies["medkit"] += 1
                    supplies["water"] += 2
                else:
                    print("Everything is trashed. Only papers remain.")
            elif choice == "look":
                print("From the roof, you see the highway in the distance. The military base is close!")
                # Allow progress after seeing the goal
                if random.random() < 0.1:
                    current_location_index += 1
                    current_location = locations_order[current_location_index]
            elif choice == "leave":
                current_location_index += 1
                current_location = locations_order[current_location_index]
            else:
                print("Invalid choice. You hear movement on the floor above you.")

        elif current_location == "highway":
            print("\n--- GOAL REACHED ---")
            print("You made it to the highway.")
            print("In the distance, you can see the old military base. It's the evacuation site!")
            win_game(player_name)


        # Generic turn-based actions and consumption
        if supplies["food"] > 0:
            supplies["food"] -= 1
        if supplies["water"] > 0:
            supplies["water"] -= 1
        
        if supplies["food"] < 1:
            print("\nYou're getting hungry...")
        if supplies["water"] < 1:
            print("\nYou're getting thirsty...")
        
        if bitten and supplies["medkit"] > 0:
            heal_choice = input("\nYou're bitten! Use a medkit? (yes/no) ").lower()
            if heal_choice == "yes":
                supplies["medkit"] -= 1
                bitten = False
                print("\nYou treated the bite. The infection is contained, for now.")
            else:
                print("\nYou decide against using a medkit. The risk grows...")
        
        time.sleep(1) # Pause for readability

 #   game_over("time ran out before you could reach the evacuation site.", player_name)

if __name__ == "__main__":
    play_game()