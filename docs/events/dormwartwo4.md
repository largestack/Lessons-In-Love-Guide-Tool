# Gamer Girl Grindfest
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo4&go=Go)


Part of event chain [A Frame on a Shelf in a House](./dormwartwo3.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwartwo4
* Group: Main
* Triggered by label: dormwartwo3

## Event code
File: \game\chap3.rpy
Code:
```python
...
label dormwartwo4:
    play sound "static.mp3"
    scene ayhh2 with flash
    scene ayhh4 with flash
    scene ayhh8 with flash
    scene gamerbattle1 with flash
    stop sound
    play music "anothernewsong.mp3"

    $ totaldays += 1
    $ day += 1
    hide friday onlayer date
    show saturday onlayer date

    "We’re not going to talk about that, though."
    "You see, there comes a time in every man’s life where he must get his priorities in order."
    "Just take a look at Haruka. She clearly has her priorities in order, doesn’t she?"
    "The point is that I would be a fool to let what comes to me at night leak out into this room so full of color when this is supposed to be a happy day. "
    "This is supposed to be a happy day."
    "This is supposed to-"

    t "Hello."
    s "Hi, Tsuneyo. Why is everyone still dressed like it’s Halloween? "
    h "Don’t ask questions. Just accept it. "
    mo "The reason is quite simple, Sir. The idea of a group-wide contest is much more alluring when we’ve all got a different set of skin on, isn’t it?"
    mo "We figured the safest way to even the playing field was by having {i}everyone{/i} keep their costume on so no one girl would have an unfair advantage if she decided to do it on her own."
    s "You really think I would go out my way to give a victory to a girl just because she dressed up for the occasion? "
    mo "Yes."
    s "Then you underestimate how seriously I take this, Molly."
    mo "Sir, do you even remember what Sana and I will be competing in today?"
    s "If it’s anything other than video games, you sure picked a strange location for the contest."
    mo "Oh-ho, so you really {i}do{/i} remember. Then tell me, Sir. Whose side are you on? Who are you rooting for?"
    s "Am I even allowed to choose sides? Wouldn’t that be a display of bias? Also, where is Imani? Isn’t she supposed to be doing this with me?"

    scene gamerbattle2
    with dissolve

    mo "That’s a good question. Nobody’s seen her since she followed us home from school yesterday."
    t "I believe this may be my fault. I have grown too powerful."
    mo "Tsuneyo’s racial passive gives her charm skill an added bonus of lasting...forever."
    t "I would like to thank my ancestors for whatever may have caused this. "
    h "Me too."
    t "Actually, never mind. It is inconvenient and I worry that I am not responsible enough for such a dangerous ability."
    t "Now, please excuse me while I go stand in the corner and prevent anyone else from falling in love."

    scene gamerbattle3
    with dissolve

    h "Nooooo! Come back!"
    mo "Are you about ready to begin, Sir? We’ve been waiting on you this entire time. "
    mo "To be honest, I assumed you’d be showing up with Ami. But I suppose even you two must spend some time apart every now and then."
    s "We spend plenty of time apart. I came here alone today. But yeah. If you guys are ready to go, then-"

    scene gamerbattle4
    with dissolve

    sa "S...Sorry I’m late...My mom...took extra long to...get ready this morning..."
    mo "Sana?..."
    mo "But...wait. If you’re in {i}that{/i} costume again, who is it in the dolphin costume? I assumed you’d just swapped back into ole reliable after realizing how atro- err...{i}attractive{/i} that costume is."
    sa "That costume...belonged to my mom, so...I’m sure there are...other people who have it as well..."

    scene gamerbattle5
    with dissolve

    mo "Well, that said, I suppose our death march is about to commence! Bequeath unto me your hand so that we may perform a blood oath and ensure that neither one of us backs down once we face certain doom!"
    sa "B...Blood oath?....Can’t we just...play games without hurting ourselves?..."

    scene gamerbattle6
    with dissolve

    mo "Aw, man. I really wanted to do the blood oath. But I suppose that would just lead to a slew of problems when it comes to operating the machines, so..."

    scene black with dissolve

    mo "Fine! Come with me, Not-Zagull! Our first of three games will begin in mere moments!"
    mo "Master! Sir! Whatever your preference for pet name is! Feel free to grind your social links in the meantime while Sana and I get into position!"
    s "What’s a social link?"
    mo "Just talk to the Magistrate of Mammaries and tell her to put her breasts away during the competition or they’re going to distract me!"
    s "Got it."

    scene gamerbattle7
    with dissolve

    s "Hey. Molly wants you to flash her for good luck. I told her it was a bad idea, but girls will be girls."
    h "Weird. She’s never responded to any of the three times I accidentally sent her pictures of them, so I assumed she just wasn’t interested."
    s "Don’t worry. I won’t be as mean if you ever accidentally send them to me."
    sar "Hi. Idol Sara here and ready for you to pay attention to me next. Tell me how cute I am."
    s "You are very cute."
    sar "Great. Now take my credit card, walk three blocks south, and look for the giant, neon diamond sign right above the big, red letters that spell out “ENGAGEMENT RINGS.”"

    scene gamerbattle8
    with dissolve

    h "I don’t think you’re supposed to pay for your own engagement ring."
    sar "You’re not. But, let’s be real, there’s no way Sensei would actually buy one and I am willing to take this financial hit if it means getting some stability back in my life."
    s "Ahem."

    scene gamerbattle9
    with dissolve

    if sarasex == True:
        sar "What? This knot is ready to be tied. "
    else:
        sar "Blah, blah, let’s stay friends, blah. Who says friends can’t get married anyway?"

    s "Okay. I’m just going to talk to Haruka now. "
    sar "And what? Ask her to flash you next?"
    s "No. Ask her why you two decided to come here when this contest doesn’t really have anything to do with you."

    scene gamerbattle10
    with dissolve

    sar "Oh! We started a betting pool. I’ve got 10,000 yen on Sana taking down Molly in two rounds."
    h "And I’ve got that same bet on Molly winning in three. "
    h "Should I be betting against Sara knowing that her financial life is hanging on by a thread? No. But if she’s going to keep being frivolous with her money, it is my job to teach her a lesson."
    h "Also, if Molly loses this contest when she spends roughly 75%% of every work day playing games on her phone, I am going to be extremely disappointed in her."

    scene black
    with dissolve

    s "Well, best of luck to you two and enjoy your time reliving your glory days by hanging out in an arcade full of teenagers."
    h "I wasn’t really cool enough to ever get invited anywhere like this."
    sar "You mean to tell me you’ve never been banged on an air hockey table before? How are we even friends?"
    h "Have...have you?"

    scene gamerbattle11
    with dissolve

    s "Hey, you two. What’s-"
    r "Shh. You’re going to scare it away."
    s "Scare what away?"
    o "The dolphin. "
    o "It’s just..."
    o "It’s just...{i}standing{/i} there..."
    s "Oh, come on. It’s obviously just one of the girls in a joke costume. "
    s "I’m sure it’s completely harmless."

    play sound "static.mp3"
    scene sexyland with flash
    scene sexyland2 with flash
    scene sexyland with flash
    scene gamerbattle12 with flash
    play sound "dolphinnoise.mp3"

    mysdol "..."
    s "Okay. That’s enough of you."

    scene gamerbattle13
    with fade

    s "I’m going to talk to you two now since I no longer like dolphins."
    a "I had no idea you ever liked them in the first place."
    m "Were you able to find out who’s inside? Because I would be willing to bet money on it being Ayane."

    scene gamerbattle14
    with dissolve

    ay "How much money?"
    m "At least-"

    scene gamerbattle15
    with dissolve

    m "Oh, god damn it."
    a "I’m glad you were able to get out of bed, Sensei. I tried shaking you for a good twenty minutes and, if it weren’t for the fact that you were still breathing, I probably would have just killed myself."
    ay "I’m also glad you made it! But I don’t really have anything that depressing to add, so I’ll just remind you that it’s because I love you."

    scene gamerbattle16
    with dissolve

    m "And I...don’t care. Besides, aren’t you supposed to be judging something right now? Because I can hear Molly yelling from here and it sounds like they’re about to start."
    s "Is there even anything {i}for{/i} me to judge? I figured they were just going to play a few games and...whoever won, won."
    m "I’m quite sure that’s how it will be, yes. I just wanted to try and say something that would get you to leave. It appears that I have failed."
    s "Wow, you’re not holding back at all today, are you?"
    a "Maya’s a little nervous that she’s going to have to dress up like a maid and say nice things to you."
    m "I’d like to make it known that there is an extreme difference between “nervous” and “nauseous.”"
    ay "And I’d like to make it known that, once again, I have nothing to add but the fact that I love you."
    s "Well, here’s hoping your stand-up routine tonight has a little more to go off than just that."

    scene gamerbattle17
    with dissolve

    ay "Heh...heheh..."
    a "Yeah...how’s that going, by the way? You were up really late practicing, weren’t-"
    ay "Oh, look! The...contest is...woo! Go Sana!"

    scene gamerbattle18
    with dissolve

    mo "Round one is a test of dexterity! A test of how limber these bodies are and of how gamers aren’t {i}always{/i} strapped down to a chair with a half empty can of Monster on their desk! Just...most of the time!"
    sa "I can’t...drink that stuff...It makes my heart...explode..."
    mo "You expect to defeat {i}Molly MacCormack{/i} with a tolerance that weak? Don’t make me laugh."
    mo "The objective of this game is simple- the first one to make it to the finish line after three laps is the winner."
    sa "So it’s...like Mario Kart, but...on a...machine?..."
    sa "Are there any powerups?...Or...other things I should know about?...Because it’s my first time...playing this game and..."
    sa "It might be unfair if...if you’ve played it before..."
    mo "It’s as plain as day, Not-Zagull. You just drive as fast as you can and try to reach the end before your opponent."
    mo "No turtles...no stars...just raw speed..."
    to "Why, it feels like just yesterday that my family and I were taking turns getting railed on this very machine."

    scene gamerbattle19
    with dissolve

    mo "I beg your pardon?"
    to "It was my first time, so I was worried that I might do something wrong. And while it started off very bumpy and hard, it felt very smooth by the end!"
    to "My younger sister was able to pick up on it almost immediately, though. My mother and I were in awe. You should have seen how deftly she handled the “shafts.”"
    sa "Uhh..."
    mo "The...sh...shafts?..."

    scene gamerbattle20
    with dissolve

    to "In the end, after my sister was railed to her heart’s content, it was my turn to rail my mother."
    to "It’s a special thing, railing one’s mother. And I was very worried that I might disappoint her. But we reached the finish line within seconds of one another and...my. It was a surprisingly intimate experience."
    mo "..."
    sa "..."

    scene gamerbattle21
    with dissolve

    u "W.......Wshhhhh........"
    to "Uta? Did I say something wrong?"
    to "Perhaps we can rail each other once these two are done? I’m sure you’ll love it."

    scene black
    with dissolve2

    "Winner of Game 1:\nSana Sakakibara"

    scene gamerbattle22
    with dissolve2

    mo "Okay, listen up! The only reason you were able to eke out a victory is because I was distracted by things I thought only happened in visual novels!"
    sa "Are you sure I’m not just...better than you?..."

    scene gamerbattle23
    with dissolve

    mo "Oh? What’s this? I had no idea Zagull had been sneaking points into {i}charisma{/i} behind his DM’s back. Remind me to review your character sheet before our next session, petulant whelp."
    sa "You’re...doing a lot of talking for...someone who’s about to lose her...second game in a row..."
    mo "And you’re sounding rather confident for someone who only managed to win because of a fluke."
    mo "Now, we’ve returned to my realm. Miles and miles away from the realm of games that require your full body rather than just your hands."
    mo "In round two...we fight. To the death. But, fair warning Zagull, years of grinding away at mobile games has caused my reflexes to develop into something you should truly fear."

    scene gamerbattle24
    with dissolve

    sa "See...that’s where you’re wrong, Molly..."
    sa "Because...the only thing I fear...."
    sa "Is spaghetti..."

    scene gamerbattle25
    with dissolve

    mo "Is...what?!"
    sa "Die! Die! Die!!!"

    scene gamerbattle26
    with hpunch

    mo "Ah! You bastard! I should have known you’d employ some sort of distraction! No one’s actually afraid of spaghetti!"
    sa "I am! And I...don’t care who knows it anymore!"

    scene black
    with dissolve

    mo "What does that even mean?!"

    "Winner of Game 2:\nMolly MacCormack"

    scene gamerbattle27
    with dissolve2

    sa "So...um...now that we’re tied at...one win each...what are we doing for our last game?..."
    mo "I don’t really know. Whatever this machine is, I guess."
    mo "I want our last match to be fair and balanced, and I’ve already played everything else inside of this arcade."
    sa "Then...isn’t it...unfair to you if you go first? Since you’ll be using your turn...figuring out how everything works..."
    mo "Probably. But I’m the one who’s chosen all of the games so far, so it’s only fair that if either one of us receives a handicap, it should be you."
    s "Can you two hurry it up? I’m just seconds away from another quote against a sky background."
    mo "I suppose we should start our final round before our teacher becomes fish food. It will be hard for him to judge the following contests if he’s decomposing at the bottom of the ocean."
    s "Thanks, Molly. That’s exactly what I wanted to hear."
    sa "I think this...is some kind of...escape game..."
    sa "I used to...play a lot of these...when I still lived with my mom..."
    mo "Yes, it appears there’s a timer ticking down as well. So we only have five minutes to get out of this house before the game ends."
    sa "It...would probably be best if we work together then..."
    mo "You’re right. An extra set of eyes will make it so we can cover twice as much ground in the same amount of time. Good thinking, Zagull."
    mo "You cover the left side of the house while I look for anything interesting on the right."
    s "So, I’m obviously no expert when it comes to this sort of thing, but I could have sworn you two were supposed to be playing {i}against{/i} each-"
    mo "Shh. We need to focus."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene gamerbattle28
    with dissolve2

    mo "This game has to be bugged. Fatally bugged. That’s why I’ve never heard of it before."
    mo "This is our fourth time trying and we still can’t figure out how to get these damn boards off of the windows. Who even designed this nonsense?"
    sa "We’ll get it soon...we just...have to keep trying..."
    sa "That’s the key to games like this..."
    sa "Sometimes you...have to...bash your head against the wall...over and over...until you find something different...something that...unlocks the rest of the pieces in the puzzle..."
    mo "Yeah, that just sounds like bad game design."
    sa "I think...it’s kind of fun...and...really rewarding...once you finally break the pattern and-"

    scene gamerbattle29
    with dissolve

    mo "Wait! That book in the top right corner of the shelf! The one that’s jutting out a little. Click on that. Our next clue could have something to do with-"

    scene gamerbattle30
    with dissolve

    sa "It...it fell down! And...there’s a key inside!"
    mo "A-ha! So it {i}is{/i} possible after all!"

    scene black
    with dissolve2

    mo "Try the key on that door in the back of the house, Sana. That’s the only one we haven’t tried yet."
    sa "It’s...no. It’s not doing anything..."
    mo "Tch...we’ll just have to try something else then."

    "Sana and Molly wind up playing their weird, unnamed arcade game for another thirty minutes- paying no attention to anything happening off of the screen they’ve glued their eyes to."
    "And while their “contest” manages to devolve into two friends playing the same game for fun instead of competition, there {i}is{/i} a winner as it winds up becoming more of a test of endurance than anything else."
    "And when it comes to endurance and the depressing act of refusing to detach yourself from the virtual world at any point, there is only one person that will ever come out on top..."

    scene gamerbattle31
    with dissolve

    sar "It’s okay, Sana. I can just not eat next week. You did your best."
    sa "I’m not upset...I...actually had a lot of fun..."
    mo "As did I, Sana. We should do this again under better circumstances...on a day where I am not destined to win. Though, I very likely will as I am just that good."
    h "Fuck yeah, Molly. All of that time being a horrible employee has finally earned me money in a really roundabout way!"
    h "This is the part where I feel like I’m supposed to say I’m proud of you but, seriously, I’m going to have to start taking your phone away when you clock in."
    s "Congratulations, Molly. I now understand why I had to be here for this."

    scene gamerbattle32
    with dissolve

    mo "To experience firsthand one more example of how great I am as the girl who may potentially be the {i}only{/i} undefeated Dorm Wars competitor by the end of tomorrow night?!"
    s "Sure. Let’s go with that."
    mo "Thank you, Sir! I’m glad that I was able to share this experience with you even if you had no idea what was happening at any point and were nearly killed by a dolphin."
    s "Yeah, the dolphin disappeared a little while ago and I’ve been on edge ever since, so...I’m just going to-"

    "A faint tapping on my shoulder reminds me of how fleeting life is."
    "So...if I turn around and come face to face with my demise, there’s something I want you to know."

    scene black
    with dissolve2

    "And that something is this:"
    "Being around dolphins is exhausting."
    "That is all."

    scene gamerbattle33
    with dissolve

    s "Oh. It’s just you."
    u "..."
    s "..."
    s "Right. You have to stay in character."
    s "I’m assuming that letter is for me?"
    u "Do not speak...You’ll give away our location...And it is finally gone..."
    s "..."
    u "..."
    s "I understand entirely. Give me the note."

    scene black
    with dissolve2

    "I snatch the card out of Uta’s hand and turn it over to find that my next “mission” is walking approximately half a mile away from the arcade- a thing I’m definitely excited to do in the midst of summer."
    "And while that may sound like a complaint (Because it {i}is{/i} one), I’m not {i}entirely{/i} distraught as it appears that this “mission” involves kicking off the date war right away."
    "Considering that this is likely going to take several hours, I nod to the rest of the girls and say my goodbyes."
    "Unfortunately, all of them know where I am headed due to the Dorm War schedule being public knowledge, so all that happens in saying goodbye is me managing to make everyone jealous before disappearing."
    "But hey, at least {i}one{/i} person is having a good day so far."

    $ renpy.end_replay()
    $ dormwartwo4 = True
    $ dorm2war2points += 1
    $ molly_love += 1
    $ sana_love += 1

    "{i}Molly MacCormack has defeated Sana Sakakibara!{/i}"
    "{i}First Floor: 0\nSecond Floor: 1{/i}"
    "{i}Molly’s affection has increased to [molly_love]!{/i}"
    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    play sound "phonebeep.wav"
    "{i}You have received two new picture messages from Imani Imai and Miku Maruyama!{/i}"
    "........."
    "......"
    "..."

    jump dormwartwo5

label dormwartwo5:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```