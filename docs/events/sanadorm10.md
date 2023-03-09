# Anywhere At All
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanadorm10&go=Go)



## Event preconditions
✅Sana love greater than or equal to 10

✅Event "[Sana: Supermom](./bar10.md)" is completed (event=bar10)



## Next events
None

## Event properties
* ID: sanadorm10
* Group: Sana
* Triggered by label: sanadorm
* Triggered by branch label: sanadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm10:
    play sound "knock.mp3"

    "I knock on Sana’s door and wait for her to answer."
    "Given that the last time she invited me into her room didn’t play out all that badly, I’m feeling a bit more confident this time than before and-"

    play sound "dooropen.mp3"
    scene giantleapredux1
    with fade

    sa "Um...hi..."
    s "Sana? I wasn’t done narrating yet. Why are you just coming out of your room without saying anything?"
    sa "Because...umm...I figured that...you were going to come inside again if I didn’t..."
    s "Is that not okay? Because there hasn’t really seemed to be any problem with that yet."

    scene giantleapredux2
    with dissolve

    sa "I know, but...it still feels a little weird..."
    sa "I just think...I might feel more comfortable talking to you...if we’re not trapped inside of a...tiny box..."
    s "Aren’t you the one who doesn’t like going outside? This unexpected moment of character growth is putting me on my backfoot and I’m not sure if I like it."

    scene giantleapredux3
    with dissolve

    sa "Well...I guess you’ll have time to figure it out then..."

    "I sigh to myself and accept that I will not be hanging out in Sana’s room tonight."
    "I can’t hold it against her, though, as I probably wouldn’t feel comfortable with the lascivious gaze of someone twice my size bouncing off the walls of my room either."

    s "So, where are we going? Do you have somewhere in mind?"
    sa "If..."
    sa "If you could go anywhere in the world..."
    sa "Where would you go?..."
    s "Anywhere in the world?"

    stop music
    scene black

    sa "Anywhere at all."

    "{s}We are swallowed by the dorm.{/s}"

    play sound "static.mp3"
    scene 1 with flash
    scene roofday
    scene 2 with flash
    scene shrine_night with flash
    scene 3 with flash
    scene urbanparadise with flash
    scene 4 with flash
    scene noonsky with flash
    scene 5 with flash
    scene emptyclassroom with flash
    scene black
    stop sound

    s "Somewhere I could be alone."
    sa "Alone?"
    s "Somewhere no one could reach me."
    s "Maybe the edge of the world?"
    sa "I think..."
    sa "I think that sounds nice."

    play sound "static.mp3"
    scene giantleapredux4 with flash
    stop sound
    play music "newhope.mp3"

    sa "Why don’t we go there, then?"
    sa "To the edge of the universe."
    s "...Sana?"

    play sound "static.mp3"
    scene giantleapredux5 with flash
    scene giantleapredux4 with flash
    stop sound

    sa "Why don’t we go there, then?"
    sa "To the edge of the universe."
    sa "This is what you want, isn’t it?"
    sa "Would it look something like this?"
    s "I..."
    sa "And if this doesn’t work, perhaps a different season?"
    s "What? You can’t just-"

    play sound "static.mp3"
    scene giantleapredux6
    with flash
    stop sound

    s "Change the-"
    sa "Is this where you want to be?"
    sa "I can’t take us if I don’t know where to go, Sensei."
    sa "I can’t take us if-"

    play sound "static.mp3"
    scene giantleapredux7
    with flash
    stop sound

    sa "Sensei?..."
    sa "Is everything okay?..."
    sa "You look kind of...pale, and-"

    play sound "static.mp3"
    scene giantleapredux8 with flash
    stop sound

    "LOST."
    "PERHAPS YOU WOULD FARE BETTER WITHOUT THE DISTRACTION OF AN UNBLOSSOMED SLIT."

    "I can feel something moving around inside of my stomach."
    "When I glance down at my hands, they appear smaller."
    "A bench half illuminated by the sporadic dance of a flickering streetlight sits or stands or lays or kneels before me and I struggle to approach it."
    "Something crawls across my foot."

    play sound "static.mp3"
    scene giantleapredux9
    with flash
    stop sound

    "It must have been a cockroach."

    sg3 "Oh my."
    sg3 "You’re early."
    s "...What?"
    s "Who are you?..."
    sg3 "Me?"
    sg3 "I am no one."
    sg3 "I am simply passing by. The same as you, I’m sure."
    sg3 "How lost the two of us are- chasing a light that seldom shines."
    sg3 "Turning into shadows under the glow of the moon and seeping into the earth as it makes moving that much easier."
    sg3 "But perhaps you’re even more lost than I am."
    s "Listen, I don’t know where I am or...how I got here, but-"
    sg3 "Don’t speak."
    sg3 "It will only make things harder."
    sg3 "I have a message for you."
    s "...For me? From who?"
    sg3 "Him."
    sg3 "He says that the path {i}you{/i} walk will be unlike the others."
    sg3 "He says that you are special. "
    sg3 "He says He wants to meet you."
    sg3 "But He is unwilling to guide you. And you must find Him yourself."
    s "Who are you talking about? How am I supposed to know who to find if-"
    sg3 "Tick tock."
    s "...What?"
    sg3 "You can’t hear it?"
    sg3 "It started counting down not too long ago."
    s "..."

    "I elect to remain quiet, not knowing how to reply to the fanatic ramblings of the mysterious, white-haired girl."
    "I half-expect her to go away, but she simply stares right back at me instead."
    "I listen for the ticking, but hear nothing."

    s "I..."
    sg3 "Need to go back?"
    s "Yeah. I was with someone just a moment ago."
    sg3 "You’re with someone now as well. "
    sg3 "The only difference is you can’t see-"

    play sound "static.mp3"
    scene giantleapredux10
    with flash
    stop sound

    sg3 "Huh?"
    s "..."
    sg3 "Where-"

    play sound "pop.mp3"
    scene giantleapredux11

    "The girl disappears just as quickly as she appeared in the first place."
    "The pain in my stomach returns, but the movements cease as whatever is inside of me transitions to a state of dormancy. "
    "RETURN."

    s "Return where? Who is-"

    stop music
    scene giantleapredux12
    play sound "knock.mp3"

    s "Open the door."

    "..."
    "..."
    "..."

    play sound "dooropen.mp3"
    scene giantleapredux13
    with dissolve

    sa "S...Sensei?..."
    s "Hello."
    sa "I..."
    sa "I...didn’t think you...were coming back..."
    s "Sorry."
    s "I must have zoned out for a second."
    sa "But...that was...almost two hours ago..."
    s "Does that mean we can’t hang out now? Because I don’t really have anything else going on {s}and I am afraid to go home{/s}."
    sa "We can, but..."
    sa "I just...have to put my shoes on..."
    s "Sounds good. I’ll wait out here."
    sa "Y...Yeah..."
    sa "I’ll...I’ll be right back..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene giantleapredux14
    with dissolve2
    play music "thesleepingcity.mp3"

    "Sana and I decide to hang out outside of the dorms and everything is normal and okay."

    sa "So...you're positive that everything is...okay?..."
    s "How many times are you going to ask that? I'm fine."
    sa "I've just...never seen anyone look that way before..."
    sa "I was worried that...maybe I offended you by...asking if we could go outside instead of...staying in my room..."
    s "That's not something I'd be offended by. It's your room and if you want me to stay out of it, I'll stay out of it."
    sa "It's not...forever...it's just..."
    sa "I...I want to know more about you first..."
    sa "Which is why I asked about...where you'd want to go earlier...but...that...didn't really work out too well..."
    s "Did I even give you an answer?"

    scene giantleapredux15
    with dissolve

    sa "Something about...the edge of the world, I think?..."
    sa "I...still don't really understand what you meant by that, but...I think the point you were trying to make is that...you wanted to be alone..."
    s "What about you, then? Where would you go if you could choose anywhere at all?"
    sa "Maybe...um..."
    sa "Akihabara?..."
    s "You can choose anywhere in the world and your answer is that? That's like visiting a neighbor's house."
    sa "Well...I've never been there before and...we can't leave Kumon-mi anymore..."
    sa "We have...something similar not that far from here, but...it's a lot smaller and..."
    sa "Should...should I pick something different?..."
    s "No, your answer is fine. I just expected something a little different, I guess."
    sa "I'm...pretty good at being different, I guess..."
    sa "Actually, umm...now that I mention it..."
    sa "There's something I want to ask you...if that’s okay..."
    s "Ask away."
    sa "Well, umm...We’ve been seeing each other more lately, and...and..."

    scene giantleapredux16
    with dissolve

    sa "You don’t...have to answer this if you don’t want to..."
    sa "It’s...a little weird, so...I would understand..."
    s "Just ask me. It’s fine."
    sa "Okay..."
    sa "Then, umm..."
    sa "What do you think I can do to seem...{i}more{/i} normal?..."
    s "Why do you ask, exactly?"
    sa "It's just...hard to...connect with anyone when...I'm not sure what types of...ports they have or something..."
    sa "Like...my wires won't fit because...they're outdated or...not the right brand..."
    s "Interesting time for a gaming analogy."
    sa "I just...want to...be less scared, I think..."
    sa "And I don't want...anyone to think I'm...avoiding them on purpose..."
    s "Hm."
    sa "I know I’m not helping myself by being so quiet, but..."
    sa "That's just...how I am, I guess..."
    s "If that's who you are, why bother trying to be more {i}normal{/i} in the first place?"
    s "Do you actually {i}want{/i} to change? Or do you just think changing will make your life more convenient?"

    scene giantleapredux17
    with dissolve

    sa "C-Convenient?"
    sa "What do you mean?..."
    s "Well, you only really talk to Ayane, right?"
    sa "Right..."
    s "So, you probably think that if you had more friends or more people to talk to, things would be easier. But that's not true."
    s "The more people you have in your life, the harder it gets to balance everything."
    sa "Well...easier...isn’t really how I would put it..."
    sa "Maybe just..."

    scene giantleapredux16
    with dissolve

    sa "Actually...never mind...I don’t...really know where I’m going with this..."

    s "Well, whatever the case, I don’t think you should try to change who you are just because not enough people see you for {i}you{/i}."

    scene giantleapredux17
    with dissolve

    sa "Huh?..."
    s "Is that really all that hard to understand?"
    sa "Well...no...but..."
    sa "It just kind of...sounded like a compliment..."
    s "That's probably because it was a compliment."
    s "It might sound sappy, but I like you the way you are."
    s "Besides, the world already has your mom, so there's really no need for you to start being outgoing or flirtatious."

    scene giantleapredux18
    with dissolve

    sa "Can we...stop talking about my mom so I can...return your compliment?..."
    s "Sure. Go ahead."
    sa "I...umm..."
    sa "I also...think you’re...a good person..."
    s "You're wrong. But thank you anyway."
    sa "Don’t say that, Sensei...You took your time getting to know me when it felt like...everyone else was either rushing or...not interested..."
    sa "I think that makes you a really good person..."
    s "Again, thanks. But I can promise you there’s a lot more to me than just that."
    sa "Then...tell me..."
    sa "About {i}you...{/i}"
    sa "I..."
    sa "I want to know..."
    s "..."
    sa "..."

    "I hope to myself that the silence might help Sana understand that I don't want this."
    "I mean, how {i}could{/i} I when I don't know the first thing about myself to begin with?"
    "I can't share something I don't have. But I also can't come out and tell her that without the risk of breaking her heart just as she's finally starting to trust me."
    "This is one of those times where silence is supposed to serve as an answer."

    s "..."
    sa "..."

    "It just doesn't."

    s "I'll...tell you more some other time, Sana."
    s "I'm not really good at talking about myself."
    sa "That...makes two of us, then..."
    sa "We can...improve together..."
    s "..."
    sa "..."

    scene black
    with dissolve2

    "Silence works this time."
    "We head our separate ways and go to sleep in separate beds."
    "I wake up in the middle of the night and forget where I am."

    $ renpy.end_replay()
    $ sana_love += 1
    $ sanadorm10 = True
    stop music fadeout 7.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ayanedorm5:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm:
    if sana_love >= 5 and sanadorm5 == False:
        jump sanadorm5
    if sana_love >= 10 and bar10 == True and sanadorm10 == False:
        jump sanadorm10
...
```