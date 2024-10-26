"""
Understand:
- Write method attack() that takes in paratmer Pokemon object opponent and
decreases oppoenent's hp by self's damage amount.
- If damaging leads to oppoenent having hp of 0 or less, print 
"<Oppenent name> fained>"
- Otherwise, print "<Pokemon name> dealt <damage> damage to <opponenent name>"

Plan:
- Initialize oppenent's hp to oppenent hp - damage amount (self)
- If oppoenent hp is <=0, set hp to 0 and print "<Oppenent name> fained>"
- Otherwise, print "<Pokemon name> dealt <damage> damage to <opponenent name>"
Implement:
"""

class Pokemon():
	def  __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp # hit points
		self.damage = damage # The amount of damage this pokemon does to its opponent every attack
		
	def attack(self, opponent):
		opponent.hp -= self.damage

		if opponent.hp <= 0:
			opponent.hp = 0
			print(f"{opponent.name} fainted")
		else:
			print(f"{self.name} dealt {self.damage} damage to {opponent.name}")


pikachu = Pokemon("Pikachu", 35, 50)
bulbasaur = Pokemon("Bulbasaur", 45, 30) 

opponent = bulbasaur
pikachu.attack(opponent)




