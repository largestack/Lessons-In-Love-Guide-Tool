# Names of Our Children
Ayane event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dojo10&go=Go)



## Event preconditions
✅Ayane love greater than or equal to 10



## Next events
* [Ayane: Imprinting](./ayanenew1.md)

## Event properties
* ID: dojo10
* Group: Ayane
* Triggered by label: dojo
* Triggered by branch label: dojo

## Event code
File: \game\AyaneEvents.rpy
Code:
```python
...
label dojo10:
    scene namesredux1
    with dissolve
    play music "lifeismostlygood.mp3"

    "I begin to make my way to the dojo because I have lost all control over my life and am slowly falling into the clutches of a rich blonde girl."
    "But hey, she's cute and she likes me- which is really way more than I should be asking for in the first place."
    "So if going along with her weird roleplay stuff is all I have to do to get closer to her, I'm absolutely going to do that."
    "Would she continue falling for me even if I decided to {i}not{/i} do things like that with her? Probably."
    "But I want her to fall faster."
    "And me looking like an idiot is a small price to pay for getting an attractive teenager's pants off."

    scene namesredux2
    with dissolve

    ay "Oh, Sensei! What are you up to?"

    "Or dress, I suppose."

    s "I was actually just on my way to the dojo. Are you heading there now?"

    scene namesredux3
    with dissolve

    ay "Actually...I'm coming {i}back{/i} from the dojo right now..."
    s "Don't tell me you actually got kicked out?"
    s "Was it the giant fan? The guns? Never listening to the instructor? Ordering pizza in the middle of lessons? Riding a-"
    ay "I get it. I like to have fun."
    ay "But no, I wasn't kicked out. The dojo is just closed for the day- which is a real bummer since I was in the mood to actually practice for {i}real{/i} this time."
    s "Yeah, I'm not buying that."

    scene namesredux4
    with dissolve

    ay "I mean it! I was feeling really fired up today!"
    ay "And just so you know, until you started showing up all the time, I really {i}was{/i} giving it my all!"
    ay "It's just a lot harder to focus on things when you're there. I blame your sweatpants."
    s "My sweatpants?..."

    scene namesredux5
    with dissolve

    ay "Yeah. Don't you feel the same way about girls in pajamas? Like, they'd just be so easy to just slip off and..."
    s "...and what?"
    ay "I can't finish that sentence because there is a woman pushing a stroller behind you and I don't want to taint the poor baby's ears with all of the impure thoughts I have."
    s "How are you able to maintain friendships when it seems like the only thing you have on your mind at all times is me?"

    scene namesredux6
    with dissolve

    ay "Mmm...I guess it probably helps that my best friend is the only other person in this city who can compete with me in terms of how much we love you."
    s "You need new hobbies."

    scene namesredux7
    with dissolve

    ay "Sorry, my only other hobby closed down for the day, so you're going to have to deal with me just talking about how much I love you for the rest of the afternoon."
    ay "Have I mentioned lately that I love you? Because I love you."
    s "I had no idea. You hide it so well."
    ay "Not as well as you hide your freakishly huge penis behind those old sweatpants in karate class."
    s "..."

    scene namesredux2
    with dissolve

    ay "Do you have a bucket of cold water you could dump on my head? That's what Maya always does when I start rambling on about you and I think it would come in handy right now."
    s "I don't, no..."

    "It never ceases to amaze me how open Ayane is about her feelings for me..."

    if bonus == True:
        "I really don’t get it, to be honest."
        "I'm not particularly attractive or...interesting..."
        "I'm not even fun."
        "I'm just...there."
        "But...maybe that's exactly {i}why{/i} she likes me?"
        "Because I'm the only man she's in regular contact with- and one that she's apparently been around for years."
        "How far back do these feelings go?"
        "And what sorts of feelings were locked away inside of {i}this{/i} body before I was granted the opportunity to take over?"

        play sound "static.mp3"
        scene namesredux8 with flash
        stop sound
        stop music

        "{s}NONE{/s}"

        play sound "static.mp3"
        scene namesredux2 with flash
        stop sound
        play music "lifeismostlygood.mp3"
    else:
        "I really wish she'd just accept me as her teacher and not constantly drop hints about a deeper type of relationship when I do not intend to ever have something like that with her."
        "Girls are gross."

    s "Well anyway, since we can’t do anything at the dojo, did you want to hang out around here?"

    scene namesredux9
    with dissolve

    ay "Like...around here? But what if people see us?"

    if bonus == True:
        s "Weren't you ranting about my penis to a mysterious woman like, thirty seconds ago?"
        ay "No, I was ranting about the layer of suspiciously provocative fabric that {i}conceals{/i} your penis. It's totally different."
        s "Either way, it’s not like we’ll be holding hands or making out or anything. It's not a big deal if people see us together in the middle of the day."

        scene namesredux10
        with dissolve

        ay "Darn it...I thought you were asking me on a date for a second."
        s "You can call it a date if you want. I’m just not a fan of the idea of publicly displaying affection."

        "Let alone publicly displaying affection with a girl young enough to be my daughter."

        scene namesredux9
        with dissolve

        ay "I figured as much. Even with Ami, you've never really liked showing affection in public. Or...really anything, for that matter."
        ay "You know, it's weird. I'm never really a fan of the mysterious type in manga...but with you, I kind of can't really imagine anything else."
        s "I'm going to take your undying love for me as an {i}okay{/i} and assume that you're fine with hanging out around here."

        scene namesredux2
        with dissolve

        ay "Sensei, you literally never have to ask me if I'm okay with anything. {i}Especially{/i} if that thing is spending time with you."
        ay "I'm just not really sure what you want to do. I've never gone on a not-date that I'm still allowed to call a date before. Let alone one with my best friend's uncle and teacher."
        s "Then I guess we can just...start off small and go for a walk or...sit on a bench and talk or something? Preferably {i}not{/i} about the type of pants I wear at the dojo."
        ay "Good call, Sensei. If there's anything I've learned from my butler, it's that you never want to get horny on a park bench."
        s "..."
        ay "..."
        ay "What?"
    else:
        s "Then we will kill them."

    scene black
    with dissolve2

    s "Nothing, Ayane."
    s "Just thinking about how I wound up here."

    "The two of us do a few laps around the block, not straying far at all from where we met up, before taking a seat on a bench near the subway station."

    scene ayanestreet1
    with dissolve

    "Ayane moves as close to me as she can without making it look like we're the world's least appropriate couple."
    "The chaotic horny energy that was radiating off of her a few minutes ago has since been replaced by an aura of adoration that painfully perforates my nostrils and lures me into a false sense of security."
    "I do not feel insecure in believing that this girl will change at the drop of a hat- but in the fact that inching closer to comfort somehow makes me less comfortable than anything else I can think of."

    ay "So, now what? Want to talk about holding hands since we're not actually allowed to do it?"
    s "I can't imagine that conversation topic lasting very long."
    ay "Then pick a better one. You're the leader of this not-date and I'm just a girl who's really thirsty for some good old-fashioned handholding."
    s "Tone it down, Ayane. Who knows what would happen to us if someone overheard you saying something as taboo as {i}that.{/i}"

    scene ayanestreet2
    with dissolve

    ay "Good point! We should talk about more socially accepted topics like the current political climate or...whether or not pineapple belongs on pizza."
    s "It doesn't."
    ay "Well, of course {i}I{/i} know that and {i}you{/i} know that, but there could be people who don't know any better walking past us and it's up to us as a responsible not-couple to not offend them."
    s "Are you sure you're okay with this, Ayane?"

    scene ayanestreet3
    with dissolve

    ay "Hm? What do you mean?"
    s "I mean, obviously I'm okay hanging out with you like this since I'm the one who asked. But the more you talk, the more I feel like you should be off bantering with someone a little better at bantering back."
    ay "But I don't want to banter with anybody else. If I did, I wouldn't have agreed to not-date you today."
    s "I guess I just don't want the not-date to be too boring for you."

    "That and I'm feeling an overwhelming difficulty being near her without capitalizing on her raging (Yet temporarily dormant) hormones."

    ay "I'm not bored at all, Sensei. I'm having tons of fun."
    ay "And it's not like I’ve ever been on a real date before, so there's no bar you need to pass or anything."

    scene ayanestreet4
    with dissolve

    s "Really? Not even once?"
    ay "Not even once."
    s "Why not?"
    ay "Because you never asked me."
    s "You make it sound like you've been saving yourself for me or something."

    scene ayanestreet5
    with dissolve

    ay "You make it sound like that's a bad thing {i}or something.{/i}"
    s "I mean, it kind of is. What if nothing ever came of it? Would you have just...gone on forever? Indefinitely waiting for me?"
    ay "Of course not, Sensei."
    s "That’s a relief. Because for a second I thought-"

    scene ayanestreet6
    with dissolve

    ay "I made a promise to myself a long time ago...that if you didn’t reciprocate my love by the time I graduate high school..."
    ay "That I would blow up the city..."
    s "..."
    ay "..."

    scene ayanestreet7
    with dissolve

    s "..."
    ay "..."

    scene ayanestreet8
    with dissolve

    ay "So, Sensei, when we get married...what are we going to name our kids?"
    ay "I really like the name Ami, but that one’s kind of already taken, so..."
    ay "Do you think Ami would be okay with changing her name if we asked her really nicely?"
    s "…"

    scene ayanestreet9
    with dissolve

    ay "Of course, there are also names like Airi or...Ayaka...or Ai..."
    ay "Or maybe Aki if we wind up having a boy first."
    ay "I like A-Names if you couldn’t tell. Like Ayane!"
    s "…"

    scene ayanestreet8
    with dissolve

    if bonus == True:
        ay "I’ve been thinking about it a lot and I’m pretty sure I want seven children if that’s okay with you."
    else:
        ay "I’ve been thinking about it a lot and I’m pretty sure I want to adopt if that’s okay with you."
        s "Oh, cool. That makes this event significantly cleaner and saves the writer from further censoring the dialogue."

    ay "I was actually telling Ami that the other day and-"

    scene ayanestreet9
    with dissolve

    ay "Oh, sorry. {i}Your{/i} Ami, not {i}our{/i} Ami. Our Ami hasn’t been born yet."
    s "…"
    ay "Anyway, I was telling her that I want seven kids with you and she was all like ‘What are you planning on doing to my [uncle]!?’"

    scene ayanestreet8
    with dissolve

    ay "And I had to be all like, ‘Nothing!’ and-"
    s "..."
    ay "..."

    scene ayanestreet10
    with dissolve

    ay "I’m a bad date, aren’t I?"
    s "What? No, that’s not it."
    s "I just don’t think I’m ready to talk about children and marriage and all that just yet..."
    ay "Is it...because you can't imagine a future with me?"
    s "I think it's more that people are...you know...sexually involved with one another before the topic of kids comes up."

    "And also the fact that I can't imagine myself ever wanting {i}any{/i} children."

    ay "I mean...I guess that makes sense."
    s "Sex is kind of required to make children, so yeah. I think it's safe to say it makes sense."
    ay "Am I wrong for daydreaming, though?"
    s "I wouldn't say {i}wrong...{/i}But I'd also maybe think a little harder before sharing some of those daydreams with people."

    scene ayanestreet11
    with dissolve

    ay "Yeah..."
    ay "Yeah, I can...get ahead of myself at times. I know."
    ay "It's just a...unique challenge to have parts of your fantasy start to come true while the other parts are forced to sit on the sidelines and wait for their turn."
    ay "I guess I'm just not great at dealing with that yet."
    ay "But I'll get better. For your sake {i}and{/i} my sake."
    ay "I don't want this to be some sort of...temporary thing, you know? I'm really serious about this, Sensei."
    s "You're-"
    ay "And before you go and say something like {i}You're just a teenager{/i} or {i}you have your whole life ahead of you{/i} I'd like an opportunity to counter."
    s "It's not really a counter unless an opposing point has been made first."
    ay "Yeah, well I've prepared myself for any opposing point you can possibly come up with-"

    scene ayanestreet12
    with dissolve
    stop music fadeout 5.0

    ay "And my counter is this..."
    s "..."
    ay "..."

    "Ayane stares deep into my eyes and I can tell that whatever she's about to say has had not months, but years of time poured into it."
    "I can only imagine how hard it must be to incessantly agonize over whether or not your dreams are achievable."
    "And with hers so close, yet so far away..."
    "These words will have to move mountains."
    "But I am no normal mountain. I am-"

    ay "I want to wake up next to those sweatpants every day for the rest of my life."
    s "..."
    ay "..."

    scene ayanestreet12r
    with dissolve
    play music "lifeismostlygood.mp3"

    s "Hah..."
    ay "I had you concerned there, didn't I?"
    ay "To be totally honest, I {i}did{/i} have a really cute, really sweet thing I was going to say- but I figured that now probably isn't the time and, well, I'm still kind of regretting not being able to do karate with you today."
    s "Well, you're definitely right. Now was most certainly not the time."
    s "Save any huge bombshells about the future of our relationship for at least a few more not-dates. {i}Then{/i} you can consider dropping them on me."
    ay "Sensei, I am going to drop so many bombshells on you that-"
    s "I'm going to cut you off right there as I can't imagine {i}any{/i} possible way for that joke to not end extremely offensively."

    scene ayanestreet13
    with dissolve

    ay "See, this is why I love you! You've been looking out for me for as long as we've known each other."
    ay "So if I can look out for you for even a fraction of that...it'll be everything I've ever wanted."
    ay "Well, almost everything."
    ay "I have several fantasies I will require your assistance in living out, but I think they would be considered bombshells, so I'll keep them to myself for now."
    s "I mean...I'd be fine with you sharing {i}those{/i} ones if-"
    ay "Nope. You made your bed and- now you have to put on your sexy sweatpants and lay in it."
    s "Okay, this date is over now."

    scene black
    with dissolve2

    ay "Woo! Best date ever! I didn't even have to use my hand grenade!"
    s "You don't have a grenade, Ayane."
    ay "That's what you think, Sensei!"
    s "Why do I feel like I understand less about you every time the two of us talk?"

    "Ayane and I leave the bench after another few minutes and make our way back to the dorms. "
    "She locks me in a bear hug for a good thirty seconds as she says goodbye and I go to pat her on the head, but have to stop myself as I don't think she's earned it quite yet."
    "Despite her mild insanity, though, she really is cute at times."
    "That cuteness just normally vanishes whenever I'm reminded that her handbag is filled with things that could get us killed."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ dojo10 = True

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"

    jump saturdaynight

label dojo20:
...
```

## Code that triggers this event
File: \game\AyaneEvents.rpy
Code:
```python
...
label dojo:
    if ayane_love >= 0 and firsttimedojo == False:
        jump firsttimedojo
    if ayane_love >= 5 and dojo5 == False:
        jump dojo5
    if ayane_love >= 10 and dojo10 == False:
        jump dojo10
...
```