MINIMA = 21


def idade_permitida(idade):
    if type(idade) is not int:
        return False
    return MINIMA <= idade <= 100
