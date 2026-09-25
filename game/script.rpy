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

label the_meeting:
    define nar = Character("Narrator")
    define vamp = Character("Vampire")
    define fa = Character("Father")
    define mo = Character("Mother")
    define fc = Character("Catherine")
    define al = Character("All")
    play music "play_song.mp3"
    scene opening_1
    nar "The greatest paradox known to man is our own lives, and their subsequent deaths."
    nar "Indomitable human spirits, wiped out by simple things." 
    nar "A car crash."
    nar "Illness."
    nar "Our vices." 
    nar "Our salvations."
    window show
    scene opening_2 with Dissolve(.2)
    
    nar "The bite of a night creature."
    nar "This was the unfortunate end of Catherine Lyon."
    window auto
    scene opening_3 with Dissolve(.2)
    fc "No, No!"

    vamp "Hush now, it will be over soon."

    fc "Stay back! Please, stay back!"
    
    vamp "I cannot, your beauty enthralls me, and I must have you to join me in the eternal dark."
    
    fc "Please{w=.2} DON’T -"

    
    nar "The scream died in her throat as...well some teeth were in it."

    scene opening_4
    fa "You, you demon! What have you done to my daughter!"

    
    vamp "The question is, what will your daughter, do to you!?"

    
    re "Sick em’!"

    
    op "Just keep going!"

    
    vamp "Sicketh them!"

    
    re "Oh shit! He actually says {i}that{/i}?!"

    
    op "Keep. Going!!"

    
    fc "I can’t...{w=.3}contain it...{w=.3}all this hunger."

    
    mo "My darling, my sweet girl, this isn’t you!"

    
    vamp "She is a creature of the night now, your words will not reach her."

    
    mo "You bastard!"

    
    vamp "You bitch!"

    
    fa "Don’t you dare talk to my wife that way!"

     
    fc "Forgive me Mother."

    
    mo "{cps=60}No!{/cps}{w=.2}{cps=*.2} NOOOOOOOOOOO!{/cps}"

    scene opening_5
    nar "Their flesh was supple, and their blood was sweat."

    
    re "Typo! Typo alert!"

    
    an "Rei."

    
    re "Shutting up, shutting up."

     
    nar "Their flesh was supple, and their blood was sweet."

    
    vamp "Yes, you have partaken!"
    vamp "Rise my creature of darkness!"
    vamp "Join me as my bride!"

    scene opening_6
    nar "Catherine turns to face the vampire with bloodlust in her eyes."
    fc "Grrr"

    
    vamp "Oh shit."

    
    nar "He had no blood to feast on, but with a meaty rip, his body lost its head. "
    nar "The vampire girl wept, she had already taken her vengeance, but it offered no relief for her guilt."
    nar "We do not know how this story ends. Many say she fled into the night, trying to outrun her own flesh."
    nar  "Her mansion - the same one over the hill - was left to rot, the last witness of the horrors that took place inside. "

    nar "Still, a through line of unease connects all of us: woven around our hearts and squeezing with each rumor."
    nar "A question scurries across the line, leaving goosebumps in its wake. "
    scene black
    nar "Is that house... truly empty?"


    nar "END OF PLAY."


    scene stage
    with Dissolve(1.0)
    play music "drama_song.mp3" 
    na "   "

    show mac tired at left
    mac "I don’t know Andrea. It seems a bit flowery."

    show ophelia dissapointed at right, flip
    op "Mac! She worked really hard on this."

    hide mac
    show aarya sigh at left, flip
    aa "You don’t even have to perform it. What do you care if it’s flowery?"

    op "The flowery-ness isn’t a {i}problem{/i}! It’s a style choice."

    hide aarya
    show mac tired at left
    mac "{i}But I’m teching it{/i}, my name's gonna be in the program. I’ll be associated. "

    show ophelia dissapointed at right, flip
    op "Then you’ll be {shader=wave:u__amplitude = 5.0}lucky {/shader}. Andrea poured her heart into this-"

    hide mac
    show andrea pride at left, flip
    an "I poured a lot of caffeine into this."

    show ophelia passionate at right, flip
    na "Ophelia throws her head back and sighs."

    op "I see even you think I’m overacting."

    show andrea snark at left, flip
    an "Nah, I’m just a lot less sensitive than you are. "

    op "For the record I really loved it. "

    an "{i}Snrk.{/i}"

    op "And no, I’m NOT just saying that {i}{b}ASH {/b}{/i}. "

    show ash happy at center

    ash "I wasn’t going to say anything. "
    hide ash
    show mac tired at center
    mac "I was. "

    hide mac
    op "No you were not! "

    show andrea serious at left, flip
    an "I’ll get you the revised script at Monday’s rehearsal."
    an "EVERYBODY HEAR THAT?!"
    an "NEXT REHEARSAL IS MONDAY!"

    hide ophelia
    show rei alright at right, flip
    re "Yeah, yeah. Drill it into our heads. "

    show andrea ticked at left, flip
    an "I am drilling it because some of you were late today. "

    show rei oops at right, flip
    re "I told you that was a one time thing! "

    an "No, you told me you missing a meeting was a one time thing. The lateness went by unremarked. "

    show rei alright at right, flip
    re "C’mon... you know you love me."

    show andrea okay at left, flip
    an "Completely irrelevant. "

    hide rei
    show aarya sigh at right
    aa "If you’re done disciplining Rei, may us innocents be dismissed?"

    show andrea pride at left, flip
    an "When is our next rehearsal?"


    al "Monday!"


    an "Then you all can go. "

    hide andrea
    hide aarya
    show ophelia excited at right, flip
    narrator "Ophelia runs over to Emily, taking her hand in between hers. "

    show emily peeved at left
    op "Is it time? "


    e "Not so loud! "


    op "Then let’s get out of here! "

    na "Ophelia pulls Emily from her seat, and they rush out of the room after Rei. Aarya trails behind them. "

    hide emily
    hide ophelia
    jump it_knows_you_by_name

label it_knows_you_by_name:
    play music "occult_song.mp3"
    scene stage_dramaroom

    na "Emily, Aarya, Ophelia, and Rei rush to get backstage. Aarya struggles with the keys."
    
    show ophelia excited at right, flip
    op "Hurry!"

    show aarya sigh at left, flip
    aa "I am!"

    play audio "door_creaking.mp3"
    na "The door pops open, and the girls rush inside, giggling. Wedged behind some curtains, they begin to sit in a circle, cross legged."
    play audio "shuffling.mp3"
    na "Ophelia retrieves a fake plastic candle out of her bag, and sets it down in the middle of them."

    hide ophelia
    show rei hyped at right, flip
    re "When are we gonna start using real candles?"

    show ophelia wondering at center, flip
    op "When we are ready for this ancient college to burn down."

    show rei alright at right, flip
    re "I {i}do{/i} kind of want to see this place go up in flames. "

    show aarya incredulous at left, flip
    aa "Start attending your classes."

    show rei hyped at right, flip
    re "I prefer the fire."

    hide aarya
    show emily curious at left
    e "Shhhhhhh..."

    na "All the girls silence, the rowdiness from earlier smothered by an intense focus. They all breathe in together, and after their exhale, Emily starts: "

    hide ophelia
    hide rei
    show emily curious at center
    e "We are gathered here today, in the dying heart of our school, to convene in the strange and mysterious. "
    e "The world is full of non-believers, so small spaces must be made, to host those that understand. "
    e "The Occult welcomes you, and it knows you by name."

    show ophelia isw at right, flip
    na "Ophelia suppresses a shiver."

    show rei hyped at left
    re "So what is it today Em?"
    re "Ghost hunting?"
    re "Tarot Readings?"

    show emily mischievous at center, flip
    e "A little breaking and entering."

    hide rei
    show aarya incredulous at left, flip
    aa "I will not be participating in crime."

    show emily flippant at center
    e "Then a little house tour."

    show ophelia comforting at right, flip
    op "Don’t worry Aarya. I’ll be there."

    show aarya sigh at left, flip
    aa "Ophelia I don’t think you can exactly stop the law."

    show ophelia passionate at right, flip
    op "No, but I can take the blame if anything goes south."

    hide aarya
    hide ophelia
    show rei alright at left
    show emily mischievous at right, flip
    re "What house are we going to?"

    e "Take a guess."

    show rei hyped at left
    na "Rei smiles wide."

    re "No. Noooo way!"

    hide rei
    show aarya incredulous at left, flip
    aa "Care to share?"

    show emily genuine at right, flip
    e "We’re going to Catherine Lyon’s Mansion."

    hide aarya
    show rei hyped at left
    re "NO WAY!"

    hide rei
    show aarya worried at left, flip
    aa "Immediate veto."

    show emily peeved at center, flip
    e "Come oooon Aarya!"
    e "We’ve got to see if the legend is true!"
    e "It’s integral research for the play."

    show aarya sure at left, flip
    aa "I am not going to prison for play research."

    show emily scolding at center
    e "Fine! When we all die horrible deaths due to rickety structuring it will be on your conscience!"

    show aarya sigh at left, flip
    aa "You’re so melodramatic."

    show emily peeved at right
    e "And about to be dead too!"

    show ophelia comforting at center, flip
    na "Ophelia takes Aarya’s hand."

    op "Unless...we have our Aarya to tell us when crossing a huge hole in the floor via a beam is not a good idea?"

    show aarya sure at left
    aa "I’m telling you it’s not a good idea now."

    show emily flippant at right, flip
    e "Well, whether or not you’re coming, it’s starting to get dark."

    hide aarya
    show rei hyped at left
    re "Finally! Let’s get out of here."

    hide emily
    hide rei
    na "Rei and Emily snap up and start walking away. Aarya turns to Ophelia, who is snatching up the plastic candle and returning it to her backpack."
    show ophelia wondering at right, flip
    show aarya sure at left, flip
    aa "Are you really gonna go?"

    na "Ophelia nods."

    op "But I’d prefer to go with you."

    show aarya sigh at left, flip
    aa "Fine."
    aa "You’d really cross a beam unless I told you not to?"

    show ophelia comforting at right, flip
    op "Yeah, but Rei would cross it even if you told him not to, so I’m mainly asking you to come in case I need help saving his life."

    show aarya sigh at left, flip
    aa "Emily’s not enough help?"

    show ophelia dissapointed at right, flip
    op "We could {i} not {/i} get Emily to carry a body."

    show aarya woah at center
    show rei hyped at left
    na "Rei turns their head back, with his body already out the door."

    re "HURRY UP SLOW POKES!"

    hide rei
    hide aarya
    hide ophelia
    na "The girls leave, the room dark without them."

    jump mansion

label mansion:
    scene vineyard
    na "The four girls stand in front of an old, abandoned mansion as twilight wanes. Left of it is a vineyard, clearly overgrown from years of neglect."
    show ophelia excited at left, flip
    op "Woah..."

    show rei hyped at right
    re "WOAH!!!"

    hide rei with MoveTransition(.3, leave=offscreenright, enter_time_warp=_warper.easein)
    play audio "run_away.mp3"
    na "Rei runs forward."

    hide ophelia
    show aarya sure at left, flip
    aa "REI!"

    hide aarya with MoveTransition(.7, leave=offscreenright, enter_time_warp=_warper.easein)
    play audio "run_away.mp3"
    na "Aarya chases after Rei."

    show ophelia wondering at right, flip
    op "Should we go after them?"

    show emily flippant at left
    e "{i} Ehhh {/i}"

    na "Aarya and Rei disappear into the vineyard."

    e "You probably should. I don’t think Aarya can deal with Rei by herself."

    show ophelia dissapointed at right, flip
    op "Are you not coming?"

    show emily mischievous at left
    e "I’ll just go ahead and make sure it’s safe! Meet me at the front entrance once you find them."

    show ophelia excited at right, flip
    op "Got it!"

    hide ophelia
    play audio "walk_grass.mp3"
    na "Ophelia runs off to the vineyard."

    scene mansion
    na "Emily walks towards the mansion. The wooden walls are extremely weathered, with vines growing along the panels and into the windows."

    na "Emily grabs the door handle."

    show emily peeved at center, flip
    e "Wait, shit. Why is it locked?"

    play audio "body_fall.mp3"
    na "Emily pauses, looks around, and walks towards a window. She pushes it all the way open, and climbs through, falling loudly flat on the floor."

    show emily gross at center, flip
    e "Ugh, stupid fucking door."

    play music "catherine_lone_piano.mp3" fadein 0.5
    hide emily
    scene potraits
    na "Emily gets up, and walks through a hallway. The interior is very well worn, with small paintings, cabinets and vases covered in a thick layer of dust lining the walls. "
    na "At the end is a staircase, with a weathered door at the top. The soft sound of piano can be heard behind it."

    show emily curious at left
    na "Emily opens the door, and sees someone sitting away from her, playing quietly on a well tuned piano."

    play audio "door_creaking.mp3"
    na "The door creaks, and they turn suddenly."
    play music "tecc.mp3"
    show catherine startled at right
    vo "Ah!"

    na "In front of Emily is a woman, of a strange, unnatural complexion and form. Her skin is a light grey, eyes purple, and ears unusually large. "
    na "She looks startled."

    show emily curious at left
    e "Um –"

    hide catherine
    na "The woman points her eyes to the floor, quickly gets up and runs to a door to her right."

    show emily peeved at left
    e "Hey!"

    play audio "door_slam.mp3"
    na "The woman slams the door behind her."
    na "Emily freezes, standing still and attentive while staring at the door. After half a minute, she cautiously walks over and knocks lightly on the door."

    show emily flippant at left
    e "Helloooooo. Can I come in?"

    na "Emily waits for a moment. A voice from the other side responds."

    vo "Um, uh, I, sorry, you shouldn’t."

    show emily curious at left
    e "Why not?"

    vo "I – Well, oh, um, well –"

    e "Are you going to hurt me?"

    vo "No!"
    vo "Maybe "
    vo "I could "
    vo" theoretically"

    show emily genuine at left
    e "Ok, well if you say you’re not going to hurt me, I’m not going to hurt you, alright?"

    vo "Oh, well, um, I guess, if you’d like to."

    e "Now, I’m going to open the door, ok?"

    vo "Ah, alright."

    show catherine bashful at right
    play audio "door_creaking.mp3"
    na "Emily slowly pushes the door forward, and the woman appears again on the other side."

    e "..."

    show catherine worried at right
    na "The woman looks tense."

    show emily genuine at left
    e "Hi, I'm Emily. What's your name?"

    vo "Oh, um, well,"

    show catherine bashful at right
    c "My name is Catherine."

    show emily curious at left
    e "Catherine Lyon?"

    show catherine worried at right
    c "Oh, uh,"

    na "Catherine looks nervous"

    c "Do you know me?"

    show emily flippant at left
    e "Well there have been stories floating around. Did you not know about them?"

    show catherine bashful at right
    c "Oh, no, not really."

    show emily curious at left
    e "..."

    na "The two stare awkwardly."

    e "So, uh, should we sit down?"

    show catherine content at right
    c "Yes, yes, that would be ideal."

    play audio "walking_wood.mp3"
    na "The two walk back into the piano room, and sit down across from each other. Emily stares at Catherine intensely."

    show emily genuine at left
    e "So, Catherine."

    show catherine bashful at right
    na "Catherine perks up."

    e "You’re very good at piano. I could hear you from the hallway playing."

    show catherine content at right
    c "Oh, yes, I've been playing for a while now."

    show emily satisfied at left
    e "I could tell. Do you play often?"

    show catherine bashful at right
    c "Only when I'm bored, really."

    show emily curious at left
    na "Emily pauses, and stares at Catherine."

    e "It's probably been a while since you’ve gotten a chance to talk with anyone."

    show catherine frown at right
    c "Yes, a while."

    show emily genuine at left
    e "Could I come over again, maybe tomorrow? You seem a bit tense right now."

    show catherine worried at right
    c "Um, well, I don't know –"

    show emily satisfied at left
    e "To give you time to process. Maybe we could have dinner here?"

    na "Emily looks around."

    e "This seems like a nice place to eat."

    show catherine bashful at right
    c "Oh, well, this isn't the dining room, I can show you that now if you’d –"

    show emily flippant at left
    e "Show me tomorrow, ok? I need to get going, I’ll be back around the same time tomorrow."

    show catherine worried at right
    c "Wait, I don't have any food here for you to eat, we can’t do dinner."

    show emily satisfied at left
    e "Well, what if I bring food?"

    show catherine content at right
    c "Perhaps that would work. Wait, let me fetch you some money."

    hide catherine
    play audio "walking_wood.mp3"
    na "Catherine runs into another room, and comes back a minute later with her hand clenched. She drops a few coins into Emily's hand. "
    show emily curious at left
    na "Emily stares at the change, puzzled, then amused."

    show emily satisfied at left
    e "...Thank you, Catherine. I’ll see what I can get with this."

    hide emily
    scene vineyard
    show ophelia wondering at right, flip
    show aarya sigh at left, flip
    show rei hyped at center
    play audio "door_open.mp3"
    play audio "walking_wood.mp3"
    na "Emily walks out the door she came in, down the hallway and out the front door."
    na "Aarya and Ophelia are standing outside, clearly out of breath, while Rei stands triumphantly."

    show ophelia excited at right, flip
    op "Em! We found Rei."

    show aarya sigh at left, flip
    aa "Somehow."

    show rei hyped at center
    re "Hey!"
    show rei hyped at center
    re "I was just having fun!"
    show rei hyped at center
    re "Neither of you {i}had{/i} to chase me."

    show aarya sure at left, flip
    aa "Well we did, and now we're all tired and we haven't even gotten into the mansion yet. "
    aa "If you do something stupid in there I'm just going to let you die at this point, I don't have enough in me to save you again."

    hide ophelia
    show emily flippant at right, flip
    e "Sounds like you three had fun."

    hide aarya 
    show ophelia dissapointed at left
    op "It was a bit much."

    show emily satisfied at right, flip
    e "Well, either way, I think we should probably head back."

    show rei oops at center
    re "What!?"

    hide ophelia
    show aarya sigh at left, flip
    aa "Thank god."

    hide aarya
    show ophelia wondering at left
    op "Really?"

    show emily flippant at right, flip
    e "I checked inside and the whole thing is basically falling apart. I don't trust the stairs to hold any of us."

    show rei alright at center
    re "Come on, Em, it can’t be that bad!"

    show ophelia comforting at left
    op "I trust Emily on this one Rei. I'm really tired too."

    hide ophelia
    show aarya sure at left, flip
    aa "Agreed, let's just call it. Maybe if you don't make us run around for 15 minutes straight we'll let you go in next time!"

    show rei cmon man at center
    re "UGH! You guys are LAME!"

    hide rei
    hide aarya
    hide ophelia
    hide emily
    play audio "walk_grass.mp3"
    na "Emily walks away from the mansion, and the rest of the girls follow."

    play music "menu_song.mp3"
    scene black
    menu:
        "Choose a Character."

        "Catherine":
            $ character = 0
            jump catherine_flashback_1

        "Emily":
            $ character = 1
            jump emily_flashback_1

label an_awkward_dinner:
    play music "gecmc.mp3"
    scene vineyard
    show emily curious at left
    na "Emily walks back, a day later, to the mansion. "
    na "She carries 2 bags of groceries, each a little too heavy. She places the bags down and knocks on the front door."

    e "..."

    play audio "door_creaking.mp3"
    na "Emily grabs the door handle and opens the door. She looks around, and then brings the groceries into the mansion, through the hallway, up the stairs, and into the piano room."

    show emily flippant at left
    e "I’m here!"

    na "Emily’s voice echoes through the mansion."

    show catherine startled at right
    c "Coming!"

    na "Catherine opens one of the doors, and enters the piano room suddenly."

    scene potraits
    show catherine worried at right
    c "I’m so sorry, I was preparing, I didn’t expect you to come so soon. Let me take those off of you."

    show emily genuine at left
    e "No problem, hopefully this is enough for both of us."

    hide catherine
    play audio "shuffling.mp3"
    na "Catherine takes the bags of groceries out of Emily’s hands. She runs off with them out the same door she came in."

    na "Emily waits, and looks around the piano room. "
    na "The piano looks old, but sounded surprisingly nice despite it. There’s a few chairs with the same quality, with a clear amount of care put into their upkeep. "
    na "There’s a few paintings on the walls, with an empty space between them where a large painting would reasonably fit. "
    show catherine bashful at right
    na "After a long while, Catherine comes back into the room."

    show catherine worried at right
    c "I’m sorry if this meal isn’t what you’re used to. I tried to make do with what you brought."

    show emily satisfied at left
    e "I’m sure it’ll be fine."

    na "Catherine leads Emily over to the dining hall."
    na "The table is neatly organized and furnished with ornate china and silverware for two."
    na "The light streams in from the windows to the side and the head of the table."
    na "Catherine walks to the foot of the table and elegantly takes her seat as Emily walks over to the head and promptly sits across from her. "
    na "Catherine stands up and pours a glass of wine for herself and walks over to Emily’s end of the table."

    show catherine content at right
    c "Is Pinot Noir acceptable? I’d offer you more, but it’s all we have left in the cellar."

    show emily curious at left
    na "Emily looks at the bottle, a bit mesmerized."

    e "How old is it?"

    show catherine bashful at right
    c "It’s from 1904. It was a good year, it’s surely still drinkable."

    show emily satisfied at left
    e "Sure then, I’ll have a bit."

    show catherine content at right
    play audio "wine_pour.mp3"
    na "Catherine smiles at Emily, and pours Emily a half glass."
    na "Catherine sits down, and Emily looks over at the food in front of her. There’s a salad, prepared using the lettuce and assorted vegetables she brought, with an odd looking dressing."
    na "Next to it is something approximating a stew or a soup, with various chunks of potato sticking out and an odd texture. "
    na "Emily looks over at Catherine’s side of the table, to see her smiling with a glass of wine in her hands and the same salad and soup in front of her."

    show emily curious at left
    e "Can you eat normal food?"

    show catherine content at right
    c "Yes, though it doesn’t do much to satisfy me. Wine helps a little, at least, but I don’t have much left."

    show emily mischievous at left
    na "Emily smiles."

    e "Can you get drunk at least?"

    show catherine stoic at right
    c "I wouldn’t get to that point. I control myself."

    show emily satisfied at left
    e "That’s nice to hear."

    na "Emily takes a sip of her wine."
    na "The two glance at their meal, and begin to eat."
    na "The food is bland, but edible."
    na "Salt would’ve been nice."

    show emily genuine at left
    e "So, Catherine."

    show catherine bashful at right
    c "Yes?"

    show emily curious at left
    e "You’re a vampire, right?"

    show catherine frown at right
    na "Catherine lowers her head."

    c "I suppose I still am."

    show emily curious at left
    e "You’re immortal, right?"

    show catherine stoic at right
    na "Catherine pauses."

    c "Well I haven’t died yet, and I don’t seem to age."

    show emily satisfied at left
    e "Mhm, immortality does that."

    play audio "clink.mp3"
    na "Emily clinks her spoon on the soup bowl."

    show catherine content at right
    c "How about you? How old are you?"

    show emily flippant at left
    e "I’m 20. I go to Lombardy College here, if it’s old enough for you to recognize."

    show catherine content at right
    c "Lombardy? Last I knew of it, it was an all boys college."

    show emily satisfied at left
    e "Well, those don’t really exist a lot anymore. Everything’s co-ed now."

    show catherine bashful at right
    c "Co-ed?"

    show emily genuine at left
    e "Co-education. Like, women and men together."

    show catherine content at right
    c "Ah, I see."

    na "Emily and Catherine sit for a while as Emily eats."

    e "..."

    c "..."

    c "You must be quite intelligent to get to go to college."

    show emily flippant at left
    na "Emily puts her spoon down."

    e "Not really."

    show catherine bashful at right
    c "Is that so?"

    show emily satisfied at left
    e "Yeah, you don’t gotta be that smart to go to college. Most of my friends from my home town are also going to college."

    show catherine content at right
    c "Well. That’s nice."

    e "..."

    show catherine frown at right
    c "I remember wanting to go to college when I was younger."

    show emily curious at left
    e "Why didn’t you?"

    show catherine shadow at right
    na "Catherine looks away, a little depressed."

    c "... Well, um, my father."

    show emily genuine at left
    e "Ah."

    c "..."

    e "...Maybe I could take you to Lombardy one day."

    show catherine bashful at right
    na "Catherine looks up again."

    c "Would that be allowed?"

    show emily mischievous at left
    e "Eh, I don’t know. I don’t think they really have a policy on vampires."

    show emily satisfied at left
    na "Emily smiles to Catherine."

    e "I’ll just get you in somehow."
    e "It’ll be fun!"
    e "Maybe I could bring you to see some of my friends, assuming that –"

    na "Emily gestures towards Catherine."

    show emily flippant at left
    e "We can find a way to hide your ears."

    show catherine awkward smile at right
    c "I – I suppose I can consider it."

    show emily genuine at left
    na "Emily gets out of her chair and walks over to Catherine, and leans on the table over her."

    e "Thanks for making the food. I liked it."

    show catherine bashful at right
    c "Oh please, I didn’t know what I was doing."

    show emily satisfied at left
    e "Well, anyways, would it be ok if I kept coming over for dinner?"

    show catherine startled at right
    na "Catherine looks a bit startled, but calms after a second."

    show catherine content at right
    c "Well, it was nice to have a guest in the house for once."

    show emily satisfied at left
    e "Good! I’ll see you tomorrow then."
    play audio "walking_wood.mp3"
    if character == 0:
        hide emily
        show catherine frown at right
        na "Emily straightens herself, and then walks out of the door, waving to Catherine as she leaves. As Emily closes the door, Catherine looks forward with a pained grin."
    else:
        hide catherine
        show emily flippant at left
        na "Emily straightens herself, and then walks out of the door, waving to Catherine as she leaves. As Emily closes the door, the smile on her face loosens."

    hide emily
    hide catherine
    if character == 0:
        jump catherine_flashback_2
    else:
        jump emily_flashback_2

