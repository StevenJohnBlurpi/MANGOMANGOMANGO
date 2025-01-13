with open("Death.txt", "r", encoding = "utf-8") as Ψ:
    read_text_english = Ψ.read()
    
with open("Death Latvian.txt", "r", encoding = "utf-8") as Latvian_Text:
    read_text_latvian = Latvian_Text.read()
    
with open("Death Polish.txt", "r", encoding = "utf-8") as Polish_Text:
    read_text_polish = Polish_Text.read()
    
with open("Death Chinese.txt", "r", encoding = "utf-8") as Chinese_Text:
    read_text_chinese = Chinese_Text.read()

print(read_text_english)