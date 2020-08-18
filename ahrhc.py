#!/bin/python

# Atomic Hot Rod Hovercrafts
# GUI Racer

# Importing
import pygame
import race as rc
import garage as gr
import os

# Should import all the mechanical functions from a seperate file for simplicity
# Functions required for rendering map

# TODO: Debug Function

def game_quit():
	# Play quit sound
	pygme.quit()
	quit()

def text_objects(text,font,color):
	textSurface = font.render(text, True, color)
	return textSurface,textSurface.get_rect()



def modify_car(file_path):
	# Load car and get car dictionary
	this_car = gr.


def show_files(options,opt_type,top,middle,cursor):


	# gp_button_loc = [500,300,280,100]
	icon_size = 48
	cursor_y = top
	cursor_x = middle
	cursor_s = cursor
	cursor_max = (display_height-top-icon_size)
	selection = None
	# cursor_s = first thing to show

	# Will need to fileter appropriatly based on type and create teh proper button

	# Print First Arrow
	not_a_button("UP",[cursor_x-140,cursor_y,280,icon_size])
	cursor_y = cursor_y+icon_size	


	if opt_type == "cars":
		# Start showing cars from where cursor s starts
		# While you can still draw
		while cursor_y < cursor_max and cursor_s < len(options):
			# Make sure if this is a car
			if options[cursor_s].endswith(".car"):
				# Get the option name by opening the file
				cf_h = open(options[cursor_s],"r")
				name = "error"
				for l in cf_h:
					if l.startswith("$:name:"):
						l = l.split(":")
						name = l[2].strip()
				cf_h.close()

				# Make button
				selection = file_buttons(name,[cursor_x-140,cursor_y,280,icon_size],options[cursor_s])

				# Only advance drawing cursor
				cursor_y = cursor_y+icon_size

			# Advance Cursors
			cursor_s = cursor_s + 1
			print(selection)

	not_a_button("DOWN",[cursor_x-140,cursor_y,280,icon_size])
	cursor_y = cursor_y+icon_size	


def arrow_up(cursor):
	cursor = cursor + 1
	return cursor

def arrow_down(cursor):
	cursor = cursor - 1
	if cursor < 0:
		cursor = 0
	return cursor
	# Make sure it doesn't go negative

def not_a_button(button_name,button_dem):
	# Draws a button facismili that doesn't actually light up or do anything, good for passing context clues?


	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	button_color = [255,90,90]
	hilite_color = [255,0,0]

	text_color = [200,200,200]
	txlite_color = [255,255,255]
	button_font = pygame.font.Font('./fonts/open24.ttf',32)

	button_x_center = ((button_dem[0]*2)+button_dem[2])/2
	button_y_center = ((button_dem[1]*2)+button_dem[3])/2
	button_text = button_name
	pygame.draw.rect(gameDisplay, hilite_color, button_dem)
	button_surf, text_rect = text_objects(button_text,button_font,txlite_color)

	# Draw Text
	text_rect.center = (button_x_center,button_y_center)
	gameDisplay.blit(button_surf,text_rect)

def outer_race_loop():
	# Load Track
	# Load Tour/Cars
	pass

def loadables(selected):
	# Returns a dictionary of all file options

	my_files = []

	if selected == "cars":
		my_path = "./tours/"
		for root, dirs, files in os.walk(my_path):
			for filename in files:
				my_files.append(root+"/"+filename)
	elif selected == "tours":
		my_path = "./tours/"
		for root, dirs, files in os.walk(my_path):
			for tours in dirs:
				my_files.append(root+"/"+tours)
	elif selected == "tracks":
		my_path = "./tracks/"
		for root, dirs, files in os.walk(my_path):
			for filename in files:
				my_files.append(root+"/"+filename)
	else:
		return []

	return my_files

def outer_garage_loop():
	garage_load = True
	# Start arrowkey cursor at 0
	cursor = 0
	# Grab array of cars to load
	loadable_files = loadables("cars")
	selected_car = None

	while garage_load:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				garage_load = False
				game_quit()
			if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					cursor = cursor + 1
					if cursor > len(loadable_files):
						cursor = len(loadable_files)
					# Figure out the expected value
				if event.key == pygame.K_DOWN:
					cursor = cursor - 1
					if cursor < 0:
						cursor = 0


		gameDisplay.fill([0,0,0])

		title_font = pygame.font.Font('./fonts/nasalization-rg.ttf',64)
		title_text = "Choose Hovercraft to Work On"
		TitleSurf, TitleRect = text_objects(title_text,title_font,[255,255,255])
		TitleRect.center = ((display_width/2),50)
		gameDisplay.blit(TitleSurf,TitleRect)

		# Buttons to return and to make a new car

		mm_buttons("Return",[500,100,280,60],main_menu)
		mm_buttons("New Car",[500,180,280,60],"New Car Function")
		# Load cars and give the option of making a new car
		show_files(loadable_files,"cars",250,display_width/2,cursor)
		# Draw Screen

		pygame.display.update()
		clock_1.tick(60)

		# If a car was chosen, break out?
		# Go to modify car mode

def outer_info_loop():
	# Bring to website
	# Pass
	pass

