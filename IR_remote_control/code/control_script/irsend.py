#!/usr/bin/env python3

import sys
import argparse
import serial
import json
import time

title = '''
    ________                               __     
   /  _/ __ \   ________  ____ ___  ____  / /____ 
   / // /_/ /  / ___/ _ \/ __ `__ \/ __ \/ __/ _ \
 _/ // _, _/  / /  /  __/ / / / / / /_/ / /_/  __/
/___/_/ |_|  /_/   \___/_/ /_/ /_/\____/\__/\___/ 
                                                  
'''

usage = '''
IR remote control

Usage:

  help, h       display this message
  exit, quit    exit the program
  connect       open connection with device

  show
    config      display the current configuration
    status      display device status
    profiles    display the available profiles
    commands    display the available commands

  set
    profile     set the profile to use
    device      set the device to use

  send
    command     send command to device

  play
    file        path to file with sequence to play
'''

encoding = {
    "Samsung": {
        "0" :     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 06FB",
        "1" :     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "2" :     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "3" :     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "4" :     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "5" :     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "6" :     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "7" :     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "8" :     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "9" :     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "power":  "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "source": "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "menu":   "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 06FB",
        "up":     "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0041 0016 06FB",
        "down":   "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0041 0016 06FB",
        "left":   "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0016 0016 0016 0016 0041 0016 06FB",
        "right":  "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0041 0016 06FB",
        "enter":  "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0041 0016 0016 0016 0016 0016 0041 0016 06FB",
        "return": "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 06FB",
        "exit":   "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 06FB",
        "mute":   "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "vol+":   "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "vol-":   "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 06FB",
        "ch+":    "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0041 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 06FB",
        "ch-":    "0000 006C 0000 0022 00AD 00AD 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0016 0041 0016 0016 0016 0016 0016 0016 0016 0041 0016 0041 0016 0041 0016 0041 0016 0016 0016 0041 0016 0041 0016 0041 0016 06FB",
    }
}


class Arduino():

    def __init__(self):
        self.connected = False
    
    def connect(self, device, baud_rate=9600, timeout=5):
        try:
            self.ser = serial.Serial(device, baud_rate, timeout=timeout)
            s = self.ser.readline().decode()
        except:
            s = ''
        if s=="READY\r\n":
            self.connected = True
            print('Successfully connected to device!\n')
        else:
            self.connected = False
            print('Cannot connect to device...')
            print('Make sure the device is correctly connected.\n')

    def disconnect(self):
        self.connected = False

    def is_connected(self):
        return self.connected

    def send(self, profile, cmd):
        if self.connected:
            print('Sending command \"%s\".' % cmd)
            enc = encoding[profile][cmd]
            s = 'SEND ' + enc + '\r\n'
            try:
                self.ser.write(s.encode())
                s = self.ser.readline().decode()
            except:
                s = 'FAILED'
            if s[:4] == "SENT":
                print('Command \"%s\" successfully sent.\n' % cmd)
            else:
                print('Error while sending command \"%s\"\n.' % cmd)
        else:
            print_error('no device connected')

    def __del__(self):
        try:
            self.ser.close()
        except:
            pass

def display_title():
    print(title)
    print('Enter \"help\" to show commands.\n')

def get_config():
    try:
        with open('irsend_config.json','r') as file:
            config = json.load(file)
    except:
        print_error('unable to open \"irsend_config.json\", creating empty config')
        config = {'profile':'', 'device':''}
        with open('irsend_config.json','w') as file:
            json.dump(config, file, indent=4)
    return config

def play_file(arduino, profile, filename):
    try:
        if arduino.is_connected():
            with open(filename,'r') as file:
                data = json.load(file)
                delay = data['delay']
                sequence = data['sequence']
                for command in sequence:
                    if command in encoding[profile].keys():
                        arduino.send(profile, command)
                    else:
                        print_error('unknown command \"%s\" for profile \"%s\"' % (command, profile))
                        break
                    time.sleep(delay)
        else:
            print_error('no device connected')
    except:
        print_error('unable to open \"%s\" or badly formatted' % filename)

def print_error(msg):
    print('ERROR: ' + msg + '\n')

def print_usage():
    print(usage)

