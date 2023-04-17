myCarInfo = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1993,
    "mailage": "120k"
}
# print(myCarInfo)
# print(myCarInfo["model"])
myCarInfo["year"] = 2020
myCarInfo["name"]="Opel"
# print(myCarInfo)

myCarInfo = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1993,
    "mailage": "120k"
}

myCarInfo.pop("year")
# myCarInfo.popitem() #It deletes the final item, in this case "mailage"
# print(myCarInfo)
# for x in myCarInfo.keys():
#     print(x)
# for x in myCarInfo.values():
#     print(x)
# for x,y in myCarInfo.items():
#     print(x,y)

for x,y in myCarInfo.items():
    print(str(x) + " is " + str(y))
####################################################### 
myBiography = {
    "city": "Dushanbe",
    "education": "PhD",
    "birth": 1993
}
myBiography["birth"]=1994
myBiography["city"]="Khorog"
myBiography["Village"]="Vrang"
# print(myBiography)

myBiography = {
    "city": "Dushanbe",
    "education": "PhD",
    "birth": 1993
}

# myBiography.pop("education")
# myBiography.popitem()
# print(myBiography)

# for x in myBiography.keys():
#     print(x)

# for x in myBiography.values():
#     print(x)
# for x,y in myBiography.items ():
#     print(x,y)

for x, y in myBiography.items():
    print(str(x)+ " is " + str(y))
