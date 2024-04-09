# Analog Devices Linux Kernel

ADI Linux is a variant of the Linux kernel that is use to support ADI drivers and platforms. This documentation is intended to provide information on how to build the kernel, how to use the drivers, and how to contribute to the project. It also provides guidance on the available userspace implementations supported by ADI, baremetal solutions, and tools used alongside the kernel drivers.

```{mermaid}
graph TB
    kernel[ADI Linux Kernel] --> kuiper[ADI Kuiper Linux]
    kernel --> buildroot[ADI Buildroot]
    kernel --> petalinux[meta-adi]

    kernel -.->|Derived|noOS[no-OS: Baremetal Solutions]

    subgraph Userspace Implementations
        kuiper
        buildroot
        petalinux
    end


```


::: {toctree}
guides/build
drivers_index
:::

# Indices and tables

-   `genindex`{.interpreted-text role="ref"}
-   `modindex`{.interpreted-text role="ref"}
-   `search`{.interpreted-text role="ref"}
