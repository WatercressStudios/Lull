label gen4:
    "CORNELIUS THATCHER, 1895"

    if success > 0: # peaceful resolution in gen3
        if FS:
            ichabod_scene
        elif FC:
            call terrence_scene
        else:
            call temperance_scene

        call negotiation_scene
    else: # everybody ded
        call temperance_scene
        
    # jump gen5
    
label temperance_scene:
    if MT:
        "I lie in the grass, and Temperance lays her head across my chest."
    else:
        "I sit in the grass, and Temperance sits across from me."
    
    t "Sometimes I like the silence."

    t "It makes things seem more… personal? Is that right?"

    t "When you get less information, it's easier to pick out the information that matters."

    "She closes her eyes, purses her face, and sways slightly. She's trying to hum."

    g "It helps me remember how it sounds…"

    "She holds my hand, and starts tapping out a rhythm with her thumb while signing with her other hand. Her hands are wrinkled and callused."

    g "My eyes have seen the glory of the coming of the Lord / He is trampling out the vintage where the…"

    "She pauses and lets go of my hand."

    g "Sorry. I need both hands for 'grapes of wrath.'"

    g "They got Brady Crenshaw last night. The Sedgewood boys, I mean."

    "I don't respond."
    
    return
    
label ichabod_scene:
    "Ichabod leans against a tree to catch his breath. He can't walk as far as he used to."

    "I lean next to him. He's looking up into the tree."

    "There's a meadowlark, puffing its chest and trying to sing. Ichabod shakes his head in disgust."

    t "I know. But sometimes I like the silence."

    t "It makes things seem more… personal? Is that right?"

    t "When you get less information, it's easier to pick out the information that matters."

    "Ichabod tries to make signs with his hands, but they're trembling too much to understand."

    "I hand him a piece of paper and some charcoal. He's better with those."

    s "My little brother lived in Illinois. He was blind."

    s "I haven't heard from him since things changed. I tried writing, but you know how the cities were back then. He's dead, I don't doubt that."

    s "But to have lost his sight, and then to watch as the last rope binding him to the world frayed away must have been... indescribable."

    s "I don't think he cherished every little smell or taste. I think he died lost and alone, swallowed up by darkness."

    "Ichabod snaps the charcoal by mistake. I hold his hand and help him keep writing."

    s "Some of my boys got Brady Crenshaw last night."

    "I don't respond."

    return
    
    
label terrence_scene:
    "When I arrive at the Crenshaw homestead, Terrence is collapsed in a heap on the porch, drunk and shouting. His cane lies broken beneath him."

    "He screams and swears and rants until he's out of breath, then sucks in more air and does it again, all without making a sound."

    "It takes him nearly five minutes just to notice me, and another five to start signing."

    c "That fucker. He's just sick of listening to us."

    "Terrence gesticulates at the sky."

    c "My son Brady got shot last night. Sedgewood's boys."

    "I don't respond."
    
    return
    
label negotiation_scene:
    "The four of us sit around a table for the last time."

    "Temperance, sagging and grey. Ichabod, too arthritic to sign three words in a row. Terrence, tapping his cane and squinting his bloodshot eyes."

    "And then there's me. I was strong. I made buildings with my hands. Now I tell other people to make buildings for me, and I am fat."

    "Time has weighed heavy on us. Most of us haven't even reached 60, and yet we decay."

    "Someone's even gotten Phineas Barrow Jr. cleaned and sobered up long enough to sit in as Ichabod's stooge."

    "The younger Barrow is dull and grinning and opportunistic, a pale imitation of his father."

    "We divide the Sedgewood lands between ourselves. With half the town working as his sharecroppers, the line between farmer and king was growing dangerously thin."

    if MT:
        if GM:
            "My land will pass to Grace, and Temperance's land will pass to her first son Silas."
        else:
            "My land will pass to Aaron, and Temperance's land will pass to her first son Silas."

    "It doesn't keep the other families from grumbling about me getting two shares, but they accept it as necessary to preserve the balance of power."

    "Then we eat dinner."

    "Terrence tells war stories. Temperance spends half an hour debating the resettlement of cities with Terrence. I flirt shamelessly with Temperance. Ichabod passes around papers with dirty jokes on them, cackling mutely all the while."

    "Even Barrow Jr. gets into the spirit. Teaches us a card game called Marked Tree."

    "Ichabod and Terrence stare each other down and raise each other's bets and try to forget how many of each other's family members they've killed."

    "I wander home drunk and full and happy."

    if not GM: # didn't get meat therefore Grace died
        "The next morning, I visit Grace's grave."

        "I have some of my sharecroppers bring fresh flowers, and I pretend to hum to her. Hopefully she can hear that, or whatever she meant when she said she heard things."

        "I cry, of course, but I feel refreshed when I leave."

    else:
        "The next morning, I visit Phineas Barrow's grave. The real Phineas Barrow."

        "I have some of my sharecroppers bring fresh flowers, and I pretend to mumble stories that I think he would have laughed at."

        "I get a little misty eyed, but I feel refreshed when I leave."

        "When I get home, I rummage through the attic until I find my old hammer."

        "I give a jutting nail an experimental whack. The vibration feels good running up my arm."

        "I think I'll build a shed today."
        
    return 
    