label scene1:
    scene bg gen1_day

    # TODO: center this line
    "CORNELIUS THATCHER, 1865"
    
    "Barrow hands me the spike."
    "He straightens up and mugs for the crowd. A smaller crowd than he wanted, but they cheer so loud you can almost hear their lungs straining."

    b "You look nervous, friend. Afraid I’ll hit your fingers?"

    "Barrow looms over me with a hammer. I smile to reassure him."
    "The man’s been good to me. His paychecks have been even better."

    t "Never liked crowds, sir."
    b "Call me Phineas. We’re all equals out here in the territories."
    t "Yes, sir."
    b "We’re in this together, so don’t flinch. I’d look a damn fool breaking my best foreman’s hand!"
    b "Ready?"
    t "Been ready for years, sir."
    
    "He brings the hammer down on the spike, and the clang shakes the trees."
    "I have to keep my jaw clenched so my teeth don’t rattle out of my skull."
    "The clang echoes through the valley, and is slowly drowned out by the joyful crowd."

    b "I hereby declare the Snake River Rail Line OPEN!"

    "After everyone’s shouted their throats hoarse, Mr. Barrow grabs me by the collar and steers me into the new tavern, through snug pine doors that don’t even creak yet."
    "He calls for a round of their best whiskey, on him. Bartender says the whiskey won’t get here for weeks, and all he’s got is the same crappy beer ration we’ve been drinking for months."

    "Barrow says a round of that, then. Fine by me. Tastes better when you drink it in a bar, for some reason."

    "We pull some tables together and cram as many workers around it as possible, and they all drink to Phineas Barrow and the Snake River Line and Pacific Star Railways until they stagger back to their tents."

    "As the singing of workers and settlers drones into the distance, I find myself around a table with four of my new neighbors."
    
    "Phineas Barrow, the young golden boy of Pacific Star Railways."
    "Terrence Crenshaw, that guard with the glittering eyes and the deep-fried smile."
    "Ichabod Salisbury— a local. Not many locals around here. About to be a lot more of them."
    "Temperance Goodwinson, Barrow’s secretary. Catch her humming to herself sometimes."

    "While we’re all sipping the only beer I remember the taste of, Mrs. Goodwinson nurses a pint of water. Makes Barrow chuckle."

    b "Temperance by name and temperance by nature, eh, Mrs. Goodwinson?"
    g "If only we were all so aptly named. Imagine murder trials. ‘How plead you, Violence Jones?’"
    "Salisbury bleats with laughter."
    s "Say, if you’re a Mrs., where’s the Mr.? Surely you’re too young to—"
    "But her smile stiffens. No, nobody’s too young for that."

    g "Mr. Goodwinson has passed. He was a martyr for the cause of freedom."
    "Crenshaw’s eyes narrow."
    
    c "Oh? Whose freedom?"
    "She hears Crenshaw’s Carolina drawl, and her smile keeps getting more brittle."
    g "He fought for the freedom of the negro, and the freedom of all mankind."

    "Barrow slams his mug to the table, rattling the unused cutlery. I’m the only one who doesn’t jump. You get used to sudden, loud noises working on the railway."

    "Goodwinson and Crenshaw don’t break eye contact. Poor Salisbury looks like a cornered dog, trapped between the two of them."

    b "My friends! These are Eastern problems for Eastern politicians. We’re all neighbors now."
    c "And I want to get the measure of my neighbors."

    "He turns to me."

    # 0 = north, 1 = south, 2 = doesn't matter
    $ northsouth = 0
    menu:
        c "So? North or South?"

        "North":
            $ northsouth = 0
            t "I fought for Lincoln and liberty, may he rest in peace."
            g "Lincoln, of course. We wouldn’t want liberty resting in peace, would we."
            "Goodwinson seems to relax. Good thing, too, she’ll be wrinkled by 30 if she keeps scrunching her brow like that."
            "Barrow slams his mug into the table again."
            b "I swear I’ll split this table in two if you all can’t play nice!"
            g "Apologies, Mr. Barrow."
            
        "South":
            $ northsouth = 1
            "I meet Crenshaw’s eyes."
            t "We lost. Now we’re here. It’s in the past."
            "Crenshaw nods."
            c "The future, too, Lord willing."
            "Barrow slams his mug into the table again."
            b "I swear I’ll split this table in two if you all can’t play nice!"
            c "Sure thing, Barrow."
            
        "It doesn't matter.":
            $ northsouth = 2
            t "Barrow’s right. I won’t be nearly drunk enough to talk politics until we get some real liquor here."
            "Barrow claps me on the shoulder. I don’t know if I’ll ever really be used to that from a man who wears a top hat on weekends."

    b "Please, it’s just Phineas!"
    b "I’ll be your neighbor, too. Pacific Star’s settling me here—they’ve got big plans for this little town! The next San Francisco, right here, you’ll see!"

    "And though that’s the goal I’ve been helping him towards for months, I sit there and hope with half my heart that Barrow’s wrong."

    "The scream of the city and the clatter of the railway… as the night swallows the singing from the camp and the fireplace dies down, all I want is peace, quiet, a stale beer, and the glow of a job well done."

    jump scene2
    
