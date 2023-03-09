# Invisible Worm
Haruka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=harukadate5&go=Go)



## Event preconditions
✅Haruka love greater than or equal to 1

✅Haruka love greater than or equal to 5

✅Event "[Haruka: Drunk Again](./harukadate1.md)" is completed (event=harukadate1)



## Next events
* [Haruka: Performance Review](./harukadate10.md)

## Event properties
* ID: harukadate5
* Group: Haruka
* Triggered by label: callharukanighthang
* Triggered by branch label: callharukanighthang

## Event code
File: \game\HarukaEvents.rpy
Code:
```python
...
label harukadate5:
    "I wonder if Haruka is doing anything tonight?"
    "Now that I think about it, the two of us haven’t really hung out since that night at the bar."
    "Which...definitely makes sense, given the circumstances."
    "Whether or not the alcohol had any influence over Haruka’s decision to shove her tongue down my throat doesn’t change the fact that it happened."
    "And knowing that most people have a much stronger moral compass than I do, I imagine she’s pretty confused about that right now."
    "I would be too, in her position."
    "But that doesn’t change the fact that I want to see her."

    play sound "phonebeep.wav"

    "And so I tap on her name in my phone and wait for her to answer."
    "…"
    "…"
    "…"

    play sound "phonebeep.wav"

    h "Um..."
    h "Hello?..."
    s "Hey, it’s me. "
    h "Yeah, hey. Uhh...what's up? Is..."
    h "Is everything okay with Rin?"
    s "Rin? Yeah."
    s "Why do you ask?"
    h "I...don’t know..."
    h "I just figured that since you were calling, it probably had something to do with her."
    s "So...does this mean I can’t call you to hang out anymore? You're pulling the plug after one time?"
    h "…"

    "An awkward silence separates the two of us more than even the phone does. I can’t tell exactly what she’s thinking, but I know it's nothing good."

    h "I mean...you {i}can.{/i} It’s just..."
    h "It's probably not a good idea."
    s "And why is that?"
    h "It’s..kind of hard to explain..."
    s "Then it would probably be better to do it in person. "
    h "I guess..."
    s "Did you want to come over?"
    h "Huh? To your place? Is that really okay?"
    s "Well, my [niece] will probably come home soon. But as long as I tell her, it’s-"
    h "Just-"
    h "Just...come over here."
    h "Do you need me to pick you up?"
    s "Nah. I remember where it is. "
    s "I’ll be there soon."
    h "...Okay."
    h "I’ll see you then."

    play sound "phonebeep.wav"

    s "…"

    scene black
    with dissolve2

    "Now, I know what you’re probably thinking."

    if bonus == True:
        "Should I really be taking advantage of a lonely woman who is clearly missing her husband right now?"
        "And the answer is probably no."
    else:
        "How {i}do{/i} magnets work?"

    stop music

    if bonus == True:
        "But Haruka’s husband is likely never coming back. "
        "And {i}I’m{/i} here right now."
        "She deserves someone that can make her feel whole again."
    else:
        "No one knows."

    "………"
    "……"
    "…"

    scene harukadatetwo1
    with dissolve2
    play sound "dooropen.mp3"

    h "Hey. Thanks for dropping by."
    s "Don’t mention it. I wanted to see you anyway."

    play music "lastdailysong.mp3"
    scene harukadatetwo2
    with dissolve

    h "Yeah...That’s kind of what I wanted to talk about."
    h "You see, I haven’t really been...entirely honest with you."
    h "And the other night...when I got drunk...I just sort of acted on impulse and-"
    s "And took what you wanted without thinking about it...right?"

    scene harukadatetwo3
    with dissolve

    h "Ngh..."
    h "I..."
    h "Yes..."
    h "I took what I wanted."
    h "But I really shouldn’t have..."
    h "It was a stupid decision and I should have had the willpower to prevent it, drunk or not."
    s "Well, what's the look for? You're not angry at {i}me,{/i} are you?"

    scene harukadatetwo4
    with dissolve

    h "What? No, it’s just..."
    h "Rin told you, didn’t she? About my...situation."
    s "Your {i}situation?{/i}"

    "Of course I know what she’s talking about. But simply coming out and doing all of the work {i}for{/i} Haruka isn’t going to do anything for her."
    "She’s the one who got herself into this mess. And sure, I didn’t do anything to prevent it, but why would I?"
    "Because it’s wrong?"
    "A lot of things I do are wrong."
    "If anything, this seems pretty tame by those standards."

    h "You...really don’t know?"
    s "I never said that. I just want to hear it from you instead of one of my students."
    s "We're both adults. We should be acting like it- not dancing around our feelings because we're afraid of them."

    scene harukadatetwo5
    with dissolve

    h "Yeah...Yeah, that’s fair. I guess I at least owe you that much."
    s "You don’t owe me anything."
    h "No, I do. I was leading you on."
    s "…"

    scene harukadatetwo6
    with dissolve

    h "I’m..."
    h "I'm married..."
    h "And I...have no idea why I've been hiding that from you."

    "Liar."

    h "It’s not your fault...and I hold absolutely nothing against you, but that doesn’t change the fact that I need to stop things now before they go any further."
    h "What happened at the bar was nothing more than an...outburst fueled by alcohol and loneliness."

    if sarainterest == True:
        h "Besides, you already told me you’re into Sara and-"
        s "What does Sara have to do with this?"

        scene harukadatetwo7
        with dissolve

        h "Sara has a ton to do with this. She likes you {i}way{/i} more than me...and it would be wrong on so many levels for me to keep acting on my feelings without thinking about hers."
        s "And what are {i}your{/i} feelings, Haruka?"
        h "Stupid...that's what."
        h "My feelings are stupid and I’m stupid for having them."

        "I can’t find it in myself to respond to her right now."
        "Instead, I watch as her gaze gets trapped within the same walls she likely imagined raising a family inside of."
        "There is no escape. Not now. Not ever."

    else:
        h "Besides...there's still the whole thing with Sara and-"
        s "What does Sara have to do with this?"

        scene harukadatetwo7
        with dissolve

        h "More than you realize."
        h "Do you have any idea how much she likes you?..."
        s "Sara and I barely even know each other. Whatever she thinks she's feeling is fake."
        s "She’s nothing more than a student’s mother to me. And I already told you I’m not interested in her."

        scene harukadatetwo6
        with dissolve

        h "But if you’re not interested in her, then..."
        s "…"
        h "…"

        "A long pause, as if she’s waiting for me to fill in the blanks."
        "But I don’t. I wait for her to fill them in herself."

        h "Are you interested in {i}me?...{/i}"
        s "…"

        scene harukadatetwo7
        with dissolve

        h "I don’t...understand why you would be when someone much more compatible and...unmarried is already throwing herself at you."
        h "I’m just..."

    h "I’m just...really lonely."

    scene harukadatetwo8
    with dissolve

    h "And I’m sure that sounds like a stupid complaint for someone our age, but...I really {i}am{/i} lonely..."
    h "Do you have any idea what it’s like having the person you’ve dedicated yourself to just...disappear one day?"
    h "To have your entire life stripped away from you without so much as a warning?"

    scene harukadatetwo9
    with dissolve

    h "I don’t even know where he is?! Or what he’s doing! Or-"

    scene harukadatetwo10
    with dissolve

    h "Or..."
    h "Or if he’s even still alive..."
    h "And like...I {i}do{/i} love him...Really...I love him so much..."
    h "But I...I can't control my thoughts...I want to, but I can't."
    h "They just keep going and going and going and going and-"

    "Bullshit. "
    "That’s not love."
    "When you’re in love, you don’t stare into someone else’s eyes after a night of drinking and drag them into the issues you’re afraid of facing on your own."
    "You don’t bite down on their lip or lean into them as they massage your chest."
    "You stay away from all of that."
    "Haruka doesn't love her husband at all."
    "If she did, I wouldn't be here."

    s "I get it."

    scene harukadatetwo11
    with dissolve

    h "You do?..."

    if bonus == True:
        s "Of course I do. I can’t even imagine going as long as you have without sex."
    else:
        s "Of course I do. I can’t imagine how hard it is going that without a big ole hug."
        h "............."

    scene harukadatetwo12
    with dissolve

    h "I mean it's...it's more than just that..."
    h "Sex is only...part of it..."
    h "I...miss feeling wanted. Or loved. Or pretty or desirable or any other good thing that I felt before I was all alone."

    scene harukadatetwo13
    with dissolve

    h "The sex thing...definitely makes it worse, though. I won't lie."
    h "I was never really interested in that kind of stuff when I was younger but, like...as soon as I started, it became really hard to hold back whenever I-"

    if bonus == False:
        "Wow. Haruka must really like hugs."

    scene harukadatetwo14
    with dissolve

    if bonus == True:
        h "Ugh...What the fuck am I even saying to you right now?! Talking about this is just going to make it even worse!"
    else:
        h "Ugh...What the Hell am I even saying to you? I already lead you on and now I’m talking about how much I miss hugs..."

    s "Talk as much as you want, Haruka. I don’t mind things like this."
    s "I do want you to know that there are plenty of people who still think you’re pretty or desirable or whatever it is you want to hear, though."

    scene harukadatetwo15
    with dissolve

    h "Knowing that just makes it harder..."
    s "Why? Didn’t you say you just wanted to feel that way again?"

    if bonus == True:
        h "Yeah, but not when feeling that way makes me think I’m some...unfaithful {i}slut{/i} who misses sex so much that she cheats on her husband while he's away."
        s "How long has he been away, if you don’t mind me asking?"
        h "…"
        s "…"
    else:
        h "Because...I'm afraid I don't remember {i}how{/i} to hug."
        s "Gasp."
        h "Yeah, I know."
        s "How long has it been since your last hug?"

    h "Three years, I think."
    s "Three years? How are you even alive?"

    scene harukadatetwo16
    with dissolve

    h "Is that supposed to make me feel better?!"
    s "I'm sorry. That's just...longer than I thought."

    scene harukadatetwo17
    with dissolve

    h "I know..."
    h "Honestly, I probably {i}would{/i} be dead if it wasn't for the local porn shop."

    scene harukadatetwo16
    with dissolve

    h "Ugh! And now I’m doing it again!"
    h "You know, this is also kind of your fault for being so attractive and...making me think things!"

    if bonus == True:
        s "Am I...supposed to apologize for that?"

        scene harukadatetwo17
        with dissolve

        h "No, I..."
        h "My mind has just been wandering all over the place lately."
        h "And more often than not, I feel like it winds up stopping somewhere near you."

        "Ahh, there it is. The admission I’ve been waiting for since this conversation started."
    else:
        "Ahh, there it is. The blunt admission I’ve been waiting for since this conversation started moving toward the hug-zone."

    "From this point on, there are two options."
    "Either I be a good guy and don’t take advantage of Haruka in this moment of desperation- dooming her to wait for a man who may never even return."
    "Or-"

    if bonus == True:
        "I seduce her."
        "And remind her of all the wonderful things she’s been missing out on inside of these walls."
    else:
        "I hug her...even though she's {i}married.{/i}"

    h "…"

    "What should I do?"

    menu:
        "Be a gentleman":
            s "…"
            s "I..."
            s "I should probably leave before this turns into something you’ll regret."

            scene harukadatetwo18
            with dissolve

            "A sigh of relief spreads across Haruka’s face."
            "Her shoulders drop and cause her breasts to bounce which, for a brief moment, remind me of all the joys I will now be missing out on."
            "But the fact is-"
            "I have no place in this woman’s life right now."
            "Not while she is this conflicted."
            "If I am going to take her, I need her mind to be on me and me only."

            if bonus == True:
                "Besides, I have plenty of other girls who are throwing themselves at me on a daily basis."
                "So what if this one is sex-starved and ready to go right now?"
                "It's not like going three years without sex might make her go all out and-"

            s "Okay, yeah. I really do need to get going. My mind is heading in a dangerous direction right now."

            scene harukadatetwo19
            with dissolve

            h "Yeah...I know how that feels."
            h "I’m...sorry to have probably put you through that."
            h "I didn’t really expect this conversation to...devolve so quickly."
            h "I've just been having an admittedly hard time around you lately. "
            h "But I’ll try harder so things like what happened at the bar will never happen again."
            s "You do whatever you need to. I’ll be around if you need me."

            scene harukadatetwo20
            with dissolve

            h "Yeah..."
            h "Thanks."
            h "I’ll...see you some other time, then."
            s "Yeah..."
            s "See you soon, Haruka."

            scene black
            with dissolve2
            play sound "dooropen.mp3"

            "I leave Haruka’s house and walk back down the same street I traversed just an hour or so ago."
            "It sucks that I came this far for essentially nothing."
            "But at the same time-"
            "It's nice being able to end a day without hurting anyone."

            $ renpy.end_replay()
            $ harukadate5 = True
            $ haruka_love += 1

            "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
            "………"
            "……"
            "…"

            if day > 5:
                jump endofsat
            else:
                jump endofweekday

        "Fuck another man’s wife" if bonus == True:
            jump cheatwithharukax
        "Hug another man’s wife" if bonus == False:
            s "Will your husband get mad if we hug?"
            h "I don't know. Will you get mad if I am bad at it?"
            s "How can you be bad at hugging?"
            h "You are about to find out."
            s "Uh-oh."

            scene black
            with dissolve

            h "Take that!"
            s "Why did you just hit me?"
            h "I am trying to hug."
            s "Oh no."

            "Haruka was right. She is very bad at hugging."
            "I'll probably keep trying to teach her, though. Because that is my job. To teach."

            h "Be vanquished!"
            s "Stop it."

            $ renpy.end_replay()
            $ haruka_love += 1
            $ harukadate5 = True
            $ harukasex = True
            stop music fadeout 5.0

            "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
            "........."
            "......"
            "..."

            if day > 5:
                jump endofsat
            else:
                jump endofweekday

label harukadogrep:
        play sound "phonebeep.wav"

        "I press on Haruka's name in my phone and wait for her to answer."
        "........."
        "......"

        play sound "phonebeep.wav"

        h "Hey...What are you doing right now?"
        s "Not much. You?"
        h "Not much..."
        s "Cool, cool."
        h "Uh-huh..."
        s "..."
        h "Um..."
        h "Do you want to come over?"

        scene black
        with dissolve

        "........."
        "......"
        "..."

        if bonus == True:
            jump harukadogrepx
        else:
            $ haruka_lust += 1
            stop music fadeout 4.0

            "{i}Haruka's lust has increased to [haruka_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label harukafirstlust:
...
```

## Code that triggers this event
File: \game\HarukaEvents.rpy
Code:
```python
...
label callharukanighthang:
    if harukanumber == True and day89 == False:
        "I think I should probably get to know Haruka a little better before calling her."
        jump callnight
    if haruka_love >= 0 and day89 == True and harukadate1 == False:
        jump harukadate1
    elif haruka_love >= 0 and haruka_love <= 4 and harukadate1 == True and harukadate5 == False:
        play sound "phonebeep.wav"

        "I tap on Haruka's name in my phone and wait for her to answer."
        "........."
        "......"
        "..."
        "There's no answer."
        "..."
        "I hope she doesn't still feel weird about what happened at the bar the other night."
        "Oh well...I guess I'll just have to...keep visiting her at the cafe or something for now."
        jump callnight
    if haruka_love >= 1 and haruka_love >= 5 and harukadate1 == True and harukadate5 == False:
        jump harukadate5
...
```