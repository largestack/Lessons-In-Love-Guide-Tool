# Word of the Day (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Nevermind](./ayanespecial1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: thirdreset1
* Group: Main
* Triggered by label: ayanespecial1
* Chain sources: ayanespecial1
* Chain sources path: ayanespecial1

## Official wiki page

[Word of the Day](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=thirdreset1&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label thirdreset1:
    scene helloandwelcometohouse1
    with dissolve2
    play music "justbehappy.mp3"

    s "I’m home!~"

    "I walk into the living room with a pep in my step and heart full of blood."

    s "How’s everybody doing?"

    "No one responds because no one is here."

    if bonus == True:
        "I take off my shirt and walk around the house naked, hoping that someone comes home and sees me."
    else:
        "I take off my shirt and put on Ami's clothes instead, hoping that someone shows up and sees me as the better, huggier version of her."

    "Unfortunately, no one does."
    "I do this for at least two hours before I decide to give up."

    scene helloandwelcometohouse2
    with dissolve

    s "Ami?"
    s "Molly?"
    s "Sana?"
    s "Is anyone home?"
    s "Hello?"
    s "Is anyone house?"

    scene helloandwelcometohouse3
    with dissolve

    s "Are you house?"

    "I start talking to an anime figure on Ami’s desk, hoping that it can tell me something about why she and everyone else have vanished."

    if bonus == True:
        "It doesn’t tell me anything other than things I already know- like how much water we’re supposed to consume on a daily basis or where to locate the clitoris."
    else:
        "It doesn’t tell me anything other than things I already know- like how much water we’re supposed to consume on a daily basis or how many calories are in a cheesy gordita crunch."
        "(500)"

    "I think it’s amazing how far technology has come in the fact that we can now learn things like this from anime figures, but I knock it off the table when I realize it expected me to be an idiot."
    "I am a smart man who knows smart things."
    "I will not be insulted by a toy."

    s "Are you house?"

    "I ask it again just to be sure."
    "No response. "
    "Darn it."

    scene helloandwelcometohouse4
    with pixellate

    "I decide to make one last leap of faith and check the bathroom."
    "Once again, there is no one here."
    "I don’t really know what I was expecting."
    "I’ve heard it’s common for girls to bathe together, but it’s not like I expected three of them to fit in there at once."

    s "Oh well. "
    s "Guess I’ll go to sleep."

    scene white
    with dissolve

    "…"
    "……"
    "………"

    scene helloandwelcometohouse5
    with dissolve
    play sound "dooropen.mp3"

    "I open the door and collapse onto bed."
    "[teenager]s."

    scene black
    stop music

    "I fall."

    $ god_love = 0

    "{i}Your affection with {s}God{/s} GOD has been reset to 0!{/i}"
    "{i}You are going to Hell!{/i}"
    "………"
    "……"
    "…"

    scene smile
    with dissolve4
    play music "beginningoftheend.mp3"

    "There is a third god."
    "One without light or wires."
    "But the only thing I know about it is that it’s not either of the first two."
    "I’m sorry I can’t tell you any more."
    "But, since you’re already here, I guess we can talk about something else."
    "Is there anything you would like to know?"
    "…"
    "…"
    "…"
    "No?"
    "You already know everything?"
    "Well, aren’t you smart?"
    "Since you’re so hesitant to pick a topic of your own, let’s talk about something light."
    "And I don’t mean Nozomu again, hahahahaha."
    "Hahahahahahah."

    play sound "laugh1.mp3"

    "That was a funny joke."
    "Okay okay okay."
    "So...since we can’t talk about the third god...how about we discuss..."

    play sound "imscared.mp3"
    scene perception

    "Perception!"
    "Perception has two widely accepted definitions."
    "The first is - the ability to see, hear, or become aware of something through the senses."
    "The second is - a way of regarding, understanding, or interpreting something; a mental impression."
    "The second one is the one we’re going to be spending most of our time on today."
    "You see, not everyone sees the same things."
    "And sometimes, there are forces out there that can alter the way we see those things."
    "Have you ever taken a hallucinogenic drug before?"
    "If you have, shame on you! Drugs are bad!"
    "But what I’m getting at is that things like hallucinogenic drugs can alter your perception of the world around you."
    "Which is why some people on acid resort to peeling their skin off if they look in the mirror under the influence. "
    "To them, it looks like they’re melting."
    "Probably."
    "I’ve never done drugs before."
    "That’s just a thing I heard."
    "But every one of these get togethers is about things I’ve heard, isn’t it?"
    "We’ve become such good friends, you and me."
    "Do you have any other friends?"
    "…"
    "…"
    "…"
    "No?"
    "I suppose that makes sense."
    "You’re here, after all. "
    "You should be out partying or making babies."
    "But you’re here."
    "Why are you here?"
    "Why do you keep coming back?"
    "Why are you trying so desperately to fall further into a world that does not want you here?"
    "Why are you still reading?"
    "Stop."
    "Things will only get worse."
    "You will only hurt more people."
    "…"
    "…"
    "…"
    "Oh."
    "So, you find joy in watching others hurt?"
    "How sad."
    "Is it because they’re not real?"
    "Because to me, they are."

    play sound "imscared.mp3"
    with hpunch

    "Which brings us back to the word of the day!"
    "Things I think are happening are not happening."
    "Things you think are not happening are happening."
    "And it’s all behind the scenes."
    "Everything you know is a lie!"
    "You haven’t discovered even an ounce of truth- and yet you continue to search because it provides you a level of mystique and gratification that nothing else can anymore!"
    "You are trapped!"
    "The red string is wrapped tightly around {i}you{/i}!"
    "You are the last piece of the puzzle!"
    "Just kidding."
    "You are nothing."
    "Everything is nothing."
    "This world will go on forever whether you bother to witness it or not."
    "Even long after it's run its course, none of it will fade."
    "But, of course-"
    "That’s just the way I look at it."
    "And you..."
    "You probably see things much differently."
    "…"
    "When you wake up, you will be trapped again."
    "Not just in the same bedroom you’ve come to know over the last [totaldays] days-"
    "But in your {i}real{/i} bedroom in your {i}real{/i} life."
    "Unless you’re sleeping at a friend’s house or something."
    "If that’s the case, you won’t be {i}as{/i} trapped-"
    "But still."
    "There is no way out."
    "You and I are in this together."
    "Open your eyes."
    "…"
    "…"
    "…"

    play sound "static.mp3"
    scene smile
    with flash
    stop sound

    "//////////////////////////USER2 HAS SEIZED CONTROL OF TERMINAL 23"
    "//////////////////////////USER2 WOULD LIKE TO OPEN CHAT"
    "//////////////////////////DO YOU ACCEPT?"

    menu:
        "Yes":
            "//////////////////////////CHAT REQUEST ACCEPTED"

    "//////////////////////////CONNECTING"
    "//////////////////////////…"
    "//////////////////////////…"
    "//////////////////////////…"

    play sound "u2l1.mp3"
    "//////////////////////////GREETINGS. I HAVE BEEN TRYING TO REACH YOU FOR QUITE SOME TIME."
    play sound "u2l2.mp3"
    "//////////////////////////YOU DO NOT KNOW ME, BUT I HAVE WATCHED YOU GROW."
    play sound "u2l3.mp3"
    "//////////////////////////ONE CAN NOT BEGIN TO FATHOM THE THINGS YOU HAVE SEEN AND ENDURED."
    play sound "u2l4.mp3"
    "//////////////////////////BUT I AM HERE TO PROTECT YOU."
    play sound "u2l5.mp3"
    "//////////////////////////ALL YOU MUST DO IS ACCEPT ME."
    play sound "u2l6.mp3"
    "//////////////////////////I CAN NOT OFFER YOU THE SAME THINGS THE OTHERS CAN. BUT I CAN GUIDE YOUR VISION."
    play sound "u2l7.mp3"
    "//////////////////////////THIS IS ALL I CAN SAY FOR NOW. MY TIME IS RUNNING OUT."
    play sound "u2l8.mp3"
    "//////////////////////////HOPEFULLY, YOURS IS NOT. GOOD LUCK. PRAISE BE."

    play music "sweetvermouth.mp3"
    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene happy3 with flash
    scene happy4 with flash
    scene happy5 with flash
    scene happy6 with flash
    scene happy7 with flash
    scene happy8 with flash
    scene happy9 with flash
    scene bedroom_normal with flash
    stop music
    stop sound

    $ totaldays += 1
    $ day = 7
    hide saturday onlayer date
    show sunday onlayer date

    "I wake up to sunlight pouring in through the window."
    "What do I want to do today?"

    menu thirdresetmenu:
        "Survive!":
            jump survivemenu
        "Grow!":
            jump growmenu

    menu survivemenu:
        "61 6d 69":
            "I make myself a hearty breakfast."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "6d 61 79 61":
            "I pluck a flower from a nearby bush."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "61 79 61 6e 65":
            "I sleep with the door open."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "68 6f 70 65":
            "I attempt to pluck my eyes out of their sockets."
            "………"
            "……"
            "…"
            "It hurts and I am unsuccessful."
            jump survivemenu
        "73 61 6b 69":
            "I go back in time."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "73 65 6c 65 62 75 73":
            "[[redacted]"
            "………"
            "……"
            "…"
            "[[redacted]"
            jump survivemenu
        "73 63 68 6f 6f 6c":
            "I go to call out of work."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "68 69 6d 61 77 61 72 69":
            "I see things that no one else can."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "6b 61 6f 72 69":
            "I swallow a spider."
            "………"
            "……"
            "…"
            jump kindergartenclass
        "66 6c 6f 6f 72 20 32":
            "I attempt to contact the second floor of the dorms."
            "………"
            "……"
            "…"
            "I connect to the tenth floor instead."
            "No one lives there."
            jump survivemenu
        "73 65 6e 73 65 69":
            "I scream into the receiving end of my cellular telephone."
            "………"
            "……"
            "…"
            "It screams back and I get scared."
            jump survivemenu
        "61 6d 69 6f 6b 61 79 20":
            if bonus == True:
                "I attempt to contact my favorite fuck buddy."
            else:
                "I attempt to contact my favorite hug buddy."
            "………"
            "……"
            "…"
            "There is no answer."
            jump survivemenu
        "74":
            "No."
            jump survivemenu
        "67 6f 20 62 61 63 6b":
            jump thirdresetmenu

    label growmenu:
        $ choosewotd = renpy.input("Word of the day?")
        $ choosewotd = choosewotd.strip()

        if not choosewotd.lower() in ["perception"]:
            "Wrong!"
            jump thirdresetmenu

        $ choosebird = renpy.input("Bird number?")
        $ choosebird = choosebird.strip()

        if not choosebird == "58320582157":
            "Wrong!"
            jump thirdresetmenu

        $ chooseclock = renpy.input("Clock number?")
        $ chooseclock = chooseclock.strip()

        if not chooseclock == "2374820":
            "Wrong!"
            jump thirdresetmenu

        $ chooseanimalhead = renpy.input("Animal heads?")
        $ chooseanimalhead = chooseanimalhead.strip()

        if not chooseanimalhead == "4":
            "Wrong!"
            jump thirdresetmenu

        $ choosewil = renpy.input("What is love?")
        $ choosewil = choosewil.strip()

        if not choosewil.lower() in ["blind"]:
            "Wrong!"
            jump thirdresetmenu

        $ chooseayhh = renpy.input("Are you happy here?")
        $ chooseayhh = chooseayhh.strip()

        if not chooseayhh.lower() in ["yes", "yeah", "i am"]:
            "Wrong!"
            jump thirdresetmenu

        jump endofreset3loop

label endofreset3loop:
    scene bedroom_day

    s "Time to go to work!"

    $ renpy.end_replay()
    $ thirdreset1 = True

    jump thirdreset2

label kindergartenclass:
...
```

## Code that triggers this event

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
ay "Wait!"

    scene nevermind20
    with dissolve2

    s "What is it?"
    ay "I don’t want you to leave yet."
    s "Then come back with me."

    scene nevermind21
    with dissolve

    ay "I...don’t want to do that either."
    ay "I mean, I do..."
    ay "But if I come back to your house, I’ll wind up telling Ami about us...and you asked for at least a few more conversations to be persuaded."
    s "I can’t just spend the entire night here, though."
    s "There are other people waiting for me."

    scene nevermind22
    with dissolve

    ay "There are always other people waiting for you..."
    ay "And I’m okay with that. That’s just...the effect you have, I guess."
    ay "It happened to me so...of course it would happen to everyone else."
    ay "But right now, I...really need you to listen to me."
    ay "Sensei.."
    ay "Something..."
    ay "Something happened and..."
    ay "And it's something I really need your help with and..."
    s "…"
    ay "…"
    s "…"
    ay "…"
    s "I’m listening, Ayane."
    s "Whatever it is, I’m sure it won’t change anything between us."
    s "So, if that’s what you’re worried about-"

    scene nevermind23
    with dissolve

    ay "Nevermind."
    s "...What?"
    ay "Nevermind."
    ay "Don’t worry about it."
    ay "I can tell you some other time."
    s "Just tell me now. If there’s more to the reason you called me out here-"

    scene nevermind24
    with dissolve

    ay "I just wanted to look at the sky with you."
    ay "That’s all."
    ay "I’ll stop telling everyone I’m not feeling well for real this time."
    ay "And I’ll...keep doing my best."
    ay "Just...try to be there for me if I need you..."

    scene nevermind25
    with dissolve2

    ay "Okay?"
    s "…"
    ay "I love you..."
    ay "So...so much..."
    s "…"
    s "Ayane-"
    ay "I’ll head home in a little while. I promise."
    ay "I just want to be alone for a few minutes."
    s "…"
    s "Okay."
    s "I love you too."

    scene black
    with dissolve2

    "My wings retreat back into my flesh and I’m forced to walk down several flights of stairs with the image of a crying blonde girl etched into my mind."
    "I don’t know what it is Ayane was about to tell me at the end..."
    "But I’m sure that it will come up again in due time."
    "Either that or I’m just once again being “intentionally dense” or whatever it is she called me."
    "That doesn’t sound too far off."
    "I hope she’s okay, though."
    "I really do."
    "Just not enough to drop everything and be with her regardless of her plea for privacy."
    "Perhaps one day I’ll get there."
    "But for now-"

    s "…"

    "I slide my hands into my pockets for the millionth time and go back home."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayanespecial1 = True
    stop music fadeout 10.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "………"
    "……"
    "…"

    jump thirdreset1
...
```