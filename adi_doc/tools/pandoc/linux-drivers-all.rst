Linux Drivers
=============

Building the ADI Linux kernel
-----------------------------

Common elements for all kernel builds:

-  make sure you have ``make`` installed on your system, but we
   generally recommend installing the build-essentials tools for your
   Linux distribution
-  some builds will require you to have ``u-boot-tools`` installed, to
   have the ``mkimage`` utilities available, so it's good to have them
   available/installed

<WRAP round 70% download> If you would like a pre-compiled kernel with
complete user space, check out ADI's `Kuiper Linux
Distribution </resources/tools-software/linux-software/kuiper-linux>`__
</WRAP>

Target specific details:

-  `Building the Zynq Linux kernel and devicetrees from
   source <linux-build//generic/zynq>`__
-  `Building the ZynqMP / MPSoC Linux kernel and devicetrees from
   source <linux-build//generic/zynqmp>`__
-  `Building the Intel SoC-FPGA Linux kernel and devicetrees from
   source <linux-build//generic/socfpga>`__
-  `Building the Nios II kernel from
   source <linux-build//generic/nios2>`__
-  `Building with buildroot
   (microblaze) <linux-build//generic/buildroot>`__
-  `Building with
   Petalinux </resources/tools-software/linux-build/generic/petalinux>`__
-  `Building for Raspberry PI <linux-build//generic/raspberrypi>`__

The rapid increase in use of free and open-source software (FOSS), in
particular Linux, represents the most significant, all-encompassing, and
long-term trend that the embedded industry has seen since the early
1980s. [1]_ Like many, Analog Devices creates and maintains Linux
Drivers for various Analog Devices products.

Life Cycle
~~~~~~~~~~

Analog Devices uses six designations to inform our customers where a
semiconductor product is in its `life
cycle <adi>en/support/customer-service-resources/sales/product-life-cycle-information.html>`__.
From emerging innovations to products which have been in production for
twenty years, we understand that insight into life cycle status is
important. Device life cycles are tracked on their individual product
pages on `analog.com <adi>>`__, and should always be consulted before
making any design decisions. Drivers for obsolete devices are still
tracked/maintained/supported on a best effort basis, since we understand
the life cycle of end products that ADI's devices are designed into can
be longer than the life cycle of the semiconductor product itself.

Maintenance and Support
~~~~~~~~~~~~~~~~~~~~~~~

These drivers are a combinations of written and maintained by Analog
Devices developers, and by many other open source volunteers (most times
end-users of various devices). All these drivers (and their
corresponding device trees), independent of origin, are supported by ADI
Linux kernel Engineers, on-line at
`linux-software-drivers <ez>linux-software-drivers>`__. This is a
combination of drivers that are maintained at Analog Devices
`github <repo>linux>`__ and the mainline `mainline
kernel <git.linux.org>>`__ at https://kernel.org/.

It is a common practice during driver development to support a subset of
what the hardware/chip is capable of. If you find a driver does not
expose a feature you require in your design, please make a request in
our `support forums <ez>linux-software-drivers>`__.

Requests
~~~~~~~~

If you find a ADI device that you would like a driver for, please ask on
our `support forums <ez>linux-software-drivers>`__. While we would like
support every request, and do try to support most; this does go through
a quick internal process before development starts. Our metrics to
create device driver additions are pretty simple, it depends on
development efforts (adding a part into an existing subsystem is easier
than developing a completely new subsystem, or extending something), and
popularity of the device (we are much more likely to do something that
is recently released, than something 25 years old). If you have a local
ADI contact (like a Sales Engineer or FAE) it's always a great idea to
contact them at the same time so we can better understand your
application and schedule. If you are an ADI employee who wants to make a
request, click on *Submit Reference Design Idea* (under Tools and
Services) on the main intranet page.

Driver List
-----------

Devices are organized by Linux subsystem.

Backlight
~~~~~~~~~

-  `ADP5020: Power Management Unit for Imaging
   Modules <git.linux.org>drivers/video/backlight/adp5520_bl.c>`__
   `ADP5020 <adi>ADP5020>`__
-  `ADP5501: Programmable Current Backlight Driver with Ambient Light
   Sensor Input <linux-drivers//multifunction-device/adp5520>`__
   `Obsolete <adi>adp5501>`__
-  `ADP5520: Backlight Driver with I/O
   Expander <linux-drivers//multifunction-device/adp5520>`__
-  `ADP8860: Charge Pump, 7-Channel Smart LED Driver with I2C
   Interface </linux-drivers/backlight/adp8860>`__
-  `ADP8861: Charge Pump, 7-Channel Smart LED Driver with I2C
   Interface </linux-drivers/backlight/adp8860>`__
-  `ADP8863: Charge Pump, 7-Channel Fun Lighting LED
   Driver </linux-drivers/backlight/adp8860>`__
-  `ADP8870: Charge Pump Parallel Backlight Driver with Image Content
   PWM Input </linux-drivers/backlight/adp8870>`__
-  `LT3593: 1MHz White LED Driver with Output Disconnect and One Pin
   Current Programming <git.linux.org>drivers/leds/leds-lt3593.c>`__
   `LT3593 <adi>LT3593>`__

Battery Charger
~~~~~~~~~~~~~~~

-  `ADP5061: I2C Programmable Linear Battery Charger with Power Path and
   USB Mode
   Compatibility </linux-drivers-all/battery-charger/adp5061>`__
-  `LTC4162-L: 35V/3.2A Multi-Cell Lithium-Ion Step-Down Battery Charger
   with PowerPath and I2C
   Telemetry <git.linux.org>drivers/power/supply/ltc4162-l-charger.c>`__
   `LTC4162 <adi>LTC4162>`__
-  `MAX14656: USB Charger Detection with Integrated Overvoltage
   Protection <git.linux.org>drivers/power/supply/max14656_charger_detector.c>`__
   `MAX14656 <maxim>MAX14656>`__
-  `MAX77650: Ultra-Low Power PMIC with 3-Output SIMO and Power Path
   Charger for Small Li+ 0.8-3.95V
   Output <git.linux.org>drivers/mfd/max77650.c>`__
   `MAX77650 <maxim>MAX77650>`__
-  `MAX77651: Ultra-Low Power PMIC with 3-Output SIMO and Power Path
   Charger for Small Li+ 2.4-5.25V
   Output <git.linux.org>drivers/mfd/max77650.c>`__
   `MAX77651 <maxim>MAX77651>`__
-  `MAX8903A: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter
   Power <git.linux.org>drivers/power/supply/max8903_charger.c>`__
   `8903A <maxim>8903A>`__
-  `MAX8903B: 2A 1-Cell Li+ DC-DC Charger for USB, Adapter Power and
   Power-Enable on Battery
   Detection <git.linux.org>drivers/power/supply/max8903_charger.c>`__
   `8903B <maxim>8903B>`__
-  `MAX8903C: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter
   Power <git.linux.org>drivers/power/supply/max8903_charger.c>`__
   `8903C <maxim>8903C>`__
-  `MAX8903D: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter
   Power <git.linux.org>drivers/power/supply/max8903_charger.c>`__
   `8903D <maxim>8903D>`__
-  `MAX8903E: 2A 1-Cell Li+ DC-DC Charger for USB, Adapter Power and
   Power-Enable on Battery
   Detection <git.linux.org>drivers/power/supply/max8903_charger.c>`__
   `8903E <maxim>8903E>`__
-  `MAX8903G: 2A 1-Cell Li+ DC-DC Charger for USB, Adapter Power and
   Power-Enable on Battery
   Detection <git.linux.org>drivers/power/supply/max8903_charger.c>`__
   `8903G <maxim>8903G>`__
-  `MAX8903H: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter
   Power <git.linux.org>drivers/power/supply/max8903_charger.c>`__
   `8903H <maxim>8903H>`__
-  `MAX8903J: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter
   Power <git.linux.org>drivers/power/supply/max8903_charger.c>`__
   `8903J <maxim>8903J>`__
-  `MAX8903N: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter
   Power <git.linux.org>drivers/power/supply/max8903_charger.c>`__
   `8903N <maxim>8903N>`__
-  `MAX8903Y: 2A 1-Cell Li+ DC-DC Charger for USB and Adapter
   Power <git.linux.org>drivers/power/supply/max8903_charger.c>`__
   `8903Y <maxim>8903Y>`__

Battery Gas Gauge
~~~~~~~~~~~~~~~~~

-  `DS2760: High-Precision Li+ Battery
   Monitor <git.linux.org>drivers/power/supply/ds2760_battery.c>`__
   `DS2760 <maxim>DS2760>`__
-  `DS2780: Stand-Alone Fuel Gauge
   IC <git.linux.org>drivers/power/supply/ds2780_battery.c>`__
   `DS2780 <maxim>DS2780>`__
-  `DS2781: 1-Cell or 2-Cell Stand-Alone Fuel Gauge
   IC <git.linux.org>drivers/power/supply/ds2781_battery.c>`__
   `DS2781 <maxim>DS2781>`__
-  `DS2782: Stand-Alone Fuel Gauge
   IC <git.linux.org>drivers/power/supply/ds2782_battery.c>`__
   `DS2782 <maxim>DS2782>`__
-  `DS2786: Stand-Alone OCV-Based Fuel
   Gauge <git.linux.org>drivers/power/supply/ds2782_battery.c>`__
   `DS2786 <maxim>DS2786>`__
-  `LT3651-4.x: Monolithic 4A High Voltage 1 Cell Li-Ion Battery
   Charger <git.linux.org>drivers/power/supply/lt3651-charger.c>`__
   `LT3651-4.1 <adi>LT3651-4.1>`__
-  `LT3651-8.x: Monolithic 4A High Voltage 2-Cell Li-Ion Battery
   Charger <git.linux.org>drivers/power/supply/lt3651-charger.c>`__
   `LT3651-8.2 <adi>LT3651-8.2>`__
-  `LTC2941: Battery Gas Gauge with I2C
   Interface <git.linux.org>drivers/power/supply/ltc2941-battery-gauge.c>`__
   `LTC2941 <adi>LTC2941>`__
-  `LTC2942: Battery Gas Gauge with Temperature, Voltage
   Measurement <git.linux.org>drivers/power/supply/ltc2941-battery-gauge.c>`__
   `LTC2942 <adi>LTC2942>`__
-  `LTC2943: Multicell Battery Gas Gauge with Temperature, Voltage and
   Current
   Measurement <git.linux.org>drivers/power/supply/ltc2941-battery-gauge.c>`__
   `LTC2943 <adi>LTC2943>`__
-  `LTC2944: 60V Battery Gas Gauge with Temperature, Voltage and Current
   Measurement <git.linux.org>drivers/power/supply/ltc2941-battery-gauge.c>`__
   `LTC2944 <adi>LTC2944>`__
-  `MAX17040: 1-Cell/2-Cell Fuel Gauge with
   ModelGauge <git.linux.org>drivers/power/supply/max17040_battery.c>`__
   `MAX17040 <maxim>MAX17040>`__
-  `MAX17041: 1-Cell/2-Cell Fuel Gauge with
   ModelGauge <git.linux.org>drivers/power/supply/max17040_battery.c>`__
   `MAX17041 <maxim>MAX17041>`__
-  `MAX17043: 1-Cell/2-Cell Fuel Gauge with ModelGauge and Low-Battery
   Alert <git.linux.org>drivers/power/supply/max17040_battery.c>`__
   `MAX17043 <maxim>MAX17043>`__
-  `MAX17044: 1-Cell/2-Cell Fuel Gauge with ModelGauge and Low-Battery
   Alert <git.linux.org>drivers/power/supply/max17040_battery.c>`__
   `MAX17044 <maxim>MAX17044>`__
-  `MAX17047: 1-Cell Fuel Gauge with ModelGauge
   m3 <git.linux.org>drivers/power/supply/max17042_battery.c>`__
   `MAX17047 <maxim>MAX17047>`__
-  `MAX17048: 3µA 1-Cell/2-Cell Fuel Gauge with
   ModelGauge <git.linux.org>drivers/power/supply/max17040_battery.c>`__
   `MAX17048 <maxim>MAX17048>`__
-  `MAX17049: 3µA 1-Cell/2-Cell Fuel Gauge with
   ModelGauge <git.linux.org>drivers/power/supply/max17040_battery.c>`__
   `MAX17049 <maxim>MAX17049>`__
-  `MAX17050: 1-Cell Fuel Gauge with ModelGauge
   m3 <git.linux.org>drivers/power/supply/max17042_battery.c>`__
   `MAX17050 <maxim>MAX17050>`__
-  `MAX17055: 7µA 1-Cell Fuel Gauge with ModelGauge m5
   EZ <git.linux.org>drivers/power/supply/max17042_battery.c>`__
   `MAX17055 <maxim>MAX17055>`__
-  `MAX17058: 1-Cell/2-Cell Fuel Gauge with ModelGauge and Low-Battery
   Alert <git.linux.org>drivers/power/supply/max17040_battery.c>`__
   `MAX17058 <maxim>MAX17058>`__
-  `MAX17059: 1-Cell/2-Cell Fuel Gauge with
   ModelGauge <git.linux.org>drivers/power/supply/max17040_battery.c>`__
   `MAX17059 <maxim>MAX17059>`__
-  `MAX17211: Stand-Alone ModelGauge m5 Fuel Gauge with SHA-256
   Authentication <git.linux.org>drivers/power/supply/max1721x_battery.c>`__
   `MAX17211 <maxim>MAX17211>`__
-  `MAX17215: Stand-Alone ModelGauge m5 Fuel Gauge with SHA-256
   Authentication <git.linux.org>drivers/power/supply/max1721x_battery.c>`__
   `MAX17215 <maxim>MAX17215>`__

Battery Manager
~~~~~~~~~~~~~~~

-  `LTC1760: Dual Smart Battery System
   Manager <git.linux.org>drivers/power/supply/sbs-manager.c>`__
   `LTC1760 <adi>LTC1760>`__

CLOCK
~~~~~

-  `AD9545: Quad Input, 10-Output, Dual DPLL/IEEE 1588, 1 pps
   Synchronizer and Jitter
   Cleaner </linux-drivers/clk/adi/clk-ad9545.c>`__
-  `MAX9485: Programmable Audio Clock
   Generator <git.linux.org>drivers/clk/clk-max9485.c>`__
   `MAX9485 <maxim>MAX9485>`__

Card Bus
~~~~~~~~

-  `MAX1600: Dual-Channel CardBus and PCMCIA VCC VPP Power Switching
   Networks <git.linux.org>drivers/pcmcia/max1600.c>`__
   `MAX1600 <maxim>MAX1600>`__

GPIO
~~~~

-  `ADP5520: Backlight Driver with I/O
   Expander <linux-drivers//multifunction-device/adp5520>`__
-  `ADP5587: Mobile I/O Expander and QWERTY Keypad
   Controller </linux-drivers/gpio/adp5588-gpio>`__
-  `ADP5588: Mobile I/O Expander and QWERTY Keypad
   Controller </linux-drivers/gpio/adp5588-gpio>`__
-  `MAX31910: Ultra-Low Power Industrial, Octal, Digital Input
   Translator/Serializer <git.linux.org>drivers/gpio/gpio-max3191x.c>`__
   `MAX31910 <maxim>MAX31910>`__
-  `MAX31912: Ultra-Low Power Industrial, Octal, Digital Input
   Translator/Serializer <git.linux.org>drivers/gpio/gpio-max3191x.c>`__
   `MAX31912 <maxim>MAX31912>`__
-  `MAX31913: Industrial, Octal, Digital Input
   Translator/Serializer <git.linux.org>drivers/gpio/gpio-max3191x.c>`__
   `MAX31913 <maxim>MAX31913>`__
-  `MAX31953: Octal Industrial Digital Input with Isolated SPI
   Interface <git.linux.org>drivers/gpio/gpio-max3191x.c>`__
   `MAX31953 <https://datasheets.maximintegrated.com/en/ds/MAX31953-MAX31963.pdf>`__
-  `MAX31963: Octal Industrial Digital Input with Isolated SPI
   Interface <git.linux.org>drivers/gpio/gpio-max3191x.c>`__
   `MAX31963 <https://datasheets.maximintegrated.com/en/ds/MAX31953-MAX31963.pdf>`__
-  `MAX7300: 2-Wire-Interfaced, 2.5V to 5.5V, 20-Port or 28-Port I/O
   Expander <git.linux.org>drivers/gpio/gpio-max7300.c>`__
   `MAX7300 <maxim>MAX7300>`__
-  `MAX7301: 4-Wire-Interfaced, 2.5V to 5.5V, 20-Port and 28-Port I/O
   Expander <git.linux.org>drivers/gpio/gpio-max7301.c>`__
   `MAX7301 <maxim>MAX7301>`__
-  `MAX7310: 2-Wire-Interfaced 8-Bit I/O Port Expander with
   Reset <git.linux.org>drivers/gpio/gpio-pca953x.c>`__
   `MAX7310 <maxim>MAX7310>`__
-  `MAX7312: 2-Wire-Interfaced 16-Bit I/O Port Expander with Interrupt
   and Hot-Insertion
   Protection <git.linux.org>drivers/gpio/gpio-pca953x.c>`__
   `MAX7312 <maxim>MAX7312>`__
-  `MAX7313: 16-Port I/O Expander with LED Intensity Control, Interrupt,
   and Hot-Insertion
   Protection <git.linux.org>drivers/gpio/gpio-pca953x.c>`__
   `MAX7313 <maxim>MAX7313>`__
-  `MAX7315: 8-Port I/O Expander with LED Intensity Control, Interrupt,
   and Hot-Insertion
   Protection <git.linux.org>drivers/gpio/gpio-pca953x.c>`__
   `MAX7315 <maxim>MAX7315>`__
-  `MAX7319: I²C Port Expander with Eight Inputs and Maskable Transition
   Detection <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7319 <maxim>MAX7319>`__
-  `MAX7320: I²C Port Expander with Eight Push-Pull
   Output <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7320 <maxim>MAX7320>`__
-  `MAX7321: I2C Port Expander with 8 Open-Drain
   I/Os <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7321 <maxim>MAX7321>`__
-  `MAX7322: I²C Port Expander with 4 Push-Pull Outputs and 4
   Inputs <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7322 <maxim>MAX7322>`__
-  `MAX7323: I²C Port Expander with 4 Push-Pull Outputs and 4 Open-Drain
   I/Os <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7323 <maxim>MAX7323>`__
-  `MAX7324: I²C Port Expander with Eight Push-Pull Outputs and Eight
   Inputs <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7324 <maxim>MAX7324>`__
-  `MAX7325: I2C Port Expander with 8 Push-Pull and 8 Open-Drain
   I/Os <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7325 <maxim>MAX7325>`__
-  `MAX7326: I²C Port Expander with 12 Push-Pull Outputs and Four
   Inputs <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7326 <maxim>MAX7326>`__
-  `MAX7327: I²C Port Expander with 12 Push-Pull Outputs and 4
   Open-Drain I/Os <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7327 <maxim>MAX7327>`__
-  `MAX7328: I²C Port Expanders with Eight I/O
   Ports <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7328 <maxim>MAX7328>`__
-  `MAX7329: I²C Port Expanders with Eight I/O
   Ports <git.linux.org>drivers/gpio/gpio-max732x.c>`__
   `MAX7329 <maxim>MAX7329>`__

Secondary function
^^^^^^^^^^^^^^^^^^

-  `ADP5585: Keypad Decoder and I/O
   Expansion <linux-drivers/input-keyboard/adp5589>`__
-  `ADP5587: Mobile I/O Expander and QWERTY Keypad
   Controller <linux-drivers/input-keyboard/adp5588>`__
-  `ADP5588: Mobile I/O Expander and QWERTY Keypad
   Controller <linux-drivers/input-keyboard/adp5588>`__
-  `ADP5589: Keypad Decoder and I/O
   Expansion <linux-drivers/input-keyboard/adp5589>`__

HWMon & PMBus
~~~~~~~~~~~~~

HWMon
^^^^^

-  `AD7314: Complete Temperature Monitoring System in an 8-Pin µSOIC
   Package <git.linux.org>drivers/hwmon/ad7314.c>`__
   `AD7314 <adi>AD7314>`__
-  `AD7414: SMBus/I2C Digital Temperature Sensor in 6-Pin SOT with SMBus
   Alert and Over Temperature
   Pin <git.linux.org>drivers/hwmon/ad7414.c>`__ `ad7414 <adi>ad7414>`__
-  `AD7416: 10-Bit Digital Temperature
   Sensor <git.linux.org>drivers/hwmon/ad7418.c>`__
   `AD7416 <adi>AD7416>`__
-  `AD7417: 10-Bit Digital Temperature Sensor and Four Channel
   ADC <git.linux.org>drivers/hwmon/ad7418.c>`__ `AD7417 <adi>AD7417>`__
-  `AD7418: 10-Bit Digital Temperature Sensor and Single Channel
   ADC <git.linux.org>drivers/hwmon/ad7418.c>`__ `AD7418 <adi>AD7418>`__
-  `ADM1177: Hot Swap Controller and Digital Power Monitor with Soft
   Start Pin <git.linux.org>drivers/hwmon/adm1177.c>`__
   `ADM1177 <adi>ADM1177>`__
-  `ADM1266: Cascadable Super Sequencer with Margin Control and Fault
   Recording <git.linux.org>drivers/hwmon/pmbus/adm1266.c>`__
   `ADM1266 <adi>ADM1266>`__
-  `ADT7301: 13-Bit, ±1ºC Accurate, MicroPower Digital Temperature
   Sensor in 6-Lead SOT-23 and 8-Lead
   MSOP <git.linux.org>drivers/hwmon/ad7314.c>`__
   `ADT7301 <adi>ADT7301>`__
-  `ADT7302: ±2°C Accurate, MicroPower Digital Temperature Sensor in
   6-Lead SOT-23 <git.linux.org>drivers/hwmon/ad7314.c>`__
   `ADT7302 <adi>ADT7302>`__
-  `ADT7310: ±0.5°C Accurate, 16-Bit Digital SPI Temperature
   Sensor <git.linux.org>drivers/hwmon/adt7x10.c>`__
   `ADT7310 <adi>ADT7310>`__
-  `ADT7320: ±0.25°C Accurate, 16-Bit Digital SPI Temperature
   Sensor <git.linux.org>drivers/hwmon/adt7x10.c>`__
   `ADT7320 <adi>ADT7320>`__
-  `ADT7408: ± 2°C Accurate, 12-Bit Digital Temperature
   Sensor <git.linux.org>drivers/hwmon/jc42.c>`__
   `ADT7408 <adi>ADT7408>`__
-  `ADT7410: ±0.5°C Accurate, 16-Bit Digital I2C Temperature
   Sensor <git.linux.org>drivers/hwmon/adt7x10.c>`__
   `ADT7410 <adi>ADT7410>`__
-  `ADT7411: SPI-/I2C-Compatible, 10-Bit Digital Temperature Sensor and
   8-Channel ADC <git.linux.org>drivers/hwmon/adt7411.c>`__
   `ADT7411 <adi>ADT7411>`__
-  `ADT7420: ±0.25°C Accurate, 16-Bit Digital I2C Temperature
   Sensor <git.linux.org>drivers/hwmon/adt7x10.c>`__
   `ADT7420 <adi>ADT7420>`__
-  `ADT7470: Temperature Sensor Hub and Fan
   Controller <git.linux.org>drivers/hwmon/adt7470.c>`__
   `ADT7470 <adi>ADT7470>`__
-  `ADT75: ±1°C Accurate, 12-Bit Digital Temperature
   Sensor <git.linux.org>drivers/hwmon/lm75.c>`__ `ADT75 <adi>ADT75>`__
-  `DS1621: Digital Thermometer and
   Thermostat <git.linux.org>drivers/hwmon/ds1621.c>`__
   `DS1621 <maxim>DS1621>`__
-  `DS1631: High-Precision Digital Thermometer and
   Thermostat <git.linux.org>drivers/hwmon/ds1621.c>`__
   `DS1631 <maxim>DS1631>`__
-  `DS1721: Digital Thermometer and
   Thermostat <git.linux.org>drivers/hwmon/ds1621.c>`__
   `DS1721 <maxim>DS1721>`__
-  `DS1731: High-Precision Digital Thermometer and
   Thermostat <git.linux.org>drivers/hwmon/ds1621.c>`__
   `DS1731 <maxim>DS1731>`__
-  `DS1775: Digital Thermometer and Thermostat in
   SOT23 <git.linux.org>drivers/hwmon/lm75.c>`__
   `DS1775 <maxim>DS1775>`__
-  `DS1780: CPU Peripheral
   Monitor <git.linux.org>drivers/hwmon/adm9240.c>`__
   `DS1780 <maxim>DS1780>`__
-  `DS620: Low-Voltage, ±0.5°C Accuracy Digital Thermometer and
   Thermostat <git.linux.org>drivers/hwmon/ds620.c>`__
   `DS620 <maxim>DS620>`__
-  `DS7505: High-Precision Digital Thermometer and
   Thermostat <git.linux.org>drivers/hwmon/lm75.c>`__
   `DS7505 <maxim>DS7505>`__
-  `Fan Control IP core: Core to control the fan used for cooling Xilinx
   Zynq Ultrascale+ MPSoC <linux-drivers/hwmon/axi_fan_control>`__
   `axi_fan_control </resources/fpga/docs/axi_fan_control>`__
