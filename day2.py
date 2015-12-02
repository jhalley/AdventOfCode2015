# Day 2: I Was Told There Would Be No Math

def amt_of_wrapping_paper():
    presents = []
    total = 0

    filename = raw_input('Enter filename: ')
    with open(filename) as f:
        presents = [i.strip() for i in f.readlines()]

    for present in presents:
        l, w, h = sorted([int(i) for i in present.split('x')])
        total += 2*l*w + 2*w*h + 2*h*l + l*w

    print total


def amt_of_ribbon():
    presents = []
    total = 0

    filename = raw_input('Enter filename: ')
    with open(filename) as f:
        presents = [i.strip() for i in f.readlines()]

    for present in presents:
        l, w, h = sorted([int(i) for i in present.split('x')])
        total += 2*l + 2*w + l*w*h;

    print total

# amt_of_wrapping_paper()
amt_of_ribbon()