import signal
import daemon
from daemon import pidfile
from time import sleep
import os
import grp
import lockfile


def initial_program_setup():
    print("initial_program_setup running...")


def do_main_program():
    while True:
        print("QKRQ!")
        sleep(10)


def program_cleanup(signum, frame):
    # https://docs.python.org/3/library/signal.html#example
    print("program_cleanup running...")


def reload_program_config(signum, frame):
    # https://docs.python.org/3/library/signal.html#example
    print("reload_program_config running...")


if __name__ == '__main__':

    file_stdout = open("/home/eugene/localsource/edu/daemon-example/out.txt", "w+")

    context = daemon.DaemonContext(
        working_directory='/home/eugene/localsource/edu/daemon-example/',
        umask=0o002,
        pidfile=pidfile.TimeoutPIDLockFile('/home/eugene/localsource/edu/daemon-example/pid_dmn.pid'),
        )

    context.signal_map = {
        signal.SIGTERM: program_cleanup,
        signal.SIGHUP: 'terminate',
        signal.SIGUSR1: reload_program_config,
        }
    context.stdout = file_stdout

    initial_program_setup()

    with context:
        do_main_program()
