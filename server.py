from flask import Flask, render_template
from flask_socketio import SocketIO, emit, join_room, leave_room

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@app.route("/")
def index():
    return render_template("index.html")


@socketio.on("message")
def handle_message(data):
    emit("message", data, broadcast=True)


@socketio.on("join")
def on_join(data):
    username = data["username"]
    room = data["room"]
    join_room(room)
    emit(
        "message",
        {"username": "Server", "message": f"{username} has entered the room."},
        room=room,
    )


@socketio.on("leave")
def on_leave(data):
    username = data["username"]
    room = data["room"]
    leave_room(room)
    emit(
        "message",
        {"username": "Server", "message": f"{username} has left the room."},
        room=room,
    )


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", port=5555)
