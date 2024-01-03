import csv
import random

temp_counter1 = 0
temp_counter2 = 0
numlist_t1 = []
numlist_t2 = []
num_temp = 0
input_varSTR = ""
input_varINT = 0
attribute_limit = 8


# defining the attributes through class

class Attribute:

    def __init__(self, att_type):
        self.att_type = att_type
        self.value = 0
        self.priority = 0
        self.wasSet = False

    def __repr__(self):
        return f"Attribute({self.att_type!r}, {self.value!r}, {self.priority!r}, {self.wasSet})"

    def __iter__(self):
        return iter([self.att_type, self.value, self.priority, self.wasSet])

strength = Attribute('strength')
arcana = Attribute('arcana')
survivability = Attribute('survivability')
defence = Attribute('defence')
intelligence = Attribute('intelligence')
agility = Attribute('agility')
judgement = Attribute('judgement')
charisma = Attribute('charisma')

myAttributes = [strength, arcana, survivability, defence, intelligence, agility, judgement, charisma]

for att in myAttributes:
    att.priority = 0
    att.value = 0

# print(f"{strength.att_type},{strength.value},{strength.priority},{strength.wasSet}")


    # __init__(Attribute, 'strength')
    # __init__(Attribute, 'arcana')

    # print(f"{__repr__(Strength())}")
    # print(f"{list(my_Attributes.priority())}")


def AttSort(order):

    for attr in myAttributes:
        if attr.priority == order:
            return attr.att_type
        # return " "


# defining races through class. If this looks like a last minute implementation, that's because it was lol

class Race:

    def __init__(self, race_type, hitdice, movement, weightclass):
        self.race_type = race_type
        self.hitdice = hitdice
        self.movement = movement
        self.weightclass = weightclass

    def __repr__(self):
        return f"Attribute({self.race_type!r}, {self.hitdice!r}, {self.movement!r}, {self.weightclass})"

    def __iter__(self):
        return iter([self.race_type, self.hitdice, self.movement, self.weightclass])

terran = Race('terran', 8, 30, 5)
elven = Race('elven', 8, 30, 6)
cybr = Race('cybr', 10, 35, 8)
siren = Race('siren', 6, 30, 4)
hound = Race('hound', 12, 45, 10)
spectre = Race('spectre', 10, 40, 6)
fae = Race('fae', 6, 50, 2)
warden = Race('warden', 12, 25, 10)
hive = Race('hive', 12, 30, 3)
gelatinous = Race('gelatinous', 10, 30, 2)
shrike = Race('shrike', 6, 45, 5)
planetarian = Race('planetarian', 0, 0, 0)
vixen = Race('vixen', 0, 0, 0)
avtr = Race('avtr', 0, 0, 0)
celestite = Race('celestite', 0, 0, 0)
imp = Race('imp', 0, 0, 0)
vultra = Race('vultra', 0, 0, 0)

my_races = [terran, elven, cybr, siren, hound, spectre, fae, warden, hive, gelatinous, shrike, planetarian, vixen, avtr,
            celestite, imp, vultra]

# all placeholder lists

v_list = ['strength', 'arcana', 'survivability', 'defence', 'intelligence', 'agility', 'judgement', 'charisma']

r_list = ['terran', 'elven', 'cybr', 'siren', 'hound', 'spectre', 'fae', 'warden', 'hive', 'gelatinous', 'shrike']

r_dict = {'terran': 8, 'elven': 8, 'cybr': 10, 'siren': 6, 'hound': 12, 'spectre': 10, 'fae': 6, 'warden': 12,
          'hive': 12,
          'gelatinous': 10, 'shrike': 6, 'planetarian': 10, 'vixen': 8, 'avtr': 6, 'celestite': 12, 'imp': 8,
          'vultra': 8}

skill_dict = {'animal handling': 0, 'athletics': 0, 'disguise': 0, 'history': 0, 'insight': 0, 'intimidation': 0,
              'investigation': 0, 'medicine': 0, 'nature': 0, 'perception': 0, 'performance': 0, 'persuasion': 0,
              'religion': 0, 'sleight of hand': 0, 'stealth': 0, 'bartering': 0, 'computers': 0, 'deception': 0,
              'leadership': 0, 'faith': 0, 'translation': 0}

dict_lists = {'strength': 0, 'arcana': 0, 'survivability': 0, 'defence': 0, 'intelligence': 0, 'agility': 0,
              'judgement': 0, 'charisma': 0}

