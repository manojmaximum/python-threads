# python-threads
This repo is to explore the Threading in Python

## Requirement
Make threads to print sequence of numbers until stopped. The threads should be started, and each thread should print a number in the sequence and go to sleep and another thread should print the next number in the sequence and then go to sleep.

## Developer Environment
1. Python 3.10
2. No virtual environment is needed for the program as no additional packages are used, as only the default packages of threading, logging and time are used

## Executing the program
Currently, only one program file is complete, which uses a global variable as shared variable between the threads, and satisfies the above requirement.
Ensuring that the above developer environment is available, please use `python .\thread-ex.py`. 

## References:
1.[Sample program which is used and edited to satisfy the requirement](https://realpython.com/intro-to-python-threading/#working-with-many-threads)
