name = input("Enter your name brave Tokyo Explorer: ")
print("Welcome", name, "to SHIBUYA CROSSING: The Hunt for Hachiko\n 'Hachiko', an actual Shiba dog has run away from his owner!\n Let's find him before sunset!")

answer = input("You are exiting JR Shibuya Station, the sun is out, with the department store wall to your left you can go right or back.\n Which do you choose? (back/right)").lower()

if answer == "back":
    answer = input("You walk through Shibuya station and exit to the other side near Shibuya Scramble, the iconic skyscraper.\n Do you go right or left? (left/right)").lower()
    if answer == "left":
        answer = input("You cross the street, go through the alley and arrive at the shiny new shopping center Miyashita Park. A dog howls in the distance.\n Do you go inside or take the elevator to the roof? (inside/elevator)").lower()
        if answer == "inside":
            print("Skateboarders are taking a break and walking around after eating some Panda Express Chinese food. No dogs in sight. Hint: He's somewhere where high up.")
        if answer == "elevator":
            print("Woof Woof...Bow Wow...(or) Wan Wan (in Japanese)! YOU FOUND HACHIKO!\n He's been enjoying the fresh air of Miyashita Park's rooftop grass patches this whole time.\n Congratulations!!***YOU WIN!!!***")

    if answer == "right":
        answer = input("You go inside Shibuya Scramble into lavishly designed cosmetics shops, flower shops, gift shops galore!\n Try the first floor or second floor. Type (first floor/second floor)").lower()
        if answer == "first floor":
                print("First floor, Women's Fashion. No pets allowed in here, please try again. Hint: He's somewhere where high up.")
        if answer == "second floor":
                print("Too many perfumes drive would a dog's nose away, please try again. Hint: He's somewhere where he can see the sun.")

elif answer == "right":
    answer = input("You see Starbucks across the road and you cross. Boy there are lots of people today.\n Do you go straight or left? (straight/left)").lower()
    if answer == "straight":
        answer = input("You walk through the alley between Taiseido Bookstore to your left & video rental chain Tsutaya to your right. Keep walking.\n Do you go left or right? (left/right)")
        if answer == "left":
            print("At the far end of the alleyway you see the electronics chain Bic Camera. No dogs here, try again. Hint: He's somewhere wide open.")
            quit()
        if answer == "right":
            print("At the far end of the alleyway you see Loft Japan, the household goods specialty chain. Not here, try again. Hint: He's somewhere green.")

    if answer == "left":
        answer = input("You walk up the street towards Shibuya 109 mall. It's the hip place to be for young people.\n Do you go inside Shibuya 109 or left? Type inside or left. (inside/left)").lower()
        if answer == "inside":
            answer = input("There are 8 floors to explore in Shibuya 109. Let's try the first and second floors.\n Type first floor or second floor (first floor/second floor)").lower()
        if answer == "first floor":
                print("Not here, try again. Hint: He's somewhere dogs love.")
        if answer == "second floor":
                print("There are two young, tanned gyaru girls chatting it up each other. Not here either, try again. Hint: It's sunny where he is.")
        if answer == "left":
                print("You've reached the famous UNIQLO Shibuya Dōgenzaka. Hachiko isn't here, but super hip styling and free 45 min. hem adjustments is a thing. Hint: He's at a newer part of town.")
else:
    print('Not a valid option. Game Over. Try Again.')
    print("Thank you for exploring Shibuya Japan today. Hopefully, we'll find the doggy soon.")