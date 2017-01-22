import sys

import os
word = open('ukr1.txt')
slovar = open ('slovar_temp.txt', 'wt')
slova = ''
for line in word.readlines():
    t=line.split(" ")
    for words in t:
        words=words.replace("<s>"," ")
        words=words.replace("</s>"," ")
        words=words.replace(" – "," ")
        words=words.replace("1"," ")
        words=words.replace("2"," ")
        words=words.replace("3"," ")
        words=words.replace("4"," ")
        words=words.replace("5"," ")
        words=words.replace("6"," ")
        words=words.replace("7"," ")
        words=words.replace("8"," ")
        words=words.replace("9"," ")
        words=words.replace("0"," ")
        words=words.replace("»"," ")
        words=words.replace("«"," ")
        words=words.replace("—"," ")
        words=words.replace("—"," ")
        words=words.replace("'","’")
        words=words.lower()
        words=words.replace("\n","")
        if len(words) > 0:
            slova=slova + (words+"\n")

slovar.write(slova)
slovar.close()

file = open('slovar_temp.txt', 'r+')
pos = 0
line = file.readlines()
file.seek(pos)
sort_text = sorted(line)
for new_line in sort_text:
    file.write(new_line)
    pos = file.tell()
file.close()
file1 = open('slovar.txt', 'wt')
file = open('slovar_temp.txt', 'r+')
line1 = ""
for line in file.readlines():
    if  line1 != line:
        file1.write(line)
    line1 = line
file1.close()
file.close()

os.remove('slovar_temp.txt')



softletters=set(u"’яїюіьє")
startsyl=set(u"#'ьаяоїуюеєіи-")
others = set(["#", "+", "-", u"ь", u"ъ", u"’"])

softhard_cons = {                                                                
    u"б" : u"b",
    u"в" : u"v",
    u"г" : u"g",
    u"ґ" : u"g",
    u"д" : u"d",
    u"з" : u"z",
    u"к" : u"k",
    u"л" : u"l",
    u"м" : u"m",
    u"н" : u"n",
    u"п" : u"p",
    u"р" : u"r",
    u"с" : u"s",
    u"т" : u"t",
    u"ф" : u"f",
    u"ц" : u"c",
    u"х" : u"h"
}

other_cons = {
    u"ж" : u"zh",
    u"ч" : u"ch",
    u"ш" : u"sh",
    u"щ" : u"sch",
    u"й" : u"j"
}
                                
vowels = {
    u"а" : u"a",
    u"я" : u"a",
    u"у" : u"u",
    u"ю" : u"u",
    u"о" : u"o",
    u"ї" : u"i",
    u"е" : u"e",
    u"є" : u"e",
    u"і" : u"i",
    u"и" : u"y",
}                                

def pallatize(phones):
    for i, phone in enumerate(phones[:-1]):
        if phone[0] in softhard_cons:
            if phones[i+1][0] in softletters:
                phones[i] = (softhard_cons[phone[0]] + "j", 0)
            else:
                phones[i] = (softhard_cons[phone[0]], 0)
        if phone[0] in other_cons:
            phones[i] = (other_cons[phone[0]], 0)

def convert_vowels(phones):
    new_phones = []
    prev = ""
    for phone in phones:
        if prev in startsyl:
            if phone[0] in set(u"’яюєї"):
                new_phones.append("j")
        if phone[0] in vowels:
            new_phones.append(vowels[phone[0]] + str(phone[1]))
        else:
            new_phones.append(phone[0])
        prev = phone[0]

    return new_phones

def convert(stressword):
    phones = ("#" + stressword + "#")


    # Assign stress marks
    stress_phones = []
    stress = 0
    for phone in phones:
        if phone == "+":
            stress = 1
        else:
            stress_phones.append((phone, stress))
            stress = 0
    
    # Pallatize
    pallatize(stress_phones)
    
    # Assign stress
    phones = convert_vowels(stress_phones)

    # Filter
    phones = [x for x in phones if x not in others]

    return " ".join(phones)
