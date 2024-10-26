def print_pair(dictionary, target):
    print("Key: " + target)
    print("Value: " + dictionary.get(target, "That pair does not exist!"))


dictionary = {"spongebob": "squarepants", "patrick": "star", "squidward": "tentacles"}
print_pair(dictionary, "patrick")
print_pair(dictionary, "plankton")
print_pair(dictionary, "spongebob")