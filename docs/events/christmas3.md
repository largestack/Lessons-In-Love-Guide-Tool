# Fuck Christmas
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmas3&go=Go)


Part of event chain [Patent-Pending](./christmas2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmas3
* Group: Main
* Triggered by label: christmas2x

## Event code
File: \game\script.rpy
Code:
```python
...
label christmas3:
    scene christmasyay
    with dissolve2
    play music "christmasyay.mp3"

    "I hate Christmas."
    "And despite not knowing much about my previous life or my opinions on the holiday when I was younger, I have a feeling I hated it then, too."
    "Sure, the cold is nice. But are the bright lights and all the decorations really necessary?"
    "And it’s not even always cold on Christmas to begin with, so the one good thing I was able to think up off the top of my head has already gone out the window."
    "But maybe, in some sort of Christmas miracle like you’d see in those old American movies-"
    "I’ll have a good time this year."

    if bonus == True:
        "I mean, the girls in my class are nowhere near my family (Except for Ami and kind of Ayane, I guess)..."
        "But at least I’ll be surrounded by people who I don’t inherently despise instead of some drunk [uncle] or dying grandmother."
        "It’s kind of nice having dodged such a dangerous bullet in the form of this party, though."
        "Considering that Christmas in Japan is more of a time for couples to spend together and I am involved in a number of illicit relationships right now..."
        "Not having to choose which girl takes up most of my time today is definitely a good thing."
        "I’m going to need a bigger Christmas miracle than just that, though, if I’m going to be able to ignore all of the {i}joy{/i} I expect to endure today."

    scene sky
    with dissolve2

    "The day gets off to an inopportune start with none of that fluffy, white stuff coming out of the sky."
    "Thankfully, the lingering cold from last night’s snowfall sticks around just like the powder that came with it-"
    "And I crunch my way down the street with Ami, Ayane, and Maya as we head toward the store to buy some things for tonight."
    "Even though everyone passed out extremely early last night, we were able to salvage most of the stuff I bought with Maya- save a few pints of ice cream that never made it into the freezer."
    "Again, going to need a bigger Christmas miracle than just this to get through the day without a frown consuming my face- reddish and dry from being beaten by the wind."

    scene noonsky
    with dissolve2

    "Another bad thing happens before we’re able to make it to the hotel."
    "Apparently, the girls wanted to go look at Christmas trees for my house because that is a thing I’m supposed to buy, I guess."

    if bonus == True:
        "Damn [niece] and her friends can’t even be Japanese correctly. Why are we going all out for a holiday that’s supposed to be centered around sex and fried chicken?"

    "This is stupid."
    "I hate Christmas."
    "I really do."

    a "Sensei! I want this one!"
    s "No."
    ay "Oh! What about this one?!"
    s "That one wouldn’t even fit in our house."
    m "How about this?"

    "I turn around to find Maya holding up a twig that fell out of a tree and, for the first time probably ever, I think she’s actually kind of funny."
    "Also, twigs are cheap, so I easily decide on our Christmas tree for the-"

    a "If you even think about humoring her I’m gonna log into your Amazon account and order like four trees in the middle of the night."
    s "But you don’t know my-"
    a "I do. It’s Boobies123. You use the same password for everything."
    ay "He does?"

    if bonus == True:
        ay "So I could log in to his LINE account and see if he’s been sending naughty pics to anyone else in class?"
        s "Why did you add an ‘else’ to that? I haven’t sent any to you and that insinuates I have."
    else:
        s "I hate that password and want a new one. I just don't know how to change it."

    m "You’re disgusting."
    s "Are you not listening? I just said I never sent anything like that."

    scene black
    with dissolve2

    "I hate Christmas."
    "So no Christmas tree was purchased today."
    "I like Ami, though. And I’m weak around cute girls, so I’ll probably wind up caving and buying one sooner or later."
    "But for now, there are other, more important matters to attend to."
    "We’re supposed to meet everyone at some hotel in the busiest part of town- kind of halfway between where we go to[school] and where Futaba’s friend with the glasses goes."

    scene christmasgreeting1
    with dissolve2

    "And eventually, we get there."
    "I’m greeted by a peculiar sight once we enter, though."

    scene christmasgreeting2
    with dissolve

    s "Karin?"
    ka "Uhh, hey! Fancy meeting you in the place that we’re inside of right now. Which is a hotel."
    s "Thanks. I had no idea."
    s "Do you work here?"

    scene christmasgreeting3
    with dissolve

    ka "Umm...no. But the girl at the desk was having some sort of emergency and I kind of volunteered to just...take her place."
    ka "But I have no idea what I’m doing and I don’t think I’m even technically allowed to be back here."
    ka "And now you’re here and I’m even more nervous and just hoping that you don’t need to check in or- yeah."
    s "Oh. Well I do. "
    s "But I can wait until the other person gets back."

    f "There’s no need for that, Sensei. Makoto handled it a little while ago."

    scene christmasgreeting4
    with dissolve

    s "Oh. You guys were here too? I didn’t even see you."
    ka "Oh, okay. I guess I’ll just keep standing here and talking to myself, then..."
    t "Are you ready for a large man to climb down your chimney and eat all of your food?"
    s "I would be if Santa Claus ex-"

    scene christmasgreeting5
    with dissolve

    f "STOP!"
    t "...?"
    s "What’s {i}your{/i} problem?"

    scene christmasgreeting6
    with dissolve

    f "I have no problem since {i}Santa Claus exists and everyone believes in him.{/i}"
    t "Obviously. Why would anyone doubt the existence of a man who defies the laws of physics by inserting himself into spaces he clearly is not supposed to fit."

    "And here I was thinking Santa and I had nothing in common."

    s "Anyway, what are you guys up to? "
    s "If Makoto checked in, shouldn’t you be up in the room?"

    scene christmasgreeting7
    with dissolve

    f "Yes, but...Molly has been in the middle of something since we got here and is refusing to go up to the room until she’s done."
    s "Well what’s she doing? Playing a game?"
    mo "GIVE...ME...MY...GEO...BOY!"
    s "…"
    s "I don’t know what that means."
    t "Just pretend you do. It gets me by."
    s "It really doesn’t, though, Tsuneyo."

    scene christmasgreeting8
    with dissolve

    t "Ah-"
    s "I’m surprised you stuck around, Futaba. I figured you’d be with Rin or something."
    f "Yeah, well...I kind of got absorbed in Molly’s efforts and have been cheering her on from the sidelines."
    mo "I need you here so I can absorb your energy."
    f "And there’s that. She needs to...absorb my energy."
    s "Right..."

    "I turn around to tell Ami and the others that we should probably be heading upstairs to thank Makoto, but..."

    s "Where did my [niece] go?"

    scene christmasgreeting9
    with dissolve

    t "If you’re talking about the girl with the nice legs, she went upstairs with two others as soon as you walked in."
    s "Are you really going to address Ami as “the girl with the nice legs” every time she’s brought up?"
    t "Until proven otherwise, probably."
    s "So...if you’re all down here and everyone else is up there, who’s left? Are we missing anybody?"
    f "Are you worried that someone may have gotten lost on the way? That’s awfully considerate of you."
    s "Well, the roads looked pretty bad, so knowing everyone is still alive would be nice."

    scene christmasgreeting10
    with dissolve

    mo "Hah!"
    mo "Ohmygodohmygodohmygodohmygodohmygodohmygodohmygodohmygod!"

    scene christmasgreeting11
    with dissolve

    mo "TAKE THAT, WORLD! "
    mo "YOU THOUGHT YOU COULD RUIN CHRISTMAS FOR ME, BUT I HAVE THE POWER OF TWO MONTHS PART TIME BARISTA MONEY TO BURN IN PROTEST!"
    mo "FUCK YEAH! "
    s "Congrats on doing whatever you were trying to do, Molly."

    scene christmasgreeting12
    with dissolve

    mo "Oh! Hello, Sir!"
    mo "Merry Christmas."
    mo "For your present, may I inform you that there are two lovely ladies behind you who seem to want your attention?"
    f "And with them, it looks like everyone is finally here."
    s "Wait, who’s behind me?"

    scene christmasgreeting13
    with dissolve

    s "Wow. You know it’s a special night when Yumi graces us with her presence."
    y "Fuck off, dickhead."
    c "Merry Christmas, Sensei~"
    c "Yumi’s broke so I made her do this one thing for me so she wouldn’t have to get me a present this year."
    y "It’s not like I would have even gotten you one anyway. Christmas is stupid. It’s just an excuse for companies to make more money and shit."
    s "Hey, it looks like we might finally agree on something."

    scene christmasgreeting14
    with dissolve

    y "Huh? Really?"
    c "Wait a minute, don’t tell me {i}you’re{/i} just as anti-Christmas as Yumi, Sensei."
    s "To be totally honest, I’m really not a fan."

    scene christmasgreeting15
    with dissolve

    if bonus == True:
        c "I implore you to look over my outfit a few more times and then reconsider."
        c "There are only so many days a year I can wear this, you know."
        y "Yup. And it only took you like two hours to get ready."
    else:
        c "Wait, what?"
        s "The smell of candy canes gives me a headache and I don't understand what eggnog is."
        c "But...you get to see me where cute things like this!"
        s "Eh. I like your normal clothes more."
        y "Looks like you spent two hours getting ready in the bathroom for nothing, Chika."

    scene christmasgreeting16
    with dissolve

    c "Well shit, Yumi! Sorry for taking so long in {i}my{/i} bathroom while you laid on {i}my{/i} bed watching {i}my{/i} TV for those two hours! "
    c "That must have been really hard on you!"
    y "It’s whatever. Just don’t come cryin’ to me when you get a cold and have to sleep in the dorm room instead of your house every night."
    y "You were complainin’ the whole way here about how cold you were and shit and I can’t blame you since you’re dressed like a fuckin’ holly-jolly ho-bag."

    scene christmasgreeting17
    with dissolve

    c "You don’t think I look like a holly-jolly ho-bag, do you, Sensei?"

    menu:
        "I think you look great":
            if bonus == True:
                s "Of course not. I think you’re adorable."

                scene christmasgreeting18
                with dissolve

                y "Hah...here we go."
                y "Hotel room is upstairs. If you two are gonna get all weird with each other, at least be respectful enough to not do it in the fuckin’ lobby."
                c "You really think so?!"
                s "Of course. I can’t imagine many other girls being able to pull that off without looking a little too...promiscuous."
                y "Isn’t that basically saying she just looks slutty but like, not {i}as{/i} slutty?"
                c "Shut up, Yumi. You’re just jealous that I was complimented and you weren’t."
                y "Yeah, that really doesn’t matter {i}at all{/i} to me..."
            else:
                s "I think you look pretty spiffy, Chika. And I can tell from here how high quality that fabric is."
                s "I just wish there was a little more of it."

            $ chika_love += 1

            "{i}Chika’s affection has increased to [chika_love]!{/i}"

        "Yumi’s got a point":
            s "I hate to break it to you, Chika...But I think Yumi’s right."

            scene christmasgreeting19
            with dissolve

            c "You do?..."
            y "You...do?"
            s "Yeah. "
            s "I mean, it’s one thing to wear something like that in private, but walking into a hotel lobby dressed that way is kind of...inappropriate."
            c "Is it...really that bad?"
            c "I knew it was showing a bit of skin but I really didn’t think it was that much of an issue."
            c "Especially with like, zero boys around."

            scene christmasgreeting20
            with dissolve

            c "I just...wanted you to think I was pretty and stuff."

            $ yumi_love += 1

            "{i}Yumi’s affection has increased to [yumi_love]!{/i}"

    s "Either way, I think you’re {i}both{/i} adorable tonight."
    s "The new hairstyles are a nice change of pace."

    scene christmasgreeting21
    with dissolve

    y "Oh, suck my dick. I look the same as always."
    c "On behalf of both of us, thank you~"
    c "I like your new shirt, Sensei. It looks slightly thicker."
    s "Thank you, Chika. I was wondering when someone would realize that."

    scene black
    with dissolve2

    "Everyone remaining in the lobby slowly but surely disperses until they all wind up in the hotel room."

    scene christmasgreeting22
    with dissolve

    "And, by association, I end up there as well."

    s "Well, I’ll be. You {i}are{/i} back to normal after all."
    mak "Back to normal? Which one of us are you talking about, exactly?"
    s "You. Last time I saw you I pushed you up against a locker."

    scene christmasgreeting23
    with dissolve

    mak "Wha-?!"
    mak "I don’t know what sort of strange fantasies you have about us, but I can assure you that this locker-pushing never happened!"
    mak "And anything that {i}did{/i} actually happen would best not be discussed here!"
    s "Yeah, yeah. I get it. I was just messing around with you."

    "Obviously, I wasn’t."
    "But it looks like the reset somehow...fixed Makoto- which is strange given that Maya claimed to have not known anything was different about her."
    "But, then again, I wouldn’t put it past Maya to lie about something like that and just go behind my back and fix things on her own."
    "She seems a little too independent for her own good, sometimes."

    scene christmasgreeting24
    with dissolve

    mak "More importantly, Sensei. Do you notice anything a little...different about my best friend here?"
    s "Different? You mean Miku’s hair?"
    s "Yeah. It was the first thing I noticed when I came in here."
    mi "Mm...Don’t stare at me. It feels weird."
    mak "As you can see, she’s very embarrassed."
    mak "And I’m not saying you’d be able to find any flaws in her makeover but, if you do, please keep them to yourself as I am the one who cut her hair this morning."

    scene christmasgreeting25
    with dissolve

    mi "It’s not...weird...right? "
    mi "Cause I was really tired this mornin’ and kinda just agreed to let Makoto do her thing to make me look more girly and stuff but like..."
    mi "I didn’t know she was gonna chop so much off. I keep lookin’ in the mirror and bein’ like “Woah who the heck is that?”"
    mi "And now I’m really self-conscience or whatever the word is."

    scene christmasgreeting26
    with dissolve

    mak "Self-{i}conscious{/i}. And you have no reason to be. You look adorable."
    mak "And you were complaining about your hair getting longer anyway. So now it’ll stay out of your eyes when you’re playing soccer."
    mi "I know..."
    mi "I’ve just gotta get used to it, I guess."
    mi "I was worried people were gonna think I was tryin’ too hard to...not be Miku anymore."
    s "I’m sure you’ll remain Miku no matter how you style your hair."
    s "I think you’re cute no matter what."

    scene christmasgreeting27
    with dissolve

    mak "Okay, now let’s not get {i}too{/i} complimentary, Sensei. Please remember that Miku is one of your students and that I will report anything unsavory you have to say about her."

    if bonus == True:
        "Says the girl who I deflowered at a Halloween party."

    s "Report whatever you want. I’ve got some other people to greet anyway. "
    mak "Yes, yes. I completely understand."
    mak "But do know that this is a relatively small hotel room and I’m sure to hear it if you decide to hit on any of these wonderful [young_girls]."

    if bonus == True:
        s "Thanks, Makoto. I’ll keep that in mind."
    else:
        s "I would never."

    scene christmasgreeting28
    with fade

    m "…"
    a "…"
    m "Do you feel at all strange knowing that we’re sitting on a bed with two swans kissing behind us?"
    a "I was hoping you weren’t going to mention that."
    m "Why are those even here?"
    m "What kind of hotel room is this?"
    a "Well, you know...Christmas is a popular day for dates, so..."
    a "Maybe the hotel got the...wrong idea or something?"

    if bonus == True:
        m "Or they watched fourteen girls come up here with one man and are going to tell this story for the rest of their lives."
    else:
        m "Or maybe this is a hotel {i}for{/i} swans and we just booked it on accident."

    a "Yeah...or that."
    m "They should have brought up more swans."
    a "…"
    m "…"
    m "Merry Christmas, Ami."
    a "Merry Christmas, Maya..."

    scene christmasgreeting29
    with fade

    s "Hey, you two. How are you doing?"
    sa "Hi, Sensei..."
    sa "M...Merry Christmas..."
    r "…"
    s "…"
    sa "…"
    s "What’s going on with Rin?"
    sa "Oh, she’s texting a friend of hers..."
    sa "I’m just...standing here since Ayane is busy and...I don’t really talk to anyone else."
    sa "But now you’re here, so..."
    sa "I’m going to talk to you...if that’s okay."
    s "Of course it’s okay. It’s not like Rin to ignore me, though."

    scene christmasgreeting30
    with dissolve

    r "Huh? Rin? That’s me."
    r "I heard my name."

    scene christmasgreeting31
    with dissolve

    r "Oh! Sensei! Merry Christmas!"
    s "Merry Christmas. What’s this about talking to a friend?"
    s "You know you’ve already got one friend beside you just...standing there, right?"
    sa "It’s okay...I’m used to being forgotten..."

    scene christmasgreeting32
    with dissolve

    r "Oh, crap! I’m sorry, Sana! I was just reading this one thing Otoha sent me and I got lost in thought."
    r "I’ll do better. Promise!"

    if cafe35 == True:
        s "Otoha? That name sounds familiar."

        scene christmasgreeting33
        with dissolve

        r "She’s the girl we saw playing guitar in the park that one time. "
        r "I wound up bumping into her again {i}totally by accident{/i} and we exchanged numbers."
        s "You put some strange emphasis on “totally by accident” there."
        r "No idea what you’re talking about."
        r "But yeah, we’re friends now."
        r "But I hereby give you permission to confiscate my phone if I get too absorbed in it."
        r "Otoha’s cool, so she’ll understand."
        s "Duly noted."

    else:
        s "Otoha? That’s a name I’ve never heard before."

        scene christmasgreeting34
        with dissolve

        r "Probs cause it’s a girl you’ve never met before."
        r "I bumped into her at some park near my old[school] with Futaba a while back."
        r "She’s this super talented musician and she’s crazy pretty and I’m definitely not becoming obsessed or whatever."
        sa "It...sounds like you are..."
        r "Okay, maybe just a little bit."
        r "But still, I hereby give you permission to confiscate my phone if I get too absorbed in it."
        r "Otoha’s cool, so she’ll understand."
        s "Duly noted."

    scene christmasgreeting35
    with dissolve

    sa "So, umm...Sensei..."
    sa "Did you...bring a present for your Secret Santa...person?"
    r "Oooooh yeah, we’re supposed to leave ‘em near the door. "
    r "Can you tell us who you got? As long as it’s not either of us, of course."
    s "…"
    sa "…"
    r "…"

    scene christmasgreeting36
    with dissolve

    r "You completely forgot, didn’t you?"
    s "Yes, but in my defense, it’s less of me forgetting and more of me never finding out in the first place."
    r "I literally watched you pull a name out of a hat."
    sa "That’s...not good..."
    sa "You’re the one who was keeping track of the names so...I don’t know who you can even ask..."
    s "That does not sound like a thing I would ever do, but I’ve already thought up a solution."
    r "What is it? Gonna wait until everyone else exchanges gifts and then just keep an eye on who the one person to not get any is?"
    s "Oh come on, even I wouldn’t stoop that low."

    "Fuck. She got me."
    "Maybe Maya will know?"
    "She knew all about this get together so...maybe she’ll remember who I’m supposed to give a present to?"
    "I’ll have to pull her aside when she’s not...on a swan-bed with my [niece]."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ christmas3 = True

    "………"
    "……"
    "…"
    "{i}Meanwhile...{/i}"

label christmas4:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
"And even though that’s something that would creep out a lot of people, I can feel myself getting harder just thinking about it."

    s "Ayane..."
    ay "{i}Mm...yeah...it’s...okay...cum...whenever you want...{/i}"

    "Her words are hard to make out and muffled by the sound of her hand, desperate to prevent anyone in the house from hearing us-"
    "But I’m pretty sure she’s fine with me finishing any second now. "

    scene ayanesneaksin19
    with dissolve

    ay "{i}Mmh...mm...ahh...fuck...yes...yes...cum for me...{/i}"
    ay "{i}Look at me and...fill my pussy up...[ayanemaster]...{/i}"

    "I can feel the muscles inside of Ayane beginning to expand and contract as I rapidly continue to thrust upward."
    "Her eyes lock with mine and between each violent upward motion, I realize that she can go an extraordinarily long time without blinking."
    "Is that just a random pre-orgasm thought to try and prevent myself from cumming?"
    "Yes."
    "Does it work?"

    with sexfade
    with sexfade
    scene ayanesneaksin20
    with cumflash
    with hpunch

    "No."

    ay "Ahh...ah...hah...hah..."
    ay "Fuck...wow...oh my god..."

    "Instead of crying out in pleasure like normal, Ayane manages to stifle almost all noise entirely and allows her lower body to do the talking instead."
    "Her hips begin to violently shake as a sudden intense increase in moisture swallows me whole."
    "It’s hard to tell if it’s from her or myself given that I’m not completely submerged in her-"
    "But either way, it feels {i}fucking amazing...{/i}"

    scene ayanesneaksin21
    with dissolve

    ay "Heheh~"
    ay "Impressed?"
    s "Impressed by what?"
    ay "My new secret technique. The patented {i}Ayane Amamiya Silent-Orgasm.{/i}"
    s "If you’re going to patent it, you should probably remove your name so people don’t have to associate it with you every time they do it."
    ay "Or, instead, how about I rename it the {i}Ayane Amamiya Plus Her Beloved Teacher and His Huge Penis Silent-Orgasm.{/i}"
    s "That’s just way too many words for a thing that can’t even be patented in the first place."

    scene ayanesneaksin22
    with dissolve

    ay "Heh~ I guess you’re right."
    ay "But now you know how I’m able to keep quiet when I touch myself to all of the pictures I candidly took of you while you weren’t paying attention."
    s "You need to stop saying that {i}and{/i} doing that before I start actually worrying about my safety around you."
    ay "I took another one before I woke you up tonight."
    s "What did I just say?"
    ay "I don’t know. I was too distracted by how much I love you."
    s "Hah..."
    ay "I should probably go now, though."
    ay "Though, I will say, I’m going to feel very inappropriate sleeping between two girls with all of your cum still floating around inside of me."
    s "Well, yeah. It’s definitely inappropriate when you say it like that."
    ay "And even more inappropriate since one of those girls is your [niece]."
    s "Yes, Ayane. Thank you for reminding me that we are engaged in an illicit relationship behind my [niece]’s back."
    ay "It won’t be illicit forever. "
    ay "You’re going to marry me one day."
    ay "But until then, I’ll just keep hiding your semen. "
    ay "Sound good?"
    s "Define “good.”"

    scene ayanesneaksin23
    with dissolve

    ay "How about I just say...goodnight?"

    scene black
    with dissolve2

    "Ayane slides herself off of me and quickly puts her pants back on."
    "She kisses me on the forehead, kind of like a mother would do to a child, before she leaves and, to be honest, it feels a little demeaning."
    "But it seemed to have made her happy so I don’t dwell on it."
    "…"
    "Now there’s just the issue of falling back asleep-"
    "Which would be significantly easier if I could just get the idea of Ayane’s freshly-screwed body sandwiched between Ami and Maya out of my head."

    $ renpy.end_replay()
    $ christmas2 = True
    $ ayane_lust += 1
    stop music fadeout 5.0

    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    "........."
    "......"
    "..."

    $ totaldays += 1
    $ day = 7
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date

    jump christmas3
...
```