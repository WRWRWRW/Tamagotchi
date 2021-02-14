from Pet import *
import threading
import time
import click


def user_input(input_buffer_size=10):
    global cmd
    while True:
        cmd.append(click.getchar())
        while len(cmd) > input_buffer_size:
            cmd = cmd[1:]


cmd = []
thread_user_input = threading.Thread(target=user_input)
thread_user_input.daemon = True
thread_user_input.start()

stage = []
c = Cat()
stage.append(c)
while True:
    print(cmd)
    if cmd and cmd[-1] == 'q':
        break
    cmd = []
    time.sleep(0.1)
