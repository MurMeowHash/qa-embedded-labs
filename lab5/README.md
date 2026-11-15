# ЛР5. Тестування навантаження комп'ютерної мережі

- `Lab5_iperf_report.docx` — звіт: TCP- і UDP-трафік через iperf, потрійне рукостискання TCP і UDP-датаграми у Wireshark, тест стабільності TCP (MTBF) з графіком gnuplot, навантажувальне тестування UDP великими (65000 Б) і малими (1000 Б) датаграмами, Test Plan TP-LOAD-01, тест-кейси TC-LOAD-01…05, Defect Report DR-LOAD-01, висновки.
- `scripts/bashTCP` — bash-скрипт тесту стабільності TCP-з'єднання (`./bashTCP ip_addr device`).
- `scripts/plotTCP.gpi` — скрипт gnuplot, будує графік швидкості з файлів `tcp_*.txt` (адаптований під формат iperf 2.1.9).
- `screenshots/` — скриншоти терміналу, Wireshark і gnuplot.

Оточення: VM Ubuntu 24.04 (VirtualBox), iperf 2.1.9, gnuplot 6.0. PC1 — сервер iperf (veth-srv 192.168.1.1/24), PC2 — клієнт у network namespace `pc2` (veth-pc2 192.168.1.2/24).
Тривалість UDP-тестів скорочено з 500/360 с до 30 с.
Дефект: сервер втрачав 1,3–2% UDP-датаграм під навантаженням через стандартний буфер сокета 208 КБ; після збільшення буфера до 32 МБ втрат 0%.
