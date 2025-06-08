def enviar_observacao_lixeira(socketio,data):
    
    socketio.emit('atualizacao_observacao_lixeira',data)