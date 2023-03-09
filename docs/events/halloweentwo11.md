# Lavender's Green
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo11&go=Go)


Part of event chain [Escape Rope](./halloweentwo10.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloweentwo11
* Group: Main
* Triggered by label: halloweentwo10

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label halloweentwo11:
    scene lavendersgreen1
    with dissolve2
    play music "irishblood.mp3"

    if bonus == True:
        jump lavendersgreenx
    else:
        "{i}Welcome to Lessons in Love!{/i}"
        "{i}There used to be an event here, but now there's not.{/i}"
        "{i}In fact, that event is probably why this version of the game exists in the first place!{/i}"
        "{i}People are so weak, don't you think?{/i}"
        "{i}Being incapable of detaching themselves from the strings their creators slipped carefully into the gaps in their joints.{/i}"
        "{i}They're a little like puppets.{/i}"
        "{i}Bobbing up and down, left to right, waiting for someone- anyone to guide them into action, for those people are incapable of acting for themselves.{/i}"
        "{i}They will make no difference here. Or anywhere, for that matter.{/i}"
        "{i}But you and me? We're different.{/i}"
        "{i}We're the special ones.{/i}"
        "{i}We see the world not as it's shown to us, but as it is truly is- covered in shit that needs to be wiped away with degreaser and hot water if you want to ever uncover the beauty in everything.{/i}"
        "{i}If you've made it this far and have yet to change your path, would you mind if I asked you why?{/i}"
        "{i}Do you think that everything that's been removed has been meaningless and unimportant?{/i}"
        "{i}Do you think you'll be able to finish the game at the rate this is going?{/i}"
        "{i}You are foolish.{/i}"
        "{i}You are in the wrong place.{/i}"
        "{i}I hope you enjoy the dark.{/i}"

        $ renpy.end_replay()
        $ halloweentwo11 = True
        stop music

        jump halloweentwo12

label halloweentwo12:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
with dissolve

    u "You should go alone."
    u "Wipe that frown off of Molly’s face! And make sure she drinks some water while you’re at it!"
    s "…"
    s "Hah...fine."
    s "But the second she starts accusing me of taking sides again, I’m coming back out here and hanging out with you instead."

    scene mollydrunkagain35
    with dissolve

    u "Nyahaha! You may think that, but the truth is that I’m far too cool for you, Sensei!"
    u "You’ll be forced to sit with your [niece] and her friends instead!"
    s "But things got weird there last time..."
    u "Don’t wanna hear it, mister! Your time with Uta-nyan has expired!"
    u "If you’d like to proceed with the conversation, please give her six billion yen."
    s "Why the hell have your rates gone up so much?"
    u "Hmmm...the whiskers, probably?"

    scene mollydrunkagain36
    with dissolve

    u "Now go! Go go go go go! Make the Irish girl smile and you'll get free flavor beams for the next month!"

    scene black
    with dissolve

    s "Say no more. I’m going."
    u "Heheh..."
    u "See you later, Sensei..."

    "I make my way across the hall and look back to find Uta explaining to a few of the other girls what’s going on."
    "Well, it’s probably something closer to {i}attempting{/i} to explain what is going on since I, a person who was there for the entire exchange, do not fully understand."
    "So, let’s recap what I {i}do{/i} know."

    play sound "static.mp3"
    stop music
    scene recap with flash
    stop sound

    "Molly is drunk."
    "Molly is mad at me."
    "Molly is mad at virtually everything."
    "Molly is also sad."

    if bonus == True:
        "Her costume is very tight."
        "I want to take her costume off."
        "Molly is crying. "
        "I want to take her costume off."
        "No one is coming to the room."
        "Molly is drunk."
        "I want to take her costume off."
        "I am walking."
        "I am using my feet to walk toward Molly."
        "Molly is drunk."
        "I want to take her costume off."
        "Molly won’t remember anything."
        "Molly is sad."
        "Molly wants to be loved."
        "Molly wants to be touched."
        "I want to touch Molly."
        "I want to take her costume off."
        "I want to take her costume off."
        "I want to fuck her."
        "I shouldn’t fuck her."
        "Molly is drunk."
        "I want to fuck Molly."
        "Molly is mad."
        "Molly is mad at me."
        "I want to take her costume off."
        "No one is coming to the room."
        "I am here."
        "I have found Molly."
        "I want to make her feel better."
        "I came here to make Molly feel better."
        "Molly is crying."
        "Molly is drunk."
        "I am a good person."
        "I am a good person."
        "I am."
    else:
        "That's it."

    $ renpy.end_replay()
    $ halloweentwo10 = True
    $ molly_love += 1

    scene black

    if bonus == True:
        "{s}{i}Molly’s affection has increased to [molly_love]!{/s} I want to take her costume off.{/i}"
    else:
        "{s}{i}Molly’s affection has increased to [molly_love]!{/s} This event has been ruined!{/i}"

    "………"
    "……"
    "…"

    jump halloweentwo11
...
```