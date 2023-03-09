# National Tsukasa Day
Tsukasa event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsukasaspecial1&go=Go)



## Event preconditions
✅Days since the start of the game greater than or equal to 530

❌Event "[Io: 1999 PC Classic, Rollercoaster Tycoon](./iospecial30.md)" is completed (event=iospecial30)

❌Event "[Karin: Emerald Eyes](./karindate25.md)" is completed (event=karindate25)

❌Day of week is Monday



## Next events
None

## Event properties
* ID: tsukasaspecial1
* Group: Tsukasa
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning

## Event code
File: \game\TsukasaEvents.rpy
Code:
```python
...
label tsukasaspecial1:
    scene hall_day
    with fade
    play music "10c.mp3"

    "Another week as the world’s most sexually active teacher means another week to completely ruin the lives of everyone around me by simply showing up to class."
    "Oh. Sorry for the self-loathing so early in the morning. I just figured that if I got it all out of the way now, I’d be able to do whatever I want for the rest of the day without thinking at all."
    "Which, to be fair, is what I try to do most days to begin with. "
    "However, I was notified of a very particular “holiday” through a phone call from my assistant this morning that has put me in a particularly passive aggressive mood."
    "Especially since it requires my full presence in the classroom at the risk of both Imani and I losing our jobs. And Imani has been kind enough to me so far that I don’t want to do that to her."
    "Also, I’m pretty sure she’s barely hanging on by a thread financially and she kind of needs this."

    scene black
    with dissolve
    play sound "slidedoor.mp3"

    "I slide open the door and prepare myself for the start of what I imagine will be the worst holiday ever- and that is saying a lot since things like Christmas exist."

    scene tsukasaday1
    with dissolve2

    "But at least on Christmas you can come up with excuses to not pay attention to certain people."

    tk "Good morning! Happy National Tsukasa Day!"
    to "Tsukasa, how much did you pester our poor father to make this childish dream of yours a reality?"
    tk "It’s not a childish dream if I’m an ancient and powerful wizard. Just because there’s not National Touka Day doesn’t mean you can get mad at {i}my{/i} holiday."
    to "Sensei is a very busy-"

    scene tsukasaday2
    with dissolve

    to "Well...actually, that’s not true at all. Sensei is practically never busy."
    to "But he’s assuredly not going to {i}start{/i} being busy when he’s preoccupied with silly games like this."
    tk "Wrong again, dear sister. I’ve heard the games this adult plays and they are a lot louder than whatever is going on in this sorry excuse for a classroom."
    s "Why are you here?"
    tk "Because it’s National Tsukasa Day and I get to do whatever I want."
    s "So you chose to...come to high school?"

    scene tsukasaday3
    with dissolve

    tk "Yup!"
    tk "The train wasn’t very exciting, so I wanted to get a closer look at the true commoner mecca! A public school!"
    tk "I even had my personal tailor make an exact copy of my sister’s uniform so I can experience firsthand the pain she endures every day as she is turned into one of you!"
    ay "Sensei, how long is Tsukasa staying here?"
    a "While I, too, would like to know the answer to that question, I’m more concerned about what sorts of games Tsukasa has heard you playing."
    s "To Ami, I have no idea what she’s talking about. And to Ayane, I assume she’ll only be here until the end of Tsukasa Day."

    scene tsukasaday4
    with dissolve

    tk "Ahem! It is {i}National{/i} Tsukasa Day! Don’t go leaving out words that describe how important it is."
    tk "Also, National Tsukasa Day doesn’t end until next Wednesday because Father said so."

    scene tsukasaday5
    with fade

    ima "Damn. I wish I was rich enough to change the way time works."
    ay "You don’t have to be rich, Imani! All you have to do to change the way time works is get pregnant with Sensei’s baby. Well, at least according to Maya."
    a "What?"
    m "I have absolutely no clue what she is talking about."

    scene tsukasaday6
    with dissolve

    ima "With all due respect, Senpai, I think I’d rather take the money."
    ima "You’re handsome and all, but if the way you treat my body is anything like the way you treat my mind, I can’t imagine that would be a very enjoyable experience."
    s "Luckily for you, I don’t intend on getting anyone preg-"
    tk "Stop paying attention to everyone not named Tsukasa on National Tsukasa Day!"

    scene tsukasaday7
    with dissolve

    ima "Right! Uhh...yeah."
    ima "See, the issue with that is that I’m not exactly...{i}good{/i} with kids that aren’t in high school yet. They make me feel weird. And even if today is National Tsukasa Day, you kind of..."
    ima "Well, you don’t belong here."
    s "Watch it, Imani. This girl may not look intimidating, but she holds our futures in the palms of her tiny hands."

    scene tsukasaday8
    with fade

    tk "Are you two sure you are even teachers? Because I’m hearing a whole lot of slander and not so much {i}teaching{/i} right now."
    tk "And I suggest that if you two want to keep your jobs, that you...actually {i}do{/i} them."
    to "I am so sorry that this is happening today. I tried my best to prevent it, but...alas."
    ima "What can we even {i}teach{/i} with someone your age here? You won’t be able to follow along."
    tk "Do you take me for a lowly peasant? I have received only the highest forms of education from the most qualified teachers in all of Kumon-mi."
    tk "Your meaningless squibbles disguised as educational lectures mean nothing before the greatness that is Tsukasa AKA “Tsurumi” Tsukioka of the Tsukioka family."
    ima "Squibble? What’s a squibble?"

    scene tsukasaday9
    with dissolve

    tk "A word I made up that means “silly and pointless!” I call it a Tsukasology. Or a...Tsukasism. There’s another one right there."
    to "Creating new words is far detached from proper education, Tsukasa...AKA Tsurumi."
    tk "Then try me! Ask me anything. I’m sure my answers will be far more acceptable than whatever these so-called “squobbles” would give you."
    ima "But...no one calls them that."

    menu:
        "What is the world’s oldest city?":
            s "What is the world’s oldest city?"
            tk "Damascus, Syria!"
            tk "That's a highly contested topic as many people believe it to be Jericho. But Jericho was more like a large town than a city during its early years."
            tk "Mother says Damascus isn’t all it’s cracked up to be, though. She visited there on one of her travels from before Kumon-mi was isolated."
            ima "Did she get it right?"
            s "I have no clue. I just asked a question thinking she wouldn’t know the answer."
            ima "Never fear, Senpai. I will do my duties as your loyal peon and utilize the glory of my smart phone to- holy shit, she’s right."
            to "Of course she is..."

        "How tall is Mt. Fuji?":
            s "How tall is Mt. Fuji?"
            tk "Three-thousand, seven-hundred-seventy-six meters!"
            tk "I’m supposed to go there with Papa once we’re allowed to leave the city again."
            tk "He says he’s going to buy part of the mountain so I can have my own little house there."
            ay "Is that even legal?"
            tk "Everything is legal when you’re rich. But you wouldn’t know that since you’re not."
            to "That’s Ayane Amamiya you’re speaking to, Tsukasa. She comes from the second richest family in all of the city."
            tk "Sorry. Can’t hear you from all the way up here in first place."

        "Who lives at the North Pole?":
            s "If you’re so smart, how about you tell me who lives at the North Pole?"

            scene tsukasaday10
            with dissolve

            ima "Bruh."
            to "Sensei..."
            tk "The North Pole?"
            tk "Do you take me for a fool, commoner?"
            tk "Everyone knows that’s where Santa’s workshop is. That was barely even a question."
            s "Are you sure about that?"
            tk "Yes. Unless you mean to tell me it is my mother who has been returning my annual letters to him. And that would just be utter nonsense."
            s "Are you {i}sure{/i} about that?"
            to "Don’t do it, Sensei..."
            a "Even you should draw the line at telling a little kid the truth about Santa Claus, Sensei. You’re better than this."

            scene tsukasaday11
            with dissolve

            tk "The truth?"
            tk "Did something happen to Santa Claus?"
            tk "If he was evicted due to the waste produced by his workshop, I would not mind forgoing some of my allowance to assist him. He does tremendous work for this country and is an asset to all of us."
            ay "Just drop it, Sensei. Before it’s too late."
            s "Fine. But I rest my case in showing that Tsukasa isn’t as smart as she thinks she is."
            to "Yes, but that is only because you asked her a question that all of those prestigious educators dared not ever speak about."
            tk "Why is everybody acting so weird? All it takes is a little personal research to figure out the truth."
            tk "Can you people not afford computers?"

    scene tsukasaday12
    with fade

    ima "What do you think, Senpai? It would feel kind of wrong getting rid of her now. But, like I said before, I’m not really the best when it comes to kids."
    s "And you think I am?"
    ima "Well, you became a teacher, didn’t you? You’ve gotta be at least a {i}little{/i} good with them."
    s "Didn’t...you also become a teacher?"
    ima "Yeah, but I’ve still got time left."
    s "I’m only 31."
    ima "Damn, that old already? Need me to go grab a cane from the nurse’s office?"
    tk "Again! You people refuse to pay attention to the one person you should be paying {i}all{/i} of your attention to today!"
    tk "This insolence will not go unpunished! As soon as my father finds out about this, you two will never work another day in this town again! You-"
    to "Tsukasa, please! They are doing their best! And all things considered, their best seems very good based on the standards of today’s public education system."

    scene tsukasaday13
    with fade

    tk "Hah...This is exactly why the youth of the nation has become so lazy and unmotivated. No one gets the education they need anymore. Papa should really do something about that."
    to "I agree but, unfortunately, progress didn’t have much place to go after the creation of bubble wrap."
    c "Hey, Tsukasa. What are you doing here?"

    scene tsukasaday14
    with dissolve

    tk "Oh! The peasant girl from Mother’s onsen!"
    tk "And here I was thinking the strong scent of cheap perfume was just the way girls’ public schools smelled."

    scene tsukasaday15
    with dissolve

    c "Is it...really that strong? Because I’m trying something new and that wasn’t exactly the type of reaction I was looking for."
    tk "What type of reaction were you looking for?"
    c "A...positive one?"
    tk "Oh."
    tk "Well, good luck."

    scene tsukasaday16
    with dissolve

    c "Th...That aside! How are things? How’s your mom?"
    tk "Things are great! As you may have noticed from all of the banners in the hall, today is National Tsukasa Day!"
    tk "Unfortunately, Mother had other matters to attend to, so she is unable to spend it with me. But that’s okay because my big sister and her teacher are looking after me."
    tk "Which isn’t to say I wouldn’t be able to function on my own when I am much better and smarter than both of them. But laws will be laws."
    tk "You do know what “laws” are, correct?"

    scene tsukasaday17
    with dissolve

    c "Yes, Tsukasa. I do know what laws are."
    tk "Good! I never know with you people."
    c "“You people” as in...commoners, right?"
    tk "Good job! Public education has not entirely failed you yet."

    scene tsukasaday18
    with dissolve

    tk "That said, it would be wise to quit while you’re ahead and follow in the footsteps of your younger sister. She and I have big plans for this world."
    c "Yeah, you two have been talking a lot lately, haven’t you?"
    tk "Talking? We’re not just {i}talking.{/i} We’re drafting business plans that are going to flip Kumon-mi on its head. People like us do not have time to simply “talk.”"
    c "Well, would you maybe like to come over and discuss business in person sometime?"

    scene tsukasaday19
    with dissolve

    tk "Can your budget home fit more than two people inside of it?"
    c "Uhh...yes."
    c "Just...probably not more than five."
    tk "I can fit more people than that in my bathroom."
    c "Why is that...ever a thing you’d want to do?"
    tk "It’s not. But I can and I felt compelled to inform you of that."

    scene tsukasaday20
    with dissolve

    c "Either way, Chinami has been excited to see you again and I figure this would give you two a good chance to play together."
    tk "I will consider it and consult with the rest of my business associates!"
    tk "If I do agree to {i}play{/i} though, will you consider teaching Chinami and I the special game you played with your teacher at the onsen? Mother says it’s for adults, but I have proven today that I-"

    scene tsukasaday21
    with hpunch

    tk "MMMFMFMFMFMFMFFFFFMFHHFHFFF!!!!!"
    ima "Special game?..."
    ima "Onsen?..."
    c "Hahaha! Kids, right?! Always making up stories!"
    s "Oh, look. A stack of papers way at the...other end of the school that I need you to file."

    scene tsukasaday22
    with fade

    ima "..."
    s "..."
    ima "..."
    s "..."
    ima "You trying to teach Chika how to time travel, Senpai?"
    s "I have no idea what you’re talking about."
    ima "And at an {i}onsen?{/i} What does that mean for all of the other girls who had to stare at your drab-ass wallpaper while you were doin’ ‘em dirty?"
    s "Is that really what you’re most concerned about?"
    ima "I’m an advocate for equality, Senpai. We {i}all{/i} deserve onsens."
    s "Well, I’ll add you to the top of my...prospective onsen visit list now."
    ima "Think saying that might be giving me a little too much attention on National Tsukasa Day, don’t you think?"

    scene tsukasaday23
    with fade

    tk "MMMFMFMFMFMFFHFHFHFFMMFMFM!!!!!!!! MMMMM!!!!!!!"
    to "Tsukasa, what does Mother say about making a racket like that? Quiet down or you’ll attract negative press."
    tk "MMMMMMMMMM!!!!!!!!!!!!"
    c "Tsukasa...I’m gonna let you go now. {i}But I kinda need you to not say anything about the onsen, okay? Nobody is supposed to know about that.{/i}"
    tk "MMMM! MMMMM! MMMM!!!"

    scene tsukasaday24
    with dissolve

    tk "Are you out of your mind?! Do you have any idea who I am?! Do you think it’s okay to just assault a princess?! I will have your head!"
    c "But if you kill me, Chinami won’t want to do business with you anymore, so...your success kinda hinges on me in a way, doesn’t it?"

    scene tsukasaday25
    with dissolve

    tk "While it {i}is{/i} true that an ally like her would certainly take us to the next level, I’m not quite sure if it is worth my own personal safety."
    c "What if I...promise not to grab your face anymore?"
    tk "That would be a start...but I am going to need something a little more than that."
    c "Uhh..."
    c "You can eat...cereal when you come over to my place?"

    scene tsukasaday26
    with dissolve

    tk "C...Cereal? But Mother says cereal is a leading cause of diabetes and that there are much tastier and healthier alternatives."
    c "And while I’m sure she’s right...you {i}do{/i} want a taste of commoner life, don’t you? What better taste than eating the same thing Chinami eats every morning {i}inside{/i} of Chinami’s house?"
    c "Think of it as a...research...project."

    scene tsukasaday27
    with dissolve

    tk "You drive a hard bargain, peasant. That does sound like something that tickles my interest. However, I have one final adjustment I’d like to add to your offer."
    c "And that...adjustment is?"

    scene tsukasaday28
    with dissolve

    tk "Can my sister come too?"
    to "What?"
    tk "It wouldn’t be fair if I got to experience something like that firsthand and she did not. I am simply doing this so that the two of us may remain on equal footing."
    tk "It is the least I can do in exchange for intruding on her personal life by being here."
    to "Tsukasa...I don’t really need to-"
    c "Sure, yeah. That’s actually..."

    scene tsukasaday29
    with dissolve

    c "You know what? Why don’t we invite Sensei too?"
    s "What?"
    tk "That seems unnecessary. Jeeves has no place in the same room as two serious and powerful businesswomen. And also Onee-chan."
    to "Why is Sensei...suddenly a part of this as well, Chika?"
    c "Because I was looking for a good time to go do something lately and kind of need a babysitter since I have no idea how long it will take."
    c "Which isn’t to say I don’t trust you, Touka. I just...don’t really know if you'll be able to grasp any of the, uhh...commoner technology at my place."
    s "I mean...I guess I can come? I doubt I’ll be much help, though."
    tk "Jeeves can wait in the lobby while the rest of us talk. That seems fair to me."
    to "I don’t believe Chika’s home is the type to have a lobby, Tsukasa. Sensei can wait in her rose garden instead."
    s "..."
    c "Sensei? You cool with that?"
    s "Depends. Do you have a rose garden now?"
    c "Who doesn’t?"
    to "Told you so, Tsukasa. You should listen to me more often."
    tk "Stop making so many silly decisions and I will."

    scene black
    with dissolve2

    "Somehow, I wound up getting roped into agreeing to be a babysitter for both Chinami {i}and{/i} Tsukasa soon."
    "That doesn’t sound exhausting at all."
    "Thankfully, I’ll at least have Touka there with me. And while that probably won’t really help either, it will definitely help me feel a little more {i}normal{/i} as there’s at least someone who isn’t..."
    "Well, someone who isn’t a full blown child there."
    "Plus, an environment like that sounds like the perfect place to fuck with her. And that is quickly becoming one of my favorite past times."
    "Anyway, the day comes to an end- and I find myself retreating back to my office."

    $ renpy.end_replay()
    $ tsukasaspecial1 = True

    jump tsukasaspecial1p2

label tsukasaspecial1p2:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
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
...
```