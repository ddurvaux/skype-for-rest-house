EESchema Schematic File Version 2
LIBS:power
LIBS:device
LIBS:transistors
LIBS:conn
LIBS:linear
LIBS:regul
LIBS:74xx
LIBS:cmos4000
LIBS:adc-dac
LIBS:memory
LIBS:xilinx
LIBS:microcontrollers
LIBS:dsp
LIBS:microchip
LIBS:analog_switches
LIBS:motorola
LIBS:texas
LIBS:intel
LIBS:audio
LIBS:interface
LIBS:digital-audio
LIBS:philips
LIBS:display
LIBS:cypress
LIBS:siliconi
LIBS:opto
LIBS:atmel
LIBS:contrib
LIBS:valves
EELAYER 25 0
EELAYER END
$Descr A4 11693 8268
encoding utf-8
Sheet 1 1
Title "Hat Arduino IR emitter"
Date "01/06/2020"
Rev "1.0"
Comp ""
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L L_Core_Ferrite_Small L1
U 1 1 5ED56BED
P 3500 2750
F 0 "L1" V 3675 2725 50  0000 L CNN
F 1 "1 uH" V 3600 2650 50  0000 L CNN
F 2 "" H 3500 2750 50  0001 C CNN
F 3 "" H 3500 2750 50  0001 C CNN
	1    3500 2750
	0    -1   -1   0   
$EndComp
$Comp
L C C2
U 1 1 5ED56C34
P 4350 3000
F 0 "C2" H 4375 3100 50  0000 L CNN
F 1 "100 nF" H 4375 2900 50  0000 L CNN
F 2 "" H 4388 2850 50  0001 C CNN
F 3 "" H 4350 3000 50  0001 C CNN
	1    4350 3000
	1    0    0    -1  
$EndComp
$Comp
L CP C1
U 1 1 5ED56C83
P 3850 3000
F 0 "C1" H 3875 3100 50  0000 L CNN
F 1 "1200 uF" H 3875 2900 50  0000 L CNN
F 2 "" H 3888 2850 50  0001 C CNN
F 3 "" H 3850 3000 50  0001 C CNN
	1    3850 3000
	1    0    0    -1  
$EndComp
$Comp
L LED_ALT D1
U 1 1 5ED56D2D
P 5200 3500
F 0 "D1" H 5200 3600 50  0000 C CNN
F 1 "LED IR" H 5250 3400 50  0000 C CNN
F 2 "" H 5200 3500 50  0001 C CNN
F 3 "" H 5200 3500 50  0001 C CNN
	1    5200 3500
	0    -1   -1   0   
$EndComp
$Comp
L R R2
U 1 1 5ED56E45
P 5950 3000
F 0 "R2" V 6030 3000 50  0000 C CNN
F 1 "R56" V 5950 3000 50  0000 C CNN
F 2 "" V 5880 3000 50  0001 C CNN
F 3 "" H 5950 3000 50  0001 C CNN
	1    5950 3000
	1    0    0    -1  
$EndComp
$Comp
L R R1
U 1 1 5ED56EC6
P 5200 3000
F 0 "R1" V 5280 3000 50  0000 C CNN
F 1 "R56" V 5200 3000 50  0000 C CNN
F 2 "" V 5130 3000 50  0001 C CNN
F 3 "" H 5200 3000 50  0001 C CNN
	1    5200 3000
	1    0    0    -1  
$EndComp
$Comp
L Q_NMOS_DSG Q1
U 1 1 5ED56F07
P 5100 5150
F 0 "Q1" H 5300 5200 50  0000 L CNN
F 1 "BS170" H 5300 5100 50  0000 L CNN
F 2 "" H 5300 5250 50  0001 C CNN
F 3 "" H 5100 5150 50  0001 C CNN
	1    5100 5150
	1    0    0    -1  
$EndComp
$Comp
L Conn_01x02_Male J1
U 1 1 5ED56F7D
P 2675 2900
F 0 "J1" H 2675 3000 50  0000 C CNN
F 1 "Conn_01x02_Male" H 2675 2700 50  0001 C CNN
F 2 "" H 2675 2900 50  0001 C CNN
F 3 "" H 2675 2900 50  0001 C CNN
	1    2675 2900
	1    0    0    -1  
$EndComp
$Comp
L Conn_01x01_Male J2
U 1 1 5ED57190
P 4400 5150
F 0 "J2" H 4400 5250 50  0000 C CNN
F 1 "Conn_01x01_Male" H 4400 5050 50  0001 C CNN
F 2 "" H 4400 5150 50  0001 C CNN
F 3 "" H 4400 5150 50  0001 C CNN
	1    4400 5150
	1    0    0    -1  
