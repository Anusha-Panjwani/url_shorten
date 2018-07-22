import string
import random

def generate_shortcode():

	shortcode = ""
	for i in range(6):
		random_value = random.choice(string.ascii_lowercase + 
									string.ascii_uppercase + 
									string.digits)
		shortcode+=random_value

	return shortcode