label the_orchestra:
    stop music fadeout 1.0
    scene potraits
    show emily curious at left
    show catherine bashful at right
    play sound "gramophone.mp3"
    e "This is insane! If I poke it, will it collapse?"

    show catherine content at right
    c "It’s possible."

    show emily flippant at left
    e "You really listen to music like {i}this{/i}?"

    show catherine bashful at right
    c "I certainly try."
    c "I’ve kept it in good shape all these years but sometimes age just...makes things fall apart."
    c "Hopefully it will still work for you today."

    show emily mischievous at left
    e "What? Wanna impress me?"

    show catherine gay blush at right
    na "Catherine’s ears twinge a color. She mutters."

    c "Would that be so bad?"

    show emily curious at left
    e "What?"

    show catherine startled at right
    c "Nothing!"

    show emily mischievous at left
    e "Just kidding, I totally heard you."

    show catherine blush at right
    c "Please do not mortify me any further. I may be immortal but I should like to spare myself a heart attack."

    show catherine frown at right
    stop sound
    play audio "static.mp3"
    na "The phonogram starts to emit an awful hissing sound."

    c "Oh please...not now..."

    na "The hissing soon turns into a violent screech."

    show catherine worried at right
    play music "gecmc.mp3"
    c "Alright, alright, I’m turning you off. "
    c "Emily, forgive me, but I think it might have gone to its gra–"

    show emily curious at left
    e "Why do you do that?"

    show catherine bashful at right
    c "Hm?"

    e "Talk to things like they’re people. They can’t hear you."

    show catherine frown at right
    c "There’s not many people to talk to."

    show emily curious at left
    e "What?"
    e "No movie-theater employees, no mall cops - actually nah you’re too straight-laced for that."
    e "But really, you’ve got no one to talk to?"

    show catherine shadow at right
    c "I don’t... go out."

    e "..."

    c "..."

    show emily peeved at left
    e "Wait, that's the end of that sentence?"

    show catherine bashful at right
    c "Yes?"

    show emily flippant at left
    e "I... I don’t even know how to respond."

    show catherine worried at right
    c "It’s not –"

    show emily satisfied at left
    e "Wait, yes I do! Yes I {i}do{/i}!"

    na "Emily grabs Catherine’s hand and begins pulling her down the hallway."

    e "I can’t believe I get to go after all! What are the chances?"

    show catherine startled at right
    c "Emily– where are we going!"

    show emily mischievous at left
    e "Out."

    show catherine worried at right
    c "Out?!"
    
    play audio "door_open.mp3"
    play audio "walking_wood.mp3"
    scene mansion
    na "Emily pushes the huge doors of the Mansion open."

    show emily satisfied at left
    e "There’s an orchestra concert in the auditorium tonight, if we sneak you up into the rafters we’ll be able to – Catherine?"

    show catherine worried at right
    na "Emily stands outside the door, her hand still outstretched, while Catherine is clinging violently to the door frame."

    show emily curious at left
    e "Why aren’t you holding my hand anymore?"

    c "I– I Emily, I cannot. Truly I cannot."

    show emily peeved at left
    e "Catherine."
    e "You gotta."
    e "You’re rotting inside your house!"

    show catherine frown at right
    c "My corpse is quite literally perfectly preserved."

    show emily scolding at left
    e "Your perfectly preserved corpse is rotting inside your house!"

    show catherine worried at right
    c "Emily..."

    show emily peeved at left
    e "Catherine..."

    na "Catherine quivers."

    show emily flippant at left
    e "Fine, If you want to stay here you can, but I don’t wanna miss it! I’ll see you later Cathy!"

    show catherine worried at right
    c "No Emily, it’s dark, I’m not sure with the lay of the land you could–"

    show emily peeved at left
    e "I know the “lay of the land”! I’ve been here practically every evening."

    show catherine bashful at right
    c "But not every {i}night{/i}."

    show emily satisfied at left
    e "I’m sure I’ll be safe Catherine, trust me, what is there to be worried about?"

    show catherine content at right
    c "I... I’ll accompany you."

    show emily genuine at left
    e "Ah don’t worry, I’ve got this one."
    e "And I understand, y’know, it’s been a long while since you left...I don’t want you to push yourself."
    e "I’ll see you tomorrow!"

    show catherine worried at right
    na "Suddenly Emily’s arm is held fast in Catherine’s grip."

    c "Please don’t go alone."

    show emily satisfied at left
    e "If you insist."

    show catherine worried at right
    c "How are we going to get in, with my appearance and... with a distinct lack of money?"

    show emily mischievous at left
    e "Money? Who says I was paying?"

    show catherine startled at right
    c "What do you mean by–"

    hide emily
    hide catherine
    scene backstage
    na "Emily and Catherine sneak backstage of the concert. "
    na "Emily, used to plays and stages, confidently climbs onto the rafters. "
    na "Once she’s settled on top, she turns around and offers her hand to Catherine, who is nervously scanning the room hoping not to be caught."

    show catherine worried at right
    c "I– I don’t think we should be doing this."

    show emily flippant at left
    e "Oh come on, I do this all the time. Look, I am a college student and you’ve got 1 dollar from the 1900s, besides –"

    na "Emily looks at the crowd and whistles."

    show emily mischievous at left
    e "The seats are packed, it’s probably like 50 bucks for a ticket. Come on."

    na "Emily twitches her fingers to beckon Catherine up. Catherine lowers her hand into Emily’s and grips tightly as Emily pulls her up."

    show catherine worried at right
    c "What if we get caught?"

    show emily flippant at left
    e "Well just be quiet and we won’t."

    show catherine content at right
    na "The girls crawl to the middle of the rafters and settle down."
    na "Catherine is in awe of the sight, sitting above all the lights."
    na "Emily turns to Catherine, who is still a little nervous."

    show emily satisfied at left
    e "Cozy?"

    show catherine bashful at right
    c "I like the view."
    c "Emily..."
    c "Thank you."
    play music "true_ending.mp3"
    na "Music starts to fill the auditorium as the orchestra starts to play."
    e "I swear they do this song every year."

    if character == 0:
        na "Catherine smiles at Emily’s outburst, then looks down at the orchestra playing and gently sways to the music."
    else:
        na "Emily looks over at Catherine and catches her smiling at the orchestra."

    na "   "

    na "After a few songs, Emily looks over."

    e "Hey, Catherine, the concert’s ending, we gotta leave."

    na "Catherine nods and gets up and they make their way out. Catherine catches Emily as she climbs out of the rafters. "
    na "They slowly make their way back to the mansion, Catherine holding Emily’s hand to prevent her from falling. "
    na "Catherine looks distantly towards the moon with the smile slowly fading off her face more the closer they get to the mansion’s doors. "
    
    play music "gecmc.mp3"
    show emily curious at left
    show catherine frown at right
    scene potraits
    na "When they enter, the room is more dim than Catherine remembers it being."

    show emily peeved at left
    e "Don’t tell me you’re gonna revert to your usual glum attitude after what we just went through!"

    show catherine worried at right
    c "What?"
    c "I’m not glum!"
    c "I enjoyed the concert thoroughly–"

    show emily scolding at left
    e "I know you enjoyed it!"
    e "I saw you smiling!"
    e "You never do that!"

    na "Emily throws out her hands expectantly."

    show emily peeved at left
    e "So how do we get it back?"

    show catherine bashful at right
    c "..."

    show emily curious at left
    e "..."

    show catherine awkward smile at right
    na "Catherine tries out a slow smile."

    show emily peeved at left
    e "The real thing!"

    show catherine bashful at right
    c "This is the “real thing”."

    show emily flippant at left
    e "No, when you’re really smiling, your pupils get brighter, and they are hella dim right now."

    show catherine startled at right
    if character == 0:
        na "Catherine is stunned into silence for a moment, she doesn’t know how to feel about someone recognizing such an innocuous detail about her. "
        na "Do they really get brighter?...She recovers with a sigh."
    else:
        na "Catherine is stunned into silence for a moment."
        na "She recoveres with a sigh."
    show catherine frown at right
    c "I swear I’m not upset, Emily."

    show emily scolding at left
    e "Catherine, the ONE thing you must NEVER do to me, is {i}lie{/i}."
    e "So why."
    e "Are you, upset?"

    show catherine worried at right
    na "Catherine blinks."
    na "She fidgets."
    na "She sweeps over to the staircase and takes a seat."
    na "Emily’s eyes track her expectantly."

    show catherine frown at right
    c "Well, hearing the music again...it reminded me of something..."

    show emily flippant at left
    e "Another 1910’s memory I have to recreate? "
    e "Catheriiiiiiine! "
    e "It’s like you’re impossible to please."

    show catherine shadow at right
    c "..."

    show emily curious at left
    e "No wait, I’m sorry, I’m sorry, go on."

    show catherine frown at right
    c "We... we used to have these extravagant dances in this ballroom. Not very often, no, probably twice a year. "
    c "My mother probably would have preferred more – those dances were the happiest – or at least the busiest – I had ever seen her."
    c "But father always said we had too little money to spend on frivolous things."

    if character == 0:
        na "Catherine pauses."
        na "She is not used to talking this much."
        na "The last person she could talk to at this length was in her life a very long time ago."
        na "But now, Emily sits, eyes trained on her, seemingly taking all this in with a perfect poker face."
        na "There is something comforting about a nil reaction to this story, but it mostly makes her feel uneasy, so she continues to fill the silence."
    else:
        na "Catherine pauses. Emily sits, eyes trained on her, seemingly taking all this in with a perfect poker face."
    c "I never participated beyond the few dances necessary to be a good host. "
    c "I really preferred to just sit on the staircase – out of sight of course, I wouldn’t want to be an eyesore for my parents."

    show catherine bashful at right
    na "She pauses again."

    c "But hearing all that commotion, all those voices, it felt that the house was less empty. It was as if I could almost fall asleep"
    c "I actually did once or twice"
    c "which was not amusing to my father – I drool in my sleep. But there’s something about having a full house that just makes it feel..."
    c "more comfortable I suppose."
    c "So when I came in and saw it empty again I..."
    c "I don’t know."

    show emily hurt at left
    na "Emily’s poker face is broken by the tenderness in her eyes."

    show catherine worried at right
    c "Is that a satisfactory answer?"

    stop music fadeout 1.0
    play music "intimate_song.mp3"
    show emily satisfied at left
    scene ballroom
    na "Emily is looking down at the floor, arms folded. She suddenly throws her hands over her head and arches her back in a stretch."

    e "Well, let’s get this over with."

    show catherine bashful at right
    c "Pardon?"

    show emily genuine at left
    e "You want to dance, like you used to."

    show catherine startled at right
    c "I {i}used{/i} to sit on the staircase."

    show emily satisfied at left
    na "Emily’s hands slowly drop to her waist and she takes a step towards Catherine, now standing only an arm’s length away from the vampire. Emily smiles slightly, and jokes"

    show emily mischievous at left
    e "You {i}are{/i} sitting on the staircase, you can check that off of the list."

    show catherine bashful at right
    na "Emily in a relaxed motion extends her hand to Catherine, who remains unconvinced."

    show emily genuine at left
    e "I can’t give you a full ballroom."

    na "She leans down closer. Their eyes connect."

    e "But we can make it feel full."

    na "   "

    show catherine bashful at right
    c "There’s no music playing."

    show emily flippant at left
    e "Does it matter?"

    show catherine bashful at right
    c "I suppose not."

    show catherine gay blush at right
    na "Catherine slowly lowers her hand into Emily’s before grasping the hand tightly."
    na "Emily slowly raises her hand and helps Catherine rise to her feet."
    na "She and Emily settle into a proper position."

    show catherine worried at right
    c "Do you... know how to do this?"

    show emily satisfied at left
    e "No, but you do. Lead me."

    show catherine content at right
    na "Catherine stops moving and the pair stand in the center of the ballroom, gently illuminated by the moonlight and candles surrounding the exterior of the room. "
    na "Catherine exhales a single breath into an exasperated laugh."

    c "As you wish."

    hide emily
    hide catherine
    na "Catherine turns her body to face Emily, their eyes locking."
    na "With their intertwined hands, Catherine pulls the other girl closer and guides Emily’s hand to rest on her shoulder before placing her free hand on the small of Emily’s back."

    na "As the moon continues to rise, Emily slowly improves with each step, matching every step Catherine takes. Before long the couple are dancing around the ballroom. "
    na "The candles slowly die out, Emily slows down as the only light illuminating the room is the moonlight pouring out of the windows surrounding the edges of the room."

    show emily satisfied at left
    e "You’re smiling."

    show catherine gay blush at right
    c "Are you pleased?"

    show emily genuine at left
    e "Your eyes are bright."

    hide emily
    hide catherine
    na "Emily tucks her head into the crook of Catherine's shoulder. Catherine tenses for a moment, but when Emily does not flinch, she relaxes and continues swaying on."

    if character == 0:
        jump catherine_flashback_3
    else:
        jump emily_flashback_3

label under_the_chandelier:
    play music "intimate_song.mp3"
    scene ballroom
    show emily curious at left
    show catherine content at right
    na "Emily and Catherine are together in the mansion after another dinner, as twilight sets in. "
    na "As Emily is exploring the mansion with Catherine, they enter a room with an ornate chandelier hanging above them. "
    na "Emily looks up, her eyes widen at the reflections of sunset bouncing off the glass onto the ceiling. "
    na "Catherine grabs Emily’s arm and leads her underneath the chandelier to the center of a carpet, and lays down, leading Emily with her. "
    na "They look up at the ceiling together."

    show emily curious at left
    e "They almost look like stars."

    na "..."

    c "Yes."

    na "..."

    c "I do this often."
    extend " Looking at the stars."

    na "Catherine reaches her right hand up towards the ceiling."

    c "They keep me sane I suppose."

    e "That’s nice."

    na "The two lay for a little while longer."
    play audio "walking_wood.mp3"
    na "Eventually, Emily looks over at the corner of the room and sees a large painting frame in the corner, with its front facing the wall. "
    na "Emily gets up and turns the frame around to see an old painting of a family of three, dressed nicely."

    na "There’s a father, slightly stern in his posture and face with a well formed mustache. "
    na "The mother looks a little tired, but smiling, in a way reminiscent of the Mona Lisa."
    na "The child is a young girl, not yet a teenager, with a serious expression on her face, standing underneath her parents. "
    na "Catherine walks up, and puts the frame back how it was."

    e "Were you an only child?"

    c "..."

    c "My mother had a miscarriage before she had me. "
    extend "But other than her" 
    c "Yes"
    extend ", I’m an only child."

    e "Ah, I’m sorry."

    na "..."

    e "Were you happy, back then?"

    c "..." 
    c "Sometimes I was."

    e "Do–"
    e "Do you think your parents were good people?"

    na "Catherine stares past Emily for a few moments. Her eyes seem focused while she looks at nothing in particular and her expression painfully still."

    c "I don’t know."

    na "..."

    e "I think my dad was a good person."

    c "Your father?"

    e "Yes, he —" 
    e "He did a lot of nice things for me and mom."
    e "He loved us a lot."

    na "..."

    e "I hope I get to see him again one day."

    na "Catherine looks at Emily with a caring expression."

    c "I’m sorry about your father."

    e "It’s–" 
    e" It’s fine."

    na "Emily lays back down on the carpet."

    e "My mother isn’t really a good person like my dad. She’s–"
    e "Well,"
    e "She’s kinda aggressive."

    c "Aggressive?"

    e "..."
    e "Did you go to church, as a kid?"

    c "Occasionally,"
    c "My mother would sometimes take me."

    e "I–" 
    e "I also went to something like a church, when I was a kid."
    e "My mom would be the one to bring us as well."

    e "..."

    e "It was more, occult focused." 
    e "I thought that was normal for a long time, but I've talked to a few other people about it" 
    e "And whenever I talk about what happened there " 
    extend "people get really scared and concerned. And my mom –"

    na "..."

    e "My mom definitely scared some people when I told them some of the things she had done." 
    e "I think it was an outlet for her,"
    extend " what she did there."

    na "..."

    e "She’d usually take it out on dad, between meetings."
    e "She took a lot out on him. He–" 
    e "He was a good person, I think." 
    e "Especially compared to mom,"
    extend " and compared to me."
    e "The occult was an outlet for him as well, but it was much less violent for him."

    na "..."

    e "I think I’m a lot more like my mom."
    e "I can feel it sometimes, when I lose myself"
    extend", I get the desire to do the things that she did when I was a kid to the people around me."

    na "Emily looks Catherine in the eyes."

    e "But I think I’m at least a little better than her!"
    e "Even if I get angry at people, even if I want to hurt people, I don’t."
    e "Even if I’m a bad person on some fundamental level, I can at least control myself better than she could."

    na "..."

    e "I just wish dad were still here."
    e "It’d make things easier."
    e "He was so nice to talk to, he’d always be so caring, always looking out for me."
    e "I never understood why mom hated him so much."

    na "..."

    c "I’m sorry you had to experience that."

    na "Emily grabs Catherine’s arm."

    e "Hey Catherine. After – after you’ve lost your parents, it’s been a long time."

    na "..."

    e "Does the pain – does it go away after a while?"

    na "Catherine thinks for a second."

    c "It does."
    c "You just need to disconnect from them."
    c "That’s why I leave the painting over there where it is."
    c "It used to be hung up in the piano room, and I just couldn’t stand to look at it after a while."
    c "And now, well now I don’t think about them often."

    na "Emily looks at Catherine, disappointed."

    e "That – that can’t be the right way to think about it! You shouldn’t forget your parents, especially if they were good people."

    na "Catherine looks away from Emily, a pained expression on her face."

    show emily curious at left
    e "I – I remember my dad told me vampires could shapeshift. Can you turn into your parents?"

    show catherine startled at right
    na "Catherine’s eyes widen."

    c "No."

    show emily peeved at left
    e "Please –"

    show catherine worried at right
    c "Absolutely not. I – I,"

    na "Catherine is on the verge of tears."

    c "I don’t want to remember."

    na "The two lay in tension for a moment."

    show emily curious at left
    e "Can you not transform, or do you just not want to?"

    show catherine frown at right
    c "Dear god Emily, I just don’t want to remember."

    show catherine stoic at right
    na "Emily looks at Catherine for a second."
    na "She sees her pull back from the edge of tears, a warm, but stoic expression on her face."
    show emily genuine at left
    na "Emily smiles and puts her arms around Catherine."

    e "You remind me a little of my dad sometimes."

    na "Catherine sits in silence for a second, before putting her arms around Emily. "
    na "The two lay there for a moment, under the chandelier, as the lights from the sunset disappear into darkness."

    hide emily
    hide catherine
    jump first_time_drinking

