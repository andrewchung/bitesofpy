import itertools


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sum = 0
    running_mean = []

    for i, num in enumerate(sequence, start=1):
        sum += num
        running_mean.append(round(sum / i, 2))

    return(running_mean)


running_mean(sequence=[3, 4, 6, 2, 1, 9, 0, 7, 5, 8])
