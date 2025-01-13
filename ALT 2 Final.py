with open("Death.txt", "r", encoding = "utf-8") as Death_English_Text:
    death_read_text_english = Death_English_Text.read()
    
with open("Death Latvian.txt", "r", encoding = "utf-8") as Death_Latvian_Text:
    death_read_text_latvian = Death_Latvian_Text.read()
    
with open("Death Polish.txt", "r", encoding = "utf-8") as Death_Polish_Text:
    death_read_text_polish = Death_Polish_Text.read()
    
with open("Death Chinese.txt", "r", encoding = "utf-8") as Death_Chinese_Text:
    death_read_text_chinese = Death_Chinese_Text.read()


death_read_text_english = death_read_text_english.split(" ")
print(death_read_text_english)