label first_time_drinking:
    scene c_bedroom
    show emily curious at left
    show catherine bashful at right
    na "Catherine and Emily get up, and Catherine leads Emily over to her bedroom. Before Emily leaves, she looks over at Catherine to ask a question."

    e "Can you shift into anyone? Y’know, besides them?"

    show catherine frown at right
    c "No."

    show emily curious at left
    e "Why not?"

    c "I’ve never drunk anyone else’s blood."

    e "Never?"

    show catherine shadow at right
    c "The first time... wasn’t exactly enjoyable."

    show emily curious at left
    e "But don’t you get hungry?"

    show catherine worried at right
    na "Catherine swallows"

    c "Very. My body doesn’t need it to survive, but all the symptoms of hunger remain."

    show emily desperate at left
    e "Catherine, you’ve been starving for years?"

    show catherine stoic at right
    c "I find that it can only get so bad. Becomes background noise after a while."

    show emily mischievous at left
    e "So you wouldn’t wanna taste me?"

    show catherine startled at right
    c "What?"

    show emily mischievous at left
    e "Aren’t you interested in what I taste like?"

    show catherine worried at right
    c "I– I don’t want to hurt you, it’s very painful."

    show emily genuine at left
    e "I’m sure what you were feeling then, is way different than what you’re feeling now. You can drink from me, aren’t we close enough for that?"

    show catherine bashful at right
    c "I suppose..."

    hide emily
    hide catherine
    scene teeth_bared
    na "Emily pulls the collar of her dress to her right side and tantalizingly leans over Catherine, giving the vampire a clear view of her neck. "
    na " Catherine fearfully leans closer, hesitantly brandishing her teeth, she looks at Emily to see her eagerly awaiting the bite."

    na "Catherine swallows, and then steps forward into a choice she can’t come back from."
    play audio "heartbeat_sound.mp3"
    na "She sinks her fangs into the willing victim, puncturing the skin slightly above the collar bone."
    na "The pain is sharp yet fleeting as the vampiric venom numbs the area surrounding the bite."

    
    na "And as blood starts to seep out of the wound, Catherine hungrily drinks the warm liquid, satiating her decades long desire."
    na "It’s the sweetest thing she’s ever tasted across both her lifetimes."
    na "She sinks her teeth deeper."
    na "Emily makes a sound, and this drives Catherine over the edge, her strength starts to activate, and she sweeps Emily up by her thighs."

    play audio "sheets.mp3"
    na "She pushes forward, and sets Emily down on the bed."
    na "Roughly."
    na "Emily relaxes into Catherine’s arms, fully immersing herself in the experience, her hands wrap around Catherine’s neck locking her close."

    na "Catherine speaks, gasping."

    c "W-Wait, we really shouldn’t..."

    e "Keep going! Please!"

    na "Emily slightly pulls on Catherine’s shoulders, and Catherine goes in again."
    na "Emily moans and as Catherine plunges deeper, she starts gasping."
    scene drinking
    play audio "heartbeat_sound.mp3"
    play audio "pillow.mp3"
    na "She grips Catherine’s horns to steady herself, arching her back further into it."

    na "The pleasure is so intense, she doesn’t know if her body can handle it."
    na "She wraps her legs around Catherine, pressing against her as hard as she can, trying to release a fraction of the tension."
    na "The venom is softening all her muscles, making her pliant, but the pain renews each time Catherine readjusts, and Emily bucks all over again."

    
    na "Catherine finally does pull away."
    na "And Emily whispers a soft “no.” Catherine’s face and the entirety of her top is drenched."
    na "Emily doesn’t waste a second."
    scene hold_1
    na "She pulls Catherine’s face to hers, Catherine can only get a puff of breath in."

    c "What are you doing?"

    e "Don’t you want to?"

    na "Catherine doesn’t move, but her eyes go down to Emily’s mouth."
    na "Emily smiles, and teasingly, wipes her tongue over Catherine’s lips."
    scene the_kiss
    na "They look at each other for a second, and then they aren’t apart anymore."

    na "When Emily begins to pull away, Catherine can’t help the whimper that comes out of her."

    scene emily_red
    na "Emily looks at Catherine, who clearly wants more, enjoying the look in her eyes."
    na "They’re both panting, and Catherine’s claws tighten on Emily’s thigh."
    na "Her mind idly wonders what it would feel like under her teeth."

    na "Emily’s face is dripping with her own blood, but the smile underneath all the red is the most alluring thing Catherine has ever seen."
    na "Emily runs a hand through Catherine’s sleek hair, cupping her cheek and gliding her thumb across Catherine’s bottom lip."
    na "When she speaks, it’s a whisper."

    e "Catherine..."

    c "Mm."

    e "I love you."

   
    na "Catherine’s whole body goes numb."
    na "The words don’t echo through the mass of cotton in her head, they hardly penetrate."
    na "She suddenly becomes aware of her blinking."
    na "She has not done so for a very long time."

    na "Then, warmth, like the sun peaking through her window seal each morning, rises through her body."
    na "It’s like having blood again."
    na "There is nothing in it’s path, nothing that blocks it, she gives no extra effort to let it through, and no force to suppress it."
    na "It is the easiest thing she has ever experienced, and she realizes that this feeling is something Emily has given to her."
    scene catherine_love
    na "When she opens her mouth, her breath hitches, but when she exhales, it’s through a smile."

    c "I love you too."

    jump the_plan

label the_plan:
    scene c_bedroom
    show emily curious at left
    show catherine gay blush at right
    play audio "sheets.mp3"
    na "Catherine and Emily are lying in Catherine’s bed, clean from the earlier blood drinking.Their gazes are soft, their poses timid."
    na "Catherine can’t turn away the pretty pictures of Emily covered in blood that keep arising, she almost wishes they hadn’t washed up."
    na "Emily’s hair frames her like a halo."
    na "Catherine does not know how such an angelic creature has allowed herself anywhere near such scum."

    na "She stares, flooded with the pleasure of being full for the first time."
    na "It is an almost sickening feeling, it might be too much... but her cheeks feel warm for the first time in decades, and she relishes it."
    na "As Emily breathes, Catherine fears that her craving for her travels in more directions than she can count, all of them insatiable."
    show emily desperate at left
    na "Suddenly, worry starts to cloud Emily’s gaze."
    show catherine worried at right
    na "Catherine tenses to it, she wishes she could remove whatever is troubling Emily and kill it instantly."

    show emily desperate at left
    e "Catherine..."

    show catherine bashful at right
    c "Yes?"

    show emily desperate at left
    e "Am I... am I going to turn?"

    show catherine startled at right
    c "Turn?"

    show emily desperate at left
    e "Will I... am I going to be like you?"

    show catherine worried at right
    c "Oh, no."
    c "No!"
    c "I would– Emily I could never do that to you."
    c "I would never trap you like that."

    show emily curious at left
    e "But then, how does it happen?"

    show catherine shadow at right
    c "..."

    show emily desperate at left
    e "...Catherine?"

    show catherine worried at right
    c "Do you truly want to know?"

    show emily genuine at left
    e "Why wouldn’t I?"

    na "..."

    show catherine frown at right
    c "It's... it’s very gruesome."

    show emily satisfied at left
    e "I can handle that."

    show catherine worried at right
    na "A moment of silence. Catherine fidgets with her hands, but the motion hurts horribly with how hard she is pressing."

    c "When I “turned”, I was... dead, for a moment."

    show emily curious at left
    e "She waits, expecting this to land heavily. Emily’s expression has not changed."

    e "What did you see?"

    show catherine bashful at right
    c "See?"

    e "When you were dead? What was –"

    na "Emily’s eyes dart around and her brow is furrowed, like she’s examining a wound."

    e "What did you see?"

    show catherine shadow at right
    c "I– I didn’t see anything."

    e "..."

    c "There wasn’t anything."

    e "..."

    c "..."

    show emily desperate at left
    e "So when you were dead..."

    show catherine frown at right
    c "I could still feel everything."
    c "Everything that– everything that Braxt– everything that he was doing to me."
    c "Did to me."
    c "I–I..."

    show emily genuine at left
    na "Emily reaches over and touches Catherine’s face."

    e "What did he do?"

    show catherine shadow at right
    c "He– He ripped out my heart."
    c "It was so strange, it was as if I could feel it bobbing away from me into the dark, my veins were tethering it and then...they snapped."
    c "For a moment, it was gone."

    na "Emily wipes a strand of Catherine’s hair away."

    show catherine frown at right
    c "I think that was the most afraid I’d ever been in my life."
    c "It must have been a brief moment though – despite it feeling like an eternity – because I felt my heart ignite again when he... bit it."
    c "Then he was shoving it down my throat."

    show catherine shadow at right
    c "I don’t know how he even fit it in there, my neck being broken beyond belief must have helped a good deal, but still..."
    c "I felt like a taxidermied animal, that they forwent the stuffing for, and instead tried filling me with boulders, boulders that were tearing my throat apart."

    c "Then, my heart was returned to its alcove."
    c "And I felt myself reset."
    c "My veins reconnected, and I felt the venom and, Emily, it was hellfire."
    c "It was foreign  {i}his {/i}, and it was flaying me alive from the inside and I – Emily I could never do that to you."
    c "I could never put you through that."
    c "You would feel every second of it."

    show emily desperate at left
    e "And it’s a lonely existence afterward anyway."

    show catherine frown at right
    c "Yes... it is."

    show emily genuine at left
    e "But Catherine, I would have you forever."

    show catherine bashful at right
    c "You already have me forever."

    show emily desperate at left
    e "Not for long... you’ve already lived practically double what I will ever get to."

    show catherine content at right
    c "Then we will spend every second of that time together."

    show emily peeved at left
    e "It’s not enough."

    show catherine frown at right
    c "It’s what we have."

    show emily desperate at left
    e "We can’t even do that though. Eventually someone will come looking for me here, and who knows what they would do to us."

    show catherine stoic at right
    c "I’m more than equipped to handle anyone that comes our way. I’m not a violent creature... but I was made to kill."

    show emily curious at left
    e "You’d do that for me?"

    show catherine content at right
    c "If it was to protect you, yes."
    stop music fadeout 1.0

    na "They lay in silence."
    na "Emily has curled her head onto Catherine's chest."
    play audio "heartbeat_sound.mp3"
    na "She can hear the beat of her heart."
    na "The heart she thought she had lost forever, now pumping venom through her veins."
    na "How much of it is hers, and how much of it is his?"

    show emily desperate at left
    e "Catherine...If there was a way you could spend forever with me, without turning me...would you take it?"

    show catherine content at right
    c "In a heartbeat."

    show emily mischievous at left
    na "Emily rises, and looks Catherine in the eye."

    e "There’s a way we could."

    play music "emily_song.mp3"

    show catherine bashful at right
    na "Catherine pushes herself off of the mattress, once seated, she folds her arms over her bent knees, listening intently, and ready to receive anything Emily offers."

    show emily genuine at left
    e "There’s a ritual, but you’d have to keep your word, you have to be willing to kill."

    show catherine worried at right
    c "..."

    show emily satisfied at left
    e "It’s not permanent."

    show catherine bashful at right
    c "How so?"

    show emily mischievous at left
    e "The killings – four of them for number’s sake – will unlock the door, and they’ll be able to join us in Paradise."

    show catherine startled at right
    c "Paradise?"

    show emily satisfied at left
    e "Yes it’s a, it’s hard to explain."
    e "But essentially: The ritual will consist of four killings."
    e "We’ll need to bury the bodies in a specific spot, in a circle, and then we’ll need to perform a blood ritual."
    e "You won’t have to worry about the details of that, I know the process by heart."

    show catherine worried at right
    c "What would it all be for?"

    show emily genuine at left
    e "I’m getting to that!"
    e "Each of the four people we choose, they’ll help us open a door, a door to a paradise built just for us– and them!"
    e "All of them will be able to join us there!"
    e "Once they’re reborn, we’ll all get to live forever in a world that’s tailored to our every desire."
    e "Doesn’t that sound perfect?"

    show catherine bashful at right
    c "How do you know about this?"

    show emily flippant at left
    e "..."

    show catherine worried at right
    c "How do... how do you know it’s real?"

    show emily desperate at left
    e "My dad went there."

    show catherine shadow at right
    c "..."

    show emily flippant at left
    e "I tried to follow but...he didn’t want me there. But that doesn’t matter, because it means I get a world with you."

    show catherine bashful at right
    c "..."

    show emily curious at left
    e "..."

    show catherine content at right
    c "Who would we pick?"

    show emily satisfied at left
    e "My friends from the occult club of course, and..."

    show catherine bashful at right
    c "And?"

    show emily flippant at left
    e "There’s this girl...her name is Rose."

    show catherine frown at right
    c "Rose..."

    show emily desperate at left
    e "We were... she’s like us."

    show catherine startled at right
    c "Oh."

    show emily genuine at left
    e "We were together for a little bit but then her parents found out and...I want her to have a world like ours too. She deserves a world where she’s accepted."

    show catherine worried at right
    c "..."

    e "..."

    show catherine content at right
    c "How will we do it?"

    show emily mischievous at left
    e "Catherine..."

    na "Emily cups Catherine’s face between her hands."

    show emily genuine at left
    e "I love you."

    hide emily
    hide catherine
    jump roses_murder

label roses_murder:
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

label ritual_one:
    play music "ritual_song.mp3"
    scene vineyard
    show emily gross at left
    e "Geez, that was, I’m...geez."

    show catherine worried at right
    c "Are you alright?"

    show emily desperate at left
    e "Yeah it was just {nw}"
    e "it was a lot {w=.3}louder than I expected."
    e "I thought"
    e "..."
    e "we’ll need to plan for that in the future."

    show catherine stoic at right
    c "I will."

    show emily satisfied at left
    e "Did you get the items I asked for?"

    show catherine content at right
    c "Yes. Her house was surprisingly easy to get into."

    hide emily
    hide catherine

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

label catherine_breakdown:
    play music "tecc.mp3"
    scene vineyard
    show emily gross at left
    show catherine shadow at right
    e "Phew, she should be good to go in the ground now."
    e "You remember where to put her, yeah?"
    e "Geez this is so fucking gross."

    show catherine worried at right
    c "Yes, I recall the location..."

    show emily mischievous at left
    e "Oh wait! You need to feed on her."

    show catherine startled at right
    c "Pardon?"

    show emily flippant at left
    e "You need to drink her blood."

    na "Emily holds up Rose’s fractured head to Catherine."

    e "Go on."

    show catherine worried at right
    c "Wha– Why would I?"

    show emily scolding at left
    na "A look from Emily."

    show catherine worried at right
    c "I’ll do it! I’ll do it...just um...I want to understand your plan."

    show emily genuine at left
    e "I can’t lure everyone to the mansion every time, it won’t look right. "
    e "What we need is good – no PERFECT timing, we’ve got three months left until the bloodmoon, it’s tight, but if we spread this right, by the time sirens are sounding we’ll be gone."

    e "We’ve got an effective method of murder and the space to store everyone...but what we don’t have, is a way for YOU to be inconspicuous. You see where I’m going with this?"

    show catherine worried at right
    na "She pushes the corpse towards Catherine again. Catherine takes it in her claws this time, but still looks at Emily with pleading eyes."

    show emily flippant at left
    e "Look, you need a way to get close to my friends."
    e "A way to also lure them out here."
    e "Learn their patterns, learn who they are so you can get their totems."
    e "Rose is your venue to that."

    show catherine frown at right
    c "So I’ll be gallavanting with you into the human world?"

    show emily satisfied at left
    e "It’s still your world Catherine, just decades into the future."

    show catherine shadow at right
    na "Catherine looks down into the pool of blood Rose is pouring onto her lap."

    show emily genuine at left
    e "I need you with me on this."
    e "The risk will be exponentially less when split between the two of us, plus I think you would wanna know who you are spending your eternity with."
    e "It’s just for a little while, shes a mask you get to wear, and then shuck off at the end of the day."
    e "No one else will know it’s you except me."
    e "We’ll still be in our little bubble."
    show emily mischievous at left
    e "And whenever it’s just us..."

    na "Emily leans over, dipping her hand in the pool. She hooks her bloody index finger on Catherine’s bottom lip."

    e "Please Catherine."

    show catherine worried at right
    na "Catherine is quivering, but she gives Emily entry, opening her maw to reveal her glistening fangs."
    na "Emily’s bloody fingers creep onto the wet surface of Catherine’s tongue, nestling there."

    c "Mmm."

    show emily seductive at left
    e "It’s okay. You can lick."

    na "Cathering shudders, her eyes squeezed painfully shut."
    na "She closes her mouth slightly, removing her tongue out from under Emily’s fingers, and instead gliding over them."
    na "She lets out an involuntary sigh as the blood starts to warm her throat."
    na "She spoons her lips over Emily’s fingers, sucking the blood off with more vigor."

    na "Emily’s other hand slides down Catherine’s side, from her breast to her hip, then up to her neck, where she uses it to hold Catherine steady while she plants a kiss."
    na "She then moves her lips from the neck to the ear, playfully biting it."

    show emily satisfied at left
    e "Good girl."

    show catherine gay blush at right
    c "Mm."

    na "Emily pulls away."
    na "Catherine opens her eyes, and then her mouth."
    na "Emily pulls her finger out, and after ensuring that they’re clean of any blood – of course they are, Catherine is very thorough – she pops her index into her mouth."
    na "Catherine feels heat flood her center."

    show emily flippant at left
    e "Go place the body."

    show catherine bashful at right
    na "Catherine can only nod."

    hide emily
    hide catherine
    scene bathroom
    na "That night as Emily sleeps soundly in their bed, Catherine is hunched over in the darkened bathroom. "
    na "Her claws grip the sink, and their hold tightens until – a piece of porcelain falls into Catherine’s hand."

    show catherine startled at center
    c "Oh no, no no no."

    show catherine shadow at center
    na "But her attention is caught by the hand holding the porcelain."
    na "Is that?"
    na "Is that her hand?"
    na "Why does it feel so far away?"
    na "She stares at it, horrified the longer she looks at the blurry image of a hand that doesn’t seem to belong to her, when suddenly something drips onto it."
    na "When Catherine looks to the mirror again, her cheeks are slick."
    na "She’s no longer herself."

    hide catherine
    jump first_day_of_school

label first_day_of_school:
    play music "intimate_song.mp3"
    scene c_bedroom
    na "“Rose” sits in front of a previously long abandoned mirror."
    na "Emily is brushing her hair, occasionally forgoing the brush to run her hands through the strands."
    na "Rose looks innocently up at Emily, and Emily comes around the chair to sit in Rose's lap."
    na "They look into the mirror together, and “Rose” thinks she sees the slight shine of tears in Emily’s eyes."
    na "Emily reaches up and takes “Rose’s” chin in her hand."

    show emily genuine at center
    e "Are you ready my love?"

    hide emily
    na "“Rose” nods."

    na "Emily gazes at her for a moment."
    na "Then she kisses “Rose” gently."
    na "It is long, and warm."
    na "When they part, Emily runs her thumb over “Rose’s” cheekbone."
    play audio "door_open.mp3"
    na "Then the girls rise, and holding hands, they exit into the true start of their plan."

    jump drama_club

label drama_club:
    play music "drama_song.mp3"
    scene dramaroom
    play audio "door_open.mp3"
    na "Emily opens the door with “Rose” following behind her as they both arrive, about 15 minutes late to drama club."
    na "Andrea, Aarya, Ophelia, Mac, and Ash are all present."
    na "Rei is conspicuously missing."
    na "Aarya is the first to notice the two come in."

    show aarya incredulous at right
    aa "Hey Emily. Lose track of time again?"

    show emily flippant at left
    e "Yeah, sorry."

    na "”Rose” takes a look at the people around here."

    show rose listening at center, flip
    show aarya sure at right
    aa "Ooooo, got distracted with Rose again? I haven’t seen you two together in a while."

    hide aarya
    show ophelia excited at right, flip
    op "Oh, Rose!"

    show ophelia comforting at right, flip
    na "Ophelia runs up to hug Rose. She looks at Rose, a little concerned."

    show ophelia wondering at right, flip
    op "Why are you here with Emily?"

    fr "... She wanted me to see the club."

    op "She did?"

    hide ophelia
    show ophelia wondering at right
    na "Emily comes up and grabs Rose’s arm. Ophelia smiles as they walk a few steps away."

    hide emily
    show andrea okay at left, flip
    an "It’s a bit too late to give her a part at this point."

    show emily peeved at right, flip
    e "I’m not bringing her here to perform, I just thought it’d be nice to have her watch."

    show andrea snark at left, flip
    an "Hm, makes sense. How about this:"

    na "Andrea walks up to Rose with a script in her hand."

    show andrea pride at left, flip
    an "This is the script. You see this part here –"

    na "Andrea points to the name “Catherine”."

    show andrea snark at left, flip
    an "I need you to memorize this so that when Emily gets it wrong, you can correct her."

    show emily scolding at right, flip
    e "Hey!"

    na "Emily rips the script out of Andrea’s hands."

    show emily peeved at right, flip
    e "God, you don’t have to be so mean about it."

    show andrea ticked at left, flip
    an "I wouldn’t be if you at least bothered to try and memorize your part."

    hide rose
    show rei alright at center, flip
    play audio "door_creaking.mp3"
    na "The door suddenly opens again, for the club to see Rei saunter in. She notices Rose and waves."

    re "Andrea, did you make a new part?"

    show andrea okay at left, flip
    an "No."

    hide emily
    show rei alright at center, flip
    re "Then what’s Rose doing here?"

    show andrea snark at left, flip
    an "Andrea gestures vaguely at Emily."

    show rei hyped at center
    re "Welp, in that case –"

    show rose listening at right, flip
    na "Rei pulls out a crumpled script from their backpack and hands it to Rose."

    re "Can you do this one:"

    na "Rei points to “Father” on the script."

    show andrea ticked at left, flip
    an "Rei! Look at me!"

    show rei oops at center
    show andrea serious at left, flip
    na "Andrea walks up and grabs Rei by the shoulders."

    an "Just."
    an "Do."
    an "Your."
    an "Part!"

    show rei oops at center
    na "Andrea passionately shakes Rei with each word, as Rei sighs and rolls her eyes."

    show rei alright at center
    re "Fineeeee."

    hide andrea
    hide rei
    hide aarya
    show ash happy at left
    na "Ash walks up with Mac to greet Rose."

    ash "Hey Rose! How’s it going?"

    na "“Rose” looks down."

    fr "Oh, hello."

    na "Ash looks a little confused, staring at Rose for a second. Mac seems checked out of the conversation."

    ash "How’s bio been going for you? Did you finish the lab yet?"

    na "“Rose” seems confused."

    fr "Oh, um, I’m not sure."

    show ash sad at left
    ash "..."

    ash "Are you doing ok right now? You seem dead compared to usual."

    fr "Oh, uh –"
    show rose startled at right, flip
    na "“Rose” laughs nervously."

    fr "Maybe I am dead!"

    na "Ash looks a bit confused, then laughs with “Rose”. Emily shoots “Rose” a death glare."

    show ash happy at left
    ash "Look, if you need help with the lab, just tell me. I can give you some of the answers."

    fr "Ah, thank you."

    hide ash
    show emily peeved at center, flip
    na "Emily walks up, and drags “Rose” away."

    hide emily
    hide rose
    if character == 0:
        jump ophelias_comedy
    else:
        jump love_like_you

label catherine_flashback_1:
    play music "catherine_song.mp3"
    scene c_flashback_1
    cm "Catherine, please, set the table will you?"

    c "Yes Mother."

    na "..."

    na "The door opens. Father and another man walks in."

    cf "Ah, and now that we’re here Mr. Braxton, I’d like to introduce you to my lovely wife, Angelica, and my daughter, Catherine."

    mb "Ah, a pleasure to make your acquaintance Mrs.Lyon. And –"

    na "Takes Catherine’s hand."

    mb "A pleasure to meet you as well, Ms. Lyon."

    cf "Please, sit down. Dinner has been prepared, has it not?"

    cm "Yes, it has."

    cf "Good."
    cf "I know that you have, as one may say to be unusual tastes, so I instructed Angelica to prepare something that would not be in conflict with those tastes."
    cf "Angelica, what did you make again?"

    cm "Black Pudding."

    cf "Perfect!"
    cf "And of course, we’ll be providing a bottle of Pinot Noir from the cellar."
    cf "Does that sound acceptable to you?"

    mb "More than acceptable!"
    mb "Mr. Lyon, really, you’re too generous with me."
    mb "I can only hope to return the favor in the coming weeks of our partnership."

    cf "Please, don’t doubt yourself. I see a rich future for the both of us, god willing!"

    play audio "clink.mp3"
    na "Father and Mr. Braxton toast their glasses."

    jump an_awkward_dinner

