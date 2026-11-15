# ЛР6. Інкапсуляція та декапсуляція на прикладі протоколу HTTP

- `Lab6_HTTP_OSI_report.docx` — звіт: PC1 як маршрутизатор (DHCP, NAT, nginx, vsftpd), DHCP DORA і ARP у Wireshark, route -n і ping, розподіл HTTP-сесії за рівнями OSI (Ethernet II, IPv4, TCP, HTTP), аналіз FTP-сесії (керуюче з'єднання і з'єднання даних), Test Plan TP-OSI-01, тест-кейси TC-OSI-01…03, Defect Report DR-HTTP-01, повторне тестування, висновки.
- `screenshots/` — скриншоти терміналу і Wireshark.

Оточення: VM Ubuntu 24.04 (VirtualBox), isc-dhcp-server 4.4.3-P1, nginx 1.24.0, vsftpd 3.0.5, curl 8.5.0, Wireshark 4.2.2.
PC1 — маршрутизатор (veth-srv 192.168.1.1/24, NAT через enp0s3), PC2 — network namespace `pc2`, адреса через DHCP (192.168.1.50/24).
HTTP-запит з PC2 виконано через curl, бо namespace не має власного графічного сеансу для браузера. Сесія на вибір — FTP (анонімний вхід, пасивний режим).
Дефект: nginx повертав 403 Forbidden через права 600 на index.html; після chmod 644 — 200 OK.
