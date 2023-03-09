# Yumi Revitalization Project
Yumi event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumidorm10&go=Go)



## Event preconditions
✅Yumi love greater than or equal to 10

✅Event "[Yumi: Fuck The Police](./yumidorm5.md)" is completed (event=yumidorm5)



## Next events
* [Maya: Close Your Eyes](./mayadorm20.md)
* [Yumi: Worse Comes to Worst](./yumidorm15.md)

## Event properties
* ID: yumidorm10
* Group: Yumi
* Triggered by label: yumidorm
* Triggered by branch label: yumidorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label yumidorm10:
    play sound "knock.mp3"

    "Once again, I find myself knocking on the door of a girl who wants nothing to do with me."
    "But, for reasons beyond my comprehension, I’m drawn to her. Like she’s a flickering light and I’m a...moth or some other fitting metaphor."
    "..."
    "Why do I feel the need to get poetic all of a sudden? This is Yumi we're talking about."

    play sound "knock.mp3"

    s "Yumi, let me in. I’m having a potentially uncharacteristic inner-monologue."
    y "Huh? The fuck are you talkin’ about? Get the hell out of here."
    s "You know I’m not going to do that. Just open the door."
    y "No! Fuck off!"

    "I hear something whack against the door and fall to the ground. She must have
    thrown her pillow at it."
    "Or maybe a cushion. Who knows? Does it even matter?"

    play sound "knock.mp3"

    s "Delivery for Yumi Yamaguchi."
    y "Oh my fucking God."
    s "I have the pizza you ordered."
    y "…"
    s "…"

    play sound "knock.mp3"
    "…"
    y "JESUS, OKAY! HOLD ON A FUCKING SECOND, WOULD YOU?"

    "I can hear the springs in her mattress squeak as she gets off the bed. I doubt
    she was going to sleep this early, so maybe she was just lounging around or something?"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "After a moment, the door opens and Yumi begrudgingly lets me in."
    "………"
    "……"
    "…"

    scene yumifirstdorm1
    with dissolve2

    y "What?..."
    s "…"
    y "…"
    s "You look really cute."

    scene yumifirstdorm2
    with dissolve

    if bonus == True:
        y "Bullshit! I do not! It’s just a track jacket and pants. Do you have some...weird fetish for overly-clothed girls or something?!"
        s "You shouldn't belittle people for their fetishes, Yumi. It's unbecoming."
        y "I'll do whatever the fuck I want, thank you very much. Now why are you here?"
        y "Are you going to try to get me to talk to you again? Cause I’m not really in a talkin’ mood right now."
    else:
        y "I hate you! When you get older, I'm going to punch you too!"

    s "Did something happen?"

    scene yumifirstdorm3
    with dissolve

    y "Yeah. This weird guy keeps followin’ me around and I’m pretty sure he’s going to [rape] me."
    s "That sounds horrible. Where did he go? I’ll take him down."
    y "…"

    "Of course I know she’s talking about me. But if she was actually concerned about me doing something horrible to her, why would she have opened the door in the first place?"

    s "Relax. You're safe here."
    y "I'd sure fucking hope so. It's {i}my{/i} room."
    y "Though, I guess you've proven you really don't give a shit about that so far."

    scene yumifirstdorm2
    with dissolve

    s "So, what's the plan? Are we going to sit here in silence for the rest of the night and stare at each other?"
    y "You know, if you're bored, you can leave whenever the fuck you want. It’s not like I actually want you here or anything."
    s "Woah, calm down there, tsundere. You’re about to confine yourself to a particular archetype."

    scene yumifirstdorm4
    with dissolve

    y "I’m not a fucking tsundere! I genuinely {i}do not{/i} want you here! I was about to go to sleep!"
    s "Sleep? But it’s only 8PM. Chika’s not even home yet."
    y "Well, what else was I gonna do?! I don’t have a laptop to fuck around with and I can’t figure out the password to Chika’s!"
    y "I thought about goin’ for a walk or whatever but then I figured that’s what {i}you{/i} would be doin’ since you’re apparently obsessed with stalking me now."
    y "But now you’re here anyway so I obviously made the wrong decision!"
    s "We can go for a walk if you want. Is there anywhere you want to go?"

    scene yumifirstdorm1
    with dissolve

    y "No...ugh. We can just...fucking stay here..."
    y "I’m already in my pajamas. I don’t want to get dressed again."
    y "I might get attacked."

    if bonus == True:
        "To be frank, I'm already having a hard time not {i}attacking{/i} her."
        "But this is also my first time seeing Yumi in her pajamas, so I think I should be forgiven for any impure thoughts I may or may not be having."
        "Sure, the words “Fuck You” are still looming in the background on her dry-erase board, but I feel like Yumi’s actually a little calmer today than usual."

    s "I guess we’ll stay here then. Do you want to, like...watch a movie or something?"
    y "How? I just fuckin’ told you I don’t have the password to Chika’s laptop."

    scene yumifirstdorm4
    with dissolve

    y "Also, stop pretending we’re friends just because I let you inside my room!"

    scene yumifirstdorm5
    with dissolve

    "I direct my attention to a bunch of old-looking TVs on a warehouse-style shelf near the door."
    "I’m not sure why either of these things are here, but I’m assuming at least one of the TVs needs to work, right?..."

    s "Why do you have all of these?"
    y "What’s it matter to you?"
    s "Just...seems like a strange thing to collect."

    scene yumifirstdorm6
    with dissolve

    y "I’m not fuckin’ collecting ‘em! I sell these!"
    s "Who in their right mind is buying old TVs from you?"
    y "I don’t know! Pawn shops...old people like you tryin’ to remember their childhood. Whoever!"
    s "Aren’t there easier ways to earn money, though?"

    scene yumifirstdorm7
    with dissolve

    y "What, like getting an actual job? Isn’t that off limits for students?"
    s "Yeah, but that hasn’t really stopped anybody else."
    y "Okay, but who the fuck is gonna hire somebody like me? You know the way I talk."
    y "I’m not workin’ material. I {i}have{/i} to do shit like this or I can’t afford to eat."
    s "Your parents don’t give you money for food?"
    y "I..."
    y "I don’t really talk to my parents. Fuck them."

    scene yumifirstdorm6
    with dissolve

    y "They’re assholes anyway! Maybe even worse than you! Who needs ‘em?"
    y "Besides, it’s not like I’m fuckin' starving or whatever. I still eat pretty much every day."
    s "Pretty much?"

    scene yumifirstdorm8
    with dissolve

    y "Well, yeah. You don’t need to eat {i}every{/i} day. All you really {i}need{/i} is water."
    s "Is that why you have so many water bottles on your side of the room?"

    scene yumifirstdorm6
    with dissolve

    y "Sh-shut up! They’re all empty! I just didn’t feel like cleanin’ em up!"
    y "I walked all over town today and my legs are fuckin’ dead, so forgive me for not gettin' rid of some stupid bottles."
    s "I didn't mention that it was a mess...I just noticed there was a lot of water, that’s all."

    scene yumifirstdorm7
    with dissolve

    y "Well...whatever. You said you wanted to know shit about me and now you know one thing. Is that enough for you to fuck off?"
    s "No, actually. In fact, I’m probably even more worried about you now."

    scene yumifirstdorm9
    with dissolve

    y "The fuck is there to worry about?! I’m fine!"
    s "You’re most definitely not fine. You’re malnourished and I’m pretty sure it’s causing your attitude to deteriorate."

    scene yumifirstdorm7
    with dissolve

    y "That’s just my fuckin' attitude...What I eat has nothin’ to do with it."
    y "If you really wanna help, just buy a fuckin’ TV."
    s "Where do you even get the TVs?"

    scene yumifirstdorm9
    with dissolve

    y "My God! The questions never end with you! Does it matter?!"
    y "Maybe I find ‘em on the side of the road! Maybe I steal ‘em! As long as it’s puttin’ food on the table, it shouldn’t fuckin' matter where they come from."
    s "I think you and I might need to do some job-hunting soon, Yumi."

    scene yumifirstdorm10
    with dissolve

    y "Yeah, well I think you should eat a fucking dick."
    s "Harsh."
    s "For real, though. Let’s try and figure out a way for you to be able to make ends meet without stealing or scavenging outdated television sets and-"
    s "What’s all that other stuff on the desk? Candy?"

    scene yumifirstdorm7
    with dissolve

    y "Yeah...Easier to sell, but doesn’t bring in as much cash."
    y "Not like I can survive off just eatin’ candy either, so none of that's for me."
    s "Okay well, either way, I’ll try and help you find some work. "

    if bonus == True:
        y "...If you think I’m gonna suck your dick in exchange for helping me out or whatever, you’re fucking delusional. It’s not gonna happen."
    else:
        y "...If you think I’m gonna hug you in exchange for helping me out or whatever, you’re fucking delusional. It’s not gonna happen."

    s "I didn’t even almost insinuate that."

    scene yumifirstdorm6
    with dissolve

    y "You don’t need to. You’ve made your motives pretty clear already, asshole."
    s "I just want you to be able to eat every day instead of “pretty much” every day."
    s "Sure, you might hate my guts, but you’re still my student."
    s "I might not be the best teacher out there-"
    y "{i}Might{/i} not be?"
    s "Okay. I'm {i}definitely not{/i} the best teacher out there, but I do know that I’m not supposed to let my students die of starvation."

    scene yumifirstdorm7
    with dissolve

    y "You really did get this job just to hang around [young_girls], didn’t you?"
    s "The answer to that question is very complicated, so I am going to disregard it. The point is, we’re going to start the Yumi Revitalization Project."

    scene yumifirstdorm11
    with dissolve

    y "Heh?"
    y "The Yumi-what now?"
    s "The Yumi Revitalization Project. Coming soon to a Yumi near you."
    y "…"
    s "…"
    y "Are you high?"
    s "High on passion."
    y "You’re a fucking lunatic."
    y "I never agreed to this."
    s "You don’t need to agree to it. I’ve decided this is best for you as your teacher."
    s "And if you disagree, I’ll report all of your absences to the principal."

    scene yumifirstdorm12
    with dissolve

    y "Wait...You mean...you haven’t already been doing that?"
    s "Of course not. I don’t want you to fail."

    "There’s also the issue of me being held responsible if I report that she’s skipping literally every day, so..."

    y "…"
    s "…"

    scene yumifirstdorm8
    with dissolve

    y "Uhh...I don’t really know what I’m supposed to say to that."
    y "Thanks...I guess?"
    y "That’s...actually really cool of you."
    s "No need to thank me - just looking out for you. What
    you {i}can{/i} do, though, is sign this contract here..."

    "I remove a sheet of receipt paper and a pen from my pocket and
    quickly scribble the words “Yumi Revitalization Project” on it."
    "I add an extra blank line underneath the subtotal for a purchase at the cafe
    and hand the sheet over to Yumi."

    scene yumifirstdorm11
    with dissolve

    y "The fuck, dude? This is a receipt for coffee."
    y "I’m supposed to sign away my freedom on {i}this{/i}?"
    s "You’re not signing away your freedom. You’re just agreeing to go job hunting with me."

    scene yumifirstdorm10
    with dissolve

    y "But...what if they don’t like me? I don’t really have the best reputation around here..."
    s "Then we’ll just find somewhere else."
    s "I’ll even buy you lunch or something whenever we go out. Free food doesn’t sound bad, right?"
    y "Doesn’t sound that good either if it’s coming from you...Who knows what you’ll ask me to
    do to ‘repay my debt’ or whatever the fuck you’re eventually gonna call it."
    s "Your happiness is more than enough payment for me, Yumi."

    scene yumifirstdorm11
    with dissolve

    y "Gross..."
    s "Yeah. That was hard to say."
    y "Ugh...whatever. Fine."

    scene yumifirstdorm10
    with dissolve

    y "Free lunch doesn’t sound that bad anyway. And if I have a chance at gettin’ more money out of it, then..."
    y "I guess I can stomach bein' near you a little more..."

    scene black
    with dissolve2

    "Yumi scribbles her name on the sheet of receipt paper and hands it back to me."
    "I try and stay for a while longer to chat with her about other things, but she manages to push me out of the room."
    "Eventually, I find myself walking back home. But not without a newly-formed contract between myself and the[school]-delinquent."
    "Here’s to hoping we can get her onto the right track soon enough."
    "Kudos to me for actually being a teacher for once."

    $ renpy.end_replay()
    $ yumidorm10 = True
    $ yumi_love += 1
    stop music fadeout 5.0

    "{i}Yumi’s affection has {s}somehow{/s} increased to [yumi_love]!{/i}"
    "{i}You can now spend time with her in her room!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yumidorm15:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label yumidorm:
    if yumi_love >= 5 and streets10 == True and yumidorm5 == False:
        jump yumidorm5
    if yumi_love >= 10 and yumidorm5 == True and yumidorm10 == False:
        jump yumidorm10
...
```