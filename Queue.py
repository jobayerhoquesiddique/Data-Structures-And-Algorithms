class Queue():
    """
    @description: This class defines several methods for Queue.
    """

    def __init__(self):
        # defining a list which will act as queue container
        self.myqueue = []

    def size(self):
        # returns the size of the queue
        return len(self.myqueue)

    def is_empty(self):
        # checks whether the queue is empty or not
        if self.size() > 0:
            return False
        else:
            return True

    def enqueue(self, item):
        # enqueue a item to the defined queue
        # insert(0, item) will insert "item" to the 0th position of the defined
        # list
        return self.myqueue.append(item)

    def dequeue(self):
        # dequeue an item from defined queue
        if self.is_empty():
            print("Sorry, the queue is empty.")
        else:
            return self.myqueue.pop(0)


def main():
    # defining the main function for the queue
    q = Queue()
    # q is an object of Queue class
    while True:
        print("1. Enqueue \n2. Dequeue \n3. Show \n4. Quit")
        print("\nWhat do you wanna do now?")
        case = int(input())
        # starting something, equivalent to Switch statement in C/C++
        if case == 1:
            # in this case, we will call our enqueue method
            print("Input item, you wanna enqueue:")
            item = input()
            q.enqueue(item)
            print("Congrats!", item, "has been enqueued.")
        elif case == 2:
            # in this case, we will call our dequeue method
            if q.is_empty():
                print("Sorry, the queue is empty.")
            else:
                print(q.dequeue(), "has been dequeued.")
        elif case == 3:
            # in this case, we will print the current condition of our queue
            if q.is_empty():
                print("Sorry, the queue is empty.")
            else:
                print("The current condition of our queue:",
                      q.myqueue)
        elif case == 4:
            # in this case, we will quit our script
            print("The script is gonna quit.")
            quit()
        else:
            print("Oops! Wrong Choice.")
            main()

if __name__ == "__main__":
    main()