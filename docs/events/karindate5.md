# Walking Penis Monster
Karin event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=karindate5&go=Go)



## Event preconditions
✅Karin love greater than or equal to 5

✅Event "[Main: Reset](./day103.md)" is completed (event=day103)

✅karinnumber equal to True (unknown variable)



## Next events
None

## Event properties
* ID: karindate5
* Group: Karin
* Triggered by label: callkarinafternoon
* Triggered by branch label: callkarinafternoon

## Event code
File: \game\KarinEvents.rpy
Code:
```python
...
label karindate5:
    play sound "phonebeep.wav"

    "I tap on Karin’s name in my phone and wait for her to answer."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene karinseconddate1
    with dissolve
    play music "retrospect.mp3" fadein 5.0

    "Karin and I decide to meet up at the same park as always."
    "She spends the first part of the meeting awkwardly running laps around the track and feeling increasingly worse about how I’m doing literally nothing each time she passes by."
    "Is it a little strange that our meetings are 95%% me supervising her exercise routine? Absolutely."

    if bonus == True:
        "But I’m not going to complain about something as trivial as that when I’m blessed enough to ogle at her body without worry of any sort of consequence."
    else:
        "But I am only here to make sure that she becomes a better athlete, so everything is okay."

    ka "Okay...no more running. I’m good for today. "
    s "Tired?"
    ka "Not at all. Just...I don’t know."
    ka "Maybe a little...embarrassed? Is that weird to say?"
    s "What’s there to be embarrassed about? You’re doing great."
    s "Your times have been improving as well. I have no idea how you have this much stamina."

    scene karinseconddate2
    with dissolve

    ka "Practice...I’ve been doing this almost every day since...well, forever. So it kind of just...developed, I guess."
    s "Good for you. Establishing positive routines is impressive."
    s "Personally, I find it hard even coming to[school] every day."

    scene karinseconddate1
    with dissolve

    ka "That’s...not good, you know? You’re a teacher."
    s "Barely."
    ka "No no no, don’t say that. I’m sure you’re great. Miku talks about you all the time."
    ka "Wasn’t she failing like, every subject before you started helping her out?"

    "I think that’s more due to the fact that I’ve stopped giving anyone grades below an A but hey, if Karin wants to think it’s due to me being a good teacher, so be it."

    s "Yeah. I guess I am pretty impressive when you put it that way."

    scene karinseconddate3
    with dissolve

    ka "Totally! It kind of makes me wish I was a year younger so I could be in class with you guys."

    scene karinseconddate4
    with dissolve

    ka "W-Wait! No! That probably made it sound like I want to spend more time with you, didn’t it?!"
    s "...Not really?"
    ka "I swear that's not what I meant!"
    ka "I was just trying to say that it would be cool to hang out with Kirin and Miku in class and stuff!"
    ka "It totally doesn’t have anything to do with you! Nothing at all!"
    s "I never said it did?..."

    scene karinseconddate5
    with dissolve

    ka "W-Wait! No! That was bad too! Now it sounds like I never want to see you! That isn’t true either!"

    scene karinseconddate6
    with dissolve

    ka "I like you!"
    ka "Like, teacher-like! Not boy-like! Boy bad! Teacher good!"
    s "Okay Karin, it’s time to calm down."

    scene karinseconddate7
    with dissolve

    ka "Ugh...I’m literally the worst."
    ka "I’m never going to get used to this, am I?"
    s "Sure you will. There’s no way you can stay this uncomfortable around me forever, is there?"

    scene karinseconddate8
    with dissolve

    ka "Th-That’s not it at all!"
    ka "I’m really comfortable! I am! "
    ka "Super comfortable! But also not!"

    scene karinseconddate9
    with dissolve

    ka "It’s just...being out here alone with you makes it feel like a...d-d-d-d-date and stuff..."
    ka "And umm...yeah, that probably sounded weird too. I mean obviously it’s not a...date thingy. You’re just doing your job and..."

    scene karinseconddate6
    with dissolve

    ka "Uhh...what were we talking about again?"
    s "I think it was about how you’re a year older than the other girls."

    scene karinseconddate1
    with dissolve

    ka "Oh...umm...yeah. That’s what I was talking about. Right."
    ka "Whoops..."

    "This girl really {i}does{/i} have a hard time talking to men. "
    "Or at least me."
    "Miku has said in the past that Karin gets like this around every boy, but I have a creeping suspicion that miss co-captain here might actually be warming up to me quicker than anticipated."

    s "So you’re a second-year then, right?"
    ka "Right! One year to go. Kind of nerve-wracking to be honest. I’m not really sure what I even want to do with my life yet."
    s "Well you have roughly a year and a half to think about it."

    "I lie."
    "Karin has all of the time in the world to think about it."
    "Everything is going to just reset before she makes a decision anyway."
    "But it’s my duty in times like this to instill false words of encouragement."
    "I really am a great teacher."

    ka "Yeah...that’s what my parents keep telling me as well. "
    ka "They’re great parents, really...but I wish they’d be a little more assertive at times."
    ka "It’s great that they’re so patient with me but like...maybe I need to be pushed in the right direction or something?"
    s "Why not just become a housewife or something like that? That sounds easy enough."

    scene karinseconddate10
    with dissolve

    ka "W-Wife?..."
    ka "Y...Y-Y-Y-Y-Y-You..."
    ka "Are you-"
    s "No Karin, I’m not proposing to you."

    scene karinseconddate11
    with dissolve

    ka "THAT’S NOT WHAT I WAS ASKING!"

    scene karinseconddate12
    with dissolve

    ka "Do...you really think I’m...housewife material?"

    if bonus == True:
        ka "I’m obviously a lot more...{i}developed{/i} and athletic than other girls my age, so everyone just normally suggests that I pursue sports."
    else:
        s "I think you will make someone pretty decently happy one day."

    ka "It’s kind of weird hearing such a...ridiculous suggestion from my coach, who I imagined would be pushing me into that field more than anyone."
    s "You really look at me as your coach? All I've done so far is use the stopwatch app."
    ka "Mhm..."
    s "Fact is, I just think you should do what makes you happy. "
    ka "Not everything that makes people happy makes money, though."
    ka "Athletic careers are one of the hardest to succeed in. And I’m just some random girl who was born with good genes and a good work ethic."
    ka "There are plenty of other Karin Kanda’s out there. "
    ka "And I think that’s one of the reasons I get so overwhelmed when thinking about what to do from here on out."
    s "I figured that’s what was going on, which is why I suggested the housewife thing."

    scene karinseconddate11
    with dissolve

    ka "S-STOP SAYING THAT! MY HEART CAN’T TAKE IT!"
    s "Why? I think you’d make a great wife."
    ka "WHY?! ALL I DO IS RUN AND...KICK! AND THEN RUN SOME MORE!"
    ka "AM I YELLING RIGHT NOW? I FEEL LIKE I’M YELLING!"
    s "You’re definitely yelling."

    scene karinseconddate13
    with dissolve

    ka "Ugh...maybe you should invest in one of those shock-collar things and just...buzz me whenever I start saying weird stuff."

    "That sentence alone warrants like three buzzes. "

    if bonus == True:
        "Do not threaten a perverted man with the opportunity to put a shock collar on a [teenage]girl."

    scene karinseconddate6
    with dissolve

    ka "But really, though?...Who would want a wife like me?"
    ka "I thought guys normally liked more...petite girls. Ones more...feminine and stuff."
    ka "Like...I’ve gotten confessions from girls before, but never a boy."
    ka "I was under the impression I was a little too...intimidating?"
    ka "I don't know the right word to use."
    s "I think you’re looking for the word ‘cute.’"

    scene karinseconddate14
    with dissolve

    ka "C-C-C-C-C-"
    s "You’re going to have to stop reacting that way if you’re ever going to be a wife."

    scene karinseconddate11
    with dissolve

    if bonus == True:
        ka "STOP CALLING ME A WIFE! I’M STILL IN HIGH SCHOOL!"
    else:
        ka "ISHUDFHGIUSDHFOIASHDF!!!!!!!!"

    scene karinseconddate8
    with dissolve

    ka "I can barely form a...s-s-sentence around boys. No way could I marry one!"
    s "Obviously, it’ll take a lot of work. But I’ve seen how you act with Miku and Kirin before."

    scene karinseconddate15
    with dissolve

    ka "Wh-What do you mean by that?"
    s "The first time I met you was in the storage shed after that ball hit the door and Miku...did whatever that thing she did was."
    s "You knew exactly how to calm her down and what to do to resolve the situation."
    s "I’m an adult and all I was able to do was stand there in shock. "
    s "So, in a sense, you’re already more mature than I am."

    scene karinseconddate16
    with dissolve

    ka "Those are more motherly qualities than housewife qualities..."
    ka "Wives are supposed to be cute and...do things for the person they love and...bake."
    s "What an archaic way of looking at the roles of a housewife. Get with the times, Karin."
    ka "...I'm sorry?"
    s "All that really matters is finding someone whose tastes are in your favor."

    scene karinseconddate17
    with dissolve

    ka "Easier said than done."
    ka "At this rate, I’m going to wind up marrying a girl and raising a family of adopted children and driving them all to[school] in my mini-van."
    ka "And on the mantle where our family picture hangs, there will sit a lone soccer-trophy serving only to remind me of the future I could have led if I had just worked harder..."

    scene karinseconddate18
    with dissolve

    ka "But then one day, my adopted son will be drafted to Manchester United and I’ll be able to live out my dreams vicariously through him!"
    ka "He’ll grow old and raise a beautiful family and I’ll become the cool grandma who smothers her grandchildren with affection and lets them eat cereal for dinner."

    scene karinseconddate19
    with dissolve

    ka "But then my wife will be diagnosed with a life-threatening illness and be given only six weeks to live."
    ka "And in those final weeks, I will realize that it was never about boys or girls...it was about love."
    ka "And even though I was hesitant and nervous to introduce her to my family at first...we really did have {i}love...{/i}"

    scene karinseconddate18
    with dissolve

    ka "But then! Out of nowhere, my second adopted son will become a doctor and find the cure!"
    ka "My wife will be healed and I will-"
    s "Karin."

    scene karinseconddate14
    with dissolve

    ka "Ah-"
    s "…"
    ka "…"
    s "You’re a bit of a daydreamer, aren’t you?"
    ka "...No."
    s "You seem to have put a lot of thought into your future for someone who is apparently having trouble figuring things out."

    scene karinseconddate9
    with dissolve

    ka "O-Okay...so {i}maybe{/i} I do get lost in daydreams from time to time...but so does every girl."
    ka "We’re predictable. I understand how we work."
    ka "But when it comes to boys...I really have no idea."
    ka "I see them and my mind is just like “OH GOD! WHY DID I HAVE TO BE BORN WITH BROAD SHOULDERS?” and stuff."

    scene karinseconddate1
    with dissolve

    ka "But thanks for spending time with me regardless...even if it’s just to...develop a better relationship with the co-captain."

    "I find it surprising that Karin is able to stay so humble despite having what so many other people work tirelessly to obtain."
    "To see someone like her, who even [teenage]girls go out of their way to confess to, not realize how wonderful she is at first glance is truly a spectacle."

    s "I’m spending time with you because I want to spend time with you."

    if bonus == True:
        ka "You really shouldn’t say things like that to girls my age...We’ll get the wrong idea."
        s "Then get the wrong idea."
        ka "I’d really rather not. The wrong idea would give me a heart attack."
    else:
        s "Platonically, of course."

    scene karinseconddate9
    with dissolve

    ka "And I’ve already done a lot of running and blah blah blah blah blah boys are scary."
    s "Everything is scary. Welcome to life."

    scene karinseconddate20
    with dissolve

    ka "Huh?"
    s "Sorry. I almost let my cynical side slip out."
    s "I don’t think you’ve had the misfortune of seeing that part of me yet."
    ka "Are you normally a cynical person?"
    s "More or less."
    ka "I had no idea..."
    ka "I learned something about you today..."
    s "It’s not a very exciting or interesting thing to learn, though."

    scene karinseconddate21
    with dissolve

    ka "I...learned a thing about a boy..."
    s "...Karin?"

    scene karinseconddate1
    with dissolve

    ka "Ah! Sorry! I just got...weirdly happy all of a sudden!"
    ka "Totally not because we’re getting closer or anything! That would be like, {i}so{/i} weird, right?"
    ka "Hahahahahah!"
    ka "So weird!"
    s "...Right."
    s "Well, let’s call it here for today."
    s "Did you maybe want to get dinner on the way home or something?"

    scene karinseconddate8
    with dissolve

    ka "Dinner?! "
    ka "I don’t know what that is!"
    ka "I mean, I do know what it is!"
    ka "I have no idea why I told you I didn’t!"
    ka "I...umm!"

    scene karinseconddate11
    with dissolve

    ka "OKAY, SEE YOU!"

    scene black
    with dissolve2

    "Karin nervously hops off of the bench and runs over to a small leather bag, picking it up and slinging it over her shoulder as she jogs out of the park."
    "She’s still utterly terrified of me, sure, but at least she was able to smile more than normal today."

    if bonus == True:
        "I wonder how much longer it will be before she starts looking at me as a human being rather than a walking penis monster?"
    else:
        "I wonder how much longer it will be before she starts looking at me as a human being rather than a monster?"

    "But hey, that nervousness is one of her greatest charms."

    if bonus == True:
        "The other of which is her thighs."
        "Those two elements combine to make a wonderful human, and I’m glad that we get to spend time together like this..."

    $ renpy.end_replay()
    $ karindate5 = True
    $ karin_love += 1
    stop music fadeout 5.0

    "{i}Karin’s affection has increased to [karin_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label karindate10:
...
```

## Code that triggers this event
File: \game\KarinEvents.rpy
Code:
```python
...
label callkarinafternoon:
    if karin_love >= 0 and karindate1 == False:
        jump karindate1
    if karin_love >= 5 and day103 == True and karindate5 == False:
        jump karindate5
...
```