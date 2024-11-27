from ambientes.ambiente_robo_reciclador import AmbienteRoboReciclador

def testar_ambiente():
    ambiente = AmbienteRoboReciclador()
    estado = ambiente.resetar()
    assert len(estado) == 5, "O estado inicial deve ter 5 elementos"

    espaco_acoes = ambiente.espaco_acoes.n
    assert espaco_acoes == 5, "O espaço de ações deve conter 5 ações"

    print("Todos os testes passaram!")

if __name__ == "__main__":
    testar_ambiente()
