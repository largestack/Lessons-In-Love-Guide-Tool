# Stop Looking For Answers (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maya love greater than or equal to 30

* Event [A Place That Can Only Exist in Our Minds](./mayadorm35.md) (Maya) is completed)



## Next events

* [Ami: Best Friends Forever](./amiinvite3.md)
* [Ami: The Big Sleep](./amidate35.md)
* [Ami: Heaven for Human Blood](./amidorm40.md)

## Event properties

* Id: shrine35
* Group: Maya
* Triggered by label: shrine
* Triggered by branch label: shrine
* Triggered by path: shrine->shrine35

## Official wiki page

[Stop Looking For Answers](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=shrine35&go=Go) for more details.

## Event code

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label shrine35:
    scene black
    with dissolve
    stop music fadeout 5.0

    "………"
    "……"
    "…"

    scene nightsky
    with dissolve
    play music "undersea.mp3"

    "Night comes before I know it."
    "I feel like I decided to visit the shrine just a few minutes ago-"
    "But the sun was shining then. And this is certainly no sun I know."
    "I make my way down the streets of the city, staring up at the sky and hoping to catch a glimpse of a supernova."
    "The thing is, viewing a supernova from all the way down here wouldn’t be nearly as exciting as seeing it up close."
    "I know this for a fact."
    "Because I viewed a supernova just the other day."

    play sound "static.mp3"
    scene imissyou11 with flash
    scene nightsky with flash
    stop sound

    "What a beautiful explosion that was."
    "I wish I could remember more of it. "
    "I’m not allowed to remember, though."
    "Maya says that if I do, I might disappear. "
    "I don’t want to disappear yet."
    "I have so much left to do..."
    "If only there was someone around to guide me."

    s "…"
    s "…"
    s "…"

    "I say that as if I expect someone to just show up and do it."
    "That’s not how this works, though."
    "The closest I have to a guide at all right now is the one I need guiding {i}to{/i}."
    "For I’ve somehow found myself lost. Wandering around in the middle of the night with a destination in mind but not enough willpower to arrive there."
    "I begin to think of the things I will say if I do."

    if bonus == True:
        "“Hello. I retract my rejection of coitus. Come, Maya. Let us repopulate the world with more people who can travel through time.”"
    else:
        "“Hello. I do want a belly rub and a hug after all. Come, Maya. Let us do a variety of cute things with one another in complete disregard for the typical dynamic of our relationship.”"

    "How ridiculous."
    "Though I suppose the sheer idea of our existence in and of itself is ridiculous in a multitude of ways."
    "It is not poor luck, though. Which is how I’m sure she would describe it."
    "It is a blessing."
    "We can see everything."
    "Why should I be punished for not closing my eyes?"

    scene black
    with dissolve

    "I walk."
    "And I walk."
    "And I walk and I walk and I walk."
    "And I find something new."

    scene mayasnowshrine1
    with dissolve2

    m "Ah..."
    ay "…"
    a "Sensei? What are you doing here this late?"
    s "I could ask the same question to all of you."
    a "We came here to get Maya since we were all supposed to hang out tonight."
    ay "You’re not suddenly religious...are you, Sensei?"
    s "Me? No. I was just wandering around."
    s "I came up here because it’s usually warm. Apparently that’s not the case tonight, though."
    m "It..."
    m "It started snowing a couple hours ago."
    m "Just after the sunset."
    s "I see."
    s "Well if you three are planning on hanging out tonight, I can just head back."

    scene mayasnowshrine2
    with dissolve

    a "What? No! Come with us!"
    a "Where were you before this? It was probably a really long walk and...you don’t even have a real jacket."
    ay "We’re going out to a family restaurant. I can pay for you if you don’t have any money."
    s "I’m not broke, Ayane."
    ay "Yes, but I’m rich. So I really insist that you come with us."
    ay "Let me treat you and get you out of the cold."
    a "Yeah! Come on. Let’s get you somewhere warm."
    m "I...agree..."
    m "You should probably come with us."
    s "Why is everyone so concerned with warming me up all of a sudden? I feel fine."
    s "I’m just bored."

    scene mayasnowshrine3
    with dissolve

    m "You’re soaking wet."
    m "Which is...worrying since it’s not even snowing that hard."
    a "Yeah. Your hair is basically all white right now. You look like a cool grandpa."
    ay "If this is how you will look when you are old, I am even more excited for our future than I already was."

    "I pat down my pants and blazer to find that, yes, they are soaking wet. "
    "But when did this even happen? And why did I not realize anything until it was pointed out?"
    "The three girls stare at me, unsure of how to proceed with the conversation given that I likely look insane right about now."
    "And, you know, maybe I am?"
    "I’d certainly pass that judgement onto anyone I saw casually walking around in soaking wet clothes during a minor snowstorm."

    m "…"
    s "…"
    a "…"
    ay "Well, I don’t think just standing here is going to do anyone good. "

    scene mayasnowshrine4
    with dissolve

    ay "Should we maybe...call an ambulance or something?"
    a "What? No. He’ll be fine. Sensei never gets colds."
    a "He just gets like this sometimes. Once we get him home and into bed he’ll be as good as new."
    s "Okay, you two realize I can hear you, right?"
    s "I’m perfectly fine."
    s "Besides, I already offered to go home since you’re busy. "
    s "Making a big deal out of it is just going to make me feel weird."
    a "See, Ayane? No ambulance necessary. In fact-"

    scene mayasnowshrine5
    with dissolve

    a "Sensei, I’m going to walk home with you and make sure you’re okay. Ayane and Maya can go out to eat by themselves."
    ay "Actually...why don’t we just get something delivered to your house? "
    ay "I’m suddenly losing my appetite anyway."
    s "I-"

    scene mayasnowshrine6
    with dissolve

    m "Would it be okay if I spoke to him alone for a moment?"
    a "Huh? Really?"
    a "But you never want to talk to Sensei."
    m "And I’m not saying I want to talk to him now either. "
    a "Then why-"
    ay "Do you want to talk to Maya, Sensei?"
    s "I wouldn’t mind that."
    s "I think there’s something we need to clear up anyway."
    ay "What...do you need to clear up, exactly?"

    scene mayasnowshrine7
    with dissolve

    a "You and Maya? Did something happen that I didn't hear about yet?"
    m "A misunderstanding of sorts."
    m "It likely won’t take long...but you two can begin heading to Ami’s house or the restaurant or...wherever and then text me to let me know which one you decided on."
    m "I’ll make sure Sensei gets there, too."
    a "I mean...I don’t have any problem with-"
    ay "I don’t want to leave Sensei’s side right now."
    ay "This all feels very strange. "
    s "It’s fine, Ayane. Really. There’s nothing to worry about."
    ay "There’s nothing to worry about?"
    ay "You just...wandered over to where Maya hangs out in the middle of the night during a snowstorm to be alone with her and there’s nothing to worry about?"

    scene mayasnowshrine8
    with dissolve

    m "It’s not like that, Ayane..."
    a "Ayane, come on. It’s {i}Maya{/i}. "
    ay "…"
    m "…"

    "It’s not common that I see Ayane look at anyone this way."
    "And I’m sure she feels just as strange as I do on account of her resulting silence."

    if bonus == True:
        "Teenage girls are so fickle, getting upset over small things like this when there’s not even any substance to it."
    else:
        "College girls are so fickle, getting upset over small things like this when there’s not even any substance to it."

    "Maya and I {i}do{/i} need to clear up a misunderstanding."
    "That’s likely why I wound up here in the first place."
    "And it’s a misunderstanding that can’t be brought up around the other two, so-"

    ay "We’ll text you in a few minutes to let you know where we’re going."
    m "Can you {i}not{/i} look so angry while saying that, please? I didn’t even do anything."
    ay "This face just happens out of natural instinct when I think someone is trying to take Sensei away."
    a "If it makes you feel better, I don’t think you’re going to take Sensei away, Maya."
    a "You’re not girly enough anyway, so I doubt he would even like you like that."
    m "Oh. Thanks, Ami. That was...kind of you."
    s "Sorry for showing up and making things really awkward when you guys just wanted to get food."

    scene mayasnowshrine9
    with dissolve

    a "No need to apologize, Sensei! We’re all totally used to working our schedules around you by now anyway."
    ay "I’m sorry if I seemed angry. I’m not. "
    ay "I’ve just been feeling a little strange lately."
    s "It’s fine."
    s "I’ll meet up with you guys again in a little while."
    a "Don’t forget to text me every five minutes so I know you didn’t die of hydrothermopoly."
    s "Hypothermia. And sure."
    s "See you soon."

    scene black
    with dissolve2

    "Ami and Ayane slowly make their way down the steps of the shrine to avoid slipping and cracking their heads open on the concrete."
    "On the bright side, if one of them {i}did{/i} fall, it would be easy to rip off Maya’s skirt and use it to soak up all of the blood."
    "It’s also the same color, so any stain left would be barely noticeable."
    "I bow twice, clap twice, and bow again to prevent any of that from ever happening."
    "………"
    "……"
    "…"

    scene mayasnowshrine10
    with dissolve

    m "…"
    s "…"
    m "…"
    s "…"
    s "Okay, I’ll talk first."
    s "Aren’t you cold in that?"

    scene mayasnowshrine11
    with dissolve

    m "At least it’s not soaking wet. "
    m "There are plenty of warm spots inside of the shrine."
    m "You look like you’ve been wandering around for hours."
    s "I probably was. "
    m "You don’t remember?"
    s "All I remember is deciding to come here around the same time I always do."
    s "Then, before I knew it, I was being invited out to eat by a bunch of girls who paint their nails in my living room."
    m "And that doesn’t worry you?"
    s "Not really. I’m just a little upset that I missed an entire part of the day."
    s "That’s time I will never get back."

    scene mayasnowshrine12
    with dissolve

    m "Ha ha ha. Time loop humor. Hilarious."
    s "Well it’s not like you ever laugh at normal humor, so it was worth a shot."
    m "I laugh at plenty of things. You just have the worst sense of humor out of any person I’ve ever encountered."

    "It’s cute how she can still insult me while nervously twirling her ribbon around in her fingers."
    "But I’m sure she has a lot of practice."
    "By now, I’m sure the amount of insults I’ve received from this girl add up to around the same total as stars in the sky."
    "I’m sure she’d be happy to hear that comparison drawn, but I’m too cold and exhausted to make anyone happy tonight."
    "And..."
    "There’s still a “misunderstanding” that needs to be cleared up."

    s "So, about the other night-"

    scene mayasnowshrine13
    with dissolve

    m "I know. "
    m "And...I’m sorry."
    m "I was desperate and angry and said some things that should never have been said. "
    m "I’m honestly surprised you’re even here right now. "
    m "I was sure you were going to be avoiding me for at least another several weeks."
    m "But I suppose that if there is anyone in the world who can so harshly reject a girl only to return and talk about it shortly after, it’s you."
    s "Under normal pretenses, I wouldn’t have rejected you at all. "
    s "In fact, I don’t even see what happened as a rejection in the first place."
    m "Please, do tell what you saw it as."
    s "I’m not sure if the words ever made it out of my mouth back then, but I didn’t want you doing something like that out of sheer desperation."
    s "It’s not like that strategy would have worked either way."

    scene mayasnowshrine14
    with dissolve

    m "I know. "
    m "Which is why I’m glad you didn’t let me follow through with it."
    m "Also, if you ever deliriously compare me to a bird again, I will not hesitate to scratch your eyeballs out."
    s "I...did what?"

    if bonus == True:
        m "You said all sorts of strange things as I was frantically trying to get you aroused."
    else:
        m "You said all sorts of strange things as I was frantically trying to hug you."

    m "It was the most embarrassing several minutes of my life."
    s "…"
    m "…"
    s "I have no idea what I’m supposed to say to that."

    scene mayasnowshrine15
    with dissolve

    m "There’s no need to say anything, really."
    m "You’ve been having episodes like that since the first loop began."
    m "They just always manifest differently...and get progressively harder to pick up on as we move closer and closer to the middle or the end of a season."
    s "And is the “middle or the end of a season” getting close now?"

    scene mayasnowshrine14
    with dissolve

    m "I’d say we’re closer to the middle of the middle. "
    m "But, then again, everything I know about the world has been slowly fading away since winter began."
    m "For all I know, everyone could vanish tomorrow."
    s "And I’m sure that’s exactly what you’re hoping for, huh?"
    m "Yes. I’m trying to remain hopeful that it not only buys you more time, but gets rid of the single worst girl I have ever crossed paths with before she can damage you any more."
    s "She has not “damaged” me, Maya."

    scene mayasnowshrine16
    with dissolve

    m "Yes she has. "
    m "It’s near impossible for you to notice, but I’d like to inform you that, as of right now, I know you a hell of a lot better than you do."
    s "So does Noriko, but at least she’s nice about it."
    m "Being nice isn’t going to keep you alive. "
    m "She’s going to chase you off the same way she did the last time."
    s "Can you at least tell me what happened “the last time?”"
    m "No."
    m "In fact, the second I tried to tell you something even simpler than that, you passed out on my bed and started hyperventilating."
    s "Well...summarize it or something."
    s "I don’t remember much about that night, but I remember it was very important."
    m "And if you pass out on the ground and start hyperventilating {i}here?{/i} What am I supposed to do then?"
    m "Let you freeze to death?"


    if bonus == True:
        s "You could always try to force me to have sex with you again. That worked really well last time."
    else:
        s "You could always try to angrily hug me again. That worked really well last time."

    scene mayasnowshrine17
    with dissolve

    m "You-"
    m "You’re disgusting."
    m "Please don’t bring that up anymore. "
    s "I hope you know I’m going to bring that up literally all the time now."
    m "Does seeing me in anguish truly make you that happy?"
    s "Not really. But seeing you blush like that does."
    m "…"
    s "…"

    scene mayasnowshrine18
    with dissolve

    m "{i}*Ahem*{/i}"
    m "Since you’re so dead set on turning your life into some sort of puzzle that must be solved, I suppose I can try to summarize at least one very important detail for you."
    m "Without divulging too much, several things have transpired over the last several months that have forced me into an inevitable change of opinions about you."
    m "I’ve been noticing it for quite some time, but my stubbornness is one of my greatest flaws, and this meant that I was unable to accept it."
    m "I have told you in the past that you are “changing.”"
    m "I was wrong."
    m "I have told you in the past that everything is part of a cycle."
    m "I was wrong about that as well."
    m "You are not changing and, with how hectic things have become lately, there is clearly no cycle at all. And if there is, it’s a really fucking stupid one without any rules."

    scene mayasnowshrine19
    with dissolve

    m "The reason I don’t want you to learn any more about “your” past is precisely because it is {i}your{/i} past."
    m "Probably."
    s "Probably?"
    m "Saying “definitely” too soon and then losing you would be the emotional equivalent of dropping my body feet first into a meat grinder."
    s "So, does that mean that I'm-"
    m "Yes."
    m "Probably."
    s "But that still doesn’t explain-"
    m "I can’t explain anymore."
    m "Not safely at least."
    m "And I would really...{i}REALLY{/i} appreciate it if you’d stop looking for answers."
    m "Stay exactly where you are now- at the precipice of everything. The edge of the world..."
    m "Because the second you fall off-"
    m "I fall as well."
    s "…"
    m "…"

    play sound "texttone.wav"
    scene mayasnowshrine20
    with dissolve

    m "…"
    s "I should probably tell Ami and Ayane we’ll be coming to meet up with them soon."
    m "I should have done that earlier but my phone is still in one of the lockers."
    s "I’ll handle it. Just go get your stuff."
    m "Okay. "

    "I start typing a message out and-"

    m "Sensei."
    s "...Yeah?"
    m "If I could tell you more, I would."
    s "Really?"
    m "Really."
    s "Even though I’m the most disgusting person in the world?"

    scene mayasnowshrine21
    with dissolve2

    m "Right."
    m "Even though you’re the most disgusting person in the world."
    s "I get it."
    s "And thanks."
    s "Now, go get your stuff."
    m "Okay."
    m "I’ll be right back then..."

    scene black
    with dissolve2

    "I finish typing out the message I was about to send to Ami and Ayane before Maya interrupted me."
    "Even after hearing all of that, though, I think she might be overreacting."
    "It is troubling how today went down with...losing several hours and managing to aimlessly wander through a snowstorm without noticing."
    "But much worse things have happened much earlier on."
    "So chalking those lapses up to the fact that I now have someone {i}willing{/i} to tell me about the past..."
    "I don’t believe it."
    "It doesn’t add up."
    "And I don’t want to say Maya is hiding anything from me, but-"
    "Maya is clearly hiding things from me."

    m "Okay...sorry."
    m "I think that’s everything."
    m "Are we going back to your house?"
    s "Yeah. It looks like that’s the plan."
    m "Okay. But we should probably hurry up. "
    m "We’ve kept them waiting for quite some time and I am extremely cold right now."
    s "Want to hold hands and keep each other warm?"
    m "..."
    s "..."
    m "I would rather freeze to death."

    $ renpy.end_replay()
    $ maya_love += 1
    $ shrine35 = True
    stop music fadeout 8.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mayafestival1:
...
```

## Code that triggers this event

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label shrine:
    if howifeel == True:
        jump howifeel
    if maya_love >= 0 and firsttimeshrine == False:
        jump firsttimeshrine
    if maya_love >= 5 and shrine5 == False:
        jump shrine5
    if maya_love >= 10 and shrine10 == False:
        jump shrine10
    if maya_love >= 15 and shrine10 == True and mayadorm10 == True and shrine15 == False:
        jump shrine15
    if maya_love >= 20 and beachvacation16 == True and mayadorm15 == True and shrine20 == False:
        jump shrine20
    if maya_love >= 25 and mayadorm20 == True and shrine25 == False:
        jump shrine25
    if maya_love >= 30 and mayadorm35 == True and shrine35 == False:
        jump shrine35
...
```