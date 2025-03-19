Data Structures and Algorithms

🚀 Overview

This project provides an implementation of fundamental Data Structures and Algorithms using Python. The data structures covered in this repository include:

Stack

Queue

Deque

Singly Linked List

Circular Linked List

Doubly Linked List

Each data structure is implemented with essential operations such as insertion, deletion, searching, and traversal.

📂 Project Structure

Data-Structures-And-Algorithms/
│-- stack.py
│-- queue.py
│-- deque.py
│-- singly_linked_list.py
│-- circular_linked_list.py
│-- doubly_linked_list.py

📌 Features

✅ Object-oriented implementations using Python classes.
✅ Fully functional operations (insertion, deletion, traversal, etc.).
✅ CLI-based interactive menu for easy testing.
✅ Well-structured code with comments for readability.

⚙️ Installation & Usage

Prerequisites

Python 3.x installed on your system.

Running the Code

Clone the repository:

git clone https://github.com/jobayerhoquesiddique/Data-Structures-And-Algorithms.git

Navigate to the directory:

cd Data-Structures-And-Algorithms

Run a specific data structure file, for example:

python stack.py

📜 Data Structures Implementation

1️⃣ Stack

class Stack():
    def __init__(self):
        self.mystack = []
    def push(self, item):
        self.mystack.append(item)
    def pop(self):
        return self.mystack.pop() if self.mystack else "Stack is empty"

📌 Operations: push(), pop(), peek(), is_empty(), size()

2️⃣ Queue

class Queue():
    def __init__(self):
        self.myqueue = []
    def enqueue(self, item):
        self.myqueue.append(item)
    def dequeue(self):
        return self.myqueue.pop(0) if self.myqueue else "Queue is empty"

📌 Operations: enqueue(), dequeue(), is_empty(), size()

3️⃣ Deque

class Deque():
    def __init__(self):
        self.mydeque = []
    def add_front(self, item):
        self.mydeque.insert(0, item)
    def add_rear(self, item):
        self.mydeque.append(item)

📌 Operations: add_front(), add_rear(), remove_front(), remove_rear()

4️⃣ Singly Linked List

class Node():
    def __init__(self, item=None, next_node=None):
        self.item = item
        self.next_node = next_node

📌 Operations: append(), insert(), remove(), search()

5️⃣ Circular Linked List

class CircularLinkedList():
    def __init__(self, head=None):
        self.head = head

📌 Operations: append(), insert(), remove(), printlist()

6️⃣ Doubly Linked List

class DoublyLinkedList():
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

📌 Operations: append(), insert(), remove(), popleft(), pop()

🏆 Contribution

🔹 Fork the repository
🔹 Create a new branch (git checkout -b feature-branch)
🔹 Commit your changes (git commit -m 'Add feature')
🔹 Push the branch (git push origin feature-branch)
🔹 Open a Pull Request

📜 License

This project is licensed under the MIT License.

📌 Star the repository ⭐ if you find it helpful!

📖 Credits

Spcecial thanks to "Shohoj Bhashay Python 3 (Bangla)" written by Maksudur Rahman Maateen.

