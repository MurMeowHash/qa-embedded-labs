# ЛР7. Основи використання фреймворку Pytest для автоматизації тестування

- `code/` — код лабораторної:
  - `client.py` — частина 1: запуск iperf3-клієнта через `subprocess.Popen`, вивід інтервалів з Transfer > 2 МБайт і Bitrate > 20 Мбіт/с або помилки;
  - `parser.py` — парсер виводу iperf3 на `re` (Interval, Transfer, Bitrate, Retr, Cwnd);
  - `conftest.py` — фікстури `server` (iperf3-сервер на PC2 через SSH/paramiko, вхід по ключу) і `client` (iperf3-клієнт через subprocess);
  - `iperf_test.py` — `TestSuite.test_iperf3_client_connection`;
  - `pytest.ini` — шаблон `*_test.py`.
- `Lab7_pytest_iperf_report.docx` — звіт: оточення, код, результати частини 1, три прогони pytest (позитивний, негативний за порогом, сервер недоступний), тест-кейси TC-PY-01 (ручний) і TC-PY-02 (автотест), Defect Report DR-PY-01 (обмеження tbf 15 Мбіт/с), повторне тестування, висновки.
- `screenshots/` — скриншоти терміналу.

Оточення: VM Ubuntu 24.04 (VirtualBox), Python 3.12.3, pytest 7.4.4, paramiko 2.12.0, iperf3 3.16, OpenSSH 9.6p1.
PC1 — клієнт (veth-srv 192.168.1.1/24), PC2 — network namespace `pc2` (veth-pc2 192.168.1.2/24) з sshd та iperf3-сервером.

Запуск:
```bash
cd lab7/code
python3 client.py [server_ip]
pytest -v iperf_test.py
BITRATE_MIN=40000 pytest -v iperf_test.py   # негативний сценарій за порогом
```
