label gen1:
    scene bg gen1_day
    with fade

    # TODO: center this line
    "CORNELIUS THATCHER, 1865"

    show PhinBarr at left
    show CornThat at right
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

    hide PhinBarr
    hide CornThat

    show bg gen1_night
    with dissolve
    
    "As the singing of workers and settlers drones into the distance, I find myself around a table with four of my new neighbors."
    
    show PhinBarr
    "Phineas Barrow, the young golden boy of Pacific Star Railways."
    hide PhinBarr
    show TerrCren
    "Terrence Crenshaw, that guard with the glittering eyes and the deep-fried smile."
    hide TerrCren
    show IchaSedg
    "Ichabod Sedgewood— a local. Not many locals around here. About to be a lot more of them."
    hide IchaSedg
    show TempGood
    "Temperance Goodwin, Barrow’s secretary. Catch her humming to herself sometimes."
    hide TempGood

    "While we’re all sipping the only beer I remember the taste of, Mrs. Goodwin nurses a pint of water. Makes Barrow chuckle."

    show PhinBarr at right
    b "Temperance by name and temperance by nature, eh, Mrs. Goodwin?"
    show TempGood at left
    g "If only we were all so aptly named. Imagine murder trials. ‘How plead you, Violence Jones?’"
    hide PhinBarr
    show IchaSedg at right
    "Sedgewood bleats with laughter."
    s "Say, if you’re a Mrs., where’s the Mr.? Surely you’re too young to—"
    "But her smile stiffens. No, nobody’s too young for that."

    g "Mr. Goodwin has passed. He was a martyr for the cause of freedom."
    show IchaSedg at center
    show TerrCren at right
    "Crenshaw’s eyes narrow."
    
    c "Oh? Whose freedom?"
    "She hears Crenshaw’s Carolina drawl, and her smile keeps getting more brittle."
    g "He fought for the freedom of the negro, and the freedom of all mankind."

    "Barrow slams his mug to the table, rattling the unused cutlery. I’m the only one who doesn’t jump. You get used to sudden, loud noises working on the railway."

    "Goodwin and Crenshaw don’t break eye contact. Poor Sedgewood looks like a cornered dog, trapped between the two of them."

    b "My friends! These are Eastern problems for Eastern politicians. We’re all neighbors now."
    c "And I want to get the measure of my neighbors."

    hide IchaSedg
    show TerrCren at center
    show CornThat at right
    "He turns to me."

    # 0 = north, 1 = south, 2 = doesn't matter
    menu:
        c "So? North or South?"

        "North":
            $ northsouth = 0
            t "I fought for Lincoln and liberty, may he rest in peace."
            g "Lincoln, of course. We wouldn’t want liberty resting in peace, would we."
            "Goodwin seems to relax. Good thing, too, she’ll be wrinkled by 30 if she keeps scrunching her brow like that."
            "Barrow slams his mug into the table again."
            b "I swear I’ll split this table in two if you all can’t play nice!"
            g "Apologies, Mr. Barrow."
            
        "South":
            $ northsouth = 1
            $ FC = True
            "I meet Crenshaw’s eyes."
            t "We lost. Now we’re here. It’s in the past."
            "Crenshaw nods."
            c "The future, too, Lord willing."
            "Barrow slams his mug into the table again."
            b "I swear I’ll split this table in two if you all can’t play nice!"
            c "Sure thing, Barrow."
            
        "It doesn't matter.":
            $ northsouth = 2
            $ FS = True
            t "Barrow’s right. I won’t be nearly drunk enough to talk politics until we get some real liquor here."
            show PhinBarr behind CornThat:
                xalign 1.1 yalign .9
            "Barrow claps me on the shoulder. I don’t know if I’ll ever really be used to that from a man who wears a top hat on weekends."

    b "Please, it’s just Phineas!"
    b "I’ll be your neighbor, too. Pacific Star’s settling me here—they’ve got big plans for this little town! The next San Francisco, right here, you’ll see!"

    hide PhinBarr
    hide TerrCren
    hide TempGood
    with dissolve
    "And though that’s the goal I’ve been helping him towards for months, I sit there and hope with half my heart that Barrow’s wrong."

    "The scream of the city and the clatter of the railway… as the night swallows the singing from the camp and the fireplace dies down, all I want is peace, quiet, a stale beer, and the glow of a job well done."

    jump gen2
    