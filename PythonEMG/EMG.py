import signal, sys, time
from serial import Serial
from MyKeyboard import PressKey
import webbrowser

def endProgram(sig, frame): 
	# Funcao de tratamento de interrupcao Ctrl+C
	try:
		serial.close()
	except:
		pass
	sys.exit(0)

#=========================== MAIN ===========================#

if (len(sys.argv) < 2):
	print("Numero de argumentos invalidos. Chame a função assim: \n EMG.py <port> <speed>")
	sys.exit(-1)

serialPort = sys.argv[1].upper()

try:
	serialSpeed = sys.argv[2]
except:
	serialSpeed = 9600

try:
	serial = Serial(serialPort, serialSpeed)
except:
	print("Falhou em abrir a porta", serialPort, "na velocidade", serialSpeed)
	sys.exit(-1)

serial.reset_input_buffer()

#=========================== LOOP ===========================#

print("Acesse: 'chrome://dino/' e divirta-se!")
time.sleep(3)

while 1:

	msg = serial.readline()
	msg = str(msg).replace("b","")
	msg = str(msg).replace("'","")
	msg = str(msg).replace("\\n","")
	msg = str(msg).replace("\\r","")
	try:
		value =	int(msg)

		if (value > 10000):
			PressKey(SPACE)
			print("Pulou!")
	except:
		pass		