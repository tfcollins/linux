

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

	<div class="iio-context">

	<p><b>ad9361-phy</b></p>
	<p>This is a device</p>
	<p class="devattr-header"><i>DEVICE ATTRIBUTES</i>: <b>ad9361-phy</b></p>
	<!-- <hr class="devattr-table-hr"> -->
	<table class="devattr-table">
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">calib_mode</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">Set calibration mode</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">calib_mode_available</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">dcxo_tune_coarse</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">dcxo_tune_coarse_available</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">dcxo_tune_fine</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">dcxo_tune_fine_available</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">ensm_mode</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">ensm_mode_available</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">filter_fir_config</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">gain_table_config</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">multichip_sync</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">rssi_gain_step_error</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">rx_path_rates</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">trx_rate_governor</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">trx_rate_governor_available</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">tx_path_rates</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">xo_correction</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">xo_correction_available</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>

	</table>

	<br>
	<!-- <hr> -->
	<br>
	<p class="devattr-header"><i>CHANNEL ATTRIBUTES</i>: <b>ad9361-phy</b></p>
	<table class="devattr-table">
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">external</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage1, altvoltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage1, altvoltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">fastlock_load</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage1, altvoltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage1, altvoltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">fastlock_recall</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage1, altvoltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage1, altvoltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">fastlock_save</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage1, altvoltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage1, altvoltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">fastlock_store</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage1, altvoltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage1, altvoltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">frequency</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage1, altvoltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage1, altvoltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">frequency_available</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage1, altvoltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage1, altvoltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">powerdown</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage1, altvoltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage1, altvoltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">bb_dc_offset_tracking_en</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">filter_fir_en</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">gain_control_mode</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">gain_control_mode_available</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">hardwaregain</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">hardwaregain_available</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">quadrature_tracking_en</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">rf_bandwidth</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">rf_bandwidth_available</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">rf_dc_offset_tracking_en</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">rf_port_select</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">rf_port_select_available</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">rssi</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">sampling_frequency</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">sampling_frequency_available</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage3, voltage2, voltage0, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">raw</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage3, voltage2, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage3, voltage2, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">scale</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage3, voltage2, voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage3, voltage2, voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">input</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>temp0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>temp0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">offset</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">voltage_filter_fir_en</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>out</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>out</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>

	</table>    


	<p><b>xadc</b></p>
	<p>This is a device</p>
	<p class="devattr-header"><i>DEVICE ATTRIBUTES</i>: <b>xadc</b></p>
	<!-- <hr class="devattr-table-hr"> -->
	<table class="devattr-table">
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">sampling_frequency</td>
	<td class="devattr-type-col">str</td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>

	</table>

	<br>
	<!-- <hr> -->
	<br>
	<p class="devattr-header"><i>CHANNEL ATTRIBUTES</i>: <b>xadc</b></p>
	<table class="devattr-table">
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">raw</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage5, voltage0, voltage4, temp0, voltage7, voltage1, voltage2, voltage3, voltage8, voltage6</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage5, voltage0, voltage4, temp0, voltage7, voltage1, voltage2, voltage3, voltage8, voltage6</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">scale</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage5, voltage0, voltage4, temp0, voltage7, voltage1, voltage2, voltage3, voltage8, voltage6</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage5, voltage0, voltage4, temp0, voltage7, voltage1, voltage2, voltage3, voltage8, voltage6</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">offset</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>temp0</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>temp0</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>

	</table>    


	<br>
	<!-- <hr> -->
	<br>
	<p class="devattr-header"><i>CHANNEL ATTRIBUTES</i>: <b>cf-ad9361-dds-core-lpc</b></p>
	<table class="devattr-table">
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">calibphase</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage1</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage1</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">calibscale</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage1</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage1</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">sampling_frequency</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage1, altvoltage3, altvoltage1, altvoltage0, altvoltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage1, altvoltage3, altvoltage1, altvoltage0, altvoltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">sampling_frequency_available</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage1</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage1</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">frequency</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage3, altvoltage1, altvoltage0, altvoltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage3, altvoltage1, altvoltage0, altvoltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">phase</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage3, altvoltage1, altvoltage0, altvoltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage3, altvoltage1, altvoltage0, altvoltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">raw</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage3, altvoltage1, altvoltage0, altvoltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage3, altvoltage1, altvoltage0, altvoltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">scale</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>altvoltage3, altvoltage1, altvoltage0, altvoltage2</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>altvoltage3, altvoltage1, altvoltage0, altvoltage2</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>

	</table>    


	<br>
	<!-- <hr> -->
	<br>
	<p class="devattr-header"><i>CHANNEL ATTRIBUTES</i>: <b>cf-ad9361-lpc</b></p>
	<table class="devattr-table">
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">calibbias</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage1</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage1</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">calibphase</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage1</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage1</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">calibscale</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage1</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage1</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">samples_pps</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage1</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage1</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">sampling_frequency</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage1</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage1</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>
	<tr>
	<td class="devattr-topleft-col"></td>
	<td class="devattr-name-col">sampling_frequency_available</td>
	<td class="devattr-type-col">str</td>
	<!-- <span>voltage0, voltage1</span></td> -->
	</tr>
	<tr>
	<td></td>
	<td></td>
	<td class="devattr-type-col"><span>voltage0, voltage1</span></td>
	</tr>
	<tr>
	<td class="devattr-bottomleft-col"></td>
	<td class="devattr-spacer-col"></td>
	<td class="devattr-about">NA</td>
	</tr>

	</table>    



	</div>
