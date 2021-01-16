#!/bin/python

# Imports
import random
import time
from datetime import datetime
from operator import itemgetter 
from os import system, name, listdir
import sys
from prettytable import PrettyTable
from tabulate import tabulate

def max_fuel():
	# Returns the maximum fuel allowed 
	return 100

def title_splash():
	cs()
	print("                       / - \\   |------|  / /-\\ \\  ||\\  /||  |=====|   //====")
	print("                      / / \\ \\     ||     | | | |  ||  - ||     |     ||     ")
	print("                      | |=| |     ||     | | | |  ||    ||     |     ||     ")
	print("                      | | | |     ||     | | | |  ||    ||     |     ||     ")
	print("                      |_| |_|     ||     \\ \\-/ /  ||    ||  |=====|   \\\\====")
	print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
	print("                  |-| |-|  / /-\\ \\  |------|           ||---\\   / /-\\ \\  ||==\\\\ ")
	print("                  |-| |-|  | | | |     ||              ||    |  | | | |  ||   ||")
	print("                  |-|=|-|  | | | |     ||     =======  ||---/   | | | |  ||   ||")
	print("                  |-| |-|  | | | |     ||              ||   \\   | | | |  ||   ||")
	print("                  |-| |-|  \\ \\-/ /     ||              ||    |  \\ \\-/ /  ||==// ")
	print("=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*=*")
	print("|-| |-|  / /-\\ \\  ||   ||  ||=====  ||---\\    //====  ||---\\    / - \\   ||=====  |------|  //=====")
	print("|-| |-|  | | | |  ||   ||  ||       ||    |  ||       ||    |  / / \\ \\  ||          ||     ||     ")
	print("|-|=|-|  | | | |  ||   ||  ||===    ||---/   ||       ||---/   | |=| |  ||===       ||     \\\\===\\\\")
	print("|-| |-|  | | | |   \\\\ //   ||       ||   \\   ||       ||   \\   | | | |  ||          ||          ||")
	print("|-| |-|  \\ \\-/ /     -     ||=====  ||    |   \\\\====  ||    |  |_| |_|  ||          ||   =======//")
	print("============================================================================================      ")
	print("======================================================================================      ")
	junk = input("                                    Press Enter to start!\n                                     ")
	return

# Danger 
def danger_roll(car):
	# Takes a car in danger and returns a car with damage

	# Can be saved by a sensors roll
	if car['sen'] >= random.randint(1,120):
		return car

	dam_roll = random.randint(0,19)

	if dam_roll == 0:
		car['spun'] = True
		car['tel_spin_count'] = car['tel_spin_count']  + 1
	else:
		car['dmg'] = car['dmg']+dam_roll

		if car['dmg'] > car['fra']:
			car['wreck'] = True


	return car

def pit(car):
	# Repair car, refuel car, mark degragation and return new car

	repair_roll = car['dia'] - random.randint(1,100)
	total_repair = car['dmg'] - repair_roll
	if total_repair <= 0:
		# Fully repaired
		car['degra'] = car['degra'] + car['dmg']
		car['dmg'] = 0
	elif total_repair > car['dmg']:
		# No repair was done
		car['dmg'] = car['dmg']
	else:
		# Partial repair
		car['degra'] = car['degra'] + total_repair
		car['dmg'] = car['dmg'] - total_repair
	car['fuel'] = max_fuel()
	return car

