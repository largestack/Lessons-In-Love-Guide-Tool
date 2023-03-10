# Less Like the Vulture (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Forever Yours](./ayanenew3.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Ayane: First Words](./ayanedorm15.md)
* [Ayane: Still Young](./ayanedorm20.md)

## Event properties

* Id: ayanedorm10
* Group: Ayane
* Triggered by label: ayanenew3
* Chain sources: ayanenew3
* Chain sources path: ayanenew3

## Official wiki page

[Less Like the Vulture](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanedorm10&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label ayanedorm10:
    if _in_replay:
        play music "meanttobe.mp3"

    scene ayanevirginredux1
    with dissolve2

    "We arrive at the dorm after everyone has already gone to sleep or, at the very least, locked themselves away from the chance to see something they shouldn't."
    "I don't think I've ever heard the halls this quiet before- and it's just as enchanting as it is worrying."
    "Ayane nervously scans the halls, listening in just as attentively as me and likely praying to whatever it is she believes in for an uninterrupted night of skin tearing ecstasy."

    ay "We're really doing this, aren't we?..."
    s "I wouldn't have followed you here if we weren't."

    scene ayanevirginredux2
    with dissolve

    ay "It's weird. The entire way back, I kept worrying that I was going to wake up."
    ay "This just...feels so much like a dream that I'm scared something is going to come along and snap me out of it before we get to the good part."
    s "Well, if you haven't already confirmed that you're awake and that this is happening, I'm sure that what you're about to endure will be more than enough to do that."

    scene ayanevirginredux3
    with dissolve

    ay "You really think it's going to hurt that much?"
    s "I have no idea what it will feel like for you but, based on the size disparity alone, I can't imagine it's going to be pleasant."
    ay "Just for the first time, though...right? How long do you think it will take for me to get used to it?"
    s "I have no idea, Ayane. I've never been a female before."
    s "Are you trying to psyche yourself out of this right now or something? Because it seems like you're having second thoughts."

    scene ayanevirginredux4
    with dissolve

    ay "Not at all. I've just never felt my heart beat this fast before."
    ay "It's like...everything is being amplified. How warm my face is...the silence of the dorm..."
    ay "I don't think I've ever felt this...{i}alive{/i} before..."
    ay "Wouldn't you say the same, Sensei?"
    s "..."
    ay "..."

    scene black
    with dissolve2

    s "Yeah..."

    if bonus == True:
        jump ayanefirstx
    else:
        "It turns out that Ayane just really wanted a hug for some reason."
        "I provide one for her and go on my merry way."

        $ renpy.end_replay()
        $ ayane_love += 1
        $ ayane_virgin = False
        $ ayanedorm10 = True

        "{i}Congratulations! You have hugged Ayane!{/i}"
        "{i}This may make an impact on the story going forward...{/i}"
        "{i}Why, you ask? Because hugs are important and meaningful.{/i}"
        "{i}Her affection has also increased to [ayane_love]!{/i}"

        stop music fadeout 3.0

        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label sanadorm15:
...
```

## Code that triggers this event

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
ay "Hey! I’ll have you know that I consistently rank among the top ten funniest girls in our class based on the polls I force Sana to run online."
    s "I’m honestly amazed that she hasn’t asked for a new roommate yet."
    ay "And {i}I’m{/i} honestly amazed by {i}how hot you are.{/i}"
    s "Ayane, please."
    ay "Sorry. I’m done now."
    ay "For real, though. Doesn’t it feel much better up here?"
    ay "I’ve never actually been on the roof of the school before- just heard about it from Ami. But my bedroom at home did have a window I could climb out of and sit on the roof."
    ay "I remember doing that a lot after my mom left."
    ay "And I guess it became some sort of coping mechanism for me or something like that since I’m still compelled to climb as high as I can whenever I’m feeling down."
    ay "Even your worries seem smaller when you’re this far off the ground."
    ay "And I’m not saying that the reason I brought you up here is to try and force the way I handle things on you-"
    ay "I just thought it might be a little easier to breathe in a place with more air."
    s "..."
    ay "..."
    s "That line would have been a lot better if higher altitudes didn’t make it {i}harder{/i} to breathe. "
    ay "Ooh! Maybe we should just have class on the roof from now on if being up here is going to help you remember cool facts like that?"
    s "Thank you, Ayane."
    s "Not for your sarcastic teaching comment, but for looking out for me even when you probably shouldn’t be."
    ay "..."
    s "..."
    ay "You’re welcome, Sensei."
    ay "You were there for me, so I’ll be here for you."
    ay "I didn’t expect you to actually thank me, though. It’s not really like you to lean into serious moments like this."
    ay "But I guess we all act a little differently when we’re on top of the world."
    ay "Oh! Here’s a fun idea. How about we take turns admitting some of our deepest, darkest secrets to one another? That’ll help kill some time before we head back, won’t it?"
    s "I’m good. I don’t really have anything I’m actively hiding from you anyway."
    ay "What? Really? Well, that’s no fun."
    ay "I guess we’ll just have to have sex instead, then."
    s "..."
    ay "..."

    "Wait, what?"

    s "Was that for real? Because it’s hard to tell with you sometimes."
    ay "Yeah. It was."
    ay "I’m a little nervous, but...I think I’m ready."
    ay "Assuming you’re still okay with it, of course. Because I absolutely wouldn’t blame you if you felt weird about this and, like...wanted to wait until I graduate or something."
    s "What would waiting that long change? "
    s "You’ll still be my niece’s best friend and I’ll still be a man who was supposed to be looking after you."
    s "This is wrong no matter what angle you look at it from."
    ay "I know."
    ay "But this is a mistake I’ve wanted to make for a very long time."
    ay "And I am also very horny right now."
    s "Sounds like a pretty normal day for you."
    ay "I am a girl in love in the throes of puberty and I will not allow you to shame me for my overactive imagination and desire to touch you."
    s "I’m not shaming you for anything. Nor am I trying to talk you out of it since I have no intention of refusing."
    ay "Then-"
    s "I just need you to promise that no one will ever find out about this."
    ay "..."
    s "Because, if they do-"
    ay "Sensei, I’m not an idiot. I may be blindly in love, but even a blind woman would be able to prevent herself from diving head first into a meat grinder."
    s "Please refrain from using the word “meatgrinder” while I am in the process of forming an erection."
    ay "I am about to sleep with my friend’s uncle...who is also my teacher...who is also nearly double my age."
    ay "I’m obviously going to keep that a secret."
    ay "When I say I love you, I don’t mean immature, schoolgirl love. I mean {i}real{/i} love. The kind that is protective and loyal and understanding."
    ay "I will do anything you ask me to, and {i}not{/i} because I’m worried that you’ll leave if I don’t-"
    ay "But because I want you to be happy."
    ay "I want us to be happy together."
    ay "But right now-"
    ay "More than anything-"
    ay "I want you to take me home and make love to me before I have an orgasm from just thinking about it."
    s "..."
    ay "..."
    s "Do we really need to go all the way back to the dorm?"
    ay "Sensei, when I said that I want my first time to be special, I didn’t mean “doggystyle on the roof” special. "
    s "I mean...there are other positions."
    ay "But my bed is so big and soft...and Sana is sleeping at her mom’s tonight."
    ay "And also, if we fall off the roof, there’s a good chance you could break your penis and never be able to have sex with me again."
    s "Dorm room it is."
    ay "Heheh...thank you."
    ay "Not just for agreeing to take me home...but for everything you’ve ever done since the moment we’ve met."
    ay "Tonight will be the start of something beautiful, Sensei."
    ay "I am forever yours...any way you want me."
    ay "Any way you-"
    s "Stop talking and start walking or I am going to wind up deflowering you on the stairs."
    ay "Deal. "

    scene black
    with dissolve2

    "We make our way off of the roof and back into the school."
    "Ayane excitedly and hurriedly pulls me through the halls by the wrist, occasionally turning around and giggling."
    "It’s a childish giggle that fills me with a sense of lustful dread in both knowing and accepting that I am about to cross a boundary that I {i}know{/i} should not be crossed-"
    "And yet none of the horrible things that I have acknowledged both verbally and mentally even partially dissuade me."
    "This is who I am."
    "I am not built for love- but if I can help someone like Ayane {i}feel{/i} loved while gaining something for myself in return..."
    "I will help her time and time again."
    "And I will take her body in my hands, the same way she has dreamt of time and time again-"
    "And cocoon myself in the idea that I am only as broken as she thinks I am."

    $ renpy.end_replay()
    $ ayane_love +=1
    $ ayanenew3 = True

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    jump ayanedorm10
...
```