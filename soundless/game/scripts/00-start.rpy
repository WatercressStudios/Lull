# SOUNDLESS
# Copyright 2014, Watercress Studios.
# Created for Ludum Dare 31 and its shitty-ass theme.

# Please make sure you have skimmed over the ‘Getting Started’ section of the Ren’Py documentation before editing the script.

# CONTRIBUTORS:
# Electro
# Axium723
# TheDwarfLard
# Luke

# Image declaration.
image bg gen1_day = "images/bg_gen1_day.png"

# Character declaration.
# GENERATION ONE MAIN.
define t = Character('Cornelius Thatcher', color="#33CCFF")
define b = Character('Phineas Barrow', color="#D14719")
define c = Character('Terrence Crenshaw', color="#FFCC00")
define g = Character('Temperance Goodwinson', color="#FF0099")
define s = Character('Ichabod Salisbury', color="#00CC00")
# GENERATION ONE'S CHILDREN
define gt = Character('Grace Thatcher', color="#66CCFF")
# GENERATION TWO MAIN.
define t2 = Character('Alex Thatcher', color="#33CCFF")
define b2 = Character('Kevin Barrow', color="#D14719")
define c2 = Character('Jared Crenshaw', color="#FFCC00")
define g2 = Character('Kathleen Goodwinson', color="#FF0099")
define s2 = Character('Dave Salisbury', color="#00CC00")

# The game begins here.
label start:
    jump scene1
    return
