def create_dictionary(keys, values):
    dictionary = {}

    for i in range(len(keys)):
        dictionary[keys[i]] = values[i]

    print(dictionary)



keys = ["peanut", "dragon", "star", "pop", "space", "foot"]
values = ["butter", "fly", "fish", "corn", "ship", "ball"]
create_dictionary(keys, values)