# Every Day I Grow Some More
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=start&go=Go)



## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: start
* Group: Main

## Event code
File: \game\script.rpy
Code:
```python
...
label start:

    stop music fadeout 10.0
    # To stop everything for 4 seconds use --- $ renpy.pause(4, hard=True)

    scene myname
    with dissolve2
    $ renpy.pause(4, hard=True)

    scene black
    with dissolve2

    scene warning2
    with dissolve2
    $ renpy.pause(5, hard=True)

    scene black
    with dissolve2

    if bonus == True:
        scene warning1
        with dissolve2
        $ renpy.pause(3, hard=True)
    else:
        scene sfwwarning
        with dissolve2
        $ renpy.pause(3, hard=True)

    scene black
    with dissolve2

    scene warning0
    with dissolve2
    $ renpy.pause(3, hard=True)

    scene black
    with dissolve2

    scene audiowarning
    with dissolve2
    $ renpy.pause(4, hard=True)

    scene black
    with dissolve2

    scene contentwarning
    with dissolve2
    $ renpy.pause(3, hard=True)

    scene black
    with dissolve2

    play music "goodmorning.mp3"

    "There are several things in life I have accepted that I will never understand."
    "The first of which has been explained to me many times- "
    "It’s the way floating dust particles manage to shimmer and glow when hit at the correct angle by light. "
    "How something invisible to the naked eye can be {i}made{/i} visible by pure electromagnetic radiation...or something like that."
    "I’ve retained the information. I’d be foolish not to after how many times I have heard it."
    "But I will never understand."
    "The second thing is the romanticization of death. "
    "And how there are people who speak of it with such fervor that it often appears to bring them more joy and curiosity than the unwrapping of presents on Christmas morning."
    "The third thing is you."
    "You’re a curious one...do you know that?"
    "Trapped in the dark, suspended somewhere between life and death...with eyes swollen shut so dramatically that you can’t even see the dust I’ve taken the liberty of illuminating for you."
    "I want you to be just as confused as me, you know?"
    "It’s lonely here."
    "It’s lonely having no one to talk to...no one to submerge myself in uncertainties with."
    "It’s just me, the dust, and the incessant circling of the drain that is the idea that I will, one day, no longer be able to share little thoughts like these with anyone."
    "Do you like poetry?"
    "..."
    "Yes?"
    "No?"
    "I’m sorry. I’m sure it’s difficult to answer a question like that in your current state."
    "Personally, I’ve never been a big fan of it. "
    "It requires too much...interpretation. To the point where sometimes, even the clearest of thoughts have a variety of different meanings that all go on to contradict one another."
    "But-"
    "There is one line from a very famous poet paraphrasing a very famous politician that goes something like..."
    "{i}There is no beauty without some strangeness in its proportions.{/i}"
    "And I like that line very much."
    "In fact, I’m sure that if you don’t already enjoy it yourself, that you’ll come to do so soon."
    "Because where you’re going is somewhere special."
    "Somewhere with so much strangeness in every single one of its proportions that you’ll be forced to understand how truly beautiful life can be, even during its darkest moments."
    "Would it be a bit preemptive for me to tell you that I love you?"
    "Not romantically, of course. We barely even know each other."
    "But I love that you’re here. "
    "I love that we’re here together because, like I said, I have been very...{i}very{/i} lonely."
    "I’m sure you’ll come to despise me in time."
    "I’m sure these little conversations that I’ll force you to have with me will eat away at you like botflies. "
    "And I’m even more sure that every one of the thoughts I share with you will get underneath your skin like the eggs those botflies lay."
    "But it’s all for good reason, you see."
    "It’s because that is my job."
    "It’s because, for some reason even I don’t understand, I was chosen to be your personal, mysterious and anonymous narrator."
    "Will we ever meet for real?"
    "Who knows?"
    "But I hope so."

    scene sky
    with dissolve2
    play sound "windlong.mp3"

    "Now, then!"
    "I suppose it’s time we get down to business."
    "Ahh, how I have missed the daylight."
    "There’s nothing quite like the feeling of sunlight soaking into your skin on a hot, summer day."
    "But I’ve bothered you enough already, so I won’t get the two of us sidetracked with some tangent about the weather."

    stop sound fadeout 10.0

    "Especially since it’ll be like this for...well, you’ll see soon enough."
    "Oh! There is {i}one{/i} more thing I’m obligated to tell you before the game starts, though. "
    "You can take it seriously or not, it doesn’t matter to me. This will be {i}your{/i} life after all- and what good is a life where you can’t even think for yourself?"
    "Anyway, the thing I’m supposed to tell you is this..."
    "Nothing is real."
    "Not me...not you...not {i}anyone{/i} you’ll meet in the journey you start today."
    "We’re all just air."
    "So..."
    "How about we breathe {i}together?{/i}"
    "It’ll be fun! "
    "Go on! Expel your worries from the depths of your lungs and envelop yourself in happier days!"
    "For this world was made for you and you alone."
    "I can’t tell you {i}who{/i} made it...and I sure as hell can’t tell you why {i}you{/i} were special enough to be given something like this."
    "But I can tell you, and I truly do wish this from the bottom of my heart-"
    "That I hope you have fun."
    "And if you’re ever feeling lost or lonely, all you have to do is close your eyes and I’ll be right there-"
    "Annoying you every step of the way."
    "So!"
    "Are you ready?"

    menu jumpymenu:
        "Yes":
            jump timetojump
        "No":
            "You’re not?"
            "Huh."
            "I guess it wouldn’t kill us to hang out for a little while longer, then."
            "So...what kind of stuff are you into? Any hobbies? "
            "Interests?..."
            "..."
            "Anything at all?"
            "..."
            "..."
            "..."
            "You know, if you’re going to keep me here, you should at least respond or something. Staying silent when someone is talking to you is very rude."
            "..."
            "..."
            "..."
            "Hah..."
            "Okay, you know what? As your one and only friend right now, I’m going to give you a little push."
            "Not a {i}literal{/i} push. That would be like, {i}really{/i} bad right now. I think."
            "No, the push I’m going to give you is courage. "
            "You can do this."
            "I know that it’s scary. {i}Everything{/i} is scary. That’s just kind of how life works, you know?"
            "But I believe in you."
            "And I can’t imagine that ever changing. "
            "We’re a lot closer than you think."
            "So...with that said-"
            "Are you ready {i}now?{/i}"

            menu:
                "Yes":
                    jump timetojump

label timetojump:
    "Great!"
    "Then..."
    "Without further ado..."
    "Jump as high as you can!"
    "As far as you can!"
    "Fly away, little bird! Spread those wings of yours!"
    "For what awaits you out there is far more amazing than anything you could ever find on this rooftop!"
    "Go!"
    "Become a better you!"
    "And remember that I’ll be right here watching."
    "{i}What do I want to do?{/i}"

    menu:
        "Jump":
            jump start2
        "Jump":
            jump start2
        "Jump":
            jump start2
        "Jump":
            jump start2
        "Jump":
            jump start2
        "Jump":
            jump start2

label start2:

    stop music

    "Welcome home."
    "6e 6f 74 68 69 6e 67 20 66 61 6c 6c 73 20 62 75 74 20 6d 65"
    scene black
    play sound "static.mp3"
    scene whyme with flash
    scene whygodwhy with flash
    scene whyme with flash
    scene whygodwhy with flash
    scene whyme with flash
    scene whygodwhy with flash
    scene lessons
    stop sound
    $ renpy.pause(3, hard=True)
    scene black with dissolve2

    "..."
    "..."
    "..."

    q ".....i?"

    "What?..."

    q "...sei?"

    "I..."
    "I can hear something..."

    q "Sensei..."

    "I can-"

    q "Sensei! Wake up already!"

    scene timetogrow1
    with dissolve4
    play music "10c.mp3"

    q "About time! Do you have any idea how much trouble you'd get into if the principal showed up and caught you sleeping right now?"
    s "Huh?..."
    q "Class ended ten minutes ago. It's time to get up."
    s "What? What class?"
    s "Where am I?"
    s "And...what did you call me just now?"

    $ totaldays += 1
    $ day += 4
    if day == 4:
        show thursday onlayer date
        jump nextstartt
    else:
        jump nextstartt

label nextstartt:
    scene timetogrow2
    with dissolve

    q "The...same thing I always call you? Sensei."
    q "What's going on? Did you have a bad dream or something?"
    s "I..."
    s "..."
    s "I guess so..."
    q "Do you want me to call the nurse or something? You seem a little flushed."

    scene timetogrow3
    with dissolve

    q "Come a little closer so I can touch your forehead and find out."
    s "I'm fine...I think I just need a few minutes to collect myself or something."

    "Excuse me for asking this so abruptly, but-"
    "What the fuck is going on right now?"
    "Who is this girl? Or, better question, who am {i}I?{/i}"
    "Why can't I remember anything?..."
    "This classroom seems vaguely familiar, but..."
    "But it's like each time I try to piece things together, I just circle back around and give up before I'm able to get anywhere."

    q "...?"

    "This girl should probably know something, right?"
    "But...if she's my student, she'll probably only know things that a {i}student{/i} would know. She'll have no idea who I am or...where I even live or-"
    "Wait, where am I supposed to go after I leave here when I still have absolutely no clue where I am?"

    scene timetogrow4
    with dissolve

    q "Um...are you sure you're okay? You're looking a little...panicky."
    s "I'm just...tired, I think."
    q "Still? Even after sleeping through the entire last period?"
    s "Yeah, sorry. Long night, I guess."

    scene timetogrow5
    with dissolve

    q "Long night? But we were together the whole time."
    s "I'm sorry, what?"

    "Am I...dating a teenager?"

    scene timetogrow6
    with dissolve

    q "Okay, seriously. What's going on with you? You're acting like you don't even recognize your own niece."

    "Oh. So that's how it is."
    "Well, that is significantly less exciting. But at least I should be able to leverage that role to...try and make sense of what's going on here."
    "At the very least, if we're related, she'll probably know where I live."

    s "Of course I recognize you. I'm just feeling a little out of it right now."

    scene timetogrow2
    with dissolve

    q "Well, do you think going home might help? Because it doesn't seem like sticking around school is helping you at all right now."
    s "Yeah, but...do you think you might be able to come with me? I could probably use the help since I'm still...you know, regaining my footing and whatnot."
    q "Why would I not come with you? We literally live together."
    s "Oh. Right. I forgot."

    "Well, at least my first five minutes in what I'm assuming is some sort of...alternate reality or something have been filled almost entirely with convenient coincidences."
    "That has to be what this is, right? Some sort of...reincarnation type thing?"
    "Wait, doesn't this mean that I must have died, though?"
    "Just what the hell is happening to me all of a sudden?"

    scene timetogrow7
    with dissolve

    q "How can you just {i}forget{/i} that we've been living together for years?"
    q "What's next? Are you going to tell me you've forgotten my name?"
    s "..."
    q "..."

    scene timetogrow8
    with hpunch

    q "Oh my God! You {i}have{/i} forgotten my name, haven't you?!"
    a "It's Ami, Sensei! {i}Ami!{/i}"
    s "Sorry. It's nothing personal...probably."
    a "Probably?!"
    s "To be completely honest, I'm having a hard time remembering literally anything right now. So...I'll probably be leaning on you for help for a little while."

    scene timetogrow9
    with dissolve

    a "I mean...helping you is pretty much all I do in the first place, so I'm happy to do whatever you need me to."
    a "But if your memories are really that jumbled, shouldn't we take you to a doctor or something?"
    a "You're old, but I didn't realize you were old enough to start dealing with that dementia thingy."
    s "I'm not {i}that{/i} old, am I?"

    "This body feels mostly healthy and well put together, so I can't imagine I'm any older than my 30's."

    a "I guess not. You're actually one of the youngest teachers we have, I think."
    a "But if there's something wrong with your brain, we should act now. Because if anything bad ever happened to you, I'd probably just die too."
    s "That seems...excessive."

    scene timetogrow10
    with dissolve

    a "Well, if your memories really are gone, you'll be finding out very soon that that's just the type of girl I am!"

    scene timetogrow11
    with dissolve

    a "Or you're just lying about all of this because you hate me and want to play a weird prank on me, but I'll play along either way!"
    a "Helping you round up your memories sounds kinda fun, actually. It's like we're characters inside of a manga now or something."
    s "Yeah...or something."

    scene timetogrow12
    with dissolve

    a "I wonder how it'll end. Normally, all of the stuff where the main character loses his memories ends up being kinda depressing by the last volume."
    s "I think there are more pressing matters at hand than figuring out how things are going to {i}end{/i} right now."

    scene timetogrow11
    with dissolve

    a "Right, right. We've gotta get you back home since you can't remember where you live without me."
    a "You know, Sensei, if you want to spend more time with me, all you have to do is ask. You don't have to fake amnesia just for my attention."
    s "Well, please forgive me if I continue to {i}fake{/i} it for a little while longer."

    "Because at this point, I still have no idea what I'm supposed to do..."

    scene black
    with dissolve2

    "Ami spins around and I instinctively leave my desk to follow her, like it's something I've done time and time before."
    "It's not, though."
    "This isn't my life."
    "It can't be."
    "Because no one would ever look at me the way she does if this is where I'm meant to be."
    "Without even knowing myself yet, I understand that much."
    "For as she pulls me through the halls of the school by my wrist, my mind ventures forth to forbidden territories-"
    "And it encircles itself in possibilities and fantasies I will not yet reveal to you."
    "If I did, I can't imagine you'd stay to observe me much longer."
    "But I suppose I don't even know who {i}you{/i} are...or who I'm even aiming these thoughts at right now."
    "Perhaps-"
    "Well...perhaps they don't need to be aimed anywhere at all."
    "And perhaps I'm content with just imagining someone is there as it makes daydreaming all the less lonely."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ everyday = True

label startsleepover:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```