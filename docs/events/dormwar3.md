# Imouto Mode!
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar3&go=Go)


Part of event chain [Pre-Game Show!](./dormwar2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwar3
* Group: Main
* Triggered by label: dormwar2

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label dormwar3:
    play music "behindabathroom.mp3"

    "I dream of something peculiar."
    "A sea of flowers sprawls out across a graveyard on the far reaches of a familiar place under a less than familiar sky."
    "As I walk toward the horizon, I notice tangled vines emerging from the ground and wrapping around various tombstones, untouched by humans for quite some time."
    "Though the same can not be said for the touch of time."
    "Edges of graves that may have once been sharp have been eroded by the weather and its incessant desire to switch from summer to winter in the blink of an eye."
    "I stop walking for some reason after reaching a grave much larger than the rest."
    "I can not make out the names on it, but it feels as if someone very important to me is buried here."
    "Or was buried here."
    "I think the important parts of human remains tend to disappear over time, feeding the soil and allowing things like vines to sprawl out as far as the eye can see."
    "I thank the remains for their wonderful contribution to painting this wasteland a plethora of beautiful colors."
    "And then I leave."
    "………"
    "……"
    "…"

    q "...sei?"
    s "…"
    q "S...sei?..."
    s "…"
    a "Sensei...wake up..."

    scene imoutomode1
    with dissolve2

    s "Ami?..."
    a "Good morning, Sensei..."
    a "Or, should I say...onii-chan?"
    s "I mean...you can call me whatever you want I guess. But that doesn’t explain why you’re waking me up at..."
    s "What time even is it right now?"
    a "It’s only 7:00."
    a "I know you like to sleep later normally, but certain...circumstances meant that I had to wake you up a little earlier than normal."

    scene imoutomode2
    with dissolve

    a "But, to make up for it, I cooked you breakfast and brewed you coffee! Isn’t that sweet of me, onii-chan?"
    s "This is weird. "
    a "What’s weird about taking care of my big brother?"
    s "Probably the fact that I am suddenly your big brother and not your [uncle]."

    scene imoutomode3
    with dissolve

    a "It’s part of the contest..."
    a "I have to compete with Noriko to show her that I’m the only person fit to take care of you..."

    if bonus == True:
        a "And I know it probably sounds a little weird since you’ve always looked at me as a [niece], but...I’m {i}kind of{/i} like a little sister too, right?"
        a "Like we could completely change roles and it wouldn’t be any different at all."
    else:
        a "And I know it probably sounds a little weird since I am your accountant and we are not at all related...but I really do think I'm the better housegirlperson."

    s "Yeah, if that’s the whole point of the contest, you kind of do have the upper hand."

    scene imoutomode2
    with dissolve

    a "Right! Which is why I’m sure you’ll pick me no matter what I do."
    a "Lucky for you, all I {i}want{/i} to do is take care of you and make you happy, so doing stuff like bringing you breakfast in bed is no trouble at all."
    a "Now go ahead and eat up! We have lots to do today, onii-chan."

    scene imoutomode4
    with dissolve

    if bonus == True:
        a "And maybe...lots to do tonight as well?..."
        u "Ooooh! A secret, suggestive attack this early in the contest?! Ami truly is a force to be reckoned with!"
    else:
        a "And maybe...I'll spare your life~"
        u "What's this?! A yandere attack?!"

    scene imoutomode5
    with dissolve

    s "Oh. I guess you two are here as well."
    s "This totally isn’t weird or anything."

    mak "Ew..."

    if bonus == True:
        mak "You do remember that you two {i}are{/i} actually related, right?..."
        a "If it’s with onii-chan...I don’t care~"

    u "Don’t mind us, Sensei! Just takin’ notes and makin’ sure nothing weird happens!"
    u "Just feel free livin’ up the fantasy until it’s time for Noriko’s turn."

    play sound "knock.mp3"
    with hpunch

    n "Noriko?! Is it my turn?! I’m ready whenever!"
    a "Stay out there, demon! I’ve barely had any time at all!"
    n "Ughhhhh fine! But only because I love you!"

    scene black
    with dissolve

    "I lean up in bed and slide further away from Uta and Makoto, who have more than likely been taking notes on...how I sleep or something."
    "I don’t really know what they were doing before Ami woke me up, but I’m not really in any rush to find out."

    if bonus == True:
        "Unless it was something sexual. Then I’d want to find out right away."
        "But it probably wasn’t so...nevermind, I guess."

    scene imoutomode6
    with dissolve

    "I quickly eat the breakfast Ami made for me and finish it off with coffee."
    "Just as always, it was exactly to my liking. But at this point, I don’t really expect anything less of her."
    "In fact, if she ever made anything that {i}wasn’t{/i} exactly to my liking, I’d take it as a sign of an emergency and quickly rush her to the hospital to make sure she isn’t dying."
    "Thankfully, she is not dying today."
    "Instead, she’s just clinging to my arm while two of her classmates look on and take notes."
    "Yup, it’s a completely normal morning."

    a "You know, onii-chan...it isn’t often that we get to be as close as this in front of others..."
    a "Would you believe me if I told you I was feeling a little...embarrassed?"
    s "I wouldn’t. I bet you’re loving this right now."

    scene imoutomode7
    with dissolve

    a "Hehehe~"
    a "You’re right..."
    a "I love my big brother more than anything else in the whole wide world. And I don’t care who knows it."
    a "So feel free to wrap your arms around me and pull me close if you want!"
    a "Or just let me cling to you like this."
    s "…"
    a "…"
    s "So is this really all this competition is?"

    scene imoutomode8
    with dissolve

    a "Mmm...I think so?"
    a "We didn’t really come up with any rules. I’m just supposed to prove that I’m the ideal sister."
    a "And I know you like time to wake up in the morning, so I can’t really do anything exciting."
    a "I’ll just sit here with you and be cute and expect you to make the right choice."
    s "It’s not like I mind or anything, but..."
    a "But what?"
    a "You want me to go the extra mile for you?"
    mak "Objection, that’s-"
    u "Shh! I wanna see what this “extra mile” is!"

    play sound "knock.mp3"

    n "Hey! Isn’t that long enough? "
    n "How am I supposed to compete if Ami’s going to take up like a whole hour in there?"
    mak "Hmm...it is getting close to the ten minutes we allotted her."
    u "That’s right...Letting Ami go any longer would mean we’d have to let Noriko do the same. "
    u "And the rest of the girls should already be heading to the park for the next contest right now."

    scene imoutomode9
    with dissolve

    a "Onii-chan...they’re trying to take me away from you..."
    a "It’s just like at the orphanage...where that mean family wanted to adopt me and use me for all sorts of gross things...but you stepped in and saved me..."
    s "…"
    s "What?"
    a "Then...as soon as we became old enough...we went out on our own..."
    a "And then...after falling asleep in each other’s arms in that cold, broken down house...we realized that we were no normal brother and sister-"

    play sound "dooropen.mp3"
    scene imoutomode10
    with dissolve

    n "Okay, I’ve waited long enough. "
    n "Tell Ami to step down before she gets any further into her backstory or I’ll basically lose before I even have a chance."
    u "Good point, Noriko. "

    if bonus == True:
        u "I’ve gotta say, as soon as she broke out the orphan thing, even {i}I{/i} started to get won over, and I’m not even on her team."
        a "I didn’t even get to the part with the graveyard yet."
    else:
        a "Wait, no! I still haven't gotten to the part with the musical number!"

    mak "You are absolutely disgusting. "
    mak "Noriko, please step in before this competition gets any more...[incest]uous."

    scene imoutomode11
    with dissolve

    n "I mean, gladly. But isn’t the whole competition conceptually [incest]uous?"

    if bonus == True:
        mak "Yes...but you and Sensei aren’t {i}actually{/i} related."
        s "Makoto is desensitized to fake [incest] thanks to all of the porn she watches with her mom and-"

        scene imoutomode12
        with hpunch

        mak "I have never once watched anything like that with my mother! "
        s "Whatever you say, Makoto."
        mak "Ami! Please leave the room now!"
        mak "You already have the advantage in that you got to be the one to wake Sensei up. So Noriko already has to figure out a way to overcome that handicap and-"
    else:
        mak "Yes, but only in a wholesome way that doesn't break any rules. Besides, you already have a handicap to overcome in going {i}after{/i} Ami."

    scene imoutomode13
    with dissolve

    n "Oh, you don’t have to worry about that. "
    mak "What do you mean? Do you already have a plan on how to counter that?"
    n "Yup! And if Sensei drank all of his coffee, then my counter attack should be kicking in any second now."
    s "I’m sorry, what?"
    a "Did..."

    if bonus == True:
        jump norikoimoutox
    else:
        a "Did you give my [uncle] a sleeping potion?!"
        n "Mwahahahaha. I have been an evil villain all along!"
        s "Noriko, how could you?"
        n "Sleep, Sensei!"
        n "But choose a winner first!"

        scene black
        with dissolve

        s "I am dying."
        a "Sensei!"
        u "Wait! No! You really do have to choose a winner! It's part of the event!"
        s "Help."
        mak "Just choose, please..."

        "Who is the better whatever?"

        menu:
            "Ami wins":
                $ imoutoami = True
                $ dorm1warpoints += 1

                s "I........pick...............Ami........"
                n "REEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE"

                $ renpy.end_replay()
                $ dormwar3 = True
                stop music fadeout 5.0

                "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
                "………"
                "……"
                "…"

                jump dormwar4

            "Noriko wins":
                $ imoutonoriko = True
                $ dorm2warpoints += 1

                s "I........pick...............Noriko........"
                a "What?! Why?!"
                s "Because.......she......"
                s "Brought me.......pizza rolls............."
                n "I knew those would come in handy one day!"
                a "FUUUUUUUCK!"

                $ renpy.end_replay()
                $ dormwar3 = True
                stop music fadeout 5.0

                "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
                "………"
                "……"
                "…"

                jump dormwar4

label dormwar4:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```