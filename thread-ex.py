import logging
import threading
import time


def another_function(name):
    '''
    A function which is just used as the target function of a thread, which is assigned to the thread after the start of a thread
    This function is used to manipulate the global variable, which is accessed by all the threads
    '''
    
    global num
    num=num+1
    logging.info(f"Thread {name}: In Another function")
    logging.info(f"Thread {name}: printing {str(num)}")
    time.sleep(2)


def thread_function(name):
    '''
    A function which is just used as the target function of a thread, which is assigned to the thread, during the start of a thread
    '''
    time.sleep(2)
    logging.info(f"Thread {name}: starting")


if __name__ == "__main__":
    
    num_of_threads=5
    num=0
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO,
                        datefmt="%H:%M:%S")

    threads = list()
    for index in range(num_of_threads):
        logging.info(f"Main    : create and start thread {index}.", )
        x = threading.Thread(target=thread_function, args=(index,))
        threads.append(x)
        x.start()
    
    try:
        while 1:
            for index, thread in enumerate(threads):
                x._target=another_function(index) ## accessing the intended private function is a bad design, but used instead writing Object oriented way of using threads and queues to achieve the functionality
    except KeyboardInterrupt:
        for index, thread in enumerate(threads):
            logging.info(f"Main    : before joining thread {index}.")
            thread.join()
            logging.info(f"Main    : thread {index} done")