# Try. Try. Try. (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Pluto Was Never Really a Planet](./secondbeach15.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: secondbeach16
* Group: Main
* Triggered by label: secondbeach15
* Chain sources: secondbeach15
* Chain sources path: secondbeach15

## Official wiki page

[Try. Try. Try.](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach16&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label secondbeach16:
    play music "beginningoftheend.mp3"

    "My blister pops and I can sense it filling with stale water and sand particles in place of where my bodily fluids were just moments ago."
    "It stings, but it’s bearable. It just sounds a lot worse when you put it into words."

    if bonus == True:
        "Kind of like a teacher having sex with his students. It’s a lot worse on paper than-"
        "Actually, no. It’s still pretty bad either way."
        "But I’ve never claimed to be a good person."
        "And it’s not like I’m having sex with any of them {i}right now{/i}, so you can deal with me for another moment or two and pretend I’m better than I actually am."
        "It’s not like what I do to any of them is eternal either way."
        "Once I inevitably fade and someone else slips into this body, so will the memories I was able to inject into them."
        "That isn’t a figure of speech. I’m talking about what I actually inject into them with my penis."
        "And how all of it is just as fleeting as the blister I’ve been walking on."
        "Ephemeral, even."

    s "…"

    "What is happening to me?"

    play sound "static.mp3"
    scene tryagain2 with flash
    stop sound

    "An ocean appears before me, full of life and...fish."
    "But what’s more important is why I’m suddenly, just moments after having a successful conversation with Yumi, a rare feat even to this day-"
    "Why I’m suddenly thinking about the end."
    "About what will happen after I’m gone."
    "I am me."
    "I know I’m me. "
    "I’m smart enough to pick up on the hundreds, if not thousands of context clues left by Maya and the Nakayamas that {i}I am real.{/i}"
    "I just...don’t know who {i}I{/i} am."
    "Which, once again, probably sounds a lot more intense than it actually is."
    "I just want to know."
    "But I can’t."
    "Now, back to the interesting things in front of me."

    t "Supreme Overlord, Herald of the Adolescents?"

    play sound "static.mp3"
    scene tryagain3 with flash
    stop sound

    t "What are you doing out here? The majority of the class is having a bonfire."
    s "Hey, Tsuneyo. Who is your friend?"
    t "My only friend is the Emerald Guardian and she is not here right now."
    t "But she insisted that I go out and enjoy myself as she was not feeling up to associating tonight."
    s "And why aren’t {i}you{/i} with the other girls?"
    t "I got lost."
    t "But thankfully, I brought this flotation device."
    s "I don’t see how that is going to help you get back to the inn."

    scene tryagain4
    with dissolve

    tf "Hi."
    s "…"
    s "You really don’t see that thing, Tsuneyo?"
    t "What thing?"
    s "The black figure standing beside you with a pink baseball cap on."
    tf "It’s actually light purple."

    scene tryagain3
    with dissolve

    s "I don’t care what color it is. You’re weird. Go away."
    t "I think I understand what is going on here."
    s "You do?"
    t "You are what my father would call “under the influence.”"
    t "Have you been drinking the beers again?"
    s "Not to my knowledge."
    t "You’ve had so many that you can’t remember having any at all. This is why our family fell apart."
    s "I think I just might have...food poisoning or something."
    s "I’ve been seeing a lot of strange things tonight."
    t "Food poisoning does not cause hallucinations, but I’d be open to hearing you describe the things you’ve seen."
    t "I am not a medical professional, but I can pretend that I am interested and make you feel validated as a human being."
    s "Well, like I said, there’s a large, shadowy figure to your left wearing a pink-"
    tf "Light purple."
    s "...Light purple hat. And then a bunch of floating fish and a giant rabbit looking thing."
    t "I see."
    t "That was a joke. I do not see at all."
    t "Perhaps we just view the world a bit differently from one another."
    s "I’m sure we do, but just seeing the world differently isn’t enough to cause things to get this...out of whack."
    t "Is it truly “out of whack” if it is what you really see?"
    t "Just because someone tells you something isn’t there doesn’t mean it’s not."
    t "Some people are just better at using their eyes than others. For all we know, you are one of those people."
    t "Have you seen anything else?"
    s "I’m sure I have, but...the memories of those things are starting to go away."
    t "To where?"
    s "What?"
    t "Where do memories go once they leave your body?"
    s "I...don’t think they’re ever really stored {i}in{/i} your body. And they just kind of...disappear, I guess."
    t "So all the rest of our thoughts stored in...somewhere that is not our bodies-"
    t "Will they vanish when we’re dead and buried and turning into trees?"
    s "I don’t know."
    s "But what I do know is that I don’t really want to spend the rest of my night theorizing about death and what comes with it when there is a group of cute girls having a party without me."
    t "Will you take me with you? I am beginning to fear for my safety alone out here in the middle of the night."
    s "And you feel more comfortable with me?"

    scene tryagain5 with dissolve

    t "I am beginning to."
    tf "Awwwwwwwwww~"
    s "And...you really don’t see any mysterious...shadowy figure beside you?"
    t "I do not."
    t "Just as you don’t see the ones beside you."
    s "The what-"

    scene tryagain6
    play music "gentle.mp3"

    r "Hey! Sorry I’m late."
    r "I ran into a...bit of a situation when I went to get my phone. But it’s all good now!"
    o "Oh. Yeah, no worries. You’re only like...three minutes late anyway, so it’s not like it’s a big deal."
    o "Are you sure you wanted to do this instead of going to that bonfire thing, though?"
    o "I don’t really care either way. Just seemed like it might be a little...livelier over there or whatever."

    scene tryagain7
    with dissolve

    r "I, umm...kind of wanted to be alone with you...if that’s cool..."
    o "...Yeah. Yeah, that’s cool."
    o "Sorry, it just feels a little different tonight than it normally does when it’s just us."

    scene tryagain8
    with dissolve

    r "Like...good different? Or bad different? Or “I actually think Rin is a boy” different?"
    o "Uhh...what?"

    scene tryagain9
    with dissolve

    r "Gah! Shit! I’m already making things awkward!"
    o "I mean...you kind of make everything ever awkward, so it’s not like I’m not used to it or anything."
    o "Also, I am well aware that you are a girl."

    scene tryagain10
    with dissolve

    r "Ugh...thank God."
    r "Because earlier, I went through this whole situation thing in my head about what I would do if you {i}didn’t{/i} think that, and the only way I could think of resolving it would be borderline sexual harassment."
    r "Soooooo anyway yeah, just ignore me until I start saying normal things again."
    o "I’d probably have to leave altogether if that were the case..."

    scene tryagain11
    with dissolve

    r "Ah! No! That would make this even worse than last time!"
    o "...Last time?"

    scene tryagain12
    with dissolve

    r "Hah..."
    r "Okay...here we go..."
    o "Rin...hold on a sec..."
    r "Otoha Okakura..."
    r "I know this might come as a bit of a shock to you...but from the moment I first saw you playing your guitar in the park, I’ve had a major...and I mean like, {i}major{/i} crush on you..."

    scene tryagain13
    with dissolve

    o "That...does not surprise me at all."
    r "And I know that you aren’t really into the whole dating thing since you’ve turned down basically everyone in Kumon-mi..."
    r "And...honestly, I can’t think of any reason why you wouldn’t turn me down too."
    r "I’m cute, yeah. But I’m sure there are plenty of other cute people that have confessed to you with...more talent or...or penises."
    o "Okay, getting weird now."
    r "Like, for all I know, you could definitely like penises more than vaginas. And that would be totally okay. In fact, I think they’re kinda cool too."
    r "A little weird, sure. But still kinda cool."
    o "Uhhhh..."
    r "But umm...even if you’re on the penis team instead of my team, I’d still...hate myself if I didn’t go through with this..."

    scene tryagain14
    with dissolve

    o "Rin, hold on. I know what you’re about to do and...there's something-"
    r "The truth is...there isn’t anything that would make me happier right now than...being able to walk down the halls of[school]...holding hands with you and stuff..."
    r "And maybe kissing under the bleachers occasionally, but we wouldn’t have to do that right away."

    scene tryagain15
    with dissolve

    o "Oh my God."
    r "I mean...if you {i}wanted{/i} to do it right away, that would be totally fine too. But...like I said, slow and steady wins the race."
    r "Wait, no. I didn’t actually say that. It was in my notes on my phone, but since I forgot where I put it earlier, I-"
    r "Actually, forget about the phone. That doesn’t matter right now."
    o "Rin...come on..."

    scene tryagain16
    with dissolve

    r "What..."
    r "What {i}does{/i} matter is...trying to do something I thought I’d be able to hold off on for a little while longer..."
    r "Because some days, it feels like I’m going to literally explode if I don’t tell you how I feel."
    o "…"
    r "I don’t know if I can make you happy...Shit, I don’t even really understand what {i}would{/i} make you happy."
    r "There’s so much I still don’t know about you."
    r "But...the things that I do know..."
    r "They’re enough to make me want you..."

    scene tryagain17
    with dissolve

    r "More than...anything I’ve ever wanted before..."
    o "…"

    r "So...if you’d...ever have any interest in...you know...being my girlfriend..."

    scene tryagain18
    with dissolve

    o "{i}Hah...{/i}"
    r "If...you’d ever have any interest in that...it would make me...happier than anything in the whole wide world."
    o "Sure."

    scene tryagain19
    with dissolve
    stop music fadeout 5.0

    r "I know it...probably sounds stupid since we’ve only known each other for a few months..."
    r "And I know that you probably need more time to-"
    r "Wait-"

    scene tryagain20
    with dissolve

    r "What..."
    r "What did you just say?..."

    scene tryagain21
    with dissolve
    play music "kimitoakinobouken.mp3"

    o "I said sure."
    o "You really have to get better at listening, dude. I was trying to talk to you that whole time."
    r "You..."
    r "Wait, hold on. Just to make sure we’re on the same page right now, you...you know I was asking you out, right?"
    o "Uhhhh, yup. You made that pretty clear."
    r "And by “Sure,” you mean, “Yes, Rin. I will be your girlfriend?”"
    o "That is what context would imply, yes."

    scene tryagain22
    with dissolve

    r "But...that would mean you like me!"
    o "Yup."
    r "Which would mean that we like each other!"
    o "Yuuuuup."
    r "But...no one’s ever liked me at the same time that I’ve liked them before."

    scene tryagain23
    with dissolve

    o "To be honest...I’ve still got a lot of learning to do in that department..."
    o "Like you said, I’ve turned down...tons of people before and never even really...felt bad about any of it."
    o "And I didn’t even really get how I felt about {i}you{/i} until a little while ago."
    o "But what I felt wasn’t really...the same sort of thing you feel for me..."
    r "I don’t like where this is going."
    o "Yeah, because you suck at listening. Let me finish."

    scene tryagain24
    with dissolve

    o "Rin...you..."
    o "You do a lot of shit that I’m not really comfortable with."
    r "Like...what?"
    r "Is this about...my dep-"
    o "It’s not about your stupid depression. We can work through that."
    o "It’s about how...quickly you started going after me."
    o "And how hard you fell despite me doing literally nothing."
    o "That shit is noticeable."
    o "And...the fact that it happened like...{i}right{/i} after you were rejected..."
    o "I just...I don’t know."
    o "I guess I never really understood why exactly all of that happened."
    o "And I wanted to sort of...clear that up {i}before{/i} something like...this."
    o "But...you're like a fuckin' freight train sometimes with how hard your feelings come on."
    o "It's really...intimidating. And unusual."
    o "And I wanted to be sure that...well, {i}you're{/i} sure."

    scene tryagain25
    with dissolve

    r "Wait! Do you..."
    r "Do you think I still like Chika?!"
    r "Is that why you got all dodgy when we went to the mall?!"
    o "Yeah?...I don’t know?"
    o "Maybe?"
    o "It was just...weird seeing you get so emotional about a thing I was finally starting to think you were over."

    scene tryagain26
    with dissolve

    r "Otoha..."
    o "I mean I guess I could be just misunderstanding you, but...I just don’t really understand how things got like {i}this{/i} so quickly."
    o "And...I was kind of really worried how this would all play out because, now that I’m finally starting to accept how {i}I{/i} feel...I’m..."

    scene tryagain27
    with dissolve

    o "I’m kind of scared, you know?..."
    o "Like...I don’t want my first experience in dating to be as some...rebound girl or something."
    o "I wanted to be like...totally sure it was more than that..."

    scene tryagain28
    with dissolve

    r "Of course it's more than that..."
    r "It’s true that I liked Chika for a really long time..."
    r "But I think I always knew in my heart there was no way that was ever going to happen."
    r "It was just...a childish crush."
    o "But...what if that’s what this is too? We don’t know. We’re like...still [young]or whatever..."

    scene tryagain29
    with dissolve

    r "Oh, come on! You don’t actually believe all that stuff old people say about being too [young]to understand love, do you?"
    o "I mean...I personally don’t understand {i}anything{/i} about love, so..."
    r "Then...let me take the lead! I have zero experience too, so...we can learn together!"
    r "Not just about love, but about each other! About all sorts of things!"
    o "Okay, but..."
    o "I need you to promise that it’ll be only me..."

    scene tryagain30
    with dissolve

    r "You are so cute that I am going to actually die."
    o "Fuck, man. How come writing love songs is so easy but saying this stuff out loud is like, insanely embarrassing?"

    scene tryagain31
    with fade

    o "Woah! Where did you come from?"
    r "Right next to you."
    o "We’re...really close all of a sudden."
    r "Cause I wanted to be really close to you."

    scene tryagain32
    with dissolve

    o "Well, I mean...since I guess we’re like...you know...dating now or whatever..."
    o "It’s okay."
    o "Just...take it slow, please. I don’t want to jump right into-"

    scene tryagain33
    with dissolve2

    r "Chu~"
    o "Mmf!"

    scene tryagain34
    with dissolve

    r "Sorry, were you saying something?"
    o "You..."
    o "Um."
    o "You are very...very bad at listening..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene tryagain35
    with dissolve2

    o "So..."
    o "This is...gonna be a thing we have to tell people about, isn’t it?"
    r "Yeah..."
    r "If I wake up in ten minutes and this was all some sort of crazy dream, I’m going to kill myself."
    o "Please don’t say things like that. As your girlfriend, I’m now obligated to care even more."
    o "I think that’s how these things work, at least. I could be wrong."

    scene tryagain36
    with dissolve

    o "But I’m...excited! This was-"

    scene tryagain37
    with dissolve

    o "Wait, why are you crying? Did I fuck up already?"
    r "No...Of course not..."

    scene tryagain38
    with dissolve

    r "I’m just...really happy..."
    o "…"
    r "…"

    scene tryagain39
    with dissolve

    o "Good."
    o "I hope you can stay that way."
    r "…"
    o "…"
    o "The moon is beautiful tonight."

    scene black
    with dissolve2

    "Sometimes, good things happen."
    "Not all the time...but if you try enough, something is bound to work eventually."
    "This was just one of those nights."
    "So revel in it while you can because, soon enough, the world will swell with misery once more."
    "Then twice more."
    "Then thrice."
    "Over and over and over again, the clock goes around in circles."
    "It ticks, it tocks. Repeats. Resets."
    "Because time itself’s eternal."
    "Wherever you are, I hope you’re happy."
    "Because God knows that I am not."

    stop music

    "///////////////////////STOP MUSIC"
    "///////////////////////…"
    "///////////////////////…"
    "///////////////////////…"

    play music "goodnight.mp3"

    "///////////////////////PLAY “GOODNIGHT.MP3”"

    $ renpy.end_replay()
    $ secondbeach16 = True

    jump secondbeach17

label secondbeach17:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
s "Excuse me?"

    scene pluto28
    with dissolve

    y "I, like...didn’t have a lot of friends and shit when I was little."
    y "But she used to come over a couple times a month and keep me company while my mom was getting high."
    y "But...she suddenly stopped coming over one day. "
    y "I tried asking why, but all anyone ever told me was that she was involved in some accident and hooked up to machines and shit."
    y "And when I didn’t hear anything after a few years and stopped talkin’ to my family, I just assumed she never made it."
    s "…"
    s "I mean...she has said some stuff about being in the hospital. And the whole accident thing lines up with the weird onomatopoeia she used to describe what happened to her..."

    scene pluto27
    with dissolve

    y "Holy fuck...I had no idea."
    y "Has she said anything about like...family or whatever? What’s she like now?"
    s "Uhh..."
    s "That is...not an easy question to answer. Especially since I was pretty sure she was an alien until a few minutes ago."

    scene pluto30
    with dissolve

    y "Uhh...what?"
    s "Did she ever...speak strangely when you used to know her? Like...swapping out words for {i}other{/i} words and whatnot?"
    y "Not really. She was pretty normal apart from how she dressed and shit."
    s "Well, I hate to be the bearer of bad news, but she is very likely not the same person she used to be."
    s "She has a very particular...way of speaking now."
    s "Kind of like she’s relearning not only everything about communication, but life itself."
    s "Great work ethic, though. Maybe you finally have a path to employment after all."

    scene pluto31
    with dissolve

    y "Nah."
    y "If she’s that fucked up, there’s no sense in showin’ up and confusing her even more."
    y "It’s just nice knowin’ she didn’t wind up in the dirt."
    y "Fuck, dude. I could have sworn I was gonna leave this conversation feelin’ like some sort of maniac-"
    y "But to know that was actually her and not just some delusion is just..."
    y "Just fuckin’ wild."
    s "You don’t even want to meet her? Or...well, {i}re{/i}-meet her, I guess?"

    scene pluto32
    with dissolve

    y "Maybe some other time. Would probably wind up just makin’ me feel weird if I met her now and she was a totally different person. ‘Specially if it’s as bad as you make it sound."
    s "If that’s what you want..."
    y "Welp..."
    y "Guess that’s that, then."
    s "Are you done opening up already? Or do you want to talk more about past experiences from your childhood that helped turn you into the person you are today?"

    scene pluto33
    with dissolve

    y "Come on, man. This actually went kind of well. Don’t ruin it by makin’ me bring up a bunch of shit that has nothing to do with...anything. "
    s "But we’re on a roll. What if there are more acquaintances of mine that you’re related to? We should just get them all out of the way now."
    y "Nah. I said all I needed to say. "
    y "Just gonna go for a walk or some shit and try to...I don’t know- come to terms with this, I guess?"
    y "Fuckin’ weird thinking somebody's been dead for so long only to find out that they’re wandering around town talkin’ to your asshole teacher. "
    s "Yeah...I can only imagine how strange-"

    play sound "static.mp3"
    scene pluto34 with flash
    stop sound
    stop music

    s "That-"
    s "…"
    s "Yumi?"

    "Oh, how lovely it must be to have the world turned on its head."
    "To discover that the misery you’ve wrapped yourself in is nothing but a shroud of misunderstandings and pessimistic assumptions."
    "What else have you shed tears over that was not worth shedding anything at all?"
    "Have you bled yourself dry when you could have remained hydrated and healthy?"
    "Or, perhaps you enjoy the misery?"
    "Perhaps it is the feeling of helplessness that you can throw yourself into that gives your life meaning."
    "Because lack of meaning is meaning in itself."
    "And existing to be miserable gives you the only excuse you need to get yourself out of bed in the morning."
    "…"
    "Where did Yumi go, you ask?"
    "She left quite some time ago. "
    "But you’ve been here the whole time."
    "Watching minutes...hours tick by as you attempt to make sense of your existence through words on the screen."
    "Why does everything have to hurt so much?"
    "That’s simple-"
    "Because you want it to."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ secondbeach15 = True

    play sound "static.mp3"
    scene yayapoem1 with flash
    scene yayapoem2 with flash
    scene yayapoem3 with flash
    scene tryagain1 with flash
    stop sound

    jump secondbeach16
...
```