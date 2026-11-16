"""Фікстури pytest: iperf3-сервер на PC2 через SSH (paramiko) і клієнт на PC1."""
import os
import subprocess
import time

import paramiko
import pytest

server_ip = os.getenv('SERVER_IP', '192.168.1.2')
username = os.getenv('SERVER_USER', 'murmurhash')
key_file = os.path.expanduser('~/.ssh/id_lab7')   # вхід по ключу, пароль у коді не зберігається


@pytest.fixture(scope='function')
def server():
    """Підключається до PC2 по SSH і піднімає iperf3-сервер.
    Повертає повідомлення про помилку сервера (порожнє, якщо все добре).
    Після тесту зупиняє сервер і закриває SSH-з'єднання."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(server_ip, username=username, key_filename=key_file, timeout=5)
    _, stdout, stderr = ssh.exec_command('iperf3 -s -D -1')
    stdout.channel.recv_exit_status()
    error = stderr.read().decode().strip()
    time.sleep(1)
    yield error
    ssh.exec_command('pkill -f "iperf3 -s"')[1].channel.recv_exit_status()
    ssh.close()


@pytest.fixture(scope='function')
def client(server):
    """Запускає iperf3-клієнт через subprocess. Повертає (вивід, помилка)."""
    proc = subprocess.Popen(['iperf3', '-c', server_ip, '-t', '10', '-i', '1'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = proc.communicate()
    return output, error
