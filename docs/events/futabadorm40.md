# Skin (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Futaba love greater than or equal to 40

* Day of week is not Wednesday

* Event [War's End](./dormwar17.md) (Main) is completed)



## Next events

* [Futaba: Shadowplay](./library40.md)

## Event properties

* Id: futabadorm40
* Group: Futaba
* Triggered by label: futabadorm
* Triggered by branch label: futabadorm
* Triggered by path: futabadorm->futabadorm40

## Official wiki page

[Skin](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabadorm40&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label futabadorm40:
    if _in_replay:
        play music "sweetvermouth.mp3"
        scene dorm

    play sound "knock.mp3"

    "I knock on Futaba’s door and wait for her to answer."

    r "Come in!"
    s "..."

    "I worry for a moment that I may have accidentally selected Rin instead, but ultimately accept that she also lives in this room and that things like this will happen sometimes."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I make my way into the room and go to take my shoes off, but am quickly stopped by a brigade of [teenager]s who appear to be on some sort of mission."

    scene futabafirstgym1
    with dissolve

    r "Yo! You’re just in time for our mission."
    s "Funny you should say that because-"
    no "Because Sensei and I had other plans tonight."
    no "Thank you for showing up exactly when we agreed."
    no "Now, I suppose I’ll be-"

    scene futabafirstgym2
    with dissolve

    r "No way, Nodoka! We’re all in this together! "
    no "{i}But I am le tired...{/i}"
    s "Uhh...I’m not interrupting something, am I?"
    f "Not...particularly. But you did choose a bad time to show up."

    scene futabafirstgym3
    with dissolve

    r "We’re about to go get ripped! Wanna come with us, Sensei?"
    s "What?"
    f "What...Rin is trying to say is that...a new gym just opened up in the area and...I’m trying to be a little...healthier."
    r "{i}We{/i} are trying to be a little healthier."
    s "That's great, but isn’t it a little late to be going to the gym?"
    f "There are actually a lot of people who prefer going later because...it means there will be less people around to...watch you."
    s "Like perverts?"

    if bonus == True:
        r "If we were worried about perverts, we wouldn’t have invited you!"
        r "Or Nodoka, for that matter!"
    else:
        r "If we were worried about perverts, we wouldn’t have invited Nodoka!"

    scene futabafirstgym4
    with dissolve

    if bonus == True:
        no "Are you insinuating that I will be gazing longingly at your overworked, sweaty bodies, wishing to be the towel you use to dry yourselves off?"
        r "Nodoka, if there is anyone who understands that exact train of thought, it is me. "
        no "You are very much a beautiful disaster, Rin."
        r "Thank you! But today isn’t about our unearthly cravings for the touch of a cute girl! It is about willpower! And determination!"
        no "Every day is about my unearthly craving for the touch of a cute girl."
    else:
        no "I am only here to get ripped."

    s "I’m with Nodoka on this."
    f "Of course you are..."

    scene futabafirstgym5
    with dissolve

    f "So...since that’s what we’re doing tonight...maybe you and Rin could...hang out some other time."
    s "Just to clarify, I came here to hang out with you, Futaba."

    scene futabafirstgym6
    with dissolve

    r "What the hell?! But {i}I’m{/i} the one who answered the door! That means you're here for me!"
    f "E-Even if you’re here to see me...it doesn’t change that the three of us already have plans, so..."
    f "Maybe some other time?"
    no "I see no harm in Sensei coming along to scope out the area. Perhaps he, too, is looking to tone up a bit?"
    s "I’m actually in surprisingly good shape for someone who never does anything. "
    s "Well, at least on the outside."
    s "I’ve tried running with Miku before and it made me want to die, so...yeah. Not really into the idea of exercising with you guys."

    scene futabafirstgym7
    with dissolve

    f "I...suppose if it’s just to...see the area, it’s fine..."
    f "But...I already feel weird about doing this with Nodoka and Rin and...I’m sure you can see where I’m going with this."
    s "Yes, you are insecure about your body despite constant reminders from all of your friends and me that you’re gorgeous."
    f "Sensei...validation and...compliments are nice and everything, but...they can’t really change the way a person sees themself. "
    f "So, yes...I am insecure and I’m...trying to actually go about handling that in a way that is...productive this time."
    s "Had you been handling it...{i}un{/i}productively up until now?"
    f "I-"

    scene futabafirstgym8
    with dissolve

    no "{i}The clock is ticking, the hours are going by. The past increases, the future recedes. Possibilities decreasing, regrets mounting.{/i}"
    no "What happened “up until now” means absolutely nothing. And standing idly around and discussing it just prevents us from making the strides we need to reach our destination."
    no "In summation, as Futaba’s makeshift attorney and the guardian of her heart, I implore you to wait until she is comfortable with discussing such matters and-"
    f "It’s okay, Nodoka...I’ve been meaning to tell him soon anyway."
    no "But “soon” is not today and I will not allow your already dwindling self-consciousness to become one more barrier between us and various exercise machines."

    if bonus == True:
        no "Also, I want to see the exposed skin and tight, form-fitting spandex of women much older and stronger than me. "
        s "That does sound alluring so, I am once again siding with Nodoka on this."
    else:
        no "Also, my arms are starting to get all jiggly and it's making me feel all sad inside."

    scene futabafirstgym9
    with dissolve

    f "So...you’re definitely coming?..."
    s "I won’t stay to watch you guys work out. "
    s "I do have time to kill, though, and knowing where a place like this is would be a good thing in the event that my lungs begin to tire out or something."
    no "Be sure to thank your organs every morning to prevent things like that from happening."
    s "That’s not how organs work, Nodoka."
    f "Well...so long as you promise to not...stick around..."
    f "I guess it wouldn’t do any harm to just...walk there with you."
    f "It’s not particularly far or anything. It’s only a few blocks away from the dorm, so...I’m sure a lot of other girls will wind up going there soon as well..."
    s "Speaking of which, where's Otoha? I could have sworn she was part of your...brigade."

    scene futabafirstgym10
    with dissolve

    r "She’s...busy writing tonight. So we’re just going to go without her."
    no "She’d make us all feel weak and insignificant anyway since she actually works out and we are solanum tuberosum."
    s "You are...what?"
    no "Potatoes."
    s "Right..."

    scene black
    with dissolve2

    "Futaba ultimately accepts that she will not be able to prevent me from tagging along and, after sighing heavily to herself as she so commonly does, the three of us leave the dorm."
    "We begin walking in the direction of the maid cafe and I inadvertently become a bit more excited than I should be."

    if bonus == True:
        "But I calm myself down when I realize that I will not be seeing girls in maid outfits and will instead be seeing them in spandex."
        "Actually, nope. Not calm at all. This is just as good."
        "I thank the god I don’t believe in that I am wearing thick jeans and that any protrusion that may emerge from them is not my fault and that I can not be held accountable for having eyes."
    else:
        "I am going to burn so many calories."

    "………"
    "……"
    "…"

    scene futabafirstgym11
    with dissolve

    if bonus == True:
        "Futaba tries to get me to leave once we arrive, but I remain insistent on seeing the inside as well because no one has changed clothes yet and that’s {i}kind of{/i} why I came in the first place."
        "I’m sure that’s part of why she wants me to leave anyway, but I have seen her with immensely {i}less{/i} clothing before and don’t quite understand why it’s suddenly a big deal."
        "Once the girls get dressed and all of us step into the gym, however, we discover that we are not the only ones here."
    else:
        "Futaba tries to get me to leave once we arrive, but I remain insistent on seeing the inside so I can confirm there are no ghosts in there."
        "Thankfully, Rin brought one of those ghost vacuums the Ghostbusters use and is able to clear out the place without my help."

    no "I like the gym now."
    r "Is it...normal for your first reaction to a girl to be “Please hit me?”"
    no "Exceedingly normal. There is no other reaction I would accept right now."

    scene futabafirstgym12
    with dissolve

    "I’m a bit surprised to find Yuki, of all people, kickboxing a punching bag in the same gym that my students are now going to be visiting."
    "But, I suppose she needs {i}some{/i} outlet for all of her built up anger now that she’s not...killing people for a living or whatever it is biker gangs do to stay afloat. "
    "Also, under these circumstances, I too would enjoy being hit. "
    "This might be the first time in my life I have ever wanted to switch places with a punching bag. "
    "So, yeah. I guess this is a thing now."

    scene futabafirstgym13
    with dissolve

    f "…"
    s "Still feeling up to this, Futaba?"
    f "Well...it’s not like I have much of a choice since...all of us already came here."
    f "I’d feel bad if we didn’t at least do {i}something.{/i}"
    f "I...can’t help but feel a little intimidated by that woman, though..."
    s "She doesn’t look so tough to me."
    r "Are you kidding? Look at her legs. Those things could kill someone."

    "And I’m sure they have."

    no "This might be the first time in my life I have ever wanted to switch places with a punching bag. "
    s "I really think we might be related, Nodoka. It’s actually starting to become a real concern of mine."
    f "So...umm...now that we’re here..."
    s "Are you going to get rid of me?"
    f "I’m just...seeing if you’re going to be true to your word or not."
    s "Yeah, I’ll head out in a second. I’m just going to give that woman a piece of my mind first for intimidating all of you impressionable, [young_girls]."

    scene futabafirstgym14
    with dissolve

    f "W-Wait! You don’t have to go that far, Sensei!"
    r "Yeah...No disrespect to you, but I’m pretty sure that girl could take you."
    no "She can take {i}me{/i} any day of the week."
    s "Don’t worry about it, Futaba. I know exactly how to deal with girls like her."
    f "Sensei!"

    scene futabafirstgym15
    with fade

    "I make my way over to Yuki, breaking her concentration on the punching bag and allowing it to live at least one more minute before being blown into pieces."

    yu "Oh shit. What are you doing here? "
    yu "You didn’t really strike me as the type to work out."
    s "Yuki, can you help me look cool in front of my students and pretend that I intimidated you out of the gym?"
    yu "…"
    s "…"

    scene futabafirstgym16
    with dissolve

    yu "You fuckin’ serious right now?"
    s "Yuki, please. They need to know how cool I am."
    yu "Fuck no, man. I’m still on my free trial. I’ve gotta make use of this time."
    yu "Unless you’re tryin’ to pay for my subscription or some shit."
    s "I can’t. I’m already paying for your daughter’s phone bill."

    scene futabafirstgym17
    with dissolve

    if bonus == True:
        yu "Oh. Well then no fuckin’ wonder she’s okay with screwing someone your age. "
        s "For the last time, I-"
    else:
        yu "Dude, pay for mine too. I don't get a job until a few updates later."

    scene futabafirstgym18
    with dissolve

    no "Hi there. Nodoka Nagasawa. I may look fragile, but I am willing to take any punishment you’d like to throw at me."
    no "Are you at all interested in younger women?"
    yu "…"
    yu "What?"

    scene futabafirstgym19
    with dissolve

    r "Excuse me, but...I can’t figure out how to turn on the water in the shower room..."
    yu "You just..."
    yu "You turn the knob..."
    r "Can..."
    r "Can you show me?..."
    yu "..."
    s "..."

    scene futabafirstgym20
    with dissolve

    yu "..."
    s "..."
    s "And stay out, bitch."
    yu "..."

    scene futabafirstgym21
    with dissolve

    yu "Hah..."
    yu "You’re gonna owe me dinner for this shit."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene futabafirstgym22
    with dissolve

    s "She’s gone. Your problems are solved."
    f "Uhh...Not all of them..."
    f "You’re still here..."
    s "Am I not allowed to support you the same way your other friends do?"
    f "Sensei...you can...support me in your own way..."
    f "But...it’s pretty obvious that the reason you’re sticking around isn’t because of that."
    s "Why is that obvious? I can do nice things from time to time."
    f "Because..."

    scene futabafirstgym23
    with dissolve

    f "Because...uhh..."
    s "What? What are you looking- "
    s "Oh."

    if bonus == True:
        "I guess my pants weren’t thick enough after all."
    else:
        s "How long have I been holding this turtle for?"

    scene futabafirstgym24
    with dissolve

    r "Hey!"
    s "Hi, Rin. Don’t look down."

    scene futabafirstgym25
    with dissolve

    r "Of course I’m going to look down if you tell me not-"

    scene futabafirstgym26
    with dissolve

    if bonus == True:
        r "Oh."
        r "Well...yeah. Okay then."
        s "I tried to warn you."
        r "Yeah...Yeah, you did."
        r "Uhh..."
        r "I’m gonna go...punch things or...something..."
        s "Okay, have fun."
        r "Uhhhhhhhhh okay."
    else:
        r "Woah. Is that a turtle?"
        s "Yeah."
        r "Cool."
        r "Uhh...why did I come over here again?"

    scene futabafirstgym27
    with dissolve

    f "So...you see now why I feel weird about you staying here?"
    s "It makes a little more sense now, yes."
    s "But I still don’t think you should be embarrassed about working out in front of me. "
    s "I think it’s great that you’re trying to be healthier and-"

    scene futabafirstgym28
    with dissolve

    f "Can you please...{i}not{/i} do this right now?..."
    f "You can come see me tomorrow and...we’ll spend time together then..."
    f "But if I’m going to be serious about doing this...I kind of need you to...not be around for it..."
    f "It’s obviously nothing personal...I just..."

    scene futabafirstgym29
    with dissolve

    f "I’m really...uncomfortable in my own skin, Sensei..."
    f "And...no amount of encouragement or validation is going to change that..."
    f "So...please..."
    f "At least...not until I’m feeling a little better about this..."

    "I sigh to myself and accept that I’ve probably overstepped my boundaries tonight."
    "I overstep my boundaries all the time, though."
    "I guess I just didn’t expect to be pushed back so firmly by Futaba of all people."
    "Now that the tears have started to show up, though, I’m obviously not going to stick around any longer."
    "Blowing things out of proportion wasn’t really at the top of my to-do list today, and it’s already starting to get late."
    "So...I should probably stop prodding her for now and wait until another opportunity arrives to see if we can progress any further."

    s "Okay, I’m leaving. "
    s "I’m happy for you, though."
    s "Well, as happy as I can be. Happiness isn’t really my thing."
    f "And working out isn’t mine, but...we have to start somewhere."
    f "I’m sorry for almost crying."
    s "I’m sorry for making you almost cry."
    s "Well, as sorry as I can be. Apologeticness isn’t really my thing either."

    scene futabafirstgym30
    with dissolve

    f "Okay...that’s enough. I’m not talking to you anymore."
    s "That’s fine. I’ll just go talk to Nodoka or-"
    s "Wait, where did Nodoka go?"
    r "Oh, she ran after that badass biker chick once she left. "
    s "Yeah..."
    s "Yeah, that checks out."

    scene black
    with dissolve2

    "I leave the gym and begin my journey home."
    "I’m not sure how often I’ll go back to a place like that, especially considering that a certain someone really does not want me around, but I’m glad to know it exists, I guess."
    "It’s good that Futaba is trying to change the parts of herself that she doesn’t like."
    "If you don’t do that while you’re young, they’ll likely wind up becoming hideous aspects of yourself that are impossible to ignore or fix."
    "And, no matter how hard you try to shut them out, something will always happen to remind you of them."
    "To transport you back to better days, when it was still possible to-"

    s "…"

    "I decide to call Ami and talk to her for the rest of my walk home."

    $ renpy.end_replay()
    $ futabadorm40 = True
    $ futaba_love += 1
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    play sound "phonebeep.wav"

    "{i}You have received a new picture message from Rin!{/i}"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label futabadorm45:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label futabadorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if futaba_love >= 5 and futabafall == False and futabafirstvisit == False:
                "Please play Futaba's level 5 Library event to unlock the first dorm event!"
                jump doorknock
            if futaba_love >= 5 and futabafall == True and futabafirstvisit == False:
                jump futabafirstvisit
            if futaba_love >= 10 and futabadorm10 == False:
                jump futabadorm10
            if futaba_love >= 15 and library15 == True and futabanew1 == False:
                jump futabanew1
            if futaba_love >= 15 and futabanew2 == True and futabanew3 == False:
                jump futabanew3
            if futaba_love >= 15 and futabanew3 == True and futabadorm15 == False:
                jump futabadorm15
            if futaba_love >= 25 and day > 5 and bookdate == True and futabadorm25 == False:
                jump futabadorm25
            if futaba_love >= 30 and library30 == True and day != 3 and futabadorm30 == False:
                jump futabadorm30
            if futaba_love >= 35 and library35 == True and futabadorm35 == False:
                jump futabadorm35
            if futaba_love >= 40 and day != 3 and dormwar17 == True and futabadorm40 == False:
                jump futabadorm40
...
```