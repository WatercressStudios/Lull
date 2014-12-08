label gen6:
    scene bg_gen7
    with fade
    
    "ALEXANDER CRENSHAW, 2005"

    "The fields are full of smoke."

    "They will hide me while I flee the estate. But they will choke me if they can. I have to get out of the fields."

    "I stuff my revolver in my waistband and run."

    "Last I heard from my father before the cell tower went down, he was holed up in the post office."

    "But trying to take one of the main roads into town would be suicide. Have to reach the emergency meeting point first."

    "The meeting point is on a hill outside town. Even though it's supposed to be hidden by trees, I can see people milling about from a distance."

    "I keep walking towards it. If those are redcaps at the meeting point, I'm dead. But I don't know what else to do."

    "I sense gun barrels following me as I approach, but that's frankly encouraging. Redcaps would have just shot me."

    "As I pass through the trees, I see Kathleen Goodwin crouched on a rock, signing out orders to a couple dozen men wearing the Goodwin colors."

    "Her husband, some distant Crenshaw, is binding a burn on her leg."
    
    show KathGood mid at left
    with dissolve

    g2 "Jesus, not the Thatchers, too."
    
    show AlexThat mid at right

    "Kathleen stands to greet me."

    g2 "Hey, Alex. Good to see you walking around."

    if not gen5_radical:
        g2 "Got to bend or we'll break, your father always said. Guess we didn't bend enough, huh."

    else:
        g2 "Looks like we're going to get that land reform you always wanted. Not quite the way you wanted it, huh."

    "She speaks with a preternatural calm. I think I can understand. Let the fear out a little, and it'll just keep on flowing through that crack."

    g2 "How come you don't have more Thatchers with you?"

    t2 "Our men are holding down the estate, for now. We haven't been able to get many people out yet."

    g2 "They're still alive, though? Thank god. After the Sedgewoods, I don't think we could take--"

    "I grab her hand to interrupt her."

    t2 "Wait, what about the Sedgewoods?"

    g2 "Well. They're all dead, that's what. Some of their house staff let the redcaps in."

    g2 "You'll see on the way into town."

    g2 "My grandfather's been in contact with the Crenshaws. They'll be making their own way into town to join up with us, hopefully."
    
    hide KathGood
    hide AlexThat

    "I follow Kathleen's men down Old Mule Road into town. Sedgewoods dangle from trees on either side of the road. I try not to recognize any of them."

    "Barrow men hold the road, for the moment. They move in groups of three: two stand watch while one climbs into a tree and unties the body."

    "As we reach the outskirts of town, the smoke makes it hard to tell whether or not we're about to wander into a firefight."

    "A strange, pulsing pressure runs through my head as we approach the old post office."

    "Little flashes of light peek through the smoke. The building is under fire."

    "We take shelter in a furniture store down the road. The display window lies in pieces on the ground. A sofa is propped up on the window frame, abandoned halfway through being stolen."

    "The strange pressure keeps coming in waves. I knead my forehead with my hands."

    show KathGood mid at left

    g2 "You sure Thatcher's still in there? I don't want to pick a fight before the other houses get here unless we have to."
    
    show AlexThat at right

    t2 "He was there two hours ago with a few of my uncles. I can't be sure what's happened since then."

    t2 "It's hard to tell with the smoke, but from the muzzle flashes I think there's a pretty significant force attacking the post office."

    g2 "We need your father, Alex."

    if not gen5_radical:
        g2 "He's a moderating influence. He's popular in town."

    else:
        g2 "I know you and him had your differences, but he's popular in town."

    g2 "We're not going to be able to massacre our way out of this conflict, no matter what Thaddeus Crenshaw thinks."

    g2 "Our best hope is a negotiated peace. We need Thatchers at the table for that. The redcaps won't deal with the more hard-line houses."

    t2 "You don't have to convince me, Kathleen. He's my father."

    g2 "We've got 20-odd men against a redcap force of unknown size. I'm trying to convince myself."

    t2 "I thought you said the Crenshaws were coming to join up with us?"

    "Kathleen cranes her head through the window and peers around in the smoke."

    g2 "Well, they should be here. Might have run into trouble, or decided they had better things to do."

    # -1 = didn't wait, 0 = wait fail, 1 = wait success
    $ gen6_wait = 0
    menu:
        g2 "We could wait for them and mount a proper attack, or my men could distract the redcaps while you run into the post office and get your father. Either's a risk."
        # 1 succeeds if Unity >= 2. Option 2 always has the same outcome.
        "Wait for reinforcements":
            t2 "They've made it this long holed up in the post office. Let's wait for the Crenshaws and do this rescue right."
            hide KathGood
            hide AlexThat
            "Kathleen nods and dispatches scouts to report if they see reinforcements coming."
            "Five minutes pass, then ten."
            "And then an orange glow cuts through the smoke."
            g2 "Fuck. They're trying to set it on fire. We've got to move."
            "The Goodwin men take up positions around the street and begin firing into the smoke."
            "I don't know how they can see where they're aiming, but apparently they hit something, because bullets start chipping the walls behind us."
            "I duck my head and run, hugging the side of the post office."
            if unity >= 2:
                call gen6_waitsuccess
            else:
                call gen6_waitfail
        "Act now":
            $ gen6_wait = -1
            $ openness += 1
            t2 "We don't have time to gamble on Crenshaws. Let's move."
            hide KathGood
            hide AlexThat
            "The Goodwin men take up positions around the street and begin firing into the smoke."
            "I don't know how they can see where they're aiming, but apparently they hit something, because bullets start chipping the walls behind us."
            "I duck my head and run, hugging the side of the post office."
            "A bullet nicks my leg. I keep dragging myself across the brick wall as blood pools in my sock. Almost there."
            "As soon as I reach the post office door I start yanking the chain for the door-flag. The view window slides open."
            show AlexThat mid at right
            t2 "It's a friend of Cornelius! Friend of Cornelius!"
            "The door opens just a crack and I slip inside."
            "My father's men lead me to him."
            "He is bloody and gaunt. A medic is desperately trying to put his chest back together."
            "When he sees me, his face lights up."
            dad "Alex…"
            "He reaches beneath his coat and unhooks something from his belt."
            "A hammer. The head is square and black and ancient. The handle is sleek and lacquered-- it has been replaced several times over the years."
            "The Hammer of the Thatchers. It pounded the final spike into the Snake River Rail Line 140 years ago."
            "The door opens again, and the Goodwin men start retreating into the building."
            "They're missing a lot of people. Kathleen Goodwin isn't with them."
            "My father pats my hand and closes his eyes, his chest gently rising and falling."
            "Then the medic starts probing around one of his wounds, and he screams in pain."
                         
    "And as the strange pressure fills my head again, an impossible thought occurs to me: I am hearing him scream."
    
    jump ending

