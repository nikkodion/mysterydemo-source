screen fg_base():
    use hakurei_shrine

    if marisa_var == 0:
        use marisa_init
    elif marisa_var == 1:
        use marisa_attack_1
    elif marisa_var == 2:
        use marisa_attack_1_getup
    elif marisa_var == 3:
        use marisa_hit_sit
    elif marisa_var == 4:
        use marisa_blockstand
    elif marisa_var == 5:
        use marisa_hit_stand
    elif marisa_var == 6:
        use marisa_blocksit
    elif marisa_var == 7:
        use marisa_jump
    elif marisa_var == 8:
        use marisa_jump_a
    elif marisa_var == 9:
        use marisa_ult

    if reimu_var == 0:
        use reimu_init
    elif reimu_var == 1:
        use reimu_backdash
    elif reimu_var == 2:
        use reimu_hit
    elif reimu_var == 3:
        use reimu_idle
    elif reimu_var == 4:
        use reimu_oh
    elif reimu_var == 5:
        use reimu_oh_a
    elif reimu_var == 6:
        use reimu_low
    elif reimu_var == 7:
        use reimu_low_a
    elif reimu_var == 8:
        use reimu_mid
    elif reimu_var == 9:
        use reimu_mid_a
    elif reimu_var == 10:
        use reimu_vuln
    elif reimu_var == 11:
        use reimu_hit_a
    elif reimu_var == 12:
        use reimu_down

    use monitor
    use currently_playing

screen excl_screen():
    if excl_var == 1:
        use excl_oh
    elif excl_var == 2:
        use excl_low
    elif excl_var == 3:
        use excl_mid
    elif excl_var == 4:
        use excl_grab

screen block_status():
    if block_status == 0:
        use block_success
    if block_status == 1:
        use block_slow
    if block_status == 2:
        use block_incorrect

screen hakurei_shrine():
    add "images/bg/hakurei_shrine.png" at init_appear

screen monitor():
    add "images/bg/monitor.png" at init_appear

transform init_appear:
    on show:
        ypos 1280
        ease .55 ypos 0

transform excl_appear:
    on show:
        xpos -1920
        ease .2 xpos 0

transform block_appear:
    on show:
        ypos 1280
        ease .1 ypos 0
    on hide:
        ease .1 alpha 0.0

screen excl_oh():
    add "images/fg/excl_oh.png" at excl_appear

screen excl_low():
    add "images/fg/excl_low.png" at excl_appear

screen excl_mid():
    add "images/fg/excl_mid.png" at excl_appear

screen excl_grab():
    add "images/fg/excl_grab.png" at excl_appear

screen block_success():
    add "images/fg/block_success.png" at block_appear

screen block_slow():
    add "images/fg/block_slow.png" at block_appear

screen block_incorrect():
    add "images/fg/block_incorrect.png" at block_appear

image mar_idle:
    "images/fg/marisa/mar_idle_1.png"
    pause 0.084
    "images/fg/marisa/mar_idle_2.png"
    pause 0.084
    "images/fg/marisa/mar_idle_4.png"
    pause 0.084
    "images/fg/marisa/mar_idle_5.png"
    pause 0.084
    "images/fg/marisa/mar_idle_6.png"
    pause 0.084
    "images/fg/marisa/mar_idle_7.png"
    pause 0.084
    "images/fg/marisa/mar_idle_8.png"
    pause 0.084
    "images/fg/marisa/mar_idle_9.png"
    pause 0.084
    "images/fg/marisa/mar_idle_10.png"
    pause 0.084
    repeat

