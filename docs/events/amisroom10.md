# Something Darker
Ami event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amisroom10&go=Go)



## Event preconditions
✅Ami love greater than or equal to 10



## Next events
* [Ami: Couple's Discount](./aminew1.md)
* [Ami: No One Can See Us](./amidorm10.md)

## Event properties
* ID: amisroom10
* Group: Ami
* Triggered by label: amisroom
* Triggered by branch label: amisroom

## Event code
File: \game\AmiEvents.rpy
Code:
```python
...
label amisroom10:
    scene lr_day
    with dissolve
    play music "shiningstarvocals.mp3" fadein 4.0

    s "…"

    "I walk into the living room to be greeted by an unfamiliar, ear-piercing sound..."
    "Apparently, Ami has decided that it is acceptable to blast music in her room at 9:00 in the morning."
    "I’m already awake, so it’s not really as big of a deal as it {i}could{/i} have been...but it’s still too early to deal with something like this."

    play sound "knock.mp3"

    s "Ami...can you turn that down a little please?"
    a "Mmm mmm hmmm...mmm hmmm hmmmmmm..."

    "She either ignores or simply doesn't hear my request as she happily hums away at whatever song is playing behind the door."

    play sound "knock.mp3"

    s "Ami, come on. It's way too early for this."
    a "Hmmm hmmm hmmmm...mmm mm mm mmm mmm..."
    s "…"

    if bonus == True:
        "Is this what it means to be the guardian of a [teenage]girl?"
        "It pains me to know that there are families out there with more than one of these things."
        "Ami’s well-behaved and cute and all that, but even I don’t know if I’d be able to deal with waking up to {i}two{/i} of her."
        "Though...I guess it wouldn't be right to ignore the prospective {i}benefits{/i} of something like that as well."

        s "..."

        "You know what? Fuck it."
        "This is my house and I have the right to barge into her room if she's not going to respond to me."
        "And if the worst (or best) case scenario happens and I end up walking in on something I shouldn't see, I can always just ask for forgiveness."
        "Especially considering that asking for {i}permission{/i} was entirely fruitless."
    else:
        "Is this what it means to be a pogchamp?"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    if bonus == True:
        jump amibrax
    else:
        "I walk into Ami's room to find that she is not just humming along with some song she likes, she is the vocalist of what she refers to as the {i}best Smashmouth cover band in Kumon-mi{/i}."
        "Despite how impressed I am, I ask her to keep it down and she agrees before introducing me to all of her bandmates."
        "The next thing I know, I am decked out in their merchandise and jumping on Ami's bed."
        "Having an accountant is so fun."

        $ renpy.end_replay()
        $ amisroom10 = True
        $ ami_love += 1
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "………"
        "……"
        "…"

        jump saturdayafternoon

label amisroom15:
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
...
```