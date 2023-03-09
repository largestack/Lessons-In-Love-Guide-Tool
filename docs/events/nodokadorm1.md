# The Man Who Would Be King
Nodoka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nodokadorm1&go=Go)



## Event preconditions
✅Nodoka love greater than or equal to 0

✅Event "[Main: Adult Supervision](./day288.md)" is completed (event=day288)

✅Event "[Nodoka: Humbert Humbert](./nodokafirsthall.md)" is completed (event=nodokafirsthall)

✅Event "[Otoha: Everybody Loves Otoha](./otohafirsthall.md)" is completed (event=otohafirsthall)

✅Day of week is not Monday

✅Day of week is not Friday



## Next events
None

## Event properties
* ID: nodokadorm1
* Group: Nodoka
* Triggered by label: nodokadorm
* Triggered by branch label: doorknock2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label nodokadorm1:
    play sound "knock.mp3"

    "I knock on the door and wait for someone to answer."
    "It’s my first time stopping by this room since Otoha and Nodoka moved in, and I’m curious about whether or not they’ve managed to settle in yet."
    "I know I kind of agreed to help them move, but..."
    "Well, without either of their phone numbers, it’s not like I could properly coordinate when I was going to do that."
    "I’ll just hope that everything’s been taken care of and that I don’t need to assist in any form whatsoever."

    if bonus == True:
        "The most ideal scenario would just be stumbling into a lesbian paradise."

    play sound "knock.mp3"

    "I knock again in great anticipation."

    r "Who’s there?"
    f "Rin...this isn’t your room."
    r "Oh, sorry. "
    r "Otoha, you say it."
    o "Uh...Okay."
    o "Who’s there?..."
    s "The coolest guy in Kumon-mi. "
    o "Do you guys have any idea who that would be?"
    f "That’s...obviously Sensei."
    no "I’m opening the door."
    no "It would be extremely impolite to not let Sensei experience this wondrous gathering of beautiful [young_girls]."

    if bonus == True:
        no "Quick, everyone, put your clothes back on."
        s "No. Keep them off. I will join you."
    else:
        s "Thank you, Nodoka. You are almost always so kind to me."

    scene black with dissolve
    play sound "dooropen.mp3"

    "Nodoka opens the door and waves me in."

    if bonus == True:
        "Unfortunately, everyone is clothed."
    else:
        "Thankfully, everyone is clothed."

    scene welcometodormeight1
    with dissolve

    no "Welcome to Yuritopia."

    if bonus == True:
        no "Please keep your hands to yourself at all times."
        no "You may not touch the girls, but you may touch yourself as you gaze at them."
        r "You may not."
        o "Please don’t do that."
        s "I was not planning on it."

    s "You two moved in pretty quickly, huh?"
    r "No thanks to you. "
    r "We spent like fifty percent of the move-in time just carrying all of Nodoka’s books up here."
    no "It’s confusing how they say knowledge is power when it doesn’t help you carry the objects containing said knowledge up stairs. "
    s "This issue could have been avoided if you’d only been a little more forward in giving me your number."
    no "Is that so? "
    no "I feel I’ve been plenty forward thus far."

    scene welcometodormeight2
    with dissolve

    o "Yeah...probably a little {i}too{/i} forward."
    r "Nodoka was really excited for you to show up, Sensei."
    s "Oh yeah? "

    if bonus == True:
        no "Of course. My body has been quaking with anticipation since our fated meeting in the janitor’s closet."
        o "The meeting that...never happened."
        no "My latest short story begs to differ."
        s "You...wrote a story about that?"
    else:
        no "You remind me of this one man I saw on a billboard once."
        no "It was my favorite billboard."
        s "That's nice."
        no "Have I mentioned lately that I am an author?"
        o "There she goes again, bragging about being an author."
        no "I recently published a new story titled {i}Billboard Man and the Battle Bots.{/i}"

    scene welcometodormeight3
    with dissolve

    r "I’m gonna need you to send me a link to that, please."
    o "I couldn’t even make it past the first page..."

    if bonus == True:
        no "Of course I wrote a story about that. "
        no "Sometimes, when inspiration strikes, you have to drop everything else you’re doing and really just go for it."
        no "In fact, the reason I was looking forward to seeing you so much is that I think it might be useful in helping me write even more."
        no "What sort of perverted things did we do together today, Sensei? I'll make a whole series about it."
        s "I was particularly fond of the part where we hooked up in front of everyone else here only to have them all join in moments later."
        f "Don’t give her any ideas, please..."
        f "She makes me read everything she writes and...the more characters involved, the...scarier it gets."
        no "Fear is but a mind-killer. What sense is there being scared of something that you secretly wish to experience?"
        no "Does that not dissuade you from following the path you’re already on?"
        f "I...think Nodoka might be assuming everyone feels the same way she does again..."
        r "Nodoka? Link?"
        r "Maybe just like, the name of a blog...or?"
    else:
        o "It was really fucking bad."
        r "I wanna see!"

    scene welcometodormeight4
    with dissolve

    o "I can send you some of her less...inappropriate stuff if you want. "

    if bonus == True:
        o "She’s an amazing writer when she’s not talking about closets."
        no "It appears that everyone else in the room isn’t on the same wavelength as us, Sensei."
        s "I’ve found that it’s normally just okay to assume that no one is ever on the same wavelength as me."
        no "Until now, that is."
        no "You may make use of this room as if it were your own home. "
        no "You may sleep in our beds. Dress in our clothes."
    else:
        o "She’s an amazing writer when she’s not talking about battle bots."
        r "The story was...inappropriate? How?"
        o "You'd have to read it to find out."
        s "Hey, am I allowed to take my shoes off and throw them at all of you in here? Or maybe jump on the bed?"

    scene welcometodormeight5
    with dissolve

    o "You may not do any of that."

    if bonus == True:
        no "Don’t mind her. She’s just never felt the touch of a man before."
        o "Neither has she..."
        s "I am having a hard time figuring out exactly what’s going on here."
    else:
        s "Aw shucks."
        no "Don't listen to her. Sure you can."

    no "It’s a welcome party, of course."
    s "Didn’t you guys say you were going to be listening to sad music or something?"
    s "There’s no music on and no one is doing anything. This party sucks."
    r "What are you talking about? We’re having a blast."
    s "Futaba is literally reading. "

    scene welcometodormeight6
    with dissolve

    f "It’s...it’s the last volume! And I don’t have this one yet!"
    o "Take your time, Futaba. You can borrow it if you want. "

    if bonus == True:
        no "Sensei, is your idealized version of a[teen]party just a bunch of flashing lights and underage drinking?"
        no "I didn’t realize you were so out of touch."
    else:
        no "Sensei, is your idealized version of a[teen]party just a bunch of flashing lights and drinking?"
        no "I didn’t realize you were such a boomer."

    scene welcometodormeight7
    with dissolve

    s "I just figured you’d all be doing something a little more exciting to celebrate how you’re a part of the family now."
    no "Family? Did you say family?"
    o "Nodoka...don't."
    no "I won’t. Incest without blood relation is utterly pointless anyway. Right, Sensei?"
    s "I...just meant that you’re a part of the group now. Like, the dorm family or something."
    s "I don’t know. Girls are always weirdly close with one another-"
    no "As they should be."
    s "...Girls are always weirdly close with one another, so I figured that you all would be having more fun than just sitting in a room and...waiting for me."
    no "But alas, that’s where you’re wrong."
    no "Come this way, Sensei."

    scene black
    with dissolve

    "Nodoka spins around and begins heading toward what I presume is her side of the room. "
    "It’s extremely easy to presume that on account of-"

    scene welcometodormeight8
    with dissolve

    s "You have way too many books."
    no "I do. But what is it you {i}see{/i}?"
    s "…"
    s "Way too many books."
    no "Stories, Sensei. All entirely fictitious stories."
    no "Each hiding something begging to be conveyed."
    no "If you were to open any one of these books, what do you think you’d find?"

    if bonus == True:
        no "Apart from all of the ones on the right. Those just contain orgasms and such."
        s "Wait, {i}all{/i} of the books on the right do?"
    else:
        no "Apart from all of the ones on the right. Those are just coloring books."
        s "Wait, {i}all{/i} of the books on the right are coloring books?"

    no "You heard me."
    no "Now, what do you think you’d find? "
    no "Answer the question."
    s "Just tell me the answer you’re looking for Nodoka. It’s late and I can’t be bothered to think right now."
    no "Fine. But, in exchange, you will not be earning any Nodoka points for your visit tonight."
    s "Whatever. Sure."

    scene welcometodormeight9
    with dissolve

    no "Characters, Sensei. The answer was characters."
    s "That answer was far too simple for such a misleadingly philosophical setup."
    no "Misleading philosophical setups are one of {i}my{/i} character’s lovable quirks. "

    scene welcometodormeight10
    with dissolve

    no "Now, tell me some of yours."
    s "You want me to just...tell you some of my lovable quirks?"
    no "Of course. We are at a party, are we not?"
    no "A [young_girl] and a handsome man find themselves caught up in an impromptu sidebar away from the prying eyes and ears of others-"
    no "This is the ideal territory for learning more about one another, correct?"
    f "We can still hear you..."
    r "And see you."
    o "Yeah, you only moved like five feet away."
    s "See? They’re all-"
    no "Shh. It’s “us” time now."
    no "Why not start with something simple? "
    no "Like explaining to me what you hope to find here."
    s "Here as in literally right here? Or are you being abstract again and using “here” as in human existence? "
    no "Here on the Nodoka side of the dorm room."
    s "This seems like a conversation that would be better served in private than it would surrounded by your friends."
    no "But they’re {i}your{/i} friends as well, correct?"

    if bonus == True:
        no "Or perhaps even {i}more{/i} in regard to our friends from the first floor?"
    else:
        s "Sure. I think you're all really neat."
        no "But if you could only include one of us in your Myspace top 8, who would it be?"

    r "Wait, what? "
    f "Nodoka..."
    s "I’m not sure what you’re implying, but-"
    no "You know what I’m implying, Sensei."
    o "Nodoka, chill. You’re being weird."
    no "If this is coming across as malicious or rude, I’d like to personally assure you that it’s anything but."
    no "You see, when I read books, I like to understand the motivations of the characters. "
    no "I like studying their...connections with those around them, as it better helps me immerse myself in exciting new ways of thinking."
    no "Don’t you want me to be immersed in you, Sensei?"

    scene welcometodormeight11
    with dissolve
    stop music fadeout 30.0

    if bonus == True:
        no "Would that make you feel as good as it makes {i}me{/i} feel?"
        s "Yeah, I’m not really liking this discussion in front of-"
        no "We’re not in front of anyone."
        no "We’re two people, alone at a party, with music blaring so loudly that no one will possibly hear anything the two of us say or do."
        no "What is it you want?"
        no "Look at me and tell me."
        s "…"
        no "…"
    else:
        no "Tell me about your top 8..."

    o "Whaaaaaat the fuck is going on right now?"

    "Good question, Otoha. Because I have no idea either."
    "I want to say this is some sort of test or something, but-"
    "It feels off."
    "Nodoka’s definitely been a little eccentric so far, but I didn’t exactly expect her to corner me like this in front of everyone."
    "Especially when, and this might come as a shock, I haven’t even {i}done{/i} anything this time."

    no "Sensei?"
    s "What I {i}want{/i} is to get closer to you, I guess."
    no "Just me?"
    s "Of course not {i}just{/i} you. I want to get closer to everyone."

    scene welcometodormeight12
    with dissolve

    no "Are you only saying that because the others can hear you?"
    s "What happened to no one else being able to hear us over the “blaring music?”"
    no "Right now, we’re in the grace period between songs...where the music fades out and everything grows quiet for a brief moment in time."
    s "That just sounds like a convenient response to prevent you from admitting you tripped up."
    no "God, you’re good..."
    no "Take ten more Nodoka points as a reward."
    r "Should we like...give these two some time alone or something?"
    no "Not necessary, assistant. I'd like all of you to be right here to witness anything that happens. "
    no "For as soon as I find out what it is he wants from me, the sooner I move on to finding out what he wants from all of you."
    s "Stop making it sound like I’m just...using you all to gain something."
    no "Why?"
    s "Because that isn’t what’s happening."
    no "It's not?"
    no "But there’s so much to be gained, Sensei."
    no "To max out your relationship with everyone around you would equate you to a king, wouldn’t it?"
    no "Perhaps even a god. "
    no "And who doesn’t want to be a god?"
    s "I’m perfectly fine just being Sensei."
    no "And I’m perfectly fine just being Nodoka."
    no "But that doesn’t mean I’m not a little curious about how things would look through your eyes instead of mine."

    scene welcometodormeight13
    with dissolve

    no "Besides, if the two of us need to rely on lenses to modify and magnify what we {i}do{/i} see, who’s to say that any of it is real at all?"
    no "Perhaps this entire world is nothing like either of us perceive it to be?"

    if bonus == True:
        no "If that’s true, having a god on my side seems like it would be a pretty good deal."
        no "For you too, of course, since you’d be able to force me to do all kinds of stuff."
        no "You know how gods can get without an outlet for their pent up sexual and emotional aggression."
        no "Before we know it, we’re all just fleshlights to-"
    else:
        no "Perhaps this entire world actually {i}is{/i} flat and all of those people on the Internet have been right all along."

    s "Okay, I’m going to step in now and prevent this from getting weird."
    o "It's...a little too late for that..."

    scene welcometodormeight14
    with fade

    "Nodoka steps away and rejoins the party."
    "Suddenly, everyone can hear everything again."
    "Not that they never couldn’t in the first place."
    "An uncomfortable silence sweeps through the room as the atmosphere inflates."

    play music "sweetvermouth.mp3"

    no "So anyway, who wants pizza?"

    "And then she pokes and deflates it with the dull tip of a mechanical pencil."
    "The air leaks out slowly, but the fact that so much pressure built up in the first place is not something anyone here will easily forget."

    r "I...like pizza..."
    r "But...I think there’s something else we should talk about first."
    f "Are...you feeling okay, Nodoka?"
    f "I know you haven’t been sleeping-"
    no "Perfectly fine, childhood friend and future wife."
    no "I was just administering a little test to my new teacher to see what the likelihood of him accidentally harming any of us beautiful girls is."
    no "The results of my analysis show that he is barely harmful at all- and that we may proceed in treating him just as casually as we had been previously."
    no "Sensei, what toppings do you like on your pizza? It will be my treat for any discomfort that tirade may have caused you."
    s "I wasn’t really uncomfortable. I was just kind of confused."
    s "Normally, people {i}actually{/i} make an attempt to be alone with someone for things like that rather than just...pretending."
    no "I’m not a fan of doing things normally. But we can leave things there for the time being."
    no "Now, back to pizza."

    scene welcometodormeight15
    with dissolve

    o "Actually...pizza is cool and stuff but...would you mind helping me get a few more things from downstairs first?"
    o "My parents texted me saying they dropped some more of my stuff off a little while ago...and my arms are kind of sore from carrying Nodoka’s books."
    no "Ahh, yes. The weight of knowledge has caused me a great deal of pain as well."
    r "Do you need any more help? Maybe I could come or something?"

    scene welcometodormeight16
    with dissolve

    o "Nah, you can chill here. Sensei’s got big arms, so he’ll be able to handle most of it alone anyway."
    s "So I’m back to being a piece of meat after all."

    scene welcometodormeight17
    with dissolve

    o "That’s right. "
    o "Come on, Meat-Sensei. And thanks in advance for your help."
    no "Enjoy your trip, you two."

    scene black
    with dissolve
    stop music fadeout 10.0

    "Otoha slips her shoes back on and exits the dorm room with me. "
    "We head down the stairs but, instead of stopping at the storage room on the ground floor, she heads right for the door and walks out into the cold."
    "If I knew this was coming, I would have probably just stayed upstairs."

    $ renpy.end_replay()
    $ nodoka_love += 1
    $ nodokadorm1 = True

    "{i}Nodoka’s affection has increased to [nodoka_love]!{/i}"
    "………"
    "……"
    "…"

label otohadorm1:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label otohadorm:
    if nodoka_love >= 0 and day288 == True and nodokafirsthall == True and otohafirsthall == True and day != 1 and day != 5 and nodokadorm1 == False:
        jump nodokadorm1
...
```