def get_initials(fullname):
    """ Given a person's name, returns the person's initials (uppercase) """
    # Grab the first char as first initial    
    inits = fullname[0]

    # Initialize a counter for the loop (should be a more elegant way?)
    position = 0
    
    # Traverse the string, and when a space is found add the next char as another initial
    for char in fullname:
        if char == ' ':
            inits += fullname[position+1]
        position += 1
    # Capitalize the string
    uppercase_inits = inits.upper()
    
    return uppercase_inits

def main():
    user_name = input("What is your full name?\n")

    print(get_initials(user_name))

if __name__ == "__main__":
  main()