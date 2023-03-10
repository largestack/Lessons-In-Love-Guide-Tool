# Abyss (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yumi love greater than or equal to 35

* Event [Tech Support](./yumidorm35.md) (Yumi) is completed)

* Day of week is not Saturday

* yuminumber equal to True (unknown variable)



## Next events

* [Futaba: Shadowplay](./library40.md)
* [Kaori: To Die, To Sleep](./kaoridate15.md)

## Event properties

* Id: yumicallnight35
* Group: Yumi
* Triggered by label: callyuminight
* Triggered by branch label: callnight
* Triggered by path: callnight->callyuminight->yumicallnight35

## Official wiki page

[Abyss](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumicallnight35&go=Go) for more details.

## Event code

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
label yumicallnight35:
    scene black
    with dissolve

    "........."
    "......"
    "..."

    play sound "phonebeep.wav"

    "I tap on Yumi’s name in my phone and wait for her to answer."
    "It’s something I never thought I’d be able to do."
    "Of course, there’s no guarantee that she’ll answer."
    "The thought of calling her alone is just-"
    "I don’t know."
    "Surreal?"
    "Like it’s the end of one age and the beginning of another."
    "Then again, it’s probably just me being dramatic."

    play sound "phonebeep.wav"

    y "…"
    s "…"
    s "Hello?"
    y "Why are you calling me?"
    s "Why did you pick up?"
    y "It’s dark out. I didn’t see the name on the ID thing."
    s "Does your phone not light up?"
    y "Shut up! It doesn’t matter why I fucking answered. What do you want?"
    s "Just...wanted to see what you’re up to."
    y "Well I’m walking. Is the call over now?"
    s "Walking where? It’s late."
    y "Chika’s place."
    y "I’m sleeping there tonight."
    s "Cool. Maybe I’ll drop by as well."

    if bonus == True:
        y "Fuck no you won’t. Chinami sleeps in a giant fuckin’ T-shirt and nothing else."
        y "If you think I’m letting you anywhere near her without pants on, you’re-"

    s "See you soon, Yumi."
    y "Wait! "

    "I go to hang up the phone as I’ve already decided what to do tonight, but an uncharacteristic, serious sort of urgency in Yumi’s voice beckons me to stop."

    s "What’s up?"
    y "…"
    y "How quickly can you get to the old district?"
    s "Are you...offering to hang out with me alone?"
    y "If it keeps you away from Chinami, yeah. I can bite the bullet."
    s "You really have no faith in me at all, do you?"
    y "Why would I?"
    y "Just...start heading over to Chika’s and I’ll meet you on the bridge or some shit."
    y "They don’t know I’m on the way yet, so I don’t have like a time limit or anything."
    s "…"

    "Huh."
    "The uncharacteristic urgency turns into an even less characteristic invitation."
    "The only times I’ve ever really seen Yumi at night have been in her dorm room or...scattered occasions where she finds me wandering around the city."
    "Is it safe for me to meet her tonight?"
    "I don’t like the second half of town. I make that known rather frequently. "
    "And with Yumi’s not-at-all suspicious tendency to be around for what she’s referred to as “mind comas or whatever-”"
    "I worry for her."
    "I should probably tell her that I don’t want-"

    play sound "static.mp3"
    scene nightsky with flash
    stop sound
    play music "blueair.mp3"

    s "I’m on my way."

    "I lose control over my words and agree to doing something that could turn out simply horrible."
    "My legs start moving on their own."
    "I want to go back inside."
    "It’s so cold."

    y "Whatever..."
    y "You have to cross the bridge to get to her house, so I’ll just wait for you over there."
    s "{s}Be careful standing around that place at night.{/s} Sounds good. I’ll see you soon."
    y "Yeah...bye."

    play sound "phonebeep.wav"

    "Yumi hangs up before I have the chance to."
    "Not like I’m sure if I’d be able to at this point anyway."

    s "…"

    "Actually-"
    "I feel fine now."
    "My legs stop moving on their own and I have to send signals to them via my brain to get them to move the old fashioned way instead."
    "Walking is better when done manually."
    "I am excited to walk very far tonight."

    play sound "static.mp3"
    scene yumiknows1 with flash
    stop sound

    "I finish walking very far and end up in the second half of town, a foot or two in front of a girl I routinely [masturbate] to."

    y "Did you fucking run here or something? That was way quicker than I thought it would be."
    s "Sorry. I was just so excited to see you that I couldn’t contain myself."

    scene yumiknows2
    with dissolve

    y "Give it a fucking rest. You were probably just doing laps around this place looking for me anyway."
    y "Wouldn’t be the first time you’ve successfully hunted me down around here."
    s "Do you think anyone else would ever exert so much effort looking for you?"

    scene yumiknows3
    with dissolve

    y "Probably fucking not, but you sound like even more of a dick than normal when you come out and say it like that."
    s "I’m sorry. Just...feeling a little strange, I guess."
    y "What kind of strange? What’s going on?"
    s "Like I don’t even remember how I got here."

    scene yumiknows4
    with dissolve

    y "This shit again? Really?"
    y "Either you’re lying about not being a fucking junkie or you need to go to a hospital, because this shit really {i}is{/i} getting out of hand."
    y "Let somebody else deal with this instead of me. I had plans tonight."
    s "Plans you surrendered to spend time with me."

    scene yumiknows5
    with dissolve

    y "Plans I {i}surrendered{/i} to prevent you from blacking out in front of anyone else."
    y "Chika and Chinami adore you. You really wanna ruin that by coming all the way out here when you’re “not feeling well?”"
    s "{s}I don’t know what I want.{/s} What I want is you, Yumi."

    "What?"
    "I didn’t-"

    scene yumiknows6
    with dissolve

    y "Watch your fucking mouth. It’s not funny to joke about shit like that."
    s "{s}I’m sorry. I didn’t mean to.{/s} It’s not a joke. I genuinely-"

    scene yumiknows7
    with dissolve

    y "If it’s not a fucking joke, it’s a trick! And I’m not gonna let you pull one over on me again!"
    y "I came out here to meet you tonight, didn’t I?!"
    y "Either talk to me like a normal fucking human being or get lost! I don’t have time for this!"

    play sound "static.mp3"
    scene smile
    with flash
    stop sound
    play music "contemplation.mp3"

    "///////////////////////////////////hello."
    "///////////////////////////////////have you lost your way?"
    "///////////////////////////////////humans tend to lose their way quite frequently, i find."
    "///////////////////////////////////perhaps i can reroute you."

    s "Who are you?"

    "It becomes easier to speak all of a sudden."
    "I regain full control over my body and my tongue, but find myself surrounded by nothing but blackness."
    "I can feel hands on my shoulders."
    "Or perhaps my hands on someone else’s."
    "Whatever is happening, it’s not happening here."

    "///////////////////////////////////a friend."

    s "You don’t look very friendly."

    "///////////////////////////////////do not worry. it is only a temporary appearance."
    "///////////////////////////////////where is it you would like to go?"
    "///////////////////////////////////i can take you anywhere you want."
    "///////////////////////////////////anywhere outside this half of town."

    s "What about Yumi?"

    "///////////////////////////////////yumi?"

    s "The girl I’m with."
    s "Outside of this abyss."

    "///////////////////////////////////oh."
    "///////////////////////////////////i know her by a different name."

    s "A different name?"

    "///////////////////////////////////it is a matter that does not concern you."
    "///////////////////////////////////but, if it will make you happy, i can send you back to her."
    "///////////////////////////////////is that where you would like to go?"

    s "…"
    s "I don’t know. Does she look mad?"

    "///////////////////////////////////she looks scared."
    "///////////////////////////////////but she always looks scared when she is with you."
    "///////////////////////////////////the same way you always looked scared when you were with her."

    s "With who?"

    "///////////////////////////////////the world."
    "///////////////////////////////////goodbye for now."
    "///////////////////////////////////i will see you again soon."

    play sound "static.mp3"
    scene yumiknows8
    with flash
    stop sound

    s "…"
    y "…"

    if bonus == True:
        "I find myself leaned up against the same guardrail where Yumi and I first kissed."
    else:
        "I find myself leaned up against the same guardrail where Yumi and I first hugged."

    "She doesn’t look mad at all, thankfully."
    "If I were in her shoes, and someone went and did something as inconvenient as getting sucked into what I can only vaguely recall as an abyss-"
    "Well, I don’t think I’d be very happy."
    "Especially when she should be somewhere else right now."

    y "You should really be fuckin’ paying me for this shit, you know?"
    s "I’m surprised you didn’t just leave me down there."

    "I obviously can’t see what Yumi sees, but I imagine that the two of us have our sights set on the bridge we started on tonight."
    "How...or rather, {i}why{/i} we ended up here is an entirely different question, though."

    y "I wanted to. But you looked so fuckin’ helpless that I just..."
    y "Kinda grabbed you and brought you up here to relax."
    s "…"
    s "Did we hold hands?"

    scene yumiknows9
    with dissolve

    y "I mean...kind of! But only because I had to!"
    y "You’re too big to fucking carry!"

    scene yumiknows10
    with dissolve

    y "And...I’m wearing gloves anyway. So it was kind of like it never even happened."
    y "In fact, it never {i}did{/i} happen."
    y "We both walked up here alone and, now that you’re fuckin’ normal again, it’s time to split up."
    s "But why {i}here{/i} of all places?"
    y "I don’t know."
    y "I kind of like the view from up here."
    y "Sucks you had to go and scar me so I can barely come up to fucking see it anymore."

    "I take a step back as she says this, putting a fair amount of distance between us so if I {i}do{/i} happen to snap again, she’ll be able to get away."
    "Or at least hurl herself over the guardrail like Shel Silverstein would have wanted."

    scene yumiknows11
    with dissolve

    y "Thanks."
    s "Please don’t feel the need to thank me for backing up."
    y "Why? It’s one of the few times you’ve actually done something to make me {i}more{/i} comfortable instead of fucking with me like you normally do."
    s "Because the only reason you’re {i}uncomfortable{/i} is because of me in the first place."

    scene yumiknows12
    with dissolve

    y "I’m always uncomfortable around here."
    y "Especially at night."
    y "All those fuckin’ homeless people. You know?"
    s "Are they like...violent or something?"
    s "I haven’t really encountered any issue like that around here."
    y "Not violent. Just fucking weird."
    y "Like they’ve had all the life sucked out of them or some shit. And now they just line the streets without anywhere to be or anything to do."
    y "You think I’ll end up like that one day?"
    s "Do {i}you{/i}?"
    y "Beats me. Not like I have anything goin’ for me."
    y "Fail at shit all the time. Succeed at shit never."
    y "It’s kind of like I’m stuck in some sorta abyss or some shit. Know what I mean?"
    s "More than you could imagine."
    y "Yeah?"
    y "Guess the difference is that I stay conscious when I feel like that and you turn into a fucking zombie."
    s "Well thank you for always dealing with it."
    y "Long as you don’t lay your hands on me, it’s whatever."
    s "Speaking of which-"
    s "When I was...out of it, I felt someone’s hands on my shoulders."
    s "Was that you?"

    scene yumiknows13
    with dissolve

    y "Huh? No. All I did was just kind of drag you along by your wrist."
    y "Maybe it was one of the homeless people? Sly fuckers, some of them."
    s "Huh..."
    s "Could have just been hallucinating it."
    y "Probably."
    s "So, what now? It’s already really dark. Aren’t Chika and Chinami expecting you?"
    y "Yeah. I’ll head over there in a few minutes."
    y "Just tryin’ to be nice for once and make sure you can find your way back and shit."
    s "You’re being suspiciously nice tonight."
    s "Why?"
    y "…"
    s "…"

    scene yumiknows14
    with dissolve

    "The moonlight reflects off of Yumi’s pale skin as she gazes up at the sky."
    "When you factor in her clothing and how it completely contrasts with the world around her right now, it makes it seem like she’s not supposed to be here at all."
    "But perhaps none of us are supposed to be here?"
    "Perhaps, and this is just one more guess to throw into the pile of “things I can’t explain-”"
    "But perhaps the only reason I so frequently “black out” beside her is that neither of us belong here."
    "{i}Here{/i} as in together."
    "We’re two people with nothing in common who keep getting tossed into situations that wind up making one of us uncomfortable or out-of-place."
    "More common than not, that person is her."
    "Tonight is different, though."
    "Tonight, I will feel out of place no matter who I’m with or where I am."
    "There is no place for me here."
    "This is not my world."

    if chikaonsen4 == False:
        y "I..."
        y "Fuck. This is harder to say than I thought it would be."

        scene yumiknows15
        with dissolve

        y "I don’t...{i}hate{/i} you, Sensei."
        y "Like, I still think you’re a fucking scumbag and want to vomit every time I come up here."
        y "But I don’t hate you."
        y "And also, I’m kind of a scumbag too. So I get it."

        if bonus == True:
            y "We’re two shitty people. Just I pick on the ones I don’t like and you try to get into their pants."
            s "Trying to get into girls’ pants doesn’t make me a scumbag."
        else:
            y "We’re two shitty people. Just I pick on the ones I don’t like and you try to hug them."
            s "Liking hugs doesn't make me a bad person."

        y "If it’s the entire fucking class, then yeah. It does."
        s "So if it was only {i}you{/i}, it would be okay?"

        scene yumiknows16
        with dissolve

        y "Ew, no! That wouldn’t be okay at all!"
        y "But at least I’d be able to find some respect for you if you’d just fucking pick one and stick with her."

        scene yumiknows17
        with dissolve

        y "Like...I don’t know. Chika?"
        s "…"
        s "Are you...giving me your blessing right now?"
        y "I’m not giving you shit."
        y "It just...kinda hurts watching her fall so hard for you when I know the type of guy you really are and she doesn’t."
        y "I’m tired of hearing how excited she is to go on that fucking trip with you and I’m tired of how many times I have to tell her “Maybe tomorrow.”"
        y "Might be hard to believe since it’s me and shit, but I care about her a lot."
        y "Her and Chinami are all I have now."

        scene yumiknows18
        with dissolve

        y "Which is why I’m not going to let you trample all over her naive fucking heart."
        y "Put her first."
        y "Tell her everything she wants to hear and never even {i}think{/i} about screwing her over. Got it?"
        s "…"
        y "{i}Got it?{/i}"
        s "I appreciate your resolve-"
        s "But you should keep your nose out of my love life."
        s "I’m not going to just drop everything and be with one person because you told me to."
        s "Chika is a great girl, don’t get me wrong."
        s "But she’s almost {i}too{/i} great."
        s "Like, she shouldn’t be with me."

        scene yumiknows19
        with dissolve

        y "Well you’re definitely right about that."
        y "Who the fuck {i}would{/i} be good with you, then?"
        y "Would have to be a real screw up. Equally as douchey. Zero work ethic. A whole bunch of shit."
        s "Sounds to me like we might be a better match than you think."

        scene yumiknows20
        with dissolve

        y "Wha-?! Shut the fuck up! We would not!"
        s "Yumi Yamaguchi..."
        s "Will you marry me?"
        y "That’s it! I’m leaving!"
        y "Never call me again!"

        scene black
        with dissolve

        "Yumi runs off into the night and I’m unable to keep up with her."
        "I could just go back to Chika’s place to see her again but..."
        "I feel like I should probably let her sit on my totally serious marriage proposal for a little longer before following up."
        "I obviously know Chika likes me."
        "And I’m glad that Yumi is finally able to talk about that with at least some semblance of seriousness to it."
        "But I do think it would be good if she’d think of herself more instead."
        "Because, despite the constant beratement-"
        "It’s as clear as the sky in the second half of town..."
        "That she may be starting to feel something as well."

        $ renpy.end_replay()
        $ yumi_love += 1
        $ yumicallnight35 = True
        stop music fadeout 5.0

        "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

    else:
        y "I..."
        y "I heard about what happened with you and Chika."
        s "…"

        "Well, that secret didn’t last very long."

        y "I don’t know how much of it is just fucking manipulation on your part, but I’m trying to give you the benefit of the doubt."
        y "So when you say shit like “I want you, Yumi...” it really pisses me the fuck off."

        scene yumiknows18
        with dissolve

        y "Chika is a good fucking person. And, for whatever reason, she wants {i}you{/i} instead of anyone else."
        y "Being her boyfriend or whatever is a good start since...I know you haven’t done anything else with her yet-"

        if bonus == True:
            "Oh...so the sex part is still a secret?"
            "I’m honestly surprised Chika managed to hold back that much."
            "That’s...actually really cool of her."

        y "But the second I find out you’re doing something to hurt her, I will destroy you."

        if bonus == True:
            y "So even if you’re joking when you say all that pervy shit to me, know that you’d be hurting the sweetest, most faithful girl I’ve ever met a lot if she ever heard any of it."
        else:
            y "So even if you’re joking when you say all that annoying shit to me, know that you’d be hurting the sweetest, most faithful girl I’ve ever met a lot if she ever heard any of it."

        s "And she told you that this was something that shouldn’t be discussed with anyone else, right?"

        scene yumiknows21
        with dissolve

        y "She did."

        if bonus == True:
            y "But I think that’s less about wanting to keep it a secret and more about you still wanting to fuck around with other girls."
            y "If you were willing to go after me of all people, I can only imagine what kind of shit you’ve tried doing to some of the others."
            s "…"

        y "Like I said, I’m going to try to give you the benefit of the doubt for her sake."
        y "But I’ll be fucking watching you. Got it?"
        y "And the second you do anything that might hurt her, I’m not only telling her about it, but I’m going to ruin your fucking life."
        y "I don’t care if the principal won’t believe me. I’m telling him. I’m telling that fucking weird, purple haired goth teacher too."
        y "Shit, I’ll send a letter to the fucking newspaper."

        scene yumiknows22
        with dissolve

        y "I...will not...let you hurt that girl."
        s "…"
        y "…"
        s "You’re being surprisingly mature about this."
        y "So?"
        s "I just kind of expected more of a freak out...You know, maybe a few more insults and whatnot."
        y "I’m too tired to insult you."
        y "I just want to go eat ice cream at Chika’s house."
        s "What is it with you and ice cream all of a sudden?"

        scene yumiknows20
        with dissolve

        y "It’s not “all of a sudden!” It’s fucking ice cream, dude! I have liked it forever!"

        if bonus == True:
            s "You certainly seemed to enjoy it with the way you-"
        else:
            s "I'm not really a big fan, to be honest."

        y "That’s it! Conversation is over!"
        y "Enjoy your walk back home, asshole!"

        if bonus == False:
            s "Wow, you really do like ice cream."

        scene black
        with dissolve

        s "Wait, Yumi. I-"
        y "I said the conversation is over! Stop following me!"

        "Yumi runs off into the night and I’m unable to keep up with her."
        "I could just go back to Chika’s place to see her again but..."
        "Given everything we talked about tonight, it’s probably best if I just leave things alone for now."
        "I’m not sure what knowing about Chika and me will do to my relationship with Yumi-"
        "But at least I can find some form of solace in knowing that she’s a good person deep down."
        "I doubt that about her sometimes."
        "I probably shouldn’t, though."
        "Not when I’m ten times worse."

        $ renpy.end_replay()
        $ yumi_love += 1
        $ yumicallnight35 = True
        $ yumiknows = True
        stop music fadeout 5.0

        "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
        "………"
        "……"
        "…"

        if day < 6:
            jump endofweekday
        else:
            jump endofsat

label yumispecial40:
...
```

## Code that triggers this event

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
label callyuminight:
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        jump callnight
    if halloweentwo5 == True and streets40 == False:
        "Yumi's phone is still broken."
        "I should call someone who is more responsible with their belongings."
        jump callnight
    if yumi_love >= 35 and yumidorm35 == True and day!= 6 and yumicallnight35 == False:
        jump yumicallnight35
...
```