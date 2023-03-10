# A Trip to the Moon (Chika)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Event [Detention](./day139.md) (Chika) is completed)

* chikanumber equal to True (unknown variable)



## Next events

* [Main: The Value of Sharing](./halloween1.md)
* [Chika: First Hunt](./chikainvite2.md)

## Event properties

* Id: chikainvite1
* Group: Chika
* Triggered by label: chikainvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->chikainvite->chikainvite1

## Official wiki page

[A Trip to the Moon](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikainvite1&go=Go) for more details.

## Event code

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label chikainvite1:
    play sound "phonebeep.wav"

    "I tap on Chika’s name in my phone and wait for her to answer."
    "I’ve been thinking lately that it might be safe for her to come visit the house soon."

    if bonus == True:
        "Obviously, Ami might show some opposition to it, but would she really be skeptical of something going on between {i}Chika{/i} and me?"
        "Now that I think of it, I can’t even remember any situations where the two of them have talked to one another."
        "And that’s not to say I don’t think they’d get along or anything."
        "It’s just...a strange combination."
        "Ami probably doesn’t even realize that Chika and I are on {i}good terms{/i} with each other."

    if invitetip == False:
        call invitetip from _call_invitetip_1

    scene noonsky
    with dissolve
    play music "normalday.mp3"
    play sound "phonebeep.wav"

    c "Hihi~ What’s up, Sensei?"
    s "Hey. Do you have any plans tonight?"
    c "Tonight? Not really. I’m just hanging out in the dorm right now."
    c "Yumi’s with Chinami so I’ve got the night to myself."
    c "Which means I’m totally free if you wanna come over~"
    s "Actually, how would {i}you{/i} feel about coming over to my place?"

    if bonus == False:
        c "Do you have a chandelier?"
        s "No."
        c "Okay, good."
        s "What?"
        c "I just wanted to make sure."
    else:
        c "Ooooooh kinky~"
        s "Not like that. I think Ami is home."
        c "More kinky~"
        c "Wait, isn’t she your [niece]? That’s kind of fucked up."
        s "I’m not suggesting a threesome..."

        "Yet."

        s "I’m just saying come over and hang out. We can tell Ami you need to catch up on[school]-work you’ve missed from taking so many “bathroom” breaks."
        c "It’s too loud in class to watch all of my idol interviews and viral videos! Where else am I going to do it?!"

    s "Are you coming over or not?"
    c "Of course I am! "
    c "But isn’t Ami a little smarter than you’re letting on? Are you sure she won’t get the wrong idea or whatever?"
    s "I can’t even mention another girl without her getting the wrong idea, so she probably will."
    s "But maybe if we just act really casual about it, she won’t even notice?"
    c "Seems like wishful thinking to me...but I’m up for a little risk! I like her anyway."
    s "I didn’t realize you two were friends."
    c "We’re not."
    c "Yet!"
    c "See ya, Sensei~ Text me your address!"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "Chika hangs up the phone and I type out my address to her. "
    "I decide to give Ami a warning as well so that, if Chika manages to somehow get ready and make it to my place before me, she isn’t entirely too surprised."
    "………"
    "……"
    "…"

    scene chikafirstvisit1
    with dissolve

    a "Umm...would you mind explaining to me why both you {i}and{/i} Chika texted me about her coming over tonight?..."
    s "She texted you as well? I didn’t tell her to do that."
    a "She must have thought it was weird that her {i}teacher{/i} was inviting her to his house."
    s "Do you also think it’s weird, Ami?"

    scene chikafirstvisit2
    with dissolve

    a "Of course I do! You have me!"
    a "And why Chika of all people?!"
    s "You don’t have a problem with her, do you?"

    scene chikafirstvisit3
    with dissolve

    a "Well...no."
    a "She’s really nice and...popular and...pretty much everyone likes her now that I think about it."
    a "I just don’t understand why she’s coming to our house all of a sudden. I didn’t even know you two knew each other."
    s "Of course we know each other. She’s in the class."
    s "I could invite over pretty much anyone from there and it wouldn’t be {i}completely{/i} random."

    scene chikafirstvisit4
    with dissolve

    a "I don’t recall giving you permission to start inviting all of the other girls over, Sensei. "
    a "I don’t like this at all. Cancel your plans."

    play sound "doorbell.mp3"

    "The doorbell suddenly rings."

    a "…"
    s "Damn. If only you would have told me to cancel them a few minutes earlier."
    s "It would be rude to turn her away after she came all the way here, wouldn’t it?"
    a "I’ll tell her if you don’t want to."
    s "No need. Come on in, Chika!"

    "I ignore Ami’s suggestion and shout at the door to let Chika know that it’s [[mostly] safe for her to enter."

    play sound "dooropen.mp3"
    scene chikafirstvisit5
    with dissolve

    c "Hey! Long time, no see!"
    a "Yeah...hey."
    a "Thanks for...letting me know you were coming over? I think?"
    c "Well it would obvs be pretty weird if I were to just come over and hang out with your [uncle] without you at least knowing about it."
    c "But rest assured, I’m here for you just as much as I am for him."
    a "You are?"
    s "You are?..."

    scene chikafirstvisit6
    with dissolve

    c "Obviously! "
    c "Ami lives here too, so we’ve gotta include her in any conversation that you and I have together or she’ll get all dejected and left out and stuff."
    c "I appreciate all you do for me as a teacher, Sensei, but I don’t really think I’m comfortable being alone with you just yet."
    c "Not saying you think about me that way or anything, but you know what I mean."

    "Jesus. Someone give this girl an Oscar. "

    a "Hmm..."
    a "I was skeptical at first...but when she puts it like that, maybe this isn’t as weird as I thought?"
    a "Chika's obviously out of your league anyway. So I don’t know what I was even worried about in the first place."
    s "Wait, what?"

    scene chikafirstvisit7
    with dissolve

    c "Aww come on...don’t flatter me like that. I don’t even have a league."
    c "I’m just regular old Chika. "
    a "Don’t be so humble. You’re out of everyone’s league."
    a "You shouldn’t even waste your time talking to someone like Sensei when there are zillions of other boys who’d be much better for you."
    a "Well, at least there were until the space war. I guess your options are a bit more limited now."
    a "Still better than Sensei, though."
    s "You do realize I’m right here, don’t you?"

    scene chikafirstvisit8
    with dissolve

    a "Of course!"

    "Chika flashes me a look that seems to be a cross of “I’m so sorry” and “There’s no way I agree with her,” but the looming thought of being underappreciated by my very own [niece] eats away at me."

    scene chikafirstvisit9
    with dissolve

    c "So...now what?"
    a "Yes, now what?"
    a "Since I’m apparently needed in order for this little hang-out session, may I offer a suggestion?"
    s "Sure. Even though you just insulted me in front of a guest."

    "It’s not like I had a plan in mind for this evening anyway. I’m just glad I was able to get Chika inside without much resistance."
    "But I guess that’s one of the benefits to her being liked by pretty much everyone."
    "And also apparently one of the bright sides to being “out of her league...”"

    a "How about we show Chika the best part of our house?"

    if bonus == True:
        s "You mean my bed?"
    else:
        s "The chandelier?"
        c "You lied to me."

    scene chikafirstvisit10
    with dissolve

    if bonus == True:
        a "No! I don’t mean your stupid bed!"
    else:
        a "No! Not the chandelier!"

    a "I mean our TV! The one that we watch movies on all the time!"

    if bonus == True:
        s "I like my bed a little more than the TV."
        a "You’re not showing Chika your bed!"
        c "Hahaha...I’m...fine with TV..."
        c "My legs are kind of tired from walking all the way here and whatnot anyway."
    else:
        s "Oh, that."
        c "Thank God."

    scene black
    with dissolve

    "Ami shoots me one final death glare before moving to the living room and taking her place on the couch."
    "Chika sits on the opposite end, leaving the space in the middle completely unoccupied."
    "Before Ami is able to slide over and prevent me from sitting directly next to Chika, I manage to find my place between the two of them."

    scene chikafirstvisit11
    with dissolve

    c "Wow! This is so much bigger than the one at my place!"
    c "You can even hear it without having to turn the volume all the way up!"
    a "The glories of surround-sound."
    c "I thought surround-sound was something only rich people could afford."

    scene chikafirstvisit12
    with dissolve

    c "Are you guys really that well off, Sensei?"
    s "Not particularly. I don’t even remember what all of this cost us."

    "Mostly due to the fact that I’m not technically the one who paid for everything."
    "Well, I guess...technically, I {i}am{/i}."
    "But a different...me. Or something."
    "Wait, why am I thinking about the cost of our entertainment set-up when I’m sandwiched between two cute [teenager]s?"

    a "Sensei and I used to spend almost every day on this couch."
    a "But now that I’m getting older, he’s losing interest in me and inviting other girls over to the house instead."
    c "You need to cherish your family, Sensei. You never know when something bad might happen to them."

    scene chikafirstvisit13
    with dissolve

    a "Listen to your guest, Sensei. Cherish me more! Buy me things!"
    s "Who invited you here, Ami?"
    a "Chika did! You’re not insinuating that {i}your{/i} guest might have made some sort of mistake, are you?"
    s "That’s exactly what I’m insinuating. Go to your room."

    scene chikafirstvisit14
    with dissolve

    a "Mmm!"
    c "Now, now...I didn’t mean to stir up any trouble between you two. I just think things like this are more fun when everyone can enjoy them together."

    scene chikafirstvisit15
    with dissolve

    c "I kind of wish my little sister could be here to experience this today."

    "The wording of that sentence makes it sound as if Chinami is dead. What a horrible thought."

    c "The only family I really have left is her and Yumi."

    "Chinami lives again. What a joyous occasion."

    a "My only family is Sensei, so I can relate to that..."
    a "I didn’t know you had a sister, Chika. All this time I thought you were an only child."
    c "Two sisters if you count Yumi. "
    c "She’s independent, but I feel like she’s even more of a kid than my actual little sister at times."
    s "If Chinami ever starts talking like Yumi, though, I’m never coming over again."

    scene chikafirstvisit16
    with dissolve

    a "Wait! Coming over?!"
    a "You’ve been to Chika’s house?!"
    a "You met her sister?!"
    a "What else are you hiding from me, bastard-[uncle]?!"
    c "Ah- Nononononono, you’ve got it all wrong! Sensei’s never come to my house before."
    c "He meant...coming to the mall! The store I work at! I bring my sister with me sometimes when I can’t find a babysitter!"

    scene chikafirstvisit17
    with dissolve

    a "Wait just a second..."
    a "Little sister..."
    a "Mall..."
    a "Does she perhaps...wear a funny-looking...dog mask?"
    c "Hahaha...yeah...that’s...a thing she does..."
    s "I was beginning to think you were never going to bring up that incident."
    a "Up until now, I’d been pretending it was all some strange delusion due to lack of sleep."
    a "Something about this story doesn’t add up, though."
    c "What?...What could possibly not add up about...this?..."

    scene chikafirstvisit18
    with dissolve

    a "If you two don’t normally spend time alone together...why are you going to visit her at the mall?"
    a "And why are you watching her little sister while she works?"
    a "Just how close are you two?"
    c "Umm...uhh..."
    s "I have a passion for luxury clothing."

    scene chikafirstvisit19
    with dissolve

    c "Y-Yes! That’s exactly it!"
    c "Sensei is a regular customer! The only times I ever see him are at[school] and work, though..."
    c "He’s never invited me to the house before, so I wouldn’t have really felt comfortable unless you were here as well, Ami!"
    a "If you’re so passionate about luxury clothes, how come you wear that same stupid blazer every day?"
    s "Stupid?"
    c "He’s...saving up money to take you on a trip!"

    scene chikafirstvisit20
    with dissolve

    a "A trip? Really? "
    a "Where are we going?"
    s "…"
    c "The...moon!"
    a "We’re going to...the moon?"
    s "…"
    s "Yes."

    "Really, Chika? The moon?"
    "Couldn’t you have at least named somewhere on this planet?"
    "How much money am I going to need to save up now?"
    "I can feel my fake passion for luxury clothing diminishing by the moment."

    a "I...don’t know if I want to go to the moon, though."
    a "That seems like it would take a really long time."
    s "Damn. I guess I’ll need to cancel our plans then."

    scene chikafirstvisit21
    with dissolve

    a "Well...I mean...I {i}would{/i} get to be alone with you...so maybe it wouldn’t be all that bad in the end."
    s "Too late. I’ve already cancelled the trip."

    scene chikafirstvisit22
    with dissolve

    a "What?! Already?! But I changed my mind!"
    a "I want to go to the moon!"
    c "Hahaha...hahah..."
    c "Hah..."

    scene chikafirstvisit23
    with dissolve

    a "Mmm..."
    s "..."
    c "..."
    s "{i}The moon? Really?{/i}"
    c "{i}It was all I could think of on such short notice.{/i}"
    s "{i}How were you so good at lying up until that part?{/i}"
    c "{i}I had a script in my head. The trip part was all improv.{/i}"
    s "{i}Was it really? I had absolutely no idea.{/i}"

    if bonus == True:
        scene chikafirstvisit24
        with dissolve

        c "{i}I’ll make it up to you...kay?{/i}"
        c "{i}Invite me over again when Ami isn’t home and you’ll see~{/i}"

    scene chikafirstvisit25
    with dissolve

    a "Hey...what are you two whispering about over there?"
    c "W-Whispering? No one’s whispering! We were sitting here in silence!"
    s "I think we need to take you to a psychiatrist, Ami. You appear to be hearing things."
    a "No! You appear to be {i}hiding{/i} things!"
    a "Tell me what you were whispering about!"

    scene black
    with dissolve2

    "Obviously, we never tell Ami what we were whispering about."
    "It takes her roughly fifteen minutes to give up on asking."
    "Within that time, Chika and I mutually decide that it might be best if she heads back to the dorm early today."
    "I feel a little bad for having her come all the way here just to leave shortly after, but I guess things like that can’t be avoided at times."
    "I’ll just need to make sure Ami isn’t around the next time I invite Chika over so we don’t have to go through something like this again..."

    $ renpy.end_replay()
    $ chikainvite1 = True
    $ chika_love += 3
    stop music fadeout 5.0

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label chikainvite2:
...
```

## Code that triggers this event

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label chikainvite:
    if chikainvite1 == False:
        jump chikainvite1
...
```