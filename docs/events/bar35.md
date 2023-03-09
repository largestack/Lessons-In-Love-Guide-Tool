# Purest Intentions
Sana event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar35&go=Go)



## Event preconditions
✅Sana love greater than or equal to 35

✅Event "[Uta: Love Me to Pieces](./utamaid5.md)" is completed (event=utamaid5)

✅Event "[Main: Fireworks, Chicken, and the Innate Fear of Death](./christmas7.md)" is completed (event=christmas7)



## Next events
* [Ami: Third Place](./amimaid30.md)
* [Sana: Waiting for Anything](./sanadorm35.md)
* [Main: Let Me Die in Spring](./day261.md)

## Event properties
* ID: bar35
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar

## Event code
File: \game\SanaEvents.rpy
Code:
```python
...
label bar35:
    scene barwakaosako1
    with fade
    play music "calmbar.mp3"

    "I make my way to the bar to be immediately greeted by not only a warm atmosphere, but the warm smile of a girl under five feet tall."

    s "{i}You’re so adorable.{/i}"
    sa "Hm?...What was that?"
    s "Just saying hello. "
    s "How’s the bar doing?"

    scene barwakaosako2
    with dissolve

    sa "Umm...the same as always, I guess."
    sa "My mom isn’t feeling well tonight so I’ve...gotta do everything on my own again."
    s "Really? What happened?"
    sa "She may have...sampled too many of the products."
    s "Oh. {i}That{/i} kind of not feeling well."
    sa "Right..."
    s "Well, thankfully, it’s not like this place is busy or anything."
    s "I’m pretty sure roughly half of your sales are just...me."

    scene barwakaosako3
    with dissolve

    sa "Well...while that’s normally true...there’s someone here tonight that’s drinking a lot more than I’ve ever...seen {i}you{/i} drink before."

    "Sana redirects her gaze to a table in the back of the room that I must have overlooked upon entering."
    "I guess I’ve gotten so used to this place being completely dead that I’ve just stopped observing my surroundings. "
    "But knowing that it’s the back of the room, there’s a good chance that it’s the same old women who-"

    scene barwakaosako4
    with fade

    s "Wait, what?"
    s "Those two know each other?"
    sa "Do you...know them, Sensei?"

    scene barwakaosako5
    with fade

    s "I’m surprised you don’t. Well, the one on the right, at least."
    sa "Why would I know her? This is her first time coming in."
    sa "She’s not...some kind of celebrity, is she?"
    s "That’s Ms. Watabe- The teacher in the classroom next to ours."
    sa "…"
    s "Does that not ring a bell?"
    sa "Sensei...I don’t know if you’ve realized this, but..."
    sa "I kind of keep my head down all day in[school]."
    sa "I don’t even think I can...name another teacher."
    s "I literally just told you the name of one. "

    scene barwakaosako6
    with dissolve

    sa "Ms...Watanabe?"
    s "Watabe. You did that on purpose."

    scene barwakaosako7
    with dissolve

    sa "Sorry...but there’s only enough room in my head for one teacher."
    s "{i}You’re so adorable.{/i}"
    sa "You need to speak up...You’re being really quiet tonight, Sensei..."
    s "Yeah, well, you’re really quiet all the time. I’m just giving you a taste of your own medicine."
    sa "Well I need to...go give those girls a taste of more...medicine...so..."
    s "Just because your mother uses it to medicate both herself and you does not make it medicine, Sana..."
    s "But fine. Why don’t I help you?"
    sa "Help me?"
    sa "You mean like...you’ll carry the-"
    s "I won’t be carrying anything."

    scene barwakaosako8
    with dissolve

    sa "Of course you won’t..."
    s "I just want to see how you interact with other adults. "
    s "We’ve practiced your public speaking enough that it’s time for us to conduct our first field test."
    sa "You kind of...stopped teaching me about speaking altogether...you just sit there and drink now."
    s "True, but my intentions are pure."

    "No they aren’t."

    sa "So...you’re going to follow me to their table and just...watch me?"
    sa "Doesn’t that sound...a little weird for...pretty much everyone involved?"
    s "Ms. Watabe is dead inside so it will only be weird for three of us."
    s "It gives me an excuse to go say hi to them anyway."
    sa "Umm...okay, but...can you just...try not to be awkward?"
    s "…"
    sa "…"
    s "You’re the one telling {i}me{/i} not to be awkward? "
    s "Do you have any idea how popular I am?"
    sa "With [teenage]girls or...regular people?"

    if bonus == True:
        s "Mostly the former. But there are plenty of adults who love me as well. "
    else:
        s "How do they not count as regular people? A large portion of the population is in college."

    s "Just ask your mom."
    sa "Uhh...I’d really rather not..."
    sa "Anytime she talks about you I...kind of want to slap her in the face..."
    s "Getting jealous that she might steal me away from you?"

    scene barwakaosako9
    with dissolve

    sa "Jealous? Me? "
    sa "You really think I’d get jealous from...my mom and my best friend talking about you all the time?"

    "Clearly. I didn't even mention Ayane and she brought her up anyway."

    sa "Hahaha...Sensei, that’s so crazy...hahaha..."
    sa "I love listening to all of the things they say about you and...not being able to contribute to the conversation at all."
    s "What do you mean you can’t contribute to the conversation? I’m here for {i}you{/i} tonight, aren’t I? Just...brag about that."
    s "It means I'm choosing you over them."

    "Well, at least for right now."

    scene barwakaosako10
    with dissolve

    sa "Are you really, though?"

    scene barwakaosako7
    with dissolve

    sa "A-Anyway...I guess...feel free to follow me to the table and...see how much I’ve improved thanks to your...pure intentions."

    scene black
    with dissolve

    "Sana comes out from behind the bar and I get out of my chair to follow her."
    "The girls in the back of the room notice this and begin to tone down their conversation in preparation for more booze."
    "They also finally notice my presence, which makes me feel a little bit better about overlooking {i}them{/i} when I first came in tonight."

    scene barwakaosako11
    with dissolve

    os "Woah. When did you get here?"
    s "A little while ago. I didn’t realize you two were friends."
    w "Is it really such a surprise to you that I have a life outside of the[school]?"
    s "Kind of, yeah."

    scene barwakaosako12
    with dissolve

    sa "Um...can I...help you two with anything else?"
    w "Speak louder. You’re too quiet. "
    os "Another beer for me. Probably four more for my {i}friend{/i} here."
    w "Five."
    w "I can still feel things. It’s troublesome."
    os "Also, do you guys have like, some taxi service you’re partnered with or anything?"
    os "She drove tonight and I definitely don’t want to get into the car with her."
    w "If I’m lucky, maybe I’ll drive off of a cliff."
    s "Good luck finding a cliff in Kumon-mi."
    sa "We, umm...don’t really have anything like that, but...I can check on my phone if that will help you..."

    scene barwakaosako13
    with dissolve

    w "Would you like anything, {i}Sensei{/i}?"
    s "Are you...offering to buy me a drink?"
    w "No. I was going to order the rest of whatever you wanted so you wouldn’t be able to have any."
    w "Of course I was offering to buy you a drink."
    w "I’m extremely drunk. Can’t you tell?"
    s "Not really, no."
    w "Well, whatever. You missed your chance."
    sa "Okay, so...six more beers total..."
    sa "Is there anything else?..."

    scene barwakaosako14
    with dissolve

    s "You should order the spaghetti. It’s really good here."
    os "Huh? This place has a food menu? I had no idea."
    sa "It...doesn’t..."
    sa "Sensei is just being...a big jerk...and tormenting me..."
    os "Ooooooh okay, okay. So this guy’s your teacher."

    if bonus == True:
        os "Here I was thinking he was just getting himself involved in a {i}second{/i} relationship with a girl your age."
    else:
        os "Here I was thinking he was just getting himself involved with a {i}second{/i} college chick."

    scene barwakaosako15
    with dissolve

    sa "S...Second?"
    sa "There’s a first?"
    os "Yeah. Some loud blonde girl that trains at my dojo with him."
    s "Sana, meet my karate instructor, Osako. "
    s "She also works at a local ma-"

    scene barwakaosako16
    with dissolve

    os "Hey! You’re not forgetting that I can kick your ass, are you?!"
    os "You said you wouldn’t tell anyone!"
    s "I said I wouldn’t tell anyone {i}at the dojo{/i}."
    os "Life’s a fuckin’ dojo. Tell ANYONE-anyone and I’ll break your fucking arms."

    scene barwakaosako17
    with dissolve

    sa "So it’s just...karate and not...an actual relationship."
    sa "I knew Ayane went but...I didn’t know you were going there too, Sensei..."
    s "Really? It’s weird that she never told you given how much she apparently talks about me."
    sa "All of the things she says about you are a lot...um...more {i}romantic{/i}."
    w "So the rumors were true."
    s "Stop bringing up those {i}entirely baseless{/i} rumors and finish your beer, Wakana."
    w "I’ve been finished with this one for five minutes."
    w "I’m still waiting on another but you’re distracting this poor girl from doing her job."

    scene barwakaosako18
    with dissolve

    sa "O-Oh! I’m...s-sorry! I-"
    w "Don’t worry about it. There’s no way I’m going to remember any of this in the morning, anyway."
    s "You’re way too competent for how drunk you apparently are."
    sa "I...umm...I’ll be right back..."

    scene barwakaosako19
    with dissolve

    "Sana suddenly scurries off to the counter and begins to stack a bunch of cans on a tray to bring over, leaving me alone with Osako and Wakana."

    w "You know it’s prohibited for students to have part-time jobs, correct?"
    s "Are you telling me none of your students have jobs?"
    w "Not anymore. You took the three that did."
    s "You don’t plan on doing anything about it, though, right?"

    if bonus == True:
        w "What would I even do? Get them all fired and force them to sell their bodies to put themselves through college?"
    else:
        w "What would I even do? I don't have the energy to get involved in this."

    w "Or are they so far behind in their education thanks to your genius teaching strategies that college isn’t an option in the first place?"
    os "Wow. You two are a lot closer than I thought."

    scene barwakaosako20
    with dissolve

    w "We’re very good friends."

    "We are?"

    s "Our relationship aside, how do you two know each other?"

    scene barwakaosako19
    with dissolve

    os "Figured you’d know since you guys are so close."
    os "Wakana and I live together."
    os "Have for a few years now."
    w "We met in college."
    w "I would die for her if the need arose."
    s "You would die for anyone or anything at this point."
    w "Not you, you fucking buffoon. "

    scene barwakaosako21
    with dissolve

    os "Hahaha! I haven’t seen her get along this well with somebody in years. "
    os "I’m actually kind of impressed."

    "{i}This{/i} is getting along with Wakana?..."

    scene black
    with dissolve

    "Sana comes back moments later and bashfully places an entire six pack on the table, telling Osako and Wakana they can just help themselves and let her know if they need anything else."
    "I decide to leave the two of them alone and retreat back to the counter with Sana to recap the {i}incredibly purposeful{/i} experiment we just had."

    scene barwakaosako22
    with dissolve

    s "You didn’t cry when I said “spaghetti.” Great job, Sana."
    sa "I’d...appreciate it if you’d stop bringing that up all the time..."
    s "It’s one of my fondest memories of you."
    sa "Why is me getting so flustered that I started crying a...good memory for you?"
    s "To be fair, I don’t have much to work with. Our relationship has been limited to pretty much the bar and your room."
    sa "And[school], but..."

    scene barwakaosako23
    with dissolve

    sa "Y-Yeah...I’m not really like Ayane and...the two of us don’t have the kind of relationship that is able to make memories like that..."
    s "Are you being jealous again now, Sana?"
    sa "I..."
    sa "…"

    "Instead of refuting that immediately like I expect her to, Sana hesitates."
    "She plays with the knot of her tie, undoing it slightly with her fingers and drawing attention to how slender her neck is."
    "If that outfit really did belong to her brother (Which I’m sure it did because why would she lie?), he must have been very small as well."
    "I guess being short is just...a Sakakibara gene or something."

    sa "I..."
    sa "I’d like...to try karate too, Sensei..."
    s "…"
    s "{i}You’re so adorable.{/i}"

    scene barwakaosako24
    with dissolve

    sa "Again?! Why are you so quiet today?!"
    s "Why not ask Ayane if you want to get into karate? She’s been going there longer than I have. "
    s "You said that you knew she did it, so why wait until now to come out and talk about wanting to try?"

    "Obviously, the answer is because now she knows I’m involved and she’s worried about things progressing any further with Ayane and me."
    "But {i}also{/i} obviously, there’s no way I’d actually come out and tell her I know that."
    "It’s my job to feign density for the sake of her comfort."
    "And not just hers, but the comfort of everyone around her as well."
    "Sana still needs to come out of her shell, and for that-"

    scene barwakaosako23
    with dissolve

    sa "Because I want to...do it with you..."

    "And there it is."
    "I’m surprised she put it so bluntly, though."

    scene barwakaosako25
    with dissolve

    sa "Ah! W-w-w-w-wait! By “do it” I meant karate! Not the other thing!"
    s "I’m aware that you meant karate, Sana."
    sa "You are?!"
    s "Of course."
    sa "So...so now me freaking out makes it seem like I w-w-was thinking about the other thing?!"
    s "A little bit, yes."
    s "You should calm down before your other customers in the back of the room take notice."
    sa "N-n-n-n-notice what?! That I want to do karate?!"
    sa "I love karate! Please teach me karate, Sensei!"
    os "Hm? You guys talkin’ about karate over there?"

    scene barwakaosako26
    with dissolve

    sa "Oh! Uhh...look at the time!"
    sa "I’ve gotta go...take care of something in the back!"
    sa "Uhhhhhh bye!"

    scene black
    with dissolve2

    "Sana runs away and trips over a rubber mat in front of the door to the back room, banging her head before letting out a high pitched shriek and tumbling inside."
    "I think about getting up to help her but realize that she’d likely rather be alone right now- at least until she’s able to calm herself down."
    "And, of course, that happens several minutes later."
    "She returns to the bar and everything goes back to normal."
    "With her being shy and me being me."
    "But progress was made today."
    "If Sana is ever going to get anywhere, she needs to start being honest with herself...and start being honest {i}to{/i} others."
    "And I don’t mean just me."
    "I mean to Ayane and Sara as well."
    "If she’s so bothered by their incessant need to bring me up in conversation, the least she can do is find a way to “contribute” as well."
    "That won’t ever happen if she doesn’t change."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar35 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar40:
...
```

## Code that triggers this event
File: \game\SanaEvents.rpy
Code:
```python
...
label sanasbar:
    if sana_love >= 0 and firsttimebar == False:
        jump firsttimebar
    if sana_love >= 5 and bar5 == False:
        jump bar5
    if sana_love >= 10 and sanafirsthall == True and bar10 == False:
        jump bar10
    if sana_love >= 15 and bar10 == True and bar15 == False:
        jump bar15
    if sana_love >= 20 and day65 == True and bar15 == True and amisroom5 == True and bar20 == False:
        jump bar20
    if sana_love >= 25 and sanadorm20 == True and makidate1 == True and bar25 == False:
        jump bar25
    if sana_love >= 30 and sanadorm25 == True and day120 == True and bar30 == False:
        jump bar30
    if sana_love >= 35 and utamaid5 == True and christmas7 == True and bar35 == False:
        jump bar35
...
```