-  `LM75: Digital Temperature Sensor and Thermal Watchdog with 2-Wire
   Interface <git.linux.org>drivers/hwmon/lm75.c>`__
   `LM75 <maxim>LM75>`__
-  `LTC2945: Wide Range I2C Power
   Monitor <git.linux.org>drivers/hwmon/ltc2945.c>`__
   `LTC2945 <adi>LTC2945>`__
-  `LTC2947: High Precision Power and Energy
   Monitor <linux-drivers/hwmon/ltc2947>`__ `LTC2947 <adi>LTC2947>`__
-  `LTC2990: Quad I2C Voltage, Current and Temperature
   Monitor <git.linux.org>drivers/hwmon/ltc2990.c>`__
   `LTC2990 <adi>LTC2990>`__
-  `LTC2992: Dual Wide Range Power
   Monitor <git.linux.org>drivers/hwmon/ltc2992.c>`__
   `LTC2992 <adi>LTC2992>`__
-  `LTC4151: High Voltage I2C Current and Voltage
   Monitor <git.linux.org>drivers/hwmon/ltc4151.c>`__
   `LTC4151 <adi>LTC4151>`__
-  `LTC4215: Hot Swap Controller with I2C Compatible
   Monitoring <git.linux.org>drivers/hwmon/ltc4215.c>`__
   `LTC4215 <adi>LTC4215>`__
-  `LTC4222: Dual Hot Swap Controller with I2C Compatible
   Monitoring <git.linux.org>drivers/hwmon/ltc4222.c>`__
   `LTC4222 <adi>LTC4222>`__
-  `LTC4245: Multiple Supply Hot Swap Controller with I2C Compatible
   Monitoring <git.linux.org>drivers/hwmon/ltc4245.c>`__
   `LTC4245 <adi>LTC4245>`__
-  `LTC4251: Negative Voltage Hot Swap Controllers in
   SOT-23 <git.linux.org>drivers/hwmon/ltc4215.c>`__
   `LTC4251 <adi>LTC4251>`__
-  `LTC4260: Positive High Voltage Hot Swap Controller with I2C
   Compatible Monitoring <git.linux.org>drivers/hwmon/ltc4260.c>`__
   `LTC4260 <adi>LTC4260>`__
-  `LTC4261: Negative Voltage Hot Swap Controllers with ADC and I²C
   Monitoring <git.linux.org>drivers/hwmon/ltc4261.c>`__
   `LTC4261 <adi>LTC4261>`__
-  `MAX1110: +2.7V, Low-Power, Multichannel, Serial, 8-Bit
   ADCs <git.linux.org>drivers/hwmon/max1111.c>`__
   `MAX1110 <maxim>MAX1110>`__
-  `MAX1111: +2.7V, Low-Power, Multichannel, Serial, 8-Bit
   ADCs <git.linux.org>drivers/hwmon/max1111.c>`__
   `MAX1111 <maxim>MAX1111>`__
-  `MAX1112: +5V, Low-Power, Multichannel, Serial 8-Bit
   ADCs <git.linux.org>drivers/hwmon/max1111.c>`__
   `MAX1112 <maxim>MAX1112>`__
-  `MAX1113: +5V, Low-Power, Multichannel, Serial 8-Bit
   ADCs <git.linux.org>drivers/hwmon/max1111.c>`__
   `MAX1113 <maxim>MAX1113>`__
-  `MAX127: Multirange, +5V, 12-Bit DAS with 2-Wire Serial
   Interface <git.linux.org>drivers/hwmon/max127.c>`__
   `MAX127 <maxim>MAX127>`__
-  `MAX16065: 12-Channel/8-Channel Flash-Configurable System Managers
   with Nonvolatile Fault
   Registers <git.linux.org>drivers/hwmon/max16065.c>`__
   `MAX16065 <maxim>MAX16065>`__
-  `MAX16066: 12-Channel/8-Channel Flash-Configurable System Managers
   with Nonvolatile Fault
   Registers <git.linux.org>drivers/hwmon/max16065.c>`__
   `MAX16066 <maxim>MAX16066>`__
-  `MAX16067: 6-Channel, Flash-Configurable System Manager with
   Nonvolatile Fault
   Registers <git.linux.org>drivers/hwmon/max16065.c>`__
   `MAX16067 <maxim>MAX16067>`__
-  `MAX16068: 6-Channel, Flash-Configurable System Manager with
   Nonvolatile Fault
   Registers <git.linux.org>drivers/hwmon/max16065.c>`__
   `MAX16068 <maxim>MAX16068>`__
-  `MAX16070: 12-Channel/8-Channel, Flash-Configurable System Monitors
   with Nonvolatile Fault
   Registers <git.linux.org>drivers/hwmon/max16065.c>`__
   `MAX16070 <maxim>MAX16070>`__
-  `MAX16071: 12-Channel/8-Channel, Flash-Configurable System Monitors
   with Nonvolatile Fault
   Registers <git.linux.org>drivers/hwmon/max16065.c>`__
   `MAX16071 <maxim>MAX16071>`__
-  `MAX1617A: Remote/Local Temperature Sensor with SMBus Serial
   Interface <git.linux.org>drivers/hwmon/adm1021.c>`__
   `MAX1617A <maxim>MAX1617A>`__
-  `MAX1617: Remote/Local Temperature Sensor with SMBus Serial
   Interface <git.linux.org>drivers/hwmon/adm1021.c>`__
   `MAX1617 <maxim>MAX1617>`__
-  `MAX1619: Remote/Local Temperature Sensor with Dual Alarm Outputs and
   SMBus Serial Interface <git.linux.org>drivers/hwmon/max1619.c>`__
   `MAX1619 <maxim>MAX1619>`__
-  `MAX1668: Multichannel Remote/Local Temperature
   Sensors <git.linux.org>drivers/hwmon/max1668.c>`__
   `MAX1668 <maxim>MAX1668>`__
-  `MAX1805: Multichannel Remote/Local Temperature
   Sensors <git.linux.org>drivers/hwmon/max1668.c>`__
   `MAX1805 <maxim>MAX1805>`__
-  `MAX197: Multi-Range (±10V, ±5V, +10V, +5V), Single +5V, 12-Bit DAS
   with 8+4 Bus Interface <git.linux.org>drivers/hwmon/max197.c>`__
   `MAX197 <maxim>MAX197>`__
-  `MAX1989: Multichannel Remote/Local Temperature
   Sensors <git.linux.org>drivers/hwmon/max1668.c>`__
   `MAX1989 <maxim>MAX1989>`__
-  `MAX199: 8-Channel, Multi-Range, 5V, 12-Bit DAS with 8+4 Bus
   Interface and Fault
   Protection <git.linux.org>drivers/hwmon/max197.c>`__
   `MAX199 <maxim>MAX199>`__
-  `MAX31722: Digital Thermometers and Thermostats with SPI/3-Wire
   Interface <git.linux.org>drivers/hwmon/max31722.c>`__
   `MAX31722 <maxim>MAX31722>`__
-  `MAX31723: Digital Thermometers and Thermostats with SPI/3-Wire
   Interface <git.linux.org>drivers/hwmon/max31722.c>`__
   `MAX31723 <maxim>MAX31723>`__
-  `MAX31730: 3-Channel Remote Temperature
   Sensor <git.linux.org>drivers/hwmon/max31730.c>`__
   `MAX31730 <maxim>MAX31730>`__
-  `MAX31790: 6-Channel PWM-Output Fan RPM
   Controller <git.linux.org>drivers/hwmon/max31790.c>`__
   `MAX31790 <maxim>MAX31790>`__
-  `MAX6581: ±1°C Accurate 8-Channel Temperature
   Sensor <git.linux.org>drivers/hwmon/max6697.c>`__
   `MAX6581 <maxim>MAX6581>`__
-  `MAX6602: 5-Channel Precision Temperature
   Monitor <git.linux.org>drivers/hwmon/max6697.c>`__
   `MAX6602 <maxim>MAX6602>`__
-  `MAX6604: Precision Temperature Monitor for DDR Memory
   Modules <git.linux.org>drivers/hwmon/jc42.c>`__
   `MAX6604 <maxim>MAX6604>`__
-  `MAX6621: PECI-to-I²C
   Translator <git.linux.org>drivers/hwmon/max6621.c>`__
   `MAX6621 <maxim>MAX6621>`__
-  `MAX6622: 5-Channel Precision Temperature
   Monitor <git.linux.org>drivers/hwmon/max6697.c>`__
   `MAX6622 <maxim>MAX6622>`__
-  `MAX6625: 9-Bit/12-Bit Temperature Sensors with I²C-Compatible Serial
   Interface in a SOT23 <git.linux.org>drivers/hwmon/lm75.c>`__
   `MAX6625 <maxim>MAX6625>`__
-  `MAX6626: 9-Bit/12-Bit Temperature Sensors with I²C-Compatible Serial
   Interface in a SOT23 <git.linux.org>drivers/hwmon/lm75.c>`__
   `MAX6626 <maxim>MAX6626>`__
-  `MAX6635: 12-Bit Plus Sign Temperature Sensors with
   SMBus/I²C-Compatible Serial
   Interface <git.linux.org>drivers/hwmon/lm92.c>`__
   `MAX6635 <maxim>MAX6635>`__
-  `MAX6636: 7-Channel Precision Temperature
   Monitor <git.linux.org>drivers/hwmon/max6697.c>`__
   `MAX6636 <maxim>MAX6636>`__
-  `MAX6642: ±1°C, SMBus-Compatible Remote/Local Temperature Sensor with
   Overtemperature Alarm <git.linux.org>drivers/hwmon/max6642.c>`__
   `MAX6642 <maxim>MAX6642>`__
-  `MAX6646: +145°C Precision SMBus-Compatible Remote/Local Sensors with
   Overtemperature Alarms <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6646 <maxim>MAX6646>`__
-  `MAX6647: +145°C Precision SMBus-Compatible Remote/Local Sensors with
   Overtemperature Alarms <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6647 <maxim>MAX6647>`__
-  `MAX6648: Precision SMBus-Compatible Remote/Local Temperature Sensors
   with Overtemperature Alarms <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX648 <maxim>MAX648>`__
-  `MAX6649: +145°C Precision SMBus-Compatible Remote/Local Sensors with
   Overtemperature Alarms <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6649 <maxim>MAX6649>`__
-  `MAX6650: Fan-Speed Regulators and Monitors with SMBus/I²C-Compatible
   Interface <git.linux.org>drivers/hwmon/max6650.c>`__
   `MAX6650 <maxim>MAX6650>`__
-  `MAX6651: Fan-Speed Regulators and Monitors with SMBus/I²C-Compatible
   Interface and up to Four
   Tachometers <git.linux.org>drivers/hwmon/max6650.c>`__
   `MAX6651 <maxim>MAX6651>`__
-  `MAX6654: 1°C Accurate Remote/Local Temperature Sensor with SMBus
   Serial Interface <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6654 <maxim>MAX6654>`__
-  `MAX6657: ±1°C, SMBus-Compatible Remote/Local Temperature Sensors
   with Overtemperature Alarms <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6657 <maxim>MAX6657>`__
-  `MAX6658: ±1°C, SMBus-Compatible Remote/Local Temperature Sensors
   with Overtemperature Alarms <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6658 <maxim>MAX6658>`__
-  `MAX6659: ±1°C, SMBus-Compatible Remote/Local Temperature Sensors
   with Overtemperature Alarms <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6659 <maxim>MAX6659>`__
-  `MAX6680: ±1°C Fail-Safe Remote/Local Temperature Sensors with SMBus
   Interface <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6680 <maxim>MAX6680>`__
-  `MAX6681: ±1°C Fail-Safe Remote/Local Temperature Sensors with SMBus
   Interface <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6681 <maxim>MAX6681>`__
-  `MAX6689: 7-Channel Precision Temperature
   Monitor <git.linux.org>drivers/hwmon/max6697.c>`__
   `MAX6689 <maxim>MAX6689>`__
-  `MAX6692: Precision SMBus-Compatible Remote/Local Temperature Sensors
   with Overtemperature Alarms <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6692 <maxim>MAX6692>`__
-  `MAX6693: 7-Channel Precision Temperature Monitor with Beta
   Compensation <git.linux.org>drivers/hwmon/max6697.c>`__
   `MAX6693 <maxim>MAX6693>`__
-  `MAX6694: 5-Channel Precision Temperature Monitor with Beta
   Compensation <git.linux.org>drivers/hwmon/max6697.c>`__
   `MAX6694 <maxim>MAX6694>`__
-  `MAX6695: Dual Remote/Local Temperature Sensors with SMBus Serial
   Interfaces <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6695 <maxim>MAX6695>`__
-  `MAX6696: Dual Remote/Local Temperature Sensors with SMBus Serial
   Interface <git.linux.org>drivers/hwmon/lm90.c>`__
   `MAX6696 <maxim>MAX6696>`__
-  `MAX6697: 7-Channel Precision Temperature
   Monitor <git.linux.org>drivers/hwmon/max6697.c>`__
   `MAX6697 <maxim>MAX6697>`__
-  `MAX6698: 5-Channel Precision Temperature Monitor with Beta
   Compensation <git.linux.org>drivers/hwmon/max6697.c>`__
   `MAX6698 <maxim>MAX6698>`__
-  `MAX6699: 7-Channel Precision Remote-Diode, Thermistor, and Local
   Temperature Monitor <git.linux.org>drivers/hwmon/max6697.c>`__
   `MAX6699 <maxim>MAX6699>`__
-  `MAX6874: EEPROM-Programmable, Hex/Quad, Power-Supply
   Sequencers/Supervisors <git.linux.org>drivers/misc/eeprom/max6875.c>`__
   `MAX6874 <maxim>MAX6874>`__
-  `MAX6875: EEPROM-Programmable, Hex/Quad, Power-Supply
   Sequencers/Supervisors <git.linux.org>drivers/misc/eeprom/max6875.c>`__
   `MAX6875 <maxim>MAX6875>`__
-  `MAX6639: 2-Channel Temperature Monitor with Dual, Automatic, PWM
   Fan-Speed Controller <git.linux.org>drivers/hwmon/max6639.c>`__
   `MAX6639 <maxim>MAX6639>`__

PMbus
^^^^^

-  `ADM1075: −48 V Hot Swap Controller and Digital Power Monitor with
   PMBus Interface <git.linux.org>drivers/hwmon/pmbus/adm1275.c>`__
   `ADM1075 <adi>ADM1075>`__
-  `ADM1272: High Voltage Positive Hot Swap Controller and Digital Power
   Monitor with PMBus <git.linux.org>drivers/hwmon/pmbus/adm1275.c>`__
   `ADM1272 <adi>ADM1272>`__
-  `ADM1275: Hot Swap Controller and Digital Power Monitor with PMBus
   Interface <git.linux.org>drivers/hwmon/pmbus/adm1275.c>`__
   `ADM1275 <adi>ADM1275>`__
-  `ADM1276: Hot Swap Controller and Digital Power and Energy
   Monitoringwith PMBus
   Interface <git.linux.org>drivers/hwmon/pmbus/adm1275.c>`__
   `ADM1276 <adi>ADM1276>`__
-  `ADM1278: Hot Swap Controller and Digital Power and Energy Monitor
   with PMBus Interface <git.linux.org>drivers/hwmon/pmbus/adm1275.c>`__
   `ADM1278 <adi>ADM1278>`__
-  `ADM1293: Digital Power Monitor with PMbus
   Interface <git.linux.org>drivers/hwmon/pmbus/adm1275.c>`__
   `ADM1293 <adi>ADM1293>`__
-  `ADM1294: Digital Power Monitor with PMbus
   Interface <git.linux.org>drivers/hwmon/pmbus/adm1275.c>`__
   `ADM1294 <adi>ADM1294>`__
-  `LTC2972: 2-Channel PMBus Power System Manager Featuring Accurate
   Output Current
   Measurement <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC2972 <adi>LTC2972>`__
-  `LTC2974: 4-Channel PMBus Power System Manager Featuring Accurate
   Output Current
   Measurement <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC2974 <adi>LTC2974>`__
-  `LTC2975: 4-Channel PMBus Power System Manager Featuring Accurate
   Input Current and Energy
   Measurement <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC2975 <adi>LTC2975>`__
-  `LTC2977: 8-Channel PMBus Power System Manager Featuring Accurate
   Output Voltage
   Measurement <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC2977 <adi>LTC2977>`__
-  `LTC2978: Octal Digital Power Supply Manager with
   EEPROM <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC2978 <adi>LTC2978>`__
-  `LTC2979: 16-Channel PMBus Low-Voltage Power System
   Manager <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC2979 <adi>LTC2979>`__
-  `LTC2980: 16-Channel PMBus Power System
   Manager <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC2980 <adi>LTC2980>`__
-  `LTC3815: 6A Monolithic Synchronous DC/DC Step-Down Converter with
   Digital Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc3815.c>`__
   `LTC3815 <adi>LTC3815>`__
-  `LTC3880: Dual Output PolyPhase Step-Down DC/DC Controller with
   Digital Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC3880 <adi>LTC3880>`__
-  `LTC3882: Dual Output PolyPhase Step-Down DC/DC Voltage Mode
   Controller with Digital Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC3882 <adi>LTC3882>`__
-  `LTC3883: Single Phase Step-Down DC/DC Controller with Digital Power
   System Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC3883 <adi>LTC3883>`__
-  `LTC3884: Dual Output PolyPhase Step-Down Controller with
   Sub-Milliohm DCR Sensing and Digital Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC3884 <adi>LTC3884>`__
-  `LTC3886: 60V Dual Output Step-Down Controller with Digital Power
   System Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC3886 <adi>LTC3886>`__
-  `LTC3887: Dual Output PolyPhase Step-Down DC/DC Controller with
   Digital Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC3887 <adi>LTC3887>`__
-  `LTC3889: 60V Dual Output Step-Down Controller with Digital Power
   System Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC3889 <adi>LTC3889>`__
-  `LTC7880: 60V Dual Output Step-Up Controller with Digital Power
   System Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTC7880 <adi>LTC7880>`__
-  `LTM2987: 16-Channel μModule PMBus Power System
   Manager <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTM2987 <adi>LTM2987>`__
-  `LTM4644: Quad DC/DC μModule (Power Module) Regulator with
   Configurable 4A Output
   Array <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTM4644 <adi>LTM4644>`__
-  `LTM4664: 54VIN Dual 25A, Single 50A µModule Regulator with Digital
   Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTM4664 <adi>LTM4664>`__
-  `LTM4675: Dual 9A or Single 18A μModule Regulator with Digital Power
   System Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTM4675 <adi>LTM4675>`__
-  `LTM4676A: Dual 13A or Single 26A μModule (Power Module) Regulator
   with Digital Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTM4676A <adi>LTM4676A>`__
