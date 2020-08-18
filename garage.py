#!/bin/python
from race import save_car

# Garage - Car manager

# Load car

def load_car(fp):

	# Return dictionary of car info
	# Generalizing to be used for races too

	car = {
	"name":"",
	"fin_min":0,
	"fin":0,
	"fin_max":0,
	"coo_min":0,
	"coo":0,
	"coo_max":0,
	"ste_min":0,
	"ste":0,
	"ste_max":0,
	"thr_min":0,
	"thr":0,
	"thr_max":0,
	"sen_min":0,
	"sen":0,
	"sen_max":0,
	"fcl_min":0,
	"fcl":0,
	"fcl_max":0,
	"afb_min":0,
	"afb":0,
	"afb_max":0,
	"dia_min":0,
	"dia":0,
	"dia_max":0,	
	"cha":"",
	"rea":"",
	"fty":"",
	"fra":0,
	"coa":0,
	"lap":0,
	"pos":0,
	"dmg":0,
	"pts":0,
	"pp_fuel":0,
	"pp_dam":0,
	"degra":0,
	"fuel":max_fuel(),
	"wreck":0,
	"locale":"Starting Grid",
	"tel_lap_splits":[],
	"tel_current_lap":0,
	"tel_pit_time":[],
	"tel_moves":[],
	"tel_ebrakes":0,
	"tel_cutoff":0,
	"tel_steer":0,
	"tel_fuel_thr":0,
	"tel_dam_thr":0,
	"time":0,
	"wreck-note":"",
	"pit_flag":0,
	"ball":random.randint(1,1000),
	"file":c_fp
	}

	c_fh = open(fp,"r")

	for l in c_fh:
		if l.startswith("#"):
			continue
		if l.startswith("$"):
			# Check what variable
			this_l = l.split(":")
			# print(this_l)
			if this_l[1] == "name":
				car['name'] = this_l[2].strip("\n")
			elif this_l[1] == "points":
				car['pts'] = int(this_l[2])
			elif this_l[1] == "thr":
				car['thr_min'] = int(this_l[2])
				car['thr'] = int(this_l[3])
				car['thr_max'] = int(this_l[4])
			elif this_l[1] == "fin":
				car['fin_min'] = int(this_l[2])
				car['fin'] = int(this_l[3])
				car['fin_max'] = int(this_l[4])
			elif this_l[1] == "sen":
				car['sen_min'] = int(this_l[2])
				car['sen'] = int(this_l[3])
				car['sen_max'] = int(this_l[4])
			elif this_l[1] == "fcl":
				car['fcl_min'] = int(this_l[2])
				car['fcl'] = int(this_l[3])
				car['fcl_max'] = int(this_l[4])
			elif this_l[1] == "ste":
				car['ste_min'] = int(this_l[2])
				car['ste'] = int(this_l[3])
				car['ste_max'] = int(this_l[4])
			elif this_l[1] == "coo":
				car['coo_min'] = int(this_l[2])
				car['coo'] = int(this_l[3])
				car['coo_max'] = int(this_l[4])
			elif this_l[1] == "afb":
				car['afb_min'] = int(this_l[2])
				car['afb'] = int(this_l[3])
				car['afb_max'] = int(this_l[4])
			elif this_l[1] == "dia":
				car['dia_min'] = int(this_l[2])
				car['dia'] = int(this_l[3])
				car['dia_max'] = int(this_l[4])
			elif this_l[1] == "rea":
				car['rea'] = this_l[2].strip("\n")
			elif this_l[1] == "fty":
				car['fty'] = this_l[2].strip("\n")
			elif this_l[1] == "cha":
				car['cha'] = this_l[2].strip("\n")
			elif this_l[1] == "pp_fuel":
				car['pp_fuel'] = int(this_l[2])
			elif this_l[1] == "pp_dam":
				car['pp_dam'] = int(this_l[2])

	# Car chassis affects fragility and coasting
	if car['cha'] == "streamlined":
		car['fra'] = 750 - car['thr'] - car['fin'] - car['sen'] - car['fcl'] - car['ste'] - car['coo'] - car['afb'] - car['dia']
		if car['rea'] == "fission":
			car['coa'] = 150
		else:
			car['coa'] = 75
	elif car['cha'] == "cubic":
		car['fra'] = 850 - car['thr'] - car['fin'] - car['sen'] - car['fcl'] - car['ste'] - car['coo'] - car['afb'] - car['dia']
		if car['rea'] == "fission":
			car['coa'] = 50
		else:
			car['coa'] = 25
	else:
		# Assume neutral
		car['fra'] = 800 - car['thr'] - car['fin'] - car['sen'] - car['fcl'] - car['ste'] - car['coo'] - car['afb'] - car['dia']
		if car['rea'] == "fission":
			car['coa'] = 100
		else:
			car['coa'] = 50



	return car

