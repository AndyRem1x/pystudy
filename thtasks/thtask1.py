import threading

counter = 0
rounds = 100000
lock = threading.Lock()


class Counter(threading.Thread):
    def run(self):
        global counter
        global rounds
        for _ in range(rounds):
            with lock:
                counter += 1


if __name__ == "__main__":
    thread1 = Counter()
    thread2 = Counter()

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(f"Final Counter Value: {counter}")
