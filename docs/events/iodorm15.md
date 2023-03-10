# Amongst Other Things (Io)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Io love greater than or equal to 15

* Event [Turn On The Lights](./bathhouse10.md) (Io) is completed)

* Day of week is not Friday



## Next events

* [Io: One Man's Trash](./bathhouse20.md)

## Event properties

* Id: iodorm15
* Group: Io
* Triggered by label: iodorm
* Triggered by branch label: doorknock2
* Triggered by path: doorknock2->iodorm->iodorm15

## Official wiki page

[Amongst Other Things](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=iodorm15&go=Go) for more details.

## Event code

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label iodorm15:
    play sound "knock.mp3"
    stop music fadeout 15.0

    "I knock on Io’s door and wait for her to answer."
    "But several seconds go by without a response and, given that she doesn’t normally work this late, I start to wonder if she might be out doing something else."
    "But then I remember that this is Io we’re talking about, and that the likelihood of her actually doing anything other than working or hanging out in her room is practically zero."
    "So I knock again."

    play sound "knock.mp3"

    s "Hey. Are you in there?"
    s "…"

    "Time starts to tick by and-"

    i "Ngh...what?"
    i "Sensei? "
    i "Is that you?"
    s "Did I wake you up? "
    i "Not...exactly but..."
    s "Can I come in?"
    i "Yeah...Let me just get this out of the way and-"
    play sound "thump.mp3"
    with hpunch
    i "Ah!"

    "Something falls over and hits the ground."
    "But considering there are roughly six million objects inside of Io’s room, things like this are bound to happen."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I’ll have to ask Ami to clean this room while Io is away since Uta is clearly incapable of fulfilling her maidly duties and-"

    scene iokotatsu1
    with dissolve2
    play music "hometown.mp3"

    i "Ngh..."
    s "Are you okay?"
    s "Was that {i}you{/i} who fell just now?"
    i "...Probably."
    s "I feel like that’s something you should know."
    i "Just...a little out of it..."

    scene iokotatsu2
    with dissolve

    i "So, uhh..."
    i "What’s up?"
    s "What’s up is you’re either extremely tired or extremely drunk."
    i "Or extremely messed up from mixing medications and not eating anything all day."
    s "Medication?"
    i "It’s the fancy word for medicine."
    s "I know what it means, Io."
    i "Cool. Then we can forget this happened and talk about something else."
    s "The next time you don’t respond to my knocks, I’m just walking away."
    s "If you need rest or whatever, you shouldn’t be getting out of bed for me."

    scene iokotatsu3
    with dissolve

    i "I told you, I’m good. Just a little out of it."
    i "This isn’t like, an abnormal thing. It happens all the time and it’s easily preventable."
    i "I’m just a little dizzy. "
    s "Can you stand?"
    i "Probably not. So if we could hang out on the ground, that would be cool."
    s "I mean...that doesn't exactly sound like a good time. But I don’t think it can be helped at this point."
    i "If you’re okay with catching me, I can try standing up."
    s "You weigh probably just as much as my cell phone, so that much wouldn’t be a problem."
    s "But I don’t think you should be overexerting yourself if you’re sick."
    i "I’m not {i}sick{/i} sick. I’m Io sick."
    s "Is that some new form of debilitating disease?"
    i "Yeah. They made it just for me."
    s "Really, though. What’s wrong?"
    i "It’s a secret."
    s "You hate secrets."
    i "The pill bottles are right behind me and I’m in no shape to fight you. "
    i "I mean, even if I wasn’t all messed up right now, I wouldn’t be in any shape to fight you. You’re really big."
    i "But go ahead and read them if you’re that curious. There are some pretty wild names on there."
    i "Oh, and there are a couple more under the bed you can probably find if you lay down and move your arm around."
    i "They fell off the mini fridge when I tried to make it to the door and now I'm gonna have to crawl under there and get them back."
    s "I’d really prefer if you’d just tell me what's wrong so I don’t have to Google some complicated name that I won't even be able to say out loud."
    i "I mean, if it was just {i}one{/i} thing, I wouldn’t have so many different bottles, right?"
    i "I’m all sorts of broken. I already told you this."
    s "You don’t look that broken to me."
    i "And {i}you{/i} don’t look that broken to me. So we’re either really good at judging each other or really bad at it."
    i "Why are you still standing?"
    s "Because I don’t want you to throw up on me."

    scene iokotatsu4
    with dissolve

    i "I’m not going to throw up on you. "
    i "Well, I probably would if you like, spun me around or something. But that’s not a thing you’ve done so far, so unless you’ve developed some weird new hobby..."
    s "Spinning isn’t really an interest of mine. But I could pick you up and put you down on your bed if you want to get some rest."

    scene iokotatsu5
    with dissolve

    i "Oooooooor...we could use the kotatsu I just fixed so you don’t have to throw me over a bunch of obstacles and risk knocking the rest of my stuff down."
    i "It also gives us an excuse for me to lay on your lap and have you pat my head."
    s "What if you’re not sick at all and this is just one elaborate ploy to obtain a lap pillow?"
    i "Then I am a much better actor than I thought I was. "
    s "Io-"
    i "Come oooooooon. It’s really warm under there. And I’m super light. You won’t even know I’m on you."
    s "I have no problem with you being “on” me. I’m just having a hard time telling you that I think we should maybe talk about all of these medications."
    i "Are you a doctor?"
    s "I’m not."
    i "Well then what good will talking about my medications do for either of us?"
    i "I’m fine. I’ve got a bunch of stuff that I can take for certain things whenever I need to take them."
    i "I just happened to need several different things tonight and, mixed with the fact that I haven’t eaten at all and how I barely slept last night-"
    i "Boom. Down goes Io."
    s "…"
    i "…"
    s "Hah..."

    scene black
    with dissolve

    "I sigh to myself and accept that Io’s probably not going to give me any specific details tonight."
    "But I think it’s pretty safe to assume that it’s nothing physical if she only takes them when she needs to and-"
    "Well, I guess they could still technically be painkillers or something."
    "Damn it. "
    "Why did she have to pick now to get all light headed?"
    "………"
    "……"
    "…"

    scene iokotatsu6
    with dissolve

    "I turn off the lights before moving over to the kotatsu and sliding myself underneath it."
    "Io waits on her step ladder until I’m in place and then very slowly and clumsily climbs onto me, resting her body in my lap and her head on my chest."

    if bonus == True:
        "It’s a position that makes me acutely aware that I must focus at least half of my energy on not getting an erection because it would be overwhelmingly apparent to her if I did."
        "I stabilize myself with my left hand and use my right one to softly rub her shoulder. "
        "It’s not something I’d normally have any interest in doing, but...given the context of the situation, I think it’s okay for me to be a little nice."
        "At least until she’s able to stand on her own two feet again."
        "As soon as that happens, she can rub her own shoulder."

    i "Guh...sleepy..."
    i "One of the downsides to pretty much every single anxiety medication is how tired they make you."

    "Ahh, so it {i}wasn't{/i} anything physical."
    "Shocker."

    s "You have anxiety?"
    i "Amongst other things."
    i "Was the anxiety part not obvious to you?"
    s "I probably could have guessed. It just sounded rude to say something like, “I thought so.”"
    i "Well, thank you for your sudden increase in generosity."
    i "Maybe I should just always invite you over before I take my meds to reap the benefits of being {i}your{/i} student."
    s "What’s with the emphasis on “your?”"
    i "There aren’t many teachers who would let an anxious, loopy, drugged out [teenager] climb into their lap."
    s "Yeah. Ms. Watabe would have never let you do this with her."
    i "Good. Because I wouldn’t {i}want{/i} to do this with Ms. Watabe."
    i "You, on the other hand..."
    i "I could do this every night for the rest of my life and not get tired of it."
    s "…"
    i "…"
    s "Io?"
    i "Yeah?"
    s "Why do you like me so much?"

    scene iokotatsu7
    with dissolve

    i "Because I have to."
    s "Why?"
    i "Because you’re my last bastion of hope for adults in this world."
    i "I am so tired of everyone else that if things don’t work out with you, I’ll probably just die."
    s "Oh, okay. That doesn’t put all of the pressure in the world on my shoulders or anything."
    i "You’ve already got the rest of me weighing down on you. Might as well go for the shoulders, too."

    scene iokotatsu8
    with dissolve

    i "That was kind of just a joke anyway."
    i "You really are my last line of defense, though."
    i "And probably the only example of something that I’ve wanted that I’ve actually made a push for."
    s "Some push you’re making, nearly passing out in front of me."
    i "There have been other pushes. This one was just a convenient coincidence."
    i "If I’m being completely honest, Sensei...I don’t know why it was you who appealed to me."
    i "You were probably just in the right place at the right time."
    s "So it could have been anyone?"

    scene iokotatsu9
    with dissolve

    i "It could have been anyone."
    i "But..."
    i "I’m glad it was you."
    s "… "
    i "…"
    s "…"
    i "…"

    play sound "dooropen.mp3"
    scene iokotatsu10
    with dissolve

    u "Uta’s home!"
    i "Welcome back. Don’t mind us."
    s "...Hi."
    u "…"
    u "Uta’s not home! Please carry on!"
    i "Wait, no. Stay."
    i "I want you here."

    scene iokotatsu11
    with dissolve

    u "Uhh..."
    i "Pleeeeeease?"
    u "I...don’t know..."
    u "Like...this seems like something I probably shouldn’t get involved in..."
    s "I think you’re misunderstanding the situation."

    scene iokotatsu12
    with dissolve

    u "Did you take too much again?"
    s "Oh. Or you completely understand the situation."
    u "After a few seconds of actually thinkin’ about it, yeah."
    u "How are you feeling? Do you need any water? Juice?"
    i "I’m okay now that Sensei’s letting me use his lap."
    u "Good...I’m glad..."
    u "Hang in there."

    scene iokotatsu13
    with dissolve

    u "Welp! I’ll leave you two kids to it, then! I’ve got no job to do here and my presence will just be a bother!"
    i "Hey, no. I really do want you to stay. It’s totally fine."
    u "Nope! I’m out! "
    u "Don’t...do anything crazy without...calling your aunt!"

    play sound "dooropen.mp3"
    scene iokotatsu14
    with dissolve

    "Uta leaves just as quickly as she arrived."
    "Where she ran off to, I have no idea. But I guess this means that I have a little more time alone with Io."

    i "I really did want her to stay..."
    s "She probably just felt uncomfortable seeing her friend cuddled up against her teacher."
    i "Probably."

    scene iokotatsu15
    with dissolve

    i "It’s admittedly not a thing either of us have any real experience with."
    s "Didn’t Uta think you were a boy when you two first started talking?"
    i "Yeah. And I thought she was a boy too. "
    i "But just because we thought each other were the opposite gender doesn’t mean we have any notable experience with said gender."
    s "It’s just weird that you make an exception to your “no girls” rule for her when she’s one of the girliest girls I’ve ever met. That’s all I’m saying."
    i "It is weird, yeah."

    scene iokotatsu16
    with dissolve

    i "But I really look up to Uta. "
    i "She’s amazing."
    s "In what way?"
    i "In that she got better."
    i "In that she can wake up and put a real smile on. And hold real conversations with all sorts of people."
    i "In that she can organize a classwide, two-day event on a whim and pull the entire thing off without so much as a drop of sweat. "
    i "In that she’s pretty and sweet and doesn’t use that as a front to get what she wants from people."
    s "You clearly have not spent enough time at the maid cafe."
    i "That's a job. It doesn't count."
    i "Uta’s the perfect girl."
    i "I hate it so much."
    i "But I also {i}love{/i} her so much."
    i "And I probably wouldn’t be here without her."

    scene iokotatsu17
    with dissolve

    i "And I’m not joking this time, by the way."
    i "I would very likely be dead if I never met Uta."
    s "She...seems like a great friend."

    "I’m not really sure what else I’m supposed to say to that."
    "Io’s always spewing out a corrosive mixture of positivity and negativity that blend just about as well together as bleach and ammonia."
    "The room fills up with fumes that my lungs can’t handle, and I slowly die with my hand still clasped around her shoulder."

    i "She’s the best friend."
    i "I just wish I could give her more than {i}me{/i}, you know? Like, I suck. She can do so much better."
    s "Yeah, you’re pretty terrible."
    s "But you’re also great in your own ways too."
    i "Like what? Tell me some."
    s "Like...you’re light."
    s "You can lay here and I can’t even feel you."
    i "Uh-huh. And what else?"
    s "That’s it."
    s "That’s all I’ve got."
    i "I can settle for that. That’s fair."

    scene iokotatsu18
    with dissolve

    s "It would probably be nice if you thought a little higher of yourself, though."
    i "I have to do something worthy of being praised for before I can even think of praising myself."
    i "Right now, I’m just a weightless, overmedicated cockroach with a grand total of two bras and four boxcutters."
    s "Why do you have four boxcutters? And why do you only have two bras?"
    i "Do you want to buy me more?"
    s "Bras or boxcutters?"
    i "Why would I need three bras? I can just wash them."
    s "Why would you need five-"
    s "You know, what? Nevermind."
    s "Just...do yourself a favor and...eat before you take your medication next time."
    i "I make no promises, Sensei. Sometimes, I just don’t want to eat."
    s "Well then don’t take your medication those days."
    i "Yeah, that’s probably an even worse idea than the not eating thing."
    s "Why do you have to be so difficult?"
    i "Why do everyone’s standards for “easy” have to be so hard to reach?"
    i "You’d think that “easy” would imply a complete lack of difficulty, but being easy to deal with takes a lot of work. Probably."
    i "I don’t know. I’m definitely not the right person to ask."
    i "I just hope that you're okay with me being the way I am, because I like this a lot."
    i "In fact, I like it so much, I’m gonna take a nap."
    i "Goodnight, Sensei."
    s "…"
    s "Goodnight."

    scene black
    with dissolve2

    "I think about shooting some snarky retort at Io about how I wouldn’t have come here if she was just going to fall asleep on me-"
    "But her forehead is basically a space heater right now."
    "And her body, despite being light as air, is the same way."
    "I’m flattered that she was able to carry on such a lengthy conversation with me despite showing all signs of not being well-"
    "But not thinking about herself will wind up killing her."
    "In fact, thinking {i}too much{/i} about herself will also wind up killing her."
    "Io is practically dead already."
    "And there is no one who deserves rest quite like the dead."
    "So I let her fall asleep."
    "And after she doesn’t wake up for the next hour, I carefully pick her up and lay her down on Uta’s bed, since that one is actually possible to reach."
    "And then I leave without checking the labels on any of her mystery bottles."

    $ renpy.end_replay()
    $ io_love += 1
    $ iodorm15 = True
    stop music fadeout 5.0

    "{i}Io’s affection has increased to [io_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

                    ############################################
                    ##########        ROOM 8         ##########
                    ############################################

label nodokadorm:
    if nodoka_love >= 0 and day288 == True and nodokafirsthall == True and otohafirsthall == True and day != 1 and day != 5 and nodokadorm1 == False:
        jump nodokadorm1
    if nodoka_love >= 5 and nodokalibrary5 == True and day < 6 and day != 1 and nodokadorm5 == False:
        jump nodokadorm5
    if nodoka_love >= 15 and yasudorm20 == True and nodokadorm15 == False:
        jump nodokadorm15
    elif day288 == True and otohadorm1 == False:
        "I don't think Nodoka is ready to hang out alone in her dorm just yet..."
        jump doorknock2
    else:
        jump nodokadormgen

label otohadorm:
    if nodoka_love >= 0 and day288 == True and nodokafirsthall == True and otohafirsthall == True and day != 1 and day != 5 and nodokadorm1 == False:
        jump nodokadorm1
    if otoha_love >= 5 and otohapark5 == True and day > 5 and otohadorm5 == False:
        jump otohadorm5
    elif day288 == True and otohadorm1 == False:
        "I don't think Otoha is ready to hang out alone in her dorm just yet..."
        jump doorknock2
    else:
        jump otohadormgen

label nodokahall:
    if nodokafirsthall == False:
        jump nodokafirsthall
    else:
        jump nodokahallgen

label nodokahallgen:
    if chapthreeactive == True:
        scene nodokasummer2hallgen
        with dissolve
    else:
        scene nodokahall3
        with dissolve

    if bonus == True:
        no "Sensei, good. Do you mind if I ask you for your thoughts on sexual torture devices?"
        no "It shouldn't take long, but I'd like to know if your thoughts on the matter match my own."
        s "..."

        "I spend several minutes trying to figure out why Nodoka wants to talk about such a thing before I chalk it up to just being on account of her...being Nodoka."
        "It's best to not get in her way when she's dead set on talking about something."
        "Even if that something is a thing that would make the vast majority of people uncomfortable."
        "But hey, she definitely could have chosen worse fetishes."
    else:
        no "Sensei, good. Do you mind if I ask you for your thoughts on cows?"
        s "Cows?"
        no "I think they're up to something."
        no "{i}I just can't figure out what...{/i}"

    scene black
    with dissolve

    if bonus == True:
        "To Nodoka's dismay, I don't have many thoughts on her topic of choice."
        "She, however, walks the fine line between loving and hating it, apparently."
        "I'd love to tell you which parts she enjoys and which parts she doesn't-"
        "But frankly, she names so many devices that I've never even heard of that I don't want to mix anything up."
        "Regardless, the conversation comes to an abrupt and awkward end as the two of us ultimately decide to head back to our respective beds."
        "Albeit with one of us significantly less aroused than the other."
    else:
        "Nodoka and I...talk about cows, I guess?"

    $ nodoka_love += 1
    stop music fadeout 5.0

    "{i}Nodoka's affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label nodokadormgen:
    play sound "knock.mp3"

    no "Come in!"

    scene nodokadormgen
    with fade

    "I decide to spend the night hanging out with Nodoka in her dorm."
    "She makes coffee for the two of us to share and we proceed to sit on her bed, making idle chit chat while listening to melancholic indie rock bleeding out of her smartphone."
    "She says that Otoha would be fine with us borrowing one of her speakers or amps and playing it through there-"
    "But then states that there's something magical about the tinge of distortion that accompanies music when streamed through the same devices we use to speak to our loved ones."
    "For those of us that have any loved ones, I mean."
    "I can't help but feel like this won't change much for her or myself."
    "Nonetheless, it changes nothing."
    "The music drags on."

    scene black
    with dissolve

    "Despite Nodoka showing no signs of growing tired, I realize I'm unable to stick around any longer without the fear of passing out."
    "And if I pass out in here, I strongly believe that she might conduct experiments on me for the purpose of her own personal {i}research{/i}."
    "I am not a lab rat. And I can get home without having to traverse a maze."
    "So I do just that and leave her behind."
    "I don't know what she does after that."

    $ nodoka_love += 1
    stop music fadeout 5.0

    "{i}Nodoka's affection has increased to [nodoka_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label otohadormgen:
    play sound "knock.mp3"

    o "Come in!"

    scene otohadormgen
    with fade

    "I decide to spend the night hanging out with Otoha in her room."
    "Without much for the two of us to do around here, I manage to coerce her into playing a few songs for me."
    "She's a bit bashful about it at first since it's apparently weird to just play and sing for one guy in her room."
    "I get that. It definitely is weird."
    "But we manage to counteract the discomfort by eighty-sixing the vocals and just maintaining different sorts of conversations while she strums away."
    "We talk about all sorts of things, none of them being noteworthy, as the sun is slowly overtaken by the moon."
    "Before we know it, it's almost midnight."

    scene black
    with dissolve

    "I try to get Otoha to play an encore for me, {i}with{/i} vocals this time-"
    "But she promptly kicks me out of the room and tells me I'll need to come see her perform elsewhere if I want a real show."
    "It's fine, though."
    "I'm perfectly content for what I {i}did{/i} get to see."
    "Because I realize that no one else will ever see it."
    "And exclusivity is one of my favorite things in the world when I am the one benefiting from it."

    $ otoha_love += 1
    stop music fadeout 5.0

    "{i}Otoha's affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label nodokafirsthall:
...
```

## Code that triggers this event

File: (install folder)\game\Dorm2Events.rpy

Code:
```python
...
label iodorm:
    if io_love >= 5 and bathhouse5 == True and iodorm5 == False:
        jump iodorm5
    if io_love >= 10 and iodorm5 == True and iofirsthall == True and iodorm10 == False:
        jump iodorm10
    if io_love >= 15 and bathhouse10 == True and day != 5 and iodorm15 == False:
        jump iodorm15
...
```