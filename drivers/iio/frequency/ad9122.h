/*
 * AD9122 SPI DAC driver for AXI DDS PCORE/COREFPGA Module
 *
 * Copyright 2012 Analog Devices Inc.
 *
 * Licensed under the GPL-2.
 */

#ifndef IIO_FREQUENCY_AD9122_H_
#define IIO_FREQUENCY_AD9122_H_

/* Registers */
#define AD9122_REG_COMM			0x00
#define AD9122_REG_POWER_CTRL		0x01
#define AD9122_REG_DATA_FORMAT		0x03
#define AD9122_REG_INTERRUPT_EN_1	0x04
#define AD9122_REG_INTERRUPT_EN_2	0x05
#define AD9122_REG_EVENT_FLAG_1		0x06
#define AD9122_REG_EVENT_FLAG_2		0x07
#define AD9122_REG_CLK_REC_CTRL		0x08
#define AD9122_REG_PLL_CTRL_1		0x0A
#define AD9122_REG_PLL_CTRL_2		0x0C
#define AD9122_REG_PLL_CTRL_3		0x0D
#define AD9122_REG_PLL_STATUS_1		0x0E
#define AD9122_REG_PLL_STATUS_2		0x0F
#define AD9122_REG_SYNC_CTRL_1		0x10
#define AD9122_REG_SYNC_CTRL_2		0x11
#define AD9122_REG_SYNC_STATUS_1	0x12
#define AD9122_REG_SYNC_STATUS_2	0x13
#define AD9122_REG_DATA_REC_STATUS	0x15
#define AD9122_REG_DCI_DELAY		0x16
#define AD9122_REG_FIFO_CTRL		0x17
#define AD9122_REG_FIFO_STATUS_1	0x18
#define AD9122_REG_FIFO_STATUS_2	0x19
#define AD9122_REG_DATAPATH_CTRL	0x1B
#define AD9122_REG_HB1_CTRL		0x1C
#define AD9122_REG_HB2_CTRL		0x1D
#define AD9122_REG_HB3_CTRL		0x1E
#define AD9122_REG_CHIP_ID		0x1F
#define AD9122_REG_FTW_7_0		0x30
#define AD9122_REG_FTW_15_8		0x31
#define AD9122_REG_FTW_23_16		0x32
#define AD9122_REG_FTW_31_24		0x33
#define AD9122_REG_NCO_PHA_OFFSET_LSB	0x34
#define AD9122_REG_NCO_PHA_OFFSET_MSB	0x35
#define AD9122_REG_NCO_FTW_UPDATE	0x36
#define AD9122_REG_I_PHA_ADJ_LSB	0x38
#define AD9122_REG_I_PHA_ADJ_MSB	0x39
#define AD9122_REG_Q_PHA_ADJ_LSB	0x3A
#define AD9122_REG_Q_PHA_ADJ_MSB	0x3B
#define AD9122_REG_I_DAC_OFFSET_LSB	0x3C
#define AD9122_REG_I_DAC_OFFSET_MSB	0x3D
#define AD9122_REG_Q_DAC_OFFSET_LSB	0x3E
#define AD9122_REG_Q_DAC_OFFSET_MSB	0x3F
#define AD9122_REG_I_DAC_FS_ADJ		0x40
#define AD9122_REG_I_DAC_CTRL		0x41
#define AD9122_REG_I_AUX_DAC_DATA	0x42
#define AD9122_REG_I_AUX_DAC_CTRL	0x43
#define AD9122_REG_Q_DAC_FS_ADJ		0x44
#define AD9122_REG_Q_DAC_CTRL		0x45
#define AD9122_REG_Q_AUX_DAC_DATA	0x46
#define AD9122_REG_Q_AUX_DAC_CTRL	0x47
#define AD9122_REG_DIE_TEMP_RANGE_CTRL	0x48
#define AD9122_REG_DIE_TEMP_LSB		0x49
#define AD9122_REG_DIE_TEMP_MSB		0x4A
#define AD9122_REG_SED_CTRL		0x67
#define AD9122_REG_COMPARE_I0_LSBS	0x68
#define AD9122_REG_COMPARE_I0_MSBS	0x69
#define AD9122_REG_COMPARE_Q0_LSBS	0x6A
#define AD9122_REG_COMPARE_Q0_MSBS	0x6B
#define AD9122_REG_COMPARE_I1_LSBS	0x6C
#define AD9122_REG_COMPARE_I1_MSBS	0x6D
#define AD9122_REG_COMPARE_Q1_LSBS	0x6E
#define AD9122_REG_COMPARE_Q1_MSBS	0x6F
#define AD9122_REG_SED_I_LSBS		0x70
#define AD9122_REG_SED_I_MSBS		0x71
#define AD9122_REG_SED_Q_LSBS		0x72
#define AD9122_REG_SED_Q_MSBS		0x73
#define AD9122_REG_REVISION		0x7F

