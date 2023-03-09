# Such Small Hands
Ami event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amisroom25&go=Go)



## Event preconditions
✅Ami love greater than or equal to 25

✅ami_virgin equal to False (unknown variable)

✅Event "[Ami: Divergence](./amidorm20.md)" is completed (event=amidorm20)



## Next events
None

## Event properties
* ID: amisroom25
* Group: Ami
* Triggered by label: amisroom
* Triggered by branch label: amisroom

## Event code
File: \game\AmiEvents.rpy
Code:
```python
...
label amisroom25:
    scene lr_day
    with dissolve
    play music "normalday.mp3"

    "I step out into the living room ready to start the day."
    "I’m immediately discouraged when I do not see breakfast on the table and decide to go back to sleep instead."

    scene black
    with dissolve

    "………"
    "……"

    scene lr_day
    with dissolve

    "Just kidding."
    "That never happens."
    "Instead, I go into the fridge and pull out a half-gallon of milk, taking a few sips directly from it because I am a man who simply can not be controlled."
    "That and I just don’t feel like making breakfast for myself."
    "Where is Ami, anyway? "
    "It’s rare that I’m up before her."
    "Could this be another opportunity to walk directly into her room without any concern for her privacy?"

    scene black
    with dissolve

    "Yes. I believe it can."

    play sound "dooropen.mp3"

    s "Ami, are you awake?"
    a "Oh, Sensei! Good morning!"

    scene amimaidsex1
    with dissolve2

    if bonus == True:
        "When I open Ami’s door, I'm hoping to find her in her underwear or something along those lines, but what I actually find is much greater."
    else:
        "I open Ami's door and prepare to hug her."

    s "Did I die and go to wherever that place people go when they die is?"
    a "There are lots of different places people think they go when they die, but you’re just in my room."
    s "I didn't even know you brought that outfit home with you."
    a "Uta found me one in my size that I stuffed into my bag before we left."
    a "What do you think? Am I adorable?"
    s "Adorable is a bit of an understatement. I’d actually appreciate it if you’d just never take this off again. "
    s "Thank you in advance for your cooperation."

    scene amimaidsex2
    with dissolve

    a "And I assume you’ll be wanting me to call you Master, too?"
    a "You know, just for practice obviously. Since I’m going to have to do a lot of that in the near future."
    s "You are forbidden from calling anyone else that name."

    scene amimaidsex3
    with dissolve

    a "Hey! {i}You’re{/i} the one who convinced me that this wasn’t a totally horrible idea, so I at least have to follow through and do it correctly."
    a "We can’t have two slackers in the house, now can we?"
    s "I guess not. Just try not to get too attached to any of the few male customers you’ll get in the future."
    s "I don’t want to wake up one day and find out that you’re moving into some random guy’s house instead of living here."

    scene amimaidsex4
    with dissolve

    a "I’d rather die than do something like that. Don’t worry."
    a "Besides, you need me in order to survive. So much so that I’m kinda worried about starting this {i}second{/i} job in the first place. "
    s "It’s fine. Like you said, I’m not normally home for most of the weekend anyway."
    s "And if I get to see you in your uniform whenever I want, this job is just as beneficial for me as it is for you."
    s "Any idea what you’re going to buy with your first paycheck?"

    scene amimaidsex5
    with dissolve

    a "Not a clue. I don’t even know what I’m getting paid yet. "
    a "Uta hasn’t told me when I’m starting either so I’m kinda just trying on the costume to see how I look and stuff today."
    a "She was definitely right about it making me feel prettier than I actually am."
    s "I mean, you’re pretty adorable to begin with. But yeah, this costume is good. I support this look."

    scene amimaidsex6
    with dissolve
    with dissolve

    a "Of course {i}you{/i} support it, Master. You and your unhealthy maid addiction."
    s "I can assure you this addiction is completely healthy for both of us. "
    a "Healthy for me? I’m gonna need you to explain why, dearest [uncle]."
    s "Why do I need to explain anything? I think our relationship has progressed enough for you to understand what that means."
    a "I have no idea what you’re talking about."
    a "I need to be a tsundere maid now, remember? I don't even like you that much."
    s "Tsundere Ami makes me feel weird. Dote on me more."

    scene amimaidsex7
    with dissolve

    a "Now why on earth would I do that? I have the upper hand here, Sensei~"
    a "I know how much you want to hug me and coddle me and keep me all to yourself right now and I-"

    if bonus == True:
        jump amisroom25x
    else:
        scene black
        with dissolve2

        "I seize the opporunity to hug Ami."
        "She enjoys the hug because hugs are good. The end."

        $ renpy.end_replay()
        $ amisroom25 = True
        $ ami_love += 3
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "………"
        "……"
        "…"

        jump saturdayafternoon

label amiinvite1:
...
```

## Code that triggers this event
File: \game\AmiEvents.rpy
Code:
```python
...
label amisroom:
    if ami_love >= 0 and firsttimeamisroom == False:
        jump firsttimeamisroom
    if ami_love >= 5 and amisroom5 == False:
        jump amisroom5
    if ami_love >= 10 and amisroom10 == False:
        jump amisroom10
    if ami_love >= 15 and amidorm15 == True and amisroom15 == False:
        jump amisroom15
    if ami_love >= 20 and beachvacation16 == True and mayadorm25 == True and amisroom20 == False:
        jump amisroom20
    if ami_love >= 25 and ami_virgin == False and amidorm20 == True and amisroom25 == False:
        jump amisroom25
...
```