$EndComp
$Comp
L +5V #PWR1
U 1 1 5ED5721B
P 3125 2650
F 0 "#PWR1" H 3125 2500 50  0001 C CNN
F 1 "+5V" H 3125 2790 50  0000 C CNN
F 2 "" H 3125 2650 50  0001 C CNN
F 3 "" H 3125 2650 50  0001 C CNN
	1    3125 2650
	1    0    0    -1  
$EndComp
$Comp
L Earth #PWR2
U 1 1 5ED57267
P 5200 5550
F 0 "#PWR2" H 5200 5300 50  0001 C CNN
F 1 "Earth" H 5200 5400 50  0001 C CNN
F 2 "" H 5200 5550 50  0001 C CNN
F 3 "" H 5200 5550 50  0001 C CNN
	1    5200 5550
	1    0    0    -1  
$EndComp
$Comp
L LED_ALT D2
U 1 1 5ED57777
P 5200 4000
F 0 "D2" H 5200 4100 50  0000 C CNN
F 1 "LED IR" H 5250 3900 50  0000 C CNN
F 2 "" H 5200 4000 50  0001 C CNN
F 3 "" H 5200 4000 50  0001 C CNN
	1    5200 4000
	0    -1   -1   0   
$EndComp
$Comp
L LED_ALT D3
U 1 1 5ED578D0
P 5200 4500
F 0 "D3" H 5200 4600 50  0000 C CNN
F 1 "LED IR" H 5250 4400 50  0000 C CNN
F 2 "" H 5200 4500 50  0001 C CNN
F 3 "" H 5200 4500 50  0001 C CNN
	1    5200 4500
	0    -1   -1   0   
$EndComp
$Comp
L LED_ALT D4
U 1 1 5ED588C5
P 5950 3500
F 0 "D4" H 5950 3600 50  0000 C CNN
F 1 "LED IR" H 6000 3400 50  0000 C CNN
F 2 "" H 5950 3500 50  0001 C CNN
F 3 "" H 5950 3500 50  0001 C CNN
	1    5950 3500
	0    -1   -1   0   
$EndComp
$Comp
L LED_ALT D5
U 1 1 5ED588CB
P 5950 4000
F 0 "D5" H 5950 4100 50  0000 C CNN
F 1 "LED IR" H 6000 3900 50  0000 C CNN
F 2 "" H 5950 4000 50  0001 C CNN
F 3 "" H 5950 4000 50  0001 C CNN
	1    5950 4000
	0    -1   -1   0   
$EndComp
$Comp
L LED_ALT D6
U 1 1 5ED588D1
P 5950 4500
F 0 "D6" H 5950 4600 50  0000 C CNN
F 1 "LED IR" H 6000 4400 50  0000 C CNN
F 2 "" H 5950 4500 50  0001 C CNN
F 3 "" H 5950 4500 50  0001 C CNN
	1    5950 4500
	0    -1   -1   0   
$EndComp
Wire Wire Line
	2875 2900 2950 2900
Wire Wire Line
	2950 2900 2950 2750
Wire Wire Line
	2950 2750 3400 2750
Wire Wire Line
	3125 2650 3125 2750
Connection ~ 3125 2750
Wire Wire Line
	3600 2750 5950 2750
Wire Wire Line
	4350 2750 4350 2850
Wire Wire Line
	3850 2850 3850 2750
Connection ~ 3850 2750
Wire Wire Line
	5200 2750 5200 2850
Connection ~ 4350 2750
Wire Wire Line
	5950 2750 5950 2850
Connection ~ 5200 2750
Wire Wire Line
	5200 3150 5200 3350
Wire Wire Line
	5950 3150 5950 3350
Wire Wire Line
	5200 3650 5200 3850
Wire Wire Line
	5950 3650 5950 3850
Wire Wire Line
	5200 4150 5200 4350
Wire Wire Line
	5950 4150 5950 4350
Wire Wire Line
	5200 4650 5200 4950
Wire Wire Line
	5200 4800 5950 4800
Wire Wire Line
	5950 4800 5950 4650
Connection ~ 5200 4800
Wire Wire Line
	5200 5350 5200 5550
Wire Wire Line
	2900 3000 2950 3000
Wire Wire Line
	2950 3000 2950 3250
Wire Wire Line
	2950 3250 4350 3250
Wire Wire Line
	4350 3250 4350 3150
Wire Wire Line
	3850 3150 3850 5450
Connection ~ 3850 3250
Wire Wire Line
	4600 5150 4900 5150
Wire Wire Line
	3850 5450 5200 5450
Connection ~ 5200 5450
Text Notes 2150 3250 0    60   ~ 0
Arduino Power
Text Notes 2425 2925 0    60   ~ 0
+5V
Text Notes 2475 3125 0    60   ~ 0
GND
Text Notes 4350 5275 0    60   ~ 0
D9
$EndSCHEMATC