label catherine_flashback_2:
    play music "catherine_song.mp3"
    scene c_flashback_2
    na "Catherine, reading. Mr. Braxton approaches her."

    mb "You must be quite the literary woman. I haven’t been here a day where you haven’t been sitting here with a book."

    c "Oh, um, well yes, I suppose I do enjoy reading."

    mb "Hm. What are you reading now?"

    c "Oh, well, this one is called {i}Phantom of the Opera{/i}."

    mb "Ah, are you a fan of more modern books then?"

    c "Yes, I am. Have you read this book before?"

    mb "No, but my niece has similar taste to you. "
    mb "It’s charming, really."
    mb "Reading is an activity well suited for women, in my opinion."
    mb "Intellectual stimulation does wonders on the feminine mind."
    mb "Servile tasks should be the purview of men, really."
    mb "Have your parents considered you for college?"

    c "No. Father never mentioned it."

    mb "Why not? You seem like you’d do well there."

    c "Well, um, I’m not too sure. It’s been a while since I went to school."

    mb "And so?"
    mb "You’re a smart girl, I think it’d do you good."
    mb "Much better than being forced to rot here in this old mansion."

    c "Do you really think so?"

    mb "Yes, of course!"
    mb "A lady like you should get to see a little bit more of the world."
    mb "And if you want to attract an intellectual man, I can assure you a little more education will do you no harm."

    c "..."

    c "Did you go to college, Mr. Braxton?"

    mb "Ah, well, not for long."
    mb "I spent a few years self-studying the classics in Paris, and I attended a few lectures at Universities wherever I happened to be, but I never formally enrolled anywhere."
    mb "A shame, really. Some of my closest friends I made studying in Paris, I would’ve stayed longer if business hadn’t forced my hand."

    c "I would really like to go to Paris one day. Is it as romantic as in my books?"

    mb "Ah, it has its unpleasantries."
    mb "But for a tourist, yes, it is quite romantic."
    mb "I’m surprised your parents haven’t taken you."

    c  "Well, Father, um, he doesn’t really take me places."

    mb "Really? Have you not even been to New York?"

    c "No, I haven’t really left town."

    mb "In how long?"

    c "Um, well, I don’t really remember."

    mb "That’s tragic!"

    c "..."

    mb "Hm, well, I need to take a trip to Boston soon. Why don’t I take you with me?"

    c "I – Well, I’d need to ask Father –"

    mb "I’ll ask him for you."
    mb "I’m sure I can convince him."
    mb "I tend to go a bit insane without company."

    c "That – that would be very kind of you, Mr. Braxton."

    mb "Please, the pleasure is mine."

    jump the_orchestra

label catherine_flashback_3:
    play music "catherine_song.mp3"
    scene c_flashback_3
    na "Catherine in her room. Braxton enters with two wine glasses in hand."

    c "Oh, hello Braxton!"

    mb "Ah, Catherine, Catherine, here, take a glass."

    c "Ah, thank you."

    mb "..."

    mb "Did you enjoy Boston?"

    c "Yes, quite."

    mb "The circus was nice, wasn’t it?"

    c "Yes, I liked the elephant."

    mb "..."

    mb "You’re a much more worldly girl than I would’ve guessed."

    c "What do you mean by that?"

    mb "Well, you understand."
    mb "It’s just, you, you seem to know how to behave yourself really quite well."
    mb "Quite well indeed."

    c "I don’t think I’m too polite –"

    mb "No no no, not polite, you’re, well. You’re really quite mature..."

    c "..."

    mb "You, you really seem quite young and innocent, but you have the sense of a woman twice your age." 
    mb "And, well, I really don’t want you to see that as a bad thing, it’s actually quite attractive."

    mb "Women your age are always so hard to deal with, always going off in some direction or another to do some frivolous activity like dancing or such. "
    mb "But you don’t really seem to do that, you’re, well you’re someone who knows how to control yourself."

    c "... I suppose so."

    mb "Catherine,"

    na "Braxton stands up and leans over Catherine."

    mb "Have you ever fancied anyone before?"

    c "..."

    mb "..."

    c "I can’t say I have."

    mb "Really? Never?"

    c "Well, not anything serious."

    mb "Oh come on, you can be honest with me! Really, I’m quite interested. "
    mb "I care about you, you know."

    c "I don’t think I should say, really, it wasn’t serious."

    mb "Catherine, Catherine, {i}please{/i}, I beg of you! Can you at least tell me his name?"

    c "She wa –"

    mb "..."

    c " I– I’m sorry! I misspoke, my apologies, {i}he{/i} wasn’t –"

    mb "Catherine."

    c "...Yes Mr. Braxton?"

    na "Braxton sits down next to her."

    mb "Catherine, remember-"
    mb "remember that time I spent in Paris?"

    c "... Yes, you said you enjoyed it there."

    mb "There was-"
    mb "there was this, well, this friend I made there. Claudius."

    mb "..."

    mb "Claudius was someone I was very close to. We-" 
    mb "well-" 
    mb "we spent a lot of time talking."
    mb "About everything!"
    mb "About the weather, his professors, about, about his family, his dreams, my dreams, our love of Cicero —"

    c "Did you fancy him?"
    mb "..."
    mb "I don’t know."

    c "..."

    mb "I think god curses those with intelligence, in one way or another. "
    mb "No character can be perfect, some are too melancholic, some too phlegmatic, and, well, I think for some –"

    na "Braxton takes Catherine’s hands."

    mb "For some, he makes us as we are."

    c "Braxton, I –"

    mb "Catherine"
    play music "murder_song.mp3"

    mb "I love you."

    c "...What?"

    mb "Catherine, I love you, really I love you more than I thought I could love."

    na "Catherine tries to pull her hands away."

    mb "Catherine, please, I love you."

    c "Mr. Braxton –"

    na "His grip on her hands tighten."

    mb "Catherine, I’m begging you, please."

    c "I – I’m really not good enough for you, Mr. Braxton —"

    na "Catherine yanks her hands away from Braxton’s."

    mb "Catherine, do you not understand? You’re perfect,{i} please {/i}, you’re good enough for me! "
    mb "We’re both sick, sick in the same way. Would you rather me wear a dress —"

    c "I don’t really think you understand."

    na "Catherine walks towards the door. Braxton grabs Catherine by the shoulders forcefully."
    scene chud_flashback_1
    mb "Catherine, look at me."

    na "Catherine's breath is heavy."

    na "Braxton tries to kiss Catherine. She moves her head away."

    c "I’m not interested, Mr. Braxton, really."

    na "Braxton pauses."

    na "Braxton stares at Catherine. Blood rushes to his face."

    na "..."

    na "Braxton squeezes Catherine, hard."

    c "Braxton, please!"
    play audio "bones_breaking.mp3"
    na "Catherine’s shoulders break. She screams."

    na "Braxton’s eyes widen."
    na "He slams his hand on her mouth."
    play audio "neck_crack.mp3"
    na "Catherine’s neck snaps."

    na "..."

    na "Braxton closes his eyes and bites into Catherine’s neck."

    na "..."

    mb "Catherine..."

    na "Braxton feels Catherine’s chest. His eyes widen once more."
    scene chud_flashback_2
    mb "..."
    play audio "ribs_opening.mp3"
    na "Braxton shoves Catherine to the ground. He claws into her chest, as her ribs crack."
    na "Skin"
    extend ", muscle"
    extend ", and sinew are spread across the floor. He reaches his right hand into her chest cavity, and rips her heart out, crushing it in his palm."
    na "He bites into it, as her heart turns a sickly green. He shoves the heart into Catherine’s mouth, down her throat and back into her chest."

    na "His breathing is heavy."

    mb "Ugh..."
    scene black
    na "Braxton opens the window and jumps out."

    jump under_the_chandelier

label emily_flashback_1:
    play music "emily_song.mp3"
    scene e_flashback_1
    define cong = Character("Congregation")

    vo "We are gathered here today, in this congregation, to convene in the strange and mysterious."
    vo "The world is full of non-believers, so small spaces must be made, to host those that understand."
    vo "The Occult welcomes you, and it knows you by name."
    vo "Amen."

    cong "Amen"

    na "Young Emily shuffles in her dress."
    na "She’s worn it three times in a row, and it’s starting to smell sour."
    na "The pews are much more crowded today than usual."

    na "..."

    na "A man steps up to the podium."

    fb "Humans."

    na "He does not shout, but with everyone’s rapt attention, his voice carries through the room easily."

    fb "Humans by nature are adverse to pain. I’m sure if I offered all of you the thrilling opportunity to jump into the icy lake out back, very little of you would partake."

    na "A laugh from the crowd. A man shouts “I know I wouldn’t!” Father Bell chuckles."

    fb "Pain comes in all forms, invisible and blinding."
    fb "Physical, mental, spiritual, emotional, pain is a root system that crosses all of human experience."
    fb "Pain can be felt in every cell of our body, and in every wisp of our ethereal form."

    fb "When faced with this evidence, could one even attempt to deny that pain is our genetic makeup?"
    fb "In an objective look at human life, one must conclude that pain will exist every step of the way, if not in action, then in potential."

    na "The air has settled uncomfortably thick."
    na "There is a charge emitting from Father Bell."
    na "Some people’s gazes are dark, as if they are remembering something terrible."
    na "Everyone is shifted towards the edge of their seat."

    fb "But we were made as we are for a purpose."
    fb "We have a natural instinct, to avoid the very thing we’re built out of."
    fb "If the human body is built of pain, and we’re practically tearing out of our skin to escape it, then it is our nature to reject ourselves."
    fb "We must honor this divine truth too."

    na "Father Bell scans the crowd, as if marking off whose eyes are trained to him and who has lost their attention to something else."
    na "Emily thinks his eyes move way too fast to actually check."

    fb "So how does one balance these two worlds?"
    fb "Well, one must first understand, that these two ideas do not contradict each other, but rather, each principle is the path for which the other can be accomplished."

    fb "We must accept that pain exists before we can move on from it."
    fb "And it remains true brothers and sisters that we must move on from it."
    fb "So how does one accept and avoid the wild beast that is pain?"
    fb "Well brothers and sisters, you do what you would do with all wild beasts."

    na "A hunger crosses over the man’s face, as he leans toward the mic, his voice containing more gravel than before."

    fb "You tame it."

    na "..."

    fb "We are pain, and to honor our instincts, we must abandon pain."
    fb "Therefore, we must abandon ourselves."
    fb "The only sure-fire method to abandon yourself, is to become a master of yourself, able to control the flow of pain in your life, able to kill off the part of you that weakens when faced with it."
    fb "This is a discipline we must devote our lives to."

    na "Emily’s Mother nods next to her."

    fb "But discipline is something most people lack the capacity for."
    fb "People do not want to master themselves."
    fb "How could they refrain from their vices?"
    fb "How could they avoid the pains we are tricked into seeing as sweet; like our alcohol, and our televisions?"
    fb "These people who lack discipline we know as subservients."
    fb "And they find too much pain in the idea of parting with themselves, so they seek that mastery somewhere else."

    fb "They seek {i}someone{/i} else, to master them."
    fb "Remember this brothers and sisters, all minds start subservient, and you will encounter many who remain so in your lifetime."
    fb "When you cross paths with them, give them the ease they desire, by providing the stimulation they crave."
    fb "They prefer the pain of subserviency to discipline, therefore, they are ready and willing to take your pain on, if it means they are controlled."
    fb "The pain you inflict on others will then become your power."
    fb "By releasing your own pain into the subservients, you become empty."

    fb "This clarity will give you greater control, and the ability to manage the flow of pain in your life so that it never enters back into you."
    fb "It is a symbiotic relationship, fueled by our unconscious wants."
    fb "We, the select few, have been enlightened, and are willing to suffer discipline for a brief moment, in exchange for the power waiting just outside of ourselves."
    fb "It is now our calling to provide mastery for others."
    fb "We are the few who can avoid pain, and the many are ready to receive it."

    fb "Amen."

    cong "Amen."

    fb "It’s a short sermon today, refreshing the basics you all know, but that’s because today, we have a special opportunity."

    na "A man, thick and bearded, emerges from a door to the side of the podium."
    scene e_flashback_2
    na "In his arms, a single white rabbit - with a burlap bag over its head – lounges contently in his arms."
    na "It is a fat thing, impossibly soft."
    na "Emily thinks it seems too pure to exist in this world, and its aura can only be accepted as “fake” to her."

    fb "We’ve been graciously offered this lovely specimen by Brother Stobacher."
    fb "It was raised in a lavish life, comfortable and adored."
    fb "Fed to excess, plenty of time and sun to run around in."
    fb "Truly we are lucky Brother Stobacher has been so generous with us."
    fb "This is a vessel {i}completely{/i} empty of pain."

    na "Father Bell makes a motion. From the same door, two more men emerge, one holding a metal bat, the other holding a rake."

    fb "And now, it is ready to receive it. For the newcomers, please observe how it is done."

    na "The rabbit is laid before the podium."
    na "Docile and trusting, it makes no effort to move."
    na "The rake comes down, holding the animal in place."
    play audio "neck_crack.mp3"
    na "Then, the man with the bat steps forward, and lands a meaty crack onto the rabbit’s leg."
    scene e_flashback_3
    play audio "rabbit_scream.mp3"
    na "Emily did not know a rabbit could scream."

    fb "I think you’ve gathered the picture."

    na "Suddenly the crowd is jumping from their seats, bounding like dogs."
    na "They rush past Emily – still seated – tripping over each other, eager to break the little thing however they can."
    na "The flurry of hands fling the rabbit around without meaning to, dragging it every direction, pulling until muscles tear and bones break."

    na "People shout curses clearly meant for other people, other places, other times. The rabbit is screaming and screaming and screaming until the screams become gurgles."

    na "Emily’s mother wrestles the bat from another wailing congregant:"

    na "And smashes it into the rabbit's head. Killing it, and making all further torture useless."

    na "It’s crazy how fast a loud room can go silent."

    na "The pastor appraises her for a moment."
    na "His demeanor has not changed, has not been shaken by the droplets of blood that now pepper his pant leg."
    na "In fact, he looks more than content."

    fb "Sister High Theobald."

    na "Emily’s mother is still heaving air."
    na "She does not turn around."
    na "She does not look at anything but a far off point nobody can see."

    fb "Try to let the others’ participation last a little longer next time, okay?"

    na "She nods."

    na "Father Bell slowly walks down the stairs and pats her on the shoulder."

    e "Amen?"

    na "Father bell looks right at Emily, smiles, and then exits. Emily can no longer smell her dress through the scent of blood."

    jump an_awkward_dinner

label emily_flashback_2:
    play music "emily_song.mp3"
    scene e_flashback_4
    cm "Useless, useless fucking man!"

    na "Young Emily lays on her bed, head down, too afraid to move."
    na "In her arms, she is squeezing a pillow for dear life."
    na "Crashing can be heard in the other room."

    cm "It feels like I am living in this house alone!"
    cm "Except I can’t even have it THAT good."
    cm "If I was alone, I wouldn’t keep having to clean up messes, left by a grown."
    cm "Fucking."
    cm "Man!"

    na "More crashing."
    na "It sounds like metal is involved."
    na "It’s not nearly as loud as the shouting that pulses through the walls."

    cm "You need to sort out whatever the fuck you’re doing, because I refuse to be seen in public with someone who can’t keep up with basic fucking house chores."

    cf "You know I’ve been feeling low lately –"

    cm "Oh I KNOW you’ve been feeling low lately, the evidence of it is all over the house!"

    na "Something shatters."

    cf "...I’m sorry Mary."

    cm "Sorry? god you’re disgusting."
    cm "If you want to be sorry, you can start by cleaning that up."
    cm "Fucking useless."
    cm "I should have left a long time ago– don’t know what I’m still doing here."

    na "Her voice fades into the background."

    na "Young Emily sobs into the pillow."
    na "Soft sounds of glass being swept up start to drift in."
    na "After a minute, Emily can feel a warm shadow behind her."

    play music "intimate_song.mp3"
    cf "Hi Emily."

    e "Hi Papa."

    cf "..."

    e "..."

    cf "Do you need a tissue?"

    e "Yes please."

    na "Father offers Emily a tissue. She sniffles, takes it out of his hands and blows."

    cf "There you go, sweetheart. Feeling better?"

    e "..."

    na "They sit in silence for a second."

    cf "Y’know..."

    na "He makes a move to touch her back, but pauses, and lets his hand drop slowly."

    cf "Y’know how {i}I{/i} try to feel better when I’m sad?"

    e "..."

    cf "I like to imagine my Paradise."

    e "What?"

    cf "My Paradise."

    e "What’s that?"

    na "Father smiles."

    cf "I was hoping you’d ask. Scoot over."

    na "Emily scoots over, her father settles heftily on the bed."

    cf "Pen and Paper?"

    na "Emily hurries to pull the items from her nightstand."
    na "She settles in excitedly."
    na "She recognizes what’s about to happen: another moment to add to her most treasured memories."

    scene e_flashback_5
    cf "I’m sure you noticed that I said “my”."

    na "Emily nods."

    cf "Heh, smart girl."
    cf "Well that’s because everybody has a unique paradise."
    cf "One tailored just for them."
    cf "It’s a world crafted solely from your wants and desires."
    cf "Mine would match me, and yours would match you."

    e "So we’ll be apart?"

    cf "Not necessarily, if you want me there, I’ll be there. Our two paradises overlap, you’ll just exist in your plane of reality and I’ll exist in mine."

    e "What does that mean?"

    cf "Well, say you want an apple pie, and I want a key lime one."

    e "I hate apples!"

    cf "Well then say you want a berry pie."

    na "He waits."

    cf "No objections?"

    na "Emily shakes her head."

    cf "Well then, if you want berry pie, and I want key lime pie, we’d only get one pie. But, we’d see, feel, smell –"

    e "And taste."

    cf "And taste, our own individual pies."

    na "Father holds up the drawing he was working on, it’s a picture of him and Emily eating their respective pies out of the same container."
    na "The whole drawing is encapsulated in what seems to be a rune drawn around the perimeter."

    cf "It’s the same object, but different experiences."

    na "Emily’s eyes are sparkling, but not because of tears anymore."

    e "How do we get there?"

    cf "That, I can tell you when you’re older. But for now, I’ll tell you the best part:"

    na "Father leans in, as if telling Emily a secret."

    cf "You can bring all the people you love there."

    na "Emily gasps."

    cf "Pretty great, right?"

    e "I’ll definitely have you in MY Paradise Papa."

    na "Father laughs, charmed."

    cf "And your Mother too right?"

    na "Emily dims."
    na "She looks away."
    na "Father sighs, and readjusts his weight on the bed."

    cf "You know, in my Paradise, your mother is there."
    cf "But I know that she’ll be different."
    cf "All of our problems in this world, they’ll all just fall away."
    cf "That’s why I don’t worry too much about what she says."
    cf "Pretty soon,"

    na "Father tucks the drawing into the corner of a picture frame on Emily’s night stand."

    cf "It won’t matter."

    na "Emily is still silent."

    cf "I really do love her, you know."
    cf "And I know that she loves you."
    cf "You don’t have to be afraid of her, okay?"
    cf "She’s just like that."

    na "Emily nods."

    cf "Good girl."

    na "Father pats Emily’s head."
    na "His hand is warm."
    na "Emily leans into her Father’s side."

    jump the_orchestra

label emily_flashback_3:
    play music "emily_song.mp3"
    scene e_flashback_6
    e "What do you mean?"

    na "Rose winces."

    ro "Please, don’t make me repeat myself."

    e "We’re– Rose you said you would never – Oh my god. Did they find out?"

    ro "I... told them."

    e "Why would you do that!?"

    ro "They deserved to know. Keeping it private was dishonest."

    e "You said this would never happen."

    na "It is clear her words are only able to make it out because they are well rehearsed:"

    ro "I’m sorry I can’t keep my promise to you."

    na "..."

    ro "I... care about you Emily, I really do. But as long as I don’t act on it – maybe I can still salvage the situation."

    e "Are they making you do this?"

    ro "It’s just better if we go our separate ways. I don’t hate you, I could never hate you, but you’re not...good for me."

    e "..."

    ro "..."

    e "So I’m not “good?”"

    ro "...I didn’t say that."

    e "No you didn’t, but what you also didn’t say is that you’re a coward. And they’re both true aren’t they?"

    ro "I’m sorry."

    e "If you wanted to leave me, just say you’re leaving me. You don’t have to make something up - pretend that it’s in the name of god or whatever."

    ro "I love you! Em you’ve got to believe me I love yo–"

    e "What’s so bad about this? I know {i}I’m{/i} not worth it, but what’s so bad about this?"

    ro "It’s a sin."

    e "Oh! Then you must be {i}selective{/i} with your sins!"

    ro "...I deserve that."

    e "Why am I still not swearing in front of you? You fucking lied."

    ro "Please don’t make this hard. I didn’t want to hurt you."

    e "Then don’t leave!"
    e "Don’t leave, Rose."
    e "If you love me, why do you need to go?"

    ro "Do you love me?"

    e "What are you, a masochist? Why would I tell you now?"

    ro "I wanted to know."

    e "Oh like a fucking parting gift?"

    ro "... don’t know. I’m sorry."

    e "Yeah, I’m sure you are."

    e "..."

    ro "..."

    e "You’re a shitty Christian Rose."

    ro "That’s what I’m trying to fix."

    e "..."

    ro "..."

    na "Emily swings her backpack over her shoulder."

    e "I’ll see you in class."

    na "Emily storms off. Rose tastes blood on her lip."

    jump under_the_chandelier

label ophelias_comedy:
    play music "friend_song.mp3"
    scene dramaroom
    na "After a typical drama club meeting, Andrea yells at a few people before telling everyone to go home and come back the next week."
    na "People linger for a while afterwards, making small talk, and while Emily is distracted by Rei, “Rose” is left on her own."
    show ophelia scared at right, flip
    na "She looks around, and notices a girl whose name she thinks is Ophelia sitting down in a corner away from other people."

    na "She seems scared, very scared. “Rose” stands away from view from her, and listens for a moment."

    show ophelia teary at right, flip
    op "Why why why –"

    na "She whimpers."

    op "They can’t possibly be getting back together, right?"
    op "Not after what happened last time."
    op "God, god I might lose both of them again."
    op "I’ll be alone again."

    show ophelia pain at right, flip
    na "She starts to cry while hyperventilating."

    op "God I’m such a failure."
    op "Why am I like this?"
    op "Why am I so weak?"
    op "I can’t even take care of myself, let alone help Rose."
    op "I can’t do this anymore, I can’t, I can’t –"

    show rose oh boy at center
    fr "“Rose” walks over and kneels in front of Ophelia."

    fr "Are you ok?"

    show ophelia shocked at right, flip
    na "Ophelia looks up, with tears in her eyes, and freezes for a second. She then takes a deep breath, and goes limp, falling to the floor."
    na "“Rose” looks at her for a second, panicked, and quickly picks Ophelia up without a hint of struggle."

    show ophelia wondering at right, flip
    na "Ophelia sighs."

    op "I must be as heavy as a bag of rocks."

    na "“Rose” looks at Ophelia, a bit confused. Ophelia sighs again, louder."

    show ophelia excited at right, flip
    op "Do you just need me? Do you go crazy without my company, my dear Rose?"

    show rose startled at center, flip
    na "“Rose” eyes widen, as her mouth contorts."
    na "After a few seconds, she starts to laugh, at first lightly, and then manically."
    na "Ophelia laughs along with her after a bit."

    show ophelia comforting at right, flip
    op "God, you’re crazy."

    hide rose
    hide ophelia
    na "“Rose” puts Ophelia back on the ground, and Ophelia hugs her. Before “Rose” has a chance to react, Ophelia breaks the hug and runs over to Emily."

    jump ophelias_death

label vomit:
    play music "murder_song.mp3"
    scene vineyard
    show catherine shadow at center
    na "Catherine stands, hunched over near the vineyard."
    na "Her eyes feel wet and her body uncomfortable as she intentionally convulses."
    na "She tries to vomit, over, and over, and over again, but all that comes out is a miniscule amount of spit."
    show catherine worried at center
    na "Her arms and legs are shaking, and after a few minutes, she eventually falls to the ground and begins to cry as she puts her hands over her face."

    na "..."

    show catherine shadow at center
    na "She mouths the word “disgusting” and slams her head against the ground as hard as she can, and goes blissfully unconscious."

    hide catherine
    jump catherine_month_3_aarya

