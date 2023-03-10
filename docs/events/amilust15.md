# As Light as Air (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Before the Sun Comes Up](./ayanespecial2.md)

## Event preconditions

* Ami lust greater than or equal to 15



## Next events

None

## Event properties

* Id: amilust15
* Group: Ami
* Triggered by label: ayanespecial2
* Chain sources: ayanespecial2
* Chain sources path: ayanespecial2

## Official wiki page

[As Light as Air](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amilust15&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amilust15:
    "{i}At my side the Demon writhes forever,{/i}"
    "{i}Swimming around me like impalpable air;{/i}"
    "{i}As I breathe, he burns my lungs like fever{/i}"
    "{i}And fills me with an eternal guilty desire.{/i}"
    "We’re all impulsive, orgasm loving, God fearing creatures moving from one area to the next in search of anything to make us feel like air."
    "But all we feel is fire."
    "And yet...even then, we rarely ever ignite as human flesh tends to peel and blister before giving us the chance to run around and turn our legacies into light shows."
    "We flail mindlessly instead."
    "Waiting."
    "Then time goes by, and our skin survives long enough to crack and leak out rendered fat."
    "And we become light."
    "As light as air?"
    "That’s hard to say."
    "But we become something. "
    "And something is more than nothing."

    if bonus == True:
        jump amilust15x
    else:
        "That's it. This entire event was a poem."
        "Nothing else happens, but I do go and give Ami a hug once I get up."

        $ renpy.end_replay()
        $ amilust15 = True
        $ ami_lust += 2

        "{i}Ami’s lust has increased to [ami_lust]!{/i}"
        "………"
        "……"
        "…"

        jump afterschoolevent

label amidate50:
...
```

## Code that triggers this event

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
scene postrthree23
    with dissolve

    ay "Do you think this is what I was talking about when I told you I’d need a little more attention soon?"
    s "I have no idea."
    ay "Yeah...and it's kind of funny cause, like..."
    ay "Neither do I..."
    ay "I’m...really confused all of a sudden..."
    ay "My stomach kind of hurts a little too..."
    ay "Is this anxiety? Do I have anxiety now?"
    s "I highly doubt it. You probably just need to get some rest."
    ay "How am I supposed to rest when you came all the way here to see me, though? "
    ay "It wouldn’t be right for me to just kick you out when you're this worried."
    s "Ayane-"

    scene postrthree24
    with dissolve

    if bonus == True:
        ay "Do you wanna at least have sex first? "
    else:
        ay "Do you wanna at least hug first? "

    ay "I’d feel a little better about going to sleep if I gave you a little reminder to take with you when you go."
    s "Sana is literally asleep on your lap right now."

    if bonus == False:
        s "The hug would disturb her."

    ay "She won’t wake up. It’ll be fine."
    s "She woke up after one knock on the door. It won’t be fine."

    if bonus == True:
        s "Besides, I can’t touch you while you’re crying anyway. That’s one of the rules on my...incredibly short list of them."

    scene postrthree25
    with dissolve

    if bonus == True:
        ay "Okay, okay. We won’t have sex."
        ay "But I owe you at least one blowjob in the future as payment for coming to make sure I was okay tonight."
        ay "I still don’t really know what it is that made me cry like this, but I’m sure it’ll be okay soon enough."
    else:
        ay "Okay, okay. No hugs, then."

    ay "I probably just need some sleep like you said."
    s "Then...I guess I’ll go home, then."

    scene postrthree26
    with dissolve

    ay "Are you sure you don’t want to sleep here?"
    ay "My bed is huge. All three of us could fit if we snuggled a little bit."
    s "Maybe some other night. I’m kind of curious about whether anyone else from the apparent “made up slumber party” is still at my house or not."
    ay "Well, if they are, feel free to give me a call. I don’t wanna miss out on the fun even if it’s almost time for[school]."
    s "Oh, shit.[school]."
    s "I didn’t even realize it was Sunday."
    ay "On the bright side, I doubt you had any tests planned or anything like that."
    s "Jokes on you, Ayane. Tomorrow is the day I’m going to become a real teacher."
    s "Well, {i}today{/i} technically, I guess."
    ay "Whatever you decide to do, I'll support it."
    ay "I love you, Sensei. And thank you for coming to see me again tonight."
    ay "I feel a lot better now..."

    scene black
    with dissolve2

    "I leave shortly after that."
    "I don’t understand anything at all."
    "What happened this weekend?"
    "Why did Ayane show up to the roof? And why did she immediately forget it?"
    "This isn’t even resetting. "
    "It’s rewriting things that {i}did{/i} happen with things that didn’t."
    "If they even...did happen?"
    "I don’t know anymore."
    "Not that I ever did, but-"
    "…"
    "But at least I’m still here."
    "And I guess that’s really the most important thing of all right now."
    "…"
    "Huh."
    "I feel like I may have lost something too."

    $ renpy.end_replay()
    $ ayanespecial2 = True
    $ ayane_love += 5
    stop music fadeout 5.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "........."
    "......"
    "..."

    if ami_lust >= 15:
        $ totaldays += 1
        $ day -= 6
        if day == 1:
            hide sunday onlayer date
            show monday onlayer date
        jump amilust15
...
```