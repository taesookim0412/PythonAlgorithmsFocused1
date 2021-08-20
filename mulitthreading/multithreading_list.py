import threading
import time
lock = threading.Lock()

# with lock is the same as lock.acquire(), lock.release() without the context manager.
def thread_a(vals, ct=0):
    print("\n", vals, "a", "\n")
    if ct == 10:
        return
    with lock:
        vals[0] += 1
    time.sleep(0.1)
    thread_a(vals, ct + 1)


def thread_b(vals, ct=0):
    print("\n", vals, "b", "\n")
    if ct == 10:
        return
    with lock:
        vals[0] += 1
    time.sleep(0.1)
    thread_b(vals, ct + 1)


def main():
    vals = [1,2,3,4,5]
    val_thread_a = threading.Thread(target=thread_a, args=(vals,))
    val_thread_b = threading.Thread(target=thread_b, args=(vals,))
    val_thread_a.start()
    val_thread_b.start()




if __name__ == "__main__":
    main()