def car_telementry(car,vm):
	# Needs a car, and a view mode (either h for human or f for file), for human readable, no actual return as it just prints out the lines, for file, returns an array of strings
	# In the uture 
	if vm == "h":
		print(car['name']+":")
		print("Data:")
		try:
			print("Slowest Lap:"+str(max(car['tel_lap_splits'])))
		except:
			print("Slowest Lap: NA")
		try:
			print("Average Lap:"+str((sum(car['tel_lap_splits'])/len(car['tel_lap_splits']))))
		except:
			print("Average Lap: NA")
		try:
			print("Fastest Lap:"+str(min(car['tel_lap_splits'])))
		except:
			print("Fastest Lap: NA")
		try:
			print("All Laps:"+str(car['tel_lap_splits']))
		except:
			print("All Laps: NA")
		try:
			print("Pitstops Taken:"+str(len(car['tel_pit_time'])))
		except:
			print("Pitstops Taken: NA")
		try:
			print("Slowest Pitstop:"+str(max(car['tel_pit_time'])))
		except:
			print("Slowest Pitstop: NA")
		try:
			print("Average Pitstop:"+str((sum(car['tel_pit_time'])/len(car['tel_pit_time']))))
		except:
			print("Average Pitstop: NA")
		try:
			print("Fastest Pitstop:"+str(min(car['tel_pit_time'])))
		except:
			print("Fastest Pitstop: NA")
		try:
			print("All Pitstops:"+str(car['tel_pit_time']))
		except:
			print("All Pitstops: NA")
		try:
			print("Total Moves:"+str(len(car['tel_moves'])))
		except:
			print("Total Moves: NA")
		try:
			print("Slowest Moves:"+str(max(car['tel_moves'])))
		except:
			print("Slowest Moves: NA")
		try:
			print("Average Moves:"+str((sum(car['tel_moves'])/len(car['tel_moves']))))
		except:
			print("Average Moves: NA")
		try:
			print("Fastest Moves:"+str(min(car['tel_moves'])))
		except:
			print("Fastest Moves: NA")
		try:
			print("All Moves:"+str(car['tel_moves']))
		except:
			print("All Moves: NA")
		try:
			print("Moves cut short by turning:"+str(car['tel_ebrakes']))
		except:
			print("Moves cut short by turning: NA")
		try:
			telemetrics.append("%:Moves cut short another car:"+str(car['tel_failed_overtakes'])+"\n")
		except:
			telemetrics.append("%:Moves cut short another car: NA\n")
		try:
			telemetrics.append("%:Succesful Overtakes:"+str(car['tel_overtakes'])+"\n")
		except:
			telemetrics.append("%:Succesful Overtakes: NA\n")
		try:
			telemetrics.append("%:Defended from overtakes:"+str(car['tel_defends'])+"\n")
		except:
			telemetrics.append("%:Defended from overtakes: NA\n")
		try:
			print("Steering vs Thrusters:"+str((car['tel_steer']))+"/"+str(len(car['tel_moves'])))
		except:
			print("Steering vs Thrusters: NA")
		try:
			print("Pitstops caused by fuel:"+str(car['tel_fuel_thr']))
		except:
			print("Pitstops caused by fuel: NA")
		try:
			print("Pitstops caused by damage:"+str(car['tel_dam_thr']))
		except:
			print("Pitstops caused by damage: NA")
		try:
			print("Total Part Degragation:"+str(car['degra']))
		except:
			print("Total Part Degragation: NA")
		try:
			print("Total Spins:"+str(car['tel_spin_count']))
		except:
			print("Total Spins: NA")
		return "To Screen"
	if vm == "f":
		my_date = str(datetime.now())
		telemetrics = []
		telemetrics.append("# Data from last race on: "+my_date+"\n")
		try:
			telemetrics.append("%:Slowest Lap:"+str(max(car['tel_lap_splits']))+"\n")
		except:
			telemetrics.append("%:Slowest Lap: NA\n")
		try:
			telemetrics.append("%:Average Lap:"+str((sum(car['tel_lap_splits'])/len(car['tel_lap_splits'])))+"\n")
		except:
			telemetrics.append("%:Average Lap: NA\n")
		try:
			telemetrics.append("%:Fastest Lap:"+str(min(car['tel_lap_splits']))+"\n")
		except:
			telemetrics.append("%:Fastest Lap: NA\n")
		try:
			telemetrics.append("%:All Laps:"+str(car['tel_lap_splits'])+"\n")
		except:
			telemetrics.append("%:All Laps: NA\n")
		try:
			telemetrics.append("%:Pitstops Taken:"+str(len(car['tel_pit_time']))+"\n")
		except:
			telemetrics.append("%:Pitstops Taken: NA\n")
		try:
			telemetrics.append("%:Slowest Pitstop:"+str(max(car['tel_pit_time']))+"\n")
		except:
			telemetrics.append("%:Slowest Taken: NA\n")
		try:
			telemetrics.append("%:Average Pitstop:"+str((sum(car['tel_pit_time'])/len(car['tel_pit_time'])))+"\n")
		except:
			telemetrics.append("%:Average Taken: NA\n")
		try:
			telemetrics.append("%:Fastest Pitstop:"+str(min(car['tel_pit_time']))+"\n")
		except:
			telemetrics.append("%:Fastest Pitstops: NA\n")
		try:
			telemetrics.append("%:All Pitstops:"+str(car['tel_pit_time'])+"\n")
		except:
			telemetrics.append("%:All Pitstops: NA\n")
		try:
			telemetrics.append("%:Total Moves:"+str(len(car['tel_moves']))+"\n")
		except:
			telemetrics.append("%:Total Moves: NA\n")
		try:
			telemetrics.append("%:Slowest Moves:"+str(max(car['tel_moves']))+"\n")
		except:
			telemetrics.append("%:Slowest Moves: NA\n")
		try:
			telemetrics.append("%:Average Moves:"+str((sum(car['tel_moves'])/len(car['tel_moves'])))+"\n")
		except:
			telemetrics.append("%:Average Moves: NA\n")
		try:
			telemetrics.append("%:Fastest Moves:"+str(min(car['tel_moves']))+"\n")
		except:
			telemetrics.append("%:Fastest Moves: NA\n")
		try:
			telemetrics.append("%:All Moves:"+str(car['tel_moves'])+"\n")
		except:
			telemetrics.append("%:All Moves: NA\n")
		try:
			telemetrics.append("%:Moves cut short by turning:"+str(car['tel_ebrakes'])+"\n")
		except:
			telemetrics.append("%:Moves cut short by turning: NA\n")
		try:
			telemetrics.append("%:Moves cut short another car:"+str(car['tel_failed_overtakes'])+"\n")
		except:
			telemetrics.append("%:Moves cut short another car: NA\n")
		try:
			telemetrics.append("%:Succesful Overtakes:"+str(car['tel_overtakes'])+"\n")
		except:
			telemetrics.append("%:Succesful Overtakes: NA\n")
		try:
			telemetrics.append("%:Defended from overtakes:"+str(car['tel_defends'])+"\n")
		except:
			telemetrics.append("%:Defended from overtakes: NA\n")
		try:
			telemetrics.append("%:Steering vs Thrusters:"+str((car['tel_steer']))+"/"+str(len(car['tel_moves']))+"\n")
		except:
			telemetrics.append("%:Steering vs Thrusters: NA\n")
		try:
			telemetrics.append("%:Pitstops caused by fuel:"+str(car['tel_fuel_thr'])+"\n")
		except:
			telemetrics.append("%:Pitstops caused by fuel: NA\n")
		try:
			telemetrics.append("%:Pitstops caused by damage:"+str(car['tel_dam_thr'])+"\n")
		except:
			telemetrics.append("%:Pitstops caused by damage: NA")
		try:
			telemetrics.append("%:Total Part Degragation:"+str(car['degra'])+"\n")
		except:
			telemetrics.append("%:Total Part Degragation: NA\n")
		try:
			telemetrics.append("%:Total Spins:"+str(car['tel_spin_count'])+"\n")
		except:
			telemetrics.append("%:Total Spins: NA\n")
		try:
			telemetrics.append("%:Cause of accident:"+str(car['wreck-note'])+"\n")
		except:
			telemetrics.append("%:Cause of accident: NA\n")
		return telemetrics

def car_status(car):
	# prints out data from the car
	txt = "Car:{0} - Position:{1} - Laps:{2} - Damage:{3} - Fuel:{4} - Pitstops:{5} - Degragation:{6}"
	print(txt.format(car['name'],car['pos'],len(car['tel_lap_splits']),car['dmg'],car['fuel'],len(car['tel_pit_time']),car['degra']))
	return

def finish_race(podium,dnf,warp):
	points = [40,35,30,27,24,21,18,15,12,10,8,6,4,2,1]
	# How many points this player earns, increment for each car in the podium until we run out of cars to award points
	p_earn = 0

	# Save all car telemetry to a file so you can pass on to players
	my_date = str(datetime.now())

	lf = open("./"+my_date+"race.log","w")
	for c in podium:
		lf.write(str(c))
	for c in dnf:
		lf.write(str(c))
	for c in warp:
		lf.write(str(c))
	lf.close()


	# Award Fastest Lap Point
	fastest_lap_time = 999

	for p in podium:
		if min(p['tel_lap_splits']) < fastest_lap_time:
			fastest_lap_time = min(p['tel_lap_splits'])

	# Award 1 point if you match the fastest lap time
	for p in podium:
		if min(p['tel_lap_splits']) == fastest_lap_time:
			p['pts'] = p['pts'] + 1
			# print()


	for c in podium:
		# Give points
		if p_earn < len(points):
			c['pts'] = c['pts'] + points[p_earn]
			p_earn = p_earn + 1

		degra_array = degrade_car(c)
		save_car(c,degra_array)


	# DNFs do the same, but no points
	for c in dnf:
		degra_array = degrade_car(c)
		save_car(c,degra_array)

	for c in warp:
		degra_array = degrade_car(c)
		save_car(c,degra_array)

	return

