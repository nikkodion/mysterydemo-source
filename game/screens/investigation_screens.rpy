image evidence_fumo_idle = im.Scale("images/evidence/investigation_1/evidence_fumo_idle.png", 87, 109)
image evidence_fumo_hover = im.Scale("images/evidence/investigation_1/evidence_fumo_hover.png", 87, 109)
image sherlock_full = im.Scale("images/chars/sherlock/sherlock_full-zoom.png", 140, 331)
image sherlock_full_hover = im.Scale("images/chars/sherlock/sherlock_full_hover.png", 140, 331)
image sherlock_full_hover_1 = im.Scale("images/chars/sherlock/sherlock_full_hover_1.png", 140, 331)
image sherlock_full_hover_2 = im.Scale("images/chars/sherlock/sherlock_full_hover_2.png", 140, 331)
image sherlock_full_hover_3 = im.Scale("images/chars/sherlock/sherlock_full_hover_3.png", 140, 331)
image sherlock_full_hover_4 = im.Scale("images/chars/sherlock/sherlock_full_hover_4.png", 140, 331)
image sherlock_full_hover = im.Scale("images/chars/sherlock/sherlock_full_hover.png", 140, 331)
image sherlock_full_sel_1 = im.Scale("images/chars/sherlock/sherlock_full_sel_1.png", 140, 331)
image sherlock_full_sel_2 = im.Scale("images/chars/sherlock/sherlock_full_sel_2.png", 140, 331)
image sherlock_full_sel_3 = im.Scale("images/chars/sherlock/sherlock_full_sel_3.png", 140, 331)
image sherlock_full_sel_4 = im.Scale("images/chars/sherlock/sherlock_full_sel_4.png", 140, 331)
image sherlock_full_sel_5 = im.Scale("images/chars/sherlock/sherlock_full_sel_5.png", 140, 331)
image sherlock_full_sel_6 = im.Scale("images/chars/sherlock/sherlock_full_sel_6.png", 140, 331)
image sherlock_full_sel_7 = im.Scale("images/chars/sherlock/sherlock_full_sel_7.png", 140, 331)
image sherlock_full_sel_8 = im.Scale("images/chars/sherlock/sherlock_full_sel_8.png", 140, 331)
image evidence_idle = im.Scale("images/misc/evidence_idle.png", 275, 68)
image evidence_hover = im.Scale("images/misc/evidence_hover.png", 275, 68)

image sher_selected:
    "sherlock_full_hover_1"
    pause 0.1
    "sherlock_full_hover_2"
    pause 0.1
    "sherlock_full_hover_3"
    pause 0.1
    "sherlock_full_hover_4"
    pause 0.1
    repeat

screen investigation_1():
    add "images/bg/bg clubroom.png"
    imagebutton:
        idle "protagbox_idle" ypos 802
        hover "protagbox_hover"
        action Jump ("investigation_1_protag")
        activate_sound "audio/sfx/sfx-bleep2.wav"
    use currently_playing
    use evidence_button_screen 
    imagebutton:
        xpos 414
        ypos 650
        idle "evidence_fumo_idle"
        hover "evidence_fumo_hover"
        action Jump("investigation_1_1")
        activate_sound "audio/sfx/sfx-bleep2.wav"
    imagebutton:
        xpos 939
        ypos 502
        idle "sherlock_full"
        hover "sher_selected"
        action Jump("investigation_1_2")
        activate_sound "audio/sfx/sfx-bleep2.wav"