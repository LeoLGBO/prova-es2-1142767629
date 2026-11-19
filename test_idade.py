from idade import idade_permitida


def test_aceita_idade_exatamente_no_limite_minimo_21():
    # preparar
    idade = 21
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is True


def test_rejeita_idade_abaixo_do_limite_20():
    # preparar
    idade = 20
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is False


def test_rejeita_idade_acima_de_100():
    # preparar
    idade = 101
    # agir
    resultado = idade_permitida(idade)
    # verificar
    assert resultado is False


def test_rejeita_idade_que_nao_e_numero_inteiro():
    # preparar: float, texto e bool, todos dentro da faixa 21 a 100
    idades_invalidas = [25.5, "30", True]
    for idade in idades_invalidas:
        # agir
        resultado = idade_permitida(idade)
        # verificar
        assert resultado is False