image mar_a_1:
    "images/fg/marisa/mar_a_1.png"
    pause 0.042
    "images/fg/marisa/mar_a_2.png"
    pause 0.042
    "images/fg/marisa/mar_a_3.png"
    pause 0.042
    "images/fg/marisa/mar_a_4.png"
    pause 0.042
    "images/fg/marisa/mar_a_5.png"
    pause 0.042
    "images/fg/marisa/mar_a_6.png"
    pause 0.042
    "images/fg/marisa/mar_a_7.png"
    pause 0.042
    "images/fg/marisa/mar_a_8.png"
    pause 0.084
    parallel:
        ease .25 xpos 470 ypos -50
    parallel:
        "images/fg/marisa/mar_a_9.png"
        pause 0.084
        "images/fg/marisa/mar_a_10.png"
        pause 0.084
        repeat

image mar_a_1_getup:
    "images/fg/marisa/mar_idle_11.png"
    pause 0.084
    "images/fg/marisa/mar_idle_12.png"
    pause 0.084
    "images/fg/marisa/mar_idle_13.png"
    pause 0.084
    "images/fg/marisa/mar_idle_14.png"
    pause 0.084
    "images/fg/marisa/mar_idle_15.png"
    pause 0.084
    "images/fg/marisa/mar_idle_16.png"
    pause 0.084
    "images/fg/marisa/mar_idle_17.png"
    pause 0.084
    "images/fg/marisa/mar_idle_18.png"
    pause 0.084
    "images/fg/marisa/mar_idle_19.png"
    pause 0.084
    "images/fg/marisa/mar_idle_20.png"
    pause 0.084
    "mar_idle"

image mar_hit_sit:
    "images/fg/marisa/mar_hit_sit_1.png"
    pause 0.084
    "images/fg/marisa/mar_hit_sit_2.png"
    pause 0.084
    "images/fg/marisa/mar_hit_sit_3.png"
    pause 0.084
    "mar_idle"

image mar_blockstand:
    "images/fg/marisa/mar_blockstand_1.png"
    pause 0.084
    "images/fg/marisa/mar_blockstand_2.png"
    pause 0.084
    "images/fg/marisa/mar_blockstand_1.png"
    pause 0.084
    "images/fg/marisa/mar_blockstand_2.png"
    pause 0.084
    "images/fg/marisa/mar_blockstand_1.png"
    pause 0.084
    "images/fg/marisa/mar_blockstand_2.png"
    pause 0.084
    "mar_idle"

image mar_hit_stand:
    "images/fg/marisa/mar_hit_stand_1.png"
    pause 0.084
    "images/fg/marisa/mar_hit_stand_2.png"
    pause 0.084
    "images/fg/marisa/mar_hit_stand_3.png"
    pause 0.168
    "mar_idle"

image mar_blocksit:
    "images/fg/marisa/mar_blocksit_1.png"
    pause 0.084
    "images/fg/marisa/mar_blocksit_2.png"
    pause 0.084
    "images/fg/marisa/mar_blocksit_1.png"
    pause 0.084
    "images/fg/marisa/mar_blocksit_2.png"
    pause 0.084
    "images/fg/marisa/mar_blocksit_1.png"
    pause 0.084
    "images/fg/marisa/mar_blocksit_2.png"
    pause 0.084
    "mar_idle"

image mar_jump:
    "images/fg/marisa/mar_jump_1.png"
    pause 0.042
    "images/fg/marisa/mar_jump_2.png"
    pause 0.042
    parallel:
        ease .336 ypos -200
    parallel:
        "images/fg/marisa/mar_jump_3.png"
        pause 0.084
        "images/fg/marisa/mar_jump_4.png"
        pause 0.084
        "images/fg/marisa/mar_jump_5.png"
        pause 0.168
        "images/fg/marisa/mar_jump_6.png"
        pause 0.084
    "images/fg/marisa/mar_jump_7.png"

image mar_jump_a:
        "images/fg/marisa/mar_jump_a_1.png"
        pause 0.084
        "images/fg/marisa/mar_jump_a_2.png"
        pause 0.084
        "images/fg/marisa/mar_jump_a_3.png"
        pause 0.084
        "images/fg/marisa/mar_jump_a_4.png"
        pause 0.084   
        "images/fg/marisa/mar_jump_a_5.png"
        pause 0.084
        "images/fg/marisa/mar_jump_a_6.png"
        pause 0.084
        "images/fg/marisa/mar_jump_a_7.png"
        pause 0.084
        "images/fg/marisa/mar_jump_a_8.png"

