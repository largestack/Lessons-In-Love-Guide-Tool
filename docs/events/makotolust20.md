# Hot Water
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotolust20&go=Go)


Part of event chain [We Were Angels](./secondbeach13.md)

## Event preconditions
✅Makoto lust greater than or equal to 20



## Next events
None

## Event properties
* ID: makotolust20
* Group: Makoto
* Triggered by label: makotolust20intro

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label makotolust20:
    if _in_replay:
        play music "behindabathroom.mp3"

    mak "Well...how about this, then?"
    mak "There’s a trail behind the inn that leads to a little hot spring Miku and I found during the last trip we went on here."
    mak "And while it isn’t technically {i}swimming,{/i} we’d still be able to say we did {i}something{/i} in the water. And hot water, at that."
    mak "I don’t think it’s co-ed, but we’ve rented out the entire inn apart from one room, so I doubt anyone will bump into us there."

    if bonus == True:
        jump makotospringx
    else:
        s "If it is not co-ed, we should obey the rules and not go in together."
        mak "Would you like to take turns?"
        s "I will just go to the boys section and bathe by myself because I am the loneliest man in a world full of nothing but girls."
        mak "It must be so hard to be you."
        s "No one ever wants to talk about UFC with me."

        scene black
        with dissolve

        "I go be a man and cry in the hot spring."

        $ renpy.end_replay()
        $ makoto_lust += 1
        $ makotolust20 = True
        stop music fadeout 5.0

        "{i}Makoto’s lust has increased to [makoto_lust]!{/i}"
        "………"
        "……"
        "…"
        "…"
        "…"
        "I miss feeling whole."

        jump secondbeach14

label secondbeach14:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
mak "Were you also trying to tell the truth when you told the girls of Dorm #8 that I’m going around sleeping with janitors before they die?"
    else:
        mak "Were you also trying to tell the truth when you told the girls of Dorm #8 that I’m going around hugging janitors before they die?"

    mak "Or when you told Touka that I had a penis?"
    s "Nope. Those were lies."

    scene makotolusttwenty3
    with dissolve

    mak "Yes. I’m aware they were {i}lies.{/i} The point I’m attempting to convey is that you don’t exactly have the best track record when it comes to telling people the truth."

    scene makotolusttwenty4
    with dissolve

    mak "But...the whole Niki Nakayama thing has already been confirmed by several members of the class."
    mak "And also...I may or may not have seen her tour bus parked at the back entrance of the inn."
    s "Oh, okay. Well thanks for freeing up some time in your busy schedule to make me seem like some sort of pathological liar when you know I’m just a...normal liar."

    scene makotolusttwenty5
    with dissolve

    mak "Lucky for you, my schedule is floating around somewhere out in the ocean right now."
    s "That’s littering and you should be fined. Also, it would sink."

    scene makotolusttwenty6
    with dissolve

    mak "I didn’t mean it literally. I mean one of the girls stole it in the middle of the night and I have no idea where it went."
    s "And you didn’t have a backup? Shame on you, Makoto."
    mak "{i}Both{/i} of my backups were stolen as well, actually. As if I’d only have one. What kind of girl do you take me for?"
    s "The kind with a sudden overabundance of time and no one to spend it with."

    scene makotolusttwenty7
    with dissolve

    mak "Hm. I do believe there must be at least {i}one{/i} custodial worker at the inn. Perhaps they’d be willing to help me figure out what to do with all of this time?"

    scene makotolusttwenty8
    with dissolve

    mak "Or perhaps I could be a {i}real{/i} badass and skip breakfast altogether."
    s "Watch out, Yumi. There’s a new delinquent in[school]."
    s "Or...not in[school]. Because we’re at the beach."
    mak "Please stop talking."
    s "I can do that."

    scene makotolusttwenty5
    with dissolve

    mak "Well, since fate has done its part in pairing the two of us together while everyone else mysteriously vanishes, how about we do something together?"
    mak "I’d pull something from the itinerary, but alas. Ocean."

    if bonus == True:
        s "We could go back to the inn and I could finger you on the bed again. That was fun last time."
        mak "Unless you’re planning on doing it with Miku sleeping right next to us, that’s probably not a good idea."

        "I mean..."
        "It would...return the favor, at least?"

        s "Miku’s still asleep?"
        mak "She stayed up a bit too late playing video games with Sana and is currently the only one left in the room."
        s "Well, there are several other places I could finger you. It doesn’t really require a lot of space."
    else:
        s "Yup. That is definitely an ocean."

    scene makotolusttwenty9
    with dissolve

    mak "Perhaps I’ll go for a swim? That sounds fun."
    mak "Granted, I’m sure the water is still freezing despite this morning being a bit of a respite from the usual low temperatures."

    if bonus == True:
        s "Or, hear me out here, what about-"

        scene makotolusttwenty6
        with dissolve

        mak "Why do you want to finger me so badly? Aren’t you the one always trying to be {i}satisfied{/i}?"
        s "I have no idea what you're talking about. I am a nice guy who exists only to do nice things for all of you girls."
        s "Also, you look really cute in your swimsuit."
    else:
        s "Or, hear me out here, what about-"

        scene makotolusttwenty6
        with dissolve

        mak "Do you really need another loan to open a sandwich shop?"
        s "Just a small one this time so I can get the good salami."
        mak "Ugh."
        s "Will it help if I say you look pretty?"

    scene makotolusttwenty2
    with dissolve

    mak "And you look...average in your average clothes. "
    s "I can not be blamed for expecting it to be cold again today. It’s cold every day. "

    if makoto_lust >= 20:
        jump makotolust20
...
```