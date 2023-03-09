# Gallows Edge
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo12&go=Go)


Part of event chain [Lavender's Green](./halloweentwo11.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloweentwo12
* Group: Main
* Triggered by label: lavendersgreenx

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label halloweentwo12:
    mo "…"
    s "…"

    scene black
    with dissolve

    "My legs feel weak, but I manage to steady them long enough to pick myself up off the ground."
    "Molly is completely unconscious and, until a second ago...I think I may have been too?"
    "I..."
    "I can’t really say."

    if bonus == False:
        s "..."

        "I give her a goodnight hug and leave."
        "I feel really bad about it afterwards."

        $ renpy.end_replay()
        $ halloweentwo12 = True
        $ mollysad = True

        jump halloweentwo13
    else:
        jump whatwedox

label halloweentwo13:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
"Does Molly have depression too?"

    s "…"

    "Is the real reason she attached herself to Rin because she knows what it’s like to have her skin sliced so raw that you lose the ability to speak clearly?"

    s "…"

    "I wonder if Rin’s scars were visible in Molly’s fantasy just before, or if she created an idealized version of her friend for the sake of better achieving climax through imaginary cunnilingus."

    s "…"

    "Shame on you, Molly. Everyone knows true love doesn’t care about stuff like that."

    s "…"

    "You’re just a horny, little transfer student chasing after the dream of being fucked as hard as one of the girls in those games you play."

    s "…"

    "I am a good guy."
    "Molly is drunk."
    "No one is coming."

    s "…"

    "I took off her costume."
    "Molly is horny."
    "Molly is wet."
    "Molly’s pussy is wet."

    s "…"

    "Molly wants me to fuck her."
    "Molly is sad."
    "I can make Molly feel better."

    s "…"

    "{i}Press the button to make Molly feel better!{/i}"

    menu:
        "Button":
            play sound "static.mp3"
            scene lavendersgreen28 with flash
            stop sound

    "I hold my cock over her slit and press the tip against her belly as I continue to jerk off."
    "Once again, pre-cum is introduced to her flesh, but in a significantly more exciting way this time around as I can now poke it with my cock and spread it around."
    "I gather up the juices clinging to the fingers I used to bring her to [[probably] orgasm and coat my cock in them."
    "I’ve heard of indirect kissing before, but never indirect sex. Is that what this is?"
    "I am a smart man who has invented a new way to have sex with virgins without devirginizing them. "
    "I am very good at everything."

    "{i}Press the button to make Molly feel better again!{/i}"

    menu:
        "Button":
            play sound "static.mp3"
            scene lavendersgreen29
            with flash
            stop sound

    "I grip the base of my cock and prepare to insert myself into Molly by prodding at her entrance a few times, just to gauge her reaction."
    "I expect a twitch or a cringe or something like that, but her body does not move at all."
    "Perhaps she does not want me to have sex with her?"

    s "…"

    "That can’t be true."
    "Everyone wants me to have sex with them."
    "I am the protagonist."
    "I am not Molly."
    "Molly is Molly."
    "Molly is drunk. "
    "Molly is sad."
    "Sex."
    "{i}Press the button to make Molly feel AWESOME!{/i}"

    menu:
        "Button":
            stop music
            scene lavendersbluescreen
            $ renpy.pause(23, hard=True)

    play sound "static.mp3"
    scene ayhh1 with flash
    scene ayhh2 with flash
    scene ayhh15 with flash
    scene lavendersgreen30 with flash
    stop sound

    s "…"
    mo "…"
    s "What?"

    $ renpy.end_replay()
    $ halloweentwo11 = True

    jump halloweentwo12
...
```