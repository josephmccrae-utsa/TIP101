def highest_rated(books):
    highest_book = {}
    highest_rating = 0
    for book in books:
        if book["rating"] > highest_rating:
            highest_book = book
            highest_rating = book["rating"]
    
    return highest_book


books = [
    {"title": "Tomorrow, and Tomorrow, and Tomorrow",
     "author": "Gabrielle Zevin",
     "rating": 4.18
    },
    {"title": "A Fortune For Your Disaster",
     "author": "Hanif Abdurraqib",
     "rating": 4.47
    },
    {"title": "The Seven Husbands of Evenlyn Hugo",
     "author": "Taylor Jenkins Reid",
     "rating": 4.40
    }
]

print(highest_rated(books))