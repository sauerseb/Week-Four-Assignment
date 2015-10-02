# 
# File Header
#
# Define vowels

vowels = "aeiouAEIOU"

# Loop through word, one letter at a time
n = 0, endword = ""
def piggy(word):
	for letter in word:
		# Check if letter is a vowel
		if letter in vowels:
			# True?  We are done
			pig = word + "yay"
		else:
			# False? Consonant
			pig = word[1:] + word[0] + "ay"
	return pig


#Ask for word

word = input("Please enter a word: ")
print (piggy(word))