def save_car(car,degra_array):
	c_fh = open(car['file'],"w")
	c_fh.write("# Car Template\n")
	c_fh.write("\n")
	c_fh.write("############################################\n")
	c_fh.write("#  DO NOT EDIT THE BELOW SECTION MANUALLY  #\n")
	c_fh.write("#           EDIT USING GARAGE.PY           #\n")
	c_fh.write("############################################\n")
	c_fh.write("$:name:"+str(car['name'])+"\n")
	c_fh.write("$:team:"+str(car['team'])+"\n")
	c_fh.write("############################################\n")
	c_fh.write("#                TOUR INFO                 #\n")
	c_fh.write("############################################\n")
	c_fh.write("$:points:"+str(car['pts'])+"\n")
	c_fh.write("############################################\n")
	c_fh.write("#                 CAR INFO                 #\n")
	c_fh.write("############################################\n")
	c_fh.write("$:cha:"+car['cha']+"\n")
	c_fh.write("$:rea:"+car['rea']+"\n")
	c_fh.write("$:fty:"+car['fty']+"\n")
	c_fh.write("$:thr:"+str(degra_array[0])+":"+str(car['thr'])+":"+str(degra_array[1])+"\n")
	c_fh.write("$:ste:"+str(degra_array[2])+":"+str(car['ste'])+":"+str(degra_array[3])+"\n")
	c_fh.write("$:coo:"+str(degra_array[4])+":"+str(car['fin'])+":"+str(degra_array[5])+"\n")
	c_fh.write("$:fin:"+str(degra_array[6])+":"+str(car['coo'])+":"+str(degra_array[7])+"\n")
	c_fh.write("$:sen:"+str(degra_array[8])+":"+str(car['sen'])+":"+str(degra_array[9])+"\n")
	c_fh.write("$:fcl:"+str(degra_array[10])+":"+str(car['fcl'])+":"+str(degra_array[11])+"\n")
	c_fh.write("$:afb:"+str(degra_array[12])+":"+str(car['afb'])+":"+str(degra_array[13])+"\n")
	c_fh.write("$:dia:"+str(degra_array[14])+":"+str(car['dia'])+":"+str(degra_array[15])+"\n")
	c_fh.write("############################################\n")
	c_fh.write("#               STRATEGY INFO              #\n")
	c_fh.write("############################################\n")
	c_fh.write("$:pp_fuel:"+str(car['pp_fuel'])+"\n")
	c_fh.write("$:pp_dam:"+str(car['pp_dam'])+"\n")
	c_fh.write("$:tactic:"+str(car['tactic'])+"\n")
	c_fh.write("$:snack:"+str(car['snack'])+"\n")
	c_fh.write("############################################\n")
	c_fh.write("#            LAST RACE TELEMETRY           #\n")
	c_fh.write("############################################\n")
	# Gather telemetry

	tele_array = car_telementry(car,"f")

	for t in tele_array:
		c_fh.write(t)

	c_fh.close()

def degrade_car(c):
	# Using a cars degragation, return degraded car

	# First, check if the car was wrecked and apply modifiers
	if c['wreck'] == True:
		c['degra'] = c['degra'] + 50


	c_fh = open(str(c['file']),"r")

	# Gather the mins and maxes of all stats
	for l in c_fh:
		if l.startswith("#"):
			continue
		if l.startswith("$"):
			# Check what variable
			this_l = l.split(":")
			# print(this_l)
			if this_l[1] == "thr":
				min_thr = int(this_l[2])
				max_thr = int(this_l[4])
			elif this_l[1] == "fin":
				min_fin = int(this_l[2])
				max_fin = int(this_l[4])
			elif this_l[1] == "sen":
				min_sen = int(this_l[2])
				max_sen = int(this_l[4])
			elif this_l[1] == "fcl":
				min_fcl = int(this_l[2])
				max_fcl = int(this_l[4])
			elif this_l[1] == "ste":
				min_ste = int(this_l[2])
				max_ste = int(this_l[4])
			elif this_l[1] == "coo":
				min_coo = int(this_l[2])
				max_coo = int(this_l[4])
			elif this_l[1] == "afb":
				min_afb = int(this_l[2])
				max_afb = int(this_l[4])
			elif this_l[1] == "dia":
				min_dia = int(this_l[2])
				max_dia = int(this_l[4])

	c_fh.close()


	# Determine total degragation
	t_deg = round(c['degra']/10)

	# Figure out total degragation
	while t_deg > 0:
		dam_what = random.choice(["min_thr","max_thr","min_fin","max_fin","min_sen","max_sen","min_fcl","max_fcl","min_ste","max_ste","min_coo","max_coo","min_afb","max_afb","min_dia","max_dia"])
		if dam_what == "min_thr":
			min_thr = min_thr + 1
			if min_thr > c['thr']:
				c['thr'] = min_thr
		elif dam_what == "max_thr":
			max_thr = max_thr - 1
			if max_thr < c['thr']:
				c['thr'] = max_thr
		elif dam_what == "min_fin":
			min_fin = min_fin + 1
			if min_fin > c['fin']:
				c['fin'] = min_fin
		elif dam_what == "max_fin":
			max_fin = max_fin - 1
			if max_fin < c['fin']:
				c['fin'] = max_fin
		elif dam_what == "min_sen":
			min_sen = min_sen + 1
			if min_sen > c['sen']:
				c['sen'] = min_sen
		elif dam_what == "max_sen":
			max_sen = max_sen - 1
			if max_sen < c['sen']:
				c['sen'] = max_sen
		elif dam_what == "min_fcl":
			min_fcl = min_fcl + 1
			if min_fcl > c['fcl']:
				c['fcl'] = min_fcl
		elif dam_what == "max_fcl":
			max_fcl = max_fcl - 1
			if max_fcl < c['fcl']:
				c['fcl'] = max_fcl
		elif dam_what == "min_ste":
			min_ste = min_ste + 1
			if min_ste > c['ste']:
				c['ste'] = min_ste
		elif dam_what == "max_ste":
			max_ste = max_ste - 1
			if max_ste < c['ste']:
				c['ste'] = max_ste
		elif dam_what == "min_coo":
			min_coo = min_coo + 1
			if min_coo > c['coo']:
				c['coo'] = min_coo
		elif dam_what == "max_coo":
			max_coo = max_coo - 1
			if max_coo < c['coo']:
				c['coo'] = max_coo
		elif dam_what == "min_afb":
			min_afb = min_afb + 1
			if min_afb > c['afb']:
				c['afb'] = min_afb
		elif dam_what == "max_afb":
			max_afb = max_afb - 1
			if max_afb < c['afb']:
				c['afb'] = max_afb
			t_deg = t_deg - 1
		elif dam_what == "min_dia":
			min_dia = min_dia + 1
			if min_dia > c['dia']:
				c['dia'] = min_dia
		elif dam_what == "max_dia":
			max_dia = max_dia - 1
			if max_dia < c['dia']:
				c['dia'] = max_dia
		t_deg = t_deg - 1

	degra_ray = [min_thr,max_thr,min_ste,max_ste,min_fin,max_fin,min_coo,max_coo,min_sen,max_sen,min_fcl,max_fcl,min_afb,max_afb,min_dia,max_dia]

	return degra_ray

