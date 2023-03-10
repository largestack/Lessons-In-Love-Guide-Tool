# First Hunt (Chika)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [A Trip to the Moon](./chikainvite1.md) (Chika) is completed)

* Event [Detention](./day139.md) (Chika) is completed)

* chikanumber equal to True (unknown variable)



## Next events

None

## Event properties

* Id: chikainvite2
* Group: Chika
* Triggered by label: chikainvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->chikainvite->chikainvite2

## Official wiki page

[First Hunt](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikainvite2&go=Go) for more details.

## Event code

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label chikainvite2:
    play sound "phonebeep.wav"

    "I tap on Chika’s name in my phone and wait for her to answer."
    "Ami told me earlier in the day that she’d be hanging out at the dorm with some of the other girls tonight so, assuming Chika isn’t one of them, the two of us might actually be able to be alone for a while."

    play sound "phonebeep.wav"
    scene noonsky
    with dissolve

    c "Hihi~ Chika’s phone, this is Chika speaking!"
    s "Strange way to answer the phone but hey."
    c "Hey~"
    c "I miss you."
    s "You could always text me if you miss me, you know. You’re always on your phone anyway."
    c "I need to restrain myself or you’ll think I’m needy."
    s "I wouldn’t really care either way."
    c "Then can I come bother you at your house tonight? I just saw Ami and some of the others down the hall, so you should be alone, right?"
    s "Funny you mention that because that’s actually why I was calling."
    c "Well I’m glad we’re on the same page!"
    c "Should I head over now?"
    s "Sure. You remember how to get there, right?"
    c "Obvs. I still have your message with your address in it anyway. "
    c "I’ll be there soon!"
    s "Cool. See you then."

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 5.0

    "I hang up the phone and slide it back into my pocket, only to have it vibrate seconds later."
    "When I pull it back out to check again, all I see is a heart emoji sent by none other than Chika Chosokabe."
    "………"
    "……"
    play sound "doorbell.mp3"
    "…"

    scene chikasecondvisit1
    with dissolve
    play music "asobeatsex5.mp3" fadein 8.0

    "Chika walks in when I give her the go-ahead and kicks her heels off at the door before skipping her way over to me."

    c "You have no idea how glad I am to not have to act this time."
    c "Ami’s cute, but that girl’s a friggin’ hawk when it comes to you."
    c "I felt like she was analyzing every single thing I said to try and frame me somehow or another."
    s "Probably because she was. She tends to do that."
    c "Guess I can’t blame her for being a little overprotective of her super-cool [uncle]."

    scene chikasecondvisit2
    with dissolve

    c "I’ve got ya all to myself this time, though. So here’s hoping we can make it at least a few hours without being interrupted."
    s "I have a feeling Ami will be gone for quite some time, so I wouldn’t worry too much about any interruptions."
    c "Heheh~ Good."

    scene chikasecondvisit3
    with dissolve

    c "It’s like...a completely different feeling being alone in here with you. I feel...weirdly special all of a sudden."
    s "Do I not normally make you feel special?"
    c "I never said that. You make me feel special all the time. This just feels a lot more...real."

    if bonus == True:
        c "Like we’ve taken it a step further than just messing around in my dorm and stuff."

    scene chikasecondvisit4
    with dissolve

    c "I almost want to suggest that the two of us just hang out and cuddle or something but I’m pretty sure I already hinted something a little special to make up for my last visit."

    if bonus == False:
        s "I hope it is a hug."

    c "It would be quite rude to only cuddle when you’re probably expecting me to go the extra mile, right?"

    if bonus == False:
        s "No. That would be great, actually."
    else:
        s "Wow, it’s almost like you understand me or something."

    scene chikasecondvisit5
    with dissolve

    c "I live to please~"
    c "Besides, I’m excited too. My heart was racing the whole way here."
    c "And now that we’re alone, I kinda just want to squeeze you until you explode. Is that weird?"

    if bonus == True:
        s "I can’t tell if you mean literally squeezing me or if that was a euphemism for jerking me off."
        c "Would the answer to that change your response?"
        s "Uhh, kind of. Yeah."
        c "I meant literally squeezing {i}you{/i} but I guess I’d also be okay with jerking you off if that’s what you want."
        c "Unless you maybe want me to do something else this time?~"
        s "What else did you have in mind? I’m open to suggestions."

        jump chikasecondinvx
    else:
        s "No. Begin the hugging."

        scene black
        with dissolve

        "Chika and I hug for a really long time."
        "She is pretty good at it, but I think I'm a little better."

        $ renpy.end_replay()
        $ chikainvite2 = True
        $ chika_lust += 3
        stop music fadeout 5.0

        "{i}Chika’s lust has increased to [chika_lust]!{/i}"
        "{i}You can now choose between affection and hugs when inviting her over!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label chikainviteaff:
    scene chikainvitegen
    with fade

    "Chika and I spend the night eating junk food and asking each other questions about things we'd like to know about one another."
    "She has a lot more questions than I do."
    "Real questions. Big ones...like 'What did you want to be when you grew up' or 'Do you ever want to get married?'"
    "I have a hard time finding answers to all of them, to be honest."
    "But even when that happens, it doesn't faze her one bit."
    "In between the barrage of questions, she wastes no time in reaching her feet out underneath the table and playfully poking and kicking me with them."
    "She smiles the entire night. Even when nothing is happening."
    "I wish I could do that."
    "I have a hard enough time smiling even when good things happen."

    scene black
    with dissolve

    "If I was any good at smiling, I'd smile back at her."
    "But, being the person I am, I sit back and let her continue to play one-sided footsie with me as I finish off the last of the french fries on the table."
    "Eventually, Chika moves to my side and rests her head on my shoulder."
    "She tells me about her dreams. How {i}she{/i} wants to get married."
    "And how some day, in the distant future, she'd like to eat junk food and play question-games with someone who will look only at her."
    "She smiles one last time."
    "And then she leaves."

    $ chika_love += 3
    stop music fadeout 5.0

    "{i}Chika's affection has increased to [chika_love]!{/i}"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label chikainvitelicking:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump chikainvitelickingx
    else:
        $ chika_lust += 3
        stop music fadeout 5.0

        "{i}Chika's lust has increased to [chika_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label chikainvitehandjob:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    if bonus == True:
        jump chikainvitehandjobx
    else:
        $ chika_lust += 3
        stop music fadeout 5.0

        "{i}Chika's lust has increased to [chika_lust]!{/i}"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label day272:
    scene chikaonseninv1
    with fade
    play music "normalday.mp3"

    c "Oh, hey! Fancy meeting you here!"
    c "Do...um...do you have a sec?"

    "I wind up running into Chika between classes."
    "And by “running into” I mean that I’m pretty sure she’s been following me around every time I leave the classroom today."

    s "Depends. "
    s "Are you trying to extort me?"
    c "What...would I be trying to extort you for?"
    s "I don't know. But you’ve been following me around all day, haven’t you?"
    s "What’s going on?"

    scene chikaonseninv2
    with dissolve

    c "Not all day! Just like, three times!"
    s "Spit it out, Chika. I am a very busy man."
    c "I...um..."

    scene chikaonseninv3
    with dissolve

    c "I wanted to show you these..."
    s "Cool."
    s "What are they?"
    c "I umm..."
    c "So, there’s this radio show I listen to with Chinami in the morning...and they were doing this thing where the 23rd caller wins a prize..."
    c "Sooo...I somehow wound up winning two tickets to some like, super nice hot spring at the edge of town."

    scene chikaonseninv4
    with dissolve

    c "Would you...you know..."
    c "Wanna come with me?"
    s "Me? You don’t want to take Yumi or Chinami?"
    c "I’d rather go with you..."
    c "But if you think it’s weird to go on a random one night vacation with a cute girl who follows you around in the hallway, that’s fine. "
    c "I’ll just go cry in the bathroom."
    s "Of course I’ll go."

    scene chikaonseninv5
    with dissolve

    c "Really?! You will?!"
    s "Sure. Why would I say no to a free vacation with a cute girl?"

    scene chikaonseninv6
    with dissolve

    c "I don’t know. Cause it’s like, super random and the middle of winter?"
    s "The middle of the winter is the best time to go to a hot spring."
    s "When are we supposed to be there?"
    c "The tickets don’t have an expiration date so we can kinda just go whenever we want I guess."
    c "Just call me in the morning whenever you’re ready and I’ll find someone to cover my shift or something."
    s "Is that really okay?"

    scene chikaonseninv7
    with dissolve

    c "Probably not, but I’m a [teenage]girl and I’m sure they'll understand if it’s for a trip with my boyfriend."

    scene chikaonseninv8
    with hpunch

    c "Ah! Forget I said that! I didn’t just call you what you think I called you!"
    s "…"
    c "I’m gonna go!"
    c "Umm...call me!"

    scene chikaonseninv9
    with dissolve

    "Chika darts down the hallway and I now have to figure out if being called her boyfriend is potentially troublesome or not."
    "But hey, at least I get to spend a whole day off with her soon. "
    "And I don’t even have to pay."

    $ onseninvite = True
    $ onsenticket = True

    "{i}Congratulations! You can now go on a special trip with Chika!{/i}"
    "{i}Things like this might happen every once in a while because you’re a super awesome, super likable guy who lights up the room just by walking in.{/i}"
    "{i}To go on this trip, call Chika in the morning.{/i}"
    "{i}But, before that, you might want to pay her roommate a visit.{/i}"

    scene black
    with dissolve
    stop music fadeout 5.0

    "………"
    "……"
    "…"

    jump afterschoolevent

label chikaonsen1:
...
```

## Code that triggers this event

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label chikainvite:
    if chikainvite1 == False:
        jump chikainvite1
    if chikainvite1 == True and chikainvite2 == False:
        jump chikainvite2
...
```