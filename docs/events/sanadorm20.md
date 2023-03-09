# Nice Weather We're Having
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sanadorm20&go=Go)



## Event preconditions
✅Sana love greater than or equal to 20

✅Event "[Sana: Scouting Mission](./bar20.md)" is completed (event=bar20)



## Next events
* [Sana: Life is a Tomato](./bar25.md)

## Event properties
* ID: sanadorm20
* Group: Sana
* Triggered by label: sanadorm
* Triggered by branch label: sanadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm20:
    play sound "knock.mp3"

    "I knock on Sana's door and wait for her to answer."
    "I can hear her bed squeak as she hops off of it and scurries over to the door, footsteps sounding a bit more...urgent than normal."
    "I doubt it's anything even close to excitement, but even the idea of her abandoning her conditioned hesitation is enough to remind me of our progress, and I'm not even inside yet."

    sa "Sensei?...Is that you?..."
    s "Sure is. Can I come in? Or are you going to try and use your pajamas as an excuse again?"
    sa "Hahah...no...you can come in..."
    sa "I...um...unlocked the door for you..."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "See what I mean? Progress."
    "To be fair, if there {i}wasn't{/i} any progress by now, I'd probably second guess all the effort I'm putting into hanging out with Sana-"
    "But, at the same time, I doubt I'd give up on it simply because..."
    "Well, you've seen her."

    scene weatherredux1
    with dissolve

    sa "Um...hi..."
    sa "How..."
    sa "How are you doing?..."
    s "Are you actually taking charge of the conversation today? Because normally, there's a {i}little{/i} more stammering involved before you start asking me questions."
    sa "Well, it's my room, so...I figured it would be...polite to ask..."
    s "Then, I'm fine. Thank you for asking. How are {i}you{/i} doing?"
    sa "I'm...also fine..."
    s "Cool."
    sa "Y-Yeah..."
    s "..."
    sa "..."

    "{s}Progress.{/s}"

    s "So, what were you doing before I showed up? Games again?"
    sa "Oh, no...I was just watching TV and...texting Ayane..."
    sa "Did you...did you know she has a room in her house that's...completely full of trampolines?..."
    s "No, but that makes sense."
    s "We can still watch TV if you want, Sana. You don't have to turn it off just because I'm here now."

    scene weatherredux2
    with dissolve

    sa "Well...actually...I'd rather talk to you if...that's okay..."
    sa "But...but just because I...still need to practice...and stuff..."
    s "Hey, fine by me. Just promise not to freak out if we drift into a topic you're not ready for."

    scene weatherredux3
    with dissolve

    sa "I don’t...freak out {i}that{/i} often...do I?"
    s "You kind of do. I know you're getting more comfortable around me but, in your current condition, I'm not sure if that skill will really translate to other conversations you might have."

    scene weatherredux2
    with dissolve

    sa "That's okay...I'll just...only talk to you for the rest of my life..."
    s "Sana, you're really going to have to get better with other people sooner or later."
    sa "But other people are...confusing..."
    sa "You’re...easy to understand..."
    s "That can't be true. There's no way you'd still open the door for me if you truly understood me."

    scene weatherredux1
    with dissolve

    sa "Then...we really...{i}should talk...{/i}"
    s "Were you not listening just now when I essentially told you that the more you know, the less you'll {i}want{/i} to know?"
    sa "I was...I just...don't believe you."
    s "Well, that'll be your loss."
    s "We can talk as much as you want. I just think it would be better if we strayed from anything involving my thoughts on you or anyone else you know."

    scene weatherredux4
    with dissolve

    sa "Do you...have thoughts about me you...need to keep to yourself?..."
    s "See, you're already crossing into dangerous territory. Ask me an easier question."
    sa "Oh. Um...uhh..."
    sa "Would you...would you like to sit down?..."

    scene black
    with dissolve2

    s "Why, yes. Thank you, Sana. That is a much better start to this conversation than asking me the one thing I suggested you {i}don't{/i} ask me about."
    sa "I'm...so confused..."

    "........."
    "......"
    "..."

    scene onthecouch1
    with dissolve2
    play music "love.mp3"

    "As expected, the two of us sit awkwardly on the couch while Sana contemplates exactly what topics we can discuss without dismantling our relationship."
    "But even though she appears determined, it’s times like these where I truly understand just how hard it is for her to converse with people."
    "Even though the two of us are only a few steps away from {i}friends{/i} at this point, she’s still having a difficult time just making eye contact with me."
    "I wonder if this is how it is with her and Ayane as well?"
    "Granted, I’m sure Ayane is a lot better at making her feel comfortable than I am."
    "Which is a strange thing to think because Ayane also brings a sword to school sometimes and that's not really a thing I'd personally equate to comfort."
    "Either way, Sana is doing her best. And it is my responsibility to not get in her way while she does that."

    sa "Um..."

    "Eventually, she manages to break the silence."

    scene onthecouch2
    with dissolve

    sa "N..."
    sa "Nice weather we’re having..."
    sa "Right?"
    s "…"

    "Well, at least she tried."

    s "Sana, I'm going to let you in on a little tip."
    s "Avoiding that question is basically rule number one when it comes to holding a conversation."
    s "As soon as you ask someone about the weather, you’re essentially admitting defeat."

    scene onthecouch3
    with dissolve

    sa "I...I know that...I just...I don’t really know what else to say..."
    sa "I still feel strange...being alone in here with you..."
    sa "It’s...a lot different than it is at the bar..."
    s "You're right. It's a lot busier in here."

    scene onthecouch4
    with dissolve

    sa "Very funny, Sensei..."
    s "I get what you’re saying, though. This feels kind of weird for me too."

    scene onthecouch5
    with dissolve

    sa "Really? Why?"

    "Sana perks up when I tell her that. I guess just thinking that she isn’t alone in feeling lonely is enough to make her feel...less lonely?"
    "I lose track of what I'm thinking with how many times loneliness comes up."
    "I'm glad she feels like she can relate, though."
    "All I have to do is hide the fact that the majority of {i}my{/i} discomfort stems from an unearthly desire to take her clothes off and everything will turn out a-okay."

    s "That's classified."
    s "I can promise you that everything will be significantly less weird if we just ignore that I said that."

    scene onthecouch6
    with dissolve

    sa "Well...us being alone together is...already weird, so...yeah..."
    sa "Plus...I know you said it doesn't matter, but...I still feel weird about the...pajamas..."
    s "Your pajamas are sweatpants and a giant hoodie. Why would that possibly make you feel weird?"
    sa "Because I...look like a...marshmallow that was held over the fire for too long..."
    s "That’s the only way to eat marshmallows."

    scene onthecouch7
    with dissolve

    sa "You're not..."
    sa "Thinking of eating me...are you?..."
    s "I have come here today to devour you whole."

    scene onthecouch8
    with dissolve

    sa "PLEASE BE GENTLE!"
    s "…"
    s "Sana, you know I'm kidding right?"

    scene onthecouch9
    with dissolve

    sa "But...you could if you really wanted to...so I need to...stay on guard..."
    s "Do you really trust me that little? I thought we were at a level where you didn't view me as a cannibal."
    sa "We were...until you said you wanted to eat me..."
    s "That...was a joke..."

    scene onthecouch10
    with dissolve

    sa "I know..."
    sa "I was...playing along..."
    sa "But I guess I'm...not good at showing that, yet..."
    sa "I know you’re not going to eat me, Sensei."
    sa "I might be small...but I'd still be a lot of food. There’s no way you’d be able to finish me in...one sitting..."
    s "{i}That{/i} is why you don’t think I’d do it? Because you'd be too much to eat?"
    sa "That and how...I know you’re actually...a really nice guy..."
    s "…"

    scene onthecouch11
    with dissolve

    sa "Umm...it’s kind of...embarrassing when you don’t say anything back..."
    s "It’s kind of embarrassing when you blindside me with compliments like that."
    sa "You don’t seem very embarrassed."
    s "I don't seem very {i}anything{/i} ever. It's kind of just who I am."
    sa "Well...{i}I'm{/i} embarrassed...so you can be too...if you want..."
    s "You're embarrassed? How come?"
    sa "Well...that's...kind of a hard question to answer..."
    s "Could it be that you’re finally starting to see me as a little {i}more{/i} than just a teacher?"

    if bonus == False:
        s "Because that would be bad and I want to avoid that at all costs so that we can remain friends who do not feel anything romantic for one another."

    scene onthecouch12
    with dissolve

    sa "More than a...what?"
    s "..."
    sa "Did you say...more than a teacher?...because...you {i}are{/i} a teacher...so I will...obviously see you as that..."

    scene onthecouch13
    with dissolve

    s "Then it will mean absolutely nothing to you if I do this."
    sa "Do...what, exactly?...I don't know what you're...talking about..."
    s "You will whenever you regain your senses."

    scene onthecouch14
    with dissolve

    sa "But...my senses are fine..."
    sa "I guess I feel a little warm, but...other than that..."
    s "..."
    sa "Other than that, I'm-"
    s "Sana. Look down."

    scene onthecouch15
    with dissolve

    sa "Why? What's-"
    s "..."

    scene onthecouch16
    with dissolve

    sa "..."
    s "You really didn't feel that?"

    scene onthecouch17
    with dissolve

    sa "WHAT IS HAPPENING?! WHAT ARE YOU DOING?!"
    s "Being hilarious."
    sa "ISN'T THIS...INAPPROPRIATE?!"
    s "No. It's a test."
    sa "A TEST OF WHAT?! THIS IS NO TEST I HAVE EVER HEARD OF!"
    s "Are you sure? Because I'm a teacher. I think I know a test when I see one."

    scene onthecouch18
    with dissolve

    sa "THIS IS NOT A TEST! LEWD CONTENT MUST BE CENSORED!"
    s "This isn’t even remotely lewd..."
    sa "YES IT IS, SENSEI! THIS WOULD BE CENSORED IN A VIDEO GAME!"
    sa "AND THEN PATREON WOULD TAKE IT DOWN ANYWAY BECAUSE EVEN IF A GAME HAS ZERO SEXUAL CONTENT BUT YOUNG LOOKING CHARACTERS LIKE ME EXIST INSIDE OF IT, THEY CAN DECIDE AT ANY GIVEN MOMENT THAT THEY DON'T WANT YOU TO EXIST ANYMORE!"
    sa "80%% OF YOUR INCOME COULD BE WIPED AWAY IN MINUTES AFTER WORKING WITH THEM FOR TWO STRAIGHT MONTHS AND EVEN RECEIVING THEIR APPROVAL!"
    sa "THEN, WHEN THEY RANDOMLY DELETE THE PAGE THAT THEY REVIEWED THEMSELVES AND GAVE THE GREENLIGHT TO DESPITE NO CHANGES BEING MADE TO IT {b}AT ALL,{/b} THEY WOULDN'T EVEN HAVE THE DIGNITY TO TELL YOU WHY THEY CHANGED THEIR MIND!"
    sa "TO THINK THAT A COMPANY WHO PRIDES THEMSELVES ON BEING A HOME FOR CREATORS COULD SIMPLY GHOST SOMEONE MAKING THEM THOUSANDS OF DOLLARS A MONTH WITHOUT EVEN TELLING THEM WHY SHOULD TERRIFY {i}ALL{/i} CREATORS OUT THERE!"
    sa "WHAT IS THE POINT OF A TERMS AND CONDITIONS SYSTEM IF NO ONE AT THE COMPANY UNDERSTANDS IT?! DOES PATREON EVEN TRAIN THEIR EMPLOYEES?! WHO EVEN ARE THEIR EMPLOYEES?! WHO THE FUCK IS MORGAN?!"
    s "Sana, chill."
    sa "FUCK YOU, MORGAN! FUCK YOU TO HELL!"

    scene onthecouch19
    with dissolve

    s "You seem really passionate about all this."
    sa "Not as passionate as the people who are going to whine and bitch about this blatant breaching of the fourth wall."
    sa "I can hear it now...{i}The older version was funnier...I liked it more when Sana looked really tall...{/i}"

    scene onthecouch18
    with dissolve

    sa "I'M STILL GROWING! LEAVE ME ALONE!"
    s "This is going to confuse so many new players."
    sa "AAAAAAHHHHH!!!!!!"
    s "Sana, I know you're going through some things right now, but I really think we should move on."

    scene onthecouch20
    with dissolve

    sa "Huh?...What?..."
    sa "Where am I?..."

    "Did my hand really cause all of this?"

    sa "I’m...feeling really tired all of a sudden..."
    sa "And my...throat suddenly hurts..."
    sa "Why is...everything from the last few minutes...such a blur?..."
    s "No clue. But I think it might be good if you maybe try and get some rest."
    sa "Rest?...But you just...got here..."
    sa "It would be..."
    sa "Impolite for me to..."

    scene onthecouch21
    with dissolve

    sa "To..."
    s "..."
    sa "Goodbye."

    scene onthecouch22
    with hpunch
    play sound "thump.mp3"

    "Sana falls off of the couch and narrowly avoids hitting her head on the coffee table."
    "I look down to make sure I don't see any blood, but I'm pretty sure she's going to be okay."

    s "Okay, well...I think it’s time for me to head out."
    s "Do you need me to...carry you to the bed? Or can you handle yourself from here?"
    sa "S-Sensei?...Where are you going?...The bar doesn’t...close for...another hour..."
    s "We’re not at the bar, Sana."
    sa "We’re not?..."
    s "Nope."
    sa "Oh..."
    sa "Are we at school?..."
    s "Yup. Gym class is about to start. It's time to wake up."
    sa "Oh...okay...just..."
    sa "Five more minutes..."

    scene black
    with dissolve2

    "I think about, at the very least, propping Sana up against the couch-"
    "But I realize that it’s probably in everyone’s best interest if I just...don’t do anything at all right now."
    "I’m sure she’ll ‘wake up’ in five more minutes and everything will be just fine."
    "And even though the night ended several steps short of tragedy, I got to hold a cute girl's hand...so everything was worth it."
    "Even if it broke the fabric of reality for a few seconds."

    $ renpy.end_replay()
    $ sanadorm20 = True
    $ sana_love += 1
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ayanedorm20:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label sanadorm:
    if sana_love >= 5 and sanadorm5 == False:
        jump sanadorm5
    if sana_love >= 10 and bar10 == True and sanadorm10 == False:
        jump sanadorm10
    if sana_love >= 15 and sanadorm15 == False:
        jump sanadorm15
    if sana_love >= 20 and bar20 == True and sanadorm20 == False:
        jump sanadorm20
...
```