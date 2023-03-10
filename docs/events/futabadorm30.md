# A Tree Falls in the Forest (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Futaba love greater than or equal to 30

* Event [Under the Table](./library30.md) (Futaba) is completed)

* Day of week is not Wednesday



## Next events

* [Futaba: No, You](./library35.md)

## Event properties

* Id: futabadorm30
* Group: Futaba
* Triggered by label: futabadorm
* Triggered by branch label: futabadorm
* Triggered by path: futabadorm->futabadorm30

## Official wiki page

[A Tree Falls in the Forest](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabadorm30&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label futabadorm30:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Futaba’s door and wait to see if she responds. "
    "A few seconds go by without so much as a noise before I decide to try again."

    play sound "knock.mp3"

    s "Hey, Futaba. Are you around right now?"

    "…"
    "…"
    "…"
    "Huh."
    "I guess she’s out?"
    "That’s strange. Futaba is pretty much always in her dorm around this time."
    "It’s a little later than normal today, too...so if she’s not here, maybe she’s out with Rin or...her one friend with the glasses or something??"

    s "…"

    "I stare at the door for a few moments and focus on the handle."
    "I know from past experience that the residents of this room very rarely lock their door...so I {i}could{/i} go in and make sure she's okay."
    "That's certainly never backfired before."
    "Well, not with Futaba at least. But Futaba and I are a lot more {i}physically open{/i} with one another than Rin and I are..."
    "So I'm sure there wouldn't be any harm in me taking a peek inside."
    "It’s just a standard...wellness visit from someone who wasn’t {i}technically{/i} invited but would probably be allowed in nonetheless."

    s "…"
    s "Fuck it."

    "I decide to act on my immoral impulses and give into the curiosity beckoning me closer and closer to the door."

    if day < 6:
        "I’m sure I look like a fucking lunatic to the other girls in the hall right now, but I’m pretty sure they know by now that this is just what I’m like."

    else:
        "Thankfully, no one else is in the hallway to see me slowly inch toward a door that I was not granted permission to open."
        "But even if someone was in the hall, I’m sure me doing something like this wouldn’t come as a complete shock."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "In times like these, it’s customary to say things like “Pardon the intrusion,” or “I’m coming in,” but I decide against both of those options."
    "Because even if it's often worse, sometimes staying silent is the easiest option of all."
    "………"
    "……"
    "…"

    scene futabasleep1
    with dissolve2
    play music "lastdailysong.mp3"

    "Behold, the reason Futaba did not answer the door tonight."
    "She’s already asleep."
    "I wonder if that's why Rin isn't here either? Maybe she's just trying to let her rest or something?"
    "I know Futaba has been spending extra time at the library lately, so I start to wonder if maybe she’s been...overworking herself."
    "I'm not sure how one manages to overwork themself at a {i}library,{/i} but I guess that too much of anything can take a toll on the body."

    s "…"
    f "Nnh..."

    "She moans lightly in her sleep- the type of moan you make when you allow yourself to be swallowed by comfort rather than stress."
    "It’s funny, though....Because she doesn’t look very comfortable."
    "She looks pretty hot actually."
    "And I don't just mean that in the “I want to climb into bed with her” way."
    "Her face is beet-red and she’s dripping sweat."
    "I think back to the beach trip when Futaba decided to leave early due to...slightly mysterious circumstances."
    "I remember Rin saying that it was because she wasn’t feeling well, so..."
    "Could this be more of that?"
    "…"
    "Part of me knows that I shouldn't disturb her when she's sleeping."
    "But another part of me does anyway."

    s "Futaba...Wake up."
    f "Mmn..."

    "I know the last thing you're supposed to do for a sick person is tear them from their rest, but...well, I guess I'm still hoping that she isn't sick at all."

    s "Futaba."

    "I poke her arm in true asshole fashion and force her out of her slumber in order to feel better about myself for coming all the way over here."

    scene futabasleep2
    with dissolve2

    f "Mm?..."
    f "S...Sensei?..."
    s "Hey."
    f "Hey..."

    scene futabasleep3
    with dissolve

    f "Wait, why are you in my room?!"
    f "I didn’t know you were coming over!"
    s "I knocked on the door a few times and you didn’t answer. I just wanted to confirm you were still alive."
    f "You almost gave me a heart attack..."
    s "Are you feeling okay? It looks like you’re burning up."

    scene futabasleep4
    with dissolve

    f "I’m fine..."
    f "How are you?"
    s "I’m also fine, but I don’t think there’s any reason to believe {i}I{/i} wouldn’t be right now."
    f "So...I take it that means you have...reason to believe {i}I’m{/i} lying to you?"
    s "I suppose it does."
    s "It’s not like you to keep things from me. What’s going on? "
    s "Are you sick?"

    scene futabasleep5
    with dissolve

    f "No...The air conditioner is just broken...And I don't...particularly enjoy sleeping without my clothes on, so..."

    if bonus == True:
        s "Would you enjoy it any more if {i}I{/i} took my clothes off and laid with you?"

        scene futabasleep6
        with dissolve

        f "Not really, no."
        f "I highly doubt you’d just...let me sleep if we were naked..."
        s "I apparently have trouble letting you sleep even when we aren’t, so you’re probably right."
    else:
        s "Would you like it a little more if I knelt down and softly sang you the 1997 hit song {i}My Heart Will Go On{/i} by Celine Dion?"

    scene futabasleep4
    with dissolve

    f "Umm...if you’re really...that insistent on helping me, can you get me a bottle of water from under my desk?"
    s "Is this for drinking or do you want me to pour it over your head to try and cool you down?"
    f "For drinking, obviously...It would be a little harder to sleep if my pillow was soaking wet."
    s "Got it. Stay right there."

    scene black
    with dissolve2

    "I walk over to Futaba’s desk and grab her a bottle of water. "
    "She decides to immediately go against my words of advice and sits up on the bed, straightening out her pajamas and doing her best to keep herself propped up."
    "I sit down next to her and hand her the bottle only to have her immediately slump down against me and start gently sipping away."

    scene futabasleep7
    with dissolve2

    f "Thank you..."
    f "I feel bad that you came all the way over here just to take care of me, but..."
    f "I guess having you do that can count as...punishment for walking into a girl’s room without knocking."
    s "I did knock. Several times."
    f "If a tree falls in the forest and no one is around to hear it, does it make a sound?"
    s "Yes. It does."
    s "I never understood why people ask that question."
    s "How would a lack of people being there to observe something translate to that thing not happening at all?"
    s "Just look at the universe. No one was there to see it form and we all know how it happened."

    if bonus == True:
        "{s}With a fleshlight and gallons of celestial cum.{/s}"

    scene futabasleep8
    with dissolve

    f "Keep talking...I like the sound of your voice."
    f "You should monologue around me more often..."
    s "Should I? I normally just keep them inside."
    f "I think so. You have a really...interesting outlook on all sorts of things, Sensei..."
    s "To be completely honest, I can't imagine you or anyone else ever benefitting from my self-indulgent ramblings. "
    s "But we’re not here to talk about me. "
    f "You're right. I’m here to sleep, but apparently I’m not allowed to do that right now."
    s "Correct. Not until you tell me what’s going on."
    s "You don’t have some sort of contagious disease that I’m going to contract now, do you? Because, if so, I should probably just go."
    f "Yes, I have a very contagious disease and you should leave so I can go back to sleep."
    s "If you were any good at lying, you actually might have had a chance to fool me there."

    scene futabasleep9
    with dissolve

    f "Why {i}lie{/i} when it's so much easier to just...hide the truth?"
    s "Interesting. That sounds like something I would say."
    s "Maybe you {i}can{/i} benefit from some of my monologues after all?"
    s "You should still tell me what you’re hiding, though."
    f "Should I?"
    s "Yes."
    f "What’s in it for me if I do?..."
    s "A...book?"
    s "You like those, right?..."

    scene futabasleep10
    with dissolve

    if bonus == True:
        f "This is the one time I choose to give you the opening to say something dirty and you offer me a book?"
        s "Well, what else am I supposed to do? Every time I offer to do something sexual for {i}you{/i}, you back off."
        s "I’m beginning to think you’re just afraid and I don't want to push my luck tonight when I've already overstayed my welcome."
    else:
        f "They're okay, I guess."
        f "I get scared when there are too many of them."
        s "What? Why?"

    scene futabasleep11
    with dissolve

    f "Isn’t something like that a normal thing to be afraid of, though?"

    if bonus == True:
        f "Doing things you’ve never done before?"
        f "Like...weren’t you nervous the first time I touched your penis?"
        s "Not at all. I thought it was pretty awesome, actually."
        f "Well, you’re very welcome. But yes, I am afraid of all sorts of new things."
        f "Not because I’m worried about how it will feel or anything-"
        f "But more because I’m worried of what you’ll think of me after."

        if futabadorm25 == True:
            s "Well first off, I’ve already told you that I’m not going to just abandon you after I have my way with you. "
            f "The word choice there makes me worry even more, Sensei."

        else:
            s "Well first off, I’d never just toss you aside after seeing what you look like on the receiving end. Quite the opposite, actually."

        s "And second, what does that have to do with you hiding your mystery-sickness from me?"
        f "Maybe I’m just really hot because I’m turned on?"
        s "Did you also leave the beach because you were turned on?"
        f "Maybe."
        s "Futaba."
    else:
        s "No."
        s "Is that how you actually feel or is that just the sickness talking?"

    scene futabasleep12
    with dissolve

    f "It’s just a fever. Stop worrying so much."
    f "I probably overworked myself at the library or...stress is just getting to me. I don’t know."
    f "It’s not a big deal. I already told you to not bother worrying about it. I’m sure I’ll be fine in a day or two."

    "That does fit the bill for what I imagined, but..."
    "I don’t know."
    "Something still seems wrong. "

    s "If I find out you have cancer or something, I’m punching you in the face."

    scene futabasleep13
    with dissolve

    f "You’d...punch a cancer-patient in the face?"
    s "I’d punch a liar in the face."
    s "Probably."
    s "Actually, I don’t think I’d hit you under any circumstances."
    s "But I do want you to know that you shouldn’t be afraid of hiding your-"

    scene futabasleep9
    with dissolve

    f "Fever."
    f "It’s just a fever."
    f "I get them pretty often, too. So if it happens in the future, the best thing you can do is just...ask me if I need soup or something."
    f "What you’re doing now is more than enough."
    f "I mean...sure. You’re not letting me rest when that’s a better medicine than anything else but...you’re worried."
    f "Self-centered, too. But definitely worried."
    s "Am I being called out right now?"

    scene futabasleep15
    with dissolve

    f "A little."
    f "I get kind of grumpy when I’m woken up. Let this be a lesson to you."
    s "Wow. It's not every day I see smug expressions like that out of you."

    scene futabasleep14
    with dissolve

    f "I guess I just save them for special moments like this."

    "Futaba nuzzles her head against my shoulder and relaxes her posture."
    "I wish I could say something like, “I feel her skin grow colder as she calms down,” but I’m afraid I can’t."
    "She remains burning up for the rest of my visit."

    scene black
    with dissolve2

    "I wind up leaving after another ten minutes or so."
    "Eventually, I’m talked into feeling bad about interrupting her slumber, so I do the responsible thing and get out of there."
    "I hope I didn’t add to whatever mystery ailment is afflicting her."
    "I’d hate to be the cause of more problems, even if it seems like I’m going out of my way to create them more often than not."
    "But, at the end of the day-"
    "Futaba is important to me."
    "She’s a lovely young girl and I wish her the speediest of recoveries."

    play sound "static.mp3"
    scene treefall1
    with flash
    stop sound
    $ renpy.pause(2, hard=True)
    play sound "static.mp3"
    scene treefall2
    with flash
    stop sound
    $ renpy.pause(2, hard=True)
    scene treefall3
    $ renpy.pause(0.1, hard=True)
    scene treefall4

    $ renpy.end_replay()
    $ futaba_love += 1
    $ futabadorm30 = True
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    scene black

    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label futabadorm35:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label futabadorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if futaba_love >= 5 and futabafall == False and futabafirstvisit == False:
                "Please play Futaba's level 5 Library event to unlock the first dorm event!"
                jump doorknock
            if futaba_love >= 5 and futabafall == True and futabafirstvisit == False:
                jump futabafirstvisit
            if futaba_love >= 10 and futabadorm10 == False:
                jump futabadorm10
            if futaba_love >= 15 and library15 == True and futabanew1 == False:
                jump futabanew1
            if futaba_love >= 15 and futabanew2 == True and futabanew3 == False:
                jump futabanew3
            if futaba_love >= 15 and futabanew3 == True and futabadorm15 == False:
                jump futabadorm15
            if futaba_love >= 25 and day > 5 and bookdate == True and futabadorm25 == False:
                jump futabadorm25
            if futaba_love >= 30 and library30 == True and day != 3 and futabadorm30 == False:
                jump futabadorm30
...
```