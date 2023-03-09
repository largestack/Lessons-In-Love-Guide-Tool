# To Sleep, Perchance to Dream
Miku event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikuwinterbeach1&go=Go)


Part of event chain [I'm Not Here](./makotowinterbeach3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: mikuwinterbeach1
* Group: Miku
* Triggered by label: makotowinterbeach3

## Event code
File: \game\MikuEvents.rpy
Code:
```python
...
label mikuwinterbeach1:
    play sound "slidedoor.mp3"

    "Makoto and I make it back to the inn to find the entire room dark and devoid of sound."
    "It’s a little disappointing knowing how quickly the day came to an end..."
    "But on the bright side, at least it means that I won’t have to figure out how to correctly answer any more of Makoto’s questions."
    "Frankly, it’s mildly miraculous that I was able to make it through the night without really pissing her off."
    "Especially since she brought up one of my least favorite topics in the idea of me fully devoting myself to one person."
    "Still, though-"
    "We wind up in the same place at the end of the day. "
    "We take our clothes off in separate rooms and reconvene in front of a mutual acquaintance of ours."

    scene mikusleeping1
    with dissolve
    play music "asobeatsex8.mp3" fadein 4.0

    mak "See? I told you she’d be out cold."
    s "Congratulations. What would you like as your reward?"

    if bonus == True:
        jump mikubeachdryx
    else:
        scene black
        with dissolve

        mak "A night of peace and quiet in separate rooms because sleeping in the same bed is unnecessary and weird."
        s "I agree. Goodnight, Makoto."

        "Makoto and I go to sleep in separate rooms, but Miku wakes up in the middle of the night to come and hug me before going back to sleep."
        "It's weird and she feels bad about it."
        "Oh well."

        $ renpy.end_replay()
        $ mikuwinterbeach1 = True
        $ miku_love += 1
        stop music fadeout 5.0

        "{i}Miku’s affection has increased to [miku_love]!{/i}"
        "………"
        "……"
        "…"

        $ totaldays += 1
        $ day += 1
        if day == 7:
            hide saturday onlayer date
            show sunday onlayer date

        jump makotowinterbeach4

label soccer35:
...
```

## Code that triggers this event
File: \game\MakotoEvents.rpy
Code:
```python
...
mak "I suppose there’s nothing else I can do."

    "I’m not here."
    "Well, I {i}am{/i} here."
    "But I’m not here."
    "I feel far away from something."
    "I feel hands on my shoulders, pulling me backwards."
    "I feel frayed wires wrapped around my ankles, scratching me enough to draw blood but not to sever my Achilles tendons."

    mak "...Huh."
    mak "Do you feel that, Sensei?"
    s "Feel what?"
    mak "A...minor earthquake, maybe?"
    mak "I thought I felt the ground shaking, but it was probably just a wave crashing down or something."

    "The ocean is still, though."
    "There are no waves anywhere to be found."

    mak "Oh, I did a little more digging on this Yasu Yasui character, by the way."
    mak "I don’t know why it never occurred to me to just ask the other girls from Kumon-mi Academy, but several of them knew her. "
    mak "Namely Uta and Noriko."
    s "Figures that the talkative ones would know her. "
    mak "I suppose. Neither of them seemed to know her all that well, though."
    mak "Apparently, she didn’t attend normal classes on account of her...behavior. So I’m now worrying that we really {i}will{/i} have another Yumi on our hands before we know it."
    s "Did they say anything about how cute she is by any chance?"
    mak "Really? You’re going to ask that now? After I {i}just{/i} finished telling you about how I want you to look at me more?"
    s "This doesn’t count as me being mean, does it?"
    mak "It...kind of does."
    s "Oh. Well then I guess I can just find out when she transfers in."
    mak "I...guess so."
    mak "Can I ask you one more thing before we head back, Sensei?"
    s "You weren’t kidding about wanting to talk a lot this weekend, were you?"
    mak "No, I was not. But there’s been something else on my mind that I haven’t really had a chance to ask you about."
    s "And what is that?"
    mak "Well...I looked into Noriko’s background after she transferred in and wound up speaking with her parents."
    s "Well that’s not creepy or an invasion of privacy by any means."
    mak "Can you let me finish, please?"
    mak "I wound up speaking with them and they definitely remember you, so her story checks out."
    mak "But I..."
    s "...You what?"
    mak "I also looked into Maya as well because...I was curious about their apparent...{i}connection{/i} with one another."
    mak "Maya spends a good deal of time at your house, correct? I know her and Ami are close, so it would only make sense if she did."
    s "Yeah. It’s basically a second home for her, I guess."
    mak "I thought so...But would you have happened to speak with any of her family in the past, by any chance?"
    mak "Because all of the phone numbers on record for her are either disconnected or simply made up. "
    s "For Maya?"
    mak "Yeah. I mean, it’s possible that it’s just outdated paperwork, but...it seems strange."
    s "All I really know is that she’s not originally from here."
    mak "Ahh. Well I suppose that would probably explain it."
    mak "Sometimes, files get mixed up when students switch municipal districts, so it probably just got lost in the shuffle somewhere."
    mak "It’s no big deal, I suppose. I’ll just ask her for updated information soon."
    mak "Oh, and is it true that you dated Niki Nakayama?"

    if otohapark1 == True or saradate10 == True:
        s "Yeah, that’s true."
        s "Want me to call her and confirm that for you? She loves when I do that."
        mak "What? No. That won’t be necessary. I have no reason to doubt you since I heard it directly from Noriko’s parents."
        mak "But that’s really surprising. I didn’t take you as the type to be into nice, pretty girls like her."
    else:
        s "Yeah, that’s true."
        mak "That’s really surprising. I didn’t take you as the type to be into nice, pretty girls like her."

    s "Pretty, sure. But I can assure you that Niki is anything but nice."
    mak "Really? But she seems so kind on TV."
    s "She’s kind of like what would happen if Yumi became really stuck up and started chewing unhealthy amounts of bubblegum."
    mak "Wow. I guess that whole thing about celebrities not being who you expect them to be is true then."
    s "Anything else you were curious about or can we start heading back now? It’s getting cold."
    mak "We can start heading back. "
    mak "We’re going to have to be quiet when we walk in, though, since Miku is probably asleep by now."
    s "Already? I figured she’d be the type to stay up until like 3:00 AM."

    if bonus == True:
        mak "Oh, lord no. She’ll be out like a light. But she wakes up very easily, so we’ll need to be really quiet while getting dressed."
        s "I guess that means there’s no chance for a nightcap then?"
        mak "Are you seriously this horny all of the time? I think you might have some sort of condition, Sensei."
        mak "We should take you to the doctor once we get back home."
        s "My feelings for you are not a sickness, Makoto."
        mak "Ugh..."
        mak "At least wait until we get back to the dorm to say things like that..."
    else:
        mak "Nope. And Makoto sleepy so we leave now."
        s "Sensei sleepy too. I want my jammies."

    scene black
    with dissolve2

    "Makoto and I make our way back to the inn."
    "Halfway there, snow begins to fall."

    $ renpy.end_replay()
    $ makotowinterbeach3 = True
    $ makoto_love += 1
    stop music fadeout 10.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

    jump mikuwinterbeach1
...
```