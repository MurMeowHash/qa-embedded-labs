"""Частина 2: автотест пропускної здатності iperf3 (TC-PY-02)."""
import os

import parser

TRANSFER_MIN = float(os.getenv('TRANSFER_MIN', 2))    # МБайт за інтервал
BITRATE_MIN = float(os.getenv('BITRATE_MIN', 20))     # Мбіт/с


class TestSuite():

    def test_iperf3_client_connection(self, client):
        """Клієнт підключився без помилки, і в кожному інтервалі
        Transfer > TRANSFER_MIN та Bitrate > BITRATE_MIN."""
        output, error = client
        assert not error, f'iperf3 client error: {error.strip()}'
        intervals = parser.parser(output)
        assert len(intervals) >= 10, 'iperf3 повернув менше 10 інтервалів'
        for value in intervals:
            print(value)
            assert value['Transfer'] > TRANSFER_MIN, f"{value['Interval']}: Transfer {value['Transfer']} MBytes"
            assert value['Bitrate'] > BITRATE_MIN, f"{value['Interval']}: Bitrate {value['Bitrate']} Mbits/sec"
