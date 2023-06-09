image protagbox_idle = im.Scale("gui/protagbox.png", 320, 278)
image protagbox_hover = im.Scale("gui/protagbox_hover.png", 320, 278)

screen currently_playing():
    $ playing = renpy.music.get_playing("music")
    $ musictitles = {"/music/film_music.mp3":("{i}Tufani's Song{i}"),
        "/music/fg_demo.mp3":("{i}Icefield White Knight{i}")}
    add "images/misc/musicnote.png"
    if playing is not None:
        $ playing = musictitles[playing]
        text playing xpos 35 outlines [ (1, "#000", 0, 0) ]
    else:
        text "No Music Playing" xpos 35 outlines [ (1, "#000", 0, 0) ]

screen evidence_button_screen():
    imagebutton:
        xpos 1643
        idle "evidence_idle"
        hover "evidence_hover"
        action [ Show("evidence_folder") ]
        mouse "investigate"
        activate_sound "audio/sfx/sfx-bleep2.wav"  

screen protag_box():
    add "protagbox_idle" ypos 802