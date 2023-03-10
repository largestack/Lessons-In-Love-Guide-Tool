# Great Burdock Leaves (Futaba)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 64

* Event [Broken Flowers](./futabanew1.md) (Futaba) is completed)

* Event [Weight Limit](./day72.md) (Main) is completed)



## Next events

* [Futaba: Clam's Tongue](./futabanew3.md)

## Event properties

* Id: futabanew2
* Group: Futaba
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->futabanew2

## Official wiki page

[Great Burdock Leaves](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=futabanew2&go=Go) for more details.

## Event code

File: (install folder)\game\FutabaEvents.rpy

Code:
```python
...
label futabanew2:
    scene futabanewtwo1
    with fade
    play music "phantomthief.mp3"

    "I toss aside a stack of papers that Makoto wanted me to go over after taking one look at them and deciding that I have much better things to do with my time."
    "I can not risk being distracted by clerical work when there are so many girls in my class that could need assistance at any given moment."
    "Now, I understand and acknowledge that most of the girls in my class {i}do not{/i} actively seek out my assistance when it comes to personal issues..."
    "{i}But what if they did?{/i}"
    "I’m sure Makoto will understand my decision to just let her handle all of this instead of doing it on my own when it’s for the sake of her classmates."

    play sound "knock.mp3"

    "Look, here’s one of them now."
    "Unless..."

    s "I’m doing them right now, Makoto. Don’t worry."
    f "Umm...it’s actually Futaba. Is it...okay if I come in?"

    "Woah. I guess someone actually {i}does{/i} need my help today?"
    "I suddenly feel a lot better about neglecting my responsibilities. "

    s "Sure. Just don’t tell the class representative that I’m irresponsible."

    scene futabanewtwo2
    with dissolve
    play sound "dooropen.mp3"

    f "Irresponsible when it comes to what, exactly? I’m not...interrupting something, am I?"
    s "Nothing that I actually wanted to do, so I wouldn’t worry too much about it."
    s "But anyway, is something wrong? Or are you just dropping by because you miss me?"

    scene futabanewtwo3
    with dissolve

    f "I...wouldn’t do that. You’re probably far too busy for me to drop by just because I want to see you."
    s "I find it surprising how you can say that despite the many times I have dropped by your dorm room specifically because I did {i}not{/i} have anything to do."
    f "It’s a little different when you’re the one who comes to me...Especially since you never intend to burden me when you do."
    s "Ahh. So you intend to burden me today?"

    scene futabanewtwo4
    with dissolve

    f "Maybe...just a little bit."
    s "Yumi again?"

    scene futabanewtwo2
    with dissolve

    f "How did you know?"
    s "Because she’s the only thing that ever lands you here. What did she do this time?"

    scene futabanewtwo3
    with dissolve

    f "Thankfully not much since Ayane showed up and...I guess convinced her to leave me alone for the time being. "
    f "But she...umm..."
    f "Well, let’s just say she was a little more assertive than usual and...I was a little more {i}defenseless{/i} than usual as well."

    "It’s nice hearing that Ayane is going out of her way for Futaba as well- but I guess I’m not that surprised to hear it since she seems like the type to step up and intervene in something like that."
    "If I could be everywhere at once, I’d have no issue with becoming a sort of personal bodyguard for Futaba or...whoever else Yumi decides to fuck with on any given day."
    "Unfortunately, sometimes it feels like I’m barely even in {i}one{/i} place at once. So relying on other people to make up for my inability to involve myself is just...something I have to do every once in a while."

    s "What was it that made you more defenseless, if you don’t mind me asking?"
    s "Did she barge into your room or something like that?"

    scene futabanewtwo5
    with dissolve

    f "Well, no...umm..."
    f "This actually happened in...the shower room after gym class one day..."
    s "..."

    "Perhaps I should find a way to make myself more available after all? "
    "If Futaba needs someone to protect her while she is completely naked, I should be the one to step up so Ayane doesn’t have to anymore."
    "That’s simply the right thing for me to do as her teacher."

    s "Are you worried she’s going to do it again? Because if things are progressing to the point where she’s cornering you in the showers-"

    scene futabanewtwo6
    with dissolve

    f "I...well, I {i}know{/i} she’s going to do it again because...she’s Yumi and I’m {i}me.{/i} And I’m not asking you to...discipline her or anything like that since...I don’t know if it’s something she can control."
    f "I just..."

    scene futabanewtwo7
    with dissolve

    f "I guess I...I’m just being selfish and...wanted to hear you console me...and tell me that she’s wrong again."
    s "I feel like I’ve been doing that a lot lately."
    f "You have...Which is why I said I’ll be burdening you a little bit today..."
    s "Futaba, if repeatedly consoling you is actually going to help you here, I’ll do it. But, based on how you’re still coming to my office seeking the same thing-"

    scene futabanewtwo8
    with dissolve

    f "I’m sure it sounds weird to you, but...at the same time...have you ever gone through something like this, Sensei?"
    f "Where...someone you don’t have any problem with has more problems with you than you can count?"

    scene colorbars
    stop music
    $ renpy.pause(5, hard=True)
    scene futabanewtwo8
    play music "phantomthief.mp3"

    s "No."
    f "See? I didn’t think so..."

    scene futabanewtwo3
    with dissolve

    f "You’re...naturally good looking, and..."
    f "I guess what I’m saying is that you’d think that I’d be immune to things like this for as long as I’ve put up with them, but..."
    f "I don’t know. "
    f "The only thing that ever works is being reminded by someone else that the Futaba Fukuyama that Yumi sees..."
    f "That the Futaba Fukuyama that {i}I{/i} see is the one that’s actually twisted."

    scene futabanewtwo8
    with dissolve

    f "So, I’m sorry again for the inconvenience as I really don’t want to trouble you...but today was one of those days where I just wanted to be reassured."
    s "..."
    f "...Sensei?"
    s "Sorry, yeah. I’ll reassure you whenever you want. "
    s "I just wish there was something more I could do."

    scene futabanewtwo9
    with dissolve

    f "Don’t. You’re already doing a great job, Sensei. It’s {i}me{/i} who needs to figure out something else to do."
    f "Positive reinforcement can only carry a person so far..."
    f "Did you know I actually used to be pretty skinny? It was a really long time ago...before I even met Rin...but there was a time where people would say things like, “You need some more meat on your bones.”"
    f "Things like that. Things that I’m sure tons of the girls in our class hear even today."
    f "But...the craziest part was that even back then, I didn’t believe them. Not one bit."
    f "In fact, I still have trouble believing them. And if it weren’t for me being able to look back at those pictures...and see with my own eyes how badly things have changed..."
    f "I think I’d still probably say that I’ve been this way forever."
    s "..."
    f "..."

    "Futaba’s eyes lock on mine but don’t do any amount of justice in showcasing the pain she feels inside."
    "I want to relate- I do. But without even being able to remember anything more than a few months back, how could I possibly do that?"
    "Is positive reinforcement seriously the only thing I can do for her? Because, as it stands, my words are nothing more than bandages over bullet holes."

    s "I don’t really know what to say here, Futaba."
    f "I wasn’t looking for a response this time...I just wanted to share a little more about myself."

    scene futabanewtwo10
    with dissolve

    f "Us writers call that {i}character development.{/i}"
    s "Look at you, calling yourself a writer before even finishing the story I assigned you. That’s the kind of confidence I want to see more of."
    f "Heheh! This confidence was a gift from you, Sensei. Without your help, I wouldn’t even be strong enough to say that yet."
    s "Well, here’s hoping you wind up getting strong enough to look at yourself differently in other areas as well."
    s "Do you really not want me to do anything about Yumi, though? Because as much knight-potential as Ayane has, I still think that role is better suited for someone like me."

    scene futabanewtwo9
    with dissolve

    f "If I become {i}completely{/i} dependent on you, I’ll never get anywhere in life..."
    f "Besides, I like Yumi. I’ve watched her stick up for Chika before when girls from another class were saying mean things about her. There’s definitely a heart in there."
    f "And who knows? Maybe her being mean to me is just...her equivalent of me coming to you for encouragement and motivation?"
    s "That’s certainly one way to look at it. Though, it’s not one I’m really sure I agree with."

    scene futabanewtwo10
    with dissolve

    f "Maybe you could give Yumi some encouragement as well then? If she ever finds herself in your office without being forced in, of course."
    s "Yeah, I have a good feeling that would somehow make things with Yumi and me even worse. So I’ll just keep complimenting you instead and we’ll see where that takes us."

    scene futabanewtwo9
    with dissolve

    f "Thank you, Sensei. And I’m sorry again for taking up so much of your time for something so...unimportant."
    f "Do you...umm..."

    scene futabanewtwo3
    with dissolve

    f "Do you have any plans after this? Or would you maybe want to...walk home together?"

    scene futabanewtwo11
    with dissolve

    f "A-And by “home,” I obviously mean the dorm! I wasn’t asking to come back to your house if...if that’s how it sounded!"
    s "Are you sure? Because I wouldn’t mind bringing you over to my place as long as we can figure out a cover story to give Ami."

    scene futabanewtwo12
    with dissolve

    f "Wh..."
    f "What would we...do at your house, exactly?..."
    s "..."
    f "..."

    scene futabanewtwo11
    with hpunch

    f "F-Forget I asked! That sounded...extremely inappropriate! Please just...walk me back to the dorm!"
    f "If that’s okay, I mean! I completely understand if something like that is-"
    s "I’ll walk you back, don’t worry. It’s about time for me to leave anyway."

    scene futabanewtwo2
    with dissolve

    f "It is?...Did I really take up that much of your time?"
    s "Yes. But, in doing so, you not only prevented me from filling out some paperwork I definitely didn’t want to touch, but allowed me to use my office for its actual purpose."
    s "That doesn’t happen very often around here."

    scene futabanewtwo9
    with dissolve

    f "Well..."
    f "I guess we both got something out of today then..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene futabanewtwo13
    with dissolve2

    "Futaba and I exit my office together and begin to make our way to the lockers so she can switch shoes and gather her things."
    "There’s still a fair amount of girls in the school, likely on their way to club meetings or friendly gatherings, but it’s not like being seen with a student while still on school grounds is going to make {i}me {/i} look bad."
    "In fact, as long as I don’t run into anyone from class who accuses me of favoritism for spending time with Futaba instead of them, I think today may actually end pretty smoothly."

    s "Futaba, I am sorry in advance."
    f "Hm? Sorry for what?"
    s "I believe I may have just jinxed us in one of my inner monologues."
    f "As sad as it is for me to admit this...life isn’t a book, Sensei. You can’t just foreshadow events in real life by just thinking things and-"

    scene futabanewtwo14
    with dissolve

    mi "What the heck is this?! Sensei and Futaba hangin’ out after school?! Without invitin’ me along?!"
    mi "I demand an explanation right now!"

    scene futabanewtwo15
    with fade

    mi "Just kiddin’. I’ve got soccer practice with the gang, so I wouldn’t be able to hang out with you guys anyway."
    s "Hey, you two. Why haven’t you gone home yet?"

    scene futabanewtwo16
    with dissolve

    mi "Are you not payin’ attention to me at all?! I just told ya I have soccer practice!"
    mi "Stop focusin’ on Futaba’s melons and listen to me! Small girls need love too! Ain’t that right, Sana?!"
    sa "I...don’t want to be involved in...that kind of conversation..."
    s "Why haven’t {i}you{/i} gone home, Sana? I already know Miku has a meeting for the home economics club or whatever it is she’s in."
    mi "I am wearin’ my friggin’ uniform! You know darn well what club I’m in, Sensei!"
    sa "I’m just...waiting for Ayane to finish cleaning the classroom."
    sa "What...um...what are...you two doing together?"

    scene futabanewtwo17
    with dissolve

    f "I was just...bothering Sensei in his office with some...personal problems."
    mi "Personal problems? You doin’ okay, Futaba? Wanna rest your head on my shoulder without the fear of whatever the cops would do to Sensei if they saw you doin’ that to him?"
    s "Hey."
    f "Oh, no. I’m fine now. It was...really stupid anyway."
    mi "Well, stupid or not, I-"

    scene futabanewtwo18
    with hpunch

    a "HEY! WHAT’S THE BIG IDEA?! WHY ARE YOU STILL IN SCHOOL WITH GIRLS WHO AREN’T ME?!"
    mi "Hah...uhh...maybe...tone it down a bit before ya just sneak up behind people and start yellin’ stuff, Ami?"

    scene futabanewtwo19
    with dissolve

    a "Was this {i}your{/i} idea, Miku? Are you trying to steal my uncle from me now too?"
    mi "Huh? I was just talkin’ to Sana before soccer practice. Futaba’s the one you’ve gotta be worried about when it comes to stealin’ Sensei away."

    scene futabanewtwo20
    with hpunch

    a "Traitor! How dare you skip our club meeting to start an affair!"
    f "What?! This isn’t like that at all!"
    m "She literally told us she was going to Sensei’s office before the meeting started."
    a "Does this look like an office to you, Maya?! Because it sure as heck doesn’t look like an office to me!"
    f "That’s...I just...needed some help from Sensei about...some personal matters..."

    scene futabanewtwo21
    with dissolve

    a "Personal matters? Is it anything we can help with?"
    m "Well, you sure got over that quickly."
    f "No, it’s..."

    scene futabanewtwo22
    with dissolve
    stop music fadeout 10.0

    f "Um...I’m not really sure how to word it without...making it seem like I’m taking it out on {i}you.{/i}"
    a "On me? Did I do something wrong? Cause if this is about the yelling thing, that was pure instinct and I can’t really help it and I am sorry."
    f "No, no. Not {i}just{/i} you, Ami."
    s "Futaba?"

    scene futabanewtwo23
    with dissolve

    f "{i}All{/i} of you..."

    play sound "static.mp3"
    scene futabanewtwo24 with flash
    scene futabanewtwo23 with flash
    scene futabanewtwo24 with flash
    scene futabanewtwo23 with flash
    scene futabanewtwo24 with flash
    scene futabanewtwo23 with flash
    scene futabanewtwo25 with flash
    stop sound

    f "I’m sorry! I actually forgot I had...something else to do today."
    f "Thank you for your help, Sensei. "
    f "And...I’m sorry to everyone else for having to leave so soon."
    f "Thank you...for your concern."

    play sound "static.mp3"
    scene futabanewtwo24 with flash
    scene futabanewtwo26 with flash
    stop sound

    mi "..."
    sa "..."
    a "..."
    m "..."

    scene black
    with dissolve2

    "Autumn came, and the leaves in the forest turned to orange and gold."
    "Then, as winter approached, the wind caught them as they fell."
    "It is only with the heart that one can see clearly, for the most essential things are invisible to the eye."
    "The scent of chlorine and porcelain has never smelled as beautiful as it does now."
    "The end."

    $ renpy.end_replay()
    $ futabanew2 = True
    $ futaba_love += 1

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "{i}Her appetite has decreased by 5.{/i}"
    "........."
    "......"
    "..."


    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label futabanew3:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
    if totaldays >= 56 and shrine5 == True and day56 == False:
        jump day56
    if totaldays >= 60 and ayanenew2 == True and ayanenew3 == False:
        jump ayanenew3
    if totaldays >= 63 and rindorm20 == True and day63 == False:
        jump day63
    if totaldays >= 64 and futabanew1 == True and day72 == True and futabanew2 == False:
        jump futabanew2
...
```