
image protag default = "chars/protag_demo/CGMI10.png"
image protag hm = "chars/protag_demo/CGMI20.png"
image protag attack = "chars/protag_demo/CGMI30N.png"
image protag hurt = "chars/protag_demo/CGMI24N.png"

image chester default = "chars/chester/default.png"

transform p1_portrait:
    xpos -170
    ypos 1000
    on show:
        ease .5 ypos 700

transform p2_portrait:
    xpos 1420
    ypos 1000
    on show:
        ease .5 ypos 700

label fg_demo:
    default marisa_var = 0
    default reimu_var = 0
    default excl_var = 0
    default fight_state = 0
    default block_status = 2
    default combo_pressed = 0

    stop music fadeout .5
    "now we will shift over to a demo of the fighting game events"
    show wall1 onlayer master with shortdiss
    show protag default at p1_portrait onlayer fg_port
    show chester default at p2_portrait onlayer fg_port
    play music "/music/fg_demo.mp3" volume 0.1
    play audio "/audio/sfx/sfx-fwashing.wav" volume .5
    $ renpy.show_screen("fg_base", _layer="lower_screens")
    pause(.5)
    $ renpy.transition(vpunch)
    window show

    "It seems Chester Cheeto wants to deny what I'm saying."

    $ reimu_var = 1
    play audio "/audio/sfx/sfx-scenechange.wav" volume .3
    c "You don’t have any evidence of anything!"

    show protag hm onlayer fg_port with shortdiss
    "He’s kinda right… I don’t have much I can say here."
    "Looking at what I have, there’s nothing I have that says much of anything…"
    "Except... probably this."
    play audio "/audio/sfx/sfx-realization.wav" volume .3
    show protag default onlayer fg_port with shortdiss
    "Yeah, if I use this move, I think I can get somewhere."
    show protag hm onlayer fg_port with shortdiss
    "I'll press {i}that key{/i} on my keyboard."

label call_key_1:
    show protag default onlayer fg_port with shortdiss
    $ p("Actually, I have something to say...", interact=False)
    play audio "/audio/sfx/sfx-evidenceshoop.wav" volume .3
    $ correct_jump = "correct_1"
    $ wrong_jump = "wrong_1"
    call screen keynav_demo_1

label wrong_1:
    hide screen keynav_demo_1
    play audio "/audio/sfx/sfx-bvvt.wav" volume .3
    show protag hm onlayer fg_port with shortdiss
    "Uh… no, that’s probably not it."
    hide screen block_status
    $ block_status = 2

    "If I'm having trouble remembering what a move does, I can hover over the button."
    "Hovering over the button will show me a tooltip with the description of the move."
    show protag default onlayer fg_port with shortdiss
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    "Let’s try that again… What do I have that I can say?"
    jump call_key_1

label correct_1:
    $ marisa_var = 1
    $ reimu_var = 2
    $ fight_state = 1
    
    hide screen keynav_demo_1
    show protag attack onlayer fg_port with shortdiss
    play audio "/audio/sfx/sfx-fwashing.wav" volume .5
    $ renpy.pause(.5)
    $ renpy.transition(vpunch)
    $ renpy.pause(.5)
    play audio "/audio/protag/p_shikashi.mp3" volume 2
    p "I found this fumo of Marisa."

    $ marisa_var = 2
    $ reimu_var = 3
    play audio "/audio/sfx/sfx-bleep.wav" volume .3
    show protag default onlayer fg_port with shortdiss
    c "So what? People find stuff around all the time."

    show protag hm onlayer fg_port with shortdiss

    p "No, there’s something about this fumo that stood out to me."

    c "That’s nonsense, there’s nothing about that fumo that stands out to you. Nothing."

    $ reimu_var = 4
    play audio "/audio/sfx/sfx-scenechange.wav" volume .3
    c "Why are you even touching people’s stuff that’s not yours?"

    "Shoot, that looks like an overhead attack."
    play audio "/audio/sfx/sfx-realization.wav" volume .3
    "When I see an overhead attack, I should block standing by holding back using the arrow keys."
    show protag default onlayer fg_port with shortdiss
    "In this case, since I'm facing right, I should press the {i}left{/i} arrow key."

