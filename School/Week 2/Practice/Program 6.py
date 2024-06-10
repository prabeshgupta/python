#Nested dictionary

student = {
    "grades":{
        "Science": 20,
        "Math":30,
        "Nepali": 60,
        "English": 64
    }
}

print(student["grades"].get("English"))