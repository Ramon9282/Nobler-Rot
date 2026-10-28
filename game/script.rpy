# The script of the game goes in this file.

init python:
    def totem_dragged(drags, drop):

        if 400 < drags[0].x < 1000 and 100 < drags[0].y < 600:
            return drags[0].drag_name

        return

init:
#Scenes
    image stage = "images/Scenes/stage_together.png"
    image school = "images/Scenes/stage_school.png"
    image gym = "images/Scenes/stage_gym.png"
    image potraits = "images/Scenes/stage_potraits.png"
    image dramaroom = "images/Scenes/stage_dramaroom.png"
    image cult = "images/Scenes/stage_cult.png"
    image e_bedroom = "images/Scenes/stage_e_bedroom.png"
    image c_bedroom = "images/Scenes/stage_c_bedroom.png"
    image bathroom = "images/Scenes/stage_bathroom.png"
    image alley = "images/Scenes/stage_alley.png"
    image ballroom = "images/Scenes/stage_ballroom.png"
    image mansion = "images/Scenes/stage_mansion.png"
    image vineyard = "images/Scenes/stage_vineyard.png"
    image backstage = "images/Scenes/backstage.png"
    image ritual_interface = "images/Scenes/Ritual_Interface.png"

#sprites
#ash
    image ash happy = "images/@2/Sprites/Ash_Happy.png"
    image ash sad = "images/@2/Sprites/Ash_Sad.png"
#mac
    image mac tired = "images/@2/Sprites/Mac_Tired.png"
    image mac fear = "images/@2/Sprites/Mac_fear.png"
#aarya
    image aarya catherine = "images/@2/Sprites/Aarya_Catherine_.png"
    image aarya dead = "images/@2/Sprites/Aarya_Dead.png"
    image aarya full = "images/@2/Sprites/Aarya_Full.png"
    image aarya incredulous = "images/@2/Sprites/Aarya_Incredulous_.png"
    image aarya sigh = "images/@2/Sprites/Aarya_Sigh.png"
    image aarya sure = "images/@2/Sprites/Aarya_Sure.png"
    image aarya woah = "images/@2/Sprites/Aarya_Woah.png"
    image aarya worried = "images/@2/Sprites/Aarya_Worried.png"
#andrea
    image andrea adec = "images/@2/Sprites/Andrea_ADEC.png"
    image andrea awe = "images/@2/Sprites/Andrea_Awe.png"
    image andrea creeped = "images/@2/Sprites/Andrea_Creeped.png"
    image andrea fear = "images/@2/Sprites/Andrea_Fear.png"
    image andrea okay = "images/@2/Sprites/Andrea_Okay.png"
    image andrea pride = "images/@2/Sprites/Andrea_Pride.png"
    image andrea serious = "images/@2/Sprites/Andrea_Serious.png"
    image andrea snark = "images/@2/Sprites/Andrea_Snark.png"
    image andrea ticked = "images/@2/Sprites/Andrea_Ticked.png"
#Catherine
    image catherine awkward smile = "images/@2/Sprites/Catherine_Awkward_Smile.png"
    image catherine bashful = "images/@2/Sprites/Catherine_Bashful.png"
    image catherine blush = "images/@2/Sprites/Catherine_Blush.png"
    image catherine content = "images/@2/Sprites/Catherine_Content_.png"
    image catherine frown = "images/@2/Sprites/Catherine_Frown.png"
    image catherine gay blush = "images/@2/Sprites/Catherine_Gay_Blush.png"
    image catherine shadow = "images/@2/Sprites/Catherine_Shadow.png"
    image catherine startled = "images/@2/Sprites/Catherine_Startled.png"
    image catherine stoic = "images/@2/Sprites/Catherine_stoic.png"
    image catherine worried = "images/@2/Sprites/Catherine_Worried.png"
#Emily
    image emily business = "images/@2/Sprites/Emily_Business_2.png"
    image emily curious = "images/@2/Sprites/Emily_Curious_2.png"
    image emily desperate = "images/@2/Sprites/Emily_Desperate.png"
    image emily flippant = "images/@2/Sprites/Emily_Flippant_2.png"
    image emily genuine = "images/@2/Sprites/Emily_Genuine_2.png"
    image emily gross = "images/@2/Sprites/Emily_Gross_2.png"
    image emily hurt = "images/@2/Sprites/Emily_Hurt_2.png"
    image emily mischievous = "images/@2/Sprites/Emily_Mischievous_2.png"
    image emily peeved = "images/@2/Sprites/Emily_Peeved_2.png"
    image emily relived = "images/@2/Sprites/Emily_Relived_2.png"
    image emily satisfied = "images/@2/Sprites/Emily_Satisfied_2.png"
    image emily scolding = "images/@2/Sprites/Emily_Scolding_2.png"
    image emily seductive = "images/@2/Sprites/Emily_Seductive_Final.png"
#Ophelia
    image ophelia comforting = "images/@2/Sprites/Ophelia_Comforting.png"
    image ophelia dissapointed = "images/@2/Sprites/Ophelia_Dissapointed.png"
    image ophelia excited = "images/@2/Sprites/Ophelia_Excited_.png"
    image ophelia isw = "images/@2/Sprites/Ophelia_ISW.png"
    image ophelia pain = "images/@2/Sprites/Ophelia_Pain.png"
    image ophelia passionate = "images/@2/Sprites/Ophelia_Passionate.png"
    image ophelia scared = "images/@2/Sprites/Ophelia_Scared.png"
    image ophelia shocked = "images/@2/Sprites/Ophelia_Shocked.png"
    image ophelia teary = "images/@2/Sprites/Ophelia_Teary.png"
    image ophelia wondering = "images/@2/Sprites/Ophelia_Wondering.png"
#Rei
    image rei alright = "images/@2/Sprites/Rei_Alright.png"
    image rei cmon man = "images/@2/Sprites/Rei_Cmon_Man.png"
    image rei death = "images/@2/Sprites/Rei_death.png"
    image rei hcy = "images/@2/Sprites/Rei_HCY.png"
    image rei hyped = "images/@2/Sprites/Rei_Hyped.png"
    image rei iwiwlt = "images/@2/Sprites/Rei_IWIWLT.png"
    image rei oops = "images/@2/Sprites/Rei_Oops.png"
    image rei regular guy = "images/@2/Sprites/Rei_Regular_Guy.png"
#Rose
    image rose bashful = "images/@2/Sprites/C_Rose_Bashful.png"
    image rose content = "images/@2/Sprites/Rose_Content.png"
    image rose demure = "images/@2/Sprites/Rose_Demure.png"
    image rose listening = "images/@2/Sprites/C_Rose_Listening_.png"
    image rose oh boy = "images/@2/Sprites/C_Rose_Oh_Boy.png"
    image rose startled = "images/@2/Sprites/C_Rose_Startled.png"
    image rose worried = "images/@2/Sprites/C_Rose_Worried.png"
    image rose dead = "images/@2/Sprites/Red_Rose.png"

