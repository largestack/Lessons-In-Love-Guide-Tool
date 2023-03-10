# Resurrection Sickness (Molly)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Molly love greater than or equal to 25

* Event [Unsleeping Aegis](./tsuneyodorm25.md) (Tsuneyo) is completed)

* Event [Technicolored Happiness Explosion](./rindorm50.md) (Rin) is completed)

* Day of week is a weekend



## Next events

None

## Event properties

* Id: mollycafe25
* Group: Molly
* Triggered by label: mollycafe
* Triggered by branch label: mollycafe
* Triggered by path: mollycafe->mollycafe25

## Official wiki page

[Resurrection Sickness](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mollycafe25&go=Go) for more details.

## Event code

File: (install folder)\game\MollyEvents.rpy

Code:
```python
...
label mollycafe25:
    scene mollycleaning1
    with fade
    play music "cafe.mp3"

    mo "Guh..."

    "It’s dark by the time I make it to the cafe. "
    "Molly, still attempting to put the pieces of herself together after losing several of them recently, has spent the last ten minutes wiping down the same spot on the counter without realizing it."
    "I think about informing her but, at this point, I’m curious to see whether or not she can manage cleaning it so thoroughly that it burns a hole into the bar."
    "I imagine that we are at least another ten minutes away from anything like that happening, unfortunately. "

    s "Keep it up, Molly. Just a little while longer until your goal is accomplished."

    scene mollycleaning2
    with dissolve

    mo "Are you kidding, Sir? We’ve been closed for ten minutes already and there are still guests inside. I am never going home."
    mo "At this rate, my long rest is going to turn into a short rest and I’m not even going to recover all of my hit points."
    mo "Do you have any idea how low my health is right now? A leaf could fall on my foot and knock me unconscious."
    s "Sounds like a big leaf."

    scene mollycleaning3
    with dissolve

    mo "Hah. Getting eliminated by nature certainly would be an ironic way to go after spending most of my life indoors."
    mo "If only I had listened to my father and went outside to play with all of the “normal” kids more often. "
    s "I’m a little confused about what a “normal” Molly would even be like."

    scene mollycleaning4
    with dissolve

    mo "Probably a little like the abnormal one, but less loud and better at not destroying friendships."
    s "Yeah. I figured that might have had something to do with your unenthusiastic demeanor tonight."
    mo "Unenthusiastic demeanor?"
    s "You’ve been wiping the counter for ten minutes now."
    mo "It’s really dirty."
    s "In just one spot?"
    mo "…"
    mo "Yes."
    s "Molly, come on. You’re not fooling anyone."

    scene mollycleaning5
    with dissolve

    mo "Okay, yeah. So maybe I {i}am{/i} a little less...rambunctious than normal. But my inability to maintain long lasting relationships isn’t a part of that, Sir."
    mo "I’ve simply been losing sleep lately."
    s "Right. And {i}why{/i} are you losing sleep, Molly?"

    scene mollycleaning6
    with dissolve

    mo "Why, gaming of course!"

    if bonus == True:
        mo "I don’t have time to grieve over my missteps when I have alts to level and fictional characters to put my fictional penis inside of!"
    else:
        mo "I don’t have time to grieve over my missteps when I am too busy making my Saurfang costume for Blizzcon!"

    s "Yes, I can see now how valuable your time truly is."
    s "Are you sure that’s it, though?"

    scene mollycleaning7
    with dissolve

    mo "You’re showing an awful lot of concern tonight when you normally seem to completely overlook me, Sir."
    s "I never {i}overlook{/i} you. You’re just a little more exhausting to spend time with than most of the other girls."
    mo "That makes sense."
    s "Plus, I always manage to be around people when they’re at the worst of their worst, and I’d like to avoid that with you if at all possible."

    if bonus == True:
        mo "You already found me at the worst of my worst when I was...admiring Rin’s Instagram. "
    else:
        mo "You already found me at my worst that one time where you walked into the janitor's closet and founding me kissing a mop."

    s "Was that really the {i}worst{/i}?"
    mo "Not at the time, but I imagine the embarrassment will linger in my mind far longer than what I am experiencing now."
    s "That sounds...surprisingly mature for you."

    scene mollycleaning8
    with dissolve

    mo "Then I suppose it would be for the best if I were to compare it to yet another reference to a video game you have never played in hopes that you will somehow understand what I’m talking about."
    s "That’s the Molly I know."
    mo "This whole thing with Rin is like a bout of resurrection sickness."
    mo "For a little while, everything is going to hurt a lot more than normal. And I’m going to have to be more careful about the things I do and...who I party up with."
    mo "But that will fade over time. "
    mo "I just need to go AFK for a little while. Or put myself on autorun against the corner of a wall or something like that."
    s "Well, if anything, you have definitely succeeded in getting me lost."

    scene mollycleaning9
    with dissolve

    mo "You know...the worst part of all of it isn’t that she’s with someone else now. Or that things between us will take a long time to get back to normal."
    mo "It’s the embarrassment of what happened. And the moments at work where our eyes meet and we have to quickly look in opposite directions to avoid feeling awkward around one another."
    mo "It’s like a scene out of the end of a visual novel, where two characters who were once close have grown apart and don’t want to stop each other from going their separate ways."
    s "Who are you and what have you done with Molly?"

    scene mollycleaning10
    with dissolve

    mo "Gah! I’m sorry, okay?! The sleep deprivation is making me more mature than I want to be!"

    scene mollycleaning11
    with dissolve

    mo "Besides, just because the hardest part isn’t what I expected doesn’t mean the whole thing isn’t hard at all."
    mo "It sucks. I hate it times a million and I want these stupid human feelings to leave my body so I can go back to focusing on games and nothing {i}but{/i} games."
    s "Maybe preserve a little bit of that focus for work, though. "

    s "Haruka will be mad if you clean a hole into her bar."

    scene mollycleaning3
    with dissolve

    mo "{i}Hah.{/i} To tell ya the truth...I haven’t really been a great employee as of late."
    s "{i}What? You? No...{/i}"

    scene mollycleaning2
    with dissolve

    mo "Okay. I haven’t been a great employee as of...ever."
    mo "But I’ve been even worse lately."
    mo "Honestly, Sir? I think I would have been fired already if Haruka didn’t understand, to some extent, the feelings I am so unfortunately...feeling right now."
    s "Then the least you can do is not destroy her belongings."

    scene mollycleaning4
    with dissolve

    mo "Sir, may I ask you a question?"
    mo "Does being disliked and being bad at your job ever keep {i}you{/i} awake at night?"
    s "I thought it was gaming that was keeping you awake at night?"
    mo "Well...yes. It is."
    mo "Games certainly are the most prominent cause of my current lack of energy, but there {i}are{/i} times that I have to lay in bed where I can’t just...escape it all."
    mo "At least not until the NerveGear is actually developed and I can just full dive into a completely different world and start over from zero."

    scene mollycleaning12
    with dissolve

    mo "Ooh! If that ever happens, you should come with me!"
    s "If what happens? I think you forgot that not everyone understands your lingo again."
    mo "A virtual reality helmet that lets you live a completely new life inside of a virtual realm!"
    mo "Think of all the amazing things you could do there!"

    if bonus == True:
        s "I could finally have sex with an elf..."
    else:
        s "I could finally hug an elf..."

    scene mollycleaning13
    with dissolve

    mo "Oooh, an elf lover. "

    if bonus == True:
        s "Hey, no one mentioned love. I just want to bang one."
    else:
        s "Hey, no one mentioned love. I just want to hug one and tell him or her they are important."

    mo "Luckily for you, NPCs are incapable of love! And in a fictional setting, they’d probably be easier to woo as well!"
    mo "Not that you have any issue with wooing women or anything. I mean, you {i}are{/i} the Herald of the Adolescents, after all."

    if bonus == True:
        s "I’m just going to assume that this section of the conversation is over and that I have your full support when it comes to interspecies sexual intercourse."
    else:
        s "Thank you, Molly. You are always so helpful and full of knowledge."

    scene mollycleaning14
    with dissolve

    if bonus == True:
        mo "Of course, Sir! In fact, I have a lengthy list of h-games readily available to scratch that exact itch of yours!"
    else:
        mo "Of course, Sir! And if you are looking for a game where you can hug as many elves as you would like, might I suggest-"

    s "Thanks, but I’ll probably stick to real humans for the time being."

    scene mollycleaning3
    with dissolve

    mo "Gah. How boring."
    s "Weren’t you head over heels for an actual human being until just recently?"

    scene mollycleaning2
    with dissolve

    mo "Well...yes. But then I received a cruel reminder as to why I shouldn’t be getting involved in affairs like that in the first place."
    mo "I’m happy that Rin is happy. "
    mo "Well, partially happy."
    s "And the other parts?"

    scene mollycleaning7
    with dissolve

    mo "Well...they’d obviously have to be unhappy, wouldn’t they?"
    s "Unhappy {i}why{/i}?"
    mo "…"
    mo "Probably...the same reason I’m happy. Just spun around until it can’t stand up anymore and has to throw up all over the floor."
    s "It’s okay to just...not be happy, you know? I-"

    scene mollycleaning15
    with dissolve

    mo "Thank you, Sir. But I’d like to save a conversation as depressing as this for a time when it’s easier for me to escape into more allusions."
    s "Sure. That’s fine. I just don’t want you feeling down if there is an option to not do that."
    mo "That is the issue, though, Sir. "
    mo "I {i}deserve{/i} to feel down right now."
    mo "I did a horrible thing. Not just once, but twice. "
    mo "If I get hung up on the fact that it did not personally benefit me instead of being happy for a friend or...{i}whatever{/i} she is now, who finally got something she wanted..."
    mo "Well...I think I’d feel even worse about myself than I already do."
    s "So what, then? Are you just going to go back to ignoring those feelings?"
    mo "If you get good enough at ignoring something, it eventually feels like it’s not even there."
    mo "And while it might not sound like a storybook ending, that outcome would be better than anything else I can think of right now."
    s "…"
    s "It sounds good to me too."

    scene mollycleaning16
    with dissolve

    mo "Yeah?"
    s "Yeah. "
    s "To be honest, I was expecting you to be doing a lot worse than you actually are."
    s "I know that you’ve been through some pretty rough shit in the past, but I also know that this was important enough for you to break down in my arms about before."
    s "But if you feel like you’re capable of just ignoring it and letting time do its shitty thing of taking forever to make you feel slightly better, go for it."
    s "Not like I can really help anyway."
    s "Oh, also, your last customer just left."

    scene mollycleaning17
    with dissolve

    mo "A-ha! Then you {i}can{/i} help!"
    s "Please don’t make me clean the store. I don’t work here."

    scene mollycleaning18
    with dissolve

    mo "So you’ll do anything possible to cheer me up {i}except{/i} for helping me do my job?"
    s "I don’t think I ever said {i}anything{/i}."
    mo "I believe it was implied, Sir. "
    mo "Are you not aware of my incapability to perform at my full potential right now?"
    mo "There is a darkness growing within me that is sucking out my life essence as we speak. How would you feel in my shoes?!"

    if bonus == True:
        s "Eh. Getting life juice sucked out of me doesn’t sound too bad right now."
    else:
        s "Probably bad. I think my feet are bigger."

    scene mollycleaning19
    with dissolve

    if bonus == True:
        mo "W-Well...no! I guess...it would make sense for you to say that!"
    else:
        mo "Uh...probably!"

    mo "But I would still very much appreciate it if you could, at the very least, place the chairs on top of all of the tables."

    scene mollycleaning20
    with dissolve

    mo "As a...one time favor to me for...not making your life as difficult as you expected me to tonight."
    s "…"
    mo "And also if you’d walk me home after we’re done."
    s "So a two time favor."
    mo "One time consisting of two things."
    mo "Maybe a third when we get back to the dorm. Who knows?"

    if bonus == True:
        s "Can you do {i}me{/i} a favor when we get back to the dorm?"
        mo "Is this favor you have in mind a lewd one?"
        s "Is it {i}allowed{/i} to be a lewd one?"
        mo "Is my name Molly Medb MacCormack?"
        s "...Maybe?"
        mo "Wrong! It is Molly Moyra MacCormack!"
        mo "Why do you not know this?!"
        s "It wasn’t in your character profile."
    else:
        s "My father never taught me how to do any handyman-type things, so if you need a lock replaced or something, you should probably just ask Io."

    mo "Silence! Chairs! Go go go!"

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I sigh to myself and somehow let Molly bully me into helping out in some way."
    "I really don’t care as much as I made it seem, though."
    "It’s not like this place has {i}that{/i} many chairs...and the ones they do have are relatively light."
    "As such, I’m able to finish the task in several minutes and proceed to wait by the counter (That lives to see another day) for Molly to finish her portion of the work."
    "She does what I imagine is a half-assed job and finishes up in about twenty minutes before changing back into her winter clothes and beckoning me outside."
    "………"
    "……"
    "…"

    scene mollycleaning21
    with dissolve
    play music "molly.mp3"

    mo "Alas, the stars have retreated back into their caves in the depths of the night sky...preserving their light for the end of days as it steadily approaches."
    s "There are no caves in the sky, Molly."
    mo "Of course I know that, Sir."
    mo "I just mean that there’s a clear amount of light pollution here. It’s not like it was at the beach."

    scene mollycleaning22
    with dissolve

    s "Ah. I guess not."
    s "I wouldn’t really expect any less in a city, though."
    mo "You don’t have to expect something before being disappointed, Sir. Sometimes, you can just...be disappointed."
    mo "I like the stars. I wish the sky always looked the way it did when we were there."
    s "Don’t let Maya hear that. She’ll probably quiz you on them."
    mo "I’d fail a quiz miserably. I just like looking at them."
    s "... "
    s "They’re okay, I guess."
    mo "So, do you intend to venture forth on a side quest back to the dorm with me? Or is this where our party disbands and heads its separate ways?"
    s "My answer to this question hinges on how long you plan on talking about stars for."
    mo "I was already done, Sir. I was simply pointing out how I wish there were more."
    s "Then yeah. I can come back to the dorm with you."
    mo "Excellent. I’ll see to it that you obtain a rather desirable quest reward as a result."

    if bonus == True:
        s "Lewd or not lewd?"
        mo "Not lewd, of course."
        s "That doesn’t sound very desirable to me."
    else:
        s "Can you teach me how to tie my shoes? My father never taught me that either."
        mo "Of course, Sir. If that is what will make you happy."
        s "Yay!"

    scene mollycleaning23
    with dissolve

    mo "Sir, I realize this may be annoying, but would we be able to stop somewhere along the way?"
    s "Where did you have in mind?"
    mo "A nearby leyline I like to draw power from when my stocks begin to run low."
    s "Based on what I know about Mollyspeak...I’m going to assume that means a convenience store."

    scene mollycleaning24
    with dissolve

    mo "It appears you still have much to learn then, as that answer is rather far from the truth."
    mo "Come. Let us pick up yet another side quest and see if that one yields any worthy rewards as well!"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ molly_love += 1
    $ mollycafe25 = True

    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "………"
    "……"
    "…"

    jump mollycafe25p2

label mollycafe25p2:
...
```

## Code that triggers this event

File: (install folder)\game\MollyEvents.rpy

Code:
```python
...
label mollycafe:
    if molly_love >= 0 and mollycafe1 == False:
        jump mollycafe1
    if molly_love >= 5 and mollycafe1 == True and mollycafe5 == False:
        jump mollycafe5
    if molly_love >= 10 and mollycafe5 == True and mollydorm5 == True and mollycafe10 == False:
        jump mollycafe10
    if molly_love >= 15 and christmas7 == True and mollycafe15 == False:
        jump mollycafe15
    if molly_love >= 20 and mollycafe15 == True and mollydorm15 == True and mollycafe20 == False:
        jump mollycafe20
    if molly_love >= 25 and tsuneyodorm25 == True and rindorm50 == True and day > 5 and mollycafe25 == False:
        jump mollycafe25
...
```