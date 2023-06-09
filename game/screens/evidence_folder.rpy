screen evidence_fumo_screen:
    vbox:
        add "images/evidence/investigation_1/evidence_fumo_box.png" xcenter 680
        text "A fumo plushie of Marisa from Touhou.\nDoesn't seem useful." size 50

screen evidence_folder():
    key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "joy_dismiss" action NullAction()
    key "K_a" action NullAction()
    key "K_s" action NullAction()
    key "K_d" action NullAction()
    key "K_UP" action NullAction()
    key "K_DOWN" action NullAction()
    key "K_LEFT" action NullAction()
    key "K_RIGHT" action NullAction()

    add "images/misc/evidence_screen_bg.png"

    viewport:
        xpos 1420 xysize (550, 1080)

        scrollbars "vertical"
        spacing 5

        vbox:
            textbutton "Close":
                action [ Hide() ]
                activate_sound "audio/sfx/sfx-bleep2.wav"   
            label "Evidence"
        

            if fumo_collected:
                textbutton "Fumo": 
                    hovered Show("evidence_fumo_screen")
                    unhovered Hide("evidence_fumo_screen")
                    action NullAction()