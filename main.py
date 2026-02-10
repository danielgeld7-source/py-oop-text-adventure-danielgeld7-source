from room import Room

kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")
kitchen.get_description()

kitchen.describe()

dinning_hall = Room("dining Hall")
dinning_hall.set_description("a large room with tables")

ballroom = Room("Ballroom")
ballroom.set_description("a vast open room with a shining floor")

kitchen.link_room(dinning_hall, "south")
dinning_hall.link_room(kitchen, "north")
dinning_hall.link_room(ballroom, "west")
ballroom.link_room(dinning_hall, "east")