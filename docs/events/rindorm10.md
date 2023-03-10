# Rin's Secret (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 10

* Event [Haruka](./cafe10.md) (Rin) is completed)



## Next events

* [Rin: Window of the Waking Mind](./cafe15.md)
* [Rin: Boundaries](./rindorm15.md)

## Event properties

* Id: rindorm10
* Group: Rin
* Triggered by label: rindorm
* Triggered by branch label: rindorm
* Triggered by path: rindorm->rindorm10

## Official wiki page

[Rin's Secret](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm10&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm10:
    play sound "knock.mp3"

    "I knock on the door and don't have time to narrate anything else as Rin answers right away."

    r "It’s open!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "........."
    "......"
    "..."

    scene rindten1
    with dissolve2
    play music "normalday.mp3"

    r "Yo! What’s crackin', homeslice?"
    s "Greet me like a normal human being please."
    r "Good afternoon, Sir. Thank you for deciding to accompany me on this lovely summer night."
    s "Closer, but still a little off."
    r "Sup bitch?"
    s "Okay, let's just skip the greetings and get right to talking. What are you up to?"
    r "Oh, you know. A little of this, a little of that."
    r "Was about to play a game or something but {i}I guess{/i} I can hang out with you instead."
    s "How generous of you."
    r "Generous would be my middle name if I was born in America and actually got to have one."

    scene rindten2
    with dissolve

    r "Futaba will be out for a while anyway, so we're free to chill without worrying about her walking in on us."
    s "Wording it that way makes it sound like you're planning on taking advantage of me."
    r "Do you {i}want{/i} me to take advantage of you?"
    s "I wouldn't mind."
    r "Not even with all of my skulls watching?"
    s "Okay, I might mind a little."
    r "That's what I thought. Can't imagine I'm very attractive in this get-up anyway."
    s "It is certainly an interesting choice for pajamas."

    scene rindten3
    with dissolve

    r "You know, I hear the same thing every time I sleep over in someone else's room."
    r "What happened to the good old days where girls were free to wear t-shirts and basketball shorts whenever they wanted? It’s not like I’m going to sleep in a three-piece suit."
    s "You know, in a weird way, I think you actually pull off this...extremely traditional look?"

    scene rindten4
    with dissolve

    r "Thanks, Sensei. And, for what it's worth, I think you can rock the black blazer and white shirt combo better than I ever could."
    s "If you're ever looking to test that theory out, I'd be more than happy to lend you the outfit. I have several pairs, so nothing will be missed."
    r "I'm glad to have finally confirmed that you're not just wearing the exact same pair of clothes all the time."

    scene rindten5
    with dissolve

    r "So, are you ready to talk business or what?"
    s "Business? What kind of business exactly? Because not only did I forget my wallet at home, but I can't imagine ever wanting to buy something without caffeine from you."
    r "Not even if it had giant boobs?"
    s "Are you...selling something with giant boobs?"

    scene rindten6
    with dissolve

    r "No, dude. I just want to know if you've talked to Futaba yet."
    s "Talked to her about what?"
    r "How you know she likes you and stuff!"
    s "Didn't you specifically tell me to {i}not{/i} mention that to her?"
    r "I told you to not reveal that {i}I{/i} told you. I didn't think you'd just treat the information like it's not valid or whatever."

    if futabadorm15 == False:
        s "So...what do you want me to do? Walk up to her and tell her I know she likes me?"
        r "For most other people, I wouldn't recommend that at all. But for Futaba, I actually think that sort of method might work."
        r "At the very least, you should at least make a move. I think you guys would be super cute together."
    else:
        "I'm not treating the information as if it's not valid. I'm just already {i}very{/i} aware of Futaba's feelings for me as {i}my{/i} feelings for {i}her{/i} wound up all over her face recently."
        "It's nice knowing that even though she's extremely close to Rin, Futaba hasn't come out and told her that yet."
        "Granted, I can't imagine bringing up the fact that you gave a teacher a handjob is an easy thing to discuss with a friend..."
        "But honestly, based on how Rin's acted about the two of us so far, I wouldn't be surprised to hear if she was super into the thought of that."

    s "You know, you've been really trying to push this Futaba thing on me lately and I'm not really sure if I get it."

    scene rindten7
    with dissolve

    r "What do you mean? What don't you get?"
    s "Like, it's one thing to think that the two of us would make a cute couple. But it's another thing if you're going to try and push me in her direction every time we talk."
    r "Not {i}every{/i} time. Just a lot of the time until you two hook up. I promise I'll shut up after that."
    s "I just don't understand what you're getting out of this is all."

    scene rindten7r
    with dissolve

    r "Sensei...Futaba is my best friend. I just want her to be happy."
    r "And I also can't imagine a future where you don't want to motorboat her enormous tits."
    s "You have a really odd way with words sometimes, Rin."

    scene rindten8
    with dissolve

    r "Oh, right! That reminds me!"
    r "I think Haruka wants a piece of you too since she's brought you up not once, not twice, but {i}three{/i} times now!"
    r "How do you keep attracting all of these extremely voluptuous women?"
    s "I suppose I'm just extremely lucky. Isn't Haruka married, though?"
    r "Yeah! That's why this whole thing was a huge surprise for me. Like, I thought she was super devoted to her husband, but apparently not."
    r "Like, I get that all women have needs and stuff, but I wasn't expecting her to start fantasizing about the first decently attractive guy to come into the store since the space war started."
    s "Thank you for the accidental compliment, Rin."

    scene rindten7
    with dissolve

    r "Accidental? No, that wasn't accidental."
    r "You're pretty hot, Sensei. I just don't know if I'm allowed to say that until my boobs grow like, eight more sizes."
    r "On the real, though, if you {i}actually{/i} want to go after Haruka...I don't think it's impossible anymore."

    "Huh..."
    "It's not like I'm entirely opposed to that. Haruka's extremely attractive."
    "It's just a matter of whether or not I want to lead someone like her down that sort of path or just...let her find her way on her own."

    s "Well, thank you for once again telling me about a girl who wants to fuck me."

    scene rindten8r
    with dissolve

    r "Well...Haruka, yeah. But I don't know if Futaba wants to do {i}that{/i} just yet. She's a bit of a...late bloomer, if you know what I mean."

    if futabadorm15 == True:
        "She is certainly in bloom now."

    r "But, uhh...yeah. Don't worry about it. That's what friends are for, right?"
    r "Like...if somebody ever liked me, I'd want you to tell me about it."
    r "In fact, please {i}do{/i} tell me about it. That's not something I want to be kept secret from me."
    s "I mean...sure. But literally everyone I know is a girl, so..."
    r "..."
    s "..."
    s "Wait-"

    scene rindten9
    with dissolve

    r "I'll save you the awkwardness of actually asking and just say yes now."
    s "So...you're a lesbian, then?"
    r "Yes."
    r "Kind of."
    r "No."
    s "I'm not sure if I follow."
    r "Like...I'm bi. I think. No. I don't think. I'm definitely bi. Probably."
    r "I've just always been, like...way more attracted to girls than I am to guys."
    r "Like, {i}way{/i} more. A scary amount more."

    scene rindten10
    with dissolve

    r "Soooo...yeah. If you ever know about anyone who was interested in me, I'd definitely want to know, like...ASAP."
    r "Especially if it was one person in particular who definitely {i}doesn't{/i} like me, but I like to pretend she does because it makes me feel warm inside."

    "It has to be Chika she's talking about, right?"
    "I've seen the way Rin looks at her before. She can barely even focus when she's around."
    "I don't think now is the right time to ask, though- considering she's only been open about her sexuality with me for a good thirty seconds now."

    r "Wow. Is it getting hot in here or is it just me?"
    s "Why are you telling me this?"

    scene rindten11
    with dissolve

    r "Should I...not have done that?"
    r "I thought you'd understand. But if-"
    s "No, I understand completely. I guess I just didn't realize we were close enough to be learning secrets like that about each other."
    r "You...didn't realize..."

    scene rindten12
    with dissolve

    r "Hah..."
    r "So, like...yeah. I know we haven't known each other that long. And I'm not like, {i}totally{/i} out yet, so you're definitely one of the only people to know for sure..."

    scene rindten13
    with dissolve

    r "I just kind of feel...comfortable enough with you I guess. Which is probably weird since I'm a teenage girl and you're a middle-ish age guy who could probably be my dad-"
    s "You can leave that part out in the future. Thanks."
    r "I just mean that even though we're totally different people living totally different lives...I kind of like the idea of you being a...bigger part of mine?"
    r "Is that weird to say? Am I being weird? Is {i}this{/i} weird? Are things going to be weird from now on?"
    s "Nah. Nothing is going to change at all."
    s "In fact, the two of us can probably bond over our shared love for teenage girls from now on."

    scene rindten14
    with dissolve

    r "Sensei! That's so sweet and only moderately creepy for you to say!"
    s "Hey, you're the one trying to hook me up with your roommate. But now, I'm wondering if that's just some sort of wish fulfillment thing for you."

    scene rindten15
    with dissolve

    r "What?! No no no no no no, it's not like that at all! I'd never even think about doing something like that with-"

    scene rindten16
    with dissolve

    r "Well, actually, that's not entirely true because I definitely {i}have{/i} thought about doing things like that with Futaba before...but purely in a fantasy world and never in real life since she's straight."

    scene rindten15
    with dissolve

    r "But that's not what the hookup thing is about at all. I really {i}do{/i} want you two to get together. And not just so I can fantasize about it. I already do that anyway."
    r "I mean what? I didn't just say that. That was the wind."
    s "Would it make you feel better if I openly admitted to fantasizing about you as well?"

    scene rindten17
    with dissolve

    r "You know, in a weird way, I really think it would."
    s "Then, I formally admit to fantasizing about you at least several times per week."
    s "And everyone else, for that matter."
    r "Thank you, Sensei. I really appreciate that."
    s "No problem, Rin. That's what friends are for, isn't it?"
    r "..."
    s "..."
    r "..."
    s "..."
    r "You should probably go now."
    s "Yeah, I think that's a good idea."

    scene black
    with dissolve2

    "I quietly leave Rin's dorm room, still confused about how things so quickly spiraled out of control tonight, but at least I'm leaving with something valuable."
    "And no- I'm not talking about the various, guaranteed lesbian fantasies that will plague my mind every time I look at her from now on."
    "I'm talking about the fact that, despite me being an outwardly horrible person who rarely does anything selfless or good for {i}anyone{/i} other than myself-"
    "Despite all that, I am trusted."
    "I am trusted and I am leaving the dorm with one of Rin's secrets."

    s "..."

    "And only time will tell if she'll regret handing it to me."

    $ renpy.end_replay()
    $ rindorm10 = True
    $ rin_love += 1
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "...."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label rindorm15:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm:
    if rin_love >= 5 and cafesugar == True and rinfirstvisit == False:
        jump rinfirstvisit
    if rin_love >= 10 and cafe10 == True and rindorm10 == False:
        jump rindorm10
...
```