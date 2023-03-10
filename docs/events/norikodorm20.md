# Homes for the Homeless (Noriko)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Noriko love greater than or equal to 20

* Event [Fair & Square](./norikospecial20.md) (Noriko) is completed)



## Next events

* [Noriko: That One FMK Scene](./convenience25.md)

## Event properties

* Id: norikodorm20
* Group: Noriko
* Triggered by label: norikodorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->norikodorm->norikodorm20

## Official wiki page

[Homes for the Homeless](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=norikodorm20&go=Go) for more details.

## Event code

File: (install folder)\game\NorikoEvents.rpy

Code:
```python
...
label norikodorm20:
    play sound "knock.mp3"

    "I knock on Noriko’s door and wait for her to answer."
    "And, now that she’s managed to get her completely unnecessary apology out of the way, I expect tonight to be mostly drama-free."
    "Or at least that would have been the case before I thought of that. "
    "Now, I worry that I may have jinxed myself."

    stop music fadeout 10.0

    "Oh well. Worse comes to worst, I just let her waste her breath and apologize for something {i}else{/i} she doesn’t have to apologize for when it’s all said and done."
    "I’ll truly never stop being thankful for how predictable most [teenager]s are-"
    "And how even the slightest whiff of love can cause their brains to go haywire."

    play sound "knock.mp3"

    s "Noriko, are you in there?"
    n "Oh, Sensei! Yeah! I didn’t hear the first knock."
    n "You can come on in."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I make my way into Noriko’s room to be assaulted by the same fruity scent of energy drinks that I’ve grown used to when visiting her and Kirin."
    "Today’s scent is particularly potent, however. And if there’s anything I know about energy drinks-"
    "It’s that Noriko will be exactly the same as always because the “energy” aspect is a myth perpetuated by big beverage companies to trick [teens] into buying products that will-"
    "help them cope with the extreme mental strain of [high_school] life and its accompanying exhaustion before ultimately becoming addicted and drinking them until their kidneys are filled with stones."
    "Just kidding."
    "I’ve never had an energy drink."
    "I’m sure they’re okay."

    scene norikochinadress1
    with dissolve2
    play music "love.mp3"

    s "Oh, wow."
    n "Good wow or bad wow? What kind of wow is that?"
    s "Just...can’t say I was expecting this."
    n "How does it look? Be honest. I can take it."
    s "It looks...great. I’m just confused about why you’re wearing it."

    scene norikochinadress2
    with dissolve

    n "My parents sent it to me."
    n "They just redid the decor of the restaurant and they’re trying out new qipao to fit the color scheme. And of course Nee-chan is too busy to model for them anymore, so...voila. "
    n "Fancy Noriko."
    s "I like fancy Noriko. It doesn’t hurt my eyes trying to keep up with the outfit."

    scene norikochinadress3
    with dissolve

    n "Hey! There wouldn’t be a need for me to dress the way I do if it weren’t for the necessity to fight back against societal expectations and the inherent Japanese obsession with professionalism!"
    n "Dressing in stuff that’s overcomplicated or hard to follow is just one of many ways I push back against what people expect of me! I’m fighting the power!"
    s "Right. And what are the {i}other{/i} ways you fight back against society’s expectations of you?"

    scene norikochinadress4
    with dissolve

    n "I pierced my belly button. Does that count?"
    s "What? No. And since when? I saw you in a swimsuit very recently and I do not remember that at all."
    n "My parents made me take it out because it got infected."
    s "You truly are one of the great rebels of this generation, aren’t you?"

    scene norikochinadress5
    with dissolve

    n "I know that I’m not {i}actually{/i} rebelling in any way. But, to be fair, what could someone my age even do?"
    n "The best chance I’d have is starting a band and just hitting it big like that. But even then, there are a gajillion others trying to do the same thing."

    if bonus == True:
        n "Teenagers don’t really have a voice, Sensei. {i}Especially{/i} [teenage]girls. "
    else:
        n "But hey, if Nickelback can do it, I can too."

    s "Hey, I’m not trying to tear you down. I’m just saying that it wouldn’t kill you to look a little more...normal from time to time."

    scene norikochinadress6
    with dissolve

    n "Normal like this? Because I feel like I’d get a lot more stares going out in a qipao than I would in a brightly colored flannel with...chains and stuff."
    n "Besides, being {i}pretty{/i} is kind of Nee-chan’s thing now. "
    n "There’s no way I was ever going to be able to seriously compete with her once she started trying, so I just...wound up going a different route."

    scene norikochinadress7
    with dissolve

    n "I thought that route would be to your liking, Sensei."
    n "A brand new Noriko would mean a brand new start to our relationship, wouldn’t it?"
    s "Just changing your clothes doesn’t change the person you are. And even if it did, you’d be brand new to me anyway. "
    n "Those memories are still in there somewhere. All the parts of the me in the past that you'd want to hang onto are still there."
    n "There are just a lot of other parts that come included now as well."

    scene norikochinadress8
    with dissolve

    if bonus == True:
        n "And some {i}other{/i} parts that have been improved in a number of ways. But I’m sure I don’t need to remind you of those."
    else:
        n "And some other parts that have been improved in a number of ways. But I'm sure I don't have to remind you of my Squidward tattoo."

    s "You certainly do not. In fact, I have a picture message saved in my phone to back that claim up."

    scene norikochinadress9
    with dissolve

    n "Sure wish I had something similar in {i}my{/i} phone."

    if bonus == True:
        s "I can’t send you a picture of my penis, Noriko. That would be putting way too much power in the palm of your hand."

        scene norikochinadress10
        with dissolve

        n "I wouldn’t do anything with it, I swear!"
        n "Well...nothing involving anyone else! It would be for personal use only! "
        s "No can do. I’ll gladly accept any other photo you want to send me, though."
    else:
        s "For the last time, I am not getting a Squidward tattoo."

    scene norikochinadress11
    with dissolve

    n "Mmm...meanie."

    if bonus == True:
        s "Like...I don’t know. Maybe one in some sort of...Chinese dress?"

        scene norikochinadress12
        with dissolve

        n "If you wanna see more of this, why not come to my parents’ restaurant with me sometime?"
        n "They’d be really happy to see you {i}and{/i} you’d get to see me serve people in this thing."

        scene norikochinadress13
        with dissolve

        n "And who knows? Maybe I could {i}serve{/i} you too?"
        s "Bold claim for someone who has only dry humped me so far."

        scene norikochinadress14
        with dissolve

        n "Ah~ The best dry humping of my life, too..."
        s "...How many people have you done that with?"

        scene norikochinadress15
        with dissolve

        n "People? Just you. But then there’s stuff like pillows and...blankets if you curl ‘em up just right...and the corner of your desk..."
        s "Excuse me?"
        n "What? It smelled like you and there was no one else in the classroom."
        s "…"
        n "I’m a growing girl. I get urges."
        n "Those urges just happen to be exponentially greater around things that you have touched."
        s "If that were true you’d have already fucked Kirin by now."

        scene norikochinadress16
        with dissolve

        n "Hey...come on."
        n "I obviously know that things have happened between you two, but you don’t need to remind me about it like that. That’s just mean."
        s "I was just kidding. I didn’t mean anything by it."
        n "You don’t have to apologize or anything, just...try not to bring other girls up if you don’t have to."
        s "…"
        n "…"

        scene norikochinadress17
        with dissolve

        n "Uhh...A-Anyway! Why don’t we sit down and go back to talking about...my parents or something?! That should stave away the horny for a little while longer, don’t you think?"
        s "The last time we tried that, I’m pretty sure you imagined me fucking your dad."

        scene norikochinadress18
        with dissolve

        n "Ewwww, Dad! No! That’s {i}my{/i} boyfriend!"
        s "And apparently you are already doing it again..."
    else:
        s "Just shut up and keep modeling so we can get on with the event."

    scene black
    with dissolve2
    stop music fadeout 15.0

    if bonus == True:
        "It takes Noriko a minute or two to stop fantasizing about a thing I really wish she wouldn’t fantasize about."
        "But after that, we manage to steer clear of “the horny” and move both locations and topics into territory we’re a bit more comfortable with."
        "Well, territory {i}she{/i} is more comfortable with."
        "To be honest, if she came out right now and asked me to do what I refused to do to her outside of the Halloween party, I wouldn’t have a second thought."
        "My hand would be buried deep inside of that sleek, Chinese dress...doing the same things to her I did to her sister in that fancy hotel room."
        "I wonder if they’re just as similar on the inside as they are on the outside."
        "I wonder how long it will take for me to find out."
        "I wonder-"
    else:
        "Noriko gets angry at me for rushing the video game and immediately skips to the next part of the event, cutting out a sizable chunk of content and ruining context in the process."

    if bonus == True:
        play sound "static.mp3"
        scene lavendersgreen1 with flash
        scene lavendersgreen13 with flash
        scene lavendersgreen18 with flash
        scene lavendersgreen23 with flash
        scene lavendersgreen29 with flash
        scene lavendersgreen30 with flash
        scene norikochinadress19 with flash
        play music "blueair.mp3"
        stop sound
    else:
        play sound "static.mp3"
        scene norikochinadress19 with flash
        play music "blueair.mp3"
        stop sound

    "I don’t wonder anything."
    "I stop thinking because I have to stop thinking."
    "Thinking more will be bad."
    "Noriko loves me."
    "Noriko won’t mind if I-"

    n "You’re being weird again."

    scene norikochinadress20
    with dissolve

    s "…"
    n "Like when we walked home from[school]."
    n "You’ve done it a few times before that too."
    n "There are these like, long stretches of time where you’ll be there and you’ll be responding, but it won’t actually be {i}you{/i}, you know?"

    scene norikochinadress21
    with dissolve

    n "Well, they’re not all {i}long{/i}, I guess. Like, this time, it was really only for a minute or two."
    s "That just happens sometimes, I guess."
    s "{s}It could be dangerous.{/i} It’s not really something you should worry about."
    n "I never said I’m worried. If anything, I’m glad I can be here for them."
    n "It’s a lot better knowing that you have me as an outlet to vent to if you ever want."
    n "Not like you {i}would{/i} ever want to do that, though, when you’ve always been pretty secretive about the things that are bothering you."
    n "Like, back when we were always with Maya-"
    s "Don’t talk about Maya right now."

    scene norikochinadress22
    with dissolve

    n "I mean...fine by me. But why not?"
    s "It’s just...not a good idea, I think."

    "Half of me wants to hear whatever it is Noriko has to say."
    "But another half of me that I thought I’d kept at bay is now begging me to steer clear on the off chance that Maya’s thoughts are right and that...learning too much might be bad."
    "And here I was thinking I’d be able to not take her advice."
    "How annoying."

    scene norikochinadress23
    with dissolve

    n "What do you want to talk about instead, then?!"
    n "I feel like tonight’s been pretty much all about me, so if there’s anything you want to say-"
    s "Keep talking about yourself."
    s "You said on Halloween that you wanted me to know more about {i}you{/i}. So tell me more about you."
    s "Where do you want to go after [high_school]? What do you want to be? Just talk."
    s "I don’t really care what it’s about."

    "I just need something to distract me."
    "I need to stop slipping."
    "I need to focus on the task at hand...getting to know Noriko and everyone else without..."
    "Without thinking at all."
    "I need to grind affection points."
    "Wait, what are affection points? "
    "What am I thinking?"
    "{s}Have I really spent so much time with Molly that it{/s} {b}HAVE RECENT EXPERIENCES SOMEHOW{/b} led to me treating life more like a game than I ever thought I would?"
    "I know those were essentially {i}my{/i} words last Halloween when-"

    play sound "static.mp3"
    scene samhain21 with flash
    scene samhain33 with flash
    scene norikochinadress23
    with flash
    stop sound

    "Molly and Tsuneyo are two girls who like me and appreciate me and admire me."
    "They will forget this the next time the world resets. "
    "Ignore it and it will go away."
    "Noriko, please break this silence."
    "Please."

    n "I think..."
    n "That what I’d want to do more than anything is help people."
    s "{s}Help me{/s} How?"

    scene norikochinadress24
    with dissolve

    n "I don’t know...charity work, maybe?"
    n "Ideally, I’d love to do something along the lines of like...building homes for the homeless, or...teaching underprivileged kids how to read."
    n "But, unfortunately, there’s just not really any money in stuff like that."
    n "It’s really sad, you know? All the nicest, best things out there have to be done by people willing to sacrifice their well-being in order to do it."
    s "And that’s something you’re considering?"
    n "I don’t really know."
    n "I mean, I’m in [high_school]."
    n "Things I say right now don’t really matter. It’s what I say {i}after{/i} I graduate that matters. And anything can happen between now and then."
    n "It would just be nice to kinda...change the world. You know?"
    s "You’re never going to change the world."

    scene norikochinadress25
    with dissolve

    n "I’m not?"
    s "{s}We’re stuck here.{/s} I highly doubt it."
    s "{s}Nothing can be changed.{/s} “Changing the world” is something a lot of people your age plan on doing."
    s "{s}Something is buried underneath your feet.{/s} Then, once they get out of [high_school], they realize it’s impossible and fall into the same slump all people fall into."

    if bonus == True:
        s "{s}You will never find it.{/s} They get jobs. Go to work. Go home. Fuck whoever they’re living with. Fuck themselves if they don’t have anyone there. Sleep. And then repeat."
        s "{s}It might not even exist.{/s} The world can’t be changed. There are too many people trying to prevent it from changing that it offsets all of the people who are."
        s "{s}Does any of this exist?{/s} If you want to waste away your life pursuing such a pipe dream, feel free. But don’t let it break your spirit when it doesn’t pan out how you want."

    n "Are you sure your memories are broken?"
    s "What?"
    n "It’s just that you said essentially the same exact thing to me when I was little."
    n "Which, at the time, was pretty upsetting since I was still just a kid."
    n "But hey, it prepared me for {i}not{/i} getting upset this time around, so at least that’s good."
    s "Have we really had this discussion before?"
    n "More or less. Just, minus the whole “[high_school]” part of it."
    s "Well...at the end of the day, you’re still just a [teenager]. Any “difference” you could make wouldn’t happen until you’re much older."

    scene norikochinadress26
    with dissolve

    n "I mean...yeah. But is that {i}really{/i} all I am? Because my time with you has made me feel like I’m a little bit more than that."
    s "The time I do remember? Or the time I don’t? Because I don’t really think I’ve done anything substantial since you walked back into my life."
    n "Before."
    n "You were no normal tutor, Sensei. Like, sure you helped us with our general studies and reading comprehension and all that..."
    n "But a lot of the things you taught us were those same cynical spiels about how the world will never change or how...time is a bitch..."
    n "And all this other stuff most girls would get weirded out by."
    n "We loved you, though. So we listened."
    n "We ate up every word and, soon enough, we started to echo those feelings."
    n "But the interesting thing about feelings is that they don’t work the same way in all people."
    n "And once they’re inside of you, they evolve and adapt in ways that make them much more than echoes. They’re closer to like...screams or...encryption keys or something."
    n "But {i}you{/i} were the one that helped us realize we were more than just average girls."
    n "My decision to go down the path of finding my own sense of...individuality was a lot more than just wanting to detach myself from Nee-chan."
    n "It was me doing something I thought would make you proud. "
    n "It was me turning into a person that wouldn’t ever fit into one of those cynical analogies you’d tell some other [young_girl], still naive to the world around her."
    n "It was me following in your footsteps, even when I had no idea where they were, what they looked like, or where they were heading."
    n "Like it or not, you were always my role model. And you’ll probably always {i}be{/i} my role model."

    scene norikochinadress27
    with dissolve

    n "Even when you think you’re the worst human being in the world...that you’re absolute shit...something I {i}know{/i} you feel sometimes..."
    n "Even then, I will be here to remind you that you are more than that."
    n "Underneath all of that pain and anguish and...defeat is the man who single handedly turned me into the girl I am today."
    n "Maya, too. She {i}definitely{/i} wouldn’t be who she is if it wasn’t for you."

    scene norikochinadress28
    with dissolve

    n "But that’s why I haven’t {i}entirely{/i} given up on changing the world yet."
    n "If {i}you{/i} weren’t able to, maybe it’ll make you feel a little better if I can. "
    n "Or, at the very least, show you that you left some sort of positive mark on the world instead of just some giant shadow..."
    s "…"
    n "…"

    scene norikochinadress29
    with dissolve

    n "So! What’s the plan for Christmas?"
    n "Wanna go on a date?"
    n "I know this one bakery that has {i}amazing{/i} cakes throughout all of December."
    s "You’re just...moving right on to the next topic?"
    n "Instead of what? Making you feel even more uncomfortable by tangentially detailing all of the reasons I still love you after all these years? Of course."
    n "We’ve reached the part of the conversation where I attempt to get closer to you through future plans instead of past occurrences. And Christmas is the most romantic day of the year."

    scene norikochinadress30
    with dissolve

    s "I’m pretty sure the class will wind up having another party."
    s "That’s what happened last year and I never really got a say in it."
    n "Are we getting each other presents?"
    s "They did a Secret Santa thing last time, so I imagine they’ll do that again as well."
    n "I’m not talking about that. I’m talking about you and me."

    scene norikochinadress31
    with dissolve

    n "I..."
    n "There’s something I want to give you."
    n "I’m not sure if you’ll {i}like{/i} it...but I found it when I was digging through some old stuff recently...and I think you should have it."
    n "And...you don’t {i}have{/i} to get me anything in return, but..."
    n "But it would make me really happy if you did..."
    s "…"
    n "Forget-"
    s "Sure."

    scene norikochinadress32
    with dissolve

    n "Ah-"
    s "I’m sure I can manage to remember that much."
    s "At least I know about this present beforehand, unlike last year."

    scene norikochinadress33
    with dissolve

    n "Mmn~"
    s "…"
    s "Is everything okay?"

    if bonus == True:
        n "I got weirdly turned on by the idea of you buying me a Christmas present and now I’m trying to stay cool."
        s "…"
        n "It's a shock thing. I don't know. I get horny when things surprise me sometimes."
        s "…"
        n "…"
        s "Do you..."
        s "Do you want me to go find you a desk or something?"

        scene norikochinadress34
        with dissolve

        n "You’re really going to make me regret telling you that desk thing, aren’t you?"
    else:
        n "Yeah. I'm just suddenly really tired."
        s "Is that so? Then I will leave this place and allow you to get some sleep, as I would not want to keep you up longer than you would like to remain awake for."
        n "I hope I have an extra pair of arms in my dream."
        s "What would you do with them?"
        n "Zzzzzzzzzzzzz..."

    scene black
    with dissolve2

    if bonus == True:
        "As Noriko would say, “the horny” fades away and I wind up leaving shortly after that."
        "And, I don’t know why...but I’m actually kind of thankful that nothing else wound up happening."
        "In fact, I might even feel a little...better?"
        "Not better in the fact that I feel {i}good{/i}...but better in the fact that some of the clouds inside of my head have begun to clear up."
        "I’m sure tomorrow will be overcast as well- it always is."
        "But it was nice being reminded of what it feels like to see a little clearer, even if it’s only for a short while..."
    else:
        "Noriko falls asleep and I never figure out what she would do with her extra arms."

    $ renpy.end_replay()
    $ noriko_love += 1
    $ norikodorm20 = True

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"

    stop music

    "The clouds come back on the way home."
    "They feel a little like hands."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label convenience25:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label norikodorm:
    if noriko_love >= 5 and kirindorm10 == True and convenience1 == True and norikodorm5 == False:
        jump norikodorm5
    if noriko_love >= 10 and convenience5 == True and kirindorm20 == True and norikodorm10 == False:
        jump norikodorm10
    if noriko_love >= 20 and norikospecial20 == True and norikodorm20 == False:
        jump norikodorm20
...
```