label call_key_2:
    $ excl_var = 1
    $ narrator("I've got to hurry and block this overhead!", interact=False)
    show screen excl_screen
    play audio "/audio/sfx/sfx-evidenceshoop.wav" volume .3
    $ time_start = 3
    $ time_max = 3
    $ interval = 0.01
    $ trigger_key = ["K_LEFT"]
    $ invalid_key = ["K_DOWN", "K_UP", "K_RIGHT"]
    $ correct_jump = "correct_2"
    $ wrong_jump = "wrong_2"
    $ slow_jump = "slow_2"

    $ cont = 0

    call screen keynav_demo_2

label slow_2:
    $ block_status = 1
label wrong_2:
    $ marisa_var = 3
    $ reimu_var = 5

    show protag hurt onlayer fg_port with shortdiss
    hide screen excl_screen
    hide screen keynav_demo_2
    play audio "/audio/sfx/sfx-bvvt.wav" volume .3
    $ renpy.show_screen("block_status", _layer="fg_ui")
    $ renpy.pause(.1)
    $ renpy.transition(vpunch)
    $ renpy.pause(.5)

    "Ouch, I didn't block correctly."
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2
    "Yeah, when I see an overhead, I've got to hurry and hold back to block standing."
    "I can't press the down arrow key, because then I'd be crouching."
    "And I shouldn't press the up or right arrow keys, because then I'd just get hit."
    $ marisa_var = 0
    $ reimu_var = 4
    show protag default onlayer fg_port with shortdiss
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    "Let's try that again. I'll hold the left arrow key to block standing before the overhead can hit me."
    jump call_key_2

label correct_2:
    $ marisa_var = 4
    $ reimu_var = 5
    $ fight_state = 2
    $ block_status = 0

    $ renpy.show_screen("block_status", _layer="fg_ui")
    hide screen excl_screen
    hide screen keynav_demo_2
    show protag attack onlayer fg_port with shortdiss
    play audio "/audio/sfx/sfx-fwashing.wav" volume .5
    $ renpy.pause(.1)
    $ renpy.transition(vpunch)
    $ renpy.pause(.4)
    $ renpy.pause(.5)
    play audio "/audio/protag/p_shikashi.mp3" volume 2
    p "That's not what this is about right now."
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2
    
    $ reimu_var = 6
    show protag default onlayer fg_port with shortdiss
    c "I think it is about that, stop touching things that aren’t yours."
    
    show protag hm onlayer fg_port with shortdiss
    "Now here comes a low attack."
    "In a real fighting game, I would have to hold downback to block this."
    play audio "/audio/sfx/sfx-realization.wav" volume .3
    "Here, though, I just need to hold the {i}down arrow key{/i} to crouch, and I'll block it."
    show protag default onlayer fg_port with shortdiss
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    "So, here it comes. This one's gonna be faster, so I've got to be quick."
   
label call_key_3:
    $ excl_var = 2
    $ narrator("I'll hold down to block this low!", interact=False)
    show screen excl_screen
    play audio "/audio/sfx/sfx-evidenceshoop.wav" volume .3
    $ time_start = 0.6
    $ time_max = 0.6
    $ interval = 0.01
    $ trigger_key = ["K_DOWN"]
    $ invalid_key = ["K_UP", "K_RIGHT"]
    $ correct_jump = "correct_3"
    $ wrong_jump = "wrong_3"
    $ slow_jump = "slow_3"

    $ cont = 0

    call screen keynav_demo_2

label slow_3:
    $ block_status = 1
label wrong_3:
    $ marisa_var = 5
    $ reimu_var = 7
    show protag hurt onlayer fg_port with shortdiss

    $ renpy.show_screen("block_status", _layer="fg_ui")
    hide screen excl_screen
    hide screen keynav_demo_2
    play audio "/audio/sfx/sfx-bvvt.wav" volume .3
    "That was pretty quick..."
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2
    "In the future, I might face attacks even faster than this."
    "I need to be ready to block any incoming attacks."
    "I've got to press the {i}down arrow key{/i} to block."
    $ marisa_var = 0
    $ reimu_var = 6
    show protag default onlayer fg_port with shortdiss
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    "Let's try this one more time."
    jump call_key_3

