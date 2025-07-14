class Vault:
    def __init__(self, galleons=0, sickles=0, knuts=0):
        self.galleons = galleons
        self.sikles = sickles
        self.knuts = knuts

    def __str__(self) -> str:
        return f"{self.galleons} Galleons, {self.sikles} Sikles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons        
        sikles = self.sikles + other.sikles        
        knuts = self.knuts + other.knuts
        return Vault(galleons, sikles, knuts)
        

potter = Vault(100, 50, 25)
print(potter)

weasly = Vault(25, 50, 100)
print(weasly)

total = potter + weasly
print(total)