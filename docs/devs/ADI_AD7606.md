

::: linux:Documentation/devicetree/bindings/iio/adc/adi,ad7606.yaml

=== "Properties"

    <table>
        <tr>
            <th>Name</th>
            <th>Type</th>
            <th>Required</th>
            <th>Info</th>
        </tr>
        
        <tr>
            <td>compatible</td>
            
            <td>enum</td>
            
            <td>yes</td>
            
            <td>Options: <span class='enum-dt'>&nbspadi,ad7605-4&nbsp</span> <span class='enum-dt'>&nbspadi,ad7606-8&nbsp</span> <span class='enum-dt'>&nbspadi,ad7606-6&nbsp</span> <span class='enum-dt'>&nbspadi,ad7606-4&nbsp</span> <span class='enum-dt'>&nbspadi,ad7606b&nbsp</span> <span class='enum-dt'>&nbspadi,ad7616&nbsp</span> </td>
            
        </tr>
        
        <tr>
            <td>reg</td>
            
            <td></td>
            
            <td>yes</td>
            
            <td></td>
            
        </tr>
        
        <tr>
            <td>spi-cpha</td>
            
            <td>bool</td>
            
            <td>yes</td>
            
            <td></td>
            
        </tr>
        
        <tr>
            <td>spi-cpol</td>
            
            <td>bool</td>
            
            <td></td>
            
            <td></td>
            
        </tr>
        
        <tr>
            <td>spi-max-frequency</td>
            
            <td>bool</td>
            
            <td></td>
            
            <td></td>
            
        </tr>
        
        <tr>
            <td>avcc-supply</td>
            
            <td>bool</td>
            
            <td>yes</td>
            
            <td></td>
            
        </tr>
        
        <tr>
            <td>interrupts</td>
            
            <td></td>
            
            <td>yes</td>
            
            <td></td>
            
        </tr>
        
        <tr>
            <td>adi,conversion-start-gpios</td>
            
            <td></td>
            
            <td>yes</td>
            
            <td>Must be the device tree identifier of the CONVST pin. This logic input is used to initiate conversions on the analog input channels. As the line is active high, it should be marked GPIO_ACTIVE_HIGH.</td>
            
        </tr>
        
        <tr>
            <td>reset-gpios</td>
            
            <td></td>
            
            <td></td>
            
            <td>Must be the device tree identifier of the RESET pin. If specified, it will be asserted during driver probe. As the line is active high, it should be marked GPIO_ACTIVE_HIGH.</td>
            
        </tr>
        
        <tr>
            <td>standby-gpios</td>
            
            <td></td>
            
            <td></td>
            
            <td>Must be the device tree identifier of the STBY pin. This pin is used to place the AD7606 into one of two power-down modes, Standby mode or Shutdown mode. As the line is active low, it should be marked GPIO_ACTIVE_LOW.</td>
            
        </tr>
        
        <tr>
            <td>adi,first-data-gpios</td>
            
            <td></td>
            
            <td></td>
            
            <td>Must be the device tree identifier of the FRSTDATA pin. The FRSTDATA output indicates when the first channel, V1, is being read back on either the parallel, byte or serial interface. As the line is active high, it should be marked GPIO_ACTIVE_HIGH.</td>
            
        </tr>
        
        <tr>
            <td>adi,range-gpios</td>
            
            <td></td>
            
            <td></td>
            
            <td>Must be the device tree identifier of the RANGE pin. The polarity on this pin determines the input range of the analog input channels. If this pin is tied to a logic high, the analog input range is ±10V for all channels. If this pin is tied to a logic low, the analog input range is ±5V for all channels. As the line is active high, it should be marked GPIO_ACTIVE_HIGH.</td>
            
        </tr>
        
        <tr>
            <td>adi,oversampling-ratio-gpios</td>
            
            <td></td>
            
            <td></td>
            
            <td>Must be the device tree identifier of the over-sampling mode pins. As the line is active high, it should be marked GPIO_ACTIVE_HIGH.</td>
            
        </tr>
        
        <tr>
            <td>adi,sw-mode</td>
            
            <td>boolean</td>
            
            <td></td>
            
            <td>Software mode of operation, so far available only for ad7616 and ad7606b. It is enabled when all three oversampling mode pins are connected to high level. The device is configured by the corresponding registers. If the adi,oversampling-ratio-gpios property is defined, then the driver will set the oversampling gpios to high. Otherwise, it is assumed that the pins are hardwired to VDD.</td>
            
        </tr>
        
    </table>

=== "Examples"

    Example

=== "sysfs"

    ```bash
    root:/> cd /sys/bus/iio/devices/
    root:/sys/bus/iio/devices> ls
    iio:device4  iio:trigger0

    root:/sys/bus/iio/devices> cd iio:device4

    root:/sys/bus/iio/devices/iio:device4> ls -l
    drwxr-xr-x    2 root     root             0 Jan  1 00:00 buffer
    -r--r--r--    1 root     root          4096 Jan  1 00:00 dev
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage0_calibbias
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage0_calibphase
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage0_calibscale
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage0_filter_high_pass_3db_frequency
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage0_test_mode
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage1_calibbias
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage1_calibphase
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage1_calibscale
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage1_filter_high_pass_3db_frequency
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage1_test_mode
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage_sampling_frequency
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 in_voltage_scale
    -r--r--r--    1 root     root          4096 Jan  1 00:00 in_voltage_scale_available
    -r--r--r--    1 root     root          4096 Jan  1 00:00 in_voltage_test_mode_available
    -r--r--r--    1 root     root          4096 Jan  1 00:00 name
    drwxr-xr-x    2 root     root             0 Jan  1 00:00 scan_elements
    lrwxrwxrwx    1 root     root             0 Jan  1 00:00 subsystem -> ../../../../bus/iio
    -rw-r--r--    1 root     root          4096 Jan  1 00:00 uevent
    root:/sys/bus/iio/devices/iio:device4>
    ```

=== "libiio API"

    libiio