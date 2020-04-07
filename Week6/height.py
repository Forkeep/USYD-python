cm_to_inches = 0.393791

inches_to_feet = 12

while True:
    try:
        height_cm = input('Enter your height in cm: ')
        if not height_cm:
            break
        height_cm = float(height_cm)
        if height_cm < 0:
            raise ValueError
        feet = height_cm * cm_to_inches // inches_to_feet
        inch = height_cm * cm_to_inches % inches_to_feet
        print("You are {:.0f} feet {:.0f} inches tall!".format(feet, inch))
    except ValueError as e:
        print('Only positive numeric inputs are accepted. Please try again.')