label love_like_you:
    play music "friend_song.mp3"
    scene dramaroom
    show emily curious at right, flip
    show rei hyped at left
    na "After a typical drama club meeting, Andrea yells at a few people before telling everyone to go home and come back the next week."
    na "People linger for a while afterwards, making small talk."
    show ophelia teary at center, flip
    na "Emily and Rei talk for a little bit about nothing, before eventually, Ophelia runs up to the both of them, slightly teary eyed."

    show rei alright at left
    re "Woah, did Andrea yell at you too?"

    show ophelia comforting at center, flip
    na "Ophelia wipes her eyes."

    show ophelia excited at center, flip
    op "Nope! Anyways, you guys wanna do karaoke tonight?"

    show rei hyped at left
    re "Hell yeah, I’m down."

    show ophelia wondering at center, flip
    na "Ophelia looks over at Emily."

    show emily flippant at right, flip
    e "Well, I do have other plans for – to –"

    show rei cmon man at left
    re "Again??"

    show ophelia teary at center, flip
    na "Ophelia starts to tear up again."

    show emily peeved at right, flip
    e "Fine!"

    show ophelia excited at center, flip
    op "Yay! Come on, let's go!"

    hide rei
    hide ophelia
    hide emily
    na "Ophelia grabs Emily by the arm and tries to run out the door."
    na "Emily pulls her back to a brisk walk as they go over to their usual karaoke place."
    na "Rei gets there, and sings “Funkytown” and a few Queen songs."
    na "Ophelia turns to Emily and tells her she wants to sing “Something Stupid” with her."

    na "Emily sings with competence and without passion, while Ophelia sings with passion and without competence."
    na "Emily looks over at Ophelia and thinks she’s clearly sick, considering how many of the lines she’s messing up."
    show emily satisfied at left
    show ophelia dissapointed at right, flip
    na "At the end, Ophelia looks over at Emily, and apologizes about a dozen times as Emily reassures Ophelia."
    show ophelia comforting at right, flip
    na "Ophelia gives Emily a hug."

    show ophelia dissapointed at right, flip
    op "God I’m so sorry Em."

    show emily genuine at left
    e "Don’t worry about it."

    show ophelia excited at right, flip
    na "Ophelia smiles a little too widely at Emily. They enjoy the rest of the night."

    hide emily
    hide ophelia
    jump ophelias_death

label love_letter:
    play music "emily_song.mp3"
    scene e_bedroom
    na "Emily goes back to her dorm, well past the point most people would be awake, but early enough to where there’s still a few other college students getting ready for bed."
    play audio "door_creaking.mp3"
    na "She opens her door to find a letter lying on the ground, clearly having been slipped underneath her door at some point recently."
    na "She picks it up and lays down on her bed to read it."
    na "Written on the back of the envelope is just “To Emily”."

    show emily curious at center
    na "A sinking feeling fills Emily’s chest as she opens up the letter."
    na "She can’t quite pinpoint the handwriting, although it seems quite clean."
    na "After a few lines it’s clear that it’s from Ophelia, as she rambles on about mutual experiences they’ve had together."
    show emily gross at center
    na "The letter is very emotionally charged, with a mix of desperation and insanity that makes Emily feel even more sick as she goes down the lines."
    na "She gets down to the end of the letter and reads:"

    show emily flippant at center
    na "“Emily, I love you more than I’ve loved anyone else in my entire life. You are the only person I’ve ever met who I felt was truly beautiful.”"

    show emily peeved at center
    na "Emily crumples the paper up, before ripping it into pieces and throwing it into her trash can. She lays in bed for a long while, thinking, before finally falling to sleep."

    hide emily
    show emily flippant at left
    show catherine content at right
    na "After an almost restless night, she wakes up."
    na "After going through her normal daily routine, she goes to the mansion again, and meets with Catherine."
    scene potraits
    na "They have dinner and make their usual small talk."

    e "I got a letter yesterday."

    show catherine bashful at right
    na "Catherine looks intrigued."

    c "From whom? Your mother?"

    show emily flippant at left
    e "No, Ophelia."

    show catherine content at right
    c "Ah, I see."

    show emily desperate at left
    e "It was, well, I think it was a love letter."

    show catherine frown at right
    c "Catherine frowns."

    show emily gross at left
    e "God, I wish I had never seen that."

    show catherine worried at right
    c "...Did you love her as well?"

    show emily hurt at left
    e "No, I just –"

    na "Emily balls her hands up in fists and scrunches up her face."

    e "I don’t know, honestly. I don’t know why it makes me feel like shit."

    show catherine content at right
    na "Catherine looks at Emily for a moment, before walking over and grabbing her arm. Emily looks up at Catherine."

    c "At least she’ll be in paradise. She’ll get to be happy."

    show emily satisfied at left
    na "Emily relaxes, and gives a pained smile to Catherine."

    hide emily
    hide catherine
    jump emily_month_3_aarya

label ophelias_death:
    play music "murder_song.mp3"
    scene dramaroom
    show ophelia wondering at right, flip
    show rose listening at left, flip
    na "After another drama club meeting, Ophelia pulls “Rose” aside."

    op "Hey Rose."

    na "“Rose” looks at Ophelia."

    op "Can you come with me for a bit? I think we should talk."

    na "Ophelia leads “Rose” by the arm outside. They start to walk, vaguely in the direction of the mansion."
    scene school
    play audio "walk_grass.mp3"

    show ophelia comforting at right, flip
    op "Rose, how have things been for you recently?"

    fr "Things have been well, I’d say."

    show ophelia dissapointed at right, flip
    na "Ophelia frowns with concern."

    op "Are you sure? You haven’t really, well you haven’t really seemed like yourself lately."

    fr "Maybe, I guess."

    na "“Rose” laughs a little."

    show ophelia wondering at right, flip
    op "Is it Emily?"

    na "“Rose” seems surprised."

    show ophelia dissapointed at right, flip
    op "I’m really shocked that you two seem to be getting back together. After, well after all that happened before, I really thought you two would have been split up for good."

    fr "I suppose so."

    na "The two walk in silence for a minute."

    scene vineyard
    show ophelia wondering at right, flip
    op "Do you remember that time in the gym?"

    show rose worried at left, flip
    na "“Rose” puts on a pained expression."

    fr "Not – not really, no."

    show ophelia dissapointed at right, flip
    na "Ophelia seems concerned."

    op "Not even the part about Emily? It was right before you broke up with her, remember?"

    fr "I, yes I think I remember now."

    show ophelia passionate at right, flip
    op "What did you say about her?"

    na "Ophelia stops walking and stares hard at “Rose”. “Rose” seems surprised, and after a bit of stuttering, gives up saying anything at all."

    op "God, you know before I thought you had changed a lot, but you don’t even seem like Rose at this point!"
    op "It’s like you're a whole different person."
    op "What the hell happened that caused you to forget everything?"

    hide rose
    show catherine startled at left, flip
    na "“Rose” starts to panic, as her heart rate rises."
    na "Before she has time to react, she accidently trips over a vine in the path as she starts to walk again, and for a split second turns back into Catherine."
    na "Ophelia goes up to help her, and stares Catherine in the face."

    show ophelia shocked at right, flip
    op "What –"

    na "Ophelia looks horrified, and backs up a few steps."
    show catherine shadow at center, flip
    na "She turns around and starts to scream, and before she can take another step, Catherine has clawed her neck."
    play audio "bones_breaking.mp3"
    hide ophelia
    play audio "body_fall.mp3"
    na "She gurgles a bit before falling to the ground, her eyes still wide."

    show emily gross at right, flip
    na "After a minute, Emily appears from behind a tree to see Ophelia’s lifeless body on the ground."
    play audio "knife_dirt.mp3"
    na "Emily buries the blood on the ground in surrounding dirt."
    show catherine stoic at left, flip
    na "Catherine’s face is emotionless as she picks up Ophelia’s body and begins to follow Emily towards the mansion."

    hide emily
    hide catherine
    jump ritual_two

label ritual_two:
    play music "ritual_song.mp3"
    scene vineyard
    show emily curious at left
    show catherine content at right
    e "Four items? We can only fit three."

    c "I thought we might want to have options."

    show emily flippant at left
    e "Options, what for?"

    show catherine bashful at right
    c "People are...very complicated. I think it would be more beneficial to really consider all their facets."

    show emily satisfied at left
    e "How are we going to decide? Rock paper scissors?"

    show catherine content at right
    c "That might be a valuable system to implant."

    show emily peeved at left
    e "Oh, nevermind, there’s a pretty clear ugly duckling here."

    hide emily
    hide catherine

    screen ritual_two_screen(res):
        add "ritual_interface"

        draggroup:
            if "Swiss Army Knife" not in res:
                drag:
                    drag_name "Swiss Army Knife"
                    droppable False
                    dragged totem_dragged
                    xpos 0 ypos 0
                    add "@4/Swiss_Army_Knife.png"

            if "Poto Mask" not in res:
                drag:
                    drag_name "Poto Mask"
                    droppable False
                    dragged totem_dragged
                    xpos 1400 ypos 0
                    add "@4/POTO_Mask.png"

            if "Friends Drawing" not in res:
                drag:
                    drag_name "Friends Drawing"
                    droppable False
                    dragged totem_dragged
                    xpos 0 ypos 600
                    add "@4/Drawing_of_Friends.png"

            if "Plush Duck" not in res:
                drag:
                    drag_name "Plush Duck"
                    droppable False
                    dragged totem_dragged
                    xpos 1400 ypos 600
                    add "@4/Small_Duck_Plushie.png"

    $ res = []

    while len(res) < 3:
        call screen ritual_two_screen(res)
        
        if _return != None:
            
            if _return == "Swiss Army Knife":
                e "Ophelia was always so eager to lend this to us. She is always right there when I need her."

                c "Ophelia’s urge to assist other people seems to hurt her a lot more than it aids her."

                menu:
                    "Add Ophelia's Swiss Army Knife?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Poto Mask":
                e "The mask from her 15th birthday party. Yeah...I don’t think we’re going to need that."

                c "Ophelia has a fire lit under her. It would be a shame for her to lose such a trait."

                menu:
                    "Add Ophelia's Poto Mask?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Friends Drawing":
                e "She’s always complimenting me. It’s almost creepy...but also nice."

                c "I’d like to lighten the load for her a bit, have her see her good qualities instead of others’ for once."

                menu:
                    "Add Ophelia's Drawing of Her Friends?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Plush Duck":
                e "Ophelia can really smother us sometimes, I don’t see the point in keeping that trait."

                c "If nothing else, Ophelia deeply cares for others. This seems inextricable from who she is."

                menu:
                    "Add Ophelia's Small Duck Plushie?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            else:
                pass

    $ _emily_cnt = sum(1 for i in res if i in ["Swiss Army Knife", "Friends Drawing"])
    $ ritual_card_2 = "emily" if _emily_cnt >= 2 else "catherine"
    $ ritual_cards.append(ritual_card_2)
    if ritual_card_2 == "emily":
        $ ritual += 1
    scene black
    stop music fadeout 1.0
    play audio "ritual_complete.mp3"
    if ritual_card_2 == "emily":
        show success_emily as success_card_1 at card_center
    else:
        show success_catherine as success_card_1 at card_center
    $ renpy.pause(1.5, hard=True)
    pause

    jump licky_licky

label licky_licky:
    play music "tecc.mp3"
    scene vineyard
    show emily satisfied at left
    show catherine worried at right
    na "Catherine and Emily sit in the vineyard, as Emily buries Ophelia’s body in dirt."
    na "It’s well into the night."
    na "Catherine looks uneasy."

    e "You did a good job."

    show catherine shadow at right
    na "Catherine doesn’t respond. She looks away from Emily."

    show emily flippant at left
    e "You need to be more careful about revealing yourself though."
    e "I don’t want it to happen to someone who we don’t want to sacrifice."
    e "No reason to kill more people than necessary."

    show catherine bashful at right
    play audio "knife_dirt.mp3"
    na "Emily holds the shovel out to Catherine, and Catherine finishes off the burial."
    show catherine startled at right
    na "At the end, Catherine looks over to see a little red spot on Emily’s collarbone."
    na "Before either has time to react, Catherine goes over and licks the blood off of Emily."
    show emily seductive at left
    na "Catherine’s eyes widen while Emily smiles."

    hide emily
    hide catherine
    if character == 0:
        jump vomit
    else:
        jump love_letter

label catherine_month_3_aarya:
    play music "friend_song.mp3"
    scene school
    show aarya sigh at right
    show rose listening at left, flip
    aa "Rose, wait. Have you talked to Ophelia recently?"

    fr "No, I haven’t heard anything."

    show aarya worried at right
    aa "God, Where is she?"
    aa "What happened to her?"
    aa "It’s been a couple weeks and nobody I’ve talked to has seen her."
    aa "I really hope she’s okay."

    fr "I’m sure that she’s fine."

    show aarya sigh at right
    aa "I hope so... but this isn’t like her."
    aa "Even her parents don’t even know what she’s doing."
    aa "They keep asking me for any news on her."

    show aarya worried at right
    na "Aarya’s breathing gets heavier."

    aa "Her parents want me to come to dinner with them, and I..."
    aa "I don’t- I can’t break the news that I have no idea where she is."
    aa "I’ve– I’ve tried looking for Ophelia everywhere, I tried her dorm, her classes."
    aa "I’m scared, y’know?"

    show rose worried at left, flip
    fr "Yeah, it is concerning."

    show aarya sigh at right
    na "Aarya puts her hands in her face. She sighs, and then looks up to “Rose” again."

    show aarya sure at right
    aa "Can you come talk with Ophelia’s parents with me?"

    fr "What for?"

    show aarya sigh at right
    aa "Y’know, just, to explain things. I don’t know, I just think it’d be better if it wasn’t just me."

    na "“Rose” sits for a second."

    fr "Alright, I suppose I can come."

    show aarya full at right
    aa "Thanks, Rose."

    na "Aarya hugs “Rose”."

    hide aarya
    jump occult_rush_vampirefunk

label emily_month_3_aarya:
    play music "friend_song.mp3"
    scene school
    show aarya sure at right
    show emily flippant at left
    aa "Emily, wait! Can I talk to you, alone?"

    na "Aarya stops Emily after class and takes her aside."

    show aarya incredulous at right
    aa "What’s going on?"

    show emily curious at left
    e "What?"

    show aarya sure at right
    aa "Don’t “what” me, you haven’t been going to classes, you haven’t been doing your homework, and you don’t practice for drama club."
    aa "Ok well you don’t do that anyways but you know what I mean."

    show aarya sigh at right
    na "Aarya sighs, her tone softer."

    aa "I haven’t seen you go to any of your classes in nearly a month. There’s no way you aren’t failing at this point."

    show emily peeved at left
    na "Emily sighs, exasperated."

    show emily flippant at left
    e "I’ve... just been busy, Aarya."

    show aarya full at right
    aa "With what?"
    aa "It must not be pretty if you’ve been struggling this much."
    aa "Look, whatever it is, you can talk to me."
    aa "Whatever’s happening, I’m here if you need it."

    show emily satisfied at left
    e "Thanks Aarya, I’ve just been dealing with some, uh, personal issues. Just, don’t worry about it, ok?"

    show aarya sigh at right
    na "Aarya sighs."

    aa "Are you sure you’re ok?"

    show emily flippant at left
    e "I’m, I’m fine."

    show aarya sure at right
    aa "Just, talk to me, ok?"

    show emily genuine at left
    e "Okay."

    hide emily
    hide aarya
    na "Emily walks off."

    jump emily_aarya_alone_time

label emily_aarya_alone_time:
    play music "friend_song.mp3"
    scene dramaroom
    show aarya sigh at right
    show emily curious at left
    aa "Emily, I don’t know Rose as well as you, but... she’s definitely acting differently."

    show emily flippant at left
    e "Really? I barely noticed it, what makes you think that she’s been different?"

    show aarya sure at right
    aa "No, she’s definitely different."
    aa "Rose used to be very happy and energetic and extroverted."
    aa "Like. a golden retriever, and now look at her."
    aa "She’s... quiet."
    aa "She’s like a completely different person."

    show emily satisfied at left
    e "Yeah, but like people change all the time, I mean look at Rei, she used to be a mama’s perfect little girl."
    e "Maybe Rose is going through something similar."
    e "Do you not like the change?"

    na "Emily stops painting the red grapes and instead starts painting her nails with the red paint while Aarya keeps making props."

    show aarya full at right
    aa "I don’t dislike it."
    aa "I actually like it a lot."
    aa "She seems more... polite."
    aa "More approachable."
    aa "I–"

    show aarya incredulous at right
    na "Aarya sees it."

    show aarya sure at right
    aa "Emily, we have a month until the play, stop messing around!"

    na "Aarya drops a pile of her completed props onto Emily’s lap."

    show aarya incredulous at right
    aa "I mean, take this for example."
    aa "The old Rose would have painted her nails with you, and the new one would have told you off."
    aa "She’s more responsible."
    aa "She kinda reminds me of myself."
    aa "I gotta talk to her more."

    show emily flippant at left
    e "Aarya, you’ve got a lot of school work and this play coming up, are you sure you have the time to talk to her?"
    e "I mean what about your future?"
    e "Look, we've got a lot of work to be doing."

    show aarya sigh at right
    na "Emily hands Aarya some paint, brushes and half of the unfinished props, Aarya groans."

    aa "This is your work... Fine, I’ll pick up your slack."

    hide emily
    hide aarya
    jump occult_rush_vampirefunk

label occult_rush_vampirefunk:
    play music "occult_song.mp3"
    scene dramaroom
    hide rose
    show emily curious at left
    show aarya sigh at right
    show rei hyped at center
    na "Another day after drama club, the occult club (with Rose, and without Ophelia) meets up again."
    na "The girls rush into the room, dim the lights, while Emily sets the candle and the rest sit in a circle."

    show rei hyped at center
    re "I know what we should do today!"

    show aarya sure at right
    aa "Rei! You have to let Emily do the chant first."

    show rei cmon man at center
    re "Ugh, I’ve been planning this thingy for months! Besides we all know the chant at this point, We are gathered here–"

    show emily scolding at left
    na "Emily interrupts, causing Rei to promptly quiet herself."

    show emily curious at left
    e "We are gathered here today, in the dying heart of our school, to convene in the strange and mysterious."
    e "The world is full of non-believers, so small spaces must be made, to host those that understand."
    e "The Occult welcomes you, and it knows you by name."

    show rei alright at center
    na "Rei raises her hand."

    re "May I present my thing now?"

    show emily peeved at left
    na "Emily sighs."

    e "As long as it’s occult related."

    show rei oops at center
    re "Uhhh, kinda?"

    show aarya incredulous at right
    aa "Rei! What’s the point of it being in occult club if you’re not going to do occult things?"

    show rei alright at center
    re "LOOK it’s kinda related, okay?"
    re "You guys know about the new gym right?"
    re "So like, I was curious about what they did with the old gym."

    show emily curious at left
    e "Nothing? They just don’t use it any more."

    show rei hyped at center
    re "I know that now!"
    re "But like I went over to check it out, and gotta say, it's pretty spooky."
    re "It’s got cobwebs, crappy lighting, and a creepy sound that made me leave the place."
    re "ANYWAYS–"

    fr "Are we going to explore it?"

    show rei alright at center
    re "Nah, even better."

    na "Rei dumps her backpack and 3 pairs of roller skates drop out."

    show rei hyped at center
    re "So like the place I work at happened to have a sale on these and I was like “What a steal!” Anyways–"

    show aarya sigh at right
    na "Aarya sighs."

    show aarya incredulous at right
    aa "Did you just want to rollerskate?"

    show rei alright at center
    re "Well yeah, kinda."
    re "Look, I don’t wanna go to a rollerskate rink by myself, or like, in general."
    re "I mean the cost, the rentals, the people, and–"

    show emily flippant at left
    e "Is anyone opposed to rollerskating in the old gym for today’s meeting?"

    show aarya sure at right
    aa "I am."

    show rei hyped at center
    re "You don’t count, Rose? Em?"

    show aarya sigh at right
    aa "HEY! That’s–"

    show rei alright at center
    re "EM! You in?"

    show emily satisfied at left
    e "Sure, sounds like fun."

    hide aarya
    show rose 
    fr "I haven’t roller skated before."

    show emily flippant at left
    e "Rose, it’ll be fine, I’ve never done it before either."

    show rei hyped at center
    re "‘Xactly. Sorry Aarya, but that's 3 outta 4, I win."

    hide emily
    hide aarya
    hide rei
    scene gym
    na "The club heads into the gym, Rei hands Emily and Aarya a pair of roller skates each before walking up to “Rose”."

    show rei alright at left
    re "Hey Rose."

    na "Rei hands “Rose” a pair of roller skates."

    show rei oops at left
    re "Look, the size is probably not going to fit right. Originally these skates were going to be Ophelia’s but... she’s not here I guess."

    hide rei
    na "“Rose” puts on the shoes and awkwardly glides across the floor like a new born fawn as Emily assuredly glides towards her."

    show emily curious at left
    e "Rose, you good?"

    fr "I’m fine."

    show emily peeved at left
    play audio "body_fall.mp3"
    na "“Rose” tries to straighten up and walk straight before immediately slipping and falling forwards onto the gym floor with a loud slam. Emily glides over and sighs."

    show emily flippant at left
    e "Let’s get you out of those shoes."

    na "Emily pulls “Rose” off of the gym floor."

    show emily curious at left
    e "I thought you’d be better at this."

    fr "..."

    show emily peeved at left
    show rose worried at center
    e "What’s wrong?"
    e "Are you not feeling well?"
    e "Do you need more blood?"

    fr "N-no Emily it’s... is this ... right? Should we be doing this?"

    show emily scolding at left
    e "Ca- Rose, what are you talking about? Is rollerskating that hard for you?"

    fr "No that’s not it, are you sure we should be doing this ritual?"

    show emily peeved at left
    na "Emily looks at “Rose” and contorts her face."

    show emily desperate at left
    e "What?"
    e "Do you not want us to be together?"
    e "Do you not want us to be happy?"

    fr "No Emily, I do! I just, I just don’t know if it’s the right thing to do"

    play music "intimate_song.mp3"

    show emily genuine at left
    na "Emily cups Rose’s face and gently presses Roses’s forehead against her own."

    e "It’s alright Catherine, You trust me right?"

    show emily mischievous at left
    na "“Rose” nods slowly, Emily takes a look around, then tangles her fingers into Rose's hair."

    e "So take a bite, Catherine."

    hide rose
    show catherine startled at center
    na "“Rose” widens her eyes, then shifts back into Catherine, first in her hair, then her skin. The bones in her face slowly shift and morph back her original form."

    show catherine worried at center
    c "Are you sure about this? They’re still around."

    show emily peeved at left
    na "Emily pulls Catherine closer and mutters."

    e "Just do it."

    show catherine worried at center
    na "Catherine’s breath grazes over Emily’s collarbone and she slowly opens her mouth, Emily grips Catherine’s shoulder tight, till her knuckles turn white."

    vo "Emily?"

    play music "murder_song.mp3"

    show emily desperate at left
    show aarya woah at right
    na "Emily’s eyes widen in fear as she looks Aarya dead in her eyes."

    show emily scolding at left
    e "C-Catherine, Do it! Stop her!"

    aa "E–"

    show catherine shadow at center, flip
    hide aarya
    show aarya dead at right
    play audio "bones_breaking.mp3"
    na "A cold hand quickly encircles Aarya’s neck and gives it a quick strong squeeze, quickly crushing Aarya’s windpipe and larynx."
    na "Aarya’s eyes widen in shock as she tries to scream in pain, but all that comes of it is bloody bubbles rising from the cavity in her neck."
    na "Catherine winces, then whispers."

    c "I’m sorry."

    show catherine shadow at right
    play audio "body_fall.mp3"
    na "Catherine’s other hand plunges into Aarya’s heart and crushes it, killing the girl instantly, the light quickly leaving her eyes as she falls on Catherine’s shoulders."
    show emily gross at left
    na "Emily quickly covers her skin and wraps her arms around herself as if to protect herself."
    na "Both of them are deeply breathing, shocked and stunned."

    show catherine worried at center
    c "Emily, I–"

    show emily desperate at left
    e "You can drink her blood, right?"
    e "Go do that..."
    e "Turn into her... tell Rei that me and Rose are going  home."

    show catherine worried at center
    c "Emily–"

    show emily scolding at left
    e "Just do it."

    hide catherine
    show aarya catherine at right
    na "Catherine drinks from Aarya’s neck, sucking up only a few drops."
    na "She pulls away disgusted, her face contorting before changing to Aarya’s. “Aarya” slowly lays Aarya to the floor, and steps out into the gym."

    hide emily
    show aarya catherine at right
    show rei alright at left
    fake_aarya "Hey Rei... Emily and Rose are going home."

    show rei cmon man at left
    na "Rei frowns, dejected."

    show rei oops at left
    re "Oh, alright."
    re "They didn’t say nothing to me."
    re "Do you still wanna skate or are you also..."

    show aarya catherine at right
    fake_aarya "Rei... I’ve just... got a lot on my mind right now."

    show rei cmon man at left
    re "Yeah, no I get it..."
    re "I do hope Ophelia shows up."
    re "I’ll... go."

    hide rei
    na "Rei slowly skates off."

    show aarya worried at center
    na "“Aarya” slowly takes a step away from the gym into where Aarya was."
    na "Her breathing quickens to a rapid pace, as she sees blood staining the floor and treadmarks of a cart leading towards the back exit."
    na "“Aarya” collapses to her knees in the pool of blood, hot tears streaming down her face."
    na "She claws at her face, leaving bloody streaks in her cheeks as she hyperventilates on the floor."

    hide aarya
    jump ritual_three

