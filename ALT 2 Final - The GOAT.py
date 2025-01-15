with open("Death.txt", "r", encoding = "utf-8") as Death_English_Text:
    death_read_text_english = Death_English_Text.read()
    
with open("Death Latvian.txt", "r", encoding = "utf-8") as Death_Latvian_Text:
    death_read_text_latvian = Death_Latvian_Text.read()
    
with open("Death Polish.txt", "r", encoding = "utf-8") as Death_Polish_Text:
    death_read_text_polish = Death_Polish_Text.read()
    
with open("Death Chinese.txt", "r", encoding = "utf-8") as Death_Chinese_Text:
    death_read_text_chinese = Death_Chinese_Text.read()
    
with open("kjv.txt", "r", encoding = "utf-8") as KJV_Text:
    kjv_read = KJV_Text.read()

first_text = input("Which text would you like to compare with? Choices are: Death, KJV: English Only. ")

if first_text == "Death":
    first_text = "Death"
elif first_text == "KJV":
    first_text = "KJV"
else:
    print("Invalid Input")

if first_text == "Death":
    first_langauge = input("Which language would you like to compare the first text with? Choices are: English, Latvian, Polish and Chinese. ")
elif first_text == "KJV":
    first_language = kjv_read
else:
    print("Invalid Input")

first_language = ""

if first_language == "English":
    first_language = death_read_text_english
elif first_language == "Latvian":
    first_language = death_read_text_latvian
elif first_language == "Polish":
    first_language = death_read_text_polish
elif first_language == "Chinese":
    first_language = death_read_text_chinese
else:
    print("Invalid Input")

print(first_language)

a = 0
e = 0
i = 0
o = 0
u = 0
        
for vowel in death_read_text_english:
    if vowel == "a":
        a += 1
    elif vowel == "e":
        e += 1
    elif vowel == "i":
        i += 1
    elif vowel == "o":
        o += 1
    elif vowel == "u":
        u += 1