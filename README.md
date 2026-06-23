# 🚀 Linux Bluetooth Installer

A lightweight, automated Python utility designed to instantly restore, configure, and boot the Bluetooth stack on Linux distributions. It simplifies system maintenance by automatically scrubbing kernel-level driver blocks, installing the core `BlueZ` tools, fetching hardware-specific Realtek microcode (vital for adapters like the TP-Link UB500), and cleanly initializing the daemon through service wrappers.

Perfect for developers, sysadmins, and users maintaining minimal or optimized Linux desktop configurations (such as Openbox/Runit layers) who want a clean, zero-bloat hardware activation script.

---

## ✨ Features

- **Automated Kernel Cleanup:** Scans `/etc/modprobe.d/` and instantly unblocks modules by purging restrictive `blacklist-bluetooth.conf` profiles.
- **Hardware-Ready Firmware Integration:** Directly pulls essential `firmware-realtek` rules to eliminate initialization loops for popular chipsets.
- **Service Agnostic Architecture:** Configured to invoke system service handlers safely (`service bluetooth start`), ensuring stability even across legacy and hybrid init architectures.
- **Zero Heavy Dependencies:** Written entirely in pure Python utilizing native system pipelines to protect precious resource footprints.

---

## 📦 Requirements

- **OS:** Debian / Devuan / antiX (with `non-free-firmware` active in your apt `sources.list`)
- **Python:** Python 3.x stable build environment
- **Privileges:** `sudo` administrative execution access

---

## 🚀 Installation & Usage
```bash
git clone https://github.com/maybepain/bluetooth-installer-for-linux
cd bluetooth-installer-for-linux
chmod +x bt-installer.py
python3 bt-installer.py



