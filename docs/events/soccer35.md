# Loxonin (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 35

* Event [One. Two. Three.](./mikudorm30.md) (Miku) is completed)

* Event [What Was](./day271.md) (Main) is completed)



## Next events

* [Makoto: Condoms in the Sand](./makotowinterbeach1.md)

## Event properties

* Id: soccer35
* Group: Miku
* Triggered by label: soccerfield
* Triggered by branch label: soccerfield
* Triggered by path: soccerfield->soccer35

## Official wiki page

[Loxonin](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=soccer35&go=Go) for more details.

## Event code

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label soccer35:
    scene gym
    with fade
    play music "highspeedprinter.mp3"

    "I make my way to the gym first thing in the morning to see what the girls are up to for soccer practice."
    "I immediately notice Karin leading a bunch of shorter girls in some drill that I should probably know the name of by now but can honestly just not be bothered to learn."
    "Well, to be more precise, I immediately notice Karin's thighs."

    if bonus == True:
        "Everything else comes after."
        "There’s no Miku anywhere in sight, though."
        "In fact, I don’t see Kirin anywhere either, but I guess that’s a lot more normal than having the team captain absent."
        "I begin to make my way over to Karin to ask about-"
    else:
        "But then I immediately look away because even if she is a grown woman, looking at her without her approval or consent would be rude."

    ki "Sensei! Come quick! Miku is in trouble!"

    if bonus == True:
        mi "I told ya I’m fine, Kirin! Sensei, you can go back to walkin’ around the gym lookin’ at butts and stuff!"
        ki "No, no! Come over here! This is where the best butts are!"
    else:
        mi "Help! She is trying to make me watch the third season of Seinfeld!"
        ki "Do it."

    scene black
    with dissolve

    if bonus == True:
        "Being swayed by the prospect of the alleged best butts on the soccer team, I follow Kirin’s voice and wind up in front of the stage..."
    else:
        s "I will save you, Miku."

    scene mikuankle1
    with dissolve

    ki "Sensei, quick! Miku needs mouth to mouth!"

    if bonus == True:
        mi "I don’t need friggin’ mouth to mouth for a twisted ankle..."
        s "Are you sure? Because I’ll do it."
    else:
        s "Ew, kissing."

    ki "You should do it. Just to be safe."

    if bonus == True:
        s "That’s a good idea, Kirin. Please step aside."
    else:
        s "I'd have to ask my accountant first."

    scene mikuankle2
    with dissolve

    mi "Jeez! When the heck did you two get as close as peanut butter and jelly?!"

    if kirin_virgin == False:
        scene mikuankle3
        with dissolve

        ki "…"
        s "…"
        ki "Do you want to tell her or should I do it?"
        mi "Tell me what? What are you talkin’ about?"
        s "I don’t think either of us should tell her."
        ki "Booooooring. I wanna do it."
        s "Kirin..."
        ki "Sensei~"
        mi "...Miku?"

    else:
        scene mikuankle3
        with dissolve

        ki "I don’t know if I’d go as far as peanut butter and jelly...but Sensei and I have definitely been spending a decent amount of time together."
        mi "What, for like...soccer coaching and stuff?"
        mi "You tryin’ to whip yourself into shape, Kirin?"

        scene mikuankle4
        with dissolve

        if bonus == True:
            ki "Yup. He’s working me {i}really{/i} hard too. It’s a good thing I like it a little rough."
            s "Okay, I’m going to cut this conversation off before it has any...adverse effects on me."
            mi "What...kinda routine does he have you on exactly?"
        else:
            ki "No. I just like his scent."

    scene mikuankle5
    with dissolve

    s "Okay, moving right along- what happened to your ankle? You said you twisted it?"
    mi "Yeah. Playin’ inside is a lot different from playin’ on the grass and I came down kinda hard on it since I ain’t totally used to things in here yet."
    ki "And yours truly swooped in to temporarily rescue her, knowing full well that our dearest coach would soon show up to carry her to safety."
    s "How did you know I was coming today?"
    ki "Because you always show up as soon as something interesting happens. It’s like clockwork or however the thing goes."
    mi "Yeah, it is kinda weird now that Kirin mentions it."

    scene mikuankle6
    with dissolve

    mi "I’ll be totally okay, though! I just need to run to the nurse’s office for some painkillers."
    mi "Except...I can’t really run because of my ankle and..."
    mi "You know what? Maybe I’m just doomed."
    ki "Sensei, maybe you should princess carry her to the nurse’s office?"

    scene mikuankle7
    with dissolve

    mi "No way! I watched him do that when Ayane hurt her ankle and when she came back, she was all red and...panting and stuff!"
    ki "Oh?"
    mi "Yeah! Not sure how just carryin’ somebody can make em get all sweaty and heated, but I’ll be totally fine on my own."
    s "I can assure you that the state Ayane returned in had nothing to do with the way I carried her."

    scene mikuankle8
    with dissolve

    mi "Well it sure as heck wasn’t like any ankle injury I’ve ever seen before, so explain that!"

    if bonus == True:
        ki "Yeah. Explain that, Sensei. We’re all dying to hear what went on with you and Ayane in the nurse’s office."
        mi "Yeah!"
        s "To be honest, that was so long ago now that I can’t even remember."

        "Lies. We made out behind a curtain. It was awesome."

        s "Anyway, talking about what happened back then won’t fix your ankle, Miku."
        mi "I ain’t lettin ya carry me like a heckin’ princess, Sensei!"
    else:
        s "You are right. It was horrible and unlike anything I've ever seen as well."
        s "But my time in the medical field prepared me for it and, today, Ayane can walk with only a tiny bit of shooting pain."

    scene mikuankle9
    with dissolve

    ki "You could always just give her a piggyback ride instead. That sounds a lot less romantic, doesn’t it? Pretty sure that’s the issue here."
    s "Miku, is that fine with you?"
    mi "I mean...yeah. I guess that’s okay."
    mi "I had to ride on your shoulders that one time in the shed so it’s not like I’m unfamiliar with the vehicle."
    s "I’m a vehicle now?"

    scene mikuankle10
    with dissolve

    mi "Yup! The cheapest, fastest one around!"
    ki "I want to take a ride when Miku is done."
    mi "Hop right on, Kirin! The Sensei express has enough room for everyone!"
    s "Yup. Hop right on Kirin. The real ride starts when we get to the nurse’s office."
    ki "Mmmmmmmmm...as much as I want to, I think I’ve gotta give this one up to Miku."
    ki "She could really use some of those good ole’ Sensei healing powers right about now."
    mi "You’ve got healing powers, Sensei?! You shoulda said somethin’! Now we don’t even have to go to the-"
    s "I don’t have healing powers, Miku."
    s "Now hurry up and get on my back before your ankle heals on its own."

    scene black
    with dissolve

    "I lean down to let Miku jump onto my back but she wraps her legs around my neck and decides to ride my shoulders again instead."
    "There will be no complaints from me regarding this situation."

    scene mikuankle11
    with dissolve

    mi "This is fine, right?"
    mi "I realize it’s not a piggyback ride but I feel little bit better holdin’ onto your head than wrappin’ my arms around those big ole shoulders of yours."
    s "I also feel better this way."
    ki "Have fun, you two."
    ki "I’ll cover for you if Karin asks where you went, which she probably will because she’s a buzzkill and she sucks."
    mi "No worries, Kirin! We won’t be gone long!"
    mi "Cause even though Ayane came back all red and sweaty that one time, her ankle was totally fine!"
    mi "And I’m a lot more fit than she is so I’m sure Sensei can do the same thing for me."
    s "Yup. Definitely can."
    ki "...Right."

    scene black
    with dissolve
    stop music fadeout 10.0

    "Having Miku on my shoulders makes it rather complicated walking through the halls of the[school]."
    "Doors are a completely separate ordeal, and Miku seems entirely unwilling to help from atop her throne, so I need to bend down and nearly break my back just to get through some of them."
    "But, after a few minutes of pain that will likely force me into taking some of whatever Miku plans on taking to fix her ankle, we wind up at the nurse's office."
    "Unfortunately, Miku hops off right away, so I don’t have a chance to drop her on the bed like I did with Ayane."
    "I guess today is going to be a bad day after all."

    scene mikuankle12
    with dissolve2
    play music "love.mp3"

    "Miku slowly limps her way over to a table holding a bunch of different bottles on the far side of the room as if she’s done it a million times before."
    "It would probably make sense for the soccer team to have their own stash of this stuff, but I guess there might be some issues that arise by providing full pharmaceutical access to a bunch of [teens]."

    mi "Sorry to make ya carry me all the way here, Sensei."
    mi "I normally bring some weaker stuff with me but I forgot to refill my bottle before comin’ to practice this morning."

    "Oh. Well I guess Miku normally {i}does{/i} have full pharmaceutical access and I was wrong."

    s "Do you...have an addiction you want to talk about, Miku?"

    scene mikuankle13
    with dissolve

    mi "What? Course not. It’s not anythin’ like that."
    mi "I rarely ever get hurt during practice. I normally just keep ‘em around in case of headaches or if one of the other girls gets hurt."
    s "Is that normal?"
    mi "Course it is. Ya think those bags that girls are always carryin’ around are just filled with rainbows and sunshine or somethin’?"
    s "Well that would certainly be more exciting than Loxonin or Eve."
    mi "Yeah but a rainbow’s not gonna make your head stop hurtin’ so you should be proud of me for bein’ so prepared."
    s "If you were prepared, you would have remembered to refill your personal bottle."

    scene mikuankle14
    with dissolve

    mi "Uh...well...yeah. I guess you’re right."

    scene mikuankle15
    with dissolve

    mi "So...uhh...I guess that’s all we needed to come here for."
    mi "We can probably...get goin’ now."
    s "You sure you don’t want me to use my miracle cure on you?"

    if bonus == True:
        mi "Do you...actually have one or...is that just a thing you’re sayin’ to try and get all touchy with me again?"
        s "Woah. Since when are you this perceptive?"

        scene mikuankle16
        with dissolve

        mi "I’m a woman now, Sensei! I’ve seen the light!"
        mi "Well...felt the light when I sat on your lap that one time!"
        mi "But I’m not allowed to talk about that!"
        mi "And a woman knows when she’s about to be duped!"
        s "And yet that “woman” willingly rode my shoulders all the way here."
        mi "I did what I had to do to fix my ankle! Gotta be crafty to survive sometimes!"
        mi "That’s what Kirin always tells me at least!"
        s "Kirin probably isn’t the best role model for you, Miku."
    else:
        mi "Yes. Please use it."
        s "I just need to capture a turtle first."
        s "I will enlist the help of Kirin. She hates turtles."

    scene mikuankle17
    with dissolve

    mi "I keep hearin’ people say stuff like that about her, but I’ve never felt that way at all."
    mi "I don’t get it. She’s always so nice to me."
    s "Well that’s probably just because you’re her friend."
    mi "She’s got lots of friends, though. Like everybody in the class is friends with her."
    s "Friends or “friends?”"
    mi "What? The heck is that supposed to mean?"
    s "Aren’t there people who you call your friend despite never really spending time with them?"
    mi "I guess so, but they’re still my friends."
    mi "I’d never call somebody that if I don’t feel that way. Friendship’s a big thing, Sensei. It’s a dog-eating world out there."
    s "I...think you meant to say “dog eat dog,” but I don’t want to sidetrack this conversation."
    s "I’m sure Kirin has a lot of “friends,” but you seem to be one of the few she genuinely cares about."
    s "So you probably don’t understand what people say about her because it’s never applied to you."

    scene mikuankle18
    with dissolve

    mi "Yeah, Makoto said somethin’ similar. Just kinda hurts to hear when I know that deep down she ain’t all that bad."
    s "Well, on the bright side, her being in the class now will give her plenty of time to show that side of herself to everyone."

    "Which I can almost guarantee she will {i}not{/i} do based on my experience with her."

    scene mikuankle19
    with dissolve

    mi "Yeah..."
    mi "It’s still kinda crazy she wound up in our class, huh?"
    s "Not really. The way she talked about it made it seem like she was going to make that happen no matter what."
    mi "Class in general has just been...all sorts of crazy lately."
    mi "Specially with that roommate of hers showin’ up."
    s "Noriko?"
    mi "Yeah, that one."
    mi "You...uhh..."
    mi "You’re...really popular with all sorts of girls, aren’t you?"
    s "If you’re worried about Noriko stealing me away from the rest of you, don’t be."
    s "I wouldn’t be me if I didn’t equally distribute my incredibly valuable time among all of you girls."

    scene mikuankle20
    with dissolve

    mi "It’s not really me I’m worried about..."
    mi "Makoto’s been gettin’ all sorts of down about stuff lately and I...don’t want more girls showin’ up to stress her out even more, ya know?"
    mi "She works suuuuuper hard. And she’s really beautiful and so smart and-"
    s "Did she pay you to talk her up again?"
    mi "…"

    "I’ve gotta hand it to Makoto. She’s definitely determined, if not anything else."

    s "Listen, if Makoto wants to talk about things like that, she can talk to me herself."
    s "And if {i}you{/i} want to talk to me about things like that, the same goes for you."
    s "But I’m not going to let you act like a middleman who's out to gauge my relationships with some of the new girls for profit."

    scene mikuankle21
    with dissolve

    mi "It’s...it’s not just for profit! I’m curious too!"
    mi "We got a maid, a green haired girl who won’t talk to anybody, and a punk lookin’ girl who wants to have your babies! It’s weird!"
    mi "Course I’m gonna wanna ask about them when you’re treatin’ em the same way ya treat all of us!"
    mi "More girls means less time for you and me to go runnin’ and stuff like that!"
    mi "And less time for you to consider buyin’ a ring and tellin’ Makoto to be your-"
    s "Miku..."

    scene mikuankle22
    with dissolve

    mi "Darn it!"
    mi "How’s a girl supposed to make any cash when she can’t even hype up her BFF?"
    s "Just tell her you followed through, it’s fine."
    mi "I can’t heckin’ lie to Makoto, Sensei! She’s Makoto!"
    mi "She’ll see through me like a friggin’ window!"
    s "Well then I suppose it’s time for you to start looking for a real job."
    mi "The heck kinda job is someone like me gonna do?"
    s "I don’t know. What are you good at besides soccer?"
    mi "..."
    s "...?"
    mi "You...have any messages that need to be delivered?"


    scene black
    with dissolve2

    "I leave a message with Miku to give to Makoto, but quickly retract it once I remember that I’m supposed to pay her."
    "Miku lives the rest of her life unemployed and dies alone and poor."
    "The end."

    $ renpy.end_replay()
    $ miku_love += 1
    $ soccer35 = True
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label mikudorm45:
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
    if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
        scene soccerfield
        with dissolve
        "I show up at the soccer field to try and talk to Miku but she immediately runs off and starts talking to one of the other girls."
        "Am I...being avoided?"
        "I should probably try visiting her dorm sometime to figure out what's going on with her..."
        jump saturdayafternoon
    if miku_love >= 15 and day83 == True and mikudorm10 == True and soccer15 == False:
        jump soccer15
    if miku_love >= 20 and soccer15 == True and soccer20 == False:
        jump soccer20
    if miku_love >= 25 and mikudorm15 == True and halloween14 == True and soccer25 == False:
        jump soccer25
    if miku_love >= 30 and mikudorm25 == True and soccer30 == False:
        jump soccer30
    if miku_love >= 35 and mikudorm30 == True and day271 == True and soccer35 == False:
        jump soccer35
...
```