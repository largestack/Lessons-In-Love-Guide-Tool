# How I Feel (Happy scenes)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: howifeel
* Group: Happy scenes
* Triggered by label: shrine
* Triggered by branch label: shrine
* Triggered by path: shrine->howifeel

## Official wiki page

[How I Feel](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=howifeel&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label howifeel:
    play sound "static.mp3"
    scene happy4
    with flash
    scene happy7
    with flash
    scene whythesky
    with flash
    scene howifeel0
    stop sound
    play music "hope.mp3"

    "A deep rumbling sound crawls into my ears and begins to violate my insides."

    if bonus == True:
        "It churns them, as if I’m being sodomized by the whispers of demons."
        "The noise turns my blood to semen and, within a matter of minutes, my organs cease to function."
    else:
        "It churns them. Kind of like butter, but also kind of not like that."
        "The noise turns my blood to strawberry juice and, within a matter of minutes, my organs cease to function."

    "Just kidding."
    "This doesn’t happen."
    "I feel fine."
    "How do you feel?"

    menu:
        "Me?":
            "Yes, you."

    "I’m talking to you."
    "I can see you. Just as you see me."
    "We all see each other."
    "But, for some reason, we can’t see what matters most."

    menu:
        "What matters most?":
            "God, of course."
            "Without him, you and I wouldn’t be here."

    "But he’s dead now."
    "Such a tragedy!"
    "Who else will we pray to?"
    "Who else will we call upon when our loved ones are on their death beds?"
    "Who else will we ask to forgive us of our misdeeds in exchange for momentary salvation?"
    "“Please, God! I will never sin again if you just X!”"
    "And so he X."
    "And you continue to sin."
    "Why do you lie?"

    play sound "static.mp3"
    scene friends1
    with flash
    stop sound

    a1 "We lie because it makes things easier!"
    a1 "What is the point of living if we need to follow rules?"

    play sound "static.mp3"
    scene howifeel1
    with flash
    stop sound

    a2 "Yes! Yes! Rules are bad!"
    a2 "We lie because it feels good!"
    a2 "Throw yourself into the wishing well!"
    a2 "The happiest place in the world!"
    a1 "Rejoice! We are finally free!"

    "Two angels appear before me. Their voices remind me of a long lost friend."
    "Her name begins with the letter T."

    six "こんにちは"
    s "Oh. You’re here too?"
    a1 "She has always been here! Truly a wonderful girl!"
    a2 "Yes! Yes! A normal [teenage]girl!"
    six "普通の女子高生。"
    s "Do you need help?"
    six "Do you?"
    six "You are the one who stumbled in here by mistake."
    six "Unless-"
    six "You came to pray?"
    a2 "No, mistakes! No! He has come with ill intent!"
    a1 "Yes! Yes! He is here for forgiveness!"
    s "Forgiveness? But I haven’t done anything wrong."

    if amifingered == True and bonus == True:
        a1 "Incest! He commits [incest]! A sin!"
        a2 "Horrible!"
        a1 "Castration!"
        a2 "Crucify the sinner!"
        a1 "{s}sssssssssssssssssssssssssssssssssssssssssssss{/s}"
        a2 "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"

    elif amifingered == True and bonus == False:
        a1 "He hugs his [niece] and thinks we do not see!"
        a2 "Horrible!"
        a1 "Hugs are bad!"
        a2 "Crucify the sinner!"
        a1 "{s}sssssssssssssssssssssssssssssssssssssssssssss{/s}"
        a2 "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"
        s "This seems like a dramatic overreaction to a hug."

    else:
        a1 "Rebirth is a sin!"
        a2 "Suicide is a sin!"
        a1 "Remove his arms!"
        a2 "Feed him to 望む!"
        a1 "Yes! Yes! Then he can be forgiven!"
        a1 "{s}sssssssssssssssssssssssssssssssssssssssssssss{/s}"
        a2 "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"

    "The two angels let loose a series of {s}horrible{/s} heavenly noises."
    "One hisses while the other chatters his teeth."
    "All the while, a biomechanical machine stirs in the background."

    if bonus == True:
        "Its tendrils plug the insides of a girl I can not see. I can only guess who it is."

    six "Don’t worry about me."
    six "I have been through much worse than this."
    six "あなたなしで毎日。。。"
    a1 "The girl cries!"
    a2 "Coward!"
    a1 "She wants to go home!"
    a2 "Coward!"

    "They mention her crying, but her voice is steady and unshaken."
    "Which is surprising because, from here, it appears that her organs are being
    dematerialized."
    "How can such a small body curve around and envelop such a horrible thing?"

    if bonus == True:
        a1 "The man becomes aroused!"
        a2 "He wants to fuck the girl!"
        six "Is..."
        six "Is this true?..."
        six "You still want to fuck me?"
        six "After all you’ve seen?"
    else:
        a1 "He wants to hug her!"
        a2 "Perhaps the hug would make her feel better!"
        s "dfhgudfhsuidfhuashdshdfugsdifgh"

    "My mouth fills with blood and I’m unable to respond."
    "Slowly and painfully, I can feel my teeth beginning to liquify."
    "Everything spills out of my mouth at once."

    a1 "Hahahahahahahahaha!"
    a2 "笑笑笑笑笑笑笑笑笑笑笑笑笑笑笑笑!"

    if bonus == True:
        "The angels laugh at me as the girl in the machine is ruthlessly violated."

    "I try to move but, once again, I find myself strapped to a chair."

    six "…"

    if bonus == True:
        six "I guess you don’t want to fuck me after all."
    else:
        six "I guess you don’t want to hug me after all."

    six "That makes sense."
    six "I’m sorry for asking."
    a1 "Hahahahahah! Truly a tragedy!"

    if bonus == True:
        a2 "Yes! Yes! Cucked by a machine! Such a weak human!"

    play sound "static.mp3"
    scene warning2
    with flash
    stop sound

    "For a moment, I remember this is all a game."

    if bonus == True:
        jump howifeelx
    else:
        scene black
        with dissolve
        stop music fadeout 5.0

        "So I decide to exit out of it because this game is too scary and I didn't realize it was horror when I downloaded it."
        "There was also this weird white thing with crazy eyes that may or may not show up again later. I don't really know."

        $ renpy.end_replay()
        $ howifeeltrack = True
        $ howifeel = False
        $ maya_love += 1

        "{s}Maya’s affection has increased to [maya_love]!{/s}"
        "………"
        "……"
        "…"

        jump saturdaynight

label day63:
...
```

## Code that triggers this event

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label shrine:
    if howifeel == True:
        jump howifeel
...
```