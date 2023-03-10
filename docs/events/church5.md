# Armor of Older Gods (Yasu)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yasu love greater than or equal to 5

* Event [Transference](./church1.md) (Yasu) is completed)



## Next events

None

## Event properties

* Id: church5
* Group: Yasu
* Triggered by label: church
* Triggered by branch label: church
* Triggered by path: church->church5

## Official wiki page

[Armor of Older Gods](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=church5&go=Go) for more details.

## Event code

File: (install folder)\game\YasuEvents.rpy

Code:
```python
...
label church5:
    stop music
    scene churchglow1
    with dissolve2
    play music "newhope.mp3"

    "A mysterious girl stands before a mysterious altar inside of a mysterious building in a mysterious part of town."
    "She was not waiting outside the same way she was the last time I came here, which I suppose means that today I am allowed to enter."
    "And, on the off chance that I am not, let {s}God{/s} god smite me with all of {s}His{/s} his wrath."

    play sound "static.mp3"
    scene p1 with flash
    scene p2 with flash
    scene p3 with flash
    scene p4 with flash
    scene churchglow1 with flash
    stop sound

    "I feel something touch me, but not long enough for me to get accustomed to the sensation. "
    "Not long enough for me to fall in love with it and have dreams of growing old together."
    "To have dreams of those celestial hands decaying with the passage of time."
    "To watch the skin wrinkle and the veins protrude."
    "One of my favorite things about older people is that it becomes easier to see the insides of their bodies without having to work for it."
    "Like their entire vascular system is laid out like a placemat, decorating wherever they may go with a display more beautiful than any work of art could ever possibly be."
    "Or hideous, depending on the way you look at things."
    "Let’s talk about perception for a moment."

    play sound "static.mp3"
    scene p1 with flash
    scene p2 with flash
    scene p3 with flash
    scene p4 with flash
    scene churchglow1 with flash
    stop sound

    "Let’s not talk about perception."
    "Let’s talk to Yasu instead."

    ya "Blessed be those who give up their eyes. "
    ya "Who give up their mouths. "
    ya "Who give up their lives."
    ya "Blessed be those who see in the dark."
    ya "Who cut off their tongues. "
    ya "Who sleep in the ark."
    ya "Come to me, Father. Come to me, Mother. "
    ya "Come to me sisters, and cousins, and brothers."
    ya "A life without light is life left unlived."
    ya "A life filled with God is a life to forgive."
    ya "Praise be."
    s "{s}Praise be.{/s}"

    "I suppress a strange desire to cry out. "
    "The air in the room is cold and stale. "
    "It smells of mold masked by scented candles, but the unlit kind that don’t carry with them the same level of warmth and comfort that the burning ones do."
    "As such, it’s not very pleasant."
    "To disguise something unfavorable with something that {i}is{/i} favorable is akin to denial. "
    "And denial makes us weak."
    "But it’s such a strong tool."
    "Here is a list of other strong tools:"
    "Hammer "
    "Power Drill"
    "Power Hammer (Probably not a thing, but it would be cool. Just think of how many nails you could drive in.)"
    "Saw (Various types)"
    "The pen (Artistic answer. Don’t actually use a pen in a fight. You will lose.)"
    "(Try using a Power Hammer™ instead)"
    "And religion."
    "Religion is actually the strongest tool out there."
    "Because not only can you use it to justify anything and everything you could possibly want, you can also use it as a scapegoat when things go wrong."
    "If God made you do it, is it really your fault?"
    "That phrase is so powerful that even those who stray from religion break it out from time to time. "
    "And I’m not just talking about those same people who only pray when things get bad. "
    "But I guess, in a sense, those people are worth mentioning here as well."
    "That’s how strong of a tool religion is."
    "Regardless, I don’t think it’s fair to compare Yasu’s religion to any of the commonly scapegoated ones as she, at least to my knowledge, is the sole follower of it."
    "But I’m sure that won’t prevent her from using it as a tool to garner favor or dodge blame in the future."
    "Thankfully, the future is a long way from here. But also on top of us at the same time."

    if bonus == True:
        "It’s pinning us down by our shoulders and shifting our panties to the side, preparing itself to ruthlessly violate our perception of-"

    play sound "static.mp3"
    scene p1 with flash
    scene p2 with flash
    scene p3 with flash
    scene p4 with flash
    scene churchglow1 with flash
    stop sound

    "Let’s not talk about perception."
    "Let’s talk to Yasu instead."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene churchglow2
    with dissolve

    ya "My, my...what a pleasant surprise."
    ya "To see another face inside of the church is nothing short of a dream come true for me. "

    if bonus == True:
        ya "Did you bring the whip?"
        s "Uhh...what?"
    else:
        ya "Did you bring the Cool Whip?"
        s "Are you baking a pumpkin pie?"
        ya "No. I am going to drown you in it."
        s "What?"

    scene churchglow3
    with dissolve

    ya "A joke, of course. Violence is not something we take lightly here."

    if bonus == False:
        s "That was a very bad joke, Yasu."

    scene churchglow2
    with dissolve

    ya "You are safe within these walls."
    ya "And even if it feels like everything is caving in, or that the floor wants to open up and swallow you whole, you will be okay."
    ya "Only good things happen here."
    s "This place is fucking weird, Yasu."
    ya "Weird? How so?"
    ya "What makes it any different than another place of worship?"
    ya "We have candles, religious symbols, benches-"

    scene churchglow4
    with dissolve

    ya "And now...people."
    ya "Oh, how wonderful it is to finally say that."
    s "Am I really the first person other than you who’s come in here?"

    scene churchglow2
    with dissolve

    ya "To my knowledge, yes."
    ya "Though I suppose it would technically be possible for others to wander in while I’m away at[school] or in my room."
    ya "I can’t be everywhere at once, of course. Omnipresence is a power of God and God alone."
    ya "Though, I do hope to become an angel one day."
    s "Don’t you need to just...die to become an angel? Isn’t that how it works?"

    scene churchglow5
    with dissolve

    ya "I’m sure there are some systems of belief that would say so. But things are a bit more complicated for people like me."

    scene churchglow2
    with dissolve

    ya "Do you remember when we last spoke of the differences between boys and girls?"
    ya "When I informed you of the wondrous role you could have if only you’d sacrifice yourself?"
    s "What do you mean, “If only?” That’s a pretty big caveat, Yasu."
    ya "Is it truly a caveat if you’re immediately reborn in the process?"
    s "I mean, I’ve definitely got some experience in the “being reborn” department and it’s not all that bad. "
    s "But still, yeah."

    scene churchglow6
    with dissolve

    ya "Hahahaha! So it {i}is{/i} true! "
    ya "Every day, you grow some more! "
    ya "You’re a truly wonderful person, Sensei. So gifted and handsome and funny."
    s "Flattery will get you nowhere, Yasu."
    s "Just kidding, it will get you everything you want. Please continue."

    scene churchglow2
    with dissolve

    ya "Perhaps another time. "

    ya "For it just occurred to me that I never finished explaining the role of the woman in all of this."

    if bonus == True:
        ya "You see Sensei, we’re not just entities meant to consume His love and spread His seed."
        ya "We are at first, but not in the end."
        ya "The truth is, if we work hard enough and make a big enough dent in the armor of older gods, we graduate and become “Angels.”"
        ya "Not angels in the traditional sense with eyes so bright that they could scorch you to death-"
        ya "But angels who decide who stays and who goes."
        s "Stays where and goes where?"
        ya "Here and there, I suppose."
        s "Informative. And how do you know this if you’re the sole follower of this weird cult thing?"
        ya "Because I can hear it."
        ya "The whispers. The rumbling. "
        ya "I can hear it."
    else:
        ya "You see Sensei...(Airplane noises)"
        s "..."
        ya "(More airplane noises)"
        s "..."

    scene churchglow4
    with dissolve

    ya "And even if I did not hear those things, I would still know them."
    ya "There are some things that you don’t need to see or hear in order to understand."

    play sound "static.mp3"
    scene churchglow7
    with flash
    stop sound

    ya "How to walk. How to blink. How to breathe. "
    ya "Like animals, human beings are born with this wonderful thing called instinct. "
    ya "We know how to do so many amazing things from the moment we escape our mothers, screaming and dripping with blood."
    ya "We don’t know where we are or who we are, but we know we exist."
    ya "We know that what we see is real and what we feel is real."
    ya "The only thing is, some of us feel a little more than others."

    scene churchglow8
    with dissolve

    ya "And some of us {i}see{/i} more than the others."

    play sound "static.mp3"
    scene churchglow9
    with flash
    stop sound

    s "So...let me just recap a few of the things you’ve said to me over the brief yet incredibly strange time we’ve known each other."
    ya "Please do~"
    s "The first time we met, you talked about how I have “seen God.”"
    ya "I did."
    s "Tonight, you are insinuating that I “see more than others.”"
    ya "Right again."
    s "But on like, four other occasions, you have told me I need to open my eyes."
    ya "Ding ding ding! You remember everything!"
    s "…"
    s "Sorry for just coming out and asking this but..."
    s "Are you on drugs?"

    play sound "static.mp3"
    scene churchglow7
    with flash
    stop sound

    ya "Not anymore. "
    s "What do you mean “not anymore?” That seems like a very important detail."
    ya "External forces like medications or narcotics slowly strip the sanity from your mind and your body. "
    ya "I am happier and safer now than I have ever been before."
    ya "Because now, nothing is held back. Nothing is suppressed."

    if bonus == True:
        ya "I can feel His glory and feel His warmth. "
        ya "And one day, I hope to feel yours."

    scene churchglow9
    with dissolve

    if bonus == True:
        s "What a strange way to come out and say that you want to have sex with me."
    else:
        s "What a strange way to invite me to prom."

    play sound "static.mp3"
    scene churchglow2
    with flash
    stop sound

    ya "What a strange way to interpret the desire to connect with another human being on a more spiritual level."

    if bonus == True:
        ya "Warmth does not strictly mean sex, Sensei."
        ya "I feel the warmth of God every day and am very much a virgin."
        ya "As such, I’d likely be able to feel yours without ever touching you. "
    else:
        s "Yasu-"
        ya "(Airplane noises)"
        s "..."

    scene churchglow10
    with dissolve

    if bonus == True:
        ya "But, of course, that does not mean we wouldn’t {i}be able{/i} to touch. Do you understand?"
        s "Not really. But I’m definitely interested in the touching part."
        ya "The touching part is a gift from Him and should not be the key interest here."
        ya "This is no joke, Sensei. The infusion of righteousness and the transfer of purpose from one body to another is not something that should be taken lightly."
        ya "To be pure as judged by the power of Him and Him alone is to rid yourself of love and desire so that he may consume them."
        s "Sex has nothing to do with love. It’s just an action."
        ya "An action that must be approved. "
        ya "For we are free to use our bodies to experience {i}that{/i} type of warmth with one another, but only when that warmth flows back into him."
        ya "Do you understand?"
        s "Again, no."
    else:
        ya "(Airplane noises)"

        "Why does this always happen to me?"

    play sound "static.mp3"
    scene churchglow11
    with flash
    stop sound

    ya "It is He who lives vicariously through our thoughts! Through our sensations!"
    ya "Why should {i}we{/i}, as less important, less virtuous creatures, feel the pleasures of life when He can not?!"
    ya "We must become one with the machinations of this world and all that lives within it so that it may all flow back into Him!"

    if bonus == True:
        ya "Each and every ounce of fluid transferred from one entity to the next without His blessing adds more to pain! It makes everything hurt!"

    scene churchglow12
    with dissolve

    ya "But when He gives us His blessing, He can feel what we feel."
    ya "It is all He has. He needs it to survive. He needs it to smile."
    ya "And when He smiles, we smile. I smile. "
    ya "Smile with me, Sensei!"
    s "I’m okay, thanks."

    play sound "static.mp3"
    scene churchglow2 with flash
    stop sound

    if bonus == True:
        ya "The act of human beings connecting on a physical level should be something witnessed before Him."
        ya "As an angel in training, it is my duty to abstain from any practice He would find abhorrent."

    ya "It is my duty to forego the realm of the senses so that each and every sensation can be used on someone much bigger than me."
    ya "I am a tiny girl, and yet this body feels so much."
    ya "I can only imagine how He, who encompasses all space, must feel."

    play sound "static.mp3"
    scene churchglow13 with flash
    stop sound

    ya "Sing me a song that reminds me of better days!"
    ya "Enter me and experience all that I am!"
    ya "Consume my thoughts and wrap yourself around my organs!"
    ya "Bask in the warmth that you have sacrificed so that we may live!"
    ya "When all others fail you, I will still be here! Feel it all through me!"
    ya "Feel everything through me! For I am yours and yours alone!"
    s "…"
    ya "Praise be!"
    s "…"
    ya "…"

    scene churchglow14
    with dissolve

    ya "He’s feeling shy tonight and doesn’t want to talk to me."
    ya "Probably because you’re here. "
    ya "But that’s okay. He is all powerful, but can act a little childish at times."
    ya "He’s still very young, all things considered."
    s "…"
    ya "…"
    s "Okay, well I think that’s enough for tonight."
    ya "Will you come back?"
    s "Probably. But not because I believe in your god."
    ya "Because I “entertain” you?"
    s "Because you “entertain” me."
    s "Goodnight, Yasu."
    ya "Goodnight, Sensei."
    ya "May the path you walk be free of callousness."

    scene black
    with dissolve2

    "I exit the church and walk out into the snow."
    "It’s somehow even warmer out here than it was in there."
    "I go home."

    $ renpy.end_replay()
    $ yasu_love += 1
    $ church5 = True
    stop music fadeout 5.0

    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label church10:
...
```

## Code that triggers this event

File: (install folder)\game\YasuEvents.rpy

Code:
```python
...
label church:
    if yasu_love >= 0 and ramen20 == True and church1 == False:
        jump church1
    if yasu_love >= 5 and church1 == True and church5 == False:
        jump church5
...
```