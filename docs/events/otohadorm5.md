# Highly Pornographic
Otoha event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohadorm5&go=Go)



## Event preconditions
✅Otoha love greater than or equal to 5

✅Event "[Otoha: Locked In](./otohapark5.md)" is completed (event=otohapark5)

✅Day of week is a weekend



## Next events
* [Main: Operation: Firestarter](./day318.md)

## Event properties
* ID: otohadorm5
* Group: Otoha
* Triggered by label: otohadorm
* Triggered by branch label: doorknock2

## Event code
File: \game\Dorm2Events.rpy
Code:
```python
...
label otohadorm5:
    play sound "knock.mp3"

    "I knock on Otoha’s door and wait for her to answer."
    "I’ve gotten to spend time with her at[school] and in the park before, but..."
    "The two of us haven't really gotten to be alone in her dorm without any interference from others yet."
    "Not that I expect anything exciting to happen, but she’s proven to be excitingly...normal by now."
    "And, given that I spend my life surrounded by people like Molly and Tsuneyo and Ayane and..."
    "Well, you get the point."
    "There are a lot of strange girls in my class."
    "So I shall wait patiently for this one particular outlier to answer."

    s "…"
    s "…"
    s "…"

    "I can no longer be patient."

    play sound "knock.mp3"

    s "Otoha, are you in there? "
    o "Mmph! Unn...sec!"
    s "...What?"
    o "Mngh. Sorry! I was eating."
    o "Door’s open."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "I walk into the room and kick my shoes off at the door, hoping that I’ll wind up staying here for at least an hour or two so I don’t have to awkwardly put them back on after like five minutes."
    "That has happened before and it has not been enjoyable."

    scene otohapajamdorm1
    with dissolve

    o "Heeeeeey..."
    o "Isn’t it a little late for you to be coming over?"
    o "I’m already in relax-mode."
    s "You look very comfortable."
    s "And hungry."

    scene otohapajamdorm2
    with dissolve

    o "Hahah...yeah..."
    o "Nodoka’s at some bookstore with Futaba tonight and Rin’s playing some game with her other friends, so I figured I’d just...do my own thing."
    s "And your own thing is gorging yourself on doughnuts and-"
    s "Wait, is that the sausage fest?"

    scene otohapajamdorm3
    with dissolve

    o "I was curious, okay?! You made it sound so...sausagey!"
    s "Otoha’s first sausage fest...and I get to be here for it."
    s "Niki would be so proud..."

    scene otohapajamdorm4
    with dissolve

    o "Do you want something or are you just here to try and embarrass me?"
    s "Just thought I’d come see what you were up to."
    s "You look nice with your hair down, by the way."

    scene otohapajamdorm5
    with dissolve

    o "Yeah? Thank you."
    o "I really only put it up because I friggin' hate how it feels when the wind pushes it into my eyes."
    o "Surprised it’s not like, too red for you or whatever."
    s "I mean, Ami’s hair is completely red and I haven’t gotten fed up with that yet."
    o "Yeah but Ami’s hair is cute and mine is just...hair."
    s "…"
    s "Yes. Your hair {i}is{/i} hair."
    o "Yeah, see? You get it."

    "I don’t."

    scene otohapajamdorm6
    with dissolve

    o "Do you want a doughnut?"
    o "I’ll probably eat all of them if you don’t take any and I don’t think my body will like that very much."
    s "No. But your heart will."
    o "What does that even mean?"
    s "It means that you should do whatever makes you happy. And if that means eating a box of doughnuts and two pounds of sausage noodles, so be it."
    o "Welp, I did pay for all of it...so I might as well go to town."
    o "Oh hey, are you good with technology by any chance? Because I can’t get this stupid TV to listen to me."
    s "What’s going on?"
    o "It’s just not doing anything when I press any of the buttons."
    s "Maybe the remote is dead?"
    o "The buttons on the TV aren’t working either. It’s just stuck on some weird picture."
    o "I think it might be frozen."
    s "Have you tried turning it off and back on?"

    scene otohapajamdorm7
    with dissolve

    o "Just tell me you’re not good with this kind of stuff if you’re going to keep giving me generic tips."
    s "Hey, you would be surprised how many things can be fixed by turning them off and then back on."
    o "I {i}have{/i} tried that, Sensei. It’s just-"
    o "You know what? Never mind. I’ll just keep myself entertained by talking to the old guy in my room like everyone else does here."

    "I somehow manage to defeat a magical rectangle in the battle for a [young_girl]’s attention."
    "I ascend."

    s "Couldn’t you have just played with Rin and the other girls? I’m pretty sure they’re right next door since Molly is like, the leader of their...game group or whatever."
    o "I would have, but Rin seemed weirdly against me coming for some reason."
    o "I’m not that close with any of the others yet anyway. She probably just wanted to avoid things being awkward."

    "Or she wanted to avoid you thinking she’s a nerd...which sounds a lot closer to what Rin would do if she’s approaching Otoha the same way she approached Chika."

    s "The game they play is kind of weird anyway. We’re better off in here."
    o "Is it like, a video game or something?"
    s "Not really. They all have these weird sheets of paper and talk in strange voices to one another."

    scene otohapajamdorm8
    with dissolve

    o "Huh."
    o "Well that definitely doesn’t sound like any game I’ve ever played before."
    s "Like I said, we’re better off in here where-"

    scene otohapajamdorm9
    with hpunch

    mo "SEVEN VIOLET FUNGUS APPEAR! ROLL FOR INITIATIVE!"
    r "Molly! Shh!"
    s "…"
    s "Like I was saying, we’re better off in here where it’s safe."

    scene otohapajamdorm10
    with dissolve

    o "I guess you’re right."
    o "Besides, I've barely eaten all day...so I should probably do that now anyway."
    s "Well you...certainly have the required materials to do just that."

    scene otohapajamdorm3
    with dissolve

    if bonus == True:
        o "I’m a growing girl, okay?! And if I don’t eat balanced meals, I’ll wind up looking all tired and dead inside like that one teacher Nodoka has the hots for!"
        o "The one that isn't you! The girl one! With the skirt!"
    else:
        o "I like food, okay?! And this is a perfectly balanced meal!"

    s "What exactly is {i}balanced{/i} about your dinner, Otoha?"
    o "It’s got all the food groups! Sausage, pastry, soda! Come on, man!"
    s "Oh..."
    s "You have no idea what to do now that you have to provide food for yourself, do you?"

    scene otohapajamdorm11
    with dissolve

    o "Well I obviously don’t think those are the real food groups, but...yeah."
    o "I’m used to my parents making dinner for me...so I’m stretching my wings and eating stuff that makes me happy instead of...green stuff."
    s "You poor, lost soul."
    s "I’m sure I used to be just like you until I acquired a [niece]."
    o "Oh, yeah. Let me just go out and get one of those really quick. Great advice."

    if bonus == False:
        s "It really is, though. They are very helpful."

    scene otohapajamdorm9
    with hpunch
    play sound "phonering.mp3"

    o "Ahh!"

    stop sound fadeout 5.0

    s "…"
    s "It’s just your phone, Otoha."
    s "You don’t actually get scared that easily, do you?"

    scene otohapajamdorm12
    with dissolve

    o "Of course not! I just...wasn’t ready for that."
    o "It surprised me."
    s "So what you’re telling me is you...got scared."
    o "Shut up. I’ve gotta take this."
    o "Hold your ears closed and...don’t listen to what I say in case it’s some...super secret business or something."
    s "Right..."

    scene black
    with dissolve

    "Otoha grabs her phone and hops off of the bed, nearly killing the sausage fest in the process."
    "Instead of exiting the room, which is what I expected her to do on account of telling me not to listen, she takes a seat on her stool and answers the call."

    scene otohapajamdorm13
    with dissolve
    play sound "phonebeep.wav"

    o "Hello?..."
    o "…"
    o "Yeah. "
    o "Yeah. I’m eating fine."
    s "You fucking liar."

    scene otohapajamdorm14
    with dissolve

    o "Shh!"

    "Otoha shushes me and whatever object has taken the place of my heart skips a beat."

    scene otohapajamdorm15
    with dissolve

    o "Huh?!"
    o "What?!"
    o "No! You didn’t hear a boy just now! That was the TV!"
    o "…"
    o "No, it really was! Listen!"

    scene otohapajamdorm16
    with dissolve

    o "{i}Help me...{/i}"
    s "…"

    "I decide to help Otoha by mimicking my favorite television program."

    if bonus == True:
        s "Take that, you little slut."
    else:
        s "BUT THIS GRILL IS NOT A HOME. THIS IS NOT THE STOVE I KNOOOOOOOOOW."

    scene otohapajamdorm17
    with hpunch

    o "Sorry! My roommate just changed the channel on accident! I’m leaving the room now!"

    if bonus == True:
        "My favorite television program is highly pornographic, by the way."
    else:
        "My favorite television program is Spongebob Squarepants."

    o "No! I’m doing totally fine! I don’t need any money!"
    o "…"
    o "Yeah. Yeah,[school] is great."
    o "…"
    o "My teacher?"
    o "Well, uhh..."

    scene otohapajamdorm18
    with dissolve

    o "He could be better."
    s "What the fuck?"
    o "Yeah..."
    o "Yeah."
    o "Okay."
    o "Love you too. Bye."

    play sound "phonebeep.wav"
    scene otohapajamdorm19
    with dissolve

    o "…"
    s "…"
    s "How was your phone call?"
    o "I invite you...into {i}my{/i} home...and offer you one of {i}my{/i} doughnuts..."
    o "And {i}this{/i} is how you repay me?"

    if bonus == True:
        o "By mimicking a porno?"
    else:
        o "By singing a song from Spongebob?"

    s "It has normal scenes as well. I just chose one of the racy ones."

    scene otohapajamdorm20
    with dissolve

    if bonus == True:
        o "That was porn! I know porn when I hear it!"
    else:
        o "I know how Spongebob works!"

    s "Do you?"
    o "Yes but don’t misinterpret that!"

    if bonus == True:
        s "There’s really only one way to interpret that, Otoha."
    else:
        s "But how would I even-"

    o "Sensei! That was my mom! You can’t just yell things like-"

    scene otohapajamdorm21
    with hpunch

    mo "Oi! Quiet down in there! There are other people on this server, you know?!"
    o "Ah! Sorry! Sorry!"

    scene black
    with dissolve

    "Otoha throws her phone onto the bed, once again almost killing the sausage fest, before moving past me and sitting back down."
    "Just...this time, she looks a lot less pleased with me than she did when I first arrived."

    scene otohapajamdorm22
    with dissolve

    o "…"
    s "…"
    o "If this is what having an older brother is like, I’m glad I was born an only child."
    s "Oh come on. I’m sure that one day we’ll look back on this and laugh about it."
    o "Yeah. Totally. I can hear it now. "

    if bonus == True:
        o "“Hey, remember when you called me a little slut while I was on the phone with my mom?”"
        o "“Hahaha. So funny.”"
        s "In my defense, I was not calling {i}you{/i} a little slut. It was a line from the-"
        o "Sensei..."
        s "…"
    else:
        o "IT'S JUST A GREASY SPOOOOOOOON."
        s "{size=-15}without yooooouuuuuuuu..."
        o "..."
        s "..."

    s "Am I...in trouble?"
    o "Yes."
    o "Seriously. Don’t do stuff like that."
    o "It’s nothing short of a miracle that I was even allowed to come live here."
    o "One wrong move and that could all come to an end. My parents know the address of this place and they could come get me at any moment."
    s "Oh great. I’m sure that’s not an omen for them to show up at the worst possible time in the future."
    o "There won’t {i}be{/i} a future if you keep doing stuff like that."

    scene otohapajamdorm23
    with dissolve

    if bonus == True:
        o "I’ve obviously come around to hanging out in here with you if we're both bored, but please don’t do things that will make my leash even tighter."
        s "Just take the leash off entirely and stop answering them."
    else:
        o "They're the ones paying my tuition. I can't just...not listen to them anymore."
        s "Just kill them."

    scene otohapajamdorm24
    with dissolve

    o "Dude, no, They’re still my parents."

    if bonus == True:
        o "Just be respectful and stay away from sex jokes while I’m talking to them. That’s all I want."
    else:
        o "Just be respectful and don't sing Spongebob songs around them. That's all I want."

    o "And maybe 1,000 yen. That would be cool too."
    s "You and this damn 1,000 yen. I literally just heard you tell your mom you didn’t need any money."

    scene otohapajamdorm25
    with dissolve

    o "Doesn’t mean I don’t {i}want{/i} any. Pay up, Sensei. It’s a fine for being a jerk."
    s "I’ll give you 1,000 yen...but I need the doughnuts in return."

    scene otohapajamdorm26
    with dissolve

    o "Wait, all of them?!"
    o "I thought you didn’t want any!"
    s "It’s for your own good, Otoha. "
    s "Besides, once you try the sausage fest, you’ll never want to eat anything else ever again."
    o "I already had a few bites."
    o "It’s...extremely average."
    s "{i}How dare you...{/i}"

    scene otohapajamdorm27
    with dissolve

    o "Ugh. Keep your money. I’ll just eat my doughnuts and watch this weird picture of a house until-"

    scene otohapajamdorm28
    with dissolve

    o "Oh. The TV went back to normal."
    o "When did that happen?"
    s "Beats me. I’m glad things worked out, though."
    s "I was starting to think I may have ruined your night."
    o "You did ruin my night, but I signed up for that when I invited you in."
    s "I like this. This is good."
    o "Like what? What’s good?"
    s "Us. You don’t let me walk all over you but you aren’t extremely abrasive in telling me to stop."
    o "Yeah, I just think you’re really annoying."
    o "Now shush. I’m gonna watch TV and eat junk food all night and you can either hang out and deal with that or just get out."
    s "Understood. Move over."

    scene black
    with dissolve2

    "I take a seat next to Otoha and {i}do{/i} ultimately receive a doughnut."
    "She manages to finish the other three as well as the entire sausage fest, and I suddenly feel the urge to visit Maya and inform her that there may be someone else in the class who is just as good at eating as her."
    "I don’t, though."
    "Instead, I hang out and watch some reality show with Otoha until Nodoka gets home."
    "It was a surprisingly refreshing night, all things considered."

    $ renpy.end_replay()
    $ otoha_love += 1
    $ otohadorm5 = True
    stop music fadeout 5.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

                    ############################################
                    ##########        ROOM 9         ###########
                    ############################################

label toukadorm:
    if touka_love >= 1 and day != 4 and toukafirsthall == True and toukadorm1 == False:
        jump toukadorm1
    if touka_love >= 5 and day != 4 and toukastreets5 == True and toukadorm5 == False:
        jump toukadorm5
    if touka_love >= 10 and day != 4 and christmastwo20 == True and toukadorm10 == False:
        jump toukadorm10
    elif day304 == True and toukafirsthall == False:
        "I don't think Touka is ready to spend time with me in her room just yet."
        jump doorknock2
    else:
        jump toukadormgen

label toukahall:
    if toukafirsthall == False:
        jump toukafirsthall
    else:
        jump toukahallgen

label yasudorm:
    if yasu_love >= 10 and yasufirsthall == True and toukadorm5 == True and makotowinterbeach4 == True and yasudorm10 == False:
        jump yasudorm10
    if yasu_love >= 20 and church20 == True and day != 2 and yasudorm20 == False:
        jump yasudorm20
    elif day304 == True and yasudorm10 == False:
        "I don't think Yasu is ready to spend time with me in her room just yet."
        jump doorknock2
    else:
        jump yasudormgen

label yasuhall:
    if yasufirsthall == False:
        jump yasufirsthall
    else:
        jump yasuhallgen

label toukadormgen:
    play sound "knock.mp3"

    to "Come in!"

    scene toukadormgen
    with fade

    "I decide to spend the night hanging out in the dorm with Touka."
    "Despite the place being light years beneath her standards, she doesn't particularly seem to {i}hate{/i} things here."
    "Granted, she spends most of her time either alone or on video calls with different instructors to make up for my inadequacy as a teacher-"
    "But she hasn't asked for a transfer or gotten me fired yet, so that is a clear plus."

    scene black
    with dissolve

    "Eventually, she moves on to talking about her family's business and I can't help but begin to lose interest."
    "Her cuteness may get her far in life, and her great wealth may get her even further-"
    "But it will not get her to the point where she can talk about boring stuff without risking my interest."
    "And, obviously, I need to be the center of her affinities because this is a world made for me."

    if bonus == True:
        "I convince Touka to leave her family and become my sex slave. She obliges and, within moments, we are naked."
    else:
        "I convince Touka to leave her family and open up an Arby's with me."

    "Just kidding."
    "I never convince her to do any of that and, instead, decide to just head home."
    "But at least the two of us managed to get a little closer."

    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka's affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yasudormgen:
    play sound "knock.mp3"

    ya "Come in!"

    scene yasudormgen
    with fade

    "I decide to spend the night hanging out in the dark with Yasu."
    "I ask her to turn the lights on because I feel incredibly uncomfortable just watching her stand there smiling, but she refuses."
    "Apparently, even artificial light stings her eyes and it isn't just the sun that manages to do that."
    "My discomfort grows, but is quelled by the fact that, unlike some of the other residents of this dorm, she does not possess any weapons."
    "That being said, I absolutely would not be surprised if there were some weird religious ritual tools tucked away under her bed or something like that."

    scene black
    with dissolve

    "I make it through the night without dying, which is a thing a lot of unfortunate people out there aren't able to say."
    "Yasu probably makes it through the night without dying as well, but I can't say that definitively as I'm not there to watch her fall asleep."
    "For all I know, she could be sacrificing herself right now in the name of her god."
    "But I'm just going to assume that doesn't happen and hopefully run into her again tomorrow."

    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu's affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label toukahallgen:
    if chapthreeactive == True:
        scene toukasummer2hallgen
        with dissolve
    else:
        scene toukahall1
        with dissolve

    to "Good evening, Sensei."
    to "Please make no sudden movements or I will call the police."
    s "What kind of person do you think I am?"
    to "The worst kind. But I will still allow you to talk to me as there is a witness in the hall."
    i "Uhh...please leave me out of this."

    scene black
    with dissolve

    "I spend some time in the hall with Touka, trying to convince her that I am not the scum of the earth."
    "It does not work and I go home without making any sort of substantial impact on her life."
    "But at least her affection goes up."

    $ touka_love += 1
    stop music fadeout 5.0

    "{i}Touka's affection has increased to [touka_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label yasuhallgen:
    if chapthreeactive == True:
        scene yasusummer2hallgen
        with dissolve
    else:
        scene yasuhall1
        with dissolve

    s "Hey, Yasu. What are you up to tonight?"
    ya "Basking in the warmth of the second dorm floor, absorbing the vibrations that crawl up the sides of the building and-"
    s "That's nice. Do you want to hang out for a little while?"
    ya "Do you have a moment to hear about our lord and savior?"
    s "I have a moment to hear about other things. Not really that, though."
    ya "How sad. What better night than tonight to be saved?"

    scene black
    with dissolve

    "I do not wind up {i}being saved{/i}, but I do wind up killing time with Yasu in the hall."
    "Or, I'm sorry- Time winds up moving onto the second plane of existence because death is not real."
    "Regardless, the two of us make idle chit chat that scares Kirin back into her room and, before long, Yasu and I part ways."
    "I head home just as confused as I always am after talking to her."

    $ yasu_love += 1
    stop music fadeout 5.0

    "{i}Yasu's affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label toukadorm1:
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label otohadorm:
    if nodoka_love >= 0 and day288 == True and nodokafirsthall == True and otohafirsthall == True and day != 1 and day != 5 and nodokadorm1 == False:
        jump nodokadorm1
    if otoha_love >= 5 and otohapark5 == True and day > 5 and otohadorm5 == False:
        jump otohadorm5
...
```