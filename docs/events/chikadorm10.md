# Side Event (Chika)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Chika love greater than or equal to 10

* Event [Behind The Curtain](./mall10.md) (Chika) is completed)

* Event [Something About Biting](./chikadorm5.md) (Chika) is completed)



## Next events

* [Chika: A Castle for Everyone](./chikadorm15.md)

## Event properties

* Id: chikadorm10
* Group: Chika
* Triggered by label: chikadorm
* Triggered by branch label: chikadorm
* Triggered by path: chikadorm->chikadorm10

## Official wiki page

[Side Event](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikadorm10&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label chikadorm10:
    play sound "knock.mp3"

    s "Chika, are you home?"
    c "Sensei? Is that you?"
    s "Have other men with similar voices been visiting your room lately?"
    c "Hold on a sec, I’m not wearing any-"
    c "Ahh, whatever. Just come in."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I open the door quicker than normal after registering the whole “not wearing any [[blank]” thing."
    "Normally, that phrase isn't succeeded by “Ahh, whatever,” which makes me a bit skeptical, but I'm not about to question that when I know Chika is just a few feet away not wearing {i}something.{/i}"

    scene chikapjs1
    with dissolve

    c "Hey. You're here late today."
    s "And you don't have any pants on."

    scene chikapjs2
    with dissolve

    c "Yeaahhh...Is that okay? I was gonna put some on when I realized it was you, but I just got out of the shower and I’m a little too comfortable right now, sooo..."
    s "I'm fine with it if you are. I just expected you to be a little more...on edge or something."

    scene chikapjs3
    with dissolve

    c "Hmm...well, maybe if you took {i}your{/i} pants off as well, we could even out the playing field and {i}both{/i} be on edge!"
    s "Deal."
    c "Wait, what?"

    if bonus == True:
        "I reach for my belt and-"

        scene chikapjs4
        with dissolve

        c "Woah! Wait a second, Sensei! I was obviously kidding! You can’t take your pants off in here!"
        s "I can't?"
        c "No!"
        s "I don't understand that at all."
        c "This is my room! Only I'm allowed to be pantsless! And obviously Yumi, but she's not here yet! But she could be! Which is why you have to keep your pants on!"
        s "I feel like the amount of trouble we'd get into with her really doesn't change much based on {i}how many{/i} of us aren't wearing pants. We'd be screwed by any combination of that."
        c "Exactly! And we can't even play the boyfriend/girlfriend card because...well, we aren't boyfriend and girlfriend!"

        "I sigh to myself and accept that my pants will have to remain on tonight."
        "Life is unfair."

        scene chikapjs4r
        with dissolve

        c "Jeez...if I knew you were gonna be in perv-mode tonight, I would've just bit the bullet and put on pants after all."
        s "Forgive me for not being able to properly contain myself around a bottomless, cute girl."

        scene chikapjs2
        with dissolve

        c "You’re gonna have to, Sensei. We can't start doing stuff like that until we've gone on a few dates first."
        s "How many dates do you think we can fit in before Yumi comes home?"
        c "Zero. But we can watch TV or something and that's like, {i}kind of{/i} a date by modern standards."
        s "Is pantsless Chika really inviting me onto the bed in her current state?"

        scene chikapjs5
        with dissolve

        c "Pantsless Chika is inviting you onto the bed for a night of wholesome bonding that may or may not lead to a small dose of cuddling if you play your cards right."
        c "And she's also going to need you to get onto the bed first so you can't try and see what she's hiding underneath her shirt."
        s "You're being extremely unfair tonight."
        c "It's easier to put your foot down when your legs aren't being weighed down by pants."
        s "That is a yearbook quote if I've ever heard one."
        c "Just shut up and get onto the bed, Sensei..."
    else:
        s "You'd be cuter if you were a clown."
        c "Yeah, I know."
        c "Anyway, wanna watch TV or something?"
        s "I want to watch Pawn Stars."
        c "Okay, we can watch Pawn Stars."

    scene black
    with dissolve2

    if bonus == True:
        "I do as Chika says and lie down on the edge of her bed, making sure to give her enough room to get in behind me."
        "She runs over to the lights and switches them off before following suit and taking her place beside me."
        "She reaches over me to grab the remote and put on whatever channel she's decided to watch tonight and, before I know it, she has her hand on my arm."

        scene chikapjs6
        with dissolve

        c "No looking over here at any point, got it?"
        s "Why am I allowed to watch you in the dressing room but not in the safety of your own bed?"
        c "You didn’t watch me get dressed, you just came in after. That's like, a totally different thing, Sensei."
        c "Besides, you’re gonna see me in lingerie soon anyway, so just hang on until then, kay?"
        s "Soon? How soon?"
        c "I don't know. Sometime before you retire."
        s "Next week is actually my last. I have decided to leave the work force."
        c "Don't even joke about that. I don't want to imagine what life would be like with a normal teacher again."

        "There are five girls on the TV in what appears to be some sort of reality show."
        "None of them seem to be aware that they're being filmed."
    else:
        "Chika and I hop onto the bed, staying as far away from each other as we can, and she puts on Pawn Stars."

    s "What are we watching right now?"

    if bonus == True:
        c "Idunno. It just sorta came on in the middle of some other show I was watching. I don't really get it, but it looks kind of creepy so I kept it on."
        s "Are you actually into stuff like this, Chika?"

        scene chikapjs7
        with dissolve

        c "What, you mean like, horror? "
        s "Horror. Thrillers. Whatever you want to call them."
        c "Mhm. Yumi and I used to watch stuff like this all the time when we first moved in."
        c "Did you know that she’s actually kind of a scaredy cat when it comes to movies?"
        s "Honestly, that doesn't really surprise me."

        scene chikapjs8
        with dissolve

        c "How about you, Sensei? Do you like stuff like this?"
        s "Eh...I don't have much of an opinion. I’m fine with pretty much anything."
        s "Ami's terrified of stuff like this, though, so it's not something I really get to see all that often."

        scene chikapjs9
        with dissolve

        c "What’s it like getting to live with Ami? Does she like, make you breakfast and stuff?"
        s "Every morning. She’s pretty great at it too."
        c "Really? I guess that doesn't surprise me."

        scene chikapjs10
        with dissolve

        c "It’s a little embarrassing, but...I’m a pretty decent cook too, you know?"
        s "Why is that embarrassing?"
        c "Just cause it's like, one of those things no one really knows, I guess."
        c "Like I'm letting you see a part of me I haven't let anyone else see before."

        scene chikapjs11
        with dissolve

        c "I’ve...never really had a guy around that I could open up to, you know? Let alone one that I-"
        c "Uhh..."
        s "One that you what?"
        c "..."
        c "Respect."
        s "..."
    else:
        c "Pawn Stars."
        s "Oh, right."

    "A minute or two without any conversation passes by as the two of us fixate on the TV."

    if bonus == True:
        "The girls in the house become increasingly panicked as they begin to search for something."
        "I can’t really make out what any of them are saying over a loud buzzing noise coming from the speakers, but it looks like one of them might be crying."
        "It makes me feel incredibly uncomfortable."
        "..."
        "I have to focus on something else."

    s "Have you really never had anyone like me to open up to before?"

    if bonus == False:
        c "Wtf"
        s "Sorry."

    c "What, you mean like, a guy?"
    s "Yeah."
    c "Not really, no. My dad left when I was still really little."
    c "It’s fine, though. I'm not really beat up over it. In fact, I think it's kind of better having {i}no{/i} dad than one that treats you like shit."
    c "I guess it did impact me in some way, though. Like, that’s probably why I told you I wanted someone dependable when you asked me what kind of guys I liked."
    c "I don’t want someone who’s just gonna up and leave me with a kid one day, you know?"
    s "You want kids?"

    scene chikapjs10
    with dissolve

    c "I think so. Babies are cute."
    c "I haven't really put {i}much{/i} thought into it yet, though, so I guess my outlook could always change."
    c "I've just got a little too much on my plate right now to worry about something like that."

    "The show continues on."
    "There is something in the attic."

    scene chikapjs11
    with dissolve

    c "..."
    s "..."
    c "Sensei?"
    c "I-"

    stop music
    play sound "phonering.mp3"
    scene chikapjs13
    with hpunch

    c "Oh my- are you fucking kidding me right now?"
    s "You what?"
    c "Nothing...Hold on just a sec."

    scene black
    with dissolve
    stop sound
    play sound "phonebeep.wav"

    c "Hello?"

    "An urgent voice leaks out of the phone and oozes into Chika's ears."
    "I turn around to make sure that everything is okay and take notice of the sudden change of color in her eyes."
    "It all fades away."

    c "…"
    s "…"
    c "Okay..."
    c "Okay, just calm down. I’ll head over right now."
    c "…"
    c "Thanks."
    c "..."
    c "Yeah."
    c "..."
    c "See you soon..."

    scene chikapjs14
    with dissolve

    "Chika gets off of the bed and I follow her to the door. I already know what she’s about to say."

    c "I’m really sorry, but I have to go..."
    s "No need to apologize. Is everything okay?"
    c "Yeah. Yeah, I think so..."
    c "Everything will be fine. I just have some stuff I need to do."
    s "Do you...want me to come with you?"

    scene chikapjs15
    with dissolve

    c "Sensei...It’s the middle of the night. I’m not gonna make you come all the way across town with me..."

    "All the way across town? What exactly does Chika need to do at this hour?"
    "There's no way I can just leave her alone for something as serious as this."

    s "And {i}I’m{/i} not going to let you travel that far without someone to look after you."
    c "I do it all the time, Sensei. It’s fine. Really."
    s "This isn't something I'm going to back down from, unfortunately."
    c "Sensei..."
    s "Just hurry up and get dressed. Whatever that call was sounded urgent."
    c "...Okay."
    c "Just..."

    scene chikapjs14
    with dissolve

    c "Look away first?..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    play sound "static.mp3"
    scene p1 with flash
    scene p2 with flash
    scene p3 with flash
    scene p4 with flash
    scene chikapjs16
    with flash
    stop sound
    play music "blueair.mp3"

    if day44 == True:
        "And so I find myself back in the second half of town."
        "The one filled with dilapidated buildings and feelings I've since forgotten."
        "..."

        if bonus == True:
            "This is where I kissed Yumi."
            "I thought about [raping] her that day."
            "I didn't do it, but I thought about it."
            "I thought about her unlubricated virgin slit and what pain it would cause both of us for me to enter without invitation."
            "I thought about [raping] her that day."
            "I didn't do it, but I thought about it."
            "She'd probably get wet within a matter of minutes. She can't hide it from me."
            "I didn't do it, but I thought about it."
            "Because I’m a good person."
            "I stole her first kiss."
            "Everyone wins."
            "I came so hard that night."
            "The dry friction of the bedsheets wrapped around my cock still stings to this day."
            "Tonight, I will have more thoughts."
            "I wonder what will come of them."
        else:
            "This is where I hugged Yumi."
            "I shouldn't have done that."

    else:
        "Chika brings me to a place I haven’t seen before."
        "It’s another half of Kumon-mi, much more run-down than the one I’m used to."
        "It’s filled with dilapidated buildings and riddled with homeless people."
        "They cling to the sides of the streets like flies on a tape-trap."
        "I’m glad I came with her tonight."
        "These people could have done horrible things to her."
        "The same sorts of things I dream to one day do."
        "But I will have her trust- which is more than flies could ever hold."
        "I am the only person allowed to do horrible things to this girl."
        "I will take her virginity and hang it on the walls of my hippocampus as if it is some sort of trophy."

    c "…"
    s "Are you okay?"
    c "Yeah...Just worried. That’s all."
    c "Thanks for coming with me, Sensei."
    c "Even though I do it all the time...I really don’t like walking around here alone at night."
    c "I...kinda had a feeling you’d come no matter how much I refused, though."
    c "We’re...getting pretty close, aren’t we?"
    c "You might have to learn some things about me."
    s "What sorts of things?"
    c "Nothing bad. Just...depressing or whatever."
    c "I’m sure I don’t have to tell you this but...please, {i}please{/i} don’t tell anyone about tonight, okay?"
    c "I don’t even want to think about what would happen if the[school] found out."

    "For some reason, words suddenly have a hard time crawling out of my throat."
    "The air in this half of town is remarkably thick."
    "It makes me think and say things I normally wouldn’t. Things that get stuck."
    "This is a side event. I can’t make any mistakes here or Chika's affection level won’t rise and I won't be able to cum inside of her."

    s "Can you at least tell me what's going on?"
    c "Yeah...maybe. I don't know. It’s just..."
    c "It's weird to talk about. Like, I know it’s just gonna shock you and make you think I’m biting off more than I can chew or something."
    c "But...I can handle it."
    c "Really."
    c "I don’t know."
    c "Life sucks, I guess."

    "I am glad she learned early."
    "It gives her time to break her nails while attempting to unearth the few things in life that can distract us from the underlying misery in all things."
    "The things that make life better."
    "The things we can not speak of."

    s "Yeah, but I’m here for you."
    s "And no matter what you’re hiding, I’ll help keep it a secret."
    c "Thank you..."
    c "That really does make me feel a lot better."

    "Chika suddenly stops in front of a rundown apartment building."

    play sound "static.mp3"
    scene chikapjs19r
    with flash
    stop sound
    stop music

    "She looks lovely in the moonlight."

    play sound "static.mp3"
    scene chikapjs19
    with flash
    stop sound

    c "This is far enough."
    c "Thanks again for coming with me, Sensei. Really."
    c "I might not be in[school] for the next few days, so just give any of my homework or handouts or whatever to Yumi."
    c "If...she shows up, that is."
    s "Will do. Feel free to let me know if you need anything."
    c "I will."
    c "Thank you."

    play sound "static.mp3"
    scene chikapjs19r
    with flash
    scene chikapjs19
    with flash
    scene chikapjs19r
    with flash
    scene chikapjs20
    with flash
    stop sound

    c "There’s something else I wanna do before I go, too."
    s "What’s that?"
    c "I want to kiss you."

    if bonus == False:
        s "Gasp."

    c "It’s okay, right?...I mean, it's pretty obvious we like each other."

    if bonus == True:
        s "Aren’t you supposed to be in a hurry?"
        c "Kissing doesn’t take long."
    else:
        s "I don't know. Kissing is kind of gross."
        c "No it's not."

    s "Well, you're right about that. But it still doesn't really seem like the time-"
    c "Can I, Sensei?"
    s "…"
    c "…"
    c "Can we kiss?"

    "6e 6f 74 68 69 6e 67 20 66 61 6c 6c 73 20 62 75 74 20 6d 65"

    menu:
        "=)":
            s "…"
            c "…"

            "Chika and I stare into each other’s eyes for what feels like forever."
            "She reaches out and grabs the collar of my shirt."
            "She pulls me closer."

            scene black

            "We kiss softly for a total of seven seconds."

            if bonus == True:
                "There is no tongue involved."
                "I go home shortly after."
            else:
                "It feels kind of weird and I start sweating."

            $ renpy.end_replay()
            $ chikatownfirst = True
            $ chikadorm10 = True
            $ chika_love += 1
            $ howifeel = True
            stop music fadeout 5.0

            "{i}Chika’s affection has increased to [chika_love]!{/i}"
            "{i}There is something buried underneath your feet.{/i}"
            "{i}Why haven’t you found it yet?{/i}"

            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

        "=(":
            s "…"
            c "…"

            "Chika and I stare into each other’s eyes for what feels like forever."
            "She reaches out and grabs the collar of my shirt."
            "She pulls me closer."

            scene black

            "Nothing happens."
            "I have made a mistake."

            play sound "static.mp3"
            scene happy1 with flash
            scene happy2 with flash
            scene happy3 with flash
            scene happy4 with flash
            stop sound

            "Life is all about being happy."
            "I heard that somewhere."
            "And one day, I will know how it feels."
            "But, for now-"

            if bonus == True:
                "I will continue to [masturbate] until my dick turns to pulp."
            else:
                "I will go home and watch more Pawn Stars."

            "That is the only happiness I know."

            $ renpy.end_replay()
            $ chikadorm10 = True
            $ howifeel = True
            stop music fadeout 5.0

            "{i}Chika’s affection has not increased!{/i}"
            "{i}You have gained nothing from this event!{/i}"
            "{i}There is something buried underneath your feet.{/i}"
            "{i}You are a coward who will never find it.{/i}"

            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label chikadorm15:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label chikadorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if chika_love >= 5 and day == 1 and chikadorm5 == False:
                "I should probably wait until Yumi's not right there to hang out with Chika..."
                jump doorknock
            if chika_love >= 5 and day != 1 and day != 3 and firsttimemall == True and chikafirsthall == True and chikadorm5 == False:
                jump chikadorm5
            if chika_love >= 10 and mall10 == True and chikadorm5 == True and chikadorm10 == False:
                jump chikadorm10
...
```