a_dict = {'shifter': 0, 'duelist': 0, 'artillerist': 0, 'pact': 0, 'warlock': 0, 'brute': 0, 'carnage': 0,
          'strategist': 0, 'blessed': 0, 'expanse':0}

p_dict = {'citizen': 0, 'devoutest': 0, 'peasant': 0, 'bounty hunter': 0, 'lab rat': 0, 'scientist': 0, 'thief': 0,
          'folk hero': 0, 'military': 0, 'cursed': 0, 'peace keeper': 0, 'cultist': 0, 'con artist': 0, 'merchant': 0,
          'spokesman': 0, 'innovator': 0, 'doctor': 0, 'detective': 0}

header = ["stat", "score"]
data = [['strength', 0], ['arcana', 0], ['survivability', 0], ['defence', 0], ['intelligence', 0],
        ['agility', 0], ['judgement', 0], ['charisma', 0], ['hp1', 0], ['hpPATRON', 0], ['hpHIVECORE', 0],
        ['animal handling', 0], ['athletics', 0], ['disguise', 0], ['history', 0], ['insight', 0], ['intimidation', 0],
        ['investigation', 0], ['medicine', 0], ['nature', 0], ['perception', 0], ['performance', 0], ['persuasion', 0],
        ['religion', 0], ['sleight of hand', 0], ['stealth', 0], ['bartering', 0], ['computers', 0], ['deception', 0],
        ['leadership', 0], ['faith', 0], ['translation', 0], ['shifter', 0], ['duelist', 0], ['artillerist', 0],
        ['pact', 0], ['warlock', 0], ['brute', 0], ['carnage', 0], ['strategist', 0], ['citizen', 0], ['devoutest', 0],
        ['peasant', 0], ['bounty hunter', 0], ['lab rat', 0], ['scientist', 0], ['thief', 0], ['folk hero', 0],
        ['military', 0], ['cursed', 0], ['peace keeper', 0], ['cultist', 0], ['con artist', 0], ['merchant', 0],
        ['spokesman', 0], ['innovator', 0], ['doctor', 0], ['detective', 0], ['terran', 0], ['elven', 0], ['cybr', 0],
        ['siren', 0], ['hound', 0], ['spectre', 0], ['fae', 0], ['warden', 0], ['hive', 0], ['gelatinous', 0],
        ['shrike', 0], ['planetarian', 0], ['vixen', 0], ['avtr', 0], ['celestite', 0], ['imp', 0], ['vultra', 0],
        ['race_type', ''], ['hit_dice', 0], ['movement', 0], ['weight_class', 0], ['archetype', ''], ['pantheon', 0],
        ['blessed', 0], ['expanse', 0]]


# rolling the character attribute numbers

i = 0
j = 0
while i < 8:

    while j < 4:
        numlist_t2.append(random.randint(1, 6))
        j += 1

    numlist_t2.sort()
    num_temp = (numlist_t2[1] + numlist_t2[2] + numlist_t2[3])
    numlist_t1.append(num_temp)

    numlist_t2 = []
    num_temp = 0
    i += 1
    j = 0

numlist_t1.sort()
# print(numlist_t1)

# assigning attribute priority

attribute_limit = 8
while attribute_limit > 0:



    input_varSTR = input(f"Input which attribute whose priority you'd like to set. The current priority order is: "
                         f"1.{AttSort(1)}, "
                         f"2.{AttSort(2)}, "
                         f"3.{AttSort(3)}, "
                         f"4.{AttSort(4)}, "
                         f"5.{AttSort(5)}, "
                         f"6.{AttSort(6)}, "
                         f"7.{AttSort(7)}, "
                         f"8.{AttSort(8)}. "
                         "Please note that 1 is the highest priority attribute, and 8 is the least priority attribute."
                         f"You have {attribute_limit} Attributes to go.")

    if input_varSTR.lower() in v_list:
        j = 1

        while j > 0:
            input_varINT = input(f"What priority would you like {input_varSTR} to have?")

            if 0 < int(input_varINT) < 9:

                for att in myAttributes:

                    if att.priority == int(input_varINT):
                        att.priority = 0
                        att.wasSet = False

                for att in myAttributes:

                    if att.att_type == input_varSTR.lower():
                        att.priority = int(input_varINT)
                        att.wasSet = True

                j = 0

            else:
                print("Please enter a valid priority position, i.e. between 1 and 8.")

    else:
        print(
            "Attribute not found. Make sure your spelling is correct."
            "Refer to the excel spreadsheet for appropriate spelling."
            "Also make sure you haven't input an attribute twice. "
            "This is not case sensitive")

    k = 0
    for att in myAttributes:
        if not att.wasSet:
            k += 1
    attribute_limit = k

    for att in myAttributes:
        if att.priority > 0:

            att.value = numlist_t1[8 - int(att.priority)]
            # print(f"type:{att.att_type}, val:{att.value}, priority:{att.priority}, wasSet:{att.wasSet}")