label ritual_three:
    play music "ritual_song.mp3"
    scene vineyard
    show emily flippant at left
    show catherine shadow at right
    e "So the four options is going to be a regular thing now?"

    c "..."

    show emily satisfied at left
    e "Alright, you know the drill. Let’s begin."

    show catherine worried at right
    c "Emily...can we talk about what happened?"

    show emily curious at left
    e "What do you mean?"

    show catherine shadow at right
    c "In the bathroom..."

    show emily flippant at left
    e "Oh, right. You did a good job Catherine, I know it wasn’t the most ideal situation, but you trusted me."

    show catherine frown at right
    c "...Of course."

    hide emily
    hide catherine

    screen ritual_three_screen(res):
        add "ritual_interface"

        draggroup:
            if "Glasses" not in res:
                drag:
                    drag_name "Glasses"
                    droppable False
                    dragged totem_dragged
                    xpos 0 ypos 0
                    add "@4/Her_Glasses.png"

            if "Bracelets" not in res:
                drag:
                    drag_name "Bracelets"
                    droppable False
                    dragged totem_dragged
                    xpos 1400 ypos 0
                    add "@4/Bracelets.png"

            if "Camera" not in res:
                drag:
                    drag_name "Camera"
                    droppable False
                    dragged totem_dragged
                    xpos 0 ypos 600
                    add "@4/Camera.png"

            if "Stress Ball" not in res:
                drag:
                    drag_name "Stress Ball"
                    droppable False
                    dragged totem_dragged
                    xpos 1400 ypos 600
                    add "@4/Stress_Ball.png"

    $ res = []

    while len(res) < 3:
        call screen ritual_three_screen(res)
        
        if _return != None:
            
            if _return == "Glasses":
                e "Aarya always pushes so hard, we need someone with her work ethic."

                c "Aarya deserves a break in the beyond."

                menu:
                    "Add Aarya's Glasses?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Bracelets":
                e "Aarya is someone we can count on. I wish I could ask her how to better handle dead bodies."

                c "It’s time for Aarya to finally get some rest."

                menu:
                    "Add Aarya's Bracelets?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Camera":
                e "Aarya can be a real drag when she’s going on about the future."

                c  "I don’t want to separate Aarya from her goals...I’m sure she’ll find a way to achieve them once we’re there."

                menu:
                    "Add Aarya's Camera?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Stress Ball":
                e "Talk about a mood killer. She takes everything so seriously."

                c "The way she sees things is always so practical, she makes it easy for people to get out of their heads."

                menu:
                    "Add Aarya's Stress Ball?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            else:
                pass

    $ _emily_cnt = sum(1 for i in res if i in ["Glasses", "Bracelets"])
    $ ritual_card_3 = "emily" if _emily_cnt >= 2 else "catherine"
    $ ritual_cards.append(ritual_card_3)
    if ritual_card_3 == "emily":
        $ ritual += 1
    $ _c1 = ritual_cards[-2] if len(ritual_cards) >= 2 else "emily"
    scene black
    stop music fadeout 1.0
    play audio "ritual_complete.mp3"
    if _c1 == "emily":
        show success_emily as success_card_1 at card_left2
    else:
        show success_catherine as success_card_1 at card_left2
    if ritual_card_3 == "emily":
        show success_emily as success_card_2 at card_right2
    else:
        show success_catherine as success_card_2 at card_right2
    $ renpy.pause(1.5, hard=True)
    pause

    jump lock_in_em

label lock_in_em:
    play music "drama_song.mp3"
    scene dramaroom
    show andrea serious at right
    an "Alright that should be enough for today, a bit early but we’ve done enough practice for today. All of you are free to go."

    show emily flippant at left
    na "Everyone storms out of the room. Andrea stops Emily."

    show andrea ticked at right
    an "Except for you."

    show andrea okay at right
    na "Andrea pulls Emily back into the classroom and sighs."

    show andrea serious at right
    an "Emily, I need you to start practicing your line."
    an "And I don’t mean improv the character, I mean read the lines."
    an "The deadline for the play is next month and honestly?"
    an "With how you’ve been?"
    an "Considering you’re the main lead and you don’t know your lines, I don’t think we’ll be able to do this play at all."

    show andrea ticked at right
    an "But."
    an "I am giving you a warning and time, get your shit together, start practicing your lines and if your performance at the final rehearsal is good enough,"
    an "I won’t mention to everyone how you almost became the reason why we weren’t able to perform."
    an "But if you come into the rehearsal and you mess up a single line, I swear to god, I will chew you out in front of everyone and cancel the play."

    an "Got that?"

    show andrea serious at right
    an "Look, I don’t want to do that, so practice–"

    show emily peeved at left
    e "I got it, don’t worry. I won’t fuck up my lines."\

    show andrea okay at right
    na "Andrea sighs."

    an "Well if you got it then we have nothing else to talk about, you are free to go."

    hide andrea
    show rose worried at right
    na "Emily steps outside of the room and sees Rose, anxiously waiting."

    fr "You feeling al–"

    show emily flippant at left
    e "Never been better! I’ll talk with you later."

    fr "But I heard Andrea–"

    show emily scolding at left
    e "I’ll."
    e "Talk."
    e "To."
    e "You."
    e "Later."

    hide emily
    hide rose
    na "..."

    scene potraits
    show emily peeved at left
    show catherine content at right
    na "Later, while eating dinner."

    show emily scolding at left
    e "What a dictator!"
    e "Always going on and on, critiquing others and yelling at others to dedicate their lives!"
    e "I’m sorry, you have no life and spend half of your free time working on this play and the other half YELLING AT US!"
    e "On and don’t get me started on this play!"
    e "She acts like she has some grand master plan, and yet she barely explains it to anyone!"

    e "And all we get is “You’re doing this wrong, now you’re doing this wrong!” Well what am I supposed to be doing?"
    e "And it’s not like we can critique her either!"
    e "She knows “best”!"
    e "It’s her play, and we’re all obedient little puppets all following her directions blindly while she claims to be doing Every Single ONE OF HER LINES PERFECTLY!"
    e "She’s a horrible self righteous narcissist!"

    e "You’ve heard her talk to us!"
    e "You’ve listened in on our rehearsals and our practice time!"
    e "Sure I might not practice as much as her Holiness demands, but her standards and requirements are horrible and controlling!"
    e "You’ve experienced it second hand right?!"

    show catherine worried at right
    na "Catherine bites her tongue."

    c "...Sure."

    show emily peeved at left
    na "Emily frowns."

    e "Sure?"
    e "You think?"
    e "After all the time you’ve been with me and around her, you think she’s horrible? ...She’s influencing you, isn’t she?"
    e "Grow a backbone and tell her off, I don’t need her opinions and ideas corrupting you too."

    hide emily
    hide catherine
    jump cast_party

label cast_party:
    play music "party_song.mp3"
    scene dramaroom
    show andrea pride at center
    na "Emily and Rose sit down as the drama club holds their party in the classroom to celebrate the month of the play and the final month of the semester."
    na "The lights dim and Andrea walks to the front of the stage."

    show andrea serious at center
    an "Alright everyone, settle down."
    an "We’re now in the final month of the school semester."
    an "I genuinely didn’t know if we would be ready by the end of the semester, but I’m glad to say we made it."
    an "I wanted to have this little party as a little break before Finals season is upon us, and the date for the play has been confirmed for the end of this month."

    show andrea okay at center
    an "Now there’s some hiccups with the cast members, specifically Ophelia not being here for all of last month, and I don’t know if she’ll show up this month or if she’ll even be ready."
    an "We’ll probably need to exclude her lines from the play."
    an "Let’s go over everyone’s roles, starting with the technicians."

    na "Everyone claps."

    show andrea pride at center
    an "Mac and Ash, while you will not be seen in the play, you probably have the most impact on the performance of the play."
    an "You guys have been spending the last couple months setting the stage for us to perform, we would not be here without you guys."
    an "Thank you."

    show andrea snark at center
    an "Rei Tran, thank you for showing up to a meeting, it must have been difficult. Thank you for being the Father for the play, and please stay in character."

    show andrea pride at center
    an "Emily, the main lead, as Catherine Lyon."
    an "I can’t wait for your performance on stage, assuming you practiced your lines like I told you to instead of improvising."
    an "I know your performance will be something the audience will remember fondly of and will remember weeks from now."

    show andrea okay at center
    an "Aarya’s not here, but I do expect her to be here for the play."
    an "The play wouldn’t be the same without her lively and dramatic voice, intricately narrating the play."
    an "I don’t think any one else could do the role justice."

    show andrea pride at center
    an "And finally, Me!"

    an "The play writer, the main antagonist, the director, the organizer, the staff manager, the costume artist."
    an "I’m glad I had every one of you here with me, and despite how much I try, I can’t perform a play all by myself."
    an "Alright go have fun and mingle."

    hide andrea
    na "The lights turn on and everyone stands up and wanders around the room, Rei bee lines to the food table."

    if character == 0:
        jump mac_month_four
    else:
        jump glass_closet_opens

label mac_month_four:
    play music "party_song.mp3"
    scene dramaroom
    show rose listening at right
    show mac tired at left
    mac "Hey Rose, can I talk to you for a second?"

    fr "Hm? Oh, well... yes?"

    mac "Do you want to step outside?"

    fr "Alright."

    play audio "door_open.mp3"
    scene stage
    show mac tired at left
    show rose listening at right
    na "Mac and “Rose” step into the hallway. Mac looks around, ensuring that no one is coming."

    mac "The music should be loud enough."

    fr "Is something wrong?"

    mac "What?"
    mac "No!"
    mac "Everything is fine, I just uh...wanted to talk to you about something."

    fr "Alright."

    show mac fear at left
    mac "Okay, so..this is – uh– we wanted to – god I am not good with words."
    mac "Look, uh."
    mac "This was Ash’s idea."
    mac "He said since we’re both shy we’d get along better, but I don’t really get along with anyone."
    mac "Except him."
    mac "With Ash the world feels more...accessible."
    mac "He’s my bridge to everything, but honestly, I don’t really need to go anywhere else."
    mac "I just need him."

    na "“Rose” waits patiently for the flustered Mac to continue."

    mac "Look, I – oh screw it – I love him."

    fr "You... love him?"

    na "Mac is completely red, he tugs at his collar."

    mac "Yeah. Uh...Romantically."

    fr "..."

    mac "It’s not a one sided thing!"
    mac "We’re - We’re actually together."
    mac "Have been for almost two years now."
    show mac tired at left
    mac "What I am trying to say is – when I don’t have Ash to talk to...it’s like I have no one else in the world."
    mac "We know what it’s like to not have anybody that knows...and nobody to get advice from."
    mac "And he– {i}we{/i}, didn’t want you to feel as alone as we were."
    mac "So, talk to us."
    mac "If you want."

    na "..."

    fr "That’s very kind Mac."

    mac "Ha. Yeah."

    na "Mac runs his hands over his face."

    mac "We finally wanted to let know you about us. Basically everyone else in the club knows."

    show rose startled at right
    fr "Everyone?"

    mac "Yeah, expect for you and Emily."

    fr "Emily?"

    mac "Yeah, sorry but everyone can kind of tell there’s something going on between you two."

    show rose worried at right
    fr "Everyone?"

    mac "Yeah...even for two girls you’re really...into each other."

    na "“Rose’s” ears are ringing."
    na "It feels like someone took a sludgehammer to the side of her head."
    na "What if their closeness means people get suspicious, what if they get caught?"
    na "What will Emily think?"
    na "Oh god, what will Emily think of her for messing this up?"

    mac "Rose?"

    fr "I have to go."

    hide rose
    show mac fear at left
    mac "Wait Rose–"

    play audio "door_slam.mp3"
    scene dramaroom
    show mac fear at left
    na "“Rose” is already opening the door to get back into the classroom. She barely is able to keep herself from ripping it off of its hinges."

    mac "Geez..."

    na "“Rose” flings herself back into the classroom, stumbling over herself."

    mac "Rose, wait!"

    na "Suddenly eyes are on Mac for shouting."
    hide mac
    na "He quiets down and retreats into himself. “Rose is panting, hunched over in the middle of the room."
    na "Where is...where’s Emily?"

    an "Rose?"

    na "“Rose” looks up to meet Andrea’s eyes. The look on her face is stern."

    an "Come with me."

    na "“Rose” can do naught but follow."

    jump andrea_month_four

label andrea_month_four:
    play music "party_song_muffled.mp3"
    scene school
    show andrea okay at left, flip
    show rose worried at right
    play audio "door_open.mp3"
    na "The sliding glass door pops open with a swoosh, as Andrea leads them to the terrace. She motions for Rose to step outside, and she obliges."

    an "You Okay?"

    na "“Rose” plops down on the floor, back against the bars of the railing."

    fr "You didn’t need to bring me out here."

    show andrea okay at left, flip
    an "Fresh air typically helps with this kind of thing."

    fr "Not with me."

    an "Okay."

    show andrea snark at left, flip
    na "Andrea lights up a cigarette."
    na "Catherine scrunches up her nose."
    na "Andrea smiles."

    an "I thought you said fresh air didn’t help."

    fr "It’s preferable to those foul things."

    show andrea okay at left, flip
    an "Do you want me to put it out?"

    fr "...No."

    an "Alright."

    na "She smokes."

    show andrea serious at left, flip
    an "Does this happen to you often?"

    fr "What?"

    an "The freaking out in group settings."
    an "You always look skittish no matter what but, this was worse than usual."
    an "Did Mac rattle you?"

    fr "..."

    show andrea okay at left, flip
    an "Is there a reason you’re so cagey around me? Did I do something?"

    fr "You are a bit of a dictator to Emily."

    show andrea snark at left, flip
    an "I’m sure she sees it that way, and that’s fair, it’s her experience. But am I dictator to you?"

    fr "...I have never found you to be such."

    show andrea pride at left, flip
    an "Great, then maybe you can smooth down your spikes for just one conversation so I can help you feel better."

    fr "I already feel fine."

    show andrea okay at left, flip
    an "Awesome."
    an "Then just talk to me."
    an "If you don’t need my company, I still want yours."

    fr "Why?"

    na "Andrea shrugs."

    show andrea serious at left, flip
    an "I like making people feel included. But I need it sometimes – most of the– all of the time too."

    fr "..."

    show andrea snark at left, flip
    an "Don’t tell anyone I said that."

    fr "Who would I tell?"

    show andrea okay at left, flip
    an "Geez, this is why we gotta get you some friends. Which I’m currently trying to submit my application for by the way."

    fr "You don’t need to apply."

    show andrea snark at left, flip
    an "So we’re already friends?"

    fr "Not exactly."

    show andrea pride at left, flip
    an "Then I’ll keep trying harder."

    fr "..."

    show andrea okay at left, flip
    na "Andrea sighs."

    an "Look, I don't really need anything from you."
    an "People don’t love needy people anyway."
    an "But what I want to offer you, is a place for you to feel comfortable."

    fr "Why do you care so much?"

    show andrea serious at left, flip
    an "Isn’t it obvious?"

    na "A moment of silence."

    show andrea adec at left, flip
    an "I’m trans."

    fr "Trans?"

    show andrea serious at left, flip
    na "Andrea shifts, putting her forearms against the railing, supporting herself from behind. She looks up into the night."

    an "Yeah, not many places for us to feel comfortable."
    an "Not many places where we can exist period."
    an "People treat us like pests, like we’re rats that they have to call the exterminator on."
    an "We keep popping up, and they’re scared we’ll spread our “disease” or bite their kids."

    show andrea okay at left, flip
    an "I know how their minds work, I’ve talked to enough of them."
    an "A lot of them who didn’t realize I was one of the people they were calling “pests.” And lemme tell ya, there’s no justification."
    an "Nothing worthwhile that makes our existence so scary."

    na "Andrea takes another breath of smoke. She pushes it out in a plume, and it billows high into the sky."

    show andrea serious at left, flip
    an "So you know: I don’t tell people this."
    an "I’m lucky enough that I can feasibly pass."
    an "Which is not even something I necessarily want all the time, but it keeps me alive, and it allows me to be me, even though it’s quietly."
    an "I’m proud of my origins, and I wish that was something I could share with the world without it instantly putting a target on my back."

    show andrea awe at left, flip
    na "Andrea finally looks down from the stars, and stares at the warm glow of the classroom. She smiles a fond smile."

    show andrea pride at left, flip
    an "That’s why I put together this little rag-tag group."
    an "Safety in numbers, for all of us."
    an "And I want you to know that includes you."
    an "You’re part of our flock."
    an "That’s why I put together this little rag-tag group."
    an "Safety in numbers, for all of us."
    an "And I want you to know that includes you."
    an "You’re part of our flock."

    show andrea serious at left, flip
    na "Andrea flips over and faces out into the night again, her forearms resting on the railing once again, but now with her facing them."

    show andrea okay at left, flip
    an "I wrote this play because one: I love writing, even if I suck ass at it. but mostly because two: it feels like a way to tell stories about people like us."
    an "In code of course - everything is always in code - but it reaches those who recognize themselves in it."

    show rose listening at right
    fr "How...how is she like you? The vampire girl..."

    show andrea awe at left, flip
    an "Well, I relate to her y’know?"
    an "She must have been so fucking scared."
    an "How do you make peace with a body you didn’t get a say in?"
    an "In a world where people don’t give you a chance to figure it out?"
    show andrea fear at left, flip
    an "They probably wanted to kill her."

    na "..."

    show andrea okay at left, flip
    an "I changed the ending of it too."
    an "I don’t think I want a tragedy after all."
    an "Who gives a shit about the macabre."
    show andrea pride at left, flip
    an "I want her to be happy."

    fr "How does it end now?"

    show andrea okay at left, flip
    an "She still runs off, still hates herself."

    fr "And then?"

    show andrea serious at left, flip
    an "She finds someone willing to accept her. And having that safe space, allows her to settle into herself."

    fr "...And then?"

    show andrea pride at left, flip
    an "Everything changes."

    na "..."

    show rose bashful at right
    fr "You’re a really good person Andrea."

    show andrea snark at left, flip
    an "Hah! First time I’ve heard that one."

    ro "You deserve to hear it more."

    show andrea okay at left, flip
    an "Think you can get your girlfriend to say that?"

    show rose startled at right
    fr "Girlfriend?"

    show andrea snark at left, flip
    an "Yeah, sorry but I clocked you and Emily a while back."

    fr "We’re ... I just didn’t know what that meant."

    show andrea awe at left, flip
    an "Woah– baby queer."

    show rose worried at right
    fr "Please don’t call me that."

    show andrea okay at left, flip
    an "Hey it’s okay,"

    na "She crouches down to be at eye level with “Rose”."

    show andrea snark at left, flip
    an "Me too. Although I’m probably a more middle aged queer."

    fr "You’re 23."

    show andrea pride at left, flip
    an "It’s metaphorical."
    an "Anyway, now that it’s out in the open, I hope you know you’re always welcome here, even if I don’t love your girlfriend...or how she treats you."
    an "You both belong here."
    show andrea serious at left, flip
    an "We may be hidden, and everyone is too afraid to come out to each other, but we recognize each other, I think."
    an "We recognize ourselves."

    na "“Rose sits there, her posture no longer rigid, her arms no longer folded. She realizes that she has stopped tracking Andrea’s movements out of suspicion, and now more with admiration."

    show andrea okay at left, flip
    an "My cigarette’s dead. I’mma head back in."

    na "Andrea offers a hand to “Rose.”"

    show andrea pride at left, flip
    an "You coming?"

    hide andrea
    na "“Rose” takes Andrea’s hand. Together they stand, and walk back into the yellow glow, still holding hands."

    jump the_fight

