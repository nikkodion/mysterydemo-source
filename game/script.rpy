define d = Character(_('Detective'), color="#FFFFFF",  who_outlines=[ (2, "#91385C") ], what_outlines=[ (2, "#91385C") ], window_background="gui/textboxdetective.png")
define narrator = Character("", color="#FFFFFF", who_outlines=[ (2, "#000000") ], what_outlines=[ (2, "#000000") ], window_background="gui/textboxnarrator.png")
define p = Character(_('Protagonist'), color="#FFFFFF", who_outlines=[ (2, "#000000") ], what_outlines=[ (2, "#000000") ], window_background="gui/textboxprotag.png", image="protag")
define c = Character(_('Chester Cheeto'), color="#FFFFFF",  who_outlines=[ (2, "#000000") ], what_outlines=[ (2, "#000000") ], window_background="gui/textboxchester.png", image="chester")
image evidence_fumo_box = im.Scale("images/evidence/investigation_1/evidence_fumo_box.png", 443, 553)
default show_quick_menu = False

screen main_menu_key():
    key "K_ESCAPE" action MainMenu()
init:
    define shortdiss = Dissolve(0.1)
    define veryshortdiss = Dissolve(0.01)
    define shortmoveinbottom = MoveTransition(0.1, enter=_movebottom)
    define config.mouse = { }
    define config.mouse['default'] = [ ( "gui/arrow.png", 0, 0) ]
    define config.mouse['investigate'] = [ ( "gui/magnifying.png", 0, 0) ]
    $ evidence_left = Position(xpos=0.3, ypos=0.75)
    $ screen_right = Position(xpos=0.7)
    $ fumo_collected = False
    define flash = Fade(.1, 0.0, .1, color="#fff")

init python:
    config.keymap['game_menu'].remove('K_ESCAPE')
    config.keymap['game_menu'].remove('mouseup_3')
    config.keymap['accessibility'].remove('K_a')
    config.layers = ['master', 'lower_screens', 'fg_port', 'transient', 'screens', 'overlay', 'fg_ui']
    config.context_clear_layers.append('fg_ui')
    config.context_clear_layers.append('lower_screens')
    config.context_clear_layers.append('fg_port')

label start:
    show screen main_menu_key
    show screen currently_playing
    show screen evidence_button_screen
    show screen protag_box

    scene bg clubroom

    play music "/music/film_music.mp3" volume 0.5

    "Well, I guess we better get started with the case."
    window hide

    scene bg clubroom blur with shortdiss

    show sherlock_half with shortmoveinbottom
    voice "/audio/sherlock/sher_soreja.mp3"
    d "First, let's look for some clues!"
    hide sherlock_half with shortmoveinbottom
    jump investigation_1