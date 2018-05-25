#!/usr/bin/python2
# -*- coding: utf-8 -*-

import random, sqlite3, datetime

db_file = "uv_test.sqlite"

def create_db():
	conn = sqlite3.connect(db_file)
	c = conn.cursor()
	c.execute("CREATE TABLE tries (date text, tries integer)")
	conn.commit()
	conn.close()

def store_tries(t):
	conn = sqlite3.connect(db_file)
	c = conn.cursor()
	try:
		now = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
		c.execute("INSERT INTO tries VALUES ('{}', {})".format(now, t))
		conn.commit()
		conn.close()
	# es existiert noch keine Tabelle namens "tries":
	except sqlite3.OperationalError:
		conn.close()
		create_db()
		store_tries(t)


def play(minint, maxint):
	random_number = random.randint(minint, maxint)
	count = 0
	
	while True:
		try:
			user_input = int(raw_input("Hallo! Gib eine Zahl zwischen {} und {} ein: ".format(minint, maxint)))
			
			# Zahl ist zu groß oder zu klein
			if (user_input > maxint) or (user_input < minint):
				print "Bitte eine Zahl zwischen {} und {} eingeben!".format(minint, maxint)
				continue
				
			# Zahl ist nicht die gesuchte Zahl
			elif user_input > random_number:
				print "Die gesuchte Zahl ist kleiner!"
				count += 1
				continue
			elif user_input < random_number:
				print "Die gesuchte Zahl ist größer!"
				count += 1
				continue
				
			# Zahl ist die gesuchte Zahl
			else:
				count += 1
				print "Richtig! Du hast {} Versuche gebraucht!".format(count)
				store_tries(count)
				break
			
		except ValueError:
			print "Bitte nur Zahlen eingeben"
			continue
		
		
if __name__ == "__main__":
	play(0, 10)
