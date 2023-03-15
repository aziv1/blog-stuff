import pymem
import pymem.process
import keyboard
import time

m_bSpotted = 0x93D
dwEntityList = 0x4DFFEF4

def main():
	print("Searching for process 'csgo.exe' \n")
	pm = pymem.Pymem("csgo.exe")
	print("csgo successfully linked with pymem")
	client = pymem.process.module_from_name(pm.process_handle, "client.dll").lpBaseOfDll
	print("Hack connected with client.dll")
	try:
		print("Hack Initiated")
		while True:			
			if keyboard.is_pressed("*"):
				print("Closing Hack")
				exit(0)			
			for i in range(1, 32):
				entity = pm.read_int(client + dwEntityList + i * 0x10)
				if entity:
					pm.write_uchar(entity + m_bSpotted, 1)
	except Exception as e:
		print(e)

if __name__ == '__main__':
	main()