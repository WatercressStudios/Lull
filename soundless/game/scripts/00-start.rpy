# SOUNDLESS
# Copyright 2014, Watercress Studios.
# Created for Ludum Dare 31 and its shitty-ass theme.

# Please make sure you have skimmed over the ‘Getting Started’ section of the Ren’Py documentation before editing the script.

# CONTRIBUTORS:
# Electro
# Axium723
# TheDwarfLard

# Image declaration.
image bg pioneers = "images/bg_pioneers.png"

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
    scene bg pioneers

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
    "It doesn't take too long to finish unpacking and moving his belongings. Despite being well-off, Ezekiel didn't as much as I would have expected with him. Perhaps he thinks that his fame will be enough."
    
    b "Have you seen the others yet? I think I'm all set, but they may require your assistance as well."
    t "Wouldn't hurt to take a look around. You wouldn't happen to know of their whereabouts?"
    
    "I can't believe we've been here for hardly any time at all, yet I don't even know where everyone else is."
    
    b "If I had to guess, they're probably still in their wagons. Hopefully they will be ready to start unpacking and setting up soon. Get a move, why don't you?"
    t "Alright. Until later, Ezekiel."
    
    "Walking towards the wagons, the first person I spot someone with fiery red hair. That would be... Goodwinson? Can't remember her first name. I shout out to her from a small distance."
    
    t "Goodwinson, are you in need of some assistance? We've all got things to unpack, and it'd be best to get it done as soon as possible."
    g "Who would that be? Actually, it doesn't matter that much. I definitely need assistance."
    
    "Oh, that's right. Her vision was pretty bad. It'd be best to announce myself around her in the future."
    
    t "Sorry, it's Thatcher. Cornelius Thatcher."
    g "Alright. You may have heard that my sight isn't so great. Can't be too sure with something like that."
    t "I understand. Where do you need all this moved to?"
    g "Moving everything out of the wagon and off to the side, perhaps 10 feet to the East? That's around where my house is going to be built. Also, you can call me Temperance."
    t "Right away."
    
    "Unpacking Temperance's belongings seems to take much longer than Ezekiel's. That just doesn't seem right. She's not as wealthy and she's certainly on the lanky side."
    "However, I've heard that she's an innovator, so a lot of this could be involved with that."
    
    g "I think that's everything. Thanks for the help, Cornelius."
    t "Any time. We're all in this together, and we all need to be able to get along and work with each other for the settlement to advance."
    
    "Two people are left now. Salisbury and Crenshaw. I haven't spoken to either of them, though I've heard brief mentions of them."
    "Salisbury is a kind man who enjoys helping others. Crenshaw seemed to be quite different. The others said he was on the aggressive side and of a high socioeconomic status. I'll have to see for myself, but he seems like someone whose bad side you don't want to be on."
    "It's probably best to find Salisbury first."
    
    return
