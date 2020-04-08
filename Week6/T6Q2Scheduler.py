def set_meeting(time):  # Fill this in...# Should print: You have a meeting at 0900 hrs. Don't forget!
    try:
        if not isinstance(time, int):
            raise TypeError
        time_ = int(time)
        if  not time_ in range(0,2360):
            raise ValueError('Error: time must be between 0000 hrs and 2359 hrs.')
        if not time_ in range(800,2200):
            raise  ValueError('No...I\'m sleeping...')
        print('You have a meeting at {:0>4} hrs. Don\'t forget!'.format(time_))
    except TypeError:
        print('Error: time must be an integer')
    except ValueError as e:
        print(e)

set_meeting(912)