label correct_3:
    $ marisa_var = 6
    $ reimu_var = 7
    $ fight_state = 3
    $ block_status = 0

    $ renpy.show_screen("block_status", _layer="fg_ui")
    hide screen excl_screen
    hide screen keynav_demo_2
    show protag attack onlayer fg_port with shortdiss
    play audio "/audio/sfx/sfx-fwashing.wav" volume .5
    $ renpy.pause(.5)
    $ renpy.transition(vpunch)
    $ renpy.pause(.5)
    play audio "/audio/protag/p_shikashi.mp3" volume 2
    p "Sure, I admit I shouldn’t touch stuff that\nisn’t mine."
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2
    show protag default onlayer fg_port with shortdiss
    p "But I did find something interesting."
    
    c "You didn't find anything interesting. I'll say it again and again."

    show protag hm onlayer fg_port with shortdiss
    "Oh boy, here it comes."
    "Sometimes, the opponent will do multiple attacks in quick succession- a blockstring."
    "Then, I'll have to do multiple blocks in a row."
    "In a real fighting game, the strategy would be to hold downback and react to highs by switching to stand block on reaction."
    "However, here, holding won't work."
    "I have to press how I want to block for each attack."
    show protag default onlayer fg_port with shortdiss
    "By the way, not all attacks are overhead or low."
    "Some attacks are just mids, meaning I can block them either standing or crouching."
    "Chester Cheeto's pressure will contain a mix of mids, lows, and overheads."
    "That might seem like a lot to keep track of,"
    "but since mids can accept either a standing block or a crouching block,"
    play audio "/audio/sfx/sfx-realization.wav" volume .3
    "I should always {i}default to pressing the down arrow key{/i} to block."
    "When I know an assault is coming, I {i}only{/i} need to react to overheads-"
    "because that's the only type of attack that's different."
    show protag hm onlayer fg_port with shortdiss
    "Alright, let's get ready."
    show protag default onlayer fg_port with shortdiss
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    "His pressure is gonna begin now."

label call_key_4:
    $ excl_var = 3
    $ reimu_var = 8
    $ time_start = 1
    $ time_max = 1
    $ interval = 0.01
    $ trigger_key = ["K_LEFT", "K_DOWN"]
    $ invalid_key = ["K_UP", "K_RIGHT"]
    $ correct_jump = "correct_4"
    $ wrong_jump = "wrong_4_1"
    $ slow_jump = "slow_4_1"

    $ cont = 0

    play audio "/audio/sfx/sfx-evidenceshoop.wav" volume .3

    $ c("There's nothing interesting.", interact=False)
    show screen excl_screen

    call screen keynav_demo_2

label slow_4_1:
    $ block_status = 1
label wrong_4_1:
    $ marisa_var = 5
    $ reimu_var = 9
    jump wrong_4

label slow_4_2:
    $ block_status = 1
label wrong_4_2:
    $ marisa_var = 5
    $ reimu_var = 7
    jump wrong_4

label slow_4_3:
    $ block_status = 1
label wrong_4_3:
    $ marisa_var = 3
    $ reimu_var = 5
    jump wrong_4

label wrong_4:
    show protag hurt onlayer fg_port with shortdiss
    $ renpy.show_screen("block_status", _layer="fg_ui")
    hide screen excl_screen
    hide screen keynav_demo_2
    play audio "/audio/sfx/sfx-bvvt.wav" volume .3
    "I screwed up."
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2
    "I've just got to remember that overheads should be blocked by pressing back,"
    "lows should be blocked by pressing down,"
    "and mids can be blocked either way."
    $ marisa_var = 0
    $ reimu_var = 8
    show protag default onlayer fg_port with shortdiss
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    "Now, let's try again."
    jump call_key_4

