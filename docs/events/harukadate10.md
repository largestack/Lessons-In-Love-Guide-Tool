# Performance Review
Haruka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=harukadate10&go=Go)



## Event preconditions
✅Haruka love greater than or equal to 10

✅Event "[Main: Kadrillionbilliontrillion](./halloween14.md)" is completed (event=halloween14)

✅Event "[Haruka: Invisible Worm](./harukadate5.md)" is completed (event=harukadate5)

✅Event "[Rin: Ten Steps Forward](./rindorm35.md)" is completed (event=rindorm35)



## Next events
* [Haruka: Watching TV Alone](./harukadate15.md)

## Event properties
* ID: harukadate10
* Group: Haruka
* Triggered by label: harukacafe
* Triggered by branch label: saturdaymorning

## Event code
File: \game\HarukaEvents.rpy
Code:
```python
...
label harukadate10:
    scene harukarinreview1
    with dissolve
    play music "cafe.mp3"

    "I show up at the cafe to find Haruka and Rin sitting at a table near the door. "
    "The girl manning the counter is someone I haven’t seen before so, not wanting to involve myself with anyone new, I decide to intrude on the conversation between these two."
    "Judging by the clipboard, however, it appears that I may have suddenly walked into a relatively important discussion."
    "Whoops."

    r "Hey! Is it Sensei-time already?"
    h "Yes, it appears it is Sensei-time."
    s "Sensei-time isn’t a thing. Please don’t say that anymore."

    scene harukarinreview2
    with dissolve

    r "{i}Sensei-time{/i}."
    s "…"
    s "Anyway, what are you two doing over here? Shouldn’t you be working right now?"

    scene harukarinreview3
    with dissolve

    h "I was actually just doing Rin’s performance review for the quarter."
    r "Yup-yup. And, news-flash, turns out I’m pretty awesome. Who would have thought?"
    s "Not me considering you have only given me what I’ve actually ordered maybe once or twice since I started coming here."
    r "That’s just cause you’re special. Tell him, Haruka."
    h "This is news to me, actually. I’m going to dock a few points from your review so I don’t have to give you a raise."
    h "Please do better in the future for the sake of the company."
    r "…"
    h "…"

    scene harukarinreview4
    with dissolve

    r "Are you bein’ for real right now?"
    h "Of course not. You can keep making whatever you want for him as long as he continues to keep doing nothing about it."
    s "Wow, the service here has really gone downhill lately."

    scene harukarinreview5
    with dissolve

    h "Like Rin said, you’re special. "
    h "Plus, we’re friends now."
    h "I don’t have to be nice to you anymore now that I know you’re here for the girls instead of the coffee."
    r "Hey wait a second, how come you two are acting super close all of a sudden?"
    r "When did this happen?"
    s "In my defense, I am not acting any different than normal. This is all Haruka."

    scene harukarinreview6
    with dissolve

    h "There’s no need to be jealous, Rin. I’m sure you still see him more often than I do."
    r "Well...probably."
    r "And I’m not jealous. I’m just surprised. "
    r "I could have sworn you were a loner, Haruka. I didn’t even know you talked to anybody other than all of us at the cafe."

    scene harukarinreview7
    with dissolve

    h "Oh. Well thank you for reminding me of how incredibly lonely I am, Rin. I appreciate that."
    r "No sweat! This is just our thing, isn’t it?"

    if bonus == True:
        r "You tease me about not being able to reach the syrup bottles on the top shelf and I tease you about going years without getting laid."
    else:
        r "You tease me about not being able to reach the syrup bottles on the top shelf and I tease you about your stupid pink hair."

    if harukasex == True:
        scene harukarinreview8
        with dissolve

        h "…"
        s "…"

        "Don’t do it, Haruka. "
        "Don’t say anything."

        r "Hm? Isn’t this the part where you come up with some sarcastic remark or something?"
        r "We’re supposed to go back and forth right about now and-"
        r "…"

        scene harukarinreview9
        with dissolve

        r "Oh my God, you fucked my boss!"
        r "Dude!"
        h "Hahaha..."
        s "Don’t you think I would have told you if something like that happened, Rin?"

        if rinbetrayed == True:
            scene harukarinreview10
            with dissolve

            r "No, actually. You kind of have a track record of going behind my back with people I know now, so yeah. "
            s "That’s..."

            "I decide against prying anymore into that side of things at the risk of further-destroying my relationship with Rin."

        else:
            scene harukarinreview11
            with dissolve

            r "Well, yeah. But Haruka really only gets quiet like this when she’s trying to hide something."
            r "Plus, I already told you she thought you were cute and stuff a while back, so it’s not {i}impossible{/i} for something like that to happen."

        scene harukarinreview12
        with dissolve

        r "I’m kind of surprised by Haruka, though. "
        r "I know you haven’t seen your husband in a while but I didn’t think you’d crack under the pressure that-"
        h "I didn’t crack. "
        h "Nothing is going on between your teacher and me. "
        h "I was just messing with you since I know you two are close."

        scene harukarinreview13
        with dissolve

        r "Well..."
        r "That’s kind of a relief. But now I also feel really bad about accusing you of something like that."
        r "You should probably get a little better at hiding things if you want to-"
        h "Get back to work, Rin."
        r "I was just leaving."
        r "Sorry."

        scene harukarinreview14
        with dissolve

        "Rin quickly ducks away from the table, taking her notebook and coffee with her before disappearing into the back room."

    else:
        scene harukarinreview15
        with dissolve

        if bonus == True:
            h "Hey. You leave my sex-life out of this. "
            h "Do you have any idea how satisfying it will actually be when he comes back from the war?"
            r "Nope. I’m an innocent virgin barista so I have no idea how satisfying it is in the first place."
        else:
            h "My hair is not stupid!"

        scene harukarinreview16
        with dissolve

        h "Oh my God...Why am I even talking to you about this?"
        r "Sensei, I’m sorry my boss doesn’t feel the same way about you as you feel about her."

        if rinbetrayed == True:
            r "Thankfully, the girl I’ve been after for literally years is, so you’ll have to settle for fucking a cute [teenager] instead of a voluptuous older woman."
            r "Sorry for your loss."
            s "Rin..."

        else:
            r "There are plenty of other fish in the sea, though. I’m sure you’ll catch one eventually."

            if bonus == True:
                r "Heck, you might even have a shot with me if you keep trying. It only makes sense to fall for someone you keep spending time with, right?"
                r "Sure there’s the added issue of me still thinking penises are kind of scary, but you know how it is."
                s "I thought I did until that last part. Now I’m just back to being confused."
            else:
                s "But Papa never taught me how to fish."

            r "It is what it is, homie."

        scene harukarinreview17
        with dissolve

        h "And on that note, our review is now complete."
        h "Get back to work, Rin."
        r "Aye aye, Captain Haruka! "

        if bonus == True:
            r "Have fun not having sex with my teacher!"
        else:
            r "Have fun not hugging my teacher!"

        h "And you have fun cleaning the bathrooms. Leave."
        r "Roger that! Love you, bye!"

        scene harukarinreview18
        with dissolve

        "Rin quickly ducks away from the table, taking her notebook and coffee with her before disappearing into the back room."

    s "I have to commend you for being able to put up with her for this long every weekend."
    h "You have to put up with her too, don’t you? Isn’t she in your class?"
    s "She is, but she’s a little different in[school] than she is here."
    s "She seems happier in the cafe. Kind of like she admires you or something like that."

    scene harukarinreview19
    with dissolve

    h "Me? Why would she admire me?"
    h "All I do is work and talk about what shows I’ve been watching on Netflix lately."

    if harukalust10 == True:
        h "I’m kind of insanely boring if you take out the part about me dressing up as a cat and riding you on occasion."
        s "But that’s my favorite part about you."

        scene harukarinreview20
        with dissolve

        h "I still kind of can’t believe I was drunk enough to do something like that."
        h "Maki really manages to bring the worst out of me sometimes."
        s "Was it Maki’s idea to invite me over?"
        h "Well, no. But-"
        s "Then don’t blame her for what happened. "
        s "You made a decision and you followed through with it. She just happened to be there for it."
        h "…"

        scene harukarinreview21
        with dissolve

        h "You’re right. I need to accept responsibility for my actions."
        h "I’ve just gone so long without being...involved in someone new that I kind of forget how it works at times."
        h "But, in my defense-"
        h "Maki is fucking hot."
        s "I can’t believe you made me wait an extra 24 hours to hook up with you two after the Halloween party at the bar."

        scene harukarinreview22
        with dissolve

        h "And I can’t believe you went upstairs with Sara without inviting the two of us."
        s "Sara didn’t want you to come."
        h "I can’t believe you didn’t keep pushing for it to happen. Jerk. "
        s "Didn’t you pass out within the next 30 minutes anyway? "
        h "Yes. Out of disappointment."
        s "Poor Maki. "
        h "More like poor Haruka."

        if saralust10 == True:
            h "Kind of degrading listening to your best friend get fucked by the guy you’re into while you sit downstairs and get drunk."
            s "You heard us?"

            "I guess that makes sense given how old the building Sara lives in is."
            "That’s kind of concerning in the event of anyone else ever being downstairs while...things are happening, though."

            h "Of course I heard you. That girl is even louder than I am."
            s "Mmm...I don’t think that’s true."

            scene harukarinreview23
            with dissolve

            h "I’m louder than {i}that{/i}? "
            s "Do you not realize how into it you get, Haruka?"
            h "I had no idea..."
            h "My neighbors...Do you think they, you know, hear us?"
            s "I’d be shocked if they didn’t, to be honest."

            scene harukarinreview24
            with dissolve

            h "Oh God..."
            s "Something wrong?"
            h "A lot is wrong. I don’t want to talk about it here, though."
            h "Apparently I’m a walking megaphone so I don’t want the girls to hear us talking about how loud I am when you fuck me."
            s "Right. "
        else:
            h "Maki might be super hot, but I don't really think she could please me the same you can."
            s "If there is any woman who can do just that, I'm positive it's Maki. Have you seen the arsenal of sex toys at her shop?"

    else:
        s "You’re right. That does sound incredibly lonely."

        scene harukarinreview25
        with dissolve

        h "It’s even lonelier when I eat an entire pint of ice cream and cry myself to sleep afterward."
        h "Such is the life of a woman who lives alone. "
        s "Sara lives alone and I doubt she cries herself to sleep every night."

        if bonus == True:
            h "Yes but Sara also keeps a dildo on the shelf next to her bed so she is clearly a force to be reckoned with."
        else:
            h "Yes but Sara also keeps an entire wheel of cheese on the shelf next to her bed so she is clearly a force to be reckoned with."

        s "Yeah, good point."

    s "But anyway, I {i}do{/i} think Rin sees you as some sort of role model. At least that’s how I’d see you in her position."
    s "People like looking up to more successful people in the same position as them."
    s "And even if you’re lonely, you’re still doing something with your life."

    scene harukarinreview26
    with dissolve

    h "Did you really come here just to lecture me?"
    s "No. I came here to see you. So this is supposed to be the part where you start feeling a little less lonely."

    scene harukarinreview27
    with dissolve

    if bonus == True:
        h "You’re here to see {i}me{/i} despite having a girl like, half my age and four times prettier than me two steps away from just...biting the bullet and admitting her love for you?"
        s "Rin doesn’t {i}love{/i} me, Haruka."

        scene harukarinreview28
        with dissolve

        if rinbetrayed == True:
            h "Oh please. She looks at you differently than pretty much every other guy that’s ever come in here."
            h "She swings both ways, doesn’t she? I’m sure she’d be more than willing to embark on a journey of sexual exploration with you under the right circumstances."
            s "It would be easier for me to believe that if I didn’t finger the girl she’s in love with."

            scene harukarinreview29
            with dissolve

            h "You fingered the cute blonde girl who comes in here all the time?!"
            s "…"
            s "No. You never heard that."
            h "No! I did totally just hear that!"
            h "How did that even happen?!"

        else:
            h "Oh, please. Ever since the blonde girl rejected her, she’s only ever really talked about you."
            s "Probably just a coincidence. I doubt Rin sees me as anything more than like, an older brother or father figure right now."

            scene harukarinreview30
            with dissolve

            h "Doesn’t mean she doesn’t want to try experimenting a little bit, though~"
            h "She’s a [teenage]girl. She’s curious. I was the same when I was her age."
            h "You really think she’s never entertained the thought of fooling around with the same guy who hangs out with her in her room all the time?"
            h "Come on, man. You know better than that."
            s "You’ve put a lot of thought into this, huh?"
            h "When you’ve got employees as cute as her, you sometimes can’t help but think about things like that."

        s "…"
        s "I’m starting to think you might be just as into [teenage]girls as me, Haruka."

        scene harukarinreview31
        with dissolve

        h "Me? Nooooo."
        h "I just staff my cafe with inexperienced, cute girls because they make the best employees."
        h "Of course I’m into them. Everyone loves cute girls, Sensei. Just because I’m a girl doesn’t mean I’m an exception to that."
        s "I mean, I’m all about this. But you should probably be careful acting on anything at the risk of getting sued one day."

        scene harukarinreview32
        with dissolve

        h "Oh, come on. I’m a degenerate but I’m not a bad person."

        if harukasex == True:
            "She says, despite actively cheating on her husband."

        h "It’s one thing for me to be attracted to girls like Rin or Molly-"
        s "Molly, too?"

        scene harukarinreview33
        with dissolve

        h "Or Rin’s friend Futaba."
        h "Or Molly’s friend...Tsuneyo, I think?"

        "Oh my God. She’s just as bad as me."

        h "But just {i}wanting{/i} to mess around with all of them doesn’t mean I actually {i}would{/i}, you know?"
        h "Unless they offered. Because in that case, I absolutely would."
        s "I’m glad we became friends, Haruka."
        s "I feel like our relationship has moved forward several steps today."
    else:
        h "You are right. I am being immature and not properly valuing our friendship."
        h "Will you ever forgive me."
        s "I forgive you right now. I understand that it is only human to act off of your emotions and that every one of us can be a little irrational from time to time."

    scene harukarinreview34
    with dissolve

    h "Then come hang out with me again soon. As friends."
    h "We’ll sit on my couch and I can show you some of the stuff I watch when I’m thinking about how lonely I am. "
    s "That sounds absolutely delightful."

    "Not."

    scene harukarinreview35
    with dissolve

    h "Sweet. Maybe I’ll invite Rin, too? Who knows?"
    s "You’re going to invite a [teenage]girl to your house to watch movies with you and another older guy?"
    s "Totally not suspicious at all."
    h "And hanging out in her dorm isn’t?"
    s "Touché."
    s "Oh well. Do whatever you want. "

    if bonus == True:
        h "If I do whatever I want, I’ll end up in jail. "
        h "I will exercise the same amount of restraint I always do, and the two of us will forget this conversation ever happened."
    else:
        h "Even if it means renting out a bounce house?"

    h "Deal?"
    s "Deal."

    if bonus == True:
        "No deal."
        "I can’t just forget finding out that Haruka is lusting after her entire cafe staff and...everyone her cafe staff knows and..."
        "Probably just everyone in general."
        "But I guess after going years without having sex, you start getting desperate."
        "To think Haruka would be permanently psychologically damaged by something like this, though..."
        "That’s just so sad."

    s "Well, I guess I’ll get out of your hair then."
    h "Sounds good. I need to start actually working again anyway."
    h "Call me soon, though. Got it?"
    s "Yup. "
    s "See you later, Haruka."
    h "Talk to you soon!"

    scene black
    with dissolve2

    "I exit the cafe without buying anything. "

    if bonus == True:
        "Not because I wasn’t thirsty, but because I’d inadvertently gotten an erection after finding out about Haruka’s hidden infatuation with [teenage]girls and didn’t want to scare any of the part-timers."
        "Eventually, the erection fades and I am free to get on with my day the way I normally do."
        "I’ll have to call Haruka some night in the near future and see if I can do anything else to quell that undying loneliness of hers."
    else:
        "I sure can be forgetful sometimes."

    $ renpy.end_replay()
    $ haruka_love += 1
    $ harukadate10 = True
    stop music fadeout 5.0

    "{i}Haruka’s affection has increased to [haruka_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label harukadate15:
...
```

## Code that triggers this event
File: \game\HarukaEvents.rpy
Code:
```python
...
label harukacafe:
    if haruka_love >= 5 and haruka_lust >= 5 and harukafirstlust == False:
        jump harukafirstlust
    if haruka_love >= 10 and halloween14 == True and harukadate5 == True and rindorm35 == True and harukadate10 == False:
        jump harukadate10
...
```