def draw_green_light(track):

	nothing = input("Press Enter to Start The Race!\n")
	cs()
	print("|-----|\n|*****|\n|*****|\n|*****|\n|-----|\n")
	time.sleep(1)
	print("|-----|\n|00000|\n|*****|\n|*****|\n|-----|\n")
	time.sleep(1)
	print("|-----|\n|00000|\n|00000|\n|*****|\n|-----|\n")
	time.sleep(random.randint(1,3))
	print("|-----|\n|00000|\n|00000|\n|00000|\n|-----|\n")
	print("BLAST OFF AT THE " + track['name']+"!!!!!!!!!!!!!!!")
	time.sleep(3)
	return

def make_car(c_fh,c_fp):
	# Takes an array of stats from a file and makes a car
	
	car = {"name":"",
	"team":"",
	"fin":0,
	"coo":0,
	"ste":0,
	"thr":0,
	"sen":0,
	"fcl":0,
	"afb":0,
	"dia":0,	
	"cha":"",
	"rea":"",
	"fty":"",
	"fra":0,
	"coa":0,
	"lap":0,
	"pos":0,
	"dmg":0,
	"tactic":"",
	"snack":"",
	"pts":0,
	"pp_fuel":0,
	"pp_dam":0,
	"degra":0,
	"fuel":max_fuel(),
	"wreck":False,
	"spun":False,
	"locale":"Starting Grid",
	"tel_lap_splits":[],
	"tel_current_lap":0,
	"tel_pit_time":[],
	"tel_moves":[],
	"tel_ebrakes":0,
	"tel_failed_overtakes":0,
	"tel_overtakes":0,
	"tel_defends":0,
	"tel_steer":0,
	"tel_fuel_thr":0,
	"tel_dam_thr":0,
	"tel_spin_count":0,
	"time":0,
	"wreck-note":"",
	"pit_flag":0,
	"ball":random.randint(1,1000),
	"file":c_fp
	}

	# "name":car name
	# "fin": fins trait
	# "coo": cooling trait
	# "ste": steering trait
	# "thr": thruster trait
	# "sen": sensors trait
	# "fcl": fuelcell trait
	# "afb": afterburner trait
	# "dia": diagnostics trait
	# "cha": chassis type
	# "rea": reactor type
	# "fty": fuel type
	# "fra": car fragility
	# "coa": car coastin
	# "lap": laps done
	# "pos": car position
	# "dmg": damange taken
	# "pts": points
	# "pp_fuel": pitting plan, pit when you have less fuel than this
	# "pp_dam": pitting plan, pit when you have more damage than this
	# "degra": amount of degragation the car has made
	# "fuel": amount of fuel the car has
	# "wreck": check if this car has wrecked
	# "tel_pits": stats, number of pit stops
	# "tel_pit_time": stats, amount of turns spent in the pits
	# "tel_ebrakes": stats, number of times a turn was cut short by corners
	# More stats can be added as players request
	# "time": amount of turns this craft has taken
	# "wreck-note": how the wreck occured
	# "pit_flag": if the craft is currently in the pit
	# "ball": random seed to tiebreak qualifiers
	# "file": path to car save file

	for l in c_fh:
		if l.startswith("#"):
			continue
		if l.startswith("$"):
			# Check what variable
			this_l = l.split(":")
			# print(this_l)
			if this_l[1] == "name":
				car['name'] = this_l[2].strip("\n")
			elif this_l[1] == "team":
				car['team'] = str(this_l[2])
			elif this_l[1] == "points":
				car['pts'] = int(this_l[2])
			elif this_l[1] == "thr":
				car['thr'] = int(this_l[3])
			elif this_l[1] == "fin":
				car['fin'] = int(this_l[3])
			elif this_l[1] == "sen":
				car['sen'] = int(this_l[3])
			elif this_l[1] == "fcl":
				car['fcl'] = int(this_l[3])
			elif this_l[1] == "ste":
				car['ste'] = int(this_l[3])
			elif this_l[1] == "coo":
				car['coo'] = int(this_l[3])
			elif this_l[1] == "afb":
				car['afb'] = int(this_l[3])
			elif this_l[1] == "dia":
				car['dia'] = int(this_l[3])
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
			elif this_l[1] == "tactic":
				car['tactic'] = str(this_l[2])
			elif this_l[1] == "snack":
				car['snack'] = str(this_l[2])


	# Car chassis affects fragility and coasting
	if car['cha'] == "streamlined": 
		car['fra'] = 750 - car['thr'] - car['fin'] - car['sen'] - car['fcl'] - car['ste'] - car['coo'] - car['afb'] - car['dia']
		if car['rea'] == "fission":
			car['coa'] = 150
		else:
			car['coa'] = 80
	elif car['cha'] == "cubic":
		car['fra'] = 850 - car['thr'] - car['fin'] - car['sen'] - car['fcl'] - car['ste'] - car['coo'] - car['afb'] - car['dia']
		if car['rea'] == "fission":
			car['coa'] = 50
		else:
			car['coa'] = 30
	else:
		# Assume neutral
		car['fra'] = 800 - car['thr'] - car['fin'] - car['sen'] - car['fcl'] - car['ste'] - car['coo'] - car['afb'] - car['dia']
		if car['rea'] == "fission":
			car['coa'] = 100
		else:
			car['coa'] = 60
	return car

def load_gp(gp):
	# Open all files in the gp folder
	# Make a car for each and return array
	prix_cars = []
	for filename in listdir("./tours/"+gp):
		# Only open car files
		if ".car" not in filename:
			continue
		if "template.car" in filename:
			continue
		# Open Files
		car_fp = "./tours/"+gp+"/"+filename
		# print(car_fp)
		car_f = open(car_fp,"r")
		car_o = make_car(car_f,car_fp)
		# Fix car filepath
		prix_cars.append(car_o)
		car_f.close()

	print(str(len(prix_cars))+" craft added.")
	return prix_cars

def load_warp():
	# Open all files in the gp folder
	# Make a car for each and return array
	warp_cars = []
	for filename in listdir("./tours/warp"):
		# Only open car files
		if ".car" not in filename:
			continue
		if "template.car" in filename:
			continue
		# Open Files
		car_fp = "./tours/warp/"+filename
		# print(car_fp)
		car_f = open(car_fp,"r")
		car_o = make_car(car_f,car_fp)
		# Fix car filepath
		warp_cars.append(car_o)
		car_f.close()

	# print(str(len(warp_cars))+" craft added.")
	return warp_cars