label correct_4:
    $ marisa_var = 4
    $ reimu_var = 9
    $ block_status = 0

    $ renpy.show_screen("block_status", _layer="fg_ui")
    show protag attack onlayer fg_port with shortdiss
    hide screen excl_screen
    play audio "/audio/sfx/sfx-bling2.wav" volume .3
    pause(0.42)
    show protag default onlayer fg_port with shortdiss
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2

    $ reimu_var = 6
    $ excl_var = 2
    $ time_start = 1
    $ time_max = 1
    $ interval = 0.01
    $ trigger_key = ["K_DOWN"]
    $ invalid_key = ["K_UP", "K_RIGHT"]
    $ correct_jump = "correct_5"
    $ wrong_jump = "wrong_4_2"

    $ cont = 0
    $ c("You didn't find anything.", interact=False)
    show screen excl_screen

    call screen keynav_demo_2

label correct_5:
    $ marisa_var = 6
    $ reimu_var = 7
    $ block_status = 0

    show protag attack onlayer fg_port with shortdiss
    $ renpy.show_screen("block_status", _layer="fg_ui")
    hide screen excl_screen
    play audio "/audio/sfx/sfx-bling2.wav" volume .3
    pause(0.588)
    show protag default onlayer fg_port with shortdiss
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2

    $ reimu_var = 4
    $ excl_var = 1
    $ time_start = 1
    $ time_max = 1
    $ interval = 0.01
    $ trigger_key = ["K_LEFT"]
    $ invalid_key = ["K_DOWN", "K_UP", "K_RIGHT"]
    $ correct_jump = "correct_6"
    $ wrong_jump = "wrong_4_3"

    $ cont = 0
    $ c("Just be quiet.", interact=False)
    show screen excl_screen

    call screen keynav_demo_2

label correct_6:
    $ marisa_var = 4
    $ reimu_var = 5
    $ block_status = 0

    show protag attack onlayer fg_port with shortdiss
    $ renpy.show_screen("block_status", _layer="fg_ui")
    hide screen excl_screen
    play audio "/audio/sfx/sfx-fwashing.wav" volume .5
    $ renpy.transition(vpunch)
    pause(0.588)
    show protag default onlayer fg_port with shortdiss
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2

    hide screen keynav_demo_2
    c "You're so annoying!"
    "He’s going for a command grab now- I just know it."
    "Yeah, aside from overheads and lows, the opponent can also open me up using strike-throw."
    show protag hm onlayer fg_port with shortdiss
    "If the opponent mixes in throws, I actually do need to pay more attention..."
    "In a real fighting game, there could be any number of options to get out of a command grab,"
    "such as backdashing, DPing, or depending on the game, mashing a fast attack."
    "But here, I should definitely jump to avoid it."
    play audio "/audio/sfx/sfx-realization.wav" volume .3
    $ reimu_var = 8
    show protag default onlayer fg_port with shortdiss
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    "I’ll avoid this by pressing the {i}up arrow key!{/i}"

label call_key_5:
    $ excl_var = 4
    $ time_start = 1
    $ time_max = 1
    $ interval = 0.01
    $ trigger_key = ["K_UP"]
    $ invalid_key = ["K_DOWN"]
    $ correct_jump = "correct_7"
    $ wrong_jump = "wrong_5"
    $ slow_jump = "slow_5"

    $ cont = 0
    play audio "/audio/sfx/sfx-evidenceshoop.wav" volume .3

    $ c("Just be quiet.", interact=False)
    show screen excl_screen

    call screen keynav_demo_2

label slow_5:
    $ block_status = 1
label wrong_5:
    $ marisa_var = 5
    $ reimu_var = 9
    show protag hurt onlayer fg_port with shortdiss

    $ renpy.show_screen("block_status", _layer="fg_ui")
    hide screen excl_screen
    hide screen keynav_demo_2
    play audio "/audio/sfx/sfx-bvvt.wav" volume .3
    "Oops, I guess I messed up."
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2
    "I need to press up to avoid getting grabbed."
    $ marisa_var = 0
    $ reimu_var = 8
    show protag default onlayer fg_port with shortdiss
    "Let's try that again."
    jump call_key_5

