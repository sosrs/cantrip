# These are the custom functions I will use in my cantrip app


def roll(num: int, die: int, bonus: int = 0)->int:

    # This function will make a standard XdY + Z roll and return it as an integer
    # Both the number of dice and the number of sides must be positive nonzero integers
    from random import randint
    total = 0
    for i in range(num):
        total += randint(1,die)
    return total + bonus

