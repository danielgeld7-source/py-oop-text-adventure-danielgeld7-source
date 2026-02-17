class Chararcter():

    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

        def describe(self):
            print(self.name)
            print(self.description)
    
        def set_conversation(self, char_conversation):
            self.conversation = char_conversation

        def talk(self):
            print(f"[{self.name} says] {self.conversation}")
    
        def descrbe(self ):
            print(self.name)
            print(self.description)
        
    
    
