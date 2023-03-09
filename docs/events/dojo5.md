# The Battle for Kumon-mi
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dojo5&go=Go)



## Event preconditions
✅Ayane love greater than or equal to 5



## Next events
None

## Event properties
* ID: dojo5
* Group: Ayane
* Triggered by label: dojo
* Triggered by branch label: dojo

## Event code
File: \game\AyaneEvents.rpy
Code:
```python
...
label dojo5:
    stop music fadeout 3.0
    scene black
    with dissolve2

    "{i}Legends have it that centuries ago...a single family ruled over all of Kumon-mi.{/i}"
    "{i}Many armies, with the aid of mercenaries and sellswords tried to overthrow this family...{/i}"
    "{i}But every attempt amounted to nothing more than senseless bloodshed and a shameful voyage back home...{/i}"
    "{i}But one day, after hundreds of years and nearly one thousand fruitless attempts..."
    "{i}The family that had once ruled over Kumon-mi...{/i}"
    "{i}Fell.{/i}"
    "{i}And from that moment on...{/i}"
    "{i}They were never able to recover.{/i}"
    "{i}...{/i}"
    "{i}Until today.{/i}"
    "{i}When one girl begins her conquest...{/i}"
    "{i}To reclaim what is rightfully hers...{/i}"
    "Disclaimer: Lessons in Love contains large amounts of information and data that is factually incorrect and no words should be taken as gospel."

    scene karate1
    with dissolve2
    play music "rapid.mp3"

    ay "My name is Ayane Amamiya of the Amamiya family...and I am here to take back what is mine!"

    scene karate2
    with fade

    s "Oh please...You really expect me to believe that a {i}child{/i} like you aims to take back Kumon-mi?"
    ay "Woah, where did that huge lens flare come from?!"
    s "This territory belongs to the Arakawas now, little girl..."
    s "The Amamiyas have had no place here since the...War of...Blood."

    scene karate3
    with fade

    ay "Who are you calling a little girl, you pathetic weakling?"
    ay "The War of Blood may have ended a long time ago, but the stains it left on these grounds have yet to be forgotten."
    ay "Do you have any idea how many lives have been taken with just these hands alone? Because it's more than you could possibly fathom."
    ay "Heed my words, Arakawa. If you have even the {i}slightest{/i} desire to survive, you'll-"

    scene karate4
    with hpunch

    s "I’ll what? Walk away from here and give up on Kumon-mi?"
    ay "Ahh! There are even more of them now!"
    s "You’re out of your mind."
    s "I have spent the last nine thousand years honing my power and-"

    scene karate5
    with hpunch

    ay "What?! Nine thousand?!"
    ay "There is no way that can be right! Can it?!"

    scene karate4
    with dissolve

    s "Nine thousand years is nothing to me."
    s "After all, I was born with..."
    s "{i}That{/i} bloodline..."

    scene karate5
    with hpunch

    ay "What?! {i}That{/i} bloodline?!"

    scene karate6
    with fade

    s "Yes..."

    scene karate7
    with hpunch

    s "{i}THAT{/i} BLOODLINE!!!"

    scene karate8
    with fade

    ay "This can't be...all this time I thought {i}I{/i} was the protagonist, but..."
    ay "If he has {i}that{/i} bloodline..."
    ay "Could this be the end of my journey?..."
    ay "No..."
    ay "It can’t be..."
    ay "Not after all I've sacrificed..."
    ay "I’ve come too far to give up now...there has to be {i}something{/i} I can do..."

    scene karate4
    with dissolve

    s "It’s over, Ayane...I have the high ground."

    scene karate5
    with hpunch

    ay "We’re on the same level! You're just a little taller!"

    scene karate6
    with dissolve

    s "But, you see...that’s where you’re wrong..."
    s "You and I will {i}never{/i} be on the same level..."

    scene karate4
    with dissolve

    s "It doesn’t matter how much you train or how many of my underlings you defeat..."
    s "This is the end of the road. Defeating me isn’t possible..."

    scene karate9
    with fade

    ay "Then you leave me no choice..."

    play sound "static.mp3"
    scene karate10
    with flash
    stop sound

    s "No...It can’t be!"
    ay "It can!"
    ay "You’ve given me no choice but to unleash the Amamiya family’s hidden technique!"
    kin "Amamiya, for the last time, put that thing away! You’re going to get us shut down!"
    ay "Miss Osaka! Turn the fan speed up! My hair isn't blowing fast enough!"
    kin "We don't have a-"
    kin "Wait, where did this giant fan even come from?!"

    scene karate11
    with fade

    ay "I’m sorry things have to end this way..."
    ay "You deserve the death of a warrior, not that of a dog."

    scene karate12
    with fade

    s "Hah..."
    s "Hahahah..."
    ay "...What's so funny?"
    s "Hahahahaha!"
    ay "Wait...No..."
    ay "He {i}can't{/i} be..."

    scene karate13
    with hpunch

    s "But I can..."
    s "You’ve fallen into my trap, little girl."
    s "You see..."
    s "I was born {i}immune{/i} to bullets."

    scene karate5
    with hpunch

    ay "No! That can’t be!"

    scene karate7
    with hpunch

    s "It is!"

    scene karate14
    with dissolve

    "The staredown between the two fierce warriors goes on for hours..."
    "Days..."
    "Weeks..."
    "Millennia..."
    "But the sheer respect for one another’s power is enough to force them into exercising more caution than they ever have before."
    "{i}This{/i} was the moment they had lived for..."
    "The moment to finally prove who the rightful ruler of Kumon-mi is!"

    "{i}How will it end?!{/i}"
    "{i}Who will triumph?{/i}"
    "{i}Will Ayane Amamiya take back the land her family had all but built with their bare hands?!{/i}"
    "{i}Or...{/i}"
    "{i}Will the mysterious ronin, clad only in sweatpants and a T-shirt, be able to fend off the legendary Amamiya fighting style?!{/i}"
    "{i}Find out next time on Lessons in Love ~ The Battle for Kumon-mi!{/i}"

    scene battletwo6
    with dissolve2

    "{i}This program was brought to you in part by Koi Cafe! Home of the [[copyrighted frozen beverage]!{/i}"
    "{i}Long day? Short night? Come to Koi Cafe and try our specialty handcrafted drinks made by adorable girls!{/i}"
    "{i}See you again next time!{/i}"
    "{i}Pluuuuus...EXTRA!{/i}"

    scene black
    with dissolve2
    stop music fadeout 5.0

    "………"
    "……"
    "…"

    scene karateredux1
    with dissolve2
    play music "sakuya4.mp3" fadein 2.0

    ay "So yeah, that’s basically how you do karate."
    kin "Are you two seriously just going to leave this thing here?! What am I supposed to do about this?!"
    s "I feel like I actually did pretty well."
    ay "Yeah, you were surprisingly good. You really had me going with that whole bloodline thing."
    s "Thanks. Came up with that off the top of my head. Totally not a play on a mildly obscure video series from 2009."
    ay "Wow, that seems so long ago."
    s "Yeah. We’re dying faster than we like to admit."

    scene karateredux2
    with dissolve

    ay "Well, you are at least. I’m a perfectly healthy, able-bodied [young_girl] who is going to take back her family’s land through martial arts!"
    s "Just remember, you’ll have to defeat me first."
    kin "Seriously. What the fuck am I supposed to do about this?"
    ay "Pfft. You make it sound like defeating you is supposed to be a challenge."
    s "It will be now that you know I’m immune to bullets."
    s "Also, where the hell did you get that gun? It looked real."

    scene karateredux3
    with dissolve

    ay "There are three things you never ask a lady, Sensei! Her age, her weight, and where she got her automatic rifle."
    s "I don’t remember ever learning about that last one."
    ay "Then maybe it’s time to start studying up!"

    scene karateredux2
    with dissolve

    ay "When you aren’t too busy training to defeat me, I mean."
    s "Right, right."
    s "Anyway, we should probably get a move on before the instructor asks us to do something about the industrial size fan you had air lifted here for our sparring match today."
    ay "Yeah. It's a good thing she hasn't noticed it yet."

    scene karateredux4
    with dissolve

    kin "I want this thing gone in ten minutes or the two of you aren't allowed back anymore."

    scene karateredux5
    with dissolve

    ay "..."
    s "..."
    ay "I'll call in another helicopter..."

    scene black
    with dissolve

    "Ayane and I finish up our ‘karate’ routine for the day and change back into our normal clothes while waiting for the helicopter to arrive."
    "Unfortunately, she has to feed her chicken after this, so the two of us need to break apart and go our separate ways."
    "Without anything left to do, I depart the dojo and begin to wander the streets in search of something to close out the day with..."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ dojo5 = True

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"

    jump saturdaynight

label dojo10:
...
```

## Code that triggers this event
File: \game\AyaneEvents.rpy
Code:
```python
...
label dojo:
    if ayane_love >= 0 and firsttimedojo == False:
        jump firsttimedojo
    if ayane_love >= 5 and dojo5 == False:
        jump dojo5
...
```