def words(file):
    file=open(file,"r")
    data=file.readlines()
    noWords=0
    for i in data:
        s=i.split(" ")
        noWords+=len(s)
    return noWords
    
def spamOrNot(fileName):
    file=open(fileName,"r")
    data=file.readlines()
    count=0
    l=["Act now! Don’t hesitate!","Click below", "Free access",
    "Additional income", "Click here link", "Free cell phone",
        "Addresses on CD", "Click to remove", "Free consultation",
        "All natural", "Click to remove mailto", "Free DVD",
        "Amazing", "Compare rates", "Free grant money",
        "Apply Online", "Compete for your business", "Free hosting",
        "As seen on", "Confidentially on all orders", 
        "Free installation","Auto email removal", "Congratulations",
        "Free investment","Avoid bankruptcy", "Consolidate debt and credit",
        "Free leads","Be amazed"]
    for i in data:
        for j in l:
            if j.lower() in i or j in i or j in i.lower():
                j=j.split(" ")
                count+=len(j)
    file.close()
    noOfWords = words(fileName)
    percentageOfSpams=count*100/noOfWords
    if(percentageOfSpams >30):
        print("spam!")
    else:
        print("not a spam!")
name=input("enter file name:")
spamOrNot(name)