def set_config(key, value):
    if key=='profile' or key=='device':
        with open('irsend_config.json','r+') as file:
            config = json.load(file)
            config[key] = value
            file.seek(0)
            json.dump(config, file, indent=4)
            file.truncate()
    else:
        print_error('unknown config key \"%s\"' % key)

def show_commands(profile):
    try:
        commands = encoding[profile].keys()
        print('Available commands for profile \"%s\":' % profile)
        for command in commands:
            print('  - ' + command)
        print()
    except:
        print_error('unknown profile \"%s\"' % profile)

def show_config(config):
    print('Config:')
    print('  Profile: %s' % config['profile'])
    print('  Device:  %s' % config['device'])
    print()

def show_profiles():
    profiles = encoding.keys()
    print('Available profiles:')
    for profile in profiles:
        print('  - ' + profile)
    print()

def show_status(arduino, config):
    if arduino.is_connected():
        print('Connected to %s\n' % config['device'])
    else:
        print('No device connected\n')

def unknown_command(cmd):
    print_error('unknown command \"%s\"' % cmd)



## MAIN
if __name__ == "__main__":

    arduino = Arduino()

    # interactive menu
    if(len(sys.argv) < 2):
        try:
            display_title()
            config = get_config()
            done = False
            while done is False:
                print('> ', end='')
                raw_cmd = input()
                cmd = raw_cmd.lower().split(' ')
                if cmd[0] == 'exit' or cmd[0] == 'quit' or cmd[0] == 'q':
                    print('Bye!\n')
                    done = True
                elif cmd[0] == 'help' or cmd[0] == 'h':
                    print_usage()
                elif cmd[0] == 'connect':
                    arduino.connect(config['device'], baud_rate=9600, timeout=5)
                elif cmd[0] == 'show':
                    if len(cmd) < 2:
                        print_error('missing argument\n')
                    elif cmd[1] == 'config':
                        show_config(config)
                    elif cmd[1] == 'status':
                        show_status(arduino, config)
                    elif cmd[1] == 'profiles':
                        show_profiles()
                    elif cmd[1] == 'commands':
                        show_commands(config['profile'])
                    else:
                        unknown_command(cmd[1])
                        print_usage()
                elif cmd[0] == 'set':
                    if len(cmd) < 2:
                        print_error('missing argument')
                    elif cmd[1] == 'profile' or cmd[1] == 'device':
                        if len(cmd) < 3:
                            print_error('missing argument')
                        else:
                            arduino.disconnect()
                            value = raw_cmd.split(' ')[2]
                            set_config(cmd[1], value)
                            config = get_config()
                    else:
                        unknown_command(cmd[1])
                        print_usage()
                elif cmd[0] == 'send':
                    if len(cmd) < 2:
                        print_error('missing argument')
                    else:
                        command = raw_cmd.split(' ')[1]
                        if command in encoding[config['profile']].keys():
                            arduino.send(config['profile'], command)
                        else:
                            print_error('unknown command \"%s\" for profile \"%s\"' % (command, config['profile']))
                elif cmd[0] == 'play':
                    if len(cmd) < 2:
                        print_error('missing argument')
                    else:
                        filename = raw_cmd.split(' ')[1]
                        play_file(arduino, config['profile'], filename)
                else:
                    unknown_command(cmd[0])
                    print_usage()

        except KeyboardInterrupt:
            print('\n\nHeyyy! You could ask politely...')
            print('OK. Quitting!\n')

    # command line interface
    else:

        parser = argparse.ArgumentParser(description="Denise\'s IR remote control.")
        parser.add_argument("command",
            type=str,
            help='command (\"send\", \"play\")',
            choices=['send','play'],
            metavar="<command>")
        parser.add_argument("value",
            type=str,
            help='command argument',
            metavar="<value>")

        config = get_config()
        profile = config['profile']
        device = config['device']

        args = parser.parse_args()
        command = args.command
        value = args.value

        if command == 'send':
            if value in encoding[profile].keys():
                arduino.connect(device, baud_rate=9600, timeout=5)
                arduino.send(profile, value)
            else:
                print_error('unknown command \"%s\" for profile \"%s\"' % (value, profile))
        elif command == 'play':
            filename = value
            arduino.connect(device, baud_rate=9600, timeout=5)
            play_file(arduino, profile, filename)

        print('Quitting.')
