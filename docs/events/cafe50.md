# The Paragon of Not Worrying About Stuff
Rin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=cafe50&go=Go)



## Event preconditions
✅Rin love greater than or equal to 50

✅Event "[Main: All is Bright. All is Beautiful.](./secondbeach18.md)" is completed (event=secondbeach18)



## Next events
* [Rin: Technicolored Happiness Explosion](./rindorm50.md)

## Event properties
* ID: cafe50
* Group: Rin
* Triggered by label: cafe
* Triggered by branch label: cafe

## Event code
File: \game\RinEvents.rpy
Code:
```python
...
label cafe50:
    scene cafefifty1
    with fade
    play music "cafe.mp3"

    "I make my way into the cafe to find things a little busier than normal this morning."
    "It’s particularly windy today, so I figure that might have something to do with it."
    "Does wind make cafes busier? That sounds like a thing."
    "Either way, I am prepared to order myself a hot beverage and immediately vacate the premises because there is clearly no reason for me to ever stay here."

    s "…"

    "That’s right. I said there is no reason for me to ever stay here."

    s "…"
    s "{i}Ahem.{/i}"

    scene cafefifty2
    with dissolve

    r "Yo! Sorry for the wait. Been a little wild this morning, if you know what I mean."
    s "What else could that possibly mean apart from the cafe being busy?"
    r "Beats me. Maybe I killed someone on the way to work? You know...found a machete and just went to town on an innocent bystander."

    if day == 6:
        r "Saturdays, am I right?"
    else:
        r "Sundays, am I right?"

    s "Sure, Rin. "
    r "So, I’m gonna assume you’re here to congratulate me on the fact that I have a girlfriend now, right?"
    s "I’m actually here to order a drink."

    scene cafefifty3
    with dissolve

    r "What? Why? "
    s "Because that is literally the purpose of this building. "
    r "No. The purpose of this building is giving you and me some time to chill outside of[school] while {i}also{/i} allowing me to get paid."
    s "Right. So what does that mean for the days that I {i}don’t{/i} come here?"

    scene cafefifty4
    with dissolve

    r "On those days, I normally just sit around frowning...hoping you’ll show up to keep me company."

    scene cafefifty5
    with hpunch

    r "Or at least that’s what I {i}would{/i} be doing if I didn’t have a girlfriend now!"
    r "So, did you hear that I have a girlfriend now? Because I totally have a girlfriend now. "
    r "Like, a real one. Not just a picture of a girl I like that I carry around in my wallet and whisper sweet nothings to when no one is looking."
    s "Is that...a thing you actually do? Or {i}have{/i} done?"

    scene cafefifty6
    with dissolve

    r "What? No. Weren’t you listening? "
    r "Besides, who prints out pictures anymore? Just set a picture of the girl you secretly like as your lock screen and move on like everybody else."
    r "Which reminds me, I have a girlfriend now."
    s "Wow, really? I had no idea."

    scene cafefifty7
    with dissolve

    h "Rin, as happy as I am for you, I {i}kind of{/i} need you...actually working today."
    r "I kind of need you to congratulate me on the fact that I have a girlfriend now."

    scene cafefifty8
    with dissolve

    h "I’ve congratulated you like ten times today alone. I can’t keep doing this for the rest of forever. It’s wasting too many words."
    r "Okay, okay. Fine. You’re off the hook for the rest of the day."
    r "But if my {i}girlfriend{/i} finds out that you don’t care about her, you can bet those huge mommy milkers of yours that she’ll have something to say about it."
    r "Just kidding. Otoha is really nice. "
    r "Otoha is my girlfriend, by the way. We’re dating now."

    scene cafefifty9
    with dissolve

    h "You didn’t bring a leash, did you?"

    if bonus == True:
        s "I wish."
        r "Careful, Sensei. The only girl who can put me on a leash is Otoha. My girlfriend."
        s "We’ll see about that, Rin."
    else:
        r "Why would he do that? There are no animals here."
        s "We will see about that."

    scene cafefifty10
    with dissolve

    r "Wait, we will? Why do you sound so sure? "
    s "Just a hunch."
    r "Ominous. "
    r "Make sure you check with my girlfriend first. Her name is Otoha, by the way. She’s the one who is dating me. Have you heard of her?"
    s "Never."
    s "But anyway, how are you doing, Haruka? You seem easier to talk to in your current mental state."

    scene cafefifty11
    with dissolve

    r "Hey! I’ll have you know that {i}my{/i} current mental state is better than ever! I’m totally happy and totally cool!"
    h "Oh, uhh...I’m doing well. "
    h "Just trying to keep things afloat in here, which is admittedly a little tough when my best employee is now somehow {i}worse{/i} at her job after getting a...girlfriend, I think it was?"
    s "If this is your best, you might want to look into hiring a few more girls."
    r "Oh, okay. Yeah. Now that Rin has a girlfriend, it’s fine to just make fun of her all day. I see how it is."
    r "You two wait until my girlfriend hears about this. She’ll show you what’s up."
    r "Her name is-"

    scene cafefifty12
    with dissolve

    h "Okay, seriously? Stop. "
    r "Ugh. Fine. I’ll keep doing my job. "
    r "If I’m ever going to inherit the family business, I can’t be slacking off like this."
    h "Thank-"

    scene cafefifty13
    with dissolve

    h "Wait, are we related now? How is this a “family” business?"
    r "You’re kinda like a mom to me, aren’t you? You’ve definitely got the boobs of one."
    h "Can we stop talking about my boobs? Also, there are plenty of mothers out there who-"
    r "You’re also just as related to me as my actual mom. So yeah, basically a family member. "
    r "If I’m not in your will, I’m gonna be really pissed."
    h "Okay. You know what? There’s a customer in the corner who just ordered a vanilla latte. "
    h "If you can get it to them in less than two minutes, I’ll add you to my will. If not, I’m leaving the cafe to Sensei."

    scene cafefifty14
    with dissolve

    r "Over my dead body..."
    s "Take your time, Rin. Inheriting a business for literally nothing sounds like a pretty sweet deal."
    r "The only thing {i}you’re{/i} going to inherit is...disappointment."
    s "Cool. Thanks."

    scene cafefifty15
    with dissolve

    h "Hah..."

    if day == 6:
        h "Saturdays, am I right?"
    else:
        h "Sundays, am I right?"


    s "You know...I really do see the nonbiological resemblance."

    if bonus == True:
        s "And I would also like to take this moment to confirm that I like your breasts just as much as Rin appears to."

        if harukasex == True:
            scene cafefifty16
            with dissolve

            h "Yeah...I am quite aware of that."
            h "You don’t really need to remind me."
        else:
            scene cafefifty16
            with dissolve

            h "Watch it. We’re just {i}friends{/i}, remember?"
            h "Saying things like that is something we should try to avoid for both of our sakes."
            s "Yeah, yeah. I get it. "

    s "Anyway, if you’re concerned about her carrying this on for much longer, you probably don’t have to worry."

    scene cafefifty17
    with dissolve

    h "You’re not rooting for those two to fail, are you?"
    r "Better not be!"
    s "No. I just mean that Rin is naturally obsessive and probably just wants to get some of that rare...{i}true{/i} happy energy out of her or something."
    s "I don’t know. I’m not really well-versed in what it means to feel happy and...do happy things."

    scene cafefifty18
    with dissolve

    h "Uhh...sorry?"
    h "Is this a cry for help? Do you need a shoulder to dry all your tears of loneliness on?"
    s "What? No."

    scene cafefifty19
    with dissolve

    h "Good. Because I do. And if we both had to cry, the angles would be all weird and we’d probably just be crying into the air."
    s "Are you feeling even lonelier than normal, Haruka?"

    scene cafefifty20
    with dissolve

    h "I mean...not any more than {i}normal{/i}. But my default state is enough to make most people want to cry."
    h "All things considered, though. It hasn’t really been that bad lately. "
    h "I’m just trying to stay focused on the business and-"

    scene cafefifty21
    with hpunch
    stop music
    play sound "glass.mp3"

    h "Ah-"

    play sound "static.mp3"
    scene happy1 with flash
    scene happy2 with flash
    scene cafefifty22
    with flash
    stop sound

    r "…"
    h "Rin? What’s wrong?"
    r "…"
    s "…"
    h "…"
    s "Should we...do something?"

    scene cafefifty23
    with dissolve

    h "Uhh...Rin? You okay?"
    r "...huh?"
    r "That’s weird. Wasn’t I just..."

    scene cafefifty24
    with dissolve

    r "Ah! Crap!"
    r "I’ll get a broom! And a...mop!"
    r "Cleaning stuff! Yeah!"
    r "Gonna...Gonna go do that!"
    r "…"
    r "Be right back!"

    scene black
    with dissolve2

    "Rin scurries off to the back of the cafe and returns moments later with a mop bucket and a broom to sweep up the broken glass of the mug she dropped."
    "Not really sure how to handle the situation, I stand around and wait for things to pass while Haruka makes another drink for the customer who just lost theirs."
    "After a few minutes, Rin finishes cleaning and returns to the two of us."
    "………"
    "……"
    "…"

    scene cafefifty25
    with dissolve
    play music "cafe.mp3"

    r "So, uhh...whoops! Hahaha..."
    r "Guess mistakes happen to even the best of us, right?"
    r "You can deduct whatever the cost of that mug was from my paycheck. It’s my fault, so I don’t really mind."
    h "I’m not really worried about the mug. I just want to make sure you’re feeling okay since you...seemed a little out of it just now."

    scene cafefifty26
    with dissolve

    r "Nah, dude. I’m good. My hand just twitched or something. It’s fine."
    h "No lightheadedness or...nausea or anything like that?"
    h "You’ve been running around all morning, so-"
    r "No nothing, Haruka. Won’t happen again."
    s "Have you gone on break yet today?"

    scene cafefifty27
    with dissolve

    r "Hm? Even {i}you’re{/i} worried? But...you’re like the...paragon of not worrying about stuff."
    h "He’s probably worried as a friend. Not an authority figure or teacher or...counselor or whatever other jobs he neglects."
    s "Thank you, Haruka. I appreciate that."
    s "And not to throw away another title so soon after getting it, but I’m not really worried right now either."
    s "I just think your {i}new girlfriend{/i} might get a little upset if her lover collapsed at work."

    scene cafefifty28
    with dissolve

    r "L-Lover?...I mean...what even is “love,” you know?"
    r "It’s still way too early to be using words like that because it would make whoever said it first clingy. And if there is anything Rin Rokuhara {i}isn’t{/i}, it’s clingy."
    r "Besides, how can I even {i}be{/i} clingy when we only kissed the one time? "
    r "And even then, it was only for a few seconds. "
    r "Was it a good few seconds? Yeah. It was awesome. But it was only a few seconds. There’s no way I {i}love{/i} her, you know? "
    h "Do you want to go on break a little early today, Rin?"

    scene cafefifty29
    with dissolve

    r "What, like now? But we’re still super busy and I’m totally fine. I swear."
    h "I’ll manage. Besides, Sensei doesn’t typically spend entire days here, and I’m sure you want to talk a little more about Otoha with him."
    r "I mean...kiiiiind of. But there’s not much to say."
    s "I’m right here, you know. You can tell me that directly."

    scene cafefifty30
    with dissolve

    r "Sure. There’s not much to say."
    s "You sure sounded like you had a lot to say earlier. Granted, it was mostly just repeating the same thing over and over again."
    h "Just take her outside and give her a breath of fresh air or something. She’s been in here since we opened and could probably use it."
    r "I’d kind of rather we stayed inside on account of the whole...evil winter wind thing going on outside."
    s "Then I guess we’ll just do that."
    r "Can it be on the couch, though? I still feel awkward about spilling that one customer’s drink and I don’t want them looking at me like I ruined their day."
    s "You certainly have a lot of demands for your break."
    r "Dude, I only get one. I’ve gotta make it the best possible break I can."
    s "Outlooks like that are better aimed toward more vague concepts like life as a whole."
    r "But what does it mean to {i}live?{/i} What if we’re all trapped in some sort of simulation, and one day we’ll all wake up and have, like...cheese for eyes or something?"
    s "What?"
    r "I don’t know. It’s possible."
    r "What if all we are is just cheese in general? What kind would {i}I{/i} be? Mozzarella? Gouda?"
    r "What’s the most bisexual cheese? I wanna be that."
    h "Since a conversation like this would {i}never{/i} happen while clocked in, I’m just going to assume that Rin’s break has already begun and start counting down the time now."
    h "Have fun, you two."

    scene black
    with dissolve2

    "Rin and I take a seat on the couch and she begins telling me all about her rather brief and uneventful first brush with romance."
    "But despite saying just moments ago that she didn’t really have anything worth mentioning, she manages to talk for the duration of her break about all sorts of things."
    "Well, all sorts of things relating to Otoha."
    "How she’s trying her best to take things slow...where she expects things to go by the end of the year...and even her hopes of being in the same class again once I’m no longer her teacher."
    "Of course, I don’t say anything about how I’ll be her teacher for the rest of eternity if all goes according to plan."
    "Just like I don’t say that I expect this honeymoon period to fizzle out over time...and how I think all connections can be broken ten times easier than they can be formed."
    "She has achieved her goal for now, but what comes next?"
    "If it follows the path of most other [young]romances, I would predict tragedy."
    "Even with the mass amount of flags popping up, though, Rin doesn’t seem particularly fazed."
    "Obviously, everything Rin says about Otoha is laced with a dose of hormonal excitement...but there’s a complete lack of worry."
    "In fact, all of the worry I imagined there would be has been swapped out with what feels like a burning sense of conviction."
    "…"
    "Which raises the question-"
    "Why does something still feel off?"

    $ renpy.end_replay()
    $ rin_love += 1
    $ cafe50 = True
    stop music fadeout 5.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon


label rindate50:
...
```

## Code that triggers this event
File: \game\RinEvents.rpy
Code:
```python
...
label cafe:
    if rin_love >= 0 and firsttimecafe == False:
        jump firsttimecafe
    if rin_love >= 5 and cafesugar == False:
        jump cafesugar
    if rin_love >= 10 and cafe10 == False:
        jump cafe10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == True and day30 == True and cafe15 == False:
        jump cafe15
    if rin_love >= 20 and ayanenew1 == True and cafe15 == True and day50 == True and cafe20 == False:
        jump cafe20
    if rin_love >= 15 and cafe15 == True and day63 == False:
        jump rincafegone
    if rin_love >= 25 and rindorm20 == True and amisroom5 == True and day65 == True and cafe25 == False:
        jump cafe25
    if rin_love >= 30 and beachvacation16 == True and cafe30 == False:
        jump cafe30
    if rin_love >= 35 and rindorm35 == True and rininvite == True and cafe35 == False:
        jump cafe35
    if rin_love >= 40 and christmas7 == True and cafe40 == False:
        jump cafe40
    if rin_love >= 45 and rindorm40 == True and cafe45 == False:
        jump cafe45
    if rin_love >= 50 and secondbeach18 == True and cafe50 == False:
        jump cafe50
...
```