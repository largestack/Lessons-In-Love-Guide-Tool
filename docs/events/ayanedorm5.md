# Home Sweet Home
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanedorm5&go=Go)



## Event preconditions
✅Ayane love greater than or equal to 5



## Next events
* [Ayane: Imprinting](./ayanenew1.md)

## Event properties
* ID: ayanedorm5
* Group: Ayane
* Triggered by label: ayanedorm
* Triggered by branch label: ayanedorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label ayanedorm5:
    play sound "knock.mp3"

    "…"

    ay "Just a second!"

    "A series of strange, loud noises leak through the bottom of the door and find their way into the hall."
    "I can not, for the life of me, tell what’s going on in there, but seeing as this is Ayane we’re talking about, I guess anything is possible."

    s "Do you...need help or something in there?"
    ay "S-Sensei?! Knocking on my door? Is this a dream?"
    s "Nope. What’s up, Ayane?"
    ay "This better not be a prank! If I open that door and it's just Ami with a tape recorder, I'm going to be really mad!"
    s "This isn't a recording, Ayane. I'm really here."
    ay "That's exactly what Ami would have had recorded since she knows I'd see through this ploy! I'm not falling for it."
    s "..."

    play sound "knock.mp3"

    s "Ayane, let me in."
    ay "If you're Sensei...say something only Sensei would know about me!"

    "Oh, good. That's a thing I don't have any trouble with at all."

    s "You know what? Maybe I'll just leave."

    play sound "knock.mp3"

    ay "You can't leave! If...that's really you I mean!"
    s "Why are you the one that's knocking on the door now?"
    ay "I don't know! I wasn't prepared for this! I still have to hide the bodies!"
    s "Is that what all that noise was in-"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    ay "Oh my God! It really {i}is{/i} you! Why are you still in the hall?"
    s "That's what I'd like to know..."
    ay "I'll make it up to you! Here, come inside!"

    "Ayane grabs my wrist and begins pulling me into her room, but something about how erratic she's being right now makes me a little hesitant to do what I came here for in the first place."
    "That or I subconsciously believe she actually {i}is{/i} hiding bodies in here and I just don't want to be an accomplice to whatever crimes she commits outside of school hours."
    "........."
    "......"
    "..."

    show ayaneroomredux1
    with dissolve

    ay "Ahh!!!!"
    s "You doing okay over there?"
    ay "You came to see {i}me!{/i} In my room! Alone! Without Ami or Maya or anybody! It finally happened!"
    s "You, uhh...really like me, huh?"

    scene ayaneroomredux2
    with dissolve

    ay "{i}Ahem.{/i}"
    ay "Yeah, I guess you could say that."

    "You know, if there's one thing I {i}really{/i} understand about this world so far, it's that Ayane has been interested in {i}me{/i} for pretty much as long as she's known me."
    "I wasn't aware it was...this bad, though."
    "She's acting like she's got front seats to some sort of boy-band concert and I'm a little worried that the next phase will involve her taking out a large foam finger and cheering me on as I rifle through her things."
    "It's a strange assumption to make, I'm sure. But things are already a lot weirder than I expected when coming here, so I might as well try to go a little bigger with my expectations."
    "Anyway, Ayane’s half of the dorm is as extravagant as I expected it to be all the way down to the very last thread of...her exceedingly large bed."
    "In fact, how did she even manage to get that thing in here? It's taking up half of the room."

    scene ayaneroom1
    with dissolve

    "I take a few steps forward and place the palm of my hand on her mattress, pressing down to see what sorts of things people with her amount of money get to fall asleep on at night."
    "It feels like a weird halfway point between a sponge and a marshmallow and I'm not exactly sure if I like it, but I'm open to spending a night or seven inside of it to confirm."

    ay "Super comfy, right? The mattress was made in France and imported here right before the barrier was put up."
    ay "Fun fact: This is actually my bed from home. I had the movers bring it here at the beginning of the year when I moved in."
    s "How did they get it to fit?"
    ay "That's what she said."
    s "Okay, but really."
    ay "They tore down the wall and rebuilt it, of course."
    ay "It made the halls a total mess for a whole day, but I think we can all agree it was worth it in the end."
    s "Yes, I'm sure everyone else is very thankful that you get to sleep on a bed the size of their homes."
    ay "So...is there anything {i}else{/i} you see that you maybe want to comment on, Sensei?"

    scene ayaneroom2
    with fade

    s "Yes, actually. Thank you for reminding me."
    s "What the fuck is this?"
    ay "My Sensei wall!"
    s "I'm going to need a better explanation than that."
    ay "Sure! When we moved in, they told us we could decorate our rooms with whatever we liked. So {i}obviously{/i} I was going to put up some of my favorite photos of you!"
    s "Am I...asleep in that one?"
    ay "Yup! Ami has a copy of that one as well. It's one of our favorites."
    ay "We have an entire album of candid photos we've taken of you. These four are just scratching the surface."

    "Okay, this may be a bit of a problem."

    ay "You know, I'd be totally open to taking better pictures of you, but you're always so against being on camera and stuff."
    s "This seems like a major invasion of privacy."
    ay "If you want to talk about invasions of privacy, you should see some of the stuff Ami has in her personal collection."
    ay "Don't get me wrong, I love it. But it's actually a little creepy that she's so adamant about keeping those ones to herself when you guys are related."
    ay "That's fine, though. I'll get back at her with my own secret stash soon enough now that you're willing to come to my room!"

    scene ayaneroom3
    with fade

    ay "You love it, right?! Doesn't it warm your heart knowing that your niece's best friend goes to sleep every night with a photo collage of candid pictures of your sometimes-sleeping body?"
    s "That seemed like a mouthful."
    ay "I will assure you my mouth can fit much more!"
    s "I will...definitely remember that."
    ay "So, what do you think I should do? Add more to it? Leave it the way it is? I want your input since you {i}are{/i} the inspiration behind it and everything."
    menu:
        "...":
            s "..."
            ay "..."
            s "It's..."
            s "It's certainly very...{i}you.{/i}"

            scene ayaneroom4
            with dissolve

            ay "I know!"
            ay "Moving into dorms for the first time was definitely a little scary...but as long as I have you next to me, I feel ten times safer!"
            s "..."

            "How exactly did she manage to say something to make me {i}kind of{/i} okay with this?"
            "Yes, it is obviously still very creepy...but now it's cute as well and I wasn't expecting to come around to this so soon."
        "This is terrifying":
            s "Ayane, this is absolutely terrifying."

            scene ayaneroom5
            with dissolve

            ay "What? Why?"
            s "Well...how would you feel if you walked into someone's room and there were pictures of you all over the wall?"

            scene ayaneroom5r
            with dissolve

            ay "Loved."
            s "Really? That's it?"
            ay "Yes. And I'd even be happy to print some out for you if you have some extra wall space and want to fall asleep next to me without Ami killing us."
            s "Something tells me she wouldn't be very happy about pictures, either."
            ay "Does this really scare you, Sensei?"
            s "Well...it's less {i}scary{/i} and more...I don't know- creepy?"

            scene ayaneroom5r2
            with dissolve

            ay "I..."
            ay "I'll take them down if you want."
            ay "I just liked how they made me feel and..."
            ay "I miss you when you're not around sometimes..."
            s "..."
            ay "..."
            s "Ugh. Fine."
            s "You can keep them up. Just stop taking pictures of me while I'm asleep. That is where I draw the line."

            scene ayaneroom5r3
            with dissolve

            ay "That is a line I'd be happy to deal with!"

    scene ayaneroom3
    with dissolve

    ay "So, now that we’re alone, what did you want to do?"
    ay "My bed is practically {i}made{/i} for cuddling, you know. And it's big enough that we could hide under the blanket and it would take Sana roughly five years to find us."
    s "As fair warning, I'd very likely wind up shooting for a little more than just {i}cuddling{/i} if we got into that bed together, Ayane."

    scene ayaneroom6
    with dissolve

    ay "Oh! You..."
    ay "I mean..."
    ay "I'm obviously not {i}opposed...{/i}"
    ay "Like...if the bed is made for cuddling, it's...obviously pretty suited for stuff like that too..."
    ay "And if it's with you..."
    s "You're nervous, aren't you?"

    scene ayaneroom7
    with dissolve

    ay "Uhhhhh..."
    ay "I don't know if nervous is the right word because I am...{i}definitely{/i} feeling something else just thinking about that..."
    ay "But I also...kind of have a weird request that I'd like to run by you if that...doesn't take away from the mood too much..."
    s "It must be one hell of a fetish if you have to warn me beforehand."

    scene ayaneroom7r
    with dissolve

    ay "It's not a fetish! It's just..."
    ay "If we're...uhh...okay with...taking things in that direction..."
    ay "I..."

    scene ayaneroom7r2
    with dissolve

    ay "I kinda...want to skip all the other stuff first..."
    s "..."
    ay "..."
    s "As in-"

    scene ayaneroom7r3
    with dissolve

    ay "As in I...kind of...maybe...want to have sex with you?..."
    ay "If that's okay to say...which it might not be since you have basically raised me the last few years and it would be all sorts of wrong from like a million different angles-"
    ay "But...I kind of also {i}really{/i} want to?..."
    s "Like...like now?"

    scene ayaneroom7r4
    with dissolve

    ay "No no no no no, definitely not now. I don't even have any idea when Sana is going to be home."
    ay "I just...want my first experience to be a really special one that we can kind of, like...prepare for or something."
    s "..."
    ay "..."

    scene ayaneroom7r5
    with dissolve

    ay "But after that, I'll basically let you do anything you want to me wherever you want to do it."
    s "You know, it was really cute seeing you embarrassed for the fifteen seconds you were able to hold it."
    ay "Oh, I'm still very embarrassed. But I also trust you with all of me, Sensei. Whether it be my heart or my body..."
    ay "When we connect, I want it to be real."

    scene ayaneroom7r6
    with dissolve

    ay "So, uhh...despite how badly I'm sure both of us want to {i}cuddle{/i} right now...we should probably hold off or we'll wind up jumping the gun and-"
    s "Hold on a second, I never agreed to this proposal."

    scene ayaneroom7r7
    with dissolve

    ay "Huh?"
    s "You said you wanted to ask me something and then just went off about your big plans without giving me the chance to respond to them."
    ay "So...you're not okay with...skipping straight to the end of the race?..."
    s "..."
    ay "..."
    s "Oh, I'm totally okay with it. I just wanted to be involved in the decision making process."

    scene ayaneroom7r8
    with dissolve

    ay "Sensei, what the heck?! That had me really worried for a second!"
    s "Did you honestly think I'd turn that down?"
    ay "I had no idea what to think! It's the first time I've ever made plans to lose my virginity!"
    s "Well, I can't guarantee I'll be able to make it special. But if you want to {i}skip straight to the end of the race,{/i} we can do that."

    scene ayaneroom8
    with dissolve

    ay "Just agreeing to be with me makes it more special than I could have ever wished for, Sensei."
    ay "I'm sorry if I'm moving too fast, I just..."
    ay "I know what I want. And I know {i}who{/i} I want."
    ay "You just happen to be both of those things."

    scene black
    with dissolve2

    "So...already, huh?"
    "I didn't even have to work for it."
    "I simply put on someone else's nametag, took a few steps forward, and was wrongly gifted a bouquet of the world's most delicate flowers without so much as a background check."
    "Desperation and loneliness make a vicious cocktail, don't they?"
    "Ayane must be so blindsided by the object of her perpetual affection leaning into her that she's abandoned all rationality in blind hope that true love is real."
    "I lift the bouquet to my nose and breathe in the scent of someone else's job well done."
    "I will remember it again when the time comes to change a girl's life."
    "I shouldn't be doing this."
    "I shouldn't."
    "But I will."
    "Because it matters not what we should or shouldn't do when what we want is ten times louder."
    "The weakest link is the first to break."
    "Everything else follows."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayanedorm5 = True

    "{i}Ayane’s affection has increased to [ayane_love]! You can now spend time with her in her room!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label ayanedorm10:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
Code:
```python
...
label ayanedorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ayane_love >= 5 and ayanedorm5 == False:
                jump ayanedorm5
...
```