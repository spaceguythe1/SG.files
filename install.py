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
    os.chdir("/")
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
    os.system(f"mkdir /home/{userwsudo}/.config")
    print("created your user!")
    time.sleep(0.1)

    print("downloading de && utilities")
    os.system("pacman -S xfce4 cava fastfetch firefox vlc kate sddm")
#  os.system(f"su {userwsudo} && pacman -S --needed git base-devel && git clone https://aur.archlinux.org/yay.git && cd yay && makepkg -si && exit")


    # Configure xfce and fastfetch
    # /usr/share/backgrounds/xfce/xfce-teal.jpg
    os.system("rm -f /usr/share/backgrounds/xfce/*")
    os.system("mv /root/archerthefact/wall.png /usr/share/backgrounds/xfce/xfce.teal.jpg")

    # fastfetch
    os.system(f"mkdir /home/{userwsudo}/.config/fastfetch && mv /root/archerthefact/ffconfig/* /home/{userwsudo}/.config/fastfetch/")
    os.system(f"echo fastfetch --logo-color-1 white --logo-color-2 red --color red >> /home/{userwsudo}/.bashrc")


    # kitty
    os.system("pacman -S kitty")
    os.system(f"mkdir /home/{userwsudo}/.config/kitty && mv /root/archerthefact/kitty.conf /home/{userwsudo}/.config/kitty/")


    # Installing tarm! (hopeless plug)
    # print("Installing utils by me...")
    # time.sleep(0.1)
    # os.system("rm -rf ~/tarm /usr/local/bin/tarm && git clone https://github.com/spaceguythe1/tarm.git && mv ~/tarm/tarm /usr/local/bin && chmod +x /usr/local/bin/tarm && rm -rf ~/tarm")
    # os.system("chmod +x /usr/local/bin/tarm")
    # os.system("rm -rf ~/tarm")

if(startchec == "y"):
    os.system("systemctl enable sddm.service")
    os.system(f"chown -R {userwsudo}:{userwsudo} /home/{userwsudo}")
    time.sleep(0.05)
    print()
    print()
    print("Installation finished!")
    time.sleep(0.5)
    print("its reccommended to reboot right after install.")
else:
    print()
    print("Quitting...")
