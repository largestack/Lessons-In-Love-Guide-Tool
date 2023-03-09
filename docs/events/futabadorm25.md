# Two Hours
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabadorm25&go=Go)



## Event preconditions
✅Futaba love greater than or equal to 25

✅Day of week is a weekend

✅bookdate equal to True (unknown variable)



## Next events
* [Futaba: Under the Table](./library30.md)

## Event properties
* ID: futabadorm25
* Group: Futaba
* Triggered by label: futabadorm
* Triggered by branch label: futabadorm

## Event code
File: \game\DormEvents.rpy
Code:
```python
...
label futabadorm25:
    play sound "knock.mp3"

    s "Futaba, are you in there? "
    f "Just a second, [futabamaster]!"

    scene black
    with dissolve

    "I take a step back and wait for Futaba to finish getting ready."
    "I also hope that {i}getting ready{/i} doesn't constitute anything out of the ordinary- because if she were to get dressed up for this, I'd feel at least a little bad for looking...entirely normal."
    "Not that I have anything else to wear in the first place, but yeah."
    "This is her first “date” ever, though, so who knows?"

    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene bookdateredux1
    with dissolve

    f "Hey! I'm ready to go whenever you are."

    "Oh, good. Looks like I may have jumped the gun in worrying about her getting dressed up for this."
    "But...I should probably be a nice person and compliment her anyway. I think that's how this sort of thing is supposed to go."

    s "Hey, Futaba. You look nice."

    scene bookdateredux2
    with dissolve

    f "What? No...I look the same as always."
    f "I was...originally planning on wearing something else, but...I decided against it at the last second."

    "Ahh, so my hunch wasn't entirely off after all."

    scene bookdateredux1
    with dissolve

    f "But, umm...thank you anyway, Sensei..."
    f "The sun still hasn’t set, so I figured we could walk there instead of taking the bus. Is that okay with you?"
    s "I kind of figured that's what was going to happen anyway, so yeah."

    scene bookdateredux2
    with dissolve
    stop music fadeout 15.0

    f "So...you're okay with that many people seeing us together?...Because I know you said it was fine if it was the book store, but walking around in public is-"
    s "Futaba, stop being weird and just focus on enjoying yourself today. I really don't care who sees us walking around together. It's not a big deal."

    scene bookdateredux3
    with dissolve

    f "R-Right! Yeah! I'm sorry...I'm just a little nervous, I think..."
    f "But if you're okay with me- Uhh...if you're okay with {i}going,{/i} we can leave now..."
    s "Good save, Futaba. Lead the way, I guess. I'm ready when you are."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene bookdateredux4
    with dissolve2
    play music "streetnoise.mp3"

    f "Hmm...It should be somewhere around here...at least based on the address my friend gave me."
    s "How long ago did this place open, exactly?"
    f "A few weeks ago, I think? I’ve heard nothing but good things, though."
    s "And this friend of yours is reliable? You're sure we're not about to walk into some mugging or something?"

    scene bookdateredux5
    with dissolve

    f "That would certainly be a strange plot twist, don't you think?"
    s "Don't smile while acknowledging the probability of us being robbed. It's improper date behavior."
    f "I'm sure we'll be fine, Sensei. My friend is plenty reliable."

    scene bookdateredux4
    with dissolve

    f "But I guess it wouldn't hurt to check for their address online as well..."
    f "Just in case she got her numbers mixed up."
    s "Worst case scenario, we get totally lost and do something else. There's a pretty good porn shop around here that I wouldn't mind taking you to."

    scene bookdateredux6
    with dissolve

    f "I'd...really rather not go some place like that..."
    s "Would you prefer just...staying lost instead?"

    scene bookdateredux4
    with dissolve

    f "I...don't think I'd be opposed."
    f "Getting lost in a...mostly random place with you...seems like it might be kind of fun."
    s "Sure. Except this isn't really a {i}random{/i} place and we both have GPS apps on our phones. Actually being {i}lost{/i} around here seems unlikely."

    scene bookdateredux5
    with dissolve

    f "Hahah...I guess that’s true."
    f "But...fortunately for both of us, it looks like we found the place after all."

    scene black
    with dissolve2

    "I turn around to find a sign advertising the book store we've been on the hunt for as Futaba quickly rushes inside."

    stop music fadeout 8.0

    "She's so excited that she forgets to even hold the door open for me- and under normal circumstances, I’d consider this incredibly rude."
    "But I know she doesn’t mean any harm by it today."
    "She’s just having a hard time containing herself."
    "Kind of like how I am whenever I see her in her pajamas."
    "But that's probably not a thing I should be having an inner monologue about when my {i}date{/i} is running around inside of a book store."
    "………"
    "……"
    "…"

    scene joyoflife1
    with dissolve2
    play music "kimitoakinobouken.mp3"

    f "Wow! Just look at everything, [futabamaster]!"
    f "There’s even more than the library in here!"

    "I wind up needing to follow Futaba up a staircase as she immediately climbs to the highest point of the bookstore."
    "She's not kidding when she says there's more in here than the library. This place feels like somewhere you can get lost in if you're not paying attention."
    "I’m actually pretty shocked, to say the least."
    "From the outside, this shop seemed relatively small."
    "But the inside is like a whole new world."
    "A world full of wonderful things."
    "At least by Futaba’s standards."
    "Me? I honestly couldn’t care less."

    scene joyoflife2
    with dissolve

    f "Isn’t this amazing? It’s even better than I dreamt it would be."
    s "You actually dreamt about a book store?"
    f "Mhm! I dreamt that you and I would come here...and that there’d be millions of stories waiting to be cracked open."
    f "And that you’d pull one of the books from one of the shelves and start reading to me."
    f "Then, I'd rest my head on your shoulder and-"
    s "…"
    f "…"

    scene joyoflife3
    with dissolve

    f "Actually, can you forget I told you about that dream? It started getting really embarrassing once I said it out loud."
    s "Done."

    scene joyoflife4
    with dissolve

    f "I mean...It’s not like I’d try to stop you if you {i}did{/i} do something like that, though...Hahahah..."

    "Futaba, overcome by what seems like sensory-overload, begins to forget how to filter her dialogue."
    "Her fingers pick at the wooden finish of the barrier in front of her as her eyes dart to the side and scan the rest of the store."
    "It’s like paradise to her."
    "And here she is, alone with the one person who can make her heart flutter even more than words can."
    "It’s not conceited to say that, is it?"

    scene joyoflife5
    with dissolve

    f "Are you going to buy anything, [futabamaster]? Is there something in particular you’re looking for?"
    f "I don’t think this place has one of those computers that more modern stores have where you can search the inventory for a particular book but-"
    f "I’ve gotten really good at finding things from working in the library! And I can help you if you want!"
    s "It’s fine. I’m just here to spend time with you."

    scene joyoflife6
    with dissolve

    f "Huh?"
    s "Does that surprise you?"
    f "A little bit, yeah...I figured you would probably buy at least {i}one{/i} thing..."
    f "And hearing you say this was all to spend time with me...made my heart skip a beat or two."

    if bonus == True:
        s "That’s probably because you’re in love with me."
    else:
        s "That’s because you’re starting to like hugs just as much as I do."

    scene joyoflife7
    with dissolve

    f "Keh-!"
    s "Is that like, a new reflex for you or something?"

    scene joyoflife8
    with dissolve

    f "Unfortunately, I think it is..."

    scene joyoflife5
    with dissolve

    f "But...I guess you’re probably right. My heart {i}does{/i} seem to be skipping a lot lately."
    f "I’m sure you have at least {i}some{/i} part in that."
    s "Wow, who could have ever predicted this?"

    scene joyoflife9
    with dissolve

    f "Heheh! I know, right?"
    f "It’s almost like I can’t help but wear my heart on my sleeve around you or something..."
    s "…"
    f "…"

    "A long pause follows Futaba’s innocent laughter."
    "Her fingers stop picking at the finish of the barrier and begin to tremble instead."
    "She takes a deep breath."
    "And then makes a horrible mistake."

    scene joyoflife10
    with dissolve

    f "I like you."
    s "…"
    f "I know you know that already. But I wanted to...finally say it out loud."
    f "You don’t have to say anything back...I’m not an idiot."
    f "I know how weird it is for a student to confess to her teacher..."

    if bonus == True:
        f "And I know you’re probably only spending time with me because I don’t say no to doing {i}that{/i} kind of stuff with you..."
        f "And...I’m honestly okay with that as long as it means that, at least every once in a while...we can do things like {i}this{/i} together."

        scene joyoflife11
        with dissolve

        f "N-Not to say I don’t like doing all of that other stuff! It’s actually...really exciting...and...umm..."
    else:
        s "As long as you understand that, it's fine."
        s "I think we would be better off as book buddies rather than significant others, especially since you have yet to obtain your degree."
        s "Dating a student would be career suicide and that is not a risk I am willing to take."

    scene joyoflife12
    with dissolve

    f "{i}Ugh...What am I even saying right now?{/i}"
    s "…"
    f "…"
    s "Futaba."

    scene joyoflife13
    with dissolve

    f "Y-Yeah?..."

    if bonus == True:
        s "I’m not just using you."
        s "You know that, right?"
    else:
        s "I’m not just using you as a punching bag for hugs. You know that, right?"
        s "Or, I guess it would be a called a hugging bag. I don't really know."

    f "..."
    f "You’re...not?"
    s "No. How many times do I need to say that?"

    scene joyoflife14
    with dissolve

    f "Ummm..."
    f "A million?..."
    s "I don’t think I have that kind of time..."

    scene joyoflife15
    with dissolve

    f "I know, [futabamaster]..."
    f "And I’m trying to understand...Really..."
    f "I just never really expected someone as amazing as you to take the time to actually {i}listen{/i} to me."
    f "I always think that my...feelings fall on deaf ears or that...I’ll be bothering someone if I open up to them."

    scene joyoflife12
    with dissolve

    if bonus == True:
        f "And...while I admit that you’re a lot...umm...{i}hornier{/i} than I thought you’d be...I still know that you listen."
        f "I’m sure there’s some sort of motive for it, whether it be l-l-liking me back or not, but...It’s still kind of hard to believe when I really think about it."
        f "And I feel like even if you {i}did{/i} tell me a million times that's not the case...there’d be a voice in the back of my head saying, “Don’t do it, Futaba! It’s a trap!”"

        scene joyoflife15
        with dissolve

        f "But...I’ve decided-"
        f "Even if this is a trap...and you {i}are{/i} just using me for weird stuff-"
        s "I’m not."
        f "Right. But if you {i}are{/i}...I’m fine with it."
        f "That’s just how much I like you."
        s "…"
        f "…"
    else:
        s "Hm? Did you say something just now? I wasn't paying attention."

    "I’m glad that this book store isn’t as crowded as I initially thought it would be."
    "Because, if it were, I’m sure there would be plenty of eyes on us right now."
    "But, being so high above the only other people in the store, no one can hear us."

    if bonus == True:
        "Futaba’s confession has fallen on me and me only."
        "But it’s a twisted one with an unwarranted dark side to it."
        "Sure, I might be pursuing a number of girls right now, but it’s not like I feel absolutely nothing when it comes to this one."
        "I do like her. As much as I can."
        "I think."
        "I don’t know."
        "It’s gotten annoyingly hard to tell what I really think as of late."
        "But as the two of us stand amidst stacks and stacks of stories under the warm light of a temporary sanctuary-"
        "There is one thing that rings true in my mind."
        "And, it’s that I can not accept this confession."

    s "Futaba."
    f "...[futabamaster]."
    s "I can’t reciprocate your love."

    if bonus == True:
        f "Like I said, I’m okay with being-"
    else:
        f "Yeah, you already said that."

    s "Yet."

    scene joyoflife16
    with dissolve

    f "...Huh?"
    f "Yet?..."
    f "What do you mean by ‘Yet?’"

    if bonus == True:
        s "I mean that it feels wrong standing next to you and hearing that you’re okay with me using you as long as the two of us go to a book store every once in a while."
        f "So...wait."
        f "I’m not sure what you’re saying. Do we need to stop...hanging out? Did I mess things up? Because-"
        s "No. You didn't mess anything up."
        s "It’s just clear to me that your confidence isn’t where it needs to be yet."
        s "And until it is, no confession of yours can possibly stick."

        scene joyoflife17
        with dissolve

        f "But..."
        f "But what if it never gets to where it needs to be?"
        f "What if I can’t ever be happy with who I am?"
        f "Then what?"
        f "I stay on-hold forever?"
        s "You won’t stay on hold forever. I’ll help you."
        f "How?"
        s "I don’t know. But I’ll figure it out."
        s "That's part of my job, isn't it?"
        f "You promise?"
        s "I promise to try."
        f "So..."
        f "So, can I try confessing again once my confidence gets a little better?"
        f "If I do it again after that...will you actually take it seriously?"
        s "You can try confessing whenever you want and I’ll listen each and every time."
        s "But you're right. I won't look at it seriously until I know for sure that you're not treating yourself like some sort of tool."
    else:
        s "Oh, sorry. I didn't mean to say that."
        s "I meant ever."
        f "..."
        s "I will never date you."

    scene joyoflife18
    with dissolve

    f "…"
    s "…"
    f "I like you..."

    if bonus == True:
        s "I already told you, I’m not-"
        f "You told me I can confess whenever I want. So I did it again."
        s "Oh. Well, uhh...thanks?"
        f "No, thank {i}you{/i}. "
        f "For everything..."
    else:
        s "Jesus Christ woman, take a hint."

    scene joyoflife19
    with dissolve

    f "But, umm..."

    "Futaba pauses once again."
    "Her fingers go back to peeling paint off of the barrier."

    f "I guess we should probably start shopping now, huh?"
    f "We’ve kinda...been up here for a while and I think the employees might think we’re up to something..."
    s "Then lead the way. Like I said, I’m here to spend time with you. Go browse to your heart’s content and I'll just...silently follow you or something."

    scene joyoflife20
    with dissolve

    f "{i}*Sniff*{/i} Okay!"
    f "But please bear with me! This might take a while~"

    scene black
    with dissolve2

    "It did take a while."
    "Nearly two hours."
    "But they were two hours I wouldn’t trade for the world."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ futabadorm25 = True
    stop music fadeout 8.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label futabahjreplay:
    play sound "knock.mp3"

    s "Hey, Futaba? Are you alone right now?"
    f "Sensei? Y-Yes...Come on in."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "..."

    if bonus == True:
        jump futabahjreplayx
    else:
        $ futaba_lust += 1
        stop music fadeout 5.0

        "{i}Futaba's lust has increased to [futaba_lust]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label futababjreplay:
    play sound "knock.mp3"

    s "Hey, Futaba? Are you alone right now?"
    f "Sensei? Y-Yes...Come on in."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        jump futababjreplayx
    else:
        $ futaba_lust += 1
        stop music fadeout 5.0

        "{i}Futaba's lust has increased to [futaba_lust]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label futababoobjobreplay:
        play sound "knock.mp3"
        "..."

        f "Yes? Who is it?"

        if bonus == True:
            s "Just a totally normal teacher who isn't here to perv out on his most well-endowed student."
        else:
            s "Sensei McSenseiPants!"

        f "S-Sensei! Someone might hear you!"

        if bonus == True:
            s "Then you better let me in before they ask any questions."
        else:
            s "You are right. I should be more careful or more people will discover my secret true last name that not even Ami knows about."

        scene black
        with dissolve
        play sound "dooropen.mp3"

        if bonus == True:
            jump futababoobjobreplayx
        else:
            $ futaba_lust += 1
            stop music fadeout 5.0

            "{i}Futaba's lust has increased to [futaba_lust]!{/i}"
            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            else:
                jump endofsat

label futabafingerreplay:
    play sound "knock.mp3"
    "..."

    f "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    if bonus == True:
        jump futabafingerreplayx
    else:
        $ futaba_lust += 1
        stop music fadeout 5.0

        "{i}Futaba's lust has increased to [futaba_lust]!{/i}"
        "........."
        "......"
        "..."

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label rindorm25:
...
```

## Code that triggers this event
File: \game\DormEvents.rpy
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
...
```