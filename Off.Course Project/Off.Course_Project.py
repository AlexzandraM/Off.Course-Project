print("This is a story about a companion's experience to be adopted!")
print("First, let's find out more about you! Press the enter key after each prompt!")
print("- - - - - - - - ")
user_name = input('What is your name: ')
print()
fav_color = input('What is your favorite color: ')
print()
fav_animal = input('What is your favorite type of animal? a : ')
print()
pet_name = input('What is the best pet name: ')
print()
gender = input("Choose the animal's gender male or female: ")
print()
fav_number = input('What is your favorite number: ')
print() 
grand_name = input("What is your grandfather's name: ")
print()
print("- - - - - - - -")
if gender.lower() == "male":
     possessive = 'he'
     sec_per = 'his'
elif gender.lower() == "female":
     possessive = 'she'
     sec_per = 'her'
else:
    possessive = 'they'
    sec_per = 'their'

print("It was a typical day in the animal adoption center, ")
print('all' , fav_number , 'of the animals were off doing their own thing.')
print('The worker was wearing his typical' , fav_color , 'band shirt, jamming')
print("out to noise protruding through his ears. As usual," , pet_name, 'the' , fav_animal)
print('went to the usual spot where' , possessive, 'spent' , sec_per , 'days since arriving in the adoption center.')
print('Suddenly, the bell on the door rings and the curious' , fav_animal, 'hears some chatter.')
print(user_name , 'pulls out a bag of treats and the animals go crazy!')
print()

energy = input("Does the animal feel energetic or calm? Type 'e' for energetic and 'c' for calm: ")
print()
if energy.lower() == 'e':
    print('The' , fav_animal , 'runs and jumps on the new visitor!' , possessive , 'Runs in circles around' , user_name)
else: 
    print(pet_name , 'sits up to watch the human.')
print()

wake = input("Does the animal want to wake up? 'y' for yes or 'n' for no: ") 
print()
if wake == 'y' :
    print(pet_name , 'eagerly greets the human at the gate!' , pet_name , 'happily joins the others, waiting for his yummy snack')
else: 
    print(pet_name , 'decides that it is probably another curious human just wanting to waste some free time. The discouraged')
    print(fav_animal , 'decides to carry on with a nap.', user_name , 'pulls out a bag of treats that attracts all of the animals,')
    print("except for" , pet_name + ".", user_name , "notices and slowly and carefully walks over to the resting" , fav_animal + ".")
print()
mood = input("Is the animal feeling nice or aggressive? Type n for nice or a for aggressive: ")
print()
if mood.lower() == 'a':
    print(user_name , 'reaches out with a treat flat on their hand. The' , fav_animal , 'nips' , user_name , 'on the hand!')
    print(user_name , 'decides to walk away to admire the others.')
    print(pet_name , 'watches the human interacting with the other animals.')
else:
    print(user_name , 'reaches out with a treat on their flat hand.' , pet_name , "gently accepts the treat.")
    print(user_name , 'gently pets the gentle' , fav_animal , 'and falls in love with how soft' , sec_per , 'coat is!')
print(pet_name , "decides that maybe the human isn't so bad.")
print()
if mood.lower() == 'a':
    print(user_name , 'decided' , pet_name , 'was too much to handle and did not want to have an aggressive pet.')
    print(pet_name , "did not get adopted this time.")
elif energy.lower() == 'e':
    print(user_name , 'decides he is not ready to be responsible for a pet right now. However,' , user_name , 'plans to return soon.')   
else:
    print("Hooray!" , pet_name , "is getting adopted!" , user_name , "was recommended to connect with the animal's previous owner," , grand_name + ",")
    print('to find out more about' , pet_name + "." , user_name , "agrees and accepts the contact information for" , grand_name + ".")
    print(pet_name , 'was excited to have a best friend again!')
