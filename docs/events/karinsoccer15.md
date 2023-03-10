# Tendrils of Flame (Karin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Still Young](./ayanedorm20.md)

## Event preconditions

* Karin love greater than or equal to 15

* Event [What Was](./day271.md) (Main) is completed)



## Next events

None

## Event properties

* Id: karinsoccer15
* Group: Karin
* Triggered by label: soccerfieldkarin
* Chain sources: ayanedorm20
* Chain sources path: ayanedorm20->saturdaymorning

## Official wiki page

[Tendrils of Flame](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=karinsoccer15&go=Go) for more details.

## Event code

File: (install folder)\game\KarinEvents.rpy

Code:
```python
...
label karinsoccer15:
    scene karinoutage1
    with dissolve
    play music "retrospect.mp3"

    "It’s fucking freezing out today."
    "Sorry for the whiny introduction, but it’s hard to think straight given that my hands are too swollen to even make their way out of my pockets."
    "It doesn’t help that I got here way ahead of schedule either."
    "The sun was just starting to rise when I left the house, but I guess even that giant fucking ball of fire thought it was too cold to bother exploring today."
    "But I guess that’s just how winter can be sometimes."
    "This is the part where I’d normally tangentialize about the harsh realities of winter and how the cold of the air mimics the cold in all of our hearts-"
    "But fuck it."
    "I’m not in the mood today."
    "I need to buy gloves."

    ka "Oh...Sensei."

    scene karinoutage2
    with dissolve

    ka "You’re here...really early today."
    s "Oh, Karin. Good."

    if bonus == True:
        s "Let’s press our bodies together to stay warm."
    else:
        s "We should hug to stay warm."

    scene karinoutage3
    with dissolve

    ka "Ah..."
    ka "Wh...What?"
    s "It’s cold. And chances are we’re going to die if we don’t do something quickly."
    s "If you’re not going to embrace me, let’s at least head inside and-"

    scene karinoutage4
    with dissolve

    ka "Oh...umm..."
    ka "I’m sorry to be the one to break the news, but...practice is cancelled today."
    s "…"
    ka "Sensei?"
    s "So you’re telling me I came all the way over here in the freezing cold for absolutely nothing?"
    ka "Well...there's...me?"
    s "Why didn’t anyone tell me?"
    ka "Umm...the[school] sent out an email about the power being out, so...{i}all{/i} of the clubs are cancelled. Not just ours."
    s "I’m obviously not going to read a work email on my day off. "
    s "If I’m going to do anything involving[school], I’m going to be paid for it."

    scene karinoutage2
    with dissolve

    ka "Do you get paid for coming to soccer practice?"
    s "I..."
    s "I actually don’t know?"

    "Am I supposed to be getting paid for those hours?"
    "I’m going to have to ask Makoto..."

    s "Wait. If the power is out and practice is cancelled...why are you here?"

    scene karinoutage5
    with dissolve

    ka "I...umm..."
    ka "That’s a good question..."
    s "Well as long as it’s not something crazy like you only showing up because you figured I would disregard my emails and come to practice anyway despite my
    inconsistent tendency to do so on a regular basis."

    scene karinoutage6
    with dissolve

    ka "Haha! Yeah! As if I’d ever do something as crazy as that! Hahah!"
    ka "Hahahah!"
    s "That’s exactly what happened, isn’t it?"

    scene karinoutage7
    with dissolve

    ka "That is exactly what happened."
    s "Did you really want to see me that badly?"
    s "Your house is further from the[school] than mine, isn’t it? You’re probably freezing."

    scene karinoutage8
    with dissolve

    ka "I am, but...I really wanted to talk to you."
    ka "Not about anything in particular..."
    ka "I just thought now might be a good time..."
    s "You know you’re allowed to text me whenever you want, right?"
    s "It’s easier to get a hold of me that way compared to waiting behind a place that I may or may not show up to."
    s "Wait, how many times have you done something like this before?"
    ka "I don’t want to talk about that."
    ka "Also, if I text you out of nowhere, you’ll think I’m annoying and then you’ll never respond to me."
    ka "And then you’ll start avoiding making eye contact with me during practice, which will lead Miku to asking me what happened between the two of us."
    ka "Then, when she realizes how crazy I am, she’ll kick me off the team and I’ll have to explain to my parents that I am simply not meant to be in the same place as males."
    ka "The story ends with me becoming a nun. "
    s "It never ceases to amaze me how good you are at-"
    ka "Predicting the future? "
    s "I was going to say nonsensically rambling, but sure. Let’s go with that."
    s "So, there has to be something on your mind, right? There’s no way you’d come all the way over here to “talk about nothing in particular.”"

    if karinlied == False:
        s "Wait...this isn’t about Kirin again is it?"

        scene karinoutage9
        with dissolve

        ka "Oh, no! No..."
        ka "I won’t really bother you about that anymore unless I {i}have{/i} to for some reason..."
        ka "It’s not my room to...pry into her business."

        scene karinoutage10
        with dissolve

        ka "I just...wanted a chance for you to...get to know {i}me{/i} instead of just her."

        if bonus == True:
            ka "I...obviously know that the two of you are much...{i}much{/i} closer than you and me, but..."
            ka "But that doesn’t mean we...can’t still...talk, right?"
            ka "I...I like the time I spend with you. Even if 90%% of it is me tripping over my words and trying not to say anything stupid."
        else:
            ka "Especially since...she's a fucking huge bitch and I want her to die..."
            s "Woah. This isn't canon, is it?"
            ka "It...might be..."

        ka "But...if you think it’s weird...which I wouldn’t blame you at all for...I completely understand."

        "Interesting."
        "I was sure that after Karin’s reaction to hearing the truth about Kirin and me, she wouldn’t have gone out of her way like this for quite some time."
        "If not ever again."
        "But I guess some people are more inclined to wait for themselves to break and patch things up {i}then{/i} compared to safeguarding everything from ever breaking in the first place."
        "Not my best figure of speech but, again, it is fucking cold out."

    else:
        scene karinoutage11
        with dissolve

        ka "No, that’s really what it is!"
        ka "If you think I’m bad at...talking in real life, you should just see me any time I try to send you a text message."
        ka "I go through so many different versions of messages trying to figure out which one's the best and wind up never sending any of them because none of them are good enough."
        s "Karin, are you actually obsessed with me?"

        scene karinoutage12
        with dissolve

        ka "What are you talking about? It’s not like I’m purposely going out of my way to make more time for-"

        scene karinoutage13

        ka "Oh my God, I actually might be."

    s "I’m totally fine with hanging out and talking to you for a while, but..."
    s "Is there anywhere we could do it that isn’t this cold?"

    scene karinoutage14
    with dissolve

    ka "Oh...well, umm..."
    ka "All of the doors to the[school] are locked, but...I do know a place where we’ll at least be safe from the wind."
    ka "And the wind is what makes cold weather like, really cold. You know?"
    ka "Like it could be zero degrees out, but with wind chill it can get all the way down to negative six thousand."
    s "That is a made-up number."
    ka "Six-thousand is most definitely a real number."
    s "…"
    ka "…"

    scene karinoutage15
    with dissolve

    ka "Heheh...I made a joke."
    s "Was that your first one?"
    ka "For you, yes. Don’t pretend that this isn’t a big deal."
    ka "I never would have been able to do that until recently."
    s "Yeah, yeah. I’m so proud of you. Now, can we go to that anti-wind place? One more second out here and I’m probably going to die."
    ka "Of course...it’s not far."
    ka "Just follow me."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene karinoutage16
    with dissolve

    s "This is literally ten feet from where we just were."
    ka "It’s where I was taking shelter in between laps around the[school] building."
    ka "I’m sorry if the build-up made it seem better than it actually is."
    s "Better than nothing, I guess."
    s "So, now what?"
    ka "What do you mean now what?"
    s "Are you planning on making me lead the conversation even though you’re the one who entrapped me?"

    scene karinoutage17
    with dissolve

    ka "Wait, am I the one who is supposed to lead?!"
    s "You’re the pursuer in this scenario, so yeah."
    ka "That’s not what the magazine said! It said the boy will lead!"
    s "That sounds like an incredibly sexist magazine."
    s "Also, since when do you even read things like that?"

    scene karinoutage18
    with dissolve

    ka "It was one of Kirin’s..."
    ka "Since she always has such an easy time talking to you, I thought I might be able to get a little better at it if I did what she does."
    s "Properly socializing isn’t something you can just pull from a magazine."
    s "If communicating was that easy, fifty percent of marriages wouldn’t end in divorce."

    scene karinoutage19
    with dissolve

    ka "Ma...marriage?"
    ka "I just...I just want to have a..."
    ka "But I guess if you’re okay with...someone like me..."
    s "Did you really think a magazine would be the solution to this problem of yours?"

    scene karinoutage20
    with dissolve

    ka "I didn’t {i}not{/i} think it...wouldn’t {i}not{/i} be a solution?..."
    s "…"
    ka "…"
    s "Was that a joke, too?"
    ka "I think it was just me being awkward. I’ve been doing that a lot lately."
    ka "And by a lot I mean for my whole life."
    ka "It’s not just you I get like this with, either. It’s every single boy I’ve ever talked to."
    ka "Even with distant male cousins I’m like “Ahhhhhhhhh!”"
    s "There you go. You’ve picked out a conversation topic. "
    s "Keep rolling with it."

    scene karinoutage21
    with dissolve

    ka "Wait! I don’t even have that many cousins! How am I supposed to talk more about them?"
    s "I meant your past. Family life."
    s "How did the Karin next to me become the Karin I see every week?"
    s "Start at the beginning and just talk until you get bored or something."
    s "I’m much better at listening than I am at talking. And a girl like you is much better off not letting me lead."

    scene karinoutage22
    with dissolve

    ka "Start at the...beginning?..."
    ka "But that’s..."
    s "…"
    s "Not the very beginning..."
    s "Just as far back as you can remember."
    s "I’ll give you a push. What’s the oldest memory you have?"

    scene karinoutage23
    with dissolve

    ka "The oldest memory I have?..."
    ka "Huh..."
    ka "That’s kind of hard..."
    ka "I feel like my memory’s been getting kind of weird lately. Like it’s getting harder and harder to remember things from back then, but-"

    scene karinoutage24
    with dissolve

    ka "Probably when I met my little sister."
    ka "Well, around when I met her at least."
    ka "My oldest memory involves the two of us sitting in a playpen together."
    ka "I don’t think we were doing anything fun or interesting because...you know...babies. But if you want like, my {i}oldest{/i} memory, I think that’s it."
    s "Not surprised to hear your oldest memory involves Kirin."

    scene karinoutage25
    with dissolve

    ka "Why do you say that?"
    s "It just seems like everything you do involves her to some extent."
    ka "Not everything...but a lot. Sure."
    ka "Is that a bad thing, though?"
    s "No, but..."
    s "Doesn’t it ever get tiring?"
    ka "What do you mean?"
    s "Like, don’t you ever wish you were able to just do something on your own without thinking of how it would be if she were there as well?"

    scene karinoutage26
    with dissolve

    ka "Of course...All the time, actually. "
    ka "But having a younger sibling means accepting that you can’t just go off and do everything you want..."
    ka "Because there’s someone always watching you."
    ka "Besides, I don’t even know if I’d be nearly as good at things like sports if Kirin wasn’t around."
    ka "Like, sure, I’m naturally tall and that gives me an advantage."
    ka "But one of the main reasons I started working so hard in the first place was because I wanted to be the cool big sister that she looks up to and brags to her friends about."
    ka "I just wound up falling in love with soccer and stuff in the process."
    ka "So of course I often...think about what it would be like to do things without her and..."
    ka "And..."

    scene karinoutage27
    with dissolve

    ka "And that’s...kind of why I’m here today..."
    ka "Sure, I may have borrowed one of her magazines to give me some pointers but..."
    ka "I showed up."
    ka "And that’s something I didn’t do for anyone but myself..."

    "A long moment of silence squeezes its way into the narrow space between us, expanding and pushing us further apart."
    "I can see the sun expelling its cowardice off in the distance, returning as if to say “I was never gone at all.”"
    "“It was you insignificant humans that misjudged my intentions.”"
    "“But I return now, with tendrils of flame and spotlights that could burn your bodies to a crisp without the correct type of sunscreen.”"
    "The sun can talk in this particular fantasy of mine."
    "The real sun does not talk."
    "Probably."
    "I don’t know, man. It’s fucking cold."

    if karinlied == False:
        scene karinoutage28
        with dissolve

        ka "Can I...ask you something kind of selfish?"
        s "After all of that talk about how you're under constant supervision of your sister? Of course."
        ka "Then..."

        if bonus == True:
            ka "The two of you...being {i}involved{/i}..."
        else:
            ka "If you're going to be...hugging my sister..."

        ka "That doesn’t mean I...have to stop...doing things like this, does it?"
        ka "I feel...a lot safer around you than I do with other boys."
        s "You probably shouldn’t. I’m really not a good person."
        ka "That’s what you say, but...you’ve never done anything wrong to me."
        ka "So until you do...I..."
        ka "I want to keep seeing you."
        s "And if it starts to hurt you?"
        ka "Then I’ll stop and rethink my decision..."
        ka "But right now, this is what I want."
        ka "I didn’t really plan on saying that today, but..."
        ka "Here we are."
        s "Well, of course I think that’s fine as long as it’s what you want."
        s "But I can’t guarantee you you’ll like it."
        s "Similar people have done similar things in your position and-"
        s "…"
        ka "...Sensei?"

        "There’s a thought stuck somewhere in the back of my head."
        "I can’t tell if it’s my own."
        "But it stings a bit."
        "It stings a lot."
        "It’s so fucking cold."

        s "Sorry. Yeah, it’s fine if the two of us continue to spend time together."
        s "I’m your coach, after all. Who is going to hold the stopwatch if I’m not there?"

        scene karinoutage26
        with dissolve

        ka "You’re right. That’s a very important job."
        ka "And, umm...thanks! For bearing the cold with me today."
        ka "Next time I’ll...maybe try and come up with a text message that’s acceptable to send you instead of..."
        ka "Instead of waiting for something that might not ever happen to begin with."

    else:
        scene karinoutage26
        with dissolve

        ka "So...do you think my mission today was a success?"
        ka "Will this be a day that I can look back on and think, “Wow, Karin! Good job!” or am I going to look at myself in the mirror tonight and question every single word I used?"
        s "Knowing you, probably the latter."
        s "But I think it was a success."
        s "Sure, it would probably be a little healthier if your idea of “doing something for yourself” did not involve waiting in the cold for hours-"
        ka "Only like...half an hour."
        s "Okay, but there was the other day at[school] as well."
        ka "Half of that was spent waiting for Kirin, so that doesn’t count."
        s "It definitely counts. Stop waiting in the cold for me to walk by and text me like a normal human being."
        ka "I can try but...I can’t promise it won’t be the worst text message you’ll ever receive in your entire life."
        s "Now I’m just looking forward to how it could possibly be {i}that{/i} bad."
        ka "I’ll figure out a way. You’ll see..."

    scene black
    with dissolve2

    "Only a few more minutes pass by before neither of us can take anymore."
    "We stand up together, do one lap around the[school] together to warm our bodies-"
    "And then head our separate ways."

    $ renpy.end_replay()
    $ karin_love += 1
    $ karinsoccer15 = True
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label karinsoccer20:
...
```

## Code that triggers this event

File: (install folder)\game\KarinEvents.rpy

Code:
```python
...
label soccerfieldkarin:
    if karin_love >= 15 and day271 == True and karinsoccer15 == False:
        jump karinsoccer15
...
```