/* AD9122_REG_COMM definitions */
#define AD9122_COMM_SDIO				(1 << 7)
#define AD9122_COMM_LSB_FIRST				(1 << 6)
#define AD9122_COMM_RESET				(1 << 5)

/* AD9122_REG_POWER_CTRL definitions */
#define AD9122_POWER_CTRL_PD_I_DAC			(1 << 7)
#define AD9122_POWER_CTRL_PD_Q_DAC			(1 << 6)
#define AD9122_POWER_CTRL_PD_DATA_REC			(1 << 5)
#define AD9122_POWER_CTRL_PD_AUX_ADC			(1 << 4)

/* AD9122_REG_DATA_FORMAT definitions */
#define AD9122_DATA_FORMAT_BINARY			(1 << 7)
#define AD9122_DATA_FORMAT_Q_DATA_FIRST			(1 << 6)
#define AD9122_DATA_FORMAT_MSB_SWAP			(1 << 5)
#define AD9122_DATA_FORMAT_BUS_WIDTH(x)			(((x) & 0x3) << 0)

/* AD9122_REG_INTERRUPT_EN_1 definitions */
#define AD9122_INTERRUPT_EN_1_EN_PLL_LOCK_LOST		(1 << 7)
#define AD9122_INTERRUPT_EN_1_EN_PLL_LOCKED		(1 << 6)
#define AD9122_INTERRUPT_EN_1_EN_SYNC_SIGNAL_LOST	(1 << 5)
#define AD9122_INTERRUPT_EN_1_EN_SYNC_SIGNAL_LOCKED	(1 << 4)
#define AD9122_INTERRUPT_EN_1_EN_FIFO_WARNING_1		(1 << 1)
#define AD9122_INTERRUPT_EN_1_EN_FIFO_WARNING_2		(1 << 0)

/* AD9122_REG_INTERRUPT_EN_2 definitions */
#define AD9122_INTERRUPT_EN_2_EN_AED_COMPARE_PASS	(1 << 4)
#define AD9122_INTERRUPT_EN_2_EN_AED_COMPARE_FAIL	(1 << 3)
#define AD9122_INTERRUPT_EN_2_EN_SED_COMPARE_FAIL	(1 << 2)

/* AD9122_REG_EVENT_FLAG_1 definitions */
#define AD9122_EVENT_FLAG_1_PLL_LOCK_LOST		(1 << 7)
#define AD9122_EVENT_FLAG_1_PLL_LOCKED			(1 << 6)
#define AD9122_EVENT_FLAG_1_SYNC_SIGNAL_LOST		(1 << 5)
#define AD9122_EVENT_FLAG_1_SYNC_SIGNAL_LOCKED		(1 << 4)
#define AD9122_EVENT_FLAG_1_FIFO_WARNING_1		(1 << 1)
#define AD9122_EVENT_FLAG_1_FIFO_WARNING_2		(1 << 0)

/* AD9122_REG_EVENT_FLAG_2 definitions */
#define AD9122_EVENT_FLAG_2_AED_COMPARE_PASS		(1 << 4)
#define AD9122_EVENT_FLAG_2_AED_COMPARE_FAIL		(1 << 3)
#define AD9122_EVENT_FLAG_2_SED_COMPARE_FAIL		(1 << 2)

