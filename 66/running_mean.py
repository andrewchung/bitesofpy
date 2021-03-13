import itertools
sequence = []
mean = []


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sum = 0
    for i, num in enumerate(sequence, start=1):
        sum += num
        mean.append(round(sum / i, 2))
    return(mean)


running_mean(sequence)