#CGs
    image opening_1 = "images/Scenes/CGs/Opening_1.png"
    image opening_2 = "images/Scenes/CGs/Opening_2.png"
    image opening_3 = "images/Scenes/CGs/Opening_3.png"
    image opening_4 = "images/Scenes/CGs/Opening_4.png"
    image opening_5 = "images/Scenes/CGs/Opening_5.png"
    image opening_6 = "images/Scenes/CGs/Opening_6.png"
    image c_flashback_1 = "images/Scenes/CGs/FINAL C_Flashback_1.png"
    image c_flashback_2 = "images/Scenes/CGs/FINAL C_Flashback_2.png"
    image c_flashback_3 = "images/Scenes/CGs/FINAL C_Flashback_3.png"
    image chud_flashback_1 = "images/Scenes/CGs/FINAL Chud_1.png"
    image chud_flashback_2 = "images/Scenes/CGs/FINAL Chud_2.png"
    image e_flashback_1 = "images/Scenes/CGs/FINAL E_Flashback_1.1.png"
    image e_flashback_2 = "images/Scenes/CGs/FINAL E_Flashback_1.2.png"
    image e_flashback_3 = "images/Scenes/CGs/FINAL E_Flashback_1.3.png"
    image e_flashback_4 = "images/Scenes/CGs/FINAL E_Flashback_2.1.png"
    image e_flashback_5 = "images/Scenes/CGs/FINAL E_Flashback_2.2.png"
    image e_flashback_6 = "images/Scenes/CGs/FINAL E_Flashback_3.png"
    image teeth_bared = "images/Scenes/CGs/FINAL Teeth_Barred.png"
    image drinking = "images/Scenes/CGs/FINAL Drinking.png"
    image the_kiss = "images/Scenes/CGs/FINAL The_Kiss.png"
    image hold_1 = "images/Scenes/CGs/Hold_1.png"
    image catherine_love = "images/Scenes/CGs/FINAL Catherine_in_Love.png"
    image emily_red = "images/Scenes/CGs/Emily_in_Red.png"
    image Heart_in_dark = "images/Scenes/CGs/FINAL Heart_In_the_Dark_1.png"
    image Heart_in_dark_2 = "images/Scenes/CGs/FINAL Heart_In_the_Dark_2.png"

#Success Cards
    image success_emily = "images/@4/Success_Card_Emily.png"
    image success_catherine = "images/@4/Success_Card_Catherine.png"

#Transforms
    transform flip:
        xzoom -1.0

    transform card_center:
        xalign 0.5
        yalign 0.5
    transform card_left2:
        xalign 0.25
        yalign 0.5
    transform card_right2:
        xalign 0.75
        yalign 0.5
    transform card_left3:
        xalign 0.167
        yalign 0.5
    transform card_mid3:
        xalign 0.5
        yalign 0.5
    transform card_right3:
        xalign 0.833
        yalign 0.5

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Emily", color="#f3ebbd")
define c = Character("Catherine", color="#ae639c")
define op = Character("Ophelia", color="#ef84ac")
define ro = Character("Rose")
define fr = Character("\"Rose\"")
define fake_aarya = Character("\"Aarya\"")
define aa = Character("Aarya", color="#ce5146")
define an = Character("Andrea", color="#fef5c5")
define ash = Character("Ash", color="#cf8530")
define mac = Character("Mac", color="#f7cf9e")
define re = Character("Rei", color="#56b1c2")
define fb = Character("Father Bell")
define cf = Character("Father")
define cm = Character("Mother")
define mb = Character("Mr. Braxton")
define vo = Character("Voice")
define na = Character(" ", what_italic=True)

default persistent.done_emily = False
default persistent.done_catherine = False

#Settings
style default:
    textshader "typewriter"

define character = 0
define death = 0
default ritual = 0
default ritual_cards = []

# The game starts here.

label start:
    jump the_meeting

label scenes:
    menu scene_selector:
        "What month do you want?"
        "Month 1":
            menu month_1:
                "Catherine, Emily, or Both?"
                "Cathy":
                    menu catherine_flashbacks:
                        "Which Scene?"
                        "Catherine Flashback 1":
                            jump catherine_flashback_1
                        "Catherine flashback 2":
                            jump catherine_flashback_2
                        "Catherine flashback 3":
                            jump catherine_flashback_3
                        
                "Ems":
                    menu emily_flashbacks:
                        "Which Scene?"
                        "Emily flashback 1":
                            jump emily_flashback_1
                        "Emily flashback 2":
                            jump emily_flashback_2
                        "Emily flashback 3":
                            jump emily_flashback_3

                "Both":
                    menu both_month_1:
                        "Which Scene?"
                        "the meeting":
                            jump the_meeting
                        "it knows you by name":
                            jump it_knows_you_by_name
                        "mansion":
                            jump mansion
                        "an awkward dinner":
                            jump an_awkward_dinner
                        "the orchestra":
                            jump the_orchestra
                        "under the chandelier":
                            jump under_the_chandelier
                        "first time drinking":
                            jump first_time_drinking
                        "the plan":
                            jump the_plan
                        "More":
                            menu more_scenes_1:
                                "Which Scenes?"
                                "rose's murder":
                                    jump roses_murder
                                "Ritual 1":
                                    jump ritual_one
                                "Catherine's breakdance":
                                    jump catherine_breakdown
                                "First day of school":
                                    jump first_day_of_school
                                "Drama club":
                                    jump drama_club
                        
                
        "Month 2":
            menu month_2:
                "Which Scene?"
                "Ophelia's Comedy":
                    jump ophelias_comedy
                "Love like you":
                    jump love_like_you
                "Ophelia's Death":
                    jump ophelias_death
                "Ritual 2":
                    jump ritual_two
                "Licky Licky":
                    jump licky_licky
                "Vomit":
                    jump vomit
                "Love Letter":
                    jump love_letter
        "Month 3":
            menu month_3:
                "Which Scene?"
                "Catherine and Aarya Scene 1":
                    jump catherine_month_3_aarya
                "Emily and Aarya Scene 1":
                    jump emily_month_3_aarya
                "Emily and Aarya Scene 2":
                    jump emily_aarya_alone_time
                "Occult Rush Vampirefunk":
                    jump occult_rush_vampirefunk
                "Ritual 3":
                    jump ritual_three
                "Lock in Em":
                    jump lock_in_em
        "Month 4":
            menu month_4:
                "Catherine, Emily, or both?"
                "Cathy":
                    menu catherine_month_4:
                        "Which Scene?"
                        "Mac month 4":
                            jump mac_month_four
                        "Andrea month 4":
                            jump andrea_month_four
                        "The murder of Andrea Barron":
                            jump the_murder_of_andrea_barron
                        
                "Ems":
                    menu emily_month_4:
                        "Which Scene?"
                        "Glass closet opens":
                            jump glass_closet_opens
                        "crime alley":
                            jump crime_alley
                        "Rei lives":
                            jump rei_lives
                        
                        
                "Both":
                    menu both_month_4:
                        "Which Scene?"
                        "Cast party":
                            jump cast_party
                        "The fight":
                            jump the_fight
                        "Andrea died":
                            jump andrea_died
                        "Rei dies":
                            jump rei_dies
                        "Andrea Lived":
                            jump andrea_lived
                        "Play or not to play":
                            jump play_or_not_to_play
                        "Last Dance":
                            jump last_dance
                        "Blood Ritual":
                            jump blood_ritual
                        "More":
                            menu more_scenes_2:
                                "Which Scenes?"
                                "Andrea Confrontation":
                                    jump andrea_confrontation
                                "Sgt Rei Doakes":
                                    jump sgt_rei_doakes
                                
        "Rituals":
            menu ritual_menu:
                "Which Ritual"
                "Ritual 1: Rose":
                    jump ritual_one
                "Ritual 2: Ophelia":
                    jump ritual_two
                "Ritual 3: Aarya":
                    jump ritual_three
                "Ritual 4: Andrea":
                    jump ritual_four_andrea
                "Ritual 4: Rei":
                    jump ritual_four_rei
                "Blood Ritual":
                    jump blood_ritual
                
        "Endings":
            menu ending_scenes:
                "Which Ending?"
                "Catherine ending":
                    jump catherine_ending
                "Emily ending":
                    jump emily_ending
                "Final Ending":
                    jump true_ending

