from ambientes.ambiente_robo_reciclador import AmbienteRoboReciclador
from agentes.agente_aleatorio import AgenteAleatorio

def main():
    # Criar o ambiente
    ambiente = AmbienteRoboReciclador()
    
    # Criar o agente
    agente = AgenteAleatorio(ambiente.espaco_acoes)

    # Rodar episódios
    num_episodios = 10
    for episodio in range(num_episodios):
        estado = ambiente.resetar()
        terminou = False
        recompensa_total = 0

        while not terminou:
            acao = agente.agir(estado)
            estado, recompensa, terminou, info = ambiente.executar_acao(acao)
            recompensa_total += recompensa
            ambiente.renderizar()

        print(f"Episódio {episodio + 1}: Recompensa total = {recompensa_total}")

    ambiente.close()

if __name__ == "__main__":
    main()
