class Pokemon:
    def __init__(self, name, types, evolution = None):
        self.name = name
        self.types = types
        self.is_caught = False
        self.evolution = evolution
    
    def print_pokemon(self):
        print({
            "name": self.name,   # Output: "name": "Squirtle",
            "types": self.types, # Output: "types": ["Water"],
            "is_caught": self.is_caught # Output: "is_caught": False
        })
    
    def catch(self):
        self.is_caught = True
    
    def choose(self):
        if self.is_caught == True:
            print(f"{self.name} I choose you!")
        else:
            print(f"{self.name} is wild! Catch them if you can!")
        

    def add_type(self, new_type):
        self.types.append(new_type)

# my_pokemon = Pokemon("Pikachu", ["Electric"])

# squirtle = Pokemon("Squirtle", ["Water"])
# squirtle.print_pokemon()

# squirtle.is_caught = True
# squirtle.print_pokemon()

# rat = Pokemon("Rattata", ["Normal"])
# rat.print_pokemon()

# rat.choose()
# rat.catch()
# rat.choose()
# rat.print_pokemon()

# jigglypuff = Pokemon("Jigglypuff", ["Normal"])
# jigglypuff.print_pokemon()

# jigglypuff.add_type("Fairy")
# jigglypuff.print_pokemon()
  
"""
Understand:
- Write method get_by_type that takes in parameters pokemon_list, list
of pokemon instances and pokemon_type a String attribute.
- Return a sublist of pokemon_list with pokemon that have the attribute
pokemon_type.
Plan:
- Create a empty list, type_list.
- Iterate through pokemon_list, for loop.
- Check each pokemon's types, if at least one of those types are pokemon_type,
append the name of the pokemon to pokemon_list.
- Return pokemon_list.
Implement:
"""
def get_by_type(pokemon_list, pokemon_type):
    type_list = []

    for pokemon in pokemon_list:
        if pokemon_type in pokemon.types:
            type_list.append(pokemon.name)
    
    return type_list


# # initializing pokemons
# jigglypuff = Pokemon("Jigglypuff", ["Normal", "Fairy"])
# diglett = Pokemon("Diglett", ["Ground"])
# meowth = Pokemon("Meowth", ["Normal"])
# pidgeot = Pokemon("Pidgeot", ["Normal", "Flying"])
# blastoise = Pokemon("Blastoise", ["Water"])

# my_pokemon = [jigglypuff, diglett, meowth, pidgeot, blastoise]
# normal_pokemon = get_by_type(my_pokemon, "Normal")
# print(normal_pokemon)


"""
Understand:
- Write function get_evolutionary_line() that takes in parameters, 
starter_pokemon, a Pokemon instance.
- Returns all the evolutions that the pokemon can evolve to.
Plan:
- Create a Pokemon variable, pokemon, intialized to starter_pokemon.
- Create a list, evolution_list, initalized to pokemon.name.
- While pokemon.evolution != None.
- Append the pokemon evolution's name to
evolution_list and intialize pokemon to the evolution.
- Return evolution_list.
Implement:
"""
def get_evolutionary_line(starter_pokemon):
    pokemon = starter_pokemon
    evolution_list = [pokemon.name]

    while pokemon.evolution != None:
        evolution_list.append(pokemon.evolution.name)
        pokemon = pokemon.evolution
    
    return evolution_list

charizard = Pokemon("Charizard", ["fire", "flying"])
charmeleon = Pokemon("Charmeleon", ["fire"], charizard)
charmander = Pokemon("Charmander", ["fire"], charmeleon)

charmander_list = get_evolutionary_line(charmander)
print(charmander_list)

charmeleon_list = get_evolutionary_line(charmeleon)
print(charmeleon_list)

charizard_list = get_evolutionary_line(charizard)
print(charizard_list)




