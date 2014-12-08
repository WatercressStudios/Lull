label gen5:
    "ALEXANDER THATCHER, 1995"

    "My father buttons my coat while one of our sharecroppers brushes my hair."

    "I have to squeeze my hands past both of them to sign."

    t2 "You're not even going to look at my speech?"

    dad "You're a man of the Thatchers now, Alex. If I didn't trust you to be responsible, I'd have asked you to stand in the back and smile."

    dad "Now, that said, San Francisco and Vancouver are sending ambassadors, so I'm really trusting you to be responsible."

    t2 "If I get nervous and need to throw up, which ambassador do I throw up on?"

    dad "Well, the Mayor of Vancouver did try to sell us a defective shipment of rifles last year."

    dad "I'm a forgiving guy, but vomiting on his ambassador seems like a proportional response."

    "He steps back and lets another of our sharecroppers start on my tie."

    dad "If the people of this town get to know you one tenth as well as I do, they are going to love you."

    "He kisses me on the back of the head and leaves to finish getting ready."

    # -------

    "I take the stage with young heirs of the other founding families."

    "I know Kathleen Goodwin and David Sedgewood from school, and I give both of them a wave. "

    "Dave turns his body to hide his signing from the crowd."

    s2 "You look like a penguin."

    "I laugh and flip him the bird."

    "I've met Phineas Barrow (the seventh, I think?) at social functions before. We bow to each other and he signs what a phenomenal honor it is to see me again. Seems a bit excessive."

    "I only ever see Jared Crenshaw at events like this. He bows deeply, but seems a bit chilly. Might just be nerves."

    "Theodore Sedgewood takes center stage and launches into a speech about our town's history."

    "He stands at the podium signing, and ten of his sharecroppers positioned on platforma around the audience repeat his signs so that everyone can see the speech."

    "He always makes a couple jokes about current events, but other than that it's the same speech every year."

    ts "This Fathers' Day we honor the Five Fathers, who lead our town through famine and strife and forged a strong, loving community."

    ts "My great-great-grandfather, Ichabod Sedgewood, a farmer who loved his workers like his own children."

    ts "Terrence Crenshaw, a hunter and warrior of immense daring. Not always on good terms with my family…"

    if unity >= 2:
        "He turns and pulls an exaggerated scowl at Jared Crenshaw. The crowd waggles their hands in laughter."

    else:
        "He turns and pulls an exaggerated scowl at Jared Crenshaw."
            
        "A couple people in the crowd waggle their hands in laughter, but the response is muted. Still too much bad blood there to find it funny."

    if gen3_success > 0:
        ts "But in the end, their friendship shone through and brought us lasting peace."

    else:
        ts "But after too much blood was spilled, their sons came together and forged a lasting peace."

    ts "Cornelius Thatcher, a builder, strong of body and strong in his convictions. When Thatcher signed, everyone watched to see what he said."

    "I clap a little harder and whoop a little louder for my great-great-great-grandfather."

    if openness >= 2:
        ts "Temperance Goodwin, a teacher of great wit and wisdom, and the woman responsible for mediating the peace between Sedgewood and Crenshaw."
        ts "They were going to call the Five Fathers the Five Parents of Assorted Gender, but it didn't really have the same ring to it!"

    else:
        ts "Silas Goodwin, a preacher of great passion and virtue, who lit a path for our community when all seemed dark."
        "Kathleen Goodwin leans over and signs to me."
        g2 "Every year I tell that bastard to put Temperance in the speech, and every year he tells me he's going to."
        if MT:
            t2 "He's just jealous that Temperance gets two whole founding families to herself."

    ts "And, of course, Phineas Barrow, the railwayman who had faith in this land and led our forefathers here. Could everyone named Phineas Barrow please stand up?"

    "Around ten Phineas Barrows stand and grin at each other. The crowd waggles their hands in laughter."

    "My attention drifts as Theodore Sedgewood's speech trickles out into repetition and platitude."

    ts "But this year, we have three fine young men and women ready to join our town as Men of the Houses!"

    "I leap to my feet. Kathleen Goodwin and Dave Sedgewood and I hold hands and raise them in the air."

    "Our parents agreed beforehand that it was important to emphasize unity between the founding families."

    if MT:
        "The Thatchers and the Goodwins might be cousins, but sometimes you fight most fiercely within your own family."

    ts "I am proud to introduce a new Man of the Thatchers: Alexander Thatcher!"

    "I step forward, and the crowd sways their arms in applause."

    menu:
        "I wipe the sweat off my hands and place my notes on the podium."
            
        "Be conventional":
            $ gen5_radical = False
            $ unity += 1
            t2 "It's an honor to stand before you all as a Man of the Thatchers."
            t2 "I can't begin to express the pride I have in our town." 
            "The crowd nods happily as I praise their ancestors and promise to work with them for the good of our community."
            "But there is a tension in the crowd I haven't seen before."
            "Sharecroppers sitting in the back start waving their arms in wild applause when I quote Temperance Goodwin--  a beloved figure among some radicals for her writing on land reform."
            "My father takes me aside after the ceremony, and asks me if I noticed anything unusual. I know exactly what he means."
            dad "The sharecroppers are restless. You could see it in the crowd today."
            dad "People don't want to believe it. But we're going to have to bend, or we're going to break."
                
        "Be radical":
            $ gen5_radical = True
            $ unity -= 2
            $ openness += 1
            "I take a deep breath and wipe sweat off my palms before I start signing. Not everyone's going to be ready to hear what I'm about to say."
            t2 "It's an honor to stand before you all as a Man of the Thatchers."
            t2 "For all the pride that I have in our town, I understand that it has not yet reached its full promise."
            t2 "When the Five Fathers arrived in Oregon, they were looking for the chance to own their own land and control their own lives. Too few people in our town have that chance."
            t2 "Redistribution of the founding families' estates is the only way to ensure a fair lot for everyone."
            t2 "As one of the future leaders of our community, I look forward to working with the founding families and the sharecroppers alike to ensure a just system for everyone."
            t2 "Thank you."
            "The audience's hands lay still for a moment. The front rows are full of Crenshaws and Sedgewoods and Barrows, their faces aghast. A couple Goodwins and Thatchers wave their arms politely."
            "I spot the San Franciscan ambassador applauding vigorously. Interesting."
            "But it's the back of the crowd that I'm looking at, where the sharecroppers stand."
            "The sharecroppers look around and sign to each other, unsure if they're allowed to applaud."
            "Of course they all want land reform, but it's the sort of thing nobody talks about in public except a couple eccentric Goodwins."
            "Dave Sedgewood shakes his head in wonder as I retake my seat. Kathleen Goodwin gives me a hidden thumbs-up."
            
            "I don't see my father after the ceremony, or even when I get back to the estate, but I find a message from him on my desk."
            dad "So you've come out in support of land reform. The sharecroppers will love you."
            dad "Maybe they'll love you so much that they'll kill me so you can take over the Thatcher family."
            dad "I don't know which frightens me more-- thinking that you were too foolish to realise that, or thinking that you absolutely knew."
    
    jump gen6