def calculate_gpa(report_card):
    sum = 0
    count = 0
    for value in report_card.values():
        if value == "A":
            sum += 4
        elif value == "B":
            sum += 3
        elif value == "C":
            sum += 2
        elif value == "D":
            sum += 1
        else:
            sum += 0
        count += 1

    return round(sum / count, 2)

report_card = {"Math": "A", "Science": "C", "History": "A", "Art": "B", "English": "B", "Spanish": "A"}
print(calculate_gpa(report_card))