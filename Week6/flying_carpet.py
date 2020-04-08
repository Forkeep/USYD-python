import T6Q4CarpetFitter

print('First carpet:')
width1 = eval(input('Enter the length:'))
length1 = eval(input('Enter the width:'))

print('Second carpet:')
width2 = eval(input('Enter the length:'))
length2 = eval(input('Enter the width:'))

area1 = T6Q4CarpetFitter.carpet_area(length1, width1)
area2 = T6Q4CarpetFitter.carpet_area(length2, width2)

if  area2 and area1:
    if area1 > area2:
        print('The first carpet is larger! Get onboard!')
    else:
        print('The second carpet is larger! Get onboard!')


