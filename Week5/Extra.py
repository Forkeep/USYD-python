def nonsense(func):
    func('The answer to life, the universe and everything: ', end='')
    return int
print(nonsense(print)('42'))  # what is going on??