image mar_ult:
    "images/fg/marisa/mar_ult_1.png"
    pause 0.084
    "images/fg/marisa/mar_ult_2.png"
    pause 0.084
    "images/fg/marisa/mar_ult_3.png"
    pause 0.084
    "images/fg/marisa/mar_ult_4.png"
    pause 0.084
    "images/fg/marisa/mar_ult_5.png"
    pause 0.084
    "images/fg/marisa/mar_ult_6.png"
    pause 0.084
    "images/fg/marisa/mar_ult_7.png"
    pause 0.084
    "images/fg/marisa/mar_ult_8.png"
    pause 0.084
    "images/fg/marisa/mar_ult_9.png"
    pause 0.084
    "images/fg/marisa/mar_ult_10.png"
    pause 0.084
    "images/fg/marisa/mar_ult_11.png"


screen marisa_init():
    if fight_state == 0:
        add "mar_idle" at init_appear
    elif fight_state == 1:
        add "mar_idle" at marisa_idle_v5
    elif fight_state == 2:
        add "mar_idle" at marisa_idle_v6
    elif fight_state == 3:
        add "mar_idle" at marisa_idle_v7

screen marisa_attack_1():
    add "mar_a_1"

transform marisa_idle_v2:
    xpos 500
    ypos 0
    ease .2 ypos 25
    pause .3
    ease .1 ypos 0

transform marisa_idle_v3:
    xpos 500
    ypos 0
    pause .2
    ease .1 xpos 480

transform marisa_idle_v4:
    xpos 480
    ypos 0
    ease .1 xpos 460

transform marisa_idle_v5:
    xpos 500

transform marisa_idle_v6:
    xpos 480

transform marisa_idle_v7:
    xpos 460

transform marisa_air_v1:
    xpos 460
    ypos -200
    ease .588 xpos 570 ypos -100

transform marisa_idle_v8:
    xpos 540

screen marisa_attack_1_getup():
    add "mar_a_1_getup" at marisa_idle_v2

screen marisa_hit_sit():
    add "mar_hit_sit" at marisa_idle_v3

screen marisa_blockstand():
    add "mar_blockstand" at marisa_idle_v3

screen marisa_hit_stand():
    add "mar_hit_stand" at marisa_idle_v4

screen marisa_blocksit():
    add "mar_blocksit" at marisa_idle_v4

screen marisa_jump():
    add "mar_jump" at marisa_idle_v7

screen marisa_jump_a():
    add "mar_jump_a" at marisa_air_v1

screen marisa_ult():
    add "mar_ult" at marisa_idle_v8








image rei_idle:
    "images/fg/reimu/rei_idle_1.png"
    pause 0.084
    "images/fg/reimu/rei_idle_2.png"
    pause 0.084
    "images/fg/reimu/rei_idle_3.png"
    pause 0.084
    "images/fg/reimu/rei_idle_4.png"
    pause 0.084
    "images/fg/reimu/rei_idle_5.png"
    pause 0.084
    "images/fg/reimu/rei_idle_6.png"
    pause 0.084
    "images/fg/reimu/rei_idle_7.png"
    pause 0.084
    "images/fg/reimu/rei_idle_8.png"
    pause 0.084
    "images/fg/reimu/rei_idle_9.png"
    pause 0.084
    "images/fg/reimu/rei_idle_10.png"
    pause 0.084
    "images/fg/reimu/rei_idle_11.png"
    pause 0.084
    repeat

image rei_bd:
    "images/fg/reimu/rei_bd_1.png"
    pause 0.084
    parallel:
        ease 1 xpos 50
    parallel:
        "images/fg/reimu/rei_bd_2.png"
        pause 0.084
        "images/fg/reimu/rei_bd_3.png"
        pause 0.084
        repeat

