# Pry With a Smile
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween13&go=Go)


Part of event chain [The Depressing Implication of Goosebumps](./halloween12.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloween13
* Group: Main
* Triggered by label: halloween12

## Event code
File: \game\script.rpy
Code:
```python
...
label halloween13:
    if _in_replay:
        play music "soda.mp3"

    scene halloweenloud1
    with dissolve

    ay "Oh, Miku. What’s up?"
    ay "How come you look so down all of a sudden?"
    sa "Is...everything okay?"
    ay "If you’re down because you can’t find Makoto, you could always hang out with us."
    ay "I think I saw her go somewhere with Sensei, so she’ll probably be back soon."
    mi "Huh? Oh, uhh, no! I’m not lonely or anythin’ like that."
    mi "I was just thinkin’ that it’s...kinda loud in here. "
    ay "Well, yeah. It’s a party."
    ay "Do you need me to turn down the music or something?"

    scene halloweenloud2
    with dissolve

    mi "U-Umm...well I wouldn’t wanna be the one to kinda ruin everythin’ for everyone else..."
    mi "I’m sure a party would be kinda borin’ without all the music and stuff but..."
    mi "If you don’t mind turning it down just a little bit, that would be...cool."
    mi "I’m not really great with loud noises."
    ay "Then yeah, definitely. I’ll turn it down right now."
    ay "You should have told me earlier if it was bothering you, Miku."
    ay "Don’t try to just keep all that stuff to yourself."

    scene halloweenloud3
    with dissolve

    mi "Sorry. I tried dealin’ with it and pretendin’ it’s not there and stuff but bein’ by myself probably...pushed me over the edge."
    mi "I’m sorry. I can just go wait outside instead. "
    sa "N-No...You don’t have to do that..."
    sa "I know where the speakers are so...I’ll go do it..."
    mi "Thanks, dolphin-Sana..."
    sa "Anytime...bat...demon...devil...Miku?"

    scene halloweenloud4
    with dissolve

    mi "Hahah...yeah...I’m not really sure what I’m supposed to be either."
    sa "R-Right..."
    sa "Well, I’ll...umm...be right back..."

    scene halloweenloud5
    with dissolve

    ay "Miku..."
    mi "Y-Yeah? What’s up?"
    mi "Why are ya soundin’ all sad-like and stuff? I already told ya I can wait outside if ya really like music that much."
    ay "Do you want to talk about anything, maybe?"

    scene halloweenloud6
    with dissolve

    mi "You’re not gonna...{i}make{/i} me talk about anything, are ya?"
    mi "I know you can do karate but I’m kind of an athlete so I can probably get away if I run really quick."
    ay "Of course not."
    ay "I just know that some people like talking about their issues instead of keeping them to themselves."
    ay "Is this sound thing a medical issue or is there something that would make you feel better if you got off your chest?"
    mi "N-No offense Ayane but I don’t really know you that well..."
    mi "I don’t really think I feel good about telling ya important backstory stuff when I don’t even know 'yer birthday."

    scene halloweenloud7
    with dissolve

    ay "September 25th. Know me well enough now?"
    ay "Are we officially friends?"
    mi "Wait a sec! Wasn’t that right around the time we went to the beach?"
    mi "What kinda friend am I for lettin’ ‘yer first birthday just pass by without gettin’ ya anything?!"
    ay "Well it wasn’t my {i}first{/i} birthday, it was my-"
    ay "Actually, it doesn’t matter how many birthdays I’ve had. "
    ay "What I’m trying to say is I’m here if you want to talk and I won’t be offended if you {i}don't{/i} want to."
    ay "Believe it or not, I’m not much of a talker when it comes to all that inside-stuff as well, so I might know where you’re coming from."

    scene halloweenloud8
    with dissolve

    mi "Umm, sorry again, but I’m pretty sure ya don’t."
    mi "Only Makoto really knows anyway and I’ve known her for like a trillion years or something, so..."
    ay "Well then I’ll ask again a trillion years from now and see if you feel any better."
    mi "Haha...yeah...thanks..."

    scene halloweenloud9
    with dissolve

    ay "Oh! There we go. Looks like Sana turned it down quite a bit."
    ay "If anyone complains, I’ll just tell them the speakers broke or something."
    ay "Is this volume okay, Miku? Anything else I can do for you?"
    ay "Maybe a nice long hug or a slice of wedding cake?"
    mi "This is fine...I should be okay now."
    mi "Sorry again for bein’ such a pest."
    mi "It’s no fun gettin’ in the way of everybody else, so feel free to karate chop me and knock me unconscious or somethin’ if that’s the sorta repayment ‘yer after."

    scene halloweenloud10
    with dissolve

    ay "Hmm...maybe a karate chop {i}would{/i} make me feel a little better after you {i}ruined my party{/i}."
    mi "Ah! I knew you were only fakin’ kindness because ya wanted somethin’ outta me!"
    mi "I bet ‘yer birthday ain’t even in September!"
    ay "That’s correct. I’m actually a robot my father created with all of his money in order to cope with the loss of his dead daughter."
    mi "Ah- holy shit. Why’d he choose blonde of all colors?"

    scene halloweenloud11
    with dissolve

    ay "Hey, wait a second. What is that supposed to mean?"
    ay "Blonde is a beautiful hair color. And sure it’s more western than something you’ll find in Japan, but that doesn’t mean it’s bad."
    ay "I like my hair a lot, actually."
    mi "Huh? Oh, yeah. It’s nice I guess."

    scene halloweenloud12
    with dissolve

    sa "Okay, I turned down the..."
    sa "..."
    sa "Why do you two seem more distant all of a sudden?"
    ay "Miku thinks blondes are ugly and wants me to leave her alone forever."
    mi "I didn’t mean for it to come out that way...I said it was nice, didn’t I?"
    mi "And thanks for turning down the volume, dolphin-Sana. Remind me to pay ya back once I’m dressed in normal clothes and don’t have my belly exposed."
    sa "What kind of favor do you...need to have your stomach covered up for?"
    mi "Most of ‘em, I figure. Unless you planned on askin’ me for somethin’ weird."
    sa "I...didn’t plan on asking you for {i}anything.{/i}"

    scene halloweenloud13
    with dissolve

    ay "Okay, well how about this-"
    ay "In order to repay us for accommodating your mysterious distaste for loud music-"
    ay "I, Ayane Amamiya of House Amamiya, sentence you to ten more minutes of girl-talk with my dolphin sidekick and I."
    sa "I’m a...sidekick now?"
    mi "What kinda knight needs a dolphin as a sidekick?"
    sa "I...would also like to know the answer to that question."
    ay "The kind who just sentenced you to ten more minutes of girl-talk and is still not currently engaging in any."

    scene black
    with dissolve

    "The three girls make their way over to a bench in the back of the room-"
    "Two of them unaware of exactly what’s being concealed from them."
    "And for good reason."
    "It’s not easy to openly admit your weaknesses to anyone, let alone those you only see in short bursts several times a week."
    "Of course, that never stops others from prying."
    "But prying can be dangerous."
    "In fact, prying is one of the most dangerous things you can do here in this world filled with {s}tragedy{/s} happiness."
    "But as long as you pry with a smile, no one is allowed to hate you."
    "After all, that just means you’re a good person."
    "So continue to invade everyone’s personal space while telling yourself that you’re only trying to help."
    "It really works!"

    scene halloweenloud14
    with dissolve

    mi "Umm...why are ya touchin’ my leg? "
    mi "And why is your sidekick huggin’ us with her dolphin hands?"
    ay "You really don’t want to talk, right?"
    ay "Because now is probably the last chance you’ll get without it being awkward or random."
    ay "And having a funny looking dolphin nearby might make it easier."
    sa "It’s true..."
    sa "Also, I’m only hugging you two so I can keep my balance and...not fall over..."
    sa "The costume is pretty heavy and it’s kind of...hot in here..."

    scene halloweenloud15
    with dissolve

    mi "Kinda just want to take my mind off of it if that’s okay. "
    mi "Sounds weird but even talkin’ about talkin’ about it makes me not wanna...talk about it even more."
    ay "You’re right, that does sound weird."
    sa "I think I get it, though..."

    scene halloweenloud16
    with dissolve

    sa "Ayane never tells me what’s wrong either, but she always wants to help other people..."
    sa "So I’m used to...dealing with this sort of thing..."
    ay "I think I’m starting to realize why you always get mad at me for that."
    ay "I feel so useless right now."
    ay "I've even resorted to physical comfort. This might be the first girl-leg I've ever grabbed. "
    ay "It’s soft but also kind of muscley."
    mi "I’m surprised you can feel anythin’ through those gloves."
    ay "This armor has become a part of me. It’s like it’s a second set of skin now."

    scene halloweenloud17
    with dissolve

    mi "Well, uhh...I’m glad you two are at least lookin’ out for me! "
    mi "Sorry to be so annoying and not just spill out why I’m actin’ all weird in the middle of what’s supposed to be a fun night for all of us."
    mi "Not gonna lie, I’d be pretty bummed out if somebody showed up at one of my soccer games and was like, “Hey, can ya kick the ball a little softer please?” and then wouldn’t tell me why."
    ay "I think this situation is a little different, but I want to remind you that I really don't care about the music."
    ay "In fact, there’s only one song that really matters to me anyway and I’ve been told I’m not allowed to play it tonight."
    mi "What song is that?"

    scene halloweenloud18
    with dissolve

    ay "Oh, just a little song by the name of DESPACITO."
    sa "Ayane, no."
    sa "Not...now..."
    mi "Isn’t that the one that’s all like, Spanishy and stuff?"
    ay "It’s written in the language of love."
    sa "Isn’t the language of love supposed to be...French?"

    scene halloweenloud19
    with dissolve

    mi "Well I don’t know much about the French Despacitos or whatever they’re called, but I’ll check ‘em out sometime."
    ay "That answer is good enough for me."
    mi "Does...that mean you’re going to let go of my leg now? I feel like that’s a good stoppin’-point for this."
    mi "You’re kinda all up in my personal space and stuff."
    ay "Aren’t you holding my hand, though? That’s basically consent to keep going."

    if bonus == True:
        mi "I’m just tryin’ to make sure it doesn’t start wanderin’ all-over my prepubescent body and goin’ someplace I don’t want it to go."
        ay "You’re definitely not prepubescent anymore, Miku. "
        ay "If you haven’t started growing by now, I’m afraid you never might."

        scene halloweenloud20
        with dissolve

        mi "I-I’m still going to grow! It just hasn’t happened yet!"
        mi "There’s no way in heck I’m gonna stay like this forever!"
        mi "Any day now, I’ll show up to[school] with size X melons and you’ll all see why you shouldn’t have messed with me!"
        sa "I’ve already...accepted my fate, Miku..."
        sa "It might be time for you to face the music as well..."
        sa "Just...at a lower volume...I suppose..."
        mi "Jeez! Why’s everybody gotta be gettin’ all up in my face about all these hormoney things lately?!"
        mi "I’m just tryin’ to be normal ole Miku but everyone keeps remindin’ me that this is the springtime of my youth!"
        ay "Hm? Has someone else had the pleasure of touching you other than me today, Miku?"

        scene halloweenloud21
        with dissolve

        mi "Well yeah but ya can’t blame him for gettin’ like that when it was {i}my{/i} fault to begin with."
        ay "Him?"
        sa "Uhhhhhhhhhhhhhhhhhhhh..."
        ay "Who are you talking about?"
    else:
        mi "No, I'm just tryin' to do this thing where I take control of my brain and force it to believe I'm holding hands with {i}him{/i} instead of you. Which makes it kinda okay."
        ay "Him?"
        sa "Uhhhhhhhhhhhhhhhhhhhh..."
        ay "Who are you talking about?"

    scene halloweenloud23
    with dissolve

    mi "Oh, did I say {i}him{/i}? I meant...her! Hahahahah!"
    mi "Ya see...me and Makoto are...a lot closer than you guys think!"
    mi "And by me and Makoto I just mean...Makoto!"
    mi "She sneaks into my bed sometimes and before I know it she’s all...ready to go!"
    mi "And I keep tryin’ to tell her, Makoto! I don’t even like girls!"

    if bonus == True:
        mi "But the thing is I look kinda like a little boy and I guess she just happens to be into that sorta thing. Hahahaha!"

    ay "…"
    sa "…"

    scene halloweenloud24
    with dissolve

    ay "None of that is true at all, is it?"
    mi "I felt something today that I don’t think I will forget for as long as I live."
    ay "I see."
    sa "…"
    mi "…"
    ay "Did you like it at least?"
    mi "I-"

    scene halloweenloud25
    with hpunch
    stop music fadeout 5.0

    mo "LADIES AND GENTLEMEN! BOYS AND GIRLS!"
    mo "DEATH IS ON THE HIGHWAY AND ISN’T PAYING ANY TOLLS!"
    mi "What’s Molly got in her hand? Looks like a can of-"
    sa "Beer..."
    sa "We sell that kind at the bar."
    ay "Is the Irish girl really drunk right now? Isn’t that a little too...cliche?"

    $ renpy.end_replay()
    $ halloween13 = True

label halloween14:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```