-  `LTM4676: Dual 13A or Single 26A μModule (Power Module) Regulator
   with Digital Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `Obsolete <adi>LTM4676>`__
-  `LTM4677: Dual 18A or Single 36A μModule (Power Module) Regulator
   with Digital Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTM4677 <adi>LTM4677>`__
-  `LTM4678: Dual 25A or Single 50A µModule Regulator with Digital Power
   System Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTM4678 <adi>LTM4678>`__
-  `LTM4680: Dual 30A or Single 60A µModule Regulator with Digital Power
   System Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTM4680 <adi>LTM4680>`__
-  `LTM4686: Ultrathin Dual 10A or Single 20A μModule Regulator with
   Digital Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTM4686 <adi>LTM4686>`__
-  `LTM4700: Dual 50A or Single 100A µModule Regulator with Digital
   Power System
   Management <git.linux.org>drivers/hwmon/pmbus/ltc2978.c>`__
   `LTM4700 <adi>LTM4700>`__
-  `MAX15301: InTune Automatically Compensated Digital PoL Controller
   with Driver and PMBus
   Telemetry <git.linux.org>drivers/hwmon/pmbus/max15301.c>`__
   `MAX15301 <maxim>MAX15301>`__
-  `MAX16064: Quad, Power-Supply Controller with Active-Voltage Output
   Control and PMBus
   Interface <git.linux.org>drivers/hwmon/pmbus/max16064.c>`__
   `MAX16064 <maxim>MAX16064>`__
-  `MAX20710: Integrated, Step-Down Switching Regulator with
   PMBus <git.linux.org>drivers/hwmon/pmbus/max20730.c>`__
   `MAX20710 <maxim>MAX20710>`__
-  `MAX20730: Integrated, Step-Down Switching Regulator with
   PMBus <git.linux.org>drivers/hwmon/pmbus/max20730.c>`__
   `MAX20730 <maxim>MAX20730>`__
-  `MAX20734: Integrated, Step-Down Switching Regulator with
   PMBus <git.linux.org>drivers/hwmon/pmbus/max20730.c>`__
   `MAX20734 <maxim>MAX20734>`__
-  `MAX20743: Integrated, Step-Down Switching Regulator with
   PMBus <git.linux.org>drivers/hwmon/pmbus/max20730.c>`__
   `MAX20743 <maxim>MAX20743>`__
-  `MAX20751: Multiphase Master with PMBus Interface and Internal Buck
   Converter <git.linux.org>drivers/hwmon/pmbus/max20751.c>`__
   `MAX20751 <maxim>MAX20751>`__
-  `MAX20796: Dual-Phase Scalable Integrated Voltage Regulator with
   PMBus Interface <git.linux.org>drivers/hwmon/pmbus/pmbus.c>`__
   `MAX20796 <maxim>MAX20796>`__
-  `MAX31785: 6-Channel Intelligent Fan
   Controller <git.linux.org>drivers/hwmon/pmbus/max31785.c>`__
   `MAX31785 <maxim>MAX31785>`__
-  `MAX34440: PMBus 6-Channel Power-Supply
   Manager <git.linux.org>drivers/hwmon/pmbus/max34440.c>`__
   `MAX34440 <maxim>MAX34440>`__
-  `MAX34441: PMBus 5-Channel Power-Supply Manager and Intelligent Fan
   Controller <git.linux.org>drivers/hwmon/pmbus/max34440.c>`__
   `MAX34441 <maxim>MAX34441>`__
-  `MAX34446: PMBus Power-Supply Data
   Logger <git.linux.org>drivers/hwmon/pmbus/max34440.c>`__
   `MAX34446 <maxim>MAX34446>`__
-  `MAX34451: PMBus 16-Channel V/I Monitor and 12-Channel
   Sequencer/Marginer <git.linux.org>drivers/hwmon/pmbus/max34440.c>`__
   `MAX34451 <maxim>MAX34451>`__
-  `MAX34460: PMBus 12-Channel Voltage Monitor and
   Sequencer <git.linux.org>drivers/hwmon/pmbus/max34440.c>`__
   `MAX34460 <maxim>MAX34460>`__
-  `MAX34461: PMBus 16-Channel Voltage Monitor and
   Sequencer <git.linux.org>drivers/hwmon/pmbus/max34440.c>`__
   `MAX34461 <maxim>MAX34461>`__
-  `MAX8688: Digital Power-Supply Controller/Monitor with PMBus
   Interface <git.linux.org>drivers/hwmon/pmbus/max8688.c>`__
   `MAX8688 <maxim>MAX8688>`__

Ethernet PHY
~~~~~~~~~~~~

-  `ADIN1100 - Robust, Industrial, Low Power 10BASE-T1L Ethernet
   PHY <linux-drivers/net-phy/adin1100>`__
-  `ADIN1200 - Robust, Industrial, Low Power 10/100 Ethernet
   PHY <linux-drivers/net-phy/adin>`__
-  `ADIN1300 - Robust, Industrial, Low Latency 10/100/1000 Gigabit
   Ethernet PHY <linux-drivers/net-phy/adin>`__

Ethernet MAC-PHY
~~~~~~~~~~~~~~~~

-  `ADIN1110 - Robust, Industrial, Low Power 10BASE-T1L Ethernet
   MAC-PHY <linux-drivers/net-mac-phy/adin1110>`__
-  `ADIN2111 - Low Complexity, 2-Port Ethernet Switch with Integrated
   10BASE-T1L PHYs <linux-drivers/net-mac-phy/adin2111>`__
-  `Open Alliance - 10BASE-T1x MAC-PHY Serial
   Interface <linux-drivers/net-mac-phy/open_alliance>`__

I2C Mux
~~~~~~~

-  `LTC4306: 4-Channel, 2-Wire Bus Multiplexer with Capacitance
   Buffering <git.linux.org>drivers/i2c/muxes/i2c-mux-ltc4306.c>`__
   `LTC4306 <adi>LTC4306>`__
-  `LTC4305: 2-Channel, 2-Wire Bus Multiplexer with Capacitance
   Buffering <git.linux.org>drivers/i2c/muxes/i2c-mux-ltc4306.c>`__
   `LTC4305 <adi>LTC4305>`__
-  `MAX9286: Quad 1.5Gbps GMSL Deserializer with Coax or STP Input and
   CSI-2 Output <git.linux.org>drivers/media/i2c/max9286.c>`__
   `MAX9286 <maxim>MAX9286>`__
-  `MAX9271: 16-Bit GMSL Serializer with Coax or STP Cable
   Drive <git.linux.org>drivers/media/i2c/max9271.c>`__
   `MAX9271 <maxim>MAX9271>`__

IIO - Accelerometers
~~~~~~~~~~~~~~~~~~~~

-  `ADXL312, ADXL313, ADXL314: Low Noise, Low Drift, Low Power, 3-Axis
   MEMS Accelerometers <linux-drivers/iio-accelerometer/adxl313>`__
-  `ADXL345: 3-Axis, ±2 g/±4 g/±8 g/±16 g Digital
   Accelerometer <linux-drivers/input-misc/adxl345>`__
-  `ADXL346: 3-Axis, ±2 g/±4 g/±8 g/±16 g Ultralow Power Digital
   Accelerometer <linux-drivers/input-misc/adxl345>`__
-  `ADXL355: Low Noise, Low Drift, Low Power, 3-Axis MEMS
   Accelerometers <linux-drivers/iio-accelerometer/adxl355>`__
-  `ADXL362: Micropower 3-Axis MEMS Accelerometer, Programmable Digital
   Output, ±2/±4/±8 g Range <linux-drivers/input-misc/adxl362>`__
-  `ADXL367: Micropower 3-Axis MEMS Accelerometer, Programmable Digital
   Output, ±2 g/±4 g/±8 g
   Range <linux-drivers/iio-accelerometer/adxl367>`__
-  `ADXL372: Micropower 3-Axis MEMS Accelerometer, Programmable Digital
   Output, ±200 g Range <linux-drivers/iio-accelerometer/adxl372>`__
-  `ADXL375: 3-Axis, ±200 g Digital
   Accelerometer <linux-drivers/input-misc/adxl345>`__
-  `ADIS16201: Programmable Dual-Axis Inclinometer /
   Accelerometer <linux-drivers/iio-accelerometer/adis16201>`__
-  `ADIS16203: Programmable 360°
   Inclinometer <linux-drivers/iio-accelerometer/adis16203>`__
-  `ADIS16209: High Accuracy, Dual-Axis Digital Inclinometer and
   Accelerometer <linux-drivers/iio-accelerometer/adis16209>`__
-  `ADIS16240: Low Power Programmable Impact Sensor and
   Recorder <linux-drivers/iio-accelerometer/adis16240>`__

IIO - Amplifiers
~~~~~~~~~~~~~~~~

-  `AD8366: DC to 600 MHz, Dual-Digital Variable Gain
   Amplifiers <linux-drivers/iio-amplifiers/ad8366>`__
-  `ADA4961: Low Distortion, 3.2 GHz, RF
   DGA <linux-drivers/iio-amplifiers/ad8366>`__
-  `ADL5240: 100 MHz TO 4000 MHz RF/IF Digitally Controlled
   VGA <linux-drivers/iio-amplifiers/ad8366>`__
-  `ADRF5720: 0.5 dB LSB, 6-Bit, Silicon Digital Attenuator, 9 kHz to 40
   GHz <linux-drivers/iio-amplifiers/ad8366>`__
-  `ADRF5730: 0.5 dB LSB, 6-Bit, Silicon Digital Attenuator, 100 MHz to
   40 GHz <linux-drivers/iio-amplifiers/ad8366>`__
-  `ADRF5731: 2 dB LSB, 4-Bit, Silicon Digital Attenuator, 100 MHz to 40
   GHz <linux-drivers/iio-amplifiers/ad8366>`__
-  `HMC271A: 1dB LSB 5-Bit Digital Attenuator SMT, 0.7 - 3.7
   GHz <linux-drivers/iio-amplifiers/ad8366>`__
-  `ADA4250 Programmable Gain Instrumentation Amplifier Linux
   Driver <linux-drivers/iio-amplifiers/ada4250>`__
-  `HMC425: 0.5 dB LSB, GaAs MMIC, 6-BIT DIGITAL POSITIVE CONTROL
   ATTENUATOR, 2.2 - 8.0 GHz <linux-drivers/iio-amplifiers/hmc425a>`__
   `Obsolete <adi>HMC425>`__
-  `HMC425A: 0.5 dB LSB, GaAs MMIC, 6-BIT DIGITAL POSITIVE CONTROL
   ATTENUATOR, 2.2 - 8.0 GHz <linux-drivers/iio-amplifiers/hmc425a>`__
   `HMC425A <adi>HMC425A>`__
-  `HMC540S: 1 dB LSB Silicon MMIC 4-Bit Digital Positive Control
   Attenuator 0.1 - 8 GHz <linux-drivers/iio-amplifiers/hmc425a>`__
-  `HMC1018A: 1.0 dB LSB GaAs MMIC 5-BIT DIGITAL ATTENUATOR, 0.1 - 30
   GHz <linux-drivers/iio-amplifiers/ad8366>`__
-  `HMC1019A: 0.5 dB LSB GaAs MMIC 5-BIT DIGITAL ATTENUATOR, 0.1 - 30
   GHz <linux-drivers/iio-amplifiers/ad8366>`__
-  `HMC1119: 0.25 dB LSB, 7-Bit, Silicon Digital Attenuator, 0.1 GHz to
   6.0 GHz <linux-drivers/iio-amplifiers/ad8366>`__

IIO - Analog to Digital Converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `AD4003: 18-Bit, 2 MSPS, Differential SAR
   ADC <linux-drivers/iio-adc/ad400x>`__
-  `AD4007: 18-Bit, 1 MSPS, Differential SAR
   ADC <linux-drivers/iio-adc/ad400x>`__
-  `AD4011: 18-Bit, 500 kSPS, Differential SAR
   ADC <linux-drivers/iio-adc/ad400x>`__
-  `AD4020: 20-bit, 1.8 MSPS, Differential SAR
   ADC <linux-drivers/iio-adc/ad400x>`__
-  `AD4030-24: 24-Bit, 2 MSPS/500 kSPS, SAR
   ADC <linux-drivers/iio-adc/ad4630>`__
-  `AD4630-16: 24-Bit, 2 MSPS/500 kSPS, Dual Channel SAR
   ADC <linux-drivers/iio-adc/ad4630>`__
-  `AD4630-24: 24-Bit, 2 MSPS/500 kSPS, Dual Channel SAR
   ADC <linux-drivers/iio-adc/ad4630>`__
-  `AD4130: 32 μA, Ultra Low Power, 24-Bit Sigma-Delta ADC with
   Integrated PGA and FIFO <git.linux.org>drivers/iio/adc/ad4130.c>`__
   `AD4130 <adi>AD4130>`__
-  `AD6684: 135 MHz Quad IF Receiver </linux-drivers/iio-adc/ad9208>`__
-  `AD6688: RF Diversity and 1.2GHz BW Observation
   Receiver </linux-drivers/iio-adc/ad9208>`__
-  `AD7091: 1 MSPS, Ultralow Power 12-Bit ADC in 8-Lead
   LFCSP <linux-drivers/iio-adc/ad7476a>`__
-  `AD7091R: 1 MSPS, ultra low power 12-Bit ADC in 10 LEAD LFCSP and
   MSOP <linux-drivers/iio-adc/ad7476a>`__
-  `AD7091R-5: 4-Channel, 12-bit Ultra Low Power
   ADC <linux-drivers/iio-adc/ad7091r5>`__
-  `AD7091R-8: 8-Channel, 12-bit Ultra Low Power
   ADC <linux-drivers/iio-adc/ad7091r8>`__
-  `AD7124: 24-Bit Low Power Sigma-Delta ADC with PGA and
   Reference <linux-drivers/iio-adc/ad7124>`__
-  `AD7124-4: 4-Channel, Low Noise, Low Power, 24-Bit, Sigma-Delta ADC
   with PGA and Reference <linux-drivers/iio-adc/ad7124>`__
-  `AD7124-8: 8-Channel, Low Noise, Low Power, 24-Bit, Sigma-Delta ADC
   with PGA and Reference <linux-drivers/iio-adc/ad7124>`__
-  `AD7170: 12-Bit Low Power Sigma-Delta
   ADC <linux-drivers/iio-adc/ad7780>`__
-  `AD7171: 16-Bit Low Power Sigma-Delta
   ADC <linux-drivers/iio-adc/ad7780>`__
-  `AD7172-2: Low Power, 24-Bit, 31.25 kSPS, Sigma-Delta ADC with True
   Rail-to-Rail
   Buffers <linux.github>master?drivers/iio/adc/ad7173.c>`__
   `AD7172-2 <adi>AD7172-2>`__
-  `AD7173-8: Low Power, 8-/16-Channel, 31.25 kSPS, 24-Bit, Highly
   Integrated Sigma-Delta
   ADC <linux.github>master?drivers/iio/adc/ad7173.c>`__
   `AD7172-2 <adi>AD7172-2>`__
-  `AD7175-2: 24-Bit, 250 kSPS, Sigma-Delta ADC with 20 µs Settling and
   True Rail-to-Rail
   Buffers <linux.github>master?drivers/iio/adc/ad7173.c>`__
   `AD7172-2 <adi>AD7172-2>`__
-  `AD7176-2: 24-Bit, 250 kSPS Sigma Delta ADC with 20 µs
   Settling <linux.github>master?drivers/iio/adc/ad7173.c>`__
   `AD7172-2 <adi>AD7172-2>`__
-  `AD7190: 4.8 kHz Ultra-Low Noise 24-Bit Sigma-Delta ADC with
   PGA <linux-drivers/iio-adc/ad7192>`__
-  `AD7192: 4.8 kHz Ultra-Low Noise 24-Bit Sigma-Delta ADC with
   PGA <linux-drivers/iio-adc/ad7192>`__
-  `AD7193: 4-Channel, 4.8 kHz Ultra-Low Noise 24-Bit Sigma-Delta ADC
   with PGA <linux-drivers/iio-adc/ad7192>`__
-  `AD7194: 8-Channel, 4.8 kHz, Ultralow Noise, 24-Bit Sigma-Delta ADC
   with PGA <linux-drivers/iio-adc/ad7192>`__
-  `AD7195: 4.8 kHz, Ultralow Noise, 24-Bit Sigma-Delta ADC with PGA and
   AC Excitation <linux-drivers/iio-adc/ad7192>`__
-  `AD7265: Differential/Single-Ended Input, Dual 1 MSPS, 12-Bit,
   3-Channel SAR A/D Converter <linux-drivers/iio-adc/ad7266>`__
-  `AD7266: Differential/Single-Ended Input, Dual, Simultaneous
   Sampling, 2 MSPS, 12-Bit, 3-Channel SAR A/D
   Converter <linux-drivers/iio-adc/ad7266>`__
-  `AD7273: 3 MSPS 10-Bit ADC in TSOT and MSOP
   Packages <linux-drivers/iio-adc/ad7476a>`__
-  `AD7274: 3 MSPS 12-Bit A/D Converter in TSOT and MSOP
   Packages <linux-drivers/iio-adc/ad7476a>`__
-  `AD7276: 3 MSPS 12-Bit ADC in 8-Lead
   MSOP <linux-drivers/iio-adc/ad7476a>`__
-  `AD7277: 3 MSPS 10-Bit ADC in 8-Lead
   MSOP <linux-drivers/iio-adc/ad7476a>`__
-  `AD7278: 3 MSPS 8-Bit ADC in 8-Lead
   MSOP <linux-drivers/iio-adc/ad7476a>`__
-  `AD7280A: Lithium Ion Battery Monitoring
   System <linux-drivers/iio-adc/ad7280a>`__
-  `AD7291: 8-Channel, I2C, 12-Bit SAR ADC with Temperature
   Sensor <linux-drivers/iio-adc/ad7291>`__
-  `AD7292: 10-Bit Monitor & Control System with ADC, DACs, Temperature
   Sensor and GPIOs <git.linux.org>drivers/iio/adc/ad7292.c>`__
   `AD7292 <adi>AD7292>`__
-  `AD7298: 8-Channel, 1MSPS, 12-Bit SAR ADC with Temperature
   Sensor <linux-drivers/iio-adc/ad7298>`__
-  `AD7380: 4MSPS Dual Simultaneous Sampling, 16-BIT SAR ADC,
   Differential Input <linux-drivers/iio-adc/ad738x>`__
-  `AD7381: 4MSPS Dual Simultaneous Sampling, 14-BIT SAR ADC,
   Differential Input <linux-drivers/iio-adc/ad738x>`__
-  `AD7386: 4-Channel, 4 MSPS, 16-Bit Dual Simultaneous Sampling SAR
   ADC <linux-drivers/iio-adc/ad738x>`__
-  `AD7387: 4-Channel, 4 MSPS, 14-Bit, Dual, Simultaneous Sampling SAR
   ADC <linux-drivers/iio-adc/ad738x>`__
-  `AD7388: 4-Channel, 4 MSPS, 12-Bit, Dual, Simultaneous Sampling SAR
   ADCs <linux-drivers/iio-adc/ad738x>`__
-  `AD7466: 1.6 V Micro-Power 12-Bit
   ADC <linux-drivers/iio-adc/ad7476a>`__
-  `AD7467: 1.6 V Micro-Power 10-Bit
   ADC <linux-drivers/iio-adc/ad7476a>`__
-  `AD7468: 1.6 V Micro-Power 8-Bit
   ADC <linux-drivers/iio-adc/ad7476a>`__
-  `AD7475: 1 MSPS, 12-Bit A/D Converter in MSOP-8 or
   SOIC-8 <linux-drivers/iio-adc/ad7476a>`__
-  `AD7476: 1MSPS, 12-Bit ADC in 6 Lead
   SOT-23 <linux-drivers/iio-adc/ad7476a>`__
-  `AD7476A: 12-Bit, 1 MSPS, Low-Power A/D Converter in SC70 and MSOP
   Packages <linux-drivers/iio-adc/ad7476a>`__
-  `AD7477: 1MSPS, 10-Bit ADC in 6 Lead
   SOT-23 <linux-drivers/iio-adc/ad7476a>`__
-  `AD7477A: 10-Bit, 1 MSPS, Low-Power A/D Converter in SC70 and MSOP
   Packages <linux-drivers/iio-adc/ad7476a>`__
-  `AD7478: 8-Bit, 1 MSPS, Low Power Successive Approximation ADC Which
   Operates From A Single 2.35 V to 5.25 V Power
   Supply <linux-drivers/iio-adc/ad7476a>`__
-  `AD7478A: 8-Bit, 1 MSPS, Low-Power A/D Converter in SC70 and MSOP
   Packages <linux-drivers/iio-adc/ad7476a>`__
-  `AD7495: 1 MSPS, 12-Bit A/D Converter in MSOP-8 or
   SOIC-8 <linux-drivers/iio-adc/ad7476a>`__
-  `AD7605-4: 4-Channel DAS with 16-Bit, Bipolar, Simultaneous Sampling
   ADC <linux-drivers/iio-adc/ad7606>`__
-  `AD7606-4: 4-Channel DAS with 16-Bit, Bipolar, Simultaneous Sampling
   ADC <linux-drivers/iio-adc/ad7606>`__
-  `AD7606-6: 6-Channel DAS with 16-Bit, Bipolar, Simultaneous Sampling
   ADC <linux-drivers/iio-adc/ad7606>`__
-  `AD7606: 8-Channel DAS with 16-Bit, Bipolar, Simultaneous Sampling
   ADC <linux-drivers/iio-adc/ad7606>`__
-  `AD7606B: 8-Channel DAS with 16-Bit, 800 kSPS Bipolar Input,
   Simultaneous Sampling ADC </linux-drivers/iio-adc/ad7606>`__
-  `AD7616: 16-Channel DAS with 16-Bit, Bipolar Input, Dual Simultaneous
   Sampling ADC <linux-drivers/iio-adc/ad7606>`__
-  `AD7680: 3 mW, 100 kSPS, 16-Bit ADC in 6 Lead
   SOT-23 <linux-drivers/iio-adc/ad7476a>`__
-  `AD7682: 16-Bit, 4-Channel, 250 kSPS PulSAR
   ADC <linux-drivers/iio-adc/ad7476a>`__
-  `AD7683: 100 kSPS 16-Bit PulSAR® A/D Converter in
   µSOIC/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7684: 16-Bit, 100 kSPS PulSAR®, Differential ADC in
   MSOP <linux-drivers/iio-adc/ad7476a>`__
-  `AD7685: 16-Bit, 250 kSPS PulSAR® ADC in
   MSOP/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7686: 500 kSPS 16-BIT PulSAR® A/D Converter in
   MSOP/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7687: 16-Bit, 1.5 LSB INL, 250 kSPS PulSAR® Differential ADC in
   MSOP/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7688: 500 kSPS 16- BIT Differential PulSAR® A/D Converter in
   µSOIC/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7689: 16-Bit, 8-Channel, 250 kSPS PulSAR®
   ADC <git.linux.org>drivers/iio/adc/ad7949.c>`__
   `AD7689 <adi>AD7689>`__
-  `AD7690: 18-Bit, 1.5 LSB INL, 400 kSPS PulSAR® Differential ADC in
   MSOP/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7691: 18-Bit, 1.5 LSB INL, 250 kSPS PulSAR® Differential ADC in
   MSOP/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7693: 16-Bit, ±0.5 LSB, 500 kSPS PulSAR® Differential A/D
   Converter in MSOP/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7694: 250 kSPS 16-BIT PulSAR® A/D Converter in
   µSOIC <linux-drivers/iio-adc/ad7476a>`__
-  `AD7766-1: 24-Bit, 8.5 mW, 109 dB, 64 kSPS
   ADC <linux-drivers/iio-adc/ad7766>`__
-  `AD7766-2: 24-Bit, 8.5 mW, 109 dB, 32 kSPS
   ADC <linux-drivers/iio-adc/ad7766>`__
-  `AD7766: 24-Bit, 8.5 mW, 109 dB, 128 kSPS
   ADC <linux-drivers/iio-adc/ad7766>`__
-  `AD7767-1: 24-Bit, 8.5 mW, 109 dB, 64 kSPS
   ADC <linux-drivers/iio-adc/ad7766>`__
-  `AD7767-2: 24-Bit, 8.5 mW, 109 dB, 32 kSPS
   ADC <linux-drivers/iio-adc/ad7766>`__
-  `AD7767: 24-Bit, 8.5 mW, 109 dB, 128 kSPS
   ADC <linux-drivers/iio-adc/ad7766>`__
-  `AD7768-1: 24-Bit, Power Scaling, Sigma-Delta
   ADC <linux-drivers/iio-adc/ad7768-1>`__
-  `AD7768: 24-Bit, Simultaneous Sampling, Power Scaling
   ADC <linux-drivers/iio-adc/ad7768>`__
-  `AD7780: 24-Bit Pin-Programmable Low Power Sigma-Delta
   ADC <linux-drivers/iio-adc/ad7780>`__
-  `AD7781: 20-Bit, Pin-Programmable, Ultralow Power Sigma-Delta
   ADC <linux-drivers/iio-adc/ad7780>`__
-  `AD7785: 3-Channel, Low Noise, Low Power, 20-Bit Σ-Δ ADC with On-Chip
   In-Amp and Reference <linux-drivers/iio-adc/ad7793>`__
-  `AD7787: Low Power, 2-Channel 24-Bit Sigma-Delta
   ADC <linux-drivers/iio-adc/ad7791>`__
-  `AD7788: 16-Bit, Single-Channel, Ultra Low Power, Sigma-Delta A/D
   Converter <linux-drivers/iio-adc/ad7791>`__
-  `AD7789: 24-Bit, Single-Channel, Ultra Low Power, Sigma-Delta A/D
   Converter <linux-drivers/iio-adc/ad7791>`__
-  `AD7790: 16-Bit, Single-Channel, Ultra Low Power, Sigma-Delta A/D
   Converter <linux-drivers/iio-adc/ad7791>`__
-  `AD7791: 24-Bit, Single-Channel, Ultra Low Power, Sigma-Delta A/D
   Converter <linux-drivers/iio-adc/ad7791>`__
-  `AD7792: 3-Channel, Low Noise, Low Power, 16-Bit Sigma Delta ADC with
   On-Chip In-Amp and Reference <linux-drivers/iio-adc/ad7793>`__
-  `AD7793: 3-Channel, Low Noise, Low Power, 24-Bit Sigma Delta ADC with
   On-Chip In-Amp and Reference <linux-drivers/iio-adc/ad7793>`__
-  `AD7794: 6-Channel, Low Noise, Low Power, 24-Bit Sigma Delta ADC with
   On-Chip In-Amp and Reference <linux-drivers/iio-adc/ad7793>`__
-  `AD7795: 6-Channel, Low Noise, Low Power, 16-Bit Sigma Delta ADC with
   On-Chip In-Amp and Reference <linux-drivers/iio-adc/ad7793>`__
-  `AD7796: Low Power 16-Bit Sigma-Delta A/D Converter for Bridge
   Sensors <linux-drivers/iio-adc/ad7793>`__
-  `AD7797: Low Power 24-Bit Sigma-Delta A/D Converter for Bridge
   Sensors <linux-drivers/iio-adc/ad7793>`__
-  `AD7798: 3-Channel, Low Noise, Low Power, 16-Bit, Sigma Delta ADC
   with On-Chip In-Amp <linux-drivers/iio-adc/ad7793>`__
-  `AD7799: 3-Channel, Low Noise, Low Power, 24-Bit, Sigma Delta ADC
   with On-Chip In-Amp <linux-drivers/iio-adc/ad7793>`__
-  `AD7816:Temperature
   Sensor <git.linux.org>drivers/staging/iio/adc/ad7816.c>`__
   `Obsolete <adi>AD7816>`__
-  `AD7817:Temperature Sensor (On Chip) 4-Channel, 9 µs, 10-Bit
   ADC <git.linux.org>drivers/staging/iio/adc/ad7816.c>`__
   `AD7817 <adi>AD7817>`__
-  `AD7818:Temperature Sensor (On Chip) 1-Channel, 9 µs, 10-Bit
   ADC <git.linux.org>drivers/staging/iio/adc/ad7816.c>`__
   `AD7818 <adi>AD7818>`__
-  `AD7887: 2.7 V to 5.25 V, Micropower, 2-Channel, 125 kSPS, 12-Bit ADC
   in 8-Lead MSOP <linux-drivers/iio-adc/ad7887>`__
-  `AD7904: 4-Channel, 1 MSPS, 8-Bit A/D Converter with
   Sequencer <git.linux.org>drivers/iio/adc/ad7923.c>`__
   `AD7904 <adi>AD7904>`__
-  `AD7908: 8-Channel, 1 MSPS, 8-Bit ADC with Sequencer in 20-Lead
   TSSOP <git.linux.org>drivers/iio/adc/ad7923.c>`__
   `AD7908 <adi>AD7908>`__
-  `AD7910: 250 KSPS, 10-Bit ADC in 6 Lead
   SC70 <linux-drivers/iio-adc/ad7476a>`__
-  `AD7914: 4-Channel, 1 MSPS, 10-Bit A/D Converter with
   Sequencer <git.linux.org>drivers/iio/adc/ad7923.c>`__
   `AD7914 <adi>AD7914>`__
-  `AD7918: 8-Channel, 1 MSPS, 10-Bit ADC with Sequencer in 20-Lead
   TSSOP <git.linux.org>drivers/iio/adc/ad7923.c>`__
   `AD7918 <adi>AD7918>`__
-  `AD7920: 250 KSPS, 12-Bit ADC in 6 Lead
   SC70 <linux-drivers/iio-adc/ad7476a>`__
-  `AD7923: 4-Channel 200 kSPS, 12-Bit A/D Converter with
   Sequencer <git.linux.org>drivers/iio/adc/ad7923.c>`__
   `AD7923 <adi>AD7923>`__
-  `AD7924: 4-Channel, 1 MSPS, 12-Bit A/D Converter with
   Sequencer <git.linux.org>drivers/iio/adc/ad7923.c>`__
   `AD7924 <adi>AD7924>`__
-  `AD7928: 8-Channel, 1 MSPS, 12-Bit A/D Converter with
   Sequencer <git.linux.org>drivers/iio/adc/ad7923.c>`__
   `AD7928 <adi>AD7928>`__
-  `AD7940: AD7940: 3 MW, 100 KSPS, 14-Bit ADC in 6-Lead
   SOT-23 <linux-drivers/iio-adc/ad7476a>`__
-  `AD7942: 14-Bit, 250 kSPS PulSAR®, Pseudo Differential ADC in
   MSOP/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7946: 14-Bit, 500 kSPS PulSAR® ADC in
   MSOP <linux-drivers/iio-adc/ad7476a>`__
-  `AD7949: 14-Bit, 8-Channel, 250 kSPS PulSAR
   ADC <git.linux.org>drivers/iio/adc/ad7949.c>`__
   `AD7949 <adi>AD7949>`__
-  `AD7980: 16-Bit, 1 MSPS PulSAR® ADC in
   MSOP/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7982: 18-Bit, 1 MSPS PulSAR® 7.0 mW ADC in
   MSOP/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7984: 18-Bit, 1.33 MSPS PulSAR® 10.5 mW ADC in
   MSOP/QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7985: 16-Bit, 2.5 MSPS PulSAR 11 mW ADC in
   QFN <linux-drivers/iio-adc/ad7476a>`__
-  `AD7988-1: 16-Bit, 100 kSPS, Ultra Low Power 16-Bit SAR
   ADC <linux-drivers/iio-adc/ad7476a>`__
-  `AD7988-5: 16-Bit, 500 kSPS, Ultra Low Power 16-Bit SAR
   ADC <linux-drivers/iio-adc/ad7476a>`__
-  `AD7991: 4-Channel, 12-Bit ADC with I2C Compatible Interface in
   8-Lead SOT-23 <linux-drivers/iio-adc/ad7998>`__
-  `AD7992: 2-Channel, 12-Bit ADC with I2C Compatible Interface in
   10-Lead MSOP <linux-drivers/iio-adc/ad7998>`__
-  `AD7993: 4-Channel, 10-Bit ADC with I2C Compatible Interface in
   16-Lead TSSOP <linux-drivers/iio-adc/ad7998>`__
-  `AD7994: 4 Channel, 12-Bit ADC with I2C Compatible Interface in
   16-Lead TSSOP <linux-drivers/iio-adc/ad7998>`__
-  `AD7995: 4-Channel, 10-Bit ADC with I2C Compatible Interface in
   8-Lead SOT-23 <linux-drivers/iio-adc/ad7998>`__
-  `AD7997: 8-Channel, 10-Bit ADC with I2C Compatible Interface in
   20-Lead TSSOP <linux-drivers/iio-adc/ad7998>`__
-  `AD7998: 8-Channel, 12-Bit ADC with I2C Compatible Interface in
   20-Lead TSSOP <linux-drivers/iio-adc/ad7998>`__
-  `AD7999: 4-Channel, 8-Bit ADC with I2C Compatible Interface in 8-Lead
   SOT-23 <linux-drivers/iio-adc/ad7998>`__
-  `AD9083 16-Channel, 125 MHz Bandwidth, JESD204B Analog-to-Digital
   Converter <linux-drivers/iio-adc/ad9083>`__
-  `AD9207 12-Bit, 6 GSPS, JESD204B/JESD204C Dual
   ADC <linux-drivers/iio-mxfe/ad9081>`__
-  `AD9208: 14-Bit, 3GSPS, JESD204B, Dual Analog-to-Digital
   Converter </resources/tools-software/linux-drivers/iio-adc/ad9208>`__
-  `AD9209 12-Bit, 4GSPS, JESD204B/C, Quad Analog-to-Digital
   Converter <linux-drivers/iio-mxfe/ad9081>`__
-  `AD9234: 12-Bit, 1 GSPS JESD204B, Dual Analog-to-Digital
   Converter <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9250: 14-Bit, 170 MSPS/250 MSPS, JESD204B, Dual Analog-to-Digital
   Converter <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9265: 16-Bit, 125 MSPS/105 MSPS/80 MSPS, 1.8 V Analog-to-Digital
   Converter <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9434: 12-BIT, 370 MSPS/500 MSPS, 1.8 V ANALOG-TO-DIGITAL
   CONVERTER <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9467: 16-Bit, 200 MSPS/250 MSPS Analog-to-Digital
   Converter <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9625: 12-BIT, 2.0/2.5 GSPS, 1.3 V/2.5 V ANALOG-TO-DIGITAL
   CONVERTER <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9643: 14-Bit, 170/210/250 MSPS, 1.8 V Dual Analog-to-Digital
   Converter (ADC) <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9649: 14-Bit, 20/40/65/80 MSPS, 1.8 V Analog-to-Digital Converter
   (ADC) <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9652: 16-bit, 310 MSPS, 3.3/1.8 V Dual Analog-to-Digital
   Converter <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9680: 14-Bit, 1000 MSPS JESD204B, Dual Analog-to-Digital
   Converter <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9683: 14-BIT, 170 MSPS/250 MSPS, JESD204B, ANALOG-TO-DIGITAL
   CONVERTER <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9684: 14-Bit, 500 MSPS LVDS, Dual Analog-to-Digital
   Converter <linux-drivers/iio-adc/axi-adc-hdl>`__
-  `AD9689: 14-Bit, 2.0 GSPS/2.6 GSPS, JESD204B, Dual Analog-to-Digital
   Converter </linux-drivers/iio-adc/ad9208>`__
-  `AD9694: Quad 14-Bit, 500 MSPS, 1.2 V/2.5 V Analog-to-Digital
   Converter </linux-drivers/iio-adc/ad9208>`__
-  `AD9695: 14-Bit, 1300 MSPS/625 MSPS, JESD204B, Dual Analog-to-Digital
   Converter </linux-drivers/iio-adc/ad9208>`__
-  `AD9697: 14-Bit, 1300 MSPS, JESD204B, Analog-to-Digital
   Converter </linux-drivers/iio-adc/ad9208>`__
-  `ADAQ4003: 18-Bit 2 MSPS μModule Data Acquisition System in
   BGA <linux-drivers/iio-adc/ad400x>`__
-  `ADAQ4224: 24-Bit, 2 MSPS μModule Data Acquisition
   Solution <linux-drivers/iio-adc/ad4630>`__
-  `ADAQ8092: 14-Bit, 105 MSPS,
   μModule <linux-drivers/iio-adc/adaq8092>`__
-  `ADAS1000: Low Power, 5-ELECTRODE ELECTROCARDIOGRAM (ECG) ANALOG
   FRONT END (AFE) <linux-drivers/iio-adc/adas1000>`__
-  `ADT7516: SPI/I2C Compatible,Temperature Sensor, 4-Channel ADC and
   Quad Voltage
   Output <git.linux.org>drivers/staging/iio/addac/adt7316.c>`__
   `ADT7516 <adi>ADT7516>`__
-  `ADT7517: SPI-/I2C-Compatible, Temperature Sensor, 4-Channel ADC and
   Quad Voltage
   Output <git.linux.org>drivers/staging/iio/addac/adt7316.c>`__
   `ADT7517 <adi>ADT7517>`__
-  `ADT7519: SPI-/I2C-Compatible, Temperature Sensor, 4-Channel ADC and
   Quad Voltage
   Output <git.linux.org>drivers/staging/iio/addac/adt7316.c>`__
   `Obsolete <adi>ADT7519>`__
-  `LTC2314-14: 14-Bit, 4.5Msps Serial Sampling ADC in
   TSOT <linux-drivers/iio-adc/ad7476a>`__
   `LTC2314-14 <adi>LTC2314-14>`__
-  `LTC2471: Selectable 208sps/833sps, 16-Bit I2C ΔΣ ADCs with 10ppm/°C
   Max Precision Reference <git.linux.org>drivers/iio/adc/ltc2471.c>`__
   `LTC2471 <adi>LTC2471>`__
-  `LTC2473: Selectable 208sps/833sps, 16-Bit I2C ΔΣ ADCs with 10ppm/°C
   Max Precision Reference <git.linux.org>drivers/iio/adc/ltc2471.c>`__
   `LTC2473 <adi>LTC2473>`__
-  `LTC2485: 24-Bit ΔΣ ADC with Easy Drive Input Current Cancellation
   and I2C Interface <git.linux.org>drivers/iio/adc/ltc2485.c>`__
   `LTC2485 <adi>LTC2485>`__
-  `LTC2488: 16-Bit 2-/4-Channel ΔΣ ADC with Easy Drive Input Current
   Cancellation <git.linux.org>drivers/spi/spidev.c>`__
   `LTC2488 <adi>LTC2488>`__
-  `LTC2496: 16-Bit 8-/16-Channel ΔΣ ADC with Easy Drive Input Current
   Cancellation <git.linux.org>drivers/iio/adc/ltc2497.c>`__
   `LTC2496 <adi>LTC2496>`__
-  `LTC2497: 16-Bit 8-/16-Channel ΔΣ ADC with Easy Drive Input Current
   Cancellation and I2C
   Interface <git.linux.org>drivers/iio/adc/ltc2497.c>`__
   `LTC2497 <adi>LTC2497>`__
-  `LTC2499: 24-Bit 8-/16-Channel ΔΣ ADC with Easy Drive Input Current
   Cancellation and I2C
   Interface <git.linux.org>drivers/iio/adc/ltc2497.c>`__
   `LTC2499 <adi>LTC2499>`__
-  `MAX1027: 10-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal
   Reference <git.linux.org>drivers/iio/adc/max1027.c>`__
   `MAX1027 <maxim>MAX1027>`__
-  `MAX1029: 10-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal
   Reference <git.linux.org>drivers/iio/adc/max1027.c>`__
   `MAX1029 <maxim>MAX1029>`__
-  `MAX1031: 10-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal
   Reference <git.linux.org>drivers/iio/adc/max1027.c>`__
   `MAX1031 <maxim>MAX1031>`__
-  `MAX1036: 2.7V to 5.5V, Low-Power, 4-/12-Channel 2-Wire Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1036 <maxim>MAX1036>`__
-  `MAX1037: 2.7V to 5.5V, Low-Power, 4-/12-Channel 2-Wire Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1037 <maxim>MAX1037>`__
-  `MAX1038: 2.7V to 5.5V, Low-Power, 4-/12-Channel 2-Wire Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1038 <maxim>MAX1038>`__
-  `MAX1039: 2.7V to 5.5V, Low-Power, 4-/12-Channel 2-Wire Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1039 <maxim>MAX1039>`__
-  `MAX11100: 16-Bit, +5V, 200ksps ADC with 10µA
   Shutdown <git.linux.org>drivers/iio/adc/max11100.c>`__
   `MAX11100 <maxim>MAX11100>`__
-  `MAX1117: Single-Supply, Low-Power, 2-Channel, Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1118.c>`__
   `MAX1117 <maxim>MAX1117>`__
-  `MAX1118: Single-Supply, Low-Power, 2-Channel, Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1118.c>`__
   `MAX1118 <maxim>MAX1118>`__
-  `MAX1119: Single-Supply, Low-Power, 2-Channel, Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1118.c>`__
   `MAX1119 <maxim>MAX1119>`__
-  `MAX11205 16-Bit, Single-Channel, Ultra-Low Power, Delta-Sigma ADC
   with 2-Wire Serial
   Interface </resources/tools-software/linux-drivers/iio-adc/max11205>`__
-  `MAX1136: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel,
   2-Wire Serial 10-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1136 <maxim>MAX1136>`__
-  `MAX1137: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel,
   2-Wire Serial 10-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1137 <maxim>MAX1137>`__
-  `MAX1138: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel,
   2-Wire Serial 10-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1138 <maxim>MAX1138>`__
-  `MAX1139: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel,
   2-Wire Serial 10-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1139 <maxim>MAX1139>`__
-  `MAX11600: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power,
   4-/8-/12-Channel, 2-Wire Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11600 <maxim>MAX11600>`__
-  `MAX11601: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power,
   4-/8-/12-Channel, 2-Wire Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11601 <maxim>MAX11601>`__
-  `MAX11602: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power,
   4-/8-/12-Channel, 2-Wire Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11602 <maxim>MAX11602>`__
-  `MAX11603: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power,
   4-/8-/12-Channel, 2-Wire Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11603 <maxim>MAX11603>`__
-  `MAX11604: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power,
   4-/8-/12-Channel, 2-Wire Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11604 <maxim>MAX11604>`__
-  `MAX11605: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power,
   4-/8-/12-Channel, 2-Wire Serial 8-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11605 <maxim>MAX11605>`__
-  `MAX11606: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11606 <maxim>MAX11606>`__
-  `MAX11607: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11607 <maxim>MAX11607>`__
-  `MAX11608: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11608 <maxim>MAX11608>`__
-  `MAX11609: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11609 <maxim>MAX11609>`__
-  `MAX11610: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11610 <maxim>MAX11610>`__
-  `MAX11611: Low-Power, 4-/8-/12-Channel, I2C,10-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11611 <maxim>MAX11611>`__
-  `MAX11612: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11612 <maxim>MAX11612>`__
-  `MAX11613: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11613 <maxim>MAX11613>`__
-  `MAX11614: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11614 <maxim>MAX11614>`__
-  `MAX11615: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11615 <maxim>MAX11615>`__
-  `MAX11616: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11616 <maxim>MAX11616>`__
-  `MAX11617: Low-Power, 4-/8-/12-Channel, I²C, 12-Bit ADCs in
   Ultra-Small Packages <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11617 <maxim>MAX11617>`__
-  `MAX11644: Low-Power, 1-/2-Channel, I²C, 12-Bit ADCs in Ultra-Tiny
   1.9mm x 2.2mm Package <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11644 <maxim>MAX11644>`__
-  `MAX11645: Low-Power, 1-/2-Channel, I²C, 12-Bit ADCs in Ultra-Tiny
   1.9mm x 2.2mm Package <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11645 <maxim>MAX11645>`__
-  `MAX11646: Low-Power, 1-/2-Channel, I²C, 10-Bit ADCs in Ultra-Tiny
   1.9mm x 2.2mm Package <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11646 <maxim>MAX11646>`__
-  `MAX11647: Low-Power, 1-/2-Channel, I²C, 10-Bit ADCs in Ultra-Tiny
   1.9mm x 2.2mm Package <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX11647 <maxim>MAX11647>`__
-  `MAX1227: 12-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal
   Reference <git.linux.org>drivers/iio/adc/max1027.c>`__
   `MAX1227 <maxim>MAX1227>`__
-  `MAX1229: 12-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal
   Reference <git.linux.org>drivers/iio/adc/max1027.c>`__
   `MAX1229 <maxim>MAX1229>`__
-  `MAX1231: 12-Bit 300ksps ADCs with FIFO, Temp Sensor, Internal
   Reference <git.linux.org>drivers/iio/adc/max1027.c>`__
   `MAX1231 <maxim>MAX1231>`__
-  `MAX1236: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel,
   2-Wire Serial, 12-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1236 <maxim>MAX1236>`__
-  `MAX1237: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel,
   2-Wire Serial, 12-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1237 <maxim>MAX1237>`__
-  `MAX1238: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel,
   2-Wire Serial, 12-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1238 <maxim>MAX1238>`__
-  `MAX1239: 2.7V to 3.6V and 4.5V to 5.5V, Low-Power, 4-/12-Channel,
   2-Wire Serial, 12-Bit
   ADCs <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1239 <maxim>MAX1239>`__
-  `MAX1240: +2.7V, Low-Power, 12-Bit Serial ADCs in 8-Pin
   SO <git.linux.org>drivers/iio/adc/max1241.c>`__
   `MAX1240 <maxim>MAX1240>`__
-  `MAX1241: +2.7V, Low-Power, 12-Bit Serial ADCs in 8-Pin
   SO <git.linux.org>drivers/iio/adc/max1241.c>`__
   `MAX1241 <maxim>MAX1241>`__
-  `MAX1361: 250ksps, +3V, 8-/4-Channel, 12-Bit ADCs with +2.5V
   Reference and Parallel
   Interface <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1361 <maxim>MAX1361>`__
-  `MAX1362: 400ksps, +5V, 8-/4-Channel, 12-Bit ADCs with +2.5V
   Reference and Parallel
   Interface <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1362 <maxim>MAX1362>`__
-  `MAX1363: 250ksps, +3V, 8-/4-Channel, 12-Bit ADCs with +2.5V
   Reference and Parallel
   Interface <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1363 <maxim>MAX1363>`__
-  `MAX1364: 400ksps, +5V, 8-/4-Channel, 12-Bit ADCs with +2.5V
   Reference and Parallel
   Interface <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1364 <maxim>MAX1364>`__
-  `MAX1368: Microcontroller-Interface, 4.5-/3.5-Digit Panel Meters with
   4-20mA Output <git.linux.org>drivers/iio/adc/max1363.c>`__
   `MAX1368 <maxim>MAX1368>`__
-  `MAX9611: High-Side, Inverting Current-Sense Amplifiers with12-Bit
   ADC and Op
   Amp/Comparator <git.linux.org>drivers/iio/adc/max9611.c>`__
   `MAX9611 <maxim>MAX9611>`__
-  `MAX9612: High-Side, Noninverting Current-Sense Amplifiers with12-Bit
   ADC and Op
   Amp/Comparator <git.linux.org>drivers/iio/adc/max9611.c>`__
   `MAX9612 <maxim>MAX9612>`__

IIO - Beamformers
~~~~~~~~~~~~~~~~~

-  `ADAR1000: 8 GHz to 16 GHz, 4-Channel, X Band and Ku Band
   Beamformer </linux-drivers/iio-transceiver/adar1000>`__

IIO - Capacitance to Digital Converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `AD7152: 2-Channel, 12-Bit Capacitance to Digital
   Converter <linux-drivers/iio-cdc/ad7152>`__
-  `AD7153: 1-Channel, 12-Bit Capacitance to Digital
   Converter <linux-drivers/iio-cdc/ad7152>`__
-  `AD7150: Ultra-Low Power, 2-Channel, Capacitance Converter for
   Proximity Sensing <linux-drivers/iio-cdc/ad7150>`__
-  `AD7151: Ultra-Low Power, 1-Channel, Capacitance Converter for
   Proximity Sensing <linux-drivers/iio-cdc/ad7150>`__
-  `AD7156: Ultra-Low Power, 1.8 V, 3 mm × 3 mm, 2-Channel, Capacitance
   Converter <linux-drivers/iio-cdc/ad7150>`__
-  `AD7745: 24-bit, 1 Channel Capacitance to Digital
   Converter <linux-drivers/iio-cdc/ad7745>`__
-  `AD7746: 24-bit, 2 Channel Capacitance to Digital
   Converter <linux-drivers/iio-cdc/ad7745>`__
-  `AD7747: 24-Bit Capacitance-to-Digital Converter with Temperature
   Sensor <linux-drivers/iio-cdc/ad7745>`__

IIO - Combined Analog to Digital and Digital to Analog converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `AD74412R: Quad-Channel, Software Configurable Input and
   Output <linux-drivers/iio-addac/ad74413r>`__
   `AD74412R <adi>AD74412R>`__
-  `AD74413R: Quad-Channel, Software Configurable Input and
   Output <linux-drivers/iio-addac/ad74413r>`__
   `AD74413R <adi>AD74413R>`__
-  `AD74115H: Single-Channel, Software Configurable Input and Output
   with HART Modem <git.linux.org>drivers/iio/addac/ad74115.c>`__
   `AD74115H <adi>AD74115H>`__

IIO - Digital to Analog Converters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `AD3552R: Dual Channel, 16-Bit, 33 MUPS, Multispan, Multi-IO SPI
   DAC <linux-drivers/iio-dac/axi-ad3552r>`__
-  `AD5024: Fully Accurate 12-Bit VOUT nanoDAC® Quad, SPI Interface, 4.5
   V to 5.5 V in TSSOP <linux-drivers/iio-dac/ad5064>`__
-  `AD5025: Fully Accurate 12-Bit VOUT nanoDAC® SPI Interface 2.7 V TO
   5.5 V IN A TSSOP <linux-drivers/iio-dac/ad5064>`__
-  `AD5044: Fully Accurate 14-Bit VOUT nanoDAC® Quad, SPI Interface, 4.5
   V to 5.5 V in TSSOP <linux-drivers/iio-dac/ad5064>`__
-  `AD5045: Fully Accurate 14-Bit VOUT nanoDAC® SPI Interface 2.7 V TO
   5.5 V IN A TSSOP <linux-drivers/iio-dac/ad5064>`__
-  `AD5064-1: Fully Accurate 16-Bit VOUT nanoDAC® Quad, SPI Interface,
   4.5 V to 5.5 V in TSSOP <linux-drivers/iio-dac/ad5064>`__
-  `AD5064: Fully Accurate 16-Bit VOUT nanoDAC® Quad, SPI Interface, 4.5
   V to 5.5 V in TSSOP <linux-drivers/iio-dac/ad5064>`__
-  `AD5065: Fully Accurate 16-Bit VOUT nanoDAC® SPI Interface 2.7 V TO
   5.5 V IN A TSSOP <linux-drivers/iio-dac/ad5064>`__
-  `AD5300: 2.7V to 5.5V, 140 ΜA, Rail-to-Rail Voltage-Output 8-Bit DAC
   in SOT-23 AND MICROSOIC Packages <linux-drivers/iio-dac/ad5446>`__
-  `AD5301: 2.5V to 5.5V, 120 ΜA, 2-Wire Interface, Voltage-Output 8-Bit
   DAC <linux-drivers/iio-dac/ad5446>`__
-  `AD5310: 2.7V to 5.5V, 140 ΜA, Rail-to-Rail Voltage-Output 10-Bit DAC
   in SOT-23 AND MICROSOIC Packages <linux-drivers/iio-dac/ad5446>`__
-  `AD5310R: Single, 10-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5311: 2.5V to 5.5V, 120 ΜA, 2-Wire Interface, Voltage-Output
   10-Bit DAC <linux-drivers/iio-dac/ad5446>`__
-  `AD5311R: Single, 10-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5320: 2.7V to 5.5V, 140 ΜA, Rail-to-Rail Voltage-Output 12-Bit DAC
   in SOT-23 AND MICROSOIC Packages <linux-drivers/iio-dac/ad5446>`__
-  `AD5321: 2.5V to 5.5V, 120 ΜA, 2-Wire Interface, Voltage-Output
   12-Bit DAC <linux-drivers/iio-dac/ad5446>`__
-  `AD5338: 2.5 V to 5.5 V, 250 µA, 2-Wire Interface, Dual Voltage
   Output, 10-Bit DACs <linux-drivers/iio-dac/ad5676>`__
-  `AD5338R: Dual 10-Bit nanoDAC® with 2 ppm/°C Reference, I2C
   Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5360: 16-Channel, 16-Bit, Serial Input, Voltage-Output
   DAC <linux-drivers/iio-dac/ad5360>`__
-  `AD5361: 16-Channel, 14-Bit, Serial Input, Voltage-Output
   DAC <linux-drivers/iio-dac/ad5360>`__
-  `AD5362: 8-Channel, 16-Bit, Serial Input, Voltage-Output
   DAC <linux-drivers/iio-dac/ad5360>`__
-  `AD5363: 8-Channel, 14-Bit, Serial Input, Voltage-Output
   DAC <linux-drivers/iio-dac/ad5360>`__
-  `AD5370: 40-Channel, 16-Bit, Serial Input, Voltage-Output
   DACs <linux-drivers/iio-dac/ad5360>`__
-  `AD5371: 40-Channel, 14-Bit, Serial Input, Voltage-Output
   DACs <linux-drivers/iio-dac/ad5360>`__
-  `AD5372: 32-Channel, 16-Bit, Serial Input, Voltage-Output
   DAC <linux-drivers/iio-dac/ad5360>`__
-  `AD5373: 40-Channel, 14-Bit, Serial Input, Voltage-Output
   DAC <linux-drivers/iio-dac/ad5360>`__
-  `AD5380: 40-Channel 14-Bit 3 V/5 V Single-Supply Voltage-Output
   DAC <linux-drivers/iio-dac/ad5380>`__
-  `AD5381: 40-Channel 12-Bit 3 V/5 V Single-Supply Voltage-Output
   DAC <linux-drivers/iio-dac/ad5380>`__
-  `AD5382: 32-Channel 14-Bit 3 V/5 V Single-Supply Voltage-Output
   DAC <linux-drivers/iio-dac/ad5380>`__
-  `AD5383: 32-Channel 12-Bit 3 V/5 V Single-Supply Voltage-Output
   DAC <linux-drivers/iio-dac/ad5380>`__
-  `AD5384: 40-Channel, 3 V/5 V Single Supply,14-Bit, Serial
   Voltage-Output DAC <linux-drivers/iio-dac/ad5380>`__
-  `AD5390: 16-Channel 14-Bit 3 V/5 V Single-Supply Voltage-Output
   DAC <linux-drivers/iio-dac/ad5380>`__
-  `AD5391: 16-Channel 12-Bit 3 V/5 V Single-Supply Voltage-Output
   DAC <linux-drivers/iio-dac/ad5380>`__
-  `AD5392: 8-Channel 14-Bit 3 V/5 V Single-Supply Voltage-Output
   DAC <linux-drivers/iio-dac/ad5380>`__
-  `AD5415: Dual 12-Bit, High Bandwidth, Multiplying DAC with 4-Quadrant
   Resistors and Serial Interface <linux-drivers/iio-dac/ad5449>`__
-  `AD5421: 16-Bit, Serial Input, Loop-Powered, 4mA to 20mA
   DA <linux-drivers/iio-dac/ad5421>`__
-  `AD5426: 8-Bit, High Bandwidth, Multiplying DACs with Serial
   Interface <linux-drivers/iio-dac/ad5449>`__
-  `AD5429: Dual 8-Bit, High Bandwidth, Multiplying DACs with Serial
   Interface <linux-drivers/iio-dac/ad5449>`__
-  `AD5432: 10-Bit, High Bandwidth, Multiplying DACs with Serial
   Interface <linux-drivers/iio-dac/ad5449>`__
-  `AD5439: Dual 10-Bit, High Bandwidth, Multiplying DACs with Serial
   Interface <linux-drivers/iio-dac/ad5449>`__
-  `AD5443: 12-Bit, High Bandwidth, Multiplying DACs with Serial
   Interface <linux-drivers/iio-dac/ad5449>`__
-  `AD5444: 12-Bit High Bandwidth Multiplying DAC with Serial
   Interface <linux-drivers/iio-dac/ad5446>`__
-  `AD5446: 14-Bit High Bandwidth Multiplying DAC with Serial
   Interface <linux-drivers/iio-dac/ad5446>`__
-  `AD5449: Dual 12-Bit, High Bandwidth, Multiplying DACs with Serial
   Interface <linux-drivers/iio-dac/ad5449>`__
-  `AD5450: 8-BIT High Bandwidth Multiplying DAC with Serial
   Interface <linux-drivers/iio-dac/ad5446>`__
-  `AD5451: 10-BIT High Bandwidth Multiplying DAC with Serial
   Interface <linux-drivers/iio-dac/ad5446>`__
-  `AD5452: 12-BIT High Bandwidth Multiplying DAC with Serial
   Interface <linux-drivers/iio-dac/ad5446>`__
-  `AD5453: 14-BIT High Bandwidth Multiplying DAC with Serial
   Interface <linux-drivers/iio-dac/ad5446>`__
-  `AD5501: High Voltage, 12-Bit Voltage Output
   DAC <linux-drivers/iio-dac/ad5504>`__ `Obsolete <adi>ad5501>`__
-  `AD5504: High Voltage, Quad Channel 12-Bit Voltage Output
   DAC <linux-drivers/iio-dac/ad5504>`__
-  `AD5512A: 2.7 V to 5.5 V, Serial-Input, Voltage-Output, 16-/12-Bit
   nanoDAC® in 16-lead 3 mm × 3 mm
   LFCSP <linux-drivers/iio-dac/ad5446>`__
-  `AD5541A: 2.7 V to 5.5 V, Serial-Input, Voltage-Output, 16-/12-Bit
   nanoDAC® in 8-lead 3 mm × 3 mm
   LFCSP <linux-drivers/iio-dac/ad5446>`__
-  `AD5542A: 2.7 V to 5.5 V, Serial-Input, Voltage-Output, 16-/12-Bit
   nanoDAC® in 16-lead 3 mm × 3 mm LFCSP & 16-lead
   TSSOP <linux-drivers/iio-dac/ad5446>`__
-  `AD5542: 2.7 V to 5.5 V, Serial-Input, Voltage-Output, 16-Bit
   DAC <linux-drivers/iio-dac/ad5446>`__
-  `AD5543: 16-Bit DAC in µSOIC-8
   Package <linux-drivers/iio-dac/ad5446>`__
-  `AD5553: 14-Bit DAC in µSOIC-8
   Package <linux-drivers/iio-dac/ad5446>`__
-  `AD5592R: 8 Channel, 12-Bit, Configurable ADC/DAC with on-chip
   Reference, SPI interface <linux-drivers/iio-dac/ad5592r>`__
-  `AD5593R: 8 Channel, 12-Bit, Configurable ADC/DAC with on-chip
   Reference, I2C interface <linux-drivers/iio-dac/ad5593r>`__
-  `AD5600: High Temperature, 16-Bit, Unbuffered Voltage Output DAC, SPI
   Interface <linux-drivers/iio-dac/ad5446>`__
-  `AD5601: 2.7V to 5.5V, <100 uA, 8-Bit nanoDAC®, SPI Interface in SC70
   Package <linux-drivers/iio-dac/ad5446>`__
-  `AD5602: 2.7V to 5.5V, <100 ΜA, 8-Bit nanoDAC® with I2C compatible
   Interface, tiny SC70 Package <linux-drivers/iio-dac/ad5446>`__
-  `AD5611: 2.7V to 5.5V, <100 uA, 10-Bit nanoDAC®, SPI Interface in
   SC70 Package <linux-drivers/iio-dac/ad5446>`__
-  `AD5612: 2.7V to 5.5V, <100 ΜA, 10-Bit nanoDAC® with I2C compatible
   Interface, tiny SC70 Package <linux-drivers/iio-dac/ad5446>`__
-  `AD5620-1: Single, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference in
   SOT-23 <linux-drivers/iio-dac/ad5446>`__
-  `AD5620-2: Single, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference in
   SOT-23 <linux-drivers/iio-dac/ad5446>`__
-  `AD5620-3: Single, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference in
   SOT-23 <linux-drivers/iio-dac/ad5446>`__
-  `AD5620: Single, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference in
   SOT-23 <linux-drivers/iio-dac/ad5446>`__
-  `AD5621: 2.7V to 5.5V, <100 uA, 12-Bit nanoDAC®, SPI Interface in
   SC70 Package <linux-drivers/iio-dac/ad5446>`__
-  `AD5622: 2.7V to 5.5V, <100 ΜA, 12-Bit nanoDAC® with I2C compatible
   Interface, tiny SC70 Package <linux-drivers/iio-dac/ad5446>`__
-  `AD5624: 2.7 V to 5.5 V, 450 µA, Rail-to-Rail Output, Quad, 12-Bit
   nano DAC® <linux-drivers/iio-dac/ad5624r>`__
-  `AD5624R: Quad, 12-Bit nanoDAC® with 5ppm/°C On-Chip
   Reference <linux-drivers/iio-dac/ad5624r>`__
-  `AD5625: Quad, 12-Bit nanoDAC®, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5625R: Quad, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5626R: Dual, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5626R: Quad, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5627: Dual, 12-Bit nanoDAC®, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5627R: Dual, 12-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5628-1: Octal, 12-Bit, SPI Voltage-Output denseDAC with 1.25 V 5
   ppm/°C reference, <linux-drivers/iio-dac/ad5064>`__
-  `AD5628-2: Octal, 12-Bit, SPI Voltage-Output denseDAC with 2.5 V 5
   ppm/°C reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5628: Octal, 12-Bit, SPI Voltage-Output denseDAC with 5 ppm/°C
   On-Chip Reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5629R: OCTAL, 12-BIT, I2C Voltage Output denseDAC with 5 ppm/°C
   On-Chip Reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5640-1: Single, 14-Bit nanoDAC® Converter with 5 ppm/°C On-Chip
   Reference in S0T-23 <linux-drivers/iio-dac/ad5446>`__
-  `AD5640-2: Single, 14-Bit nanoDAC® Converter with 5 ppm/°C On-Chip
   Reference in S0T-23 <linux-drivers/iio-dac/ad5446>`__
-  `AD5640-3: Single, 14-Bit nanoDAC® Converter with 5 ppm/°C On-Chip
   Reference in S0T-23 <linux-drivers/iio-dac/ad5446>`__
-  `AD5640: Single, 14-Bit nanoDAC® Converter with 5 ppm/°C On-Chip
   Reference in S0T-23 <linux-drivers/iio-dac/ad5446>`__
-  `AD5641: 2.7V to 5.5V, <100 mA, 14-Bit nanoDAC®, SPI interface in
   LFCSP and SC70 <linux-drivers/iio-dac/ad5446>`__
-  `AD5644R: Quad, 14-Bit nanoDAC® with 5ppm/°C On-Chip
   Reference <linux-drivers/iio-dac/ad5624r>`__
-  `AD5645R: Quad, 14-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5647R: Dual, 14-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5648: Octal, 14-Bit, SPI Voltage-Output denseDAC with 5 ppm/°C
   On-Chip Reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5648-1: Octal, 14-Bit, SPI Voltage-Output denseDAC with a 1.25 V 5
   ppm/°C reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5648-2: Octal, 14-Bit, SPI Voltage-Output denseDAC with 2.5 V 5
   ppm/°C reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5048-1: Octal, 14-Bit, SPI Voltage-Output denseDAC with 1.25 V 5
   ppm/°C reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5048-2: Octal, 14-Bit, SPI Voltage-Output denseDAC with 2.5 V 5
   ppm/°C reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5660-1: Single, 16-Bit nanoDAC® with 5 ppm/°C On-Chip
   Reference <linux-drivers/iio-dac/ad5446>`__
-  `AD5660-2: Single, 16-Bit nanoDAC® with 5 ppm/°C On-Chip
   Reference <linux-drivers/iio-dac/ad5446>`__
-  `AD5660-3: Single, 16-Bit nanoDAC® with 5 ppm/°C On-Chip
   Reference <linux-drivers/iio-dac/ad5446>`__
-  `AD5660: Single, 16-Bit nanoDAC® with 5 ppm/°C On-Chip
   Reference <linux-drivers/iio-dac/ad5446>`__
-  `AD5662: 2.7-5.5V, 16-Bit nanoDAC® Converter in a
   Sot-23 <linux-drivers/iio-dac/ad5446>`__
-  `AD5664R: Quad, 16-Bit nanoDAC® with 5ppm/°C On-Chip
   Reference <linux-drivers/iio-dac/ad5624r>`__
-  `AD5665: Quad, 16-Bit nanoDAC®, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5665R: Quad, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5666: Quad, 16-Bit D/A Converter with 10ppm/°C max On-Chip
   Reference in 14-lead TSSOP <linux-drivers/iio-dac/ad5064>`__
-  `AD5667: Dual, 16-Bit nanoDAC®, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5667R: Dual, 16-Bit nanoDAC® with 5 ppm/°C On-Chip Reference, I2C®
   Interface <linux-drivers/iio-dac/ad5064>`__
-  `AD5668: Octal, 16-Bit, SPI Voltage-Output denseDAC with 5 ppm/°C
   On-Chip Reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5668-1: Octal, 16-Bit, SPI Voltage-Output denseDAC with 5 ppm/°C
   On-Chip Reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5668-2: Octal, 16-Bit, SPI Voltage-Output denseDAC with 2.5 ppm/°C
   On-Chip Reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5668-3: Octal, 16-Bit, SPI Voltage-Output denseDAC with 5 ppm/°C
   On-Chip Reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5669R: OCTAL, 16-BIT, I2C Voltage-Output denseDAC with 5 ppm/°C
   On-Chip Reference <linux-drivers/iio-dac/ad5064>`__
-  `AD5671R: Octal, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5672R: Octal, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5673R: 16-Channel, 12-/16-Bit nanoDAC+ with 2 ppm/°C Voltage
   Reference TC, I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5674R: 16-Channel, 12-/16-Bit nanoDAC+ with 2 ppm/°C Voltage
   Reference Temperature Coefficient, SPI
   Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5675R: Octal, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5676: Octal, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5676R: Octal, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5677R: 16-Channel, 12-/16-Bit nanoDAC+ with 2 ppm/°C Voltage
   Reference, I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5679: 16-Channel, 12-/16-Bit nanoDAC+ with 2 ppm/°C Voltage
   Reference Temperature Coefficient, SPI
   Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5679R: 16-Channel, 12-/16-Bit nanoDAC+ with 2 ppm/°C Voltage
   Reference Temperature Coefficient, SPI
   Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5681R: Single, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5682R: Single, 14-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5683R: Single, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5683: Single, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5684: Quad, 12-Bit nanoDAC+ with SPI
   Interface <linux-drivers/iio-dac/ad5686>`__
-  `AD5684R: Quad, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5686>`__
-  `AD5685R: Quad, 14-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5686>`__
-  `AD5686R: Quad, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   SPI Interface <linux-drivers/iio-dac/ad5686>`__
-  `AD5691R: Single, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5692R: Single, 14-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5693R: Single, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5693: Single, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5694: Quad, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5694R: Quad, 12-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5695R: Quad, 14-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5696: Quad, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5696R: Quad, 16-Bit nanoDAC+ with 2 ppm/°C On-Chip Reference and
   I2C Interface <linux-drivers/iio-dac/ad5676>`__
-  `AD5721: Multiple Range, 12-Bit, Unipolar, Voltage Output
   DACs <https://github.com/torvalds/linux/blob/master/drivers/iio/dac/ad5761.c>`__
   `AD5721 <adi>AD5721>`__