label Insert_name1:
    define nar = character("'Narrarator'")
    
    na "Scene One: The Reading of the Play"

    na "August 23rd, 1993 - Lombardy University"

    an "Let's start from the top."


    “NARRATOR”
    *Clears throat*

    The immortal walls of the Lyon Mansion stand impervious to the rain, peering down the hills of Fritmoor like an ancient gargoyle. Yet, in the bowels of such decadence—

    REI
    Gnarly!

    ANDREA
    What? 

    REI
    Bowels.  

    ANDREA
    (Sighing) We’re barely a sentence in. 

    REI
    Exactly. And you used the word bowels. 

    AARYA
    I’m going to keep reading. 

    “NARRATOR”
    —Yet in the bowels of such decadence, fate carved a bloody new grave. One fitted perfectly for the body of Catherine Lyon.


    “CATHERINE”
    No, No! 

    “VAMPIRE”
    Hush now pet, it will be over soon. 

    “CATHERINE”
    Stay back! Please, stay back! 

    “VAMPIRE”
    Your beauty enthralls me. I must have you to join me in the eternal dark. 

    “CATHERINE”
    NOOOOoooo -

    “NARRATOR”
    Her screams died in her throat…cause some teeth were in it. Catherine’s parents rush onto the scene: dismayed, and all too late. 

    “FATHER”
    You—you DEMON! What have you done to my daughter!? 

    “NARRATOR”
    The creature rises to its feet, reinvigorated.

    “VAMPIRE”
    The true question is, what will your daughter do to YOU!? 

    “NARRATOR”
    And so too, does the spawn.


    REI
    Sick em’! 

    OPHELIA
    Rei! Focus! 

    “VAMPIRE”:
    Sicketh them! 

    REI
    Oh shit! He actually says that?! 

    OPHELIA
    Shhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhhh (keeps going until “Narrator” abruptly cuts in)

    “NARRATOR”
    Catherine clutched her stomach, unsure if she was still herself, or simply a beast made of her own ravenous urges. 

    “CATHERINE”
    I can’t…contain it…this…HUNGER. 

    “MOTHER”
    No! My darling, my sweet girl, this isn’t you! 

    “NARRATOR”
    The mother’s horror is met only with triumphant laughter.


    “VAMPIRE”
    You fool. She is a creature of the night now. Your words cannot reach her. 

    “MOTHER”
    You bastard!

    “VAMPIRE”
    You bitch! 

    “FATHER”
    Hey! (a really long pause coding wise) Don’t talk to my wife that way! 

    “CATHERINE”
    …Forgive me Mother. 

    “MOTHER”
    No, NOOOOOOOOOOO!

    “FATHER”
    IT CAN’T BEEEEEEE!

    “NARRATOR” 
    Their flesh was supple, and their blood was sweat. 

    REI
    Typo! Typo alert! 

    ANDREA
    Rei. 

    REI
    Shutting up, shutting up— 

    “NARRATOR” 
    Their flesh was supple and their blood was sweet. 

    “VAMPIRE”
    Finally, my darling, you have partaken! Rise, my creature of darkness! Join me as my bride! 

    “CATHERINE” 
    (Bloodlusting) Grrr

    “VAMPIRE”
    Oh shit.

    “NARRATOR”
    He had no blood to feast on, but that did not stop Catherine from tearing his muscles apart fiber by fiber. Bones, once set for an eternity, snapped in two when met with her newborn strength. Soon, Catherine’s vengeance left nothing but a mangled pile on the floor. 

    MAC
    Jeez. 

    “NARRATOR”
    We do not know how this story ends. Many say Catherine fled into the night, trying to outrun the truth of her corrupted form. Her mansion - the same one over that very hill - was left to rot, the last witness of the horrors that took place inside. 

    Decades later, a through line of unease still connects all of us: woven around our hearts and squeezing with each rumor. We ask ourselves, in the most hushed corners of our minds: 

    Is that house… truly empty?


    END OF PLAY. 

    …

    MAC
    I don’t know Andrea. It seems a bit flowery. 

    OPHELIA
    Mac!

    AARYA
    You aren’t the one performing it. What do you care if it’s “flowery”? 

    OPHELIA
    The flowery-ness isn’t a problem! It’s a style choice. 

    MAC
    But I’m teching it. My name's going to be in the program. I’ll be associated. 

    OPHELIA
    C’mon Mac…Andrea poured her heart into this—

    ANDREA
    I poured a lot of caffeine into this. 

    Ophelia throws her head back and sighs. 

    OPHELIA
    I see even you think I’m over reacting. 

    ANDREA
    Nah, I’m just a lot less sensitive than you are.                  
    Andrea punches Ophelia’s shoulder lightly. 

    OPHELIA
    For the record, I really do love it. 

    ANDREA
    Snrk. Thanks O. 

    OPHELIA
    And no, I’m NOT just saying that ASH. 

    ASH
    I wasn’t going to say anything. 

    MAC
    …I was. 

    OPHELIA
    No you were not! 

    ANDREA
    Criticism received Mac, I’ll get you the revised script at Saturday’s rehearsal. EVERYBODY HEAR THAT? DON’T FORGET! REHEARSAL IS EVERY SATURDAY!

    REI
    Yeah, yeah. No need to drill it into our heads. 

    ANDREA
    I am drilling it because one of you was late today. 

    REI
    Hey! I told you that was a one time thing! 

    ANDREA
    No, you told me missing callbacks was a one time thing. Today’s lateness went by unremarked. 

    REI 
    Wack! You know you looooooove meeeee. 

    ANDREA 
    Completely irrelevant. 

    AARYA
    If you’re done disciplining Rei, may we be dismissed?

    ANDREA 
    When is our next rehearsal?

    ALL 
    Saturday! 

    ANDREA
    Then you all can go. 

    Ophelia runs over to Emily, sandwiching one of  Emily’s hands in between hers. 

    OPHELIA 
    Is it time? 

    EMILY
    Not so loud! 

    OPHELIA
    Let’s get out of here! 

    Ophelia pulls Emily from her seat, and they rush out of the room after Rei, who has already bolted. Aarya trails behind them.

    jump it_knows_you_by_name


    play music "murder_song.mp3"
    scene vineyard
    show emily flippant at left
    show rose content at right
    play audio "walk_grass.mp3"
    e "The ground is a little rough around here, don’t snap your ankles."

    ro "Thank you for the warning, I’ll try to abide by it."

    show emily mischievous at left
    e "Pssh you’re still so polite."

    ro "I try to be."

    show emily peeved at left
    e "Maybe you should try less, people are gonna think you’re hiding something, you’re too nice."

    ro "I’m not really worried about what they think, as long as I know {i}I{/i} have integrity. And I wouldn’t want to stop being nice just because people judge me for it."

    show emily flippant at left
    e "Yeah... right."

    play audio "walk_grass.mp3"
    na "Emily and Rose continue to make their way over the bumpy dirt and stones. The path to the Vineyard begins to be clearer."

    e "This way."

    na "Rose attempts to follow Emily into the withered leaves, but Emily suddenly stops."

    show emily curious at left
    e "Hey..."

    ro "Yes?"

    e "Why’d you come?"

    show emily peeved at left
    na "Emily turns around to face Rose."

    e "When I invited you to a collapsing mansion, at night, with me – who you haven’t talked to in years. Why’d you come?"

    ro "Because I’m a crappy Christian. And I’ve never been good at staying away from you."

    show emily flippant at left
    e "..."

    na "Emily steps further into the Vineyard getting shrouded by the dark. Rose follows."

    show emily mischievous at left
    e "...I didn’t say “crappy”"

    ro "I still don’t swear."

    show emily flippant at left
    e "Oh yeah... cause words are so big and scary."

    ro "Don’t make me recite the doctrine to you."

    show emily satisfied at left
    e "Oh yeah, no {i}those{/i} words are scary."

    na "Rose can’t suppress her smile. Neither can Emily."

    show rose demure at right
    ro "You know why I picked Lombardy, right?"

    show emily curious at left
    e "Yeah, I was surprised you ended up here, you were always so smart, could’ve gone anywhere."

    ro "Yeah, but..."

    ro "I wanted to go where you –"

    
    
    show rose dead at right
    with Dissolve(.05)
    play audio "knife_stab.mp3"
    na "Suddenly, a claw punches through Rose’s stomach. For a moment everyone is still."
    play sound "heartbeat_sound.mp3"
    ro "{cps=*.2}Hra - {w=.4}{i}Huhg-{/i} {w=.4}Hah -{w=.2} {i}rah{/i}{w=.1} {/cps}{cps=*.7}{b}aaaaaa{i}AAAAAAAAAAAAAAA{/i}{/b}{/cps}!!!!!!"

    show emily gross at left
    e "Why’d you choose her stomach!?"

    show rose dead at center
    show catherine shadow at right
    c "It was the softest area of least resistance."

    show emily scolding at left
    e "You have super strength! You don’t need “least resistance”!"

    hide rose
    with moveoutbottom
    ro "Rose falls to her knees, still screaming bloody murder. The only thing cutting her off is the guttural choking and the blood clogging her throat."

    show emily desperate at left
    e "We need to shut her up!"

    show catherine worried at right
    c "Do you want me to go for the throat?"

    show rose dead at center
    ro "Emn– wrily..."

    show emily gross at left
    e "Crush her head."

    show catherine startled at right
    c "Are you sure?"

    show emily scolding at left
    e "DO IT!"

    show emily scolding at left
    show catherine shadow at right
    play audio "bones_breaking.mp3"
    na "Catherine slams her fist into the side of Rose’s head, and mercifully, the screaming stops."
    
    hide rose
    hide emily
    hide catherine
    jump ritual_one

