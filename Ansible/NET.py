Ansible

Control machine 	— управляющий хост. Сервер Ansible, с которого происходит
					  управление другими хостами
Manage node 		— управляемые хосты 
Inventory 			— инвентарный файл. В этом файле описываются хосты, группы хостов,
					  а также могут быть созданы переменные
Playbook		    — файл сценариев
Play 				— сценарий (набор задач). Связывает задачи с хостами, для которых эти
					  задачи надо выполнить
Task				— задача. Вызывает модуль с указанными параметрами и переменными
Module 				— модуль Ansible. Реализует определенные функции
===================================================================================


 Ansible - Установка на Ubuntu 16.04 и CentOS 7


Установка на Ubuntu 16.04:
sudo apt-add-repository ppa:ansible/ansible
sudo apt-get update
sudo apt-get install ansible

Установка на CentOS 7:
sudo yum install epel-release
sudo yum install ansible

---------------------------------
ansible --version
---------------------------------
настройка

./ansible.cfg – в текущем каталоге;
~/.ansible.cfg — в домашнем каталоге;
/etc/ansible/ansible.cfg 

---------------------------------

hostfile: — путь к inventory file, содержит список ip-адресов (или имен) хостов для подключения;
library: — путь к модулям Ansible;
forks: — кол-во потоков, которые может создать Ansible;
sudo_user: — пользователь, от которого запускаются команды/инструкции на удаленных хостах;
remote_port: — порт для подключения по протоколу SSH;
host_key_checking: — включить/отключить проверку SSH–ключа на удаленном хосте;
timeout: — таймаут подключения по SSH;
log_path: — путь к файлу логов.

----------------------------------
Генерация SSH-ключа на сервере ansible

ssh-keygen -C "$(whoami)@$(hostname)-$(date -I)"

Если при генерации ключа на все вопросы был дан стандартный ответ (клавишей Enter), 
то в каталоге ~/.ssh/ появится два файла — id_rsa (закрытый ключ) и id_rsa.pub (открытый ключ).

Открытый ключ нужно скопировать на удаленный сервер, 
это можно сделать с помощью команды ssh-copy-id, например так:
ssh-copy-id user@server     

user - пользователь на удаленном сервере

Еще один способ скопировать открытый ключ на удаленный сервер — скопировать содержимое
~/.ssh/id_rsa.pub с локального компьютера в файл ~/.ssh/authorized_keys на удаленном хосте. 
Важно: чтение/запись в этот файл может производить только владелец, добиться этого можно командой:
chmod 600 ~/.ssh/authorized_keys



===================================================================================
Inventory 

[cisco-routers]  		# название группы
192.168.255.1:22022     # использование не стандартного порта ssh
192.168.255.2

[cisco-edge-routers]
192.168.255.1			# oдин и тот же адрес или имя хоста можно помещать в разные группы
92.168.255.[1-5]

[cisco-devices:children] # группа из групп
[cisco-edge-routers]
[cisco-routers] 

===================================================================================
Ad-hoc команды - это возможность запустить какое-то действие Ansible из командной строки.

$ ansible cisco-routers -i myhosts -m raw -a "sh ip int br" -u cisco --ask-pass

cisco-routers  		- группа устройств
-i myhosts  		- параметр -i позволяет указать инвентарный файл
-m raw 				- означает, что используется модуль raw
-a "sh ip int br" 	- параметр -a  указывает, какую команду отправить
-u cisco  			- подключение выполняется от имени пользователя cisco
--ask-pass  		- параметр, который нужно указать, чтобы аутентификация была по
					  паролю, а не по ключам
===================================================================================
ansible.cfg

[defaults]
inventory = ./myhosts     # местоположение инвентарного файла
remote_user = cisco
ask_pass = True
host_key_checking=False   # отвечает за проверку ключей при подключении по SSH

теперь команда выше будет иметь вид
$ ansible cisco-routers -m raw -a "sh ip int br"
===================================================================================
Переменные
можно создавать словари с переменными (в формате YAML):
R1:
  IP: 10.1.1.1/24
  DG: 10.1.1.100
Обращаться к переменным в словаре можно двумя вариантами:
R1['IP'] - предпочтительнее
R1.IP    - могут быть проблемы если название ключа совпадает с зарезервированным словом

===================================================================================
Переменные в специальных файлах для группы/устройства

Ansible позволяет хранить переменные для группы/устройства в специальных файлах:

Для групп устройств, переменные должны находиться в каталоге group_vars, в
файлах, которые называются, как имя группы.

Кроме того, можно создавать в каталоге group_vars файл all, в котором будут
находиться переменные, которые относятся ко всем группам.

Для конкретных устройств, переменные должны находиться в каталоге host_vars,
в файлах, которые соответствуют имени или адресу хоста.

Все файлы с переменными должны быть в формате YAML. Расширение файла
может быть таким: yml, yaml, json или без расширения

каталоги group_vars и host_vars должны находиться в том же каталоге, что и
playbook, или могут находиться внутри каталога inventory (первый вариант более
распространенный).

если каталоги и файлы названы правильно и расположены в указанных
каталогах, Ansible сам распознает файлы и будет использовать переменные

myhosts 
------------
[cisco-routers]
192.168.100.1
192.168.100.2
192.168.100.3
[cisco-switches]
192.168.100.100
------------
Можно создать такую структуру каталогов:
├── group_vars                 _
│   ├── all.yml                 |
│   ├── cisco-routers.yml       |  Каталог с переменными для групп устройств
│   └── cisco-switches.yml     _|
|
├── host_vars                  _
│   ├── 192.168.100.1           |
│   ├── 192.168.100.2           |
│   ├── 192.168.100.3           |  Каталог с переменными для устройств 
│   └── 192.168.100.100        _|
|
└── myhosts                     |  Инвентарный файл

group_vars/all.yml (в этом файле указываются значения по умолчанию, которые
относятся ко всем устройствам):
------------
cli:
  host: "{{ inventory_hostname }}"
  username: "cisco"
  password: "cisco"
  transport: cli
  authorize: yes
  auth_pass: "cisco"
------------
inventory_hostname - это специальная переменная, которая указывает на тот хост,
для которого Ansible выполняет действия.


group_vars/cisco-routers.yml 
В файле group_vars/cisco-routers.yml находятся переменные, которые указывают IP-
адреса Log и NTP серверов и нескольких пользователей. Эти переменные могут
использоваться, например, в шаблонах конфигурации.
------------
log_server: 10.255.100.1
ntp_server: 10.255.100.1
users:
  user1: pass1
  user2: pass2
  user3: pass3
------------
group_vars/cisco-switches.yml указана переменная vlans со списком VLANов.

------------
vlans:
  - 10
  - 20
  - 30
------------


Файл host_vars/192.168.100.1
------------
hostname: london_r1
mgmnt_loopback: 100
mgmnt_ip: 10.0.0.1
ospf_ints:
  - 192.168.100.1
  - 10.0.0.1
  - 10.255.1.1
------------

===================================================================================

Особенности подключения к сетевому оборудованию
При 
работе с сетевым оборудованием есть несколько параметров в playbook, которые
нужно менять:

gather_facts - надо отключить, так как для сетевого оборудования используются
свои модули сбора фактов
connection - управляет тем, как именно будет происходить подключение. Для
сетевого оборудования необходимо установить в local
То есть, для каждого сценария (play), нужно указывать:
gather_facts: false
connection: local
Пример:
---
- name: Run show commands on routers
  hosts: cisco-routers
  gather_facts: false
  connection: local
===================================================================================