def load_track(t_fh):

	this_track = {
	"name":"",
	"lc":0,
	"course":[],
	"flag":0,
	"anomaly":"none"}

	for l in t_fh:
		if l.startswith("$"):
			this_l = l.split(":")
			if this_l[1] == "name":
				this_track["name"] = this_l[2].strip("\n")
			elif this_l[1] == "laps":
				this_track["lc"] = int(this_l[2])
			elif this_l[1] == "course":
				this_track["course"] = this_l[2].strip("\n").split(",")

	return this_track

def roll_anomaly():
	# Returns a string to delcare what the anomaly is and about how long it will last
	roll_anomaly = random.randint(0,6)
	time = random.randint(10,30)
	if roll_anomaly == 0:
		return "Dog on track.", time
	elif roll_anomaly == 1:
		return "Toxic goo on track.", time
	elif roll_anomaly == 2:
		return "Robot uprising.", time
	elif roll_anomaly == 3:
		return "Unspeakable horror.", time
	elif roll_anomaly == 4:
		return "MEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOWMEOW.", time
	elif roll_anomaly == 5:
		return "Advertising break required.", time
	elif roll_anomaly == 6:
		return "Bigfoot on track.", time

def battle(attacker,defender):
	# Roll
	if attacker['snack'] == "porridge":
		att_roll = random.randint(20,80)
	elif attacker['snack'] == "nachos":
		att_roll = random.randint(-20,120)
	elif attacker['snack'] == "universe":
		att_roll = random.randint(-50,150)
	else:
		# Ice cream!
		att_roll = random.randint(0,100)

	# Roll
	if defender['snack'] == "porridge":
		def_roll = random.randint(20,80)
	elif defender['snack'] == "nachos":
		def_roll = random.randint(-20,120)
	elif defender['snack'] == "universe":
		def_roll = random.randint(-50,150)
	else:
		# Ice cream!
		def_roll = random.randint(0,100)

	# Modifiers
	if attacker['tactic'] == "cautious":
		att_roll = att_roll - 15
	elif attacker['tactic'] == "psycho":
		att_roll = att_roll + 20
	elif attacker['tactic'] == "universe":
		att_roll = att_roll + 25

	if defender['tactic'] == "cautious":
		def_roll = def_roll + 20
	elif defender['tactic'] == "psycho":
		def_roll = def_roll - 15
	elif defender['tactic'] == "universe":
		def_roll = def_roll + 25

	# Compare
	if att_roll > def_roll * 2:
		# Double damage!
		defender = danger_roll(defender)
		defender = danger_roll(defender)
		attacker['tel_overtakes'] = attacker['tel_overtakes'] + 1
	elif def_roll > att_roll * 2:
		# Double damage!
		attacker = danger_roll(attacker)
		attacker = danger_roll(attacker)
		attacker['c_speed'] = 0
		defender['tel_defends'] = defender['tel_defends'] + 1
		attacker['tel_failed_overtakes'] = attacker['tel_failed_overtakes'] + 1
	elif def_roll > att_roll:
		attacker['c_speed'] = 0
		defender['tel_defends'] = defender['tel_defends'] + 1
		attacker['tel_failed_overtakes'] = attacker['tel_failed_overtakes'] + 1
	else:
		attacker['tel_overtakes'] = attacker['tel_overtakes'] + 1
	
	return attacker,defender