dic=open('slovar_out.dic','wt')
for line in open("slovar.txt"):
    stressword = line.strip()

    # замена слов на ударения
    for accent in open("ukrdic.txt"):
        accent=accent.replace("\n","")
        wordwa=accent.replace("+","")
        
        if wordwa.strip() == line.strip():
            stressword=accent

            # опишем правила фонетики
            # sproschenny grupi prigolosnih
            stressword=stressword.replace("стс","сс")
            stressword=stressword.replace("здц","зьц")
            stressword=stressword.replace("стд","зд")
            # stressword=stressword.replace("стч","шч")
            stressword=stressword.replace("стц","сьц")
            stressword=stressword.replace("нтст","нст")
            stressword=stressword.replace("нтськ","ньськ")
            # asimilyativni zminy prigolosnih
            stressword=stressword.replace("сш","шш")
            stressword=stressword.replace("зж","жж")
            # блок 
            stressword=stressword.replace("жся","зься")
            stressword=stressword.replace("жсї","зьсї")
            stressword=stressword.replace("жсю","зьсю")
            stressword=stressword.replace("жсі","зьсі")
            stressword=stressword.replace("жсь","зьсь")
            stressword=stressword.replace("жсє","зьсє")

            # блок 
            stressword=stressword.replace("шся","сься")
            stressword=stressword.replace("шсї","сьсї")
            stressword=stressword.replace("шсю","сьсю")
            stressword=stressword.replace("шсі","сьсі")
            stressword=stressword.replace("шсь","сьсь")
            stressword=stressword.replace("шсє","сьсє")

            # блок 
            stressword=stressword.replace("чся","цься")
            stressword=stressword.replace("чсї","цьсї")
            stressword=stressword.replace("чсю","цьсю")
            stressword=stressword.replace("чсі","цьсі")
            stressword=stressword.replace("чсь","цьсь")
            stressword=stressword.replace("чсє","цьсє")
            
            # блок 
            stressword=stressword.replace("жця","зьця")
            stressword=stressword.replace("жцї","зьцї")
            stressword=stressword.replace("жцю","зьцю")
            stressword=stressword.replace("жці","зьці")
            stressword=stressword.replace("жць","зьць")
            stressword=stressword.replace("жцє","зьцє")
            # блок 
            stressword=stressword.replace("шця","сьця")
            stressword=stressword.replace("шцї","сьцї")
            stressword=stressword.replace("шцю","сьцю")
            stressword=stressword.replace("шці","сьці")
            stressword=stressword.replace("шць","сьць")
            stressword=stressword.replace("шцє","сьцє")
            # блок 
            stressword=stressword.replace("чця","цься")
            stressword=stressword.replace("чцї","цьсї")
            stressword=stressword.replace("чцю","цьсю")
            stressword=stressword.replace("чці","цьсі")
            stressword=stressword.replace("чць","цьсь")
            stressword=stressword.replace("чцє","цьсє")

            # блок замени к на г
            stressword=stressword.replace("кб","ґб")
            stressword=stressword.replace("кд","ґд")
            stressword=stressword.replace("кз","ґз")
            stressword=stressword.replace("кд","ґж")
            stressword=stressword.replace("кг","ґг")
            stressword=stressword.replace("кґ","ґґ")

            # блок замени г на х
            stressword=stressword.replace("гт","хт")
            stressword=stressword.replace("гк","хк")

            # блок замени зч
            stressword=stressword.replace("зч","шч")

            # блок замени стч на шч
            stressword=stressword.replace("стч","шч")

            # блок замени ситуація
            stressword=stressword.replace("ія","іья")
            
            # блок замени зш на вначалы
            if stressword.find("зш") == 0:
                stressword=stressword.replace("зш","шш")
            if stressword.find("зш") >= 0:
                stressword=stressword.replace("зш","жш")

            
            word=line.strip(), stressword.replace("+", ""), convert(stressword)
            print (word)
            dic.write (line.strip()+" "+convert(stressword)+"\n")
dic.close()


vowels = {
    u"а" : u"a",
    u"я" : u"a",
    u"у" : u"u",
    u"ю" : u"u",
    u"о" : u"o",
    u"ї" : u"i",
    u"е" : u"e",
    u"є" : u"e",
    u"і" : u"i",
    u"и" : u"y",
}                                

def pallatize(phones):
    for i, phone in enumerate(phones[:-1]):
        if phone[0] in softhard_cons:
            if phones[i+1][0] in softletters:
                phones[i] = (softhard_cons[phone[0]] + "j", 0)
            else:
                phones[i] = (softhard_cons[phone[0]], 0)
        if phone[0] in other_cons:
            phones[i] = (other_cons[phone[0]], 0)

def convert_vowels(phones):
    new_phones = []
    prev = ""
    for phone in phones:
        if prev in startsyl:
            if phone[0] in set(u"'яюєї"):
                new_phones.append("j")
        if phone[0] in vowels:
            new_phones.append(vowels[phone[0]] + str(phone[1]))
        else:
            new_phones.append(phone[0])
        prev = phone[0]

    return new_phones