image rei_hit:
    xpos 50
    "images/fg/reimu/rei_bd_2.png"
    pause 0.084
    "images/fg/reimu/rei_bd_3.png"
    pause 0.084
    "images/fg/reimu/rei_bd_2.png"
    pause 0.084
    "images/fg/reimu/rei_bd_3.png"
    pause 0.084
    "images/fg/reimu/rei_bd_2.png"
    pause 0.084
    "images/fg/reimu/rei_bd_3.png"
    pause 0.084
    "images/fg/reimu/rei_bd_2.png"
    pause 0.084
    "images/fg/reimu/rei_hit_1.png"
    pause 0.084
    "images/fg/reimu/rei_hit_2.png"
    pause 0.084
    "images/fg/reimu/rei_hit_3.png"

image rei_hit_a:
    xpos 120
    "images/fg/reimu/rei_mid_6.png"
    pause 0.4
    xpos 0
    "images/fg/reimu/rei_hit_1.png"
    pause 0.084
    "images/fg/reimu/rei_hit_2.png"
    pause 0.084
    "images/fg/reimu/rei_hit_3.png"   

image rei_oh:
    "images/fg/reimu/reimu_oh_1.png"
    pause 0.084
    "images/fg/reimu/reimu_oh_2.png"
    pause 0.084
    "images/fg/reimu/reimu_oh_3.png"
    pause 0.084
    "images/fg/reimu/reimu_oh_4.png"
    pause 0.084
    "images/fg/reimu/reimu_oh_5.png"
    pause 0.084
    block:
        "images/fg/reimu/reimu_oh_6.png"
        pause 0.084
        "images/fg/reimu/reimu_oh_7.png"
        pause 0.084
        repeat

image rei_oh_a:
    "images/fg/reimu/reimu_oh_8.png"
    pause 0.084
    "images/fg/reimu/reimu_oh_9.png"
    pause 0.084
    "images/fg/reimu/reimu_oh_10.png"
    pause 0.084
    "images/fg/reimu/reimu_oh_11.png"
    pause 0.084
    "images/fg/reimu/reimu_oh_12.png"
    pause 0.084
    "images/fg/reimu/reimu_oh_13.png"
    pause 0.084
    "images/fg/reimu/reimu_oh_14.png"
    pause 0.084
    "rei_idle"

image rei_low:
    "images/fg/reimu/rei_crouch_1.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_2.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_3.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_4.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_a_1.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_a_2.png"

image rei_low_a:
    "images/fg/reimu/rei_crouch_a_3.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_a_4.png" 
    pause 0.084
    "images/fg/reimu/rei_crouch_a_5.png" 
    pause 0.084
    "images/fg/reimu/rei_crouch_a_6.png"   
    pause 0.084
    "images/fg/reimu/rei_crouch_a_7.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_a_8.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_a_9.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_a_2.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_a_1.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_4.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_3.png" 
    pause 0.084  
    "images/fg/reimu/rei_crouch_2.png"
    pause 0.084
    "images/fg/reimu/rei_crouch_1.png"  
    pause 0.084
    "rei_idle"

image rei_mid:
    "images/fg/reimu/rei_mid_1.png"
    pause 0.084
    "images/fg/reimu/rei_mid_2.png"  

image rei_mid_a:
    "images/fg/reimu/rei_mid_3.png"
    pause 0.084
    "images/fg/reimu/rei_mid_4.png"
    pause 0.084
    "images/fg/reimu/rei_mid_5.png" 
    pause 0.084  
    "images/fg/reimu/rei_mid_6.png"
    pause 0.084
    "images/fg/reimu/rei_mid_7.png"  
    pause 0.084
    "rei_idle"

image rei_vuln:
    "images/fg/reimu/rei_mid_3.png"
    pause 0.084
    "images/fg/reimu/rei_mid_4.png"
    pause 0.084
    "images/fg/reimu/rei_mid_5.png" 
    pause 0.084  
    "images/fg/reimu/rei_mid_6.png"

