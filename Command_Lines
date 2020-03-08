# Instruction on how to create an Linux image at terminal
# On Apple computer, you need to confirm they are unmounted first

diskutil list
# This will show you all the disk/usb drive

# Unmount your usb drive
sudo diskutil unmountDisk /dev/disk3

# To Copy The Linux image file
sudo dd if=~/Downloads/archlinux-2020.03.01-x86_64.iso of=/dev/disk3 bs=1m

# Press control-t to see progress
# Output:
# load: 1.60  cmd: dd 1822 uninterruptible 0.00u 1.81s
# 94+0 records in
# 93+0 records out
# 97517568 bytes transferred in 119.453178 secs (816366 bytes/sec)