def draw_race():
	pass

def debug():
	pass

def file_buttons(button_name,context,button_dem,filepath):
	# Draws a button based on a rectangle and a button name (string on the button), clicking on a button loads a file and progresses based on file type
	# Tour > Go to track Selection
	# Track > Go to race?
	# Car > Go to edit?

	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	button_color = [255,90,90]
	hilite_color = [255,0,0]

	text_color = [200,200,200]
	txlite_color = [255,255,255]
	button_font = pygame.font.Font('./fonts/open24.ttf',32)

	button_x_center = ((button_dem[0]*2)+button_dem[2])/2
	button_y_center = ((button_dem[1]*2)+button_dem[3])/2
	button_text = button_name
	if button_dem[0] < mouse[0] < button_dem[0]+button_dem[2] and button_dem[1] < mouse[1] < button_dem[1]+button_dem[3]:
		pygame.draw.rect(gameDisplay, hilite_color, button_dem)
		button_surf, text_rect = text_objects(button_text,button_font,txlite_color)
		if click[0] == 1: and context = "mod_car":
			print("Chose")
			# Modify Car
	else:
		pygame.draw.rect(gameDisplay, button_color,button_dem)
		button_surf, text_rect = text_objects(button_text,button_font,text_color)
	# Draw Text
	text_rect.center = (button_x_center,button_y_center)
	gameDisplay.blit(button_surf,text_rect)


def mm_buttons(button_name,button_dem,action=None,action_args=None):
	# Draws a button based on a rectangle and a button name (string on the button), and then lets you run a function
	# Also takes the mouse value to determine if it should be drawn with a hiter or not
	# Main Menu Only! - Unless we want to pass all the color/font info then it can be used everywhere

	mouse = pygame.mouse.get_pos()
	click = pygame.mouse.get_pressed()

	button_color = [255,90,90]
	hilite_color = [255,0,0]

	text_color = [200,200,200]
	txlite_color = [255,255,255]
	button_font = pygame.font.Font('./fonts/open24.ttf',32)

	button_x_center = ((button_dem[0]*2)+button_dem[2])/2
	button_y_center = ((button_dem[1]*2)+button_dem[3])/2
	button_text = button_name
	if button_dem[0] < mouse[0] < button_dem[0]+button_dem[2] and button_dem[1] < mouse[1] < button_dem[1]+button_dem[3]:
		pygame.draw.rect(gameDisplay, hilite_color, button_dem)
		button_surf, text_rect = text_objects(button_text,button_font,txlite_color)
		if click[0] == 1 and action != None and action_args == None:
			action()
		elif click[0] == 1 and action != None and action_args != None:
			action(action_args)
		# Figure out an general action with files
	else:
		pygame.draw.rect(gameDisplay, button_color,button_dem)
		button_surf, text_rect = text_objects(button_text,button_font,text_color)
	# Draw Text
	text_rect.center = (button_x_center,button_y_center)
	gameDisplay.blit(button_surf,text_rect)

def main_menu():
	# Outer Loop of the game, calls other locations from here

	intro = True
	while intro:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				intro = False
				game_quit()

			# Only looking for a click
			if event.type == pygame.MOUSEBUTTONUP:
				x,y = event.pos
				if event.button == 1:
					pass

		# Draw Display
		gameDisplay.fill([0,0,0])

		# Draw title
		title_font = pygame.font.Font('./fonts/nasalization-rg.ttf',64)
		title_text = "Atomic Hot Rod Hovercrafts"
		TitleSurf, TitleRect = text_objects(title_text,title_font,[255,255,255])
		TitleRect.center = ((display_width/2),50)
		gameDisplay.blit(TitleSurf,TitleRect)

		# Subtitle

		subtitle_font = pygame.font.Font('./fonts/nasalization-rg.ttf',32)
		subtitle_text = "A Nuclear Racing Game"
		subTitleSurf, subTitleRect = text_objects(subtitle_text,subtitle_font,[255,255,255])
		subTitleRect.center = ((display_width/2),100)
		gameDisplay.blit(subTitleSurf,subTitleRect)


		

		# Draw Buttons
		# Pass button label, position, and function NAME (without())
		gp_button_loc = [500,300,280,100]
		mm_buttons("Grand Prix",gp_button_loc,"gp")
		gr_button_loc = [500,410,280,100]
		mm_buttons("Garage",gr_button_loc,outer_garage_loop)
		in_button_loc = [500,520,280,100]
		mm_buttons("Info",in_button_loc,"in")
		qu_button_loc = [500,630,280,100]
		mm_buttons("Quit",qu_button_loc,game_quit)


		# Show title Screen
		pygame.display.update()
		clock_1.tick(60)


if __name__ == "__main__":
	pygame.init()

	## Define game constants here?

	# Display size should be the option
	display_width = 1280
	display_height = 800

	gameDisplay = pygame.display.set_mode([display_width,display_height])

	# TODO - define in a style file or a dictionary

	# Game Window Title
	pygame.display.set_caption('Atomic Hot Rod Hovercrafts')

	# Set FPS Clock
	# Other clocks for order timing
	clock_1 = pygame.time.Clock()

	##############################################
	main_menu()