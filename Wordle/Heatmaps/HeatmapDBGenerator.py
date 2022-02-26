import json

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

master_list = []

for length in range(2,16):
    for letter in alphabet:
        for letter_index in range(0,length):
            master_list.append({"length":length,"letter":letter,"index":letter_index,"value":0.0})

with open("wordlist.json","r") as wl:
    word_list = json.load(wl)
    for word in word_list:
        for i,v in enumerate(word):
            d = next(item for item in master_list if item["length"] == len(word) and item["letter"] == v and item["index"] == i)
            d["value"] +=1


with open("heatmaps.json","w") as hm:
    json.dump(master_list,hm)