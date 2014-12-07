# LULL
# SCENE THREE. 1885.

label gen3:
    scene bg gen3
    with fade
    
    "CORNELIUS THATCHER, 1885"

    gt "Daddy. I heard monsters."

    "Grace signs slowly, but with more and more confidence."
    
    if MT:
        "Her mother spends most of her time teaching adults to sign, but Grace gets lots of practice with her half-brothers."

        "I slump down onto the couch and pull Grace onto my lap."

        "The couch still smells of alcohol from when Phineas Barrow used to sleep there."

        "Then he came home drunk one night too many and my wife turned him out. Died of exposure a year later."

        "Another friend on an ever-longer list. I hear Phineas Jr. has inherited his father's stool at the tavern."

    else:
        "Since her mother died, I've started bringing her to construction sites so I can practice with her during breaks."

        "I point to the sleeping Phineas Barrow. After two years, he's still nesting on our couch, and still making the house reek of alcohol."

        b "Do you mean Phineas?"

        gt "No. Monsters."
        
    b "Tell me about these monsters, Grace."

    gt "Down. Outside. Horse."
    
    # Got Paper
    if not GM:
        "She struggles through the signs, then reaches into her pocket for paper and charcoal."

        "I lay my hand on hers."

        b "Don't use paper, Gracie. Practice the signs."
        
    # Got Meat
    else:
        "She struggles through the signs, then scowls in frustration."

        gt "Paper. Paper."

        b "Sorry, Gracie. No more paper."
    
    b "You should sleep. If you sleep more, you won't need as much food."

    "She kneads her forehead and shakes her head in frustration."

    gt "Have to kill the monsters."

    "Just then, the door-flag starts waving up and down. Grace points at the door and glares at me as if to say See?"
    
    if MT:
        "I slide the view-window open. Temperance waggles her eyebrows at me from the other side of the door."

        "Grace runs to the door, eager to tell her mother about the monsters."

        g "Give mommy a kiss."

        "Grace licks Temperance's cheek. Her face breaks into laughter, though no sound comes out."

        t "Is Crenshaw back?"

        g "He is. Let's get down there before word spreads."
            
    elif FG:
        "I slide the view-window open. Temperance gives me a cheerful wave from the other side of the door."

        "Grace runs to the door, eager to tell Auntie Temperance about the monsters."

        g "Give your auntie a kiss."

        "Grace licks Temperance's cheek. Her face breaks into laughter, though no sound comes out."

        g "Good heavens, is that Phineas Barrow on your couch? I thought you'd gotten rid of that drunk."

        "I shrug. He's a friend."

        t "Is Crenshaw back?"

        g "He is. Let's get down there before that pig eats every last scrap."

    elif FC:
        "I slide the view-window open. Terrence Crenshaw smiles serenely on the other side of the door."

        "Grace runs to the door, eager to tell Uncle Terrence about the monsters."

        c "Ah, Cornelius's little tiger!"

        "Grace bites Crenshaw on the hand. Both their faces break into laughter, though no sound comes out."

        c "My god, Phineas Barrow still lives on your couch? How do you stand the smell?"

        "I shrug. He's a friend."

        t "Back from the hunt?"

        c "I sure am. Let's get to my place before word spreads."
            
    elif FS:
        "I slide the view-window open. Ichabod gives me a cheerful nod from the other side of the door."

        "Grace runs to the door, eager to tell Uncle Ichabod about the monsters."

        s "Ah, my girl! Spare a kiss for an old man."

        "Grace licks Ichabod's cheek. Her face breaks into laughter, though no sound comes out."

        s "Lord almighty, Phineas Barrow is still living on your couch? I don't think you'll ever get that drunk out of here."

        "I shrug. He's a friend."

        t "Is Crenshaw back?"

        s "He is. Let's get down there before word spreads."
    
    # Doesn't Matter in first scene. I don't care either.
    else: 
        "I slide the view-window open. Ichabod gives me a nod from the other side of the door."

        "Grace hovers in the back of the room."

        t "Is Crenshaw back?"

        s "He is. Let's get down there before word spreads."
    
    "Grace tugs my sleeve."

    gt "Food?"

    b "I'm going to get food."

    gt "Food?"

    # Got Meat in Scene 2
    if GM:
        b "If you're really hungry, you can have one pork strip. Just one!"

        "She nods gleefully and charges down to the cellar."
    # Got Paper
    else:
        b "Food soon. Food real soon."

        "She nods and resumes her watch by the door."
        
    "Day breaks over the Crenshaw homestead."

    "A group of Ichabod's farmhands are helping the Crenshaw boys unload game from their mules. Skinny game. Skinny mules."
    
    if not GM:
        "Ichabod hobbles around, scrawling orders on crumpled bits of paper and thrusting them at farmhands."

    # if Got Meat
    else:
        "Ichabod hobbles around, thrusting his hands in farmhands' faces to sign orders."
        
    "Terrence Crenshaw watches from a rocking chair on his front porch. Temperance and I linger on the porch next to him."

    c "Been a while since we've had the old crowd in one place."

    t "Except that bum Barrow."
    
    if MT:
        g "May the Lord rest his soul."

        "Her face briefly wrinkles with guilt."
        
    "Terrence nods to himself slowly, with a reptilian ease."

    c "You know how you tell a predator from prey? With animals, I mean."

    "I shake my head."

    c "Predators have eyes forward. Focused on one target. Like humans."

    c "Prey have eyes on the sides of their head. Sensing all around. Like cattle."

    c "Not a hard and fast rule. But the same goes for sound. Prey needs to sense all around to stay safe. No sound… bad to be prey."

    c "Good to be a predator, right? Wrong. Predators eat all the prey. Predators starve. Bad everywhere."

    c "Even insects have gone funny since sound went away. Ask Ichabod. Bad for crops, too. In the country folks starve. In the city folks riot, then starve."

    c "I'm a hunter, Cornelius. I'm a predator. But we live in a time of too many predators and not enough prey."

    "Down in front of the house, Ichabod's face bends into a mute scream. His hands thrash, first in half-formed signs, then in furious nonsense."

    c "Lecture concluded. Now for the object lesson."

    "Temperance and I peer over the bannister and spot the last animals lashed to the mules: two humans, their chests pitted with shot."

    s "DAMN FUCK WHY WHO KILL"

    c "You're not making any sense, Ichabod. Write it out."

    "Crenshaw holds up a slate and chalk. Sedgewood storms up towards the porch, but two of the Crenshaw boys block the steps."

    "Crenshaw passes the slate over the railing. Sedgewood scrawls a single word."

    s "EXPLAIN"

    c "Your farmhands went bandit, Ichabod. They attacked my boys."

    s "LIE"

    c "Well, they were out in the wilds, armed with your guns… how could such a thing be?"

    c "I trust you wouldn't send them out to poach. So I can only assume they went bandit."

    s "NO"

    c "I've lost a son to bandits. Plenty of people in town have. Imagine what they'll think."

    "Sedgewood breathes deeply and fiddles with his hands, feeling out his next words. He sets down the slate."

    s "Not bandits. I asked them for meat."

    "Crenshaw stands, leaning on the railing to support his bum leg. He sneers down at Ichabod Sedgewood like a disappointed god."

    c "Even worse. Bandits kill some people. Poachers kill everyone."

    c "I hunt. Not you. Not your farmhands. Me. Overhunting means we all starve."

    s "We are all starving, and nobody can hunt but you? Ridiculous."

    c "So says Ichabod Sedgewood, the man who owns every patch of farmland from the Pacific to the horizon."

    "Sedgewood makes a forceful gesture, and suddenly half a dozen farmhands are staring at Crenshaw down shotgun sights. Angus and Brady Crenshaw draw revolvers. Millicent Crenshaw leans out of an upstairs window with an old rifle."

    s "Temperance. Cornelius. You need to go."

    "I don't need to be told twice. I help Temperance climb the railing and then vault over it myself."

    c "I asked them here to bear witness, Ichabod. Respected, beloved… they will tell of what you do here."

    s "Good. Let nobody doubt that Ichabod Sedgewood looks after his own."

    if MT:
        "And then Temperance Goodwin Thatcher steps forward, and without signing a word, walks between the rows of pointed guns."
    else:
        "And then Temperance Goodwin steps forward, and without signing a word, walks between the rows of pointed guns."
    
    # meaning: 1 = success, 0 = failure, -1 = crenshaw failure
    $ gen3_success = 0
    menu:
        "Fool that I am, I follow her."
        
        "Appeal to their sense of reason":
            t "There's only one thing any of us want here, and that's to not starve!"
            t "You think killing our town's farmers will help that? Or killing our hunters?"
            t "Put down your guns before your damnfool pride kills us all."
            if openness >= 1:
                $ gen3_success = 1
        "Appeal to their community spirit":
            t "Goddamnit, you two, how long have we all known each other?"
            t "We've laughed over drinks and argued over dinner for two decades now."
            t "We built this town from the ground up. I refuse to believe this is how it all ends."
            if unity >= 1:
                $ gen3_success = 1
        "Plead with Sedgewood":
            t "Ichabod, I'm begging you, don't do this."
            t "You'll have justice for the boys. But you'll have it in court."
            t "Don't ask more of your friends to die tonight."
            if FS:
                $ gen3_success = 1
        "Plead with Crenshaw":
            t "Terrence, I'm begging you, don't do this."
            t "You did what you had to. The town will understand."
            t "Go back inside. I don't want to see you bury any more sons."
            $ gen3_success = -1
            
    if gen3_success > 0:
        $ unity += 1
        "Ichabod's mouth opens and he tries to say something to me. He tries to speak again. And then he crumbles in on himself."

        s "Yes. No more."

        "He jabs two signs at Crenshaw."

        s "Another day."
        
        if MT:
            "Once the Crenshaw homestead is a speck in the distance, I take Temperance in my arms and hold her for a long time."

            "When I get home, Grace is still keeping watch on the door."

            t "No monsters, Gracie. Just friends coming home."
            
            if GM: # got meat
                "Grace shakes her head and taps her foot impatiently."

                gt "Have to kill the monsters."
            else:
                gt "Food?"

                "I promised Grace food. Lord have mercy, I promised I'd bring back food."
    else: #failure
        $ unity -= 1
        if gen3_success == -1:
            if not FC:
                "Crenshaw's bum leg trembles. He slumps back into his rocking chair."
                c "I asked you here to witness, Cornelius. It's time for you to go."
            else:
                "Crenshaw's bum leg trembles. He slumps back into his rocking chair."
                c "Of course, Cornelius. You are right. I must think of my family."
                c "Ichabod. Listen to our friend. Let us settle this in court, like civilized people."

            "Ichabod gives him a sad smile."
            s "They're my boys, Terrence. Love 'em like my own sons."
        
        "I grab Temperance by the arm and put every ounce of strength into my legs."

        "As I glance back, the morning sun outshines the flash of a dozen muzzles. Without the crack of gunfire, the Sedgewoods and the Crenshaws look like children acting out a play battle."

        "When I look away, I can almost convince myself that my old friends will dust themselves off and stand back up again."

        if not GM:
            # we should probably have a pause here /Kyle
            "I promised Grace food. Lord have mercy, I promised I'd bring back food."
    
    jump gen4