-  `AD5721R: Multiple Range, 12-Bit, Unipolar Voltage Output DACs with 2
   PPM/⁰C
   Reference <https://github.com/torvalds/linux/blob/master/drivers/iio/dac/ad5761.c>`__
   `AD5721R <adi>AD5721R>`__
-  `AD5735: Quad Channel, 12-Bit, Serial Input, 4-20 mA & Voltage Output
   DAC with Dynamic Power Control <linux-drivers/iio-dac/ad5755>`__
-  `AD5737: Quad Channel, 12-Bit, Serial Input, 4-20 mA Output DAC with
   Dynamic Power Control and HART
   Connectivity <linux-drivers/iio-dac/ad5755>`__
-  `AD5744: Complete Quad, 14-Bit, High Accuracy, Serial Input, Bipolar
   Voltage Output DAC <linux-drivers/iio-dac/ad5764>`__
   `Obsolete <adi>ad5744>`__
-  `AD5744R: Complete Quad, 14-Bit, High Accuracy, Serial Input, Bipolar
   Voltage Output DAC <linux-drivers/iio-dac/ad5764>`__
-  `AD5755-1: Quad Channel, 16-Bit, Serial Input, 4-20 mA & Voltage
   Output DAC, Dynamic Power Control, HART
   Connectivity <linux-drivers/iio-dac/ad5755>`__
