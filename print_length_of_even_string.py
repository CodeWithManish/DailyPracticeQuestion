"""
print even length words
"""


def even_str(my_str):
    my_str = my_str.split(' ')
    for word in my_str:
        if len(word) % 2 == 0:
            print(word)
    return word


if __name__ == '__main__':
    my_str = "today is a great day to work with python"
    even_str(my_str)
