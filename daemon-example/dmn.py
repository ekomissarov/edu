import sys
import signal
import daemon
from daemon import pidfile
from time import sleep
import os
import grp
import lockfile


class dmn:
    def __init__(self):
        self.working_directory = '/home/eugene/localsource/edu/daemon-example/'
        self.umask = 0o002
        self.pidfile = '/home/eugene/localsource/edu/daemon-example/pid_dmn.pid'
        self.filename_stdout = "/home/eugene/localsource/edu/daemon-example/stdout.txt"
        self.filename_stderr = "/home/eugene/localsource/edu/daemon-example/stderr.txt"
        self.file_stdout = None
        self.file_stderr = None

    def run(self):
        if os.path.exists(self.pidfile):
            pid = self.get_pid()
            if self.check_pid(pid):
                print("Daemon already running...")
                exit(0)

        self._initial_program_setup()

        context = daemon.DaemonContext(
            working_directory=self.working_directory,
            umask=self.umask,
            pidfile=pidfile.TimeoutPIDLockFile(self.pidfile),
        )

        context.signal_map = {
            signal.SIGTERM: self._program_cleanup,
            signal.SIGHUP: 'terminate',
            signal.SIGUSR1: self._reload_program_config,
            signal.SIGUSR2: self._get_daemon_status,
        }
        context.stdout = self.file_stdout
        context.stderr = self.file_stderr

        with context:
            self.do_main_program()

    def stop(self):
        pid = self.get_pid()
        if not pid:
            message = "Cant read pidfile {}\n"
            sys.stderr.write(message.format(self.pidfile))
            exit(1)

        try:
            while True:
                os.kill(pid, signal.SIGTERM)
                sleep(1)
        except OSError as msg:
            if str(msg).find("No such process") != -1:
                self._del_pid()
            else:
                sys.stderr.write("{}\n".format(msg))
                exit(1)

    def reload(self):
        pid = self.get_pid()
        if not pid:
            message = "Cant read pidfile {}\n"
            sys.stderr.write(message.format(self.pidfile))
            exit(1)

        try:
            os.kill(pid, signal.SIGUSR1)
        except OSError as msg:
            if str(msg).find("No such process") != -1:
                self._del_pid()
            else:
                sys.stderr.write("{}\n".format(msg))
                exit(1)

    def get_pid(self):
        try:
            pf = open(self.pidfile, 'r')
            pid = int(pf.read().strip())
            pf.close()
        except Exception as msg:
            sys.stderr.write("{}\n".format(msg))
            pid = None
        return pid

    def _del_pid(self):
        try:
            if os.path.exists(self.pidfile):
                os.remove(self.pidfile)
        except Exception as msg:
            pass

    @staticmethod
    def check_pid(pid):
        """ Check For the existence of a unix pid. """
        try:
            os.kill(pid, 0)
        except OSError:
            return False
        else:
            return True

    def _initial_program_setup(self):
        print("initial_program_setup running...")
        self.file_stdout = open(self.filename_stdout, "w+")
        self.file_stderr = open(self.filename_stderr, "w+")

    def do_main_program(self):
        while True:
            print("QKRQ!")
            sleep(10)

    def _program_cleanup(self, signum, frame):
        # https://docs.python.org/3/library/signal.html#example
        print("program_cleanup running...")
        self.file_stdout.close()
        self.file_stderr.close()
        exit(1)

    def _reload_program_config(self, signum, frame):
        # https://docs.python.org/3/library/signal.html#example
        print("reload_program_config running...")


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("run: python dmn.py (start|stop|restart|status|reload)")
        exit(1)

    if sys.argv[1] == "start":
        print("Starting daemon...")
        d = dmn()
        d.run()
    elif sys.argv[1] == "stop":
        print("Stopping daemon...")
        d = dmn()
        d.stop()
    elif sys.argv[1] == "restart":
        print("Restarting daemon...")
        d = dmn()
        d.stop()
        d.run()
    elif sys.argv[1] == "status":
        print("Daemon status...")
        d = dmn()
        pid = d.get_pid()
        if pid is None:
            print("PID not found. Daemon Stopped?")
        else:
            print("Daemon PID = {}".format(pid))
    elif sys.argv[1] == "reload":
        print("Reloading settings...")
        d = dmn()
        d.reload()
