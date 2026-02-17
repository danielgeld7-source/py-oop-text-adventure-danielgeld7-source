class Room():
    def __init__(self, room_name,):
        self.name = room_name
        self.descripton = None
        self.linked_rooms = {}
        self.items = []
        self.all_items = []
         
       
    

    def set_description(self, room_description):
        self.description = room_description
    
    def add_item(self, item_object): # <--- MUST HAVE THIS METHOD
        self.items.append(item_object)

    def get_description(self):
        return self.description 
    
    def describe(self): 
        print( self.description )
    
    def link_room(self, room_to_link, direction):
        self.linked_rooms[direction] = room_to_link

        print( self.name + " linked rooms :" + repr(self.linked_rooms) )

    def get_name(self):
        return self.name
    
    def add_item(self, item):
        self.items.append(item)
    
    def get_description(self):
        return self.description
    
    
    def get_details(self):
        """This single method handles everything the player needs to see."""
        print(f"\nYou are in the {self.name}")
        print(self.description)
        
        # This part was being overwritten in your original code
        for item in self.items:
            print(f"You see a {item.name} here.")
            
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print(f"The {room.name} is to the {direction}")
        
    
    def remove_item(self, item_name):
        for item in self.items:
            if item.name.lower() == item_name.lower():
                self.items.remove(item)
                return item  # Return the object to put in player inventory
        return None



    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        elif direction in self.all_items:
            item_obj = self.all_items[direction]
            print(item_obj.description)
    
    
            
        else:
            print("You can't go that way")
            return self

    class Inventory:
        def __init__(self):
       
            self.all_items = {}

        def display_items(self):
            for item_name in self.all_items:
                item_obj = self.all_items[item_name]
            # Use f-strings for cleaner formatting
            print(f"There is a {item_name}: {item_obj.description}") 

        def remove_item(self, item_name):
            del self.all_items[item_name]

        def add_item(self, item_obj, item_name):
	        self.all_items[item_name] = item_obj

        
        
    