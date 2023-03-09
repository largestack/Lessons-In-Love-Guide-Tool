# Good Morning
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach1&go=Go)



## Event preconditions
✅Day of week is Saturday

✅Days since the start of the game greater than or equal to 370

✅Event "[Main: Permission Slip](./day355.md)" is completed (event=day355)

✅Event "[Karin: Sweet Tooth](./karindate20.md)" is completed (event=karindate20)

✅Event "[Chinami: Happy Hour](./chinamidate20.md)" is completed (event=chinamidate20)

✅Event "[Uta: Blood Everywhere](./utadorm20.md)" is completed (event=utadorm20)

✅Event "[Sana: Mine](./sanadorm50.md)" is completed (event=sanadorm50)

✅Event "[Osako: Floating Forever, Unfulfilled](./osakodojo1.md)" is completed (event=osakodojo1)

✅Event "[Kirin: All That is Contaminated](./kirindate25.md)" is completed (event=kirindate25)



## Next events
None

## Event properties
* ID: secondbeach1
* Group: Main
* Triggered by label: saturdaymorning
* Triggered by branch label: saturdaymorning

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label secondbeach1:
    scene black
    with dissolve

    "{i}Some people will tell you that there are only two guarantees in life-{/i}"
    "{i}Death and taxes, I think they say.{/i}"
    "{i}But the truth is that there is a third guarantee.{/i}"
    "{i}Though, it’s one that’s a bit too artistic or pretentious to lump in with the others.{/i}"
    "{i}But I am an artistic and pretentious person, so I am going to do it anyway. {/i}"
    "{i}The third guarantee is that there is beauty in everything around you.{/i}"
    "{i}It sticks to your clothing like cigarette smoke.{/i}"
    "{i}Clings to your skin like the nails of a house cat.{/i}"
    "{i}But despite all that, it can still be a little hard to see sometimes.{/i}"
    "{i}But it’s there.{/i}"
    "{i}I promise.{/i}"
    "{i}- No one{/i}"

    scene goodmorning1blur
    with dissolve2
    play music "goodmorning.mp3"

    "My eyelids wage war with an incessant desire to sleep in and, just seconds after waking up, I can already tell that it’s going to be another day of losing battles or losing patience."
    "Or losing anything, really. "
    "Sense of self?"
    "Sleep?"
    "I don’t know."
    "But something will be lost."
    "I fight back against the desire to keep my eyes closed and attempt to figure out who the figure is before me."
    "They haven’t crawled into my bed yet, so based on that assumption, it could probably only be one person."

    s "Maya?..."

    scene goodmorning1
    with dissolve2

    m "Good morning."
    s "Good morning."
    m "…"
    s "…"

    "I decide not to say anything about how strange this is- not just because it’s too early for the banter to begin, but because I’m sure that the two of us are already acutely aware of it."
    "And yet we remain in silence for a minute or two. "
    "It doesn’t feel longer or anything like that."
    "It genuinely feels like a minute or two."
    "But then the silence becomes uncomfortable and I find myself losing my first battle out of many to come."

    if bonus == True:
        s "No good morning kiss?"
    else:
        s "Did you come to see how the huggy boy is doing?"

    m "Oh, look. Just two sentences in and I’m already regretting my decision to come here."
    s "Sorry. Just a little confused as to why you decided to be my wake up call today."
    m "Hm. "
    m "I’m going to go out on a limb here and assume that no one told you what today is."
    s "You’d be very correct in assuming that."

    scene goodmorning2
    with dissolve

    m "Well, I’m sure you’ll be able to figure it out the second you step into Ami’s room."

    if bonus == True:
        m "Fortunately for me, I won’t be there to be ogled at half-naked this time around. Hooray."
    else:
        m "Fortunately for me, I won’t be there to be ogled at half- wait. No. That didn't happen in this timeline."

    "I lose a second battle."

    s "The beach trip isn’t today, is it?"

    scene goodmorning1
    with dissolve

    m "It is. And at the risk of sounding excited, I’d like to inform you that I am very much not excited."
    s "I’m not really sure you needed the disclaimer if you were just going to come out and say it like that."
    m "As {i}glad{/i} as I am to have {i}you{/i} back in {i}your own{/i} body, it is once again making things very difficult for me."
    s "Apologies. Any reason for the strange amount of emphasis on words in that last sentence, though?"
    m "Dodging memory lapses, perhaps. "

    if bonus == True:
        m "It would be rather inconvenient if I caused you to black out and subsequently felt pressured to fuck you back to life again with all of my friends in the next room over."
    else:
        m "It would be rather inconvenient if I caused you to black out and subsequently felt pressured to hug you back to life again with all of my friends in the next room over."

    s "Oh, come on. That’s like the one thing I’ve been able to successfully tease you about. Please don’t take that away from me."

    scene goodmorning3
    with dissolve

    m "Alas. It appears that all good things must come to an end."

    "Another minute of silence."
    "Then another."
    "Then I lose again."

    s "So...you were really the one they sent over to wake me up this time?"
    s "Ami normally jumps at the opportunity to be the first thing I see in the morning."

    scene goodmorning4
    with dissolve

    m "No one sent me anywhere. It just looks like we’re going to be leaving early today."
    m "And since I wasn’t able to eat breakfast on the way over, I’m taking a walk to the convenience store and am being kind enough to see if there is anything you want."
    s "Are you...actually doing something nice for me?"

    scene goodmorning5
    with dissolve

    m "Nice? Of course not. "
    m "It would just wind up saving all of us time in the long run if I could get everything done in one trip."
    s "…"
    m "What?"
    s "It’s just a little funny to hear you of all people talking about saving time when-"
    m "Yes, I get it. Haha. Funny joke."
    m "Do you want anything or not?"

    if bonus == True:
        s "I’m still waiting on that good morning kiss."
    else:
        s "Uhhhhhh yeah. Let me get two number 9's, a number 9 large, a number 6 with extra dip, a number 7, two number 45's, one with cheese, and a large soda."

    scene goodmorning6
    with dissolve

    m "I’m going to go ahead and take that as a no. "
    m "Congratulations on missing out on a chance for a free convenience store breakfast."

    "Another loss, but I earn a victory in the form of not being called disgusting, so it cancels out."

    m "Well, that was all I came here to ask, so-"
    s "Wait. Hold on a second."

    if bonus == True:
        m "How many times must I decline your less-than-subtle advances before you realize that I’m not going to kiss you?"
    else:
        m "What? I already told you I'm not getting you anything."

    s "No, I get that part."
    s "You just look a little different today."

    scene goodmorning7
    with dissolve

    m "Different?"
    m "You mean because I’m not wearing my hair down?"
    s "Yeah, that. And there’s no scarf either. "
    s "What happened to all of that stuff about how you don’t like your neck getting cold?"
    m "I am...surprised you remember that detail of all things. "

    scene goodmorning8
    with dissolve

    m "And while that may be an issue I’ll have to confront in the near future, I’d like to take this opportunity to remind you that everything from this point on is basically brand new to me."
    m "My inability to predict how things will play out from this point has tossed me into quite a bit of a predicament."
    m "And so I’m attempting to circumvent my apparent lack of understanding of this city’s weather patterns by dressing in winter clothes while donning my summer haircut."
    s "Winter clothes minus the scarf, you mean."

    scene goodmorning9
    with dissolve

    m "That..."
    s "…"
    m "…"
    m "I just didn’t want to risk losing it."
    s "…"
    m "Anyway, bye. "
    m "Don’t tell the others I came in here."

    scene goodmorning10
    with dissolve

    "Maya leaves the room without looking back and I’m left to lie there in silence for another few minutes as I fight yet another battle of whether or not I’m going to get out of bed yet."

    scene black
    with dissolve2

    "I lose again."

    "{i}Welcome to the second special Lessons in Love beach update!{/i}"

    if bonus == True:
        "{i}Please enjoy the next twenty-one events (Or slightly less if you are bad at sex) and remember to savor every moment to your heart’s content!{/i}"

    "{i}Just like last time, it’s sure to be filled with plenty of special memories and fun activities that’ll have you wishing to never go home!{/i}"
    "{i}Unfortunately, even the sanctuaries that stitch themselves to the thick silhouettes of escape mechanisms tend to lose their grip from time to time.{/i}"
    "{i}Will you lose your grip?{/i}"
    "{i}Or will you hold onto these precious days like the hand of a dying loved one?{/i}"
    "{i}Smile always!{/i}"
    "{i}If you don’t, you lose!{/i}"
    "{i}And life is just a game after all, isn’t it?{/i}"
    "{i}And all of this is fake, isn’t it?{/i}"
    "{i}But it’s all still beautiful, isn’t it?{/i}"
    "…"
    "{i}Why does everything have to hurt so much?{/i}"

    scene goodmorning11
    with dissolve2

    s "Good morning, everyone."
    a "Sensei! You’re up early! I was just about to come and get you."
    sa "Um...g...good morning..."
    ay "Are you ready, Sensei?!"
    ay "Ready to brave the harsh winter winds and get lost in a weekend of fun in the sun even when the sun probably won’t be there?!"
    s "Nope."
    s "I’m glad to see you’re feeling better, though."

    scene goodmorning12
    with dissolve

    ay "Uhh...thank you..."
    ay "Sorry for skipping[school] the last few days and stuff. Just been a little under the weather."
    ay "I’m starting to feel better now, though. So...you don’t really have to worry about me."
    a "I still have no idea what happened, but I’m glad to have you back, Ayane."
    a "There's no denying that you are loud and obnoxious and like my [uncle] way too much, but things around here just aren’t the same without you."

    scene goodmorning13
    with dissolve

    ay "I don’t just {i}like{/i} Sensei, Ami! I love him!"
    ay "I love him and I don’t care who knows!"
    a "Nevermind. You can go back to being sick now. I forgot how loud and obnoxious you actually were."
    ay "Nonsense, Ami! We can love him together!"
    a "I like loving him by myself more, thanks."
    s "Sana, would you like to join in and proclaim your love for me as well?"
    sa "Um...no thank you..."
    sa "But...I would like to know how exactly...a winter beach trip is going to work..."
    sa "Like...the weather didn’t seem like it was going to be...suddenly hot or anything, so..."
    sa "Um...why are we even wearing our swimsuits?"

    scene goodmorning14
    with dissolve

    ay "We’re wearing them {i}now{/i} because we have no idea if we’ll be able to once we get to the beach, Sana!"
    ay "And just because the weather might be cold doesn’t mean we need to abandon our...beach spirit!"
    sa "Beach...spirit?"
    ay "The...spirit of the beach!"
    ay "You know what I’m talking about...right, Ami?"
    a "I have no clue what she’s talking about. I just wanted Sensei to see me in my new swimsuit and tell me how cute I am, but he hasn’t said anything yet."

    scene goodmorning15
    with dissolve

    s "All three of you are looking as cute as ever."

    if bonus == True:
        s "Now, turn around and let me judge the backs of your swimsuits as well."

        "Uta, Miku, and Futaba didn’t fall for it...but maybe these three will."

        ay "Okay! Let’s do it, girls!"
    else:
        s "I imagine you'll all make some man who is definitely not me very happy one day."

    scene goodmorning16
    with dissolve

    if bonus == True:
        a "Better idea! How about you two leave and Sensei just gets a better look at the back of {i}my{/i} swimsuit?"
        a "I’ve already seen the backs of your swimsuits and can just clue him in on the details while he is helping me retie the drawstring on my bikini."
        ay "But I thought you said you tied it really tight since it’s still a little big for you and that you didn’t want it coming undone in the water."
        a "{i}...Yes, Ayane.{/i} But maybe it’s still not tight enough and I need his help to fix it?"
    else:
        a "Better idea! How about somebody helps me reattach my prosthetic limbs since I didn't put them on correctly this morning?"

    ay "You know, I wouldn’t mind helping you if-"

    scene goodmorning17
    with hpunch

    a "DAMN IT, AYANE! TAKE A HINT AND GET LOST ALREADY!"

    if bonus == True:
        ay "Teehee~"
    else:
        ay "Sometimes, I'm happy you're not fully human."

    s "Thank you for not making this morning any more exhausting for me, Sana. "
    s "I hereby crown you the winner of this year’s Arakawa House Swimsuit Competition."
    sa "Um...that’s nice and everything, but...I..."
    sa "I think I’m going to...put my normal clothes back on now..."

    if bonus == True:
        s "By all means, don’t let me get in the way."
        sa "You..."
        sa "You’re in the way by being here..."
    else:
        s "Okay. See you later, Sana. Have a nice day."

    play sound "doorbell.mp3"
    scene goodmorning18
    with dissolve

    "The doorbell suddenly goes off and officially concludes the ending to the AHSC, a new competition I just made up and will absolutely remember if I’m fortunate enough to go on a third beach trip."

    sa "Did...Maya lock herself out?"
    a "No, Maya knows where the spare key is. I think that’s Karin."
    s "Oh, right. I forgot she was going to tag along with you guys since her sister is a demon."

    if ayanelust10 == True:
        ay "Demon is a bit of an understatement, don’t you think?"

    a "I’ll go let her in. Everybody, stay at least ten feet away from Sensei while I'm gone and-"
    s "Actually, Ami- I'll let her in."

    scene goodmorning19
    with dissolve

    a "But Karin specifically asked me to let her in instead of you because you’re a boy and she’ll have a panic attack or something."

    if bonus == True:
        a "She was also under the impression you’d be in nothing but your boxers for some reason."
        s "Which I am not. So it should be fine if it’s me then, right?"
    else:
        a "She was also under the impression we lived in a tent for some reason."
        s "But we don't. So it's okay for me to let her in, right?"

    a "I mean...I’d still rather-"
    s "Great. I’ll go let her in then."

    scene black
    with dissolve
    play sound "dooropen.mp3"

    a "Wait, Sensei! She really will have a panic attack!"

    "I exit Ami’s room and make my way over to the front door to let Karin in."
    "I also figure that if she {i}does{/i} wind up having a panic attack that she’s in the right place to do so since the couch isn’t that far away and I could just toss her onto it or something."
    "Also, I’m not sure if first aid would be required for something like that, but Ayane is Ayane and she’d probably know some way to handle it."

    play sound "dooropen.mp3"

    "………"
    "……"
    "…"

    scene goodmorning20
    with dissolve

    ka "H-H-H-H-H-H-H-H-H-House!"
    s "Hi, Karin."

    scene goodmorning21
    with dissolve

    ka "R...Right..."
    ka "Hi is...the word I was looking for..."

    scene goodmorning22
    with dissolve

    ka "U...Umm...could you show me which room is Ami’s?"
    ka "She said she...had something to show me and..."
    ka "And she...probably knows where it is...maybe..."
    s "Ami and the others left already. "
    s "I figured you and I could just hang out here for the rest of the day and then go to the beach ourselves."

    scene goodmorning23
    with dissolve

    ka "T...Together?!"
    ka "Here?!"
    ka "Ourselves?!"
    ka "Beach?!"
    s "Is that a problem?"
    ka "I..."
    ka "Ah..."
    ka "Uhh..."
    s "…"
    ka "…"
    s "…"

    play sound "thump.mp3"
    scene goodmorning24
    with hpunch

    "Karin dies."

    s "Do you need help? Or can you-"
    ka "I...I can stand! I’m okay!"

    scene goodmorning25
    with dissolve

    ka "Ha ha! Legs! Am I right?!"
    s "I...don’t know?"
    s "I was just kidding about Ami not being here, though. Round the corner and her room is the first one on your left."

    scene goodmorning26
    with dissolve

    ka "Ha...hahah...that was a...really funny prank you just pulled on me, Sensei..."
    ka "It definitely wasn’t...really scary and...I’m definitely not a little...upset or anything that it’s not true..."
    ka "Definitely not. Not at all."
    s "You’re so good at hiding how you really feel, Karin."

    scene goodmorning27
    with dissolve

    ka "I should have just taken the bus..."

    play sound "dooropen.mp3"
    scene goodmorning28
    with dissolve

    m "I’m back."
    m "Everyone decided they didn’t want anything, so I just bought this since I am already historically bad at carrying things and-"

    scene goodmorning29
    with dissolve

    m "And..."
    s "…"
    ka "…"
    m "…"
    ka "Um...h...hi, Maya..."

    scene goodmorning30
    with dissolve

    m "Stay back! I paid money for this!"
    ka "I’m...not going to attack the melon this time..."
    m "No! You’re not! Because I’m going to hide it!"
    ka "I..."
    m "My melon!"
    ka "…"
    m "Don’t follow me!"

    scene goodmorning31
    with dissolve

    ka "…"
    s "…"

    scene goodmorning32
    with dissolve

    ka "…"
    s "She really likes watermelons for whatever reason."
    s "I'm sure it's somehow relevant."
    ka "I...see that..."

    scene goodmorning33
    with dissolve

    m "{i}Ahem...{/i}"
    m "So, the beach."

    "Karin gently places her bag down by her feet and the three of us proceed to forget about the entire melon ordeal that nearly just turned this house into a crime scene."

    ka "Y-Yeah! Thanks for letting me tag along with you guys..."
    ka "Kirin was still being kind of mean this morning and...she didn’t really like it when I told her I was coming."
    s "You actually told her?"

    scene goodmorning34
    with dissolve

    ka "I figured it would be a little better than just...surprising her and causing a scene."
    ka "Though...she’s already told me that if I {i}do{/i} come that she’s going to make a scene anyway, so...I have to meet up with her as soon as I get there."
    s "Or, alternatively, you could avoid her altogether and let her self-destructive tendencies manifest in a way that won’t cause damage to you."
    m "Agreed. Confrontation is conceptually exhausting and should be avoided in nearly all cases where only one party is feeling emotionally vulnerable."
    s "Does this mean you’re going to finally apologize to Noriko for exploding on her in the middle of class?"

    scene goodmorning35
    with dissolve

    m "Nope."
    m "In fact, I’d laugh myself into a coma if I were to witness her being eaten by a shark this weekend."
    s "No, you wouldn’t. Not because I think you secretly like her, but because I’m starting to doubt that you even know how to laugh."
    m "Don’t you think you should maybe just take into account the fact that you are not funny?"
    s "Me? I’m hilarious."
    m "That statement alone is the closest you’ve come to a joke in literal centuries."
    ka "I...I know Sensei is older, but...I think centuries seems like a little much..."

    scene goodmorning36
    with dissolve

    a "Hey! Sorry I didn’t answer the door for you. I tried, but Sensei told me that he was going to do it instead and his word is law."
    s "What? Since when?"

    scene goodmorning37
    with dissolve

    a "Always, obviously! "
    a "I’d kill for you if you asked me to, Sensei."
    ka "Aww. I knew you guys were close but I didn’t think it was {i}this{/i} close."
    m "Yes. Adorable."
    m "But as much as I’d love to stay and talk about Ami’s unhealthy obsession with Sensei and how {i}incredibly normal{/i} it is, I have a melon to eat."

    scene goodmorning38
    with dissolve

    a "Can’t you just eat it here if it's that big of a deal?"
    m "Here? Instead of on the beach? Are you insane?"
    m "Everyone knows that the beach is the best place to enjoy a watermelon. I don’t mind waiting at all if that’s a feasible option."
    m "I just don’t want to wait {i}too much{/i} because, well...melon."

    scene goodmorning39
    with dissolve

    a "Well...all of us girls are ready to go whenever. "
    a "I think we’re just waiting on Sensei to pack his things before heading over to the bus stop."
    ka "I’m...also ready whenever you want to leave. I wouldn’t want to be a burden by messing up your plans, so...my schedule is entirely up to you guys."
    m "Melon."
    s "Yes, Maya. Melon."
    m "Melon now."
    s "…"
    s "Melon now."

    scene wintersky
    with dissolve2

    "I wind up packing up my things rather quickly given that we’re only going to be gone for two days and that I...barely have anything to bring either way. "
    "Then, before long, the six of us make our way over to the bus stop, each carrying our own possessions apart from Karin- who is repenting for the watermelon tragedy by carrying Maya’s bag."
    "She offered to carry the melon itself, but...well, you can probably imagine how that went."
    "A few minutes go by with us waiting at the bus stop and gazing up at the sky, trying to figure out whether or not the snow will end by the time we get to the beach."
    "Or if it’s even snowing there to begin with."
    "It would be easy to check the weather and find out within a matter of seconds, but it’s not like any of us really trust weather forecasts in the first place."
    "Besides, life is better with an added layer of mystery thrown into the mix."
    "Life is better with an added layer of basically anything thrown into the mix, though."
    "But that’s mostly because it just sucks on its own and requires a multitude of spices to be even somewhat palatable."

    scene black
    with dissolve2

    "The bus arrives just as the snowfall ends and we all pack our things into overhead storage receptacles- melon included."
    "Ami and I sit together as everyone else finds a different place on the bus."
    "She falls asleep on my shoulder on the way and I can make out the faint smell of her shampoo."
    "It’s different than normal."
    "And slightly nostalgic."
    "………"
    "……"
    "…"

    play sound "phonebeep.wav"

    s "Hm?"

    "I get a text message just as I’m about to close my eyes as well and look down at my phone to see who it is."
    "Chances are it’s just Ayane on the other side of the bus, checking in to see what I’m-"

    ni "{i}Hey.{/i}"
    s "…"
    s "{i}Hey.{/i}"
    "…"

    play sound "phonebeep.wav"

    ni "{i}Are you busy this weekend?{/i}"
    s "{i}Are you actually trying to make plans with me?{/i}"

    play sound "phonebeep.wav"

    ni "{i}Are you busy or not? I don’t have all day to be texting, you know.{/i}"

    play sound "phonebeep.wav"

    ni "{i}In case you don’t remember, I’m very, very famous.{/i}"
    s "{i}Sorry, but I have plans.{/i}"
    s "{i}We can do something when I get back, though.{/i}"

    play sound "phonebeep.wav"

    ni "{i}Okay.{/i}"

    play sound "phonebeep.wav"

    ni "{i}Bye then I guess.{/i}"

    stop music fadeout 15.0

    "My phone finds its way through a maze of even more nostalgia (There’s quite a bit of it on this bus) and makes its way back into my pocket."
    "I gaze out of the window, letting the scent of Ami’s hair invade my nostrils, and find the skeleton of a fully decomposed animal."
    "One I recall seeing sometime before."
    "I think of how it died."
    "And ultimately follow that train of thought up to the point where it becomes far too dangerous to follow anymore."
    "I jump off board and chase after it, though."
    "Hoping that wherever it’s heading is somewhere I’ll be able to see some day."
    "But then I lose again."

    $ renpy.end_replay()
    $ maya_love += 1
    $ secondbeach1 = True

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    jump secondbeach2

label secondbeach2:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
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
...
```