label correct_7:
    $ marisa_var = 7
    $ reimu_var = 10
    $ block_status = 0

    show protag attack onlayer fg_port with shortdiss
    $ renpy.show_screen("block_status", _layer="fg_ui")
    hide screen excl_screen
    hide screen keynav_demo_2
    play audio "/audio/sfx/sfx-bling2.wav" volume .5
    "Great!"
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2
    show protag default onlayer fg_port with shortdiss
    "The thing about command grabs is that the opponent is usually open after a failed attempt."
    "So, while it can be a scary tool, it also has higher risk."
    "Now's my chance for a counterattack!"
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    "I'll use the evidence to do a landing counterattack!"

label call_key_6:
    $ p("I did find something interesting, and I'll prove it.", interact=False)
    play audio "/audio/sfx/sfx-evidenceshoop.wav" volume .3

    $ correct_jump = "correct_8"
    $ wrong_jump = "wrong_6"

    call screen keynav_demo_1

label wrong_6:
    hide screen keynav_demo_1
    play audio "/audio/sfx/sfx-bvvt.wav" volume .3
    show protag hm onlayer fg_port with shortdiss
    "Uh… no, that’s probably not it."
    "If I'm having trouble remembering what a move does, I can hover over the button."
    "Hovering over the button will show me a tooltip with the description of the move."
    show protag default onlayer fg_port with shortdiss
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    "Let’s try that again… What do I have that I can say?"
    jump call_key_6

label correct_8:
    $ marisa_var = 8
    $ reimu_var = 11

    show protag attack onlayer fg_port with shortdiss
    hide screen keynav_demo_1
    play audio "/audio/sfx/sfx-fwashing.wav" volume .5
    $ renpy.pause(.5)
    $ renpy.transition(vpunch)
    $ renpy.pause(.5)
    play audio "/audio/protag/p_shikashi.mp3" volume 2
    show protag default onlayer fg_port with shortdiss
    "I got him, now's my chance to do some real damage."
    play audio "/audio/sfx/sfx-evidenceshoop.wav" volume .3
    $ default_mouse = "investigate"
    $ p("The part of this fumo that's suspicious is this:", interact=False)

    call screen select_sus

label correct_9:
    play audio "/audio/sfx/sfx-bling2.wav" volume .3
    $ default_mouse = "default"
    hide screen select_sus

label call_key_7:
    show protag attack onlayer fg_port with shortdiss
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    $ narrator("Now for a combo! I'll mash the A key!", interact=False)
    $ time_start = 5
    $ time_max = 5
    $ trigger_key = ["K_a"]
    $ invalid_key = ["K_s", "K_d"]
    $ correct_jump = "correct_10"
    $ wrong_jump = "wrong_10"
    $ slow_jump = "slow_10"

    call screen combo_prompt_1

label slow_10:
    $ block_status = 1
label wrong_10:
    show protag hurt onlayer fg_port with shortdiss
    play audio "/audio/sfx/sfx-bvvt.wav" volume .3
    $ renpy.show_screen("block_status", _layer="fg_ui")
    "Oops."
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2
    "Guess I wasn't ready and had trouble hit-confirming."
    "Yeah, sometimes I'll have to keep pressing the opponent."
    "I'll have to input a certain combo within the time limit."
    show protag default onlayer fg_port with shortdiss
    play audio "/audio/protag/p_hajimeru.mp3" volume 2
    "Let's try that again."
    jump call_key_7

transform show_evidence:
    
label correct_10:
    $ block_status = 0
    $ marisa_var = 9
    $ reimu_var = 12

    show protag attack onlayer fg_port with flash
    $ renpy.show_screen("block_status", _layer="fg_ui")
    play audio "/audio/sfx/sfx-fwashing.wav" volume .5
    $ renpy.pause(0.3)
    $ renpy.transition(vpunch)
    hide screen combo_prompt_1

    show evidence_fumo_box at select_sus_appear onlayer fg_port
    p "There's some cheeto dust on this fumo!"
    $ renpy.hide_screen("block_status", layer="fg_ui")
    $ block_status = 2
    
    c "You got me... I was there and that's my fumo."
    c "You saw through everything. I bow to you."

    
    