/* AD9122_REG_CLK_REC_CTRL definitions */
#define AD9122_CLK_REC_CTRL_DACCLK_DUTY_CORRECTION	(1 << 7)
#define AD9122_CLK_REC_CTRL_REFCLK_DUTY_CORRECTION	(1 << 6)
#define AD9122_CLK_REC_CTRL_DACCLK_CROSS_CORRECTION	(1 << 5)
#define AD9122_CLK_REC_CTRL_REFCLK_CROSS_CORRECTION	(1 << 4)

/* AD9122_REG_PLL_CTRL_1 definitions */
#define AD9122_PLL_CTRL_1_PLL_EN			(1 << 7)
#define AD9122_PLL_CTRL_1_PLL_MANUAL_EN			(1 << 6)
#define AD9122_PLL_CTRL_1_MANUAL_VCO_BAND(x)		((x) & 0x3F) << 0)

/* AD9122_REG_PLL_CTRL_2 definitions */
#define AD9122_PLL_CTRL_2_PLL_LOOP_BANDWIDTH(x)		(((x) & 0x3) << 6)
#define AD9122_PLL_CTRL_2_PLL_CHARGE_PUMP_CURRENT(x)	(((x) & 0x1F) << 0)

/* AD9122_REG_PLL_CTRL_3 definitions */
#define AD9122_PLL_CTRL_3_N2(x)				(((x) & 0x3) << 6)
#define AD9122_PLL_CTRL_3_PLL_CROSS_CTRL_EN		(1 << 4)
#define AD9122_PLL_CTRL_3_N0(x)				(((x) & 0x3) << 2)
#define AD9122_PLL_CTRL_3_N1(x)				(((x) & 0x3) << 0)

/* AD9122_REG_PLL_STATUS_1 definitions */
#define AD9122_PLL_STATUS_1_PLL_LOCKED			(1 << 7)
#define AD9122_PLL_STATUS_1_VCO_CTRL_VOLTAGE(x)		(((x) & 0xF) << 0)

/* AD9122_REG_PLL_STATUS_2 definitions */
#define AD9122_PLL_STATUS_2_VCO_BAND_READBACK(x)	(((x) & 0x3F) << 0)

/* AD9122_REG_SYNC_CTRL_1 definitions */
#define AD9122_SYNC_CTRL_1_SYNC_EN			(1 << 7)
#define AD9122_SYNC_CTRL_1_DATA_FIFO_RATE_TOGGLE	(1 << 6)
#define AD9122_SYNC_CTRL_1_RISING_EDGE_SYNC		(1 << 3)
#define AD9122_SYNC_CTRL_1_SYNC_AVERAGING(x)		(((x) & 0x7) << 0)

/* AD9122_REG_SYNC_CTRL_2 definitions */
#define AD9122_SYNC_CTRL_2_SYNC_PHA_REQUEST(x)		(((x) & 0x3F) << 0)

/* AD9122_REG_SYNC_STATUS_1 definitions */
#define AD9122_SYNC_STATUS_1_SYNC_LOST			(1 << 7)
#define AD9122_SYNC_STATUS_1_SYNC_LOCKED		(1 << 6)

/* AD9122_REG_SYNC_STATUS_2 definitions */
#define AD9122_SYNC_STATUS_2_SYNC_PHA_READBACK		(((x) & 0xFF) << 0)

/* AD9122_REG_DATA_REC_STATUS definitions */
#define AD9122_DATA_REC_STATUS_LVDS_FRAME_LEVEL_H	(1 << 5)
#define AD9122_DATA_REC_STATUS_LVDS_FRAME_LEVEL_L	(1 << 4)
#define AD9122_DATA_REC_STATUS_LVDS_DCI_LEVEL_H		(1 << 3)
#define AD9122_DATA_REC_STATUS_LVDS_DCI_LEVEL_L		(1 << 2)
#define AD9122_DATA_REC_STATUS_LVDS_DATA_LEVEL_H	(1 << 1)
#define AD9122_DATA_REC_STATUS_LVDS_DATA_LEVEL_L	(1 << 0)