-  `AD5755: Quad Channel, 16-Bit, Serial Input, 4 mA to 20 mA and
   Voltage Output DAC, Dynamic Power
   Control <linux-drivers/iio-dac/ad5755>`__
-  `AD5757: Quad Channel, 16-Bit, Serial Input, 4-20 mA Output DAC,
   Dynamic Power Control, HART
   Connectivity <linux-drivers/iio-dac/ad5755>`__
-  `AD5758: Single Channel, 16-Bit, Current/Voltage Output DAC, Dynamic
   Power Control, HART Connectivity <linux-drivers/iio-dac/ad5758>`__
-  `AD5760: ULTRA STABLE 16-BIT ±0.5 LSB INL, Voltage Output
   DAC <linux-drivers/iio-dac/ad5791>`__
-  `AD5761: Multiple Range, 16-Bit, Bipolar, Voltage Output
   DACs <https://github.com/torvalds/linux/blob/master/drivers/iio/dac/ad5761.c>`__
   `AD5761 <adi>AD5761>`__
-  `AD5761R: Multiple Range, 16-Bit, Bipolar Voltage Output DACs with 2
   PPM/⁰C
   Reference <https://github.com/torvalds/linux/blob/master/drivers/iio/dac/ad5761.c>`__
   `AD5761R <adi>AD5761R>`__
-  `AD5764: Complete Quad, 16-Bit, High Accuracy, Serial Input, Bipolar
   Voltage Output DAC <linux-drivers/iio-dac/ad5764>`__
-  `AD5764R: Complete Quad, 16-Bit, High Accuracy, Serial Input, Bipolar
   Voltage Output DAC <linux-drivers/iio-dac/ad5764>`__
-  `AD5766: 16-Channel, 16-Bit Voltage Output
   denseDAC <git.linux.org>drivers/iio/dac/ad5766.c>`__
   `AD5766 <adi>AD5766>`__
-  `AD5767: 16-Channel, 12-Bit Voltage Output
   denseDAC <git.linux.org>drivers/iio/dac/ad5766.c>`__
   `AD5767 <adi>AD5767>`__
-  `AD5770R: 6-Channel, 14-Bit, Current Output DAC with On-Chip
   Reference, SPI Interface </linux-drivers/iio-dac/ad5770r>`__
-  `AD5780: SYSTEM READY, 18-BIT ±1 LSB INL, Voltage Output
   DAC <linux-drivers/iio-dac/ad5764>`__
-  `AD5781: True 18-Bit, Voltage Output DAC ±0.5 LSB INL, ±0.5 LSB
   DNL <linux-drivers/iio-dac/ad5791>`__
-  `AD5790: System Ready 20-Bit, +-/ 2 LSB INL, Voltage Output
   DAC <linux-drivers/iio-dac/ad5791>`__
-  `AD5791: 1 ppm 20-Bit, ±1 LSB INL, Voltage Output
   DAC <linux-drivers/iio-dac/ad5791>`__
-  `AD7303: +2.7 V TO +5.5 V, Serial Input, Dual Voltage Output 8-Bit
   DAC </resources/tools-software/linux-drivers/iio-dac/ad7303>`__
-  `AD7293: 12-Bit Power Amplifier Current Controller with ADC, DACs,
   Temperature and Current
   Sensors </resources/tools-software/linux-drivers/iio-dac/ad7293>`__
-  `AD8801: Octal 8-Bit TrimDAC with Power Shutdown & Mid-Scale
   Preset <git.linux.org>drivers/iio/dac/ad8801.c>`__
   `AD8801 <adi>AD8801>`__
-  `AD8803: Octal 8-Bit TrimDAC with Power Shutdown & Mid-Scale
   Preset <git.linux.org>drivers/iio/dac/ad8801.c>`__
   `AD8803 <adi>AD8803>`__
-  `AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog
   Converter <linux-drivers/iio-dds/axi-dac-dds-hdl>`__
-  `AD9136: Dual, 16-Bit, 2.8 GSPS, TxDAC+® Digital-to-Analog
   Converter <linux-drivers/iio-dds/axi-dac-dds-hdl>`__
-  `AD9144: Quad, 16-Bit, 2.8 GSPS, TxDAC+® Digital-to-Analog
   Converter <linux-drivers/iio-dds/axi-dac-dds-hdl>`__
-  `AD9152: Dual, 16-Bit, 2.25 GSPS, TxDAC+ Digital-to-Analog
   Converter <linux-drivers/iio-dds/axi-dac-dds-hdl>`__
-  `AD9154: Quad, 16-Bit, 2.4 GSPS, TxDAC+® Digital-to-Analog
   Converter <linux-drivers/iio-dds/axi-dac-dds-hdl>`__
-  `AD9162: 16-Bit, 12 GSPS, RF Digital-to-Analog
   Converters <linux-drivers/iio-dds/axi-dac-dds-hdl>`__
-  `AD9171: Dual, 16-Bit, 6.2 GSPS RF DAC with Single
   Channelizer </resources/tools-software/linux-drivers/iio-dds/ad9172>`__
-  `AD9172: Dual, 16-Bit, 12.6 GSPS RF DAC with
   Channelizers </resources/tools-software/linux-drivers/iio-dds/ad9172>`__
-  `AD9173: Dual, 16-Bit, 12.6 GSPS RF DAC with
   Channelizers </resources/tools-software/linux-drivers/iio-dds/ad9172>`__
-  `AD9174: Dual, 16-Bit, 12.6 GSPS RF DAC and Direct Digital
   Synthesizer </resources/tools-software/linux-drivers/iio-dds/ad9172>`__
-  `AD9175: Dual, 11-Bit/16-Bit, 12.6 GSPS RF DAC with Wideband
   Channelizers </resources/tools-software/linux-drivers/iio-dds/ad9172>`__
-  `AD9176: Dual, 16-Bit, 12.6 GSPS RF DAC with Wideband
   Channelizers </resources/tools-software/linux-drivers/iio-dds/ad9172>`__
-  `AD9177 Quad, 16-Bit, 12 GSPS RF DAC with Wideband
   Channelizers <linux-drivers/iio-mxfe/ad9081>`__
-  `AD9739A: 14-Bit, 2.5 GSPS, RF D/A
   Converter <linux-drivers/iio-dds/axi-dac-dds-hdl>`__
-  `ADT7316 ±0.5°C Accurate Digital Temperature Sensor and Quad Voltage
   Output 12-Bit
   DAC <git.linux.org>drivers/staging/iio/addac/adt7316.c>`__
   `ADT7316 <adi>ADT7316>`__
-  `ADT7317 ±0.5°C Accurate Digital Temperature Sensor and Quad Voltage
   Output 10-Bit
   DAC <git.linux.org>drivers/staging/iio/addac/adt7316.c>`__
   `ADT7317 <adi>ADT7317>`__
-  `ADT7318 ±0.5°C Accurate Digital Temperature Sensor and Quad Voltage
   Output 8-Bit
   DACs <git.linux.org>drivers/staging/iio/addac/adt7316.c>`__
   `ADT7318 <adi>ADT7318>`__
-  `LTC1660: Micropower Octal 10-Bit
   DACs <git.linux.org>drivers/iio/dac/ltc1660.c>`__
   `LTC1660 <adi>LTC1660>`__
-  `LTC1660: Micropower Octal 8-Bit
   DACs <git.linux.org>drivers/iio/dac/ltc1660.c>`__
   `LTC1660 <adi>LTC1660>`__
-  `LTC1665: Micropower Octal 8-Bit
   DACs <git.linux.org>drivers/iio/dac/ltc1660.c>`__
   `LTC1665 <adi>LTC1665>`__
-  `LTC2606: 16-Bit Rail-to-Rail DACs with I2C
   Interface <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2606 <adi>LTC2606>`__
-  `LTC2607: 16-Bit Dual Rail-to-Rail DACs with I²C
   Interface <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2607 <adi>LTC2607>`__
-  `LTC2609: Quad 16-/14-/12-Bit Rail-to-Rail DACs with I2C
   Interface <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2609 <adi>LTC2609>`__
-  `LTC2616: 14-Bit Rail-to-Rail DACs with I2C
   Interface <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2616 <adi>LTC2616>`__
-  `LTC2617: 14-Bit Dual Rail-to-Rail DAC with I2C
   Interface <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2617 <adi>LTC2617>`__
-  `LTC2619: Quad 16-/14-/12-Bit Rail-to-Rail DACs with I2C
   Interface <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2619 <adi>LTC2619>`__
-  `LTC2626: 12-Bit Rail-to-Rail DACs with I2C
   Interface <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2626 <adi>LTC2626>`__
-  `LTC2627: 12-Bit Dual Rail-to-Rail with I²C
   Interface <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2627 <adi>LTC2627>`__
-  `LTC2629: Quad 16-/14-/12-Bit Rail-to-Rail DACs with I²C
   Interface <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2629 <adi>LTC2629>`__
-  `LTC2631: Single 12-/10-/8-Bit I2C VOUT DACs with 10ppm/°C
   Reference <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2631 <adi>LTC2631>`__
-  `LTC2632: Dual 12-/10-/8-Bit SPI VOUT DACs with 10ppm/°C
   Reference <git.linux.org>drivers/iio/dac/ltc2632.c>`__
   `LTC2632 <adi>LTC2632>`__
-  `LTC2634: Quad 12-/10-/8-Bit Rail-to-Rail DACs with 10ppm/°C
   Reference <git.linux.org>drivers/iio/dac/ltc2632.c>`__
   `LTC2634 <adi>LTC2634>`__
-  `LTC2636: Octal 12-/10-/8-Bit SPI VOUT DACs with 10ppm/°C
   Reference <git.linux.org>drivers/iio/dac/ltc2632.c>`__
   `LTC2636 <adi>LTC2636>`__
-  `LTC2633: Dual 12-/10-/8-Bit I2C VOUT DACs with 10ppm/°C
   Reference <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2633 <adi>LTC2633>`__
-  `LTC2635: Quad 12-/10-/8-Bit I2C VOUT DACs with 10ppm/°C
   Reference <git.linux.org>drivers/iio/dac/ad5064.c>`__
   `LTC2635 <adi>LTC2635>`__
-  `LTC2664: Quad 16-Bit/12-Bit ±10V VOUT SoftSpan DACs with 10ppm/°C
   Max Reference <linux-drivers/iio-dac/ltc2664>`__
-  `LTC2688: 16-Channel, 12-/16-Bit Voltage Output SoftSpan
   DAC <git.linux.org>drivers/iio/dac/ltc2688.c>`__
   `LTC2688 <adi>LTC2688>`__
-  `MAX5821: Dual, 10-Bit, Low-Power, 2-Wire, Serial Voltage-Output
   DAC <git.linux.org>drivers/iio/dac/max5821.c>`__
   `MAX5821 <maxim>MAX5821>`__
-  `MAX517: 2-Wire Serial 8-Bit DACs withRail-to-Rail
   Outputs <git.linux.org>drivers/iio/dac/max517.c>`__
   `MAX517 <maxim>MAX517>`__
-  `MAX518: 2-Wire Serial 8-Bit DACs withRail-to-Rail
   Outputs <git.linux.org>drivers/iio/dac/max517.c>`__
   `MAX518 <maxim>MAX518>`__
-  `MAX519: 2-Wire Serial 8-Bit DACs withRail-to-Rail
   Outputs <git.linux.org>drivers/iio/dac/max517.c>`__
   `MAX519 <maxim>MAX519>`__
-  `MAX520: Quad/Octal, 2-Wire Serial 8-Bit DACs with Rail-to-Rail
   Outputs <git.linux.org>drivers/iio/dac/max517.c>`__
   `MAX520 <maxim>MAX520>`__
-  `MAX521: Quad/Octal, 2-Wire Serial 8-Bit DACs with Rail-to-Rail
   Outputs <git.linux.org>drivers/iio/dac/max517.c>`__
   `MAX521 <maxim>MAX521>`__
-  `DS4422: Two-/Four-Channel, I²C, 7-Bit Sink/Source Current
   DAC <git.linux.org>drivers/iio/dac/DS4424.c>`__
   `DS4422 <maxim>DS4422>`__
-  `DS4424: Two-/Four-Channel, I²C, 7-Bit Sink/Source Current
   DAC <git.linux.org>drivers/iio/dac/DS4424.c>`__
   `DS4424 <maxim>DS4424>`__

IIO - Direct Digital Synthesis
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `AD9832: 25 MHz Serial Interface DDS With On-Chip 10-Bit
   DAC <linux-drivers/iio-dds/ad9832>`__
-  `AD9833: Low Power, 12.65 mW, 2.3 V to +5.5 V, Programmable Waveform
   Generator <linux-drivers/iio-dds/ad9834>`__
-  `AD9834: 20 mW Power, 2.3 V to 5.5 V, 75 MHz Complete
   DDS <linux-drivers/iio-dds/ad9834>`__
-  `AD9835: Complete DDS With 10-Bit On-Chip
   DAC <linux-drivers/iio-dds/ad9832>`__
-  `AD9837: Low Power, 8.5 mW, 2.3 V to 5.5 V, Programmable Waveform
   Generator <linux-drivers/iio-dds/ad9834>`__
-  `AD9838: 11 mW Power, 2.3 V to 5.5 V, Complete
   DDS <linux-drivers/iio-dds/ad9834>`__