image rei_down:
    "images/fg/reimu/rei_hit_3.png"
    pause 0.4
    "images/fg/reimu/rei_downed_1.png"
    pause 0.084
    "images/fg/reimu/rei_downed_2.png"
    pause 0.084
    "images/fg/reimu/rei_down_1.png"
    pause 0.084
    "images/fg/reimu/rei_down_2.png"
    pause 0.084    
    "images/fg/reimu/rei_down_3.png"
    pause 0.084
    "images/fg/reimu/rei_down_4.png"
    pause 0.084    
    "images/fg/reimu/rei_down_5.png"
    pause 0.084
    "images/fg/reimu/rei_down_6.png"
    pause 0.084   
    "images/fg/reimu/rei_down_7.png"
    pause 0.084    
    "images/fg/reimu/rei_down_8.png"
    pause 0.084
    "images/fg/reimu/rei_down_9.png"
    pause 0.084    
    "images/fg/reimu/rei_down_10.png"
    pause 0.084
    "images/fg/reimu/rei_down_11.png"

screen reimu_init():
    add "rei_idle" at init_appear

screen reimu_backdash():
    add "rei_bd"

screen reimu_hit():
    add "rei_hit"

transform reimu_idle_v3:
    xpos 120

screen reimu_idle():
    add "rei_idle" at reimu_idle_v3

screen reimu_oh():
    add "rei_oh" at reimu_idle_v3

screen reimu_oh_a():
    add "rei_oh_a" at reimu_idle_v3

screen reimu_low():
    add "rei_low" at reimu_idle_v3

screen reimu_low_a():
    add "rei_low_a" at reimu_idle_v3

screen reimu_mid():
    add "rei_mid" at reimu_idle_v3

screen reimu_mid_a():
    add "rei_mid_a" at reimu_idle_v3

screen reimu_vuln():
    add "rei_vuln" at reimu_idle_v3

screen reimu_hit_a():
    add "rei_hit_a"

screen reimu_down():
    add "rei_down"





transform keynav_a_appear:
    on show:
        xpos 306
        ypos 1280
        ease .3 ypos 647
    on hide:
        ease .3 ypos 1280

transform keynav_s_appear:
    on show:
        xpos 436
        ypos 1280
        ease .32 ypos 647
    on hide:
        ease .32 ypos 1280

transform keynav_d_appear:
    on show:
        xpos 566
        ypos 1280
        ease .34 ypos 647
    on hide:
        ease .34 ypos 1280
    
screen keynav_demo_1():
    # key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "joy_dismiss" action NullAction()
    key "K_a" action [Hide("evidence_fumo_screen_fg"), Jump(correct_jump)]
    key "K_s" action [Hide("evidence_fumo_screen_fg"), Jump(wrong_jump)]
    key "K_d" action [Hide("evidence_fumo_screen_fg"), Jump(wrong_jump)]


    imagebutton at keynav_a_appear:
        idle "images/evidence/fg_demo/keynav_1_a.png"
        hovered Show("evidence_fumo_screen_fg")
        unhovered Hide("evidence_fumo_screen_fg")
        action NullAction()

    imagebutton at keynav_s_appear:
        idle "images/evidence/fg_demo/keynav_1_s.png"

    imagebutton at keynav_d_appear:
        idle "images/evidence/fg_demo/keynav_1_d.png"

transform keynav_left_appear:
    on show:
        xpos 1354
        ypos 1280
        ease .1 ypos 647
    on hide:
        ease .1 ypos 1280

transform keynav_down_appear:
    on show:
        xpos 1484
        ypos 1280
        ease .12 ypos 647
    on hide:
        ease .12 ypos 1280

transform keynav_right_appear:
    on show:
        xpos 1614
        ypos 1280
        ease .14 ypos 647
    on hide:
        ease .14 ypos 1280

transform keynav_up_appear:
    on show:
        xpos 1484
        ypos 1280
        ease .12 ypos 517
    on hide:
        ease .12 ypos 1280

