# ЛР3. Мережний рівень OSI, статична/динамічна IP-адресація, DHCP (варіант 0)

- `Lab3_DHCP_report.docx` — звіт: оточення, статична IP і traceroute, налаштування isc-dhcp-server, DORA у Wireshark, Test Plan, тест-кейси TC-DHCP-01…03, Defect Report DR-DHCP-01, висновки.
- `screenshots/` — скриншоти терміналу та Wireshark (видно користувача й дату).

Оточення: VM Ubuntu 24.04 (VirtualBox). PC1 — сервер і маршрутизатор (veth-srv 192.168.1.1/24, NAT через enp0s3), PC2 — клієнт у network namespace `pc2` (veth-pc2).
Дефект за варіантом 0: у `dhcpd.conf` вказано неправильний маршрутизатор `option routers 192.168.1.254;`.
