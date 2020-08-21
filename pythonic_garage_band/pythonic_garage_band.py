from abc import abstractmethod

class Band:
    
    members = []

    class Musician():
    
        def __init__(self,name):
            self.name = name
            Band.members.append(self.name)
        
        @classmethod
        def play_solos(self):
            result = ''
            for i in Band.members:
                result += f'{i} play a solos\n'
            return result
        
        @abstractmethod
        def __str__(self):
            return f"Musician <{self.name}>"
        
        @abstractmethod
        def __repr__(self):
            return f" '{self.name}' "
        
        def to_list(self):
            return Band.members
    
    
    class Guitarist(Musician):
        
        def __init__(self,name):
            super().__init__(name)

        def __str__(self):
            return f"Guitarist <{self.name}>"
        
        def __repr__(self):
            return f" '{self.name}' "
        
        def get_instrument(self):
            return 'Guitarist'
        
        def play_solo(self):
            return 'Play Guitar'
    
    
    class Bassist(Musician):
        
        def __init__(self,name):
            super().__init__(name)
        
        def __str__(self):
            return f"Bassist <{self.name}>"
        
        def __repr__(self):
            return f" '{self.name}' "
        
        def get_instrument(self):
            return 'Bassist'
        
        def play_solo(self):
            return 'Play Bassist'
    
    
    class Drummer(Musician):
        
        def __init__(self,name):
            super().__init__(name)
        
        def __str__(self):
            return f"Drummer <{self.name}>"
        
        def __repr__(self):
            return f" '{self.name}' "
        
        def get_instrument(self):
            return 'Drummer'
        
        def play_solo(self):
            return 'Dom Dum Dom Dum'



if __name__ == "__main__":
    emad = Band.Bassist('Emad')
    aziz = Band.Guitarist('Aziz')
    saleh = Band.Drummer('Saleh')
    print(emad)
    print(emad.get_instrument())
    print(aziz)
    print(aziz.get_instrument())
    print(saleh)
    print(saleh.get_instrument())
    print(emad.play_solo())
    print(aziz.play_solo())
    print(saleh.play_solo())
    print(Band.members)
    print(emad.play_solos())