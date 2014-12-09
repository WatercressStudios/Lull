label gen2:
    stop music fadeout 1.0
    # Soundless Melody (Solo Piano)
    play music "snd/soundless-melody-solo-piano.ogg"
    scene bg gen2
    with fade

    "CORNELIUS THATCHER, 1875"

    "I wake to muffled knocking."

    "I don’t answer it-- not yet. I grab my father’s watch off my bedside table."

    "10:07. God have mercy."

    "The 9:30 train’s come and gone, right outside my window, and I never heard a thing. Fourth time this week."

    "I want to scream at the sky, just to prove I can, but hearing half a scream would only frighten me more."

    "Lift your feet. Answer the door. Someone smarter than you will put the world right soon enough."
    
    # if answered North
    if northsouth == 0:
        show TempGood mid at right
        with dissolve
        "I open the door. Temperance Goodwin's on the other side, covering her eyes with her hand."
        
        menu:
            g "You're not decent, are you? Get decent, Cornelius."
            "Flirt":
                $ MT = True

                show CornThat mid at left
                with dissolve
                t "You've never dreamt of seeing me in my long johns, Temperance?"

                g "Cornelius!"

                "Temperance turns red and balls her fists in anger. She realizes a moment too late that she can see me now. She stuffs her fists back over her eyes."

                "I roar with laughter, but quickly stop. Of all the things that just don't sound right anymore, laughter's the worst of them. I start putting on work clothes."
            
            "Be respectful":
                $ FG = True
                
                show CornThat mid at left
                with dissolve
                
                t "Long johns is decent among friends, Temperance."

                "She's rolling her eyes behind her hand, no doubt about it. I start putting on work clothes."
                
                
        "I can tell Temperance is straining her voice to speak at a normal level."

        "For someone who talks about the Lord's will as often as Temperance, she sure can't take a hint that the Lord wants us to be quiet."

        t "Does your boy want to help out at the construction site today? My crew's always glad to have him."

        g "Not today. We're meeting at Barrow's office. To discuss the… thing."

        t "Who's we, and what thing?"

        g "Oh, you know, just some pillars of the community. And you know what thing."
        
        hide TempGood
        with dissolve

        "I do. There's only one thing worth discussing these days."

        "The Recent Change, they call it euphemistically. The Lull, they call it optimistically."

        "A \"Lull\" would end. And ever since the world started going quiet, it has shown no sign of reversing course."
        
        show TempGood mid at right
        with dissolve

        "When we arrive at Barrow's office, a crowd has already gathered."

        t "Just pillars of the community, eh?"

        "Temperance shrugs."

        g "Every good citizen is a pillar, I suppose."

        "The crowd parts as we approach. Every man doffs their cap to Temperance-- she's a teacher, after all, and even grown men never quite lose that fear and respect you have for a schoolmarm."

        "A fair few doff their caps to me as well. It's an honor hard earned; I've built half the houses in this town, and half of those with my own hands."
    
        hide TempGood
        
    elif northsouth == 1:
        show CornThat mid at left
        show TerrCren mid at right
        with dissolve

        "I open the door. Terrence Crenshaw's on the other side, impatiently bouncing his leg up and down like his kneecap's trying to escape."

        c "Still in your long johns, Cornelius? Honestly, I'm worried that bed will swallow you whole one day."

        "He knows as well as I do why the train doesn't wake me anymore. It's rare to hear someone make light of it though. And, to be honest, a bit of a relief."

        "I chuckle, but quickly stop. Of all the things that just don't sound right anymore, laughter's the worst of them. I start putting on work clothes."

        t "Are you going hunting today? I could leave Willet in charge of the construction site if you need an extra rifle."

        c "Another time, gladly, but today duty calls. And by duty I mean Phineas Barrow. He wants a few of us for a meeting."

        "Terrence's voice is unnaturally quiet, and he doesn't bother raising it. I think he likes when people have to lean in and listen close to hear him."

        t "Who's us? And what's this meeting about?"

        c "Us as in a select handful of local notables. And you know what the meeting's about."
        
        hide TerrCren
        with dissolve

        "I do. There's only one thing worth discussing these days."

        "The Recent Change, they call it euphemistically. The Lull, they call it optimistically."

        "A \"Lull\" would end. And ever since the world started going quiet, it has shown no sign of reversing course."
        
        show TerrCren mid at right
        with dissolve

        "When we arrive at Barrow's office, a crowd has already gathered."

        t "A select handful of local notables, I believe you said?"

        c "What can I say? Notability just keeps lowering its standards, apparently."

        "The crowd parts as we approach. Some folks doff their caps to Crenshaw-- his tales of military derring-do have made him a legend down at the tavern."

        "Besides, whenever he comes back from hunting he saves the best cuts of meat for his friends."

        "A fair few doff their caps to me as well. It's an honor hard earned; I've built half the houses in this town, and half of those with my own hands."
    
        hide TerrCren
        
    # northsouth == 3: Doesn't matter
    else:
        show CornThat mid at left
        show IchaSedg mid at right
        with dissolve
        
        "I open the door. Ichabod Sedgewood's on the other side, shuffling his feet nervously. He perks up and gives a toothy grin when he sees me."

        s "Cornelius, m'boy! Is wearing long johns at 10 in the morning some crazy eastern fashion, or are you just getting lazier on me?"

        "He knows as well as I do why the train doesn't wake me anymore. It's rare to hear someone make light of it though. And, to be honest, a bit of a relief."

        t "Don't lose your head over it, Ichabod."

        "I chuckle, but quickly stop. Of all the things that just don't sound right anymore, laughter's the worst of them. I start putting on work clothes. Sedgewood stamps his foot and scowls."

        s "Why do people keep telling me that?"

        "I can tell Sedgewood is straining to speak at a normal level. In fact, he's overcompensating by speaking a little too loud, and a little too desperate."

        t "Does your boy want to help out at the construction site today? My crew's always glad to have him."

        s "Oh, I'll have you teach him honest work one of these days, but right now Mr. Barrow's called a few of us for a meeting."

        t "Who's us? And what's this meeting about?"

        s "Why, just us pillars of the community, of course! Imagine, Pacific Star Railways wants to know what this daft old farmer thinks."

        s "As for what it's about, well, I think you know as well as I do."
        
        hide IchaSedg

        "I do. There's only one thing worth discussing these days."

        "The Recent Change, they call it euphemistically. The Lull, they call it optimistically."

        "A \"Lull\" would end. And ever since the world started going quiet, it has shown no sign of reversing course."
        
        show IchaSedg mid at right
        with dissolve

        "When we arrive at Barrow's office, a crowd has already gathered."

        t "Just pillars of the community, eh?"

        "Ichabod shrugs."

        s "More pillars sprout up every time you look."

        "The crowd parts as we approach. Some folks doff their cap to Ichabod. Plenty of them work his fields, and he puts food on everyone's plate."

        "A fair few doff their caps to me as well. It's an honor hard earned; I've built half the houses in this town, and half of those with my own hands."
        
        hide IchaSedg
    
    show PhinBarr mid at right
    with dissolve
    "Barrow's office smells like sweat. He pumps my hand up and down."

    "His desk is covered in a thick sheet. I gather around it with the others."

    b "Cornelius, my friend. Temperance, Ichabod, Terrence."

    "I look around the desk at the schoolteacher, the farmer, the hunter. Each rigid with all the poise they can muster for the crowds. Each seething with the same fears and doubts as I am."

    b "We have a problem. The same problem as all the world, and yet… problematic in its own way."

    "Barrow whisks the blanket off his desk as if revealing a gift."

    "Beneath is a jumbled mound of bloody flesh. The only way I can tell it used to be a railway worker is from the blue jeans poking out of the bottom."

    b "Mr. Wilmot, ah… well, he missed the 9:30 train, so to speak."

    "Poor Wilmot. Whenever Mrs. Goodwin started humming, he'd start humming the same song half a second behind to mess her up. Made me laugh."

    "Barrow tosses the sheet back over the meat that was Barry Wilmot."

    t "I've noticed the train getting quiet, but he can't have heard it at all."

    b "My thoughts precisely. Mr. Wilmot was neither hard of hearing nor given to drink. There is but one sensible conclusion."

    show TempGood
    
    g "It's getting worse."

    b "Yes. Yes. The newspapers will know tomorrow, but… there have been train collisions as well."

    c "I see where this is going."
    
    hide CornThat
    hide TempGood

    "He pushes himself away from the desk and stalks around us in a circle."

    c "The stock market's in shambles. The railways aren't safe. Nobody knows what's up or down or if they'll be able to hear themselves talk tomorrow."

    show TerrCren mid at left
    c "And Pacific Star is going to leave us in the lurch."

    "Barrow looks miserable."

    b "You've got it all wrong, my friends. Pacific Star isn't abandoning us."

    b "They're. Ah. Well. They're shutting down, I'm afraid."

    "A dense silence falls around the table. Ichabod Sedgewood rushes to fill it by clearing his throat loudly."
    
    hide TerrCren
    show IchaSedg mid at left

    s "We made do before the railway. We'll make do after."

    b "You're honest folk, and you've done right by the company. So I've pulled what strings I had left to pull, and we'll be getting some of their property in the foreclosure."

    show TempGood

    g "A nice caboose for my yard, perhaps?"

    if MT:
        hide IchaSedg
        show CornThat mid at left
        t "You've a nice caboose already, Temperance."

        "She swats me on the arm, hard enough to sting. Ichabod stifles a cackle."
        hide CornThat
        show IchaSedg mid at left
        
    hide IchaSedg
    hide TempGood

    b "Well, Pacific Star had fingers in a lot of pies, so we've got options."

    b "One of my favorites is sitting in a railyard in Kansas now: an entire cancelled shipment of preserved pork. It'll last halfway to forever and it's just the thing to keep a hungry settlement growing."

    show TerrCren mid at left
    c "Sold. Let's take it."

    hide TerrCren
    show IchaSedg mid at left
    s "Hold your horses, boy! What other options do we have?"

    b "Well, this is a strange one, but appropriate given the… ah… circumstances."

    b "The central offices have a lot of paper. A LOT of paper. Fountain pens too. We can have those."

    b "Now, normally I'd say meat beats paper…"

    g "But you're thinking ahead. If things keep going the way they're going, we're going to need paper and pens. Enough to last us lifetimes."

    s "Now, that's just outlandish!"

    show TempGood at center

    g "Ichabod, that's just pattern recognition."

    c "I'm with the farmer. You can't eat paper and you can't starve on silence."

    b "Thatcher?"
    hide IchaSedg
    show CornThat mid at left

    menu:
        c "Come on, Thatcher, let's make this a proper consensus."
        
        "Take the Meat":
            $ GM = True
            t "We need to be prepared, it's true. But we can survive a period of silence while we start making our own paper. We're not in a position to survive a famine."
            
            # IF FRIENDS WITH TEMPERANCE
            if northsouth == 0:
                g "I don't know if it'll be that simple. Without communication, civilization cannot stand."
                g "I trust you'll bear that in mind, Cornelius. I support the group's decision."
                hide CornThat
                show TerrCren mid at left
                c "It's so refreshing to see our schoolmarm listen to reason."
                $ unity += 1

            # IF FRIENDS WITH CRENSHAW
            elif northsouth == 1:
                $ FC = True
                hide TempGood
                show TerrCren mid at center
                g "How shortsighted can you people be? Are we expected to grunt at each other like savages?"
                c "My, my, Cornelius, our schoolmarm is all a-fluster. Perhaps she needs to calm down at home."
                "Mrs. Goodwin balls her fists as if to strike Crenshaw, then forces herself away and storms out of the room without a word."
                $ openness -= 1

            # IF FRIENDS WITH ICHABOD
            else:
                g "How shortsighted can you people be? Are we expected to grunt at each other like savages?"
                hide CornThat
                show IchaSedg mid at left
                s "C'mon, Temperance, we're only trying to be practical."
                g "God have mercy, this town will choke on your practicality."

                b "Well, that settles it. I'll send word to the central office that we'll take the meat."
                b "Let's go outside and tell our town what's what."

        "Take the Paper":
            # GM is not set to true -> GP is true
            $ GM = False
            t "I've seen hunger before, and I hope to never see it again. But a world where we can't communicate with each other… that's a nightmare I never want to face. We'd be animals."
            $ openness += 2

            hide TempGood
            show TerrCren mid at center

            # IF FLIRTING WITH TEMPERANCE
            if MT:
                c "I think my friend Cornelius is rather more taken with the schoolmarm's charms than her logic."

            # IF FRIENDS WITH CRENSHAW
            elif northsouth == 1:
                # you disappointed Crenshaw
                $ FC = False
                c "I never thought you were the sort to be ordered around by a schoolmarm, Cornelius. It's rather a disappointment."
                $ unity -= 1

            # OTHERWISE
            else:
                c "I always rather suspected my friend Cornelius was the sort to be ordered around by a schoolmarm."

            hide CornThat
            show IchaSedg mid at left
            "Sedgewood shuffles his feet and chews his knuckles."
            s "Mr. Barrow, sir? I'd like to change my vote."
            s "My fields are strong, and they'll feed us for years. Better the devil I know-- I'll take the paper."
            "Barrow nods and rubs his hands together."
            b "Well, that settles it. I'll send word to the central office that we'll take the paper."
            b "Let's go outside and tell our town what's what."

    # hide almost everyone leaving Barrow
    hide TerrCren
    hide TempGood
    hide CornThat
    hide IchaSedg
    
    if northsouth != 1:
        "Barrow leads the five of us outside." 
    else:
        # IF TEMPERANCE STORMED OUT
        "Barrow leads the four of us outside."

    "He raises his voice to address our town, and it takes three tries before they can even hear him speak."

    jump gen3