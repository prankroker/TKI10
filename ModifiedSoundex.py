names = ["Melnyk","Shevchenko","Kovalenko","Bondarenko","Boyko","Tkachenko","Kravchenko","Kovalchuk","Koval""Oliynyk","Shevchuk",
         "Polishchuk","Tkachuk","Savchenko","Bondar","Marchenko","Rudenko","Moroz","Lysenko","Petrenko","Klymenko","Pavlenko",
         "Kravchuk","Kuzmenko","Ponomarenko","Savchuk","Vasylenko","Levchenko","Kharchenko","Sydorenko","Karpenko","Havryliuk","Shvets"]

def Soundex(word):
    word = word.upper()

    soundex = ""

    only_consonants = ""

    soundex += word[0]

    dictionary = {"B, P":"1",
                  "F,V":"2",
                  "C,K,S":"3",
                  "G,J":"4",
                  "Q,X,Z":"5",
                  "D,T":"6",
                  "L":"7",
                  "M,N":"8",
                  "R":"9"}

    vowels = {"A":"1",
              "E":"2",
              "I":"3",  
              "O":"4",
              "U":"5",
              "Y":"6"}
    
    for char in word[1:]:
        for key in vowels.keys():
            if char not in key:
                only_consonants += char

    for char in only_consonants:
        for key in dictionary.keys():
            if char in key:
                code = dictionary[key]
                if code != soundex[-1]:
                    soundex += code
    return soundex

for name in names:
    print(f"{name}: {Soundex(name)}")