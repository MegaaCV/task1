import datetime

def get_greeting():
    hour = datetime.datetime.now().hour
    
    if 5 <= hour < 12:
        return "Good morning"
    elif 12 <= hour < 17:
        return "Good afternoon"
    elif 17 <= hour < 21:
        return "Good evening"
    else:
        return "Good night"

def age_message(age):
    age = int(age)
    if age < 18:
        return "You have a bright future ahead. Keep learning and exploring."
    elif age <= 25:
        return "This is a great age to build skills and shape your career."
    elif age <= 35:
        return "You are in a wonderful phase to grow professionally and personally."
    elif age <= 50:
        return "Your experience brings both strength and maturity."
    else:
        return "Your knowledge and life experience are truly inspiring."

def hobby_suggestion(hobby):
    hobby = hobby.lower()

    if "music" in hobby:
        return "You might enjoy exploring new playlists or learning an instrument."
    elif "reading" in hobby:
        return "You can try Goodreads to discover new books based on your interests."
    elif "coding" in hobby or "programming" in hobby:
        return "You could explore competitive programming or contribute to open source."
    elif "drawing" in hobby or "art" in hobby:
        return "Digital art platforms like Procreate can help enhance your skills."
    elif "sports" in hobby:
        return "You may enjoy joining local clubs or playing outdoor games regularly."
    elif "gardening" in hobby:
        return "Growing seasonal plants can make your garden even more lively."
    elif "photography" in hobby:
        return "Experimenting with angles and natural light can improve your shots."
    elif "cooking" in hobby:
        return "Trying new recipes can improve your creativity in the kitchen."
    elif "travel" in hobby or "travelling" in hobby:
        return "Exploring new cultures can be a great way to learn and relax."
    elif "gaming" in hobby:
        return "You can try strategy-based games to improve decision-making skills."
    elif "writing" in hobby:
        return "Writing daily journals can improve your creativity and expression."
    elif "dance" in hobby or "dancing" in hobby:
        return "Practicing regularly to different rhythms can boost your skills."
    else:
        return "That is a wonderful hobby. Keep exploring it."

print("=== Personal Introduction Program ===\n")

name = input("Enter your name: ").strip()
while not name.replace(" ", "").isalpha():
    name = input("Please enter a valid name (letters only): ").strip()

age = input("Enter your age: ").strip()
while not age.isdigit() or int(age) <= 0:
    age = input("Please enter a valid positive number for age: ").strip()

hobby = input("Enter your hobby: ").strip()

print("\n------------------------------------")
print(f"{get_greeting()}, {name}.")
print(f"You are {age} years old and your hobby is {hobby}.")
print(age_message(age))
print(hobby_suggestion(hobby))
print("------------------------------------")

with open("user_info.txt", "a") as f:
    f.write(f"{name}, {age}, {hobby}\n")