screen keynav_demo_2():
    # key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "joy_dismiss" action NullAction()

    timer interval repeat True action If(time_start > 0.01, true=SetVariable('time_start', time_start - interval), false=[Return(0), Jump(slow_jump)])

    key trigger_key action ( Jump(correct_jump) )
    key invalid_key action ( Jump(wrong_jump) )

    text "[time_start:.2f]" xpos 1354 ypos 777 size 50 outlines [ (3, "#000", 0, 0) ]

    imagebutton at keynav_left_appear:
        idle "images/evidence/fg_demo/keynav_left.png"

    imagebutton at keynav_down_appear:
        idle "images/evidence/fg_demo/keynav_down.png"

    imagebutton at keynav_right_appear:
        idle "images/evidence/fg_demo/keynav_right.png"

    imagebutton at keynav_up_appear:
        idle "images/evidence/fg_demo/keynav_up.png"

screen evidence_fumo_screen_fg():
    vbox:
        add "images/evidence/fg_demo/keynav_1_a_hover.png" xpos 306 ypos 467
        text "A fumo plushie of Marisa from Touhou.\nDoesn't seem useful. However, you have a\nfeeling it could be used to catch backdashes\nfrom around round-start position." size 25 xpos 456 ypos 305 outlines [ (3, "#000", 0, 0) ]

transform select_sus_appear:
    xpos 741
    ypos 1358
    on show:
        ease 0.5 ypos 78
    on hide:
        ease 0.5 ypos 1358

transform cheeto_dust_appear:
    xpos 1135
    ypos 1547
    on show:
        ease 0.5 ypos 267
    on hide:
        ease 0.5 ypos 1547
   
screen select_sus():
    # key "mouseup_1" action NullAction()
    key "K_RETURN" action NullAction()
    key "K_SPACE" action NullAction()
    key "K_KP_ENTER" action NullAction()
    key "joy_dismiss" action NullAction()

    add "images/evidence/investigation_1/evidence_fumo_box.png" at select_sus_appear

    add "images/evidence/fg_demo/select_prompt.png" at combo_prompt_appear
    
    imagebutton at cheeto_dust_appear:
        idle "images/evidence/investigation_1/cheeto_dust.png"
        hover "images/evidence/investigation_1/cheeto_dust_hover.png" 
        action Jump ("correct_9")

transform combo_prompt_appear:
    ypos 1280
    on show:
        ease 0.5 ypos 0
    on hide:
        ease 0.5 ypos 1280

image combo_pressed_1 = ConditionSwitch(
    "combo_pressed == 0", "images/blank.png",
    "combo_pressed == 1", "images/evidence/fg_demo/combo_p1_1.png",
    "combo_pressed == 2", "images/evidence/fg_demo/combo_p1_2.png",
    "combo_pressed == 3", "images/evidence/fg_demo/combo_p1_3.png",
    "combo_pressed == 4", "images/evidence/fg_demo/combo_p1_4.png",
    "combo_pressed == 5", "images/evidence/fg_demo/combo_p1_5.png",)

screen combo_prompt_1():
    add "images/evidence/fg_demo/combo_prompt_1.png" at combo_prompt_appear

    timer interval repeat True action If(time_start > 0.01, true=SetVariable('time_start', time_start - interval), false=[SetVariable('combo_pressed', 0), Jump(slow_jump)])

    key trigger_key action If( combo_pressed < 4, false=(SetVariable('combo_pressed', combo_pressed + 1), Jump(correct_jump)), true=(Play("sound", "/audio/sfx/sfx-bleep.wav"), SetVariable('combo_pressed', combo_pressed + 1)))
    key invalid_key action ( SetVariable('combo_pressed', 0), Jump(wrong_jump) )

    text "[time_start:.2f]" xpos 1354 ypos 777 size 50 outlines [ (3, "#000", 0, 0) ]

    add "combo_pressed_1" at combo_prompt_appear