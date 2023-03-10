# Taking the Reins (Kirin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The Yellow Wallpaper](./secondbeach6.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: kirinlust20intro
* Group: Kirin
* Triggered by label: secondbeach6
* Chain sources: secondbeach6
* Chain sources path: secondbeach6

## Official wiki page

[Taking the Reins](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirinlust20intro&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label kirinlust20intro:
    play sound "slidedoor.mp3"
    scene kirinnodoka1
    with dissolve2
    play music "acoustic.mp3"

    no "Hm."
    no "It looks just like our room, but with less makeup bags and no lingering scent of perfume."

    if bonus == True:
        "I’m not really sure what the plan is here, but it appears that Nodoka and I are now alone in my room."
        "Is she actually functioning off of the residual fumes of leftover lesbianic lust? Perhaps."
        "But I doubt that this will end in anything more than some flirting and maybe a batch of Nodoka points or two."

    s "You can turn the light on if you want."
    no "There’s no need. I tend to function a bit better in darker environments."

    if bonus == True:
        s "I’ll remember this when it comes time to lock you in my secret cave."
    else:
        s "I’ll remember this when it comes time to adopt a giant red dog with you."

    scene kirinnodoka2
    with dissolve

    if bonus == True:
        no "Do not tempt me with a good time, Mr. Humbert. "
        no "If there is one thing sure to excite me apart from the touch of an older woman, it’s being handcuffed and tossed into a dank natural structure and left there to rot."
        s "…"
        s "Cool."
        s "So now what?"
        no "What do you mean, Mr. Humbert?"
        s "I mean that you’ve seen my room and nothing has happened..."
        s "So, either we’re going to take our clothes off...or a lot of girls are going to be mad at both of us for not paying any attention to them."
    else:
        no "If we ever adopt a dog, please don't keep it in the dark for extended periods of time. It will get scared."
        s "I thought dogs had nightvision?"
        no "Don't say that word. It will cause people to theorize."
        s "What?"

    play sound "slidedoor.mp3"
    scene kirinnodoka3
    with dissolve

    ki "Jesus Christ. About fucking time you showed up."

    if bonus == True:
        jump kirinnodokax
    else:
        scene black
        with dissolve

        s "Nodoka, run. She is going to make us watch the third season of Seinfeld."
        no "Oh no."
        ki "Come back. We need to watch the third season of Seinfeld."
        s "You can't make me."
        no "I will watch it with you, Kirin."
        s "Oh no."
        s "I am too late."
        ki "Sensei. You must return to the room and-"

        "I run away as quickly as I can."

        if kirin_lust < 20:
            $ renpy.end_replay()
            $ kirinlust20skip = True
            stop music fadeout 5.0

            "………"
            "……"
            "…"

            jump secondbeach7
        else:
            $ renpy.end_replay()
            $ kirinlust20 = True
            $ kirin_lust += 1
            stop music fadeout 5.0

            "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"

            "………"
            "……"
            "…"

            jump secondbeach7

label secondbeach7:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
no "You...you really are here..."
    os "Uhhhhhhhhhhhh..."
    w "Do not {i}sniff{/i} me, you mischievous wench. "

    scene nodokaispretty13
    with dissolve

    if bonus == True:
        no "I’m open to threesomes, you know..."
        no "I’ll do anything you want me to..."
        s "…"

        "I bite my tongue and manage to prevent myself from scolding Nodoka for being open to hooking up with a female teacher and not me. "
        "Even though Osako already seems to be aware of my relationship with Ayane and...Wakana has her suspicions as well, incriminating myself like that would probably be a death sentence."
    else:
        no "Let's go charge our iPhones together and talk about bears."

        "I bite my tongue and manage to prevent myself from scolding Nodoka for being open to hooking up her phone with a female teacher and not me. My battery is so low."

    s "Nodoka. Please stop sniffing Wakana."

    scene nodokaispretty14
    with dissolve

    if bonus == True:
        no "In the event that they would like a {i}fourth{/i} participant to even out the numbers, I’d like to rescind my earlier statements regarding the probability of us-"
    else:
        no "But I want to talk about bears with her. How else am I supposed to show that?"

    os "Yeah, no. Hold on a second."

    scene nodokaispretty15
    with dissolve

    os "That’s my girlfriend you’re...inhaling right now."
    no "Hm..."
    no "You touched Miss Watabe without her wincing in disgust."
    no "You two must truly have a deeper connection than I believed at first glance."

    scene nodokaispretty16
    with dissolve

    no "No matter. If you’d prefer to use me as some sort of object or toy instead of an active participant in the bedroom, I’d be open to that as well."
    w "Osako. Do the...karate to her."
    os "It’s not {i}the{/i} karate, babe. It’s just karate."
    os "And I’m pretty sure I could get arrested for hitting someone her age, so...let’s just get to our room so you can take a nap."

    scene nodokaispretty17
    with dissolve

    w "Nagasawa, if you attempt to make contact with me even once before the weekend is over, I will poison you in your sleep."
    no "I’m a reeaaaaaally heavy sleeper, Miss Watabe. You could do all sorts of other things to me as well if you wanted and {i}no one would ever know.{/i}"
    os "Uhh...hi. And bye, I guess."

    if bonus == True:
        os "Please keep your weird pervert friend away from us."
    else:
        os "Please keep your weird friend away from us."

    s "I...will do my best."

    scene nodokaispretty18
    with dissolve

    if bonus == True:
        "Osako pulls Wakana along and the two of them hastily walk down the halls of the inn to the room where I imagine they’ll be quarantining for the weekend on account of a[school]girl lesbian outbreak."

    no "Huh."
    no "You know, I’m going to go out on a limb here and assume that if I still had my swimsuit on that none of this painful rejection would have ever happened."

    if bonus == True:
        no "I have very nice legs. And now they are missing out on a cute, obedient girl in the prime of her sexuality."
        s "Nodoka, harness that energy and take it into {i}my{/i} room."
    else:
        no "I have very nice legs. Like that lamp from A Christmas Story but without the fishnet stockings."

    scene nodokaispretty19
    with dissolve
    stop music fadeout 10.0

    if bonus == True:
        no "But it’s just not the {i}same{/i} with a penis."
        s "How do you know? You have zero experience."
        no "Girls are gentle and delicate like flowers, while you are a torrential downpour looking to flood my insides with your seed when all I want is a light shower."
        s "I..."
        s "{i}What?{/i}"

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ secondbeach6 = True
    $ nodoka_love += 1

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "………"
    "……"
    "…"

    jump kirinlust20intro
...
```