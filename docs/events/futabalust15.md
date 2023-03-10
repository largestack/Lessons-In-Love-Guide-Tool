# C'est La Vie (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Why Now?](./dormwar9.md)

## Event preconditions

* Futaba lust greater than or equal to 15

* Event [I See Everything](./nodokadorm5.md) (Nodoka) is completed)



## Next events

None

## Event properties

* Id: futabalust15
* Group: Futaba
* Triggered by label: dormwar9
* Chain sources: dormwar9
* Chain sources path: dormwar9

## Official wiki page

[C'est La Vie](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabalust15&go=Go) for more details.

## Event code

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label futabalust15:
    scene futabanodokahotel1
    with dissolve

    no "Huh. It’s just a normal hotel room. There are no...ropes or shackles or anything."

    if bonus == True:
        s "Yeah, the bondage room was apparently sold out for the night, so I got stuck with this."
        no "Damn. Hate when that happens."
    else:
        s "Do not accuse me of abducting and enslaving people. I am so nice."
        no "Sorry."

    scene futabanodokahotel2
    with dissolve
    play music "acoustic.mp3" fadein 4.0

    no "So, now what?"

    if bonus == True:
        no "You’re alone with two beautiful [young]women. And one of them is allegedly locked into a rather physical relationship with you, Mr. Humbert."
        s "I really can’t tell if you actually believe this is true or not."
    else:
        no "Want to talk about biochemistry or something?"
        s "You are so hard to follow."

    no "Are you saying I’m hard to follow?"

    if bonus == True:
        s "Yes. Very hard, actually."
        no "As hard as Futaba makes you when you sneak into her dorm at night?"
    else:
        s "Pay attention to me for once."

    scene futabanodokahotel3
    with dissolve

    f "I knew telling you was a bad idea..."

    if bonus == True:
        jump futabanodokax
    else:
        no "I would like to propose a contest idea."
        s "You have the floor, Miss Nagasawa."
        no "Let's see who can jump on the bed for the longest without getting tired or hitting their head."
        s "Great idea. I'm sure that's exactly what the two of you came here to do."
        f "You know us so well, Sensei."

        scene black
        with dissolve

        "All three of us take our shoes before getting onto the bed because we wouldn't be able to live with ourselves if we got it dirty."
        "The jumping begins, but I am significantly taller than the average Japanese male, so I quickly wind up hitting my head on the ceiling."
        "Nodoka and Futaba continue jumping for the next hour and it quickly becomes apparent that neither of them will ever stop, so I am forced to make a decision."
        "That decision is to dropkick Nodoka in the ankles, causing her to fall and lose."

        no "Ouch."
        s "This is revenge for being so smart."
        no "If only there was a member of the American Red Cross here."

        "Futaba and I look at each other and giggle (Because that's me) and then we let Nodoka relocate all of the bones in her leg by herself."
        "Futaba wins the thing."

        $ renpy.end_replay()
        $ futaba_lust += 1
        $ dorm1warpoints += 1
        $ futabalust15 = True
        stop music fadeout 5.0

        "{i}Futaba’s lust has increased to [futaba_lust]!{/i}"
        "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
        "………"
        "……"
        "…"

        $ totaldays += 1
        $ day += 1
        if day == 7:
            hide saturday onlayer date
            show sunday onlayer date
        else:
            "ERROR ADVANCING TO SUNDAY"

        jump dormwar10

label library40:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
f "Nodoka! Why?! "

    if bonus == False:
        s "Y-Yeah, Nodoka! It's not like the two of us would...h-h-hug or anything..."

    no "Futaba, my sweet girl. My sweet, sweet girl. My sweet, beautiful girl with gigantic breasts."

    if bonus == True:
        no "Do you not understand why I struggle to believe the news of your apparent...experiments with our dear teacher?"
        no "It was just the other day that we were frolicking through a field of flowers, holding hands and-"
        f "Even if it wasn’t true, why would you just bring it up like that?!"
        no "Because it’s funny {i}and{/i} sexual and those are two of my most important character traits."
        no "So either it’s not true and we all have a laugh about it, or it {i}is{/i} true and I get to watch my teacher copulate with my best friend. Win win."
        s "…"
    else:
        no "You do not need to hide your hugs from me."

    s "Futaba...did you tell Nodoka about us?"

    scene likemotherlikedaughter17
    with dissolve

    f "I...may have said...some things. "
    f "But I had no idea she was going to immediately blurt them out to you."
    no "I have only known about this for ten whole minutes, but they have been ten of the most exciting minutes of my life if any of it is true."
    no "I do acknowledge that this may still be some elaborate ploy to toy with me, but I am the official dorm wars knowledge champion until further notice, so I’m kind of a big deal."
    no "Not really one to be so easily {i}tricked{/i}, I mean."
    s "You’re not going to say anything about this to anyone else, are you?"

    scene likemotherlikedaughter18
    with dissolve

    no "Sensei, I’m going to let you in on a little secret."
    no "I kind of love the girl sitting next to me right now. And I would never do anything that I believe would even come close to hurting her."
    no "And, should I happen to hurt her accidentally, I would carve out my insides with a wakizashi."
    no "So, no. I’m not going to tell anyone else."

    scene likemotherlikedaughter19
    with dissolve

    no "Besides, this isn’t something I’d believe without seeing with my own eyes. "

    if bonus == True:
        no "Futaba is a delicate flower who will not do anything sexual until she is married, and I am sure this is all just a big, poorly executed prank."
    else:
        no "Futaba always tries to run away when {i}I{/i} hug her and I want to see if it's just a reflex of hers or more of a personal issue with me directly."

    no "Also, the girls in my room were so loud that it made reading near impossible. And if your room is any quieter, I’d like to utilize it for some good ole word absorption."
    f "…"
    s "…"
    s "And your thoughts on this, Futaba?"
    f "I think that she should stop calling reading “word absorption.”"
    s "You know what I’m talking about."

    scene likemotherlikedaughter20
    with dissolve

    f "I...am a little curious about your room."
    f "And going there doesn’t automatically mean that...you know."

    if bonus == True:
        s "I have no idea what you mean by that, Futaba. You and I have never done anything sexual before. Why would you lie about this to Nodoka?"
    else:
        s "NO, FUTABA. NO HUGS!"

    scene likemotherlikedaughter21
    with dissolve

    f "H-Hey! Now that she already knows, there’s really no point in-"

    if bonus == True:
        s "In fact, while I’m at it, I’ve never done anything sexual with anyone ever."
        s "I’m a total virgin who’s never even seen boobs before."
        s "Now...if only there were girls around who’d be willing to show me them..."
        no "Oh dear. Perhaps we {i}could{/i} find a janitor’s closet somewhere in the hotel..."
        f "No! We’re going to Sensei’s room now before anyone else hears us talking about this!"
    else:
        s "NOOOOOOOOOOO!!!!!!!"

    scene black
    with dissolve2

    "Futaba quickly stands up and grabs Nodoka by the wrist, dragging her up as well."
    "She must already know my room number as she immediately begins to lead the way there."
    "Nodoka looks back every few seconds to wink at me and...I really can’t tell if it’s because of the janitor’s closet thing, if she believes what I’ve done with Futaba, or if she {i}doesn’t{/i} believe anything at all."
    "It could really mean anything with that girl."

    play sound "dooropen.mp3"

    "Eventually, we make it to my door and I grab the key out of my pocket, insanely curious about whatever is about to happen."

    if futaba_lust >= 15 and nodokadorm5 == True:
        $ renpy.end_replay()
        $ dormwar9 = True
        stop music fadeout 5.0
        "………"
        "……"
        "…"
        jump futabalust15
...
```