wordLongerThan8 = False
while wordLongerThan8 == False:
    word = str(input("What word are you using for the word workout today? "))
    if len(word) < 8:
        wordLongerThan8 = False;
        print("That isn't longer than 8. Use another word.\n")
    elif len(word) >= 8:
        wordLongerThan8 = True;
print("\n")
word = word.replace(" ", "")
word = word.lower()
workoutValues = {
    "a": "20 side lunges",
    "b": "15 bicep curls",
    "c": "20 alternating scissors",
    "d": "20 squats",
    "e": "20 reverse crunches",
    "f": "20 alternating jumping lunges",
    "g": "10 burpee pushups",
    "h": "30 seconds of jump rope",
    "i": "30 jumping jacks",
    "j": "20 skaters",
    "k": "20 bicycle crunches",
    "l": "15 shoulder presses",
    "m": "30 second wall sit",
    "n": "20 crunch toe touches",
    "o": "10 pushups",
    "p": "10 superman pushups",
    "q": "20 jump squats",
    "r": "10 burpees",
    "s": "20 crunches",
    "t": "30 mountain climbers",
    "u": "30 second pushup plank",
    "v": "20 shoulder taps",
    "w": "12 walk outs",
    "x": "20 alternating forward lunges",
    "y": "20 alternating side lunges",
    "z": "30 seconds of in-place jogging"
}
i = 0;
for letter in word:
    if i == len(word) - 1:
        print("and " + workoutValues[letter] + " today." + "\n")
    elif i == 0:
        print("I did " + workoutValues[letter] + ", ", end = '')
    else:
        print(workoutValues[letter] + ", ", end = '')
    i += 1