-  `AD9122: Dual, 16-Bit, 1200 MSPS, TxDAC+® Digital-to-Analog
   Converter <linux-drivers/iio-dds/axi-dac-dds-hdl>`__
-  `AD9144: Quad, 16-Bit, 2.8 GSPS, TxDAC+® Digital-to-Analog
   Converter <linux-drivers/iio-dds/axi-dac-dds-hdl>`__
-  `AD9739A: 14-Bit, 2.5 GSPS, RF D/A
   Converter <linux-drivers/iio-dds/axi-dac-dds-hdl>`__

IIO - Filters
~~~~~~~~~~~~~

-  `ADMV8818: 2 GHz to 18 GHz, Digitally Tunable, High-Pass and Low-Pass
   Filter <linux-drivers/iio-filter/admv8818>`__

IIO - Frequency Synthesizers / Phase-Locked Loop
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `AD9161: 11-Bit/16-Bit, 12 GSPS, RF Digital-to-Analog
   Converters <linux-drivers/iio-pll/ad9162>`__
-  `AD9162: 11-Bit/16-Bit, 12 GSPS, RF Digital-to-Analog
   Converters <linux-drivers/iio-pll/ad9162>`__
-  `AD9163: 16-Bit, 12 GSPS, RF DAC and Digital
   Upconverter <linux-drivers/iio-pll/ad9162>`__
-  `AD9164: 16-Bit, 12 GSPS, RF DAC and Direct Digital
   Synthesizer <linux-drivers/iio-pll/ad9162>`__
-  `AD9166: DC to 9 GHz Vector Signal
   Generator <linux-drivers/iio-pll/ad9162>`__
-  `AD9508: 1.65 GHz Clock Fanout Buffer with Output Dividers and Delay
   Adjust <linux-drivers/iio-pll/ad9508>`__
-  `AD9516-0: 14-Output Clock Generator with Integrated 2.8 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9516-1: 14-Output Clock Generator with Integrated 2.5 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9516-2: 14-Output Clock Generator with Integrated 2.2 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9516-3: 14-Output Clock Generator with Integrated 2.0 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9516-4: 14-Output Clock Generator with Integrated 1.6 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9516-5: 14-Output Clock
   Generator <linux-drivers/iio-pll/ad9517>`__
-  `AD9517-0: 12-Output Clock Generator with Integrated 2.8 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9517-1: 12-Output Clock Generator with Integrated 2.5 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9517-2: 12-Output Clock Generator with Integrated 2.2 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9517-3: 12-Output Clock Generator with Integrated 2.0 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9517-4: 12-Output Clock Generator with Integrated 1.6 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9518-0: 6-Output Clock Generator with Integrated 2.8 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9518-1: 6-Output Clock Generator with Integrated 2.5 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9518-2: 6-Output Clock Generator with Integrated 2.2 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9518-3: 6-Output Clock Generator with Integrated 2.0 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9518-4: 6-Output Clock Generator with Integrated 1.6 GHz
   VCO <linux-drivers/iio-pll/ad9517>`__
-  `AD9523-1: Low Jitter Clock Generator with 14 LVPECL/LVDS/HSTL/29
   LVCMOS Outputs <linux-drivers/iio-pll/ad9523>`__
-  `AD9528: JESD204B Clock Generator with 14 LVDS/HSTL
   Outputs <linux-drivers/iio-pll/ad9528>`__
-  `ADF4159: Direct Modulation/Fast Waveform Generating, 13 GHz,
   Fractional-N Frequency Synthesizer <linux-drivers/iio-pll/adf4159>`__
-  `ADF4169: Direct Modulation/Fast Waveform Generating, 13.5 GHz,
   Fractional-N Frequency Synthesizer <linux-drivers/iio-pll/adf4159>`__
-  `ADF4350: Wideband Synthesizer with Integrated
   VCO <linux-drivers/iio-pll/adf4350>`__
-  `ADF4351: Wideband Synthesizer with Integrated
   VCO <linux-drivers/iio-pll/adf4350>`__
-  `ADF4360-0: Clock Generator PLL with Integrated
   VCO <linux-drivers/iio-pll/adf4360>`__
-  `ADF4360-1: Clock Generator PLL with Integrated
   VCO <linux-drivers/iio-pll/adf4360>`__
-  `ADF4360-2: Clock Generator PLL with Integrated
   VCO <linux-drivers/iio-pll/adf4360>`__
-  `ADF4360-3: Clock Generator PLL with Integrated
   VCO <linux-drivers/iio-pll/adf4360>`__
-  `ADF4360-4: Clock Generator PLL with Integrated
   VCO <linux-drivers/iio-pll/adf4360>`__
-  `ADF4360-5: Clock Generator PLL with Integrated
   VCO <linux-drivers/iio-pll/adf4360>`__
-  `ADF4360-6: Clock Generator PLL with Integrated
   VCO <linux-drivers/iio-pll/adf4360>`__
-  `ADF4360-7: Clock Generator PLL with Integrated
   VCO <linux-drivers/iio-pll/adf4360>`__
-  `ADF4360-8: Clock Generator PLL with Integrated
   VCO <linux-drivers/iio-pll/adf4360>`__
-  `ADF4360-9: Clock Generator PLL with Integrated
   VCO <linux-drivers/iio-pll/adf4360>`__
-  `ADF4371: Wideband Synthesizer with Integrated
   VCO <linux-drivers/iio-pll/adf4371>`__
-  `ADF4372: Wideband Synthesizer with Integrated
   VCO <linux-drivers/iio-pll/adf4371>`__
-  `ADF4377: Wideband Synthesizer with Integrated
   VCO <linux-drivers/iio-pll/adf4377>`__
-  `ADF4355: Microwave Wideband Synthesizer with Integrated
   VCO <linux-drivers/iio-pll/adf5355>`__
-  `ADF4355-2: Microwave Wideband Synthesizer with Integrated
   VCO <linux-drivers/iio-pll/adf5355>`__
-  `ADF4355-3: Microwave Wideband Synthesizer with Integrated
   VCO <linux-drivers/iio-pll/adf5355>`__
-  `ADF5355: Microwave Wideband Synthesizer with Integrated
   VCO <linux-drivers/iio-pll/adf5355>`__
-  `ADF5356: Microwave Wideband Synthesizer with Integrated
   VCO <linux-drivers/iio-pll/adf5355>`__
-  `ADMV1013: 24 GHz to 44 GHz, Wideband, Microwave
   Upconverter <linux-drivers/iio-pll/admv1013>`__
-  `ADMV1014: 24 GHz to 44 GHz, Wideband, Microwave
   Downconverter <linux-drivers/iio-pll/admv1014>`__
-  `ADRF6780: 5.9 GHz to 23.6 GHz, Wideband, Microwave
   Upconverter <linux-drivers/iio-pll/adrf6780>`__
-  `HMC7044: Clock Jitter Attenuator with
   JESD204B <linux-drivers/iio-pll/hmc7044>`__
-  `HMC7043: High Performance, 3.2 GHz, 14-Output Fanout
   Buffer <linux-drivers/iio-pll/hmc7044>`__
-  `LTC6952: Ultralow Jitter, 4.5GHz PLL,
   JESD204B/JESD204C <linux-drivers/iio-pll/ltc6952>`__
-  `LTC6953: Ultralow Jitter, 4.5GHz Clock Distributor with 11 Outputs,
   JESD204B/JESD204C <linux-drivers/iio-pll/ltc6952>`__

IIO - Gyroscopes
~~~~~~~~~~~~~~~~

-  `ADIS16060: Wide Bandwidth Yaw Rate Gyroscope with
   SPI <linux-drivers/iio-gyroscope/adis16060>`__
-  `ADIS16080: ±80°/sec Yaw Rate Gyro with SPI
   Interface <linux-drivers/iio-gyroscope/adis16080>`__
   `Obsolete <adi>ADIS16080>`__
-  `ADIS16100: ±300°/sec Yaw Rate Gyro with SPI
   Interface <linux-drivers/iio-gyroscope/adis16080>`__
   `Obsolete <adi>adis16100>`__
-  `ADIS16130: Digital Output, High-Precision Angular Rate
   Sensor <linux-drivers/iio-gyroscope/adis16130>`__
   `Obsolete <adi>adis16130>`__
-  `ADIS16133: ±1200°/sec Precision Angular Rate
   Sensor <linux-drivers/iio-gyroscope/adis16136>`__
   `Obsolete <adi>adis16133>`__
-  `ADIS16135: ±300°/sec Precision Angular Rate
   Sensor <linux-drivers/iio-gyroscope/adis16136>`__
-  `ADIS16136: ±450°/sec Precision Angular Rate
   Sensor <linux-drivers/iio-gyroscope/adis16136>`__
-  `ADIS16137: ±1000°/Sec Precision Angular Rate
   Sensor <linux-drivers/iio-gyroscope/adis16136>`__
-  `ADIS16251: Programmable Low Power
   Gyroscope <linux-drivers/iio-gyroscope/adis16260>`__
   `Obsolete <adi>adis16251>`__
-  `ADIS16250: Programmable Low Power
   Gyroscope <linux-drivers/iio-gyroscope/adis16260>`__
   `Obsolete <adi>adis16250>`__
-  `ADIS16255: Programmable Low Power
   Gyroscope <linux-drivers/iio-gyroscope/adis16260>`__
   `Obsolete <adi>adis16255>`__
-  `ADIS16260: Programmable Low Power
   Gyroscope <linux-drivers/iio-gyroscope/adis16260>`__
-  `ADIS16265: Programmable Digital Gyroscope
   Sensor <linux-drivers/iio-gyroscope/adis16260>`__
-  `ADIS16266: ±14,000°/sec Digital Gyroscope
   Sensor <linux-drivers/iio-gyroscope/adis16260>`__\ `Obsolete <adi>adis16266>`__
-  `ADXRS290: Ultralow noise, dual-axis MEMS Gyroscope for Stabilization
   Applications <git.linux.org>drivers/iio/gyro/adxrs290.c>`__
   `ADXRS290 <adi>ADXRS290>`__
-  `ADXRS450: ±300°/sec High Vibration Immunity Digital
   Gyro <linux-drivers/iio-gyroscope/adxrs450>`__
-  `ADXRS453: High Performance, Digital Output
   Gyroscope <linux-drivers/iio-gyroscope/adxrs450>`__

IIO - Heart-Rate
~~~~~~~~~~~~~~~~

-  `MAX30100: Pulse Oximeter and Heart-Rate Sensor IC for Wearable
   Health <git.linux.org>drivers/iio/health/max30100.c>`__
   `MAX30100 <maxim>MAX30100>`__
-  `MAX30102: High-Sensitivity Pulse Oximeter and Heart-Rate Sensor for
   Wearable Health <git.linux.org>drivers/iio/health/max30102.c>`__
   `MAX30102 <maxim>MAX30102>`__

IIO - Impedance Converters and Network Analyzers
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `AD5933: 1 MSPS, 12 Bit Impedance Converter Network
   Analyzer <linux-drivers/iio-impedance-analyzer/ad5933>`__
-  `AD5934: 250 kSPS 12-Bit Impedance Converter Network
   Analyzer <linux-drivers/iio-impedance-analyzer/ad5933>`__

IIO - Inertial Measurement Units
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `ADIS16300: Four Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
   `Obsolete <adi>adis16300>`__
-  `ADIS16305: Precision Four Degrees of Freedom
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
   `Obsolete <adi>adis16305>`__
-  `ADIS16334: Low-Profile Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
-  `ADIS16350: High Precision Tri-Axis Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
   `Obsolete <adi>adis16350>`__
-  `ADIS16354: High Precision Tri-Axis Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
   `Obsolete <adi>adis16354>`__
-  `ADIS16355: High-Precision Tri-Axis Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
   `Obsolete <adi>adis16355>`__
-  `ADIS16360: Six Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
   `Obsolete <adi>adis16360>`__
-  `ADIS16362: Six Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
-  `ADIS16364: High Precision Tri-Axis Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
-  `ADIS16365: Six Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
-  `ADIS16367: Six Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
   `Obsolete <adi>adis16367>`__
-  `ADIS16375: Low Profile, Low Noise Six Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16480>`__
-  `ADIS16400: High Precision Tri-Axis Inertial Sensor Gyroscope,
   Magnetometer,
   Accelerometer <linux-drivers/iio-inertial-measurement-units/adis16400>`__
   `Obsolete <adi>adis16400>`__
-  `ADIS16405: High Precision Tri-Axis Gyroscope, Accelerometer,
   Magnetometer <linux-drivers/iio-inertial-measurement-units/adis16400>`__
   `Obsolete <adi>adis16405>`__
-  `ADIS16445: Compact, Precision Six Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
-  `ADIS16448: Low Noise, High Stability Ten Degree of Freedom MEMS
   Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16400>`__
-  `ADIS16460: Compact, Precision, Six Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16475>`__
-  `ADIS16465: Precision MEMS IMU
   Module <linux-drivers/iio-inertial-measurement-units/adis16475>`__
-  `ADIS16467: Precision MEMS IMU
   Module <linux-drivers/iio-inertial-measurement-units/adis16475>`__
-  `ADIS16470: Wide Dynamic Range, Miniature MEMs
   IMU <linux-drivers/iio-inertial-measurement-units/adis16475>`__
-  `ADIS16475: Precision, Miniature MEMs
   IMU <linux-drivers/iio-inertial-measurement-units/adis16475>`__
-  `ADIS16477: Precision, Miniature MEMs
   IMU <linux-drivers/iio-inertial-measurement-units/adis16475>`__
-  `ADIS16480: Ten Degrees of Freedom MEMS Inertial Sensor with Dynamic
   Orientation
   Outputs <linux-drivers/iio-inertial-measurement-units/adis16480>`__
-  `ADIS16485: Tactical Grade Six Degrees of Freedom MEMS Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16480>`__
-  `ADIS16488: Low Profile, Low Noise Ten Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16480>`__
   `Obsolete <adi>adis16488>`__
-  `ADIS16490: Tactical Grade, Six Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16480>`__
-  `ADIS16495: Tactical Grade, Six Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16480>`__
-  `ADIS16497: Tactical Grade, Six Degrees of Freedom Inertial
   Sensor <linux-drivers/iio-inertial-measurement-units/adis16480>`__
-  `ADIS16500: Precision, Miniature MEMs
   IMU <linux-drivers/iio-inertial-measurement-units/adis16475>`__
-  `ADIS16505: Precision, Miniature MEMs
   IMU <linux-drivers/iio-inertial-measurement-units/adis16475>`__
-  `ADIS16507: Precision, Miniature MEMs
   IMU <linux-drivers/iio-inertial-measurement-units/adis16475>`__

IIO - Light
~~~~~~~~~~~

-  `MAX44000: Ambient and Infrared Proximity
   Sensor <git.linux.org>drivers/iio/light/max44000.c>`__
   `MAX44000 <maxim>MAX44000>`__
-  `MAX44009: Industry's Lowest-Power Ambient Light Sensor with
   ADC <git.linux.org>drivers/iio/light/max44009.c>`__
   `MAX44009 <maxim>MAX44009>`__

IIO - Mixed Signal Front Ends (MxFE)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `AD9081 MxFE® Quad, 16-Bit, 12 GSPS RF DAC and Quad, 12-Bit, 4 GSPS
   RF ADC <linux-drivers/iio-mxfe/ad9081>`__
-  `AD9082 MxFE® Quad, 16-Bit, 12 GSPS RF DAC and Dual, 12-Bit, 6 GSPS
   RF ADC <linux-drivers/iio-mxfe/ad9081>`__
-  `AD9088 MxFE® 4T4R Direct RF Transmitter and Observation
   Receiver <linux-drivers/iio-mxfe/ad9081>`__
-  `AD9086 MxFE® 4T2R Direct RF Transmitter and Observation
   Receiver <linux-drivers/iio-mxfe/ad9081>`__

IIO - Potentiometers
~~~~~~~~~~~~~~~~~~~~

-  `MAX5487: Dual, 256-Tap, Nonvolatile, SPI-Interface, Linear-Taper
   Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5487.c>`__
   `MAX5487 <maxim>MAX5487>`__
-  `MAX5488: Dual, 256-Tap, Nonvolatile, SPI-Interface, Linear-Taper
   Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5487.c>`__
   `MAX5488 <maxim>MAX5488>`__
-  `MAX5489: Dual, 256-Tap, Nonvolatile, SPI-Interface, Linear-Taper
   Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5487.c>`__
   `MAX5489 <maxim>MAX5489>`__
-  `MAX5481: 10-Bit, Nonvolatile, Linear-Taper Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5481.c>`__
   `MAX5481 <maxim>MAX5481>`__
-  `MAX5482: 10-Bit, Nonvolatile, Linear-Taper Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5481.c>`__
   `MAX5482 <maxim>MAX5482>`__
-  `MAX5483: 10-Bit, Nonvolatile, Linear-Taper Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5481.c>`__
   `MAX5483 <maxim>MAX5483>`__
-  `MAX5484: 10-Bit, Nonvolatile, Linear-Taper Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5481.c>`__
   `MAX5484 <maxim>MAX5484>`__
-  `MAX5432: 32-Tap, Nonvolatile, I2C, Linear, Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5432.c>`__
   `MAX5432 <maxim>MAX5432>`__
-  `MAX5433: 32-Tap, Nonvolatile, I2C, Linear, Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5433.c>`__
   `MAX5433 <maxim>MAX5433>`__
-  `MAX5434: 32-Tap, Nonvolatile, I2C, Linear, Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5432.c>`__
   `MAX5434 <maxim>MAX5434>`__
-  `MAX5435: 32-Tap, Nonvolatile, I2C, Linear, Digital
   Potentiometers <git.linux.org>drivers/iio/potentiometer/max5432.c>`__
   `MAX5435 <maxim>MAX5435>`__
-  `DS1803: Addressable Dual Digital
   Potentiometer <git.linux.org>drivers/iio/potentiometer/ds1803.c>`__
   `DS1803 <maxim>DS1803>`__
-  `AD5110: Single Channel, 128-Position, I2C, ±8% Resistor Tolerance,
   Nonvolatile Digital
   Potentiometer <git.linux.org>drivers/iio/potentiometer/ad5110.c>`__
   `AD5110 <adi>AD5110>`__
-  `AD5112: Single Channel, 64-Position, I2C, ±8% Resistor Tolerance,
   Nonvolatile Digital
   Potentiometer <git.linux.org>drivers/iio/potentiometer/ad5110.c>`__
   `AD5112 <adi>AD5112>`__
-  `AD5114: Single Channel, 32-Position, I2C, ±8% Resistor Tolerance,
   Nonvolatile Digital
   Potentiometer <git.linux.org>drivers/iio/potentiometer/ad5110.c>`__
   `AD5114 <adi>AD5114>`__

IIO - Resolvers
~~~~~~~~~~~~~~~

-  `AD2S90: Low Cost, Complete 12-Bit Resolver-to-Digital
   Converter <linux-drivers/iio-resolver/ad2s90>`__
-  `AD2S1200: 12-Bit R/D Converter with Reference
   Oscillator <linux-drivers/iio-resolver/ad2s1200>`__
-  `AD2S1205: 12-Bit R/D Converter with Reference
   Oscillator <linux-drivers/iio-resolver/ad2s1200>`__
-  `AD2S1210: Variable Resolution, 10-Bit to 16-Bit R/D Converter with
   Reference Oscillator <linux-drivers/iio-resolver/ad2s1210>`__

IIO - Receivers
~~~~~~~~~~~~~~~

-  `AD6676: Wideband IF Receiver
   Subsystem <linux-drivers/iio-adc/ad6676>`__

IIO - Transceivers
~~~~~~~~~~~~~~~~~~

-  `AD9361: RF Agile
   Transceiver <linux-drivers/iio-transceiver/ad9361>`__
-  `AD9363: RF Agile
   Transceiver <linux-drivers/iio-transceiver/ad9361>`__
-  `AD9364: RF Agile
   Transceiver <linux-drivers/iio-transceiver/ad9361>`__
-  `AD9371: RF Transceiver <linux-drivers/iio-transceiver/ad9371>`__
-  `AD9375: RF Transceiver <linux-drivers/iio-transceiver/ad9371>`__
-  `ADRV9002: RF Transceiver <linux-drivers/iio-transceiver/adrv9002>`__
-  `ADRV9008-1: RF
   Transceiver <linux-drivers/iio-transceiver/adrv9009>`__
-  `ADRV9008-2: RF
   Transceiver <linux-drivers/iio-transceiver/adrv9009>`__
-  `ADRV9009: RF Transceiver <linux-drivers/iio-transceiver/adrv9009>`__
-  `ADRV9009-ZU11EG: RF System on
   Module <linux-drivers/iio-transceiver/adrv9009>`__
-  `ADRV9361-Z7035: RF System on
   Module <linux-drivers/iio-transceiver/ad9361>`__
-  `ADRV9364-Z7020: RF System on
   Module <linux-drivers/iio-transceiver/ad9361>`__

IIO - Temperature
~~~~~~~~~~~~~~~~~

-  `LTC2983: Multi-Sensor Digital Temperature Measurement
   System <linux-drivers/iio-temperature/ltc2983>`__
   `LTC2983 <adi>LTC2983>`__
-  `LTC2984: Multi-Sensor Digital Temperature Measurement
   System <linux-drivers/iio-temperature/ltc2983>`__
   `LTC2984 <adi>LTC2984>`__
-  `LTC2986: Multi-Sensor Digital Temperature Measurement
   System <linux-drivers/iio-temperature/ltc2983>`__
   `LTC2986 <adi>LTC2986>`__
-  `LTM2985: Multi-Sensor Digital Temperature Measurement
   System <linux-drivers/iio-temperature/ltc2983>`__
   `LTM2985 <adi>LTM2985>`__
-  `MAX31856: Precision Thermocouple to Digital Converter with
   Linearization <git.linux.org>drivers/iio/temperature/max31856.c>`__
   `MAX31856 <maxim>MAX31856>`__
-  `MAX31855: Cold-Junction Compensated Thermocouple-to-Digital
   Converter <git.linux.org>drivers/iio/temperature/maxim_thermocouple.c>`__
   `MAX31855 <maxim>MAX31855>`__
-  `MAX6675: Cold-Junction-Compensated K-Thermocouple-to-Digital
   Converter (0°C to
   +1024°C) <git.linux.org>drivers/iio/temperature/maxim_thermocouple.c>`__
   `MAX6675 <maxim>MAX6675>`__

IIO - Vector Power Measurement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  `ADL5960: 10 MHz to 20 GHz, Integrated Vector Network Analyzer
   Front-End <linux-drivers/iio-vector-power/adl5960>`__
   `ADL5960 <adi>ADL5960>`__

Input - Keyboard
~~~~~~~~~~~~~~~~

-  `ADP5520: Backlight Driver with I/O
   Expander <linux-drivers//multifunction-device/adp5520>`__
-  `ADP5585: Keypad Decoder and I/O
   Expansion <linux-drivers/input-keyboard/adp5589>`__
-  `ADP5587: Mobile I/O Expander and QWERTY Keypad
   Controller <linux-drivers/input-keyboard/adp5588>`__
-  `ADP5588: Mobile I/O Expander and QWERTY Keypad
   Controller <linux-drivers/input-keyboard/adp5588>`__
-  `ADP5589: Keypad Decoder and I/O
   Expansion <linux-drivers/input-keyboard/adp5589>`__
-  `MAX7359: 2-Wire Interfaced Low-EMI Key Switch
   Controller/GPO <git.linux.org>drivers/input/keyboard/max7359_keypad.c>`__
   `MAX7359 <maxim>MAX7359>`__

Input - Misc
~~~~~~~~~~~~

-  `AD7142: Programmable Controller for Capacitance Touch
   Sensors <linux-drivers/input-misc/ad714x>`__
-  `AD7143: Programmable Controller for Capacitance Touch
   Sensors <linux-drivers/input-misc/ad714x>`__
-  `AD7147: CapTouch® Programmable Controller for Single-Electrode
   Capacitance Sensors <linux-drivers/input-misc/ad714x>`__
-  `AD7147A: CapTouch® Programmable Controller for Single-Electrode
   Capacitance Sensors <linux-drivers/input-misc/ad714x>`__
-  `AD7148: CapTouch® Programmable Controller for Single-Electrode
   Capacitance Sensors <linux-drivers/input-misc/ad714x>`__
   `Obsolete <adi>ad7148>`__

Input - Touchscreens
~~~~~~~~~~~~~~~~~~~~

-  `AD7873: Touch Screen
   Digitizer <linux-drivers/input-touchscreen/ad7873>`__
-  `AD7843: Touch Screen
   Digitizer <linux-drivers/input-touchscreen/ad7873>`__
-  `AD7877: Touch Screen
   Controller <linux-drivers/input-touchscreen/ad7877>`__
-  `AD7879: Low Voltage Controller for Touch Screens
   (SPI) <linux-drivers/input-touchscreen/ad7879>`__
-  `AD7879-1: Low Voltage Controller for Touch Screens
   (I2C) <linux-drivers/input-touchscreen/ad7879>`__
-  `AD7889: Low Voltage Controller for Touch Screens
   (SPI) <linux-drivers/input-touchscreen/ad7879>`__
-  `AD7889-1: Low Voltage Controller for Touch Screens
   (I2C) <linux-drivers/input-touchscreen/ad7879>`__
