# O World
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day60&go=Go)


Part of event chain [Ode to a Marsh Warbler](./aminew2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Ami: No One Can See Us](./amidorm10.md)

## Event properties
* ID: day60
* Group: Main
* Triggered by label: aminew2

## Event code
File: \game\script.rpy
Code:
```python
...
label day60:
    if _in_replay:
        play music "beyondthewayoftime.mp3"

    "Death is a terrifying thing, isn’t it?"
    "Recall your closest experience with it."
    "What was it like?"
    "How did it feel?"
    "…"
    "…"
    "…"
    "I see."
    "You’re wondering why I’m asking something like this, aren’t you?"
    "This is supposed to be an escape."
    "That which makes you sad should have no place here."
    "And you’re right."
    "But, you see...that’s the funny thing about misery."
    "It always finds its way in."
    "Even through the smallest of cracks."
    "And so we find ourselves, once again, at the edge of everything- trading sadness for solace."

    scene sky
    with dissolve2

    "Hey..."
    "Do you remember when you jumped?"
    "Where do you think you landed?"
    "What do you think happened when you did?"
    "Who would have found you?"
    "And what would they have done with your body?"
    "…"
    "I’m sorry."
    "I won’t keep you much longer."
    "I know you have plans today."
    "But just like last time, there’s something I want you to know first."
    "There are many worlds like this one."
    "In some of them, you will be miserable."
    "And in others-"
    "Nothing will change."
    "But what if there’s {i}one{/i} world out there where that isn’t the case?"
    "And what if getting there is as simple as dropping a penny into a wishing well?"
    "Most assuredly, you’d want to visit that place, correct?"
    "…"
    "Okay. Well then-"

    scene black
    with dissolve2

    "We’re going to count down from ten."
    "When we’re done, you’ll be in that world."
    "A world where problems only exist as long as you believe they do."
    "A world where nothing and everything are both real."
    "And a world where the cracks are small enough that misery only finds its way in sometimes."
    "So-"
    "What do you think?"
    "Will today be a good day?"
    "…"
    "…"
    "…"
    "I see."
    "It appears you still have much to learn."
    "…"
    "Goodbye again."
    "I’ll see you soon."
    "{s}Please begin counting now.{/s}"
    "10"
    "9"
    "8"
    "7"
    "6"
    "5"
    "4"
    "3"
    "2"
    "1"
    "..."

    scene amiani1
    with dissolve2

    a "..."
    s "..."

    "I wake up again. "
    "A wonderful start to the day."
    "Ami sits at my bedside with tears clinging to her eyelids like spiders cling to their webs."
    "One puts forth an effort to crawl down her cheeks in search of a meal, but doesn't make it far and ends the day starving."
    "The rest don't try at all and just give up."
    "I think the sensation of all of the tiny legs must bother Ami, as she removes all of the webs with the back of her hand and continues to stare at me while the spiders rebuild their homes."

    if bonus == True:
        "I think about taking her into my arms and protecting her myself."
        "But my fear of spiders outweighs the desire to prevent her cheeks from being bitten."
        "And should any of them be venomous or poisonous or anything along those lines- I hope that her antibodies will be able to cope."
        "For losing her now would put an end to everything."
    else:
        "But not before making a list of their assets to get their deductions in order for tax season."

    scene amiani2
    with dissolve

    a "Are...you ready to go?..."
    s "Yes."

    "I speak without thinking. It’s as if my mind is reacting to something I’m not entirely aware of."
    "This must be the event Maya had mentioned the other day."
    "Something important to Ami."
    "Something she wouldn’t forgive me if I forgot about."
    "Something that would make her look like this."

    s "Are you okay?"
    a "…"

    "Ami stares at me with a loneliness in her eyes that I’ve never seen before."
    "It shakes what’s left of my heart to the core."

    scene amiani3
    with dissolve

    a "I’ll be fine...I just want to get there before it gets too late."
    s "That’s fine. Me too."

    "Again, I speak reflexively."
    "It’s like I’ve lost control over {s}my{/s} this body somehow."

    scene black
    with dissolve2

    "I get out of bed and the feeling finally returns to my limbs."
    "I open my mouth to stretch my jaw, still stiff from sleeping on it, and suddenly remember how to speak on my own."

    s "Do you want to leave the room while I get dressed?"
    a "No...I’ll stay here."
    a "I'll close my eyes, though."
    s "..."

    "Not wanting to delay us any further, I get dressed as quickly as I can and the two of us make our way out of the house."
    "We walk close together down the street toward the bus station."
    "Ami reaches for my hand and I allow her to take hold of it."
    "Her nails dig into my skin as she clutches it tightly."
    "It’s as if she’s holding on for dear life."

    scene sky
    with dissolve2

    "We board the bus and set off toward our destination- wherever that is."
    "Something in my gut tells me that it will be the end of the world."
    "And so, as I sit here surrounded by unfamiliar faces, clutching the hand of a girl I have only known for a few months-"
    "I speak to myself."

    "{i}O world-{/i}"
    "{i}Please remind me what it means to be alive.{/i}"
    "{i}Because now-{/i}"
    "{i}In what feels like our final moments-{/i}"
    "{i}I still do not know.{/i}"

    scene black
    with dissolve2

    "The bus arrives."
    "We get off of it."
    "We start walking."
    "We arrive."
    "We stop walking."

    "{i}Because I feel that, in the Heavens above-{/i}"
    "{i}The angels, whispering to one another-{/i}"
    "{i}Can find, among their burning terms of love-{/i}"
    "{i}None so devotional as that of “Mother.”{/i}"
    "………"
    "……"
    "…"

    scene amiani4
    with dissolve3

    a "…"
    s "…"

    "Here we are."
    "The end of the world."
    "Or at least, the end of someone’s world."
    "But how did I know to come here?"
    "Ami barely uttered a word the entire trip."
    "All we did was board a bus."

    s "…"
    a "…"
    a "Sensei..."
    a "Do you think..."
    a "Do you think they would be proud of me?"
    s "..."
    a "..."
    s "I do."
    s "You’re a wonderful, [young_girl]."
    s "And I don’t know where I’d be without you."

    "{s}Whose words are these?{/s}"

    scene amiani5
    with dissolve

    a "I don’t know where I’d be without you, either."
    a "You try to act strong all the time, but I know it’s not easy having to look after a little girl all on your own."
    a "That’s why I’ve been trying to grow up as quickly as possible."
    a "To make you proud when..."
    a "When...I can’t..."

    "Ami suddenly stops speaking when she realizes where her sentence is heading."

    scene amiani6
    with dissolve

    "Her legs give out and she slowly crumbles to her knees."
    "She places a hand on the gravestone to try and pick herself up, but it only prevents her from falling further."

    a "I...think I might throw up..."
    s "…"

    "I wish there was more I could say to her, but I can feel my throat closing up."
    "I wonder why?..."

    scene amiani7
    with dissolve

    a "They’re really...right underneath us...aren’t they?"
    s "..."
    a "They..."
    a "..."
    a "They can’t see how tall I’ve gotten."
    s "…"

    scene amiani8
    with dissolve

    a "Mom?..."
    a "Dad?..."
    a "I’m up here..."
    a "Can you see me?..."
    a "Tell me you see me..."
    a "I...I look a lot different now."
    a "My hair has gotten really long..."
    a "Probably even longer than Mom's used to be..."
    a "Is it bad that I...can't even remember that anymore?..."
    a "Don’t you want to see it?..."
    s "Ami..."

    scene amiani9
    with dissolve

    a "Why won’t they answer me?"
    s "They can’t answer you..."
    a "But why?..."
    a "Why can I talk to them but {i}they{/i} can't answer me?..."
    a "How is that fair?..."

    scene amiani10
    with dissolve

    "I kneel down next to Ami, hoping it will prevent her from snapping in half."

    s "Because they’re gone."
    a "Gone?..."
    a "No...No, they’re right here."
    a "Don't you smell Mom’s perfume?"
    a "You always talked about how she smelled like cherry blossoms. It made Dad really angry."
    a "Don't you remember?..."
    s "Ami..."

    scene amiani11
    with dissolve

    a "Hey, say something to them...I know they'd want to hear you too..."
    a "Today’s the only day we can do this...Don’t you have {i}anything{/i} you've been wanting to tell them?"
    a "It could even be something simple, like...like how you took care of me when I got sick! Yeah...tell them that!"

    if bonus == True:
        a "Family comes first, right?...They deserve to know!"
        a "They deserve to know! So why can't they know?! Why?!"
        s "…"
    else:
        s "I am glad that your trachea healed so nicely."

    "Seeing Ami as broken as this forces me into the depressing realization that she's been suppressing this side of herself the entire time I've known her."
    "And while I know I haven’t known her all that long-"
    "That doesn't diminish what she must be going through at all."
    "She's like an entirely different person right now."

    scene amiani12
    with dissolve2

    a "Sensei, tell them-"
    s "I’ve already said everything I need to say to them."

    "My mind begins to work on its own again."
    "And my tongue moves in ways I do not understand."

    a "But you haven’t said anything! I haven't-"
    s "I talk to them every night when I lay in bed."
    s "I tell them about how proud I am of you and how quickly you’re growing up."
    s "I talk about all the fun you have at[school]...and how you’re getting good at cooking."
    s "I've even talked to them about the time you set the classroom on fire because you couldn’t figure out how to work a knob on a Bunsen burner."

    scene amiani13
    with dissolve

    a "Wha...You even told them that?! Why?! That was really embarrassing!"
    s "Because I tell them everything about you."
    s "They deserve to know, right?"
    s "And it’s my job as your guardian to make sure they get all of that information."

    scene amiani14
    with dissolve

    a "Huh?..."
    s "What's wrong?"
    a "It's just..."
    a "Why does hearing that..."
    a "Why does hearing that make me feel happy?"
    a "Today is supposed to be a sad day..."
    s "It {i}is{/i} a sad day. But that doesn’t mean there can’t be any joy at all, does it?"
    s "A wise man once said, ‘Without sorrow, there is no happiness...’ or at least something like that."
    a "Who said that?..."
    s "Some wise man. The point is, any time you’re feeling down, it’s my job to lift you back up."
    s "And if that means talking to the sky at night or quoting random wise men, so be it."
    s "I just don’t want to see you break down like this again."

    scene amiani15
    with dissolve

    a "Woah..."
    s "What?"
    a "You just...sounded really cool all of a sudden..."
    s "I’m always cool. You just haven’t realized it yet."

    scene amiani16
    with dissolve

    a "Hahahah! I guess I haven't!"

    "Ami calms down for long enough to force a smile. "
    "Or...perhaps it isn't forced at all."
    "I’m not sure how much of what I said was actually honest...but it felt honest in the moment..."
    "And that's really all I can ask for."
    "Somehow, Ami has managed to become incredibly important to me. So important that seeing her hurt like this is almost...physically painful."
    "So painful that it still hurts even when she's smiling."

    scene amiani17
    with dissolve

    a "Hey...do you want to talk to them some more? We came early, so we’ve got all day."
    s "We can do whatever you want. Just try not to cry again, okay?"

    scene amiani18
    with dissolve

    a "Mhm! Of course!"
    a "As long as you’re with me, I think I can stop myself!"
    a "Just pinch me or something if I start getting all weepy again, okay?"
    s "I'll hold you to that, Ami..."

    scene black
    with dissolve2

    "We stay at the cemetery until it gets dark."
    "Ami went back on her promise and broke down another three times."
    "On the third, I pinched her so hard that I broke skin."
    "………"
    "……"
    "…"

    scene bedroom_night
    with dissolve2

    "We made a promise on the way home to forget about today."
    "At least until next year."
    "Ami was embarrassed by how much she cried, but I never teased her for it."
    "She seems okay now, though."
    "And I’m sure she’ll be back to normal as soon as we wake up tomorrow."
    "She’s a strong girl."
    "And so I pray to the god I don’t believe in that she’s able to stay that way."

    scene black
    with dissolve2

    "{i}Congratulations! You’ve made it back to the happiest place on Earth!{/i}"

    if bonus == True:
        "{i}You are an exceptional legal guardian and your [niece] loves you very much.{/i}"
    else:
        "{i}You are an exceptional little pogchamp and your [niece] loves you very much.{/i}"

    "{i}Why have you not yet reciprocated those feelings?{/i}"
    "{i}Are you scared?{/i}"
    "{i}And if so, why?{/i}"
    "{i}Tell me all there is to know about you!{/i}"
    "{i}Tell me everything!{/i}"
    "{i}I'm so very interested!{/i}"
    "{i}...{/i}"
    "{i}Fine.{/i}"
    "{i}I'd also have a hard time responding in your shoes.{/i}"
    "{i}I'll let you sleep for now.{/i}"
    "{i}But I'll always be watching, okay?{/i}"
    "{i}Goodnight...{b}Sensei...{/b}{/i}"

    stop music fadeout 5.0
    $ renpy.end_replay()
    $ ami_love +=1
    $ day60 = True

    "{i}Your affection with Ami has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    if day == 6:
        jump advancetosun
    else:
        jump advancetomon

label swimming:
...
```

