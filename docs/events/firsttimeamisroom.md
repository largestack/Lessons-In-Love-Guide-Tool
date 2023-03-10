# Harem Tutorial (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ami love greater than or equal to 0



## Next events

None

## Event properties

* Id: firsttimeamisroom
* Group: Ami
* Triggered by label: amisroom
* Triggered by branch label: amisroom
* Triggered by path: amisroom->firsttimeamisroom

## Official wiki page

[Harem Tutorial](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=firsttimeamisroom&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label firsttimeamisroom:
    scene lr_day
    with dissolve
    play music "normalday.mp3"

    "I step out into a living room that I’ve yet to fully familiarize myself with and think for a moment about who I am and why I am here."
    "But then I remember that there is a cute girl sleeping in the room right next to mine and that any thought I could possibly have apart from that is essentially pointless."
    "I still don’t know much about Kumon-mi...but what’s even more bizarre is that, somehow, I know even less about the girl who’s been guiding me through it thus far."
    "Well, I guess {i}guiding{/i} might be a bit too generous of a word when all she’s really done is provide baseline hints and...vaguely generic information I would have likely figured out on my own."
    "But I guess now is as good a time as any to try and change that."

    play sound "knock.mp3"

    "I knock on Ami’s door, hoping that she hasn’t gone out for the morning as that would leave me alone with nothing but my thoughts- and my thoughts have been rather...intense these last few nights."
    "In a good way, of course. But it’s kind of hard to {i}not{/i} have thoughts like that when you wake up in what I’m pretty sure is the early stages of a harem."

    a "Come in, Sensei! The door is open."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "Good. It looks like my unofficial tour guide and slightly-official niece hasn’t gone out yet."
    "Now, all I have to do is figure out how to talk to her without sounding like a complete creep. And how hard could that possibly be?"

    scene aminewfirstevent1
    with dissolve2

    s "Good morning, Ami. You smell nice."

    "Fuck."

    a "Oh! Umm...thank you! "
    a "Are you sure it’s me and not my room, though? Because I was doing some cleaning a little earlier and sprayed way too much Cleaning Juice all over the place."
    s "Please don’t call it cleaning juice. I don’t like that at all."
    a "Hm? That’s just the name of the brand. It’s some kind of deodorizer or something...Which isn’t me saying that my room normally smells bad. I just...want it to smell better?"
    a "Anyway, if you’re wondering why there’s still stuff all over the place, I’m just taking a little break before I get back to business. I promise it’ll all be gone soon."
    s "Oh, I don’t really care. You can leave your room a mess indefinitely and it really won’t make much of a difference to me."

    scene aminewfirstevent2
    with dissolve

    a "Well, it will make a difference to me since keeping things clean is a good quality and I want you to love me even more than you already do. "

    "Any amount of love at all would be more than what I currently have for this girl..."
    "But I will keep that to myself for the time being as it’s still way too early for me to do something with the potential to ruin this prospective harem."

    scene aminewfirstevent3
    with dissolve

    a "But yeah...I should be done with my room by the afternoon. And I handled the living room and the bathroom yesterday, so that really just leaves the attic after this."
    s "So is cleaning just...what you do as a hobby or something? "

    scene aminewfirstevent4
    with dissolve

    a "Wait a second...is your memory still all weird from when I woke you up from your nap the other day?"
    s "...Yes. That is what is happening."
    a "Should we maybe take you to the doctor or something? Because if you’re still feeling weird all this time later, you might be, like...really really sick or something."
    s "I’m sure I’ll be fine. I just need to get my bearings a little."

    scene aminewfirstevent5
    with dissolve

    a "Never worry, Sensei. Your beloved niece and favorite girl in the entire world, Ami Arakawa, can help you with that."
    a "To start off...no. Cleaning isn’t a {i}hobby{/i} of mine. It’s just something I do because I know you never will."

    "Well, at least that’s one thing the original Sensei and I have in common."

    a "In fact, I handle basically all the chores around here so you can relax to your heart’s content. It’s the least I can do after all you’ve done for me."
    s "I see. So...there’s nothing I need to do to like, repay you for all of your work around here? "
    a "Sensei, all you need to do is repay me with love."
    s "Is there anything {i}else{/i} I can repay you with?"

    scene aminewfirstevent6
    with dissolve

    a "Love is like the easiest thing I could have possibly asked for! Can you at least go back in time to when you remembered you cared about me?!"
    s "Yeah, I don’t really think time works like that. But I do thank you for...all of the work that you apparently do around here while I..."
    s "I..."

    scene aminewfirstevent7
    with dissolve

    a "You can’t even remember what to do with your free time?"
    s "Honestly, it would probably be easier for both of us if you just pretend I know literally nothing about this place."
    a "Hah...I’m starting to feel like one of those NPCs that guides the protagonist in the beginning of an RPG."
    s "I think I know what those acronyms mean, but I’m not sure. So I’m just going to nod in agreement and hope you tell me more about how to live my life."

    scene aminewfirstevent1
    with dissolve

    a "Of course. But only because I’m so used to helping you out when you’re at your lowest point."
    a "Now, I don’t know {i}exactly{/i} how you spend every day...but I do know that you normally try to ration your time so you’re not spending all of it on just one person. {size=15}But if you do, that person should be me.{/size}"

    scene aminewfirstevent8
    with dissolve

    a "Now, let’s see...What are some things to do in the morning?"
    a "Oh. There’s a place called Koi Cafe just a few miles away from here that opened up a couple months ago that you might like."
    a "And the school library is also open on weekends if you ever want to go check out a book or something, so...there’s always that!"
    a "Also, I’m pretty sure the soccer team is looking for a coach as well. But you’ve never really been into sports so I can’t really see you ever going there."
    s "And what about things to do in the afternoon? Anything notable? Or..."

    scene aminewfirstevent1
    with dissolve

    a "Well...there’s the shrine or the dojo, but...again, I have no idea why you’d go to either one of those places."
    a "There’s the mall as well, but..."
    s "I’m going to take a wild guess here and say that you’re assuming I wouldn’t like hanging out in a place like that."

    scene aminewfirstevent9
    with dissolve

    a "Yeah. That’s exactly what I was assuming."
    a "You’re not a very exciting person, Sensei."

    "It’s true that none of those options sound particularly appealing to me...but I am not about to allow myself to be ridiculed by a pubescent redhead in bunny pajamas."
    "But I am also not about to fight back because Ami really is going out on a limb for me here and I don’t want to risk her just...not cooking or cleaning anymore."

    s "There has to be {i}something{/i} else for me to do around noon, right?"
    a "You...could always just walk around and look for something to do, I guess? Most people are busy in the afternoon, so I have no idea if you’ll find anything you’re interested in, though."

    scene aminewfirstevent10
    with dissolve

    a "Oh! You could always come hang out with me! I-"
    s "And what about night? What are some things to do around then?"
    a "..."
    s "..."

    scene aminewfirstevent11
    with dissolve

    a "I’m not sure if I want to tell you anymore if you’re just going to be mean and neglect me."
    s "I’m not neglecting you at all. I came to you first thing in the morning, didn’t I?"
    a "You did...but I’m starting to think you would have just left if I kept a pile of travel brochures near the door."
    s "Hey, if you want to run a travel agency out of your bedroom, that’s fine by me. I’ll be your first customer and everything."
    a "..."
    s "..."

    scene aminewfirstevent12
    with dissolve

    a "Hah...I really hope your memories come back soon, Sensei. I’m kind of tempted to feed you false information just to confuse you at this point."
    s "Please don’t. You’re all I have right now."

    scene aminewfirstevent2
    with dissolve

    a "I’m all you’ll ever have because I’m also all you’ll ever need."

    scene aminewfirstevent1
    with dissolve

    a "But, when it comes to night time...all I can really think of is the school dorms."
    a "Pretty much all of us gather there so, if you’re ever looking to kill some time or come see your adorable niece, that’s where you should go."
    a "I’m sure there’s also some {i}nightlife{/i} stuff you can find if you really want to..."

    scene aminewfirstevent13
    with dissolve

    a "But I’d really prefer you didn’t! "
    s "What? Why not?"
    a "Because that’s where I imagine older girls would be. And if you ever get a girlfriend, I will burn this house to the ground."
    s "..."
    a "..."

    "Okay. I’m beginning to think that Ami may like her uncle a little too much."

    scene aminewfirstevent14
    with dissolve

    a "Did you hear me, Sensei? I said I would-"
    s "Burn this house to the ground. I know. Which, by the way, is completely irrational."
    a "You would think it’s rational if you understood how much I love you."
    s "I can’t imagine that’s true. But I doubt you’d have to worry about something like that in the first place since...relationships aren’t really my type of thing."
    s "Besides, I already have ten girls I need to worry about on a daily basis. I don’t have time for romance."

    "Seduction, however, is another story entirely. But I’m fine with keeping that contained to my students for the time being."

    scene aminewfirstevent1
    with dissolve

    a "This is the best news I have ever heard."
    s "Because you’re not going to be abandoned?"
    a "If you abandoned me, what would happen if I needed to get something off of the top shelf? "
    s "What would happen if you needed to pay rent? Or...the mortgage? "
    s "You don’t happen to know how all of the bills here are handled, do you?"

    scene aminewfirstevent15
    with dissolve

    a "I’m pretty sure that all of our bills are automated since I’ve only seen you use your checkbook like one or two times."
    a "Either that or we’re way behind on every bill we have and will have to go live in an Internet cafe soon."
    s "I’d like to avoid that if at all possible, so I guess I’ll just...look into it on my own or something."
    a "Okay. And I’ll go back to being a teenage girl who doesn’t fully understand what a mortgage is yet."
    s "Sounds good. And thanks for all your help today, Ami."

    scene aminewfirstevent5
    with dissolve

    a "You don’t have to thank me, Sensei. I do this because I love you. Even {i}if{/i} you’d rather spend your free time aimlessly wandering around Kumon-mi instead of calling me pretty and buying me clothes."
    s "Sorry. I’d offer to take you to the mall but, like you implied, that’s just not really a place that a guy like me would hang out at."

    scene aminewfirstevent11
    with dissolve

    a "How the heck did you manage to forget literally everything except how to be sarcastic?"
    s "Luck maybe? I’m not really sure."
    s "But I should probably be heading out. There are a series of places I wouldn’t normally go to calling my name right now, and you need to get back to cleaning anyway."

    scene aminewfirstevent7
    with dissolve

    a "Yeah...I guess I should probably finish up as soon as possible if I’m going to make it back to the dorm by dinner time."
    a "And I haven’t even {i}looked{/i} at the attic yet, so I have no idea how long that’s going to take."
    s "Well...good luck, I guess. "

    scene aminewfirstevent1
    with dissolve

    a "Thanks, Sensei. Have fun taking advantage of your free time and remember to text me every thirty minutes so I know you’re okay."
    s "No."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    a "At least pretend that you’re going to! I deserve at least that much!"

    "I exit Ami’s room and make my way to the front door to see what else this city has to offer."
    "And while I didn’t learn much about my niece herself (Apart from her...extreme affinity for “me”), I do feel a little more at home now."
    "I’m still a fish out of water at the end of the day- but I’m one of those fish that can breathe on land for an extended period of time and won’t just flat out die within the first few minutes."
    "Either way, I’m glad Ami is as helpful and reliable as she’s been so far."
    "I can’t see any way at all that the two of us don’t wind up even closer."
    "It’s just {i}how{/i} close that remains to be seen."

    $ renpy.end_replay()
    $ firsttimeamisroom = True
    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"
    jump saturdayafternoon

label amisroom3to4:
    play music "Normalday.mp3" fadein 2.0
    scene amiroom_day
    with dissolve

    "I decide to spend the morning hanging out with Ami."
    "She tells me a little about some Korean drama show she’s been watching
    while the two of us make breakfast together."
    "It feels strange being involved in a relationship like this out of virtually nowhere, but I'm getting used to it."
    "She seems rather comfortable with me as well..."

    $ ami_love += 1

    "{i}Ami’s affection has increased to [ami_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0

    "........."
    "......"
    "..."
    jump saturdayafternoon

label amisroom5:
...
```

## Code that triggers this event

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amisroom:
    if ami_love >= 0 and firsttimeamisroom == False:
        jump firsttimeamisroom
...
```