/* AD9122_REG_DCI_DELAY definitions */
#define AD9122_DCI_DELAY_DCI_DELAY(x)			(((x) & 0x3) << 0)

/* AD9122_REG_FIFO_CTRL definitions */
#define AD9122_FIFO_CTRL_FIFO_PHA_OFFSET(x)		(((x) & 0x7) << 0)

/* AD9122_REG_FIFO_STATUS_1 definitions */
#define AD9122_FIFO_STATUS_1_FIFO_WARNING_1		(1 << 7)
#define AD9122_FIFO_STATUS_1_FIFO_WARNING_2		(1 << 6)
#define AD9122_FIFO_STATUS_1_FIFO_SOFT_ALIGN_ACK	(1 << 2)
#define AD9122_FIFO_STATUS_1_FIFO_SOFT_ALIGN_REQ	(1 << 1)

/* AD9122_REG_FIFO_STATUS_2 definitions */
#define AD9122_FIFO_STATUS_2_FIFO_LEVEL			(((x) & 0xFF) << 0)

/* AD9122_REG_DATAPATH_CTRL definitions */
#define AD9122_DATAPATH_CTRL_BYPASS_PREMOD		(1 << 7)
#define AD9122_DATAPATH_CTRL_BYPASS_INV_SINC		(1 << 6)
#define AD9122_DATAPATH_CTRL_BYPASS_NCO			(1 << 5)
#define AD9122_DATAPATH_CTRL_NCO_GAIN			(1 << 3)
#define AD9122_DATAPATH_CTRL_BYPASS_PHA_COMP_DC_OFFSET	(1 << 2)
#define AD9122_DATAPATH_CTRL_SELECT_SIDEBAND		(1 << 1)
#define AD9122_DATAPATH_CTRL_SEND_I_DATA_TO_Q_DATA	(1 << 0)

/* AD9122_REG_HB1_CTRL definitions */
#define AD9122_HB1_CTRL_HB1(x)				(((x) & 0x3) << 1)
#define AD9122_HB1_CTRL_BYPASS_HB1			(1 << 0)

/* AD9122_REG_HB2_CTRL definitions */
#define AD9122_HB2_CTRL_HB2(x)				(((x) & 0x3F) << 1)
#define AD9122_HB2_CTRL_BYPASS_HB2			(1 << 0)

/* AD9122_REG_HB3_CTRL definitions */
#define AD9122_HB3_CTRL_HB3(x)				(((x) & 0x3F) << 1)
#define AD9122_HB3_CTRL_BYPASS_HB3			(1 << 0)

/* Value of AD9122_REG_CHIP_ID */
#define	AD9122_CHIP_ID	0x08

/* AD9122_REG_NCO_FTW_UPDATE definitions */
#define AD9122_NCO_FTW_UPDATE_FRAME_FTW_ACK		(1 << 5)
#define AD9122_NCO_FTW_UPDATE_FRAME_FTW_REQ		(1 << 4)
#define AD9122_NCO_FTW_UPDATE_UPDATE_FTW_ACK		(1 << 1)
#define AD9122_NCO_FTW_UPDATE_UPDATE_FTW_REQ		(1 << 0)

/* AD9122_REG_I_PHA_ADJ_LSB definitions */
#define AD9122_REG_I_PHA_ADJ_7_0(x)			(((x) & 0xFF) << 0)

/* AD9122_REG_I_PHA_ADJ_MSB definitions */
#define AD9122_REG_I_PHA_ADJ_9_8(x)			(((x) & 0x3) << 0)

/* AD9122_REG_Q_PHA_ADJ_LSB definitions */
#define AD9122_REG_Q_PHA_ADJ_7_0(x)			(((x) & 0xFF) << 0)

/* AD9122_REG_Q_PHA_ADJ_MSB definitions */
#define AD9122_REG_Q_PHA_ADJ_9_8(x)			(((x) & 0x3) << 0)

