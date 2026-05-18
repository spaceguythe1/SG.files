import time
import os
print("WARNING")
print("the following script is ment to ONLY be run on a fresh install of arch")
print("(aside from python, git and a valid internet connection).")
print("running the script on a device that dosent meet these conditions could destroy important files.")
time.sleep(0.25)

print()
print("Do you acknowledge this and want to continue installation? (y/n)")
startchec = input()
if(startchec == "y"):
    print("starting install...")
    time.sleep(0.05)
    os.system("pacman -S sudo")
    os.system('echo "%wheel ALL=(ALL:ALL) ALL" | sudo tee /etc/sudoers.d/wheel')
    time.sleep(0.1)

    print("what should your user be called? (will have sudo)")
    userwsudo = input()
    os.system(f"useradd -m {userwsudo}")
    os.system(f"usermod -aG wheel {userwsudo}")
    os.system(f"passwd {userwsudo}")
    time.sleep(0.1)
    print("created your user!")
    time.sleep(0.1)

    print("downloading de && utilities")
    os.system("pacman -S xfce4 cava fastfetch firefox vlc kate sddm")
    os.system(f"su {userwsudo} && pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si && exit")