label the_fight:
    play music "party_song.mp3"
    scene dramaroom
    show emily flippant at left
    show rose worried at right
    e "Where were you?"

    fr "Are you okay?"

    show emily peeved at left
    e "I’m fine."

    fr "I was with Mac, and then I was with Andrea."

    show emily scolding at left
    e "Andrea, why?"

    fr "It’s...a lot. Can we wait until we’re home?"

    na "Emily appraises “Rose”, she shoots a look at Andrea, who waves slightly. When she looks back at “Rose”, she nods."

    scene c_bedroom
    show emily peeved at left
    show catherine bashful at right
    play music "tecc.mp3"

    e "So Mac pulled the same shit with you huh?"

    show catherine worried at right
    c "What – I.. no...he just."
    c "He offered to help and I panicked."
    c "He could tell we were close and I..I felt like I had jeopardized the situation."

    show catherine frown at right
    na "Catherine waits for a reassurance that doesn’t come."

    show catherine worried at right
    c "Did he talk to you?"

    show emily peeved at left
    e "No, but Ash did. I told him to fuck off."

    show catherine worried at right
    c "What, why? Did he do something to you?"

    show emily flippant at left
    e "He didn’t know what he was talking about."

    show catherine frown at right
    na "Catherine mulls this over."

    show emily curious at left
    e "What about Andrea?"

    show catherine bashful at right
    c "We...talked. It was surprisingly nice."

    show emily peeved at left
    e "You talked?"

    show catherine bashful at right
    c "Yes."

    show emily scolding at left
    e "About what?"

    show catherine content at right
    c "About...a lot of things actually."

    show emily peeved at left
    e "So what, you’re friends now?"

    show catherine bashful at right
    c "I think so."

    show emily scolding at left
    e "Catherine, Andrea is not someone to be friends with."

    show catherine worried at right
    c "I know you don’t exactly get along, but she said that she accepts us, {i}both{/i} of us–"

    show emily scolding at left
    e "You told her about us?!"

    show catherine startled at right
    c "No!"
    c "She just knew."
    c "I wouldn’t betray your trust like that."

    show emily peeved at left
    e "..."

    show catherine worried at right
    c "Emily, you know I would never betray you right–"

    show emily scolding at left
    e "Then why are you going behind my back like this?"

    show catherine bashful at right
    c "What?"

    show emily scolding at left
    e "Why are you suddenly trying to be best friends with Andrea Barron?!"

    show catherine worried at right
    c "I-I’m not. She just saw that I was panicking and she–"

    show emily peeved at left
    e "Oh she rescued you?"
    e "Poor little Catherine."
    e "Acts so tough but turns out to always need saving."

    show catherine frown at right
    c "Where is this coming from?"

    show emily scolding at left
    e "It’s coming from you lying to me! You say that you love me, and then you go and get all buddy-buddy with a bitch like her–"

    show catherine worried at right
    c "What are you talking about?"

    show emily scolding at left
    e "Maybe you deserve each other."

    show catherine shadow at right
    c "..."

    show emily desperate at left
    e "Wait no."
    e "Catherine I didn’t mean it."
    e "I didn’t mean it."

    na "Emily has fallen to her knees in front of Catherine, who has not moved an inch. Emily cups one hand on Catherine’s face, the other she used to frantically pet her hair."

    e "No, Catherine please."
    e "Please!"
    e "Don’t go."
    e "Please don’t leave me."
    e "I can’t stand to lose you."
    e "Please don’t go anywhere."

    na "Emily has dissolved into sobs. She is clutching Catherine in an embrace, gripping her with shaking hands."

    show catherine worried at right
    c "Emily I’m not– I will {i}never{/i} leave you. I promise."

    na "Emily does not respond, she only keeps crying, as Catherine tries to rock slowly to calm her down."

    show catherine content at right
    c "I promise."
    c "But I do hope you change your mind about Andrea."
    c "Because I think she should come with us."

    show emily peeved at left
    na "Emily stills completely."

    show catherine worried at right
    c "She’s scared, Emily. There’s no one she can confide in but us–"

    show emily scolding at left
    na "Emily lifts her face up to Catherine’s. Her eyes are sharpened with white fury."

    e "Catherine. If you ever bring Andrea near us again, I will not forgive you."

    show catherine startled at right
    c "What? But you said that–"

    show emily scolding at left
    e "Hear me now."
    e "If you bring that bitch into our plan and into our life, I will {i}never{/i}."
    e "Forgive you."

    show catherine shadow at right
    c "...Understood."

    na "Emily cozies back into Catherine’s embrace. Catherine continues to rock...her view far into the distance."

    hide emily
    hide catherine
    
    play music "menu_song.mp3"
    menu:
        "Who do you want to sacrifice?"

        "Andrea":
            $ death == 0

            if character == 0:
                jump the_murder_of_andrea_barron
            else:
                jump crime_alley

        "Rei":
            $ death == 1
            
            if character == 0:
                jump crime_alley
            else:
                jump the_murder_of_andrea_barron

            

label the_murder_of_andrea_barron:
    play music "intimate_song.mp3"
    scene vineyard
    show andrea okay at left, flip
    an "Rose?"
    an "I’m here."
    an "God never thought I’d actually come to this freaky place."

    show andrea fear at left, flip
    na "The mansion is filled with shadows, as if returned to its dormancy before Emily. Andrea scans the dark, her hand not moving from the door."

    show andrea serious at left, flip
    an "Rose I may dress like this but I don’t actually rock with the scary shit, so if you’re here: speak now."

    show catherine shadow at right
    c "I’m here."

    show andrea okay at left, flip
    an "Great, you wanna come out of the shadows?"

    show catherine bashful at right
    c "I will, but I don’t want you to scream."

    show andrea fear at left, flip
    an "Oooooookay."

    na "Andrea chews on the inside of her cheek. Catherine wonders if she can hear her breathing."

    show andrea serious at left, flip
    an "Alrighty I’m gonna count down from three, and if you don’t come out I’m hightailing it out of here."

    na "No response."

    an "Good plan. 3...2..."

    show catherine bashful at right
    na "Catherine’s foot emerges, there’s a pause, and then the rest of her follows it."

    c "Please don’t be scared, I promise, I know I’m unusual but you can trust me- it’s me– I’m Ro–"

    show andrea awe at left, flip
    an "You’re her... aren’t you? The vampire girl."

    show catherine bashful at right
    c "I am."

    na "Andrea takes a step forward."

    show andrea awe at left, flip
    an "You’re beautiful."

    show catherine gay blush at right
    na "Catherine blushes."

    show andrea serious at left, flip
    an "What should I call you?"

    show catherine content at right
    c "Catherine. Catherine Lyon."

    show andrea okay at left, flip
    an "That’s really your name?"

    na "Catherine nods."

    show andrea serious at left, flip
    an "Is the rest of the story true?"

    show catherine frown at right
    c "It’s complicated. No, not really."

    show andrea okay at left, flip
    an "I hope you weren’t too insulted by my portrayal of you."

    show catherine content at right
    c "It did take a lot of creative liberties."
    c "But I like the ending."
    c "The new one."

    show andrea awe at left, flip
    an "Catherine..."

    na "Andrea takes another step closer, she and Catherine are almost chest to chest now. Catherine reaches out and intertwines her hand with Andrea’s."

    show andrea serious at left, flip
    an "Did you find someone who accepted you?"

    show catherine content at right
    c "I did."

    show andrea okay at left, flip
    an "Emily, right?"

    na "Catherine nods. Tears form in Andrea’s eyes."

    show andrea awe at left, flip
    an "And did everything change?"

    show catherine content at right
    c "It did."

    show andrea snark at left, flip
    an "God, no wonder you two are attached at the hip."

    show catherine content at right
    c "It will change for you too Andrea."

    show andrea awe at left, flip
    an "I hope so, I really hope so."

    show catherine bashful at right
    c "We’re gonna give you a world where you belong."

    na "Andrea nods."

    show catherine worried at right
    c "You still wish to be friends with this version of me?"

    show andrea pride at left, flip
    an "Safety in numbers."

    show catherine shadow at right
    na "Catherine smiles, then raises her claws."

    show andrea fear at left, flip
    an "Wait ro– catherine...what are you doing."

    show catherine stoic at right
    c "I need you to trust me."

    show andrea serious at left, flip
    an "Okay, just put your claws down and I will."

    show andrea fear at left, flip
    na "Andrea chuckles at her own joke. Catherine doesn’t move."

    an "Catherine?"

    show catherine shadow at right
    c "I’ll keep my word to you Andrea. I’ll see you again soon."

    show andrea fear at left, flip
    an "Wait."
    an "Wait Don’t!"
    an "I want to live– I want to li–"

    hide andrea
    play audio "knife_stab.mp3"
    na "Before Andrea can even move back five feet, Catherine has slashed her jugular."
    play audio "body_fall.mp3"
    na "Andrea collapses, and Catherine catches her gracefully."
    show catherine worried at right
    na "Catherine holds her there for a moment, wincing at the primordial fear in Andrea’s eyes."

    show catherine shadow at right
    na "Andrea forces out gurgles and her hands claw at the air around her bleeding throat."
    na "Catherine’s wince turns into a grimace...no matter how noble the cause...this part still twists her gut."
    na "Andrea’s eyes mercifully close."
    na "And Catherine continues to hold her in the dark and silence."

    na "..."

    hide catherine
    jump andrea_died

label andrea_died:
    play music "tecc.mp3"
    scene vineyard
    show catherine shadow at right
    show emily peeved at left
    na "..."

    e "..."

    show catherine frown at right
    c "And then...there was only one course of action to take."

    show emily scolding at left
    e "So she followed you to the mansion?"

    show catherine worried at right
    c "Yes, I was taken entirely by surprise."

    show emily peeved at left
    e "Did you lead her?"

    show catherine bashful at right
    c "Pardon?"

    show emily scolding at left
    na "Emily’s face is like stone."

    e "Did you lead her?"

    show catherine worried at right
    c "No, it was an unfortunate...coincidence."

    show emily peeved at left
    e "..."

    show catherine worried at right
    c "Coincidence isn’t the proper term...but I’m struggling to find words amidst...all of this."

    na "In a moment of silence, the girl’s eyes pick up the conversation."
    na "Emily’s eyes offer “Don’t do this.” but something lies underneath that statement, like a snake under a hatch."
    na "Catherine’s eyes say...something unreadable, but understood."

    show catherine stoic at right
    c "We have nothing else to do with her body, if not disposed of properly, she could expose our entire plan."

    show emily scolding at left
    na "Emily’s fists are clenched."

    e "Do you have the totems?"

    show catherine content at right
    c "I do."

    show emily peeved at left
    e "Did you get them after?"

    show catherine shadow at right
    c "..."

    show emily scolding at left
    e "How’d you know to get them?"

    show catherine worried at right
    c "..."
    c "She had them on her."
    c "She left her satchel by the door."
    c "They may not fit perfectly, but it should work."

    show emily desperate at left
    e "Catherine..."

    show catherine bashful at right
    c "Yes?"

    show emily peeved at left
    e "..."

    show catherine worried at right
    c "Will you trust me in this one instance, my love?"

    show emily flippant at left
    e "..."

    show catherine shadow at right
    c "..."

    show emily scolding at left
    e "Let’s just do the fucking ritual already."

    hide emily
    hide catherine
    jump ritual_four_andrea

label ritual_four_andrea:
    play music "ritual_song.mp3"
    scene vineyard
    show catherine shadow at right
    show emily peeved at left
    c "..."

    e "..."

    show catherine bashful at right
    c "Shall we begin?"

    show emily scolding at left
    na "Emily responds sarcastically."

    e "Oh we certainly shall!"

    show catherine worried at right
    c "Emily, I told you, it was an accident."

    show emily scolding at left
    e "Oh yes Catherine. It just happened to be a very, very convenient one."

    show catherine shadow at right
    c "..."

    show emily peeved at left
    e "Just stuff her already."

    hide emily
    hide catherine

    screen ritual_four_andrea_screen(res):
        add "ritual_interface"

        draggroup:
            if "Lunchbox" not in res:
                drag:
                    drag_name "Lunchbox"
                    droppable False
                    dragged totem_dragged
                    xpos 0 ypos 0
                    add "@4/Lunchbox.png"

            if "Shoelaces" not in res:
                drag:
                    drag_name "Shoelaces"
                    droppable False
                    dragged totem_dragged
                    xpos 1400 ypos 0
                    add "@4/Yellow_and_Lavender_Shoelaces.png"

            if "Keys" not in res:
                drag:
                    drag_name "Keys"
                    droppable False
                    dragged totem_dragged
                    xpos 0 ypos 600
                    add "@4/Keys.png"

            if "Script" not in res:
                drag:
                    drag_name "Script"
                    droppable False
                    dragged totem_dragged
                    xpos 1400 ypos 600
                    add "@4/Script.png"

    $ res = []

    while len(res) < 3:
        call screen ritual_four_andrea_screen(res)
        
        if _return != None:
            
            if _return == "Lunchbox":
                e "..."

                c "I know we can trust her Emily."

                menu:
                    "Add Andrea's Tattered Lunchbox?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Shoelaces":
                e "..."

                c "I wish I had her way of...standing up for what she believes in."

                menu:
                    "Add Andrea's Lavender and Yellow Shoelaces?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Keys":
                e "At least she’ll be able to defend us. What a useful skill...in paradise...where we all need protection."

                c "Do you think this one is a good pick?"

                menu:
                    "Add Andrea's Keys?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Script":
                e "She yanked me around enough in life. I don’t need that in the beyond."

                c "I didn”t mean to hurt you Emily."

                menu:
                    "Add Andrea's Script?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            else:
                pass

    $ _emily_cnt = sum(1 for i in res if i in ["Keys", "Script"])
    $ ritual_card_4 = "emily" if _emily_cnt >= 2 else "catherine"
    $ ritual_cards.append(ritual_card_4)
    if ritual_card_4 == "emily":
        $ ritual += 1
    $ _c1 = ritual_cards[-3] if len(ritual_cards) >= 3 else "emily"
    $ _c2 = ritual_cards[-2] if len(ritual_cards) >= 2 else "emily"
    scene black
    stop music fadeout 1.0
    play audio "ritual_complete.mp3"
    if _c1 == "emily":
        show success_emily as success_card_1 at card_left3
    else:
        show success_catherine as success_card_1 at card_left3
    if _c2 == "emily":
        show success_emily as success_card_2 at card_mid3
    else:
        show success_catherine as success_card_2 at card_mid3
    if ritual_card_4 == "emily":
        show success_emily as success_card_3 at card_right3
    else:
        show success_catherine as success_card_3 at card_right3
    $ renpy.pause(1.5, hard=True)
    pause

    jump play_or_not_to_play

label andrea_lived:
    play music "drama_song_tense.mp3"
    scene dramaroom
    show andrea okay at center
    show emily desperate at left
    show ash sad at right, flip
    an "..."

    mac "..."

    ash "..."

    e "..."

    fr "..."

    show andrea serious at center
    na "Andrea opens her mouth and somberly asks"
    an"Everyone knows, right? "
    mac "Seeing as we all got questioned by the police: yeah, we know.  "

    show andrea okay at center
    an "Do you all want to talk about it?"

    ash "I feel so stupid. "
    na "Everyone’s attention rushes to Ash. "

    ash "Of course they aren’t sick, or traveling or whatever excuse I came up with."
    ash "I didn’t even check on them once."
    ash "I’m a piece of shit."

    fr "Ash...it’s not your fault- "

    ash "That’s what people always say!"
    ash "But someone’s gotta take the blame for it!"
    ash "Disappearances don’t just “happen.”"

    show andrea serious at center
    an "Yes, it is someone's fault."
    an "But it’s not yours."
    an "It’s the fucker that took them’s."
    na "Everyone’s attention returns to Andrea."
    na "Ash’s head falls into his hands."
    na "Mac puts a hand on Ash’s back."

    show andrea okay at center
    an "Nobody expects these things to happen to them. Don’t blame yourself for not being paranoid. "
    na "Andrea moves from her standing position to sit in a chair. "

    show andrea serious at center
    an "Listen, I get it. We don’t know where they are, so we’re gonna wanna react like they’re gone for good, but it doesn’t help anyone to mourn when we don’t have proof. "
    na "She pauses, looking at the floor. "

    show andrea okay at center
    an "Still, I understand that we’re gonna grieve anyway, cause it’s one of those things you just can’t stop. And because of that, I think we cancel the play. "
    na "Nods from around the room. "

    show emily desperate at left
    e "Are we sure? "
    na "Everyone looks to Emily. "

    show andrea okay at center
    an "What do you mean? "

    e "Should we really cancel the play?"
    e "We can’t throw our life out of order."
    e "It’s like you said, we don’t wanna mourn when we don’t have proof."

    ash "Geez em, do you even care about them? "
    show emily scolding at left
    na "Suddenly Emily shoots out of her chair, and yells emotionally"
    e "I care about them more than anybody in this room does! More than you’ll ever know! "
    show emily desperate at left
    na "Tears are starting to flow now. All the repressed fear is causing Emily to shake. “Rose” wishes she could reach out to her. "

    e "And that’s why I think we shouldn’t give up."
    e "If we don’t do this...it could be the last thing...the last thing we have of them, and we would’ve given up on it!"
    e "How do you think that’s going to feel if they never get found?"
    e "The last thing that had a piece of them in it, and we threw it away!"

    e "We need to do this play Andrea."
    e "I’ll study my lines harder, I’ll actually do those silly breathing exercises you showed us - The play just needs to happen."
    e "Otherwise,"
    na "Emily Sniffles. "

    e "What do we have left? "
    na "..."

    show andrea serious at center
    an "Emily...you have a big heart."
    an "But it seems like trying to do this is only gonna hurt you more."
    an "I really don’t think-"

    fr "I trust her. "
    na "Everyone turns to look at “Rose”"

    fr "I trust Emily’s judgement."
    fr "If she says she can handle it, she can."
    fr "This -This is her way of - her way of showing - showing that she cares."

    mac "Thanks for the input Rose, but frankly, you’re not even a member of the club-"

    show andrea okay at center
    an "Okay. "
    na "Everyone’s neck is getting whiplash at this point. "

    show andrea serious at center
    an "You two know each other best. If this is going to help you, we’ll do it. "
    na "She addresses the room."

    show andrea okay at center
    an "Do you think we can do it guys?  "
    na "Mac sighs. Ash’s head is still in his hands. "

    mac "It’s three against two anyway. "

    show andrea serious at center
    an "Ash... you don’t have to-"

    na "Ash shakes his head as tears fall from his eyes."

    ash "N-Nope! You said we’re doing th-this, Andrea, and you’re al-always right!"

    fr "Hey!"

    na "Emily looks at Catherine in disbelief, Catherine shrinks in on herself. "

    show andrea okay at center
    an "Ash if you want out - "

    ash "I said we’re doing this!"

    show andrea snark at center
    an "Geez okay. "

    show andrea okay at center
    na "ANDREA leans back in her chair and sighs a weighty sigh. She raises her hand towards the ceiling, and stares at her rings. "

    show andrea pride at center
    an "Call time is 6:00 PM tomorrow."

    hide emily
    hide andrea
    jump last_dance

label last_dance:
    play music "intimate_song.mp3"
    scene ballroom
    show emily genuine at left
    show catherine content at right
    na "The night of the blood moon. Emily and Catherine sit on the stairs of the mansion. "

    e "Are you sure you’re not going to miss this place? "

    show catherine bashful at right
    c "After 120 years? I doubt I’ll grieve it too heartily. "

    show emily satisfied at left
    e "Plus if you ever do miss it, it’ll be right there in Our Paradise. "

    show catherine content at right
    na "Catherine nods"
    c "Mm."

    show emily mischievous at left
    na "Emily teases"
    e "No other goodbyes you want to say?"

    show catherine frown at right
    na "Cather lets out a dry laugh."
    c "Ha ha."
    na "The girls sit in silence."
    na "Emily stares at Catherine, while Catherine examines her claws."
    show emily satisfied at left
    na "Emily suddenly throws her hands over her head and arches her back in a stretch."

    e "Well, let’s get this over with. "

    show catherine worried at right
    c "Emily, we should be preparing...we don’t want to miss it-"
    show emily flippant at left
    e "Pssh we’ve prepared perfectly."
    e "Come on!"
    e "Give me one short dance with my..."
    show emily desperate at left
    na "She stumbles."
    na "They’ve never defined what this devotion is between them."
    na "Girlfriend, wife, conspirator?"
    show emily genuine at left
    e "With my Catherine. "
    show catherine frown at right
    na "Catherine looks at her a moment, her sadness trickling from her brows into her eyes."
    na "Emily’s smile falters."
    show catherine content at right
    na "Then Catherine sighs and stands, Emily eagerly grabs her, slotting the two of them into position."

    show catherine bashful at right
    c "There’s no music playing."

    show emily flippant at left
    e "Does it matter? "

    show catherine content at right
    c "It kind of does."
    na "Catherine relents and starts swaying."

    show emily desperate at left
    e "Has it been a less lonely existence with me? "

    show catherine gay blush at right
    c "Yes. "

    show emily genuine at left
    e "Then would it really be so bad, if I lived forever with you? You know, the other way. "

    show catherine frown at right
    c "Yes...you’d be miserable shackled to just me. "

    show emily peeved at left
    e "How do you know? "

    show catherine shadow at right
    c "..."
    na "After a long while of silence, Emily speaks. "

    show emily genuine at left
    e "Catherine, I never thanked you, y'know for all of this. "
    na "Emily looks up into Catherine’s eyes. "

    e "So this is me thanking you. "
    na "They continue to sway. Emily lays her head on Catherine’s chest. "

    show emily desperate at left
    e "I mean, you’re my beacon, nobody has ever taken care of me like you do, no one has ever looked at me and decided that I was worth taking care of. And honestly, I’m probably not."

    show catherine worried at right
    c "Emily..."

    show emily genuine at left
    e "You’re good, more good than I ever... you make me better. "

    show catherine content at right
    c "Emily, you’re more than worth it. "
    na "Emily looks up to Catherine once more, her hand tracing the structure of Catherine’s face."
    na "They gaze at each other for a moment."
    na "Then, Emily gently moves in, her lips padding softly against Catherine’s."
    na "Catherine remains still for a moment, but then she reciprocates."
    na "Emily moves her hand onto the back of Catherine’s neck, resting her hands in her baby hairs."
    na "Catherine has fully embraced Emily now, her hands caressing her hips."
    na "Emily slides her hands around from the back of Catherine’s neck to her shoulders, and she begins searching for an in, a way to remove the top."
    show catherine shadow at right
    na "Catherine pulls away."
    show emily desperate at left
    na "Emily stands in shock."
    hide catherine
    play audio "walk_grass.mp3"
    scene mansion
    na "Catherine begins walking towards the Vineyard."
    na "Emily stands there for a moment, her hand clutching the side of her own arm."
    hide emily
    jump blood_ritual

