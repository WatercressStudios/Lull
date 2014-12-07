# SOUNDLESS
# Copyright 2014, Watercress Studios.
# Created for Ludum Dare 31 and its shitty-ass theme.

# Please make sure you have skimmed over the ‘Getting Started’ section of the Ren’Py documentation before editing the script.

# CONTRIBUTORS:
# Electro
# Axium723
# TheDwarfLard

# Image declaration.
image bg gen1_day = "images/bg_gen1_day.png"

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
    scene bg gen1_day

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
     
    "Walking towards the other wagons, I see someone who must be Salisbury. Brown hair, muscular, tanned. That's all the other information going around about him."
    "It's probably best to call out to him and say who I am first to avoid any awkwardness. Anyway, none of us are that familiar with each other."
    
    t "Hello, Salisbury? I'm Cornelius Thatcher. Do you need any assistance?"
    s "Well met, Thatcher! I could indeed use your help. There's a lot to unpack. You wouldn't mind some friendly talking, would you?"
    t "No, not at all. So, what do you think of everything so far?"
    s "Things aren't nearly as bad as I had expected. In all honesty, I can already see this as a home for all of us. We're not finished yet, there's still plenty to do, but if we can all get along, this community will thrive." 
    t "I hear you. As soon as I stepped out of my wagon, I was met with a beautiful vista, the brightly shining sun, and a chance for the opportunity to create a new life for everyone here. Yet, that path will certainly be difficult."
    
    "Salisbury has a moderate amount of belongings to unpack, but the time passes quite quickly while talking. He certainly seems like an amicable person, if a bit a naive."
    
    s "Cornelius, before I forget, you can call me Ichabod. I feel like we're already getting along well enough to cut out the formalities."
    t "Alright, Ichabod, I need to get going now. Crenshaw may need some assistance."
    s "If I may say this: there's something slightly off about Crenshaw. Couldn't specify what, but he doesn't think like the rest of us. It's probably nothing, but perhaps just keep that in mind."
    t "I'll be sure to remember that. Until then, Ichabod."
    s "Goodbye, Cornelius."
    
    "What did Ichabod mean by that? People think differently, but is it going to make that much an impact on myself and everyone else? I don't think so. Crenshaw should be given a fair chance."
    
    "As I walk up to the last wagon, someone, presumably Crenshaw, calls out to me."
    
    c "Who's there? Are you one of the other settlers?"
    t "Yes, Crenshaw, I'm one of the settlers. Thatcher, Cornelius Thatcher. Came over to see if you needed any help with unpacking."
    c "Oh, very well then. You can help, but make sure you don't drop or break anything!"
    t "Why would I even think of doing that? These things are your belongings, it's only right to make sure they stay intact."
    c "You can't be too sure with some people... In any case, the assistance is appreciated." 
    
    "It takes some time to unpack Crenshaw's belongings. He seems to have far more than he needs in multiple areas: suits, shoes, jewelry, etc. I probably shouldn't inquire about that."
    
    c "Before you go, you should at least know my name, if we're all going to be living together. It's Terrence."
    t "Alright, Terrance. I have to get going now, but we'll definitely meet again."
    
    "Terrence Crenshaw didn't seem that different to me, besides the slightly different introduction."
    "Time will have to tell what will become of him, the community, all of us. We can't afford to be going after each other."
    "While we all may be able to get along decently, a lot of us seem wary of the railroad crew in the area."
    
    "The crew has been making a lot of noise over the past few hours, and they seem to be making little to no progress. Even Phineas"
    return
