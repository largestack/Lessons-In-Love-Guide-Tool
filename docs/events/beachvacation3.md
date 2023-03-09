# My Heart is Full
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation3&go=Go)


Part of event chain [All Along the Shoreline](./beachvacation2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: beachvacation3
* Group: Main
* Triggered by label: beachvacation2

## Event code
File: \game\script.rpy
Code:
```python
...
label beachvacation3:
    scene beachinn
    with dissolve
    play sound "slidedoor.mp3"
    play music "acoustic.mp3" fadein 4.0

    "Makoto and I finish checking in at the entrance to the inn and walk into the room we’ll be staying at for the weekend."
    "Well, one of the rooms."
    "The innkeeper seemed reluctant to give up the key to the other one for some reason."
    "But that doesn’t matter."
    "What does matter is that this place is surprisingly nice."
    "It’s broken up into two separate rooms."
    "The first of which, the one we’re standing in now, is spacious enough to fit a futon for almost everyone."
    "The second, which is just beyond the sliding doors in front of us, is what I’m assuming is the bedroom."
    "I could have sworn Ayane or Ami told me something about the room having two beds, but according to the girl at the front desk, there’s only one."
    "Oh well. Not like it makes any difference to me."
    "I figure the chances are that I’ll wind up staying in the second room anyway thanks to Maya."
    "But it is what it is. "
    "I shouldn’t be complaining if I get to spend time in a place like this for free."

    scene makotoinn1
    with dissolve

    mak "Wow...this is...actually really nice."
    mak "I have to admit, I was kind of skeptical when I read some of the reviews, but I completely get it now."
    mak "It’s traditional, but not {i}too{/i} traditional. You know? It’s like...a mix."

    "Makoto’s eyes light up as she scans the room, stopping on each and every object and greeting it with a level of childish curiosity not common for someone as high-strung as her."
    "It’s one of the first times she’s looked truly happy to me."

    s "You seem to be in a good mood."

    scene makotoinn2
    with dissolve

    mak "Oh? What gave you that idea?"
    s "Your smile."
    mak "Do I not normally smile?"
    s "No, you do. Sometimes."
    s "This one is just different."

    scene makotoinn3
    with dissolve

    if bonus == True:
        mak "Maybe because I know I won’t have to spend the night selling anal beads to unattractive women."
    else:
        mak "It's probably just because I have a horrible case of depression that you won't find out about until way later on."

    s "Wow, way to ruin the moment."

    scene makotoinn4
    with dissolve

    mak "I’m kidding, of course."
    mak "I’m probably just in a good mood because I’m doing my best to forget everything for the next 48 hours or so."
    mak "Once Monday comes around, though, normal Makoto is coming back in full-swing."
    mak "I didn’t even bring a notebook with me."
    s "Woah, are you going to be okay? You’re not going to go through withdrawal, are you?"
    mak "Depends. Will you hold me if I do?"
    s "Sure. As long as no one else is around."
    mak "Then maybe~"

    scene makotoinn5
    with dissolve

    "Makoto paces around the room a few times, nearly skipping, before stopping in front of a refrigerator in the corner."

    mak "Holy crap, have you seen the fridge yet? It’s fully stocked!"
    mak "There’s even alcohol in here."
    s "You’re not planning on getting drunk, are you?"

    scene makotoinn6
    with dissolve

    mak "Depends. Will you hold me if I do?"
    s "You already used that line."
    mak "Does that make it any less cute?"
    s "It does not. And the answer stays the same. "
    s "As a responsible adult, I probably shouldn’t be letting you drink, but I’m kind of curious about what drunk-Makoto would be like."

    scene makotoinn7
    with dissolve

    mak "Probably mean. "
    mak "I’ve drunk a little with my mom before and apparently I called her a bunch of horrible names."
    mak "My dad grounded me for a week after that."
    s "A whole week? How in the world did you survive?"
    mak "Willpower, I guess. And lots of...Makoto-time."
    s "You’re going to need to explain what Makoto-time is for me. I need confirmation that it is what I think it is."

    scene makotoinn4
    with dissolve

    mak "It is. No point in hiding it anymore since I know you’re just going to keep manipulating me anyway."
    s "Manipulating you?"

    scene makotoinn7
    with dissolve

    if bonus == True:
        mak "Yeah. That thing you do where you get all perverted and force stuff out of me because you know I’m weak around you."
        s "That’s just me being me, though."
    else:
        mak "Yeah. That thing you do where you push me up against the wall and force me to give you my lunch money."
        s "That’s just plain bullying."

    mak "I know that. But it doesn’t mean you’re not manipulative. "
    mak "You know how to get what you want. "
    mak "I’m not mad about it. If anything, I should probably be learning from you."
    mak "Maybe it was your strategy all along to go from being a good[school]-teacher to a good...life-teacher or something."
    s "…"
    mak "…"
    s "Yeah, let’s go with that. That was my strategy all along."

    scene makotoinn4
    with dissolve

    mak "Heheh~ I’m sure it was."

    scene makotoinn8
    with dissolve

    "Makoto suddenly begins to walk away."

    s "Where are you going?"
    mak "The bedroom. I need to make sure everything is up to code in there."
    s "What code?..."
    mak "The Makoto-code. The one that tells me whether or not I need to go complain about stuff."
    mak "I also need to child-proof the room in case Miku gets hyper and hits her head on anything."

    scene black
    with dissolve

    "Yeah, that sounds about right."
    "Sometimes, I forget how close Makoto and Miku are."
    "Their personalities couldn’t be any further apart, so the fact that they’re like sisters is mildly confusing to me."

    scene makotoinn9
    with dissolve
    play sound "slidedoor.mp3"

    "I walk into the room to find Makoto sitting on the bed, happily bouncing up and down."

    if bonus == True:
        jump makotoinnx
    else:
        mak "Jump on the bed with me."
        s "But what if there are cameras."
        mak "Then we can sell the footage of us jumping on the bed."
        s "To who?"
        mak "Miku. She will buy it."
        s "Oh, Miku. She's so crazy."
        mak "And horrible with money. Now, quick! Jump!"

        scene black
        with dissolve2

        "I jump so high that I go into space and die."
        "Please tell Ami I love her."

        $ renpy.end_replay()
        $ makoto_love += 3
        $ beachvacation3 = True
        stop music fadeout 6.0

        "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
        "………"
        "……"
        "…"

label beachvacation4:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```