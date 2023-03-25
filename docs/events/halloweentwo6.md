# Porcelain Labyrinth (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Conscious or Not](./amilust20.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloweentwo6
* Group: Main
* Triggered by label: amilust20x
* Chain sources: amilust20
* Chain sources path: amilust20

## Official wiki page

[Porcelain Labyrinth](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo6&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label halloweentwo6:
    "{i}Meanwhile, in the actual bathroom that Noriko ran off to...{/i}"

    scene norikobathroom1
    with dissolve2
    play music "wewereangels.mp3"

    ki "Uhh...Noriko? I don’t really wanna be a buzzkill or whatever, but this is a Halloween party and it’s prooooobably not the best time to lock yourself inside of a bathroom and cry."

    if bonus == True:
        jump norikobrx
    else:
        n "{i}*Sniff*{/i}"
        n "You're right..."

        scene black
        with dissolve2
        stop music fadeout 5.0

        "{i}Noriko and Kirin head back to the party!{/i}"
        "………"
        "……"
        "…"

        $ renpy.end_replay()
        $ halloweentwo6 = True

        jump halloweentwo7

label halloweentwo7:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
with dissolve

    a "Hah...hah...really?..."
    a "That’s all you’ve got me for me...[amimaster]?..."
    a "You can’t fuck me any harder?"
    a "After all I’ve done for you...you can’t even do that much?..."

    scene amilusttwenty34
    with fade

    s "Well if you’re actually going to challenge me, fine. "
    a "AHHH YES! IT’S SO DEEP...SO...AHH!"

    "You know, I was trying to hold back because fucking my [niece] in cosplay for {i}any{/i} amount of time is dangerous enough-"
    "But if Ami is going to egg me on and beg for more of my cock when there is plenty more to offer, fuck it. "
    "Besides, the quicker I cum, the quicker she shuts her mouth and prevents anyone wandering down one of Ayane's many hallways from finding us."

    a "AAAAAAAAAAaaaaaaaah [amimaster]...it’s...it’s throbbing...I can feel it...throbbing..."
    a "CuuuuuuUUUUUUuuUUUuuumm...I’m..................aaaAAAAAaaaAAAahhhhhhhh~"

    "Ami grabs my neck with one hand to maintain her balance while using her other one to spread apart the plump lips of her, as she called it, “perfect pussy.”"

    a "Nghhh...noooooo...mooooooOOOOooore...I can’t...[amimaster]..."
    s "Tired already? You were asking for me to go harder like one minute ago."
    a "I caaAAAAaaan’t feeeeeEEEEl...my...leeeEEEEeeeegs..."
    s "So all of that was just a bluff? How am I supposed to believe you love me if you give up this easily?"
    a "AAAAAaaaAAAaaaAAAAAaaaaaahhhhhhhhfuuuuuUUUUuuuuuuuuuUUUCK~~~~"

    scene amilusttwenty35
    with fade

    s "Oh, come on. You-"
    s "Woah. Are you okay?"
    a "AaaaaaaaaaaAAAAAAAaaaaAAAAAaaahhhhhhhhhhhh~"

    "Ami begins to go limp in my arms as I quickly (And now confusedly) continue pumping into her."

    a "[amimaster]........................co........cock......................"
    s "…"

    "I try to slow down out of sheer concern for her health, but she locks her legs around my back as if to say, “Nope. Not today.”"
    "Whether it’s a conscious decision or not, I have no idea. But I’m not about to just...stop when we’ve already come this far."

    a "Give............Ami...........................cum..................................."
    s "…"

    "I can now add “Fucked a girl so hard that she started referring to herself in third person” to my achievement list."

    a "Deep.........................er............deep..................................er...."

    scene amilusttwenty36
    with fade

    a "Yes......................yesssssssssssssss...............................cum....cuuuuuuuuuuuuuuuuuum~~~~~"

    "The only appendage now functioning in Ami’s body is her left arm as she devotes all of the energy inside of her to clinging onto me. "
    "Even the fingers she was using to spread herself apart for me have now started to twitch violently as she slips into a state I imagine is somewhere close to shock."
    "And while I’d started to feel my impending orgasm slipping away due to actual concern, I now realize that was entirely false as I can no longer contain myself and will likely not even last another ten seconds."

    a "In...............siiiiiiiiide....................................."
    a "B................ba...........bies....................................."

    "I ignore that last word and cum inside of Ami."

    with sexfade
    with sexfade
    scene amilusttwenty37
    with cumflash
    with hpunch

    a "{size=-20}aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa........................................................{/size}"

    "Ami doesn’t really make much noise as I empty myself out inside of her- just a very long-winded breath that sounds like it's the last bit of life force draining out of her body."
    "Either she was incredibly horny tonight (Which isn’t impossible given that this is Ami we’re talking about) or I am now so good at sex that I can kill people by simply having it with them."

    scene black
    with dissolve2

    "Either way, I stay with Ami in the bathroom until she regains consciousness because I am a good [uncle]."
    "Then, once she wakes up and realizes that we’re done, she gathers her things and-"

    a "[amimaster]........"
    a "One...................more time................"
    s "…"

    "Strike that."
    "Ami and I have sex one more time before she has finally had her fill."
    "{i}Then{/i} we head back to the party..."

    $ renpy.end_replay()
    $ amilust20 = True
    $ ami_lust += 3
    stop music fadeout 5.0

    "{i}Ami’s lust has increased to [ami_lust]!{/i}"
    "………"
    "……"
    "…"

    jump halloweentwo6
...
```