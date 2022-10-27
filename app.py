from flask import Flask
from flask_socketio import SocketIO, send, emit
import random

app = Flask(__name__)
app.config["SECRET_KEY"] = 'super secret key'
socketio = SocketIO(app)

def create_client_id():
    first_num = random.randint(100,200) * random.randint(200, 300)
    final_num = first_num // random.randint(5, 15)
    return final_num

@socketio.on('connect')
def test_connect(auth):
    print('client has connected')
    send('connected')
    
@socketio.on('recieve_id')
def handle_client_recvid():
    emit('accept_id', {"id": str(create_client_id())})

@socketio.on('test_custom_event')
def handle_message(event):
    print(f'recieved json {str(event)}')
    #client_id = event["client_id"]
    #message = event["message"]
    emit('ios_client_event', event, broadcast=True)
    
@socketio.on('get_hand')
def handle_deal_hand(client_id):
    if client_id == '08281':
        emit('ios_client_event', {'message': 'HAND: Ace of hearts, Jack of Diamond'})
    
if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0")