# Different Worlds
Maya event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=shrine5&go=Go)



## Event preconditions
✅Maya love greater than or equal to 5



## Next events
* [Main: Normal Office Visit](./day56.md)

## Event properties
* ID: shrine5
* Group: Maya
* Triggered by label: shrine
* Triggered by branch label: shrine

## Event code
File: \game\MayaEvents.rpy
Code:
```python
...
label shrine5:
    play music "hammockofpeace.mp3"
    scene shrine_noon
    with dissolve

    "Once again, I find myself at the shrine without much of an objective in mind."
    "I’ve been coming here a lot lately for reasons beyond my comprehension...but even with that, Maya seems no more open to talking to me than she did when I showed up for the first time."
    "Well, the first time by my standards at least. I have no idea how frequently the {i}last{/i} me showed up. But judging by her reaction, I can't imagine it was all that often."
    "In fact, speaking of Maya...where is she? I feel like she normally questions my existence by now. And if she's not here, I really have no reason to-"

    m "Why?..."
    m "Why do you keep doing this?"

    scene mayasweep1
    with fade

    m "You are already aware that I want nothing to do with you, so why? Why do you continue to show up {i}here{/i} despite that?"
    s "I really wish I had a good reason to give you."
    m "Do you have a good reason for literally anything at any point? Because I really just can't imagine that."
    s "Maybe I was just wondering what you were up to? Am I not allowed to show up and...check on my niece's best friend?"
    m "I’m doing the same thing I do every weekend. Does that answer your question? Are you ready to go home now?"
    s "You’re in a different spot than normal, so you're clearly not doing the same thing you do {i}every{/i} weekend."
    m "This may come as a surprise to you, but I have a tendency to move around at various points in the day."
    s "You mean you {i}don't{/i} stop existing the second I take my eyes off of you?"
    m "No, but I often wish I did."
    s "So, do you have some time to spare? We might as well talk since I'm already here, right?"

    scene mayasweep2
    with dissolve

    m "Wrong. This is actually the part where we forget you ever came here and simply move on with our lives."
    m "I’ve already told you that I have no intention of getting to know you and the fact that you are continuing to disregard that is really starting to grate on me."
    s "I understand that. But what I don't understand is {i}why?{/i} What did I ever do to you?"

    scene mayasweep3
    with dissolve

    m "You? Nothing in particular- but that's likely because I haven't let you."
    s "I don't-"
    m "Do you believe that someone needs to have wronged you in order to avoid them?"
    s "Well, no. But-"
    m "Then I suggest you take issue with someone or {i}something{/i} else."
    m "I am in no position to be associating with you right now. Or...ever, for that matter."
    s "In no position? What does that mean?"
    m "It means that simply being {i}near{/i} you has the potential to greatly alter both of our paths. And that the impending fallout would bring nothing but harm to everyone and everything."
    s "That seems like a pretty major repercussion for just trying to learn about you."
    m "It does. Doesn't it?"
    s "Let's just talk. That's all I want."

    scene mayasweep4
    with dissolve

    m "No. I am very much content with who and what I have now, and I will not back down from that stance just because a man old enough to be my grandfather wants to {i}talk to me.{/i}"
    s "Okay, now that was an exaggeration and you know it. You could pass for my daughter at best."

    scene mayasweep2
    with dissolve

    m "It doesn’t make a difference how old you are, really."
    m "You are you and I am me."
    m "We live in different worlds."
    s "Doesn't that contradict that whole thing you said about us living in the same world?"
    m "Have you never heard of a figure of speech before, you pathetic excuse for a man?"
    s "Wow. My bad."
    m "As I was saying...we live in different worlds."
    s "Yeah, well...your friends don’t seem to think that."

    scene mayasweep3
    with dissolve

    m "That's true. Because their judgement has been clouded by a skewed- no. A {i}mutilated{/i} perception of you."
    m "As unfortunate as it is to say this, I'm the only one who knows what you really are and what you hope to gain in this {i}exciting{/i} new life of yours."
    m "But to everyone else? You're the same person you've always been."
    m "In fact, you're likely even {i}better{/i} to them now than you've always been since the {i}real{/i} you wasn't all that great either."
    m "How fun it must be to start off several steps above {i}unremarkable.{/i} Think of how many boobies you'll get to see if you play your cards right."
    s "Hearing you say “boobies” makes me feel weird."
    m "Hearing you say anything at all makes me feel weird. And by weird, I mean nauseous."
    m "To me, you are nothing more than a worm. But to Ami and Ayane, you're the same man they’ve known since childhood. So it's no wonder they're as...forward about their feelings as they are."
    m "The rest are sure to follow suit. It's simply the way things work here."
    m "But I am an outlier. I am an exception to that."
    m "And no amount of shrine visits or half-hearted attempts to disrobe me are going to change that."
    s "…"

    scene mayasweep2
    with dissolve

    m "What? Have you finally run out of things to say?"
    s "It's less that I've run out of things to say and more that I’m still just...kind of confused about who you are."
    s "Or {i}what{/i} you are."
    m "{i}What?{/i} Is that supposed to be some sort of insult?"
    s "Not really. Just a...skeptical inquiry."
    m "Well, I am sorry to disappoint you...but I'm a normal teenage girl."
    s "I don't think normal teenage girls typically talk about how normal they are."
    m "Oh? And how many others have you pressed with the same line of questioning?"
    s "None. But even if I did, I doubt they'd respond like...{i}that.{/i}"
    m "Would it make you feel better if I spoke more like them? Would it get you any closer to leaving?"
    s "Maya-"

    scene mayasweep5
    with dissolve

    m "Good evening, Sensei! I'm sorry to bother you, but I was wondering if you'd be able to help me with my homework after school."
    m "Then, perhaps afterward...we could maybe hold hands and talk about all of the things we like about one another? Doesn't that sound fantastic?"

    "Maya’s voice moves up an octave or two as an incredibly off-putting impression finds its way out of her mouth."

    scene mayasweep3
    with dissolve

    m "There. Was that more in-line with what you've grown used to over your short time here?"
    s "Not really. And, for the record- saying things like that, even if they're done jokingly, doesn't really fit within the lines your character has drawn for itself so far."

    scene mayasweep6
    with dissolve

    m "{i}Hah...{/i}"
    m "What does it even mean to ‘fit?’"
    s "Is it time to get existential again?"

    scene mayasweep1
    with dissolve

    m "Perhaps. That {i}is{/i} within the lines I've allegedly drawn, is it not?"
    s "It's-"
    m "That was a rhetorical question. I know who I am and how I speak."
    m "What I don't know is why {i}you{/i} seem to believe that things should always appear as you expect or want them to without making a conscious effort to mold them into that form."
    m "You're like a...3D puzzle piece trying to blend in with 2D ones atop the coffee table of...some old person who likes puzzles."
    s "I feel like that wasn't as strong as a lot of your other analogies."
    m "What I'm trying to ask is...do you think that {i}you{/i} fit anywhere?"
    s "Sure. I think I fit in pretty well here, at least."

    scene mayasweep6
    with dissolve

    m "Do you? Or do you just {i}think{/i} you do because you’re assuming the role you were placed into?"
    m "You got a head start. Everyone already loves you."
    m "But you know for a fact that they wouldn't if they could see what I see."
    s "…"

    "I’m not really sure how to respond to that."
    "Not because I’m shocked, but because Maya has managed to pinpoint my exact situation with virtually no hesitation at all."
    "This life is only working as well as it is right now because I’m pretending to be someone else."
    "Or at least living inside of their skin and letting my intuition guide me rather than any goals or concrete thoughts."
    "But...how am I supposed to do anything but that?"
    "How can I emulate a person I never knew in real life?"
    "How can I fill these shoes without knowing the shape of the feet that resided within them before mine, burned by the coals of uncertainty, slipped inside?"

    scene mayasweep3
    with dissolve

    m "Is your sudden silence a sign of agreement?"
    s "Who are you?"
    m "I already told you."
    m "I’m a normal [teenage]girl."
    m "Nothing more, nothing less."
    s "You think it’s normal to talk about things like alternate worlds and reincarnation?"
    m "Do you think it’s normal not to?"
    s "When you’re the only person who’s even mentioned something like that to me so far, yeah. I kind of do."
    m "Maybe everyone else is strange? Maybe {i}I'm{/i} the normal one?"
    s "Are you sure that you’re not some type of...omniscient being or something like that?"
    s "You’re a shrine maiden. So if anyone here has some sort of {i}divine influence{/i} or something-"

    scene mayasweep2
    with dissolve

    m "If I had this so-called {i}divine influence{/i} you speak of, don’t you think I would have taken advantage it by now to make you leave me alone?"
    s "Not if you actually {i}enjoy{/i} my company and are just pretending not to."

    scene mayasweep1
    with dissolve

    m "Ha ha ha. The tsundere role is already filled at our school, I’m afraid."
    s "There can be two. There's no rule against that."
    m "Are we done here? Because I would like to go back to sweeping before the sun sets."
    m "As you can see, this shrine is very large and I am the only person here holding a broom."
    s "And looking very good while doing it."

    scene mayasweep3
    with dissolve

    m "I truly wonder if you will ever make it through an entire conversation without hitting on me."
    s "I think I did a lot better than usual today, so who knows? If I keep improving at this rate, maybe we’ll even start getting along soon?"
    m "Or maybe we won’t and you’ll give up on me entirely."
    s "Sorry, but I can't really see a future where that happens."

    scene mayasweep2
    with dissolve

    m "I'm sure there's one out there somewhere."
    m "There has to be..."

    scene mayasweep3
    with dissolve

    m "Now, please leave. You have insulted this place enough by once again refusing to pray."
    m "And the fact that you are now attempting to woo your [niece]’s best friend is only making things worse. The gods are sure to smite you at this rate."
    s "Okay, okay. I’ll go."
    s "But I'm not going to apologize for bothering you and I want you to know that it is only going to get worse from here on out."

    scene mayasweep2
    with dissolve

    m "Unfortunately, this is one of very few times in my life where I feel obligated to agree with you."
    s "I'll see you later, Maya."
    m "Please don't."

    scene black
    with dissolve2

    "I begin to descend down the shrine's obnoxiously long flight of stairs back to the streets, unsure of what to do with the rest of my day."
    "I don't want to say I've given up on ever understanding Maya at this point, but..."
    "Well, let's just say I've got a lot of work to put in if I ever actually want that to happen..."

    $ renpy.end_replay()
    $ shrine5 = True
    $ maya_love += 1
    stop music fadeout 3.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label shrine10:
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
...
```