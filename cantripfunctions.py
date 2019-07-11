# These are the custom functions I will use in my cantrip app
skillSet = {'Athletics','Acrobatics','Sleight of Hand','Stealth,','Arcana','History','Investigation','Nature',
            'Religion','Animal Handling','Insight','Medicine','Perception','Survival','Deception','Intimidation',
            'Performance','Persuasion'}
conditionSet = {'Blinded','Charmed','Deafened','Fatigued','Frightened','Grappled','Incapacitated','Invisible',
                'Paralyzed','Petrified','Poisoned','Prone','Restrained','Stunned','Unconscious','Exhaustion'}

def roll(num: int, die: int, bonus: int = 0)->int:

    # This function will make a standard XdY + Z roll and return it as an integer
    # Both the number of dice and the number of sides must be positive nonzero integers
    from random import randint
    total = 0
    for i in range(num):
        total += randint(1,die)
    return total + bonus

class Char:
    def __init__(self,name,STR,DEX,CON,INT,WIS,CHA):
        self.name = name
        self.status = []
        self.STR = STR
        self.DEX = DEX
        self.CON = CON
        self.INT = INT
        self.WIS = WIS
        self.CHA = CHA
        self.skillProf = set()
        self.condition = set()


