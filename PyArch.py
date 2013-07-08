#!/usr/bin/env python

########################################################################
#
# PyArchitecture: Architecture class for handling different classess of
#		  CPU instruction sets.
#
# Matthew Byrne - theblurg@gmail.com - 2013
#
# License: None
#
########################################################################

'''
PyArchitecture:

This class will implement a way of interigating the kind of architecture
that we are currently dealing with. This is particularly necessary for
ARM based processors which can switch between ARM and Thumb mode.
'''

class Architecture:

# Instance variables
self.__architecture__ = None

	def __init__(self):
		# Do nothing for now
		pass
	
	def setArchitecture(self, architecture = "x86"):
		if architecture == "x86":
			self.__architecture__ = "x86"
		elsif architecture == "x64":
			self.__architecture__ = "x64"
		else:
			raise RuntimeError, "The architecture requested is invalid"

	def getArchitecture(self):
		return self.__architecture__
