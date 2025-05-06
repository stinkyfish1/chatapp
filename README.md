Here's a basic technical documentation (TechDocs) for your chat application project, covering the architecture, components, setup, usage, and how to extend it further:

---

# 📡 Socket Chat Application – TechDocs

## 🧩 Overview

This project is a **multi-client chat application** built using **Python's socket and threading libraries**. It consists of two core components:

* A **Server** that manages multiple clients and handles broadcasting messages.
* A **Client** that connects to the server and sends/receives messages in real-time.

---

## 📁 Project Structure

```
chat-app/
├── client.py      # Client-side logic
├── server.py      # Server-side logic
```

---

## 🔧 Technologies Used

* Python 3.x
* `socket` module for TCP communication
* `threading` module for concurrency

---

## 🚀 How It Works

### Server (`server.py`)

* Listens for incoming client connections.
* Accepts client names and stores their sockets.
* Spawns a new thread for each client to listen for messages.
* Broadcasts incoming messages to all connected clients.
* Cleans up when a client disconnects.

### Client (`client.py`)

* Connects to the server using a user-specified hostname and port.
* Sends the user's name to the server.
* Starts two threads:

  * One for **sending** user input.
  * One for **receiving** and displaying incoming messages.
* Disconnects gracefully when user types `bye`.

---

## ⚙️ Installation & Setup

### Requirements

* Python 3.x

### 1. Start the Server

On your server or local machine:

```bash
python3 server.py
```

### 2. Start the Client

On each client machine:

```bash
python3 client.py
```

You'll be prompted to enter your name before joining the chat.

> **Note:** Update the `HOST` variable in `client.py` to point to your server's IP or hostname.

---

## 🧪 Example Usage

**Server Terminal Output:**

```
Server waiting for connections....
New connection from ('127.0.0.1', 55666)
```

**Client 1:**

```
Enter your name: Alice
Alice: Hello everyone!
```

**Client 2:**

```
Enter your name: Bob
Bob: Hi Alice!
```

---

## 🧯 Graceful Exit

Clients can leave the chat anytime by typing:

```bash
bye
```

---

## 🎨 Features

* Real-time message broadcasting
* Username-based identification
* Graceful join/leave notifications
* Colored incoming messages for visibility (red with ANSI escape codes)

---

## 🛠️ Possible Improvements

* Add authentication or unique client IDs
* Use message formatting (timestamps, emojis, etc.)
* Upgrade to use asynchronous sockets (`asyncio`)
* Add GUI (e.g., with `tkinter` or `PyQt`)
* Support private messaging (DMs)
* Store chat history in a file or database

---

## 📌 Troubleshooting

| Issue                    | Solution                                          |
| ------------------------ | ------------------------------------------------- |
| `ConnectionRefusedError` | Make sure the server is running and reachable     |
| Messages not showing     | Check firewall settings or NAT configurations     |
| Crashes on disconnect    | Ensure `recv()` and `send()` are properly wrapped |

---