label Insert_name2:

label Insert_name3:

label Insert_name4:

label Insert_name5:

label Insert_name6:

label Insert_name7:

label Insert_name8:

label Insert_name9:

label Insert_name10:

label Insert_name11:

label Insert_name12:

label Insert_name13:

label Insert_name14:

label Insert_name15:

label Insert_name16:

label Insert_name17:

label Insert_name18:

label Insert_name19:

label Insert_name20:

label Insert_name21:

label Insert_name22:

label Insert_name23:

label Insert_name24:

label Insert_name25:

label Insert_name26:

label Insert_name27:

label Insert_name28:

label Insert_name29:

label Insert_name30:

label Insert_name40:

label Insert_name41:

label Insert_name42:

label Insert_name43:

label Insert_name44:

label Insert_name45:

label Insert_name46:

label Insert_name47:

label Insert_name48:





label ritual_one:
    play music "ritual_song.mp3"
    scene vineyard

    screen ritual_one_screen(res):
        add "ritual_interface"

        draggroup:
            if "Music Box" not in res:
                drag:
                    drag_name "Music Box"
                    droppable False
                    dragged totem_dragged
                    xpos 0 ypos 0
                    add "@4/Roses_Music_Box.png"

            if "Pin Cushion" not in res:
                drag:
                    drag_name "Pin Cushion"
                    droppable False
                    dragged totem_dragged
                    xpos 700 ypos 600
                    add "@4/Wrist_Pin_Cushion.png"

            if "Hair Clip" not in res:
                drag:
                    drag_name "Hair Clip"
                    droppable False
                    dragged totem_dragged
                    xpos 1400 ypos 0
                    add "@4/Roses_Hair_Clip.png"

    $ res = []

    while len(res) < 3:
        call screen ritual_one_screen(res)
        
        if _return != None:
            
            if _return == "Music Box":
                e "Family matters a lot to Rose...I want her to see that she isn’t stuck with her blood one."

                menu:
                    "Add Rose's Music Box?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Pin Cushion":
                e "She would get poked by these things all the time."
                e "Didn’t even tear up."
                e "I had to point it out to her for her to notice."

                menu:
                    "Add Rose's Wrist Pin Cushion?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Hair Clip":
                e "I actually had this one."
                e "She gave it to me in Sophomore year when we first became friends."
                e "She never asked for it back."

                menu:
                    "Add Rose's Hair Clip?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            else:
                pass

    stop music fadeout 1.0
    play audio "ritual_complete.mp3"
    $ renpy.pause(1.5, hard=True)
    pause

    jump catherine_breakdown

    play music "ritual_song.mp3"
    scene vineyard
    show emily genuine at left
    show catherine stoic at right

    na "Emily and Catherine stand in the middle of the vineyard, with Emily holding a small ritualistic knife and a jar with a thin piece of saran wrap covering the top in her pocket."
    na "They stand, starting down at the ground."
    na "Emily surprises Catherine with a hug."

    e "This is it."

    show catherine frown at right
    c "Yes, I suppose it is."

    show emily satisfied at left
    e "Thank you, again."

    show catherine content at right
    c "... Yes, I’m glad to be here."
    na "Emily looks up at Catherine, happy. She releases her hug, and then breathes in."

    show emily flippant at left
    e "Alright, let’s do it."
    play audio "knife_dirt.mp3"
    na "Emily takes the knife and marks out a rhombus in the ground, with the bodies of the 4 girls buried beneath each of the 4 corners."
    na "Inside the rhombus, she sketches out a pentagram, before sketching out a triangle outside the rhombus."
    na "She holds out the jar to Catherine."

    e "Bite in here."
    na "Catherine bites into the saran wrap."
    na "A slightly green, translucent liquid leaks out of her teeth."
    na "Emily pulls the jar back out, and pours a bit of the venom on each corner of the triangle, then the rhombus, then the pentagram."

    e "Alright, now bite here."
    na "Emily points to her arm."
    play audio "heartbeat_sound.mp3"
    na "Catherine carefully bites, taking a sip, before letting go and leaving Emily with an open wound."
    na "Emily walks around, and makes sure to drip some of her blood on each corner of the pentagram, then the rhombus, then the triangle."

    e "Almost done, just come over here."
    na "Emily leads Catherine to the center of the pentagram, She writes in a few lines in the ground using her knife in Latin,"
    na "dipping the knife in her own blood like ink on a quill, digging the text into the ground."
    na "Emily gestures for them to sit, and the two lay down in the middle of the ritual shape they’ve created."
    show emily desperate at left
    na "Emily leans over and kisses Catherine, softly."

    e "I love you, Catherine."

    show catherine gay blush at right
    c "I love you as well."
    na "The two look at each other, intensely, relaxing themselves on the ground."
    na "The air is warm, and the two feel soothed in each other’s presence."
    hide emily
    hide catherine
    na "They lay down fully, and close their eyes, Emily’s left hand holding Catherine’s right."
    na "The blood moon moves above them, slowly approaching the apex of its position in the sky."
    na "The two girls wait as the moon calmly floats over, as the final part of the ritual is about to be put into place."
    na "... "

    na "The two girls are fully relaxed."
    na "Consciousness escapes them for a moment, and they find themselves in a sleep like trance."
    na "Visions of their ideal worlds flash in front of them, where they stand together, with the friends they’ve lost on the path reunited with them once again."
    na "They feel happy, and content."
    na "..."
    na "Emily opens her eyes."
    na "The sun has crept over the horizon, with it clearly being past noon."
    na "Catherine is fast asleep."
    na "She lies in the middle of a vineyard, with an oddly complex shape drawn into the ground."
    na "She slowly gets up, before looking down and seeing Latin text beneath her."
    na "She blinks, focusing a bit, and looks over at the corners of the rhombus."
    na "They seem nearly identical to how they were the previous night, with just the blood fully dried."
    na "Catherine opens her eyes. She wishes that she hadn’t, as she looks over at Emily, a horrified expression on her face."

    play music "murder_song.mp3"
    show emily peeved at left
    show catherine startled at right

    e "Fuck."

    show catherine worried at right
    c "What?"
    na "Emily looks over quickly at Catherine. She’s tense."

    e "Catherine, it didn’t work."

    c "It didn’t work?"

    show emily scolding at left
    e "It didn’t fucking work Catherine, look."
    na "Emily points over vaguely to her right."

    e "They’re not fucking here yet!"

    show catherine worried at right
    c "Who?"
    if death == 0:
        show emily desperate at left
        e "Rose!"
        e "Ophelia!"
        e "Aarya, even Andrea."
    else:
        show emily desperate at left
        e "Rose!"
        e "Ophelia!"
        e "Aarya, even Rei."

    c "Are they supposed to be here?"

    show emily flippant at left
    e "I – I mean."
    na "Emily thinks for a moment."

    e "Maybe, uh, hah, maybe they just aren’t here yet, yeah! They’re probably doing just fine, like, like from before."
    show catherine startled at right
    na "Catherine looks at Emily. Her eyes widen as she gets up."

    c "Emily, what exactly was supposed to change?"

    show emily desperate at left
    e "We were supposed to be put in paradise. And, well, just the people we brought were supposed  to come with us."

    show catherine worried at right
    c "What does paradise look like?"

    show emily flippant at left
    e "Well, um, —"
    na "Emily looks around, panicked."

    show emily scolding at left
    e "I guess it looks just like hell! Maybe they’re just, the fucking same!"

    show catherine startled at right
    c "Emily, please, tell me you know more!"
    na "Catherine looks horrified as well now. Her voice comes out pained."

    show emily desperate at left
    e "I thought, I thought –"

    na "Emily starts to cry."

    e "FUCK, Catherine, I thought I knew!"
    na "Emily’s phone starts to ring. She suddenly composes herself, with an unnatural smile on her face."

    show emily flippant at left
    e "God please tell me..."
    na "Emily answers the phone."

    if death == 0:
        e "Hello Rei?"

        re "Emily, you were supposed to be here 15 minutes ago!"

        e "Wait, I’m sorry I just woke up, I –"

        re "You have 30 minutes or else I am calling it off and sending everyone home!"
        re "Jesus Christ, it’s 5 pm, day of the play, and you still can’t wake up on time!"
        re "{i}You{/i} insisted on performing this too."

        e "Rei, has everyone-"

        re "I’m not dealing with this bullshit."

        na "Rei hangs up."

    else:
        e "Hello Mac?"

        mac "Yeah, Emily, where are you?"

        e "What?"

        mac "Oh my god please don’t tell me you FORGOT! You were supposed to be here 15 minutes ago!"

        e "Wait, I’m sorry I just woke up, I —"

        mac "Look, it’s fine. Just get here in the next half hour."

        e "Mac, please, is, is everyone else shown up?"

        mac "Andrea is here. "

        e "And, and is that it?"
        mac "..."
        mac "God, it was your idea to keep doing this Emily."
        mac "Just get here and get it over with, please."
        na "Mac hangs up. Emily stands for a moment, stunned."

    show catherine worried at right
    c "Should, should we go?"

    show emily peeved at left
    e "..."
    show emily flippant at left
    e "Fuck, you know what, why not?"
    e "I don’t want to kill myself here."
    hide emily
    hide catherine
    na "Emily walks off towards the theater. Catherine follows."

    if death == 0:
        jump sgt_rei_doakes
    else:
        jump andrea_confrontation

