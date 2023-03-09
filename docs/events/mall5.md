# Big Shot Teacher
Chika event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mall5&go=Go)



## Event preconditions
✅Chika love greater than or equal to 5



## Next events
None

## Event properties
* ID: mall5
* Group: Chika
* Triggered by label: mall
* Triggered by branch label: mall

## Event code
File: \game\ChikaEvents.rpy
Code:
```python
...
label mall5:
    scene mall1
    with dissolve
    play music "mall.mp3"

    "Once again, I decide to kill some time at the mall."
    "This time, however, it doesn’t look like Chika is on her normal bench."
    "I suppose my streak of perfect convenience comes to an end today as I must now scan the halls of this brightly colored, obnoxiously loud building in order to find her."
    "But it is what it is, I guess."
    "I was honestly beginning to question whether or not she even had a job or if she was just pretending to have one to impress me."
    "Granted, she could {i}actually{/i} be working right now, but...I don't know."
    "I won't believe it until I see it."

    scene mall2
    with dissolve2

    "I walk around the mall for a good ten minutes or so without any sign of Chika, meaning she’s either off today or on the clock right now."
    "If I remember correctly, I think she said she worked at some high-end boutique or something along those lines."
    "The only problem is that I have no idea what counts as {i}high-end,{/i} so I don't even have a place to start."
    "Not knowing what else to do, I check out a nearby directory and pinpoint the store with the fanciest name I can find before beginning my search there..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene mallfive1
    with dissolve2

    c "Hey, welcome-"
    c "Woah! Sensei! I had no idea you were coming in today!"

    scene mallfive2
    with dissolve

    "Chika excitedly throws a handbag onto a display shelf and hurries over to me."

    c "Hey! What are you doing here? Shopping on your day off?"
    c "We're actually having a sale on men's clothing right now, so instead of everything costing like, 90%% of your annual salary, it's probably closer to, like...70%%."
    s "Wow, you really weren’t kidding when you said ‘high-end’ were you?"

    scene mallfive3
    with dissolve

    c "Hahahah~ Oh, come on! You know I’m just messing around!! There's no way we'd charge more than 60%% of your annual salary, tops."
    s "You know, I think I'll stick to my one outfit."

    scene mallfive4
    with dissolve

    c "I get it, no worries. I guess everything here {i}is{/i} still kind of expensive when you compare it to...literally everywhere else."

    scene mallfive4r
    with dissolve

    c "But you’re like, a big shot teacher, right? I’m sure you’ve got some extra cash to spare."
    s "I mean...I wouldn't say I'm {i}poor{/i} by any means, but I'm not really sitting on a mountain of cash either."
    s "Besides, I don’t really think any of this stuff would suit me."

    scene mallfive5
    with dissolve

    c "Hey, don’t say that! I think you’d look really handsome in some of our stuff."
    c "I can help you pick some stuff out, if you want. I'm pretty good at that sort of thing."
    s "Maybe some other time. I sort of just dropped by to see how you were doing today."

    scene mallfive6
    with dissolve

    c "Oh my God! Did you really come all the way over here just to see me?! That’s like, totally adorable!"
    c "How come? Isn’t there someone like, closer to your age you’d rather spend your time with?"
    s "Someone I’d rather hang out with than Chika Chosokabe? Unlikely."

    scene mallfive7
    with dissolve

    c "Oh, stop it. I don't believe that for even a second."
    c "There’s gotta be {i}someone{/i} out there you’ve got, like...more in common with or whatever."
    s "I don’t think we need to have anything in common to enjoy being around each other."
    s "If you enjoy being around me, I mean."

    scene mallfive2
    with dissolve

    c "Oh my God, of course I like being around you! Haven’t you noticed that I’ve been skipping class waaaaay less often lately?"
    c "My grades have been getting a little better-ish, too!"
    c "I mean, I’m sure that’s also thanks to you barely giving us any work, but yeah. I like you."

    scene mallfive8
    with dissolve

    c "Oh! Wait! No! Not like that! That...That probably sounded weird, didn't it? Like...I like you as a {i}teacher.{/i} Or a...friend. Or something."
    s "Don’t worry, Chika. I like you too."

    scene mallfive6
    with dissolve

    c "I...okay! Yeah!"
    c "We...like each other! Which is awesome!"
    s "..."
    c "Well, uhh...just so you know, you can come hang out here whenever you want."
    c "I work most of my shifts alone, so as long as my boss isn’t here and it’s not super busy, I'd love to see you."

    scene mallfive9
    with dissolve

    c "And who knows? Maybe I’ll even let you judge some of the stuff I try on but can’t afford!"
    s "Well, I'm not really known for my fashion sense, but I’d love seeing you dress up."
    c "You’re in luck, then! Part of the job is knowing what would look good on who, and I can't really {i}know{/i} that without trying stuff on myself."
    s "Again, not a fashion icon, but I don't really think that's true."
    c "Well, I won't tell anyone you're here to watch me try on clothes if {i}you{/i} don't tell anyone that it's a perk I've been taking advantage of."

    scene mallfive4
    with dissolve

    c "Just kinda wish dresses looked a little better on me."
    s "Really? Why is that?"

    scene mallfive7
    with dissolve

    c "Mmm...Idunno. I guess they just don’t really fit my style?"
    c "All the clothes I wear are pretty flashy, so trying on cutesy stuff just makes me feel like a loser."
    s "I’m sure you don’t look like a {i}loser.{/i} I can't really see anything not working on you, if you want my opinion."
    s "In fact, I'm going to seize this opportunity and say that you should model a dress for me before anything else."

    scene mallfive10
    with dissolve

    c "How come we've gotta start on hard mode?! What about, like...a tank top or something?"
    c "We've got a whole lingerie section too, you know. Which isn't me implying that I'd model any of it for you. But at this point I'm just trying to steer the conversation away from the dress thing and-"
    s "If lingerie is off the table, I'm going to stick to the dress suggestion."

    scene mallfive7
    with dissolve

    c "I mean...I wouldn't say it's off the table {i}forever...{/i}just..."
    c "Oh my God. What am I even saying right now? I'm sorry, Sensei. I just-"
    s "There's no need to apologize. {i}Other{/i} teachers might get weirded out by the idea of a student offering to one day model underwear for them, but not me."
    s "Which sounds a lot worse when I say it out loud, but I can guarantee it's-"
    c "Uhh...would you maybe...mind keeping your voice down a little? I don't really have a problem with what we're talking about, but I don't want you to, like...get in trouble or anything."

    "I quickly look around to make sure no one's been paying attention to the conversation and confirm that we at least {i}appear{/i} to have gone unnoticed just now."

    s "I think we're fine. But yeah, that's probably not something we should talk about."
    s "Even if it was a completely normal conversation between two people without any ulterior motives whatsoever."

    scene mallfive6
    with dissolve

    c "See, this is why I like you! You’re so chill about everything and like, never make me feel uncomfortable even when we're talking about uncomfortable stuff."
    c "It's kind of like you’re my...big brother or something."

    if bonus == True:
        s "You would model lingerie for your big brother?"
    else:
        s "Sure. A big brother who really fucking likes clowns."

    scene mallfive10
    with dissolve

    c "Well, I-"
    c "Uhh..."
    c "No! Of course not!"
    c "Also, I thought we were moving on!"
    s "I'm sorry if this bursts your bubble, Chika, but I don't really see you as a little sister."

    scene mallfive5
    with dissolve

    c "Well...what {i}do{/i} you see me as, Sensei? Just out of curiosity."
    c "I’ve never had a teacher come visit me at work before. And it’s not like I really view you as {i}just{/i} a teacher either, so..."
    s "I view you as Chika."

    scene mallfive4
    with dissolve

    c "That feels...weirdly embarrassing to hear for some reason..."

    scene mallfive6
    with dissolve

    c "Like, I’m glad you see me as me and not just some...flirty bimbo who’s always breaking dress code and stuff."
    s "It would be kind of hard to view you as a {i}flirty bimbo{/i} since you recently confirmed to me that you’ve never done anything with a boy before."

    scene mallfive10
    with dissolve

    c "Well, that's not because I’m {i}against{/i} it! I just...haven't met the right person yet! Nobody's really interested me or whatever!"
    c "Plus, I’m super busy all the time and like, no one’s schedule would ever match up with mine."
    s "You think so? Because my schedule seems to match up pretty nicely. We even see each other during[school] days."

    scene mallfive3
    with dissolve

    c "Yeah, but it’s not like I can have my teacher as a boyfriend, right? Isn’t that like, totally against the rules?"
    s "Since when do you care about rules?"

    scene mallfive6
    with dissolve

    c "Ooooh, good point. So what, then? You wanna go out, Sensei?"
    s "Would you be able to keep it a secret?"

    scene mallfive10
    with dissolve

    c "Wait, we're still joking, right? I wasn’t...really being serious, but you look super serious right now and it's making me unsure of how to answer."
    s "..."

    if bonus == True:
        "I guess I should probably wait a {i}little{/i} longer before I go down that path with Chika."
        "I keep forgetting how innocent she is despite her subconscious desire to flirt with me every second of the day."
        "I can definitely feel the two of us getting closer quickly, so I'm sure {i}more{/i} is bound to happen eventually, but..."

        s "Let's take a rain check on dating. I need to at least see you in lingerie before I make my final decision."
    else:
        s "Of course it’s a joke. I need to at least see you in a clown costume before I make my final decision."

    scene mallfive9
    with dissolve

    c "Heheh...sounds good to me."
    c "I guess all we can really do is hope you’re not disappointed whenever that time finally comes..."

    scene black
    with dissolve2

    "Chika and I hang out for a little while longer before a few customers walk in and she needs to focus on them."
    "I decide it’s time to head back and we say our goodbyes to one another."
    "Having no other reason to stay at the mall, I board a bus back to the main part of the city and attempt to figure out what to do with the rest of my day..."

    $ renpy.end_replay()
    $ mall5 = True
    $ chika_love += 1
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label mall10:
...
```

## Code that triggers this event
File: \game\ChikaEvents.rpy
Code:
```python
...
label mall:
    if chika_love >= 0 and firsttimemall == False:
        jump firsttimemall
    if chika_love >= 5 and mall5 == False:
        jump mall5
...
```