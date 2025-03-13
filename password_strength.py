import re
import random
def check_password_strength(password):
    score = 0
    message = []
    if(len(password) >= 8):
        score+= 1
    else:
        message.append("❌ Password should be at least 8 characters long.")
    
    if re.search(r"[A-Z]", password) and re.search(r"[a-z]", password):
        score += 1
    else:
       message.append( "❌ Password must contains both uppercase and lowercase. 🆎")
      
    if re.search(r"\d",password):
        score += 2
    else:
        message.append("❌ Add atleast one digit (0-9).")
    
    if re.search(r"[!@##$%^&*():~`;'><?/']", password):
        score += 1
    else:
        message.append("❌ Add atleast one special character to make your password strong. (!@##$%^&*():~`;'><?/')")
        
    return score, message
        
        
        
def password_generator(length):
    if length < 4:
        raise ValueError("Length should be at least 4 to include all character types.")
    
    lower = random.choice("abcdefghijklmnopqrstuvwxyz")
    upper = random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    digit = random.choice("0123456789")
    special = random.choice("!@#$%^&*()_+-=[]{}|;':\",.<>?/")
    
    # Ensure the password has at least one of each type
    password = lower + upper + digit + special
    
    # Fill the rest of the password length with random choices from all characters
    all_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+-=[]{}|;':\",.<>?/"
    password += "".join(random.choice(all_chars) for _ in range(length - 4))
    
    # Shuffle the password to ensure randomness
    password = ''.join(random.sample(password, len(password)))
    
    return password
