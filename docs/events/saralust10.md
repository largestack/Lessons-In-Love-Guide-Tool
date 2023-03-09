# Medical Assistance
Sara event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=saralust10&go=Go)


Part of event chain [Once, Twice, Ten Times](./halloween7.md)

## Event preconditions
❌Sara lust less than 10



## Next events
None

## Event properties
* ID: saralust10
* Group: Sara
* Triggered by label: halloween7

## Event code
File: \game\script.rpy
Code:
```python
...
label saralust10:
    if bonus == True:
        jump saralust10x
    else:
        "Just kidding. None of that ever happens."
        "Sara and I spend the next two hours watching the critically acclaimed animated film {i}Shrek 2{/i} and spend the rest of the night discussing how silly the donkey is."
        "We also eat ice cream and have a good time."
        "After that, I tell her she's pretty cool and decide to leave."

        $ renpy.end_replay()
        $ sara_lust += 1
        $ saralust10 = True

        "{i}Sara’s lust has increased to [sara_lust]!{/i}"
        "………"
        "……"
        "…"

        jump halloween8

label halloween8:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
maki "Oh, you’d get behind it alright. Not sure you’d be able to handle what comes next, though."
        h "Maki...are you sure you’re not drunk?"
        maki "Who knows? I do feel pretty good right now."
        maki "But then again, that might just be because I have a cute catgirl on my shoulder."

        scene milfparty22
        with dissolve

        maki "Are you sure you feel okay, though? Your boobs are being like, completely suffocated by your costume."
        h "That’s my fault for trying to fit into a smaller size..."
        sar "She does this every year and always complains about it. I’ve just accepted it as part of Halloween at this point."
        sar "Come to think of it, mine feels a little tight too."
        sar "Maybe if I just..."

        scene milfparty23
        with dissolve

        sar "There. That feels better."

        "Sara suddenly unbuttons her nurse outfit and exposes her chest right next to Maki and Haruka, who seem too wrapped up in each other to pay it any mind."

        sar "Ah- Sensei! Where are you looking?"
        s "Where do you think I’m looking?"
        sar "Why, at a beautiful woman, of course~"
        sar "I even bought a new bra to go along with my costume. Cute, right?"
        sar "But wouldn’t it look even better on the floor of my bedroom?"
        s "Can I take that as the cue for being invited upstairs?"
        s "Because I honestly don’t know how much more of this sight I can handle."

        "Sara looks at me in silence for a moment as Haruka and Maki fall deeper into each other’s eyes."

        scene milfparty24
        with dissolve

        sar "Hey, do either of you two mind if Sensei and I disappear for a bit?"
        h "Hey, are you trying to pull me closer right now?"
        h "I might be drunk but I’m not {i}that{/i} drunk yet."
        maki "Hm? Why on earth would I try to pull you closer? What are you insinuating, Haru?"

        scene milfparty25
        with dissolve

        sar "Yeah, I don’t even think they’ll see us leave."
        s "Fine by me. Lead the way."
        sar "What, you’re not going to carry me up the stairs?"
        s "You’re the nurse. You’re the one supposed to be caring for me, remember?"

        scene milfparty26
        with dissolve

        sar "Oh, I’ll care for you alright."
        sar "I just need to make sure I can safely get up the stairs first."
        s "Any thoughts on inviting the cats as well?"
        sar "Sorry, Sensei~ Animals aren’t allowed in the hospital. "
        s "That’s a stupid rule. Animals should always be allowed in the hospital."
        sar "Maybe another night~ I want you all to myself this time."
        sar "Besides, those two are probably going to start making out soon anyway."
        s "Then...can we stay and watch?"
        sar "If we stay any longer, I might pass out."
        sar "It’s now or never~"
        s "Well then I obviously pick now. But I think we might wind up missing out on something pretty great, to tell you the truth. "
        sar "Now is an excellent choice..."

        scene black
        with dissolve2
    else:
        s "Of course. They're extremely important in the medical field."

        scene black
        with dissolve

        s "Now, if you'll please excuse me, I am going to close my eyes. This is getting a bit too saucy for my liking."
        sar "HAHA! YOU HAVE LET YOUR GUARD DOWN!"
        s "What? No-"


    sar "We’ll be back later, you two! "
    sar "Enjoy your couch!"

    "Sara hobbles over to me and pulls me by the wrist with what little strength she’s able to get out of her intoxicated body."

    if bonus == True:
        "She doesn’t even bother buttoning her shirt back up because, at this point, it would just be creating one more step on our way to what I imagine will be kinky Halloween sex."
        "Sure, I wish the other two could have gotten involved as well, but I’m not going to cry about {i}only{/i} getting into bed with a sexy nurse."

    stop music fadeout 10.0

    "We finally make it up the stairs after a bit of a struggle from Sara in maintaining her balance."
    "But once we’re in the apartment, she slams me up against the door and passionately kisses me before throwing it open so hard it almost puts a hole in her wall."
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ halloween7 = True

    if sara_lust < 10:
        jump saralust10skip
    else:
        jump saralust10
...
```