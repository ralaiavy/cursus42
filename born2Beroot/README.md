*This project has been created as part of the 42 curriculum by fralaiav.*

# Born2beRoot

## Description

Born2beRoot is a system administration project from the 42 curriculum. The goal is to set up a secure Linux server inside a virtual machine, following strict rules regarding partitioning, security policies, user management, and system monitoring.

By the end of this project, you will have a fully configured server with:
- Encrypted LVM partitions
- A hardened SSH configuration
- A strict password and sudo policy
- A firewall allowing only the necessary ports
- A monitoring script broadcasting system information every 10 minutes

---

## Instructions

### Requirements

- [VirtualBox](https://www.virtualbox.org/)
- A Debian ISO (latest stable release)

### Setup Overview

1. **Create the virtual machine** in VirtualBox with the Debian ISO.
2. **Partition the disk** with at least 2 encrypted LVM partitions (no graphical interface).
3. **Configure SSH** on port 4242, with root login disabled.
4. **Set up the firewall** UFW for Debian, keeping only port 4242 open.
5. **Apply the password policy** via `/etc/login.defs` and `libpam-pwquality`.
6. **Configure sudo** with strict rules (3 attempts max, TTY required, logging to `/var/log/sudo/`).
7. **Create users and groups**: a user named `fralaiav` belonging to `user42` and `sudo`.
8. **Deploy `monitoring.sh`** and schedule it with `cron` to run every 10 minutes at startup.

### Submission

Only two files are required at the root of your Git repository:
- `README.md`
- `signature.txt` — containing the SHA1 signature of your virtual machine's disk file

To generate the signature:
```bash
# Linux
sha1sum ~/VirtualBox\ VMs/fralaiav42/fralaiav42.vdi
```

> ⚠️ Do NOT include the virtual machine itself in your Git repository.

---

## Project Description

### Operating System Choice: Debian

**Debian** was chosen over Rocky Linux for the following reasons:

| | Debian | Rocky Linux |
|---|---|---|
| **Target audience** | General purpose, beginners friendly | Enterprise / RHEL-compatible |
| **Package manager** | `apt` / `aptitude` | `dnf` / `yum` |
| **Security module** | AppArmor | SELinux |
| **Firewall** | UFW | firewalld |
| **Complexity** | Lower — ideal for learning | Higher — SELinux is complex to configure |
| **Community** | Very large, excellent documentation | Large, enterprise-focused |
| **Release cycle** | Stable, conservative | Follows RHEL releases |

**Advantages of Debian:** easier to configure for beginners, huge community support, stable package management, and excellent documentation.

**Disadvantages of Debian:** packages can be older than cutting-edge distros; less common in enterprise environments than RHEL-based systems.

---

### Key Design Choices

#### Partitioning

At least 2 encrypted LVM partitions were created:
- `/boot` — unencrypted, required for bootloader
- An encrypted partition containing LVM logical volumes: `/` (root), `[SWAP]`, `/home`

LVM (Logical Volume Manager) was used to allow flexible resizing of partitions and to sit on top of the LUKS-encrypted physical partition.

#### Security Policies

**Password policy** (`/etc/login.defs` + `libpam-pwquality`):
- Expires every 30 days (`PASS_MAX_DAYS 30`)
- Minimum 2 days between changes (`PASS_MIN_DAYS 2`)
- Warning 7 days before expiry (`PASS_WARN_AGE 7`)
- Minimum 10 characters, must include uppercase, lowercase, and digit
- No more than 3 consecutive identical characters
- Cannot contain the username
- Must differ from the previous password by at least 7 characters

**Sudo policy** (`/etc/sudoers.d/`):
- Max 3 incorrect password attempts
- Custom error message on wrong password
- All inputs/outputs logged to `/var/log/sudo/`
- TTY mode enabled (`requiretty`)
- Restricted secure paths

#### User Management

- `root` account: SSH login disabled, strong password enforced
- `fralaiav`: member of `user42` and `sudo` groups

#### Services Installed

| Service | Purpose |
|---|---|
| OpenSSH | Remote access on port 4242 |
| UFW | Firewall, only port 4242 open |
| AppArmor | Mandatory access control |
| cron | Scheduled execution of `monitoring.sh` |

---

### Technology Comparisons

#### AppArmor vs SELinux

| | AppArmor | SELinux |
|---|---|---|
| **Model** | Path-based (profiles per application) | Label-based (every object has a security context) |
| **Complexity** | Easier to configure and understand | More powerful but significantly more complex |
| **Default on** | Debian, Ubuntu | Fedora, RHEL, Rocky Linux |
| **Profile format** | Human-readable text files | Binary policies |
| **Use case** | Good for most server setups | Required for high-security/enterprise environments |

AppArmor was used in this project (Debian default). It restricts programs using profiles, limiting what files and capabilities they can access.

#### UFW vs firewalld

| | UFW | firewalld |
|---|---|---|
| **Stands for** | Uncomplicated Firewall | — |
| **Backend** | iptables / nftables | nftables / iptables |
| **Default on** | Debian / Ubuntu | Fedora, RHEL, Rocky |
| **Configuration** | Simple command-line interface | Zones and services concept |
| **Complexity** | Very simple, beginner-friendly | More flexible but more complex |

UFW was used in this project. Port 4242 is the only open port:
```bash
sudo ufw allow 4242
sudo ufw enable
sudo ufw status
```

#### VirtualBox vs UTM

| | VirtualBox | UTM |
|---|---|---|
| **Platform** | Windows, Linux, macOS (Intel) | macOS (Intel + Apple Silicon) |
| **Apple Silicon** | No native support | Full native support via QEMU |
| **License** | Free (GPLv2) | Free (open source) |
| **Performance** | Good on x86 | Excellent on Apple Silicon (native ARM) |
| **Ease of use** | Very user-friendly, extensive docs | Clean UI, well adapted to macOS |

VirtualBox was used for this project (x86 machine). UTM is the recommended alternative for Apple Silicon (M1/M2/M3) users.

---

### monitoring.sh

The script runs every 10 minutes via `cron` and broadcasts system information to all terminals using `wall`. It displays:

- OS architecture and kernel version
- Number of physical and virtual CPUs
- RAM usage (used/total + percentage)
- Disk usage (used/total + percentage)
- CPU load percentage
- Date and time of last reboot
- Whether LVM is active
- Number of active TCP connections
- Number of logged-in users
- Server IPv4 and MAC address
- Number of `sudo` commands executed

To interrupt it without modifying the script:
```bash
sudo crontab -e
# Comment out or remove the cron line
```

---

## Resources

### Documentation

- [Debian Official Documentation](https://www.debian.org/doc/)
- [Debian Installation Guide](https://www.debian.org/releases/stable/installmanual)
- [LVM Administrator's Guide](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_logical_volumes/index)
- [LUKS / dm-crypt on Debian](https://wiki.debian.org/Cryptsetup)
- [AppArmor Wiki](https://wiki.debian.org/AppArmor)
- [UFW Documentation](https://help.ubuntu.com/community/UFW)
- [sudoers manual (`man sudoers`)](https://www.sudo.ws/docs/man/sudoers.man/)
- [pam_pwquality](https://linux.die.net/man/8/pam_pwquality)
- [cron manual (`man cron`)](https://man7.org/linux/man-pages/man8/cron.8.html)
- [wall command](https://man7.org/linux/man-pages/man1/wall.1.html)

### Articles & Tutorials

- [VirtualBox User Manual](https://www.virtualbox.org/manual/)
- [DigitalOcean — How To Set Up a Firewall with UFW on Debian](https://www.digitalocean.com/community/tutorials/how-to-set-up-a-firewall-with-ufw-on-debian-10)
- [DigitalOcean — How To Edit the Sudoers File](https://www.digitalocean.com/community/tutorials/how-to-edit-the-sudoers-file)
- [Arch Wiki — LVM](https://wiki.archlinux.org/title/LVM)
- [Arch Wiki — dm-crypt](https://wiki.archlinux.org/title/dm-crypt)

### AI Usage

AI was used for the following tasks:
- **Understanding concepts**: clarifying the differences between AppArmor vs SELinux, UFW vs firewalld, apt vs aptitude, and LVM concepts before implementing them.
- **Debugging**: asking targeted questions (not for direct answers) when commands produced unexpected results.

All implementation, configuration, and technical decisions were made independently after studying the relevant documentation and through peer-learning exchanges.