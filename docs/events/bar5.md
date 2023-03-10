# The Bare Minimum (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sana love greater than or equal to 5



## Next events

* [Main: Cleaning Duty](./day36.md)

## Event properties

* Id: bar5
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar
* Triggered by path: sanasbar->bar5

## Official wiki page

[The Bare Minimum](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar5&go=Go) for more details.

## Event code

File: (install folder)\game\SanaEvents.rpy

Code:
```python
...
label bar5:
    scene bareredux1
    with fade
    play music "calmbar.mp3"

    "I walk into the bar to find absolutely no one- a small but noticeable change from last time."
    "I'm not really sure if this can be chalked up purely to me showing up late, either, considering Sana's already informed me of the struggling state of this business-"
    "But maybe it's even worse off than I thought?"
    "At the bare minimum, there should be at least one customer half-passed out behind the counter, silently drinking to him- or, sorry, {i}her{/i}self."
    "I'm still not fully used to the idea of there not really being any men around here yet, I guess."

    scene bareredux2
    with dissolve

    sa "Umm...Hi, Sensei..."
    s "Hey, Sana. Where is everybody?"
    sa "This...{i}is{/i} everybody..."

    if day < 6:
        sa "Weekdays...aren’t really that busy for us..."
    else:
        sa "Weekends...aren’t really that busy for us..."

    s "Yeah...I can see that."
    s "Would you mind if I took a seat? I’ve been walking for a while and I’m pretty exhausted."

    scene bareredux3
    with dissolve

    sa "O-Oh! Right! I’m...so sorry...I shouldn't have stopped you as soon as you walked in..."
    s "It’s fine. You were probably just so excited to see another human lifeform in here that you couldn't help but approach me as soon as the door opened."

    scene bareredux4
    with dissolve

    sa "What's...really sad is that...you're probably not wrong..."
    sa "Is it...okay if I sit next to you, though?..."
    s "What if another customer shows up, though?"

    scene bareredux5
    with dissolve

    sa "I...don’t really think we have to worry about that..."
    sa "I was...probably just going to close down soon anyway, so..."
    s "Then, sure. I don’t mind at all."
    s "It might be a good time to start your {i}lessons{/i} anyway."

    scene black
    with dissolve

    sa "As...good a time as any, I guess..."

    "Sana leads me over to the bar and politely pulls out a stool for me despite it being larger than her and probably weighing twice as much."
    "She may not have much faith in the business, but at least she's attentive when it comes to customers."
    "Or at least me."
    "To be fair, though, there haven’t been many opportunities to see how she acts around others."

    scene barfive1
    with dissolve

    sa "…"
    s "…"

    "I kick off the lesson by remaining completely silent and just observing how Sana acts around me."
    "And, if she had the confidence in herself to even look my way, she'd be made immediately aware of how creepy and unacceptable this method is."
    "Unfortunately for her, her inability to make eye contact has already resulted in her missing out on a valuable lesson."
    "Here's hoping she's at least {i}tried{/i} practicing in some way during my absence."

    s "So, any progress on your end lately? Have you been able to hold any conversations with anyone you're not directly related to?"

    scene barfive2
    with dissolve

    sa "Well...there's Ayane too, but...other than that...not really..."
    sa "I’ve been trying...but..."

    "Sana drifts off, as if she's expecting me to fill in the blanks of her inadequacies."
    "Which, to be fair, I probably could. But me doing the legwork isn't going to help her in any way."
    "If she's going to improve herself, she first needs to confront her problems head on."

    s "But what?"
    sa "It’s just...kind of hard without anyone to talk to..."
    s "I guess that's fair."
    s "Maybe try practicing in the mirror or something? Isn't that what actors do when they're first starting out?"

    scene barfive3
    with dissolve

    sa "Does that...actually work?..."
    s "Maybe. I've never tried. Just...pretend you’re someone else and try to strike up a conversation while...playing both sides?"

    scene barfive1
    with dissolve

    sa "That sounds...way too complicated..."
    sa "Plus...I don’t really like mirrors...so..."
    s "Why not?"
    sa "It's...kind of personal, so...if you don't mind..."
    s "Don't worry about it, then. We can just keep going like this."

    "I can't blame Sana for not wanting to just freely divulge personal information to me now that we're talking somewhat regularly."
    "No one should trust anyone until they're given a reason to- and I am no exception to that."
    "Sana needs time to grow."
    "Mentally, at least. Because, to be quite honest, I hope she stays her current size forever."

    s "Here's an idea, Sana. How about we try a little roleplay?"

    scene barfive3
    with dissolve

    sa "Roleplay?...You mean like...a game?"
    s "Sure. You can call it a game if you want. Just pretend I’m a customer and-"
    s "Well, actually, I {i}am{/i} a customer. But I’m sure you know where I’m going with this."

    scene barfive4
    with dissolve

    sa "Uh...yeah...if...if it's just a game...I can...probably do it..."
    s "Just to mix things up, though, I’m going to try and be difficult. Got it?"

    scene barfive3
    with dissolve

    sa "Difficult? How so?"
    s "I mean that I’m going to give you problems that might arise at the bar and you’re going to need to figure out what to do about them."

    scene barfive5
    with dissolve

    sa "You’re not...going to break anything...are you?"
    sa "Because...it comes out of my paycheck if you do..."
    s "First off, no. Second, do you really have to pay for things that break on your shift here?"
    sa "Well...no...But I’d...feel really bad if I didn’t..."

    scene barfive2
    with dissolve

    sa "Not having customers means my mom doesn't have much money, and...I wouldn't want her to pay for all of that out of pocket..."
    sa "So...if I can help by...paying for a few broken glasses...I don't really mind..."

    "I guess this means I can assume Sana’s dad isn’t in the picture either."
    "Is it really just Sana and her mom trying to keep this place afloat on their own? No wonder why they're going under."
    "There's only so much two people can do- especially when it comes to maintaining a place like this."

    s "Okay. Well, I promise to not break anything. I’ll just act kind of rude toward you or something. "
    s "Will you be able to handle that?"

    scene barfive5
    with dissolve

    sa "Well...can you tell me how rude you’re going to be?"
    s "Nope."
    sa "..."
    sa "But-"
    s "Sana, hurry up and get behind the bar. This is a trial by fire."
    sa "But...our extinguisher is...really old and...I don't know if it still works..."
    s "I'm going to ignore that extreme safety hazard for now and say it again. Get behind the bar."
    sa "Okay, but...I can already tell...I'm going to fail whatever this is..."

    scene black
    with dissolve2

    "Sana gets out of her seat and nervously rounds the corner into the bar area..."
    "She closes her eyes and takes a deep breath, though I'm not sure how much benefit it will have since I don't intend to pull any punches with this."

    scene firstbar4
    with dissolve

    sa "Umm...Hello, sir...What can I-"
    s "Yeah, whatever. Give me a beer and a plate of spaghetti."

    scene barfive6
    with dissolve

    sa "A plate of...spaghetti?..."
    s "Did I stutter? Or are you just really fucking bad at your job?"
    sa "Well...I don't think so...but..."

    scene barfive7
    with dissolve

    s "Listen kid, I’m in a hurry. So if you don’t have my spaghetti in five minutes, I’m gonna have to-"
    s "Wait, Sana, are you crying? We literally just started."
    sa "W...w...we...d...don’t...have any...s...sp...spaghetti..."

    "This is even worse than I thought."

    s "Sana, if this is too hard-"

    scene barfive8
    with hpunch

    sa "I’LLGOGETYOURBEER!!!"

    scene firstbarnone
    with dissolve

    "Sana sprints over to the opposite side of the bar and trips over one of the mats on the
    ground, knocking a few things off the counter."
    "She scrambles to pick them all up and quickly pulls the first bottle she sees out of the cooler."

    scene barfive9
    with dissolve

    sa "H...Here it is...your..."

    scene barfive9r
    with dissolve

    sa "Your..."
    s "..."
    sa "..."

    scene barfive10
    with hpunch

    sa "Ah!"
    s "..."

    scene barfive11
    with dissolve

    sa "I’LLBERIGHTBACK!!!"

    scene firstbarnone
    with dissolve

    "This is hard to watch."

    scene barfive12
    with dissolve

    sa "…"
    s "…"
    sa "Don’t laugh at me..."
    s "I’m not laughing. In fact, I feel like I owe you an apology."

    scene barfive13
    with dissolve

    sa "No...You don’t...I’m just not really used to...dealing with pressure..."
    sa "No one has ever asked for spaghetti before...I didn’t know how to handle it..."
    s "Well, if it makes you feel any better, I don't think a real customer will ever ask for spaghetti. Especially considering you don't have a menu."
    s "But, in the event that someone does, it’s always okay to just tell them that you don’t have any."

    scene barfive12
    with dissolve

    sa "B...But when I tried that and you...said..."
    s "What I said doesn't matter."
    s "I’m sure you’ve heard that whole thing about how the customer is always correct, right?"
    sa "Y...Yes..."
    s "Well, that’s not true. In fact, the customer is pretty much always wrong."
    s "You know this place better than they do, so be assertive and tell me that you don’t have any spaghetti."
    sa "..."
    sa "Like...Like right now?..."
    s "Right now."
    sa "..."
    s "Deny me the spaghetti, Sana."
    sa "We..."
    sa "We don’t have any spaghetti..."
    s "Perfect. That concludes our lesson for the day."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene barfive14
    with dissolve

    sa "I’m...so confused..."
    sa "Was that...really supposed to help?..."
    s "It probably could have gone a little better on both of our ends. But don't be surprised if you wake up tomorrow and you're suddenly an expert at talking to people."

    scene barfive15
    with dissolve

    sa "Well...at least it was...a little fun?..."
    s "Are you still crying?"
    sa "..."
    s "Sana."
    sa "I’ll...try not to freak out next time! I promise!"
    s "And I will try not to make you cry. But, honestly, I'm not sure how much good that's going to do when all it took was spaghetti."
    sa "It was...more the...context of the spaghetti that...made me cry..."
    s "I'm sure it was, Sana."

    scene black
    with dissolve2

    s "I'm sure it was."

    "Sana and I say our goodbyes and she walks me to the door so she can lock it behind me."
    "Was today actually successful in teaching her anything?"
    "No."
    "But, like she said-"
    "At least it was a little fun."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar5 = True

    "{i}Sana’s affection has increased to [sana_love]!{/i}"

    stop music fadeout 3.0
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar10:
...
```

## Code that triggers this event

File: (install folder)\game\SanaEvents.rpy

Code:
```python
...
label sanasbar:
    if sana_love >= 0 and firsttimebar == False:
        jump firsttimebar
    if sana_love >= 5 and bar5 == False:
        jump bar5
...
```