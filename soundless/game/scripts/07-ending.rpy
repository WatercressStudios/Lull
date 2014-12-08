label ending:
    show bg black with fade
    "ALEXANDER THATCHER, 2045"
    # decide whether good/bad ending and jump to relevant ending
    if openness >= 3:
        jump goodend
    else:
        jump badend
        
label goodend:
    scene bg goodend
    with fade

    "These days, the world no longer has time for our town."

    "It was an agrarian throwback in an industrial world."

    "It could survive like that as long as every town spoke their own homegrown sign language, but once sound came back, so did spoken English."

    "At first, people just used spoken English to communicate with outsiders. But when my son told me that he wasn't bothering to teach his children the signs, I knew my mother tongue would die."

    "They've left now. Almost everyone has left now. To Vancouver, or Hawaii, places where you can get a good job and make good money."

    "I can't say I mind. The neighbors weren't exactly friendly."

    "Not much love for the Thatchers anymore. Not that I blame them."

    "Sarah left too. No point in a political marriage now. No Barrows left here to ally with."

    "The last time my daughter visited from Vancouver, she brought me a cat. Now it's just me and the cat and the old Thatcher estate."

    "I signed away the rest of my family's land in the peace agreement, but they let me keep the house."

    "I mostly stay inside. Never really got used to noise."

    "I just don't know how to read it-- it's like someone flashing bright colored lights into my eyes all the time."

    "Sometimes I'll put in my earplugs and walk into town, though. The cat comes when he feels like it."

    "Most of the older buildings are getting pretty overgrown, but I like to see if I can find ones that have \"C. THATCHER\" scratched into the back."

    "He hid his signatures well, but they're there if you know where to look."

    "And I'm the last of his line."

    "My children changed their names. Even in Vancouver, the name \"Thatcher\" raises eyebrows."

    "The first of the line built a town with his hands, and the last wanders around with earplugs and a cat."

    "I think I'll go join my children in Vancouver once I get too old to live on my own. Maybe then I can stop being a Thatcher."

    "Today I go down to the old railroad. The cat is too busy launching sneak attacks on bits of dust to come."

    "There's a plaque next to the Founder's Spike, hammered at the founding of the town in 1865."

    "If I pry the spike up, will my abandoned home fold in on itself and cease to be?"

    "I take out my hammer. Worth a try."

    
label badend:
    scene bg badend with fade
    
    "The Fathers' Day parade was good this year. Everyone still remembers that disaster from ten years back when they tried to work instruments into the parade."

    "People didn't ask for sound to come back, and they weren't ready for it. Even before the Fix, most of us went around with earplugs."

    "I just don't know how to read sound-- it was like someone flashing bright colored lights into my eyes all the time."

    "But it was more than just an inconvenience. It would have been the death of our town."

    "We live in an agrarian throwback in an industrial world. There's no shame in admitting that."

    "We could survive like that as long as every town spoke their own homegrown sign language, but once sound came back, so did spoken English."

    "At first, people just used spoken English to communicate with outsiders."

    "But some people wanted it to replace the signs. They wanted to tear down our traditions, change our way of life."

    "The sharecroppers demanded the right to abandon the land in the peace agreement. Once they spoke English, they started to abuse that right, migrating to Vancouver and San Francisco in droves."

    "Even once we had restored their legal responsibility to the land, the sharecroppers used sound as a weapon against us."

    "They would whisper to each other in the fields, plotting further acts of violence. If our overseers couldn't see what they were saying, they couldn't keep our town safe."

    "After what happened to the Sedgewoods, that was an unacceptable risk."

    "The Fix is safe, painless, and fair. Founding families and sharecroppers alike get Fixed."

    "While our neighbors are wracked with change, we are stable and content."

    "And now that we are Fixed, sound will never trouble us again."