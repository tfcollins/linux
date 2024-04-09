Building Kernels
################

Building the ADI Linux kernel must be done on a Linux machine, Linux VM, or through `WSL <https://docs.microsoft.com/en-us/windows/wsl/about>`_ as Windows cannot support the kernel's filesystem by default. It will also require a supported compiler and a few utilities. For FPGA based platforms it is typically recommended to use the vendor tools for that platform, such as from AMD's SDK (or Vitis), Intel's SDK, or the standard ARM compilers from the Linaro project.

This version of the documentation is targeted at the |release_version_bold| release of the ADI prototyping platform and related tools. For other versions including **main** development branches, select the target release from the sidebar dropdown.

Installing Dependencies
-----------------------

First install the target compiler for your platform:

* `Xilinx/AMD FPGA <dd>`_
* `Intel FPGA <dd>`_
* `Raspberry PI <dd>`_

Install the additional tools:

.. tab:: Debian/Ubuntu

    .. code-block:: bash

      sudo apt-get install git build-essential fakeroot libncurses5-dev libssl-dev ccache
      sudo apt-get install dfu-util u-boot-tools device-tree-compiler libssl1.0-dev mtools
      sudo apt-get install bc python cpio zip unzip rsync file wget

.. tab:: RHEL/Fedora

    .. code-block:: bash

      sudo dnf install git gcc flex make bison openssl-devel elfutils-libelf-devel


Building Instructions
---------------------

First clone the kernel source and checkout the target branch:

.. code-block:: bash
  :substitutions:

  git clone -b |linux_branch| https://github.com/analogdevicesinc/linux.git


Next build for the desired target platform.

.. tab:: AMD Zynq

    Source tools

    .. code-block:: bash
      :substitutions:

      source /opt/Xilinx/Vivado/|vivado_version|/settings64.sh

    Configure environment

    .. code-block:: bash

      export ARCH=arm
      export CROSS_COMPILE="arm-linux-gnueabihf-"

    Configure and build the kernel

    .. code-block:: bash

      make zynq_xcomm_adv7511_defconfig
      make -j5 UIMAGE_LOADADDR=0x8000 uImage


.. tab:: AMD ZynqMP

    Source tools

    .. code-block:: bash
      :substitutions:

      source /opt/Xilinx/Vivado/|vivado_version|/settings64.sh

    Configure environment

    .. code-block:: bash

      export ARCH=arm64
      export CROSS_COMPILE="aarch64-linux-gnu-"

    Configure and build the kernel

    .. code-block:: bash

      make adi_zynqmp_defconfig
      make -j5 Image UIMAGE_LOADADDR=0x8000

.. tab:: AMD Microblaze

    Source tools

    .. code-block:: bash
      :substitutions:

      source /opt/Xilinx/Vivado/|vivado_version|/settings64.sh

    Configure environment

    .. code-block:: bash

      export ARCH=microblaze
      export CROSS_COMPILE="microblazeel-xilinx-linux-gnu-"

    Configure the kernel

    .. code-block:: bash

      make adi_mb_defconfig


    Get the root filesystem (rootfs)

    .. NOTE::
      The root file system or rootfs contains everything (besides the Linux kernel itself) needed to support a full Linux system. It contains all the (user) applications, configurations, services, data, etc. Without the rootfs your Linux system cannot run. You can either just download the pre-build image or build it yourself. Instructions can be found here: `Building with buildroot <https://wiki.analog.com/resources/tools-software/linux-build/generic/buildroot>`_.

      rootfs.cpio.gz rootfs.cpio.gz must be placed in the root of your kernel source directory.

    .. code-block:: bash

      wget https://swdownloads.analog.com/cse/microblaze/rootfs/rootfs.cpio.gz

    Build the kernel and package simple image. This will require use of a specific target device tree file. For available targets provided with the kernel source, see the `arch/microblaze/boot/dts/` directory.

    .. code-block:: bash

      make -j5 simpleImage.<dts filename>

    This will generate a strip image file that can be used to boot the kernel and rootfs on the target platform located at **arch/microblaze/boot/simpleImage.<dts filename>.strip**.


    With the strip image and related bitstream file, the target platform can be flashed using the Xilinx SDK (XSDB) or other programming tools.

    .. tab:: Command-line Example

      .. code-block:: bash

        xsdb> connect
        xsdb> fpga -f system_top.bit
        xsdb> targets
          1  xcku040
             2  MicroBlaze Debug Module at USER2
                3  MicroBlaze #0 (Running)
        xsdb> targets 3
        xsdb> dow simpleImage.kcu105_fmcdaq2
        xsdb> con

    .. tab:: TCL Script Example
        
        .. code-block:: tcl
  
          connect
          fpga -f system_top.bit
          after 1000
          targets 3
          dow simpleImage.kcu105_fmcdaq2.strip
          after 1000
          con
          disconnect


.. tab:: Intel

    Source tools

    .. code-block:: bash
      :substitutions:

      source /opt/Xilinx/Vivado/|vivado_version|/settings64.sh

    Configure environment

    .. code-block:: bash

      export ARCH=arm
      export CROSS_COMPILE="arm-linux-gnueabi-"

    Configure and build the kernel

    .. code-block:: bash

      make make socfpga_adi_defconfig
      make -j5 zImage


Device Trees
------------

.. NOTE::
  This section does not apply to MicroBlaze platforms. As the devicetree is built into the kernel image already.


Once the kernel is built specific devicetrees can be built for the target platform. The devicetree is a data structure that describes the hardware components of a particular system. It is used by the kernel to configure the hardware and provide information to the kernel about the hardware layout.

Available target devicetrees can be found on this page.

With the target devicetree name, the devicetree can be built using the following command:

.. tab:: AMD Zynq/Intel

    .. code-block:: bash

      make <target devicetree filename with .dtb extension>

    Example:

    .. code-block:: bash

      make zynq-zc706-adv7511-ad9361-fmcomms2-3.dtb

.. tab:: AMD ZynqMP

    .. code-block:: bash

      make xilinx/<target devicetree filename with .dtb extension>

    Example:

    .. code-block:: bash

      make xilinx/zynqmp-zcu102-rev1.0-ad9361-fmcomms2-3.dtb