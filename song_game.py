print("Welcome to the song game!") 
print("I am going to ask you some questions, and then you will have your own song!")
name = input("\nPlease enter your name: ")
gender1 = input("Are you a he or a she? ")

if gender1 == "she":
	gender2 = "her"
	
if gender1 == "he":
	gender2 = "his"
	
animal1 = input("Please enter an animal (singular): ")
animalsound1 = input("Please enter the sound your animal makes (singular): ")
animal2= input("Please enter a different animal (singular): ")
animalsound2 = input("Please enter the sound your animal makes (singular): ")
animal3 = input("Please enter a different animal (singular): ")
animalsound3 = input("Please enter the sound your animal makes (singular): ")

print("\nOld Mac" + name + " had a farm, E-I-E-I-O.") 
print("And on " + gender2 + " farm " + gender1 + " had a " + animal1 + ". E-I-E-I-O.")
print("With a " + animalsound1 + " " + animalsound1 + " here, and a " + animalsound1 + " " + animalsound1 + " there, here a " + animalsound1 + ", there a " + animalsound1 + ", everywhere a " + animalsound1 + " " + animalsound1 + ".")

print("Old Mac" + name + " had a farm E-I-E-I-O.")
print("And on " + gender2 + " farm " + gender1 + " had a " + animal2 + ". E-I-E-I-O.")
print("With a " + animalsound2 + " " + animalsound2 + " here, and a " + animalsound2 + " " + animalsound2 + " there, here a " + animalsound2 + ", there a " + animalsound2 + ", everywhere a " + animalsound2 + " " + animalsound2 + ".")

print("Old Mac" + name + " had a farm E-I-E-I-O.")
print("And on " + gender2 + " farm " + gender1 + " had a " + animal3 + ". E-I-E-I-O.")
print("With a " + animalsound3 + " " + animalsound3 + " here, and a " + animalsound3 + " " + animalsound3 + " there, here a " + animalsound3 + ", there a " + animalsound3 + ", everywhere a " + animalsound3 + " " + animalsound3 + ".")

print("Old Mac" + name + " had a farm EEE-I-EEE-I-OOO...")

