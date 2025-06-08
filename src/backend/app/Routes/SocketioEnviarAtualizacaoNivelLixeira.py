def enviar_atualizacao_nivel_lixeira(socketio,data):

    socketio.emit('atualizacao_lixeira',data)