def move_car(car,track,mover,all_cars,warp):
	# print(car['name'] + " moving!")
	# Car takes 1 clock tick
	car['time'] = car['time'] + 1
	car['tel_current_lap'] = car['tel_current_lap'] + 1

	# Takes on the car, track, and if moving using thrust or sensors, returns car with new position and flags

	# Check if pitting
	if car['pit_flag'] > 0:
		# print("In the pit")
		# If its the first turn in the pit, do the work
		if car['pit_flag'] == 1:
			car = pit(car)
			car['pit_flag'] = car['pit_flag']+1
			return car, all_cars,warp
		# Otherwise, wait for daignostics to finish
		if car['dia'] + ((car['pit_flag']-2)*5) > random.randint(1,100):
			roll = car['dia'] + (car['pit_flag']*5)
			# print("Pit roll of "+str(roll)+" was not high enough!")
			car['tel_pit_time'].append(car['pit_flag'])
			car['pit_flag'] = 0
			car['pos'] = car['pos']+1
		else:
			car['pit_flag'] = car['pit_flag'] + 1

		return car, all_cars,warp

	# SPinning goes here
	if car['spun']:
		# Attempt to un spin
		if car['ste'] > random.randint(0,120):
			car['spun'] = False
			return car, all_cars,warp
		else:
			return car, all_cars,warp

	
	# Speed roll, either thrusters or steering based on other driver positions and based on reactor
	if['rea'] == "fission":
		if mover == 0:
			c_speed = car['thr']-random.randint(1,100)+car['coa']
		else:
			c_speed = car['ste']-random.randint(1,100)+car['coa']
	else:
		if mover == 0:
			c_speed = ((car['thr']*2)-random.randint(1,200))+(car['afb']-random.randint(20,80))
		else:
			c_speed = ((car['ste']*2)-random.randint(1,200))+(car['afb']-random.randint(20,80))

		if c_speed < car['coa']:
			c_speed = car['coa']

	
	# Fuel affects afterburners, fuelcell, and coolant efficiency
	if track['flag'] > 0:
		if random.randint(0,3) == 0:
			car['fuel'] = car['fuel'] - 1
	elif car['fty'] == "plutonium":
		# Plutonium is the high risk/high reward fuel, requires both coolant and fcl efficiency
		if car['coo'] < random.randint(1,100) or car['fcl'] < random.randint(1,100):
			car['fuel'] = car['fuel'] - 3
		else:
			car['fuel'] = car['fuel'] + 1
		# Check if you 

		# After burner always runs
		ab_roll = car['afb'] - random.randint(1,80)

		if ab_roll > 0:
			c_speed = c_speed + ab_roll

	elif car['fty'] == "uranium":
		# Middle of the ground fuel
		if car['coo'] < random.randint(1,100):
			car['fuel'] = car['fuel'] - 6
		elif car['fcl'] < random.randint(1,100):
			car['fuel'] = car['fuel'] - 2
		else:
			car['fuel'] = car['fuel'] + 1

		ab_roll = car['afb'] - random.randint(1,100)

		if ab_roll > 0:
			c_speed = c_speed + ab_roll
	else:
		# Radium
		# Safest fuel
		if car['coo'] < random.randint(1,100):
			car['fuel'] = car['fuel'] - 4
		elif car['fcl'] < random.randint(1,120):
			car['fuel'] = car['fuel'] - 2
		else:
			car['fuel'] = car['fuel'] + 1

		ab_roll = car['afb'] - random.randint(1,120)

		if ab_roll > 0:
			c_speed = c_speed + ab_roll

	# If there is a yellow flag, and this is the first car, reduce speed greatly.
	if track['flag'] > 0 and car == all_cars[0]:
		c_speed = 15

	# Check for anomaly events
	if track['anomaly'] == "Dog on track.":
		unlucky = random.randint(0,999)
		if unlucky == 999:
			car['wreck'] = True
			car['wreck-note'] = "Crashed into the dog! "+car['name']+" died!"
			return car, all_cars,warp
		elif unlucky >= 900:
			car['wreck'] = True
			car['wreck-note'] = "Crashed into the dog!"
			return car, all_cars,warp
	elif track['anomaly'] == "Robot uprising.":
		unlucky = random.randint(0,999)
		if unlucky == 999:
			car['wreck'] = True
			car['wreck-note'] = "Was attacked by robots! "+car['name']+" was taken prisoner by the robots!"
			return car, all_cars,warp
		elif unlucky >= 900:
			car['wreck'] = True
			car['wreck-note'] = "Was attacked by robots!"
			return car, all_cars,warp		
	elif track['anomaly'] == "Unspeakable horror.":
		unlucky = random.randint(0,999)
		if unlucky == 999:
			car['wreck-note'] = "WARPED!"
			all_cars.remove(car)
			warp.append(car)
			return car, all_cars,warp


	# If you max out fuel, or go too fast, danger!
	if car['fuel'] > 105 or c_speed >= 250:
		# If you ate the nachos, you may warp
		if car['snack'] == "nachos" and random.randint(0,249) == 0 and len(all_cars) > 0:
			# WARP
			car['wreck-note'] = "WARPED!"
			all_cars.remove(car)
			warp.append(car)
			return car, all_cars,warp
		car = danger_roll(car)
		if car['wreck'] == True:
			car['wreck-note'] = "Destroyed in meltdown!"
						# Roll to see if the driver survived
			if random.randint(0,99) == 99:
				car['wreck-note'] = car['wreck-note']+" "+car['name']+" died!"
			return car, all_cars,warp

	# If you run out of fuel your done!
	if car['fuel'] < 0:
		car['wreck'] = True
		car['wreck-note'] = "Out of fuel."
		return car, all_cars,warp

	# Move based on car position
	while c_speed > 0:
		# Check if you need to change local
		# for k in track['layout']:
		# 	if car['pos'] == k
		#		car['locale'] = track['layout'][k+1]
		# Check next position of the track, finishing laps is automatic
		if car['pos'] >= len(track['course']):
			car['pos'] = 0
			car['lap'] = car['lap']+1
			c_speed = c_speed - 5
			# Add to car splits
			if car['lap'] > 0:
				car['tel_lap_splits'].append(car['tel_current_lap'])
				car['tel_current_lap'] = 0
			# Stop checking if car finished
			if car['lap'] >= track['lc']:
				return car, all_cars,warp
			continue
		# Then race as normal:
		if track['course'][car['pos']] == "straight":
			# Pay 5
			c_speed = c_speed - 5
			car['pos'] = car['pos']+1
		elif track['course'][car['pos']] == "curve":
			# Check with fins
			if car['fin']  >= random.randint(1,80):
				c_speed = c_speed - 5
				car['pos'] = car['pos']+1
			# Pay extra
			elif c_speed >= 10:
				c_speed = c_speed - 10
				car['pos'] = car['pos']+1
			# Danger
			else:
				c_speed = 0
				car['tel_ebrakes'] = car['tel_ebrakes']+1
				car = danger_roll(car)
				if car['wreck']:
					car['wreck-note'] = "Wrecked on curve"
				return car, all_cars,warp
		elif track['course'][car['pos']] == "turn":
			# Check with fins
			if car['fin']  >= random.randint(1,120):
				c_speed = c_speed - 5
				car['pos'] = car['pos']+1
			# Pay extra
			elif c_speed >= 20:
				c_speed = c_speed - 20
				car['pos'] = car['pos']+1
			# Danger
			else:
				c_speed = 0
				car['tel_ebrakes'] = car['tel_ebrakes']+1
				car = danger_roll(car)
				if car['wreck']:
					car['wreck-note'] = "Wrecked on turn."
					if random.randint(0,99) == 99:
						car['wreck-note'] = car['wreck-note']+ " "+car['name']+" died!"
				return car, all_cars,warp
		elif track['course'][car['pos']] == "pit":
			if car['pp_fuel'] >= car['fuel'] or car['pp_dam'] <= car['dmg'] or track['flag'] >= 5:
				if car['pp_fuel'] >= car['fuel']:
					car["tel_fuel_thr"] = car["tel_fuel_thr"] + 1
				if car['pp_dam'] <= car['dmg']:
					car["tel_dam_thr"] = car["tel_dam_thr"] + 1
				car['pit_flag'] = 1
				return car, all_cars,warp
			else:
				c_speed = c_speed - 5
				car['pos'] = car['pos'] + 1				
			# Check pit flag
			# If lit, then go into the pit
		# Check if you passed a car
		else:
			print("ERROR! " + track['course'][car['pos']])
			print(car['pos'])
			time.sleep(1)
		
		# Go through all cars
		for v in all_cars:
			# Skip this car
			if car['name'] == v['name']:
				continue
			# Skip Cars behind this one, as lapped cars move to the side
			elif car['lap'] > v['lap']:
				continue
			# If there is a saftey car, dont try and overtake
			elif track['flag'] > 0 and car['lap'] == v['lap'] and (car['pos'] == v['pos'] -1 or (car['pos']==len(track['course']) and v['pos'] == 0)):
				return car, all_cars,warp				
			elif car['pos'] == v['pos']:
				# If you are teammates, maybe you wont fight
				if v['team'] == car['team']:
					if v['tactic'] == "team" or v['tactic'] == "cautious" or car['tactic'] == "cautious":
						continue
				else:
					car,v = battle(car,v)
					if v['wreck']:
						v['wreck-note'] = "Wrecked in collision with "+car['name']
						# Roll to see if the driver survived
						if random.randint(0,99) == 99:
							v['wreck-note'] = v['wreck-note']+" "+v['name']+" died!"
					if car['wreck']:
						car['wreck-note'] = "Wrecked in collision with "+v['name']
						# Roll to see if the driver survived
						if random.randint(0,99) == 99:
							car['wreck-note'] = car['wreck-notename']+car['driver']+" died!"				
						return car, all_cars,warp


	# Return the car with the new position

	return car, all_cars,warp

