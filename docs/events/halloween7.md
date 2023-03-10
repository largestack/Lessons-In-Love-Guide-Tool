# Once, Twice, Ten Times (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [They're Just Lights](./halloween6.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloween7
* Group: Main
* Triggered by label: halloween6
* Chain sources: halloween6
* Chain sources path: halloween6

## Official wiki page

[Once, Twice, Ten Times](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween7&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label halloween7:
    play sound "static.mp3"
    scene milfparty1
    with flash
    stop sound

    "I show up at the bar and-"
    "Wait, what?"

    play music "letsfuckingo.mp3"

    sar "Sensei! Over here!"

    "Sara slumps over the bar counter with a drink in her hand, likely already tipsy- if not worse."
    "Or better, depending on how you look at it."
    "I’m not sure how late I am but it was clearly enough time for her to start drinking without me."

    scene milfparty2
    with dissolve

    sar "What took you so long? I’ve been waiting all night~"
    s "How long has the party been going on?"
    sar "Almost a whoooooooole hour~"
    s "Oh. That’s it?"
    k "This establishment confuses me."
    k "The lights are blue and everyone appears to be aroused."
    k "You have inserted me into a strange situation, Friend."

    scene milfparty3
    with dissolve

    sar "Hey! How’d ya get Kaori to come cover the bar?"
    sar "You two good friends or somethin’?"
    sar "She’s reallyyyy cute, right? Don’t ya just wanna eat'erup?"

    scene milfparty4
    with dissolve

    k "Friend does not consume human beings, the Sara. He only collects the small ones and sells them through his various connections."
    s "Neither of these things are true."
    sar "Hehe~ You’re so funny, Kaori. You should come work here all the time."
    sar "My daughter would love you~ She could use a cool big sister. "
    sar "Other than me, I mean~"
    k "I hope you were less intoxicated when you decided to procreate. "
    k "It is a bad thing to make a child when there is so much dizzy-fluid involved."
    sar "Heheh~ How much do you know about making children, Kaori?"
    sar "Is there a boyfriend I should know about?"

    scene milfparty5
    with dissolve

    k "Wha?! B-Boyfriend?! Never!"

    if bonus == True:
        k "I would not be able to maintain so many jobs if I had to devote myself to a male companion!"
        sar "Suuuure, but then whaddya do about sex? Have anybody you like to fool around with?"

    scene milfparty6
    with dissolve

    k "Y-You did not inform me the Sara was so vulgar! I was not prepared for this line of questioning!"
    s "She’s just drunk. Don’t pay attention to her."

    scene milfparty7
    with dissolve

    sar "If she’s not gonna pay attention to me, {i}someone{/i} has to. It would be rude to make me feel all lonely in my own bar, Sensei~"
    sar "Heheh~ You know what would be {i}really{/i} fun? "

    if bonus == True:
        sar "If you and Kaori both gave me lots of attention. She looks like she could use a good teacher~ Whydontcha show her how to make *hic* a girl happy?"
    else:
        sar "If you *hic* started...teachin' Kaori how to do calculus right there on the counter..."
        s "Don't tempt me with a good time, Sara."

    scene milfparty8
    with dissolve

    k "This man has already taught me many things. "
    k "I am a slow learner and there is much I do not understand, but he has been kind to not move very fast."
    s "Kaori, why are your misunderstandings always so suggestive?"

    scene milfparty9
    with dissolve

    sar "Heheh~ Now it makes a littlemoresense how you were able to get her here on such short notice."
    sar "I’m a little jealous~ I take back my offer about sharing you. Nurse Sara is gonna get ya alltoherself tonight."
    k "The Sara, you are going to catch a cold if you do not properly button your shirt."
    k "It may also cause the men around you to become aroused, which could lead to several legal issues given that you own this bar."
    k "Also, can I put my regular outfit back on? My arms are unusually exposed and it frightens me."

    scene milfparty10
    with dissolve

    sar "But you look so cute in my barmaid outfit, Kaori~"
    sar "And besides, you have to dress up for Halloween. It’s one of the rules."
    k "But Friend is not wearing a costume."

    if bonus == True:
        sar "Of course he is~ He’s dressed up as “Guy with a huge penis.”"
    else:
        sar "Of course he is~ He’s dressed up as the huggy boy."

    scene milfparty11
    with dissolve

    k "I am not familiar with this character. He appears to be dressed the same as always."
    k "Are you a professional cosplayer as well as a teacher and human trafficker?"
    s "…"

    s "Can I have a beer, Kaori?"

    scene milfparty12
    with dissolve

    k "I will return with your carbonated wheat water shortly. "

    scene milfparty13
    with dissolve

    sar "Heheh~ She’s so funny, isn’t she? And so pretty, too."
    sar "Have you really gone all the way with her like she said?"
    s "That is not what she said. She just said I teach her, and even that isn’t entirely correct since all I do is correct her sentences."
    s "Now, if she {i}asks{/i} me to teach her other things..."
    sar "Can {i}I{/i} ask you to teach me other things, Sensei?"
    s "I don’t know, Sara. You seem to know most things already."
    sar "I can forget them if that will make you happy~"
    s "Can you really, though?"
    s "And also, where is everyone else? Is it really just you and Kaori tonight?"
    sar "Of course not. Haru-chan and Maki are on the couch."
    sar "Was my costume so alluring that you managed to walk right past them without even noticing?"
    s "To be fair, the pose you’re in is rather inviting. I can’t be blamed for approaching you first."

    scene milfparty14
    with dissolve

    sar "Well after you made me wait so long of course I’m going to look inviting~"
    sar "I’ve been looking forward to you getting here all night."
    sar "Just like I’m looking forward to playing Nurse Sara when you come up to my room after this~"
    s "I’m suddenly feeling very ill and require immediate medical attention."

    scene milfparty15
    with dissolve

    sar "At least go and say hi to the other girls first~ It will hurt their feelings if you completely neglect them for me, Sensei."
    sar "Besides, they’re super hot tonight. And Haru-chan’s boobs are all like “Whazaaaaaam.”"
    s "I don’t know if you’ve realized this, but they’re always like that."
    sar "Oh, I’ve realized alright. Poor me and my tiny boobs, having to hang out with someone like her all the time. "
    sar "It really hurts my self-esteem, you know?"
    k "The Sara! There are no cans of happiness anymore!"
    k "Where do you store the surplus ones?!"
    sar "Boo~"
    sar "I need to go help Kaori, so go hang out on the couch with the other girls for a minute, Kay? "
    sar "I won’t be gone long, I promise..."
    s "Oh damn. Well I guess if I {i}have{/i} to..."

    scene black
    with dissolve

    "I move through the dimly lit bar toward a table in the front of the room."
    "I guess I really did walk right past them when I came in."
    "But, to be fair, it’s not every day I get to see Sara in a costume."
    "And Kaori looks pretty adorable in Sara’s clothes as well."
    "Here’s hoping that Haruka and Maki look nice, too..."

    scene milfparty16
    with dissolve

    maki "Oh, look. He decided to show up after all."
    maki "And here I was thinking we may have lost our charm, Haru."
    h "Soooooo mean~ Especially after all the work it took to squeeze into our costumes."
    s "Yeah, that seems like a pretty tight fit for you, Haruka. "

    if bonus == True:
        maki "Don’t worry. I was able to help her into it just fine."
        maki "You should have heard her cute little moans when I touched her bare skin."
    else:
        s "You should be careful or the costume will cut off your circulation and kill you."

    scene milfparty17
    with dissolve

    if bonus == True:
        h "I only made those noises because your hands were so cold, Maki. "
        h "You need to watch what you say or Sensei might get the wrong idea about us."
        s "Yeah, I’m pretty sure the way you two are looking at each other right now is enough to give me the “wrong idea.”"
        s "Is there some sort of history here that I should be aware of?"
        maki "Sober history or drunk history?"
        s "...Both?"
        h "We may have kissed once or...twice or...ten times before."
        s "When? Not like I'm passing judgement here but aren't you married?"
        h "Is there something wrong with kissing another girl if you're married?"
        maki "Girls are an exception, obviously. I think he even watched us a few times."
        maki "I'm not really the best judge when it comes to that sort of thing, though."
        maki "I've definitely watched my husband fuck other girls, sooooo..."
        h "Besides, we were always drunk for it anyway."
        maki "Correction, {i}you’re{/i} always drunk. I’ve definitely faked it a couple times."
        h "What? You took advantage of me while I was drunk? Pervert!"
        maki "I pay for my apartment by selling dildos. You know I’m a pervert."
        maki "Besides, I shouldn’t be held accountable for anything I do to you since you’re so cute~"
        s "Wow, it’s like I’m not even needed here."
    else:
        h "Am I going to die, Maki?"
        maki "We're all going to die, Haruka. It's just a matter of when."
        s "Wow, it’s like I’m not even needed here."

    scene milfparty18
    with dissolve

    maki "You’re not."
    maki "Especially after walking right by us."
    maki "You’re banned from Maki and Haruka tonight. "
    maki "But don’t worry, Sara’s been talking about you since we got here. You can still have her."

    if bonus == True:
        h "Sorry, Sensei...I don’t make the rules, I just...get really drunk and kiss girls dressed in cat costumes."
        s "I wish I could say the same."
        h "Maybe you will soon...who knows?"

        "God I hope so."
    else:
        s "I do not want her. Please keep her away."

    k "One carbonated hoppy beverage for the glasses-man!"

    "Kaori walks up behind me and places a cold can of beer against my neck, causing me to flinch a bit in surprise."

    k "I attempted to cool your skin with it seeing as there are two women very close together in front of you."

    if bonus == True:
        k "That is bound to stimulate you biologically."
    else:
        k "If you are anything like me, you likely want to hug them."

    s "Thanks, Kaori."
    k "No, thank YOU for your assistance in acquiring the chicken-money! "
    k "I am leaving the bar now, but I will see you again soon!"
    k "I hope!"
    s "Sure. I'll call you soon."

    scene milfparty19
    with dissolve

    "Kaori leaves the bar at an almost sprint-like speed and Sara collapses onto the couch next to Maki."

    sar "That girl’s really something else, huh?"
    sar "I felt kinda bad making her see how...hot everything has gotten in here on account of these two love-cats, so I let her go home early."
    sar "I’m already super drunk anyway."
    s "So are these two, don’t worry."

    scene milfparty20
    with dissolve

    maki "Incorrect! I am not drunk whatsoever."
    maki "I have a surprisingly high tolerance when it comes to alcohol. "
    maki "I’m really just here to see Haru and Sara in their costumes. And you’re cool I guess, too."
    s "Thanks, Maki. I really appreciate that. "
    h "I also think you’re cool, Sensei..."
    h "Really cool..."
    h "Do you...like cats?"

    if bonus == True:
        s "I do now. "
    else:
        s "They're okay."

    sar "But you like nurses more, right?"

    if bonus == True:
        s "I believe I’d have to put those two things on the same pedestal. "
        s "Maybe next year all three of you could dress as cat-nurses or something. That would be a decision I could get behind."

        scene milfparty21
        with dissolve

        maki "Oh, you’d get behind it alright. Not sure you’d be able to handle what comes next, though."
        h "Maki...are you sure you’re not drunk?"
        maki "Who knows? I do feel pretty good right now."
        maki "But then again, that might just be because I have a cute catgirl on my shoulder."

        scene milfparty22
        with dissolve

        maki "Are you sure you feel okay, though? Your boobs are being like, completely suffocated by your costume."
        h "That’s my fault for trying to fit into a smaller size..."
        sar "She does this every year and always complains about it. I’ve just accepted it as part of Halloween at this point."
        sar "Come to think of it, mine feels a little tight too."
        sar "Maybe if I just..."

        scene milfparty23
        with dissolve

        sar "There. That feels better."

        "Sara suddenly unbuttons her nurse outfit and exposes her chest right next to Maki and Haruka, who seem too wrapped up in each other to pay it any mind."

        sar "Ah- Sensei! Where are you looking?"
        s "Where do you think I’m looking?"
        sar "Why, at a beautiful woman, of course~"
        sar "I even bought a new bra to go along with my costume. Cute, right?"
        sar "But wouldn’t it look even better on the floor of my bedroom?"
        s "Can I take that as the cue for being invited upstairs?"
        s "Because I honestly don’t know how much more of this sight I can handle."

        "Sara looks at me in silence for a moment as Haruka and Maki fall deeper into each other’s eyes."

        scene milfparty24
        with dissolve

        sar "Hey, do either of you two mind if Sensei and I disappear for a bit?"
        h "Hey, are you trying to pull me closer right now?"
        h "I might be drunk but I’m not {i}that{/i} drunk yet."
        maki "Hm? Why on earth would I try to pull you closer? What are you insinuating, Haru?"

        scene milfparty25
        with dissolve

        sar "Yeah, I don’t even think they’ll see us leave."
        s "Fine by me. Lead the way."
        sar "What, you’re not going to carry me up the stairs?"
        s "You’re the nurse. You’re the one supposed to be caring for me, remember?"

        scene milfparty26
        with dissolve

        sar "Oh, I’ll care for you alright."
        sar "I just need to make sure I can safely get up the stairs first."
        s "Any thoughts on inviting the cats as well?"
        sar "Sorry, Sensei~ Animals aren’t allowed in the hospital. "
        s "That’s a stupid rule. Animals should always be allowed in the hospital."
        sar "Maybe another night~ I want you all to myself this time."
        sar "Besides, those two are probably going to start making out soon anyway."
        s "Then...can we stay and watch?"
        sar "If we stay any longer, I might pass out."
        sar "It’s now or never~"
        s "Well then I obviously pick now. But I think we might wind up missing out on something pretty great, to tell you the truth. "
        sar "Now is an excellent choice..."

        scene black
        with dissolve2
    else:
        s "Of course. They're extremely important in the medical field."

        scene black
        with dissolve

        s "Now, if you'll please excuse me, I am going to close my eyes. This is getting a bit too saucy for my liking."
        sar "HAHA! YOU HAVE LET YOUR GUARD DOWN!"
        s "What? No-"


    sar "We’ll be back later, you two! "
    sar "Enjoy your couch!"

    "Sara hobbles over to me and pulls me by the wrist with what little strength she’s able to get out of her intoxicated body."

    if bonus == True:
        "She doesn’t even bother buttoning her shirt back up because, at this point, it would just be creating one more step on our way to what I imagine will be kinky Halloween sex."
        "Sure, I wish the other two could have gotten involved as well, but I’m not going to cry about {i}only{/i} getting into bed with a sexy nurse."

    stop music fadeout 10.0

    "We finally make it up the stairs after a bit of a struggle from Sara in maintaining her balance."
    "But once we’re in the apartment, she slams me up against the door and passionately kisses me before throwing it open so hard it almost puts a hole in her wall."
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ halloween7 = True

    if sara_lust < 10:
        jump saralust10skip
    else:
        jump saralust10

label saralust10skip:
    s "Wait..."
    s "Sara?"

    if bonus == True:
        scene saralust10skip1
        with dissolve

        "Sara passes out face-first on the bed as soon as we make it into the room."

        s "…"

        "Did I really come all the way up here for this?"
        "Maki and Haruka are probably making out right now."

        s "Wake up..."

        "I poke Sara’s ribs a few times, hoping that will shock some life back into her, but she stays completely still, breathing heavily."

        sar "Mmm...Sen...sei..."
        sar "Time for...your..."
        sar "Medicine..."
        s" …"

        "I poke her again to no avail before deciding to give up on this entirely."

        scene black
        with dissolve

        "{i}Uh-oh! It looks like Sara wasn’t horny enough to persist through the effects of alcohol!{/i}"
        "{i}If only her lust had been a little bit higher...{/i}"

        "I head back downstairs to find Haruka and Maki still close to kissing but not exactly there yet."
        "I wait around and watch for another ten minutes or so before I decide to give up on that as well."
        "Tonight just isn’t my night, I guess."
        "Here’s hoping tomorrow will be better."

        "………"
        "……"
        "…"

        jump halloween8
    else:
        sar "Zzzzzzzzzzzzzz..."

        "Sara falls asleep and I am unable to hug her."
        "Drat."

        "………"
        "……"
        "…"

        jump halloween8

label saralust10:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```