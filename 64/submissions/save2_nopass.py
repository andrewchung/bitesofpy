import itertools

names = 'Tim Bob Julian Carmen Sofia Mike Kim Andre'.split()
locations = 'DE ES AUS NL BR US'.split()
confirmed = [False, True, True, False, True]


def get_attendees():
    for participant in itertools.zip_longest(names, locations, confirmed):
        participant = list(participant)
        if participant[1] is None:
            participant[1] = '-'
        if participant[2] is None:
            participant[2] = '-'
        y = tuple(participant)
        return(y)


if __name__ == '__main__':
    get_attendees()