def race(these_cars,track,info):
	podium = []
	dnf = []
	warp = load_warp()
	normality = True
	entro_bonus = 0

	# Calculate nachos roll
	for car in these_cars:
		if car['tactic'] == "nachos":
			entro_bonus = entro_bonus + 10

	positions = []

	# Line Up cars
	# Hand over cars with highest time to lowest (or in order of being loaded in the case of practice), and use that to slot them in starting on the lowest line
	s = 0
	for t in these_cars:
		t['pos'] = len(track['course'])-1-s
		s = s + 1
		positions.append(t['pos'])

	# Draw race at pole, then start
	draw_race(podium,dnf,warp,these_cars,track,info)
	draw_green_light(track)

	while len(these_cars) > 0:
		for c in these_cars:
			# print(c)
			# Detemine if you should use sensors or thrusters
			mm = 0

			for v in positions:
				if v == c['pos']:
					continue
				if c['pos'] - 5 <= v <= c['pos'] + 5:
					# print(str(v) + " within range of " + str(c['pos']))
					mm = 1
					c['tel_steer'] = c['tel_steer']+1
					break
				else:
					# print(str(v) + " out of range of " + str(c['pos']))
					pass

			# Save current car position for telemetry
			start_point = c['pos']

			c,these_cars,warp = move_car(c,track,mm,these_cars,warp)


			# Save move speed
			if c['pos'] < start_point:
				# Wonky math from the lap over
				c['tel_moves'].append((len(track['course'])-start_point)+c['pos'])
			else:
				c['tel_moves'].append(c['pos']-start_point)


			# Do a secondary check for running out of fuel
			if c['fuel'] < 0 and c['wreck'] == False:
				c['wreck'] = True
				c['wreck-note'] = "Out of fuel."

			if c['lap'] >= track['lc']:
				print("FINISH - "+c['name'])

				# Extra damage is added to degragation
				c['degra'] = c['degra'] + c['dmg']

				podium.append(c)
				these_cars.remove(c)
			elif c['lap'] + 1 == track['lc']:
				# Maybe a car is released from the Warp
				for w in warp:
					if random.randint(0,99) == 99:
						w['laps'] = track['lc'] - 1
						w['pos'] = 0
						warp.remove(w)
						these_cars.append(w)
			elif c['wreck']:
				c['degra'] = c['degra'] + c['dmg']
				dnf.append(c)
				these_cars.remove(c)
				# Look if there was another car that was wrecked during the move
				for v in these_cars:
					if v['wreck']:
						c['degra'] = c['degra'] + c['dmg']
						dnf.append(v)
						these_cars.remove(v)					
				# Check for pile ups
				for v in these_cars:
					if v['wreck']:
						continue
					if c['pos'] - 5 <= v['pos'] <= c['pos']:
						# Avoid damage with a positive roll from the driver
						dodge_roll = random.randint(-50,50)
						if c['tactic'] == "cautious":
							dodge_roll = dodge_roll + 20
						elif c['tactic'] == "psycho":
							dodge_roll = dodge_roll - 10

						if c['tactic'] == "porridge" or c['tactic'] == "universe":
							dodge_roll = dodge_roll + 20
						elif c['tactic'] == "nachos":
							dodge_roll = dodge_roll + random.randint(-25,25)

						if dodge_roll < 0:
							v = danger_roll(v)
							v = danger_roll(v)
							v = danger_roll(v)

					if v['wreck']:
						v['wreck-note'] = "Wrecked in pileup"
						# Roll to see if the driver survived
						if random.randint(0,99) == 99:
							v['wreck-note'] = v['wreck-note']+" "+v['name']+" died!"
						v['degra'] = v['degra'] + v['dmg']
						dnf.append(v)
						these_cars.remove(v)
				# Check if a saftey car must be deployed
				if random.randint(0,1) == 1:
					track['flag'] = track['flag']+random.randint(10,30)
					track['anomaly'] = "Cleaning up wreck."
			else:
				pass



			#Refresh positions if the race is continuing
			if len(these_cars) <= 0:
				break


			positions = []
			for r in these_cars:
				positions.append(r['pos'])


		# Reset order of cars for next clock tick
		these_cars = sorted(these_cars, key=itemgetter('lap','pos'),reverse=True)

		# Move saftey car if required
		if track['flag'] > 100:
			track['flag'] = 99
		elif track['flag'] > 0:
			track['flag'] = track['flag'] - 1
		elif normality == True and (random.randint(0,1999)+entro_bonus > 1998):
			# Roll for an anomaly
			track['anomaly'],track['flag'] = roll_anomaly()
			normality = False

		try:
			draw_race(podium,dnf,warp,these_cars,track,info)
		except:
			print("draw error!")

	these_cars = sorted(these_cars, key=itemgetter('time','ball'))
	print("+----------------------+")
	print("|      RACE OVER!      |")
	print("|* * * * * * * * * * * |")
	print("| * * * * * * * * * * *|")
	print("|* * * * * * * * * * * |")
	print("| * * * * * * * * * * *|")
	print("|      RACE OVER!      |")
	print("+----------------------+")

	junk = input("Press enter to see the podium\n")
	cs()

	print("Podium:")
	for c in podium:
		print(c['name']+" - "+str(c['time']))

	print("Crashes:")

	for c in dnf:
		print(c['name']+" - "+c['wreck-note'])


	for c in warp:
		if c['name'] == "The Red Spector" or c['name'] == "The Green Phantom":
			continue
		print(c['name']+" is stuck in the warp!")

	return podium,dnf,warp

def qualify(these_cars,track):
	# Returns cars with their poll position
	q = 0

	for c in these_cars:
		print("Pilot "+c['name']+" qualifying")
		time.sleep(1)

		while c['lap'] < 3:
			# Positions is a null array because there are no other cars on the track during qualifiers, also that is why move value is always 0!
			move_car(c,track,0,[],[])


			# If a car wrecks, they go to the end of the qualfying table
			if c['wreck'] == 1:
				c['time'] = 2000+q
				q = q + 1
				break

		print("TIME:"+str(c['time']))
	# Sort cars by pole time and set up grid

	these_cars = sorted(these_cars, key=itemgetter('time','ball'))

	# Show qualifying information:
	grid_position = 1
	t = PrettyTable(["Position","Pilot","Team","Time"])

	for c in these_cars:
		t.add_row([grid_position,c['name'],c['team'],str(c['time'])])
		grid_position = grid_position + 1
	# 1 Point for pole position
	these_cars[0]['pts'] = these_cars[0]['pts'] + 1

	# After quaifying, car is repaired and readied for the race
	for c in these_cars:
		c['fuel'] = max_fuel()
		c['dmg'] = 0
		c['lap'] = -1
		c['degra'] = 0
		c['wreck'] = 0
		c['time'] = 0
		c['wreck-note'] = ""
		c['pit_flag'] = 0
		# Reset car telemetry?
		c['tel_lap_splits'] = []
		c['tel_current_lap'] = 0
		c['tel_pit_time'] = []
		c['tel_moves'] = []
		c['tel_ebrakes'] = 0
		c['tel_failed_overtakes'] = 0
		c['tel_overtakes'] = 0
		c['tel_defends'] = 0
		c['tel_steer'] = 0
		c['tel_fuel_thr'] = 0
		c['tel_dam_thr'] = 0
		c['locale'] = "Starting Grid"


	return these_cars



