# We Were Angels
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach13&go=Go)


Part of event chain [Left Out in Light](./secondbeach12.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: secondbeach13
* Group: Main
* Triggered by label: secondbeach12

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label secondbeach13:
    scene nikiami1
    with dissolve2
    play music "remember.mp3"

    a "...and so that’s the story of how Ayane got kicked out of Taco Bell!"
    ka "Yeah...that sounds about right."
    to "Forgive me, but I’m a bit lost. I’m not seeing the connection between elephants and affordable {size=-15}(By commoner standards){/size} Mexican food. "
    a "That’s exactly it, Touka! Those two things have nothing to do with one another. "
    a "It’s just Ayane being Ayane, I guess."
    to "The Amamiya family sure uses their wealth in a different way than my own."

    scene nikiami2
    with dissolve

    to "Why, I recall a time not too long ago when I was craving nourishment. My father had an entire restaurant airlifted all the way to me just to satisfy those needs."
    ka "You mean like...some kind of helicopter DoorDash or something?"
    to "Heavens, no. I mean the entire restaurant. And, come to think of it, that time was last night. "
    to "Is that funny by your standards, Ami? I’m attempting to mimic lower middle class humor by telling mildly amusing stories that people from all walks of life can relate to."

    scene nikiami3
    with dissolve

    a "Wait...why just me? Karin counts as a commoner too, doesn’t she?"
    to "I’m afraid I’ve only just met her, so I didn’t want to assume she had less money than she actually does and wind up offending her."
    ka "That’s not really something that would offend anyone, Touka. I mean, the majority of the country is in the same financial bracket as Ami and me. "

    scene nikiami4
    with dissolve

    a "That’s right. We have accepted our place in society as average Joes and Julies and must resort to dreaming about the amount of money you have since we’ll never actually {i}have{/i} it."
    to "I’m very sad to hear this, but I’m still having trouble understanding how the elephant wound up {i}inside{/i} of the restaurant."
    a "Haha! Classic Ayane."
    ka "That girl's going to walk into the wrong fast food place one day."
    ka "Just kidding. She already did that. "
    ka "I tried to make a joke but it sounded more like I wasn’t paying attention. I am."
    ka "I’m sorry, everyone."

    scene nikiami5
    with fade

    u "Otoha, where did you get your swimsuit? I really like it."
    o "Uhh...Amazon? I don’t really remember."
    u "Are you just saying that because we’ve already name dropped Taco Bell and DoorDash and this is the product placement event?"
    o "What? No. Of course not."

    scene nikiami6
    with dissolve

    f "Oh, look. Here comes Maya."

    scene nikiami7
    with fade

    m "Hey, guys."
    u "Princess Maya! What are you up to this fine morning?"
    m "Just enjoying the crisp, refreshing taste of a Coca Cola. "
    m "How about you?"
    f "We’re trying to figure out which store Otoha got her swimsuit from."
    o "I’m not really participating in any way. I’m supposed to stay out of product placement because it won’t be good for my image if I make it in the future."
    m "That’s really depressing."
    m "But what’s not depressing is the taste of an ice cold Coca Cola after a long day of work or[school]."

    scene nikiami8
    with dissolve

    m "Coca Cola. "

    scene nikiami7
    with dissolve

    m "Anyway, bye."

    scene nikiami9
    with fade

    o "Yeah, so I’m pretty sure I just got it off Amazon."
    u "Neat!"
    f "Hey...you went out with Rin after D&D last night, didn’t you?"

    scene nikiami10
    with dissolve

    o "Hm? Yeah, right before we went back to our rooms. We didn’t really do anything, though. Why do you ask?"
    f "Oh. I was just wondering how things went since...Nodoka told me you thought she might have been avoiding you."

    scene nikiami11
    with dissolve

    o "Oh! Yeah. I...think that’s over with now? "
    o "Was just kinda confused since she’s never done anything like that before."
    f "I'm pretty sure it was just a weird morning. And...however long she was doing it before that for."
    f "It was probably several weird mornings."
    f "I don’t know. I’m glad everything is okay, though."
    f "You two made plans for...tonight, didn’t you?"

    scene nikiami12
    with dissolve

    o "Uhh...I think so?..."
    o "But she kind of just ran off as soon as I agreed so...can only imagine what that was about."

    scene nikiami13
    with fade

    a "Have I mentioned at all this morning how much I hate the two of you and want you to die?"

    scene nikiami14
    with dissolve

    ka "Yes. Several times on the way to the table. And when we passed that one palm tree that looked like a hockey stick. And then again when we sat down."
    to "I recall the last instance, but this is the first time our deaths have been associated with it."
    to "Do you really desire large breasts so badly that it drives you to despising those who possess them?"
    a "Whaaaat? Meeeee? Noooooo. Meeeee?"

    scene nikiami15
    with dissolve

    ka "You...are really pretty though, Touka."
    ka "Like...not just your breasts. But the...whole Touka...thing..."
    to "Oh my. "
    to "Karin...you aren’t flirting with me, are you? Because I’ve not yet trained myself on how to properly reject a woman- let alone one that’s also my senpai."

    scene nikiami16
    with dissolve

    ka "Why do I even talk when everything I say comes out as...words?"
    a "Don’t worry, Karin! You’ll get there soon enough!"

    if bonus == True:
        a "What I used to do to prepare myself for saying cute things to Sensei was saying them to stuffed animals first!"
        a "Then, once I was able to do it with my eyes closed, I’d go say it to him."
    else:
        a "When I want to say cute things to Sensei, I write them down in blood on parchment paper and then take little bites out of them until I re-absorb all of the feelings."

    a "It never worked so this probably isn’t great advice, but I’m sure you get what I’m trying to say."
    to "My, how peculiar."
    to "I do believe there is a famous pop musician who just joined us at the table."

    scene nikiami17
    with dissolve

    a "Touka...I don’t know how else to say this, so I’m just going to be blunt."
    a "Your high class jokes don’t really work on us...{i}normal{/i} people."
    a "You can’t just say “Oh look, there’s a thing here that isn’t {i}actually{/i} there,” because that’s more like a...prank than a joke."
    a "And even then, it’s just...not all that funny."
    ka "Oh my God. Niki Nakayama is right behind you."
    a "See? It’s just not funny at all. And thanks for the example, Karin."
    to "No...Ami, I do believe she is, in fact, right behind you."
    ka "She’s looking right at you. "
    to "Poor Chika...sleeping in on the day her favorite artist shows up to breakfast."

    scene nikiami18
    with dissolve

    a "Guys, I’m not going to fall for it."
    a "I might not {i}look{/i} mature, but I can guarantee you that there’s no way I’m gullible enough to believe that the queen of everything, Niki Nakayama, my all time favorite non-Sensei human, is at our table."
    a "You think {i}Niki{/i} would come to this beach? Are you insane?"
    a "Sure, she might be Noriko’s older sister, but there’s no way Noriko would be able to convince her to come waste her time on {i}us{/i} when she has so many better things to do."

    scene nikiami19
    with fade

    o "Yo. What are you doing here?"
    u "Is this..."
    u "Is this real?"
    f "Ami...I..."
    f "I think you better turn around..."
    a "You too, Futaba? Come on. I’m not-"
    ni "{i}*Ahem*{/i}"
    a "…"
    n "Surprise! I brought a pop star!"
    a "Noriko, you didn’t-"

    scene nikiami20
    with hpunch

    a "AAAAAAAHHHHHHHHH! YOU REALLY ARE HERE!"

    "Ami jumps out of her seat at the picnic table and stands before who I guess is her role model."
    "Little does Ami know, her role model is actually a conniving and evil pink demon who thinks the world should bow before her because she knows how to dance or something."
    "Just kidding."
    "Niki isn’t that bad. She just calls me mean things a lot."
    "But so does Maya and I still talk to her."
    "And Yumi."
    "And Tsuneyo."
    "And Wakana and Osako."
    "Wait, why are so many girls mean to me?"
    "Am I actually unpopular with women?"

    ni "Hi, Ami."
    ni "You’ve gotten so tall."
    ni "Well...comparatively. You weren’t even really human sized the last time I saw you."

    scene nikiami21
    with dissolve

    a "You...saw me and...I don’t remember it?"
    ni "You were just a little kid back then. I can’t even remember how old."
    s "She was also at the diner when you were there for the D&D thing. "
    s "If I knew it was this big of a deal, I would have just introduced you back then."

    scene nikiami22
    with dissolve

    ni "You knew Ami was at the diner and you didn’t introduce me?!"
    a "You knew Niki was at the diner and you didn’t introduce me?!"
    s "Jeez. There’s no need to be dramatic. I didn’t realize it was that big of a thing."
    a "You {i}know{/i} I love Niki! She’s the only girl I’d share you with!"

    scene nikiami23
    with dissolve

    ni "You don’t have to worry about that. Your [uncle] and I broke up a really long time ago. Before you two...even..."

    scene nikiami24
    with dissolve

    ni "You know what? Let’s not even talk about that. Can I have a hug?"
    a "You...you’re asking...{i}me{/i} for a hug?..."
    a "But...but you’re...an angel...and I’m just..."
    ni "An adorable [young_girl] who I’ve wanted to see again for a very long time."

    scene nikiami25
    with dissolve

    a "This can’t be real..."
    n "Hug my friggin’ sister, Ami. She’s waited years for this moment!"
    s "We should probably tell Niki that Ami very likely won’t ever let go. It’s hard enough for {i}me{/i} to get her off and she doesn’t sing any of my songs while she’s in the bath."
    n "I was unaware you had songs, Sensei."
    s "Yeah, well, now I guess you’ll have to come to my next band practice. "
    ni "They’re kind of ruining the moment, aren’t they?"
    a "I’m still...trying to figure out if...I’m going to wake up or not..."

    scene nikiami26
    with fade

    f "So...that rumor was...actually true?"
    f "Sensei...dated Niki?..."
    f "{i}The{/i} Niki?..."
    o "I didn’t believe it at first either, but...yup."
    o "She still talks about him all the time, too. "
    o "Granted, it’s in a pretty horrible way since all she does is complain...but they definitely dated."
    u "{size=-15}Great...{/size}"

    scene nikiami27
    with dissolve

    f "Well...I guess my self-confidence was bound to vanish again soon enough."
    o "Dude, no. You’re great. Don’t go letting this drag you down just because Niki has depressingly poor taste in guys."
    s "Hey. I heard that."

    scene nikiami28
    with fade

    ni "It must have been hard having to take care of your [uncle] for all those years, huh?"
    a "I can’t believe...this is happening..."
    ni "You did a great job, Ami. "
    ni "Even if he’s a horrible human being who left me on my own until just recently. "
    ni "And then ditched me to come to the beach with my little sister."
    ni "And never told me that we were literally right next to each other and that this reunion took much longer to happen than it had to."
    ni "But besides all of that, you did great."
    ni "You can cry as much as you want."

    scene nikiami29
    with dissolve

    a "{i}*Sniff*{/i}"
    a "Can you...move in with us?..."
    ni "Um...I don’t think that’s a very good idea."

    scene nikiami30
    with dissolve

    ni "But if your asshole [uncle] wants to finally tell me where he’s been hiding out all these years, I’d be happy to come over and see {i}you{/i} whenever I can!"
    ni "And let me clarify! I mean {i}you{/i}, Ami! Not him!"

    scene nikiami31
    with dissolve

    n "{i}Ooooooooh...you’re in troooooouble...{/i}"
    s "I’m pretty much always in trouble. It has become a staple of my everyday life."
    s "But that’s just how things work when everyone around you falls in love with you."

    scene nikiami32
    with dissolve

    n "Guess so."
    n "Those two are cute, though, huh?"
    n "It’s almost like Niki would rather have Ami as a sister than me."
    s "Seems like she’s playing more of a mother role right now."
    n "She really did worry, you know. I wasn’t kidding about that."
    n "I did too, of course. But it’s not like I was really old enough to remember {i}that{/i} much about Ami."
    n "I just always used to hear Nee-chan talking about you two...hoping that you two were able to be there for each other because you wouldn’t let us be there for you."
    s "…"
    n "That wasn’t fair, you know."

    if bonus == True:
        n "I understand that Ami’s your family...but you had more family than that. You had us."
    else:
        n "I understand that Ami’s been your accountant for a really long time...but you had more family than that. You had us."

    n "We were little angels back then. "

    if bonus == True:
        n "And if you played your cards right and waited until I was developed and stuff, I probably could have talked Nee-chan into a threesome. Lord knows I was ready for it."
        s "Oh. I thought this was going to be a sentimental moment. Now I’m just turned on."
    else:
        n "Or at least we would have been if we weren't vampires."
        s "What"

    scene nikiami33
    with dissolve

    n "Whoops~"
    n "Really, though. I’m glad we could be here to see this. "
    n "But aaaaaafterwards...if you’d want to go back to the inn-"

    scene nikiami34
    with hpunch

    ni "NORIKO! GET YOUR STUPID FUCKING HEAD OFF OF HIS STUPID FUCKING SHOULDER!"

    if bonus == True:
        n "What?! You’re interrupting my seduction!"
    else:
        n "(Aggressive hissing)"

    ka "Did...Did Niki just curse?..."
    to "Is she allowed to do that?"
    o "Oh man. You guys have no idea..."

    scene black
    with dissolve2

    "Niki manages to break apart from Ami much easier than I thought she’d be able to before making her way over to Noriko and demanding that she help her with her shoot."
    "Being unable to refuse as her sister’s part time employee or...helper or whatever Noriko’s unofficial title is, she submits and vanishes shortly after."
    "The rest of the girls disperse, but Ami remains standing in the exact place where she and Niki separated."
    "I look down to see her clasping something in her hands and, to my surprise, it’s a business card."

    if bonus == True:
        "However, I notice that it is distinctly different from the one she handed {i}me{/i} when we first “reunited,” confirming that Niki actually {i}is{/i} a demon and likes my [niece] more than me."
    else:
        "She is such an accomplished professional and strong career woman."

    s "Are you going to call her?"
    a "...Can I?"
    s "You can do whatever you want. Just know that she’s really busy most of the time."
    a "…"
    a "Sorry, Sensei...but I’m gonna go wash my face...I think I cried a little too much."
    s "Hm? Oh, sure. I’ll just...see you later then, I guess."

    "Ami takes off as well, leaving me alone on the sand despite knowing a grand total of twenty-four girls on the beach right now. "
    "I guess it’s a big beach, though. So I’m bound to run into-"

    mak "Sensei?"

    $ renpy.end_replay()
    $ secondbeach13 = True
    stop music fadeout 20.0

    "See what I mean?"
    "………"
    "……"
    "…"

    jump makotolust20intro

label makotolust20intro:
    scene makotolusttwenty1
    with dissolve

    mak "What are you doing out here by yourself? I could have sworn you’d have gotten roped into some type of breakfast shenanigans with some of the girls."
    s "Nah. There was just an emotional reunion between my [niece] and my ex-girlfriend who apparently really likes her despite only meeting her two or three times."
    mak "Ahh, yes. Your apparently super famous idol ex-girlfriend who would definitely show up to a local beach in the middle of winter for some sort of...cold gravure photoshoot. "
    mak "How completely believable and not at all something you’re saying to get a rise out of me."
    s "First off, that is exactly what happened and I didn’t realize how strange the whole photoshoot thing in winter was until you pointed it out."

    scene makotolusttwenty2
    with dissolve
    play music "behindabathroom.mp3"

    mak "So you admit that you were just messing with me?"
    s "What? No. That’s not even close to what I said. I’m trying to tell the truth."

    if bonus == True:
        mak "Were you also trying to tell the truth when you told the girls of Dorm #8 that I’m going around sleeping with janitors before they die?"
    else:
        mak "Were you also trying to tell the truth when you told the girls of Dorm #8 that I’m going around hugging janitors before they die?"

    mak "Or when you told Touka that I had a penis?"
    s "Nope. Those were lies."

    scene makotolusttwenty3
    with dissolve

    mak "Yes. I’m aware they were {i}lies.{/i} The point I’m attempting to convey is that you don’t exactly have the best track record when it comes to telling people the truth."

    scene makotolusttwenty4
    with dissolve

    mak "But...the whole Niki Nakayama thing has already been confirmed by several members of the class."
    mak "And also...I may or may not have seen her tour bus parked at the back entrance of the inn."
    s "Oh, okay. Well thanks for freeing up some time in your busy schedule to make me seem like some sort of pathological liar when you know I’m just a...normal liar."

    scene makotolusttwenty5
    with dissolve

    mak "Lucky for you, my schedule is floating around somewhere out in the ocean right now."
    s "That’s littering and you should be fined. Also, it would sink."

    scene makotolusttwenty6
    with dissolve

    mak "I didn’t mean it literally. I mean one of the girls stole it in the middle of the night and I have no idea where it went."
    s "And you didn’t have a backup? Shame on you, Makoto."
    mak "{i}Both{/i} of my backups were stolen as well, actually. As if I’d only have one. What kind of girl do you take me for?"
    s "The kind with a sudden overabundance of time and no one to spend it with."

    scene makotolusttwenty7
    with dissolve

    mak "Hm. I do believe there must be at least {i}one{/i} custodial worker at the inn. Perhaps they’d be willing to help me figure out what to do with all of this time?"

    scene makotolusttwenty8
    with dissolve

    mak "Or perhaps I could be a {i}real{/i} badass and skip breakfast altogether."
    s "Watch out, Yumi. There’s a new delinquent in[school]."
    s "Or...not in[school]. Because we’re at the beach."
    mak "Please stop talking."
    s "I can do that."

    scene makotolusttwenty5
    with dissolve

    mak "Well, since fate has done its part in pairing the two of us together while everyone else mysteriously vanishes, how about we do something together?"
    mak "I’d pull something from the itinerary, but alas. Ocean."

    if bonus == True:
        s "We could go back to the inn and I could finger you on the bed again. That was fun last time."
        mak "Unless you’re planning on doing it with Miku sleeping right next to us, that’s probably not a good idea."

        "I mean..."
        "It would...return the favor, at least?"

        s "Miku’s still asleep?"
        mak "She stayed up a bit too late playing video games with Sana and is currently the only one left in the room."
        s "Well, there are several other places I could finger you. It doesn’t really require a lot of space."
    else:
        s "Yup. That is definitely an ocean."

    scene makotolusttwenty9
    with dissolve

    mak "Perhaps I’ll go for a swim? That sounds fun."
    mak "Granted, I’m sure the water is still freezing despite this morning being a bit of a respite from the usual low temperatures."

    if bonus == True:
        s "Or, hear me out here, what about-"

        scene makotolusttwenty6
        with dissolve

        mak "Why do you want to finger me so badly? Aren’t you the one always trying to be {i}satisfied{/i}?"
        s "I have no idea what you're talking about. I am a nice guy who exists only to do nice things for all of you girls."
        s "Also, you look really cute in your swimsuit."
    else:
        s "Or, hear me out here, what about-"

        scene makotolusttwenty6
        with dissolve

        mak "Do you really need another loan to open a sandwich shop?"
        s "Just a small one this time so I can get the good salami."
        mak "Ugh."
        s "Will it help if I say you look pretty?"

    scene makotolusttwenty2
    with dissolve

    mak "And you look...average in your average clothes. "
    s "I can not be blamed for expecting it to be cold again today. It’s cold every day. "

    if makoto_lust >= 20:
        jump makotolust20
    else:
        mak "Well...how about this then?"
        mak "You can walk with me back to the inn and change into your swimsuit, assuming you brought it."
        s "I did not."

        if bonus == True:
            mak "Then you can walk with me back to the inn because you’re bored and having nothing else to do."
            mak "And if you manage to convince me that having some form of sex with you is a good idea along the way, I’ll see what I can do."
            s "Deal."
            s "If there’s anything I’m good at, it’s convincing girls to have sex with me."

            scene makotolusttwenty10
            with dissolve

            mak "Wow. You’re...not even hiding it anymore."
            s "You’ve made it very apparent you already know."
            mak "Yes, but I’d still appreciate a bit of tact. "
            s "I don’t have time for tact, I have to start convincing you to let me into your pants because the inn isn’t that far away."
            mak "Hah...whatever."
            mak "Just..."
            mak "Whatever."

            scene black
            with dissolve2

            "Makoto and I begin walking back to the inn and I do everything in my power to turn her on."
            "Nothing works."
            "I don’t know if it’s {i}because{/i} of the whole thing about mentioning other girls, but I can definitely see why that wouldn’t have helped."
            "I don’t really care, though."
            "Even if Makoto and I aren't doing anything sexual together, I'm still able to kill a little bit of time."
            "She breaks apart from me and goes back to check on Miku, while I take a few moments to get some extra rest in my {i}own{/i} room since last night was kind of...exhausting."
            "Unfortunately, I wind up falling asleep for a couple hours."
            "And by the time I go back outside, the sun has already begun to set..."

            $ renpy.end_replay()
            $ makotolust20skip = True
            stop music fadeout 5.0

            "{i}Makoto’s lust does not increase because you couldn't convince her to have sex with you!{/i}"
            "{i}Haha! You suck!{/i}"
            "………"
            "……"
            "…"
            "…"
            "…"
            "I miss feeling whole."

            jump secondbeach14
        else:
            mak "Then we can go buy one."
            s "So the loan for the salami is bad but the swimsuit is okay? You make literally no sense to me."
            mak "Shut up and accept the swimsuit, Sensei."
            s "Fine. But only because I want to feel the sensation of the cold air against my belly button."
            mak "Stop making everything ever weird."
            s "No."

            scene black
            with dissolve2

            "Makoto and I go to the swimsuit store and I buy a really cute one piece to try on while I am home alone."
            "I'm going to look so cute."

            $ renpy.end_replay()
            $ makotolust20skip = True
            stop music fadeout 5.0

            "……"
            "…"
            "…"
            "…"

            jump secondbeach14

label makotolust20:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
s "Can I just quickly touch on the fact that you two have an absurd amount of rules? What does rule #74 even do?"

    scene norikowakeup24
    with dissolve

    nni "Nakayama Sisters’ Rule #74: If a Nakayama sister believes the other is making a decision they will regret, they can enact this rule to strip them of free will and force one to act for the other."
    s "Okay, first off- you two are creepy."
    s "Secondly, how old were you when you came up with that? I thought this was going to be a kid thing at first, but that was a very professionally worded rule."

    scene norikowakeup25
    with dissolve

    ni "It’s more like a law, I guess. But it wouldn’t exist if there wasn't a reason for it, so..."
    ni "If Noriko is going to enact Rule #74 now, I don’t really have a choice other than to go along with it."
    s "Having a sister sounds exhausting."
    nni "It is."

    scene norikowakeup26
    with dissolve

    nni "Pfft..."
    s "...?"

    scene black
    with dissolve2

    "The Nakayama sisters erupt into a fit of laughter as I am left to stand beside them, wondering how far back this goes and whether or not it’s something I ever found out about."
    "Perhaps in a previous life-"
    "Perhaps then, I would have understood more about their silly rules."
    "About what their relationship is with not only each other, but with me and the girl Niki was apparently so worried about for years."
    "It must have been hard having to live with those thoughts."
    "I wonder why, if that person from back then was actually me-"
    "I wonder why they locked her out."
    "She seems kind enough."
    "Sure, she’s a stuck up princess but, if what I understand about her is correct, isn’t she only like that because of me?"
    "If so, why did I leave her behind?"
    "Everything I learn about those two makes the past seem brighter-"
    "But perhaps the issue is that it’s becoming so bright that it’s too blinding to see anything else."
    "And perhaps the reason Maya is so hesitant to me finding out any more about it is because its inescapable light will consume the world I’m in now."
    "Maya is in that world, so I don’t blame her for not wanting to be consumed."
    "But I also shouldn’t be blamed for occasionally quelling the misery of others when it requires minimal effort on my end in order to do so."
    "All I’m doing is walking down the beach with two cute girls who love me."
    "Well, one cute girl who loves me and one other cute girl who hates me."
    "But also loves me."
    "Probably."
    "And if the three of us happen to bump into one more girl who loves me-"
    "One more girl who goes back just as long as the two of them, if not longer-"
    "If that happens, it will just be a coincidence."
    "It will not be my fault."
    "Nothing is ever my fault."

    scene norikowakeup27
    with dissolve

    n "Onward! To [niece]hood!"
    ni "Are you really just going to let her pull you along like that?"
    s "I...guess so?"

    scene norikowakeup28
    with dissolve

    ni "Hah...you’ve always been too nice to her. You just let her do whatever she wants."
    ni "No wonder she’s this obsessed with you now instead of chasing after someone actually worth the time and effort."
    s "Sorry, but aren’t you the same Niki Nakayama who tried to invite me on a work trip because she couldn’t get enough of me?"

    scene norikowakeup29
    with dissolve

    ni "Of course not."
    ni "I’m the Niki Nakayama who tried to invite you on a work trip because I didn’t want to carry my own luggage."
    ni "But it’s fine now. I just got one of the people from the agency to do it instead. I don’t need you anymore."
    s "Then I guess I’ll just go back to enjoying my romantic getaway with your little sister and-"

    scene norikowakeup30
    with dissolve

    ni "Yeah, yeah. Do whatever you want. I know you’ll come crawling back soon enough."
    ni "Just keep on walking, [nikitemp]. You have a grand total of roughly ten minutes with me and you shouldn’t be wasting them on your textbook sarcasm."
    s "..."

    scene black
    with dissolve2

    "I begrudgingly do as I’m told and shut my mouth, though I’m not sure why."
    "We continue walking along the shoreline together until the entrance of the beach and its accompanying picnic tables come into view."
    "And in the hundreds of seconds it takes to get there, not one feels out of place."

    $ renpy.end_replay()
    $ niki_love += 1
    $ noriko_love += 1
    $ secondbeach12 = True
    stop music fadeout 5.0

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "………"
    "……"
    "…"

    jump secondbeach13
...
```