def new_car():

	in_tour = input("Tour Name: ")
	in_fname = input("File Name: ")

	file_path = "./"+in_tour+"./"+in_fname+".car"

	in_name = input("Craft name: ")

	print("Chassis Types")
	print("s - streamlined")
	print("n - neutral")
	print("c - cubic")
	in_cha = input("Craft chassis: ")

	if in_cha == s:
		in_cha = "streamlined"
	elif in_cha == n:
		in_cha = "neutral"
	elif in_cha == c:
		in_cha = "cubic"
	else:
		in_cha = "neutral"

	print("Reactor Types")
	print("i - fission")
	print("u - fusion")
	in_rea = input("Craft reactor: ")

	if in_rea == i:
		in_rea = "fission"
	elif in_rea == u:
		in_rea = "fusion"
	else:
		in_rea = "fission"


	print("Fuel Types")
	print("p - plutonium")
	print("u - uranium")
	print("r - radium")
	in_fue = input("Fuel Type: ")

	if in_fue == p:
		in_fue = "plutonium"
	elif in_fue == u:
		in_fue = "uranium"
	elif in_fue == r:
		in_fue = "radium"
	else:
		in_fue = "uranium"

	# Set Stats

	print("Tune Components: ")
	int(in_thr) = input("Thrusters: ")
	int(in_ste) = input("Steering: ")
	int(in_coo) = input("Coolant: ")
	int(in_fin) = input("Fins: ")
	int(in_sen) = input("Sensors: ")
	int(in_fcl) = input("Fuel Cell: ")
	int(in_afb) = input("Afterburners: ")
	int(in_dia) = input("Diagnostics: ")

	# Calculate fragility and coasting: so the constructor knows what they are getting into:
	# Car chassis affects fragility and coasting
	if in_cha == "streamlined":
		fragility = 750 - in_thr - in_fin - in_sen - in_fcl - in_ste - in_coo - in_afb - in_dia
		if in_rea == "fission":
			coasting = 150
		else:
			coasting = 75
	elif in_cha == "cubic":
		fragility = 850 - in_thr - in_fin - in_sen - in_fcl - in_ste - in_coo - in_afb - in_dia
		if in_rea == "fission":
			coasting = 50
		else:
			coasting = 25
	else:
		# Assume neutral
		fragility = 800 - in_thr - in_fin - in_sen - in_fcl - in_ste - in_coo - in_afb - in_dia
		if in_rea == "fission":
			coasting = 100
		else:
			coasting = 50

	print("\nFragility: "+str(fragility))
	print("Coasting: "+str(coasting))

	print("\nRace Strategy: ")

	pp_fuel = input("Pit if you have fuel below: ")
	pp_dam = input("Pit if you have more damage than this: ")

	# Make array
	this_car = [file_path,in_name,in_cha,in_rea,in_fue,1,in_thr,110,1,in_ste,110,1,in_coo,110,1,in_fin,110,1,in_sen,110,1,in_fcl,110,1,in_afb,110,1,in_dia,110,pp_fuel,pp_dam]

	save_car(this_car)
	return

def mod_car():
	pass

def save_car(car_array,c_fh):

	c_fh = open(car_array[0],"w")
	c_fh.write("# Car Template\n")
	c_fh.write("\n")
	c_fh.write("############################################\n")
	c_fh.write("#  DO NOT EDIT THE BELOW SECTION MANUALLY  #\n")
	c_fh.write("#           EDIT USING GARAGE.PY           #\n")
	c_fh.write("############################################\n")
	c_fh.write("$:name:"+car_array[1]+"\n")
	c_fh.write("############################################\n")
	c_fh.write("#                TOUR INFO                 #\n")
	c_fh.write("############################################\n")
	c_fh.write("$:points:0\n")
	c_fh.write("############################################\n")
	c_fh.write("#                 CAR INFO                 #\n")
	c_fh.write("############################################\n")
	c_fh.write("$:cha:"+car_array[2]+"\n")
	c_fh.write("$:rea:"+car_array[3]+"\n")
	c_fh.write("$:fty:"+car_array[4]+"\n")
	c_fh.write("$:thr:"+str(car_array[5])+":"+str(car_array[6])+":"+str(car_array[7])+"\n")
	c_fh.write("$:ste:"+str(car_array[8])+":"+str(car_array[9])+":"+str(car_array[10])+"\n")
	c_fh.write("$:coo:"+str(car_array[11])+":"+str(car_array[12])+":"+str(car_array[13])+"\n")
	c_fh.write("$:fin:"+str(car_array[14])+":"+str(car_array[15])+":"+str(car_array[16])+"\n")
	c_fh.write("$:sen:"+str(car_array[17])+":"+str(car_array[18])+":"+str(car_array[19])+"\n")
	c_fh.write("$:fcl:"+str(car_array[20])+":"+str(car_array[21])+":"+str(car_array[22])+"\n")
	c_fh.write("$:afb:"+str(car_array[23])+":"+str(car_array[24])+":"+str(car_array[25])+"\n")
	c_fh.write("$:dia:"+str(car_array[26])+":"+str(car_array[27])+":"+str(car_array[28])+"\n")
	c_fh.write("############################################\n")
	c_fh.write("#               STRATEGY INFO              #\n")
	c_fh.write("############################################\n")
	c_fh.write("$:pp_fuel:"+str(pp_fuel)+"\n")
	c_fh.write("$:pp_dam:"+str(pp_dam)+"\n")
	c_fh.write("############################################\n")
	c_fh.write("#            LAST RACE TELEMETRY           #\n")
	c_fh.write("############################################\n")
	# Gather telemetry

	c_fh.close()

	return

if __name__ == "__main__":
	print("Hotrod Garage")
	option_1 = "x"

	while (option_1 != "q"):
		print("n - make a new craft")
		print("l - load an exsisting craft")
		print("q - quit")
		option_1 = input("What would you like to do? ")

		if option_1 == "n":
			new_car()
		elif option_1 == "l":
			mod_car()
		elif option_1 == "q":
			quit()
		else:
			print("Error! - Invalid Entry")

