# Nothing is Real
Maya event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=shrine20&go=Go)



## Event preconditions
✅Maya love greater than or equal to 20

✅Event "[Main: See You in the Morning](./beachvacation16.md)" is completed (event=beachvacation16)

✅Event "[Maya: Takoyaki](./mayadorm15.md)" is completed (event=mayadorm15)



## Next events
* [Maya: Close Your Eyes](./mayadorm20.md)

## Event properties
* ID: shrine20
* Group: Maya
* Triggered by label: shrine
* Triggered by branch label: shrine

## Event code
File: \game\MayaEvents.rpy
Code:
```python
...
label shrine20:
    scene shrinetwenty1
    with fade
    play music "shrinesong.mp3"

    "I arrive at the shrine to find Maya taking a break from whatever it is shrine maidens do every day, calmly sitting on a rock and not paying much attention to anything."
    "She stares up at the sun as its rays leak through the trees and find their way onto her dress, illuminating her body and turning her almost angelic in nature."
    "Though, I highly doubt angels are as confrontational as her."

    if bonus == True:
        "Ideally, an angel wouldn’t accuse you of sleeping around with [teenage]girls on a daily basis."
    else:
        "Ideally, an angel wouldn’t accuse you of hugging everyone she knows on a daily basis, even if it's mostly true with a few notable exceptions."

    "Or call you a disgusting waste of life in the middle of every conversation."
    "But I guess beggars can’t be choosers, and I am very much a beggar."

    scene shrinetwenty2
    with dissolve

    m "Oh, look. A pervert."
    m "Please leave me alone or I'll be forced to call security."
    s "Hey, Maya."
    m "Hello."
    m "Goodbye, now."
    s "Not goodbye. I’m here to talk to you."

    scene shrinetwenty3
    with dissolve

    m "About what, exactly?"
    s "I don’t know. Probably something that I don’t possess enough intellect to comprehend or follow along with."
    m "So a normal conversation for you."
    s "Yeah, exactly."
    m "I see."
    m "Well, I’m not exactly in a talking mood. So maybe we should just save this for another day?"
    s "You’re never in a talking mood."
    m "That’s not true."
    m "We had a lengthy discussion about stars on the beach just recently."
    m "Or perhaps you’ve already forgotten that?"

    "My mind races back to when I found Maya alone on the shore just an hour or two before Rin’s heart was snapped in half."
    "A lot happened that day, so the conversation is a little foggy, but what I do remember is that it..."
    "Well, it was just another conversation with Maya."

    s "Not entirely. I remember that you like stars."
    m "Yes. An important character trait."
    m "Take note of that in your journal."
    s "Sure. I’ll put it right next to “Hates my guts” and “Likes watermelons.”"

    scene shrinetwenty4
    with dissolve

    m "I don’t think “Hate” even begins to describe my feelings toward you."
    s "It’s fine. I’ll just scratch that part out and fill it with a bunch of question marks, then."
    m "Thank you. I’d also edit your entry in my journal, but I was afraid it would begin to bleed into the other pages, so I already tore it out and set it on fire."
    s "That’s rude."
    m "It burned up very quickly."
    s "Thanks. That’s a thing I wanted to know."

    scene shrinetwenty3
    with dissolve

    m "That aside, has anything else changed since you’ve come back from vacation?"
    m "The ending must have been rather eventful for you."
    s "How do you know about the ending?"
    m "It’s hard to not overhear things when everyone is so close together."
    m "Perhaps I stumbled upon a stray conversation or two while I was out watching the stars?"
    m "Such a thing could happen, could it not?"
    s "It could. But I feel like things aren’t usually as they seem with you."

    scene shrinetwenty5
    with dissolve

    m "Oh?"
    m "I’m not sure what you mean. I’m just a normal [teenage]girl."
    m "Everything I say is exactly as it is. I have nothing to hide, especially from someone like you."
    s "If you have nothing to hide, then how about we talk about your past for a little while? Or your interests. "
    s "Anything to make me feel like we’re getting somewhere."

    scene shrinetwenty6
    with dissolve

    if bonus == True:
        m "Maya Makinami. Age, [[redacted]. My hobbies include watermelons and the violin. My past is of none of your concern."
    else:
        m "Maya Makinami. Height, short. My hobbies include watermelons and the violin. My past is of none of your concern."

    s "Watermelons aren’t a hobby, Maya."

    scene shrinetwenty2
    with dissolve

    m "And stalking shrine maidens is?"
    s "I’m not stalking you."
    m "Yes you are. I was enjoying my break and you just showed up and started asking me questions about myself."
    s "What are you even taking a break from? All you do is sweep."
    m "Then I suppose I am taking a break from sweeping."
    m "Are we done now? Or are you going to pester me more?"
    s "I’m going to pester you more."

    scene shrinetwenty6
    with dissolve

    m "Of course you are."

    "Maya lets out a heavy sigh and squeezes her arm. "
    "I can feel her getting annoyed, but I doubt it’s any more annoyed than {i}I{/i} am having to keep up with her all the time."

    s "How was vacation for you? Other than spending the bulk of your second night watching the stars, I mean."

    scene shrinetwenty2
    with dissolve

    if bonus == True:
        m "I wasn’t very fond of the part where you walked in on me getting changed, but other than that it was fine."
    else:
        m "I wasn’t very fond of the part where you existed, but other than that it was fine."

    s "That was actually one of my favorite parts of the whole weekend. "
    m "You’re disgusting."
    m "And yes, I know I’ve said that many times now."
    m "You create too many opportunities. "
    m "You should try being less horrible."
    s "But then I wouldn’t be me."

    scene shrinetwenty7
    with dissolve

    m "That’s debatable."
    m "You still don’t even know who {i}you{/i} are. Isn’t that right?"
    s "You’re right, I don’t. And, to be honest, it’s pretty hard figuring that out without any help."
    s "You’d think if you really wanted me to succeed at this whole ‘reincarnation’ thing, you might actually help me."
    s "Given that you’re the one person who seems to know what’s going on."

    scene shrinetwenty2
    with dissolve

    m "You succeeding only makes things harder for me."
    m "I need you to fail to a certain degree."
    m "Also, I’d appreciate it if you’d stop assuming that I know what’s going on."

    scene shrinetwenty7
    with dissolve

    m "I told you this on the beach, but this world isn’t something I have complete control over. I just know how to manipulate certain parts of it to make things easier."
    m "If “easier” is even the right word to describe it. "
    m "Sometimes, I don’t think it is."
    s "I’m lost again."

    scene shrinetwenty5
    with dissolve

    m "We’re all lost. "
    m "But that doesn’t mean we can’t find our way."
    m "We just need to follow the appropriate steps."
    s "And I’m assuming those steps involve not getting closer to you."

    scene shrinetwenty8
    with dissolve

    m "Perhaps they do. Perhaps they don’t."
    m "What would I know? I’m just a normal [teenage]girl."
    s "A normal [teenage]girl with a set of very abnormal circumstances."
    m "There’s a difference between abnormal circumstances and horrible luck."
    m "Though, I suppose I’ve been blessed with both."
    s "…"
    m "…"

    scene shrinetwenty9
    with dissolve

    m "If you knew when the world was going to end, what would you do about it?"
    s "Is this about the reset thing?"
    m "Perhaps it is. Perhaps it isn’t."
    s "Well, knowing what would happen {i}after{/i} the end of the world would play a big part in determining that."
    s "If I didn’t know the world would just be starting over again, I’d probably spend my last days making sure I don’t have any regrets."
    s "But, if I know things are just going to start over, I don’t think I’d change much at all."
    m "No. You wouldn’t."
    m "You’d keep doing everything exactly the same way while everyone else faces the apocalypse."
    m "Then, you’d watch as a new world forms and fills back up with everything you’ve grown to know over your time there."

    scene shrinetwenty6
    with dissolve

    m "But then, that begins to raise questions."
    m "Is the new world that generates the same as the old one?"
    m "If all of the buildings and structures stay the same, but the people filling them are all replaced with identical copies equipped with altered minds, can we still call it the same world?"
    s "I guess that depends on how much of a person’s worth is tied to their memories."

    scene shrinetwenty2
    with dissolve

    m "That’s a surprisingly insightful answer. Please explain yourself."
    s "Well, after the first reset, everything felt exactly the same. "
    s "It was like the only thing that actually changed was where we were in time."
    s "But the only people that seem to realize that are you and me."
    m "Is that what you believe?"
    s "Is that not the case?"

    scene shrinetwenty7
    with dissolve

    m "I’m not sure."
    m "It’s a confusing situation."
    m "Pretty soon, the seasons will change. "
    m "We’ll be walking to[school] in the snow instead of the sun, and yet no one will think anything of it."
    m "No one but us."
    m "Why is that?"
    m "Something about the way time flows here is different than it should be."

    "Wait, will everyone really just be acting normal once winter comes?"
    "I know it’s right around the corner, but I figured there’d at least be some sort of reaction from people when we get there."

    scene shrinetwenty9
    with dissolve

    m "But I guess things like that don’t particularly matter to you, do they?"
    m "You’re just here to advance yourself."
    m "You’ll treat this like it’s all just a game and, eventually, you too will reach the end."

    scene shrinetwenty10
    with dissolve

    m "But what happens after the credits roll?"
    m "What becomes of everyone inside of that game?"
    m "And what happens if they don’t reset along with the others the next time you press “Start?”"

    scene shrinetwenty11
    with dissolve

    m "I don’t know how many times I’ve said this to you, but this isn’t a game. "
    m "You only think it is."

    "Has she said that to me at all before? "
    "I can’t remember..."

    s "Who says that I think this is a game?"
    s "It's true that, at first, I may have approached it as one."
    s "But as time goes by, I’m beginning to think that this is where I belong. "
    s "I’ll admit that I haven’t been here all that long in the grand scheme of things, but the progress I’ve made with everyone is real."
    s "Isn’t it?"

    scene shrinetwenty6
    with dissolve

    m "Obviously, I won’t know the answer to that."
    m "It’s up to you to figure out what is real and what isn’t."
    m "I’ve already come up with my answer, but you need to learn to think for yourself."
    m "If something feels real to you, then it’s probably real."
    m "But, knowing the type of person you are now, I can’t imagine anything will ever feel that way again."
    s "You feel real to me."

    scene shrinetwenty5
    with dissolve

    m "I’m really, {i}really{/i} tired of hearing that line."
    m "It was cute the first time, but now it’s just getting annoying."
    s "How many times have you heard it exactly?"
    m "Almost the same amount of times I’ve heard that one."
    m "And the one you’ll say after that."

    scene shrinetwenty8
    with dissolve

    m "Sure, there are some minor changes here and there, but everything follows the same pattern for the most part."

    scene shrinetwenty12
    with dissolve

    m "It’s all part of the cycle."
    m "But that’s something you already know."
    m "For now, at least. "
    m "Just keep on living and forget about all of my ramblings. "
    m "Frankly, I’m getting tired of having to explain myself."
    m "Perhaps I should just let you figure things out on your own from now on?"
    s "Definitely don’t do that. "
    s "Part of me feels like I would have gotten caught in that pre-reset loop for months without your help."

    scene shrinetwenty5
    with dissolve

    m "In some regard, I’m sure you already have."

    scene shrinetwenty2
    with dissolve

    m "But, now it’s time for me to get back to work."
    s "Already? But I just got here."
    m "And you’ll be here again."
    m "To be fair, you got a lot more out of me today than you’re supposed to. "
    s "Yeah, you’re rather talkative for someone who isn't in a talkative mood."
    m "And you’re rather obnoxious for someone who is."

    scene shrinetwenty12
    with dissolve

    m "Oh. By the way-"
    m "I may require your help again in the near future. "
    m "I hope you don’t mind carrying a few more boxes."

    scene black
    with dissolve2

    "Maya gets up off of the rock and begins to walk away without saying goodbye."
    "As confused as I am (Both about the boxes and the entire conversation we just had) I don’t call out to her."
    "She was right in saying that I got a lot more out of her today than I normally do."
    "But, even with that, I still don’t feel much closer to her. "
    "I wonder if the two of us will ever meet up on the same wavelength in the future?"
    "And, if so-"
    "I wonder how long it will take to get there."

    $ renpy.end_replay()
    $ maya_love += 1
    $ shrine20 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label shrine25:
...
```

## Code that triggers this event
File: \game\MayaEvents.rpy
Code:
```python
...
label shrine:
    if howifeel == True:
        jump howifeel
    if maya_love >= 0 and firsttimeshrine == False:
        jump firsttimeshrine
    if maya_love >= 5 and shrine5 == False:
        jump shrine5
    if maya_love >= 10 and shrine10 == False:
        jump shrine10
    if maya_love >= 15 and shrine10 == True and mayadorm10 == True and shrine15 == False:
        jump shrine15
    if maya_love >= 20 and beachvacation16 == True and mayadorm15 == True and shrine20 == False:
        jump shrine20
...
```