label endings:
    if ritual > 1:
        jump emily_ending
    else:
        jump catherine_ending

label emily_ending:
    play music "intimate_song.mp3"
    scene backstage
    show catherine worried at right
    c "Emily, I love you!"
    c "Why don't you believe me!"
    c "Please, let me be enough for you."
    c "I'm trying to give you everything, but it's all I have."
    c "I don't want you to leave, please - oh goodness, don't leave."
    c "I'm sorry, I'm sorry you have to see me like this, but I promise, I’ll be better, I’ll do anything you want,"
    c "I’ll be anyone you want, I can be rose forever just, let me protect you, let me fix this, let me make it go away."
    c "I’ll be enough for you Emily- Please let me be enough for you."
    c "I'm sorry, I'm so sorry, I'm disgusting, and it's so selfish, but I need you."
    c "I need you Emily."
    c "I can make this all better, I just need you."

    show emily genuine at left
    e "Catherine...here is what we are going to do. You’re going to turn me."

    show catherine startled at right
    c "What I-"

    show emily peeved at left
    e "Do not protest."
    e "Listen, There's no way we're getting out of this one unless we can both fight, I can’t be dead meat."
    e "They'll get me."

    show catherine worried at right
    c "Emily, you don't want this! You’ll be-"
    na "She searches for the words."

    c "Stuck! Permanently!"

    show emily desperate at left
    e "I’ll be with you."
    e "It's our paradise, our own little paradise, immortal together, hidden from this world, and when it comes for us, we can bite back."
    e "We can have it all -"

    show catherine frown at right
    c "But what about our friends?"

    show emily genuine at left
    e "...I’m sure they’ll never leave us either."

    show catherine shadow at right
    c "I can’t...I can’t curse you."
    c "You deserve to be free of all this..."
    c "Emily I can’t."

    show emily desperate at left
    e "You can."
    e "I know you can."
    e "Because you have to."
    na "Catherine smells fresh blood."
    show catherine startled at right
    c "What?"
    play audio "knife_stab.mp3"
    na "Emily pulls away, revealing that in the crush of their embrace, she has planted her demise."
    na "Emily has stabbed herself with her knife."
    hide emily
    e "Dammit, too slow."
    e "Th- blwegh - There we go."
    show catherine worried at right
    c "No...no no no... not like this, we were supposed to have years...I haven't had time, you haven't had time."
    e "But I will. Because you’re going to bring me back."
    na "Emily puts her forehead to Catherine’s."
    e "I love you."
    e "I don't say it enough."
    e "I love you."
    c "Emily..."
    na "Catherine can hear voices."
    na "She has minutes, if not seconds."
    na "What else does she have?"
    na "Her head...her gut...her heart."
    na "What can she do?"
    na "From the floor, Emily gurgles in an attempt at a chuckle. The blood is pooling around her like a halo, like wings."

    e "Pfft, I’m so fragile."
    na "She turns her head to Catherine, it wobbles, goes further than she wants it to, then comes back. It’s what she used the last of her effort on."

    e "I’ll see you soon."
    e "..."

    na "Blackness."
    play audio "heartbeat_sound.mp3"
    na "A heart, beating in the dark...barely."
    na "It's damaged, bleeding."
    na "Then, it's jostled from its crevice."
    na "It pulls away into the endless dark, a ship out onto an eternal ocean."
    na "Blipping its signal from afar, dripping its blood on the ground."
    na "Blip Blip Blip and then:"
    na "Gone. "
    na "Is it the most scared she’s ever been in her life? She doesn’t think so."
    play audio "ribs_opening.mp3"
    na "Fire. IGNITION."
    na "A bright railroad spike driven through her previously limp organ."
    na "Muscles pulsing back into place, fiber outgrowing itself and its limits to come to completion."
    na "Had it truly been dead a minute ago?"
    na "The pain has never been so raw!"
    na "Her ship speeds back toward the harbor, And then it is crashing, crashing crashing crashing...cascading."
    na "Ripping her throat apart."
    na "Someone on a distant shore is crying out “Sorry, Sorry, Sorry!” She has no redemptive power to offer them."
    na "What do their faults matter to her?"
    na "The ship, having left shrapnel of flesh in it's wake, settles into the harbor, curling up as if a child on a mother's lap, finally home."
    na "She sighs, it flaps her torn lining."
    na "And then, it is no longer her just ribcage in the dark, she has limits, borders."
    na "Something envelopes her, cuts her out of the void."
    na "Catherine did not wake in the comfort of someone's arms, maybe this eternity will be different."
    na "It will not be a lonely existence."
    show emily genuine at left
    na "Emily opens her eyes, Catherine is still weeping violently, her tears the first sensation the world offers Emily in her new form. Emily smiles weakly."

    e "I knew you could do it."
    na "Catherine sobs, it's guttural and ugly."
    na "Emily simply cozies into Catherine's torso."
    na "Home."
    na "This, Emily thinks, this shall be my whole world."
    hide emily
    hide catherine
    play music "emily_song.mp3"
    na "—-"

    scene stage
    show emily hurt at center
    na "The stage is lit with a single spotlight."
    na "It's waiting for her."
    na "She makes no hurry to reach it."
    na "Her graceful stride enters the circle as soon as she intends to."
    na "She settles in."
    na "She thought breathing might be different."
    na "Ah yes it is, it's much colder."
    na "She has yet to see her new appearance, the mirrors were shattered in the green room, but she can feel the horns."
    na "Has the audience been whispering?"
    na "She hadn't noticed."
    na "She doesn't care."
    na "But she is ready to start now."

    show emily business at center
    e "My love, this world was not meant for us. It’s better than it’s ever been, and it’s still not good enough."
    e "I hate this world. The only good thing I've found in it was you, and you are not even a part of it."
    e "You are a crevice I can enter into, wide enough to adjust to my shape, wide enough to hold my desires, my needs, my hunger, my pain."
    e "Slim enough to keep me warm, to extinguish my fears, to give me peace."
    e "My love, within your skin:"
    show emily genuine at center
    na "Emily extends her hand out into the audience."
    e "My world."
    e "My Paradise."
    e "My Catherine."
    na "Emily pulls her hand back to her, placing a kiss on the back of her ring finger, and then softly biting it."
    e "Forever."

    hide emily
    na "The lights do not turn off. Emily walks off stage, and into an eternity."
    na "END OF PLAY."
    na "ENDING 2: Paradise After All"
    $ persistent.done_emily = True
    if persistent.done_catherine:
        jump true_ending_transition
    return

