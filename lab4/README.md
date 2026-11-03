# ЛР4. Служби DNS та NAT. Підходи до траблшутінгу мережі

- `Lab4_NAT_report.docx` — звіт: налаштування NAT через iptables (ip_forward, MASQUERADE, iptables-save), аналіз трансляції адрес і DNS у Wireshark, траблшутінг NAT за 8 кроками, DHCP/NAT Test Plan, тест-кейси TC-DHCP-04, TC-NAT-01, TC-NAT-02, Defect Report DR-NAT-01, висновки.
- `screenshots/` — скриншоти терміналу та Wireshark.

Оточення: VM Ubuntu 24.04 (VirtualBox). PC1 — DHCP-сервер і маршрутизатор з NAT (veth-srv 192.168.1.1/24, зовнішній enp0s3 10.0.2.15), PC2 — клієнт у network namespace `pc2` (veth-pc2, 192.168.1.50 за DHCP).
Дефект: правило `MASQUERADE` створено для неіснуючого інтерфейсу `-o enp0s8` замість `enp0s3`, пакети клієнтів виходять без трансляції адреси.
