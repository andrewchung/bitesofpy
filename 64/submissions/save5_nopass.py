import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    x = []
    for participant in itertools.zip_longest(names, locations, confirmed):
        y = list(participant)
        if y[1] is None:
            y[1] = '-'
        if y[2] is None:
            y[2] = '-'
        participant = tuple(y)
        z = str(participant)
        x.append(''.join(z))
    return(x)



if __name__ == '__main__':
    get_attendees()