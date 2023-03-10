# Full Blossom (Kirin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Kirin lust greater than or equal to 5

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

* [Kirin: All That is Contaminated](./kirindate25.md)

## Event properties

* Id: kirinlust5
* Group: Kirin
* Triggered by label: soccerfieldkirin
* Triggered by branch label: soccerfieldkirin
* Triggered by path: soccerfieldkirin->kirinlust5

## Official wiki page

[Full Blossom](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirinlust5&go=Go) for more details.

## Event code

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label kirinlust5:
    scene kirinfirstlust1
    with fade
    play music "highspeedprinter.mp3" fadein 5.0

    "I show up at the soccer field...well, soccer-{i}gym{/i} due to the poor weather, and make my way over to Kirin."

    ki "Ohoho~ Approaching me first out of everybody? To what do I owe the pleasure, Sensei?"
    ki "Also, before you tell me that it’s just because I was the first person you saw, allow me to inform you that that is absolutely not an acceptable answer."
    s "It’s not?"
    ki "Nope."
    s "Do you want me to tell you it’s because you’re the prettiest girl in the gym?"
    ki "That would be nice, yes. "
    s "You are the prettiest girl in the gym, Kirin."

    scene kirinfirstlust2
    with dissolve

    ki "Aww, that’s so sweet of you! "

    scene kirinfirstlust3
    with dissolve

    if bonus == True:
        ki "So, what’s up? You actually gonna do some coach-stuff today or are you just here to stare at all of our asses again?"
        s "I don’t exclusively stare at asses, Kirin. I am a man who appreciates the entire package."

        scene kirinfirstlust4
        with dissolve

        ki "More like a man trying to give out {i}the entire package.{/i}"
        s "Perhaps. Interested in buying-in?"
        ki "Is my name Kirin Kanda?"
        s "If it’s not, you’re even less trustworthy than I thought you were."

        scene kirinfirstlust5
        with dissolve

        ki "What do you mean? I’m plenty trustworthy."

        if ayanelust10 == True:
            ki "I never told anybody I caught you fucking Ayane during the beach trip, did I?"
            s "No, you just forced yourself in between us."
            ki "And I’d do it again, too. That was hot as fuck."
            s "I agree as long as you subtract the subsequent trauma. "
            ki "That’s the part that made it hot, though."
            s "Wait, what?"

        else:
            ki "To prove it, I’ll have you know that I still haven’t told a single soul about our little deal."
            s "You mean the one where you have sex with me in exchange for free absences?"
            ki "Yeah, that."
            s "Have you even missed[school] since then?"
            ki "Well...no."
            ki "But it’s still a deal we made and I could really mess things up for you if I recorded it or something."
            s "..."
            s "Please tell me that was a joke."
            ki "Why? I’m so untrustworthy that you wouldn’t believe me either way."

    scene kirinfirstlust6
    with dissolve

    mi "Morning, you two!"
    ki "Oh, Miku. What’s up?"
    ki "Karin told you my ankle is messed up, right?"

    scene kirinfirstlust7
    with dissolve

    mi "Sure did. No sense in worryin’ about practice today, Kirin. Just sit over here and talk to Sensei or somethin’."
    s "What happened to your ankle?"

    scene kirinfirstlust8
    with dissolve

    mi "Sensei! It doesn’t matter what happened! What matters is that she’s hurt!"
    mi "Ya have any idea what could happen to an athlete if they keep goin’ durin’ an injury? Nothin’ good, I’ll tell ya that much!"
    s "But she seems fine to-"
    ki "Listen to the captain, {i}Sensei{/i}."
    ki "If I say I’m hurt, I’m hurt. "
    mi "For real! The nerve of this guy!"

    "What is going on right now?"

    scene kirinfirstlust9
    with dissolve

    ki "You know, Miku, I heard that Sensei’s got some pretty great massage skills."
    ki "Would you mind if maybe he helped me out with my ankle or something? "
    ki "Karin and I cleaned the store-room this morning so there’s plenty of room for the two of us in there."
    ki "Of course, only if you’re okay with it, I mean."

    "Oh. Yeah, I probably should have figured something like that was going on."

    scene kirinfirstlust10
    with dissolve

    mi "I...uhh...well, ya see..."
    mi "There’s a chance Sensei might not be as...great as ya think he is...at that stuff..."

    if bonus == True:
        s "..."
        "She's not going to tell her about what happened in her dorm room, is she?"
    else:
        s "Wtf"

    mi "Two people bein’ alone in the store-room could cause all sorts of trouble..."
    ki "What? But you seemed all-for the idea in the summer. "
    ki "You kept talking about how great it would be for our muscles to get over soreness and blah blah blah soccer-talk."

    scene kirinfirstlust11
    with dissolve

    mi "Yeaaaaaah...I did say all that stuff...didn’t I?..."
    ki "…"
    mi "It’s just...Idunno...I thought more about it and it seems kinda inappropriate...if ya know what I mean."
    ki "Inappropriate? Surely you’re not accusing our dedicated and beloved coach of doing anything {i}weird{/i} with his students, are you?"

    scene kirinfirstlust12
    with dissolve

    mi "I have no idea what the heck I’m even sayin’ anymore."
    ki "Miku, Sensei is a responsible adult who’d {i}never{/i} even think of what you’re suggesting."

    if bonus == True:
        ki "And unless you have..."

        scene kirinfirstlust13
        with dissolve

        ki "Personal experience...to back that up..."
        mi "Huh? I couldn’t hear that last part. Yer gonna have to...speak up or somethin’..."
        ki "…"
        mi "…"

    scene kirinfirstlust14
    with hpunch

    mi "OKAY FINE! GO GET YOUR STUPID LEGS RUBBED!"
    mi "BUT NO FUNNY BUSINESS OR I’M CALLIN’ OFF PRACTICE FOR THE REST OF THE YEAR!"
    ki "Yeah...of course."
    ki "We’ll be in and out in no-time."
    mi "OKAYBYE!"

    scene kirinfirstlust15
    with dissolve

    "Miku quickly sprints away from Kirin and me and falls flat on her face after tripping over a traffic cone."
    "It might be the first time I’ve ever seen her lose her balance, so it’s a little jarring."
    "But not as jarring as the look I receive from Kirin shortly after."

    scene kirinfirstlust16
    with dissolve

    ki "That...was kinda weird..."

    if bonus == True:
        jump kirinfirstlustx
    else:
        s "Yeah. Miku's a fucking weirdo."

        scene black
        with dissolve2

        "Kirin leads me into the storage room where I prefer a completely platonic and not at all sensual massage on only the parts of her body that someone like me would be allowed to touch."
        "I receive express consent regardless because I am a good man and, within a matter of minutes, she's as good as new."

        ki "I'm as good as new."
        s "Hooray!"

        $ renpy.end_replay()
        $ kirinlust5 = True
        $ kirin_lust += 1
        stop music fadeout 5.0

        "{i}Kirin’s lust has increased to [kirin_lust]!{/i}"
        "………"
        "……"
        "…"

        jump saturdayafternoon

label kirininvite1:
...
```

## Code that triggers this event

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label soccerfieldkirin:
    if kirin_lust >= 5 and christmas7 == True and kirinlust5 == False:
        jump kirinlust5
...
```