# Token Tsundere
Yumi event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=streets20&go=Go)



## Event preconditions
✅Yumi love greater than or equal to 20

✅Event "[Yumi: Apples to Apples](./streets15.md)" is completed (event=streets15)

✅Event "[Tsuneyo: Snake Venom](./ramen1.md)" is completed (event=ramen1)



## Next events
* [Yumi: Great Expectations](./yumidorm20.md)

## Event properties
* ID: streets20
* Group: Yumi
* Triggered by label: streets
* Triggered by branch label: streets

## Event code
File: \game\YumiEvents.rpy
Code:
```python
...
label streets20:
    scene yumipizza1
    with dissolve
    play music "yumiska.mp3"

    y "...and that’s exactly what I fucking hate about cafes!"
    y "They’re always worried about like, “Oh, customer this, customer that!” but what about the fucking {i}employees{/i}?"
    y "Like, do they realize that employees are the fucking BACKBONE of businesses like that?!"
    y "Keeping them happy matters more than anything else!"
    y "So what if I offered to beat some dude’s face in for trying to scam the store? Shit like that shows {i}dedication!{/i}"
    y "Fucking unreal."

    "As you can see, Yumi is still a little upset about not getting the first job she applied to."
    "But, in all fairness, I’m sure we can all understand why. "
    "It’s one thing to actually follow through on some of her...problem-solving techniques, but talking about them in a job interview is a completely different matter."

    s "Well hey. At least you did your best. "
    s "And now you have pizza, so all is well."

    scene yumipizza2
    with dissolve

    y "Whatever...It’s not like I wanted pizza or anything."
    s "Is this what we’ve come to? Token tsundere lines and complaining about cafes?"

    scene yumipizza3
    with dissolve

    y "Stop fuckin’ calling me tsundere!"
    y "The “dere” part implies that I actually fucking like you which I {i}clearly{/i} do not. I barely even like pizza!"
    s "Okay, now that’s just flat out untrue. Everyone likes pizza."

    scene yumipizza2
    with dissolve

    y "Wow, one more thing preventin' me from fitting in with everyone else. Who woulda guessed?"
    s "Insecurities aside, what do you think our next course of action should be?"

    scene yumipizza4
    with dissolve

    y "Probably {i}eating{/i} the stupid pizza, dipshit. That’s normally what you do after you buy one."
    s "I meant about the job hunt..."
    y "Oh."
    y "Well how the fuck would I know? This was all your idea."
    y "Don’t tell me that confidence was all just another front to make yourself look cool?"
    y "Wait, you don’t even have money for the pizza, do you? This was all one big scam, wasn’t it?"
    s "I literally paid for this already. "

    scene yumipizza5
    with dissolve

    y "Listen, dude...Maybe it’ll be better for both of us if we just fuckin’ stop the job search here."
    y "We clearly don’t like being around each other and this is only making things worse."
    s "I like being around you, though."

    scene yumipizza1
    with dissolve

    y "Well I don’t like being around you! So my idea stands!"

    "Maybe a new sort of strategy is needed?"
    "Yumi is clearly not an average girl, so maybe it’s best to find her a job that...isn’t entirely average to begin with?"
    "Do people still deliver newspapers? Maybe that’s a thing she can do?"

    s "How do you feel about newspapers?"
    y "…"
    s "…"

    scene yumipizza6
    with dissolve

    y "Huh?"
    s "You know. Like...being a delivery girl."
    y "I know you’re a fuckin’ dinosaur, but how old do you think {i}I{/i} am?"
    y "Isn’t shit like that meant for like, 10 year olds or whatever?"
    s "I think it’s more about work experience than age. And you have virtually none, so..."

    scene yumipizza7
    with dissolve

    y "That’s not true. I’ve been running my own business for almost two years now."
    s "Stealing and selling old TVs doesn’t exactly count as running a business, Yumi."
    y "It’s not just TVs. There’s candy too."
    y "Sure, a lot of that goes to Chinami, but it’s not like I don’t scam grade[school]ers on their way to class every now and then."
    s "Wait, do you really?"
    y "Obviously. Who else is gonna fuckin’ buy candy from me? You have any idea how sketchy that looks?"
    s "Maybe we just...need to get you a job at a candy store?"

    scene yumipizza8
    with dissolve

    y "Good luck finding one I haven’t already lifted. Pretty sure I’ve got my picture in almost every convenience store in Kumon-mi at this point."
    s "Well how about this...Tell me what sort of job you’d be interested in."
    s "List a few qualities, and I’ll just...try and come up with something suitable."

    scene yumipizza6
    with dissolve

    y "You mean like you did with the cafe? That sure worked out well, didn’t it?"
    s "Okay, that wasn’t entirely my fault. I just overestimated your ability."
    y "Oh, fuck off with that. You just wanted to see me embarrass myself."

    scene yumipizza8
    with dissolve

    y "But at least I got dinner out of it so...whatever."

    "Yumi takes a deep breath and watches a few cars as they drive by."
    "We’re in an area of the city that neither of us have really been to before, so I imagine she’s trying to scope out a store she hasn’t been caught stealing from yet."
    "That or she’s just watching the sunset. But, let’s be real, {i}Yumi{/i} watching the sunset? Come on."

    s "So, any ideas?"
    y "Somewhere quiet, but like, not too quiet. I guess that’s one thing I’d like."

    scene yumipizza7
    with dissolve

    y "Also, somewhere I’d be able to eat for free."
    y "Making money would be nice and all but, being able to save it would be even better."
    y "And if I don’t have to pay for food, that’ll be a lot easier."
    s "That’s...surprisingly pragmatic of you."

    scene yumipizza3
    with dissolve

    y "The fuck did you just say to me, douchebag?!"
    s "Yumi, pragmatic means sensible."

    scene yumipizza7
    with dissolve

    y "Oh."
    y "Uhh, thanks then."
    s "Right..."
    s "Any other qualities before we start narrowing down the list?"
    s "We’ve already got...mildly quiet and free food. I think we can do a little better than that."

    scene yumipizza8
    with dissolve

    y "Uhh...I guess somewhere close to Chika’s place would be good."
    y "It’s kind of shitty having to walk back and forth between districts all the time."
    s "Are you really walking that far every day?"

    scene yumipizza4
    with dissolve

    y "You have any idea how hard it is to steal a bus ride? What else am I gonna fuckin’ do?"
    s "I think we need to buy you a pair of shorts or something. I can’t imagine it feels nice to be walking miles in a skirt that long for the entire summer."

    scene yumipizza3
    with dissolve

    if bonus == True:
        y "Hey! Get back to the fuckin’ topic at hand and stop picturing me without my skirt on!"
        y "I realize that might be pretty fucking difficult for you, but you should probably mind your own business when it comes to what I fucking {i}wear{/i}."
        y "At least let me have some freedom over that if you’re going to try and control every other aspect of my life."
    else:
        y "I really like this skirt!"

    s "Wow, you really like that skirt, don’t you?"

    scene yumipizza9
    with dissolve

    y "Oh. My. Fucking. God."
    s "Okay, okay. Moving on."
    s "Mildly quiet. Free food. Old district."
    y "…"
    s "…"

    "I scan through countless unimportant memories stored in my brain and try to locate something that might fit Yumi’s qualifications."
    "I can’t say I go to the old district all that often, but..."
    "There is one place that sticks out in my mind."

    if ramen10 == True:
        "But...I already know that Tsuneyo didn’t want to hire Kaori."
        "And if someone as...suspiciously talented as her wasn’t hired, Yumi’s chances seem pretty slim."
        "But oh well, I guess."
        "Life is all about failing before figuring out what the right way to do things is."
        "Maybe Yumi just needs to fail again in order to...find motivation or something?"

        s "What about the ramen shop?"

    else:
        s "What about the ramen shop?"

    scene yumipizza7
    with dissolve

    y "Ramen shop? What ramen shop?"
    s "The one that Chika tried to make us eat at a while back."

    scene yumipizza10
    with dissolve

    y "Oh. That place."
    y "Kinda forgot since I was only in there for like, two minutes."
    y "But uhh...doesn’t Noodles work there?"
    s "No. Noodles is a bird. He doesn’t work."
    y "…"

    scene yumipizza6
    with dissolve

    y "Are you high?"
    s "No. But I guess you wouldn’t know the real Noodles anyway."
    y "Again, are you high?"
    s "Again, no. You’re talking about Tsuneyo, right?"

    scene yumipizza10
    with dissolve

    y "Is that her name? I just know her as the weird girl who talks like a robot."
    s "Yeah, definitely Tsuneyo."
    s "Is it a problem if she works there?"

    scene yumipizza7
    with dissolve

    y "Well...I mean, it wouldn’t be a {i}problem{/i} if the two of us were to work together...At least she doesn’t say much."
    y "Better than the other new girl, at least. That one’s fucking insane."
    s "Yeah, that’s a fair assessment of Molly. I worry about her."
    y "You think I’d be able to handle some place like that?"
    s "Do you actually want my opinion or is that a rhetorical question?"

    scene yumipizza10
    with dissolve

    y "I mean it...for real."
    y "I kind of felt like you just threw me into the fire at the last place, and I’m trying not to get my hopes up again if it’s the same thing this time."
    s "Well let me ask you this, did you expect finding a job to be easy?"

    scene yumipizza11
    with dissolve

    y "Uhh...yeah. Kind of."
    y "Chika didn’t have any problem finding one when her mom died. It was like, the first thing she did."
    y "But I feel like people take one look at me and think I’m just going to beat the shit out of them or something."
    s "To be fair, saying that you’re going to beat the shit out of them probably doesn’t quell that notion at all."
    y "Yeah, it really doesn’t."
    y "But maybe I can try a new approach at this noodle place?"
    s "You mean...you’re going to act normal?"

    scene yumipizza10
    with dissolve

    y "No harm in trying, right? Not like being myself helped at all last time. The cafe would have been a sweet gig, too."
    s "…"
    y "...Are you tearing up right now?"
    s "You’re growing up so fast..."

    scene yumipizza3
    with dissolve

    y "Who do you think you are, my dad?! Stop fucking crying, you pussy!"
    s "I didn’t mean to, I’m just so proud."

    scene yumipizza12
    with dissolve

    y "I haven’t even fuckin’ done anything yet! At least save your stupid tears for when I’m actually hired!"
    y "{i}If{/i} I’m actually hired, that is. That place is still sketchy as fuck."
    y "Pretty sure it’s the same one a lot of the people I used to chill with would hang out at every night."

    scene yumipizza13
    with dissolve

    y "Are you going to be there, too?"
    y "Not because I want you there, obviously. But because maybe you could...put a good word in for me or something."
    y "Noodles seems to like you, so maybe you can help...you know, talk me up or something."
    s "Of course. I’ll be sure to tell Tsuneyo about all of your amazing qualities and qualifications."

    scene yumipizza14
    with dissolve

    y "Actually, on second thought, how about you just go fuck yourself and I head over there alone?"
    y "I can’t imagine your word would be good for anything even {i}if{/i} Noodles likes you just as much as the rest of your fuckin’ harem."

    scene black
    with dissolve2

    "Yumi and I finish the pizza and I give her a few pointers about how to conduct herself in a job interview."
    "To be honest, I don’t know if any of those pointers will apply to an interview held by someone like Tsuneyo, but..."
    "I guess we’ll just have to wait and see."
    "Yumi and I decide that we’re both tired of talking about job-related stuff and make plans to reconvene at the dorms in the future to strategize."
    "For now, though, she asks to be left alone and I’m suddenly left wandering around on my own in yet another unfamiliar part of the city..."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ streets20 = True
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label streets25:
...
```

## Code that triggers this event
File: \game\YumiEvents.rpy
Code:
```python
...
label streets:
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        jump satafternoonmenu
    if yumi_love >= 0 and firsttimestreets == False:
        jump firsttimestreets
    if yumi_love >= 5 and streets5 == False:
        jump streets5
    if yumi_love >= 10 and day44 == True and streets10 == False:
        jump streets10
    if yumi_love >= 15 and yumidorm15 == True and streets15 == False:
        jump streets15
    if yumi_love >= 20 and streets15 == True and ramen1 == True and streets20 == False:
        jump streets20
...
```