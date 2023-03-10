# Broken Bones (Miku)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Miku love greater than or equal to 5

* firsttimesoccerfield equal to True (unknown variable)



## Next events

None

## Event properties

* Id: mikudorm5
* Group: Miku
* Triggered by label: mikudorm
* Triggered by branch label: mikudorm
* Triggered by path: mikudorm->mikudorm5

## Official wiki page

[Broken Bones](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mikudorm5&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mikudorm5:
    play sound "knock.mp3"

    "I knock on Miku's door and wait for her to answer."
    "The two of us have been getting to know each other a little better lately, so I figure it’s probably fine if the two of us start hanging out somewhere other than the soccer field or the hallway."
    "Miku also seems like the type to just let me in without question as well, so there's minimal room for this attempt on getting into her room to somehow fail."

    mi "Who goes there?!"
    s "Hey, Miku. It's me."
    mi "If this is about homework, I didn't even know we had any! I'll make it up to ya, I swear!"
    s "It's not about homework and it likely never will be. I just want to come inside."
    mi "What? You do? That ain't like, weird for ya or anythin'?"
    s "I wouldn't have knocked if it was."
    mi "Fine by me! But don't go complainin' when ya realize how boring it is."

    scene black
    with dissolve
    play sound "lock.mp3"

    "Miku quickly unlocks the door and, just as expected, I'm heading into her room with essentially no resistance whatsoever."
    "If I was some kind of horrible person, I might even take advantage of this situation."
    "Luckily for Miku and everyone else, I’m a responsible adult with an infallible moral compass who will wait until I get home to sexually fantasize about her."
    "Probably."
    "I don't know. It really depends on how the conversation goes."

    play sound "dooropen.mp3"
    scene mikufirstdorm1
    with dissolve

    mi "Heya! Welcome to Casa Del Miku! If you're lookin' for Makoto, she ain't around right now."
    s "Then, I guess it's good I came here for you."

    scene mikufirstdorm2
    with dissolve

    mi "Yeah? You sure you wanna hang out with me of all people? There are at least a zillion other girls in this dorm and they all seem closer to your type than me."
    s "What do you know about my type, Miku?"
    mi "Beats me but I imagine it involves boobs."
    mi "So, whatcha wanna do? I was about to go out for a jog, but I guess I can do that later since you don't look like you're up for it."
    mi "Come to think of it, you ever even been in our room before? Do I need to break out my tour guide voice?"

    if makotodorm5 == True:
        s "Makoto's already shown me around, actually. There was no tour guide voice involved, though."

    else:
        s "You have a tour guide voice?"
        mi "Not really. But I wouldn't mind showin' ya around in my normal Miku voice! Which may or may not sound like a tour guide."
        mi "I ain't ever toured anywhere, so I've got no idea what they actually sound like and don't know why I even mentioned it in the first place."
        s "You can just go ahead and show me around, then."

    s "It’s actually a lot cleaner in here than I imagined it would be. I’m guessing Makoto keeps it that way?"

    scene mikufirstdorm3
    with dissolve

    mi "Hey! What the heck is this?! Ya think you can just waltz into a lady’s room and insult her?!"
    mi "I’ve got pride too, ya know! I ain't some kinda slob, Sensei!"
    s "There are half-empty bottles of green tea falling off of your table as we speak."

    scene mikufirstdorm4
    with dissolve

    mi "Those are...supposed to be like that! It makes ‘em easier for me to reach!"
    s "Right, right..."

    scene mikufirstdorm5
    with dissolve

    mi "Forreal, though! I do my share of the cleanin' too! Don't let those bottles ruin your first impressions of my half of the dorm, Sensei!"
    s "Like I said, it's already better than I expected. But if you want to take the next thirty seconds showing me around the rest of the room, feel free."
    mi "Then, follow me! It ain't much, but I'll show ya everything I've got."
    s "Everything?"
    mi "Down to the last bottle of tea!"

    scene black
    with dissolve2

    "Miku doesn't pick up on the innuendo and, instead, guides me over to her bed before taking a seat on it."
    "I'm hoping she'll leave room for me as well but, unfortunately, it looks like it'll be a little longer before {i}both{/i} of us can be on it at once."
    "In other news, my streak of not sexually fantasizing about Miku comes to an abrupt end just several minutes after it began."

    scene mikufirstdorm7
    with dissolve

    mi "This here's my bed! Complete with the world's most comfortable body pillow that Makoto got me for my last birthday!"
    mi "I've also got a TV that Makoto got me for my birthday before that! And some posters she got me for some other birthdays!"
    s "Do you own anything that {i}wasn't{/i} purchased by Makoto?"
    mi "Not really, no."
    mi "Me and Makoto might not look like it, but we've been BFFs for a while and I've always spent a lot of time around her and her mom."
    s "Well, your posters could be a little straighter, but I guess you’re right about not being a slob."
    mi "The posters ain't even my fault. When you've gotta jump just to get ‘em high enough on the wall, it ain't that easy to make 'em stick."
    mi "Ya might not realize this since you’re a billion feet tall, but us short folk have it pretty rough."
    mi "Thankfully, the bed is bouncy enough that I can get up pretty high without much trouble!"
    mi "Oh, here's an idea! Wanna jump on the bed with me? Makoto ain't here, so we won't even get in trouble."
    s "I think I'll have to respectfully decline."
    mi "Guess that makes sense. Somebody your size would probably hit his head if he jumped on this anyway."
    s "I’d also probably break your bed and I don't want you to have to sleep on the floor."
    mi "Nah. I'm sure it’s strong enough to support the two of us as long as we’re not doin’ anything crazy."

    if bonus == True:
        "The fantasies continue."
    else:
        "I wonder if backflips count as crazy?"

    s "Would you mind describing what sorts of {i}crazy{/i} things you're referring to, Miku?"
    mi "That sounds like a question for Makoto. I don't know the first thing when it comes to crazy bed activities. I just know she doesn't like it when I jump too high."
    s "Sounds to me like Makoto could benefit from jumping on the bed herself."
    mi "That’s what I keep tellin’ her but she’s always like “Miku, you’re gonna break your legs and I can't afford that kind of medical bill!”"

    scene black
    with dissolve2

    "Miku picks herself up off the bed and heads over to a balance beam set up underneath her dry erase board."
    "Why she has a balance beam in her room, I have no idea. But I guess I’m not too surprised given the type of girl she is."

    scene mikufirstdorm8
    with dissolve

    mi "You ever broken a bone before, Sensei?"
    s "I don't...think so? But I could be wrong."

    scene mikufirstdorm9
    with dissolve

    mi "Probably not, then. You'd definitely remember it if you ever broke somethin'."
    s "Yeah, I'm not quite sure about that."
    mi "No, really. It hurts like heck and takes forever to get better."
    s "I take it you {i}have{/i} broken something, then?"
    mi "Well, I...yeah."

    scene mikufirstdorm8r
    with dissolve

    mi "But I mean...that sorta thing is expected when you're somebody like me, right?"
    mi "Crazy how easily bones can break even when ya go through so much conditioning, right?"
    s "The human body is surprisingly fragile."

    scene mikufirstdorm8
    with dissolve

    mi "Darn right it is! That’s why I thank my organs every morning!"
    s "You do...what?"
    mi "Ya know. Thank ‘em for performin’ their daily functions! Kinda like I thank all the girls on the soccer team after a successful practice."
    mi "Your body’s kinda like its own team, don'tcha think? "
    mi "All those weird parts inside of ya, movin’ around and pumpin’ blood! Keepin’ viruses and parasites from turnin’ yer organs to mush!"
    mi "Without teamwork, ya’d be as good as dead!"
    s "So...you thank your organs to prevent them from turning into mush?"

    scene mikufirstdorm10
    with dissolve

    mi "Well, of course it sounds weird when ya word it like that!"
    mi "I like to think of it as just the right thing to do, though."
    mi "Besides, we've all got our own weird habits and stuff!"

    scene mikufirstdorm8
    with dissolve

    mi "I'm sure you've got plenty too, Sensei!"
    s "Don't be too sure. I'm not very exciting."
    mi "Really? No weird habits at all? Nothin' that yer’ too embarrassed to tell anyone else about?"
    mi "Your old pal Miku can keep a secret! I won’t tell anyone. Scout's honor!"

    "I'm not sure if they count as habits, but there are absolutely things about myself I can't tell anyone else about- and that includes Miku."
    "Well...at least for now."

    s "No weird habits, I don’t think. I'm glad to know you can keep a secret, though. I’ll try to keep that in mind in the event that I ever decide to open up."

    scene mikufirstdorm11
    with dissolve

    mi "Sounds good to me! I'm all about the juicy stuff and I know when to keep my lips sealed!"
    s "And I will keep that in mind even more than the last thing you said."

    scene mikufirstdorm8
    with dissolve

    mi "Great! Cause whenever ya need me, I’m all yours!"

    "I can't tell if Miku is saying slightly provocative things on purpose or if she is just...incapable of thinking before speaking."
    "Actually, I'm pretty sure it's the latter now that I've actually put words to it."

    mi "I'll lend ya a hand whenever ya need it, Sensei! {i}Two{/i} hands if one ain't big enough."

    "Okay, and now I'm unsure again."

    scene black
    with dissolve

    "Miku pulls herself off of the balance beam, informally concluding our tour, before returning to the center of her room."
    "I follow her, sensing that it will very likely be time for me to leave soon as an extended session with the two of us alone might be a bit much for a first visit."

    scene mikufirstdorm5
    with dissolve

    mi "Hey...you mind if I ask ya a question really quick, Sensei?"
    s "Sure. What’s up?"
    mi "Before I ask, I've gotta say that I'm really only doin' this for Makoto's sake, though."
    mi "Like, sure I'm curious! But not as much as her. So she's the real reason this is happenin' right now."
    s "I'm confused. Are you asking me? Or is Makoto asking me {i}through{/i} you?"
    mi "Maybe...we're both askin' you at the same time? Just she's only here in spirit, so the talkin' part falls onto me."
    s "...I’m sorry, what?"
    mi "I just-"

    scene mikufirstdorm11r
    with dissolve

    mi "I...kinda wanna know what sorta girls you're into!"
    mi "For Makoto's sake! Not mine! Because...I obviously ain't your style!"
    s "Why do you keep assuming you know my style?"
    s "And why even ask in the first place if you're expecting me to say something that will put you down?"
    s "Is this some sort of trap or something?"
    mi "Course not. It ain't about bein' put down. I'm not worried at all about that sorta thing."
    mi "I'm just wonderin' since...I've got a feelin' you and me are gonna be good pals soon. And I wanna know more about you so I can be a better friend."
    s "That's nice. But I'm not going to answer your question."

    scene mikufirstdorm3
    with dissolve

    mi "What?! Why not?!"
    s "Because that's not a question that can be easily answered."
    s "I'm into whoever I'm into and I'm not going to favor anyone just for presenting themself a certain way."

    scene mikufirstdorm11r2
    with dissolve

    mi "Woah! Sensei...are you actually {i}cool?...{/i}"
    s "...Am I?"
    mi "That sounded like a thing a cool person would say. You're like the love interest in a shoujo manga all of a sudden."
    s "Thanks?"
    s "I'm telling the truth, though."
    s "You're just as much my type as anyone else, Miku."

    scene mikufirstdorm11r3
    with dissolve

    mi "Thanks, Sensei. Ya ain't gotta say stuff like that to me, though. I really {i}do{/i} just wanna get to know ya better."
    mi "Hangin' out with you's fun...and I want you to come around some more."
    s "Then, I'll be sure to do that."
    mi "..."
    s "..."

    scene mikufirstdorm11r4
    with dissolve

    mi "A-Anyway! I’m glad we’re on the same page!"
    mi "Just...don’t tell Makoto that we’re buds now or she’ll get super jealous, got it?!"
    s "Got it. Same goes for you. No one will know this meeting ever even happened."

    scene mikufirstdorm11r5
    with dissolve

    mi "Don’t gotta tell me twice, Sensei!"
    mi "Secret friendship...ACTIVATE!"

    scene black
    with dissolve2

    "Despite me sensing that it was time to leave, Miku and I hang out in her room for another hour or two before I finally head back home."
    "And just in time as well, as I bump into Makoto returning home from work on my way out of the dorm."
    "I’m glad that Miku and I are close enough to hang out like this now."

    stop music

    "But I'm even more glad that she's already starting to show her first signs of weakness."

    $ renpy.end_replay()
    $ mikudorm5 = True
    $ miku_love += 1

    "{i}Miku’s affection has increased to [miku_love]!{/i}"
    "{i}You can now spend time with her in her room!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mikudorm10:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mikudorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if miku_love >= 5 and firsttimesoccerfield == True and mikudorm5 == False:
                jump mikudorm5
...
```