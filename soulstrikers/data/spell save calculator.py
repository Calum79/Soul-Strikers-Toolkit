import csv
import math
import random
filename = 'SoulStrikerData1.csv'
data = []
myAttributes = ['strength', 'arcana', 'survivability', 'defence', 'intelligence', 'agility', 'judgement', 'charisma']
input_varSTR = ''
input_varINT = 0
tempINT1 = 0
tempINT2 = 0
spell_check = 0
tempSTR = ''
severity = ''
spelltype = ''


# implementing an easy attribute increase system

def att_increase(name, val):
    tempint1 = 0
    tempint2 = int(0)
    while tempint1 < 8:
        if data[tempint1][0] == name:
            tempint2 = int(data[tempint1][1])
            tempint2 = int(tempint2)
            tempint2 += val
            data[tempint1][1] = tempint2
        tempint1 += 1


# defining severity by class

class Severity:

    def __init__(self, sev_type, dmgdice, scmodifier, order):
        self.sev_type = sev_type
        self.dmgdice = dmgdice
        self.scmodifier = scmodifier
        self.order = order

    def __repr__(self):
        return f"Attribute({self.sev_type!r}, {self.dmgdice!r}, {self.scmodifier!r}, {self.order!r})"

    def __iter__(self):
        return iter([self.sev_type, self.dmgdice, self.scmodifier, self.order])

miniscule = Severity('miniscule', 4, 2, 1)
light = Severity('light', 6, 4, 2)
medium = Severity('medium', 8, 6, 3)
heavy = Severity('heavy', 12, 8, 4)
severe = Severity('severe', 20, 10, 5)
deadly = Severity('deadly', 100, 12, 6)

mySeverities = [miniscule, light, medium, heavy, severe, deadly]


with open(filename, 'r', newline="") as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:

        data.append([row['stat'], row['score']])
        # print(row['stat'], row['score'])

i = 0
while i < 32:
    data[i][1] = int(data[i][1])
    i += 1

# print(data)

# modifiers
i = 1
j = 0
k = 1

if data[80][1] == 'innovator':
    data[4][1] += 2
elif data[80][1] == 'cursed':
    input_varSTR = input('Input attribute you want to disadvantage')
    while i > 0:
        if input_varSTR.lower() in myAttributes:
            while j == 0:

                # print(data[k-1][0])
                if data[k-1][0] == input_varSTR.lower():
                    j = k
                k += 1

            # print(f'{data[j-1][0]},{data[j-1][1]}')
            tempINT1 = data[j-1][1]
            tempINT1 = int(tempINT1)
            tempINT1 -= 2
            data[j-1][1] = tempINT1
            i = 0
            # print(f'{data[j][0]},{data[j][1]}')

        else:
            print('attribute not found')

i = 0

match data[79][1]:
    case 'shifter':
        att_increase('arcana', 1)
        att_increase('agility', 2)
    case 'duelist':
        att_increase('strength', 1)
        att_increase('survivability', 2)
    case 'artillerist':
        att_increase('intelligence', 1)
        att_increase('arcana', 2)
    case 'pact':
        att_increase('survivability', 1)
        att_increase('strength', 2)
    case 'warlock':
        att_increase('intelligence', 1)
        att_increase('arcana', 2)
    case 'brute':
        att_increase('defence', 1)
        att_increase('strength', 2)
    case 'carnage':
        att_increase('charisma', 1)
        att_increase('survivability', 2)
    case 'strategist':
        att_increase('judgement', 1)
        att_increase('intelligence', 2)
    case 'blessed':
        att_increase('', 0)
        att_increase('', 0)
    case 'expanse':
        att_increase('', 0)
        att_increase('', 0)

lvl = input("Input current player level")
prof_bonus = 1 + math.floor(int(lvl)/3)
spell_save = 8 + data[1][1] + prof_bonus
dmg_output = ''


# defining adjusted attribute scores

