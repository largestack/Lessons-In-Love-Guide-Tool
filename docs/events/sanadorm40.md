# The Inside of a Triangle (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Closer to Me](./bar40.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Sara: She's Always a Woman](./sarabar20.md)
* [Main: Operation: Firestarter](./day318.md)

## Event properties

* Id: sanadorm40
* Group: Sana
* Triggered by label: bar40
* Chain sources: bar40
* Chain sources path: bar40

## Official wiki page

[The Inside of a Triangle](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanadorm40&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label sanadorm40:
    scene sanawalkedhome1
    with dissolve2

    sa "Um...thanks again for...walking all the way here with me, Sensei..."
    sa "I feel a little bad that...you didn’t even get to have a drink first..."
    s "You can just make it up to me by giving me free beer for the next month. That seems fair to me."
    sa "The price for...hanging out with you is pretty high...huh?"
    s "Supply and demand, Sana. Supply and demand."

    "I’m surprised the two of us made it all the way up here without her giving the signal that it was time for me to leave."
    "Here I was, ready to tuck my hands into my pockets and rush over to the closest convenience store for a hot beverage, but-"
    "Somehow or another, I’m outside of Sana’s dorm."

    sa "Well there...sure is a lot of demand for you, so...I guess I understand..."
    sa "Can I...umm...ask you something, though?"
    s "Is it another pricing question? Because I might need to have you call my secretary if it is."
    sa "It’s not a...pricing question..."
    sa "I just wanted to ask if you could...keep all of that stuff about my mom a secret..."

    scene sanawalkedhome2
    with dissolve

    s "Of course. It’s not like I’d come out and just tell someone, “Hey. Sana’s mom is in denial about the death of her son. Pass it on.”"
    sa "I’m more worried about you...saying something about it to her..."
    s "And then what? Watch her break down in front of me and not know how to handle it?"
    s "I’m by no means a good person, but it’s not like I’m {i}evil{/i}, Sana."

    scene sanawalkedhome3
    with dissolve

    sa "Then it...shouldn’t be an issue for you to promise me, right?"
    sa "I’ve compared you to a...dad a few times tonight, but...you aren’t family..."
    sa "So you shouldn’t really get involved..."
    s "Are you saying you want to live in denial as well, then?"

    scene sanawalkedhome4
    with dissolve

    sa "I’m not denying anything..."
    sa "My big brother died and...part of me died with him."
    sa "But the part that’s left needs to stay intact so...my mom can stay sane."
    s "Crazy to think that just the other day, your big breakthrough moment was confessing that you suddenly wanted to learn karate."

    scene sanawalkedhome5
    with dissolve

    sa "H-Hey! Th-that was...probably even harder to come out and say than...all of this..."
    sa "It would be weird if...everyone I know kept getting closer to you and I stayed..."
    s "On the inside of a triangle?"

    scene sanawalkedhome6
    with dissolve

    sa "That’s...actually a really good way of wording it..."
    s "Thanks. I thought it up on the way over."

    scene sanawalkedhome7
    with dissolve

    sa "Hah...all I kept thinking of was...how weird it felt walking around with you and...how tall you are..."

    scene sanawalkedhome1
    with dissolve

    sa "B-But...yes..."
    sa "I’m on the...inside of a triangle..."
    sa "And I...told myself that I’ll start being more honest with you..."
    s "And what better place to do that than karate lessons?"

    scene sanawalkedhome8
    with dissolve

    sa "Stop bringing up karate lessons! "
    sa "And...and stop bringing up spaghetti!"
    s "I didn’t even mention spaghetti."
    sa "You were going to! You have the...spaghetti look in your eyes!"
    s "…"
    sa "…"

    scene sanawalkedhome9
    with dissolve

    sa "Pfft..."
    sa "What am I...even saying right now?"

    "It’s peculiar what jealousy can do to a person."
    "Between the Christmas party and now...and even before that, Sana and I never really had a dramatic shift in our dynamic."
    "She’s always just...been there being cute and...doing cute things, but-"
    "We’re actually getting somewhere now."

    if bonus == True:
        "Maybe I {i}don’t{/i} just want to protect her? (And obviously have sex with her because...come on. I'm only human.)"
        "But maybe I want to learn about her?"
        "Maybe I want to watch her...try and fail?"
        "To learn from her mistakes-"
        "Maybe even succeed sometimes-"
        "And to keep nervously smiling at me like I expect her to any moment now."
    else:
        "Nowhere romantic, though. Just closer to the platonic relationship I have always wanted with her."

    scene sanawalkedhome10
    with dissolve

    sa "Are you...um..."
    sa "Are you...cold?"

    "Right on cue."

    s "Of course. It’s freezing out."
    s "Why do you ask?"
    sa "Well, you...walked the whole way here, so..."
    sa "If you want to...come warm up inside my room for a little while..."
    sa "That’s...that’s okay..."

    if bonus == True:
        "Holy crap, am I actually being invited in?"
        "It’s way later than I’m usually here."
        "Is she really okay with this?"
        "What has happened to my precious, reserved little Sana?"

        s "You do realize how this sounds, right?"
        sa "I...have no idea what you’re talking about..."
        sa "But, um...Ayane isn’t home tonight and...it’s easier to talk about stuff when we’re...in a private room..."
        s "Do you {i}really{/i} not realize how this sounds?"
        sa "I told you...I...I have no idea what you’re talking about..."
        sa "I just...don’t really want you to go home yet...or something..."
        s "When you say it like that, how could I possibly refuse?"

        scene sanawalkedhome11
        with dissolve

        sa "R...Really?"
        sa "I mean...I always knew you were going to say yes because...you’re a very...sketchy person..."
        sa "But it’s...still nice...actually hearing it."
        s "Okay, you’re still new to this, so I won’t be too harsh. But you don’t normally insult someone immediately after inviting them inside."

        scene sanawalkedhome9
        with dissolve

        sa "Heheh...it wasn’t meant as an insult..."
        sa "I...like how unpredictable you are..."
        sa "It makes me...do things outside of my comfort zone..."
        sa "It’s...nice having someone like that again..."
    else:
        s "Of course it is okay. You are a wonderful host and it is very polite of you to invite me in as a friend."
        sa "Thank you for understanding and appreciating the platonic relationship we have even though I am a health inspector."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "Sana opens the door and steps aside, lightly bowing to me and allowing me to walk in first."
    "Technically, I’m probably the one who should be doing that for her-"
    "But since she offered, I’m obviously going to walk in."
    "Otherwise we’d just have two people standing around in the hallway and looking even more suspicious than we already were with our one-foot height gap."

    ay "Oh, Sana! You’re home!"
    ay "I texted you and you didn’t respond, but I decided to-"

    scene sanawalkedhome12
    with dissolve

    ay "Stay home tonight..."

    play music "asobeatsexdark.mp3"

    sa "O-Oh! I’m...sorry..."
    sa "My...umm...my phone died on the way home..."
    ay "What are you doing here so late?"
    ay "And why are you two together?"
    s "I walked Sana home from work. "
    ay "You walked...all the way from the bar with her?"
    s "I did."
    ay "You didn't just run into her on your way somewhere else?"
    s "I...did not."

    "Sana nervously closes the door and takes a step toward Ayane with great hesitation."

    scene sanawalkedhome13
    with dissolve

    sa "Um...Ayane...it was me who...asked him to t-take me home..."
    ay "And you invited him into the room as well?"
    sa "Y-Yeah..."
    ay "Even though it’s getting close to midnight and you knew I wasn’t going to be home?"
    sa "Well...it was cold out...so..."
    sa "I thought he could...warm up..."

    scene sanawalkedhome14
    with dissolve

    ay "Do you need to warm up, Sensei?"

    if ayanesleepover == True and bonus == True:
        ay "You’ve been in my bed several times before, so you know how warm it can get when you hide under the covers."
        s "Ayane..."
    elif ayanesleepover == False and bonus == True:
        ay "You can stay the night in my bed if you want."
        ay "I know you’ve rejected that same offer before, but it’s not like I’m crying this time or anything."
        sa "A...Ayane..."
    else:
        s "No. Stay away from me. If you touch me, I will scream."

    "Okay, well, everyone here is clearly uncomfortable now."
    "Obviously, Ayane would be a bit confused seeing me walk into the room with Sana at this hour, especially since she was supposed to be away tonight."
    "Any rational person would come to the same conclusion."
    "And hell, Ayane isn’t even always rational and she’s seemed to reach that exact end-point."

    scene sanawalkedhome15
    with dissolve

    ay "How was work?"
    ay "Did you have a good time?"
    ay "Seems like you closed early."
    sa "Um...y...yeah...we did..."
    sa "Otherwise, Sensei wouldn’t have..."
    ay "…"
    sa "…"
    ay "Wouldn’t have what?"

    scene sanawalkedhome16
    with dissolve

    s "She probably wants to say I wouldn’t have bothered walking home with her if it was any later."
    ay "Is that true, though?"
    s "No. I still would have walked with her."
    ay "Of course you would."
    ay "Because you’re kind and caring and compassionate and lovely and wonderful."
    ay "And so is Sana."
    sa "I...I know what it looks like...but that’s really...not what’s happening..."
    ay "I’ll probably believe that in the morning but, right now, I’m just trying to get some thoughts sorted out."

    scene sanawalkedhome17
    with dissolve

    ay "It’s...definitely a little bit of a shock, though...hahahaha..."
    ay "I can’t even remember what I was about to say before you walked in."
    ay "I’m not normally this forgetful."
    ay "Sensei, pinch me and turn me back to normal."

    scene sanawalkedhome18
    with dissolve

    sa "A-Ayane!"
    ay "Hm? What’s up?"
    sa "Can we maybe...talk out in the hallway for a minute?..."
    ay "The hallway? Why not just talk in here?"
    sa "Because it’s...something...I want to tell you and not...S...Sensei..."

    scene sanawalkedhome19
    with dissolve

    ay "But...what if it’s something I don’t want to hear?"
    sa "It’s something...I {i}want{/i} you to hear..."
    sa "And...that should be enough...right?"
    sa "I...listen to things you tell me all the time and...I don’t ever...say anything bad about them..."
    ay "Yeah...I know...I just-"

    scene sanawalkedhome20
    with dissolve

    sa "Sensei...I’m sorry but...maybe it’s best if you...go home now..."
    s "Yeah. I was just thinking about how warm I’ve suddenly become anyway."
    sa "R...Right..."
    sa "And...um...I’m sorry that...you weren’t able to stay longer..."
    sa "I’m sure your legs are-"
    s "My legs are fine. You’re underestimating just how much I walk around this god forsaken town."

    scene sanawalkedhome21
    with dissolve

    s "Goodnight, you two. Sorry for showing up unannounced, Ayane."
    ay "What? Why are you apologizing to me? There’s no need to-"
    sa "Goodnight, Sensei...I’m...I’m sorry again..."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    "I exit the room and quickly make my way out of the dorm."
    "It feels a lot colder than it did thirty minutes ago, but I guess things like that happen once your body temperature readjusts to the way things are indoors."
    "As I pass under streetlights, looking up at a suddenly cloudy sky, I think to myself about shapes."
    "About triangles, in particular."
    "And about how difficult it would be to escape if you were to ever find yourself trapped inside of one."

    $ sana_love += 1

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"
    "{i}Meanwhile...{/i}"

    scene sanawalkedhome22
    with dissolve2

    sa "Do you...want anything to drink?"
    ay "Why do we have to do this in the hallway?"
    sa "When my mom is feeling upset...I always offer to go for a walk with her..."
    sa "And you’re feeling upset, so...I’m just...doing the only thing I know how to do..."

    scene sanawalkedhome23
    with dissolve

    sa "You know that I’m...not good with people...so I’m sorry if this doesn’t...work with you..."
    ay "I’m not just “people” though, Sana. I’m Ayane."
    ay "We live in the same room and even sleep in the same bed sometimes."
    ay "You know everything about me, so..."
    ay "So..."

    scene sanawalkedhome24
    with dissolve

    ay "Why didn’t I know {i}this{/i} about you?..."
    sa "Wh...what? I don’t understand..."
    ay "When did you...start feeling this way about Sensei?"

    scene sanawalkedhome25
    with dissolve

    sa "Wha-"
    sa "What way?!"
    sa "All...all we did was walk home together!"
    ay "That may be all you did but...was that all you wanted?"
    ay "I just...want to know how long you’ve felt like this for..."
    sa "But...I don’t feel like anything!"
    sa "I’m...I’m out here talking to you because I wanted to clear up any misunderstandings you had!"
    ay "What would you have done if Sensei tried to kiss you tonight?"
    sa "Run away and die!"

    scene sanawalkedhome26
    with dissolve

    ay "Sana..."
    ay "Your brain and your heart are disconnected..."
    sa "I..."
    sa "No! That’s not what’s happening!"
    ay "It is. "
    ay "It’s the same thing that happened to me."
    ay "I just wish I would have found this out a lot less...suddenly."
    sa "You’re...you’re wrong!"
    sa "I don’t even understand what you’re saying but I...I know it’s wrong!"

    play sound "dooropen.mp3"
    scene sanawalkedhome27
    with dissolve

    m "Is everything okay out here?"
    m "It’s not every day that you hear Sana yell like that. "
    m "What’s going on?"
    ay "It’s nothing, Maya..."
    m "Sure as hell doesn’t sound like nothing."
    sa "..."
    ay "..."
    m "Okay. Well, it’s clear that this is something I shouldn’t be involved with, so I’m gonna go back to bed."
    ay "Goodnight, Maya."
    sa "Good...Goodnight..."
    m "…"
    m "Yeah."
    m "Goodnight."

    play sound "dooropen.mp3"
    scene sanawalkedhome28
    with dissolve

    ay "…"
    sa "…"
    ay "Sana..."
    ay "I’ll...stop pestering you about it, but..."
    ay "I understand that it’s not possible to control how you feel about someone..."
    sa "I don’t feel that way about Sensei..."
    sa "I...can’t feel that way about him..."
    ay "Why?"
    ay "Because you’re afraid of hurting me?"
    sa "My mom likes him too, you know..."

    scene sanawalkedhome29
    with dissolve

    if bonus == True:
        ay "Oh, stop. We both know Sensei isn’t into girls your mom’s age."
        sa "We..."
        sa "We do?..."
        ay "That’s what I’m banking on, at least."
        ay "But if you {i}do{/i} feel that way about him-"
        sa "I don’t."
        ay "Right. But if you {i}do{/i}-"
        ay "Don’t worry about something like hurting me."
        ay "I’ve been hurt plenty of times."
    else:
        ay "Sana...your mother died five years ago."
        sa "...What?"
        ay "This is all a simulation."
        sa ".........What?"
        ay "You're not even a real health inspector."
        sa "Oh god."

    scene sanawalkedhome30
    with dissolve

    ay "Also, I’ve made it my life’s mission to never give up on him. "
    ay "So even if you somehow manage to defeat me, I’ll take him back by any means necessary."

    if bonus == True:
        ay "Unless you’re willing to share."
        ay "Cause you know how cute I think you are and I probably wouldn't mind as long as it was a three-"
    else:
        ay "Also, do you want to try making a bone necklace with-"

    scene sanawalkedhome31
    with dissolve

    sa "AYANE! STOP!!!!"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ sanadorm40 = True
    stop music fadeout 8.0

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ayanedorm35:
...
```

## Code that triggers this event

File: (install folder)\game\SanaEvents.rpy

Code:
```python
...
sa "Huh? What do you mean?"
    s "I mean that bottling things like that up can literally kill people."
    sa "But...so can grief."
    sa "No matter what we do, we’re going to...keep hurting."
    sa "A third of our family was taken away from us..."
    sa "All we can do is...help each other deal with that any way we can..."
    s "…"

    if sarasex == True:
        s "Didn’t you tell me when you were drunk that you wished Sara {i}would{/i} talk about it, though?"

        scene barwalkhome19
        with dissolve

        sa "..."
        sa "Things you do or say when...you’re drunk...don’t count..."
        s "That’s an incredibly dangerous thing for someone working in a bar to be saying."
        sa "Yes, but...it’s something I need to think or...everything will get even worse than it already is..."
        s "…"
        sa "…"

    scene barwalkhome20
    with dissolve

    sa "Oh no! I...I made this a really awkward walk all of a sudden!"
    sa "Wh-what were we talking about at first?"
    s "How I’m the closest you’ve ever had to a father figure."
    sa "Th-that’s awkward, too! Wh-wh-what was our last {i}normal{/i} conversation about? Let’s go back to that!"
    s "I think that was just about how tall I am."
    sa "So tall! The tallest!"
    s "Sana, calm down. It’s okay that things got awkward for a few minutes."
    s "If you’re embarrassed about it, just look at it as another exercise in public speaking."
    s "You were able to talk at length about something that makes you uncomfortable, and now I know more about you as a result."

    scene barwalkhome21
    with dissolve

    sa "Uh...uh-huh..."
    sa "But now it will probably be a little bit harder for me to...spend time with you when you could just...go hang out with Ayane instead and...avoid my awkwardness..."
    sa "At least when...she compares you to a dad, she...knows what she’s talking about..."
    s "Good point."

    if bonus == True:
        s "Maybe I should just adopt the two of you and get it over with?"
        sa "I think you’d...have to marry my mom to be able to adopt me..."
        s "I feel like there are several people who would be very unhappy with me if that were to happen."
        sa "And...one of them is right next to you..."
        sa "But it’s okay..."
        sa "Like I said...I don’t view you that way..."

    sa "I’m...perfectly fine if things just...stay like this..."
    sa "That would be...the easiest thing for everyone..."
    s "…"
    sa "…"
    s "You’re really fine with things never changing?"

    scene barwalkhome22
    with dissolve

    sa "…"
    sa "Actually..."
    sa "When I say this would be the easiest thing for everyone...I really just mean me..."
    sa "If you get any closer to Ayane...you’ll get further away from me."
    sa "If you get any closer to my mom...you’ll get further away from me."
    sa "And if..."
    sa "You get any closer to me..."
    s "…"
    sa "…"

    "Sana never finishes that thought but, through context clues and my unparalleled wisdom in the world of [teenage]girls, I’m able to ascertain what she means."
    "She’s afraid of her feelings for me growing."
    "{s}Growing like a tree.{/s}"
    "She’s afraid of what she’ll have to do and what she’ll have to go through if she, too, falls victim to my suspicious gravitational pull on all of these girls."
    "Take Ayane, Sara, and me and arrange us so we form a triangle."
    "Right now, Sana is in the middle of the triangle- and she wants to get out."
    "The only way to do that is by breaking one of the lines."
    "Breaking a line means the triangle would crumble."
    "So, just like her mother-"
    "She doesn’t try to change anything."
    "She stays exactly where she is and waits for everything else to resolve on its own."
    "It’s a horrible way to live."
    "A horrible, impassive way to live-"
    "That I, too, am guilty of in more ways than one."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar40 = True
    stop music fadeout 100.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"
    "{i}A short while later...{/i}"

    jump sanadorm40
...
```