import platform
import subprocess

import psutil


def get_size(bytes, suffix='B'):
    factor = 1024
    for unit in ['', 'K', 'M', 'G', 'T', 'P']:
        if bytes < factor:
            return f'{bytes:.2f}{unit}{suffix}'
        bytes /= factor


print('=' * 40, 'Системная информация', '=' * 40)
uname = platform.uname()

print(f'Система: {uname.system}')
print(f'Имя узла: {uname.node}')
print(f'Выпуск: {uname.release}')
print(f'Версия: {uname.version}')
print(f'Машина: {uname.machine}')
print(f'Процессор: {uname.processor}')

print('=' * 40, 'Информация о процессоре', '=' * 40)
print(f'Физические ядра:', psutil.cpu_count(logical=False))
print(f'Всего ядер:', psutil.cpu_count(logical=True))
cpufreg = psutil.cpu_freq()
print(f'Максимальная частота: {cpufreg.max:.2f} МГц')
print(f'Минимальная частота: {cpufreg.min:.2f} МГц')
print(f'Текущая частота: {cpufreg.current:.2f} МГц')
print(f'Загруженность процессора на ядро:')
for core, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)):
    print(f'Ядро {core}: {percentage} %')
print(f'Общая загруженность процессора: {psutil.cpu_percent()} %')

print('=' * 40, 'Информация о памяти', '=' * 40)
svmem = psutil.virtual_memory()
print(f'Объем: {get_size(svmem.total)}')
print(f'Доступно: {get_size(svmem.available)}')
print(f'Используется: {get_size(svmem.used)}')
print(f'Процент: {svmem.percent} %')

print('=' * 40, 'Память подкачки', '=' * 40)
swap = psutil.swap_memory()
print(f'Объем: {get_size(swap.total)}')
print(f'Свободно: {get_size(swap.free)}')
print(f'Используется: {get_size(swap.used)}')
print(f'Процент: {swap.percent} %')

print('=' * 40, 'Информация о диске', '=' * 40)
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f'=== Диск: {partition.device}')
    print(f' Тип файловой системы: {partition.fstype}')
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    print(f'    Общий объем: {get_size(partition_usage.total)}')
    print(f'    Используется: {get_size(partition_usage.used)}')
    print(f'    Свободно: {get_size(partition_usage.free)}')
    print(f'    Процент: {partition_usage.percent} %')

print('=' * 40, 'Информация о сети', '=' * 40)
ip_addrs = psutil.net_if_addrs()
for interface_name, interface_adresses in ip_addrs.items():
    print(f'=== Интерфейс: {interface_name} ===')
    for address in interface_adresses:
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f'    IP: {address.address}')
            print(f'    Сетевая маска: {address.netmask}')
            print(f'    Широковещательнай IP-адрес: {address.broadcast}')
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f'    MAC-адрес: {address.address}')
            print(f'    Сетевая маска: {address.netmask}')
            print(f'    Широковещательнай IP-адрес: {address.broadcast}')

net_io = psutil.net_io_counters()
print(f'Общее кол-во отправленных байтов: {get_size(net_io.bytes_sent)}')
print(f'Общее кол-во полученных байтов: {get_size(net_io.bytes_recv)}')
#


print('=' * 40, 'Вывод всех активных процессов', '=' * 40)
rp = subprocess.check_output('powershell -Executionpolicy ByPass -Command Get-Process')
print(rp.decode(encoding='Windows-1251'))
