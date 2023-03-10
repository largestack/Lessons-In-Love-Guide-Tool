# Floral Aura (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Sonnet 18](./futabainvite1.md) (Futaba) is completed)

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

None

## Event properties

* Id: futabainvite2
* Group: Futaba
* Triggered by label: futabainvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->futabainvite->futabainvite2

## Official wiki page

[Floral Aura](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabainvite2&go=Go) for more details.

## Event code

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label futabainvite2:
    play sound "phonebeep.wav"

    "I tap on Futaba’s name in my phone and wait for her to answer."
    "Considering that her last visit was a resounding success, I’m sure she’ll agree to dropping by again today."
    "Granted, she likely would have agreed to that regardless, but the type of visit I have in mind this time is rather different from the last one."
    "In fact, even if she’d never come over in the first place, I’d have probably wound up in her room looking for the exact same thing tonight."
    "I’m not the type of guy to say that when I put my mind to something, I always accomplish it-"
    "But that trait certainly seems to apply to my outlook concerning girls."
    "And tonight, my sights are set on the resident busty librarian."

    play sound "phonebeep.wav"

    f "Hey! What’s up, Sensei?"
    f "Did you need me to come over and tutor Ami again or something?"
    s "How about you come over here and tutor {i}me{/i} on how to...feel...good?..."

    if bonus == False:
        s "Like...by hugging me. Just to clarify."

    f "…"
    s "I’m sorry."

    "How exactly do I keep succeeding with girls again?"

    f "I’m...going to forget you said that...but I’ll still come over and...see what happens."
    f "Is Ami not home?"
    s "She should be with Ayane tonight, I think. I overheard the two of them talking in class."
    f "Oh, right. I think they were going to the bathhouse or something together. "
    f "You’re not going with them?"
    s "If I was going with them, I wouldn’t have time for you."
    f "Heheh~ You can have time for me whenever you want."
    s "Cool. So right now is good then?"
    f "Of course...I’ll get dressed and head on over. Okay?"
    s "Yup. See you soon, Futaba."

    play sound "phonebeep.wav"

    "I hang up the phone and continue down the road to my house."

    scene black
    with dissolve2
    stop music fadeout 8.0

    if bonus == True:
        "Given that I’ll be {i}alone{/i} with Futaba in my room for the first time ever tonight, perhaps it’s time to try out something we haven’t done yet?"
        "I’m still not sure if she’s ready to lose her virginity, nor am I sure if I’m ready to steal that from her based on any potential blows it may deal to her already-low self confidence..."
        "But there’s definitely something else I can do for her that she may or may not like the idea of..."
        "I guess I’ll just have to wait and see how things play out."

    "………"
    "……"
    "…"

    play music "asobeatsex1.mp3" fadein 5.0
    scene futabacun1
    with dissolve2

    "Futaba makes it to the house shortly after I arrive and follows me into the bedroom, placing her scarf on my desk before sitting down beside me."
    "It’s clear that she’s a little nervous, but it’s not nearly as bad as I imagined it would be."
    "If this were the “beginning of the[school] year” (AKA: My new term for when I was reincarnated into Kumon-mi), she’d probably get those weird, confused swirlies in her eyes she always used to get back then."
    "She’s been a lot more composed lately."
    "I think she’s really trying- which is incredibly respectable given how much shit Yumi she's taken from Yumi."

    f "So...this is your room..."
    s "It is."
    f "It’s...not what I expected..."
    s "What do you mean?"

    scene futabacun2
    with dissolve

    f "Ah! Nothing bad, of course!"
    f "I just expected it to be a little more...sophisticated?..."
    f "It’s kind of hard to describe..."
    f "But I’m sure you’d feel the same way about my room back at home if you were to see it today."

    scene futabacun3
    with dissolve

    f "But...I guess I haven’t been in there in years so...it’s probably a lot more immature now than I remember it being..."
    s "Years? But you’ve only been in the dorms for several months, haven’t you?"

    scene futabacun4
    with dissolve

    f "That’s right. But before that, my parents were paying for me to stay in an apartment close to my last[school]."
    s "You mean the one that sunk into the ground out of nowhere?"

    scene futabacun3
    with dissolve

    f "Yup...that’s the one..."
    s "Are your parents rich or something?"
    s "I know that they’re overseas, but it sounds rough having to send you money {i}on top of{/i} renting out an apartment for you."

    scene futabacun4
    with dissolve

    f "I don’t think we’re rich...but we’re definitely not poor."
    f "They didn't like the idea at first...but I got them to cave since I didn’t want to go with them and leave Japan."
    f "Plus, it was only going to be a year before I switched[school]s and moved into the dorms anyway, so it wasn’t a {i}major{/i} commitment."
    s "Any chance they’d be willing to tack on like...five extra phone bills to their plan? Asking for a friend."

    scene futabacun5
    with dissolve

    f "Sensei...are you...paying for five phone bills?"
    s "Semi-reluctantly, yes."
    f "Why? "
    f "You’re not running some sort of...illegal drug operation that requires you to have that many phones, are you?"
    s "Honestly, going with that is easier to explain, so I’m just going to say yes."

    scene futabacun6
    with dissolve

    f "I don’t really get it but...I’m not sure if my parents would be okay adding that many phone lines without a good reason."
    s "And they wouldn’t be okay with that drug story, I’m guessing?"
    f "No...I don’t think they would."
    s "Any idea when they’re coming back?"

    scene futabacun7
    with dissolve

    f "My parents? No clue."
    f "Are they even allowed to come back right now? "
    f "I’ve heard of some people being allowed to return to Kumon-mi in the middle of the war, but I’m pretty sure it’s only the really {i}important{/i} people and...I don’t think architects count."
    s "So it’s just a matter of waiting for the war to end, then?"

    scene futabacun8
    with dissolve

    f "How would I know?..."
    f "Besides...a-a-aren’t there...you know..."
    f "{i}Other{/i} reasons...you called me over today?"

    if bonus == True:
        jump futabacunx
    else:
        s "No."
        f "...Oh."
        s "Yeah."
        f "Huh."
        s "..."
        f "..."
        s "Wanna play Scrabble and listen to the Tarzan soundtrack?"
        f "..."
        f "Sure."

        scene black
        with dissolve

        "Futaba and I have a heated one-on-one Scrabble battle in which I absolutely wipe the floor with her because I am so smart."
        "Phil Collins is great."

        $ renpy.end_replay()
        $ futabainvite2 = True
        $ futaba_lust += 3
        stop music fadeout 8.0

        "{i}Futaba’s lust has increased to [futaba_lust]! She really likes Phil Collins!{/i}"
        "{i}You can now invite her over to the house on nights and choose to raise your affection or hug her!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label futabalust15:
...
```

## Code that triggers this event

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label futabainvite:
    if futabainvite1 == False:
        jump futabainvite1
    if futabainvite1 == True and futabainvite2 == False:
        jump futabainvite2
...
```