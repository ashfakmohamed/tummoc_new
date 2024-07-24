def is_valid_credit_card(number):
    number_str = str(number)
    
    if len(number_str) not in [13, 15, 16]:
        return False
    
    if (number_str.startswith('4') and len(number_str) not in [13, 16]) or \
       (number_str.startswith('5') and len(number_str) != 16) or \
       (number_str.startswith('37') and len(number_str) != 15) or \
       (number_str.startswith('6') and len(number_str) != 16):
        return False
    
    total = 0
    is_second = False
    
    for i in range(len(number_str) - 1, -1, -1):
        digit = int(number_str[i])
        
        if is_second:
            digit *= 2
            if digit > 9:
                digit -= 9
        
        total += digit
        is_second = not is_second
    
    return total % 10 == 0


while True:
    try:
        card_number = int(input("Enter a credit card number (or 0 to exit): "))
        if card_number == 0:
            break
        
        if is_valid_credit_card(card_number):
            print("Valid credit card number.")
        else:
            print("Invalid credit card number.")
    except ValueError:
        print("Please enter a valid integer.")

print("Program ended.")