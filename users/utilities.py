def chinese_zodiac_sign(year):
    zodiac_signs = ["Rat", "Ox", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Goat", "Monkey", "Rooster", "Dog", "Pig"]
    return zodiac_signs[(year - 1900) % 12]