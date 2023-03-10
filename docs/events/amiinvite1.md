# Living (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md) (Main) is completed)



## Next events

* [Ami: Rising to the Challenge](./amiinvite2.md)

## Event properties

* Id: amiinvite1
* Group: Ami
* Triggered by label: amiinvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->amiinvite->amiinvite1

## Official wiki page

[Living](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amiinvite1&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amiinvite1:
    play sound "phonebeep.wav"

    "I tap on Ami’s name in my phone and wait for her to answer."
    "I’m feeling a bit out of it today, so it would probably be nice to just lounge around the house with her."
    "Plus, something like this is definitely easier and significantly less risky than inviting anyone else over."
    "Slightly strange, considering that she lives {i}with{/i} me and inviting her to her own house is conceptually weird-"
    "But yeah, definitely easier."

    if invitetip == False:
        call invitetip from _call_invitetip_3

    play sound "phonebeep.wav"

    a "Hello? [amimaster]? What’s up?"
    a "Did you need something?"
    s "Hey, Ami. Are you doing anything today?"
    a "Hm? I’m just making dinner right now. Are you coming home early?"
    a "Want me to save you some?"
    s "Actually, I was wondering if you’d want to come over today."
    a "…"
    s "…"
    a "Come over where?"
    s "Come over our house."
    a "You’re...inviting me to...our house?"
    a "But I...just told you I'm here."
    a "Are you okay? Did you hit your head somewhere?!"
    a "Hold on, [amimaster]! I’ll call an ambulance!"
    s "No ambulance needed. "
    s "I just wanted to make sure you were okay with visiting your own house."
    a "The ambulance is on the way, [amimaster]! Just hold on!"

    scene black
    with dissolve

    "I manage to convince Ami to call off the ambulance as I walk home."
    "Thankfully, we don’t live in the US and thus incur no additional fees after she has one dispatched."

    play sound "phonebeep.wav"

    "I end the phone call as I make my way to the door, sliding my cell back into my pocket as I turn the handle."

    play sound "dooropen.mp3"
    stop music fadeout 15.0

    "Ami greets me with a hug and sets out a plate for me on the table that I promptly devour."
    "Once she finishes hers (Which takes exponentially longer- that girl eats very slowly), we make our way into {i}my{/i} room for once."
    "Typically, if the two of us were going to hang out, it would be in either the living room or, in some rare cases, her room."
    "So having her in here is actually kind of odd now that I think about it."

    scene amifirstinvite1
    with dissolve2
    play music "acoustic.mp3" fadein 5.0

    a "Wow...I can’t even remember the last time I was in here."
    s "Probably the last time you had to come wake me up or clean my room."
    a "Besides those times, obviously. "
    a "I mean just...hanging out in here."
    a "You’ve been getting better at waking up when I call out to you anyway. There’s barely a reason for me to actually come in anymore."
    a "So...why are we in here today?"

    if ami_virgin == False:
        a "Sexy stuff?"
        s "Surprisingly, no."

    s "I’ve been feeling really tired all day, so I kind of wanted to just relax and hang out with my one and only [niece]."
    a "Why are you specifying that I’m your one and only [niece]? Wording it like that makes me think you’re hiding something."
    a "[amimaster], if you’re hiding any extra [niece]s from me, I {i}will{/i} destroy them. I want you to know that."
    s "Yeah, that’s...not a thing you need to worry about."

    scene amifirstinvite2
    with dissolve

    if ami_virgin == False:
        a "Hooray! Now I know your [incest] fetish is specific to me and me only!"
    else:
        a "Hooray! Now I don’t have to worry about anyone taking you from me!"

    s "Calm down, Ami."
    s "What you and I have together is special."
    s "There's no one who could ever take your place."

    scene amifirstinvite3
    with dissolve

    a "Okay, something’s going on, isn’t it?"
    a "First, you come home on time. Then you take me into your room...and {i}now{/i} you’re saying adorable stuff to me."
    a "Is everything okay, [amimaster]? I don’t know if the ambulance made it back to the hospital yet, but-"
    s "Again, I’m okay. Stop threatening to call ambulances each time I act out of character."
    a "Sorry. I’ve just gotten so used to you neglecting me lately that the sudden increase in attention is making me nervous."
    a "Like you’re about to break some bad news to me or something."
    s "Actually, now that you mention it, I do have some bad news."

    scene amifirstinvite4
    with dissolve

    a "Ah! Here it comes! I thought I was ready but I’m really not!"
    s "You, see Ami...I-"

    if bonus == True:
        a "You {i}do{/i} have hidden family members you never told me about, don’t you?!"
    else:
        a "You {i}do{/i} have other accountants, don’t you?!"

    a "How many of them have twintails?! "
    a "Tell me or I’ll kill myself!"
    s "I was just going to say my legs are tired from walking all the way home and that I want to sit down."

    scene amifirstinvite5
    with dissolve

    a "Oh."
    a "Your definition of “bad news” is a lot different from mine."
    s "I can see that."

    scene amifirstinvite6
    with dissolve

    a "How’s that even bad, [amimaster]? "
    s "You had just gotten so into voicing your concern for me that I felt a little bad about having to interrupt you."
    s "But if you’d like to keep talking about how awesome I am, feel free. I’m just going to sit down for it."

    scene amifirstinvite2
    with dissolve

    a "Then I’ll sit down with you! I’m not just gonna stand here and keep shouting across the room. That would be weird."
    a "In fact, I’m gonna get all up in your space and rub up against you to mark my territory."
    s "Are you an animal now?"

    scene amifirstinvite7
    with dissolve

    a "Do you have a purrrrrroblem with that, [amimaster]?~"
    s "Not as long as I can feed you out of a bowl and keep you up to date on your shots."
    a "Heheh, I knew you’d li-"

    scene amifirstinvite8
    with dissolve

    a "Wait, why is {i}that{/i} the first thing your mind went to? Don’t you wanna pet me or scratch my chin or something?"
    s "Once I confirm you’re properly vaccinated, of course."
    a "…"
    s "…"
    a "Just go sit down, already. Clearly the cat thing isn’t something you’re interested in right now."

    scene black
    with dissolve

    "Ami follows me as I make my way to the bed, waiting for me to sit down before-"

    a "Move your legs a little."
    s "What, why?"
    a "I said move ‘em, mister!"
    a "Here, I’ll do it for you-"
    "………"
    "……"
    "…"

    scene amifirstinvite9
    with dissolve

    a "Welp, this is better than nothing, I guess."
    a "So, where were we?"
    a "You were talking about how much you love me, right?"
    s "That is not a thing I have said even once today."
    a "Are you sure? I distinctly heard an “I love you, Ami” as soon as you came home tonight."
    s "Probably just the voices inside of your head or something."
    a "I don’t think so. Those are a lot less reserved."
    s "Wait, you don’t actually have-"
    a "Hey, [amimaster]...do you remember how this room used to look before I moved in?"

    "I can’t even remember my name, let alone something that happened before I “existed” here."

    s "I can’t say I do."
    a "Really? "
    a "I guess that makes sense, though. "
    a "You were a lot different back then. A lot more...spacious?"
    s "Are you calling me fat?"
    a "No, no. What’s the word for when somebody like, wanders around and doesn’t really have any idea what they’re doing and stuff?"
    s "Oh. I think you’re thinking of “spaced out.”"

    scene amifirstinvite10
    with dissolve

    a "Yeah, yeah! That!"
    a "You were always super spaced out. To the point where you’d have food from like, weeks ago still out on your desk and bottles all over the floor and stuff."

    scene amifirstinvite11
    with dissolve

    a "But you weren’t exactly in the best state of mind back then. And, to be fair, neither was I."
    a "We were both really lazy for way longer than we ever should have been."
    a "I guess it’s kind of good that we wound up breaking each other out of it, huh?"
    a "Imagine how things would be if the house was still like that?"
    a "Filled with rotting food and discarded tissues from all of our tears..."
    a "Well, my tissues were from tears. Yours were probably from a few things."
    s "This conversation went from sentimental and cute to mildly disturbing within a matter of seconds."

    scene amifirstinvite12
    with dissolve

    a "Heheh~ You’re a growing boy, [amimaster]. Things like that are natural."

    if ami_virgin == False:
        a "You never would have needed all of those tissues if you’d have just pounced on me earlier, though."
        a "That would have snapped me out of my slump, {i}really{/i} quick. Like pressing a reset button."

    s "Okay, well, on a slightly different note, I’m glad that things aren’t like that anymore."
    s "I don’t think I’d be able to live if the house was that filthy."

    scene amifirstinvite13
    with dissolve

    a "What we were doing back then could barely be called “living” anyway. "
    a "We were kinda just drifting along from one day to the next, surviving off of garlic bread and soda."
    s "So I {i}was{/i} spacious after all..."

    scene amifirstinvite12
    with dissolve

    a "Hahaha~ Maybe a teensy bit."
    a "But now you’re big and strong and can protect me if I ever get attacked by a rottweiler."
    s "You say some really strange things sometimes, you know?"

    scene amifirstinvite14
    stop music

    a "61 6c 62 61 74 72 6f 73 73"

    "///////////////////////////////////////////CONNECTION WEAK"
    "///////////////////////////////////////////PLEASE MAKE SURE ALL WIRES ARE PROPERLY CONNECTED"
    "///////////////////////////////////////////……………………………"
    "///////////////////////////////////////////ATTEMPTING TO RESTORE CONNECTION"
    "///////////////////////////////////////////……………………………"
    "///////////////////////////////////////////……………………………"
    "///////////////////////////////////////////TESTING CONNECTION"
    "///////////////////////////////////////////3"
    "///////////////////////////////////////////2"
    "///////////////////////////////////////////1"
    "///////////////////////////////////////////……………………………"
    "///////////////////////////////////////////CONNECTION RESTORED"

    scene amifirstinvite13
    play music "acoustic.mp3"

    a "I’m not the only one who says strange things, [amimaster]."
    a "Like, remember how you fell asleep in the classroom a few months ago and didn’t even know who I was when you woke up?"
    a "What was up with that?"
    a "It’s like you were a different person all of a sudden."

    "What Ami still doesn’t understand is that I {i}was{/i} a different person all of a sudden."
    "My life changed dramatically that day."
    "Just as hers did when her parents were turned into a roadside sculpture of steel and shattered bones."
    "Life changes for everyone."
    "Sometimes, you grow fat and pace around your room for months on end as a result."
    "You leave food out on your desk."
    "Flies find it and lay eggs."
    "The eggs hatch."

    if bonus == True:
        "Then, before long, maggots consume everything as your traumatized [niece] finds new ways to please herself on the opposite end of the house."
        "Anything to distract from the pain."
        "That is all life is and that is all we are."
    else:
        "But surprise! Chickens come out! There were never any fleas at all!"

    scene amifirstinvite15
    with dissolve

    a "Mm..."
    a "I’m feeling really tired now that I get to lay like this, [amimaster]."
    s "Really? It doesn’t seem like a very comfortable position."
    a "Any position is fine as long as you’re with me."
    a "I could probably sleep standing up as long as you’re in the same room."
    a "But, then again, I’m also kind of crazy for you, so that might just be a special thing only I would be able to do."
    a "Do I make you comfortable as well, [amimaster]?"
    s "Of course."
    a "Really?"

    if ami_virgin == True:
        if bonus == True:
            a "Then how come you won’t finger me?"
            a "Is it because we’re family?"
            a "Does that make it a problem for you?"
            a "I think it’s okay for family members to help each other out like that, [amimaster]."
            a "In fact, I don’t think there’s anyone else in the world who I’d rather have fuck me from dawn ‘til dusk."
            s "...Ami, I-"
        else:
            a "Then how come you won’t hug me?"
            a "Is it because we have a mature business relationship?"
            s "...Ami, I-"

        scene amifirstinvite16
        with dissolve

        a "Ahhh~ I’m feeling really tired all of a sudden."
        a "It’s okay if I sleep here, right?"
        a "Wake me up in a few hours if you want dessert or something."
        a "I picked up a cake on the way home today."
        a "Goodnight, [amimaster]~ "
        a "I love you~"

        scene black
        with dissolve2

        s "…"
        s "I love you too..."

        if bonus == True:
            "I’m not sure what that little outburst was about, but-"
            "Well, actually-"
            "Correction: I {i}am{/i} sure of what that little outburst was about."
            "But I’ve already decided that I won’t be pursuing a relationship like that with Ami."
            "And even if that’s what she wants, I can’t possibly bring myself to defile her that way."
            "So, it will probably be best for everyone if she continues to keep her feelings for me private."
            "There’s no way it would ever work out between us if others caught wind of anything more than how we’re {i}supposed{/i} to be..."
        else:
            "{i}As an accountant...{/i}"

        $ renpy.end_replay()
        $ amiinvite1 = True
        $ ami_love += 3
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "{i}You can now invite her over to her own house every night if you’d like!{/i}"

        if bonus == True:
            "{i}Normally, you’d also get the option to do all kinds of sexual stuff with her, but it appears you made a mistake somewhere, so that part won’t happen!{/i}"
            "{i}Imagine having morals in a place like this.{/i}"

        $ amiinvite2miss = True

        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

    else:
        a "That makes me really happy."
        a "The fact that the two of us can be ourselves together now..."
        a "It’s unlike anything I would have ever wished for."
        a "I’ll admit, even though it was super weird, my heart skipped a beat when you “invited me over” today."
        a "It was almost like being asked out on a date- just the date was to your room and all we did was talk."
        a "But I got to lay on my favorite bed in the whole wide world with my favorite man in the whole wide world."
        a "And there’s nothing else that I’d have rather done."
        a "Stay with me forever, [amimaster]."
        a "Stay with me forever and I’ll make you happier than anyone has ever made anyone in the history of the universe."

        scene black
        with dissolve2

        "Ami falls asleep several minutes later."
        "Her hand drops to the side and hangs just an inch or two off of the floor."
        "I think more about how she said that floor used to be, covered in trash from neglect, and I wonder what it must have been like for her and the old Sensei during those dark, hopeless times. "
        "I imagine it must have been hard."
        "And in imagining that-"
        "I wonder if it would ever be possible for me to feel that much all at once."

        $ renpy.end_replay()
        $ amiinvite1 = True
        $ ami_love += 3
        stop music fadeout 5.0

        "{i}Ami’s affection has increased to [ami_love]!{/i}"
        "………"
        "……"
        "…"

        if day >= 6:
            jump endofsat
        else:
            jump endofweekday

label amiinvite2:
...
```

## Code that triggers this event

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amiinvite:
    if amiinvite1 == False:
        jump amiinvite1
...
```