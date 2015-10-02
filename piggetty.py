# Evan Sauers
# Collaborated with Dr. Neumann, Marissa Gross, and Rebekah Orth
# File Header-piggetty.py
#
# Add your name to this:
# Evan Sauers

# Define a function called piggy(string) that returns a string
# 
# File Header
#
# Define vowels

vowels = "aeiouAEIOU"

# Loop through word, one letter at a time
def piggy(word):
	n = 0
	endword = ""
	for letter in word:
		# Check if letter is a vowel
		if n == 0:
			# True?  We are done
			pig = word + "yay"
			return pig
		else:
			# False? Consonant
			pig = word[n:] + endword + "ay"
			return pig
	else:
		endword = endword + word[n]
		n = n + 1


#Ask for word

word = input("Please enter a word: ")
print (piggy(word))

def piggy(word):
	
	# Magic Happens Here
	pig = word
	# Ignore previous line
	
	return pig

# Open the file *getty.txt* for reading.  
gettyFile = open("getty.txt", "r")

# Open a new file *piggy.txt* for writing.  
piggyFile = open("piggy.txt", "w")

# Read the getty.txt file into a string.  
gettyString = gettyFile.read()

# Strip out bad characters (, - .).  
gettyString = gettyString.replace(",", "")
gettyString = gettyString.replace(".", "")
gettyString = gettyString.replace("-", "")

# Split the string into a list of words.  
gettylist = gettyString.split()

# Create a new empty string.  
pigstring = ""

# Loop through the list of words, pigifying each one.  
for word in gettylist:

# Add the pigified word (and a space) to the new string.  
	if len(word) > 0:
			pigstring = pigstring + piggy(word) + " "
			
# Write the new string to piggy.txt.  
print (pigstring, file = piggyFile)

# close the files.
gettyFile.close()
piggyFile.close()