label gen6_waitsuccess:
    $ gen6_wait = 1
    $ openness += 2
    "As I round the corner, I run headlong into someone. He staggers back and levels a rifle at me."
    "I'm about to reach for my revolver, but then I notice the red and brown pin on his lapel."
    show AlexThat mid at right
    t2 "Thatcher! I'm Alexander Thatcher!"
    "The man lowers his gun and bows."
    man "Apologies, sir. Thaddeus Crenshaw sends his compliments, and hopes you find your father well."
    "As Crenshaw's men flood into the street, I tug the post office's door-flag chain. The view window slides open."
    t2 "It's a friend of Cornelius."
    "The door opens just a crack and I slip inside."
    "My father's men lead me to him."
    "He is bloody and gaunt. A medic is desperately trying to put his chest back together."
    "When he sees me, his face lights up."
    dad "Alex…"
    "He reaches beneath his coat and unhooks something from his belt."
    "A hammer. The head is square and black and ancient. The handle is sleek and lacquered-- it has been replaced several times over the years."
    "The Hammer of the Thatchers. It pounded the final spike into the Snake River Rail Line 140 years ago."
    "My father pats my hand and closes his eyes, his chest gently rising and falling."
    "Then the medic starts probing around one of his wounds, and he screams in pain."
    return

label gen6_waitfail:
    $ gen6_wait = 0
    "A bullet nicks my leg. I keep dragging myself across the brick wall as blood pools in my sock. Almost there."
    "As soon as I reach the post office door I start yanking the chain for the door-flag."
    "Nobody opens the view window."
    "I reach up and start prying the view window open with my fingers."
    "My father's men are inside, trying to beat back the fire with blankets while the redcaps keep pouring gasoline through the windows."
    "One of the men steps in a puddle of gasoline. He screams and stumbles backwards."
    return