label scene2:

    "CORNELIUS THATCHER, 1875"

    "I wake to muffled knocking."

    "I don’t answer it-- not yet. I grab my father’s watch off my bedside table."

    "10:07. God have mercy."

    "The 9:30 train’s come and gone, right outside my window, and I never heard a thing. Fourth time this week."

    "I want to scream at the sky, just to prove I can, but hearing half a scream would only frighten me more."

    "Lift your feet. Answer the door. Someone smarter than you will put the world right soon enough."
    
    # if answered North
    if northsouth == 0:
        "I open the door. Temperance Goodwinson's on the other side, covering her eyes with her hand."
        
        menu:
            g "You're not decent, are you? Get decent, Cornelius."
            
            "Flirt":
                t "You've never dreamt of seeing me in my long johns, Temperance?"

                g "Cornelius!"

                "Temperance turns red and balls her fists in anger. She realizes a moment too late that she can see me now. She stuffs her fists back over her eyes."

                "I roar with laughter, but quickly stop. Of all the things that just don't sound right anymore, laughter's the worst of them. I start putting on work clothes."
            
            "Be respectful":
                t "Long johns is decent among friends, Temperance."

                "She's rolling her eyes behind her hand, no doubt about it. I start putting on work clothes."
                
                
        "I can tell Temperance is straining her voice to speak at a normal level."

        "For someone who talks about the Lord's will as often as Temperance, she sure can't take a hint that the Lord wants us to be quiet."

        t "Does your boy want to help out at the construction site today? My crew's always glad to have him."

        g "Not today. We're meeting at Barrow's office. To discuss the… thing."

        t "Who's we, and what thing?"

        g "Oh, you know, just some pillars of the community. And you know what thing."

        "I do. There's only one thing worth discussing these days."

        "The Recent Change, they call it euphemistically. The Lull, they call it optimistically."

        "A \"Lull\" would end. And ever since the world started going quiet, it has shown no sign of reversing course."

        "When we arrive at Barrow's office, a crowd has already gathered."

        t "Just pillars of the community, eh?"

        "Temperance shrugs."

        g "Every good citizen is a pillar, I suppose."

        "The crowd parts as we approach. Every man doffs their cap to Temperance-- she's a teacher, after all, and even grown men never quite lose that fear and respect you have for a schoolmarm."

        "A fair few doff their caps to me as well. It's an honor hard earned; I've built half the houses in this town, and half of those with my own hands."
    
    elif northsouth == 1:
        "I open the door. Terrence Crenshaw's on the other side, impatiently bouncing his leg up and down like his kneecap's trying to escape."

        c "Still in your long johns, Cornelius? Honestly, I'm worried that bed will swallow you whole one day."

        "He knows as well as I do why the train doesn't wake me anymore. It's rare to hear someone make light of it though. And, to be honest, a bit of a relief."

        "I chuckle, but quickly stop. Of all the things that just don't sound right anymore, laughter's the worst of them. I start putting on work clothes."

        t "Are you going hunting today? I could leave Willet in charge of the construction site if you need an extra rifle."

        c "Another time, gladly, but today duty calls. And by duty I mean Phineas Barrow. He wants a few of us for a meeting."

        "Terrence's voice is unnaturally quiet, and he doesn't bother raising it. I think he likes when people have to lean in and listen close to hear him."

        t "Who's us? And what's this meeting about?"

        c "Us as in a select handful of local notables. And you know what the meeting's about."

        "I do. There's only one thing worth discussing these days."

        "The Recent Change, they call it euphemistically. The Lull, they call it optimistically."

        "A \"Lull\" would end. And ever since the world started going quiet, it has shown no sign of reversing course."

        "When we arrive at Barrow's office, a crowd has already gathered."

        t "A select handful of local notables, I believe you said?"

        c "What can I say? Notability just keeps lowering its standards, apparently."

        "The crowd parts as we approach. Some folks doff their caps to Crenshaw-- his tales of military derring-do have made him a legend down at the tavern."

        "Besides, whenever he comes back from hunting he saves the best cuts of meat for his friends."

        "A fair few doff their caps to me as well. It's an honor hard earned; I've built half the houses in this town, and half of those with my own hands."
    
    # northsouth == 3: Doesn't matter
    else:
        "I open the door. Ichabod Salisbury's on the other side, shuffling his feet nervously. He perks up and gives a toothy grin when he sees me."

        s "Cornelius, m'boy! Is wearing long johns at 10 in the morning some crazy eastern fashion, or are you just getting lazier on me?"

        "He knows as well as I do why the train doesn't wake me anymore. It's rare to hear someone make light of it though. And, to be honest, a bit of a relief."

        t "Don't lose your head over it, Ichabod."

        "I chuckle, but quickly stop. Of all the things that just don't sound right anymore, laughter's the worst of them. I start putting on work clothes. Salisbury stamps his foot and scowls."

        s "Why do people keep telling me that?"

        "I can tell Salisbury is straining to speak at a normal level. In fact, he's overcompensating by speaking a little too loud, and a little too desperate."

        t "Does your boy want to help out at the construction site today? My crew's always glad to have him."

        s "Oh, I'll have you teach him honest work one of these days, but right now Mr. Barrow's called a few of us for a meeting."

        t "Who's us? And what's this meeting about?"

        s "Why, just us pillars of the community, of course! Imagine, Pacific Star Railways wants to know what this daft old farmer thinks."

        s "As for what it's about, well, I think you know as well as I do."

        "I do. There's only one thing worth discussing these days."

        "The Recent Change, they call it euphemistically. The Lull, they call it optimistically."

        "A \"Lull\" would end. And ever since the world started going quiet, it has shown no sign of reversing course."

        "When we arrive at Barrow's office, a crowd has already gathered."

        t "Just pillars of the community, eh?"

        "Ichabod shrugs."

        s "More pillars sprout up every time you look."

        "The crowd parts as we approach. Some folks doff their cap to Ichabod. Plenty of them work his fields, and he puts food on everyone's plate."

        "A fair few doff their caps to me as well. It's an honor hard earned; I've built half the houses in this town, and half of those with my own hands."
        