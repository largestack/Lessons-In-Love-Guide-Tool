# Nightvision (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 10



## Next events

* [Main: A Proper Introduction](./day150.md)
* [Happy scenes: Everything is Connected](./everythingisconnected.md)
* [Miku: You and Me and the Night](./mikudorm10.md)

## Event properties

* Id: soccer10
* Group: Miku
* Triggered by label: soccerfield
* Triggered by branch label: soccerfield
* Triggered by path: soccerfield->soccer10

## Official wiki page

[Nightvision](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=soccer10&go=Go) for more details.

## Event code

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label soccer10:
    scene soccerfield
    with fade
    play music "highspeedprinter.mp3" fadein 3.0

    "I make my way onto the soccer field in a slightly better mood than normal- probably on account of how many thighs I am going to see today."
    "Perhaps it's a little more than that, though?"
    "Perhaps I actually {i}enjoy{/i} spending time with Miku and...trying to keep up with her bullet-train of thought or something?"
    "Hell, at this rate, I might actually wind up becoming the coach of this team."
    "That is, assuming it doesn't hurl a wrench at my {i}extremely busy{/i} schedule as the world's worst teacher."
    "Does that analogy still work when the wrench is being thrown {i}at{/i} something rather than inserted {i}into{/i} something? I don't know."
    "Besides, how busy can coaching a girls’ soccer team possibly be when they don’t even play any games?"

    mi "Senseiiiiii!!!!!"

    with hpunch

    "I’m suddenly assaulted as Miku crashes into my back at full speed."
    "She does her best to wrap her arms around my abdomen in an alarmingly friendly greeting hug, but doesn’t find much success as her hands can barely touch one another."

    mi "Woah! Your abs are super hard, Sensei. I knew you were muscley, but this makes it seem like you're some kinda bodybuilder or somethin'."
    s "Nope. Not even close. The only exercise I ever really get is just...walking around town."

    scene nightvisionredux1
    with fade

    "Miku releases her death grip on my suspiciously hard abdomen, allowing me to turn around and actually face who I'm speaking to."

    mi "You know, if ya ever wanna get some more exercise, I’m always around!"
    mi "Maybe I could be your personal trainer or somethin'? First three lessons are free."
    s "{i}I{/i} would need to be paid in order to convince me to run with you, Miku. That is not a thing I...ever want to do."
    s "At least not until you learn to calm down a bit."

    scene nightvisionredux2
    with dissolve

    mi "Oh, come on! You think I’m some kinda slave-driver or somethin'?"
    mi "I’m totally fine with just joggin' if your stamina ain't all that great. That's what I have to do with Makoto whenever I can convince her to come with me."
    mi "Heck, I could even give ya a piggyback ride if you get tired!"
    s "I would literally crush you."

    scene nightvisionredux3
    with dissolve

    mi "Nuh-uh! I could totally lift you up!"
    s "Please don't try."
    mi "Well, I kinda have to now."
    s "You really don't."

    scene nightvisionredux4
    with dissolve

    mi "Prepare for liftoff, Sensei!"

    "Miku once again takes position behind me and wraps her arms around my body. Or at least...tries to."
    "She arches her back and bends her knees, attempting to lift me up, but obviously failing due to the fact that I’m more than double her weight."

    mi "Guh...What the heck is this? How are you this heavy? I can lift up Kirin just fine."
    s "I have no idea who Kirin is, but I am going to guess she is not a six foot male with suspiciously hard abs."

    scene nightvisionredux5
    with dissolve

    mi "Maybe I should practice on her sister before I try pickin' you up again?"
    s "Maybe. Or, here's an even better idea, you could just...give up."
    mi "Whatever. I know when to accept defeat. "

    scene nightvisionredux1
    with dissolve

    mi "But yeah! If ya ever wanna run around or anything like that, I promise I won’t blow ya out of the water!"
    mi "Or if you just wanna come grab a snack with me and Makoto, that’s okay too!"
    s "Did Makoto pay you to say this?"

    scene nightvisionredux2
    with dissolve

    mi "Hahaha! Not this time, I promise! This invitation is 100%% Miku-approved!"

    scene nightvisionredux1
    with dissolve

    mi "It's only a matter of time 'til you become our coach, so we should probably start gettin’ to know each other better anyway, right?"
    s "You sound pretty confident that this is a thing I’m going to eventually do."
    mi "I am confident! Why else would ya keep showin’ up here?"
    s "You do realize I'm a teacher right? Being at school is kind of my job."
    mi "Mhm! But have you ever seen any other teachers around here over the weekend?"
    s "Actually...no. I haven’t."
    mi "Yeah, that's what I thought! Take a friggin' day off sometime, Sensei!"

    "Huh...I can't tell if it's weird that I've yet to bump into any other teachers around here yet."
    "I've obviously seen some other staff members around, but...none on the weekend."
    "Which...I guess makes sense if there aren’t any other clubs with weekend practice."

    scene nightvisionredux6
    with dissolve

    mi "All jokin' aside, we kinda need you, Sensei!"
    mi "The other teachers don’t really care about our team now that the normal coach is havin’ her baby and stuff."
    mi "I've heard from some of the other girls that they're calling our club pointless without any real opponents."
    s "I mean...isn't it?"
    mi "Heck no! That ain't it at all! We're all here for one reason and one reason only! To be a part of a team and to have fun playin' soccer."
    s "That would be two-"
    mi "Bein’ part of a team means hangin’ out and practicin’ every day...and helpin’ each other through tough times!"
    mi "We're like a big family over here!"

    "A family, huh? I guess I can see that."
    "That reminds me, I don’t really know anything about Miku’s family yet."
    "I wonder what they’re like?"

    s "Hey Miku, I was wondering-"

    play sound "whistle.mp3"
    scene nightvisionredux7
    with hpunch

    mi "GUH! Can't we invest in a...quieter whistle or something?"
    sg "Miku! We still need those extra cones for our drills! Can you get them or should I just send Kirin instead?!"
    s "Oh, good. A chance to find out if Kirin is actually a six foot male."
    mi "Shoot. I totally forgot I was supposed to be doin’ stuff."
    s "Aren’t you the captain? Why’s that tall girl bossing you around like that?"
    mi "I’ll get em in one sec! Sorry about that!"

    scene nightvisionredux6
    with dissolve

    mi "That tall girl is Karin Kanda. She’s the vice-captain of the team and ain't really tryin' to boss me around."
    mi "She’s been wantin’ to try more of that ‘bein’ in charge stuff’ lately, so I figured I’d let her take the reins today."

    scene nightvisionredux1
    with dissolve

    mi "Oh! Here's an idea! Wanna help me carry all the cones out so we can get back to talkin' faster?"
    mi "Your arms are a lot bigger than mine so we can probably do it all in one trip with the two of us!"
    s "Sure. I don't see any problem following a teenage girl into a dark storage room with tons of other girls watching."

    scene nightvisionredux6
    with dissolve

    mi "Problems? Whatcha mean? "
    s "…"
    s "Nothing at all, Miku. Just lead the way."

    scene black
    with dissolve2

    "Miku starts sprinting over to a storage room attached to what I believe is the school gym and I am forced to jog just to keep up with her."
    "I think about looking behind me to see if anyone is watching but, after realizing that might make me look even {i}more{/i} suspicious, I elect to keep my head down instead..."
    "........."
    "......"
    "..."

    scene painisreal1
    with dissolve2

    mi "So! Here we are! Home sweet home!"
    s "Would you mind explaining to me why we just stepped over a mattress?"
    mi "Doesn't every storage room need a mattress?"
    s "...No?"
    mi "I obviously know that, Sensei. The mattress is just a thing Kirin set up so she could slack off during practice."
    mi "Pretty sure she dragged it here by herself and none of us wanna get rid of it, so...I guess we've just got a mattress now?"
    mi "Kinda works out, though, since the storage room doubles as our medical tent thingy for now."
    s "Isn’t the actual nurse’s office connected to the soccer field?"
    mi "Yeah, but she doesn’t come in on weekends."
    s "Huh..."

    scene painisreal2
    with dissolve

    mi "You got some kinda problem with mattresses, Sensei? Yer actin' all weird all of a sudden."
    s "Nope. If anything, I'm glad to have such a convenient mattress stashed away in such a discreet location."
    mi "For what? You gonna sneak in here to take naps during school or something?"
    s "Close. I'm sure you’ll find out eventually."

    scene painisreal3
    with dissolve

    mi "Well, Idunno what the heck you’re talkin’ about, but I’m gonna start grabbin’ some cones."
    mi "If we’re in here for too long, the girls might get the wrong idea or somethin’."

    scene painisreal1
    with dissolve

    mi "You start grabbin’ all the ones in the corner near the door and I’ll get the ones over here in the back, got it?"
    s "Got it."

    scene painisreal4
    with fade

    "I turn around and begin searching my side of the room for any cones we might be able to use for the girls’ drills."
    "I can make out one tucked away behind a-"

    stop music
    play sound "imscared.mp3"
    with hpunch

    s "...!"
    s "Jesus...what the fuck was that?"
    sg2 "Sorry, sorry! Rogue soccer ball! Everything's okay!"

    "I can hear a set of footsteps outside of the door as one of the girls comes over to retrieve the apparently {i}rogue{/i} soccer ball."
    "I guess someone must have kicked it a little too hard or...too far or something and it wound up bouncing off of the door."

    s "Shouldn't they be playing a little more...I don't know, carefully?"
    s "You guys might wind up breaking something at this rate."
    mi "..."
    s "..."
    s "Miku?"

    play sound "static.mp3"
    scene help
    with flash
    stop sound

    "67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20
    67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20
    67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 67 65 74 20 61 77 61 79 20 "
    play sound "static.mp3"
    scene help2
    with flash
    scene painisreal5
    with flash
    stop sound
    play music "painisreal.mp3"

    mi "{i}Hah...hah...hah...hah...hah...hah...ahhhhh...{/i}"
    s "…"

    play sound "static.mp3"
    scene help3
    with flash
    scene painisreal6
    with flash
    stop sound

    mi "{i}Hahhhh...Ahhh...ahhhhh...hahhhhh...AHHHhhh..AHHH...HAHHHHHH...{/i}"
    s "…"

    play sound "static.mp3"
    scene help4
    with flash
    scene painisreal7
    with flash
    stop sound

    mi "{s}AHHHH!!!!AHHHHAHHHHAH!!!HAHHAHHH!!!h{/I}"

    play sound "static.mp3"
    scene help5
    with flash
    scene painisreal8
    with flash
    stop sound

    mi "{b}AAAAAAAAHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH!!!!!{/i}"

    "I’m frozen in place as I watch Miku begin to claw at her scalp with her fingernails."

    mi "{i}Ahhhh.....hah...hah......AHHHHH!!{/i}"

    "She won’t stop screaming."

    play sound "static.mp3"
    scene happy1
    with flash
    scene happy2
    with flash
    scene happy9
    with flash
    stop sound
    scene painisreal8

    s "Miku...what’s going-"

    play sound "static.mp3"
    scene help5
    with flash
    scene painisreal9
    with flash
    stop sound

    mi "{b}DON’T COME NEAR ME!{/b}"

    play sound "static.mp3"
    scene painisreal8
    with flash
    stop sound

    mi "GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY"
    mi "GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY GET AWAY"

    play sound "static.mp3"
    scene happy1
    with flash
    scene happy2
    with flash
    scene happy9
    with flash
    stop sound
    scene painisreal10

    "A world without light, where nightvision plays messiah."
    "Where good little boys and good little girls are gifted with forgiveness."
    "Come with me!"
    "To a better place!"
    "Let us {s}GET AWAY{/s} escape this hell together!"
    "Do your eyes play tricks on you?"
    "If so, close them!"
    "Relinquish yourself to me and the two of us can spend our lives together!"
    "Time matters not!"
    "Fear matters not!"
    "All that matters is us!"

    scene painisreal11

    "Pain is real!"
    "Happiness is real!"
    "Everything is real!"
    "A whole new world awaits us!"
    "信じて！"
    "信じて！"
    "信じて！"
    "信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！信じて！"

    play sound "static.mp3"
    scene help5
    with flash
    scene painisreal8
    with flash
    stop sound
    play sound "slidedoor.mp3"

    sg "What’s going on in here?!"

    "Two girls from the team run into the storage room and surround Miku."

    scene painnew1
    with dissolve

    mi "{b}NO! GET AWAY FROM ME! LEAVE ME ALONE! GET AWAY GET AWAY GET AWAY!{/b}"
    sg "Oh my god...but...how?..."
    sg "What happened?"
    sg2 "I...I kicked a ball and...and it hit the door...The noise must have-"
    sg "Miku. Miku, it's me. Karin. Everything is okay. You're fine."

    scene painnew2
    with dissolve

    sg2 "We...we were just playing...I didn’t mean to-"
    ka "Kirin, let me handle this."
    ka "Miku, listen to me. You're safe. We're here for you. "
    mi "{i}Hah...hah...hah...hahhh...ahhhhh...{/i}"
    ka "Good girl...Just like that...Deep breaths...In and out...In and out..."

    "The girl to my left, begins to coach Miku through some breathing exercises as I stand here absolutely useless."
    "What...could have caused this?"
    "What happened to her?"

    scene painnew3
    with dissolve

    ka "Sensei...I’m sorry, but could you please leave us alone for now?"
    ka "She’ll be okay."
    ka "She’s just a little scared, that’s all."
    s "Oh, uhh...yeah."
    s "I’ll go."
    s "Are you sure you’ve got this under control?"
    ka "I am. It's not the first time something like this has happened."
    ka "Kirin will come with you. It would be best if I did this alone."
    ki "But I...I can..."

    scene painnew4
    with dissolve

    ki "Okay..."
    ki "I..."
    ki "I really didn’t mean to-"
    ka "Just go. We’ll talk about it later."

    scene black
    with dissolve2

    "I exit the storage room alongside Kirin, enveloping myself in the sounds of urgent consolation bleeding through the large metal doors."
    "Something is wrong."
    "Something is very wrong."

    stop music
    scene ohno

    "{i}Oh no! It looks like Miku may have ripped out some of her hair!{/i}"
    "{i}Will you still think she’s pretty when it's all gone?{/i}"

    $ renpy.end_replay()
    $ soccer10 = True
    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label soccer15:
...
```

## Code that triggers this event

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label soccerfield:
    if miku_love >= 0 and firsttimesoccerfield == False:
        jump firsttimesoccer
    if miku_love >= 5 and soccer5 == False:
        jump soccer5
    if miku_love >= 10 and soccer10 == False:
        jump soccer10
...
```