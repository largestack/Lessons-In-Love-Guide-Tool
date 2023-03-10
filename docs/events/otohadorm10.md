# Breathing in Unison (Otoha)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Two-Octave Pitch Glide](./otohaspecial10.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: otohadorm10
* Group: Otoha
* Triggered by label: otohaspecial10
* Chain sources: otohaspecial10
* Chain sources path: otohaspecial10

## Official wiki page

[Breathing in Unison](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohadorm10&go=Go) for more details.

## Event code

File: (install folder)\game\OtohaEvents.rpy

Code:
```python
...
label otohadorm10:
    scene noonsky
    with dissolve2
    play music "icantseeher.mp3"

    o "What? Seriously?"
    o "Well, what are we supposed to do in the meantime then?"
    o "..."

    "Otoha and I are making our way to the cafe following her lesson, but I’m sure that’s about to change based on the apparent urgency of this phone call."

    o "But what if he like, kidnaps me or something?"
    s "Otoha, this way. I know a shortcut through a dark alley."
    o "Oh my God, it’s literally about to happen. Help."
    o "..."
    o "Yeah, I know. It’s fine. We’ll just kill some time or whatever until you’re off."
    o "..."
    o "Okay. Talk to you later."

    play sound "phonebeep.wav"

    s "I’m going to go out on a limb here and assume that was Rin."
    o "Yup. The cafe’s gotten way too busy for her to be able to chill with us, so she told us to “Save ourselves” and not bother coming."
    s "Looks like you and I will have to use this opportunity to bond, then."
    o "Guess so. But can we maybe cut back on the Rin stuff this time and talk about something more...fun?"
    s "I’m telling Rin you don’t think she’s fun."
    o "That’s obviously not what I mean. There’s just only so much drama I can handle before it becomes a burden."
    o "So if I have a chance to break away from that...I’m probably going to take it."

    scene black
    with dissolve2

    "We’ve reached the time of day where the sun begins to migrate to the opposite side of the globe."
    "We follow its light, for it always sets behind the dorms."
    "And, before we know it, we’re there."
    "We move away from the orange glow into a lobby brought to life by the welcome sensation of air conditioning, something that hasn’t been present here in quite some time."
    "The lack of windows makes it hard for air to properly circulate in here, so the difference in climate is noticed by both of us immediately."
    "We inhale deeply in unison, filling our lungs with the start of something we hope is wonderful."
    "Our eyes meet for a moment. "
    "Otoha smirks."
    "We go upstairs."

    scene otohaworkshard1
    with dissolve2

    o "Okay, so...remember earlier when I said that Nodoka was going through another manic phase?"
    s "Yes."

    play sound "glass.mp3"

    no "FUCK! NO! EVERYTHING IS WRONG!"
    s "She sounds pretty normal to me."
    o "Uh-huh. I guess destroying everything on her side of the room isn’t exactly {i}off brand{/i} for her, but we should still kinda tread lightly, you know?"
    o "Don’t ignore her existence because then she’ll think she’s like, turned invisible or something. But don’t spend too much time staring at her either."
    s "Otoha, if you want me to pay more attention to you, all you have to do is ask."

    scene otohaworkshard2
    with dissolve

    o "Noted. Opening the door now. Brace for impact."

    scene black
    with dissolve2

    no "Nononononono, bad! Bad marker! You stay alive while I’m spreading your guts out all over the board! That is an order!"
    o "Nodoka, I’m back. And I brought Sensei for some reason."

    scene otohaworkshard3
    with dissolve

    no "Why the fuck are you here?! Can’t you see I’m working?! Can’t you see?!"
    s "Where are your pants?"
    no "Pants??? Those things??? They inhibit the movement of my legs. Of course I’m not wearing pants. Why would anyone wear pants???"
    no "Get the fuck out of my room if you’re just going to talk about pants. Or help me. Yes, help me. I could use the help. Just don’t mention pants again. "

    scene otohaworkshard4
    with dissolve

    o "What do you need help with, Nodoka?"
    no "Something grey. And edible. I need you to find this. Find an item like that for me. Bring it to me. I need to look at it. It’s extremely FUCKING important."
    s "Nodoka, what are you writing on your board right now?"
    no "Secrets. Secrets, secrets, secrets. For me to know and you to find out. "
    no "The only problem is I DON’T FUCKING KNOW THEM EITHER. Get me something grey. Go. Shoo. Fetch. "
    o "I can’t think of anything grey and edible off the top off my head, so I’m going to take Sensei over to my side of the room and-"
    no "No. Bad. Bring him here. I need to see something. I need to stare at something. I need to stare into something so I can see it. And I can’t see him from all the way over here."
    no "Quickly. The marker is dying. It is the last one. The last one before a new one. You don’t want the new one. The new one is bad."

    scene otohaworkshard5
    with dissolve

    o "Uhh...have fun? I’ll be at my desk."

    scene black
    with dissolve2

    "I stare through Nodoka, trying to piece together the words haphazardly scribbled all over her dry erase board, but nothing comes to mind."
    "Carefully, I step over all of the things she’s pushed off of her desk and make my way over to her. "
    "The carpet is damp from spilled cups of old coffee and makes an interesting squishing noise the closer I get to the desk."

    scene otohaworkshard6
    with dissolve2

    "It was hard to notice from halfway across the room, but both her head and hands are shaking rather violently and her skin is an even paler shade of white than normal."
    "She locks eyes with me, pupils transitioning to colorlessness, and doesn’t say a word for roughly twenty seconds."
    "In the background, I can hear Otoha logging into her computer, followed by the sound of keys on a keyboard being pressed down."
    "Everything becomes apparent all at once."
    "Everything except why I’m here in front of Nodoka."

    no "They’re the same as hers."
    s "I’m sorry?"
    no "Deep. Black. Everything and nothing, shaped into a tiny little circle you can fit in your mouth."
    no "Yes. Yes. But...no. Wait. What? I thought I understood, but I don’t understand anything. Come closer."
    s "But I don’t-"

    play sound "static.mp3"
    scene otohaworkshard7
    with flash
    stop sound

    no "A girl with blue eyes. She came to me in a dream."
    no "She opened up her palm and showed me what she was holding. It was a little toy car."
    no "Her mouth opened thereafter and she swallowed it like it was a pill. She washed it down with a glass of orange juice."
    no "I can picture it driving around in the caves of her intestines- stopping at stomach ulcers to refill its gas tank before continuing on with its journey."
    no "What else resembles intestines, Sensei? List all of the long, tubular objects you know."

    "I list some things."

    no "Do you think I am something to love?"
    no "Do you think I am anything like her?"

    "I think."

    play sound "static.mp3"
    scene otohaworkshard8 with flash
    stop sound
    play sound "seek.mp3"

    "The world turns into a negative thing and my hands begin to feel kind of like the tongue of a clam but with more glass and less sand."
    play sound "seek.mp3"
    "I approach the girl who isn’t the other girl and get ready to raise my affection points with her."
    play sound "seek.mp3"
    "I wonder how many living things there are inside of us right now."

    play sound "static.mp3"
    scene otohaworkshard9
    with flash
    stop sound

    o "What did Nodoka want? Couldn’t really hear whatever was going on over there on account of all the whispering."
    s "To be honest, I’m not really sure."
    o "Yeah. I guess I can’t fault you for not understanding her when she’s...in that state."
    o "Seems quieter now, though. So whatever you two talked about must have helped in some way."
    s "Now, I just have to figure out how to help {i}you.{/i}"

    scene otohaworkshard10
    with dissolve

    o "Me? What do I need help with?"
    s "Well, judging by the mass amount of notebooks spread out all over your desk, I assume you’re having your own little bout of mania. Albeit one significantly less interesting than Nodoka’s."

    scene otohaworkshard11
    with dissolve

    o "Oh...hahah. Yeah. That."
    o "Uhh...I’m not really sure if I’d call it {i}mania{/i}...but I’ve been getting my ass kicked by some song I’ve been trying to write lately."
    s "What are you writing about?"
    o "Do you think I’d have this many notebooks out if I had any idea what the answer to that question was?"
    s "I have no idea. I’m not really familiar with your...creative process."

    scene otohaworkshard12
    with dissolve

    o "Okay. So, like...every notebook serves its own purpose. I keep them organized by a combination of genre, lyrical style, and the mood or tone of whatever the song I’m writing is."
    o "But, sometimes, when I can’t figure out what I’m trying to say, I have to hop between notebooks."
    s "You know you could just invest in those divider things, right? That way, you wouldn’t have to use a different notebook for literally everything you do."

    scene otohaworkshard13
    with dissolve

    o "Uh-huh. But then I’d also have to keep track of all of the dividers on top of all of the notebooks and that just sounds like too much of a hassle."
    s "I mean, the whole point of getting dividers would be to get rid of the notebooks."
    o "I hear you, and I’m glad you’re trying to help out, but there’s kind of a way I need to do things and I don’t really intend to change that any time soon."
    s "I just think that-"

    play sound "thump.mp3"
    scene otohaworkshard14
    with hpunch

    o "Back the fuck off! I’m not going to-"

    scene otohaworkshard15
    with dissolve

    o "Mm!"
    s "Woah."
    o "I’m so sorry. I didn’t mean to yell."

    scene otohaworkshard16
    with dissolve

    o "I’ve just been under a lot of stress lately...trying to balance everything out and whatnot."
    o "That’s why I’m hoping I can at least get this song right since everything else has been turning to shit. It’s nothing against you."
    s "That’s fine. Everyone gets overwhelmed from time to time."
    s "Don’t you think it might be best to focus on something a little more serious if you’re just trying to make {i}one{/i} thing right, though?"

    scene otohaworkshard17
    with dissolve

    o "Oh, come on. I thought we weren’t going to talk about her?"
    s "If your organizational skills were a little better, we probably weren’t."
    o "Dude, come on. I’m trying to write a song {i}for{/i} Rin. That’s why my shit is everywhere. I can’t risk fucking this up too."
    o "Am I going a little overboard? Sure. But it’ll pay out in the long run."
    o "I’ve got no problem killing myself like this so long as I’m able to get my point across."
    s "And what is your point, exactly?"
    o "No clue. See: desk."
    o "If I can just come up with like, a clear message or a clear point I want to get across...I can avoid having to blindly throw darts at a dart board like this."
    s "I’m starting to understand why you’re so unfazed by Nodoka’s apparent psychotic breaks."

    scene otohaworkshard18
    with dissolve

    o "Oh, please. Me overworking myself is {i}way{/i} different from whatever the hell is going on in Nodoka’s super-brain."
    o "I’ve got this under control, man. It’ll all be worth it in the long run."
    s "Famous last words, Otoha."
    o "What? What are you talking about?"
    s "Just that you should know more about the dangers of what you’re doing. Plenty of people have thought the same way only to end up in boxes."

    scene otohaworkshard19
    with dissolve

    o "You’re worrying about the wrong person, Sensei. I’ve got way too much shit to do. I don’t have time to die."
    s "Well, I hope that’s true. Because I kind of like you."

    scene otohaworkshard20
    with dissolve

    o "Huh?..."
    s "And I mean that in the least creepy way possible."
    o "Yeah. That didn’t sound creepy at all that time. That’s why I probably look so shocked."
    o "Like, it sounded like you actually being a decent person for once."
    o "I’m not really sure what to say."
    s "You can say you like me too. Nodoka is too out of it to remember, so it will be like no one ever heard anything."

    scene otohaworkshard21
    with dissolve

    o "I don’t...{i}not{/i} like you."
    s "I’ll take the double negative. I know what it really means."

    scene otohaworkshard22
    with dissolve

    o "You know...I know we’ve joked about it before. But today, you really {i}have{/i} felt kind of like an older brother or something to me."
    o "Annoying, yeah. And way too close to my personal space. But mostly full of advice and actually like, genuinely looking out for me. Kind of."
    o "I’m sure there are some horrible intentions mixed in that are the cause of that, but I’m going to ignore them for the time being since it’s actually been pretty nice so far."
    o "I always wanted someone like that. Someone to kind of...counterbalance how suffocated I always felt by my parents. Someone who would, at the very least, understand that..."
    o "And I’m not saying you do just yet.. But you’re closer to it than most people. That’s nice."

    if bonus == True:
        "I’m glad she’s able to look past my “horrible intentions,” because the way Otoha is blushing right now is certainly reinforcing them."
        "It’s no time to dwell on the sexual fantasies of a surrogate little sister, though. Not when it’s becoming clear that whatever hinges keep Otoha functional are slowly coming unscrewed."
        "It’s possible you might be thinking that {i}I’m{/i} thinking too deeply into this, but I’d like you to consider the countless other cases in which creative minds rotted from the inside out in pursuit of...anything."
        "There’s that old saying “A mind is a terrible thing to waste.”"
        "But, if that’s the case- why do we waste so many?"
        "And why is the beauty created by those minds only truly appreciated once they’re lowered into the soil?"
        "Some things can be beautiful above ground."
        "Before me is one of them."

    s "Just take it easy. Don’t get lost in whatever you’re doing and I’m sure everything will turn out...okay-ish."

    scene otohaworkshard23
    with dissolve

    o "Okay-ish is all I ask. So thanks."
    s "Also, if you ever want to call me “Big bro” or “Onii-chan” I am more than okay with it."
    o "I’ll think about it."
    s "That’s honestly more than I thought I would get. So thank {i}you{/i}, Otoha."

    scene otohaworkshard24
    with dissolve

    o "No problem, man. Just don’t go snooping around in my closet and always knock before coming into the room. We’ve gotta set some ground rules if we really want this to work out."
    s "I think this is the part where I tell some joke about having to check your closet to make sure you’re growing properly."
    o "Rad. Cause that means it’s also the time for me to punch you in the face and send you flying into orbit."
    s "At least I’ll die happy."

    scene black
    with dissolve2

    "Otoha and I spend the next hour or so hanging out in her room, swapping back and forth between casual conversation and observing her roommate’s manic episode."
    "And while I’d like to say that I’m glad she used this opportunity to take her mind off of working, I caught her jotting several things into several notebooks while we waited for night to come."
    "I guess some people just can’t stop even when you make it incredibly apparent that they should."
    "More power to her, I guess."
    "If Otoha thinks she’s able to just avoid being overwhelmed for the rest of eternity, she has every right to try and prove that."
    "But-"
    "That also gives us (Or just me, I guess) the right to tell her “I told you so” when she can’t do it anymore."
    "That day will most assuredly come. And, when it does, I’ll be somewhere beside her."
    "Close, but not too close."
    "Probably going through her closet."

    play sound "phonebeep.wav"

    o "Oh. Niki’s choreography thing just ended. She wants to know if we’re ready to head over to the restaurant yet."
    s "Is that what we’re doing? I remember agreeing to the double date thing, but I didn’t know we already chose a place."
    o "I guess so. It’s close-ish to the cafe, too, so Rin can probably come straight over after getting out of work in an hour."
    s "Are you going to be able to stay away from your ten thousand notebooks for the rest of the night?"
    o "Yeah. I’ve got a pocket-sized one that I keep on me at all times in case inspiration strikes while my babies are away."
    s "You have a problem, Otoha."
    o "Don’t we all, man? Don’t we all..."

    $ renpy.end_replay()
    $ otohadorm10 = True
    $ otoha_love += 2
    stop music fadeout 25.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump otohadorm10p2

label otohadorm10p2:
...
```

## Code that triggers this event

File: (install folder)\game\OtohaEvents.rpy

Code:
```python
...
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
...
```