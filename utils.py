"""This is the chest its got junk and treasures so get out."""

import colors as c

"""---------------------------------------"""

def ask(question):
    print(question)
    answer = input('> ').strip().lower()
    print(c.reset)
    return answer

"""---------------------------------------"""

if __name__ == '__main__':
    print(c.clear)
    name = ask("what is your name?")
    color = ask ("what is your name in color?",c.random_color())

"""-----------------------------------"""

