# Slumber Party
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=slumparty&go=Go)


Part of event chain [First  Day of School](./thefirstclass.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: slumparty
* Group: Main
* Triggered by label: makotoofficemassx

## Event code
File: \game\script.rpy
Code:
```python
...
label slumparty:
    scene street_noon
    with dissolve

    play music "streetnoise.mp3" fadein 5.0

    "I wound up sitting in the office for a good hour after Makoto left, but it seems that my services as the least qualified guidance counselor to ever exist are not all that sought after."
    "But hey, at least I won't have to worry about that for the next couple days."
    "Tomorrow is Saturday, so I should finally have some free time to actually do things I want rather than just...hang around teenage girls all day."
    "Which, to be fair, is exactly what I'm going to be doing anyway. Just this time it will be out of my own free will and not determined by a schedule."
    "Either that or I won't be able to find anyone at all and I'll spend the whole day just aimlessly wandering around an unfamiliar town."
    "Something tells me my luck won't be {i}that{/i} horrible, though."
    "I mean...look where I ended up. This world is every man's dream."
    "There are millions of people who would kill to walk even a day in my brand new shoes, and I'll be damned if I don't start walking as far as I can as fast I can."
    "The only question is how I'm going to leverage this new life to get what I want out of it."
    "There are ten girls in my class right now. And if what Ami said yesterday is true, more could show up at any time."
    "That said, the best course of action would be to try and...balance out my time with all of them, right?"
    "Focusing too much on one will just wind up drawing attention to us. And even if most of the girls I've encountered so far are...{i}eccentric,{/i} I doubt any of them would be okay with-"
    "Well, pretty much {i}any{/i} of the things I want to do at this point in time."
    "I'm sure the line will be different for everyone...I just have to figure out how thin or thick those lines are and the best methods to cross over them."
    "But that's a problem I'll figure out how to deal with once I actually encounter it."
    "For now, I should be heading home."
    "I remember Ami mentioning that she was going to have Ayane and Maya stay over tonight, but I doubt that means I'll be able to spend any time with either of them."
    "They're teenage girls after all. Chances are they'll just be...gossipping in Ami's room or whatever it is girls that age do."
    "Maybe I'll just go to sleep early tonight? The closer I get to having any free time, the better. And Saturday is less than twelve hours away at this point."

    scene black
    with dissolve2
    stop music fadeout 3.0

    "Yeah..."
    "I think that's what I'll wind up doing tonight."
    "........."
    "......"
    "..."

    play sound "dooropen.mp3"
    scene lr_noon
    with dissolve

    play music "lifeismostlygood.mp3" fadein 5.0

    if bonus == True:
        "I let myself into the house after realizing that Ami forgot to lock the door."
        "And while my initial instinct is to storm into her room and reprimand her for enabling a situation that could result in her being raped and killed while I am not home, I decide against it."
        "Though, I {i}do{/i} like the idea of being able to embarrass a girl I am apparently the guardian of in front of her friends."
        "I also, however, have not ruled out the idea of sleeping with her yet. And I feel that embarrassing her now would only serve to inhibit that budding desire of mine."

        a "What?! No way! You did not!"
        s "..."

        "Yeah."
        "I'll just let girls be girls tonight."
        "I don't have to involve myself in {i}everything.{/i}"
        "Sometimes the best thing to do is just sit back and let things happen on their own."

        scene black
        with dissolve2

        "Not just because the cogs in the background are already powering a machine built to pleasure me, but because being alone can be just as fulfilling as being {i}with{/i} someone."
        "When I'm alone, I can fantasize about all I want. And, between you and I-"
        "I have very quickly learned that being a high school teacher comes with its fair share of fantasies."

        s "..."

        "I hope no one minds if I take a few of those fantasies into the bathroom for a little while."
        "........."
        "......"
        "..."

    else:
        "I let myself into the house, ready to learn."

        s "I can't wait to have a peaceful day all by myself without being bothered by my accountant or any of her friends."

    "{i}Meanwhile...{/i}"

    scene sleepover1
    with dissolve2

    ay "And {i}that's{/i} why I was permanently banned from the convenience store near the school!"

    scene sleepover2
    with fade

    m "Well, that was...certainly a story."
    a "Umm...how many convenience stores have you been banned from now, Ayane? Six? Seven?"
    ay "Something like that, but it's not really a big deal since DoorDash exists and I can just get anything I want sent right to my dorm."
    m "Yes, please brag more about how rich you are. It is a thing that we very much enjoy hearing about."

    scene sleepover3
    with fade

    ay "Hey! How is taking advantage of the DoorDash Dash Pass for the low, low cost of $9.99 per month bragging about being rich?!"
    a "That's right, Maya! The DoorDash Dash Pass is so cheap right now that virtually anyone can afford it."
    a "And with new restaurants being added to Dash Pass every day, there has never been a better time to take advantage of the opportunity."

    "{i}Lessons in Love is not sponsored by nor affiliated with DoorDash.{/i}"

    m "What's going on with you two? That's the third advertisement you've spontaneously broken into tonight."

    scene sleepover3r
    with dissolve

    ay "Is that really it? It felt like more."
    m "No wonder your family is so rich if you can't even make it through a sleepover without advertising some sort of...app or something."
    ay "Excuse me, Maya, but my family is rich because my father invented unpoppable bubble wrap. And I am very tired of reminding you about this."
    m "I am very tired of being reminded..."

    "{i}Hi, there! It's your favorite narrator here to confirm that what Ayane just said is true!{/i}"
    "{i}The Amamiya family is set for life due to the innovative and fun-destroying mind of her father.{/i}"
    "{i}Why would anyone ever think of creating unpoppable bubble wrap, you ask?{/i}"
    "{i}Good question!{/i}"
    "{i}Unfortunately, I have no idea.{/i}"
    "{i}But what I do know is that the answer will be revealed in the upcoming Lessons in Love expansion pack, “A World Without Bubbles!”{/i}"
    "{i}Pre-order your copy from GameStop today and unlock three bonus costumes for Ayane’s dad.{/i}"

    scene sleepover4
    with fade

    a "Why would someone go out of their way to just...make a normal shipping product worse?"
    a "Especially when you can visit your local FedEx store and ship anything you want for-"
    m "Ami, stop. Ayane, tell us more about why your dad is suddenly an evil human being who hates plastic bubbles."

    scene sleepover5
    with fade

    ay "Uhh...better idea: how about we {i}don't{/i} talk about my dad?"
    ay "I kind of wanted tonight to be relaxing and fun, and it's not going to be {i}either{/i} of those things if I'm forced to talk about my arch nemesis."

    scene sleepover6
    with dissolve

    a "Nemesis? Isn’t that taking things a little too far?"
    a "He's still your dad at the end of the day. Even if he's a giant jerk butt now."
    ay "Are you kidding? All he does is drink whiskey and listen to smooth jazz now."
    ay "That is super villain behavior, Ami. He is clearly my nemesis."
    m "You have a strange idea of what constitutes a “super villain” but okay."
    a "Smooth jazz? Is normal jazz...too rough for some people or something?"

    scene sleepover8
    with fade

    ay "It’s seriously unbearable. Like, he won't even {i}listen{/i} to my favorite song when I ask him to."
    m "I have heard your favorite song and want to make it formally known that I am on his side."
    ay "That's fine because Ami is still on my side. Right, Ami?"
    a "Umm..."

    scene sleepover8r
    with dissolve

    ay "Ahh! You’re so lucky! You get to live with Sensei and all I get is a borderline alcoholic with poor taste in music!"

    scene sleepover9
    with fade

    m "What is your fascination with him, anyway? He’s just some...normal old guy who also happens to be our teacher."
    m "Is that really all you look for in a partner? Age and...{i}age?{/i}"
    a "Maya, are you ever going to warm up to him?..."
    a "You two have known each other for years and I've only really seen him be nice to you."
    m "Just being nice isn’t a good enough reason to like someone. If it was, I’d like pretty much everybody. Do you think I have the energy for that?"

    scene sleepover10
    with dissolve

    ay "It's hard to put into words...but my fascination with him runs way deeper than just his age and his occupation."
    ay "Sensei...is everything I like in a man. No- he's everything I like in a {i}person.{/i}"
    ay "He’s smart...and he’s kind...and he’s funny...and-"
    m "Twice your age."

    scene sleepover11
    with hpunch

    if bonus == True:
        ay "Age is just a number, Maya! If Sensei wants me, Sensei can have me!"
    else:
        ay "This changes nothing, Maya! You'd be on my side if you understood love."

    scene sleepover12
    with dissolve

    if bonus == True:
        m "I really don't think you should be the one saying {i}age is just a number{/i} in this situation..."
    else:
        m "Oh man. You just wait until the later chapters. You don't even know what you're talking about."

    ay "Besides, it won't be weird at all a few years from now."
    m "No, it definitely still will."
    ay "Nuh-uh! We'll have a house...a dog...seven children-"

    scene sleepover13
    with hpunch

    a "Seven?!"
    a "Just what the heck do you think you're planning on doing with my uncle, Ayane?!"
    a "Do you really think I would allow {i}seven{/i} children?!"
    m "Wording it like that makes it sound like you'd be okay with less..."
    a "Answer me, damn it! What are you planning on doing, Ayane?!"

    scene sleepover14
    with hpunch

    ay "Showering him with my unconditional love!"

    scene sleepover15
    with hpunch

    a "And what if he doesn't {i}want{/i} your unconditional love?!"

    scene sleepovergun
    stop music

    ay "Then I end my life the only way I know how."

    scene sleepover16
    with dissolve
    play music "lifeismostlygood.mp3"

    a "You really need to stop carrying that thing around. You're going to accidentally hurt someone one day."
    m "Where did you even get that? Aren't guns illegal in Japan?"

    scene sleepover17
    with fade

    ay "Nothing is illegal when you're rich, unfortunately."
    m "What do you mean {i}unfortunately?{/i}"
    ay "Well, the getting anything you want part isn't unfortunate. But the being rich part kind of {i}is{/i} in a...really roundabout way that you can't really complain about without people thinking you suck."
    ay "Like, the only person in the mansion who even pays attention to me anymore is Geoffrey. And you know how Geoffrey is."

    "{i}Hey! Narrator again. Just figured I'd clue you in on Geoffrey since you haven't had the pleasure of meeting him yet.{/i}"
    "{i}He's actually a really great guy if you can look past all the scars!{/i}"
    "{i}Geoffrey is an American immigrant who works and lives in the Amamiya mansion.{/i}"
    "{i}His family was brutally murdered many years ago and he is currently working as a butler while devising a plan to avenge them!{/i}"
    "{i}But that's all I'm allowed to tell you for now since I signed an NDA!{/i}"
    "{i}Don't worry, though! You can find out more by preordering the upcoming Lessons in Love expansion pack, “A World Without Geoffrey’s Family!”{/i}"
    "{i}And if you pre-order your copy from GameStop today, you'll unlock three bonus coffins for Geoffrey’s wife!{/i}"

    scene sleepover19
    with dissolve

    a "Geoffrey! I miss him. How is he doing?"
    m "Did he ever get that thing with the Irish mafia sorted out?"
    a "Yeah, I remember him being really intense about it the last time I came over."
    ay "I think so. He disappeared for a few days a month or two ago and came back covered in blood, but he seems fine now."

    scene sleepover23
    with dissolve

    m "And on that note, I'm hungry."
    a "Blood made you hungry?"
    m "Everything makes me hungry. Were we still planning on going to that cafe Rin works at?"
    a "Didn’t you just eat karaage at the karaoke place like, two hours ago? Can't we wait a little longer?"
    m "Ami, I’m really going to need you to stop judging me if this friendship is going to continue."
    a "Just eat something here. It's basically your house too, so you can help yourself to anything you can find in the fridge or the pantry."
    m "I hope you realize how dangerous what you just said to me is."

    scene sleepover24
    with dissolve

    ay "I can heat something up for Maya. I have to get up to go to the bathroom anyway."
    a "Can you microwave some popcorn while you're in the kitchen as well? Sensei says that watching a movie without popcorn is a sin and I don't want God to kill me."
    m "I second the popcorn motion, but for reasons not pertaining to any higher power."

    scene black
    with dissolve2
    stop music fadeout 10.0

    ay "Yup! I'll be back in a few, so don't miss me too much!"
    m "Bring drinks too. As quickly as possible. I require all of them."
    a "Maybe we should just buy a second fridge for you to use whenever you come over?..."
    "........."
    "......"
    "..."

    play sound "slidedoor.mp3"
    "{i}Roughly thirty seconds later...{/i}"

    scene newchu1
    with dissolve2

    ay "Wha-"
    s "Oh. Hey, Ayane."
    s "The bathroom is in use right now."
    ay "..."
    s "..."

    scene newchu2
    with dissolve

    ay "..."
    s "..."

    scene newchu1
    with dissolve

    ay "..."
    s "..."

    scene newchu3
    with dissolve

    ay "..."
    s "..."
    ay "That..."
    ay "That's a really big penis..."
    s "Thanks. I appreciate that."
    ay "..."
    s "..."

    scene newchu4
    with dissolve

    ay "Okay. I'm gonna go die now."
    s "Okay. I'll be out of here in a few minutes if you need to use the bathroom."
    ay "You can't pee when you're dead, Sensei."

    scene newchu5
    with dissolve
    play sound "slidedoor.mp3"

    s "..."
    s "No...No, I guess you can't."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Several seconds later...{/i}"

    scene newchu6
    with hpunch
    play music "rapid.mp3"

    ay "OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD OHMYGOD."
    ay "That happened. That just happened. I saw it. I actually saw it. He saw me see it. I saw him see me see it. Oh my god."
    ay "How long did I stare for? Seconds? Minutes? Days? What time is it? What am I doing here? Who am I?"
    ay "All I know is penis. All I know is penis. All I know is penis. All I know is-"
    m "Uhh...what the fuck are you doing?"

    scene newchu7
    with dissolve

    ay "I..."
    ay "I don't know anymore, Maya."
    ay "It happened so quickly...I couldn't even think straight."
    ay "It's like...my mind was telling me to move forward. But before I knew it, I was out here in the hallway again...contemplating life and what has become of me."
    m "You were gone for literally two minutes."

    scene newchu8
    with dissolve

    ay "That's it?! It felt like I was in there for days!"
    m "Okay well, you're being gross and I'm just going to make my own food because this is obviously about something I am very much not interested in."
    ay "Will you sleep next to me tonight? I don't know if I'll be able to fall asleep if I'm by myself. I just...keep seeing it. It's in my head, Maya. {i}It's in my head.{/i}"
    m "What is in your head? What are you- oh."
    m "Oh...ew..."

    scene newchu9
    with dissolve

    ay "Do you...think Ami has also seen-"
    m "Shut up. Shut up, shut up, shut up. I never heard this and I am now going to go back to the reason I came out here."
    m "Goodbye and please don't ever bring this up again. Thanks."
    ay "Oh my god...Oh my god...Oh my god..."
    ay "Oh my god..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "{i}And that was the first time Ayane ever saw a penis in real life...{/i}"
    "{i}Some say, she's still immobilized outside of that bathroom door to this very day...{/i}"
    "........."
    "......"
    "..."

label afterbrscene:
    scene bedroom_night
    with dissolve2

    "I walk into my room and immediately collapse onto the bed."
    "I have no idea what the future implications of Ayane walking in on me are but, if there is {i}anyone{/i} that is bound to be okay with something like that, it's her."
    "I can't say I expected her to just run away, though. And, who knows? Maybe if she actually knew what she was walking into, she wouldn't have run at all."
    "Regardless, I have no regrets and I am glad we got this out of the way sooner rather than later."
    "Because even if nothing comes of it, I know for a fact that the image of me is now engraved into her mind."
    "Either way, my new life of attempted debauchery and depravity begins tomorrow."
    "Ayane just happened to get a bit of a head start to the party."

    scene black
    with dissolve2

    "Goodnight, world."
    "Please keep whatever dreams you were thinking of gracing me with to yourself, for I am about to fall asleep {i}in{/i} one-"
    "One that I will hopefully remain in forever."

    s "..."

    "I will make the most of this life."
    "I will live for myself."
    "And if others get hurt in the process, I will do what I do best and write them off."

    s "..."

    "A voice in the back of my mind reminds me that none of this is real."
    "A second one fights against it."
    "A third carries me off to sleep."

    $ renpy.end_replay()
    $ sleepover = True

    "{i}From this point on, you will be able to make decisions that will impact your relationships with every character in the game.{/i}"
    "{i}Weekends will give you a morning, afternoon, and night phase.{/i}"
    "{i}Each phase gives you time to hang out with one girl. But each girl is only available at specific times in specific places each day.{/i}"
    "{i}You will eventually have the option to call the girls and bypass this, but you must first acquire their phone numbers.{/i}"
    "{i}You will soon find that certain actions or certain events will require you to be in the right place at the right time.{/i}"
    "{i}And if you get lost, remember that's exactly where I want you.{/i}"
    "{i}On school days, you will only be able to act freely at night. The morning and afternoon will be consumed by class and counseling.{/i}"
    "{i}Remember, many events in this game will be locked behind others. Focusing on one character is both not advised and not possible.{/i}"
    "{i}Oh, but remember this more than anything else-{/i}"
    "{i}This world was made for you.{/i}"
    "{i}Please enjoy it to your heart’s content.{/i}"

    stop music fadeout 3.0

    "………"
    "……"
    "…"

    jump advancetosat

label advancetosat:

    $ totaldays += 1
    $ day += 1
    if day == 6:
        hide friday onlayer date
        show saturday onlayer date
        jump saturdaymorning
    else:
        jump saturdaymorning

label saturdaymorning:

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

    if ((totaldays >= 220) and (day220 == False) and (chap1point >= 90) and (happypoint >= 10 or (happypoint + happymiss == 10)) and (chikapoint >= 13) and
        (yumipoint >= 12) and (ayanepoint >= 18 or (ayanepoint + ayanemiss == 18)) and (sanapoint >= 14) and (makotopoint >= 16) and (mikupoint >= 13) and
        (rinpoint >= 16 or (rinpoint + rinmiss == 16)) and (futabapoint >= 19 or (futabapoint + futabamiss == 19)) and (amipoint >= 14 or (amipoint + amimiss == 16)) and
        (mayapoint >= 12) and (mollypoint >= 6) and (tsuneyopoint >= 6) and (sarapoint >= 5 or (sarapoint + saramiss == 5)) and
        (harukapoint >= 6 or (harukapoint + harukamiss == 6)) and (karinpoint >= 3) and (kirinpoint >= 3) and (kaoripoint >= 3) and (makipoint >= 2) and (chinamipoint >= 2) and (day == 6)):
            jump day220
    if day == 6 and totaldays >= 370 and day355 == True and karindate20 == True and chinamidate20 == True and utadorm20 == True and sanadorm50 == True and osakodojo1 == True and kirindate25 == True and secondbeach1 == False:
        jump secondbeach1
    if totaldays >= 464 and christmastwo20 == True and day == 6 and mayafestival1 == False:
        jump mayafestival1
    if utamaid25p2 == True and day == 6 and iodorm25 == True and iospecial30 == False:
        jump iospecial30

    scene bedroom_day
    with dissolve2

    "{i}[totaldays] Days have passed...{/i}"

    if totaldays >= 24 and day24 == False:
        jump day24
    if totaldays >= 60 and day56 == True and aminew1 == True and aminew2 == False:
        jump aminew2
    if totaldays >= 80 and day72 == True and day80 == False:
        jump day80
    if totaldays >= 102 and day == 7 and day96 == True and mayadorm15 == True and letterttrack == True and howifeeltrack == True and day102 == False:
        jump day102
    if totaldays >= 174 and day154 == True and amidorm15 == True and futabadorm15 == True and day79 == True and makotonew3 == True and kirindate1 == True and ramen1 == True and mollydorm10 == True and rindorm25 == True and bar10 == True and day == 6 and beachvacation1 == False:
        jump beachvacation1
    else:
        "I wake up to sunlight pouring in through the window."

    "What should I do today?"

    menu satmorningmenu:
        "Go somewhere":
            "Where should I go?"
            menu:
                "Archery Range" if chapthreeactive == True:
                    "Who do I want to spend time with?"
                    menu:
                        "Kirin":
                            jump kirinarchery
                        "Touka":
                            jump toukaarchery
                        "Uta":
                            jump utaarchery
                "Koi Cafe" if firsttimeamisroom == True:
                    if harukadate1 == True:
                        "Who do I want to spend time with?"
                        menu:
                            "Rin":
                                jump cafe
                            "Haruka":
                                if harukafirstlust == True:
                                    "What do I want to do?"
                                    menu:
                                        "Hang out":
                                            jump harukacafe
                                        "Quickie (Doggystyle)" if bonus == True:
                                            jump harukacafedogrep
                                        "Hug Really Quickly" if bonus == False:
                                            jump harukacafedogrep
                                else:
                                    jump harukacafe
                    else:
                        jump cafe
                "Library" if firsttimeamisroom == True:
                    jump library
                "Pool" if chapthreeactive == True:
                    jump mikupool
                "Soccer field" if firsttimeamisroom == True and chapthreeactive == False:
                    if soccer20 == True:
                        "Who do I want to spend time with?"
                        menu:
                            "Miku":
                                jump soccerfield
                            "Karin":
                                jump soccerfieldkarin
                            "Kirin":
                                jump soccerfieldkirin
                    else:
                        jump soccerfield
                "Ami's Room" if christmas7 == False:
                    jump amisroom
                "Maid Cafe" if christmas7 == True:
                    jump amimaidhub
                "Park" if day288 == True:
                    if otohadorm1 == False:
                        "I should make sure Otoha is settled into the dorm first before visiting her at the park."
                        jump satmorningmenu
                    else:
                        jump otohapark
                "Streets" if day304 == True and chapthreeactive == False:
                    jump toukastreets
                "New Hope Cathedral" if buckettoken == True and day == 7:
                    jump bucketscene
                "=D" if swimming == True:
                    jump swimming
                "Go Back":
                    jump satmorningmenu

        "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
            jump phone_morning

        "Call someone" if use_new_phone_ui == False:
            jump callmorning

        "Use the computer":
            jump computer

        "Wait until afternoon" if firsttimeshrine == True:
            s "It's still too early to do anything...I'll just sit around for a few hours or something."

            scene black
            with dissolve
            stop music fadeout 3.0

            "........."
            "......"
            "..."

            jump saturdayafternoon

label saturdayafternoon:

if totaldays >= 38 and firsttimepornshop == True and day36 == True and day38 == False:
    jump day38
else:
    "Now what should I do?"

    menu satafternoonmenu:
        "Go somewhere":
            "Where should I go?"
            menu:
                "Archery Range" if chapthreeactive == True:
                    jump tsuneyoarchery
                "City Streets" if firsttimeshrine == True:
                    jump streets
                "Shopping Mall" if firsttimeshrine == True:
                    jump mall
                "Shrine":
                    jump shrine
                "Dojo" if firsttimeshrine == True:
                    if osakodate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang Out With Ayane":
                                jump dojo
                            "Hang Out With Osako":
                                jump osakodojo
                    else:
                        jump dojo
                "Bathhouse" if day247 == True:
                    jump bathhouse
                "Library" if day288 == True:
                    if otohadorm1 == False:
                        "I should make sure Nodoka is settled into the dorm first before visiting her at the library."
                        jump satafternoonmenu
                    else:
                        jump nodokalibrary
                "Go Back":
                    jump satafternoonmenu

        "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
            jump phone_afternoon

        "Call someone" if use_new_phone_ui == False:
            jump callafternoon

        "Wait until night" if firsttimeshrine == True:
            s "I'll just...walk around until it starts to get dark, I guess."

            scene black
            with dissolve
            stop music fadeout 3.0

            "I decide to wander around for a few hours."
            "........."
            "......"
            "..."

            jump saturdaynight

        "Wait until morning" if anewkey == True:
            jump goodboy

label saturdaynight:

if totaldays >= 130 and day128 == True and day > 5 and day130 == False:
    jump day130
if totaldays >= 344 and day340 == True and amiinvite3 == True and day == 6 and day344 == False:
    jump day344
else:
    "It's late, but I should be able to fit one more thing in today..."
    "What should I do now?"

    menu satnightmenu:
        "Go somewhere":
            "Where should I go?"
            menu:
                "Bar":
                    if sarasex == True or saradate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Sana":
                                jump sanasbar
                            "Hang out with Sara" if saradate1 == True:
                                jump sarasbar
                            "Hang out with Yuki" if chapthreeactive == True:
                                jump yukibar
                            "Missionary Sex (Sara)" if sarasex == True and bonus == True:
                                jump saramissionaryanim
                            "Cunnilingus (Sara)" if saralust5 == True and bonus == True:
                                jump saraeatoutanim
                            "Blowjob (Sara)" if saralust10 == True and bonus == True:
                                jump sarabjreplay
                            "Hug Her Tightly (Sara)" if sarasex == True and bonus == False:
                                jump saramissionaryanim
                            "Appreciate Her (Sara)" if saralust5 == True and bonus == False:
                                jump saraeatoutanim
                            "Tightly Hug And Appreciate Her (Sara)" if saralust10 == True and bonus == False:
                                jump sarabjreplay
                    else:
                        jump sanasbar
                "Porn Shop" if bonus == True:
                    if makidate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Makoto":
                                jump pornshop
                            "Hang out with Maki":
                                jump pornshopmaki
                            "Blowjob (Maki)" if makibj == True and bonus == True and makiblock == False:
                                jump makibjanim
                    else:
                        jump pornshop
                "DVD Store" if bonus == False:
                    if makidate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Makoto":
                                jump pornshop
                            "Hang out with Maki":
                                jump pornshopmaki
                            "Blowjob (Maki)" if makibj == True and bonus == True:
                                jump makibjanim
                    else:
                        jump pornshop
                "Koi Cafe" if day154 == True and mollysad == False:
                    jump mollycafe
                "Tojo Ramen" if day154 == True:
                    if day == 7 and trinity2 == True:
                        menu:
                            "Somewhere fun":
                                jump trinity2
                            "Tojo Ramen":
                                jump ramenshop
                    else:
                        jump ramenshop
                "Maid Cafe" if day247 == True:
                    jump utamaid
                "Convenience Store" if norikofirsthall == True:
                    jump convenience
                "New Hope Cathedral" if yasufirsthall == True:
                    jump church
                "Dive Bar" if day == 5 and wakanaspecial15 == True and imanidate1 == True:
                    "Who do I want to spend time with?"
                    menu:
                        "Imani":
                            jump imanidive
                        #"Rika":
                        #    jump rikadive
                        "Wakana":
                            jump wakanadive
                "School Dorms":
                    jump dorms
                "Go Back":
                    jump satnightmenu

        "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
            jump phone_night

        "Call someone" if use_new_phone_ui == False:
            jump callnight

        "Invite over" if use_new_phone_ui == False:
            jump inviteover

        "Go home and sleep":
            s "I'm feeling kind of tired today...Maybe I'll just head back to the house and go to sleep early?"

            "I decide to walk home."

            scene black
            with dissolve
            stop music fadeout 3.0

            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            if day >= 6:
                jump endofsat

label inviteover:

    # Use the new phone UI when enabled
    if use_new_phone_ui == True:
        jump phone_night

    "Who should I invite over?"
    if specialclassroom == True and day >= 6:
        menu:
            "There is something buried underneath your feet":
                jump specialclassroom
    else:
        menu:
            "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx" if trinity3 == True and trinity2track == True and day >= 6:
                jump trinity3
            "Ami" if christmas7 == True:
                jump amiinvite
            "Ayane" if christmas7 == True:
                jump ayaneinvite
            "Chika" if day139 == True and chikanumber == True:
                jump chikainvite
            "Futaba" if christmas7 == True:
                jump futabainvite
            "Haruka" if christmas7 == True:
                jump harukainvite
            "Kirin" if christmas7 == True:
                jump kirininvite
            "Maki" if halloweentwo13 == True:
                jump makiinvite
            "Makoto" if makotolust5 == True and day77 == True:
                jump makotoinvite
            "Niki" if norikodorm25 == True:
                jump nikiinvite
            "Noriko" if norikodorm10 == True:
                jump norikoinvite
            "Sara" if saradate1 == True:
                jump sarainvite
            "Go back":
                if day < 6:
                    jump asmenu
                if day >= 6:
                    jump satnightmenu

label endofsat:
    if day == 6:
        play sound "dooropen.mp3"
        scene bedroom_night
        with dissolve

        "I open the door and immediately collapse onto the bed."
        "Today was a good day...I should still have some free time tomorrow as well."
        "I should think carefully about how I want to spend it."

        scene black
        with dissolve

        "........."
        "......"
        "..."
        jump advancetosun
    else:
        play sound "dooropen.mp3"
        scene bedroom_night
        with dissolve

        "I open the door and immediately collapse onto the bed."
        "Today was nice, but I'll be going back to work tomorrow..."
        "I wonder if anything interesting will happen?"

        scene black
        with dissolve

        "........."
        "......"
        "..."
        jump advancetomon

label endofweekday:
    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve

    "I open the door and immediately collapse onto the bed."
    "Being around teenagers is exhausting."
    "I should probably get some sleep before heading out tomorrow..."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    if day == 1:
        jump advancetotues
    if day == 2:
        jump advancetowed
    if day == 3:
        jump advancetothurs
    if day == 4:
        jump advancetofri
    else:
        jump advancetosat


label advancetosun:
    $ totaldays += 1
    $ day += 1
    if day == 7:
        hide saturday onlayer date
        show sunday onlayer date
        jump saturdaymorning
    else:
        "ERROR ADVANCING TO SUNDAY"

label advancetomon:
    $ totaldays += 1
    $ day -= 6
    if day == 1:
        hide sunday onlayer date
        show monday onlayer date
        jump weekdaymorning
    else:
        "ERROR ADVANCING TO MONDAY"

label advancetotues:
    $ totaldays += 1
    $ day += 1
    if day == 2:
        hide monday onlayer date
        show tuesday onlayer date
        jump weekdaymorning
    else:
        "ERROR ADVANCING TO TUESDAY"

label advancetowed:
    $ totaldays += 1
    $ day += 1
    if day == 3:
        hide tuesday onlayer date
        show wednesday onlayer date
        jump weekdaymorning
    else:
        "ERROR ADVANCING TO WEDNESDAY"

label advancetothurs:
    $ totaldays += 1
    $ day += 1
    if day == 4:
        hide wednesday onlayer date
        show thursday onlayer date
        jump weekdaymorning
    else:
        "ERROR ADVANCING TO THURSDAY"

label advancetofri:
    $ totaldays += 1
    $ day += 1
    if day == 5:
        hide thursday onlayer date
        show friday onlayer date
        jump weekdaymorning
    else:
        "ERROR ADVANCING TO FRIDAY"

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
    if totaldays >= 65 and bar15 == True and cafe20 == True and day65 == False:
        jump day65
    if totaldays >= 68 and ayane_lust >= 5 and day68 == False:
        jump day68
    if totaldays >= 70 and bar10 == True and day70 == False:
        jump day70
    if totaldays >= 72 and day70 == True and day72 == False:
        jump day72
    if totaldays >= 77 and day77 == False:
        jump day77
    if totaldays >= 79 and day == 5 and chikadorm15 == True and day79 == False:
        jump day79
    if totaldays >= 83 and mikudorm10 == True and day83 == False:
        jump day83
    if totaldays >= 85 and streets10 == True and day85 == False:
        jump day85
    if totaldays >= 86 and futaba_lust >= 5 and day == 5 and day86 == False:
        jump day86
    if totaldays >= 89 and day65 == True and day89 == False:
        jump day89
    if totaldays >= 91 and day63 == True and day65 == True and day91 == False:
        jump day91
    if totaldays >= 96 and day == 1 and shrine15 == True and ayanenew1 == True and day96 == False:
        jump day96
    if totaldays >= 98 and ami_lust >= 5 and day98 == False:
        jump day98
    if totaldays >= 103 and day102 == True and day103 == False:
        jump day103
    if totaldays >= 110 and day103 == True and day110 == False:
        jump day110
    if totaldays >= 114 and day103 == True and bar20 == True and day114 == False:
        jump day114
    if totaldays >= 120 and day103 == True and day91 == True and day120 == False:
        jump day120
    if totaldays >= 121 and day85 == True and day103 == True and day121 == False:
        jump day121
    if totaldays >= 126 and day103 == True and streets15 == True and chikadorm15 == True and day126 == False:
        jump day126
    if totaldays >= 128 and day103 == True and day126 == True and day == 5 and day128 == False:
        jump day128
    if totaldays >= 138 and day103 == True and day130 == True and day85 == True and day138 == False:
        jump day138
    if totaldays >= 139 and chika_lust >= 5 and chikadorm20 == True and mall20 == True and chikadetention == True and day139 == False or chikadorm20 == True and mall20 == True and chika_lust >= 10 and day139 == False:
        jump day139
    if totaldays >= 140 and day138 == True and day140 == False:
        jump day140
    if totaldays >= 142 and amidorm15 == True and day140 == True and day142 == False:
        jump day142
    if totaldays >= 144 and day128 == True and day142 == True and day144 == False:
        jump day144
    if totaldays >= 150 and day144 == True and streets15 == True and cafe20 == True and soccer10 == True and day150 == False:
        jump day150
    if totaldays >= 153 and day150 == True and day153 == False:
        jump day153
    if totaldays >= 154 and day153 == True and day154 == False:
        jump day154
    if (totaldays >= 200 and day == 5 and beachvacation16 == True and chikainvite1 == True and harukadate1 == True and kaoridate1 == True and cafe25 == True and bar25 == True and mayadorm25 == True
    and mikudorm15 == True and streets25 == True and makotoinvite2 == True and makidate1 == True and rindorm35 == True and halloween1 == False):
        jump halloween1
    if totaldays >= 214 and makidate5 == True and halloween14 == True and makotodorm25 == True and mikudorm30 == True and amidorm25 == True and day == 1 and day214 == False:
        jump day214
    if totaldays >= 215 and day214 == True and day == 2 and day215 == False:
        jump day215
    if totaldays >= 216 and day215 == True and day == 3 and day216 == False:
        jump day216
    if totaldays >= 217 and day216 == True and day == 4 and day217 == False:
        jump day217
    if totaldays >= 218 and day217 == True and day == 5 and day218 == False:
        jump day218
    if totaldays >= 230 and makoto_lust >= 10 and christmas7 == True and makotolust10 == False:
        jump makotolust10
    if totaldays >= 237 and day == 1 and christmas7 == True and day237 == False:
        jump day237
    if totaldays >= 239 and day == 3 and day237 == True and day239 == False:
        jump day239
    if totaldays >= 240 and day == 4 and day239 == True and day240 == False:
        jump day240
    if totaldays >= 244 and day == 1 and day240 == True and day244 == False:
        jump day244
    if totaldays >= 246 and day == 3 and day244 == True and day246 == False:
        jump day246
    if totaldays >= 247 and day == 4 and day246 == True and day247 == False:
        jump day247
    if totaldays >= 261 and day == 3 and day247 == True and kirininvite2 == True and bar35 == True and day261 == False:
        jump day261
    if totaldays >= 263 and day == 5 and day261 == True and day263 == False:
        jump day263
    if totaldays >= 264 and day == 1 and day263 == True and day264 == False:
        jump day264
    if totaldays >= 269 and day == 3 and day264 == True and day269 == False:
        jump day269
    if totaldays >= 270 and day == 4 and day269 == True and day270 == False:
        jump day270
    if totaldays >= 271 and day == 5 and day270 == True and day271 == False:
        jump day271
    if totaldays >= 272 and day271 == True and onseninvite == False:
        jump day272
    if totaldays >= 280 and day == 1 and day271 == True and rindorm45 == True and iodorm10 == True and nikidate5 == True and chikaonsen4 == True and yumidorm30 == True and norikofirsthall == True and convenience5 == True and day280 == False:
        jump day280
    if totaldays >= 281 and day == 2 and day280 == True and day281 == False:
        jump day281
    if totaldays >= 282 and day == 3 and day281 == True and day282 == False:
        jump day282
    if totaldays >= 283 and day == 4 and day282 == True and day283 == False:
        jump day283
    if totaldays >= 287 and day == 1 and day283 == True and day287 == False:
        jump day287
    if totaldays >= 288 and day == 2 and day287 == True and day288 == False:
        jump day288
    if totaldays >= 295 and day == 3 and day288 == True and chikaonsen4 == True and amidate35 == True and makotowinterbeach4 == True and day295 == False:
        jump day295
    if totaldays >= 297 and day == 5 and day295parttwo == True and day297 == False:
        jump day297
    if totaldays >= 302 and day == 3 and day297 == True and day302 == False:
        jump day302
    if totaldays >= 303 and day == 4 and day302 == True and day303 == False:
        jump day303
    if totaldays >= 304 and day == 5 and day303 == True and day304 == False:
        jump day304
    if totaldays >= 318 and day == 5 and toukadorm5 == True and utadorm10 == True and mikudorm40 == True and mollydorm20 == True and otohadorm5 == True and kirindorm20 == True and iodorm10 == True and yukidate5 == True and sanadorm40 == True and yasudorm10 == True and day318 == False:
        jump day318
    if totaldays >= 333 and dormwar17 == True and day333 == False:
        jump day333
    if totaldays >= 340 and ayanedorm35 == True and day == 2 and day340 == False:
        jump day340
    if totaldays >= 351 and thirdreset3 == True and utadorm20 == True and day351 == False:
        jump day351
    if totaldays >= 355 and day351 == True and day355 == False:
        jump day355
    if totaldays >= 400 and secondbeach18 == True and (rindate50 == True or (rindorm50special == True and rinbetrayed == True)) and ramen30 == True and mollydorm30 == True and nikidate15 == True and day == 5 and halloweentwo1 == False:
        jump halloweentwo1
    if totaldays >= 400 and day == 1 and halloweentwo13 == True and norikospecial20 == False:
        jump norikospecial20
    if totaldays >= 410 and kirin_love >= 30 and kirinsoccer25 == True and ayanelust15 == True and kirinspecial30 == False:
        jump kirinspecial30
    if totaldays >= 417 and streets40 == True and day == 5 and yumispecial45 == False:
        jump yumispecial45
    if totaldays >= 424 and kirindorm25 == True and day == 1 and chikaspecial40 == False:
        jump chikaspecial40
    if totaldays >= 455 and chikadate45 == True and yumispecial45 == True and norikodorm25 == True and nikiinvite2 == True and sarabar25p2 == True and day == 4 and christmastwo1 == False:
        jump christmastwo1
    if totaldays >= 500 and chapthree8 == True and church15 == True and yasuspecial15 == False:
        jump yasuspecial15
    if totaldays >= 514 and yasudorm20 == True and nodokadorm15 == True and day == 4 and nodokaspecial15p1 == False:
        jump nodokaspecial15p1
    if totaldays >= 522 and sadgirls7 == True and day == 5 and sadgirls8 == False:
        jump sadgirls8
    if totaldays >= 530 and iospecial30 == True and karindate25 == True and day == 1 and tsukasaspecial1 == False:
        jump tsukasaspecial1
    if totaldays >= 535 and wakanadate15 == True and day == 5 and imanispecial1 == False:
        jump imanispecial1
    if totaldays >= 540 and imanispecial1 == True and day == 2 and ayanespecial40 == False:
        jump ayanespecial40
    if totaldays >= 541 and rindorm55p2 == True and bar55 == True and day == 3 and rikaspecial1 == False:
        jump rikaspecial1
    if totaldays >= 543 and rikaspecial1 == True and osakodate20 == True and day == 5 and day543 == False:
        jump day543
    if totaldays >= 547 and day543 == True and ayanesanabeach1 == True and day == 1 and ayanespecial50 == False:
        jump ayanespecial50
    if totaldays >= 550 and ayanelust15 == True and ayanespecial50 == True and day == 4 and ayanekirintalk == False:
        jump ayanekirintalk
    elif totaldays >= 550 and ayanelust15 == False and ayanespecial50 == True and day == 4 and ayanekirintalk == False and ayanekirintalkskip == False:
        $ ayanekirintalkskip = True
    if totaldays >= 558 and ayanespecial50 == True and day543 == True and day == 5 and futabainvite3 == True and dormwartwo1 == False:
        jump dormwartwo1
    else:
        scene bedroom_day
        with dissolve2
        play sound "knock.mp3"

        a "Sensei! Breakfast is ready! Time to wake up!"

        "Ugh...Is it morning already?"

        scene black
        with dissolve

        "........."
        "......"
        "..."

        jump afterschool

label afterschool:

    if chapthreeactive == True:
        scene street_noon
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene citysnow
        with dissolve
    else:
        scene street_noon
        with dissolve

    play music "streetnoise.mp3" fadein 2.0

    "School passed by without anything interesting happening today."
    "It should be getting dark any minute now, but I still have a little time before I need to head home."

    jump afterschoolmenu

label afterschoolevent:

    if chapthreeactive == True:
        scene street_noon
        with dissolve
    elif christmas7 == True and chapthreeactive == False:
        scene citysnow
        with dissolve
    else:
        scene street_noon
        with dissolve

    play music "streetnoise.mp3" fadein 2.0

    "Hmm...I should still be able to fit one more activity in today."

    jump afterschoolmenu

label afterschoolmenu:
    "What should I do?"

    menu asmenu:
        "Go somewhere":
            "Where should I go?"
            menu:
                "Bar":
                    if sarasex == True or saradate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Sana":
                                jump sanasbar
                            "Hang out with Sara" if saradate1 == True:
                                jump sarasbar
                            "Hang out with Yuki" if chapthreeactive == True:
                                jump yukibar
                            "Missionary Sex (Sara)" if sarasex == True and bonus == True:
                                jump saramissionaryanim
                            "Cunnilingus (Sara)" if saralust5 == True and bonus == True:
                                jump saraeatoutanim
                            "Blowjob (Sara)" if saralust10 == True and bonus == True:
                                jump sarabjreplay
                            "Hug Her Tightly (Sara)" if sarasex == True and bonus == False:
                                jump saramissionaryanim
                            "Appreciate Her (Sara)" if saralust5 == True and bonus == False:
                                jump saraeatoutanim
                            "Tightly Hug And Appreciate Her (Sara)" if saralust10 == True and bonus == False:
                                jump sarabjreplay
                    else:
                        jump sanasbar
                "Porn Shop" if bonus == True:
                    if makidate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Makoto":
                                jump pornshop
                            "Hang out with Maki":
                                jump pornshopmaki
                            "Blowjob (Maki)" if makibj == True and bonus == True and makiblock == False:
                                jump makibjanim
                    else:
                        jump pornshop
                "DVD Store" if bonus == False:
                    if makidate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Makoto":
                                jump pornshop
                            "Hang out with Maki":
                                jump pornshopmaki
                            "Blowjob (Maki)" if makibj == True and bonus == True:
                                jump makibjanim
                    else:
                        jump pornshop
                "Koi Cafe" if day154 == True and mollysad == False:
                    jump mollycafe
                "Tojo Ramen" if day154 == True:
                    jump ramenshop
                "Maid Cafe" if day247 == True:
                    jump utamaid
                "Convenience Store" if norikofirsthall == True:
                    jump convenience
                "New Hope Cathedral" if yasufirsthall == True:
                    jump church
                "Dive Bar" if day == 5 and wakanaspecial15 == True and imanidate1 == True:
                    "Who do I want to spend time with?"
                    menu:
                        "Imani":
                            jump imanidive
                        #"Rika":
                        #    jump rikadive
                        "Wakana":
                            jump wakanadive
                "School Dorms":
                    jump dorms
                "Go Back":
                    jump asmenu

        "Check phone" if firsttimeshrine == True and use_new_phone_ui == True:
            jump phone_night

        "Call someone" if use_new_phone_ui == False:
            jump callnight

        "Invite over" if use_new_phone_ui == False:
            jump inviteover

        "Go home and sleep":
            s "I'm feeling kind of tired today...Maybe I'll just head back to the house and go to sleep early?"

            "I decide to walk home."

            scene black
            with dissolve
            stop music fadeout 3.0

            "........."
            "......"
            "..."

            if day < 6:
                jump endofweekday
            if day >= 6:
                jump endofsat

label callmorning:

    # Use the new phone UI when enabled
    if use_new_phone_ui == True:
        jump phone_morning

    "Who do I want to call?"
    menu:
        "Ami":
            jump callamimorning
        "Ayane":
            jump callayanemorning
        "Chika" if chikanumber == True:
            jump callchikamorning
        "Chinami" if chinaminumber == True:
            jump callchinamimorning
        "Futaba" if futabanumber == True:
            jump callfutabamorning
        "Haruka" if harukanumber == True:
            jump callharukamorning
        "Imani" if imaninumber == True:
            jump callimanimorning
        "Io" if ionumber == True:
            jump calliomorning
        "Kaori" if kaorinumber == True:
            jump callkaorimorning
        "Karin" if karinnumber == True:
            jump callkarinmorning
        "Kirin" if kirinnumber == True:
            jump callkirinmorning
        "Maki" if makinumber == True:
            jump callmakimorning
        "Makoto" if makotonumber == True and firsttimepornshop == True:
            jump callmakotomorning
        "Miku" if mikunumber == True:
            jump callmikumorning
        "Molly" if mollynumber == True:
            jump callmollymorning
        "Niki" if nikinumber == True:
            jump callnikimorning
        "Nodoka" if nodokalibrary1 == True:
            jump callnodokamorning
        "Noriko" if norikonumber == True:
            jump callnorikomorning
        "Rin" if rinnumber == True:
            jump callrinmorning
        "Sara" if saranumber == True:
            jump callsaramorning
        "Tsubasa" if tsubasanumber == True:
            jump calltsubasamorning
        "Uta" if utanumber == True:
            jump callutamorning
        "Wakana" if wakananumber == True:
            jump callwakanamorning
        "Yuki" if yukinumber == True:
            jump callyukimorning
        "Yumi" if yuminumber == True:
            jump callyumimorning
        "Go Back":
            jump satmorningmenu

label callafternoon:

    # Use the new phone UI when enabled
    if use_new_phone_ui == True:
        jump phone_afternoon

    "Who do I want to call?"
    menu:
        "Ami":
            jump callamiafternoon
        "Ayane":
            jump callayaneafternoon
        "Chika" if chikanumber == True:
            jump callchikaafternoon
        "Chinami" if chinaminumber == True:
            jump callchinamiafternoon
        "Futaba" if futabanumber == True:
            jump callfutabaafternoon
        "Haruka" if harukanumber == True:
            jump callharukaafternoon
        "Imani" if imaninumber == True:
            jump callimaniafternoon
        "Io" if ionumber == True:
            jump callioafternoon
        "Kaori" if kaorinumber == True:
            jump callkaoriafternoon
        "Karin" if karinnumber == True:
            jump callkarinafternoon
        "Kirin" if kirinnumber == True:
            jump callkirinafternoon
        "Maki" if makinumber == True:
            jump callmakiafternoon
        "Makoto" if makotonumber == True and firsttimepornshop == True:
            jump callmakotoafternoon
        "Miku" if mikunumber == True:
            jump callmikuafternoon
        "Molly" if mollynumber == True:
            jump callmollyafternoon
        "Niki" if nikinumber == True:
            jump callnikiafternoon
        "Nodoka" if nodokalibrary1 == True:
            jump callnodokaafternoon
        "Noriko" if norikonumber == True:
            jump callnorikoafternoon
        "Rin" if rinnumber == True:
            jump callrinafternoon
        "Sara" if saranumber == True:
            jump callsaraafternoon
        "Tsubasa" if tsubasanumber == True:
            jump calltsubasaafternoon
        "Uta" if utanumber == True:
            jump callutaafternoon
        "Wakana" if wakananumber == True:
            jump callwakanaafternoon
        "Yuki" if yukinumber == True:
            jump callyukiafternoon
        "Yumi" if yuminumber == True:
            jump callyumiafternoon
        "Go Back":
            jump satafternoonmenu

label callnight:

    # Use the new phone UI when enabled
    if use_new_phone_ui == True:
        jump phone_night

    "Who do I want to call?"
    menu:
        "Ami":
            jump callaminight
        "Ayane":
            jump callayanenight
        "Chika" if chikanumber == True:
            jump callchikanight
        "Chinami" if chinaminumber == True:
            jump callchinaminight
        "Futaba" if futabanumber == True:
            jump callfutabanight
        "Haruka" if harukanumber == True:
            jump callharukanight
        "Imani" if imaninumber == True:
            jump callimaninight
        "Io" if ionumber == True:
            jump callionight
        "Kaori" if kaorinumber == True:
            jump callkaorinight
        "Karin" if karinnumber == True:
            jump callkarinnight
        "Kirin" if kirinnumber == True:
            jump callkirinnight
        "Maki" if makinumber == True:
            jump callmakinight
        "Makoto" if makotonumber == True and firsttimepornshop == True:
            jump callmakotonight
        "Miku" if mikunumber == True:
            jump callmikunight
        "Molly" if mollynumber == True:
            jump callmollynight
        "Nodoka" if nodokalibrary1 == True:
            jump callnodokanight
        "Niki" if nikinumber == True:
            jump callnikinight
        "Noriko" if norikonumber == True:
            jump callnorikonight
        "Rin" if rinnumber == True:
            jump callrinnight
        "Sara" if saranumber == True:
            jump callsaranight
        "Tsubasa" if tsubasanumber == True:
            jump calltsubasanight
        "Uta" if utanumber == True:
            jump callutanight
        "Wakana" if wakananumber == True:
            jump callwakananight
        "Yuki" if yukinumber == True:
            jump callyukinight
        "Yumi" if yuminumber == True:
            jump callyuminight
        "Go Back":
            jump satnightmenu

label day5:
...
```

## Code that triggers this event
File: \game\scripts\subscribestar\inappropriatecontent.rpy
Code:
```python
...
mak "Wha-"
    a "I'm coming in!"

    play sound "dooropen.mp3"

    scene makcouch10
    with hpunch

    "Makoto pushes me away right as the door begins to open and we're able to assume unsuspicious positions impressively quick."
    "She takes a moment to straighten out her clothes and her hair, finishing just as Ami arrives at my desk."

    scene makcouch11
    with dissolve

    a "Oh hey, Makoto's here. Was I interrupting something?"
    mak "Nope! Nothing at all!"
    mak "In fact, I...I forgot I have a...thing...to go to."
    a "A thing? What kind of thing?"

    scene makcouch12
    with hpunch

    mak "A thing, okay?! That's all! Stop asking me, already!"
    a "I just-"
    mak "Wow! Look at the time! Goodbye, you two!"

    scene makcouch13
    with dissolve
    play sound "dooropen.mp3"

    "Makoto rushes out of the office, leaving me with another girl and a debilitating case of blue balls."

    s "Ami, do you understand how knocking works?"

    scene makcouch14
    with dissolve

    a "Hm? Of course I do."
    s "Really? Because you're supposed to wait until someone {i}answers{/i} to enter a room after knocking."
    s "This is a counseling office. How would you like if someone just walked in on you while you were opening up?"

    scene makcouch15
    with dissolve

    a "I’m sorry...I didn't mean anything by it."
    s "It's fine, just...what's up? What do you need?"
    a "I forgot my key to the house and I was wondering if I could borrow yours."
    s "Do we not have a spare key under the mat or something?"
    a "We used to...but somebody took it and we had to change the locks, remember? I'll go get another spare made this weekend."
    a "But for now, I kinda need yours if I'm going to be able to go home."
    a "Ayane and Maya are sleeping over tonight, so I can just let you in whenever you get back."
    s "Ahh. Yeah, I guess that’s fine."

    "Thankfully, I took note of our address in my phone so I can just use a GPS app if I can't find the way back myself."
    "With no real reason to refuse, I reach into my pocket and toss my house key over to Ami."

    scene makcouch16
    with dissolve

    "Surprisingly, she actually manages to catch it."

    a "I think that might be the most athletic thing I've ever done..."
    s "That is...very sad."

    scene makcouch17
    with dissolve

    a "It's fine. I put all of my energy into loving you anyway."

    scene makcouch18
    with dissolve

    a "But I should probably be heading out now! Any longer and Maya will probably kill me."
    a "Do you want me to pick you up anything from the convenience store?"
    s "Nah, I'll be fine. Just go have fun or whatever it is teenage girls do in their free time."
    a "That is exactly what we do in our free time, so I will do my best!"
    a "See you later, Sensei! I love you!"

    scene black
    with dissolve2

    "Ami leaves the room and I'm alone once more."
    "I think for a moment about leaving as well, but just so I can go track down Makoto and see if she wants to pick up where things left off."
    "Something tells me I should probably just leave it be for now, though."
    "It's only a matter of time until she starts seeing me in the same light that I see her in."
    "And, when that time comes, I'm sure the lights will be so bright that we'll have nothing left to do but blind one another."
    "For now, I will continue to live in the dark...lying in constant wait for the faint glow of ten young girls to seep in through the crack under the door to my heart."
    "I want to see the dust light up."

    $ renpy.end_replay()
    $ firstclass = True
    $ makoto_love += 1
    stop music fadeout 5.0

    "{i}Makoto’s affection has increased to 1!{/i}"
    "………"
    "……"
    "…"

    jump slumparty
...
```