label catherine_ending:
    play music "murder_song.mp3"
    scene backstage
    show catherine worried at right
    show emily hurt at left
    c "Oh god, I can’t, I can’t anymore Emily."

    show emily peeved at left
    e "You can’t what?"
    na "Catherine sobbing"

    show catherine shadow at right
    c "We’re horrible people, Emily. We’re murderers."

    show emily flippant at left
    e "..."

    show emily scolding at left
    e "Oh fuck this. I should have never dragged you into this shit-show."

    show catherine shadow at right
    c "..."

    show emily scolding at left
    e "I mean you agree right? Poor Catherine, dragged down to hell by Emily Theobald, who killed her friends, killed her ex, killed to get out...of...it. "
    show emily desperate at left
    na "Emily has started to cry"

    e "What because I wasn’t good enough for Mom?"
    e "Wasn’t good enough for Dad?"
    e "Wasn’t good enough for magic to work - but maybe that one’s not my fault - it might as well be though."
    e "Right?"
    e "Right Catherine?"

    show catherine worried at right
    c "Emily, I’m, I’m sorry. "

    show emily peeved at left
    e "For what?"
    e "For what Catherine?"
    e "For going along with a bat-shit crazy plan that I made?"
    e "Because my Dad told me some STUPID story when I was kid?"
    e "Because he killed himself for it?"
    e "Because now I know he died for nothing? ...How was any of that your fault?"

    show catherine frown at right
    c "I’m sorry for letting you do this."
    c "I’m sorry for, well, I’m sorry for helping."
    c "Maybe, maybe, god maybe I shouldn’t have left the mansion with you."

    show emily peeved at left
    e "What? "

    show catherine shadow at right
    c "I don’t think I’ve done very much to make your life better. I think, I think I’ve hurt you, by being here, really."

    show emily scolding at left
    e "Will you shut up! Can I have one moment where you talk to me like an actual person, where you’re not acting like a kicked puppy and making me feel guilty for - for - for making me feel l– "

    show catherine worried at right
    c "I’m not trying to make you feel guilty, Emily."

    show emily peeved at left
    e "You should be! You should be making me feel like shit. "

    show catherine content at right
    c "I care about you Emily, I love you."
    c "I don’t want to make you feel bad."
    c "You already feel bad enough, I don’t want to hurt you more."

    show emily peeved at left
    e "...Do you even know what love feels like ,Catherine? "

    show catherine shadow at right
    c "..."

    show emily desperate at left
    e "How...it doesn’t matter does it?"
    e "Whether you love me or not."
    e "You’re...are you?"
    e "Are you sticking around?"

    show catherine worried at right
    c "I love you Emily."
    c "Really, I, I know I shouldn’t, but I do."
    c "You’ve done a lot of things that have made me a lot happier than I’ve been for a long time."
    c "But just, I –"

    show emily peeved at left
    e "You what?"
    na "Emily looks disgusted."

    show catherine shadow at right
    c "I just think it’d be better if we parted ways."
    show emily desperate at left
    na "Emily’s eyes widen."

    show emily desperate at left
    e "..."
    e "OK, yeah, sure, just leave me here?"
    e "With a dead body in the fucking back?"

    show catherine worried at right
    c "Emily, please, I –"

    show emily scolding at left
    e "I get it."
    e "I’m worthless."
    e "I’m a fucking horrible piece of shit whose hurt you and now you’re going to let me rot in jail for the rest of my STUPID fucking life, god, you know what?"
    e "How about this?"
    e "How about I just stab myself right FUCKING now –"
    na "Emily has pulled out her knife."

    e "AND HOW ABOUT I SAVE BOTH OF US THE TROUBLE?"
    na "Emily’s scream echo from behind backstage."
    na "She lifts the knife up in front of her heart with both hands."
    show catherine startled at right
    na "Before she can use them, Catherine grabs them."

    show emily scolding at left
    e "God, you BITCH!"
    show emily desperate at left
    na "Emily’s sobbing uncontrollably."

    show catherine shadow at right
    c "I – I’m sorry."
    hide catherine
    na "Catherine runs out the back door before Emily can look up again. Emily’s face is in her hands."

    e "Please don’t go..."
    na "Emily falls to the floor and continues to sob, close to hyperventilating."
    na "She stays for a few minutes, until eventually she gets up, stumbling towards the stage."
    hide emily
    na "She looks out at the audience."

    scene stage
    show emily desperate at center
    play music "catherine_song.mp3"
    c "There’s a mansion, not far from here, where a woman used to live. She was strong and stoic, and loyal, so loyal."
    c "..."
    c "She was hurt by her parents."
    c "She was hurt by a vampire, a man who took her trust and betrayed her."
    c "And she, in turn, turned into one."
    c "She killed her parents after turning, filled with a blood lust she hadn’t known before."
    c "She had changed, she was cruel and monstrous, her stoicism turned to a desire to inflict pain."
    c "But part of her old self remained."
    c "She, she remembered the things that used to make her happy."
    c "The dances she used to have."
    c "The music she used to listen to."
    c "Even as she rotted away year after year, a part of her was still good."
    c "..."
    c "But she had been cursed."
    c "Deep down, her heart had been crushed, and the goodness that was left lived only on the surface."
    c "She was a bad, cruel person."
    c "And she found, one day, many years after she had given up hope of leaving, someone just as evil as herself."
    c "They thought they could go to paradise."

    c "Paradise. They thought one day they’d get to see paradise."
    na "Emily stands, shaking violently."

    show emily genuine at center
    c "But paradise is for good people."
    c "And she, she wasn’t good enough."
    c "God had cursed her, and God had cursed the woman who brought her out."
    c "And so she left her."
    show emily desperate at center
    na "Emily falls to the floor, sobbing. Her head in her hands."

    c "Left her to rot."

    hide emily
    na "END OF PLAY. "
    na "ENDING 1: Release"

    $ persistent.done_catherine = True
    if persistent.done_emily:
        jump true_ending_transition
    return

