def enviar_observacao_lixeira(socketio,data):

    print(f"Foi adicionado uma nova observação !")
    print(data)
    socketio.emit('atualizacao_observacao_lixeira',data)