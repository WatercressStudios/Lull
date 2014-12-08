# SOUNDLESS
# Copyright 2014, Watercress Studios.
# Created for Ludum Dare 31 and its shitty-ass theme.

# Please make sure you have skimmed over the ‘Getting Started’ section of the Ren’Py documentation before editing the script.

# CONTRIBUTORS:
# Electro
# Axium723
# TheDwarfLard
# Luke

# Coder: Kylemsguy

# Note: this VN is divided into Acts and Generations
# Act 1 = Gen 1-4
## add more here

# Image declaration.
## Backgrounds
image bg gen1_day = "images/bg_gen1_day.png"
image bg gen1_night = "images/bg_gen1_night.png"
image bg gen2 = "images/bg_gen2.png"
image bg gen3 = "images/bg_gen3.png"
image bg gen4 = "images/bg_gen4.png"
image bg gen5 = "images/bg_gen5.png"
image bg gen6 = "images/bg_gen6.png"
image bg gen7 = "images/bg_gen7.png"
image bg gen8 = "images/bg_gen8.png"
image bg goodend = "images/bg_gen9_goodend.png"
image bg badend = "images/bg_gen9_badend.png"

## Character Sprites
image TempGood = Image("images/chars/TempGood.png", yalign=0.5)

# Character declaration.
# ACT ONE MAIN.
define t = Character('Cornelius Thatcher', color="#33CCFF")
define b = Character('Phineas Barrow', color="#D14719")
define c = Character('Terrence Crenshaw', color="#FFCC00")
define g = Character('Temperance Goodwin', color="#FF0099")
define s = Character('Ichabod Sedgewood', color="#00CC00")
# GENERATION ONE'S CHILDREN
define gt = Character('Grace Thatcher', color="#66CCFF")
# ACT TWO MAIN.
define t2 = Character('Alex Thatcher', color="#33CCFF")
define b2 = Character('Phineas Barrow VII', color="#D14719")
define c2 = Character('Jared Crenshaw', color="#FFCC00")
define g2 = Character('Kathleen Goodwin', color="#FF0099")
define s2 = Character('Dave Sedgewood', color="#00CC00")

# The game begins here.
label start:
    # Variable declarations (so we can keep track of which vars we are using)
    python:
        unity = 0
        openness = 0
        
        northsouth = 0 
        gen3_success = 0 # whether ppl be ded
        
        # For the below:
        MT = False # Married Temperance (North + Flirt)
        FG = False # Friend of Goodwin (North + Be Respectful)
        FS = False # Friend of Sedgewood (It Doesn't Matter)
        FC = False # Friend of Crenshaw (South + Meat)
        GM = False # True = Got Meat, False = Got Paper

    # Introduction goes here if any
    jump gen1
    
    # uncomment below lines to jump directly to scenes for debug
    #jump gen2
    #return
