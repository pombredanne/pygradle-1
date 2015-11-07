import subprocess


def call_system_command_async(cmd):
    return subprocess.Popen(cmd, stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT, shell=True)


def call_system_command(cmd):
    return call_system_command_async(cmd).communicate()[0].decode('ascii')
