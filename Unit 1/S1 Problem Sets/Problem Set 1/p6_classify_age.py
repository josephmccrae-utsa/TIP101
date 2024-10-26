def classify_age(age):
    if(age < 18):
        return "child"
    else:
        return "adult"
    
output = classify_age(18)
print(output)
output = classify_age(7)
print(output)
output = classify_age(50)
print(output)