class Adj_Attribute:

    def __init__(self, att_type, att_original, att_adjusted):
        self.att_type = att_type
        self.att_original = att_original
        self.att_adjusted = att_adjusted

    def __repr__(self):
        return f"Attribute({self.att_type!r}, {self.att_original!r}, {self.att_adjusted!r})"

    def __iter__(self):
        return iter([self.att_type, self.att_original, self.att_adjusted])

strength = Adj_Attribute('strength', int(data[0][1]), math.floor((int(data[0][1]) - 10)/2))
arcana = Adj_Attribute('arcana', int(data[1][1]), math.floor((int(data[1][1]) - 10)/2))
survivability = Adj_Attribute('survivability', int(data[2][1]), math.floor((int(data[2][1]) - 10)/2))
defence = Adj_Attribute('defence', int(data[3][1]), math.floor((int(data[3][1]) - 10)/2))
intelligence = Adj_Attribute('intelligence', int(data[4][1]), math.floor((int(data[4][1]) - 10)/2))
agility = Adj_Attribute('agility', int(data[5][1]), math.floor((int(data[5][1]) - 10)/2))
judgement = Adj_Attribute('judgement', int(data[6][1]), math.floor((int(data[6][1]) - 10)/2))
charisma = Adj_Attribute('charisma', int(data[7][1]), math.floor((int(data[7][1]) - 10)/2))

myadj_attributes = [strength, arcana, survivability, defence, intelligence, agility, judgement, charisma]


# spell name

spell_name = input('Please input the name of the spell')


# spell severity

i = 1
j = 0
while i > 0:
    input_varSTR = input('Please input the spell severity.')
    for sev in mySeverities:

        if sev.sev_type == input_varSTR.lower():
            severity = sev
            j += 1
            spell_check += sev.scmodifier
            dmg_output = f'{random.randint(1,sev.dmgdice)}d{sev.dmgdice}'

    if j == 0:
        print('Please input a valid severity.')

    else:
        i = 0


# spell type

class spell:

    def __init__(self, spell_type, scaling, scmod):
        self.spell_type = spell_type
        self.scaling = scaling
        self.scmod = scmod

    def __repr__(self):
        return f"Attribute({self.spell_type!r}, {self.scaling!r}, {self.scmod!r})"

    def __iter__(self):
        return iter([self.spell_type, self.scaling, self.scmod])

physical = spell('physical', strength, 2)
projectile = spell('projectile', judgement, 2)
movement = spell('movement', 'NA', 4)
status = spell('status', arcana, 8)
area = spell('area', judgement, 5)
summon = spell('summon', survivability, 7)
enhancement = spell('enhancement', arcana, 5)
necrotic = spell('necrotic', survivability, 8)
transformation = spell('transformation', strength, 6)
healing = spell('healing', survivability, 0)
illusion = spell('illusion', arcana, 4)
trap = spell('trap', intelligence, 5)
transmutation = spell('transmutation', intelligence, 6)

mySpells = [physical, projectile, movement, status, area, summon, enhancement, necrotic, transformation, healing,
            illusion, trap, transmutation]

def_spells = ['physical', 'projectile', 'area', 'healing', 'trap']


