# A New Beginning (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maya love greater than or equal to 0



## Next events

* [Maya: Mondays](./mayafirsthall.md)

## Event properties

* Id: firsttimeshrine
* Group: Maya
* Triggered by label: shrine
* Triggered by branch label: shrine
* Triggered by path: shrine->firsttimeshrine

## Official wiki page

[A New Beginning](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=firsttimeshrine&go=Go) for more details.

## Event code

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label firsttimeshrine:
    scene anewbeginning1
    with dissolve2
    play music "shrinesong.mp3"

    "I find myself wandering up the stairs to one of the last places I ever expected to be."
    "I’m sure that doesn’t mean much to you considering we haven’t known each other very long, but it’s the truth."
    "I’ve never been a religious person. Or...at least I don’t {i}think{/i} I’ve ever been much of a religious person."
    "Ask me again later and I might have a better answer for you. "
    "But for now, I’ll take cover in the shade provided by the clouds within my head and hope to somehow escape this summer heat unscathed."
    "There’s an old saying here where all Japanese are born Shinto and die Buddhist, but just because it’s a commonly used expression doesn’t mean it’s something that applies to all of us."
    "Some of us are simply born. "
    "Some of us simply die."
    "Some of us get lost somewhere in between those two things."
    "And some of us are lucky enough to wake up in an alternate reality based on sheer luck and no influence from any god whatsoever."
    "I’ll throw myself into that category as it keeps me out of debt with any higher power...and I’ll tell myself that the reason I am standing here right now is not because I am seeking salvation."
    "It is not because I am lost."
    "It is because I wanted to spit in God’s face."
    "I contort my mouth into a grotesque shape and allow saliva to pool up inside of my cheeks, but wind up swallowing it all down when a soft set of footsteps head my way to break me out of my daydreaming."

    q "Oh...wonderful. "
    q "Getting started early this time, I see."

    scene anewbeginning2
    with dissolve

    m "And here I was thinking I’d be able to make it at least the first weekend without you showing up and ruining my day."
    s "I’m sorry?"
    m "It’s nothing. Just...complaining to myself."
    s "Well, feel free to complain to me if you like. We’ve known each other long enough that-"

    scene anewbeginning3
    with dissolve

    m "Oh, give me a break. We both know you’re not who you say you are."
    s "I...have no idea what you’re talking about."
    m "Oh? So you {i}didn’t{/i} just happen to wake up inside of that body and assume the role of someone entirely unfamiliar to you?"

    "How...does she know that?"
    "This has to be some sort of trap, right? "
    "If my own niece wasn’t able to pick up on me taking over, why would one of her friends be able to?"

    s "Nope. In fact, that sounds pretty ridiculous."

    scene anewbeginning4
    with dissolve

    m "It does, doesn’t it?"
    m "Allow me to clue you in on something if you’re going to continue being so determined to walk a mile in someone else’s shoes."
    m "The {i}real{/i} you would have never come to a place like this. So, if you’re going to be that dedicated to playing the part, you should probably just leave now before someone else sees you here."

    "Well, at least that’s one thing the previous inhabitant of this body and I have in common."
    "I say, despite acting out of my own character and deciding to come here anyway for no reason whatsoever."

    s "You’re really just...not going to believe me, are you?"
    m "Sorry. I normally have to get to know someone a little better before I start trusting them like that."
    m "Unfortunately for you, you’re one of the last people I’d ever go out of my way to do that with."
    m "So again, quit while you’re ahead and leave. You’ll be saving both of us a great deal of energy."
    s "Just out of curiosity, are you always this confrontational with me? "
    m "Yes. Yes, I am."
    m "But isn’t that something you would already know if you really were {i}you?{/i}"
    s "Didn’t Ami tell you the other day? I’ve been having-"

    scene anewbeginning5
    with dissolve

    m "Memory problems? Is that really the best that all of you can come up with?"
    m "Just once, I’d like to hear a new excuse and not the same...default answer I always get."
    s "For the last time, I’m-"

    scene anewbeginning6
    with dissolve

    m "If you’re the real Sensei, what’s Ami’s birthday? Here, I’ll even give you a hint. It’s sometime in August."
    s "..."
    m "What’s wrong? Have you really forgotten your own niece’s birthday?"
    s "August..."
    m "..."
    s "Seventh?"
    m "..."
    s "..."

    scene anewbeginning7
    with dissolve

    m "Hah..."

    "Fuck."

    m "Just as I thought. And I even gave you a hint this time and everything."
    m "Though...I guess I have no idea if the {i}real{/i} you would have even remembered that answer in the first place. That was just the type of guy he was."
    s "Just the type of guy I {i}am,{/i} you mean."

    scene anewbeginning8
    with dissolve

    m "Seriously? You’re going to keep the charade up even though I’ve already caught you in like, three different ways so far? How stupid are you?"
    s "Correct me if I’m wrong, but I don’t think shrine maidens are really supposed to be talking to people that way."

    scene anewbeginning9
    with dissolve

    m "Fine. I will. You are wrong and this is me correcting you."
    m "Do you feel like an idiot yet? Are you embarrassed at how easily I managed to see through your act?"
    s "Are {i}you{/i} embarrassed wearing that dress?"
    m "Why would I be embarrassed? I am fucking adorable."
    s "I don’t think shrine maidens are supposed to say “fucking adorable” either."
    m "You sure seem to know a lot about shrine maidens for someone who has yet to even pray. "
    m "Is your affinity for girls who dress like me the reason you came here first this time?"
    m "Am I just fetish material for you? Are you that unabashedly perverted?"
    s "No, I just...didn’t really have a choice, I think."

    scene anewbeginning10
    with dissolve

    m "You...didn’t have a choice? What is that supposed to mean?"
    s "After talking to Ami, I left the house. Then...before I knew it, I was walking up the steps and monologuing about the whole “Born Shinto, Die Buddhist” thing."
    m "Oh, is {i}that{/i} why you looked so pathetic on your way up the stairs? I had just assumed it was because you’re getting too old to walk anymore."
    s "Come on. I’m not that old, am I?"
    m "You tell me. At the very least, you should remember your age. Right?"
    s "..."
    m "..."

    "The longer this conversation carries on, the further Maya manages to press me into a corner. "
    "And as much as I want to say I don’t think she’s serious and that this is all just some sort of...vetting process or something, I understand that it’s much more than that."
    "She knows something. "
    "Something about {i}me.{/i}"
    "Something about how I got here or...where we are or...any of the things Ami wasn’t able to fill me in on during our talk earlier."

    s "..."

    "But-"
    "For some reason..."
    "I can’t bring myself to admit that she’s right out loud."
    "And so I do what I imagine I always did in my previous life."
    "I lie through my teeth in hopes of persuading her."

    s "You’re wrong about me, you know."
    m "No, I’m not."

    "As you can see, it doesn’t work."

    scene anewbeginning11
    with dissolve

    m "So...this monologue you speak of...exactly what did it entail?"
    s "Oh? Are you actually interested in something I have to say now? Or are you just going to use this opportunity to mock me a little more?"
    m "I guess it really depends on your answer. I’m not particularly fond of religion, but I’d be lying if I said it didn’t interest me in...some form."
    s "You’re really just full of anti-miko jargon, aren’t you?"
    m "I’m perhaps the world’s worst {i}and{/i} best shrine maiden all at once. Though, I imagine anyone actually good at this wouldn’t really understand what I consider my strong points."
    s "Well, the monologue wasn’t all that interesting. It was moreso just an excuse for me to be fatalistic on the way up the stairs, I think."
    m "I see."

    scene anewbeginning10
    with dissolve

    m "Well, you’re right about it not being interesting if that’s really all it was. So allow me to use this opportunity to tell you more about what {i}I{/i} think."
    m "Do you have a pen and paper on you? Because this is information that I think you’ll want to keep in mind if you really do want to succeed in this world."
    m "{i}Especially{/i} if you have so many alleged memory issues."
    s "I...don’t really carry that sort of stuff with me."
    m "Aren’t you supposed to be a teacher?"
    s "Just...tell me what you’re trying to tell me, Maya."
    m "Okay. But, if you’re anything like the rest of them, you’re not going to remember any of this anyway. "
    s "Then why bother telling me at all? Since you’re so sure of who I am, I mean."
    m "Because despite my cold demeanor and mostly expressionless face...and the fact that I really just abhor you all around-"
    m "I want to give you a head start."
    m "Or a...chance, so to speak."
    m "It’s the least I can do before permanently severing ties with you."
    s "Permanently? Why does it have to be permanent?"
    m "Because I want absolutely nothing to do with you for reasons I don’t have the time to explain today."
    m "If you must, you may speak to me in school. But only when there are others present and only when what you need to speak about pertains to school itself."
    m "Or anything I personally find interesting. But even then, I’d likely rather just think about those things on my own than discuss them with my friend’s grandfather."
    s "Uncle."
    m "Great uncle?"
    s "Just uncle..."
    m "Apologies."

    scene anewbeginning12
    with dissolve

    "Maya closes her eyes and smacks her broom against the ground but, since the hard part of it is facing upward, the soft part is the one that makes contact with the concrete and barely makes a noise at all."
    "Needless to say, it was a failed attempt at looking cool and I’m hoping that whatever her speech is about winds up earning her some bonus points in that department."

    m "There is an infinite amount of worlds out there...and an infinite amount of possibilities within each and every one of them."
    m "And with an infinite amount of people and souls waiting to be recycled, the contents of each one of those worlds are rapidly changing. "
    m "They spin together, but in different directions. "
    m "Sometimes, they spin so fast that parts of them combine. "
    m "With that in mind, each one of those potential worlds in the never ending, ever expanding list of them is like a cocktail of misfortune and agony with an occasional splash of joy and...mint."
    s "Mint?"
    m "Shut up. I’m not done."

    "Maya slaps the ground with the broom again, but actually looks a little bit cool this time."

    m "Somehow or another, despite the endless amount of possibilities and universes overflowing with the opposites of what we desire-"
    m "Somehow or another, you wound up here. "
    m "At the same shrine as me. "
    m "In the same town as me."
    m "Feigning ignorance and pretending that you’ve been here all along is a slap in the face to whatever force or forces brought you before me."
    m "If you believe that force to be coincidence, coincidence is God. "
    m "If you believe it to be some supernatural entity, {i}that{/i} is your God."
    m "But no matter what “God” you choose and what story you decide on, you must remember first and foremost..."

    scene anewbeginning13
    with dissolve

    m "That none of that matters at all."
    s "..."
    m "..."
    s "What?"
    m "None of it. "
    s "Then why did you even bother-"
    m "Because what matters more than {i}how{/i} you got here is what you are going to do now that you are."
    m "Now that you know how the world works, you are free to ignore it...for the most part, at least."
    s "{i}What?{/i}"
    m "Somehow or another, you were given a life in the same space as me. At the same time as me."
    m "And you would be an absolute moron to not make the most of it- whether you call that life yours or accept that it belongs to someone else."
    s "But...why are you telling me this when you’ve already come out and admitted to disliking me?"
    s "Why help me at all?"

    scene anewbeginning14
    with dissolve

    m "The answer to that is one I’ve already alluded to."
    m "And it’s because..."
    m "From this moment on..."

    scene anewbeginning15
    with dissolve

    m "You will have nothing to do with me."
    m "I don’t care how badly you want to see me. I don’t care if it eats at you from the inside out."
    m "You are strictly forbidden from coming here...and you are strictly forbidden from ever even {i}attempting{/i} to get to know me."
    m "The reason I was willing to help you out to the extent I have today is that {i}my{/i} existence is heavily dependent on yours."
    m "And that existence is in grave danger if you do not heed this warning."
    m "Do I make myself clear?"
    s "Absolutely."
    m "So you agree to leave me alone? And to never come here again?"
    s "Absolutely not."
    m "..."
    s "..."
    m "..."
    s "..."

    scene anewbeginning16
    with dissolve

    m "Hah..."

    "There is no slap of the broom this time- just the resigned sigh of a girl who looks like she’s all out of options."

    m "Predictable as ever."
    s "Why is it so important that I stay away from you? And what do you mean when you say that your existence is dependent on mine?"
    m "What I mean is that I want you to stop looking for answers and just go enjoy your exciting new life surrounded by tons of cute girls not named Maya."
    s "But what if I’m only into girls named Maya?"

    scene anewbeginning17
    with dissolve

    m "Then I suggest you find another."
    m "Because getting close to you is the actual worst thing that could possibly happen."
    s "That’s-"
    m "For {i}both{/i} of us. Not just me."

    scene anewbeginning16
    with dissolve

    m "Now, go. I still have work to do around here."
    m "And don’t worry about me revealing your big {i}secret{/i} to any of the other girls. It’s not like they’d even believe me if I told them anyway."
    s "..."
    m "..."
    s "..."
    m "Why have you not left yet?"
    s "I just figured I’d say thank you first."

    scene anewbeginning13
    with dissolve

    m "Oh?"
    s "Especially since I can’t make good on that whole “leaving you alone” thing."
    m "So you intend to drag the two of us into ruin together? Is that really what you want?"
    s "I have no idea what I want. "
    s "I just know that leaving you out of it won’t be part of the plan."

    scene anewbeginning14
    with dissolve

    m "You’re disgusting. Please leave me alone forever."
    s "I’ll leave you alone {i}for now{/i}."
    s "But I’ll be back soon."
    m "Then I suppose I’ll begin looking for hiding places as soon as you leave. I appreciate you for giving me a heads up."
    s "Same here. Just...with the whole parallel universes thing and not the hiding thing. Even if I...barely understood any of what you were talking about."
    m "I knew that you wouldn’t. Your brain is too smooth and full of sexual fantasies involving your niece and her friends. "
    s "You know you’re one of those friends, right?"
    m "Please don’t ruin my lunch for me before I’ve even had a chance to eat it..."

    scene black
    with dissolve2

    "So..."
    "That’s Maya, I guess."
    "..."
    "She’s a little...different from how I expected her to be."
    "Granted, I wasn’t really sure what {i}to{/i} expect since every interaction I’ve had with her up until now has been extremely brief, but..."
    "Having her...aware of my existence when no one else is?"
    "How is that even possible?"
    "And how can she expect me to just leave her alone after {i}revealing{/i} that she knows all of that?"
    "Of course I’m going to keep coming back to her when she’s presenting an entire platter worth of reasons to do that right in front of my face."
    "I just..."
    "I have no idea where to start when I do."
    "Everything on the platter is something I’ve never seen before."
    "..."
    "But, I guess that’s how {i}everything{/i} is for me now."
    "This life. This town. "
    "It’s all one big platter full of beautiful, new things."
    "..."

    stop music

    "And I can’t wait to get my hands on all of them."

    $ renpy.end_replay()
    $ firsttimeshrine = True
    $ maya_love += 1

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Enjoy your stay in Kumon-mi!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label shrine2to4:
    play music "hammockofpeace.mp3" fadein 2.0
    scene shrine_noon
    with dissolve

    "I head back to the shrine to see if Maya’s there."
    "As I reach the top of the stairs, I spot her sweeping the area around a donation box."
    "She greets me with a mix of confusion and surprise before asking me why
    I’d willingly come back to a place like this."
    "I tell her it’s out of boredom but, honestly, I just like seeing her in her shrine maiden outfit."
    "Eventually, she asks me to leave so she can go back to
    focusing on her duties, and I find myself walking back down the stairs shortly after..."

    $ maya_love += 1
    $ shrinegeneric = True

    "{i}Maya’s affection has increased to [maya_love]!{/i}"

    scene black
    with dissolve
    stop music fadeout 3.0
    "………"
    "……"
    "…"
    jump saturdaynight

label shrine5:
...
```

## Code that triggers this event

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label shrine:
    if howifeel == True:
        jump howifeel
    if maya_love >= 0 and firsttimeshrine == False:
        jump firsttimeshrine
...
```