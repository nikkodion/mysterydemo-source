label investigation_1:
    $ default_mouse = "investigate"
    $ renpy.transition(shortdiss)
    call screen investigation_1 with shortdiss

label investigation_1_protag:
    $ default_mouse = "default"
    "We should find some clues."
    jump investigation_1

label investigation_1_1:
    $ default_mouse = "default"
    hide screen investigation_1
    if fumo_collected is False:
        show sherlock_half at screen_right with shortmoveinbottom
        show evidence_fumo_box at evidence_left with shortmoveinbottom
        voice "/audio/sherlock/sher_naruhodo.mp3"
        d "Oh! You found something interesting!"
        d "Let's note this down as evidence!"
        play sound "/audio/sfx/sfx-selectjingle.wav" volume .2
        $ fumo_collected = True
        show evidence_fumo_box at topright with ease
        hide evidence_fumo_box with shortdiss
        show sherlock_half at center with ease
    else:
        show sherlock_half with shortmoveinbottom
    d "I'm glad we found this! It might be helpful later!"
    p "Are you sure about that?"
    play sound "/audio/sherlock/sher_wakarimashitaka.mp3"
    d "We don't know what's useful or not until we have to use it!"
    hide sherlock_half with shortdiss

    hide screen protag_box
    jump fg_demo

    jump investigation_1

label investigation_1_2:
    $ default_mouse = "default"
    hide screen investigation_1
    show sherlock_half with shortmoveinbottom
    voice "/audio/sherlock/sher_aaa.mp3"
    d "Hm... I can't find anything."
    voice "/audio/sherlock/sher_demone.mp3"
    d "But maybe something will come up if we keep looking!"
    hide sherlock_half with shortdiss
    jump investigation_1

label call_evidence_folder:
    $ default_mouse = "default"
    $ renpy.transition(shortdiss)
    call screen evidence_folder
    jump investigation_1
