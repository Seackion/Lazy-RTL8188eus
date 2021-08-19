import os , subprocess
from tqdm import tqdm  , trange
import time


if os.geteuid() != 0:
    print('  Please run as root')
    exit()
   
subprocess.run('clear',shell=True)



print('''
 _                      ______ _   _ _____  __   _____  _____                
| |                     | ___ \ | | |  _  |/  | |  _  ||  _  |               
| |     __ _ _____   _  | |_/ / |_| |\ V / `| |  \ V /  \ V /  ___ _   _ ___ 
| |    / _` |_  / | | | |    /| __| |/ _ \  | |  / _ \  / _ \ / _ \ | | / __|
| |___| (_| |/ /| |_| | | |\ \| |_| | |_| |_| |_| |_| || |_| |  __/ |_| \__ \
\_____/\__,_/___|\__, | \_| \_|\__|_\_____/\___/\_____/\_____/\___|\__,_|___/
                  __/ |                                                      
                 |___/                                                       
        >>>>>>>>>>>>Creadted By:@Seckion<<<<<<<<<<<<<
''')

try: 
    input('''   
    Please Plug in our Adaptar And Press ENTER To Continue  ''')
except SyntaxError:
    pass

print('''

                        Adding New Repositories

    ''')
subprocess.run('echo "deb http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee /etc/apt/sources.list',shell=True)
subprocess.run('echo "deb http://http.kali.org/kali kali-last-snapshot main non-free contrib" | sudo tee /etc/apt/sources.list',shell=True)
subprocess.run('echo "deb http://http.kali.org/kali kali-experimental main non-free contrib" | sudo tee -a /etc/apt/sources.list',shell=True)
subprocess.run('echo "deb-src http://http.kali.org/kali kali-rolling main non-free contrib" | sudo tee -a /etc/apt/sources.list',shell=True)
    # 
for i in trange(10):
    time.sleep(0.3)

print('''

                        Updating Apt

''')
subprocess.run('apt-get update ',shell=True)
    # 
for i in trange(10):
    time.sleep(0.3)

print('''

                        Upgrading Packages

''')
subprocess.run('apt upgrade -y',shell=True)
    # 
for i in trange(10):
    time.sleep(0.3)    
print('''

                        Installing Dependences

''')
subprocess.run("apt-get --assume-yes install bc  build-essential    linux-headers-$(uname -r) dkms",shell=True)
    # 
for i in trange(10):
    time.sleep(0.3)


print('''

                        Installing  rtl8188eus 

''')

subprocess.run("git clone https://github.com/aircrack-ng/rtl8188eus.git ",shell=True)
    #    
subprocess.run('touch ~/.hushlogin ',shell=True)
    # 
subprocess.run(' echo "blacklist r8188eu" to  "/etc/modprobe.d/realtek.conf" ',shell=True)
    # 
    
    # 

print('''


    ''')
subprocess.call('make',cwd='rtl8188eus',shell=True)
    # 
subprocess.call('make install',cwd='rtl8188eus',shell=True)
    # 
for i in trange(10):
    time.sleep(0.3)
    
print("""*Note: If monitor mode wont't work on the adapter then run :

      sudo rmmod r8188eu.ko && sudo modprobe 8188eu

           And replugin your adapter
 """)    


print('''
            _____________________________________________________

              The Drivers  has Successfully Installed!
            ______________________________________________________

''')

subprocess.run(' sudo rmmod r8188eu.ko',shell=True)
subprocess.run(' sudo modprobe 8188eu',shell=True)

