"""Частина 1: підключення iperf3-клієнта до сервера через subprocess."""
import subprocess
import sys

import parser

server_ip = '192.168.1.2'   # PC2 (namespace pc2), iperf3 -s піднято вручну


def client(server_ip, duration=10):
    """Запускає iperf3-клієнт і повертає (вивід, помилка)."""
    proc = subprocess.Popen(['iperf3', '-c', server_ip, '-t', str(duration), '-i', '1'],
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    output, error = proc.communicate()
    return output, error


if __name__ == '__main__':
    ip = sys.argv[1] if len(sys.argv) > 1 else server_ip
    result, error = client(ip)
    if error:
        print(error.strip())
        sys.exit(1)
    result_list = parser.parser(result)
    print(f'Інтервалів: {len(result_list)}; Transfer > 2 МБайт і Bitrate > 20 Мбіт/с:')
    for value in result_list:
        if value['Transfer'] > 2 and value['Bitrate'] > 20:
            print(value)
