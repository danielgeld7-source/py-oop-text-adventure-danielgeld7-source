from room import Room
from item import Item
from character import Character
from character import Enemy



kitchen = Room("kitchen ")
kitchen.set_description("A dank and dirty room buzzing with flies. ")

dinning_hall = Room("dining Hall ")
dinning_hall.set_description("a large room with tables ")

ballroom = Room("Ballroom ")
ballroom.set_description("a vast open room with a shining floor ")

dave = Character("Dave", "A smelly zombie")
bob = Enemy("bob", "a knight of the opposing side")
bob.set_weakness("poop")
dinning_hall.set_character(dave)
ballroom.set_character(bob)
kitchen.describe()
dave.describe()
bob.describe()
print("What will you fight with?")
fight_with = input()
bob.fight(fight_with)


player_inventory = []
kitchen.link_room(dinning_hall, "south")
dinning_hall.link_room(kitchen, "north")
dinning_hall.link_room(ballroom, "west")
ballroom.link_room(dinning_hall, "east")
cheese = Item("cheese", "A smelly block of cheddar.")
kitchen.add_item(cheese)
sword = Item("sword", "a long dark nights blade with the taste of blood but still as sharp as ever")
dinning_hall.add_item(sword)
current_room = kitchen 

while True:		
    print("\n")         
    current_room.get_details()         
    command = input("> ")    
    current_room = current_room.move(command)
    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()
    if command.startswith("take "):
        item_name = command.replace("take ", "")
        for item in current_room.items:
            if item.name == item_name:
                player_inventory.append(item)
                current_room.items.remove(item)
                print(f"You pick up the {item.name}: {item.description}")
                break
        else:
            print("That isn't here.")
    else:
        current_room = current_room.move(command)