/* AD9122_REG_I_DAC_FS_ADJ definitions */
#define AD9122_I_DAC_FS_ADJ_I_DAC_FS_ADJ_7_0(x)		(((x) & 0xFF) << 0)

/* AD9122_I_DAC_CTRL definitions */
#define AD9122_I_DAC_CTRL_I_DAC_SLEEP			(1 << 7)
#define AD9122_I_DAC_CTRL_I_DAC_FS_ADJ_9_8(x)		(((x) & 0x3) << 0)

/* AD9122_REG_I_AUX_DAC_DATA definitions */
#define AD9122_I_AUX_DAC_DATA_I_AUX_DAC_7_0		(((x) & 0xFF) << 0)

/* AD9122_REG_I_AUX_DAC_CTRL definitions */
#define AD9122_I_AUX_DAC_CTRL_I_AUX_DAC_SIGN		(1 << 7)
#define AD9122_I_AUX_DAC_CTRL_I_AUX_DAC_CURRENT_DIR	(1 << 6)
#define AD9122_I_AUX_DAC_CTRL_I_AUX_DAC_SLEEP		(1 << 5)
#define AD9122_I_AUX_DAC_CTRL_I_AUX_DAC_9_8(x)		(((x) & 0x3) << 0)

/* AD9122_REG_Q_DAC_FS_ADJ definitions */
#define AD9122_Q_DAC_FS_ADJ_Q_DAC_FS_ADJ_7_0(x)		(((x) & 0xFF) << 0)

/* AD9122_Q_DAC_CTRL definitions */
#define AD9122_Q_DAC_CTRL_Q_DAC_SLEEP			(1 << 7)
#define AD9122_Q_DAC_CTRL_Q_DAC_FS_ADJ_9_8(x)		(((x) & 0x3) << 0)

/* AD9122_REG_Q_AUX_DAC_DATA definitions */
#define AD9122_Q_AUX_DAC_DATA_Q_AUX_DAC_7_0		(((x) & 0xFF) << 0)

/* AD9122_REG_Q_AUX_DAC_CTRL definitions */
#define AD9122_Q_AUX_DAC_CTRL_Q_AUX_DAC_SIGN		(1 << 7)
#define AD9122_Q_AUX_DAC_CTRL_Q_AUX_DAC_CURRENT_DIR	(1 << 6)
#define AD9122_Q_AUX_DAC_CTRL_Q_AUX_DAC_SLEEP		(1 << 5)
#define AD9122_Q_AUX_DAC_CTRL_Q_AUX_DAC_9_8(x)		(((x) & 0x3) << 0)

/* AD9122_REG_DIE_TEMP_RANGE_CTRL definitions */
#define AD9122_DIE_TEMP_RANGE_CTRL_FS_CURRENT(x)	(((x) & 0x7) << 4)
#define AD9122_DIE_TEMP_RANGE_CTRL_REF_CURRENT(x)	(((x) & 0x7) << 1)
#define AD9122_DIE_TEMP_RANGE_CTRL_CAP_VALUE		(1 << 0)

/* AD9122_REG_SED_CTRL definitions */
#define AD9122_SED_CTRL_SED_COMPARE_EN			(1 << 7)
#define AD9122_SED_CTRL_SAMPLE_ERR_DETECTED		(1 << 5)
#define AD9122_SED_CTRL_AUTOCLEAR_EN			(1 << 3)
#define AD9122_SED_CTRL_COMPARE_FAIL			(1 << 1)
#define AD9122_SED_CTRL_COMPARE_PASS			(1 << 0)

/* Values of AD9122_REG_REVISION */
#define AD9122_DIE_REV_1				0x1
#define AD9122_DIE_REV_2				0x3

#define CHIPID_AD9122 0x8

#define AD9122_HB23_INTERP(x)			(((x) << 1) | ((x) << 4))
#define AD9122_HB1_INTERP(x)			((x) << 1)

#define AD9122_MAX_DAC_RATE			1230000000UL

#endif /* IIO_FREQUENCY_AD9122_H_ */
