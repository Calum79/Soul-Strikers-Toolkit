Hi, thanks for opening this.

Welcome to the Soul Striker Toolkit!

Included in this toolkit is a character initialiser, a spell check calculator, and an advanced 
character sheet.

STEP 1 - TECHNICAL DETAILS:

The first thing you want to do is make sure you have Python installed, since the code for the
character initialiser and the spell save calculator run off python scripts.

Next, for convenience, you can alter the batch files in the data folder to give yourself a 
slightly smoother experience with the character initialiser and the spell check calculator.

When you open the batch file by pressing right click and then 'edit', each batch file should be 
formatted in the following way:
@echo off
"C:\Folder where python is installed\python.exe" "C:\Where the SoulStriker Toolkit is placed\soulstrikers\data\Python Script name.py"
pause

Make sure to alter the paths appropriately!

Now, you can just open the character initialiser and the spell check calculator from the shortcuts 
right next to the character sheet and this text file!


STEP 2 - CHARACTER INITIALISATION AND STAT ALTERING

The first thing you want to do is use the character initialiser to create your character's 
initial stats.

It will first ask you for attribute priority. What this means, is that the program will observe what
attributes you favour the most, to the least, and then assign randomly rolled values (4d6 and sum the
highest 3 values) accordingly.

If you have already made your character up, that's okay!

Go through the process of initialising your character through the character initialiser regardless, 
and just manually override your stats.

To do so, go into the Data folder, and open the CSV file named 'SoulStrikerData1'. This CSV formatted 
file is used to store all of your initial character data.

If somewhere down the line, you want to increase your stats, you can go into the sheet 'SoulStrikerData1' 
within the Character Sheet excel file, and add (or subtract) x amount, by adding '+ x' to the end of the 
formula. You can do the same thing for your skills by adding '+ x' in the skills section of the character
stat sheet.

As you level up, your character's health will increase. You can add any additional manual health rolls
(as the campaign progresses), by going into the Character Sheet Excel file, going into the sheet
'SoulSrikerData1', and adding '+ x' to the end of the formulae in cells C10, C11 and C12.


STEP 3 - THE SPELL CHECK CALCULATOR

This component is very simple. Just give the calculator all the relevant information, and it will
give you a spell check, information regarding damage output, the probability of you succeeding the
spell check, and other minor details.

This spell check calculator doesn't input your spells automatically into your character sheet, so
make sure to input the spell details manually.

Since the spell builder has a lot of nuanced rules and minor details, its always a good idea to run the
specifics of your spell by the DM to make sure that everything is allowed by the rules of the game!
As SoulStrikers becomes more developed, so too will the spell check calculator, and you will (likely)
be made aware as soon as a modified version comes out!

OTHER MATTERS

If you have any concerns about how these programs operate, or if you have any security concerns, all files
in this project is open source, meaning you can just open the python code and inspect through things
yourself. Alternatively, you can send me a message on Discord @ Calum79
If you want to know more about how Soul Strikers operates, feel free to consult the Soul Strikers Handbook
here: https://docs.google.com/document/d/11pBQFM_l9MYS8vv5R0-NpvY-wFeVc7XV9Dblo8z3YLM/edit#heading=h.3g20e8fdt5lf



