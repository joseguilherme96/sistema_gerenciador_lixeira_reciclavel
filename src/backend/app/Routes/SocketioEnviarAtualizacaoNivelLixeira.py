def enviar_atualizacao_nivel_lixeira(socketio,data):

    print(f"O nivel da lixeira foi alterada")
    print(data)
    socketio.emit('atualizacao_nivel_lixeira',data)