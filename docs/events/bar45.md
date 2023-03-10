# Sweet Vermouth (Sana)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Sana love greater than or equal to 45

* Event [Sayonara](./thirdreset3.md) (Main) is completed)

* Event [Hall of Mirrors](./futabadorm45.md) (Futaba) is completed)



## Next events

* [Sana: Mine](./sanadorm50.md)

## Event properties

* Id: bar45
* Group: Sana
* Triggered by label: sanasbar
* Triggered by branch label: sanasbar
* Triggered by path: sanasbar->bar45

## Official wiki page

[Sweet Vermouth](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=bar45&go=Go) for more details.

## Event code

File: (install folder)\game\SanaEvents.rpy

Code:
```python
...
label bar45:
    scene sanayukitrain1
    with dissolve
    play music "calmbar.mp3"

    "I decide to spend the night hanging out at the bar with Sana."

    sa "You...didn’t really pick the best night to...hang out here..."

    scene black
    with dissolve

    "I go home because Sana hates me."

    scene sanayukitrain1
    with dissolve

    s "Sana, I don’t really think you should be picking and choosing your customers when your mother’s store is about to go under."
    sa "I...don’t really have much to pick and choose from either way..."
    sa "I just meant that...I might be a little busier than normal tonight..."
    s "Oh? Did someone accidentally book a birthday party here thinking it was some other bar?"

    scene sanayukitrain2
    with dissolve

    sa "Um...no..."
    sa "It’s just that...our new employee is here tonight and...I have to show her how to make drinks..."
    s "How many customers do you actually have to make drinks for? "
    s "Because the friendly neighborhood lesbian couple and myself are the only people who seem to come here and all three of us just get beer."
    sa "Well...we don’t really...ever make them, but...it’s an important thing for a bartender to know..."
    s "Well, good luck. I can’t imagine your new employee is very easy to train."
    yu "Hey. You talkin’ shit over there?"

    scene sanayukitrain3
    with fade

    s "Please don’t hit me."
    yu "You think I’d actually hit you while I'm workin’?"
    s "No. But I’m afraid you’d follow me home and beat me up on the way there."

    scene sanayukitrain4
    with dissolve

    yu "Hah...not worth the effort..."
    yu "Just havin’ a job is tiring enough. "
    sa "Yuki...you’ve only been working for...half an hour..."
    yu "Jesus, is that all? I feel like I’ve been here all night."
    yu "No wonder Yumi started her own business. "
    s "Again, she..."
    s "Ah, fuck it. Sure. "

    "I resign myself to the concept of Yumi Yamaguchi being a successful entrepreneur and allow Yuki to believe whatever it is her shriveled heart desires."

    scene sanayukitrain5
    with fade

    yu "So, now what? What’s step two in becoming a successful barmaid or whatever?"
    sa "Um...well...you can start by...taking Sensei’s order..."

    scene sanayukitrain6
    with dissolve

    yu "Cool. What do you want?"
    sa "Sensei...for the sake of...Yuki’s training...can you order something different from what you usually order?..."
    s "Uhhhh..."
    s "I’ll take...a Manhattan?"
    yu "A Manhattan? Are you a fucking prissy boy?"
    yu "There’s a perfectly good beer in front of you. Drink that."

    scene sanayukitrain7
    with dissolve

    sa "Y...Yuki! You can’t...talk to customers that way!"
    yu "Really?"
    yu "But I thought your mom said to play up my “rough exterior” or whatever it is she thought would bring new people in."
    sa "It’s okay to be mean to Sensei normally-"
    s "Wait, it is?"
    sa "But for right now...you have to look at Sensei like...not Sensei...and...and treat him like a normal person..."

    scene sanayukitrain8
    with dissolve

    yu "You want me to treat {i}this guy{/i} like a normal customer? Dude’s far from normal if he’s comin’ here to chat with a four foot tall [teenager]."
    s "I take great offense to this entire exchange. I just want to drink."
    s "Where is Sara? I need to speak to the owner."
    sa "She’s...in the urban district, passing out fliers right now..."

    scene sanayukitrain9
    with dissolve

    sa "Also...I’m...almost five feet tall..."
    yu "Same shit. "
    yu "But if we’ve gotta do this the normal way...what are you drinking, bud?"
    s "Bud?"
    yu "What're you ordering, pal?"
    s "Why do I need a weird nickname?"
    yu "What’re you havin’, champ?"
    s "How about “master” or “my prince?”"
    yu "How about you suck my fucking dick and order your stupid ass Manhattan already?"

    scene sanayukitrain10
    with dissolve

    s "Well, when you put it that way- one Manhattan, please."
    sa "Hah...this is...proving to be even harder than I thought it would be..."
    yu "Comin’ right up."

    scene sanayukitrain11
    with dissolve

    yu "So, now what?"
    yu "You’re the genius bartender girl and I don’t have any idea what the fuck goes into a Manhattan."
    sa "Well...the ingredients for a Manhattan are...bourbon...orange and Angostura bitters...and...um...sweet vermouth..."
    s "I love sweet vermouth."
    sa "And...it’s...garnished with a brandied cherry on top..."

    scene sanayukitrain12
    with dissolve

    sa "So...um...you’ll want to add the bourbon, vermouth and bitters to a mixing glass with ice and...stir it until it’s chilled..."
    sa "Then you just...strain it into a glass and...add the garnish..."
    sa "And then it’s done..."
    yu "Got it. Now, where can I find all that stuff?"
    sa "We...um..."
    sa "We...don’t have any in stock right now..."
    yu "…"
    sa "…"
    yu "Your mom's gonna need a lot of fuckin' fliers."

    scene black
    with dissolve2

    "Sana goes over the ingredients to a bunch of popular cocktails that the bar is currently incapable of making and I imagine that Yuki forgets all of them instantaneously."
    "I’m a little surprised to see that Sana has everything memorized, though. Especially when no one ever orders anything like that here."
    "But I guess things haven’t always been like that at the bar."
    "If I’m remembering correctly, the place has been in Sana and Sara’s family for a while now and was actually relatively popular before the space war."
    "It kind of sucks that everything went downhill after that, but...maybe there really {i}is{/i} a chance for them to turn things around?"
    "Though...I imagine that will be pretty hard without actual ingredients."
    "Anyway, Sana winds up sending Yuki home after another hour of training and pulls a few bills out of their register to pay her for the night."

    if bonus == True:
        "I notice that it’s nowhere near the amount that she’s likely owed, but...I don’t think Yuki’s really in the position to ask for more with zero work experience in her late thirties."
    else:
        "I notice that it’s nowhere near the amount that she’s likely owed, but...I don’t think Yuki’s really in the position to ask for more with zero work experience."

    "I also doubt that she’s even familiar with what minimum wage is."
    "But regardless, she accepts the money and exits the bar...leaving Sana and I alone once again."
    "………"
    "……"
    "…"

    scene sanayukitrain13
    with dissolve2

    sa "I...um...I’m sorry you...couldn’t get the Manhattan you ordered..."
    s "I never would have ordered that if I wasn’t asked to order something...fancier."
    s "Frankly, I didn’t even remember what a Manhattan was. It’s just the first cocktail that came to mind."
    s "Also, you should probably restock the bar some day."

    scene sanayukitrain14
    with dissolve

    sa "I agree...and...so does my mom..."
    sa "There just...hasn’t really been any reason to with our current...clientele."
    s "Is Sara really passing out fliers in the urban district right now? "

    scene sanayukitrain15
    with dissolve

    sa "Mhm. It’s the first time in a while that I’ve seen her go out of her way to try and bring people in."
    sa "So...I’m doing my part and training our new employee while she’s out doing that."
    s "Speaking of which, you handled Yuki surprisingly well."
    s "I figured that she was the exact type of person who’d cause you to cower in fear by simply looking at her."

    scene sanayukitrain16
    with dissolve

    sa "If she was in her normal clothes...I probably would have been a lot more scared..."
    sa "It was just a little easier since...we were dressed in pretty much the same outfit..."
    sa "And...I think it’s also because...I might...kind of be getting used to people now..."
    s "Well you’ve certainly increased your friend count by a sizable margin."

    scene sanayukitrain17
    with dissolve

    sa "Heheh...yeah..."
    sa "I was...even able to sleep over your house without Ayane recently..."
    s "Yeah. I was kind of surprised about that-"

    "Wait..."
    "I thought the last reset made it so that sleepover never happened?"
    "At least that’s what Ayane said and...Sana {i}was{/i} at the dorm when I got back from the rooftop."

    s "…"
    sa "…"

    scene sanayukitrain18
    with dissolve

    sa "Um...Sensei?..."
    sa "Is...there a reason you’re just...staring at me?"
    s "When did you sleep over my house without Ayane?"

    scene sanayukitrain19
    with dissolve

    sa "Um...it was...recently, wasn’t it?"
    s "For me, yes. But Ayane was under the impression that it never even happened."
    sa "That’s...weird. I could have sworn I talked to her about it..."
    sa "And I...still remember the dinner that...Tsuneyo made for us..."
    sa "But...um..."
    sa "There’s...something else I kind of wanted to say as long as we’re done talking about that..."
    s "…"
    sa "…"
    sa "Is that...okay?"

    scene sanayukitrain20
    with dissolve

    s "Yeah."
    s "Sorry for getting distracted. Time is just kind of weird sometimes."
    sa "Yeah..."
    sa "It’s crazy how...quickly it can go by when you stop paying attention..."
    sa "But...the time we’ve spent together...if anything...has seemed kind of slow for me..."
    sa "Which is weird because...it also feels like so much has happened..."
    sa "And if it weren’t for you, I...probably wouldn’t be able to do stuff like...train really intimidating employees or...sleep places I’ve never slept before."
    s "Congratulations on the character growth."
    sa "Hehe...that’s a good way of putting it..."
    sa "My mom...didn’t put any of my stat points into speech, so...I’ve been kind of...soft locked progression-wise for a little while."
    sa "But...now I’ve got...another party member who...can help me train in that field..."
    s "I think you’ve been spending a little too much time with Molly."

    scene sanayukitrain21
    with dissolve

    sa "Probably...but...spending time with other people isn’t really always a bad thing..."
    sa "I know that now."
    sa "Not that I...ever thought it {i}was{/i} bad. It just seemed kind of hard."
    s "Well, you still have the rest of the class to work up to befriending. And I want to warn you now that if you think getting closer to Yuki will help win over Yumi, it most certainly will not."

    scene sanayukitrain22
    with dissolve

    sa "Yeah...I already heard about that..."
    sa "Yumi is...not really near the top of my...potential friends list right now..."
    sa "She’s still...really scary..."
    sa "But..."
    sa "I don’t think it’s impossible anymore."
    sa "In fact...I’m starting to think that there isn’t really anything that’s impossible."
    sa "I don’t know how you did it, but...you kind of just walked into my life and opened up a bunch of doors that I...didn’t think I’d ever be able to open."
    s "Were the handles too high up?"

    scene sanayukitrain23
    with dissolve

    sa "Is everyone going to pick on my size tonight or something?"
    s "Hey. I, for one, appreciate how small you are."

    if bonus == True:
        s "I want you to stay this size forever."

    scene sanayukitrain24
    with dissolve

    if bonus == True:
        sa "You do?"
        sa "Why?"
        s "…"
        sa "…"
    else:
        sa "Is it because you are raising a horse that you require a jockey for?"
        s "..."
        sa "That's it, isn't it"

    scene sanayukitrain25
    with dissolve

    if bonus == True:
        s "No reason."
    else:
        s "Nope."

    sa "I...highly doubt that...but I’m going to...go ahead and assume you're just joking..."
    sa "I might be growing as a person, but...I also think I shouldn't really count on growing any more as a {i}person.{/i}"
    sa "My mom is...really small for her age, too...so I doubt I have many inches left."

    if bonus == True:
        s "Don’t worry. I’ll let you borrow several of mine as soon as you’re ready."
        sa "I...don’t really think that’s how height works..."

        "Even if Sana does wind up growing a little more, I hope her level of wholesomeness stays about the same."
        "I don’t want to think about a time where I can say things like that and have her immediately comprehend the unreal amount of ulterior motives I have."
    else:
        s "Don't give up, Sana. You will one day be a giant."
        sa "I hope so..."

    s "Anyway, I’m proud of you or whatever."

    scene sanayukitrain26
    with dissolve

    sa "Or whatever?..."
    s "Fine. I’m proud of you, okay?"
    s "I thought it would take a lot longer for you to stop acting like a scared little bunny rabbit- and that you’d wind up leaning on me a little more than you actually had to."
    sa "That’s funny, cause...all this time...I felt like I might have been leaning on you a little too much..."
    sa "Ayane, too."
    sa "Both of you believed in me when...I had trouble believing in myself..."

    scene sanayukitrain27
    with dissolve

    sa "And I...don’t want to agree that I’m a...bunny or anything..."
    sa "But I’d like it if...I could still maybe...lean on you a little bit once I start having to...do harder things..."
    sa "Like...ordering food over the phone or...making a withdrawal at the bank..."
    s "Just use an ATM. No one actually goes inside of banks anymore unless it’s something really important."

    scene sanayukitrain28
    with dissolve

    sa "It was just an example, Sensei."
    sa "What I mean is that...just because I’m doing a little better doesn’t mean I don’t still need you."
    s "Well, thanks. But, just to remind you, I’m a highly sought after individual and it might not always be as easy as this to get my attention."
    sa "Is that...the next phase of my training? Having to...force you to spend time with me so others can’t?"
    s "Maybe not the {i}next{/i} step, but it feels like that one is definitely on the way to whatever your final goal may be."
    sa "I need a final goal? I can’t just...enjoy my time with you and everyone else?"
    s "Sure you can."
    s "I just don’t think complacency is really as fulfilling as you’re making it sound."
    sa "But...isn’t that exactly how you live {i}your{/i} life, Sensei?"
    sa "I thought you just...wanted things to stay the way they are now..."
    sa "Or..."
    sa "Or do you maybe...have something you actually want?..."
    s "…"
    sa "…"

    scene black
    with dissolve2

    "The two of us sit there in silence for a little while longer as I attempt to think of all of the things I want."
    "Within a matter of moments, I find myself stranded on a desert island filled with blurry thoughts and the idea that there {i}are{/i} things that I want."
    "So many of them that I feel surrounded."
    "But they lurk in the shadows of large trees-"
    "And I can’t make out what they look like."
    "So I decide they aren’t there at all."
    "And I go to sleep in a shelter someone else built and abandoned."
    "I leave the bar."

    $ renpy.end_replay()
    $ sana_love += 1
    $ bar45 = True
    stop music fadeout 5.0

    "{i}Sana’s affection has increased to [sana_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label bar50:
...
```

## Code that triggers this event

File: (install folder)\game\SanaEvents.rpy

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
    if sana_love >= 40 and sanadorm35 == True and bar40 == False:
        jump bar40
    if sana_love >= 45 and thirdreset3 == True and futabadorm45 == True and bar45 == False:
        jump bar45
...
```