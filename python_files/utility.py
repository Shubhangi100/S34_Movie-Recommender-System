
import re
#Loading data of user into the user array u 
class User:
    def __init__(self, id, age, sex, occupation, zip):
        self.id = int(id)
        self.age = int(age)
        self.sex = sex
        self.occupation = occupation
        self.zip = zip
        self.avg_r = 0.0

class Dataset:
    def load_users(self, file, u):
        f = open(file, "r")
        text = f.read()
        entries = re.split("\n+", text)
        for entry in entries:
            e = entry.split('|', 5)
            if len(e) == 5:
               u.append(User(e[0], e[1], e[2], e[3], e[4]))
        f.close()