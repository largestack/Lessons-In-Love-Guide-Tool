# Locked In
Otoha event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohapark5&go=Go)



## Event preconditions
✅Otoha love greater than or equal to 0

✅Event "[Otoha: Japanese Summer](./otohapark1.md)" is completed (event=otohapark1)



## Next events
* [Otoha: Highly Pornographic](./otohadorm5.md)

## Event properties
* ID: otohapark5
* Group: Otoha
* Triggered by label: otohapark
* Triggered by branch label: saturdaymorning

## Event code
File: \game\OtohaEvents.rpy
Code:
```python
...
label otohapark5:
    scene otohacafetrip1
    with fade
    play music "brighterdays.mp3"

    "It doesn’t take long to find Otoha once I make my way over to the park again."
    "In fact, she winds up spotting me first and trots over without me even having to ask."
    "This is good. "
    "If she keeps growing at this rate, she might just wind up walking over to my house in the morning and, eventually, I won’t need to leave at all."

    s "I’ll leave a key for you under the doormat."
    o "Key? What?"
    o "What are you talking about?"
    s "Just the bright future the two of us have together..."
    o "Oh. Uhh, okay. Whatever floats your boat."
    s "No guitar today either?"

    scene otohacafetrip2
    with dissolve

    o "Not really any point until it gets a little warmer."
    o "The other day would have been fine, but it’s back to being chilly again and I don’t want to wind up botching any of my songs when I’m still not known around here."
    s "Just buy hand warmers or something. Problem solved."

    scene otohacafetrip3
    with dissolve

    o "Sure, that’ll solve my finger stiffness...but it’s not like everybody will come flocking to the park as soon as they hear that some random girl bought handwarmers."
    o "There’s more than just one problem, Sensei."
    s "Why not play indoors then?"
    o "What, you mean at that gazebo thing over there? That’s not really going to do much."
    s "I meant something more like an actual business. Like some local venue or a-"

    scene otohacafetrip4
    with dissolve

    sao "Cafe!"
    o "Holy shit! Yeah! That place where Rin works would be great to play at! "
    o "People actually go there in the morning and there’s like...tons of space!"
    s "Also, the manager there really has a thing for [teenage]girls. So you’re basically already locked in."

    scene otohacafetrip5
    with dissolve

    o "You know, maybe we should think of other places just in case. The cafe is cool and all, but-"
    s "Don’t worry. She’s still running a business, so it’s not like she’ll make a move on you mid-set or anything."

    scene otohacafetrip3
    with dissolve

    o "Is that supposed to make me more comfortable?..."
    s "Hey. As a female musician, and a rather attractive one, might I add-"
    o "You really didn’t have to add that."
    s "You should start getting used to being the center of attention. It’s only going to happen more once you start getting popular."
    s "How do you think Niki feels? She’s on actual billboards and she loves the attention."

    if bonus == True:
        o "Sure, yeah. But don’t you feel a little weird being her ex and knowing that there are a bunch of dudes out there who want to get it on with her?"
    else:
        o "Sure, yeah. But don’t you feel a little weird being her ex and knowing that there are a bunch of dudes out there who want to hug her?"

    s "Not really. Because I know I’m the only one who has."
    s "Probably."

    if bonus == True:
        o "If you’re worried about her hooking up with anybody else, I know for a fact that she hasn’t."
        o "She’s really only ever talked about one guy and...that guy somehow wound up being you."
        s "That’s cool. But I meant more that I haven’t exactly confirmed if {i}I{/i} have had sex with her yet."

    o "…"
    o "How...can you not know that?"

    scene otohacafetrip6
    with dissolve

    if bonus == True:
        o "Wait, she didn’t like...do stuff to you in your sleep or something...did she?"
        s "She very well may have done just that, Otoha..."
        o "Oh my God. That’s so messed up."
        o "She’s kind of controlling though, so I guess I could see that."

        "Sorry, Niki. I have tarnished your name once again."
        "Unless you actually {i}did{/i} assault me in my sleep."
        "If that’s the case-"
        "Nice."

        s "But anyway, you should probably get used to people wanting to “get it on” with you."
        o "That’s a little easier said than done, man..."
        s "Well, if you’d like...I could help loosen you up a-"
    else:
        s "I only recently started keeping a log of all my hugs. You're referencing a hug from a date range I didn't keep track of."

    scene otohacafetrip7
    with dissolve

    o "Oh, look. Is that a police officer behind you?"

    if bonus == True:
        s "I could help you learn to deal with any insecurities that may have led to your apparent disdain for unwarranted, romantically-focused attention from others."
    else:
        s "I hope so. I love law enforcement and would like to thank him or her for their service."

    if bonus == True:
        scene otohacafetrip8
        with dissolve

        o "Nah. I’m good."
        o "I’ll take my allowance now, though. I’m still waiting on that 1,000 yen."
        s "Who are you, my [niece]?"

        scene otohacafetrip9
        with dissolve

        o "Hmm...maybe more of a cool big sister."
        o "I guess little sister would also work given our current dynamic, though."
        o "But we should probably stop talking about this before Nodoka shows up out of nowhere and tries to write some doujin about us."

        scene otohacafetrip1
        with dissolve

        o "Since you won't be giving any generous contributions to my music fund, do you want to at least take a trip to the cafe with me?"
        o "It's not like I have anything else going for me this morning since I don't have lessons."
        o "Plus, it will probably be really funny to see Rin’s reaction to the two of us showing up together."
        s "I feel like she will either love it or absolutely hate it."
        o "I’m leaning toward the former. I think she’ll be stoked to know that two of her confirmed “favorite people” have started hanging out."
        s "Just wait until she learns we’re family now as well."

        scene otohacafetrip10
        with dissolve

        o "Come on, big bro! Let’s go torment our favorite barista!"

    scene black
    with dissolve2

    if bonus == True:
        "Otoha and I set off toward the cafe and I feel slightly bad for Molly in not giving her the title of my favorite barista."
        "But, to be fair, Molly is very bad at her job."
        "I can’t even remember if she’s ever actually sold me anything. "
        "At least Rin tries."
        "Tries a little too hard sometimes, sure. But she tries."
        "A short while later, Otoha and I wind up outside the cafe and exchange one final look of platonic sibling love before walking in and ruining (Or making) Rin’s day."
    else:
        "Otoha and I set off toward the cafe after that because our throats get all dry and scratchy and we need milk to make them feel all nice again."

    "………"
    "……"
    "…"

    if rinbetrayed == False:
        scene otohacafetrip11
        with dissolve

        o "Yo! Morning."
        s "One copyrighted frozen beverage please."
        r "…"
        r "Well I definitely don’t like this."
        o "It’s cool. We’re family now."
        r "…"
        r "Does Nodoka know?"
        s "I demand customer service."
        o "Not yet. We’re trying to keep it a secret from her."
        o "You want in as well?"

        scene otohacafetrip12
        with dissolve

        r "Yes. Immediately."
        r "Tell me what I must do."
        o "Nothing {i}that{/i} serious..."
        o "Just...you know. Maybe letting me play here sometime?"
        o "It’s a little too cold out to be playing in the park right now, and Sensei came up with the idea of maybe playing in the cafe."
        o "If that’s cool, I mean. I totally understand if it’s not."

    else:
        scene otohacafetrip13
        with dissolve

        o "Yo! Morning."
        s "One copyrighted frozen beverage please."
        r "…"
        r "Are you fucking kidding me?"
        r "Was the first time not enough? "
        r "You’re really going to do this again?"

        scene otohacafetrip14
        with dissolve

        o "Wait, what? What’s going on?"
        o "Is everything okay? We didn’t come here to mess with you or anything."
        r "Maybe {i}you{/i} didn’t."
        r "It wouldn’t be the first time Sensei decided to start getting close to someone I...am friends with, though."
        s "…"
        s "Yeah. This probably wasn’t a good idea after all."

        scene otohacafetrip15
        with dissolve

        o "Well...I’m really sorry if we upset you..."
        o "But we’re really just here to ask if it would be okay for me to...maybe play in the cafe sometime."
        o "It’s a little too cold out to be playing in the park right now, and Sensei came up with the idea of maybe playing here."
        o "If that’s cool, I mean. I totally understand if it’s not."

    scene otohacafetrip16
    with dissolve

    r "Oh my God, yeah! Totally!"
    r "I mean, it’s not really up to me. But my manager like, really has a thing for [teenage]girls. So you’re basically already locked in."

    scene otohacafetrip17
    with dissolve

    o "Hell yeah! Mission complete! "
    s "Wait, you know about that?"

    if bonus == True:
        r "Dude, why else would she hire exclusively cute girls? We work in a cafe, not a topless bar."
        s "I’m pretty sure Haruka thinks she’s managed to hide it from you."
        r "Then she should probably stop “accidentally” sending pictures of her in her underwear to our group chat and saying they were meant for someone else."
    else:
        r "Dude, why else would she hire exclusively cute girls? We work at a cafe, not Hooters."

    scene otohacafetrip18
    with dissolve

    o "You know, maybe we should think of other places just in case. The cafe is cool and all, but-"
    s "Don’t you dare chicken out after coming this far. "
    s "Think of what Niki would do."
    o "Is like...{i}everyone{/i} on this side of town weird, or?..."
    s "If you think this is bad, you should take a visit to the old district."

    scene otohacafetrip19
    with dissolve

    o "Uhh...I’m good. That place kinda creeps me out."
    r "I’ll try talking to Haruka about it. I’m sure she’ll say it’s fine, but...Hey, you never really know."
    r "Do you guys need anything? I’m in charge today, so I can give you extra shots for free or something."
    s "Two “Rin Specials” please."

    scene otohacafetrip20
    with dissolve

    r "You got it, Sensei."
    r "Go sit down. I’ll bring over something crazy in just a minute."
    o "What did you just order me? "
    s "Don’t worry about it."
    o "But...I’m lactose intolerant. "

    scene black
    with dissolve

    "Otoha and I make our way to a table only slightly touched by the sun and take our respective places at opposite ends."
    "Rin shows up a few moments later with two different drinks and sets one in front of each of us before rushing back to the counter to help another customer..."

    scene otohacafetrip21
    with dissolve

    o "So, I might as well get it out of the way now and say thanks for coming up with this idea."
    s "Don’t thank me until it’s at least been approved."
    o "But you guys said it yourself, I’m basically locked in."
    s "Sure. But what if Haruka thinks you’re so attractive that she won’t be able to contain herself around you?"
    s "That could affect business."
    o "…"
    s "Well?"
    o "Let’s talk about something else."
    s "Sure. Let’s talk about Rin instead."

    scene otohacafetrip22
    with dissolve

    o "Welp, guess the chance for a normal conversation topic is off the table."
    s "How are things going for the two of you now that you don’t live far enough apart to come up with excuses for not hanging out with her?"

    scene otohacafetrip23
    with dissolve

    o "Wait, what? What are you talking about?"
    s "Weren’t the two of you supposed to go on a trip to some arcade in your neck of the woods a while back?"
    s "I wound up going in your place."
    o "Yeah, but that was because my parents wouldn’t let me go. It had nothing to do with me trying to get out of it."
    o "I thought it sounded really fun and we’ve already made new plans to go there together."
    s "Oh, really? I didn’t hear about that."
    o "Yeah. I was never trying to avoid her or anything if that’s what you were thinking."
    s "Well, that’s good. "
    s "She didn’t really let it show, but she was pretty upset that day."

    scene otohacafetrip24
    with dissolve

    o "Oh come on...I like, {i}just{/i} stopped feeling bad about that..."

    if rinbetrayed == False:
        scene otohacafetrip25
        with dissolve

        o "Besides...didn’t getting to go in my place kind of like...work out for you or whatever?"
        s "What do you mean?"
        o "I mean that like...you guys kissed or something, right?"
        s "…"

        "Rin told her that?"
        "Why?"
        "I figured she’d be worried about that ruining her chances with Otoha."
        "Maybe she just...doesn’t want to hide anything from her?..."
        "I don’t know."

        s "Yeah. We did."
        o "Yeah. So like...sorry if it seems like I’m trying to take your place or something. Even if that was only a one time thing."
        s "I don’t think you’re trying to take my place. "
        s "Hell, I don’t even fully understand what my “place” with Rin is."
        s "I just wasn’t sure what to think about how you two were doing specifically now that you’re seeing each other a lot more."

        scene otohacafetrip26
        with dissolve

        o "More or less the same as we were before. "
        o "Just now I don’t have to worry about the pressure of being her first kiss if we {i}do{/i} wind up becoming anything more than what we are now."
        s "Wait, so you’re okay with what happened between us? There’s no lingering resentment or anything?"

        scene otohacafetrip27
        with dissolve

        o "Why would I resent anything about two people who like each other kissing for a few minutes?"
        o "Things like that happen."
        o "It’s not like me and her are dating."

        if bonus == True:
            o "Like, if I made out with Nodoka, I’m sure Rin wouldn’t be upset at all."
            s "I don't think that’s true. She likes you a lot."

        o "She likes {i}you{/i} a lot, too."
        o "It’s like she’s going through some...intense war inside of her head where you and me are duking it out for the upper hand."
        o "Just neither one of us is actually {i}fighting{/i} and it’s all on her."
        o "Pretty good material for a song, now that I think about it."
        s "Stop being so mature and cool or I’m going to start liking you too."

        if bonus == True:
            o "But you’re my brother. What would our parents think?"
            s "Haven’t I been telling you this whole time that they don’t matter anymore?"
            s "All that matters is {i}us{/i}, my dearest Otoha."
            o "…"
            s "…"

            scene otohacafetrip28
            with dissolve

            o "Okay. I’m uncomfortable now. "
            o "Let’s just talk about music or something instead..."

    else:
        s "There’s no need to feel bad. She still really likes you."
        s "The second you texted her that night, she completely stopped paying attention to me."
        s "And I don’t blame her after how I’ve treated her feelings in the past."

        scene otohacafetrip29
        with dissolve

        o "If you’ve messed with her feelings in the past, why do you seem so worried about them now?"
        s "Because I’m naturally a horrible person and you’re not."
        s "Rin still has faith in you. So if {i}you{/i} wind up screwing her over as well, she’s probably just doomed to romantic misfortune for the rest of eternity."

        scene otohacafetrip30
        with dissolve

        o "That’s putting way too much pressure on me, Sensei. That’s not fair."
        o "Rin’s happiness shouldn’t be entirely dependent on either one of us reciprocating her feelings. "
        o "I don’t think you’re a bad guy. I just think you might do bad things every once in a while."
        o "I’m no different."
        o "If someone’s feelings get hurt as the result of my actions, like they did with Rin and the arcade trip, I’m obviously going to be upset."
        o "But I’m not going to give up on everything I want just to make sure they don’t get upset anymore."
        o "I have no idea how I feel about Rin right now. And there’s a good chance I won’t for a while. I just..."
        o "I have no idea."
        o "Everything is all so new to me all of a sudden."
        o "So just let me kinda...take it all in for a little while, okay?"
        s "…"
        o "…"
        s "Yeah. Sure. The way I worded that was pretty bad anyway."
        s "I just meant there’s no need to get down about upsetting her since she still thinks you’re the coolest girl she’s ever met."

        scene otohacafetrip31
        with dissolve

        o "That really seems to be a recurring theme these days, huh?"
        o "Why does everyone think I’m so cool? Does playing guitar and singing really help that much?"
        s "I don’t know. I still think it’s the rings."
        o "Bring up the rings one more time and I’m cutting my fingers off."

    scene black
    with dissolve2

    "Otoha and I wind up talking until an orange glow consumes Kumon-mi and daytime begins to exit stage left. "
    "The cafe stays busy throughout the morning, so Rin never gets a chance to spend any time with us. "
    "I’m a little surprised that she was able to prioritize work over hanging out, though."
    "But I guess she might be trying to prove herself or something since Haruka was confident enough to leave the cafe in her hands for the day."
    "Either that or she’s just starting to realize that Otoha needs her space to thrive."
    "I don’t know if I’d go as far as saying she’s truly “out of the cage” yet-"
    "But Otoha's cage is extremely large. "
    "So I’m sure she still has plenty of room to fly and just...hasn’t found the door yet."

    $ renpy.end_replay()
    $ otoha_love += 1
    $ otohapark5 = True
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label otohapark10:
...
```

## Code that triggers this event
File: \game\OtohaEvents.rpy
Code:
```python
...
label otohapark:
    if otoha_love >= 0 and otohadorm1 == True and saradate10 == True and otohapark1 == False:
        jump otohapark1
    if otoha_love >= 0 and otohapark1 == True and otohapark5 == False:
        jump otohapark5
...
```