def draw_race(podium,dnf,warp,cars,track,info):
	# Needs a practice argument to change the output?
	# info = r = race info, a lot of stuff hidden
	# info = p = practice info, show lots of metrics?

	# Clear screen
	cs()
	print(track['name'])
	# Use first place car for metrics
	try:
		txt = "Time:{0}"
		print(txt.format(cars[0]['time']))
		txt = "Laps:{0}/{1}"
		print(txt.format(cars[0]['lap'],track['lc']))
	except:
		txt = "Time:{0}"
		print(txt.format(podium[0]['time']))
		txt = "Laps:{0}/{1}"
		print(txt.format(podium[0]['lap'],track['lc']))
	# Would also like to show fastest time if possible

	# Show - if a green or yellow flag
	if track['flag'] == 0:
		print("###GREEN FLAG###")
	else:
		print("###YELLOW FLAG!### : "+str(track['flag'])+" : "+track['anomaly'])

	#Calculate interval based on first place
	try:
		lead_int = podium[0]['pos']+(podium[0]['lap']*len(track['course']))		
	except:
		lead_int = cars[0]['pos']+(cars[0]['lap']*len(track['course']))

	# print(lead_int)
	p = 1
	# Table Header
	pole_headers = ["Pos","Pilot","Team","Interval","Fastest Lap","Pitstops","Damage","Fuel","Status"]
	pole_table = []

	for c in podium:
		c_inter = lead_int - c['pos']-(c['lap']*len(track['course']))
		c_damper = round(((c['dmg']/c['fra'])*100),2)
		c_damper = str(c_damper)+"%"
		try:
			pole_table.append([p,c['name'],c['team'],c_inter,str(min(c['tel_lap_splits']))+"."+str(c['ball']),len(c['tel_pit_time']),c_damper,c['fuel'],"FINISHED-"+str(c['time'])])
		except:
			pole_table.append([p,c['name'],c['team'],c_inter,"NA","NA",c_damper,c['fuel'],"FINISHED-"+str(c['time'])])
		p = p + 1

	for c in cars:
		c_inter = lead_int - c['pos']-(c['lap']*len(track['course']))
		c_damper = round(((c['dmg']/c['fra'])*100),2)
		c_damper = str(c_damper)+"%"
		if c['pit_flag'] > 0:
			try:
				pole_table.append([p,c['name'],c['team'],c_inter,min(c['tel_lap_splits']),len(c['tel_pit_time']),c_damper,c['fuel'],"In Pit"])
			except:
				pole_table.append([p,c['name'],c['team'],c_inter,"NA","NA",c_damper,c['fuel'],"In Pit"])
		elif c['spun']:
			try:
				pole_table.append([p,c['name'],c['team'],c_inter,min(c['tel_lap_splits']),len(c['tel_pit_time']),c_damper,c['fuel'],"Spun!"])
			except:
				pole_table.append([p,c['name'],c['team'],c_inter,"NA","NA",c_damper,c['fuel'],"Spun!"])
		elif c['pit_flag'] == 0:
			try:
				pole_table.append([p,c['name'],c['team'],c_inter,min(c['tel_lap_splits']),len(c['tel_pit_time']),c_damper,c['fuel'],"Racing"])
			except:
				pole_table.append([p,c['name'],c['team'],c_inter,"NA","NA",c_damper,c['fuel'],"Racing"])
		p = p + 1

	for c in dnf:
		c_damper = round(((c['dmg']/c['fra'])*100),2)
		c_damper = str(c_damper)+"%"
		try:
			pole_table.append(["X",c['name'],c['team'],"NA",min(c['tel_lap_splits']),len(c['tel_pit_time']),c_damper,c['fuel'],c['wreck-note']])
		except:
			pole_table.append(["X",c['name'],c['team'],"NA","NA","NA",c_damper,c['fuel'],c['wreck-note']])

	for c in warp:
		if c['name'] == "The Red Spector" or c['name'] == "The Green Phantom":
			continue
		pole_table.append(["?",c['name'],c['team'],"???","???","???","???","???","WARPPED!"])

	# print(t)
	print(tabulate(pole_table,pole_headers,tablefmt="github"))

	time.sleep(1)

	return

def draw_podium(podium,dnf):
	pass

def cs():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')

	return


def setup():
	these_cars = []
	these_files = []

	title_splash()
	cs()
	print("Event Type")
	print("p - Practice")
	print("r - Grand Prix")
	r_type = input('Race Type: ')

	if r_type == "p":
		event = "practice"
		tour = input("Tour Folder: ")
		t_car = input("Load Car 1: ")
		car_fp = "./"+tour+"/"+t_car+".car"
		car_fh = open(car_fp,"r")
		a_car = make_car(car_fh,car_fp)
		these_cars.append(a_car)
		car_fh.close()

		t_car = input("Load Car 2 or na: ")

		if t_car == "na" or t_car == "NA":
			pass
		else:
			car_fp = "./"+tour+"/"+t_car+".car"
			car_fh = open(car_fp,"r")
			a_car = make_car(car_fh,car_fp)
			these_cars.append(a_car)
			car_fh.close()

	elif r_type == "r":
		event = "race"
		t_car = ""

		t_gp = input("Enter Tour Folder: ")
		these_cars = load_gp(t_gp)

	else:
		print("Error - Invalid Race Type")
		quit()

	
	t_track = input("Track: ")
	track_fh = open("./tracks/"+t_track+".track","r")
	my_track = load_track(track_fh) 
	track_fh.close()

	return these_cars,my_track,event,these_files


# Race Type
# Practice, Grand Prix

# Load Cars
# If practice, load a single car
# If qualifier/grand prix, load a who folder which represents a GP

if __name__ == "__main__":
	cs()
	cars,track,event,car_files = setup()
	cs()

	if event == "practice":
		# Set up starting grid based on the way cars were added:


		for t in cars:
			grid.append(t['pos'])

		# "Race" with the predfined grid
		race(cars,track,"p")

		for c in cars:
			print(c)
			car_telementry(d,"h")			

	else:
		print("Hovercrafts Qualifying:")
		# Draw Something?
		grid = qualify(cars,track)
		junk = "Lineup?\n"
		# Qualifiers don't damage cars or use fuel, all cars should actually return perfectly fine:

		# Cars get a pitstop before racing?

		podium,dnf,warp = race(grid,track,"r")
 
		do_save = input('Save y/n? ')

		if do_save == "y":
			finish_race(podium,dnf,warp)
		elif do_save == "d":
			for p in podium:
				print(p)
				car_telementry(p,"h")
			for d in dnf:
				print(d)
				car_telementry(d,"h")
			for d in warp:
				print(d)
				car_telementry(d,"h")

	quit()