label andrea_confrontation:
    play music "drama_song_tense.mp3"
    scene stage
    show emily desperate at center
    mac "Geez Emily you look like fucking hell."
    mac "Are you covered in dirt?"
    mac "Holy fuck!"
    mac "What happened to your arm?"
    mac "Ash?"
    mac "Ash, get over here!"
    mac "Rose, go get help!"
    show emily peeved at center
    na "“Rose” makes eye contact with Emily. Emily uses every ounce of her power to try and restrain “Rose” with just her gaze."
    fr "I’ll be right back."
    show emily scolding at center
    e "Catherine!"
    mac "Who?  "
    hide emily
    play audio "run_away.mp3"
    na "“Rose” flees, heading to the green room, hoping that she’ll find someone, or no one and a moment of peace to herself."
    na "She doesn’t make it all the way there before she slams into somebody."
    show andrea okay at right
    na "“Rose” looks up, and she meets eyes with Andrea, who is panting too, as if she has been running."
    na "They stay pressed against each other, their breath puffing hot against each other’s faces."
    na "Andrea grabs “Rose’s” wrist and turns on her heel, pulling the girl into running."
    na "They run the rest of the way to the greenroom."
    na "When they get to the room, Andrea gently shifts her hand from “Rose’s” wrist to the outside of her upper arm, guiding her into the room, all the while her neck is turned looking behind them."
    play audio "door_slam.mp3"
    scene backstage
    na "When “Rose” is safely inside, Andrea whips around with violence and slams the door shut, locking it."

    show andrea serious at right
    show rose worried at left, flip
    an "“Rose”...I know."
    na "“Rose” goes pale."
    fr "Know what?"
    show andrea okay at right
    an "And I know it’s not your fault."
    an "Because you’re her aren’t you?"
    an "The vampire girl."
    fr "..."

    show andrea awe at right
    an "Can you...can you show me the real you? "

    na "“Rose” winces"
    fr "..."

    na "My real friend? "

    fr "Things might get a bit difficult looking back if you see it."

    show andrea serious at right
    an "I’m more focused on going forward "

    na "Andrea steps closer. "

    show andrea pride at right
    an "Together. "

    hide rose
    show catherine bashful at left, flip
    na "Catherine looks at her friend, taking in her last view of eyes that hold hope for her, and lets the mask drop. "

    show andrea awe at right
    an "Oh god. "

    show catherine startled at left, flip
    na "Catherine flinches. "

    show andrea awe at right
    an "You’re beautiful. "
    show catherine gay blush at left, flip
    na "Catherine looks up in shock, Andrea’s eyes are full of adoration. "

    show andrea serious at right
    an "What can I call you?"

    show catherine bashful at left, flip
    c "...Catherine. Catherine Lyon. "

    show andrea okay at right
    an "Catherine. Hello Catherine. "

    show catherine frown at left, flip
    c "It’s still me, Andrea. "
    show andrea serious at right
    an "Right, I just wanted to be polite. How long have you been - "

    show catherine worried at left, flip
    c "Please forgive me for interrupting. I can answer all your questions, but first, will you answer one of mine? "
    na "Andrea nods. "

    c "How did you know? "

    show andrea serious at right
    an "That’s actually why I’m here, I suspected something wasn’t right, the hold Emily had on you, I know us queer women can be codependent but geez."
    an "When Rei told me he was going to meet with Emily, but didn’t mention you, it felt like a trap."
    an "I’m sorry to suspect you two like that, but I’m paranoid by practice now."
    show andrea fear at right
    an "I told Rei not to go but he just ruffled my hair and told me not to worry- and then he didn’t come back."
    an "So I followed you and Emily back to the manor after the meeting...What the hell was she making you do in that garden?"
    show andrea creeped at right
    an "I left before I saw the whole thing, but I already have enough evidence."
    an "We can’t go to the cops but we can figure out something."
    an "I’m here to help you, help both of you-"
    show catherine startled at left, flip
    na "The door knob jangles. "

    show emily scolding at center
    e "Rose? Rose are you in there? "

    hide emily
    show andrea serious at right
    an "Look, I know that she’s probably got it in your head that I’m the bad guy. But Catherine, I swear I want to help you, and I want to help her most of all. "

    show catherine worried at left, flip
    c "Andrea..."

    show emily scolding at center
    e "Don’t bullshit me now Catherine, I can hear your voice!"

    hide emily
    show andrea serious at right
    an "Catherine, I know it’s hard for you to trust right now, so listen to your gut, not your head. "
    na "Andrea reaches out her hand to Catherine and nods quickly but steadily. "

    show emily scolding at center
    e "Catherine, you know what you need to do!"

    hide emily
    show andrea pride at right
    an "Emily! I just want to help you! "
    na "The jiggling on the door knob stops. "

    show emily desperate at center
    e "..."
    e "I really wish I believed you."
    e "Where were you then, when all this started, when they were still here."
    e "Why didn’t you stop it?"
    e "Why didn’t you stop me!?"

    hide emily
    show andrea okay at right
    an "I’m sorry Emily, I’m here now. Hold on just one second. "
    na "She turns to Catherine. "

    show andrea serious at right
    an "I have a tape recorder of some of your conversations, it’s okay, this will all be over soon."
    an "It’s gonna be hell for a while, but you’ll both be safe."
    an "We’re going to call an ambulance for her-"

    show emily scolding at center
    e "She has evidence?! Catherine, do something! "
    hide emily
    na "The door starts being hit with massive thuds. "

    show andrea pride at right
    an "And we’ll get you into hiding. Catherine..."
    na "Andrea pushes her hand further towards Catherine."
    na "She smiles sweetly, with a look that promises it will weather storms with you."
    show catherine worried at left, flip
    na "Catherine goes to take her hand.."

    show emily scolding at center
    e "GRAH!"

    show catherine startled at left, flip
    hide emily
    c "Emily, DON’T! - "
    hide andrea
    show emily scolding at center
    play audio "door_slam.mp3"
    na "The door swings open, and hits Andrea violently."
    play audio "bones_breaking.mp3"
    na "The impact sends her into the too-near wall, and her head splits open."
    na "Emily stands in her costume, heaving."

    show catherine startled at left, flip
    c "Andrea! Emily how could you-"

    show emily peeved at center
    e "Quiet! They’ll hear you. "
    na "Emily appraises Andrea, eyebrows furrowed, eyes like prey. She nods, almost like checking it off of a list. "

    show emily scolding at center
    e "She’ll be dead soon. How could you do this? "

    show catherine startled at left, flip
    c "What?"

    show emily scolding at center
    e "How could you choose her over me!"

    show catherine worried at left, flip
    c "I wasn’t - I - geez Emily I was trying to do what’s best for you!"

    show emily scolding at center
    e "Don’t lie to me Catherine, I can’t take it!"
    e "Why do you lie to me?"
    e "Why do you tell me you love me and then pull away?"
    e "Make up your damn mind, am I worth it or not!"

    show catherine worried at left, flip
    c "Everything I’ve done, I’ve done for you. I... fucking worship you dammit. "

    show emily scolding at center
    e "Then why would you leave me!"

    show catherine frown at left, flip
    c "I-"
    show emily desperate at center
    na "Emily collapses on the floor sobbing."
    show catherine startled at left, flip
    na "Catherine is momentarily silenced."
    show emily desperate at center
    na "Emily blubbers through her tears."

    e "C-Catherine..."
    show catherine shadow at left, flip
    na "After a second, Catherine’s eyes lose focus. She falls to her knees. "
    na "She begins to scream. "
    show emily peeved at center
    na "Emily’s head snaps up, tears still rushing down their trails."
    show catherine worried at left, flip
    na "Catherine wails and gags, trying to vomit, she swings her arms around and her legs jerk in erratic ways."
    show emily gross at center
    na "Emily’s face contorts in disgust."

    e "Oh god. "
    show emily desperate at center
    na "Emily takes in the catastrophe around her, a well painted portrait of her damnation. Andrea’s dead body, Catherine wailing, her own tear streaked face."

    e "Oh Catherine...how are we going to get out of this one?"

    hide emily
    hide catherine
    jump endings

label glass_closet_opens:
    play music "party_song.mp3"
    scene dramaroom
    show emily flippant at left
    na "After a few minutes of mingling, Ash approaches Emily."

    ash "Hey, Em, can we talk?"

    show emily curious at left
    e "Sure, what is it?"
    ash "You and Rose went to the same high school, right?"


    show emily flippant at left
    e "Yeah. I think we met, like, freshman year?"

    na "Ash stares at Emily for a second, looks down at his  drink, and then puts his head back up."

    ash "How long have you two been together?"
    show emily peeved at left
    e "Together?"

    ash "Yeah, together."

    show emily peeved at left
    na "Emily gives Ash an annoyed look."


    show emily flippant at left
    e "Well we’ve been friends since high school."

    ash "Still friends? I’ve seen you two, you’re basically joined at the hip."

    show emily scolding at left
    e "What the hell are you implying?"
    na "Ash sighs."

    ash "Emily, it’s not exactly subtle, y’know?"

    show emily peeved at left
    e "What, what’s not subtle? I still don’t know what you’re trying to fucking say."

    ash "I’m trying to have a basic conversation, Emily. I don’t know why that’s so hard."
    show emily flippant at left
    e "Doesn’t seem very basic to me."
    na "Ash sighs again, more exasperated than before. He points towards Mac and “Rose”."


    ash "Do you see that man over there?"
    ash "That’s my fucking boyfriend, Emily."
    ash "Did you know that?"

    show emily mischievous at left
    na "Emily forms a smirk."


    e "... No, I didn’t."

    ash "Really? You didn’t realize?"


    show emily flippant at left
    e "I hadn’t even thought about it. It’s not any of my business anyway who you’re fucking, it’s not like I’m into you."

    ash "I think I’ve told every single other person here except for you, about me and Mac. We’re all some kind of gay here anyways, so I don’t know why you’re so scared of me outing you."
    na "Ash looks at Emily, a soft look in his eyes."
    ash "I wouldn’t do that to you two, ok?"
    show emily peeved at left
    e "Oh shut up."

    ash "Huh?"


    show emily scolding at left
    e "Why would I care about being outed!"

    ash "You don’t?"


    show emily peeved at left
    e "Just – ugh, look. I don’t want you prying into me and Ca–"

    show emily desperate at left
    na "Emily stops, a little surprised at herself."

    show emily scolding at left
    e "Rose’s relationship, okay?"
    e "It’s none of your fucking business what me and her are doing, and honestly, I don’t know why you care!"
    e "I don’t know why you think it’s a good idea to come up and ask me how my relationship is doing, cause you wanna know something?"
    e "It’s doing great!"
    na "Emily takes a step closer to Ash. Ash backs away a little bit."

    e "And I don’t need you to come over and fuck things up!"
    na "Ash and Emily stare at each other for a few moments, both feeling tense. Ash sighs."


    ash "I guess I’m sorry I asked."

    hide emily
    na "Ash walks away, sulking."

    jump the_fight

label crime_alley:
    play music "occult_song.mp3"
    scene dramaroom
    show emily genuine at right, flip
    show rei regular guy at left
    e "Rei, are you free today?"

    re "Sure, what’s up?"

    e "Want to see a movie with me?"

    show rei hyped at left
    re "Hell yeah!"
    re "Got any movie in mind or do you want to choose?"
    re "Because I heard that there’s a new Batman movie that’s pretty good."

    show emily flippant at right, flip
    e "Sure Rei, I wouldn’t mind watching Batman with you."

    scene school
    na "The girls leave the theatre, they walk towards the park and sit down on a bench, talking about the movie."

    show emily satisfied at right, flip
    e "Rei, Stick out your hand."

    show rei alright at left
    re "Sure, Em."

    na "Emily puts a friendship bracelet on Rei’s wrist."

    show rei hyped at left
    re "Woahhhh! This is cool!"

    show emily genuine at right, flip
    e "Yeah! I know you’ve been kinda quiet and down since Aarya and Ophelia have been gone for a while, so I just wanted to give you this bracelet as a way to say I’m glad that you’re my friend and I’m glad to have you around."

    show rei iwiwlt at left
    re "Awww, thanks Em. I wish I could do something for you, you brought me out to see a movie, gave me this cool bracelet, and I don’t even have anything to give you."

    show emily satisfied at right, flip
    e "Hehe, it’s nothing Rei, You’ve done a lot for me, you’ve kept so many secrets of mine, and I wanted to thank you for being someone I can talk to about my private thoughts."

    show rei hyped at left
    re "Haha. That’s because we’re both evil, we gotta stick together."

    play audio "walk_grass.mp3"
    scene alley
    na "Rei and Emily walk back from the park towards the university."

    play music "murder_song.mp3"
    show emily peeved at right, flip
    e "Hey Rei Wait!"
    e "I know a shortcut to the university."
    e "It’s a little creepy though, but I’m sure you can go through it."

    show rei alright at left
    re "Creepy schmeepy, This alley right here?"

    na "Emily points towards an alley."

    show emily flippant at right, flip
    e "Yeah it’s through here."

    show rei hyped at left
    na "Rei steps into the alley, and sprints down inside, before turning and facing Emily with a smile on his face."

    re "Yooooooo!"
    re "This is creepy for sure!"
    re "This is just like the alley from the batman movie!"
    re "This is literally Crim–"
    if death == 0:
        jump rei_lives
    else:
        jump rei_dies

label rei_dies:
    show rei death at right
    na "A silhouette slips out of the shadows, her purple eyes illuminating behind Rei."
    play audio "knife_stab.mp3"
    na "A red wet hand shoots out of Rei’s chest, grasping the Punk’s heart."
    play audio "body_fall.mp3"
    na "Rei’s face quickly contorts in pain and agony before his body falls limp onto the Vampire’s arm."
    show catherine stoic at right
    hide rei

    c "She was so spunky and happy."

    show emily peeved at left
    e "And she’ll be so much happier in paradise with us. Got the cart?"
    na "Catherine pulls out the red wagon cart with her free hand. Emily carefully lifts Rei’s legs without touching any of his blood."

    show emily satisfied at left
    e "That was very clean. Well done. "

    c "Hm."

    show emily genuine at left
    e "I mean it Catherine, you did a beautiful job. No one will suspect it was even a murder."

    show catherine worried at right
    c "May we return home now?"

    show emily flippant at left
    e "..."

    c "..."

    e "Of course."

    na "They stride out of the alley, Rei hidden in the red wagon they cart behind them."
    na "Catherine walks with reckless abandon."
    na "Emily can not stand the tension any longer."

    show emily peeved at left
    e "Catherine, look at me."

    na "Emily forces Catherine’s face into her hands."

    show emily genuine at left
    e "Thank you. For choosing Rei."

    na "Catherine stares blankly."

    show catherine frown at right
    c "I...I really am sorry. For everything that happened with Andrea."

    show emily flippant at left
    e "It’s fine."

    c "Is it?"

    na "This time she gets no response."
    na "Catherine pulls her face away, and continues walking."
    na "Emily follows after."
    hide emily
    hide catherine

    jump ritual_four_rei

label rei_lives:
    play music "occult_song.mp3"
    show rei alright at left
    re "Crime Alley."

    na "Rei looks at Emily, who is anxiously looking around, waiting for Catherine to strike."

    re "Looking for something?"

    show emily peeved at right, flip
    e "It’s nothing Rei, I really enjoyed TAKING YOU OUT."
    e "It makes my HEART ACHE."
    e "I hope that this moment will never END, HMM?"

    show rei oops at left
    re "Your throat okay? You kinda said some of those words a little loud."

    na "Emily coughs aggressively."

    show emily flippant at right, flip
    e "Sorry my throat was congested, Let’s go back to the university."
    hide emily
    hide rei

    jump andrea_died

label ritual_four_rei:
    play music "ritual_song.mp3"
    scene vineyard
    show emily flippant at left
    show catherine stoic at right
    e "..."

    c "..."

    show emily genuine at left
    e "Are we okay?"

    show catherine frown at right
    c "I'm fine."
    hide emily
    hide catherine

    screen ritual_four_rei_screen(res):
        add "ritual_interface"

        draggroup:
            if "Punk Patch" not in res:
                drag:
                    drag_name "Punk Patch"
                    droppable False
                    dragged totem_dragged
                    xpos 0 ypos 0
                    add "@4/Punk_Patch.png"

            if "Gem" not in res:
                drag:
                    drag_name "Gem"
                    droppable False
                    dragged totem_dragged
                    xpos 1400 ypos 0
                    add "@4/Citrine_Stone.png"

            if "Friendship Bracelet" not in res:
                drag:
                    drag_name "Friendship Bracelet"
                    droppable False
                    dragged totem_dragged
                    xpos 0 ypos 600
                    add "@4/Friendship_Bracelet.png"

            if "Skateboard" not in res:
                drag:
                    drag_name "Skateboard"
                    droppable False
                    dragged totem_dragged
                    xpos 1400 ypos 600
                    add "@4/Skateboard.png"

    $ res = []

    while len(res) < 3:
        call screen ritual_four_rei_screen(res)
        
        if _return != None:

            if _return == "Punk Patch":
                e "As much as I love Rei, I wish she would cool her jets at least some of the time. Right Catherine?"

                c "I could not bare to see Rei without their spunk."

                menu:
                    "Add Rei's Punk Patch?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Gem":
                e "Rei will be plenty happy."
                e "It’s paradise!"
                e "Let’s not waste space."

                c "I must admit...I’d be remissed if I never heard Rei laugh again."

                menu:
                    "Add Rei's Gem?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Friendship Bracelet":
                e "I think Rei is the only one I could trust with our secret, except you of course Catherine."

                c "..."

                menu:
                    "Add Rei's Friendship Bracelet?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            elif _return == "Skateboard":
                e "Everything is so exciting when I’m with Rei."

                c "..."

                menu:
                    "Add Rei's Skateboard?"

                    "Yes":
                        $ res.append(_return)
                    "No":
                        pass
            else:
                pass

    $ _emily_cnt = sum(1 for i in res if i in ["Friendship Bracelet", "Skateboard"])
    $ ritual_card_4 = "emily" if _emily_cnt >= 2 else "catherine"
    $ ritual_cards.append(ritual_card_4)
    if ritual_card_4 == "emily":
        $ ritual += 1
    $ _c1 = ritual_cards[-3] if len(ritual_cards) >= 3 else "emily"
    $ _c2 = ritual_cards[-2] if len(ritual_cards) >= 2 else "emily"
    scene black
    stop music fadeout 1.0
    play audio "ritual_complete.mp3"
    if _c1 == "emily":
        show success_emily as success_card_1 at card_left3
    else:
        show success_catherine as success_card_1 at card_left3
    if _c2 == "emily":
        show success_emily as success_card_2 at card_mid3
    else:
        show success_catherine as success_card_2 at card_mid3
    if ritual_card_4 == "emily":
        show success_emily as success_card_3 at card_right3
    else:
        show success_catherine as success_card_3 at card_right3
    $ renpy.pause(1.5, hard=True)
    pause

    jump andrea_lived

label play_or_not_to_play:
    play music "occult_song_tense.mp3"
    scene dramaroom
    show rei alright at center
    show emily desperate at left

    na "The drama club is silent. Rose and Emily arrive to see Rei, Mac and Ash, somber expressions on their faces."

    re "Did you two have the police show up at your door?"

    show emily flippant at left
    e "No, I was out late with Rose."
    na "Rose nods, Rei sighs."

    re "Ophelia, Aarya, and Andrea are officially missing according to the police."

    show ash sad at right, flip
    ash "I feel so stupid. "
    na "Everyone’s attention rushes to Ash. "

    ash "Of course they aren’t sick, or traveling or whatever excuse I came up with."
    ash "I didn’t even check on them once."
    ash "I’m a piece of shit."
    na "Rei frowns."

    show rei oops at center
    re "No ash."
    re "It’s better that you didn’t investigate."
    re "Aarya noticed Ophelia was missing and now she’s gone too."

    show rei alright at center
    re "As far as I know, the disappearances are only happening to drama club members, Lucky Rose!"

    na "Mac whispers in fear"

    mac "Oh my god is one of us next?"

    re "...I don’t know."
    re "I can say this though, there is not going to be a play, much less another meeting."
    re "As long as the police are still investigating the disappearances and the fucker taking our friends isn’t behind bars or dead, drama club won’t ever meet again."
    re "Anyone against this?"
    re "I’m not the club leader, but as much as Andrea loved this club and the plays, I know she would prioritize the people over the club."

    show emily desperate at left
    e "Andrea wouldn’t have wanted that, she’s spent so long and has worked so hard, putting her heart and soul into this play."
    e "I know she would have wanted us to perform this play and I’m sure everyone else here does too."
    e "We’re the drama club for a reason, and I’m sure that Aarya and Ophelia would have agreed to do the play too."
    hide ash
    show rose content at right
    ro "You’re right."

    re "What?"

    ro "From what I saw, everyone really put their heart and spirit into this play, everyone really wants to do this play and I don’t think we should drop everyone’s efforts."
    show rei oops at center
    na "Rei sighs"

    re "Fine, We’ll do the play. I’ll... try to go through Andrea’s work, step up and... take over."
    na "Rei turns to Mac and Ash."

    show rei alright at center
    re "You two in? Leave if you want, I don’t blame you, you don’t have to put your life on the line for this."

    hide rose
    show ash sad at right, flip
    ash "No, We’ll do it, Em’s right. We’ve already spent so much time and effort on this."

    na "Rei sighs"

    show rei oops at center
    re "Alright, fine. The play is 6 pm tomorrow, go home guys, stay safe."

    na "The rest of the club leaves. Rei stops Emily and pulls her behind."

    hide ash
    show rei alright at center
    re "Em, stop."
    re "Do you seriously think that this play is worth it?"
    re "Do you want to do this?"
    re "Or is there another reason you’re doing the play?"

    show emily genuine at left
    e "Rei, I want to do this play. "

    re "Rose is forcing you isn’t she?"
    re "I know you two have been close since highschool, but ... haven’t you noticed how different she’s been acting lately?"
    re "If she’s forcing you to do this damn play, tell me and I’ll cancel and make everyone go home."

    e "No, Rei, I want to do this."

    show rei alright at center
    re "Fine, Em. Go home."
    hide emily
    hide rei

    jump last_dance

label sgt_rei_doakes:
    play music "occult_song_tense.mp3"
    scene stage
    show rei alright at center
    na "As people walk into the theatre, Ash and Mac are nowhere to be found."
    na "Emily walks in, with “Rose” following behind her."
    na "They walk backstage, where Rei is there to greet them."

    re "Forced us to do this and showed up 45 minutes late!"
    re "Go get changed, and- oh great you’re here too."
    re "C’mon I’m taking you backstage, if you’re gonna be back here you should at least be out of the way."
    na "Rei takes a hand of “Rose” and leads her backstage."
    hide rei
    play audio "door_slam.mp3"
    na "After Emily is out of sight, Rei forcefully shoves “Rose” into the green room."
    scene backstage
    show rei hyped at center
    show rose worried at right
    na "Rei closes the door, and before “Rose” can react, Rei holds a steak knife up to her back."

    re "Look, I’m gonna give you one chance to explain what the hell you’ve been doing with Emily."
    na "“Rose” winces."
    ro "I – I haven’t done anything."

    re "I don’t have time for denial bullshit - I know you’ve been doing something to her, and I swear to god if you’ve been hurting her I will-"

    ro "I- I would never - UGH!"
    na "Rei’s arm shakes aggressively as he starts to breathe heavily."

    re "Just tell me what you’ve done to us."

    ro "Rei...I’m sorry."

    re "For what!? For what Rose!?"
    na "The pain becomes too much to bear - Catherine loses her hold on her form."

    re "What the-"
    hide rose
    show rei oops at center
    na "Rei hops back. Stunned by the now massive creature before him."

    show catherine startled at right
    re "What are you?"

    show catherine worried at right
    c "I – I don’t know."

    re "What?"
    na "Catherine stammers for a second."

    c "I – I’m a, I’m a vampire."
    show rei oops at center
    re "Holy shit."
    re "Holy shit!"
    show rei hcy at center
    re "you’re the reason!"
    re "The reason all of - did you eat them?"
    re "What the fuck is wrong with you!?"
    re "What made you think you had any right to do this to us, to Em!?"
    re "you’re- you’re a monster."
    show catherine shadow at right
    na "Rei raises the knife. The door behind Rei swings open."

    re "I’ll fucking kill you, I’ll fucking kill you!"
    show rei death at center
    play audio "knife_stab.mp3"
    na "Emily stabs him. Rei convulses, then looks down at the ritual knife plunged through their gut."
    play audio "body_fall.mp3"
    na "As they fall back to the floor, their mouth forms a scowl as they look Emily, dead, in the eyes."
    hide rei
    show emily scolding at left
    na "Catherine and Emily stand in silence for a moment."
    na "Catherine takes Rei’s knife and throws it towards her chest."
    show catherine startled at right
    na "She stops right before her heart, and drops the knife as her hands and arms start to shake uncontrollably."
    show emily desperate at left
    na "Emily goes up and hugs Catherine, trying to block her wounds from bleeding out."
    na "Emily whispers."

    e "Don’t die."
    e "..."
    na "After a few minutes, the bleeding seems to stop. The two look at Rei’s dead body."

    show emily peeved at left
    e "God, how are we gonna get out of this one?"
    hide emily
    hide catherine

    jump endings

label blood_ritual:
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