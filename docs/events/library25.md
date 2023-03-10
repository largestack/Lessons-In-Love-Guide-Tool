# A Book About Dragons (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Futaba love greater than or equal to 25

* Event [Clam's Tongue](./futabanew3.md) (Futaba) is completed)

* Event [Only Child](./library20.md) (Futaba) is completed)



## Next events

* [Futaba: Under the Table](./library30.md)

## Event properties

* Id: library25
* Group: Futaba
* Triggered by label: library
* Triggered by branch label: library
* Triggered by path: library->library25

## Official wiki page

[A Book About Dragons](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=library25&go=Go) for more details.

## Event code

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label library25:
    scene black
    with dissolve2

    "I decide to spend the morning at the library."

    if bonus == True:
        "Futaba and I haven't done anything exciting together lately, so I’m thinking it might be time to amp things up a bit."
        "Or at least as much as a person like me {i}can{/i} ‘amp things up.’"
        "It’s clear that she’s fond of me. That much I’ve known since the beginning."
        "But if you told me months ago that I’d somehow start developing ‘feelings’ for her, I’d have called you insane."
        "I’m not meant to become attached to anyone."
        "That’s not why I’m here."
        "But there’s something about receiving constant, undeserved affection from someone that sort of flips a switch inside of your head."
        "It makes you think you actually {i}do{/i} deserve it."
        "I wonder if that’s what’s happening to me?"
        "That must be what's happening to me."
    else:
        "Probably because I love reading so much and want to absorb more knowledge so I can become a better teacher."

    "………"
    "……"
    "…"

    scene morningmoon1
    with dissolve2
    play music "gentle.mp3"

    s "…"
    f "…"

    "Sunlight permeates the air of the library, illuminating scattered dust particles trying to sneak their way into my eyes."
    "Amidst my partially-obscured vision stands Futaba Fukuyama, volunteer librarian and full-time student, engrossed in a book I can’t make out from here."
    "I imagine it’s a happy one."
    "Maybe something with dragons or princesses."
    "Something to help distract her from how horrible life really is and how, on average, we consume over fifty pounds of these same dust particles every year."
    "She might not be thinking about that last part, but I am."
    "Anyway, life isn't horrible for her and her alone. It's like that for all of us."
    "And no one who is truly happy with their life spends this much time reading."
    "Reading is an escape mechanism. And if you love where you are, or {i}who{/i} you are-"
    "Well...what is there to escape from?"
    "I imagine you want me to shut up right about now, correct?"
    "Well, I’m sorry, but I won’t."
    "I am here to remind you of how horrible all of this is."
    "Let my words be a floor of daggers, cutting into your feet with every step you take."

    scene morningmoon2
    with dissolve2

    f "Oh, Sensei! I didn’t see you walk in."
    f "How are you this morning?"
    s "I’m pretty good. What are you reading?"
    f "Huh? Oh, just some book about...umm..."

    scene morningmoon3
    with dissolve

    f "Umm..."

    "She looks away in an attempt to escape from her escape mechanism."

    f "I guess it's about...dragons...and stuff...hahah..."

    "Princesses too, I imagine."

    scene morningmoon2
    with dissolve

    f "Things have been pretty slow around here lately, so I was reorganizing the fantasy section."
    f "But...then I came across a book I used to read when I was little and..."

    scene morningmoon3
    with dissolve

    f "Well, one thing kind of led to another..."

    scene morningmoon2
    with dissolve

    f "Did you read a lot when you were younger, Sensei?"
    s "Me?"
    s "Uhh...I-"
    f "..."
    s "..."
    f "Sensei?"
    s "Sorry. I just feel like there's something I want to say here, but I can't quite put my finger on it..."
    f "You...um..."

    scene morningmoon3
    with dissolve

    f "I'm...also having a hard time finding the words I want to say, but...I imagine someone as talented as you read quite a lot when you were a child."
    s "Maybe I did. Maybe I didn't. There's no way to know for sure."
    f "No, I suppose there isn't..."

    scene morningmoon2
    with dissolve

    f "But I don't think it was luck alone that got you here, Sensei."
    f "And I think that...it isn't entirely a bad thing to just...{i}make up{/i} memories if you can't find ones you enjoy on your own."
    s "That's a...relatively uncharacteristic thing for you to say, Futaba."

    scene morningmoon4
    with dissolve

    f "Is it? How so?"
    s "You've just always struck me as the more...honest type."
    f "I don't think what I suggested was dishonest. I see it as...just one more form of creativity?"

    scene morningmoon2
    with dissolve

    f "Like...writing a book! Just the book is {i}you.{/i} And it's highly probable that you just...filled in the pages out of order and have to...go back and make some corrections?"
    s "Nice try. But I'm sure that whatever I have to say about my reading habits as a child isn't anywhere near that...dramatic or serious."
    s "I'm pretty positive I was just a normal person who did normal shit and is now going to work a normal job until he dies."
    f "I think you're amazing, Sensei. I-"
    s "I didn't come here to talk about myself, Futaba. Tell me about what you want to do instead."

    scene morningmoon5
    with dissolve

    f "Oh...I'm...Okay, sure!"
    f "I still don’t...really know what I want to do when I'm done with school..."
    f "But it's probably a safe bet to assume it’ll be something involving books."

    scene morningmoon3
    with dissolve

    f "Maybe I can get a job at a publishing company or...open a book store?"
    f "Would you come visit me if I owned a book store, Sensei?"
    s "Of course. I already come visit you at the library all the time."
    s "Might be nice to get a discount on stuff too. Maybe I'd actually pick up a book for the first time in...well, as long as I can remember."
    f "Everything here is free...isn’t that the biggest discount there is?"
    s "Yeah, but I need to give everything back and that's no fun."

    scene morningmoon6
    with dissolve

    f "Well...you never take anything out in the first place, so..."
    s "That’s just because I’m kind enough to leave the books for people who need them more than me."
    f "How awfully considerate of you..."

    scene morningmoon2
    with dissolve

    f "But, I guess I understand. Book stores are much more fun than libraries."
    f "It’s nice owning the things you care about."
    f "The value of something that’s already been used by someone else is always a little worse, isn’t it?"
    s "Yeah...something like that."

    scene morningmoon7
    with dissolve

    f "Th...That being said..."
    f "I'm glad you showed up today, because..."
    f "Well, there’s actually something I’ve been meaning to ask you for a little while now, but I’m kind of nervous so..."
    f "I’m not really sure if {i}right now{/i} is the best time or...if I'll even be able to follow through with it..."
    s "Is this a confession?"

    scene morningmoon8
    with dissolve

    f "Keh-!"

    "Looks like I might have hit the nail on the head."

    scene morningmoon9
    with dissolve

    f "That's...That’s not it! That comes later!"
    s "So...it {i}is{/i} coming then?"
    f "I...never said that!"
    s "It was {i}very{/i} heavily implied. Besides, do you really think I don’t know by now?"
    s "I’m not some dense harem protagonist- I’m the other kind. The kind that's suspiciously successful with girls despite putting in virtually no effort whatsoever."
    f "That sort of character is entirely unrealistic, Sensei."
    s "Exactly. Nothing is real, Futaba."
    f "Nothing is...real?"
    s "Not you, not me..."
    s "Nothing."

    scene morningmoon4
    with dissolve

    f "That's...an interesting philosophy."
    s "I'm sure there's more to it, but I didn't really have any idea where I was going with it."
    s "Just in a weird mood today, I guess."

    scene morningmoon5
    with dissolve

    f "Well, I'm glad your weird mood landed you here..."
    f "Because what I've been meaning to ask you involves...umm...a yes or a no...And I'd like to know soon so I can stop agonizing over your answer."
    s "But...it's {i}not{/i} a confession?"
    f "It's not a confession."
    s "Because that made it sound a lot like a confession."

    scene morningmoon9
    with dissolve

    f "Stop calling it that! My heart can't take it!"

    scene morningmoon3
    with dissolve

    if bonus == True:
        f "I’d understand if you don’t want to do it since I’m kind of...you know...a {i}little{/i} bit younger than someone you’d want to spend time with outside of school."
        s "I think I’ve made it overwhelmingly clear that our age gap makes zero difference to me."
    else:
        s "If it's about how many spiders human beings consume in their sleep every year, I really don't want to hear it. I think I've made my distate for factoids like that clear enough by now, haven't I?"

    f "This is a little...different, though."
    f "Almost everything we've done has been here...or the dorms...We've barely been to any places where we'd seem...{i}out of{/i} place."
    f "And I'm comfortable with you everywhere, but..."

    scene morningmoon5
    with dissolve

    f "That doesn’t mean it’s not a little nerve-wracking when I think about going somewhere else."
    f "I li-...I really respect you as a person and a teacher and I’m worried that you’ll maybe..."

    scene morningmoon3
    with dissolve

    f "I don’t know...get bored of me or something?..."
    f "It’s hard to explain."
    s "Then don’t explain it. Just ask whatever you want to ask me and we’ll take it from there."
    s "It’s probably just about accompanying you to a new book store or something along those lines, right?"

    scene morningmoon8
    with dissolve

    f "Keh-!"

    "Second nail hit. This fence will be built in no time at all."

    f "H-H-How did you-"
    s "It's the next logical step, isn't it? Something with the potential to pull the two of us closer together."
    s "If we don't start doing things like that, everything will just...stagnate."

    scene morningmoon4
    with dissolve

    f "Stagnate? How so?"
    s "You know that fake Einstein quote about how doing the same thing over and over again is the definition of insanity? Well, that applies to relationships too."
    s "We can't just confine our time together to school or the dorm. Fake Einstein would hate that."
    s "So, if going out there and doing new things together is how we're supposed to keep this alive, sure. I see no problem with that."
    f "Is that really what you think?"

    scene morningmoon7
    with dissolve

    s "Is {i}what{/i} really what I think? I said a lot just now."
    f "That we'll...fizzle out if we don't open up a little more."
    f "Because all this time, I was worried that the exact opposite would be the biggest issue for you."
    s "The world is big, even if the majority of it is closed off to us."
    s "But that doesn't mean we should trap ourselves in an even smaller box because we're afraid of what might be outside."
    f "So..."

    scene morningmoon2
    with dissolve

    f "Wait, does that mean you’ll come?"
    s "..."
    f "..."
    s "Of course. It would be pure evil if I were to build this up like that and then say no."

    scene morningmoon10
    with dissolve

    f "Hahaha! It really would!"
    f "But I never really know with you and...and..."

    scene morningmoon10r
    with dissolve

    f "You...have no idea how excited this makes me, Sensei..."
    f "I didn’t think...you’d ever want to go on a date with someone like me..."

    "To be fair, I never said it was a {i}date{/i}...But I guess that was heavily implied as well."
    "And it's not like I mind. Futaba can probably pass as a college student if the two of us go out together anyway."
    "Plus, if it can get her to smile like that, she can ask me on as many {i}dates{/i} as she wants."

    s "I guess you were wrong, then. But let me ask you this...why aren't {i}you{/i} weirded out by the idea of being seen with me?"
    s "If people {i}do{/i} see us together, they might assume all types of things."

    scene morningmoon10r2
    with dissolve

    f "And...they would probably be right about half of them."
    s "Fair point."

    scene morningmoon2
    with dissolve

    f "Besides, I love the idea of being seen with someone like you!"
    f "I feel like any time I go anywhere, it's with either Rin or one of my friends from my old school...and you're so much...well...{i}cooler{/i} than them."
    s "Don't let Rin hear that. She'll probably cry."

    scene morningmoon10
    with dissolve

    f "Heheh...probably..."
    s "Can I ask you one more question before I head out, Futaba?"

    scene morningmoon2
    with dissolve

    f "Of course, Sensei! Ask anything you-"

    if bonus == True:
        s "Are you absolutely positive you're not asking me out because you’re actually in love with me? Because now would be a good time to just admit it already."
    else:
        s "You’re positive it’s not because you want another hug?"

    scene morningmoon8
    with dissolve

    f "Keh-!"

    "Third nail. Fence complete."

    scene black
    with dissolve2

    "Futaba and I make plans to meet at her dorm room sometime over the
    weekend and she goes over where the store is located."
    "Apparently, it’s not all that far from here and is open relatively late, so we should be
    able to head over at night."
    "It’s strange going on a nighttime ‘date’ to a book store, but I guess it is what it is."
    "I’m just glad that I’ll be getting to spend more time with her."
    "And that, for some strange reason...she continues to give me things I do not deserve."

    $ renpy.end_replay()
    $ bookdate = True
    $ futaba_love += 1
    $ library25 = True
    stop music fadeout 6.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label library30:
...
```

## Code that triggers this event

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label library:
    if futaba_love >= 0 and firsttimelibrary == False:
        jump firsttimelibrary
    if futaba_love >= 5 and futabafall == False:
        jump futabafall
    if futaba_love >= 10 and library10 == False:
        jump library10
    if futaba_love >= 15 and futabadorm10 == True and library15 == False:
        jump library15
    if futaba_love >= 20 and library20 == False:
        jump library20
    if futaba_love >= 25 and futabanew3 == True and library20 == True and library25 == False:
        jump library25
...
```