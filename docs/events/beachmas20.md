# Shelter
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachmas20&go=Go)


Part of event chain [I Will Deliver You to the Fireflies](./beachmas19.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: beachmas20
* Group: Main
* Triggered by label: beachmas19

## Event code
File: \game\chap3.rpy
Code:
```python
...
label beachmas20:
    scene littlebunny1
    with dissolve2

    "Somehow, I wind up in the backseat of a limousine heading to who-knows-where when, just moments ago, I was less than an inch from flipping the world on its head."
    "I’m not sure when I switched to auto-pilot, but it feels like every minute since leaving Noriko alone in her orange-tinted clearing has been the first minute of my life."
    "So I ask you-"
    "When was the last time {i}you{/i} felt alive?"
    "Because for me, it..."
    "Fuck it."
    "I don’t want to talk to you anymore."

    s "You know...you’re one of the last people I would have expected to end the night with."
    to "Oh? And why is that?"
    s "Because I’ve been having a nonstop marathon of melancholy with girls that I know much better than you over the last forty-eight hours- in which I have barely seen {i}you{/i} at all."
    to "That problem could be easily remedied by looking at me a little more, Sensei."
    s "My bad, Tobiko. I guess I just had other things on my mind."
    to "If you’re going to start playing the name replacement game again, please at least give me a {i}human{/i} name. I like to believe I’m a tier or two above {i}fish eggs.{/i}"
    to "As for your {i}mind{/i} and what could have been on it, I apologize again for interrupting you and Maya. But I hope that what I am about to show you will make it at least {i}somewhat{/i} worth it."
    s "Me too. Opportunities like that haven’t really been all that common for me."
    to "Nonsense. You have plenty of opportunities to push the boundaries of what is and isn’t acceptable with your students every single day. I have heard the things they say about you, you know? I have ears."
    s "Sure, but that’s not {i}Maya.{/i}"
    to "Is there something special about Maya? Something {i}she{/i} has that the rest of us do not?"
    s "Well..."
    s "There was."
    to "And there’s not anymore?"
    s "Things have changed a little, but...there probably still is. Explaining it would take a lot longer than a drive to...wherever it is you’re taking me right now, though."
    to "Then I suppose I’ll be waiting with bated breath for whenever that time comes."
    to "For now, I’m unfortunately going to have to blindfold you."
    s "What is it with your family and blindfolding people? Is Imani in the trunk? Who is going to try and sell me things this time?"
    to "Shush. Surely, you don’t mind covering your eyes for a few minutes to repay me for all of the trouble I went through in order to ensure that we got away undetected."
    s "I hope you realize how much trouble this is going to get {i}me{/i} into. I already disappeared last night. There’s no way pulling that two nights in a row is going to end well."
    to "I suppose I’m a bit of a troublemaker now, aren’t I? "
    s "“Kidnapper” is probably more accurate."
    to "I wonder who it is that’s been such a bad influence on me?"
    s "I saw you talking to Molly earlier, so probably her."
    to "Oh good. So you did look at me at least once. "
    to "Was it on purpose? Or did you just happen to catch a glance while you were looking for Maya?"
    s "What happened to pretending you never saw anything?"
    to "Rest assured, I won’t tell anyone else. But I seldom get opportunities to push {i}your{/i} buttons and I think you look awfully cute when you’re on the defensive."
    s "I’m not defending anything."
    to "Adorable. It’s like you’re a real, living thing all of a sudden."
    s "Says the fish eggs."
    to "Close your eyes, Sensei."

    scene black
    with dissolve2

    s "Fine. But the last time somebody told me to do that, I wound up with a tongue in my mouth."
    to "But there is always a tongue in- oh. Ew. Stop that."

    "Touka leans over and wraps a blindfold around my head."

    play sound "static.mp3"
    scene littlebunny2 with flash
    stop sound

    "{i}And then I take over again!{/i}"
    "{i}Hi there! Everybody’s favorite narrator here to bash you over the head with as many life lessons as I’m able to fit in these scrawny little arms of mine.{/i}"
    "{i}Or should I say...Lessons IN LOVE?! Ha! I kid, I kid. But only because I know breaking whatever wall that title lies behind will get your brain chugging.{/i}"
    "{i}So, it appears that our third beach vacation is coming to a close. And while a handful of doors have both opened AND closed over the last couple days, it’s important to remember that doors are just doors!{/i}"
    "{i}What I mean by that is that there’s almost always something on the other side.{/i}"
    "{i}It doesn’t matter if it’s closed or open so long as there is latent awareness that objects exist on both sides! Right? Right!{/i}"
    "{i}Behind Door #1, we have two lovely, albeit relatively scary teenage girls about to connect in a way that both of them were beginning to feel they never would!{/i}"
    "{i}The lesson? That following your heart is a double-edged sword! Especially when your heart keeps leading you toward a dead end with a face.{/i} "
    "{i}Take it away, Noriko!{/i}"

    n "Kirin!"
    ki "Uhh...hi? Aren’t you supposed to be hanging out with Sensei right now?"
    n "I did! And then we made out! And then we dry humped for like ten minutes! And then I came!"

    scene littlebunny3
    with dissolve

    ki "Woah, really?! Then what?!"
    n "Then he left!"

    scene littlebunny4
    with dissolve

    ki "What?! Why?! "
    ki "Don’t tell me you were gonna force him to wear one of those stupid-"
    n "No, no. I would have let him do whatever. He just had...other plans, I guess."
    ki "..."
    n "..."

    scene littlebunny5
    with dissolve

    ki "Are you okay?"
    n "Yeah. I’m okay."
    ki "Noriko-"
    n "Seriously. I’m good. Progress is progress and I’m not about to rush him when he’s been so patient with me. "
    ki "Are you just saying that because you think it’ll make it hurt less?"
    n "It works for you, doesn’t it?"
    ki "It’ll...hold you over for a little while."
    n "Do you think it’ll last until we make it back home? Because I’d much rather cry on my bed than a random beach chair."

    scene black
    with dissolve

    ki "Hah...what about a beach chair with your best friend on it?"
    n "That doesn’t really change how random the chair is."
    ki "Get on."
    n "Will you rub my head?"
    ki "Yes, but you’ll owe me a back massage before the year ends."

    play sound "static.mp3"
    scene littlebunny6 with flash
    stop sound

    "{i}Behind Door #2, a small group of friends with an appendage severed in the form of an absentee! But what is that disembodied limb up to right now? And why does its counterpart keep trying to find it?{/i}"
    "{i}The short and easy answer would be that things are easier when you work as a team! And that two heads are always better than one!{/i}"
    "{i}But the longer, more complicated answer involves a series of painful, psychological discussions in which we evaluate the concepts of codependency, adultery, honesty, and most importantly...hormones! Yay!{/i}"
    "{i}Take it away, gals!{/i}"

    r "Hah...come on, Otoha. At least give me a “Merry Christmas” or something. Anything."
    f "Nodoka, what did you give Sana for Christmas? She’s been freaking out for almost an hour now."
    no "The only thing that could possibly benefit her at such a confusing time in her life, of course."
    f "..."
    no "..."
    f "You didn’t."

    scene littlebunny7
    with dissolve
    play sound "phonebeep.wav"

    no "If that is what you wish to believe, my beloved Futaba. But know that any gift I give to {i}anyone{/i} is done with only the most excessive amount of care."
    r "Ah! Guys! Guys! She finally texted back! And with...two hours and thirteen minutes to spare!"
    r "But what does it say? What does-"

    scene littlebunny8
    with dissolve

    r "Ooooooh...my god..."
    f "I’m so happy for you, Rin! Even though it probably wasn’t worth the time investment and-"
    no "Oh my. I’d recognize those breasts anywhere."

    scene littlebunny9
    with dissolve

    no "I should probably look a little closer just to be sure, though."
    f "What?! Why?! Who ignores someone for two days and then sends them naughty pictures?! That doesn’t make any sense at all!"
    r "Nodoka! Stop looking! And Futaba, this doesn’t make any sense to me either! But I am definitely not about to argue!"
    r "Maybe this is her way of apologizing?! Or telling me she’s ready to start doing other stuff?!"
    r "Either way! I suddenly have to go to the bathroom! Goodbye!"

    scene black
    with dissolve

    no "Oh, I’ll come. It’s safer to go in groups after all."
    r "No thanks, Nodoka! Please don’t come looking for me either!"

    "{i}What lesson did we learn this time, friends?{/i}"
    "{i}That’s right! That hiding the truth when it’s going to hurt someone isn’t always bad! In fact, sometimes it fixes everything! Hooray!{/i}"

    to "Okay...you can open your eyes now."

    play sound "static.mp3"
    scene littlebunny10 with flash
    stop sound

    "I open my eyes and..."

    s "..."

    "And I still have no idea where I am."

    scene littlebunny11
    with dissolve

    to "Hmm...it’s smaller than it looked in the pictures. But I suppose this will do. "
    s "Do {i}what?{/i} Where are we?"

    scene littlebunny12
    with dissolve

    to "Your new apartment."
    s "My {i}what?{/i}"
    to "Apartment. It’s like a smaller, temporary housing unit in a-"
    s "I know what a fucking apartment is, Touka. What I’m asking is why you bought me one."

    scene littlebunny13
    with dissolve

    to "Do you not like it?"
    s "That’s not the problem here. This is way too huge of a gift. And I already own a house."
    to "Yes, but this one is much closer to {i}my{/i} house. And I have seen your home. It is rather outdated, Sensei. No offense."
    s "I can’t accept this. There’s no way. Void the lease or something."
    to "There is no lease. I bought the entire building."
    s "Oh my god."

    scene littlebunny14
    with dissolve

    to "I thought it would be a good means of training myself to handle part of the family’s hospitality business once I enter college. "
    s "So...you’re my landlord?"
    to "Land{i}lady.{/i}"
    s "Who else knows about this?"
    to "Just Makoto. She told me it was a bad idea. But by the time I was informed of that, it was already too late."
    s "You really need to start getting your presents approved ahead of time. This is insane."

    scene littlebunny10
    with dissolve

    to "I think it’s rather fun, actually! "
    to "Come! We can test out the bed together!"
    s "Do you not hear yourself right now?"

    play sound "static.mp3"
    scene littlebunny15 with flash
    stop sound

    "{i}Behind Door #3 we have more friends, joined this time by the stark realization that this world might be a little more complicated than we think!{/i}"
    "{i}The lesson this time is that things ARE more complicated than we think. And also that I’m only a little bit jealous of Yumi’s chest. Wowza.{/i}"

    c "Hey. How’d it go? That took a lot longer than I thought it would."
    y "Sensei left a while ago...I was just over there thinkin’ about shit."
    c "What kind of shit?"
    y "Chika, you ever, like...lose your memories? Or get really confused when trying to explain certain stuff?"
    c "Uhh..."
    c "I mean, Sensei has memory problems, doesn’t he? I can’t really say I’ve ever experienced anything like that."
    y "Then...do you remember what me and him talked about after the Dorm Wars? Or...{i}anything{/i} that’s happened over the last two months?"
    c "I remember the last two months, of course. But I have no clue what you and Sensei talked about back then. You never told me."

    scene littlebunny16
    with dissolve

    y "Huh..."
    c "This isn’t what you wanted to talk to Sensei about tonight, is it? Because I was assuming it was something a little more...I don’t know. Important?"
    y "Important how?"
    c "Beats me. Maybe something about how much time you guys have been spending together lately?"

    scene littlebunny17
    with dissolve

    y "We’ve...what? Why? {i}When?{/i}"
    c "Yumi, you can’t just never tell me anything and then ask me to recap your life for you. I just figured it had something to do with you getting let back into school."
    c "Do you remember that much at least?"
    y "Yeah, I-"

    scene littlebunny18
    with dissolve

    y "I..."
    c "..."
    y "I don’t remember {i}shit...{/i}"
    c "Yumi..."
    y "What the fuck is going on?"

    play sound "static.mp3"
    scene littlebunny19 with flash
    stop sound

    "{i}Here we are at Door #4!{/i}"
    "{i}I had to mess with the handle a little bit to get this one open, but I wanted to make sure you saw it before the credits roll or however it goes when stuff like this normally ends for you.{/i}"
    "{i}Anyway, this one’s a little depressing, so I won’t bother with a full-on introduction this time.{/i}"
    "{i}But I will remind you that it’s okay to cry! Even when it feels like there’s nothing to cry about.{/i}"
    "{i}Goodbye for now! I have to go bust down Door #5.{/i}"

    m "..."
    m "..."
    m "..."
    m "What am I doing here?..."
    a "Maya?"

    scene littlebunny20
    with dissolve

    m "Uhh...hey! I didn’t realize you were...this far along the beach."
    ay "We were...looking for Sensei..."
    ay "Is everything-"

    scene littlebunny21
    with dissolve

    m "Y-Yeah! Just...got some sand in my eyes. It’s nothing."
    ay "Ami...maybe we should leave Maya alone for-"

    scene littlebunny22
    with dissolve

    m "Huh?..."
    a "Why are you lying?"
    m "Ami?..."
    a "It’s okay to cry."
    a "Even when it feels like there’s nothing to cry about."

    scene littlebunny23
    with dissolve

    m "I’m not crying..."
    a "Maya!"

    scene littlebunny24
    with dissolve

    m "I’m not crying!"

    scene littlebunny25
    with dissolve2

    m "I’m..."
    m "I’m not..."

    play sound "static.mp3"
    scene happy9 with flash
    stop sound

    m "{b}AAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!!!{/b}"

    play sound "static.mp3"
    scene littlebunny26 with flash
    stop sound

    to "..."
    s "..."
    to "I’ll get you a new mattress. This one isn’t as soft as I expected it to be."
    s "I can’t believe you bought me a fucking apartment. What am I going to tell Ami?"
    to "You don’t have to tell her anything if you don’t want to. It’s not as if I was expecting you to live here full-time."
    to "I just figured it would be a convenient place for you to relax or take shelter from the many young girls fighting for your heart every day."
    to "Even I could tell it was getting to you during the Dorm Wars."
    s "Thank you, Touka. No one else ever believes me when I say that."

    scene littlebunny27
    with dissolve

    to "Ooh! I’ve always wanted to say this-"

    scene littlebunny28
    with dissolve

    to "{i}I’m not like the other girls...{/i}"
    s "Well, you’re certainly right about that. The only girl I can think of who’s had as grand of a gesture as this is Noriko and..."

    scene littlebunny29
    with dissolve

    s "And I left her all by herself tonight..."
    to "You can’t please everyone all the time, Sensei."
    s "Pleasing one person one time might be a nice change of pace, though."
    to "I’m sure that day will come."
    to "But in the meantime, allow me to please {i}you.{/i}"
    s "Fine. But I need to close the window first so no one sees us."
    to "And that’s my cue to leave."

    scene black
    with dissolve

    s "You’re leaving already?"

    scene littlebunny30
    with dissolve2

    to "You didn’t expect me to live here with you, did you?"
    s "No, but...it feels like you just got here."
    to "I did. And so did you. But {i}now,{/i} I have to be getting back to the beach house to continue celebrating with my friends. "
    to "You’re welcome to come if you’d like, but the driver will be different and there won’t be a blindfold this time."
    s "..."
    to "What’s wrong? I believe that was the moment where you were supposed to comment on not actually liking blindfolds or something along those lines."
    s "I don’t think I want to go back to the inn."
    to "Worried the rest of the girls will see us come back together?"
    s "Worried of {i}who{/i} I’ll see."
    to "Hmm...My initial impression of you is proven more and more wrong every day."
    to "You really are interesting, Sensei."
    s "I don’t understand what you mean..."
    to "Nothing in particular. There are just certain things you do and say that make me want to baby you...similar to the way I do with Yasu."
    s "Please don’t."
    to "Why not?"
    to "Will it make you feel weak?"
    s "..."
    to "You can act brave and strong all you want, but that facade won’t last forever."
    to "But at least now you have somewhere it can crumble in private."
    s "I think you should stay here with me."
    to "Why?"
    s "Why do you {i}think?{/i}"

    scene littlebunny31
    with dissolve

    to "Boop."
    s "Touka-"
    to "I will not let you take shelter from your feelings in me. I’m far too smart for that."
    to "You’re afraid of new sensations...so you want to mask them with familiar ones instead. Is that right?"
    s "I don’t think you understand-"
    to "Goodnight, Sensei. "
    to "Oh, and kiss her next time. Idiot."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "Wait-"
    to "The driver is waiting! Either you come back to the inn and talk to me along the way, or I will see you in school next Monday!"
    s "..."
    to "..."
    to "That’s what I thought."

    play sound "static.mp3"
    scene littlebunny32 with flash
    stop sound

    "{i}Fuck! Uhh...I got Door #5 open, but I kind of have to go now, so...bye!{/i}"

    ya "Let the birds sing, dilly, dilly...And the lambs play~"
    ya "We shall be safe, dilly, dilly...Out of harm's-"

    scene littlebunny33
    with dissolve

    ya "Ah! Penemue! You can fly! Where did you learn how to do that?!"
    ya "Come down before you hurt yourself and I’ll reward you with a bucket of well water."
    se "Well, aren’t you the cutest little thing?"

    scene littlebunny34
    with dissolve

    ya "Huh? "
    ya "Who-"

    play sound "static.mp3"
    scene minigod1 with flash
    scene minigod2 with flash
    scene minigod3 with flash
    scene littlebunny35 with flash
    stop sound

    s "..."
    s "..."
    s "..."

    "Touka was right...I {i}was{/i} trying to take shelter from my feelings by using her body as a shield."
    "It wasn’t my proudest moment, asking her to stay less than an hour after {i}almost{/i} kissing Maya, but...I doubt Maya would even be surprised if she heard about it."
    "There’s no expectation placed on me to drop everyone else just because she and I are...what {i}are{/i} we anyway?"
    "She never said anything and never did anything. So it’s kind of like nothing ever happened in the first place."
    "And if nothing ever happened in the first place, things right now aren’t any different from how they were last night when I forgot about her."
    "I don’t even understand love in the first place, right?"
    "That was just a thing I said in the heat of the moment, right?"
    "And...her too. "
    "She never would have acted that way if I never-"

    s "..."
    s "..."
    s "..."

    scene black
    with dissolve2
    stop music fadeout 20.0

    "I wonder if there’s a pen around here?"

    $ renpy.end_replay()
    $ beachmas20 = True

    scene tobecontinued
    with dissolve2

    jump postbeachmas1

label postbeachmas1:
    "........."
    "......"
    "..."
    jump postbeachmas1
...
```

## Code that triggers this event
File: \game\chap3.rpy
Code:
```python
...
m "Everything evil and everything worse!"
    s "And?"

    scene fireflies21
    with dissolve2

    m "And..."
    m "If the world ends right now, I won’t care."
    m "I’ll find you again."
    m "As many times as it takes."
    s "You still haven’t said anything..."
    m "I’ve never had much of a way with words."
    m "I liked your second idea better."

    scene fireflies22
    with dissolve

    to "Oh, wonderful! I’ve been looking all-"

    scene fireflies23
    with hpunch

    to "Ah! Never mind! I was never here and didn’t see anything! Please go back to having your moment and feel free to entirely disregard my existence from this point onward!"
    m "Moment? What moment? We weren’t doing anything weird. I don’t even like Sensei."
    s "Why would I ever have a moment with someone who spends the entire day insulting me?"
    m "And why would {i}I{/i} ever have a moment with an adult? I’m a normal teenage girl with normal teenage interests and preferences."
    s "Yeah. Maya’s too short and her chest is too small for me."
    m "{i}Okay, that wasn’t necessary and is also blatantly untrue.{/i}"

    scene fireflies24
    with dissolve

    to "I’m not sure if I believe any of that when you both sound so much different from the way you normally speak...and are also so close in physical proximity to one another..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene fireflies25
    with dissolve2

    m "{i}Ahem.{/i}"
    m "So...that was an interesting and informative platonic meeting we just had. Right, Sensei?"
    s "Yeah. It was interesting and informative and completely free of anything inappropriate between teacher and student."
    to "Just so the two of you are aware and can put an end to this terrible game of charades, I have no intention of telling anyone what I saw."
    m "Saw what? You didn’t see anything."
    s "Yeah. Nothing happened. And if anything did happen, it would have all been one big misunderstanding."
    m "Yup. "
    to "R...Right..."

    scene fireflies26
    with dissolve

    m "So, uhh...Touka! What...are {i}you{/i} doing over here?"
    to "I...was assigned Sensei for Secret Santa this year and, considering the slightly time-sensitive nature of his present, was out looking for him before my driver returns to the manor."
    s "Driver? Your present involves going somewhere?"

    scene fireflies27
    with dissolve

    to "It does. But I’m afraid we must leave right now as I’ve already kept him waiting for far longer than I would have liked due to my hesitancy regarding the matter."
    s "Can it maybe wait until another time? Maya and I-"
    m "No! Now is fine! Go! I’m gonna...uhh..."
    m "I’m gonna for a walk! Platonically, of course! Which doesn’t really make sense because it’s just a walk by myself and..."
    m "Hahah! Anyway, bye!"

    scene fireflies28
    with dissolve

    s "Maya-"
    m "See you! Bye! Tell Ami I- ack!"
    to "Maya, please face forward when you’re walking. There are many large rocks on this beach and it would dangerous to have you tripping over more of them."
    m "I’m okay! Bye!"
    s "..."
    to "..."

    scene fireflies29
    with dissolve

    to "Well, that was certainly a side of her I’ve never seen before."
    s "Yeah...same."
    to "Sensei, I truly am sorry for interrupting what appeared to be such an important moment between you two. But seeing as the driver is waiting-"
    s "Yeah, we can go. And thanks for...coming to find me, I guess."
    s "You either showed up at the worst possible time or the best."
    s "I’m not really sure yet..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ beachmas19 = True

    jump beachmas20
...
```