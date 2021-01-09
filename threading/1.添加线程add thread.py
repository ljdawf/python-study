import threading
def thread_job():
    print("this is added thread,number is %s"% threading.current_thread())

def main():
    added_thread = threading.Thread(target=thread_job)
    added_thread.start()
    print(threading.activate_count())#####看看多少激活的线程
    print(threading.enumerate())####线程数量
    print(threading.current_thread())###现在得线程
if __name__ == "__main__":
    main()