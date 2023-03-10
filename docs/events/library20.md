# Only Child (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Futaba love greater than or equal to 20



## Next events

* [Futaba: A Book About Dragons](./library25.md)

## Event properties

* Id: library20
* Group: Futaba
* Triggered by label: library
* Triggered by branch label: library
* Triggered by path: library->library20

## Official wiki page

[Only Child](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=library20&go=Go) for more details.

## Event code

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label library20:
    scene onlychildredux1
    with fade
    play music "normalday.mp3"

    f "Oh, Sensei! Good timing."
    s "Good timing for what? What's going on?"
    f "I was actually just about to leave, so I’m happy you showed up when you did."
    s "Futaba, I am not going to watch the library for you. Especially because I don't even think you get paid for this."
    f "I don't. But I'm not going to ask you to do that either since I actually {i}don’t{/i} have to volunteer at all today. I just completely forgot and showed up anyway."
    s "Well, I'm glad you did. Because if I showed up here and you weren't around, I have no idea what I would even do."
    f "You could always read?"
    s "Pass."

    scene onlychildredux2
    with dissolve

    f "Regardless...the library is going to be closed for cleaning today, so you wouldn't be able to read even if you wanted to."
    s "Uh-oh. What are you going to do if you can't spend your morning surrounded by books?"

    scene onlychildredux3
    with dissolve

    f "Well...I was kind of hoping...that's where you'd come in."
    f "You know...since you {i}also{/i} don’t have anything to do..."
    s "Sounds good. I’ll hang out with you."

    scene onlychildredux4
    with dissolve

    f "You will?! Outside of the library?!"
    s "Sure. I mean, like you said, what else do I have going on?"
    s "Besides, it might be good for the two of us to get out instead of just hanging around here all the time. And that's doubly true for today since it's actually not extremely hot out."

    scene onlychildredux5
    with dissolve

    f "The weather has been rather unkind lately, hasn't it?"
    s "So, what should we do with our new-found free time? Want to go get lunch or something?"
    f "I would love to...If that’s okay with you, of course."
    f "I can't imagine it would be a...very good look for you being out at some restaurant with someone so much younger..."
    f "Not to mention that some of the other girls from our class could be around here right now..."
    s "I don’t really mind. If we run into someone from class, we can always just tell them I’m helping you study or something."
    s "And if that doesn't work, I'll probably just wind up having to spend some alone time with whoever catches us. So it's really not a big deal."

    scene onlychildredux6
    with dissolve

    f "Heheh...I suppose...that’s one way to handle that situation..."
    s "Hey, if you're jealous about me hanging out with the other girls, just try a little harder to not get us caught today."

    scene onlychildredux7
    with dissolve

    f "I don't...really think that's in my hands, Sensei."

    scene black
    with dissolve

    s "Well, there's only one way to find out. Come on, Futaba."
    f "Wait! Sensei! I still have to pack up my things!"

    "Futaba and I leave the library and begin to head down the same road I normally take home."
    "There are plenty of couples out and about today, but no one that we recognize."
    "Well, at least not yet."
    "After a while, we come to a stop in front of a small restaurant that Ami and Maya eat at often and decide that this is a suitable place to settle down for the time being..."
    "........."
    "......"
    "..."

    scene futabaday1
    with dissolve

    f "Umm...thanks for hanging out with me today, Sensei."
    f "I know you probably have lots of other stuff to do and-"
    s "I'm going to stop you right there, Futaba. I don't want you making it sound like I’m only doing this for you."
    f "But...I'm-"
    s "You know, one of these days, you’re going to have to accept that I might just enjoy your company."

    scene futabaday2
    with dissolve

    f "Yeah...uhh...that might be a little harder than you think."
    f "A girl like me...hanging out with someone as cool and...awesome as you? It just...doesn’t really make sense."
    f "You've noticed how people have been looking at us, haven't you? It’s like they know..."
    s "Yeah, I think there might be other reasons why people have been looking at us strangely."

    scene futabaday3
    with dissolve

    f "What...exactly do you mean by that?"
    s "I mean that even if you don't look as young as someone like Ami or Sana, I'm still noticeably older than you."
    s "I could probably even be your father."

    scene futabaday1
    with dissolve

    f "Don’t be silly, Sensei. My father is way older than you are."
    f "If anything, you'd be more like...my older brother."

    scene futabaday3
    with dissolve

    f "If...you can get past the part where we don't look anything alike."

    "Come to think of it, I don’t really know anything about Futaba’s family."
    "In fact, I barely know anything about Futaba apart from her affinity for both books and me."
    "That said...wouldn't this be a good opportunity to maybe learn about some of that?"
    "It's clear that the two of us are getting closer, but there's a limit to how close we can get without me going out of my way to learn more about her."
    "And I know wording it like that might make it seem like I don't {i}want{/i} to know anything about her, but that's not true."
    "I just think it would be a lot easier {i}not{/i} to."

    s "So...on the topic of family...why don't you tell me about yours?"
    s "I don't really know anything about them."

    scene futabaday4
    with dissolve

    f "My family? Is that...something you're actually interested in hearing about?"
    s "Sure. I mean...they're a part of your life, aren't they? You can't just keep me in the dark about your backstory forever."

    scene futabaday4r
    with dissolve

    f "Heheh...no, I suppose I can't. I can't guarantee you'll be entertained, though, as I don't think we're all that abnormal."
    f "Is there anything in particular you want to know? "
    s "How about...your parents? What do they do? Do they live around here?"
    f "They did. They live overseas now, so I haven't seen them since before Kumon-mi was closed off."
    f "Well, in person. I still video chat with them every once in a while."

    scene futabaday2
    with dissolve

    f "It’s a little sad that they're so far away...but I’m independent enough to function on my own, so it’s not like I {i}have{/i} to see them or anything."
    s "How far overseas are they, exactly?"

    scene futabaday4r
    with dissolve

    f "America. My father is an architect and is working on a bunch of aquariums for some company over there."
    f "And of course my mother followed him since the two of them are pretty much inseparable."

    "It’s good to see that there’s at least one fully functioning family still out there. I was beginning to think that all of my students were from broken homes."

    s "Do you look more like your father or your mother?"
    f "My mom. She’s like a prettier, skinnier, taller version of me."
    s "Prettier than you? I find that hard to believe."

    scene futabaday5
    with dissolve

    f "Sensei, stop! That’s way too embarrassing and...definitely not true."

    if bonus == True:
        s "Sorry, I couldn’t help it. I made a promise to myself many years ago that I would capitalize on every single chance I have to flirt with attractive girls."

        scene futabaday6
        with dissolve

        f "I guess that explains why you're so good at it...It must be all the experience."
        s "It definitely comes in handy during times like this."
    else:
        s "I apologize and will now proceed to talk about something entirely different."

    s "So, what about siblings? Do you have any?"

    scene futabaday4r
    with dissolve

    f "I don’t. I’m an only child."
    f "My mom wanted to have at least one more, but she and my dad decided it wouldn't be a good idea since the two of them travel so much."
    f "It's fine, though. I would have liked having a sibling, but I lucked out and wound up with Rin instead."
    f "She might not look like me, but she's better than any other sister I could have possibly asked for."
    s "Well, she definitely seems like she can be a handful at times...so I guess that having her is more than enough to fulfill your sibling quota."

    scene futabaday2
    with dissolve

    f "Hahah...I suppose so..."
    f "I...wouldn’t mind having a big brother as well, though. I’ve kind of always thought it would be nice to have a person like that."
    s "Any reason why?"
    f "I don’t know...I just think it would be nice to have someone who would always look after me."
    f "Unfortunately...I don't think I'll-"
    s "Don’t worry, Futaba. I’ll look after you."

    scene futabaday6
    with dissolve

    f "Heheh...You promise, Sensei?"
    f "Because I won't let you take something like that back, you know."
    s "Fine by me. I can't imagine wanting to go back on that."
    f "Is it okay if I call you big brother then?"
    s "Of course it is. In fact, please start calling me that right now."

    scene futabaday7
    with dissolve

    f "W-Wait a second! I was only kidding!"
    f "There’s no way I can just...start calling you that right now! It’s way too embarrassing!"
    s "Too late. You’ve already brought it up and it's something I absolutely need to hear now."
    f "It's also something I absolutely can't do!"
    s "How come you can call Rin your sister but not me your brother?"
    f "Because I don't have a c-"

    scene futabaday8
    with hpunch

    f "Cat! I don't have a cat! I definitely wasn't going to say {i}crush!{/i} Nope!"
    s "..."

    scene futabaday9
    with dissolve

    f "A-Anyway! What else do you want to know about my family?! I'll tell you anything you want!"
    s "You don't have to make it sound like I'm shaking you down, you know?"

    scene black
    with dissolve2

    "Futaba and I spend the next hour or so discussing her parents while finishing our meals."
    "As it turns out, she barely even remembers the last time she saw them before they left."
    "She mentions something about how it sometimes feels as if they're fading away, but I have a hard time relating on account of...well, knowing literally {i}nothing{/i} about my parents."
    "Either way, it’s surprising how unfazed she seems in the face of that. But I guess that as long as they’re sending her money, everything will be fine."

    if bonus == True:
        "Some people cherish that level of independence, especially at her age. And Futaba is no exception."
        "I just hope that this part of her doesn't change any time soon."
        "Because, despite what I frequently tell her, I have no idea if I'll always be there for her or not."
        "And being all alone in this world doesn't seem like it would be very fun."
    else:
        "Though, I guess it is kind of weird how her parents are still giving her money even though she's in college."
        "Either way, I'm glad that I learned a little more about her today..."

    $ renpy.end_replay()
    $ library20 = True
    $ futaba_love += 1
    stop music fadeout 3.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdayafternoon

label library25:
...
```

## Code that triggers this event

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label library:
    if futaba_love >= 0 and firsttimelibrary == False:
        jump firsttimelibrary
    if futaba_love >= 5 and futabafall == False:
        jump futabafall
    if futaba_love >= 10 and library10 == False:
        jump library10
    if futaba_love >= 15 and futabadorm10 == True and library15 == False:
        jump library15
    if futaba_love >= 20 and library20 == False:
        jump library20
...
```