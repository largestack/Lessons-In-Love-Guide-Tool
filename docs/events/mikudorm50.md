# The Devil & God Are Raging Inside Me (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Someone Else's Skin](./mikuspecial50.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: mikudorm50
* Group: Miku
* Triggered by label: mikuspecial50
* Chain sources: mikuspecial50
* Chain sources path: mikuspecial50

## Official wiki page

[The Devil & God Are Raging Inside Me](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikudorm50&go=Go) for more details.

## Event code

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
label mikudorm50:
    "We manage to spend at least another hour at the mall and, miraculously, don’t bump into anyone we know. "
    "Feeling victorious due to this once in a lifetime, genuinely fortunate happening, Miku and I decide to head back home after grabbing a quick bite to eat at some fast food place she likes."
    "And while she manages to stay bright and cheerful for the bulk of our “date” today, she gets noticeably quieter on the bus ride back."
    "The silence snowballs to the point where she stops speaking altogether and the air between us thickens."
    "And while I want to say that she’s just upset that the two of us are going to have to part ways, I’m sure there’s more to it than that."
    "There’s always more to it than that."
    "Unfortunately-"
    "It’s hard to ever find out {i}what{/i} without doing a little pushing."

    scene mikudormfivezero1
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    mi "..."
    s "..."

    if bonus == True:
        jump mikudorm50x
    else:
        scene black

        mi "Sensei no what are you doing"
        s "Pushing you!"
        s "Be vanquished, Miku!"
        mi "Sensei no we were supposed to do the thing"
        s "Only if that THING is PUSHING!"
        mi "Ahhhhhhhhhhhhh"

        "I defeat Miku, but it takes a long time and all of my abilities go on cooldown."

        $ renpy.end_replay()
        $ mikudorm50 = True
        $ miku_love += 1
        stop music fadeout 5.0

        "{i}Miku’s affection has increased to [miku_love]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label mikuinvite1:
...
```

## Code that triggers this event

File: (install folder)\game\MikuEvents.rpy

Code:
```python
...
"If you can even call the acceptance of relationships existing outside of your own personal bubble “negative” to begin with."
    "Which you can’t, because that’s just how life works."
    "But it would still be nice for her to get a {i}little{/i} bit jealous."

    scene black
    with dissolve2

    mi "Okay...I..."
    mi "I think I’ve got somethin’."
    mi "Yeah...Yeah, this’ll work."
    s "Need me to come in there with you?"
    mi "I know how to dress myself, ya friggin’ horn dog! Just wait out here and I’ll be done in a sec!"

    "Maybe one day..."
    "........."
    "......"
    "..."

    scene mikugirly19
    with dissolve2

    mi "..."
    s "..."
    mi "Good? Bad? What’s the verdict?"
    s "You look nice. I think I prefer the dress, though."
    mi "I like the dress too, but...I just ain’t ready yet, Sensei. Stuff like this is what I’m more comfortable in."
    mi "I’m fine with tryin’ to go a little more outside of my comfort zone, but...I’ve gotta take baby steps."
    mi "Ain’t always right to expect yourself on the starting roster if it’s your rookie season, ya know?"
    s "Not really, but I’ll trust your judgement."
    s "What you wear or the way you choose to style your hair doesn’t really make any difference to me. So as long as you’re happy, I’m fine with it."

    scene mikugirly20
    with dissolve

    mi "Guess it’s settled, then! Summer Miku’s makin’ her debut appearance before summer even begins!"
    mi "She’s also about to actually spend money on clothes for the first time in forever! So that’s a big step in...some sorta direction as well! Thanks for the help, Sensei!"
    s "What help? All I did was stand here and say you look cute a few times."

    scene mikugirly21
    with dissolve

    mi "Exactly! That was all ya needed to do."
    mi "Sometimes, girls just need moral support. We say a bunch of stuff that’s been squirmin’ around our minds cause we want ya to disagree with us."
    mi "You not doin' that means you passed the test!"
    s "Test?"

    scene mikugirly22
    with dissolve

    mi "The test to prove that I actually {i}do{/i} like ya after all!"
    mi "Sorry Makoto, but Miku Maruyama ain’t backin’ down any time soon!"

    scene black
    with dissolve2

    "Miku goes back into the dressing room to gather the dress her {s}best friend{/s} rival bought for her and decides that she’s just going to keep wearing her {i}new{/i} new outfit for the rest of the “date.”"
    "While we’re waiting in line to pay, it becomes increasingly apparent that mostly all of her nerves have departed with the addition of new clothing or, to harken back to an earlier metaphor-"
    "A different set of skin."
    "We leave the store in a hurry as Miku returns to her normal self and, within a matter of minutes, she has the {i}other{/i} thing she came here for as well..."
    "........."
    "......"
    "..."

    scene mikugirly23
    with dissolve2

    mi "Here! I went ahead and got you vanilla since you seem so boring and normal all the time."
    s "That’s a very offensive thing to say to someone who just bought you ice cream."

    scene mikugirly24
    with dissolve

    mi "I’m obviously just kiddin’, Sensei. I don’t think you’re normal at all."

    if bonus == True:
        mi "Ain’t nothin’ even remotely normal about gettin’ locked inside of a love triangle with two students. Let alone ones as young as-"
        s "Yes, thank you for acknowledging how inappropriate and abnormal our situation is. I would never have recognized it otherwise and I thank you for setting me down the right path."
        mi "Well, wherever that path is headed, I hope I can walk it with ya."
        mi "I might not be as smart or feminine as the other girls, but I’ve got tons of energy and I can’t think of anybody I’d rather spend it on than you."
        mi "Now eat your friggin’ ice cream before it starts to melt!"
        mi "We’ve got lots more hangin’ out to do!"
    else:
        s "Are you bullying me right now?"
        mi "Gimme all your lunch money, punk!"
        s "But I just bought you ice cream D="

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ miku_love += 3
    $ mikuspecial50 = True
    stop music fadeout 20.0

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "........."
    "......"
    "..."

    jump mikudorm50
...
```