# Carry Me Home (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sana love greater than or equal to 15

* Event [Supermom](./bar10.md) (Sana) is completed)



## Next events

* [Main: Girl-Talk](./day65.md)
* [Sana: Scouting Mission](./bar20.md)
* [Sara: A Woman's Heart](./saradate1.md)

## Event properties

* Id: bar15
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar
* Triggered by path: sanasbar->bar15

## Official wiki page

[Carry Me Home](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar15&go=Go) for more details.

## Event code

File: (install folder)\game\SanaEvents.rpy

Code:
```python
...
label bar15:
    play music "calmbar.mp3"
    scene carryredux1
    with fade

    "I show up to the bar around the usual time and, just as always, there are no customers anywhere in sight."
    "I wonder how much longer the Sakakibaras will be able to keep this up before just calling it quits and trying something else?"
    "I can't imagine it would be easy since Sara lives upstairs, but I just...can't imagine this being sustainable at all."

    scene carryredux2
    with dissolve

    sa "Oh, Sensei...good...good evening..."
    s "Hey, Sana. How is work going?"
    sa "Oh, you know...more of the same...there’s...{i}hic{/i}...not really anything happening, so..."
    sa "We're just........{i}hic{/i}...hangin' out..."
    s "..."
    sa "What? Why're...ya...lookin' at me like that..."
    s "Sana, are you drunk right now?"
    sa "{i}Hic...{/i}"
    sa "Nahh."
    sar "She's fiiiiiine~"
    sar "Sana, get Sensei a beer and lock the door."
    s "You should probably-"
    sa "One...{i}hic{/i}...spaghetti...coming up..."
    s "..."

    scene black
    with dissolve2

    "Yeah, this definitely isn't sustainable."
    "Sana gets me a beer from behind the counter and I guess...completely forgets it's meant for me as she walks it over to the couch and cracks it open herself."
    "It's clear that the two of them have been going at it for at least {i}some{/i} amount of time given how far gone Sana already is, but..."
    "Well, Sana also weighs the same amount as a large brick, so I can't imagine she holds alcohol very well."
    "Her mother, on the other hand..."

    scene drunk1
    with dissolve2

    "Is not much different."

    sar "{i}You're hot.{/i}"
    sa "{i}Hic...{/i}"
    sa "{i}I can't even...taste anything anymore...{/i}"

    "I begin to go over the possible scenarios that may have led to this in my head and all of them fall back on Sara being the one to blame."
    "Now, is it wrong for me to be assuming this despite our relationship still being in its earliest stages? Maybe."
    "But I can't really think of many scenarios in which it would be okay for a guardian to encourage this sort of behavior."
    "That being said, I don't really intend to stop it because I think it's funny and has created an opportunity for me to flirt with a hot mom."
    "Sorry, Sana. Please don't become an alcoholic."

    s "Thanks, Sara. Are you sure it’s okay to let Sana drink, though? She seems pretty out of it."
    sar "Whaaaat? Of course it’s okay. We live above a bar. She's in good hands."
    s "Is she? Because I'm not convinced you'd really be able to carry her in your condition."

    scene drunk2
    with dissolve

    sar "Sensei, she's {i}fine.{/i} There's no problem doing something like this every once in a while, is there?"
    s "How often is {i}once in a while{/i} exactly?"
    sar "What? You think I keep track? Come on, Sensei. Be like Sana and live a little."

    scene drunk3
    with dissolve

    s "I didn't realize your idea of {i}living{/i} was so...depressingly mature."
    sa "I am a...{i}hic{/i}...victim of...peer pressure..."
    sa "This...{i}hic{/i}...was all...my mom's...idea..."
    sa "{i}Hic{/i}........Who are you again?..."

    scene drunk3r
    with dissolve

    s "She's so drunk that she's forgotten who I am."
    sar "Oh, stop. She's just playing around. There's no way Sana would forget about {i}you{/i} with how much she's been looking forward to your visits lately."
    sar "Sana, be a dear and tell your teacher how you really feel. You hurt his feelings by pretending to forget about him."
    sa "How I...really feel?..."
    sa "Was there...something I wanted to tell him?"
    sar "I don't know, dear. Was there?"
    sar "We won't know if you don't share it with us."

    "Correct me if I’m wrong here, but isn’t it normally the mother who talks their kid {i}out{/i} of doing things like this?"
    "I mean, Sana isn’t in any danger since she can sleep upstairs if she winds up passing out, but this is still kind of weird."

    scene drunk4
    with dissolve

    sa "{i}Hic...{/i}S-Sensei..."
    sa "You’re...a really...cool guy...you know that?..."
    s "Thanks, Sana."
    sa "No, like...{i}really{/i} cool...youknowwhatI’msayin’?"
    s "..."

    scene drunk5
    with dissolve

    sar "I think that’s her code for saying she likes you."

    scene drunk6
    with hpunch

    sa "Ayy! You stay outta this, {i}Mom!{/i} Stop...{i}hic...{/i}stop puttin’ words in my mouth!"

    scene drunk7
    with dissolve

    sa "Sensei...you don’t...gotta listen to her...she's {i}clearly{/i} drunk..."
    s "You are {i}both{/i} clearly drunk and I haven't really figured out how to handle it yet."
    sa "{i}Whatareyatalkinabout?{/i} I’ve only had like, one beer..."
    s "There is no way that's true. And I'd be honestly surprised if that wasn't all it took to knock out a girl your size in the first place."
    s "Are you even going to be able to make it back to the dorm?"

    scene drunk8
    with dissolve

    sa "The wha?"
    s "The dorm. Where you live."
    sa "Ooooohhhh...the {i}dorm...{/i}"
    sa "You're right...I gotta...{i}hic{/i}...tell Ayane I'm...not gonna make it back..."
    sa "I think...I’m just...gonna sleep here tonight..."
    sar "Maybe if you ask nicely, your teacher will volunteer to carry you upstairs and put you to bed?"

    scene drunk6
    with dissolve

    sa "Ayy! Whatareyou still doin’ here?! Take a...{i}hic...{/i}hint forcryinoutloud!"
    sar "I live here, dear. Remember?"
    sa "I don’t care {i}where{/i} you live...{i}hic{/i}...I’m tryina’ have a...conversation with my...teacher and...you're just...{i}hic{/i}...gettinintheway..."

    scene drunk7
    with dissolve

    sa "Sensei, you don’t...have to carry me upstairs...I can do it myself..."
    s "I mean, I really don’t mind. I've carried bags of rice that weigh more than you."

    scene drunk7r
    with dissolve

    sar "You can always carry {i}me{/i} upstairs instead...."

    scene drunk6
    with dissolve

    sa "Mom! Stop tryina’ seduce my teacher! Sensei is...{i}hic...{/i}a good guy who doesn’tevenlike girls!"
    s "What? No, I definitely like girls."
    sa "Shuddup! Don’tgiveheranyideas! She’ll {i}hic...{/i}drink your blood and {i}hic{/i} throw ya to the curb!"
    sar "Sana, dear, I only bite when I'm {i}asked{/i} to. I'd never just-"

    scene drunk9
    with hpunch

    sa "AHHHHHHH!!!!!!!"
    sa "WHOWANTSANOTHERBEER?!"

    scene black
    with dissolve2

    "Sana winds up passing out and falling into my lap roughly five minutes later."
    "She had a good run, though. I just hope that this isn't something that happens as regularly as Sara made it sound."
    "Drinking away your worries is one thing when it's adults doing it, but for someone like Sana-"
    "Well, what would she even have to worry about at her age to begin with?"
    "Anyway, sensing that the collapse of the world's shortest bartender is a good stopping point for the night, I take Sana into my arms and princess carry her to her old room upstairs."

    play sound "dooropen.mp3"

    "I lay her down on the bed, feeling too awkward to bother covering her with a blanket, before turning around and walking into Sara's living room."
    "It's a relatively sparse apartment. Nothing lavish by any means. And Sara is busy-"
    "Wait. Where {i}is{/i} Sara?"
    "Wasn't she just here a second ago?"
    "I pace around the apartment, checking behind corners and curtains, thinking maybe she's playing some drunken prank on me, before realizing that she's probably passed out in her own-"

    sar "Sensei! Help! There's a spider in here!"

    "Or, she is fighting for her life."

    s "I'm coming..."

    "You know, I really dislike dealing with drunk people."

    play sound "dooropen.mp3"
    scene drunk10
    with dissolve
    stop music fadeout 3.0

    "It's like every time you say something to them, they just-"

    sar "Lock the door."
    s "..."

    "What was I saying just now?"

    if bonus == True:
        jump sarabarfirstx
    else:
        s "Why would I do that? It insinuates that there would be adult content and things like that are strictly forbidden."
        sar "I just wanted to know if it would be okay for the two of us to hug."
        s "But Sana is asleep in this very building."
        sar "Hug me anyway, Sensei."

        "What should I do?"

        menu:
            "Hug Sana's mom":
                s "I will now hug you."
                sar "Rejoice. The hug approaches."

                scene black
                with dissolve

                $ renpy.end_replay()
                $ sana_love += 1
                $ bar15 = True
                $ sarasex = True

                "{i}Despite having hugging her mom, Sana’s affection has increased to [sana_love]!{/i}"

                stop music fadeout 3.0

                "........."
                "......"
                "..."

                if day < 6:
                    jump endofweekday
                else:
                    jump endofsat

            "Hugs are icky":
                s "I can not, for I am an educational professional in charge of your daughter's well-being."
                s "Hugging you here would put that at risk."
                sar "I understand and thank you for considering my daughter's education. Thank you, Sensei."

                scene black
                with dissolve

                $ renpy.end_replay()
                $ sana_love += 1
                $ bar15 = True

                "{i}Sana’s affection has increased to [sana_love]!{/i}"

                stop music fadeout 3.0
                "………"
                "……"
                "…"

                if day < 6:
                    jump endofweekday
                else:
                    jump endofsat

label saramissionaryanim:
    scene barnight
    with dissolve
    play music "calmbar.mp3"

    "I show up at the bar to find that Sana isn't working tonight."
    "Instead, Sara and I hang out and talk about different ways for her to start attracting business."
    "Well, to be concise, we talk about that for roughly five minutes before we turn to just flirting with each other."

    if bonus == True:
        "It quickly becomes apparent how horny both of us are and-"
    else:
        "It quickly becomes apparent how much we want to hug, and-"

    "Well..."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump saramissionaryanimx
    else:
        $ sara_lust += 1
        stop music fadeout 4.0

        "We do that."
        "{i}Sara's lust has increased to [sara_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label bar20:
...
```

## Code that triggers this event

File: (install folder)\game\SanaEvents.rpy

Code:
```python
...
label sanasbar:
    if sana_love >= 0 and firsttimebar == False:
        jump firsttimebar
    if sana_love >= 5 and bar5 == False:
        jump bar5
    if sana_love >= 10 and sanafirsthall == True and bar10 == False:
        jump bar10
    if sana_love >= 15 and bar10 == True and bar15 == False:
        jump bar15
...
```