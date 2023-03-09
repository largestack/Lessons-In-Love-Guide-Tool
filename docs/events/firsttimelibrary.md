# Impossible Blossoms
Futaba event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=firsttimelibrary&go=Go)



## Event preconditions
✅Futaba love greater than or equal to 0



## Next events
None

## Event properties
* ID: firsttimelibrary
* Group: Futaba
* Triggered by label: library
* Triggered by branch label: library

## Event code
File: \game\FutabaEvents.rpy
Code:
```python
...
label firsttimelibrary:
    scene black
    with dissolve2
    play music "morningmoon.mp3"

    "I decide to spend the morning at the library."
    "It’s still a little too early for me to bother getting involved in whatever is going on in the more exciting parts of town, so I figure relaxing in here is probably the best way to avoid that."
    "Besides, the library is attached to the school, which greatly increases my chances of bumping into one of my students and ultimately having sex with them."
    "This calculated move has been brought to you in part by a man with nothing to lose and everything to gain."

    q "Oh! Good morning, Sensei."

    scene blossomredux1
    with dissolve

    s "Good morning, Futaba. What brings you here today?"
    f "The same thing that always brings me here, I suppose...Until someone else volunteers to handle mornings, I'll be right where I always am on Saturday and Sunday."

    "Ah. So Futaba volunteers at the school library over the weekend. I guess that seems pretty in-line with the type of girl she came across as in {i}my{/i} journal."

    f "You’re here early as ever, I see."

    "And...I suppose {i}I{/i} also frequently drop by on the weekends? I guess that's useful to know."
    "I wonder if whoever the last person to possess this body was {i}also{/i} wound up being dragged here by an early morning appetite for immorality?"

    s "You know me. Early bird gets the worm and whatnot."

    "I do my best to feign a slightly pompous teacher-laugh but it sounds pretty terrible and I promise myself to never try that again."

    scene blossomredux2
    with dissolve

    f "Hahaha...right..."

    scene blossomredux3
    with dissolve

    f "Oh! That reminds me...Do you have a moment to go over the homework assignment from last week with me?"
    f "I was going to wait until we were in class again but, seeing as you're here right now...there's not really a need to wait."
    s "Oh. Uhh...sure. You might need to remind me what that assignment actually was, though."
    f "Of course, Sensei. I don't mind at all. Just give me a moment to get my notebook."

    scene black
    with dissolve

    "Futaba retreats behind the front desk and reaches into something on one of the shelves I can't see from where I'm standing."
    "She returns a moment later and pulls up a seat next to me, revealing a bright pink notebook that, based on a few glimpses I'm able to steal of the insides, seems pretty well-used."
    "The scent of her perfume tickles my nostrils as a gust of wind from the open window steers it closer to me."
    "It’s a mix of lemon and lavender- or at least something along those lines."
    "It’s subtle, but enjoyable...The type of scent I wouldn’t mind waking up to every day."

    scene blossomredux4
    with dissolve

    f "The assignment you gave us was another, umm...poetry interpretation thing."
    f "The part I'm having trouble with is this one poem in particular."
    f "I know that all you asked us to do was give you our interpretation of the writer’s words, but...I guess I'm just having trouble actually {i}interpreting{/i} anything."
    s "Not much of a poetry person?"

    scene blossomredux5
    with dissolve

    f "I like it! It's just...harder than what I'm used to."
    f "I...umm...well, I read mostly fantasy. And there's usually a lot less {i}interpreting{/i} to do in books that often overload you on details."
    s "Fair enough. Let's see what we've got here, then."

    "I peer into the notebook and scan the pages for whatever poem Futaba is referencing."
    "Thankfully, her handwriting is both elegant and easy to decipher, so I'm able to find it in no time at all..."

    s "'There are days we live...as if death were nowhere...in the background; from joy to joy to joy..."
    s "From wing to wing...from blossom to blossom...to impossible blossom...to sweet impossible blossom.'"

    f "…"
    s "…"
    f "So...what does all this mean, exactly?"

    menu:
        "Death creeps up on us":
            s "I think this stanza is about how death is much closer than most of us imagine."

            scene blossomredux6
            with dissolve

            f "Really? But that’s in such stark contrast to the rest of the poem."
            s "That’s exactly why this part hits as hard as it does."
            s "Like death itself, this poem embodies the same element of surprise typically associated with it."
            s "The more sudden type of death, of course. Not the drawn-out type we're all subjected to enduring over the course of our lives."
            f "That's...so much darker than I thought. No wonder I couldn't get it."
            s "Of course, we’re all free to create our own interpretations of the work. That’s the entire point of poetry, after all."
            s "I'm just letting you know how I feel about it."
            f "Wow..."
            f "You’re amazing, Sensei..."
            s "I exist."
            s "I might not be a great or attentive teacher, but even I can handle this much."
            jump chosepoem

        "Happiness is fleeting":
            s "The writer is attempting to get across how fleeting happiness can be."

            scene blossomredux7
            with dissolve

            f "That’s actually really close to what I thought at first!"
            f "The use of the ‘impossible blossom’ as a metaphor for happiness shows how unattainable and immature a never-ending state of ecstasy can and would be."
            s "See? It's really not that hard if you just go with your gut feeling."
            s "Overanalyzing things not only serves to break immersion and take you out of a moment, but is often entirely wrong and pointlessly convoluted."
            s "I guess that's just me being a little pretentious, though."

            scene blossomredux8
            with dissolve

            f "Heheh! Maybe..."
            f "Thanks so much for your help, though. I'm a lot more confident in my answer now."
            s "No problem. I expected nothing less from my star student."

            scene blossomredux9
            with dissolve

            f "Oh stop...We both know that role belongs to Makoto..."
            f "She's probably writing up a ten page paper on this as we speak."
            s "Yes, well, Makoto is a monster and that amount of work is entirely unnecessary."
            jump chosepoem

        "He likes blossoms?":
            s "I think the writer just enjoys blossoms."

            scene blossomredux6
            with dissolve

            f "Was it...really that easy? Was I being too analytical?"
            f "I read that stanza at least eight times trying to figure out a meaning, but to think it was as simple as {i}literally{/i} interpreting it-"
            s "Can we talk about something else?"
            s "After reading this, I'm not in the mood for poetry anymore."

            scene blossomredux10
            with dissolve

            f "Oh. Umm...of course. I'm sorry if this-"
            s "It's fine. Just talk about something else."
            f "Then...umm..."
            jump chosepoem

label chosepoem:
    scene blossomredux11
    with dissolve

    f "Oh, Sensei."
    f "I’ve been thinking a lot about your new approach to teaching, and I have a question."
    s "Sure. What’s up?"
    f "So, I understand the informal approach...but I don’t really understand why you want us to treat you more like a friend than an authoritative figure."
    f "Isn’t respect important to you?"
    s "Of course. But you can still respect someone you see as your friend, can’t you?"
    f "You can. It just...seems like a very sudden change of heart to me."
    f "Did something maybe...happen? Is it okay for me to ask that?"
    f "I don't want to...overstep my role as a student, but-"
    s "You're already venturing outside the box again by calling yourself that."
    s "If this relationship is going to work, you're going to need to stay {i}inside{/i} the box and see yourself as a little more than just a student."

    scene blossomredux12
    with dissolve

    f "Y...You're right. And I'm sorry."
    f "This is all just a little embarrassing for me. Being friends, I mean."
    s "And why is that?"
    f "Well, you’re like...so much cooler than all of us. Wouldn’t being our friend make you look bad?"
    s "Look bad in front of who? I don’t talk to anyone else besides all of you girls."

    scene blossomredux13
    with dissolve

    f "So you...don't have a...g...girlfriend or...anything?"
    s "Nope. Just all of you."

    scene blossomredux14
    with dissolve

    f "I see...I think I get it now."
    f "You’re a really...interesting person, Sensei...And I’m really glad that you’re our teacher."
    f "All of the teachers I had before you...never really seemed to care."
    f "But you actually listen to my problems when I come to you for help. And that..."
    f "That means a lot to me."
    s "I'm just doing my job in the least exhausting way possible. And if you ever need help, you know where to find me."
    f "Of course..."

    scene blossomredux15
    with dissolve

    f "On that note, though...maybe I'll start visiting your office again sometime soon?"
    f "I stopped coming because I didn't really want to bother you, but...just...being around you helps sometimes."

    "Futaba's tone changes- like she's admitting something she's been keeping bottled up."
    "The only thing is that the weight of her admission is so light that I can't imagine there was any reason to keep it bottled up in the first place."
    "I'm sure mine would feel that same way to someone else, though."
    "If I could even pinpoint where that weight is coming from, that is."
    "Right now, it all just feels like recycled air."

    s "Anyway...I should probably get going now."
    s "I’ve got a few other things I need to do today."

    "I don't."

    scene blossomredux16
    with dissolve

    f "Oh, right! I’m...sorry for taking up so much of your time. I realize how valuable it is for someone like you."
    s "I came here on my own, remember? You didn't take up anything."

    scene blossomredux17
    with dissolve

    f "Well, I'm sorry anyway. But I'm glad you stopped by again."
    f "I’ll see you in[school], Sensei. And thank you for helping me with my homework."
    s "Any time. I'll see you around, Futaba."

    scene black
    with dissolve2

    "I leave the library and begin to wander the school grounds, hoping that my mind manages to choose a direction to steer me in."
    "It does, but not until I have already lapped the building three times."
    "Futaba and I made eye contact the second time I passed the library window."
    "She still smiled at me, even though she shouldn't have."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ firsttimelibrary = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"
    jump saturdayafternoon

label library2to4:
    play music "morningmoon.mp3" fadein 2.0
    scene library
    with dissolve

    "I head to the library to hang out with Futaba."
    "When I get there, she waves me over to a table and immediately starts talking about some book she’s been reading."
    "It’s surprisingly cute to see how excited she gets when discussing it."
    "And even as someone who doesn’t particularly like reading, I can feel myself getting wrapped up in her description."
    "She’s so much different alone than she is in class."
    "I hope that some day she's able to act like this around everyone else as well..."

    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label futabafall:
...
```

## Code that triggers this event
File: \game\FutabaEvents.rpy
Code:
```python
...
label library:
    if futaba_love >= 0 and firsttimelibrary == False:
        jump firsttimelibrary
...
```