import subprocess as sb
import time

def packageinstaller():
	sb.run('sudo apt install bluetooth bluez bluez-tools -y',shell=True)
	sb.run('sudo apt install firmware-realtek -y',shell=True)
	sb.run('sudo apt install blueman -y',shell=True)

def service_starter():
	service_manager = sb.run(["ps", "-p", "1", "-o", "comm="], capture_output=True, text=True)
	service_manager = service_manager.stdout.strip()
	try:
		if service_manager=='systemd':
			sb.run('sudo systemctl enable bluetooth.service',shell=True)
			sb.run('sudo systemctl start bluetooth.service',shell=True)
		elif service_manager=="init":
			sb.run('sudo service bluetooth start',shell=True)
	finally:
		print()
		print()
		print('Bluetooth Manager will appear on application menu')
		print('Bluetooth Manager will appear on application menu')
		print('Bluetooth Manager will appear on application menu')
		print()
		print('device restart is recommented')
		while True:
			choice=input('Do you want to restart mechine( Y OR N )??').lower()
			if choice=='y':	
				for i in range(1,4):
					print(f"Device will restart in {i} seconds")
					time.sleep(1)
					if i==3:
						sb.run('sudo reboot',shell=True)
					else:
						pass
			if choice=='n':
				break
			else:
				print('invalid choice')

packageinstaller()
service_starter()
		
			
		



	
