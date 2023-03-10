# Prisoner (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Reverse Cowgirl](./beachvacation12.md)

## Event preconditions

* Ayane lust greater than or equal to 10



## Next events

* [Ayane: What a Wonderful World](./ayanelust15.md)

## Event properties

* Id: ayanelust10
* Group: Ayane
* Triggered by label: beachvacation12
* Chain sources: beachvacation12
* Chain sources path: beachvacation12

## Official wiki page

[Prisoner](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanelust10&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label ayanelust10:
    ay "Well, well, well...If it isn’t good ole’ [ayanemaster]..."

    scene whatwelove1
    with dissolve
    play music "acoustic.mp3"

    s "If it isn’t Ayane Amamiya, heiress to the Amamiya fortune."

    scene whatwelove2
    with dissolve

    ay "In the flesh."
    s "What are you up to?"
    ay "Hmmm..."
    ay "Will you think I’m creepy if I say I’ve been waiting here for you to walk by?"
    s "A little, yeah. But I already think you’re kind of creepy so just say whatever."
    ay "I see. Then I just so happen to be passing by."
    s "You’re not passing anything. You’re just standing there leaning against a wall."

    scene whatwelove3
    with dissolve

    ay "Ugh...Would it kill you to just play along for once?"
    ay "I’ve barely got to spend any time with you since we got here and...I miss you and stuff."
    s "I can tell by the fact that you’ve been literally waiting for me to walk past you."

    scene whatwelove2
    with dissolve

    ay "On the bright side, I haven’t been waiting very long!"
    ay "It’s only been maybe...twenty minutes or so? I figured you’d need to pass by eventually."
    s "That’s still a decently long time to be doing literally nothing for."

    scene whatwelove4
    with dissolve

    ay "But it’s all worth it because I got to see you!"
    ay "So, mission accomplished! Ayane wins!"

    "Ayane lets out what sounds like a mixture between a sigh of relief and a childish laugh."
    "Despite how creepy it definitely is to stand there waiting for twenty minutes, I really don’t mind."
    "Things like this are commonplace for a girl like her."
    "A girl who wants to be noticed."
    "Who wants to be loved."

    if bonus == True:
        "And-"
        "One that is inexplicably horny at all times of the day."
        "What more could you ask for?"

    scene whatwelove5
    with dissolve

    ay "Is it okay if the two of us hang out for a little while? I freed up my afternoon so I’d be able to spend as much time with you as possible."
    s "Well when you put it like that, there’s not really any way I can refuse."
    ay "Then I’m glad I put it like that!"

    scene whatwelove6
    with dissolve

    ay "Let it be true! For the next two or so hours, I will be your prisoner!"
    s "Wouldn't I be {i}your{/i} prisoner in this case? You’re the one who ambushed me."
    ay "I ambushed no one. I just happened to be standing here while you passed by."
    s "But you said-"

    scene whatwelove7
    with dissolve

    ay "Shh...No words. I’ve accepted my fate and am ready to take any punishment you are willing to give me."

    if bonus == True:
        jump prisonerx
    else:
        scene black with dissolve

        "I decide to punish Ayane by forcing her to build one hundred sand castles."
        "However, just as she finishes the ninety-nineth, Kirin shows up and kicks all of them down."
        "It causes a rift in their friendship and the two of them immediately sever all ties."
        "I'm pretty sure Kirin just wanted a hug, though."
        "Either way, there are easier ways to hug people. And I do not endorse destroying someone's hard work as a means of bringing yourself closer to your goal."

        $ renpy.end_replay()
        $ ayanelust10 = True
        $ ayane_lust += 1
        stop music fadeout 5.0

        "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
        "………"
        "……"
        "…"

        jump beachvacation13

label ayanelust10skip:
    "I fall asleep, but do not dream."
    "Everything is black."
    "And nothing falls but me."

    "………"
    "……"
    "…"

    jump beachvacation13

label beachvacation13:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
c "Everybody I hang out with is more into like, fashion and stuff like that. But Rin is super creative and I totally respect that kind of person."
    c "Did you know she plays guitar?"
    s "I did."

    scene sunbathing28
    with dissolve

    c "So cool, right?!"
    c "Do you think she’d teach me?"
    s "That’s...something you’d have to ask her about."
    c "Yeah, I figured. I know you two are close, so I just wasn’t sure if you’d know the answer off the top of your head or not."

    scene sunbathing29
    with dissolve

    c "{i}Also, between you and me...I think she might have a crush on you.{/i}"
    s "…"

    "That’s not good."
    "I’m not sure what Chika and Rin talked about last night, but I’m pretty sure that Rin’s true feelings didn’t come across if {i}this{/i} is the impression Chika was left with."

    if chikadorm20 == True:
        c "{i}What are you gonna say to her if that’s true?{/i}"
        c "{i}Like...you and me are already a thing.{/i}"
        c "{i}And I love the girl but...I don’t really want to share you. And she doesn’t know about us either.{/i}"
        s "You know...maybe it’s best if we talk about this when there aren’t two other girls sitting right next to you."
        c "{i}But I’m a really good whisperer. See? They haven’t even noticed.{/i}"
        s "I see that. But I’m a very bad whisperer and they would definitely notice if I tried saying something."
        c "{i}Okay. We can talk later then.{/i} "
        s "Works for me..."

    else:
        c "{i}What are you going to do if that’s true?{/i}"
        s "I haven’t really thought about it, to be honest..."

        "Well, correction- I {i}have{/i} thought about it."
        "But Rin’s made it overwhelmingly apparent how interested in Chika she is."
        "I mean, the girl is basically obsessed."
        "So what I’m more concerned about than anything is how Chika will react if {i}she{/i} finds out it’s her that Rin is into."
        "Because right now...it seems like she doesn’t have any idea whatsoever."
        "And that worries me."
        "So...maybe there’s a way for me to find out?"

        s "If you were in my shoes, what would you do?"
        c "{i}If I were in your shoes?{/i}"

        scene sunbathing30
        with dissolve

        c "{i}Hmm...{/i}"
        c "{i}Well...I obviously can’t get into your head so I don’t know how attracted you are to her...{/i}"
        c "{i}But I would consider that there are probably several other girls into you as well...And some might be a little more suited to your tastes or-{/i}"

        scene sunbathing31
        with dissolve

        c "{i}More mature...{/i}"

        scene sunbathing32
        with dissolve

        c "{i}Not to say she’s not or anything! It’s just...you know.{/i}"

    scene sunbathing33
    with dissolve

    mi "Hey, what are you guys whisperin’ about over there?"
    c "Huh?! Oh! Uhh...nothing! We were just talking about our plans for tonight and stuff..."
    mi "Well then why the heck were you whispering? You guys up to some secret, no-good stuff?"
    c "We’re not up to anything!"
    t "You’re up to something."
    c "You too, Tsuneyo?!"

    scene sunbathing34
    with dissolve

    t "Ah-"

    scene black
    with dissolve2

    "The conversation quickly spirals into a series of other spontaneous topics like where we’d want our next vacation to be or what the girls plan on dressing up as for Halloween."
    "Apparently, Tsuneyo had never heard of Halloween, so we needed to explain that to her...which took around half an hour or so."
    "Actually, I’m pretty sure it took even longer."
    "I wound up leaving before the discussion ended and started heading back to the inn to take a break from everything..."

    $ renpy.end_replay()
    $ beachvacation12 = True
    $ chika_love += 1
    $ tsuneyo_love += 1
    $ miku_love += 1
    stop music fadeout 5.0

    "{i}Your affection with Chika, Tsuneyo, and Miku has increased by 1!{/i}"
    "………"
    "……"
    "…"

    if ayane_lust >= 10:
        jump ayanelust10
...
```