# SOUNDLESS
# Copyright 2014, Watercress Studios.
# Created for Ludum Dare 31 and its shitty-ass theme.

# Please make sure you have skimmed over the ‘Getting Started’ section of the Ren’Py documentation before editing the script.

# CONTRIBUTORS:
# Electro
# Axium723
# TheDwarfLard

# Image declaration.

# Character declaration.
# GENERATION ONE.
define t = Character('Cornelius Thatcher', color="#33CCFF")
define b = Character('Ezekiel Barrow', color="#D14719")
define c = Character('Terrence Crenshaw', color="#FFCC00")
define g = Character('Temperance Goodwinson', color="#FF0099")
define s = Character('Ichabod Salisbury', color="#00CC00")
# GENERATION TWO.
define t2 = Character('Alexander Thatcher', color="#33CCFF")
define b2 = Character('Kevin Barrow', color="#D14719")
define c2 = Character('Jared Crenshaw', color="#FFCC00")
define g2 = Character('Kathleen Goodwinson', color="#FF0099")
define s2 = Character('Dave Salisbury', color="#00CC00")

## Note from Kyle: This file should contain the introduction, and then call the first scene. 
##   Scene 1 should probably belong in 01-scene-name.rpy
## Feel free to rename the files as you see fit, as long as it makes sense

# The game begins here.
label start:
    
    "I emerged out of the wagon to face the morning sun."
    "The rest of the train was still coming to a stop. It'd taken so long to get here, it felt so strange to say that we'd finally reached our destination."
    "I tested the ground by crushing some grass underfoot. Dropping my rucksack, I stretched out and sucked in a breath of fresh air."
    "I could hear chattering voices emerging out behind me as more settlers hopped down from their wagons. It was good to know I was sharing this sight, and I knew the others found it just as wonderful as I did."

    
    b "Hey there, Thatcher. I'd be mighty obliged if you helped unload some o' this in my wagon."
    
    "Turning around, I saw a short man with red hair coming my way. With skinny features and a lanky stance, he hardly looked like a pioneer."
    "I'd talked with him a few times before, whenever the wagon train stopped to rest. Ezekiel Barrow, I remember his name being."
    
    t "I've told you before, sir. You can just call me Cornelius. We're all equals now, out here in the Territories."
    b "Well then, how about helping me out, Cornelius? And call me Ezekiel, if you're so inclined to be intimate."
    
    t "Just lead the way. We're all going to need to look out for each other now."
    t "Take a look at this view, though. Don't you reckon it's the most gorgeous thing you've yet to see."
    
    "Ezekiel and I fell silent for that moment and took in the sight of the prairie."
    "The fresh air, the clear sky, the green grass in the soil. All flooding out around us for as far as we could see."
    "This new frontier was ripe for our settling, and it was here we would build our new lives."
    "This was like our own new world."
    
    b "... So this is Kansas Territory."
    t "We've finally made it."
    
    b "So, are you going to keep looking, or are you going to help out?"
    t "Oh, right. I'll get right on that."
    
    "While unpacking Ezekiel's wagon, I can't help but looking at my surroundings when there's a chance. It's nothing like the desolate wasteland we had heard about."
    
    
    return
