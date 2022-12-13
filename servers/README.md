Templates for Zabbix

Servers

- Dell PowerEdge R630 (iDrac8)
Monitoring
1) controller Roll Up Status
2) controller Component Status
3) physical Disk State
4) physical Disk Component Status
5) physical Disk Smart Alert Indication
6) physical Disk Power State
7) battery State
8) battery Component Status
9) virtual Disk State
Triggers
1) controller Roll Up Status
	Information: 1, 2
	Warning: 4
	Hight: 5
	Disaster: 6
2) controller Component Status
	Information: 1, 2
	Warning: 4
	Hight: 5
	Disaster: 6
3) physical Disk State
4) physical Disk Component Status
	Information: 1, 2
	Warning: 4
	Hight: 5
	Disaster: 6
5) physical Disk Smart Alert Indication
6) physical Disk Power State
	Warning: 1, 3, 4
7) battery State
	Information: 6
	Warning: 1, 3, 4, 5, 7
8) battery Component Status
	Information: 1, 2
	Warning: 4
	Hight: 5
	Disaster: 6
Discovery
1) physical Disk State
2) physical Disk Component Status
3) physical Disk Smart Alert Indication
4) physical Disk Power State