label true_ending_transition:
    scene black
    play sound "ritual_complete.mp3"
    pause 1.5
    jump true_ending

label true_ending:
    play music "intimate_song.mp3"
    scene backstage
    show emily desperate at left
    show catherine worried at right
    e "We need to go."

    na "Emily grabs Catherine’s wrist."

    e "Catherine, get up we need to run. "

    na "Catherine only continues to cry. "

    e "Catherine, you have to-"

    show catherine shadow at right
    na "Catherine drags Emily down. She pins Emily under her, fists around wrists, her tears flooding Emily’s face. "

    show emily peeved at left
    e "What the hell are you doing? "

    show catherine worried at right
    c "Please, please don’t go. "

    show emily desperate at left
    e "Catherine we can still-"

    show catherine shadow at right
    c "We can’t! We can’t undo any of it. "

    show emily scolding at left
    e "But we can’t stay here!"

    show catherine worried at right
    c "You...don’t want to stay with me."

    show emily peeved at left
    e "Are you crazy?! I’m- "

    na "Catherine suddenly lets go and retreats with a speed that stuns Emily into silence."
    show catherine shadow at right
    na "Catherine looks like a mutt left in the rain, hunched, still, cold."
    show emily desperate at left
    na "Emily scrambles up, hitting her back against the nearest wall."
    na "Still, Catherine does not move."
    na "After a seconnd, she does shift, but only to lay down on her back, and look towards the ceiling."

    na "The most painstaking beat passes. Emily looks at Catherine, and something in her moves. "

    e "Catherine, I’m sorry."
    e "I never should have dragged you into this."
    e "Rei, Ophelia, Aarya, Andrea, D- They’re all truly gone."

    na "Emily knows she was wrong, but the guilt would rend her asunder if she tried to admit it now."
    na "Still, she sits with it in silence, tears bubbling over her cheeks."
    na "She tries to be genuine with Catherine:"

    show emily genuine at left
    e "I thought, I thought there was a better world out there, someplace where we’d all be protected, someplace where we wouldn’t have to explain ourselves, somewhere I"
    e "...somewhere we belonged. "

    na "Emily can no longer speak through the tears. She does not see Catherine’s head turning to her. "

    show catherine frown at right
    c "I think this is all we have. "

    show emily desperate at left
    na "Emily sobs"

    show catherine content at right
    c "But maybe it’s not all wretched. I have you now. "

    na "Emily does not respond. Catherine rises and moves to put her face in front of Emily’s."

    c "Emily, the person I am now, for better or for worse, she was forged by you."
    c "I understand now- y-you are not kind."
    c "And you are not good."
    c "But neither am I!"
    c "I...I was a monster before you found me, and I will remain a monster beyond even the stars snuffing out."
    c "But now I have purpose again!"
    c "A-and my monstrosity only allows me to better serve that purpose!"
    c "That’s why you chose me, right?"
    c "You chose me because I could help you."

    show emily genuine at left
    e "..."

    show catherine bashful at right
    c "Emily...you have made me into who I am."
    c "I could not tear myself from you if I tried...and I- I don’t want to."
    c "You have me, if you want me, even in this."
    c "You do not deserve to lose anyone else."

    na "Catherine places her hand on Emily’s knee. "
    c "Emily, please, will you continue to be mine? "

    na "Emily sniffs, the tears are finally slowing. "

    show emily genuine at left
    e "I don’t want to leave you alone. "

    show catherine content at right
    c "You don’t have to. "

    show emily desperate at left
    e "No, Catherine."

    show catherine startled at right
    na "Emily Guides Catherine’s hand over her heart."
    na "Catherine looks down in confusion, and then shock blooms into her features. "

    c "Emily, no."
    c "You don’t want this."
    c "I don’t want this."

    show emily genuine at left
    e "It’s a lonely existence right? We can change that. "

    show catherine worried at right
    c "Emily...I’m not sure I can. "

    show emily genuine at left
    e "I’ll be here the whole time. "

    na "..."

    show catherine frown at right
    c "I can’t do it to you. "

    show emily desperate at left
    e "You will, because it’s what we both want isn’t it?"

    na "Catherine looks away, ashamed. Emily brings her back by kissing the palm of her hand."

    e "Even if the world doesn’t get better, and there’s nowhere to go, I’ve tied you to me."
    e "You’re my responsibility now."
    e "So please, tie me to you."
    e "I want you to turn me."

    e "Their eyes meet, and Catherine knows the battle is lost."
    e "Emily slides down the wall, now lying under Catherine again, the palm once again pressed to her heart."
    play audio "ribs_opening.mp3"
    e "Wincing, Catherine plunges her hand into Emily’s chest."
    e "It’s warm, slick, encapsulating."
    e "Catherine’s mind slides before Emily’s cry of pain forces her into the moment."
    e "She freezes."
    hide emily
    hide catherine
    scene Heart_in_dark
    e "Your-you’re doing good Catherine. "
    c "Emily-"
    e "Shit! Will you - please - "
    c "Right- "
    na "Blood is starting to bubble out of Emily’s mouth."
    play audio "heartbeat_sound.mp3"
    na "Catherine panics and rips out the heart with too much force."
    na "Emily screams."

    e "Good...almost...there..."

    na "Catherine can’t take her eyes off of Emily, her hand shakes as she raises the still pumping organ to her mouth."

    e "I’m...ready..."

    na "Catherine tries to bite down...then she finally does. Emily screams. "

    e "Heh...one last..."
    scene Heart_in_dark_2
    na "She can’t finish."
    na "Catherine shudders, and huffing, shoves the heart into Emily’s mouth."
    na "She doesn’t want to watch it travel down her throat, but she can’t look away, it’s gratuitous the way the skin bulges and wraps around the traveling clod."
    na "Finally, it regains it’s place in Emily’s chest cavity."
    na "Catherine waits, her breath held."
    na "She waits a second too long. "
    
    scene black
    c "Emily, Emily oh god wake up. Emily...."
    na "Emily does not stir. "
    na "Catherine screams."
    na "She screams and screams and screams until her throat is raw, and she pushes through to keep expelling the invasive explosion that has filled her body and refuses to leave. "
    na "In a moment where she is forced to breathe, she hears voices, worried and muffled, a world away. "
    na "The audience. "
    na "Delirious, Catherine stands, and walks onto the stage."

    scene stage
    show catherine stoic at center
    na "The lights are bright."
    na "She hardly registers them."
    na "She opens her mouth, voice raspy, and begins to speak."

    play music "true_ending.mp3"

    c "There was once a girl."
    c "A girl who simply wanted to live."
    c "And in the end, she was denied that, in the cruelest way possible."
    c "You see, this girl grew up in a home colder than the harsh winters she was subjected to."
    c "No snow or frost was worse than the way her father looked at her, or the way her mother looked away from her, "
    c "or the ache that shot pain into her limbs for those many days and nights she went hungry."
    c "She would remain hungry for a very long time."
    c "One day, a man came into her life."
    c "She had never been exposed to warmth before, so the extreme frostbite this man offered, might as well have been heat."
    c "She was drawn to him, entranced and enchanted, and when he...When he turned her."
    c "She hated herself more than she hated him."
    c "He had wormed his way into her system, gave her a glimpse of a life she wanted, hiding the price of it behind him."
    c "He told her what he found inside her wasn’t rotten, that she was not a monster, and the promise of absolvance was so sweet, she could not resist believing."
    c "But she was a monster."
    c "Now in flesh as in soul, for with his bite, he took from her the life she wanted."
    c "And raised her to last eternally in isolation."
    c "In a winter darker than all she had known before."
    c "She stayed there, in the home that held all her tormentors, and all her memories. She waited not for a disruption to come along, but rather sat in endlessness. "
    c "But then... finally, the sun."
    c "A girl entered."
    c "Beautiful, and vicious, and... hers."
    c "The girl was found, she was seen, and there was a place that existed beyond winter."
    c "There was a place that existed beyond herself."
    c "And though she was a monster, she was content to be one, because the sun didn’t seem to care. "
    c "But then she...then she.."
    show catherine shadow at center
    na "Catherine chokes up."
    na "Her gaze sharpens from reflective to seeing those in front of her for the first time."
    na "The audience."
    na "She feels a wave of nausea roll over her at the sight of them."
    c "Why? "
    na "Nobody moves."
    na "Nobody speaks."
    na "They do not know they are meant to answer, but Catherine doesn’t care, they are still cowards."

    show catherine frown at center
    c "Why do you hate us? Why do you push us to be monsters when we are so human? "
    na "The audience now looks at each other, confused."
    na "Is she speaking to them?"
    na "What could they have done wrong?"
    na "Catherine scoffs."
    na "They seem to think them sitting here is an isolated moment, as if they haven’t built the world that broke Emily’s heart."
    na "The one that forced them to bury the world that was theirs."

    show catherine shadow at center
    c "Well all of you can go to hell."
    c "Because I may have no place in this world, but there is a girl who loves me."
    c "Loved me."
    c "Loves me."
    show catherine content at center
    na "She looks at them with no more questions, no more room for their interjection. "

    c "And I would take your rejection a thousand times if it meant I could keep her love. "
    na "A skitter to her right. "
    na "Catherine looks. "
    na "Emily. "
    show catherine content at left, flip
    show emily genuine at right, flip
    na "Freshly sprouted horns, her human blood dripping from her mouth, her heart returned, her eyes bright, and her smile sweet. "
    na "Emily. "
    na "She walks to Catherine, and lifts her hand to Catherine’s face."
    na "She is no longer warm, and Catherine feels a pang in her chest, but still, Emily is the sun."
    na "Always the sun."
    na "Catherine cannot help but orbit, she is willing to be burned."
    show catherine bashful at center
    na "Emily offers her lips to Catherine, and tenderly, Catherine takes them."
    na "They wrap around each other, their revived hearts as close as they can be."
    na "They will never be lost again."
    na "fin"
    hide emily
    hide catherine

    return