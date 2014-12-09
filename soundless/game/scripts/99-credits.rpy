define cred = Character(None, kind=nvl)
image bg black = Solid("#000")
label credits:
    scene bg black
    nvl clear
    stop music fadeout 1.0
    play music "snd/soundless-melody-reorchestrated.ogg"
    $ config.skipping = None
    
    python:
        cred("LULL.\n" + 
            "DEVELOPED BY WATERCRESS STUDIOS FOR THE LUDUM DARE 31 COMPETITION.\n\n"+

            "LEAD WRITING\n"+
            "Luke Bean\n"+

            "ASSISTANT WRITING\n"+
            "Axium723\n"+
            "Levi \"Anthrozil7\" Kerns\n"+
            "Ben \"TheDwarfLard\" Thibault\n"+
            "Ty \"Electromancer\" Kiatathikom\n\n"+

            "ART\n"+
            "Nathan \"OptionalSauce\" Burns\n\n"+

            "MUSIC\n"+
            "Ben \"Cidious\" Rockett\n"+
            "Kieren \"Kierious\" Eller")
    nvl clear
    python:
        cred("CODING\n"+
            "Kyle \"Kylemsguy\" Zhou\n\n"+

            "PLAYTESTING\n"+
            "Noah \"Speedy\" Aman\n\n"+

            "(C) 2014 WATERCRESS STUDIOS\n"+
            "www.watercressstudios.com")
    nvl clear
    $ config.skipping = "slow"
    return