-  `MAX11800: Low-Power, Ultra-Small Resistive Touch-Screen Controllers
   with I²C/SPI
   Interface <git.linux.org>drivers/input/touchscreen/max11801_ts.c>`__
   `MAX11800 <maxim>MAX11800>`__
-  `MAX11801: Low-Power, Ultra-Small Resistive Touch-Screen Controllers
   with I²C/SPI
   Interface <git.linux.org>drivers/input/touchscreen/max11801_ts.c>`__
   `MAX11801 <maxim>MAX11801>`__
-  `MAX11802: Low-Power, Ultra-Small Resistive Touch-Screen Controllers
   with I²C/SPI
   Interface <git.linux.org>drivers/input/touchscreen/max11801_ts.c>`__
   `MAX11802 <maxim>MAX11802>`__
-  `MAX11803: Low-Power, Ultra-Small Resistive Touch-Screen Controllers
   with I²C/SPI
   Interface <git.linux.org>drivers/input/touchscreen/max11801_ts.c>`__
   `MAX11803 <maxim>MAX11803>`__

LED
~~~

-  `ADP1650: 1.5 A LED Flash Driver with I2C-Compatible
   Interface </linux-drivers/leds/adp1650>`__
-  `ADP1653: Compact, High Efficiency, High Power, Flash/Torch LED
   Driver with Dual
   Interface <git.linux.org>drivers/media/i2c/adp1653.c>`__
   `ADP1653 <adi>ADP1653>`__
-  `ADP5501: Programmable Current Backlight Driver with Ambient Light
   Sensor Input <linux-drivers//multifunction-device/adp5520>`__
-  `ADP5520: Backlight Driver with I/O
   Expander <linux-drivers//multifunction-device/adp5520>`__
-  `ADP8860: Charge Pump, 7-Channel Smart LED Driver with I2C
   Interface </linux-drivers/backlight/adp8860>`__
-  `ADP8861: Charge Pump, 7-Channel Smart LED Driver with I2C
   Interface </linux-drivers/backlight/adp8860>`__
-  `ADP8863: Charge Pump, 7-Channel Fun Lighting LED
   Driver </linux-drivers/backlight/adp8860>`__
-  `ADP8870: Charge Pump Parallel Backlight Driver with Image Content
   PWM Input </linux-drivers/backlight/adp8870>`__

Miscellaneous
~~~~~~~~~~~~~

-  `AD5160: 256 Position SPI Compatible Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5161: 256 Position SPI/I2C Selectable Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5162: 256-Position Dual Channel SPI Digital
   Potentiometer <linux-drivers/misc/dpot>`__ `AD5162 <adi>AD5162>`__
-  `AD5165: 256-Position, Ultralow Power 1.8 V Logic-Level Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5170: 256-Position, Two-Time Programmable, I2C Compatible Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5171: 64 Position OTP Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5172: 256-Position, One-Time Programmable, Dual Channel, I2C
   Digital Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5173: 256-Position, One-Time Programmable, Dual Channel, I2C
   Digital Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5200: 256-Position Digital
   Potentiometers <linux-drivers/misc/dpot>`__
-  `AD5201: 33-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5203: 4-Channel, 64-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5204: 4-Channel Digital Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5206: 6-Channel, 256-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5207: Dual, 256 Position, Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5231: Nonvolatile Memory, 1024-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5232: Nonvolatile Memory, Dual, 256-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5233: Nonvolatile, Quad, 64-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5235: Nonvolatile Memory, Dual 1024-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5241: I2C® Compatible Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5242: Dual-Channel, I2C® Compatible, 256 Position, Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5243: 256-Position Dual Channel I2C Compatible Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5245: 256 Position I2C Compatible Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5246: 128 Position I2C Compatible Programmable Resistor in SC70
   Package <linux-drivers/misc/dpot>`__
-  `AD5247: 128-Position I2C®-Compatible Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5248: 256-Position Dual Channel I2C Compatible Digital
   Resistor <linux-drivers/misc/dpot>`__
-  `AD5251: I2C, Nonvolatile Memory, Dual 64-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5252: I2C, Nonvolatile Memory, Dual 256-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5253: Quad 64-Position I2C Nonvolatile Memory Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5254: Quad 256-Position I2C Nonvolatile Memory, Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5255: 3-Channel, Dual 512- and Single 128-Position I2C Digital
   Potentiometer <linux-drivers/misc/dpot>`__ `Obsolete <adi>ad5255>`__
-  `AD5258: Nonvolatile, I2C®-Compatible 64-Position, Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5259: Nonvolatile, I2C Compatible 256-Position, Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5260: +15 V or ±5 V, Single-Channel, SPI Compatible, 256 Position
   Digital Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5262: +15 V or ±5 V, Dual-Channel, SPI Compatible, 256 Position
   Digital Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5263: Quad, 15 V, 256-Position Digital Potentiometer with
   Pin-Selectable SPI/I2C <linux-drivers/misc/dpot>`__
-  `AD5270: 1024-Position, 1% Resistor Tolerance Error, SPI Interface
   and 50-TP Memory Digital Rheostat <linux-drivers/misc/dpot>`__
-  `AD5271: 256-Position, 1% Resistor Tolerance Error, SPI Interface and
   50-TP Memory Digital Rheostat <linux-drivers/misc/dpot>`__
-  `AD5272: 1024-Position, 1% Resistor Tolerance Error, Single Channel
   I2C Interface and 50-TP Memory Digital
   Rheostat <linux-drivers/misc/dpot>`__
-  `AD5273: 64-Position, One-Time-Programmable (OTP) Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5274: 256-Position, 1% Resistor Tolerance Error, I2C Interface and
   50-TP Memory Digital Rheostat <linux-drivers/misc/dpot>`__
-  `AD5280: Single/Dual, +15 V/±5 V, 256-Position, I2C-Compatible
   Digital Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5282: Single/Dual, +15 V/±5 V, 256-Position, I2C-Compatible
   Digital Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5290: Compact +30 V / ±15 V 256-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD5291: Single Channel, 256-Position, 1% R-Tol, Digital
   Potentiometer with 20-Times Programmable
   Memory <linux-drivers/misc/dpot>`__
-  `AD5292: Single Channel, 1024-Position, 1% R-Tol, Digital
   Potentiometer with 20-Times Programmable
   Memory <linux-drivers/misc/dpot>`__
-  `AD5293: Single Channel, 1024-Position, 1% R-Tol, Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD7376: +30 V/±15 V Operation 128-Position Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD8400: Single-Channel Digital
   Potentiometer <linux-drivers/misc/dpot>`__
-  `AD8402: 2-Channel Digital Potentiometer <linux-drivers/misc/dpot>`__
-  `AD8403: 4-Channel Digital Potentiometer <linux-drivers/misc/dpot>`__
-  `ADN2850: Nonvolatile Memory, Dual 1024-Position Digital
   Resistor <linux-drivers/misc/dpot>`__
-  `ADN2860: 3-Channel, Dual 512- and Single 128-Position I²C Digital
   Potentiometer <linux-drivers/misc/dpot>`__ `Obsolete <adi>adn2860>`__
-  `DS1620: Digital Thermometer and
   Thermostat <git.linux.org>./drivers/char/ds1620.c>`__
   `DS1620 <maxim>DS1620>`__

Multifunction Device
~~~~~~~~~~~~~~~~~~~~

-  `ADP5520: Backlight Driver with I/O
   Expander <linux-drivers//multifunction-device/adp5520>`__
-  `ADP5501: Programmable Current Backlight Driver with Ambient Light
   Sensor Input <linux-drivers//multifunction-device/adp5520>`__

Multiplexers
~~~~~~~~~~~~

-  `ADGS1408: Multiplexer driver <linux-drivers//mux/adgs1408>`__
-  `ADGS1409: Multiplexer driver <linux-drivers//mux/adgs1408>`__

Networking - MAC802154
~~~~~~~~~~~~~~~~~~~~~~

-  `ADF7241: Low Power IEEE 802.15.4 Zero-IF 2.4 GHz Transceiver
   IC <linux-drivers/networking-mac802154/adf7242>`__
-  `ADF7242: Low Power IEEE 802.15.4/Proprietary GFSK/FSK Zero-IF 2.4
   GHz Transceiver IC <linux-drivers/networking-mac802154/adf7242>`__

Real Time Clocks
~~~~~~~~~~~~~~~~

-  `DS1216B: SmartWatch RAM
   (16K/64K) <git.linux.org>drivers/rtc/rtc-ds1216.c>`__
   `DS1216B <maxim>DS1216>`__
-  `DS1216C: SmartWatch RAM
   (64K/256K) <git.linux.org>drivers/rtc/rtc-ds1216.c>`__
   `DS1216C <maxim>DS1216>`__
-  `DS1216D: SmartWatch RAM
   (256K/1M) <git.linux.org>drivers/rtc/rtc-ds1216.c>`__
   `DS1216D <maxim>DS1216>`__
-  `DS1216E: SmartWatch ROM
   (64K/256K) <git.linux.org>drivers/rtc/rtc-ds1216.c>`__
   `DS1216E <maxim>DS1216>`__
-  `DS1216F: SmartWatch ROM
   (65K/256k/1M) <git.linux.org>drivers/rtc/rtc-ds1216.c>`__
   `DS1216F <maxim>DS1216>`__
-  `DS1216H: SmartWatch RAM
   (1M/4M) <git.linux.org>drivers/rtc/rtc-ds1216.c>`__
   `DS1216H <maxim>DS1216>`__
-  `DS1286: Watchdog
   Timekeepers <git.linux.org>drivers/rtc/rtc-ds1286.c>`__
   `DS1286 <maxim>DS1286>`__
-  `DS12887: PC Real Time
   Clock <git.linux.org>drivers/rtc/rtc-cmos.c>`__
   `DS12887 <maxim>DS12887>`__
-  `DS1302: Trickle-Charge Timekeeping
   Chip <git.linux.org>drivers/rtc/rtc-ds1302.c>`__
   `DS1302 <maxim>DS1302>`__
-  `DS1305: Serial Alarm Real-Time
   Clock <git.linux.org>drivers/rtc/rtc-ds1305.c>`__
   `DS1305 <maxim>DS1305>`__
-  `DS1306: Serial Alarm Real-Time
   Clock <git.linux.org>drivers/rtc/rtc-ds1305.c>`__
   `DS1306 <maxim>DS1306>`__
-  `DS1307: 64 x 8, Serial, I²C Real-Time
   Clock <git.linux.org>drivers/rtc/rtc-ds1307.c>`__
   `DS1307 <maxim>DS1307>`__
-  `DS1308: Low-Current I²C RTC with 56-Byte NV
   RAM <git.linux.org>drivers/rtc/rtc-ds1307.c>`__
   `DS1308 <maxim>DS1308>`__
-  `DS1337: I²C Serial Real-Time
   Clock <git.linux.org>drivers/rtc/rtc-ds1307.c>`__
   `DS1337 <maxim>DS1337>`__
-  `DS1338: I²C RTC with 56-Byte NV
   RAM <git.linux.org>drivers/rtc/rtc-ds1307.c>`__
   `DS1338 <maxim>DS1338>`__
-  `DS1339: I²C Serial Real-Time
   Clock <git.linux.org>drivers/rtc/rtc-ds1307.c>`__
   `DS1339 <maxim>DS1339>`__
-  `DS1340: I²C RTC with Trickle
   Charger <git.linux.org>drivers/rtc/rtc-ds1307.c>`__
   `DS1340 <maxim>DS1340>`__
-  `DS1341: Low-Current I²C RTCs for High-ESR
   Crystals <git.linux.org>drivers/rtc/rtc-ds1307.c>`__
   `DS1341 <maxim>DS1341>`__
-  `DS1343: Low-Current SPI/3-Wire
   RTCs <git.linux.org>drivers/rtc/rtc-ds1343.c>`__
   `DS1343 <maxim>DS1343>`__
-  `DS1344: Low-Current SPI/3-Wire
   RTCs <git.linux.org>drivers/rtc/rtc-ds1343.c>`__
   `DS1344 <maxim>DS1344>`__
-  `DS1347: Low-Current, SPI-Compatible Real-Time
   Clock <git.linux.org>drivers/rtc/rtc-ds1347.c>`__
   `DS1347 <maxim>DS1347>`__
-  `DS1374: I²C, 32-Bit Binary Counter Watchdog RTC with Trickle Charger
   and Reset Input/Output <git.linux.org>drivers/rtc/rtc-ds1374.c>`__
   `DS1374 <maxim>DS1374>`__
-  `DS1388: I²C RTC/Supervisor with Trickle Charger and 512 Bytes
   EEPROM <git.linux.org>drivers/rtc/rtc-ds1307.c>`__
   `DS1388 <maxim>DS1388>`__
-  `DS1390: Low-Voltage SPI/3-Wire RTCs with Trickle
   Charger <git.linux.org>drivers/rtc/rtc-ds1390.c>`__
   `DS1390 <maxim>DS1390>`__
-  `DS1393: Low-Voltage SPI/3-Wire RTCs with Trickle
   Charger <git.linux.org>drivers/rtc/rtc-ds1390.c>`__
   `DS1393 <maxim>DS1393>`__
-  `DS1394: Low-Voltage SPI/3-Wire RTCs with Trickle
   Charger <git.linux.org>drivers/rtc/rtc-ds1390.c>`__
   `DS1394 <maxim>DS1394>`__
-  `DS1511: Y2K-Compliant Watchdog Real-Time
   Clocks <git.linux.org>drivers/rtc/rtc-ds1511.c>`__
   `DS1511 <maxim>DS1511>`__
-  `DS1553: 64kB, Nonvolatile, Year-2000-Compliant Timekeeping
   RAM <git.linux.org>drivers/rtc/rtc-ds1553.c>`__
   `DS1553 <maxim>DS1553>`__
-  `DS1672: I²C 32-Bit Binary Counter
   RTC <git.linux.org>drivers/rtc/rtc-ds1672.c>`__
   `DS1672 <maxim>DS1672>`__
-  `DS1682: Total-Elapsed-Time Recorder with
   Alarm <git.linux.org>drivers/misc/ds1682>`__
   `DS1682 <maxim>DS1682>`__
-  `DS1685: 3V/5V Real-Time
   Clock <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS1685 <maxim>DS1685>`__
-  `DS1687: 3V/5V Real-Time
   Clock <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS1687 <maxim>DS1687>`__
-  `DS1688: 3 Volt/5 Volt Serialized Real-Time Clock with NV RAM
   Control <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS1688 <maxim>DS1688>`__
-  `DS1689: 3 Volt/5 Volt Serialized Real Time Clock with NV RAM
   Control <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS1689 <maxim>DS1689>`__
-  `DS1691: 3 Volt/5 Volt Serialized Real-Time Clock with NV RAM
   Control <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS1691 <maxim>DS1691>`__
-  `DS1693: 3 Volt/5 Volt Serialized Real Time Clock with NV RAM
   Control <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS1693 <maxim>DS1693>`__
-  `DS17285: 3V/5V Real-Time
   Clocks <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS17285 <maxim>DS17285>`__
-  `DS17287: 3V/5V Real-Time
   Clocks <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS17287 <maxim>DS17287>`__
-  `DS1742: Y2KC Nonvolatile Timekeeping
   RAM <git.linux.org>drivers/rtc/rtc-ds1742.c>`__
   `DS1742 <maxim>DS1742>`__
-  `DS1743: Y2KC Nonvolatile Timekeeping
   RAMs <git.linux.org>drivers/rtc/rtc-ds1742.c>`__
   `DS1743 <maxim>DS1743>`__
-  `DS17485: 3V/5V Real-Time
   Clocks <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS17485 <maxim>DS17485>`__
-  `DS17487: 3V/5V Real-Time
   Clocks <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS17487 <maxim>DS17487>`__
-  `DS17885: 3V/5V Real-Time
   Clocks <git.linux.org>drivers/rtc/rtc-ds1685.c>`__
   `DS17885 <maxim>DS17885>`__
-  `DS17887: 3V/5V Real-Time
   Clocks <git.linux.org>drivers/rtc/rtc-ds1685.c/>`__
   `DS17887 <maxim>DS17887>`__
-  `DS2404: EconoRAM Time
   Chip <git.linux.org>drivers/rtc/rtc-ds2404.c>`__
   `DS2404 <maxim>DS2404>`__
-  `DS3231: Extremely Accurate I²C-Integrated
   RTC/TCXO/Crystal <git.linux.org>drivers/rtc/rtc-ds1307.c>`__
   `DS3231 <maxim>DS3231>`__
-  `DS3232: Extremely Accurate I²C RTC with Integrated Crystal and
   SRAM <git.linux.org>drivers/rtc/rtc-ds3232.c>`__
   `DS3232 <maxim>DS3232>`__
-  `DS3234: Extremely Accurate SPI Bus RTC with Integrated Crystal and
   SRAM <git.linux.org>drivers/rtc/rtc-ds3232.c>`__
   `DS3234 <maxim>DS3234>`__
-  `MAX6900: I²C-Compatible RTC in a
   TDFN <git.linux.org>drivers/rtc/rtc-max6900.c>`__
   `MAX6900 <maxim>MAX6900>`__
-  `MAX6902: SPI-Compatible RTC in a
   TDFN <git.linux.org>drivers/rtc/rtc-max6902.c>`__
   `MAX6902 <maxim>MAX6902>`__
-  `MAX6916: SPI-Compatible RTC with Microprocessor Supervisor, Alarm,
   and NV RAM Controller <git.linux.org>drivers/rtc/rtc-max6916.c>`__
   `MAX6916 <maxim>MAX6916>`__
-  `MAX6369: Pin-Selectable Watchdog
   Timers <git.linux.org>drivers/watchdog/max63xx_wdt.c>`__
   `MAX6369 <maxim>MAX6369>`__
-  `MAX6370: Pin-Selectable Watchdog
   Timers <git.linux.org>drivers/watchdog/max63xx_wdt.c>`__
   `MAX6370 <maxim>MAX6370>`__
-  `MAX6371: Pin-Selectable Watchdog
   Timers <git.linux.org>drivers/watchdog/max63xx_wdt.c>`__
   `MAX6371 <maxim>MAX6371>`__
-  `MAX6372: Pin-Selectable Watchdog
   Timers <git.linux.org>drivers/watchdog/max63xx_wdt.c>`__
   `MAX6372 <maxim>MAX6372>`__
-  `MAX6373: Pin-Selectable Watchdog
   Timers <git.linux.org>drivers/watchdog/max63xx_wdt.c>`__
   `MAX6373 <maxim>MAX6373>`__
-  `MAX6374: Pin-Selectable Watchdog
   Timers <git.linux.org>drivers/watchdog/max63xx_wdt.c>`__
   `MAX6374 <maxim>MAX6374>`__

Regulators
~~~~~~~~~~

-  `ADP122: 5.5 V Input, 300 mA, Low Quiescent Current, CMOS Linear
   Regulator, Fixed Output Voltage <linux-drivers/regulator/adp150>`__
-  `ADP123: 5.5 V Input, 300 mA, Low Quiescent Current, CMOS Linear
   Regulator, Adjustable Output
   Voltage <linux-drivers/regulator/adp150>`__
-  `ADP124: 5.5V Input, 500 mA, Low Quiescent Current, CMOS Linear
   Regulator w/31 Fixed-output
   Voltages <linux-drivers/regulator/adp150>`__
-  `ADP125: 5.5V Input, 500 mA, Low Quiescent Current, CMOS Linear
   Regulator w/External Voltage
   Divider <linux-drivers/regulator/adp150>`__
-  `ADP150: Ultralow Noise, 150 mA CMOS Linear
   Regulator <linux-drivers/regulator/adp150>`__
-  `ADP5022: Dual 3 MHz, 600 mA Buck Regulator with 150 mA
   LDO <linux-drivers/regulator/adp150>`__
-  `AD5398: 120 mA, Current Sinking, 10-Bit, I2C D/A
   Converter <linux-drivers/regulator/ad5398>`__
-  `AD5821: 120 mA, Current Sinking, 10-Bit, I2C®
   DAC <linux-drivers/regulator/ad5398>`__
-  `LTC3589: 8-Output Regulator with Sequencing and
   I2C <git.linux.org>drivers/regulator/ltc3589.c>`__
   `LTC3589 <adi>LTC3589>`__
-  `LTC3676: Power Management Solution for Application
   Processors <git.linux.org>drivers/regulator/ltc3676.c>`__
   `LTC3676 <adi>LTC3676>`__
-  `MAX8952: 2.5A Step-Down Regulator with Remote Sense in 2mm x 2mm
   WLP <git.linux.org>drivers/regulator/max8952.c>`__
   `MAX8952 <maxim>MAX8952>`__
-  `MAX8660: High-Efficiency, Low-IQ, PMICs with Dynamic Voltage
   Management for Mobile
   Applications <git.linux.org>drivers/regulator/max8660.c>`__
   `MAX8660 <maxim>MAX8660>`__
-  `MAX8649: 1.8A Step-Down Regulator with Remote Sense in 2mm x 2mm
   WLP <git.linux.org>drivers/regulator/max8649.c>`__
   `MAX8649 <maxim>MAX8649>`__
-  `MAX77826: Highly Integrated PMIC for Camera and Peripherals in 3mm x
   3mm WLP <git.linux.org>drivers/regulator/max77826-regulator.c>`__
   `MAX77826 <maxim>MAX77826>`__
-  `MAX1586: High-Efficiency, Low-IQ PMICs with Dynamic Core for PDAs
   and Smart Phones <git.linux.org>drivers/regulator/max1586.c>`__
   `MAX1586 <maxim>MAX1586>`__
-  `MAX1587A : High-Efficiency, Low-IQ PMICs with Dynamic Core for PDAs
   and Smartphones <git.linux.org>arch/arm/mach-pxa/hx4700.c>`__
   `MAX1587A <maxim>MAX1587A>`__
-  `MAX8893A: µPMICs for Multimedia Application Processors in a 3.0mm x
   2.5mm WLP <git.linux.org>drivers/regulator/max8893.c>`__
   `MAX8893A <maxim>MAX8893A>`__
-  `MAX8893B: µPMICs for Multimedia Application Processors in a 3.0mm x
   2.5mm WLP <git.linux.org>drivers/regulator/max8893.c>`__
   `MAX8893B <maxim>MAX8893B>`__
-  `MAX8893C: µPMICs for Multimedia Application Processors in a 3.0mm x
   2.5mm WLP <git.linux.org>drivers/regulator/max8893.c>`__
   `MAX8893C <maxim>MAX8893C>`__
-  `MAX8973A: 9A, Three-Phase Step-Down Switching
   Regulator <git.linux.org>drivers/regulator/max8973-regulator.c>`__
   `MAX8973A <maxim>MAX8973A>`__

Power-Off
^^^^^^^^^

-  `LTC2952: Pushbutton PowerPath Controller with
   Supervisor <git.linux.org>drivers/power/reset/ltc2952-poweroff.c>`__
   `LTC2952 <adi>LTC2952>`__

Serial
~~~~~~

-  `MAX3100: SPI/MICROWIRE-Compatible UART in
   QSOP-16 <git.linux.org>drivers/tty/serial/max3100.c>`__
   `MAX3100 <maxim>MAX3100>`__
-  `MAX3107: SPI/I²C UART with 128-Word
   FIFOs <linux-drivers/serial/max310x>`__
-  `MAX3108: SPI/I²C UART with 128-Word FIFOs in
   WLP <linux-drivers/serial/max310x>`__
-  `MAX3109: Dual Serial UART with 128-Word
   FIFOs <linux-drivers/serial/max310x>`__
-  `MAX14830: Quad Serial UART with 128-Word
   FIFOs <linux-drivers/serial/max310x>`__

Sound
~~~~~

-  `AD1815: SoundPort®
   Controller <git.linux.org>sound/isa/ad1816a/ad1816a.c>`__
   `Obsolete <adi>ad1815>`__
-  `AD1816: SoundPort®
   Controller <git.linux.org>sound/isa/ad1816a/ad1816a.c>`__
   `Obsolete <adi>ad1816>`__
-  `AD1819: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1819>`__
-  `AD1835: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta
   Codec <git.linux.org>sound/soc/codecs/ad1836.c>`__
   `Obsolete <adi>ad1835>`__
-  `AD1835A: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta
   Codec <linux-drivers/sound/ad1835a>`__
-  `AD1836: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta
   Codec <git.linux.org>sound/soc/codecs/ad1836.c>`__
   `Obsolete <adi>ad1836>`__
-  `AD1836A: Multichannel 96 kHz Codec <linux-drivers/sound/ad1835a>`__
-  `AD1837: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta
   Codec <git.linux.org>sound/soc/codecs/ad1836.c>`__
   `Obsolete <adi>ad1837>`__
-  `AD1837A: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta
   CODEC <linux-drivers/sound/ad1835a>`__ `Obsolete <adi>AD1837A>`__
-  `AD1838: 2 ADC, 6 DAC 96 kHz, 24-Bit Sigma Delta
   Codec <linux-drivers/sound/ad1835a>`__ `Obsolete <adi>AD1838>`__
-  `AD1838A: 2 ADC, 6 DAC 96 kHz, 24-Bit Sigma Delta
   Codec <linux-drivers/sound/ad1835a>`__ `Obsolete <adi>AD1838A>`__
-  `AD1839: 2 ADC, 8 DAC, 96 kHz, 24-Bit Sigma Delta
   Codec <git.linux.org>sound/soc/codecs/ad1836.c>`__
   `Obsolete <adi>ad1839>`__
