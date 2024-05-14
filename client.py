import socket
import threading


# Fungsi untuk menerima pesan dari server
def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")
            if message == "Enter your name: ":
                client_socket.send(name.encode("utf-8"))
            else:
                print(message)
        except:
            print("Connection lost")
            client_socket.close()
            break


# Inisialisasi klien
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("127.0.0.1", 5555))

# Ambil nama pengguna
name = input("Enter your name: ")

# Mulai thread untuk menerima pesan
receive_thread = threading.Thread(target=receive_messages, args=(client,))
receive_thread.start()

# Kirim pesan ke server
while True:
    message = input(f"{name}: ")
    if message.lower() == "quit":
        client.close()
        break
    client.send(message.encode("utf-8"))
