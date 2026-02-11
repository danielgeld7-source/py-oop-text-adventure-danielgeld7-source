from room import Room
from item import Item

kitchen = Room("kitchen ")
kitchen.set_description("A dank and dirty room buzzing with flies. ")
kitchen.get_description()

kitchen.describe()

dinning_hall = Room("dining Hall ")
dinning_hall.set_description("a large room with tables ")

ballroom = Room("Ballroom ")
ballroom.set_description("a vast open room with a shining floor ")
player_inventory = []
kitchen.link_room(dinning_hall, "south")
dinning_hall.link_room(kitchen, "north")
dinning_hall.link_room(ballroom, "west")
ballroom.link_room(dinning_hall, "east")
cheese = Item("cheese", "A smelly block of cheddar.")
kitchen.add_item(cheese)
sword = Item("blood sword ", "a long dark nights blade with the taste of blood but still as sharp as ever")
dinning_hall.add_item(sword)
current_room = kitchen 

while True:		
    print("\n")         
    current_room.get_details()         
    command = input("> ")    
   
    if command.startswith("take "):
        item_name = command.replace("take ", "")
        for item in current_room.items:
            if item.name == item_name:
                player_inventory.append(item)
                current_room.items.remove(item)
                print(f"You picked up the {item_name}!")
                break
        else:
            print("That isn't here.")
    else:
        current_room = current_room.move(command)