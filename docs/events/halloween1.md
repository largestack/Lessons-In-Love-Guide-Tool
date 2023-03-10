# The Value of Sharing (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 200

* Day of week is Friday

* Event [See You in the Morning](./beachvacation16.md) (Main) is completed)

* Event [A Trip to the Moon](./chikainvite1.md) (Chika) is completed)

* Event [Drunk Again](./harukadate1.md) (Haruka) is completed)

* Event [How to Date a Human](./kaoridate1.md) (Kaori) is completed)

* Event [Good Day, Humans](./cafe25.md) (Rin) is completed)

* Event [Life is a Tomato](./bar25.md) (Sana) is completed)

* Event [FLAVOR BEAM!](./mayadorm25.md) (Maya) equal to Tru (event=mayadorm25)



## Next events

None

## Event properties

* Id: halloween1
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->halloween1

## Official wiki page

[The Value of Sharing](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween1&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label halloween1:
    scene firsthalloweenevent1
    with dissolve
    play music "justbehappy.mp3" fadein 5.0

    "I’m relaxing in my room after a long and uneventful day at[school]."
    "Well, maybe not entirely uneventful."
    "Molly took it upon herself to start hosting some impromptu game show since nothing else was going on."
    "It pretty much ruined any chance I had of sleeping through the post-lunch part of the day so, believe it or not, I’m in a pretty sour mood right now."
    "Now, I know what you’re thinking-"
    "That I’m typically so full of life and am essentially the beacon of what a self-sufficient adult male should be."
    "But I assure you-"
    "Right now, there isn’t anything that could possibly make me feel any better."

    play sound "knock.mp3"

    ay "Hi! Coming in now!"

    scene firsthalloweenevent2
    with dissolve
    play sound "dooropen.mp3"

    ay "Good evening, Sensei. How would you like to see all of us in costumes?"

    "Never mind. Life is good again."

    s "Yes, please."
    a "You’re supposed to wait until {i}after{/i} someone responds to the knock to actually go into their room, Ayane."
    a "Why doesn’t anyone understand the concept of knocking around here?"
    s "Ami, don’t you do that exact thing with my office at work all the time?"

    scene firsthalloweenevent3
    with dissolve

    a "I have special [niece] privileges! I don’t need to wait for you to answer since I have to make sure you’re okay!"
    s "Why would I be in distress in my own office?"
    a "Because I said so!"
    sa "Umm...I don’t really think I should...be in here..."
    sa "It feels a little...early..."

    scene firsthalloweenevent4
    with dissolve

    ay "Oh, stop. You’re in good hands. "

    if bonus == True:
        ay "Besides, if Sensei tries to do anything lewd to you, I’ll just sacrifice myself in your place so you can continue being pure."
    else:
        ay "Besides, this is the Patreon version of the game. We're {i}all{/i} safe here!"

    sa "Umm..."
    sa "Thank...you?..."
    s "Sorry to interrupt, but I’m going to need a little more information about you three putting on costumes for me."
    s "Since you’re all in my room, I can only assume it's because you want to-"

    scene firsthalloweenevent5
    with dissolve

    a "Halloween party. Ayane’s house. Shopping. Go. Tomorrow."
    s "Ayane, translate."
    ay "What she said pretty much covers all of the bases."
    ay "Sunday is Halloween, and Geoffrey said it’s okay if we throw a party at my place."
    ay "I already know what I’m going as, but Ami and Sana still need to buy a few things to get their costumes ready."
    sa "I...don’t even know what I want to be yet..."
    sa "So if you have any ideas..."

    "A Halloween costume for Sana?"
    "She'd look cute in pretty much anything, so I might as well use this opportunity to put an idea I like quite a bit in her head."

    s "Why not some sort of animal? Like...a cat or something?"

    "I'd also accept a rabbit. Or a dog."
    "Actually, I’m sure she’ll be adorable in whatever she chooses."
    "I stand by my initial cat-choice, though. Cat-girl Sana is my number-one pick."

    scene firsthalloweenevent6
    with dissolve

    ay "Oooooh! I want to see you dressed up like an animal too!"
    ay "And then I want to take pictures of you in the dorm and keep them in a special photo-album that I can look at whenever I feel sad!"
    ay "Let’s do it!"
    sa "Ayane...You’re scaring me again..."

    scene firsthalloweenevent7
    with dissolve

    s "Wait, does this whole ‘taking you guys shopping’ thing mean I’m going to be spending money? Or is Ayane fronting everything?"
    ay "Oh, I can’t pay for Ami this time. "
    ay "I actually got into trouble for spending a little over my monthly allowance on the beach trip, so I can’t really buy an extra costume or anything."
    a "Is that a problem?"
    a "I have some money saved up that I could probably use, but I was hoping to spend that on something a little different."
    s "How about you just...go in your pajamas? You can be a...tired girl for Halloween."

    scene firsthalloweenevent8
    with dissolve

    a "That’s a horrible idea, even for you."
    a "I don’t want to walk around Ayane’s mansion in my pajamas."
    s "You walk around our house in your pajamas all the time."

    scene firsthalloweenevent9
    with dissolve

    a "I’m not walking around a mansion in my pajamas! That is final!"
    ay "Come to think of it, this will be your first time actually coming over...won't it, Sensei?"
    ay "Does this mean it’s finally time for you to meet my dad and tell him that we’ll be getting married?"

    scene firsthalloweenevent10
    with dissolve

    a "Does this mean I’ll have to explain to him what happened when the police discover both of your bodies chopped up and placed into dumpsters all around the city?"
    ay "Oh, right. I told you I’d hold off on hitting on your [uncle] while you’re around. Sorry."

    scene firsthalloweenevent11
    with dissolve

    a "Not just ‘while I’m around!’ In general! Stop hitting on my [uncle]!"

    scene firsthalloweenevent12
    with dissolve

    sa "Umm...Sensei?..."
    sa "Have these two always...fought like this?"
    sa "You’ve known them both for a long time and...it’s a little strange to me how much they yell when they’re...supposedly best friends."

    "That’s a good question. I wonder how long this rivalry goes back?"

    if bonus == True:
        "I’m sure it got worse after Ayane and I started having a more...sexual relationship, but I’m pretty sure they’ve had to always kind of be like this, right?"
    else:
        "What will it take to make the two of them just get along and stop all of this senseless bickering?"

    s "I stopped keeping track, to be honest. I’ve just accepted it as a part of life."

    scene firsthalloweenevent13
    with dissolve

    ay "Hey, that’s exactly what I’ve done with my love for you!"
    ay "I realized there’s no good way to hide it, so I’ve just added that trait into my personality."
    s "Didn’t you literally just tell Ami you’d stop doing this?"
    ay "Oh, right."
    ay "This is exactly what I’m talking about, though. I can’t help it."
    a "Why are you still here?!"

    scene firsthalloweenevent14
    with dissolve

    ay "The same reason you’re here, Ami."
    ay "Because it’ll be getting dark out any minute now and we’re all going to sleep in Sensei’s bed with him tonight."
    sa "..."
    sa "I’m sorry, what?"
    a "{i}I’m sorry, what?...{/i}"
    ay "Isn’t this the perfect opportunity? I obviously wouldn’t have barged in here just to tell him about a party. I could have texted him that."
    a "So you barged in here to sleep in his bed?..."
    sa "This is...a joke...right?"
    sa "No one is laughing, so I...don’t really know..."

    if bonus == True:
        s "In case anyone wants my opinion, I’m fine with Ayane's idea."
    else:
        s "Don't even joke about something as serious as that, Ayane. It is not funny."

    scene firsthalloweenevent15
    with dissolve

    ay "Yay! Slumber party!"

    if bonus == True:
        a "Of course {i}you’re{/i} okay with it! You’re a stupid boy!"
        sa "I’m...not okay with it! I don’t even like sleeping with Ayane!"
    else:
        "This girl needs to learn to listen."

        a "AYANE!"
        sa "I don't want to sleep in here! I don’t even like sleeping with Ayane!"

    scene firsthalloweenevent16
    with dissolve

    ay "Oh? Then how come you always squeeze my arm in the middle of the night, Sana?"
    s "Excuse me, but I’d like to inquire about why you two sleep together when you have separate beds."
    s "I’d also like a little more detail about how Sana looks while she is squeezing you and the noises she makes while she sleeps."

    scene firsthalloweenevent17
    with dissolve

    sa "S-Sensei!"
    ay "I’m glad you asked, future-husband! "
    ay "She makes these cute little moaning noises whenever she rolls over that make my heart skip a beat even though I don’t like girls."
    ay "They’ve even made me question my love for you on several occasions, Sensei."
    ay "You always come out on top, though, so don't worry! I’m sorry for the confusing thoughts about my roommate!"

    scene firsthalloweenevent18
    with dissolve

    sa "What confusing thoughts?! This is the first time I’ve heard about any confusing thoughts!"
    a "I don’t like how your eyes look right now, Sensei..."
    s "How do they look, exactly?"

    if bonus == True:
        a "They’re filled with desire. Like you’re thinking things you shouldn’t be thinking."
    else:
        a "Squiggly."
        s "{i}But what does it mean?{/i}"

    a "Look at me. Only me. Not Ayane or Sana."

    if bonus == True:
        a "In fact, tell those two to get out of here and I will sleep in your bed tonight. To protect you, of course."
    else:
        a "As your accountant, it is my duty to protect your assets."

    scene firsthalloweenevent19
    with dissolve

    ay "But Sensei doesn’t need protection. Isn’t that right, Sensei?"
    s "…"
    a "…"
    a "Excuse me?"
    s "Protection is for cowards. I know how to take care of myself."
    ay "You also know how to take care of-"
    a "One more word and you die."
    ay "...Flowers!"
    ay "You are an admirable gardener."

    scene firsthalloweenevent20
    with dissolve

    sa "Umm...are we planning on staying here much longer?"
    sa "I told my mom I could work tonight and...I didn’t realize you had planned a sleepover here..."
    sa "I really wish you’d tell me these things in advance..."
    sa "Also...I’d...really appreciate it if...you don’t take me into boys’ rooms anymore."
    sa "It smells like Sensei in here and it makes me feel funny."
    ay "Right? It's magical, isn't it? "
    ay "Doesn’t it get your heart racing, Sana?"
    ay "Being just inches away from where Sensei sleeps? Where he dreams?"
    ay "Can’t you feel your blood pumping?!"

    scene firsthalloweenevent21
    with dissolve

    sa "Uh..."
    sa "..."
    sa "No?"

    scene firsthalloweenevent22
    with dissolve

    ay "Well, either way, be prepared to take us shopping tomorrow, Sensei."
    ay "Like I said, I don’t need anything, but it’s not like I’m going to just turn down an opportunity to spend more time with you. Hahahahaha!"

    scene firsthalloweenevent23
    with dissolve

    a "Since Ayane doesn’t need anything, it would probably make more sense for just Sana and me to come, right?"
    a "We can have her stay at home with her butler."
    a "Or, better yet, how about Sana doesn’t come either and the two of us spend the entire day together?"
    a "Oh! And even better than that! How about the two of us just have our {i}own{/i} Halloween party and let everyone else go to Ayane’s?"
    sa "That’s fine...but...I still need to find a costume..."
    s "Don’t worry Sana, you’re still coming. And so is Ayane."
    s "Ami is old enough that I think it's time she learns the value of sharing."
    a "What am I sharing exactly? Because it certainly isn’t you."
    s "It is me."

    scene firsthalloweenevent24
    with dissolve

    a "I refuse."
    a "Love me more~"
    s "I love you plenty enough already."
    a "Heheh~ Sensei said he loves me."
    ay "Me next! Me next! Tell me you love me too! "
    ay "It’s not fair that only Ami gets to hear it when I’m the one who brought everyone in here!"
    ay "Reward me with your affection!"
    s "...I love you Ayane."

    "It really makes my stomach hurt having to use the ‘L’ word twice in one day, but I might as well try and go three-for-three while I’m at it."

    scene firsthalloweenevent25
    with dissolve

    s "Sana."
    sa "...?"
    s "I love you too."
    sa "…"
    s "…"
    sa "…"
    s "…"
    sa "…"
    s "…"

    play sound "thump.mp3"
    scene firsthalloweenevent26
    with hpunch

    ay "Ah! Sana!"
    ay "Sensei! What do you think you’re doing?!"
    s "I was just giving her the same treatment I gave you two."
    s "Is she dead?"
    ay "No! Just...unconscious, I think!"
    ay "Sana isn’t ready to accept your love yet! That comes much later in the story!"
    s "How much later? I feel like I’ve been waiting for eons."
    ay "Eons longer! Can’t you see how she’s reacting to just hearing your words?!"
    s "I wish she’d react more like Ami. She’s handling it very well."
    a "Hehehe~ Love love love~ My [uncle] loves me~ Ayane is stupid~"

    scene firsthalloweenevent27
    with dissolve

    ay "Well...I guess there’s no harm in letting her nap on your floor for a little while."
    s "Didn’t she say she had work, though?"
    ay "Did she? I have an admittedly hard time focusing on anything that isn’t you while I’m in your room."
    ay "Or in general, for that matter."
    s "Yeah, I’ve noticed that."
    s "What should we do about Ami, though? It seems like she’s under a spell right now."
    ay "Oh, don’t worry about that. I know how to handle this."

    scene firsthalloweenevent28
    with dissolve

    ay "Psst...Ami..."
    ay "*Unintelligible whispering noises*"
    s "…"
    ay "*Even more unintelligible whispering noises*"
    s "Ayane, what are you-"

    scene firsthalloweenevent29
    with dissolve

    a "Ah-"
    ay "Heheh~"
    s "…"
    a "Is that really true?"
    s "…"
    a "…"
    s "...Yes?"

    scene firsthalloweenevent30
    with dissolve

    a "Sensei..."
    s "Ayane, what did you say to her?"
    ay "A secret, obviously. Why would I have whispered if it was something it was okay for you to hear?"
    s "But...my curiosity..."
    a "You have no idea...how happy it makes me to hear that..."
    s "Hear what? What the hell did she say to you?"
    ay "Just a little of this and that. It’s nothing bad. Don’t worry."
    s "Ayane."
    ay "Sensei~"

    scene firsthalloweenevent31
    with dissolve

    ay "Okay, Sana! Time to get up."

    "Ayane kneels down and begins to try and shake Sana back to consciousness. "
    "Within a matter of minutes, she starts to come-to. While Ami, on the other hand..."

    a "…"

    "Ami remains broken for the rest of the night."

    scene black
    with dissolve2

    "{i}Welcome to Lessons in Love’s first special Halloween update!{/i}"
    "{i}The following events will play in succession from start-to-finish.{/i}"
    "{i}You will not be able to choose how you spend your time during the events.{/i}"
    "{i}Once the Halloween events end, everything will go back to normal.{/i}"
    "{i}So sit back, relax, and enjoy the update!{/i}"
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ halloween1 = True

label halloween2:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
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
...
```