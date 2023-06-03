import re

def analyze_password_strength(password):
    score = 0
    if len(password) >= 8: score += 1
    if re.search(r'[A-Z]', password): score += 1
    if re.search(r'[a-z]', password): score += 1
    if re.search(r'\d', password): score += 1
    if re.search(r'[@$!%*?&]', password): score += 1
    
    return score


def get_password_strength_label(score):
    if score == 0: return 'Very Weak'
    elif score == 1: return 'Weak'
    elif score == 2: return 'Moderate'
    elif score == 3: return 'Strong'
    elif score == 4: return 'Very Strong'
    else: return 'Invalid'


password = input("Enter a password: ")
strength_score = analyze_password_strength(password)
strength_label = get_password_strength_label(strength_score)
print("Password Strength Status:", strength_label)