# !!!!! go over with mic since the character sheet doesn't document stuff well
i = 1
j = 0
while i > 0:
    input_varSTR = input('Please input the spell type.')

    for spl in mySpells:
        if input_varSTR.lower() == spl.spell_type:

            if input_varSTR.lower() in def_spells and input_varSTR.lower() != 'healing':
                tempSTR = f'Damage = {dmg_output}+{spl.scaling.att_adjusted}'
                dmg_output = tempSTR
                i = 0

            elif input_varSTR.lower() in def_spells and input_varSTR.lower() == 'healing':
                tempSTR = f'Healing = {dmg_output}+{spl.scaling.att_adjusted}'
                dmg_output = tempSTR

            else:
                match input_varSTR.lower():
                    case 'movement':
                        dmg_output = f'Movement = {5 * severity.order}ft'
                        i = 0

                    case 'status':
                        dmg_output = f'Damage per tick = {1 * severity.order}'
                        i = 0

                    case 'summon':
                        dmg_output = f'Summon HP = {random.randint(1,severity.dmgdice)}d10 + ' \
                                     f'{2 * severity.order + spl.scaling.att_adjusted + prof_bonus} ' \
                                     f'and Summon Dmg = 1d{severity.dmgdice}'

                        i = 0

                    case 'enhancement':
                        dmg_output = f'Enhancement to stat of {1 * severity.order + spl.scaling.att_adjusted}'
                        i = 0

                    case 'necrotic':
                        dmg_output = f'Damage = {random.randint(1,severity.dmgdice) + random.randint(1,severity.dmgdice) + random.randint(1,severity.dmgdice) }' \
                                     f'd{severity.dmgdice} + {2 * severity.order + spl.scaling.att_adjusted}'
                        i = 0

                    case 'transformation':
                        dmg_output = f'Damage = {random.randint(1,severity.dmgdice) + random.randint(1,severity.dmgdice)}' \
                                     f'd{severity.dmgdice} + {2 * severity.order + spl.scaling.att_adjusted}'
                        i = 0

                    case 'illusion':
                        dmg_output = f'Illusion intensity = {severity.sev_type} intensity'
                        i = 0

                    case 'transmutation':
                        dmg_output = f'Consult the item guide for exact damage'
                        i = 0

            spelltype = input_varSTR.lower()
            spell_check += spl.scmod

    if i == 1:
        print('Input valid spell type.')


# asking for additional status application

i = 1
j = 0
add_status = False
if spelltype != 'status':
    while i > 0:
        input_varSTR = input('Are you adding an additional status effect? (type "yes" or "no")')

        if input_varSTR.lower() == 'yes':
            input_varSTR = input('What status effect would you like?')
            tempSTR = f'{dmg_output} + {input_varSTR.lower()}'
            dmg_output = tempSTR
            spell_check += 2
            add_status = True
            i = 0

        elif input_varSTR.lower() == 'no':
            i = 0

        else:
            print('Please enter a valid response')


# range

spell_range = ''

input_varINT = input('Input spell range as a number, i.e. omit "ft"')
spell_range = f'Spell range = {input_varINT}ft'
spell_check += math.floor((int(input_varINT))/10)


# cast time

cast_time = ''

input_varINT = input('Input cast time as a number, i.e. omit "turns"')
Cast_time = f'Cast time = {input_varINT}ft'
spell_check -= max(0, (int(input_varINT)) - 1)


# check for requirement

i = 1
while i > 0:
    input_varSTR = input('Is your spell an Instant cast or a Reaction cast? (type "yes" or "no")')
    if input_varSTR.lower() == 'yes':
        spell_check += 2
        i = 0
    elif input_varSTR == 'no':
        i = 0
    else:
        print('Please enter a valid response')


# active duration

active_duration = 0
if add_status == True or spelltype == 'status' or spelltype == 'summon':
    input_varINT = input('Input status active duration as a number, i.e. omit "turns"')
    active_duration = input_varINT
    input_varINT = int(input_varINT)
    spell_check += max(0, input_varINT - 3)


# target type
targ_type = ''
target_dict = {'single': 1, 'multi':2, 'chain': 3, 'area':2}
i = 1
while i > 0:
    input_varSTR = input('Input the target type')

    if input_varSTR in target_dict:
        spell_check += target_dict[input_varSTR]
        targ_type = input_varSTR

        i = 0

    else:
        print('target type not found')

print(f'Your spell, {spell_name}, has a spell check is {spell_check}')
print(f'The spell details are: Spell type = {spelltype}, {dmg_output}, {spell_range}, {cast_time}, '
      f'Active duration = {active_duration} turns, target type = {targ_type}')
print(f'Since you have an arcana bonus of {arcana.att_adjusted}, you have a'
      f' {max(0,round(100 * (1 - (spell_check - arcana.att_adjusted)/20) , 1))}% chance of succeeding the spell check')










