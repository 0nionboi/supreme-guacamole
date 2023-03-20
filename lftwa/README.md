# Linux for the Windows Administrator
## Written by Phoenix Fritch, with contributions from the community via Github Copilot
## Last updated on March 20th, 2023

### Introduction
Linux for the Windows Administrator is written for Windows Administrators with little-to-no linux experience.  Consider this a quick-and-dirty cheatsheet to help keep those pesky linux servers running.

GNU/Linux can be beautifully simple, or overwhelmingly complex.  This guide focuses on keeping it simple.  Once you get your feet wet, I highly recommend finding a good linux book or course and diving in.  Use this cheatsheet to help you keep your linux servers running in the meantime.

### Table of Contents
- [Navigating The Linux Filesystem](#navigating-the-linux-filesystem)
- [SSH](#ssh)
- [top](#top)
- [cron](#cron)
- [services](#services)
- [Useful Utilities and Tools](#useful-utilities-and-tools)
	- [cockpit](#cockpit)
	- [htop, btop, glances](#htop-btop-glances)
		- [htop](#htop)
		- [btop](#btop)
		- [glances](#glances)
		- [top](#top)
	- [ncdu](#ncdu)

### Change Log
- v0.2 - March 20th, 2023
	- Updated the Useful Utilites and Tools section
	- Created Table of Contents
- v0.1 - August 29th, 2022
	- Creation of Linux for the Windows Administrator.
	- Created Navigating the Linux Filesystem section
	- Created SSH section
	- Created Useful Utilites and Tools section
		- Added cockpit
		- Added htop, btop, glances
		- Added ncdu
	- Created top section
	- Created cron section
	- Created services section

### Navigating The Linux Filesystem
The Linux filesystem is organized into a hierarchy of directories.  The root directory is the top of the hierarchy.  All other directories are subdirectories of the root directory.  The root directory is represented by a single forward slash (/).  The root directory is the parent of all other directories.


### SSH
TO DO: write documentation.

### top
top is a command-line utility for monitoring the status of a Linux system.  It is a ncurses-based application, and requires no special terminal support.  It runs on Linux, FreeBSD, OpenBSD, NetBSD, Solaris, and macOS.
top is most useful for determining what is eating up RAM or CPU usage.  It is included in most Linux distributions, and is installed by default on Fedora, RHEL, and CentOS.
#### Usage
##### Starting top
To start top, type the following command:
```
top
```
###### Sample
```
Tasks: 175 total,   2 running, 173 sleeping,   0 stopped,   0 zombie
%Cpu(s):  2.6 us, 10.5 sy,  0.0 ni, 86.8 id,  0.0 wa,  0.0 hi,  0.0 si,  0.0 st
MiB Mem :   3901.1 total,    905.7 free,   1352.9 used,   1642.6 buff/cache
MiB Swap:   3901.0 total,   3814.0 free,     87.0 used.   2227.8 avail Mem 

    PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND                           
 137341 phoenix   20   0   11828   4024   3256 R   5.9   0.1   0:00.03 top                               
      1 root      20   0  176676  12832   7568 S   0.0   0.3   0:02.62 systemd                           
      2 root      20   0       0      0      0 S   0.0   0.0   0:00.13 kthreadd                          
      3 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_gp                            
      4 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 rcu_par_gp                        
      5 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 slub_flushwq                      
      6 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 netns                             
      8 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 kworker/0:0H-events_highpri       
     10 root       0 -20       0      0      0 I   0.0   0.0   0:00.00 mm_percpu_wq                      
     12 root      20   0       0      0      0 I   0.0   0.0   0:00.00 rcu_tasks_kthread                 
     13 root      20   0       0      0      0 I   0.0   0.0   0:00.00 rcu_tasks_rude_kthread            
```
##### Exiting top
To exit top, press the q key.

For other tools that monitor system resources, see the Useful Utilities and Tools section.

### cron
TO DO: write documentation

### services
TO DO: write documentation

### Useful Utilities and Tools
This section includes tools that I have found useful for Linux Administration.
#### cockpit
Useful for managing linux servers from a web browser.  Cockpit is a web-based graphical interface for servers.  It is easy to install and use.  Cockpit is available on most Linux distributions, and is included in Fedora, RHEL, and CentOS.
#### htop, btop, glances
Various tools for monitoring system resources.  I prefer htop, but btop and glances are also good options.
##### htop
htop is a text-mode process viewer for Unix systems.  It aims to be a better 'top'.  htop is an interactive process viewer.  It allows you to scroll through a list of processes, and view detailed information about individual processes.  htop is a ncurses-based application, and requires no special terminal support.  It runs on Linux, FreeBSD, OpenBSD, NetBSD, Solaris, and macOS.
##### btop
btop is a cross-platform resource monitor.  It shows usage and stats for processor, memory, disks, network and processes.  It is a ncurses based application, and requires no special terminal support.  It runs on Linux, FreeBSD, OpenBSD, NetBSD, Solaris, and macOS.
##### glances
Glances is a cross-platform system monitoring tool written in Python.  It aims to present a large amount of monitoring information through a curses or Web based interface.  It is a ncurses based application, and requires no special terminal support.  It runs on Linux, FreeBSD, OpenBSD, NetBSD, Solaris, and macOS.
#### ncdu
ncdu is a disk usage analyzer with an ncurses interface.  It is designed to find space hogs on a remote server where you don't have an entire graphical setup available.  It is a ncurses based application, and requires no special terminal support.  It runs on Linux, FreeBSD, OpenBSD, NetBSD, Solaris, and macOS.
It is recommended to install ncdu during system setup.  If the hard drive is already full, you will need to find something to delete BEFORE you can install and run ncdu.