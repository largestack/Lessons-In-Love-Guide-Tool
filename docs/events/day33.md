# So Many Voices
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day33&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 33



## Next events
None

## Event properties
* ID: day33
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\script.rpy
Code:
```python
...
label day33:
    scene newdespacito1
    with dissolve
    play music "justbehappy.mp3"

    a "So...are you excited, Sensei?! This will be your first time coming with us to karaoke."
    s "I don't know if {i}excited{/i} is the word, but it beats doing nothing."
    ay "Are you planning on singing?"
    m "{i}As if you would let him...{/i}"
    s "Me? Not a chance. I'm just tagging along to watch."
    s "You three can just forget I'm even there if that makes things easier for you."

    scene newdespacito2
    with dissolve

    ay "Absolutely not! I demand that you keep your eyes on me at all times and never even {i}suggest{/i} that I forget about you ever again."
    ay "Besides, you not singing just means that I’ll have to sing hard enough for the two of us."
    m "Why, though? You’re just going to sing the same song you always do..."

    scene newdespacito3
    with dissolve

    ay "It’s a good song and you know it, Maya!"
    a "Heheh...heh..."

    "So, I bet you’re wondering how I wound up in this predicament."
    "Me too."
    "All I know is that I was about to head home and that Ayane wound up grabbing me by the arm and forcibly dragging me to meet up with the other girls."
    "I didn't even realize we were going to a karaoke booth until a couple minutes ago."
    "As you may have guessed, Maya didn’t agree to this."
    "But seeing as she was promised food, she was unable to refuse. And now their typical friend group has been met with an unhealthy abundance of testosterone out of virtually nowhere. "
    "Luckily, Ami and Ayane both want me here, so...sucks to be Maya, I guess."

    scene newdespacito4
    with dissolve

    a "Anyway...I'm not going to blame you for not wanting to sing, Sensei. I know that's not really your thing."
    ay "Do you know Spanish? Maybe the two of us can do a duet?"
    s "Do...{i}you{/i} know Spanish?"
    m "Oh, she knows it alright."
    ay "Can you {i}fake{/i} Spanish?"
    s "Probably not without sounding extremely racist, so I'm going to abstain."
    m "This is the best news I have heard all year."
    s "Rude."

    scene newdespacito5
    with dissolve

    m "Am I wrong, though? Even Ami admitted that this isn't your thing and Ami is literally obsessed with you."
    ay "It's true. She really is."
    s "Like you're one to talk."
    a "Maya, just because you’re really good at singing doesn’t mean you get to make fun of people who aren’t."
    m "Ami, please. Can you really imagine even a halfway decent singing voice coming from {i}him?{/i}"
    ay "I can."
    m "You don't have the right to weigh in. You're just as bad as he probably is."
    s "Sorry, did I hear just now that Maya is actually a good singer?"

    scene newdespacito6
    with dissolve

    a "She's actually really amazing. Most of the time she just eats, though."
    m "I’m much better at that."
    ay "Sensei, don't listen to what Maya said about me. She knows that I'm the real best singer here."
    ay "And as soon as you hear the special song I'm going to dedicate to you today, you'll know it as well."

    scene newdespacito7
    with dissolve

    a "Wait, are you actually going to sing something different today, Ayane?"
    ay "Huh? Of course not. Do other songs even exist?"
    a "You’re..."
    a "You're going to dedicate {i}that{/i} song to him?..."
    ay "Of course. It will make it all the more romantic when we eventually walk down the aisle to it."

    scene black
    with dissolve2

    "We walk for another ten minutes or so before finally arriving at the karaoke bar."
    "Maya and Ayane go into the room first and I attempt to follow them in, but Ami grabs my sleeve and pulls me aside before I have the chance to..."
    "........."
    "......"
    "..."

    scene karaoke1
    with dissolve

    a "Okay, so before we go in there, I just want you to know a little about proper karaoke etiquette."
    s "There’s ‘karaoke etiquette?’ What does that even mean?"
    a "It means that you’re supposed to stay super-duper positive and cheer for whoever sings even if they’re really, really bad."
    a "Like...{i}really, really{/i} bad..."
    s "Is Ayane really that terrible?"

    scene karaoke2
    with dissolve
    stop music fadeout 10.0

    a "Well, uhh..."
    a "No, actually..."
    a "Her voice is really nice and...she's got good rhythm."
    a "But, uhh...her song choice is..."
    a "Um..."

    scene karaoke3
    with dissolve

    a "You know what? Why don't we just go in there and...let you see for yourself?"

    scene black
    with dissolve2

    "I have a very bad feeling about this..."
    "........."
    "......"
    "..."

    scene karaoke4
    with hpunch
    play music "letsfuckingo.mp3"

    ay "OKAY, BITCHES! THIS ONE IS CALLED DESPACITO AND IT’S DEDICATED TO MY FUTURE HUSBAND AND BEST FRIEND'S UNCLE!"
    ay "LET'S FUCKING GO!"
    a "Do you see what I mean now, Sensei? Do you finally understand?"
    s "Why is this happening?"

    scene karaoke5
    with dissolve

    ay "DES-PA-CITO. Quiero respirar tu cuello DESPACITO."
    ay "¡Deja que te diga cosas al oído!"
    ay "¡Para que te acuerdes si no estás conmigo!"
    s "Why would you do this to me?"
    a "To...spend more time with you?"

    scene karaoke6
    with hpunch

    ay "DES-PA-CITO."

    scene karaoke8
    with fade

    "Ami takes a seat beside Maya, who is obviously significantly more prepared for this than either of us."

    s "You guys really let her do this every time you come here?"
    a "Hahahah...Yeah..."
    s "She’s already selected it like four more times after this."
    a "We’ve found that it’s best to just let her get it out of her system as soon as possible."
    ay "¡DES-PA-CITO! Quiero respirar tu cuello DESPACITO."
    s "Her Spanish is surprisingly good."

    scene karaoke7
    with dissolve

    a "Right? I think her butler must have taught her because our school doesn't even offer a Spanish class."

    scene karaoke9
    with dissolve

    m "Can we order food now? I’m really hungry and you promised me dinner."
    a "Huh? Oh, right. What do you want?"
    m "What? You're going to have to speak up. I'm currently protecting myself from bodily harm."
    a "Oh, forget it. I'm just going to make you come with me anyway."
    m "What? I can't hear you."

    scene karaoke10
    with dissolve

    a "Sensei, do you want anything? It’s on me today."
    s "I don’t think I’m supposed to let my [niece] buy me dinner."
    a "But you let me {i}make{/i} you dinner all the time. I don't see how this is that much different."
    m "Seriously, what are you saying?"
    s "You know what? Good point. Just get me whatever you're having."

    scene karaoke10r
    with dissolve

    a "Roger that. The phone in this room is broken and Maya orders way too much anyway, so...watch over Ayane for me while I'm gone?"
    s "Wait, what?"

    scene karaoke11
    with hpunch

    ay "¡DESSS-PAAA-CITO!"
    a "Sorry, Sensei! I love you!"
    a "Please hang in there!"
    m "What? What are we hanging on? Ami, I really can't hear-"
    a "TAKE OFF THE HEADPHONES THEN, MAYA! COME ON!"

    scene black
    with dissolve2

    ay "THANK YOU, LADIES AND GENTLEMEN. THIS NEXT SONG IS A BRAND NEW ONE."
    ay "IT’S CALLED “DESPACITO” AND IT'S ALL ABOUT HOW MUCH I LOVE SENSEI!"
    ay "ONE, TWO, THREE, FOUR!"
    ay "DESPAAAA-"

    "Ami and Maya disappear for what feels like years."
    "There is no one left in this world that I can trust."
    "I fall victim to the darkness and lose myself."
    "Despacito consumes me whole."

    $ renpy.end_replay()
    $ day33 = True
    $ ami_love += 1
    $ ayane_love += 1
    $ maya_love += 1
    stop music fadeout 8.0

    "{i}Ami's affection has increased to [ami_love]!{/i}"
    "{i}Ayane's affection has increased to [ayane_love]!{/i}"
    "{i}Maya's affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    jump endofweekday

label day36:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
...
```