def convert(stressword):
    phones = ("#" + stressword + "#")


    # Assign stress marks
    stress_phones = []
    stress = 0
    for phone in phones:
        if phone == "+":
            stress = 1
        else:
            stress_phones.append((phone, stress))
            stress = 0
    
    # Pallatize
    pallatize(stress_phones)
    
    # Assign stress
    phones = convert_vowels(stress_phones)

    # Filter
    phones = [x for x in phones if x not in others]

    return " ".join(phones)
for line in open("ukr.txt"):
    stressword = line.strip()

    # замена слов на ударения
    for accent in open("ukrdic.txt"):
        accent=accent.replace("\n","")
        wordwa=accent.replace("+","")
        
        if wordwa.strip() == line.strip():
            stressword=accent
            break

    # опишем правила фонетики
    # sproschenny grupi prigolosnih
    stressword=stressword.replace("стс","сс")
    stressword=stressword.replace("здц","зьц")
    stressword=stressword.replace("стд","зд")
    # stressword=stressword.replace("стч","шч")
    stressword=stressword.replace("стц","сьц")
    stressword=stressword.replace("нтст","нст")
    stressword=stressword.replace("нтськ","ньськ")
    # asimilyativni zminy prigolosnih
    stressword=stressword.replace("сш","шш")
    stressword=stressword.replace("зж","жж")
    # блок 
    stressword=stressword.replace("жся","зься")
    stressword=stressword.replace("жсї","зьсї")
    stressword=stressword.replace("жсю","зьсю")
    stressword=stressword.replace("жсі","зьсі")
    stressword=stressword.replace("жсь","зьсь")
    stressword=stressword.replace("жсє","зьсє")

    # блок 
    stressword=stressword.replace("шся","сься")
    stressword=stressword.replace("шсї","сьсї")
    stressword=stressword.replace("шсю","сьсю")
    stressword=stressword.replace("шсі","сьсі")
    stressword=stressword.replace("шсь","сьсь")
    stressword=stressword.replace("шсє","сьсє")

    # блок 
    stressword=stressword.replace("чся","цься")
    stressword=stressword.replace("чсї","цьсї")
    stressword=stressword.replace("чсю","цьсю")
    stressword=stressword.replace("чсі","цьсі")
    stressword=stressword.replace("чсь","цьсь")
    stressword=stressword.replace("чсє","цьсє")
    
    # блок 
    stressword=stressword.replace("жця","зьця")
    stressword=stressword.replace("жцї","зьцї")
    stressword=stressword.replace("жцю","зьцю")
    stressword=stressword.replace("жці","зьці")
    stressword=stressword.replace("жць","зьць")
    stressword=stressword.replace("жцє","зьцє")
    # блок 
    stressword=stressword.replace("шця","сьця")
    stressword=stressword.replace("шцї","сьцї")
    stressword=stressword.replace("шцю","сьцю")
    stressword=stressword.replace("шці","сьці")
    stressword=stressword.replace("шць","сьць")
    stressword=stressword.replace("шцє","сьцє")
    # блок 
    stressword=stressword.replace("чця","цься")
    stressword=stressword.replace("чцї","цьсї")
    stressword=stressword.replace("чцю","цьсю")
    stressword=stressword.replace("чці","цьсі")
    stressword=stressword.replace("чць","цьсь")
    stressword=stressword.replace("чцє","цьсє")

    # блок замени к на г
    stressword=stressword.replace("кб","ґб")
    stressword=stressword.replace("кд","ґд")
    stressword=stressword.replace("кз","ґз")
    stressword=stressword.replace("кд","ґж")
    stressword=stressword.replace("кг","ґг")
    stressword=stressword.replace("кґ","ґґ")

    # блок замени г на х
    stressword=stressword.replace("гт","хт")
    stressword=stressword.replace("гк","хк")

    # блок замени зч
    stressword=stressword.replace("зч","шч")

    # блок замени стч на шч
    stressword=stressword.replace("стч","шч")
    
    # блок замени зш на вначалы
    if stressword.find("зш") == 0:
        stressword=stressword.replace("зш","шш")
    if stressword.find("зш") >= 0:
        stressword=stressword.replace("зш","жш")

    
    word=line.strip(), stressword.replace("+", ""), convert(stressword)
    print (word)