-  `AD1839A: 2 ADC, 6 DAC 96 kHz, 24-Bit Sigma Delta
   Codec <linux-drivers/sound/ad1835a>`__ `Obsolete <adi>ad1839a>`__
-  `AD1843: Serial-Port 16-Bit SoundComm
   Codec <git.linux.org>sound/mips/ad1843.c>`__
   `Obsolete <adi>ad1843>`__
-  `AD1845: Parallel-Port 16-Bit SoundPort® Stereo
   Codec <git.linux.org>sound/isa/sscape.c>`__ `Obsolete <adi>ad1845>`__
-  `AD1847: Serial-Port 16-Bit SoundPort Stereo
   Codec <git.linux.org>sound/isa/wss/wss_lib.c>`__
   `Obsolete <adi>ad1847>`__
-  `AD1848: Parallel-Port 16-Bit SoundPort Stereo
   Codec <git.linux.org>sound/isa/ad1848/ad1848.c>`__
   `Obsolete <adi>ad1848>`__
-  `AD1852: Stereo, 24-Bit, 192 kHz, Multibit Sigma Delta
   DAC <git.linux.org>sound/pci/rme96.c>`__ `ad1852 <adi>ad1852>`__
-  `AD1855: Stereo, 96 kHz, Multibit Sigma
   Delta <git.linux.org>sound/pci/rme96.c>`__ `Obsolete <adi>ad1855>`__
-  `AD1881A: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1881a>`__
-  `AD1881: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1881>`__
-  `AD1884: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1884>`__
-  `AD1885: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1885>`__
-  `AD1886A: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1886a>`__
-  `AD1887: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1887>`__
-  `AD1888: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1888>`__
-  `AD1933: 8 DAC with PLL, 192 kHz, 24-Bit
   Codec <linux-drivers/sound/ad1936>`__
-  `AD1934: 8 DAC with PLL, 192 kHz, 24-Bit
   Codec <linux-drivers/sound/ad1936>`__
-  `AD1936: 4 ADC/8 DAC, 192 kHz, 24-Bit CODEC with PLL, Single-Ended
   Output, I2C Control <linux-drivers/sound/ad1936>`__
   `Obsolete <adi>ad1936>`__
-  `AD1937: Four ADCs/Eight DACs with PLL, 192 kHz, 24-Bit
   Codec <linux-drivers/sound/ad1936>`__
-  `AD1938: 4 ADC/8 DAC with PLL, 192 kHz, 24-Bit
   CODEC <linux-drivers/sound/ad1936>`__
-  `AD1939: 4 ADC/8 DAC with PLL, 192 kHz, 24-Bit
   Codec <linux-drivers/sound/ad1936>`__
-  `AD1980: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1980>`__
-  `AD1981A: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1981a>`__
-  `AD1981B: AC’97 SoundMAX®
   Codec <git.linux.org>sound/pci/ac97/ac97_codec.c>`__
   `Obsolete <adi>ad1981B>`__
-  `AD1983: HD Audio SoundMAX®
   Codec <git.linux.org>sound/pci/hda/patch_analog.c>`__
   `Obsolete <adi>ad1983>`__
-  `AD1984B: HD Audio SoundMAX®
   Codec <git.linux.org>sound/pci/hda/patch_analog.c>`__
   `Obsolete <adi>ad1984b>`__
-  `AD1984: HD Audio SoundMAX®
   Codec <git.linux.org>sound/pci/hda/patch_analog.c>`__
   `Obsolete <adi>ad1984>`__
-  `AD1985: HD Audio SoundMAX®
   Codec <git.linux.org>sound/pci/hda/patch_analog.c>`__
   `Obsolete <adi>ad1985>`__
-  `AD1986A: HD Audio SoundMAX®
   Codec <git.linux.org>sound/pci/hda/patch_analog.c>`__
   `Obsolete <adi>ad1986a>`__
-  `AD1986: HD Audio SoundMAX®
   Codec <git.linux.org>sound/pci/hda/patch_analog.c>`__
   `Obsolete <adi>ad1986>`__
-  `AD1988A: HD Audio SoundMAX®
   Codec <git.linux.org>sound/pci/hda/patch_analog.c>`__
   `Obsolete <adi>ad1988A>`__
-  `AD1988B: HD Audio SoundMAX®
   Codec <git.linux.org>sound/pci/hda/patch_analog.c>`__
   `Obsolete <adi>ad1988B>`__
-  `AD73311: Single Voiceband Codec <linux-drivers/sound/ad73322>`__
-  `AD73322: Dual Voiceband Codec <linux-drivers/sound/ad73322>`__
-  `AD73322L: Dual-Channel, 3 V Front-End Processor for General Purpose
   Applications Including Speech and
   Telephony <linux-drivers/sound/ad73322>`__
-  `ADAU1328: 2 ADC/8 DAC with PLL, 192 kHz, 24-Bit
   Codec <linux-drivers/sound/ad1936>`__
-  `ADAU1361: Stereo, Low Power, 96 kHz, 24-Bit Audio Codec with
   Integrated PLL <linux-drivers/sound/adau1361>`__
-  `ADAU1372: Quad ADC, Dual DAC, Low Latency, Low Power
   Codec <linux-drivers/sound/adau1372>`__
-  `ADAU1373: Low Power Codec with Speaker and Headphone
   Amplifier <linux-drivers/sound/adau1373>`__
   `Obsolete <adi>adau1373>`__
-  `ADAU1381: Low-noise Stereo Codec with Enhanced Recording and
   Playback Processing <linux-drivers/sound/adau1381>`__
   `Obsolete <adi>adau1381>`__
-  `ADAU1401A: SigmaDSP® 28/56-Bit Audio Processor with Two ADCs and
   Four DACs <linux-drivers/sound/adau1701>`__
-  `ADAU1401: SigmaDSP® 28/56-Bit Audio Processor with Two ADCs and Four
   DACs <linux-drivers/sound/adau1701>`__
-  `ADAU1461: SigmaDSP Stereo, Automotive Low Power, 96 kHz, 24-Bit
   Audio Codec with Integrated PLL <linux-drivers/sound/adau1361>`__
   `Obsolete <adi>adau1461>`__
-  `ADAU1701: SigmaDSP® 28/56-Bit Audio Processor with Two ADCs and Four
   DACs <linux-drivers/sound/adau1701>`__
-  `ADAU1702: SigmaDSP® 28/56-Bit Audio Processor with Two ADCs and Four
   DACs <linux-drivers/sound/adau1701>`__
-  `ADAU1761: SigmaDSP® Stereo, Low Power, 96 kHz, 24-Bit Audio Codec
   with Integrated PLL <linux-drivers/sound/adau1361>`__
-  `ADAU1781: SigmaDSP Low-noise Stereo Audio Codec for Portable
   Applications <linux-drivers/sound/adau1381>`__
   `Obsolete <adi>adau1781>`__
-  `ADAU1961: Automotive Stereo, Low Power, 96 kHz, 24-Bit Audio Codec
   with Integrated PLL <linux-drivers/sound/adau1361>`__
-  `ADAU1977: Quad ADC with Diagnostics (10V
   Input) <linux-drivers/sound/adau1977>`__
-  `ADAU1978: Quad ADC (2V Input) <linux-drivers/sound/adau1977>`__
-  `ADAU1979: Quad ADC (4.5V Input) <linux-drivers/sound/adau1977>`__
-  `ADAU7002: Stereo PDM to I2S or TDM Conversion
   IC <linux-drivers/sound/adau7002>`__
-  `ADAU7118: 8 Channel, PDM to I2S or TDM Conversion
   IC <linux-drivers/sound/adau7118>`__
-  `ADAV801: Audio Codec for Recordable
   DVD <linux-drivers/sound/adav801>`__
-  `ADAV803: Audio Codec for Recordable
   DVD <linux-drivers/sound/adav801>`__
-  `MAX2165: Single-Conversion DVB-H
   Tuner <git.linux.org>/drivers/media/tuners/max2165.c>`__
   `MAX2165 <maxim>MAX2165>`__
-  `MAX2175: RF to Bits Automotive Radio
   Tuner <git.linux.org>/drivers/media/i2c/max2175.c>`__
   `MAX2175 <maxim>MAX2175>`__
-  `MAX9759: 3.2W, High-Efficiency, Low-EMI, Filterless, Class D Audio
   Amplifier <git.linux.org>/sound/soc/codecs/max9759.c>`__
   `MAX9759 <maxim>MAX9759>`__
-  `MAX9768: 10W Mono Class D Speaker Amplifier with Volume
   Control <git.linux.org>sound/soc/codecs/max9768.c>`__
   `MAX9768 <maxim>MAX9768>`__
-  `MAX98088: Stereo Audio Codec with FlexSound
   Technology <git.linux.org>/sound/soc/codecs/max98088.c>`__
   `MAX98088 <maxim>MAX98088>`__
-  `MAX98089: Stereo Audio Codec with FlexSound
   Technology <git.linux.org>/sound/soc/codecs/max98088.c>`__
   `MAX98089 <maxim>MAX98089>`__
-  `MAX98090: Ultra-Low Power Stereo Audio
   Codec <git.linux.org>sound/soc/codecs/max98090.c>`__
   `MAX98090 <maxim>MAX98090>`__
-  `MAX98095: Audio Hub with FlexSound
   Processor <git.linux.org>/sound/soc/codecs/max98095.c>`__
   `MAX98095 <maxim>MAX98095>`__
-  `MAX98357A: Tiny, Low-Cost, PCM Class D Amplifier with Class AB
   Performance <git.linux.org>sound/soc/codecs/max98357a.c>`__
   `MAX98357A <maxim>MAX98357A>`__
-  `MAX98360A: Tiny, Cost-Effective, Plug-and-Play Digital Class-D
   Amplifier <git.linux.org>/sound/soc/intel/boards/sof_da7219_max98373.c>`__
   `MAX98360A <maxim>MAX98360A>`__
-  `MAX98371: Digital Input Class D Speaker Amplifier with Dynamic
   Headroom Tracking <git.linux.org>/sound/soc/codecs/max98371.c>`__
   `MAX98371 <maxim>MAX98371>`__
-  `MAX98390: Boosted Class-D Amplifier with Integrated Dynamic Speaker
   Management <git.linux.org>/sound/soc/codecs/max98390.c>`__
   `MAX98390 <maxim>MAX98390>`__
-  `MAX9850: Stereo Audio DAC with DirectDrive® Headphone
   Amplifier <git.linux.org>/sound/soc/codecs/max9850.c>`__
   `MAX9850 <maxim>MAX9850>`__
-  `MAX9860: 16-Bit Mono Audio Voice
   Codec <git.linux.org>/sound/soc/codecs/max9860.c>`__
   `MAX9860 <maxim>MAX9860>`__
-  `MAX9867: Low-Power, Stereo Audio
   Codec <git.linux.org>/sound/soc/codecs/max9867.c>`__
   `MAX9867 <maxim>MAX9867>`__
-  `MAX9877: Low RF Susceptibility Mono Audio Subsystem with DirectDrive
   Headphone Amplifier <git.linux.org>/sound/soc/codecs/max9877.c>`__
   `Obsolete <maxim>MAX9877>`__
-  `SSM2305: Filterless, High Efficiency, Mono 2.8 W, Class-D Audio
   Amplifier <git.linux.org>sound/soc/codecs/ssm2305.c>`__
   `SSM2305 <adi>SSM2305>`__
-  `SSM2518: Digital Input Stereo, 2 W, Class-D Audio Power
   Amplifier <linux-drivers/sound/ssm2518>`__
-  `SSM2602: Low Power Audio Codec <linux-drivers/sound/ssm2602>`__
-  `SSM2603: Low Power Audio Codec <linux-drivers/sound/ssm2602>`__
-  `SSM2604: Low Power Audio Codec <linux-drivers/sound/ssm2602>`__
-  `SSM4567: Digital 2.5 W, 5.1 V, Boost Class-D Audio Amplifier with
   Output Sensing <linux-drivers/sound/ssm4567>`__

Transceiver
~~~~~~~~~~~

-  `DS26522: Dual T1/E1/J1
   Transceiver <git.linux.org>drivers/net/wan/slic_ds26522.c>`__
   `DS26522 <maxim>DS26522>`__

USB
~~~

-  `MAX3420E: USB Peripheral Controller with SPI
   Interface <git.linux.org>drivers/usb/gadget/udc/max3420_udc.c>`__
   `MAX3420E <maxim>MAX3420E>`__
-  `MAX3421E: USB Peripheral/Host Controller with SPI
   Interface <git.linux.org>drivers/usb/host/max3421-hcd.c>`__
   `MAX3421E <maxim>MAX3421E>`__
-  `MAX3355E: ±15kV ESD-Protected USB On-the-Go Charge Pump and
   Comparators in
   UCSP <git.linux.org>drivers/extcon/extcon-max3355.c>`__
   `MAX3355E <maxim>MAX3355E>`__
-  `MAX9490: USB to 1-Wire/iButton
   Adapter <git.linux.org>drivers/w1/masters/ds2490.c>`__
   `DS9490 <maxim>DS9490>`__

Video
~~~~~

-  `AD9389B: High Performance HDMI®/DVI
   Transmitter <git.linux.org>drivers/media/i2c/ad9389b.c>`__
   `AD9389B <adi>AD9389B>`__
-  `AD9889B: High Performance HDMI®/DVI
   Transmitter <git.linux.org>drivers/media/i2c/ad9389b.c>`__
   `AD9889B <adi>AD9889B>`__
-  `ADV7123: CMOS, 330 MHz Triple 10-Bit High Speed Video
   DAC <git.linux.org>drivers/gpu/drm/bridge/simple-bridge.c>`__
   `ADV7123 <adi>ADV7123>`__
-  `ADV7170: CMOS, 330 MHz Triple 10-Bit High Speed Video
   DAC <git.linux.org>drivers/media/i2c/adv7170.c>`__
   `Obsolete <adi>ADV7170>`__
-  `ADV7171: Digital PAL/NTSC Video Encoder with 10-Bit SSAF™ and
   Advanced Power
   Management <git.linux.org>drivers/media/i2c/adv7170.c>`__
   `ADV7171 <adi>ADV7171>`__
-  `ADV7175: Digital PAL/NTSC Video Encoder with 10-Bit SSAF™ and
   Advanced Power
   Management <git.linux.org>drivers/media/i2c/adv7175.c>`__
   `Obsolete <adi>ADV7175>`__
-  `ADV7175A: Digital PAL/NTSC Video Encoder with 10-Bit SSAF™ and
   Advanced Power
   Management <git.linux.org>drivers/media/i2c/adv7175.c>`__
   `Obsolete <adi>ADV7175A>`__
-  `ADV7176: Integrated Digital CCIR-601 YCrCb to PAL/NTSC Video
   Encoder <git.linux.org>drivers/media/i2c/adv7170.c>`__
   `ADV7176 <adi>ADV7176>`__
-  `ADV7180: 10-Bit, 4× Oversampling SDTV Video
   Decoder <git.linux.org>drivers/media/i2c/adv7180.c>`__
   `ADV7180 <adi>ADV7180>`__
-  `ADV7182: 10-Bit, SDTV Video Decoder with Differential
   Inputs <git.linux.org>/drivers/media/i2c/adv7180.c>`__
   `ADV7182 <adi>ADV7182>`__
-  `ADV7182A: 10-Bit, SDTV Video Decoder with Differential
   Inputs <git.linux.org>/drivers/media/i2c/adv7180.c>`__
   `ADV7182A <adi>ADV7182A>`__
-  `ADV7183: Advanced Video Decoder with 9-Bit ADC, & Component Input
   Support <git.linux.org>drivers/media/i2c/adv7183.c>`__
   `Obsolete <adi>ADV7183>`__
-  `ADV7280: 10-Bit, 4× Oversampled SDTV Video Decoder with
   Deinterlacer <git.linux.org>/drivers/media/i2c/adv7180.c>`__
   `ADV7280 <adi>ADV7280>`__
-  `ADV7280A: 10-Bit, 4× Oversampled SDTV Video Decoder with
   Deinterlacer <git.linux.org>/drivers/media/i2c/adv7180.c>`__
   `ADV7280A <adi>ADV7280A>`__
-  `ADV7281: 10-Bit, 4× Oversampled SDTV Video Decoder with Differential
   Inputs <git.linux.org>/drivers/media/i2c/adv7180.c>`__
   `ADV7281 <adi>ADV7281>`__
-  `ADV7281A: 10-Bit, 4× Oversampled SDTV Video Decoder with
   Differential Inputs <git.linux.org>/drivers/media/i2c/adv7180.c>`__
   `ADV7281A <adi>ADV7281A>`__
-  `ADV7282: 10-Bit, 4× Oversampled SDTV Video Decoder with Differential
   Inputs and
   Deinterlacer <git.linux.org>/drivers/media/i2c/adv7180.c>`__
   `ADV7282 <adi>ADV7282>`__
-  `ADV7282A: 10-Bit, 4× Oversampled SDTV Video Decoder with
   Differential Inputs and
   Deinterlacer <git.linux.org>/drivers/media/i2c/adv7180.c>`__
   `ADV7282A <adi>ADV7282A>`__
-  `ADV7481: Integrated Video Decoder and Dual-Mode HDMI/MHL
   Receiver <git.linux.org>drivers/media/i2c/adv748x/adv748x-core.c>`__
   `ADV7481 <adi>ADV7481>`__
-  `ADV7482: Integrated Video Decoder and HDMI
   Receiver <git.linux.org>drivers/media/i2c/adv748x/adv748x-core.c>`__
   `ADV7482 <adi>ADV7482>`__
-  `ADV7343: Multiformat Video Encoder with Six, 11-Bit, 297 MHz
   DACs <git.linux.org>drivers/media/i2c/adv7343.c>`__
   `ADV7343 <adi>ADV7343>`__
-  `ADV7393: Low Power, Chip Scale 10-Bit SD/HD Video
   Encoder <git.linux.org>drivers/media/i2c/adv7393.c>`__
   `ADV7393 <adi>ADV7393>`__
-  `ADV7604: 12-Bit, Deep Color HDMI v1.3 Receiver with Analog
   Interface <git.linux.org>drivers/media/i2c/adv7604.c>`__
   `ADV7604 <adi>ADV7604>`__
-  `ADV7611: Low Power 165 MHz HDMI
   Receiver <git.linux.org>drivers/media/i2c/adv7604.c>`__
   `ADV7611 <adi>ADV7611>`__
-  `ADV7612: Dual Port, Xpressview, 225 MHz HDMI
   Receiver <git.linux.org>drivers/media/i2c/adv7604.c>`__
   `ADV7612 <adi>ADV7612>`__
-  `AD9389B: High Performance HDMI®/DVI
   Transmitter <git.linux.org>drivers/media/i2c/ad9389b.c>`__
   `AD9389B <adi>AD9389B>`__
-  `ADV7842: Dual HDMI 1.4 Fast Switching Receiver with 12-Bit, 170 MHz
   Video and Graphics Digitizer and 3D Comb Filter
   Decoder <git.linux.org>drivers/media/i2c/adv7842.c>`__
   `ADV7842 <adi>ADV7842>`__
-  `ADV7844: Quad HDMI 1.4 Fast Switching Receiver with 12-Bit, 170 MHz
   Video and Graphics Digitizer and 3D Comb Filter
   Decoder <git.linux.org>drivers/media/i2c/adv7842.c>`__
   `ADV7844 <adi>ADV7844>`__
-  `ADV7511: 225 MHZ, HIGH PERFORMANCE HDMI® TRANSMITTER WITH
   ARC <linux-drivers/drm/adv7511>`__
-  `ADV7511W: 165 MHZ HIGH PERFORMANCE HDMI
   TRANSMITTER <linux-drivers/drm/adv7511>`__
-  `ADV7513: 165 MHZ HIGH PERFORMANCE HDMI
   TRANSMITTER <linux-drivers/drm/adv7511>`__
-  `ADV7533: MIPI/DSI Receiver with HDMI
   Transmitter <linux-drivers/drm/adv7511>`__
-  `ADV7535: MIPI/DSI Receiver with HDMI
   Transmitter <linux-drivers/drm/adv7511>`__

1-Wire Controller
~~~~~~~~~~~~~~~~~

-  `DS9490: USB to 1-Wire/iButton
   Adapter <git.linux.org>drivers/w1/masters/ds2490.c>`__
   `DS9490 <maxim>DS9490>`__
-  `DS2490: USB to 1-Wire Bridge
   Chip <git.linux.org>drivers/w1/masters/ds2490.c>`__
   `DS2490 <maxim>DS2490>`__
-  `DS2482-100: Single-Channel 1-Wire
   Master <git.linux.org>drivers/w1/masters/ds2482.c>`__
   `DS2482-100 <maxim>DS2482-100>`__
-  `DS2482-800: 8-Channel 1-Wire
   Master <git.linux.org>drivers/w1/masters/ds2482.c>`__
   `DS2482-800 <maxim>DS2482-800>`__

1-Wire Peripheral
~~~~~~~~~~~~~~~~~

-  `DS28E17: 1-Wire®-to-I2C Master
   Bridge <git.linux.org>drivers/w1/slaves/w1_ds28e17.c>`__
   `DS28E17 <maxim>DS28E17>`__
-  `DS28E04-100: 4096-Bit Addressable 1-Wire EEPROM with
   PIO <git.linux.org>drivers/w1/slaves/w1_ds28e04.c>`__
   `DS28E04-100 <maxim>DS28E04-100>`__
-  `DS28E05: 1-Wire
   EEPROM <git.linux.org>drivers/w1/slaves/w1_ds2805.c>`__
   `DS28E05 <maxim>DS28E05>`__
-  `DS2438: Smart Battery
   Monitor <git.linux.org>drivers/w1/slaves/w1_ds2438.c>`__
   `DS2438 <maxim>DS2438>`__
-  `DS2433: 4Kb 1-Wire
   EEPROM <git.linux.org>drivers/w1/slaves/w1_ds2433.c>`__
   `DS2433 <maxim>DS2433>`__
-  `DS2431: 1024-Bit 1-Wire
   EEPROM <git.linux.org>drivers/w1/slaves/w1_ds2431.c>`__
   `DS2431 <maxim>DS2431>`__
-  `DS2423: 4kbit 1-Wire RAM with
   Counter <git.linux.org>drivers/w1/slaves/w1_ds2423.c>`__
   `DS2423 <maxim>DS2423>`__
-  `DS2413: 1-Wire Dual Channel Addressable
   Switch <git.linux.org>drivers/w1/slaves/w1_ds2413.c>`__
   `DS2413 <maxim>DS2413>`__
-  `DS2411: Silicon Serial Number with VCC
   Input <git.linux.org>drivers/w1/slaves/w1_smem.c>`__
   `DS2411 <maxim>DS2411>`__
-  `DS2405: Addressable
   Switch <git.linux.org>drivers/w1/slaves/w1_ds2405.c>`__
   `DS2405 <maxim>DS2405>`__
-  `DS2406: Dual Addressable Switch Plus 1Kb
   Memory <git.linux.org>drivers/w1/slaves/w1_ds2406.c>`__
   `DS2406 <maxim>DS2406>`__
-  `DS2408: 1-Wire 8-Channel Addressable
   Switch <git.linux.org>drivers/w1/slaves/w1_ds2408.c>`__
   `DS2408 <maxim>DS2408>`__
-  `DS2401: Silicon Serial
   Number <git.linux.org>drivers/w1/slaves/w1_smem.c>`__
   `DS2401 <maxim>DS2401>`__
-  `DS1990A: iButton Serial
   Number <git.linux.org>drivers/w1/slaves/w1_smem.c>`__
   `DS1990A <maxim>DS1990A>`__
-  `DS2502: 1Kb Add-Only
   Memory <git.linux.org>drivers/w1/slaves/w1_ds250x.c>`__
   `DS2502 <maxim>DS2502>`__
-  `DS2505: 16Kb Add-Only
   Memory <git.linux.org>drivers/w1/slaves/w1_ds250x.c>`__
   `DS2505 <maxim>DS2505>`__
-  `DS1822: Econo 1-Wire Digital
   Thermometer <git.linux.org>drivers/w1/slaves/w1_therm.c>`__
   `ds1822 <maxim>ds1822>`__
-  `DS1825: Programmable Resolution 1-Wire Digital Thermometer With
   4-Bit ID <git.linux.org>drivers/w1/slaves/w1_therm.c>`__
   `DS1825 <maxim>DS1825>`__
-  `DS18S20: 1-Wire Parasite-Power Digital
   Thermometer <git.linux.org>drivers/w1/slaves/w1_therm.c>`__
   `DS18S20 <maxim>DS18S20>`__
-  `DS28EA00: 1-Wire Digital Thermometer with Sequence Detect and
   PIO <git.linux.org>drivers/w1/slaves/w1_therm.c>`__
   `DS28EA00 <maxim>DS28EA00>`__
-  `DS28E04-100: 4096-Bit Addressable 1-Wire EEPROM with
   PIO <git.linux.org>drivers/w1/slaves/w1_ds28e04.c>`__
   `DS28E04-100 <maxim>DS28E04-100>`__

.. [1]
   IDC study/survey from over 5000 developers in 116 countries. Open
   Source in Global Software: Market Impact, Disruption, and Business
   Models. 2006.
