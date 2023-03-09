# Humans With Hollow Bones
Makoto event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotowinterbeach2&go=Go)


Part of event chain [Condoms in the Sand](./makotowinterbeach1.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: makotowinterbeach2
* Group: Makoto
* Triggered by label: makotowinterbeach1

## Event code
File: \game\MakotoEvents.rpy
Code:
```python
...
label makotowinterbeach2:
    play sound "slidedoor.mp3"
    play music "wewereangels.mp3"

    "Makoto slides open the door and steps aside to let me in."
    "I feel mildly impolite for moving past her, but I do so anyway because asking her to go first would defeat the purpose of her holding the door."
    "I probably should have just been the one to open it."

    scene mikuisheretoo1
    with dissolve

    "Oh."
    "I guess Miku is here?"

    mi "Uhh...hey."
    mi "Sorry for taggin’ along outta nowhere. I know you and Makoto were tryin’ to spend the weekend alone and stuff."
    s "There’s...no need to apologize."
    s "I’m just a little surprised."
    s "But I guess the reason for not being able to do certain things is now a lot clearer."

    if bonus == False:
        mi "This about my coconut allergy?"
        s "Yes. I hate you."

    mi "Oh, don’t let me get in the way of anythin’ like that. Just pretend I’m not even here."
    s "Well, Makoto. You heard her. We can just pretend that she’s not here and-"
    mak "Sensei...you haven’t even been here for half an hour yet."
    mak "Giving up on your promise to be “good” the second Miku says she doesn’t want to get in the way is akin to never having made a promise at all."
    s "Well said. So let’s throw away the promise and-"

    scene mikuisheretoo2
    with dissolve

    mak "Ha ha ha. "
    mak "I’ll allow you to joke while we’re inside, but the second we go back out there, you’re done."
    s "We’re going back out? I thought you were cold?"
    mak "I am cold. But the pizza we ordered while waiting for you is sure to warm me right up."

    scene mikuisheretoo3
    with dissolve

    mi "I know I was supposed to wait to start eatin’ but...I couldn’t just leave a whole pizza sittin’ there lookin’ all lonely and stuff."
    mak "Don’t worry about it. Sensei and I got caught up in a discussion on our way over in the first place."
    mak "I knew very well that asking you to wait that long was just...not going to happen."
    s "Well...since we’re {i}all{/i} here instead of just two of us, what are we going to do now?"
    s "I know Makoto wanted to talk to me about something, but I don’t know if Miku is also part of-"

    scene mikuisheretoo4
    with dissolve

    mi "Oh! I’ll get outta the way now! "
    mi "Like I said, I’m sorry for taggin’ along! It was just a last minute thing and...you know. Stuff."
    s "Yes, I completely understand everything now."
    mi "Yeah! "
    mi "So like...I’ll just go into the other room now and read with...less light."

    scene mikuisheretoo5
    with dissolve

    mi "I mean...who needs eyes anyway, right?! Hahahaha!"
    s "Miku, you don’t have to-"
    mak "Let her go, Sensei."
    mak "I already told her that I wanted to spend some time alone with you this weekend {i}to catch up on[school] related things{/i}, so she knew this was coming."
    mi "Yup! Just two of my best buds schedulin’ a winter beach trip to talk about[school]!"
    s "It definitely doesn’t sound like she thinks we’ll be talking about-"

    if bonus == True:
        mak "School. Which we are. Talking about school is why we’re here."
    else:
        mak "College. Which we are. Talking about college is why we’re here."

    mi "Aaaaand on that note, Miku Maruyama...out!"

    scene mikuisheretoo6
    with dissolve

    mi "Have fun..."

    scene mikuisheretoo7
    with dissolve
    play sound "slidedoor.mp3"

    "Miku grabs her book and her drink and heads to the bedroom."
    "I hear the sound of the light clicking on several seconds later as Makoto and I wait for her to get absorbed in whatever manga or comic she’s currently reading."

    mak "Would you like any pizza, Sensei? There’s plenty for all of us."
    s "I’ll eat later. I’m not hungry right now."

    scene mikuisheretoo8
    with dissolve

    mak "Not eating it now will just cause it to get cold. Are you sure you don’t want to reconsider?"
    s "Pizza is best when it’s been sitting out at room temperature for about half a day. "

    scene mikuisheretoo9
    with dissolve

    mak "I’m sorry, what? That’s completely unsanitary. "
    s "Right. Which is exactly how pizza should be. "
    s "You feel free to gorge yourself, though. Even if you decide to eat the entire thing, I won’t think any less of you."
    mak "No...you probably should think less of me if I eat the entire thing..."

    scene black
    with dissolve

    "Makoto grabs a slice of pizza and places it on a paper plate that she removes from an already opened sleeve of them."
    "Instead of returning to eat at the table, though, she moves to the back of the room...basically as far as we can get from Miku without finding ourselves in the hall."
    "She motions me over and I follow suit, still trying to get a grip on why she might have decided to sit all the way over here."

    scene mikuisheretoo10
    with dissolve

    mak "You sure you don’t want any? I’ll let you have the first bite of mine."
    s "But Makoto, wouldn’t that mean your next bite would be an indirect kiss? "

    if bonus == True:
        s "We’ve already sworn off things like that for the rest of the weekend."

    scene mikuisheretoo11
    with dissolve

    mak "I was just trying to be nice. But yes, if you’re going to be weird about it, I won’t offer you anything ever again."
    s "Now that’s just an overreaction."

    if bonus == True:
        s "In fact, I'm starting to think you strategically brought Miku here to prevent me from making a move on you."
        s "And this is all one elaborate setup to get closer to me by creating roadblocks or something."
    else:
        mak "I am going to steal your nose and hide it in a secret basket."

    s "That sounds like a Makoto thing to do."

    scene mikuisheretoo12
    with dissolve

    mak "I understand why you’d think that, but that really isn’t what’s happening here."
    mak "Also, try to keep your voice down because I don’t want her to hear us."
    mak "We’re probably leaving as soon as I’m done eating anyway."
    s "Sure, yeah."
    s "If that’s not the reason you brought her, though...what is?"
    s "You seemed really excited to get away with just the two of us."
    mak "..."
    s "...?"

    "Makoto doesn’t respond right away- just looks over at the door separating her from her best friend."
    "If this were any other weekend, I’m sure that door would be wide open. "
    "I’m sure the two of them would be spending the night laughing and having pillow fights or doing makeup or...whatever it is [teenage]girls do when they’re locked in confined spaces with one another."
    "Actually, neither of those two wear a lot of makeup, so cross that one off the list."
    "The point is, there’s a reason that Miku is separated from us today."
    "And that reason is..."

    mak "The second floor of the dorm is very loud, Sensei."
    mak "We have several...excitable personalities up there always causing a ruckus and-"
    mak "Well, Miku isn’t good with that sort of thing. Which I know you’re aware of."
    s "Yeah. It’s not fun to witness."

    scene mikuisheretoo13
    with dissolve

    mak "It’s not."
    mak "It’s one thing if it happens while I’m around as I’ve gotten quite good at dealing with her breakdowns over the years-"
    mak "But the thought of her going through something like that on her own is not something I ever want to let happen again."
    s "It’s happened before?"

    scene mikuisheretoo14
    with dissolve

    mak "The last time was right before Christmas."
    mak "I came home from work to find her barely keeping herself together under the bed. "
    mak "Poor thing had ripped so much of her hair out that I had to try and salvage it by giving her a new haircut."

    scene mikuisheretoo15
    with dissolve

    s "Wait, but you guys said you were just giving her a makeover."
    mak "That is what we said, yes."
    s "..."
    mak "..."
    s "Well, why would you lie about something like that?"
    mak "Why would we come out and tell you something that would make literally everyone in a room full of our peers feel uncomfortable?"
    s "Good point."
    s "But that really brings up the question of what else you’ve been hiding from me."

    scene mikuisheretoo16
    with dissolve

    mak "A lot. And part of why I wanted to get together with you here was to come clean about that."
    mak "There are plenty of things that I'm constantly implying and praying that you’ll pick up on...which you never do, by the way-"
    mak "But there are also plenty of things that I’ve been keeping to myself."

    scene mikuisheretoo17
    with dissolve

    mak "My only worry is that coming out and talking about those things might change your opinion of me."
    mak "But, after a heavy analysis of our relationship conducted over the course of several months, I’ve deduced that you think barely anything of me at all."

    if bonus == True:
        mak "That I’ve been nothing but a tool for you to use as you please and-"

    s "Hey. Calm down. It’s not like that."

    scene mikuisheretoo18
    with dissolve

    mak "Well then what is it? "
    mak "Why do you think so little of me even though I do so much for you?"
    mak "It’s really frustrating, you know? "
    mak "I’m tearing up with a slice of pizza in my hand right now. It’s not normal."
    s "I think you’re a great girl, Makoto. "
    s "You’re extremely talented and your dedication to me is almost laughably stern. "
    s "Like, you’d be one of the first people I’d come to if I ever had to bury a body."
    mak "Is that...supposed to make me feel better?"
    s "In a roundabout way, yeah. Yeah it is."
    s "I’m not doing those things because I want to hurt you, it’s just..."
    mak "...Just what?"
    s "Sorry. I’m trying to think of a way to say it that won’t make me sound like an asshole."

    scene mikuisheretoo19
    with dissolve

    mak "I already foresee you failing miserably...so just come out and say it."
    mak "I’ve already told myself I’d try to put an end to it, so if hearing your motivations helps me do that...I want to hear them."
    mak "It will also help me discern whether or not {i}I{/i} am the root cause in all of this. Just please...help me understand."
    s "…"

    "I said something earlier, albeit in the form of a monologue, about how relationships become pointless once one of the parties no longer has anything left to give."
    "But it appears that we’ve run into a situation where I may or may not have already taken everything this bluejay has to offer."
    "And so the logical thing to do would be to repair its wings so it can fly around and gather more sticks and berries or...do whatever it is birds do while they’re not shitting on cars."
    "Birds are so interesting, aren’t they?"
    "Apart from the shitting, I mean."
    "They’re like humans but with hollow bones."

    s "Well, it’s an anticlimactic answer, but I really just...have fun messing with you."
    mak "I have fun when you do that, too..."
    mak "But there are certain times...and a lot of them, might I add, where I want you to really just talk to me and treat me like a human being."

    scene mikuisheretoo20
    with dissolve

    mak "And...I’m not saying I want to go back to just being another student of yours either. I like what we’ve become sometimes."
    mak "I like how you can come to my room and...go on spontaneous beach trips in the middle of winter with me where I drag my friend along out of fear for her safety."
    mak "I’m just saying that sometimes people who you don’t expect to be hurting can be hurting a lot."
    mak "Even when they shouldn’t be."
    s "…"
    s "Yeah."
    s "I’m sorry."

    scene mikuisheretoo21
    with dissolve

    mak "Woah. Was that a real apology?"
    s "It was."
    mak "I didn’t realize you knew how to do that."
    s "I’m full of surprises. It’s just usually better for everyone if I keep them locked away."
    s "Do you mind if I ask you something next, though?"

    scene mikuisheretoo22
    with dissolve

    mak "That depends. Is it going to completely undermine everything that we’ve discussed while I’ve been holding this slice of pizza?"
    s "You know you...can eat that now. Right?"
    mak "At this point, I may as well wait the twelve hours it will take for it to measure up to your standards."

    scene mikuisheretoo23
    with dissolve

    mak "But yes...you can ask me something. "
    s "Then..."
    s "What brought this on? Why now?"
    s "Did I do something recently to upset you or is it just...the buildup of everything {i}else{/i} I’ve done finally piling up so high that you can’t see the top anymore?"
    mak "Neither."
    mak "But this is likely where I start saying things that will make you think I’m entirely unfit for conversation at all."
    s "Try me."
    mak "Are you sure? "
    s "I can assure you that I’ve either heard or experienced things much worse than whatever you’re about to tell me."
    s "I’ve come to realize that basically anything is possible at this point."
    s "So even if you wind up being unfit for conversation with others, I’ll still talk to you."
    mak "Then...forgive me for asking something so strange, but-"

    scene mikuisheretoo24
    with dissolve

    mak "We’ve been here before, haven’t we?"
    mak "Because I...remember it happening. But I don’t remember when."

    if bonus == True:
        mak "I even remember...something that happened between us in the bedroom that Miku is in right now."
        mak "And I...very much hope they changed the sheets."
        s "Me too. It’s been like half a year since then."
    else:
        s "Yeah. It was before one of the resets. The really hard one with the IP address, I think."

    scene mikuisheretoo25
    with dissolve

    mak "So you {i}do{/i} remember! "
    s "Yes, I do. But all I can really say is that it was summer."
    s "I still don’t understand enough to say anything more than that."
    mak "But we shouldn’t have known each other in the summer. This is our first year together as-"

    play sound "static.mp3"
    scene fly with flash
    scene mikuisheretoo26 with flash
    stop sound

    mak "Ngh!"
    s "Makoto? What’s wrong?"
    mak "Nothing! Just...random migraine!"
    mak "There are...painkillers in Miku’s bag..."
    s "Got it. I’ll be right back."
    mak "Th...Thanks..."

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "I open the door to the bedroom and ask Miku if she can help me search for some sort of migraine medication for Makoto."
    "She responds by dumping the entirety of her bag onto the bed and frantically pushing everything aside in search of the right bottle."
    "We eventually find it after creating a huge mess that I leave her to take care of (Sorry, Miku) and then return to Makoto, who promptly swallows the pills without the aid of water."
    "It’s funny how this action alone earns more respect for her in my book than everything she’s told me over the course of the last hour or two."
    "Our conversation never picks back up after that."
    "Instead, the two of us sit around for another hour or so, waiting for her headache to subside before finally making our way back out into the cold..."

    $ renpy.end_replay()
    $ makoto_love += 1
    $ makotowinterbeach2 = True
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

label makotowinterbeach3:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```