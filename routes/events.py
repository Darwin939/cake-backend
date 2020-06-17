from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio


@socketio.on('connect')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    print ("connected")
    emit('status', {'msg': ' has entered the room.'})

