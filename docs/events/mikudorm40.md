# Speed of Light (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 35

* Event [Triple Whammy](./mikudorm35.md) (Miku) is completed)

* Day of week is not Thursday



## Next events

* [Main: Operation: Firestarter](./day318.md)

## Event properties

* Id: mikudorm40
* Group: Miku
* Triggered by label: mikudorm
* Triggered by branch label: mikudorm
* Triggered by path: mikudorm->mikudorm40

## Official wiki page

[Speed of Light](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikudorm40&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mikudorm40:
    scene mikunightmolly1
    with dissolve
    play sound "knock.mp3"

    mi "Just a second!"

    "I knock on Miku’s door and don’t have to wait for an answer at all."
    "I figured there’d be a bit more hesitation considering that the last time the two of us actually got to hang out in here things didn’t really end on a good note."

    if bonus == True:
        "In fact, pretty much everything after Miku’s breakdown blurred into one collage of uncertainty and confusion that I’m pretty sure culminated in me just passing out as soon as I got home."
    else:
        "In fact, pretty much everything after our last failed hug (Which I will now refer to as a breakdown for continuity purposes) blurred into one collage of uncertainty and confusion that I’m pretty sure culminated in me just passing out as soon as I got home."

    "I’m awake now, though."
    "I am awake, alert-"
    "And ready to find new and exciting ways to hurt this girl’s feelings, whether those ways be intentional or not. "
    "Though I suppose they sound intentional by the way I worded that."
    "But what difference does the way something is worded really make when any action whatsoever will speak louder than it?"
    "And what is the point of acting at all if things like destiny are as widely believed as they are?"
    "If I surrender to the prospect of ever doing anything with my life, destiny actually seems like a rather alluring idea."
    "I wish I was naive enough to believe in something like that."
    "I suppose I’ll just stick to actions for the time being."
    "Or at least until something better comes along."

    play sound "dooropen.mp3"
    scene mikunightmolly2
    with dissolve
    stop music fadeout 30.0

    mi "Uh...hey. I had a feelin’ it was gonna be you."
    s "Yup. I’m here for another one of the “Miku apologizes for something she doesn’t have to apologize for” meetings."

    scene mikunightmolly3
    with dissolve

    mi "Is it okay if we hold the meeting outside tonight?"
    mi "It’s not really somethin’ I feel comfortable talkin’ about in the dorms."

    if day == 1:
        scene mikunightmolly4
        with dissolve

        mi "Especially with Yumi right next to us..."
        s "Hi, Yumi."
        y "The fuck are you two lookin’ at me for? Wasn't planning on interrupting."

        scene mikunightmolly3
        with dissolve

        mi "So...is that okay, Sensei?"

    s "Sure, going somewhere else is totally fine. Is there anywhere you had in mind?"
    mi "Just...outside on the bench is fine. We don’t really need to go anywhere since all we’re gonna be doin’ is talkin’ anyway."
    s "Well, I guess just...lead the way then."

    scene black
    with dissolve

    "Miku nods at me and makes her way down the hall."
    "And then the stairs."
    "Uta and Io, who are apparently just now getting home, notice us and begin to make their way over, but I wave them off and they awkwardly turn around and reroute themselves down another wing of the hallway."
    "Miku never notices anything as her gaze has been fixed on the floor this entire time."
    "It isn’t until we get outside that her eyes trail back upward, skipping over me and landing somewhere among the stars as she subconsciously inches her way over to a nearby park bench."

    scene nightsky
    with dissolve
    play music "undersea.mp3"

    "That bench winds up being very cold."
    "And, unlike Miku, I’m not dressed for arctic temperatures."
    "It winds up chilling me to the bone as a result."
    "And I can’t even move closer to her for warmth because if all of the misfortune in the world shows up at the same time again, Miku might begin to associate {i}me{/i} with disaster."
    "Kind of like how a dog would begin to fear a human being if the dog was struck by lightning each time that human showed up."
    "I’m sure that analogy is all sorts of unnecessarily confusing, but association is easier to explain with animals and it is once again too cold for me to come up with anything better."
    "You will have to take what you can get for now."
    "And contrary to how I normally desire to live-"
    "Contrary to what my fake destiny predicts for me-"
    "I must take nothing."
    "I must take nothing and hear something."

    scene mikunightmolly5
    with dissolve

    mi "...So, I guess I’ll just get the apology outta the way now, huh?"
    s "And I guess I’ll get my obligatory, “Don’t apologize for things that are out of your control” out of the way as well."

    scene mikunightmolly6
    with dissolve

    mi "This time was a little different, though..."

    if bonus == True:
        mi "I mean...with Makoto showin’ up and me not havin’ a shirt on and stuff..."
        s "She actually wound up apologizing about that for some reason. I never really bothered asking why though, because...yeah."
    else:
        s "My cheek still stings from Makoto's vicious slap."

    scene mikunightmolly7
    with dissolve

    mi "I was able to convince her it was all some sort of misunderstanding."

    if bonus == True:
        s "Were you? Because I feel like Makoto is one of the last people to believe that me being in a room with a shirtless girl is ever a misunderstanding."
    else:
        s "Does this mean I get to slap her now?"
        mi "No."

    mi "Course I can’t speak for her, but she trusts me...so she was willing to hear me out and all that."
    mi "Once I...stopped actin’ all weird, I mean."
    s "Is there...something I should be doing when that happens? Because I normally just freeze up and let it play out."

    scene mikunightmolly8
    with dissolve

    mi "Nuh-uh! You did totally fine during the thunderstorm that one time!"
    mi "I mean, I don’t really remember what ya did in the first place, but I remember not bein’ as scared as I probably should’ve been in front of some random store in the middle of the night."
    mi "It’s gettin’ kinda annoying always havin’ you around for that stuff when it happens, though. Like, what the heck gives?"
    s "I’m not {i}always{/i} there. It happens a lot when I’m not around, doesn’t it?"

    scene mikunightmolly9
    with dissolve

    mi "I’m guessin’ Makoto told ya that?"
    s "You were a relatively popular conversation topic on the beach."
    mi "The only reason I was at the beach in the first place was because of my...problem."
    mi "I don’t even know what to call it since I’ve never gotten one of those diagnosis things."

    scene mikunightmolly10
    with dissolve

    mi "But...I’m practicing! "
    mi "Trainin’ just as hard with that as I am for soccer and stuff!"
    mi "I’ve been turnin’ up the volume on the TV and...listenin’ to music with headphones on. All kinds of stuff!"
    mi "And pretty soon I’ll be able to do things like...light fireworks or...go to concerts or something!"

    scene mikunightmolly11
    with dissolve

    mi "And I won’t have to worry about blackin’ out every time there’s a loud bang..."
    mi "Or makin’ a big inconvenience for everybody other than Makoto or Karin, who have already figured out how to calm me down..."
    mi "So...yeah...I’m practicing really hard..."
    s "…"
    s "Are you sure you don’t want to tell me {i}why{/i}-"

    scene mikunightmolly12
    with dissolve

    mi "Um!"

    "As expected, Miku cuts in before she even has anything to say."
    "It's desperation at its finest."
    "She wasn’t ready to talk about whatever happened (Or is happening) to her after the first breakdown and she’s still not ready now after the third."

    if bonus == True:
        "And I can’t even tell if I’m closer to or further away from finding out now that I can do things like take her clothes off while her roommate is away."
        "This would feel like progress for most girls."
        "But, in some twisted sort of way, it feels like things might be moving backwards on some fronts."
        "Especially now that Miku has essentially come out and said that she hasn’t really been thinking of something like a future with me and is just acting...hormonal."
        "But that’s too simple. Things are never that simple."

    scene mikunightmolly13
    with dissolve

    mi "Um...it’s not that I...don’t want to tell you..."
    s "Let me guess-"
    s "It’s that you can’t."
    mi "...Yeah."
    mi "B-Besides! We’ve got bigger fish to fry anyway, right Sensei?"
    s "Do we?"
    mi "Yeah...cause like...now that we’ve almost been...caught by Makoto-"
    mi "We should probably...kinda like...cut things off, you know?"
    s "Am I being dumped from a relationship that hasn’t even started yet?"

    scene mikunightmolly12
    with dissolve

    mi "No! I still like spendin’ time with you and wanna keep doin’ that...just..."
    mi "That whole thing was kind of a wake up call..."
    mi "Do you know why Makoto was able to make it over so fast last night, Sensei?"
    s "I just figured it was a coincidence."
    mi "It’s because she came runnin’ the second she heard that bang upstairs."
    mi "It's like a friggin’ reflex for her."
    mi "She didn’t even think to check on where it came from or what happened, just bolted right over to our room because she knows how I am."
    mi "And if somethin’ like that were to happen while you and I were...you know..."

    scene mikunightmolly14
    with dissolve2

    mi "I..."
    mi "I wouldn’t be able to explain it all away again..."
    s "Well there’s always other places we can-"
    mi "You’re...not gettin’ it, Sensei..."

    if bonus == True:
        mi "If I can’t even feel comfortable tellin’ you {i}why{/i} I get like that, do you really think I’m comfortable enough to start doing more...adult-ish things with you?"
        s "I just think you should be doing what you want to do."
        s "That’s how I’ve always lived and I turned out fine."
        mi "It has nothin’ to do with what I want...it’s more about what I can and can’t do."
        mi "I’m pretty friggin’ good at soccer, but if I went out there and was asked to play goalie for a match, I’d be completely useless."
        mi "Bein’ with you is kinda like that. "
        mi "I just got thrown into it all of a sudden and now everything is goin' super fast and I don’t even know if I {i}like{/i} bein’ a goalie yet."
        mi "And Makoto-"
        s "I’m assuming you’re about to tell me that Makoto is a good goalie and that you feel like you’d be taking her position even if you {i}did{/i} train?"
    else:
        s "Just give me the Sparknotes."

    scene mikunightmolly15
    with dissolve

    if bonus == True:
        mi "You adults really are smart. I didn’t even have to finish talkin’ for you to get what I meant."
        s "Just some standard pattern recognition."
        s "I push...you back off...you blame yourself...you bring up Makoto...and then things happen anyway."
        mi "So take a friggin’ hint and stop makin’ things happen."

    mi "You’re smarter and bigger than me and I think you’re really cool so...all that combined means I’m easy to trick."
    s "I can’t be that much smarter than you if you’ve already figured out my tactics. "
    s "There are some girls I’ve spent a lot more time with who still don’t understand that."
    mi "It got easier once I started thinkin’ of you like I think about soccer."
    mi "First rule of playin’ a team stronger than you is to analyze their weaknesses and come up with a plan of attack."
    s "Wouldn’t your plan of attack be that cycle I mentioned before, then?"
    mi "Yeah. But another thing you need to always be prepared for when playin’ a stronger team is for your plan of attack to fail."
    s "Ahh, so we’ve moved into Miku Maruyama’s “Plan B.”"

    scene mikunightmolly16
    with dissolve

    mi "Heck yeah we have! You’ve fallen right into my trap!"
    s "What’s the backup plan then? How are you going to stop me when you seem to already know how I’m going to handle this?"
    mi "Easy!"
    mi "I’m subbin’ myself out and becomin’ a player-coach."
    mi "Now I’m Team Makoto all the way! Puttin’ all my eggs in the basket of the same girl who cares more about me than she does herself."
    s "And you think that’s something that will make you happy?"
    mi "Happy as a peach!"
    s "That’s not a phrase, Miku."
    mi "Cool as a cucumber!"
    s "That one is, but it doesn’t really apply right now."
    mi "When life gives you lemons, make beef stew!"
    s "And that’s just an obscure reference to an early 2000’s TV show that neither of us should know about given our Japanese upbringing and inexposure to American culture."

    scene mikunightmolly17
    with dissolve

    mi "You should be with {i}her{/i}, Sensei. Not me."
    mi "What we’re doin’ right now doesn’t make sense for either one of us."
    mi "She needs you."
    s "And you don’t?"
    mi "Why the heck would I need you? You’re a bad coach and an even worse teacher."
    s "Wow. Why wasn’t this your plan of attack from the get go?"

    scene mikunightmolly18
    with dissolve

    mi "Because wordin’ it like this makes me sound like a quitter. And if there’s anythin’ Miku Maruyama hates, it’s quitters!"
    mi "So without givin’ you time to come up with a backup plan of your own, I’m gonna end things right here! "
    mi "And we’re gonna go back to bein’ buds who keep any weird thoughts we have about each other to ourselves instead of airin’ em out under the covers next to the real heroine of this story!"
    mo "Ohoho~ What’s this I hear about the real heroine?"

    scene mikunightmolly19
    with dissolve

    mi "Oh, Molly! Nothin’ to see here! Just two buds doin’ bud stuff!"
    mo "Cloaked in darkness, a beautiful stranger emerges from the shadows, bringing with her the gift of eternal love and unending...joy!"
    mo "It is she! The main heroine of the-"
    mi "Oh, no. I was talkin’ about Makoto when I mentioned the main heroine. "
    mi "I’m on her team full time now."

    scene mikunightmolly20
    with dissolve

    mo "...I beg your pardon?"
    mi "Yeah. We weren’t talkin’ about you at all, but you’re welcome to join us if ya want."
    s "Sorry, Molly. But keep up the good work. You’ve already seamlessly blended into the harem."
    mo "I need to put more points into charisma..."

    scene mikunightmolly21
    with dissolve

    mo "Oh...and um...Miku-"
    mo "I’m really sorry for adding to the noise the other night...even if it was mostly our neighbors' fault."
    mo "It completely slipped my mind how much things like that upset you."
    mo "I’ll do better to try and keep quiet. Really."
    mi "Oh...you don’t have to apologize for that..."
    mi "It’s not like I expect everybody to work around me or anything."
    s "I highly doubt Molly will succeed in her mission to remain quiet anyway. That’s probably her greatest weakness."

    scene mikunightmolly22
    with dissolve

    mo "Lies! My greatest weakness is fire!"
    mo "Shows how much you know about grass types, Supreme Overlord!"

    scene mikunightmolly23
    with dissolve

    mi "I guess we should probably head back inside now, huh?"
    s "Is your backup plan complete?"
    mi "It’s not really a thing that ever finishes..."
    mi "The game’s on an infinite timer and I’ve just gotta keep the ball away from ya as long as possible."
    s "Well then..."
    s "Here’s hoping our legs don’t tire out."

    scene black
    with dissolve2

    "I see no need to walk Miku back to her room now that Molly has waltzed into the picture."
    "I also see no need for Miku to do something as drastic as giving up on her feelings just so she can support someone else’s."
    "That amount of selflessness can kill someone."
    "You can’t force people into relationships they don’t want to be a part of, though."
    "Which is not me saying, by any stretch of the imagination, that I wanted a “relationship” with Miku."
    "But I wanted something."
    "And I almost got something."
    "But now, with her finally deciding to do something on her own instead of letting me drag her along-"
    "I’ve somehow wound up falling behind."
    "That’s not how this is supposed to work."
    "I look up at the sky as I begin to head home and the light from the moon stings my eyes."
    "A short while later, I receive an apology text from Miku."
    "It’s a lot less detailed than Makoto’s was."
    "It explains nothing."
    "Just says, “I’m sorry.”"
    "I put my phone back in my pocket."
    "I think about responding and telling her not to worry about it, but I know that tends to have a subconscious effect on people that often forces them to do the exact opposite."
    "At the end of the day, I am not happy with how things ended up."
    "And I don’t think Miku is either."
    "But I suppose that this is the path that we’ll have to walk until I manage to steal the ball back."

    $ renpy.end_replay()
    $ miku_love += 1
    $ mikudorm40 = True
    stop music fadeout 5.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

                    ############################################
                    ##########        ROOM 4          ##########
                    ############################################

label rindorm:
    if rin_love >= 5 and cafesugar == True and rinfirstvisit == False:
        jump rinfirstvisit
    if rin_love >= 10 and cafe10 == True and rindorm10 == False:
        jump rindorm10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == False:
        jump rindorm15
    if rin_love >= 20 and cafe20 == True and day50 == True and rindorm20 == False:
        jump rindorm20
    if rin_love >= 25 and rindorm20 == True and rindorm25 == False:
        jump rindorm25
    if rin_love >= 30 and day != 2 and cafe30 == True and rindorm30 == False:
        jump rindorm30
    if rin_love >= 35 and rindorm30 == True and rindorm35 == False:
        jump rindorm35
    if rin_love >= 40 and cafe40 == True and day != 2 and day != 6 and day != 7 and rindorm40 == False:
        jump rindorm40
    if rin_love >= 50 and cafe50 == True and day != 1 and rindorm50 == False:
        jump rindorm50
    if rin_love >= 55 and imanispecial1 == True and futabainvite3 == True and day != 2 and rindorm55 == False:
        jump rindorm55
    else:
        jump rindorm6to9

label futabadorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if futaba_love >= 5 and futabafall == False and futabafirstvisit == False:
                "Please play Futaba's level 5 Library event to unlock the first dorm event!"
                jump doorknock
            if futaba_love >= 5 and futabafall == True and futabafirstvisit == False:
                jump futabafirstvisit
            if futaba_love >= 10 and futabadorm10 == False:
                jump futabadorm10
            if futaba_love >= 15 and library15 == True and futabanew1 == False:
                jump futabanew1
            if futaba_love >= 15 and futabanew2 == True and futabanew3 == False:
                jump futabanew3
            if futaba_love >= 15 and futabanew3 == True and futabadorm15 == False:
                jump futabadorm15
            if futaba_love >= 25 and day > 5 and bookdate == True and futabadorm25 == False:
                jump futabadorm25
            if futaba_love >= 30 and library30 == True and day != 3 and futabadorm30 == False:
                jump futabadorm30
            if futaba_love >= 35 and library35 == True and futabadorm35 == False:
                jump futabadorm35
            if futaba_love >= 40 and day != 3 and dormwar17 == True and futabadorm40 == False:
                jump futabadorm40
            if futaba_love >= 45 and day != 3 and day < 6 and library40part2 == True and futabadorm45 == False:
                jump futabadorm45
            if futaba_love >= 50 and makiinv3 == True and futabadorm50 == False:
                jump futabadorm50
            else:
                jump futabadorm6to9
        "Handjob" if futabadorm15 == True and bonus == True:
            jump futabahjreplay
        #"Blowjob" if futabadorm20 == True and bonus == True:
        #    jump futababjreplay
        #"Boobjob" if day86 == True and bonus == True:
        #    jump futababoobjobreplay
        "Fingering" if futabadorm35 == True and bonus == True:
            jump futabafingerreplay

label futabafirstvisit:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mikudorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if miku_love >= 5 and firsttimesoccerfield == True and mikudorm5 == False:
                jump mikudorm5
            if miku_love >= 10 and soccer10 == True and mikudorm10 == False:
                jump mikudorm10
            if miku_love >= 15 and mikudorm10 == True and mikudorm15 == False:
                jump mikudorm15
            if miku_love >= 25 and soccer25 == True and mikudorm25 == False:
                jump mikudorm25
            if miku_love >= 30 and soccer30 == True and day != 4 and trinity3track == True and mikudorm30 == False:
                jump mikudorm30
            if miku_love >= 35 and makotowinterbeach4 == True and day != 4 and mikudorm35 == False:
                jump mikudorm35
            if miku_love >= 35 and mikudorm35 == True and day != 4 and mikudorm40 == False:
                jump mikudorm40
...
```