## Code that triggers this event
File: \game\AmiEvents.rpy
Code:
```python
...
"The grass, the thicket, and the fruit-tree wild;\n
    White hawthorn, and the pastoral eglantine;"

    "Fast fading violets cover'd up in leaves;\n
    And mid-May's eldest child,"

    "The coming musk-rose, full of dewy wine,\n
    The murmurous haunt of flies on summer eves."

    "..."

    "Do I wake or sleep?"

    "........."
    "......"
    "..."

    scene warble22
    with dissolve2

    a "Come on...we’re almost there."
    s "I want to feel it again. I want to feel it again. I want to feel it again."
    a "I know."
    a "Today is hard for me too."
    a "But you’ll feel better soon."
    a "I’ve got you."

    scene warble23
    with dissolve

    s "Ami?..."
    a "Mhm. I’m right here."
    a "Just keep walking, okay?"
    a "Only a few more steps to go."
    s "..."

    scene warble24
    with dissolve

    a "{i}Only a few more steps to go...{/i}"
    s "..."
    a "I’ve got you...{i}I’ve got you...{/i}"
    a "And I’ll always protect you...okay?"
    a "No matter what."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene amiani1
    with dissolve2

    "My heart aches, and a drowsy numbness pains\n
    My sense, as though of hemlock I had drunk,"

    "Or emptied some dull opiate to the drains\n
    One minute past, and Lethe-wards had sunk:"

    "'Tis not through envy of thy happy lot,\n
    But being too happy in thine happiness,—"

    "That thou, light-winged Dryad of the trees\n
    In some melodious plot"

    "Of beechen green, and shadows numberless,\n
    Singest of summer in full-throated ease."

    a "Close your eyes, Sensei."
    a "When you wake up, I’ll be right here."
    a "And the two of us will go out together."
    a "The same way we’ve done so many times before."
    a "I’ll cry...and you’ll stand tall."
    a "And when tomorrow comes, it will be like none of this ever happened."
    a "We’ll forget together."
    a "We’ll survive together."
    a "We’ll grow together."

    scene amiani2
    with dissolve

    a "I love you so much."
    a "Now..."
    a "Sleep."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ aminew2 = True
    $ ami_love += 1

    jump day60
...
```