# The Adventures of Karli & Steve (Karin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Still Young](./ayanedorm20.md)

## Event preconditions

* Karin love greater than or equal to 20

* Event [Food Groups](./day351.md) (Main) is completed)



## Next events

* [Karin: Sweet Tooth](./karindate20.md)

## Event properties

* Id: karinsoccer20
* Group: Karin
* Triggered by label: soccerfieldkarin
* Chain sources: ayanedorm20
* Chain sources path: ayanedorm20->saturdaymorning

## Official wiki page

[The Adventures of Karli & Steve](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=karinsoccer20&go=Go) for more details.

## Event code

File: (install folder)\game\KarinEvents.rpy

Code:
```python
...
label karinsoccer20:
    scene karinadventure1
    with fade
    play music "justbehappy.mp3"

    mi "I’m gonna dieeeeeeeeeeeeeee..."

    "Hi there."

    if bonus == True:
        "As much as I’d love to tell you that the reason these two girls are beet red and dripping sweat is sexual, it isn’t."
        "The reason for this is actually much simpler and...well, involves exactly what this gym is made for and why this team exists in the first place."
    else:
        "As you can see, I am a very good coach and am forcing the girls to become stronger through a strict but reasonable practice regimen."

    "The thing is, I’ve seen them practice a million times by now and have never seen them {i}this{/i} exhausted."
    "So...what was so different about today, you ask?"

    scene karinadventure2
    with dissolve

    mi "Did ya really have to be so ruthless today?"
    mi "Is givin’ ya free reign of the practice schedule goin’ to your head? This some sort of power trip?"
    ka "No...I just...read in a magazine that intense workouts can be good if done in moderation."
    ka "And we’ve never really gone at it that hard and long before."
    s "Ha."

    scene karinadventure3
    with dissolve

    ka "Hm? Why are you laughing?"

    if bonus == True:
        s "What you just said."
        ka "That we went at it hard and long? "
        ka "Is this some sort of inside joke?"
        mi "Nah. Sensei’s just bein’ bad with girls again."
    else:
        s "I just remembered a silly Vine I saw."

    ka "I don’t get it."
    s "That aside, you guys should be done for the day now, right?"

    scene karinadventure4
    with dissolve

    ka "Right!"
    ka "Like I said, it’s only good to do things like this in moderation. Overworking yourself on a daily basis is one of the easiest ways to destroy your body."
    s "Well that’s great for me because it means I get to actually talk to you two instead of just staring at you for a concerning amount of time."

    scene karinadventure5
    with dissolve

    ka "Um...please don’t stare for too long..."
    ka "It’ll make me...trip or something..."
    mi "There somethin’ you were lookin’ to do, Sensei? Or were ya literally just gonna talk to us?"
    s "Is there something wrong with “literally just talking to you?”"
    mi "Yeah. It’s boring."

    scene karinadventure6
    with dissolve

    mi "I wanna go on an adventure!"
    ka "An adventure?"
    mi "Yeah! No practice regime is too tough for Miku Maruyama!"
    mi "And now that her blood’s pumpin’, she’s ready to take on the world!"
    ka "Didn’t you just say you wanted to die?"
    mi "Nope!"
    mi "Sensei! How do you feel about an adventure?"
    s "Bad. "
    mi "Well tough cookies because you’re outvoted two to one!"

    scene karinadventure7
    with dissolve

    ka "Oh, okay. I guess I choose the adventure option instead of taking a shower like I really wanted to."
    mi "We can shower later! "
    mi "I hate gettin’ in there next to you anyway, Karin."
    mi "I learned recently that what I lack in the chest department, I make up for in abs- and you’ve got me beat in both of those things."
    ka "Yes, Miku. You remind me of that after every practice."
    s "Karin, if you’re not feeling up to it, I’m sure that the two of us could overpower-"

    scene karinadventure8
    with dissolve

    ka "I’m fine with an adventure...I’m just not very good at coming up with ideas, so it will probably be really boring and you’ll probably hate it."
    s "Anywhere is fine as long as I can be with you."

    if karinlied == True:
        scene karinadventure9
        with dissolve

        ka "Wha-?!"
        ka "Wh-wh-wh-wh-what are you saying?! That makes it sound like you and me are..."
        mi "Ooooh, direct hit. Nice job, Sensei."
        s "Are what, Karin?"

        scene karinadventure10
        with dissolve

        ka "I...I don’t know!"
        ka "Ask someone else!"

    else:
        scene karinadventure11
        with dissolve

        ka "Are you...sure you’re not confusing me with my sister?"
        mi "Hm? Kirin’s not even here today."
        s "…"

        if bonus == True:
            "Well, it looks like it’s still a little too early to make jokes like that after coming clean about my...{i}relationship{/i} with Kirin."

    scene karinadventure12
    with dissolve

    mi "Alls I know is...if we’re gonna do this thing, we better get goin’ soon!"
    mi "And since it was {i}my{/i} idea to go on this adventure in the first place, I leave choosin’ the adventure up to you two."
    s "I hereby relinquish all responsibility onto Karin as I didn’t even want to do this in the first place."
    s "I am more than happy with staying here and making more suggestive jokes that Karin doesn’t understand."
    ka "It’s...not really much of an {i}adventure,{/i} but...I kind of needed to go get something from my classroom..."
    ka "Would...that work?"

    scene karinadventure13
    with dissolve

    mi "Heck yeah it would! And it’s close enough that Sensei probably won’t even complain about it!"
    s "Well...it {i}is{/i} in this building..."
    s "So yeah. I guess that’s fine."

    scene karinadventure14
    with dissolve

    mi "Heck yeah! Adventure crew away! First person to make it to Karin’s classroom is crowned the queen or king of...adventuring or something!"
    ka "Um...yaaaaay?"

    scene black
    with dissolve2

    "Karin and Miku get off the ground, grabbing their bags and dropping them off in the girls’ locker room before coming back out and...setting off on what I imagine will be a rather anticlimactic journey."
    "Of course, Miku takes the lead and leaves both Karin and myself lingering in the background, equal parts confused and curious."
    "And, without any further delay, things become more or less as exhausting as I expected them to be as soon as the word “adventure” was broken out."

    scene karinadventure15
    with dissolve

    mi "There! At the end of this hall lies our final destination!"
    ka "Um...actually...my room is on the second floor..."
    mi "Right! You’re so stacked that I often forget you’re a second year!"
    ka "…"
    s "Can you really say you didn’t expect things to turn out like this?"

    scene karinadventure16
    with dissolve

    ka "Well it’s not like I had a choice, is it?"

    if bonus == True:
        s "You literally gave up and let Miku vote for you. The three of us could be in the locker room together right now if you and I out-voted her."
        ka "I think you mean the gym, Sensei. You're not allowed in the locker room."
        s "I said what I said."
    else:
        s "You were literally given a chance to vote, Karli."
        ka "Who is Karli?"
        s "You will find out in a second."

    mi "You guys...I can only hold this pose for so long."
    mi "If we’re gonna get past the dreaded six headed janitor demon, we’re gonna need to be real tactical with our movements and whatnot!"
    mi "Then, once we find the destination...treasure will await!"

    scene karinadventure17
    with dissolve

    ka "There isn’t any treasure...I just need to grab my history textbook so I can study for a test."
    mi "Ahh, yes....tests."
    mi "I remember the days when {i}I{/i} was forced to learn!"
    mi "Now, I’m free to wander the halls and the world to my heart’s content with my trusty companions...Karli and...Steve!"

    scene karinadventure18
    with dissolve

    ka "Your real name is Steve?"
    s "Yes. It’s nice to meet you, Karli."
    ka "You don’t look like a Steve."
    s "Karin, come on. You’re smarter than this."
    mi "I...am...losing...my...patience!"

    scene karinadventure19
    with dissolve

    ka "Let’s go, Steve."
    ka "I’m sure it won’t be a very exciting adventure...but I guess we can have fun just...watching Miku have fun."
    s "I still think we should have had fun in the locker room instead."
    ka "Gym, Steve."
    ka "It’s called a gym."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "Karin and I walk slowly behind Miku as she marches down the halls of the[school]."
    "The sound of her footsteps bounces off of the walls as she makes her presence known to virtually every person still inside of the building."
    "I’m not a fan of the idea of being spotted with these two outside of normal[school] hours, but I guess I could always fall back on the fact that I’m just their coach or whatever."
    "Unless there was supposed to be some sort of formal process for me to actually {i}accept{/i} and {i}assume{/i} that position."
    "Now that I think of it, there probably was."
    "So, if we {i}are{/i} caught, I guess I’ll just have to, once again, take up the role of “mildly weird guy hanging out with girls who are way too [young]for him.”"
    "But hey, at least one of those two is responsible."

    if bonus == True:
        "And the other one needs to sleep strapped into her bed so she doesn’t wind up dry humping older men in the middle of the night."

    mi "Ahoy, mateys! Land ho!"
    s "Are we pirates now?"
    ka "A...Argh!"
    s "Karin, come on."
    ka "What?...I want to play along too..."

    "………"
    "……"
    play sound "slidedoor.mp3"
    "…"

    scene karinadventure20
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "Karin looks out of the window as she removes a textbook from the depths of her desk."
    "Her tanned skin catches and absorbs the sunlight, distributing a fair amount of Vitamin D3 throughout her toned and divinely shaped body."
    "I think about how many of the nutrients must have been intercepted by the glass and then attempt to wrap my mind around how light can carry value in the first place."
    "The only value I’ve ever assigned to things like that is the importance of its existence in terms of brightening up dark areas."
    "But when the world itself is overcome with darkness, no amount of sunlight or Vitamin D3 can truly return it to form."

    mi "Adventure complete!"
    mi "It wasn’t a {i}long{/i} journey, but it was a journey nonetheless!"
    mi "Now, for our next adventure, I’d like to propose-"

    play sound "texttone.wav"

    mi "Hm?"
    s "Your phone?"
    mi "Guuuuuh. Yeah. Looks like Makoto needs to check on somethin’."
    mi "Sensei! Keep an eye on Karin and make sure she doesn’t go...learning! Or doing other[school] stuff!"
    mi "Just...do what you do best, I guess, and I’ll be right back!"

    play sound "slidedoor.mp3"

    "Miku leaves the room and suddenly the two people who didn’t even want to be a part of this adventure are the only ones left in the party."
    "It’s not too nerdy for me to say that, is it? Party?"
    "Who came up with that word anyway?"
    "How much Vitamin D3 can bleed through glass?"

    ka "I like the second floor, you know."
    s "...What?"

    scene karinadventure21
    with dissolve

    ka "S...Sorry...That probably sounded a little weird without any context, didn’t it?"
    s "I mean...I’m not really one to judge peoples’ hobbies or interests..."

    scene karinadventure22
    with dissolve

    ka "What I mean is that I kind of...like being in the middle of things."
    ka "Being at the bottom sucks because you have so many stairs to walk up if you ever want to go to the roof or something like that-"
    ka "Granted, walking up stairs is an excellent form of cardio and-"
    s "Finish your analogy before talking about exercise, please."

    scene karinadventure21
    with dissolve

    ka "Heheh...whoops..."

    scene karinadventure20
    with dissolve

    ka "So, continuing from where I was...being at the top is also kind of frustrating because the only place to go from there is down."
    ka "When you’re in the middle, it’s like everyone is going to be forced to see you at some point. And you’re always only one step away from wherever you want to be."
    ka "I guess that wouldn’t really matter in a[school] with more than three floors, though."
    s "If you’re trying to get some sort of point across, I’d appreciate a more direct approach."
    s "Stairs are great and all-"
    ka "And excellent for cardio."
    s "Yes. And that."
    s "But even though I’m in a classroom right now, I’d prefer to keep my “teaching hat” off."

    scene karinadventure23
    with dissolve

    ka "Can I...tell you one of the reasons I like you as a coach, Sensei?"
    s "Does it have something to do with stairs?"
    ka "A little bit. Yeah."
    ka "But...one of the reasons I like you as a coach, even though you barely do any {i}coaching{/i}...is that you don’t really expect any more out of me than you do anyone else."
    ka "It’s kind of refreshing in a way."
    ka "Like I can hang out on the second floor for as long as I want and you’ll just walk past me and not be like, “Karin! Someone upstairs needs you!”"
    s "Are you exhausted?"

    scene karinadventure24
    with dissolve

    ka "From practice or in general?"
    s "From all of the people trying to make you change floors."
    ka "…"

    scene karinadventure25
    with dissolve

    ka "Kinda. "
    ka "Yeah."
    ka "And I can’t even complain about it because then it will just sound like I’m stepping on the toes of everyone who wishes they were as...tall or...muscular or-"
    s "Talented?"

    scene karinadventure26
    with dissolve

    ka "…"
    ka "Sorry. I’m just being dramatic, I think."
    ka "It’s not like I planned on talking about this today or anything."

    scene karinadventure27
    with dissolve

    ka "Just...thinking out loud as I look outside the window."
    ka "Wishing I could trade places with someone like Kirin for a day or two...and not being able to talk to {i}her{/i} about it because she’ll just get mad."
    s "Yeah, it would probably be best if you never repeated that to her."
    ka "Which is part of the problem."
    ka "Her and my parents...they all think I’m some sort of...amazing human being. The rest of the girls on the soccer team do too."
    ka "Like, Miku is better than me in pretty much every way, but still {i}I’m{/i} the one people are looking up to most of the time."
    s "To be fair, it’s probably pretty difficult to look {i}up{/i} to Miku."

    scene karinadventure28
    with dissolve

    ka "I was hoping that joke wasn’t coming."
    s "I couldn’t resist and I’m sorry."
    s "But hey, on the bright side, you’re still {i}technically{/i} on the second floor from at least an academic standpoint."
    ka "True. But even that has its downsides."
    s "Like?"
    ka "Like..."

    scene karinadventure29

    with dissolve

    ka "L...Like I...can’t be in your class, for example..."
    ka "You’re the first b...boy I’ve ever been able to talk to without exploding..."
    ka "So if I got to see you every day, maybe I’d get better at facing one of my many, many fears?"
    s "Many?"
    s "How many fears can someone like you have?"

    scene karinadventure30
    with dissolve

    ka "Hm..."
    ka "Let’s see..."
    ka "So there’s snakes..."
    ka "And heights...and large fish..."
    ka "And that sound macaroni and cheese makes when you stir it."
    ka "And graveyards and gondola rides."
    ka "And those weird dream loops you get where one dream ends only to throw you into the middle of another one-"
    ka "And then the next thing you know, you have to change a tire for Serena Williams on the way to Newark, New Jersey."
    s "...What?"

    scene karinadventure31
    with dissolve

    ka "I’m scared of a lot of weird stuff, okay?! It’s not my fault!"
    ka "B...But..."

    scene karinadventure32
    with dissolve

    ka "I’m a little less scared...whenever you’re around..."
    s "…"
    ka "…"
    s "…"
    ka "…"

    play sound "slidedoor.mp3"

    mi "Okaaaaaay! Miku’s back, y’all! Which means-"
    mi "Hey, what are you two doin’ just standin’ around in silence?"
    mi "I know I’m the leader of the adventure squad, but if we’re ever gonna find {i}real{/i} treasure, we’re gonna have to bump up the team chemistry!"
    mi "So go ahead and hug it out so we can get a move on!"

    scene karinadventure33
    with hpunch

    ka "I-I-I-I can’t hug Sensei! We’re not married yet!"
    s "Yet?"
    ka "You know what I mean!"
    s "I do?..."
    mi "Blah blah fear of boys blah blah. "
    mi "You’d think somebody as tall and muscular and talented as you wouldn’t have any trouble at all with somethin’ like that, Kari-"
    mi "Err, I mean...Karli!"

    scene karinadventure34
    with dissolve

    ka "Right..."
    ka "You...{i}would{/i} think that...wouldn’t you?"

    scene black
    with dissolve2

    "We have three more adventures before the morning comes to an end."
    "All of them take place on the second floor of the[school] building."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karinsoccer20 = True
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label karindate20:
...
```

## Code that triggers this event

File: (install folder)\game\KarinEvents.rpy

Code:
```python
...
label soccerfieldkarin:
    if karin_love >= 15 and day271 == True and karinsoccer15 == False:
        jump karinsoccer15
    if karin_love >= 20 and day351 == True and karinsoccer20 == False:
        jump karinsoccer20
...
```