# assigning Attribute data to data list

i = 0
j = 0
while i < 8:

    for key in dict_lists:

        while j < 8:

            if data[j][0] == key:

                data[j][1] = dict_lists[key]
                i += 1

            j += 1

        j = 0


i = 0
j = 0
while i < 8:

    for att in myAttributes:

        while j < 8:

            if data[j][0] == att.att_type:
                data[j][1] = att.value
                i += 1
            j += 1
        j = 0


# assign character race

i = 0
while i < 1:

    input_varSTR = input("Please enter your character's race")

    if input_varSTR.lower() in r_list:

        data[8][1] = random.randint(1, r_dict[input_varSTR.lower()])
        if input_varSTR.lower() == 'hive':
            data[10][1] = random.randint(1, 12)
        data[9][1] = random.randint(1, 10)
        i = 1

    else:

        print("Race not found, please enter a valid race.")

# assigning race into the data list

for key in r_list:
    i = 0
    while i < 17:
        # print(f"{data[i + 58][0]},{key},{input_varSTR.lower()}")
        if data[i + 58][0] == key and input_varSTR.lower() == key:
            data[i + 58][1] = 1
        i += 1

for race in my_races:
    if race.race_type == input_varSTR.lower():
        data[75][1] = race.race_type
        data[76][1] = race.hitdice
        data[77][1] = race.movement
        data[78][1] = race.weightclass
        print(f"{data[75]},{data[76]},{data[77]},{data[78]}")


# assigning skills

skill_limit = 20
while skill_limit > 0:

    input_varSTR = input(
        "Choose a skill you'd like to allocate points to. If you want to reset your allocation, type reset")

    if input_varSTR.lower() in skill_dict:

        input_varINT = input(
            f"Choose how many skill points you'd like to allocate to {input_varSTR.lower()}. "
            f"You have {skill_limit} points left.")

        if 20 >= skill_limit - int(input_varINT) >= 0:
            skill_dict[input_varSTR.lower()] += int(input_varINT)
            skill_limit -= int(input_varINT)

        else:
            print(f"You had {skill_limit} points left, but you used {int(input_varINT)}!")

    elif input_varSTR.lower() == "reset":

        for key in skill_dict:
            skill_dict[key] = 0
            skill_limit = 20

    else:
        print("Skill not found, please enter a valid skill. Using spaces is fine.")


# assigning archetype

i = 1
while i > 0:

    input_varSTR = input('Please enter your Archetype. Please omit the "the " when typing your response')
    if input_varSTR.lower() in a_dict:

        for a in a_dict:
            a_dict[a] = 0

        a_dict[input_varSTR.lower()] = 1
        data[79][1] = input_varSTR.lower()
        i = 0

    else:
        print("Please enter a valid Archetype")


# assigning pantheon

i = 1
while i > 0:

    input_varSTR = input('Please enter your Pantheon.')
    if input_varSTR.lower() in p_dict:

        for p in p_dict:
            p_dict[p] = 0

        p_dict[input_varSTR.lower()] = 1
        data[80][1] = input_varSTR.lower()
        i = 0

    else:
        print("Please enter a valid Pantheon")


# writing skills, pantheon and archetype data to the data list

i = 0
for skill in skill_dict:
    i = 0

    while i < 21:

        if data[i + 11][0] == skill:
            data[i + 11][1] = skill_dict[skill]
        i += 1

i = 0
for key in a_dict:
    i = 0
    if key == 'blessed' and data[79][1] == 'blessed':
        data[81][1] = 1
    if key == 'expanse' and data[79][1] == 'expanse':
        data[82][1] = 1

    while i < 8:

        if data[i + 32][0] == key:
            data[i + 32][1] = a_dict[key]
        i += 1

for key in p_dict:
    i = 0
    while i < 18:

        if data[i + 40][0] == key:
            data[i + 40][1] = p_dict[key]
        i += 1


# writing data to CSV format

filename = 'SoulStrikerData1.csv'

with open(filename, 'w', newline="") as file:
    csvwriter = csv.writer(file)
    csvwriter.writerow(header)
    csvwriter.writerows(data)