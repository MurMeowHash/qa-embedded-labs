"""Парсер виводу iperf3-клієнта: повертає список інтервалів."""
import re

# [  5]   0.00-1.00   sec  3.20 GBytes  27.5 Gbits/sec    0   3.15 MBytes
REGEXP = re.compile(
    r'\[\s*\d+\]\s+(?P<Interval>[\d.]+-[\d.]+)\s+sec\s+'
    r'(?P<Transfer>[\d.]+)\s+(?P<t_unit>[KMG]?)Bytes\s+'
    r'(?P<Bitrate>[\d.]+)\s+(?P<b_unit>[KMG]?)bits/sec\s+'
    r'(?P<Retr>\d+)\s+(?P<Cwnd>[\d.]+)\s+(?P<c_unit>[KMG]?)Bytes')
KEYS = ('Interval', 'Transfer', 'Bitrate', 'Retr', 'Cwnd')
SCALE = {'': 1e-6, 'K': 1e-3, 'M': 1.0, 'G': 1e3}   # -> МБайт / Мбіт/с


def parser(output):
    """Повертає список словників {'Interval', 'Transfer' (МБайт),
    'Bitrate' (Мбіт/с), 'Retr', 'Cwnd' (КБайт)} для кожного інтервалу.
    Підсумкові рядки sender/receiver не потрапляють (у них немає Cwnd)."""
    result = []
    for m in REGEXP.finditer(output):
        result.append({
            'Interval': m['Interval'],
            'Transfer': round(float(m['Transfer']) * SCALE[m['t_unit']], 2),
            'Bitrate': round(float(m['Bitrate']) * SCALE[m['b_unit']], 1),
            'Retr': int(m['Retr']),
            'Cwnd': round(float(m['Cwnd']) * SCALE[m['c_unit']] * 1e3, 1),
        })
    return result
