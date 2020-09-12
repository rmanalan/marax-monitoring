import glob
import time

base_dir = '/sys/bus/w1/devices/'
device_folder = glob.glob(base_dir + '*-*')[0]
device_file = device_folder + '/w1_slave'
log = open('/var/log/thermo/temp.log', 'a')

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    while lines[0].strip()[-3:] != 'YES':
        lines = read_temp_raw()
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000
        temp_f = temp_c * 9 / 5 + 32
        return temp_c, temp_f

temp = read_temp()
log.write("{:.0f},{:.2f},{:.2f} \n".format(time.time(), temp[0], temp[1]))
