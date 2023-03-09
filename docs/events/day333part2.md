# Lesbian Stuff
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=day333part2&go=Go)


Part of event chain [Record Breaker](./day333.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
* [Ayane: Under the World Tree](./dojo35.md)

## Event properties
* ID: day333part2
* Group: Main
* Triggered by label: day333

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label day333part2:
    scene doubledate1
    with dissolve

    m "Help."
    m "This strange man is following me and I think I’m in danger."
    os "Wow. "
    os "You know, I’ve been thinking about it for a while, but you really don’t look like you should be working here."
    s "Thanks, Osako. It’s nice to see you too."
    w "School hours are over. I can’t do anything for you."
    w "If you are still alive when[school] opens tomorrow-"
    w "Actually, just find someone else. I don't want to deal with this."
    s "She’s not in danger anyway. We’re just both heading in the same general direction and apparently that grosses her out or something."

    scene doubledate2
    with dissolve

    os "Fair enough."
    w "That’s a perfectly acceptable reason to be disgusted. You’re the scum of the earth."

    if bonus == True:
        m "I’m somehow relieved that you’re not as popular with adults as you are with [teenager]s."
    else:
        m "I’m somehow relieved that you’re not as popular with the staff as you are with the students."

    s "Yeah, don’t worry Maya. These two are too in love with one another to ever fall for me anyway."

    scene doubledate3
    with dissolve

    os "Oh! Hahahaha..."
    os "I...don’t know if Wakana really wants word of that getting out in her workplace..."
    w "You said something I don’t inherently despise for once. How nice."
    m "Uhh...congratulations. But I’ll be going now."
    m "I don’t really see how any of this relates to me."

    if bonus == True:
        s "Don’t you want to be part of a cool adult conversation where all of us do cool adult stuff and you get to feel included?"
    else:
        s "But this is finally your chance to be part of the cool crowd. Just look at us and how...cool we are!"

    scene doubledate4
    with dissolve

    m "Do you really think that’s the kind of stuff that I’m interested in?"

    if bonus == True:
        m "I may act mature for my age, but I’m still a [teenage]girl and would much prefer to hang out with people that aren’t paying homeowner's insurance."
    else:
        s "Yes."
        m "No."

    m "Now stop following me."
    w "Heh...You look sort of like a kitten right now, Osako."
    w "Do you mind if I pet you?"
    s "Isn’t this fun, Maya? We’re about to watch lesbians do lesbian stuff."
    m "Yes. Hooray. Again, this has nothing to do with me."

    scene doubledate5
    with dissolve

    os "Hey! Uhh...Wakana and me were just going to go out for coffee and-"
    w "Wakana and {i}I{/i}, my cute little kitten. "
    os "Wakana and I were about to go out for coffee and...if you two aren’t doing anything...why not come with us?"
    m "No thanks."
    s "Sure. I’m okay with it if Maya is."

    scene doubledate6
    with dissolve

    m "Have you just given up on paying any attention to me for the rest of the day now that all of the world ending stuff is out of the way?"
    w "World ending stuff?"
    s "Long story. But also, yes. "
    s "We finished our formally scheduled conversation and are now free for the rest of the day."
    s "And if you leave now, I’d just wind up following you to your dorm and forcing you to hang out with me anyway."
    os "Is...it really okay for you to say stuff like that in[school]?"
    m "I don’t know these people. What reason is there for me to join all of you when-"
    s "I’ll buy you food."
    m "I..."

    scene doubledate7
    with dissolve

    m "Mmh!"
    s "Did you just scoff at me?"
    m "You tapped into one of my weaknesses and now I’m having a hard time declining."

    scene doubledate8
    with dissolve

    os "If it makes you feel any better, I’ve kicked this guy’s ass on multiple occasions now and could easily intervene if he tries to pull anything on you."
    m "Thank you. That does make me feel slightly better."
    w "Peculiar."
    s "What do you mean?"

    if bonus == True:
        w "I had just assumed this girl was one of your concubines due to her outburst when that pink haired anarchist professed her love to you."
    else:
        w "The spirits are telling me that this girl might be able to manipulate time."
        s "=O"

    scene doubledate9
    with dissolve

    m "Okay. If we’re going to get coffee or whatever, let’s do it now."
    m "There’s no use standing around talking about things that don’t matter to anyone when there are...bagels and stuff."
    s "That’s a bit of a touchy subject seeing as I just had to convince Maya not to murder that girl less than twenty minutes ago."
    w "Huh. "
    w "Well, I never have to be convinced to {i}not{/i} talk about something, so that’s fine."
    w "But if you two are coming, please try to keep conversation to a minimum. "
    s "Just don’t bring up stars or religion or whatever and I’m sure that much will be doable."

    scene doubledate10
    with dissolve

    m "I hope you’re aware that you are the actual bane of my existence."
    s "I hope you’re aware that you have an allowance for this double date and that I will not be bankrupted by a girl with a bottomless pit for a stomach."
    os "A...double date, huh?"

    if bonus == True:
        os "That’s actually really cute if we...ignore the fact that one of the girls isn’t old enough to drink and is...going out with her teacher."

    m "Don’t call it a date. I didn’t agree to that."
    m "I’m just hungry."
    s "Well then, like you said, there’s no use standing around."

    scene black
    with dissolve2
    stop music fadeout 13.0

    "Maya grabs her coat out of her locker and the four of us leave the[school] together."
    "We begin walking in the opposite direction of the path I normally take home and it quickly becomes clear to me that there are still a lot of places in Kumon-mi that I’m not familiar with yet."
    "We pass by the takoyaki stand Maya brought me to a long time ago and I notice that it’s closed for the winter."
    "Either that or the old man running it died and left it to rot."
    "I wonder how many pounds of octopus still linger within the confines of the cart’s freezers?"
    "I wonder how rotted they’ve become and if any insects have managed to crawl their way inside to feed off of the-"

    os "Okay! We’re here."
    s "Oh."
    s "That was...extremely quick."

    "………"
    "……"
    "…"

    scene doubledate11
    with dissolve
    play music "cafe.mp3"

    s "…"
    m "…"

    scene doubledate12
    with dissolve

    os "…"
    w "…"
    os "So...now what?"
    os "Wakana and {i}I{/i} haven’t been on a double date since college."
    m "Please...don’t call it that. I just want to eat."
    w "I’d prefer not to think about anything that happened in college."
    w "This also wouldn’t qualify as a double date considering the two on the opposite side of the table are here against their will."

    scene doubledate13
    with dissolve

    m "Correction: {i}I{/i} am here against my will. Frankly, there is no place Sensei would rather be."
    s "Wow, you really do know me better than I know myself."
    m "That aspect of your personality is just common sense. "
    m "Why else would you spend so much time chasing after someone so obviously trying to get away from you?"
    os "Hahah...that sounds a little like us."
    m "Please don’t explain why."

    scene doubledate14
    with dissolve

    w "Osako kept her feelings for me secret for far longer than she had to."
    os "You’re...not exactly easy to approach about that sort of thing, you know."
    os "And since we were already friends...it made it like, eleven times harder."
    w "Eleven?"

    scene doubledate15
    with dissolve

    os "Yeah. I don’t know. Leave me alone."
    w "Osako gets embarrassed when we talk about the old days. Please don’t pay it any mind."
    w "She’s a lot more...brazen when we’re alone. "

    scene doubledate16
    with dissolve

    m "I changed my mind. I love them and I want them to be together forever."
    s "I didn’t realize your mind needed changing."

    if bonus == True:
        m "I initially mistook them for a swinger couple trying to get the two of us involved in their...antics."
        m "And that this was a meeting designed to get me to open up to the idea of it."
    else:
        m "Honestly, I was just a little upset because I wanted to be alone with you and thought they'd get in the way."

    s "And you still came?"

    if bonus == True:
        m "You underestimate my love for food."
    else:
        m "You underestimate my love for you."

    scene doubledate17
    with dissolve

    if bonus == True:
        os "Oh my God, I...didn’t even realize that...people your age could interpret things that way."
        os "I guess the...sudden invitation probably did seem a little weird then..."
        w "While it’s true that relationships like that exist, I think it’s a bit unfair to immediately assume my partner and I were a part of one."
        m "It is, and I apologize. I can’t help but be a little judgemental at times and, unfortunately, Ms. Watabe’s reputation isn’t exactly...good."
    else:
        os "Oh my God, I...didn’t even realize that...Of course you two would want to be alone."
        m "It's fine. Also, I may have been a little on edge because of Ms. Watabe’s reputation."

    scene doubledate18
    with dissolve

    w "I beg your pardon?"
    s "Careful, Maya. She can probably give you detention."

    scene doubledate19
    with dissolve

    m "At the risk of sounding rude, there are just a lot of girls who think she might be into some...strange practices."
    w "Please explain what you mean by “strange practices.”"
    m "I’m afraid I can’t do that without relinquishing my aura of stoicism and I am, once again, very sorry."
    s "I could call Nodoka and find out. She seems to really like Wakana."

    scene doubledate20
    with dissolve

    w "Absolutely not. The last thing I want is that smut writer rattling off her fantasies about me over the telephone for the whole world to hear."
    os "That’s not how phones work, babe."
    w "Silence, Osako. Clear my name to our companions. I’m too infuriated to speak."
    os "I...don’t really want to tell them about our...{i}personal{/i} life..."
    s "That’s unfortunate because I really want to hear about it."
    m "May I be excused? Despite how fond I’m growing of you two, I’m still here for the food and I’m pretty sure we order at the counter."
    s "But we’re finally getting to the good part."

    if bonus == True:
        m "No, we’re getting to the swinger part. The part I specifically stated that I want no part of."
    else:
        m "No, we’re not."

    m "Now, if you’ll please excuse me."

    if bonus == True:
        "Maya gets up and goes to the counter to likely order every single item on the menu, leaving me alone with two women who have probably even {i}less{/i} interest in sleeping with me than she does."
    else:
        "Maya gets up and goes to the counter to likely order every single item on the menu...but she doesn't ask me if I want anything first =("

    "Today is suddenly bad."

    scene doubledate21
    with dissolve

    os "So...what’s that girl’s name again? She’s...a lot different from Ayane."
    w "Oh, right. This incorrigible fiend is also a student of yours."
    s "Her name is Maya. And yes, she is very different from Ayane."
    os "Does Ayane know you’re out with her? Because...I was pretty sure you two were like...you know."

    if bonus == True:
        w "Rumor has it that he is “you know” with roughly half of his class."
        s "That rumor is false, thank you very much."

        "I have yet to crack the halfway point."
        "But rest assured, Wakana-"
        "I will get there."
    else:
        s "Absolutely not. Ayane is nothing more than my student and karate partner. I would never look at her, nor anyone that way."

    os "Well...whatever the case, I like this girl. "

    if bonus == True:
        os "She doesn’t really talk the way most girls her age do."
    else:
        os "I want to jingle her bell and stuff."

    w "…"
    w "Oh my. "

    if bonus == True:
        w "{i}Are{/i} you actually attempting to swing, Osako?"
    else:
        w "Are you contemplating leaving me for her?"

    scene doubledate22
    with dissolve

    os "God, no! I was just saying that this is kind of fun and that we should maybe do it again sometime or something!"

    if bonus == True:
        s "That sounds like what a swinger would say."
        w "It does..."
        w "You haven’t been hiding another strange fetish from me, have you?"
        s "{i}Another?{/i}"
    else:
        s "But what does that have to do with her bell?"
        w "Yeah. What {i}does{/i} that have to do with her bell?"
        w "Do you have {i}another{/i} strange hobby I haven't been made aware of yet?"

    scene doubledate23
    with dissolve

    os "It’s not {i}another{/i}! It would be the first one!"
    os "And it isn’t! Because it’s not true!"
    w "Hm...whatever you say."
    w "Despite being a teacher, I’m not very in tune with what youths nowadays are after."

    if bonus == True:
        w "But if you say that wanting to be blindfolded, tied up, and teased is normal, I have no reason to disbelieve you."
    else:
        w "But if you say playing Fortnite for nine hours a day is normal, I have no reason to disbelieve you."

    scene doubledate24
    with dissolve

    os "{i}Wakana, why?!{/i}"
    os "It’s not even that weird! And now I’m going to have to kill him for knowing!"

    if bonus == True:
        w "If you’re going to go all out with this swinging thing, you’re going to have to disclose your interests to all parties first."
    else:
        w "You can't. He is the huggy boy."

    os "Oh my God, I hate you so much. "
    s "I don’t think I’ll ever be able to look at you the same way again."
    os "Ahhhhh! Come on!"
    m "Okay, I’m back. I only ordered half of the menu items and-"

    scene doubledate25
    with dissolve

    m "..."
    m "What did you do?"
    s "It really wasn’t my fault this time."
    m "Right. And why is Ms. Watabe’s girlfriend covering her eyes?"
    s "..."

    if bonus == True:
        s "Because she likes being blindfolded."
    else:
        s "Because she likes Fortnite, I think?"

    os "Mmmmmmm!"
    m "...I don’t get it."
    s "Because you’re too [young]and innocent."

    scene doubledate26
    with dissolve

    m "Uh-huh. Right."
    w "While my partner grieves at the loss of one of her most intimate details, I would like to take a moment to make an important announcement."

    scene doubledate27
    with dissolve

    m "An...important announcement?"
    m "You didn’t invite us to some sort of...big thing, did you? Because I still barely know either of you and would feel very uncomfortable if that were the case."

    scene doubledate28
    with dissolve

    os "An...announcement?"
    os "But what would you be-"

    scene doubledate29
    with dissolve

    os "Oh my God...are you..."
    os "Is this what I think it is?"
    m "I really, really hope not."
    os "Wakana..."
    os "Are..."
    os "Are you..."
    w "Everyone..."
    w "Osako..."

    scene doubledate30
    with dissolve

    w "I want to fucking die."
    s "Beautiful."
    m "…"
    os "…"
    os "You..."
    os "Why would that be...an important announcement?"

    scene doubledate31
    with dissolve

    w "Were you expecting something else, my kitten?"
    os "No! I just..."
    os "I’m gonna go order something, too!"
    w "Would you mind ordering me another tea, my love?"
    os "Fine! What kind?!"
    w "Lavender, please. It will remind me of your eyes."
    os "God, I hate that you’re so cute!"

    scene black
    with dissolve2

    "As Osako clumsily runs over to the counter to order, Wakana removes a notebook from a large black bag and begins to scribble something down on it."

    if bonus == True:
        w "This was fun. And, at the risk of sounding like a swinger, I’d like to invite you both to do it again sometime."
    else:
        w "This was fun. And, at the risk of sounding like a fun person, I’d like to invite you both to do it again sometime."

    w "It isn’t often that Osako and I spend time with other couples. And even if you two are not romantically involved, I’d like the opportunity to tease her some more around you, if you will have us."
    w "Doing so is the only thing that can shine light upon the dark tangle of wires that has become my heart."
    m "I will respectfully decline."
    s "I will respectfully accept your phone number. "
    s "But if Osako tries to beat me up for texting you, I’m going to need you to stand up for me."
    w "Osako is a free woman and you will accept my telephone number fully understanding the risk it carries with it."
    s "Damn it. Fine. Just give it to me."
    m "Absolutely pathetic."

    "I mark this down as a victory in my book not only because I got a new phone number, but because Maya called me pathetic instead of disgusting for once."
    "Which...I guess isn’t really much better in the grand scheme of things."
    "Or better at all, for that matter."
    "But hey, phone number."
    "Osako returns a short while later with a spread of pastries for all of us to share and, after we spend around forty-five minutes eating everything, we pay our bills and leave the cafe..."

    $ renpy.end_replay()
    $ wakananumber = True
    $ day333part2 = True
    stop music fadeout 5.0

    "{i}Congratulations! You now have Wakana’s phone number!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label day340:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
if bonus == True:
        s "I don’t know. I think you might just be a secret pervert."
        m "I’m not a secret pervert."
        s "How can I be so sure?"
        m "Because...I’m not. Now, can we please talk about the reset?"
    else:
        s "I don’t know. I think you might just like me."
        m "I do. I have always liked you. Please give me more attention and stop hugging other girls."
        s "Mmmmmmmmmmmmmm no thanks."
        m "Fiojhsdfgouhsdiufghuasdfoisdf FINE let's just talk about the reset then."

    m "That {i}is{/i} the reason I called you here, after all."
    s "Fine, fine. "
    s "So, it’s coming and {i}I’ve{/i} never made it that far before. "
    s "Do you have some sort of plan or something that will help me...survive?"

    scene aminewuniform16
    with dissolve

    m "Hm..."
    m "I have one plan, but I don’t think you’ll like it."
    s "What is it?"
    m "Killing Noriko."
    s "Yeah, I don’t like that at all."
    s "I also don’t think that would change anything and that you’re just letting your grudge get the better of you again."
    m "Possibly. But I do think it would be better to be safe than sorry."
    s "Any plans that don’t involve killing one of your classmates?"

    scene aminewuniform20
    with dissolve

    m "Just to do things normally again, I suppose."
    m "Last time, I was an absolute idiot and let my mind get crowded during the process. Which may or may not have led to the destruction of an entire[school]."
    m "It’s still hard to tell if that was my fault or not. "
    m "But given that it was such an unusual change, I can’t help but hold myself at least slightly responsible."
    m "If everyone you’ve met over the last couple months {i}does{/i} disappear, though, know that I will not shed a single tear and that I would actually {i}prefer{/i} things that way."
    s "Really? Even after the dorm wars? "
    s "You won’t feel upset about all of your new friends just vanishing overnight?"
    m "Not really. "
    m "I’ve become rather exceptional at not getting attached to anything since my life has been reduced to near-quarterly looping through the same[school] year over and over and over."
    m "It’s incredibly exhausting, to tell you the truth."
    s "Well, hopefully I’m able to continue exhausting you in the future."
    s "It would kind of suck if things just ended here."

    scene aminewuniform22
    with dissolve

    m "Good. That’s exactly what I wanted to hear."
    m "Start treasuring your life. "
    m "Treasure it...but don’t do anything stupid with it either."
    m "It can be scary how fragile our existence is at times. "
    m "One wrong move and you might wind up back at the start."
    m "I hope things don’t come to that, though, because..."

    scene aminewuniform23
    with dissolve

    m "Well..."
    m "It would probably be a little {i}more{/i} exhausting having to explain everything over again from the beginning."
    m "You know basically just as much as I do now."
    m "Well, about the world and how it works, at least."
    m "There’s still plenty I know about your history that I can’t disclose without the fear of melting your brain."
    m "But life itself feels new again."
    m "Everything that’s happened recently is something I’ve never seen."
    m "And...it’s terrifying."

    scene aminewuniform20
    with dissolve

    m "But that’s enough of my expressive self for today."
    s "Really? You looked cute with your little smile just now."
    m "Shut up."
    m "I’ve warned you of the encroaching reset, so now it’s entirely on you to make it to the roof."
    s "Can you just meet me at my house next time?"
    m "Absolutely not. That is a horrible idea and never plays out the way I expect it to."
    m "Just save both of us some trouble and come to the roof on your own. "
    m "I’ll be waiting..."
    m "Just like always."

    scene black
    with dissolve2

    "Maya goes to leave the classroom and I follow closely behind her."
    "Not because I’m trying to spend more time with her or anything, but because it would simply be strange for me to continue standing around here when the final bell rang nearly an hour ago."

    m "Stop following me."
    s "We’re both leaving[school], aren’t we? What’s the harm in walking together for a little while?"
    m "There is no {i}harm{/i}. It’s just not something I particularly enjoy."
    s "That’s fine. I’ll just walk silently behind you and admire you from the back then."
    m "You’re disgusting."

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ day333 = True

    jump day333part2
...
```