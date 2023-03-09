# The Virgin of the Apocalypse
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chapthree1&go=Go)


Part of event chain [Utinam Ne Illum Numquam Conspexissem](./returntosummer3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: chapthree1
* Group: Main
* Triggered by label: chap4intro

## Event code
File: \game\chap3.rpy
Code:
```python
...
label chapthree1:
    $ chapthreeactive = True
    "Or at least nothing of {i}value{/i} here."
    "The center of the rooftop is missing perhaps the most important piece of the puzzle there is."
    "And in the space she normally occupies, there is nothing but the memory of her expressionless face and the fading recollection of the way her eyes would catch and reflect the light."
    "I can’t tell her."
    "I can’t tell her anything if she is not here."
    "I can’t."
    "I can’t tell her anything if she is not here."

    ay "Sensei..."

    "There is nothing."
    "No picnic. No scarf. No unenthusiastic welcome or the subtle realization and subsequent acceptance that things are going to be “okay.”"
    "Because they’re not."
    "Things are {i}not{/i} going to be okay."
    "How {i}could{/i} they be? "
    "I still don’t understand what’s supposed to happen next."
    "And I’m even more confused about what is going to happen to {i}her.{/i}"

    ay "Sensei..."
    ay "I don’t see her..."

    "You don’t see her because she’s not there."
    "You don’t see her because she’s already gone."
    "You don’t see her because the two of {i}us,{/i} the ones without hundreds or thousands or millions of years of experience are the ones who managed to make it here in her place."
    "And that she likely vanished or disintegrated or melted or whatever the fuck happens to those of us who aren’t fortunate enough to stand beneath these stars."
    "That’s right..."
    "The stars."
    "She can’t see them anymore."
    "And I still can’t figure out what it is about them that made her fall in love."
    "I can’t do anything."
    "I can’t do anything."
    "I can’t."
    "I can’t if she’s not here."

    ay "Sensei...please say something. This is already weird enough for me and...having you silent is only making me feel worse."

    scene resetwithoutmaya1
    with dissolve2
    play music "meanttobe.mp3"

    s "..."
    ay "..."
    s "This hasn’t ever happened before."
    ay "What hasn’t happened before? Maya not being here?"
    s "..."
    ay "Well...maybe she’s just running late?"
    s "How long were you here before you found me, Ayane?"
    ay "Me?..."
    ay "I...can’t really remember..."
    ay "It all happened so quickly that I wasn’t really keeping track of time..."
    s "..."
    ay "..."

    scene resetwithoutmaya2
    with dissolve

    ay "Well...uhh...at least we have each other! Right?"
    ay "And if the world does wind up doing that...reset thingy, then you and me will go back to the start and...and we can just remind Maya of all the stuff she’s missed!"
    s "It doesn’t work that way, Ayane."

    scene resetwithoutmaya3
    with dissolve

    ay "I..."
    ay "I’m sorry, but I still don’t know how any of this is supposed to work... "
    ay "And without Maya here to clue me in on all of that stuff like you said, the only person who can tell me {i}anything{/i} is you."
    ay "So tell me..."
    ay "Help me understand what happens next. Help me understand how we can...start over and...bring everyone back."
    ay "Maya included."
    s "..."
    ay "..."
    ay "Sensei..."
    s "I don’t know if the Maya you know will {i}ever{/i} come back."

    scene resetwithoutmaya4
    with dissolve

    ay "What?...But you said-"
    s "Everyone starts over. Which they do."
    s "But Maya was doing this for so long that she stopped keeping track of time."
    s "She came to this roof under this sky over and over again and had to put up with me more than any one person should ever have to."
    s "Do you have any idea how long she must have been doing this for, Ayane?"
    ay "I don’t...but-"
    s "Do you think that clearing millions of years worth of memories out of her would result in her being the same person we know today?"
    s "What about thousands? "
    s "Hundreds? "
    s "Even {i}ten{/i} years worth of experiencing this would turn a person into someone else."
    s "If she doesn’t do this with us, we’ll never see {i}her{/i} again."
    s "Sure, there might be someone in her body. But it won’t be {i}Maya.{/i}"
    ay "..."
    s "..."

    scene resetwithoutmaya5
    with dissolve

    ay "Has she...really been doing this for that long?..."
    ay "How come she never said anything?"
    s "I’m sure she tried. But she can’t even {i}talk{/i} about the past to me without risking my brain malfunctioning."

    scene resetwithoutmaya6
    with dissolve

    ay "But...But I talk about the past all the time and you’ve never once {i}malfunctioned{/i} around me!"
    ay "How come I can do it but she can’t? That doesn’t make any sense."
    s "Does any of this make sense?"

    scene resetwithoutmaya7
    with dissolve

    s "Not long ago, I was in the same position you’re in right now. And even though my memory is shit compared to what you want it to be, I can still faintly recall how confused I must have been back then."
    s "But unlike Maya, I’m not ready or even {i}capable{/i} of filling in all of the blanks because I’ve yet to find anything to actually fill them in {i}with.{/i}"
    s "I’m only a little less lost than you are, Ayane. But that doesn’t mean I have any idea where to go from here."

    scene resetwithoutmaya8
    with dissolve

    s "One of the worst parts of this, though...is that I’m pretty sure she tried warning me."
    s "But I just shrugged it off like it was another one of her patented spiritual monologues and pretended that sort of thing wouldn’t ever happen."
    s "I always figured the chances of {i}me{/i} not making it back here were higher than the chances of her, the girl who’s done it for longer than she can even remember, were."
    ay "Sensei...I know you’re...scared and hurt and...probably worried about what’s going to happen to Maya..."
    ay "But please remember that this is just as scary for me..."
    ay "And that even if you don’t know as much as Maya does about what’s happening..."
    ay "That I could really use the comfort right now..."

    scene resetwithoutmaya9
    with dissolve

    ay "It’s my first “end of the world” after all."
    ay "Well...I guess you said it was technically my second. But I don’t have any memories of the first one, so...I guess I’m kind of an apocalypse virgin by proxy."
    s "..."
    ay "..."

    scene black
    with dissolve2

    "She’s right. "
    "The absence of the girl who knows too much doesn’t mean that the one who knows too little should suffer."
    "And despite my inadequacies in the face of understanding this, I should be...figuring out a way to make Ayane more comfortable instead of wallowing in my own self-doubt."
    "It’s just that the idea of doing that when I’m less comfortable than ever before is intimidating to me."
    "This is {i}all{/i} so intimidating to me."
    "And while I’m reluctant to call it codependency because that’s just the type of person I am...could it be anything but?"
    "For the first time, I experience what it means to miss someone."
    "I wish she was here."
    "I wish she was here so I could stop taking the incessant warnings for granted and actually take a step forward in hopes of preparing myself for this exact scenario. "
    "I wish she was here so I could see the shock on her face when she thinks I’ve managed to impregnate Ayane {i}again{/i} and I wish to hear the subsequent “You’re disgusting” that would come from that."
    "But all I hear is the soft, controlled sobbing of another girl who’s gotten too close to me and the faint clopping of our footsteps as we make our way over to a nearby planter."
    "........."
    "......"
    "..."

    scene resetwithoutmaya10
    with dissolve2

    s "..."
    ay "..."
    s "I’m sorry, Ayane."
    ay "Don’t apologize. You never apologize for anything and it’s making me worried."
    s "If there’s ever a time to worry, I’m pretty sure this is it."
    s "The world could end at any given moment and we’d either just...die or pick up from some unknown point in time and have to live our lives all over again."
    s "I guess there’s not much of a difference in either of those things if we can’t remember anything, though."
    ay "If..."
    ay "If something like that really did happen...and we did have to start our lives all over..."
    ay "Do you think there’s anything you’d change?"
    s "..."
    ay "..."
    s "I..."
    s "I think there are things I would want to change."
    s "But I doubt I’d be able to actually make any of those changes happen."
    s "I’d probably be the same cynical...immoral...teenager-fucking narcissist I am now. "
    s "No god or twist of fate would be able to change that."

    scene resetwithoutmaya11
    with dissolve

    s "Assuming you’d still sleep with me, that is. And that you wouldn’t use your new lease on life to make better, more informed, and less impulsive decisions."
    ay "Sensei..."
    ay "You are the one decision in my life that I could not possibly regret."
    ay "Not in this world or any others."

    scene resetwithoutmaya12
    with dissolve

    ay "That doesn’t mean I wouldn’t change {i}anything,{/i} though. There are plenty of regrets I have in my life."
    ay "But if I had to choose {i}one{/i} thing..."
    ay "I’d probably tell my mom I love her more often."
    ay "Maybe that was all it would have taken to keep her around."
    s "It’s just like you to think of someone who abandoned you at a time like this."
    ay "I don’t think it’s that uncommon to think about your parents in what could be your final moments. Even adults cry for their moms sometimes when they’re feeling scared."
    ay "Plus, since I’ve already vowed to keep all of my Sensei-based decisions as-is, having her around would certainly take a load off of {i}your{/i} back."
    s "Having a caring parent around would put a lot {i}more{/i} strain on my back if you truly intend to keep all of your Sensei-based decisions as-is."

    scene resetwithoutmaya13
    with dissolve

    ay "I guess so."
    ay "But hey! We don’t even know for sure if something like that is going to happen yet. "
    ay "For all we know, Maya could show up at any moment and the two of us could welcome her with open arms the same way she’s welcomed you in the past."
    s "She’s not coming, Ayane. She’s never been late before."
    ay "Maybe she’s not late at all?"
    ay "Maybe {i}we’re{/i} just early?"
    s "That seems just as unlikely. "
    ay "How come? Cause it hasn’t happened yet in the few times you’ve done this?"
    ay "That’s not a very big sample size, Sensei. And if you really {i}don’t{/i} know the full details of what’s going on here, can you really say with such conviction that something {i}isn’t{/i} going to happen?"
    s "I don’t know how we got to this point, but I’m pretty sure that I’m the one who’s supposed to be comforting you right now. Not the other way around."
    ay "That’s what I thought at first too. "
    ay "But the longer we sit here...and the longer I stare at that mopey face of yours-"
    ay "The more I understand how important Maya is to you."
    ay "And the more I understand how scared you must be right now."

    scene resetwithoutmaya14
    with dissolve

    s "She’s no more important to me than anyone else is."
    ay "Oh? So you also showed the same level of hesitation every time you’ve come up here to find that everyone {i}other{/i} than Maya was missing?"
    s "Only after being reassured that you’d all come back and be exactly the same."
    ay "I guess that’s a fair point. But I still think there’s a side of it that you’re not telling me."
    ay "Which is fine. I’d never ask you to tell me anything you don’t want to, just like I’d never expect you to do the same for me."
    ay "But, so long as you’re going to sit here looking worried, I’m going to sit right beside you and try to make some of those worries go away."
    ay "That’s what it means to love someone after all."
    ay "And even now, with the stars crashing down around us, there is nothing I am more sure of than the fact that I’d dive in front of one to save your life."
    s "We’d both die if a star ever came that close to us."
    ay "True. But it’s the thought that counts during times like that. And I’m sure your final thoughts of me would be something like, “Wow! Ayane is so cool!”"

    scene resetwithoutmaya15
    with dissolve

    ay "Or maybe the Arakawa and Amamiya families could combine forces and use both of their secret techniques to take the star down once and for all and save everyone?"
    s "This certainly would make a good final installment for the Battle of Kumon-mi, wouldn’t it?"
    ay "If only Todd were here with us."
    s "Did the reset claim him as well?"

    scene resetwithoutmaya16
    with dissolve

    ay "You know, it’s the craziest thing. "
    ay "He just ran out of the dorm the other night faster than I’d ever seen him run before. So fast that even I couldn’t keep up with him."
    ay "I have no idea where he went, but I haven’t seen him ever since. And if every other {i}human{/i} is gone, I guess it wouldn’t be crazy for chickens to follow suit."
    ay "Also, the more I talk about this, the more I realize how weird reality has become and that we really are just living in a simulation. "
    s "This is a really shitty simulation if that is actually true."

    scene resetwithoutmaya17
    with dissolve

    ay "Hey, nobody said it had to be a good one."
    ay "At the end of the day, though...simulation or not..."
    ay "I’m glad I met you."
    ay "And I’m not just saying that because we could die at any given moment."
    s "I’m glad I met you too, Ayane. "
    s "It’s unfortunate that you have to deal with this version of me in what could very well be our final moments."
    ay "If I can’t handle you at your worst, I don’t deserve you at your best."
    s "Would you care to remind me exactly what my “best” is? Because that’s not really a thing I thought I had."

    scene resetwithoutmaya18
    with dissolve

    ay "Your best is the side of you that is able to frown over the loss of a girl who’s done nothing but insult you and avoid you for as long as I’ve known you two."
    ay "Though...I guess there’s a lot more to it that I just don’t understand yet."
    s "..."
    ay "..."

    "I was wrong."
    "There is something of value here."
    "It might not be the sort of value that can guarantee my prolonged existence or assist me in unraveling the mysteries of the universe-"
    "But it’s the sort of value that can manage to make me care a little less about those things as our time runs out."

    ay "So..."
    ay "How long until this actually happens?"

    scene resetwithoutmaya19
    with dissolve

    s "See...that’s the thing."
    s "I don’t really know {i}what{/i} happens now that Maya isn’t here."
    s "This is normally the part where she just resets the world and everything jumps backward or...forward. Or in some other direction."
    s "But I have no idea if there’s like, some sort of time limit to this or anything."
    ay "Well...how exactly does she reset the world?"
    s "I think she just...prays or something. "
    s "She’s told me anyone can do it before, but..."
    ay "But?..."
    s "..."
    ay "..."

    scene resetwithoutmaya20
    with dissolve

    ay "Ah..."
    ay "You can’t bring yourself to try without her here..."
    ay "Is that it?"
    s "Something...like that."
    ay "Well...I’m fine with waiting if you are."
    ay "Maya is important to me as well, even if she {i}is{/i} yet another rival in love now. And one with a pretty distinct advantage at that."
    ay "I wonder if I’d be far ahead too if I was some sort of supernatural time traveler?"
    s "Probably. Those are qualities that are hard to overlook in a romantic interest."

    scene resetwithoutmaya13
    with dissolve

    ay "Let me ask you this, then."
    ay "If we really don’t intend to try this resetting thing {i}without{/i} Maya here, which I am in full support of...do we really want to wait for her? Or do we want to be proactive about this instead?"
    s "Proactive?"
    ay "Like...what if she’s still out there somewhere? "
    ay "What if she’s doing what I did and just frantically searching all over the place for signs of life?"
    s "I think she’s experienced this sort of thing enough by now to know that such an effort is futile."
    ay "Then, better question-"
    ay "What if she’s also wandering around in some random location completely naked right now? Like you were minutes before I found you."
    s "..."
    ay "All I’m saying is that, during a time like this, I think it makes sense for {i}anyone{/i} to go a little crazy. Even if it’s something they’ve seen a bunch of times before."
    ay "Is that a little too optimistic? Probably. But it’s much better to think of crazy, naked Maya than no Maya at all, right?"
    s "That...would certainly be a better alternative, yes."
    s "I thought you checked everywhere, though?"
    ay "Kumon-mi’s a big city, Sensei. There are tons of stones I haven’t turned yet. "
    ay "The only problem is that, if there {i}is{/i} some sort of time limit for this, we might die before we actually find her."
    ay "But at this point, since neither of us want to try going through with this without her, that’s probably going to happen anyway."
    ay "Plus, if I hadn’t made that announcement over the PA, you might still be running around somewhere with your penis flapping in the wind."
    ay "I think that sort of method is worth a shot for Maya. We’ve just...gotta figure out where she is."

    scene resetwithoutmaya21
    with dissolve

    s "That’s..."
    s "I mean, it’s not a {i}bad{/i} idea by any means. It’s just-"
    ay "You’re a pessimist, I know. "
    ay "But even if there is 0.01%% chance of this working, I think we have to try."
    ay "And I think that, if we don’t, we’ll wind up regretting it for the rest of our lives..."

    "I guess...there’s not really any {i}harm{/i} in going out and looking for Maya. Especially since she’d just wind up waiting for me after getting here anyway."
    "But, like Ayane said, Kumon-mi is a huge city...and if Maya is constantly moving around, she could theoretically stay lost forever. "
    "With that in mind, wouldn’t it be best to just wait {i}here?{/i}"

    s "..."

    "My stomach twists itself in knots as I do my best to fight off what I believe at first to be a wave of nausea, but discern moments later as just a sinking feeling in my gut."
    "A feeling telling me to go along with Ayane’s idea despite its flaws and the fact that it could very well backfire and cause both of us to lose ourselves forever."
    "A feeling that I should be discarding in favor of {i}her{/i} safety so that I can ensure at least {i}she{/i} does not have to repeat a life that brought her nothing but pain and perpetual longing."
    "But a feeling that I {i}can’t{/i} discard because it is impossible for me to prioritize the feelings of others over my own."
    "It’s only fitting that my organs would start twisting the moment I come to terms with the possibility of acting selfless."
    "And it’s only fitting that I would risk it all once more in an attempt to move one step closer to the embrace of someone who should only be admired from afar."
    "The idea of Maya living on in my memories without retaining her own makes me sick."
    "But what makes me even sicker is knowing that she’s been stifling that nausea this whole time."
    "And that each and every warning she gave me must have only made it worse. "
    "Before making my decision, a familiar thought crosses my mind."
    "Why does everything have to hurt so much?"

    scene black
    with dissolve2

    "On our way down the stairs and into the street, I bite off a large chunk of my nail."
    "A great deal of my skin comes off along with it."
    "And while I roll it across my teeth and press against the sharpest bit of it with my tongue, I am reminded once more of why everything has to hurt so much."
    "It is not because we want it to."
    "It is because we deserve it."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ chapthree1 = True

    jump chapthree2

label chapthree2:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
label chap4intro:
    "There is nothing."

    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop10 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    jump chapthree1
...
```