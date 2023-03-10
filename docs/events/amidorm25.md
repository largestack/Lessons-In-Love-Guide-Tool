# Everlasting Love (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ami love greater than or equal to 25

* Event [Divergence](./amidorm20.md) (Ami) is completed)

* Day of week is not Friday



## Next events

* [Main: As Loud as a Whisper Can Be](./day214.md)

## Event properties

* Id: amidorm25
* Group: Ami
* Triggered by label: amidorm
* Triggered by branch label: amidorm
* Triggered by path: amidorm->amidorm25

## Official wiki page

[Everlasting Love](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amidorm25&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label amidorm25:
    play sound "knock.mp3"
    stop music fadeout 10.0

    "I knock on Ami’s door and immediately hear some shuffling from behind it as she hops off of her bed."

    a "Come in! It’s open."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I’m not sure why she needs to hop off of the bed if she’s just going to have me let myself in, but it doesn’t really matter I guess."
    "After all, I’m-"

    scene amiclingy1
    with hpunch
    play music "love.mp3"

    a "Attack-hug!"

    "Ami wraps her arms around me and squeezes with every ounce of strength that her small and unsurprisingly weak body is able to muster."

    s "Why the attack-hug?"
    a "Because I missed you."
    s "Oh."
    s "Well, hi."
    a "Hi."
    a "I love you."
    s "You’re being unusually clingy right now. Is something wrong?"
    a "Does something have to be wrong for me to want to hug you?"
    s "No, but that’s kind of dodging the question, isn’t it?"

    scene amiclingy2
    with dissolve

    a "Nothing’s wrong. I was just thinking about some stuff."

    scene amiclingy3
    with dissolve

    a "Oh! I forgot to tell you!"
    a "Uta says I can start at the maid cafe soon!"
    a "I met up with her earlier and she was teaching me how to talk to customers and stuff."
    a "I told her that I deal with you all the time, so the training wasn’t like suuuuuuper necessary, but it still helped I think."
    s "I can’t imagine I’m particularly difficult to “deal with.”"

    scene amiclingy4
    with dissolve

    a "You’re not~ It’s almost like you’re going to be an actual adult soon."
    a "They grow up so fast, don’t they?"
    s "I did not come here to be ridiculed."
    a "I know. You came here to let me cuddle with you."
    s "That is closer to the reason I am here, yes."
    a "I believe this calls for a journey to the couch then, doesn’t it?"
    a "As much as I like attack-hugs, this room’s prime cuddling location is a little bit closer to the wall."
    s "Why not the bed then?"

    scene amiclingy5
    with dissolve

    if ami_virgin == False:
        if bonus == True:
            a "Because if we’re on the bed, you’ll take my pants off and then I’ll take your pants off and it’ll be a whole thing."
            s "I don’t see how this is a problem."
        else:
            a "Because that would be inappropriate."
            s "You are right. What was I thinking?"

    else:
        if bonus == True:
            a "Are you inviting your [niece] into bed right now? Aren’t you supposed to be a good [uncle], Sensei?"
            a "Cuddling in bed with a girl my age is forbidden-love territory. "
            a "And while I’m not really against it, I don’t think you’ve seemed particularly up for it as of late."

            "Ami brings up a good point. "
            "The last time we were in bed together, I kind of...let her down when I feel like she was expecting me to take advantage of her."
        else:
            a "Because that would be inappropriate."
            s "You are right. What was I thinking?"

        s "You’re right. We should probably just sit on the couch then."

        if bonus == True:
            s "Sorry for suggesting something that would get your hopes up."
            a "It’s unfair to bring my hopes into this. Besides..."

    scene amiclingy6
    with dissolve

    a "Maya is going to be home soon anyway...and she’s always saying stuff about how you and I are a little too close."

    scene amiclingy4
    with dissolve

    a "I think she might be jealous~"
    s "Because of me? Yeah, I definitely don’t think Maya is jealous that you get to be this close to me."
    a "Nonono, I mean she’s jealous that {i}you{/i} get to be so close to {i}me{/i}. "
    a "Have you even noticed how adorable I am? It’s not my fault if my roommate winds up falling in love with me."

    if bonus == True:
        a "I’ll just have to tell her my heart belongs to someone else. And that person may or may not be the same person who’s helped raise me since I was a little girl."
        s "You still kind of {i}are{/i} a little girl, Ami."

        scene amiclingy7
        with dissolve

        a "Heheh~ You’re right."
        a "I’m {i}your{/i} little girl."
        a "Now come on. Cuddle with me on the couch for a little while."
    else:
        s "As long as it is her and not me. I refuse to ever fall in love because I do not think I would make an adequate partner."

    scene black
    with dissolve

    "I go to move toward the couch but Ami refuses to loosen her grip on me, causing me to forcefully drag her over there as I attempt to walk both of us."
    "Ami might be light, but she feels a lot heavier when she’s standing on my feet."
    "I almost knock her over a few times (One of which was intentional because I thought it might be funny), but we ultimately make it to the sofa and she quickly curls up against me."

    scene amiclingy8
    with dissolve

    a "I always forget how big you are until I look at you from the side."
    s "I’m pretty sure I’m the same height no matter which direction you look at me from."
    a "Obviously. But when you face away from me like that and wrap your arm around me, I feel tiny enough to just kinda like, absorb into your skin and stuff."
    s "Please don’t. If I absorb you, you won’t be able to cook for me anymore."
    a "I won’t be able to hug you either. But I guess the absorby thing would be kinda like a permanent hug."
    a "A permanent hug sounds good. Maybe you should absorb me after all?"
    s "I think you’ll be fine just staying like this."

    scene amiclingy9
    with dissolve

    a "Hehe~ Yeah...just this is perfect."

    "We proceed to sit in silence for a suspicious amount of time."
    "Ami’s normally the one to lead the two of us in conversation, but something about the way she’s acting tonight makes her feel a little different than normal."
    "I don’t think anything is wrong. She normally makes her moods very apparent. "
    "And I mean {i}very{/i} apparent."
    "At this point, I can normally tell how she’s feeling by just paying attention to the inflection of her voice or the volume she’s speaking at."
    "It’s one of the many things I like about her."
    "People that are hard to read are annoying. "
    "I’m glad I didn’t wind up with a [niece] like Maya."
    "I doubt she’d even cook for me in the morning."

    a "…"
    s "…"

    "Ami tries a little harder to reach her arm across the length of my back, but it’s not long enough."
    "She resorts to softly rubbing it instead, like she’s trying to calm down a child or something along those lines."
    "It’s not a particularly enjoyable feeling, but I know she’s doing it out of affection so I let her proceed."

    s "Is there anything you want to talk about? You mentioned starting at the maid cafe soon, right?"
    s "Are you excited to not have to bother me about money anymore?"

    scene amiclingy10
    with dissolve

    a "A little bit. I just figured it was time to try something different."
    a "I’m kind of nervous, though. Like, I was ready to devote my entire life to just doing everything that you need whenever you need it."
    a "But the more time we spend together, the less I feel like you actually {i}need{/i} me."
    s "But who would-"
    a "I’m not talking about cooking and cleaning and all of that house-wifey stuff. I’m talking about like...{i}needing me{/i}, needing me."

    scene amiclingy11
    with dissolve

    a "I didn’t think you’d be willing to let me go so easily when the job thing came up. "
    a "And yeah it hurt my feelings for a little while, but if there’s anything I’ve learned over the years it’s that growing up can be kinda hard at times."
    a "So if this is what you think I’ve gotta do to become the type of girl you want me to be...{i}which is apparently a maid{/i}...I’ll try it out."
    s "..."
    s "This was never just about money at all, was it?"

    scene amiclingy8
    with dissolve

    a "Nope! Just a last-stitch effort to get you to admit how much you need me."
    s "Last {i}ditch{/i} effort. Not stitch."

    scene amiclingy12
    with dissolve

    a "Wait, what? Why? That doesn’t make any sense."
    a "I thought it was stitch because like, you know, you get to the last stitch of something when you’re sewing it and stuff."
    s "I think it’s a war reference. Like when soldiers only had one last ditch to hide in before running out into the open and getting their brains blown out."

    scene amiclingy13
    with dissolve

    a "Ew. What kind of creepy [uncle] talks about peoples’ brains getting blown out while he’s cuddling with his [niece]?"
    s "What kind of [niece] tricks her [uncle] into supporting her efforts to get a job because she can’t realize how important she is to him?"

    scene amiclingy14
    with dissolve2

    a "…"

    "Okay, fine."
    "I genuinely care about Ami."
    "For real."
    "There you go."
    "It’s kind of hard not to when I spend almost half of this strange excuse for a life inside the same set of walls as her."
    "But that’s one of the reasons why I don’t think it’s particularly harmful for her to spend some time doing...other stuff every now and then."
    "Just expecting her to sit around catering to me every second of every day is an unrealistic expectation."
    "And even if nothing about this world is real-"
    "Even if nothing is real in general, we can at least pretend it is."
    "Can’t we?"

    a "That was really cute..."
    s "Shut up. Don’t call my words cute. I’m the picture of a cool and mysterious [uncle]."

    scene amiclingy15
    with dissolve

    a "You know, a lot of girls think the coolest thing a boy can do is all of that caring and affectionate stuff. "
    a "Say more nice things about me. Go."

    if bonus == True:
        s "I like how flat your chest is."
    else:
        s "I think it's cute how frequently you misdocument my annual income."

    scene amiclingy16
    with dissolve

    a "Wha- That’s the opposite of nice!"

    if bonus == True:
        a "I’m self conscious about that part of me and you know it! Even if you’re into girls with smaller boobs!"

        scene amiclingy17
        with dissolve

        a "First you kick me out of the house and tell me to get a job. Now you’re saying I have stupid boobs. You hate me, don’t you?"
        s "Neither of those things happened. And no. I do not hate you."
        a "Then sleep over and prove it to me."
        s "Didn’t you just say a little while ago that Maya was coming home? She’d kill both of us in our sleep."
    else:
        a "It makes me want to die!"
        s "Don't do that. I don't know any other accountants and Maya's firm is not open yet."

    scene amiclingy18
    with dissolve

    a "I am prepared to die as long as I can die next to you."
    a "It would be a romantic ending to this everlasting love."
    s "…"
    a "…"

    scene amiclingy19
    with dissolve

    s "…"
    s "I don’t really want to die tonight."
    a "If you leave here I’ll kill you."
    s "So my choices are be killed by my [niece] or be killed by my [niece]’s best friend?"

    scene amiclingy20
    with dissolve

    a "Which one will it be, Sensei?"
    s "I choose life."
    a "…"
    s "…"
    a "That wasn’t one of the options. "
    a "Besides, don’t you wanna sit around and look at cute winter outfits on my phone with me?"
    a "Since I’m finally going to be able to buy clothes, I might as well prepare myself for the change of seasons, right?"
    a "It’s been getting colder lately and I don’t wanna get hydrothermopoly or whatever that “Holy heck, I’m so cold” disease is."
    s "That would be hypothermia. "
    a "Yeah, that. I don’t want that."
    a "So either help me pick out clothes or resign yourself to an entire season of hugging me and carrying me around like a baby."
    s "Why don’t we just go back to the mall sometime and I can help you choose there?"

    scene amiclingy21
    with dissolve

    a "So you’re fine with going to the mall with me as long as I’m paying?"
    s "I need to be responsible with my money or we’ll wind up having to go the entire winter without heat."

    if mall20 == True:
        "I’m also kind of paying for five peoples’ phone bills too, so...I kind of need to save whenever possible."

    scene amiclingy22
    with dissolve

    a "Well, it’s not like I’m gonna say no to a day-trip with you."
    a "Do you think Maya could come with us, though? I kinda promised her that I wouldn’t buy any wintery stuff without at least showing her first so the two of us can match."
    s "That’s such a [teenage]girl thing to do."
    a "Well, we {i}are{/i} [teenage]girls, so...yeah. It kind of is."

    scene black
    with dissolve2

    "I get off the couch and Ami follows me to the door."

    scene amiclingy23
    with dissolve

    a "You sure you don’t wanna stay?"
    s "It’s less that I don’t want to and more that I should head back before Maya finds out I’ve been in the room again."
    a "But what if this is the last time we ever see each other?"
    s "Why on earth would this ever be the last time we see each other?"
    a "I don’t know. What if the world just randomly blows up or everyone disappears all of a sudden?"
    a "How would you feel knowing you left your [niece] scared and alone in the middle of the apocalypse?"
    s "You won’t be alone, you’ll have Maya."

    scene amiclingy24
    with dissolve

    a "I love Maya but I don’t really think she’s ‘end of the world’ material."
    s "You’d be surprised."
    s "But anyway, I’m going to get out of here. Want me to call you when I get home so you can confirm I wasn’t stabbed to death along the way?"

    scene amiclingy25
    with dissolve

    a "Yes please. I wouldn’t be able to sleep at night unless I received that exact confirmation."
    s "Will do."
    s "Goodnight, Ami."
    a "Goodnight, Sensei~"

    scene black
    with dissolve2
    stop music fadeout 6.0
    play sound "dooropen.mp3"

    "I can feel Ami’s gaze remain on my back as I walk away from the dorm."
    "She doesn’t follow me to the hall, but stands in the doorway watching me leave. Probably to make sure I don’t get stabbed on my way down the stairs, I guess."
    "I don’t know. She’s a weird girl."
    "But she’s {i}my{/i} weird girl."
    "Or at least she is now."
    "So that’s just something I’m going to have to deal with."
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ amidorm25 = True
    $ ami_love += 1

    "{i}Ami’s affection has increased to xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx{/i}"
    "///////////////////////???????????????"

    play sound "static.mp3"
    scene amibreak1
    with flash
    scene amibreak2
    with flash
    scene amibreak3
    with flash
    scene amibreak5
    with flash
    scene amispecial1
    with flash

    a "…"
    a "…"
    a "…"
    a "…"
    a "…"
    a "…"
    a "…"
    a "…"
    a "…"

    play sound "static.mp3"
    scene amispecial2
    with flash
    stop sound

    a "…"
    a "…"

    play sound "static.mp3"
    scene amispecial3
    with flash
    stop sound

    a "…"
    a "…"
    a "…"

    play sound "static.mp3"
    scene amispecial4
    with flash
    stop sound

    a "…"
    a "…"

    play sound "static.mp3"
    scene amispecial5
    with flash
    stop sound

    a "…"
    a "…"
    a "…"

    play sound "static.mp3"
    scene amispecial6
    with flash
    stop sound

    a "…"
    a "…"

    play sound "static.mp3"
    scene amispecial7
    with flash
    stop sound

    $ renpy.pause(7, hard=True)
    scene black

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mayadorm30:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label amidorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ami_love >= 5 and amidorm5 == False and day == 1 or day == 5:
                play sound "knock.mp3"

                s "Hey, Ami. Are you in there?"
                "..."
                "There's no answer."
                jump doorknock
            if ami_love >= 5 and day != 1 and day != 5 and amidorm5 == False:
                jump amidorm5
            if ami_love >= 10 and day > 5 and day60 == True and amidorm5 == True and amidorm10 == False and day24 == True and amisroom10 == True:
                jump amidorm10
            if ami_love >= 15 and amidorm10 == True and mayadorm5 == True and amidorm15 == False:
                jump amidorm15
            if ami_love >= 20 and day != 1 and day != 5 and amisroom20 == True and amidorm20 == False:
                jump amidorm20
            if ami_love >= 25 and amidorm20 == True and day != 5 and amidorm25 == False:
                jump amidorm25
...
```