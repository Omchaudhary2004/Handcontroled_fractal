import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import threading
import socket

shared_scale = {'value': 0.85}

# Fern generator
def generate_fern(scale_factor, n=50000):
    x = np.zeros(n)
    y = np.zeros(n)
    for i in range(1, n):
        r = np.random.random()
        if r < 0.01:
            x[i] = 0
            y[i] = 0.16 * y[i - 1]
        elif r < 0.86:
            x[i] = scale_factor * x[i - 1] + 0.04 * y[i - 1]
            y[i] = -0.04 * x[i - 1] + scale_factor * y[i - 1] + 1.6
        elif r < 0.93:
            x[i] = 0.2 * x[i - 1] - 0.26 * y[i - 1]
            y[i] = 0.23 * x[i - 1] + 0.22 * y[i - 1] + 1.6
        else:
            x[i] = -0.15 * x[i - 1] + 0.28 * y[i - 1]
            y[i] = 0.26 * x[i - 1] + 0.24 * y[i - 1] + 0.44
    return x, y

# Animation update
def animate(frame):
    ax.clear()
    scale = shared_scale['value']
    x, y = generate_fern(scale)
    ax.scatter(x, y, s=0.1, color='green')
    ax.set_title(f"Scale Factor: {scale:.2f}")
    ax.axis('off')

# Start animation
def start_animation():
    ani = animation.FuncAnimation(fig, animate, interval=200)
    plt.show()

# Socket listener to receive scale values
def start_socket_server():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(('localhost', 5001))
        s.listen()
        print("[Fern] Listening on port 5001")
        conn, addr = s.accept()
        with conn:
            print(f"[Fern] Connected by {addr}")
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                try:
                    new_scale = float(data.decode())
                    if 0.3 <= new_scale <= 1.5:
                        shared_scale['value'] = new_scale
                        print(f"[Fern] Updated scale to {new_scale}")
                    else:
                        print("[Fern] Invalid scale received")
                except:
                    print("[Fern] Could not parse received data")

# Setup plot
fig, ax = plt.subplots(figsize=(5, 8))

# Start threads
threading.Thread(target=start_socket_server, daemon=True).start()
start_animation()
