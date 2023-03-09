# Two-Octave Pitch Glide
Otoha event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohaspecial10&go=Go)


Part of event chain [Pull the Plug](./otohapark10.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: otohaspecial10
* Group: Otoha
* Triggered by label: otohapark10

## Event code
File: \game\OtohaEvents.rpy
Code:
```python
...
label otohaspecial10:
    "The two of us make our way across town and, while I {i}think{/i} about asking Otoha if she needs any help carrying her things, I decide against it because the walk is kind of long."
    "Not extremely long, but long enough to make me not want to carry her things. Which I guess would be any amount of distance whatsoever."
    "But that’s beside the point."
    "Either way, she doesn’t seem to mind as she gets caught up in a text conversation with who I imagine is either Rin or a mysterious secret girlfriend she is keeping on the side."
    "Maybe that’s why Otoha doesn’t want Rin to meet her parents? Maybe they’ve already met her {i}real{/i} girlfriend?"
    "I can admire that."
    "I’ll have to ask her about how she manages to effectively keep her primary relationship hidden once we finish descending this suspicious staircase."

    scene otohabasement1
    with dissolve2
    play music "brighterdays.mp3"

    o "..."
    s "..."
    o "Something wrong, bud?"
    s "Do you really sing in here? Because I feel like this sort of environment would just kill the mood."
    o "The acoustics are nice at least."

    "I guess Otoha and Rin really weren’t kidding when they were talking about the sketchy basement Otoha gets her vocal lessons in."
    "To think someone like Niki would willingly spend time in a place like this is a little bizarre to me, though."
    "I get that her whole idol persona isn’t really the true “her,” but I can’t imagine the true her would like something dark and damp either."
    "But hey, if Otoha is fine spending time in a room where someone has probably been murdered, more power to her."

    ni "Oh, good. You’re-"

    scene otohabasement2
    with fade

    ni "Wait, why are {i}you{/i} here?"
    s "I want to learn how to sing."
    ni "Oh, okay. So Otoha tried to come alone and you followed her?"
    s "Stop knowing me so well. It makes my sarcasm less funny."

    scene otohabasement3
    with dissolve

    o "You guessed it. Sorry that he knows where you work now. I understand if you want to relocate and I’m willing to help you find some other sketchy basement if you want."
    ni "It’s fine. If it was anyone else, I’d be a little disappointed. But I’ve gotten pretty good at dealing with this thing over the years."
    s "So I’m just a {i}thing{/i} now?"

    scene otohabasement4
    with dissolve

    ni "Yes, but only just barely."
    ni "You can stay here and watch, but if you do anything to disturb my lesson, I’m...going to be really mad."
    s "I am shaking in my boots."

    scene otohabasement5
    with dissolve

    o "Oh, I brought back all those CDs and DVDs you lent me, and you were totally right. It’s really easy to see how you’ve improved over the years if you check everything out side by side."
    ni "I’m still getting better, too. And before long, I’m sure someone else will be saying the same sort of things about your performances."
    s "This is boring."

    scene otohabasement6
    with dissolve

    ni "Okay, {i}now{/i} you can leave."
    o "What exactly did you expect when you agreed to come to a singing lesson?"
    s "Well, singing for one."
    o "We’ve been here for a grand total of two and a half minutes. I don’t even know what today’s lesson is on yet."

    scene otohabasement7
    with dissolve

    ni "Oh, we’ll be working on your stamina today. The longer you’re able to last, the better and more consistent your performance will be."

    "Wow, maybe I {i}do{/i} want to learn how to sing after all."

    o "You’re not going to make me, like...dance are you? Because I can not fucking dance to save my life. And I’m not really trying to be an idol either."
    ni "I’m not going to make you dance. I’m talking more about vocal stamina anyway. "
    ni "And, while dancing does help to build up cardio and exercise your lungs, there are ways to improve it without going down that path."
    o "Welp, I’m ready whenever you are."

    scene otohabasement8
    with dissolve

    ni "Are you able to behave yourself while I show you how a real teacher does her job? Or are you going to continue annoying us until we pay attention to you?"
    s "I’ll just hang out on the couch until the lesson is over."

    if bonus == True:
        ni "If you’re going to watch porn on your phone, please keep the volume muted."
        o "Or just...don’t watch porn on your phone."
    else:
        ni "If you’re going to play Raid: Shadow Legends on your phone, please keep the volume muted."

    s "You two are really asking a lot of me today."

    if bonus == True:
        o "I think not watching porn on my instructor’s couch is a pretty fair thing to ask in exchange for following me across town."
        s "Fine. But I’m only agreeing to prevent Niki from “getting really mad.” I have no idea how I would survive something as rare and unheard of as {i}that.{/i}"
        ni "Have I told you that I hate you yet today? Because I hate you."

    scene black
    with dissolve2

    "Otoha and Niki move to the other side of the room, but that isn’t really saying much since this basement is only slightly larger than my bedroom."
    "I take a seat on the couch and observe my surroundings but, after running out of things to look at after only twenty seconds, I begin to focus on Otoha and Niki instead."
    "It’s refreshing to see the two of them out here this early in the morning just...doing what they love."
    "Even if what they love is no fun to observe if it’s not on some sort of stage."

    scene otohabasement9
    with dissolve2

    "Otoha takes her position near the stairs, straightening her body out and awaiting Niki’s instructions."
    "It’s the first time I’ve actually seen her interested in learning something but, to be fair, it’s not like I’ve created many opportunities for her to feel that way."
    "Maybe I should, though."
    "I mean, if Niki’s going to go out of her way to-"
    "You know what? Nope. I can’t do it."
    "I seriously contemplated the idea of teaching for a fraction of a second right there and I can already feel myself falling asleep."

    play sound "phonering.mp3"
    scene otohabasement10
    with dissolve

    "Oh, good. Someone probably felt that I was in trouble and is calling to keep me occupied and prevent me from falling asleep."

    o "Please tell me you’re not going to-"

    scene otohabasement11
    with dissolve
    play sound "phonebeep.wav"

    s "Hello?"
    o "...answer that."
    ni "Otoha! Eyes forward. Don’t pay any attention to him."

    scene otohabasement12
    with dissolve

    o "Got it."
    ni "If you’re ever going to make it as a musician, you’re going to have to learn how to avoid distractions."
    ni "Let’s make the most of this opportunity by pretending he’s some asshole in the crowd. "
    ni "Now, deep breaths. Take in as much air as you can and start warming up with the two octave pitch glide tactic I taught you. Whenever you’re ready."
    ni "Without the piano this time. You should be able to remember the notes by now. And I {i}will{/i} call you out if you’re off key."
    o "Understood."

    scene otohabasement13
    with dissolve

    s "Hello? Is anyone there?"
    r "{i}Oh! Yeah. Hey. Sorry, I thought I heard Otoha and- wait, yeah. That’s definitely Otoha.{/i}"

    if rinbetrayed == True and bonus == True:
        r "{i}Is she...is she fucking moaning right now?? What is that noise?? What the fuck are-{/i}"
        s "I’m at her singing lesson..."
    else:
        r "{i}But...what are those noises she’s making? What kind of weird stuff are you two getting up to without me?{/i}"
        s "I’m at her singing lesson."

    r "{i}Oh, right! She had one of those today.{/i}"
    r "{i}I was wondering why you didn’t show up to the cafe this morning. But now that I know you’re at her-{/i}"
    r "{i}Wait. Nope. Still not making any sense to me.{/i}"
    r "{i}Are her parents there too? Am I the only one not invited?{/i}"
    s "Yeah. Her entire extended family is here and we’re all saying bad things about you."
    r "{i}Ha ha ha. Do you guys have any plans after that? Because I have to work a little later today and I wanted you to come keep me company.{/i}"
    r "{i}But if both of you are together, that’s even bet- WAIT. IDEA.{/i}"
    r "{i}Otoha’s instructor is your ex, right? How “ex” is she exactly? Like...if I were to propose that all four of us went out on a double date tonight, would that be weird?{/i}"
    s "For me? No. But I figured you’d be a little hesitant given the current state of things."
    r "{i}Me? Nah. I’m over it.{/i}"
    r "{i}Well, not really. But this sounds fun and I kind of, like...need to get out and do something.{/i}"
    s "I’ll ask them, but-"
    r "{i}Shit! Like six million people just walked in. Gotta go, Sensei! Ask Otoha to check her phone whenever she’s done!{/i}"
    s "Sounds good. Talk to you later, Rin."
    o "AAAAaaaaaaAAAAAaaaa-"

    play sound "phonebeep.wav"
    scene otohabasement14
    with dissolve

    o "Wait, Rin? Why was Rin calling you?"
    ni "Ah-ah-ah! Eyes forward!"

    scene otohabasement15
    with fade

    o "Oh, yeah. Sorry...It’s just that the two of us are kind of fighting right now and-"
    ni "Singing now, drama later. You need to get your head in the game."
    ni "You think the audience would give two shits about what’s happening between you and your girlfriend? No. Because the audience wouldn’t even {i}know{/i} about your girlfriend."
    ni "In fact, the audience {i}is{/i} your girlfriend. As long as you’re up on stage, they are the only thing that matters."
    ni "Now, keep going."

    scene otohabasement16
    with dissolve

    o "Right now? But you’re still holding-"
    ni "Keep. Going."

    scene otohabasement17
    with dissolve

    o "A...AAAAAAaaaaaAAAAAaaaaAAAAAHHH..."

    scene black
    with dissolve2

    "Feeling that I’ve already annoyed Niki and Otoha (But mostly Otoha) enough during this lesson, I decide to remain quiet this time around and focus on the two of them as they get lost in their element."
    "Despite not properly following orders or whatever is going on, Otoha’s voice is both powerful and beautiful- which says a lot since she’s just cycling through one sound at different pitches right now."
    "And Niki...Well, she is just as much of a demon as always. But she clearly knows what she’s doing and is a lot more serious about teaching than I expected her to be."

    o "AAAAAAaaaaaah-"
    ni "Stop. No. What is that? What are you doing?"
    o "Huh? What? I...don’t know. What did I do wrong? It sounded fine in my head."
    ni "Yeah, that’s exactly the problem. Look-"

    scene otohabasement18
    with dissolve2

    o "Woah! Niki?"
    ni "Stop focusing so much on your head. Your voice is fine when you sing with that section of your body. What you’re struggling with is down here."
    ni "If you’re going to drop octaves, keeping everything up in your head is going to sound fucking horrible. You need to focus on your diaphragm more. "
    ni "How does it feel when I press there?"
    o "Uhhhhh...I don’t know?"

    scene otohabasement19
    with dissolve

    ni "Liar. Try singing right now."
    o "I...can’t."
    ni "Exactly. Because if I’m pressing down like this, it’s impairing your ability to not only breathe, but to bend and create sounds."
    o "I mean...yeah, but...that’s not really what I-"
    ni "Learning to use this properly is going to be a major key in controlling your stamina and expanding your range."
    ni "It sucks right now because all you’re doing is singing with your head. It’s no wonder you always sound so strained after a few songs. "

    scene otohabasement20
    with dissolve

    ni "And why the fuck is your face so red right now? Are you embarrassed? Why? There is {i}one{/i} person watching you."
    ni "If you’re this red now, I can only imagine how you’ll be when you’ve got thousands of people watching."
    ni "Assuming you’re ever able to perform for more than ten minutes without your vocal cords giving out and-"

    scene black
    with dissolve2

    o "Sorry, just gotta...run to the bathroom really quick! Be back soon!"

    "Otoha breaks away from Niki and darts up the stairs, leaving the two of us alone in the basement together."
    "........."
    "......"
    "..."

    scene otohabasement21
    with dissolve2

    ni "So...having fun?"
    s "You do realize why she was actually blushing that hard, right?"
    ni "Because I’m hot and famous and I was touching her. Anyone with even half of a brain cell would blush like that."
    ni "But I’m not just going to come out and say that to her when it would embarrass her so badly that she’d never come back."
    s "That just means more free time for you."
    ni "I don’t care about free time for myself. Otoha’s got serious potential, and I’ll be damned if I don’t help her get every last drop of it out."
    s "You-"

    if bonus == True:
        ni "If you make a fucking penis joke right now, I swear to God I’ll fucking kill you."
    else:
        ni "No. I do not want to open a food truck with you."
        s "Ugh."

    s "I was just going to say that I admire how strict and dedicated you are to your students. You’re a real role model, Niki."
    ni "I know I am. But thanks anyway."
    o "Okay! Back."

    scene otohabasement22
    with dissolve

    o "Sorry about that. Just needed to get some fresh air."
    ni "In the bathroom? "
    o "..."
    o "There was a window?"
    ni "Whatever. Just get back into position and we’ll start on some more stamina-"
    s "Oh, before that."

    scene otohabasement23
    with dissolve

    ni "What do you mean {i}before{/i} that? We’re on {i}my{/i} time right now. I don’t have all fucking day."
    s "I know. I just wanted to see if you’d go on a date with me."

    scene otohabasement24
    with dissolve

    ni "Wait...an actual date? Like...just the two of us?"
    s "Yeah."
    s "And Otoha."
    o "I’m sorry. What?"

    scene otohabasement25
    with dissolve

    ni "Oh, you better have a good fucking explanation for this."
    s "You know, I actually do this time. "
    ni "Well, then? Out with it."

    scene black
    with dissolve2

    "I tell Otoha and Niki about Rin’s double date idea and both of them seem to be completely fine with it after a short discussion."
    "Strangely enough, it’s actually Otoha who needs a little prodding in order to agree. But I’m sure that’s just because I’m going to be there."
    "Niki, on the other hand, is all for the idea. "
    "In fact, she likes it so much that she even offers to have one of the drivers from her agency come pick us up after a choreography session she has booked after Otoha’s lesson."
    "Not wanting to impose, however, Otoha rejects the idea and uses the whole “Improving her stamina” thing as an excuse to walk there instead."
    "Eventually, the two of them are able to get back to Otoha’s lesson, while I-"
    "Well..."

    if bonus == True:
        "Let’s just say I wound up watching something on my phone that neither of them wanted me to watch for the next hour."
    else:
        "Let’s just say I spent some time playing the number one mobile game of all time- Raid: Shadow Legends."

    "But..."
    "At least it was muted."

    $ renpy.end_replay()
    $ otoha_love += 1
    $ niki_love += 1
    $ otohaspecial10 = True
    stop music fadeout 10.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "........."
    "......"
    "..."

    jump otohadorm10

label otohadorm10:
...
```

## Code that triggers this event
File: \game\OtohaEvents.rpy
Code:
```python
...
s "I don’t think it’s wrong to want to create a world where things won’t get any more complicated than your relationship with one person- but that sort of thing isn’t realistic."
    s "And I think that you know, even if you won’t admit it, that there would just be a different problem soon enough if this thing with your parents never happened."
    o "I don’t know that. How could someone ever know that?"
    o "The only thing I {i}know{/i} is that they’re the problem right now. And that if it weren’t for them, Rin and I would still be just as happy as we were before the Christmas party."
    o "I want that back."
    o "I don’t like where we are now."
    s "Then go somewhere else. Do something about it. "
    s "How much of what you’ve told me today have you told her?"
    o "To be totally honest...not a lot."
    o "But she’s hard to talk to about stuff like this. I don’t want her to internalize it and think it’s all on her when, in all actuality, it’s my...indecisiveness that’s creating these problems."
    s "{i}Tell her that.{/i}"
    o "Yeah, because the whole, “It’s me, not you” thing always goes over so well in movies."
    s "This isn’t a movie, Otoha."
    o "Good, because this movie would fucking suck."

    scene black
    with dissolve2

    "Otoha doesn’t say anything that I didn’t already expect to hear when I approached her today."
    "And while there was minimal refilling of cracks or fixing of anything, I did manage to learn that at least she doesn’t dislike me as much as she lets on."
    "But of course that’s what I’d jump to since it’s the only detail pertaining to me I was able to siphon out of the entire conversation."
    "I’m not involved in this. It’s not my {i}place{/i} to be involved in this."
    "I’m simply observing what could be either the earliest stages of a potential fallout...or the first of many hurdles in a long and successful relationship."
    "Unfortunately, this world doesn’t have enough long and successful relationships."
    "In fact, I can’t put my finger on a single one- but that’s mostly due to the fact that my fingers belong closer to short term options than ones that will grow old beside me."
    "In that sense, I wish Otoha the best in her pursuit of eternal youth or eternal freedom or whatever it is that she wants to last forever."
    "My wishes fall on deaf ears, but that’s okay-"
    "Because those things might be closer than she’s willing to believe."
    "Those wishes might come true."

    scene otohaparkten19
    with dissolve2

    o "Okay, well...I need to start heading out. But thanks for dropping by and letting me vent."
    o "Didn’t really sound fun at first, but I guess it did kind of help."
    o "I’m gonna text Rin and see if she’s able to talk about this tonight. I probably should be filling her in on some of the stuff I said to you if I really do want this relationship to work out."
    s "I’m glad I was able to help in...whatever way I was able to help."

    scene otohaparkten20
    with dissolve

    o "Cool. So, uhh..."
    o "See you later, then."
    s "..."
    o "..."
    o "You’re not going to ask me for like...a goodbye hug or something, are you?"

    if bonus == True:
        s "I am not."
    else:
        s "I wouldn't {i}refuse{/i} one. But that's not why I'm not leaving."

    o "..."
    o "Then...why are you not leaving?"
    s "Because I’m going to come with you to your lesson."
    o "No. You’re not."
    s "Why not?"
    o "Because I don’t want you to be there."
    s "{i}You{/i} might not want me to be there, but I’m not so sure your vocal coach feels the same way."

    scene otohaparkten21
    with dissolve

    o "Why do you even want to come? It’s going to be totally boring and that basement is cold as shit."
    s "I don’t have anything else to do today. And also, Niki confessed to still being in love with me and I thought it might be nice to drop by unannounced and make her blush."
    s "Besides, it’ll also give you an opportunity to see how a real couple deals with their issues."

    scene otohaparkten22
    with dissolve

    o "Wait, are you two actually back together?"
    s "No. But we act like we are sometimes, and I think that should be good enough."

    scene otohaparkten23
    with dissolve

    o "Ugh...whatever. I know there’s no stopping you once you decide to actually do something, and I’m already running late."
    o "I’m warning you now, though- it really is going to be boring. And if you do anything to mess up the lesson, I’m never talking to you again."
    o "I need this, dude. It’s an amazing opportunity. Please don’t mess it up for me."
    s "Otoha, why would I ever mess {i}anything{/i} up for you?"
    o "That emphasis on {i}anything{/i} is really starting to make me worry, Sensei."

    scene black
    with dissolve2

    s "Don’t worry at all, Otoha."
    s "If there is anything I am good at, it is spending time with Niki without causing her to get flustered or angry at anyone."
    o "I swear to God..."

    $ renpy.end_replay()
    $ otohapark10 = True
    $ otoha_love += 1
    stop music fadeout 10.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump otohaspecial10
...
```