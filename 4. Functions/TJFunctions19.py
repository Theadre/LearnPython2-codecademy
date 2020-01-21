num = -50
word = "test"


def distance_from_zero(num):
    if type(num) == int or type(num) == float:
        return abs(num)
    else:
        return "Nope"


print(distance_from_zero(num))
print(distance_from_zero(word))