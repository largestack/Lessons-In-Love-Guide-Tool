# A Thing of the Past (Yuki)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Opposite Directions](./yukidate10.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Sara: Tell Me When](./sarabar25.md)

## Event properties

* Id: yukidate10p2
* Group: Yuki
* Triggered by label: yukidate10
* Chain sources: yukidate10
* Chain sources path: yukidate10

## Official wiki page

[A Thing of the Past](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yukidate10p2&go=Go) for more details.

## Event code

File: (install folder)\game\YukiEvents.rpy

Code:
```python
...
label yukidate10p2:
    scene yukiconvenience1
    with dissolve2

    yu "So, what do you want? Choose any one food item in the store and it’ll be my treat for pretending to help me tonight."
    s "Hey, for all you know, I successfully distributed roughly one hundred fliers just now. Who says I was pretending?"
    yu "Only way you could have actually handed off that many bar ads in just a few minutes is if you just conveniently waltzed into the world’s largest AA meeting."
    s "I think that’s the sort of place that’s supposed to make it {i}harder{/i} to hand out bar ads."
    yu "Yeah. You’d {i}think{/i} that. Sad truth is that half the people that go to those meetings are ready to jump on the first fuckin’ excuse they can think of to relapse."
    yu "Take it from someone who has experience, kid."
    s "I don’t know how I feel about being called “kid” when I’m only a few years younger than you."
    yu "Right, right. My b. Just keep seein’ that baby face of yours and thinking you’re only a little older than my daughter."
    s "My face is not childish and I would greatly appreciate it if you’d take that back."
    yu "And I’d {i}greatly appreciate it{/i} if you’d get a fuckin’ move on and pick your poison already before the people workin’ here think I’m stealin’ shit."
    s "…"
    s "{i}Are{/i} you stealing shit?"

    scene yukiconvenience2
    with dissolve

    yu "What? No. Obviously not."
    s "I don’t think it’s obvious if you said yourself that people are going to be assuming that-"
    yu "I have a job now, man. I don’t have to steal shit."
    yu "Remember? I pay bills. I’m a normal person. All that gang shit’s a thing of the past as of a little while ago."
    s "You can’t even name all of your bills yet. "
    yu "Well, forgive me for not fuckin’ memorizing ‘em. "
    yu "You have any idea what the longest time I’ve held down an apartment is? Go on. Take a guess."
    s "I feel like anything I guess here is bound to offend you."

    scene yukiconvenience3
    with dissolve

    yu "Three months."
    yu "In all fairness, it should {i}probably{/i} be two. But I’m pretty sure the owner of the place I’m talkin’ about was too scared to remind me that I actually needed to {i}pay{/i}."
    s "How do you keep finding living arrangements with such a horrible track record as a tenant?"

    if bonus == True:
        yu "How do you keep finding preppy girls with perky tits ready to jump your bones despite being twice their age? Just happens. Best not to question any of it."
        s "I’m glad to hear you’ve been...paying attention to my students’ chests?"
    else:
        yu "How do you keep finding cute girls who want to hug you and shit?"
        s "How do you know they're all cute? They could be hideous. Or even worse, old."

    yu "They’re fuckin’ teenagers, man. Their bodies ain’t had time to get all mature and saggy and shit yet. Just safe to assume, you know?"
    s "At the risk of you hitting me, I’d like to say I wouldn’t go as far as describing you as “mature and saggy.”"

    scene yukiconvenience4
    with dissolve

    yu "I’d sure fuckin’ hope not."

    scene yukiconvenience5
    with dissolve

    yu "Might not be the same as they were back when I was Yumi’s age, but there’s still some life left in these things for now."
    yu "Maybe cause I’ve been goin’ to the gym? "
    yu "I don’t know. What do you think?"
    s "Uhhhhhhhh..."

    scene yukiconvenience6
    with dissolve

    yu "Sup?"
    s "Not...much? I just didn’t expect you of all people to wind up groping yourself in the middle of a convenience store."
    yu "Wanna cop a feel yourself?"

    if bonus == True:
        s "There is no way this isn’t a trap."
    else:
        s "No thank you, madam."

    scene yukiconvenience7
    with dissolve

    if bonus == True:
        yu "Oh, stop. It’s not like I was planning on putting you in an arm lock the second you reached for my chest or anything. That would have just been rude."

    "I take a moment to thank my intuition and self control for at least improving in...some sort of way recently."

    yu "Color me surprised, man. You normally don’t waste any time at all when it comes to hittin’ on me for whatever reason."
    yu "And here I was actually givin’ you a chance, only for you to pussy out. You’re all talk after all, ain’t ya?"
    s "I’m definitely not all talk. You’re just being suspiciously handsy and surprisingly flirty for someone who’s apparently not interested in romance or sex or anything."

    if bonus == True:
        s "Well, apart from keeping me at the top of your secret sex list, I mean."

    scene yukiconvenience8
    with dissolve

    yu "Handsy? The fuck you talkin’ about?"
    s "Probably the hand you’re repeatedly tapping me with."
    yu "That’s just me fuckin’ with you, dude. Just because a girl touches you doesn’t mean she’s tryin’ to sleep with you."
    s "Sure. Just like how girls who pick on boys in school by pushing them around on the playground don’t actually have crushes on whoever they’re bullying."
    yu "I didn’t, at least. I used to pick on kids just for lookin’ weird and shit."

    "Is bullying just a genetic trait for the Yamaguchi family or something?"
    "Well, I guess Yuki’s maiden name would be something different...but I’m not really in any rush to figure out whatever it was."

    scene yukiconvenience9
    with dissolve

    yu "There. Do you feel a little safer now that the big, bad ex-biker lady isn’t trying to take your lunch money?"
    s "The fact that you were offering to buy me dinner just a minute ago is making this sudden roleplay thing a little harder to follow."
    yu "{i}Still{/i} offering. Just waiting for you to fucking pick something instead of waiting for me to keep “flirting” with you. "
    s "But the flirting is so much more fun."
    yu "Maybe if it was actual flirting and not just two friends going on a late night sandwich run after work."
    s "This late night sandwich run is probably the closest you’ve been to being on an actual date literally ever."

    scene yukiconvenience10
    with dissolve

    yu "Yo! That ain’t even remotely-"

    scene yukiconvenience11
    with dissolve

    yu "...true?"
    s "…"
    s "You seem confused."
    yu "Hold on. I’m tryin’ to think."
    yu "…"
    s "…"
    yu "Well, shit. I think you’re right."
    yu "I’m sure there were some in the past, but either I was too fucking high to remember ‘em or they just weren’t worth rememberin’ in the first place."

    scene yukiconvenience12
    with dissolve

    yu "So now what? Wanna hold hands or somethin’? Take turns tellin’ each other what we like about each other?"
    s "…"

    if bonus == True:
        s "Is the opportunity to grope you still on the table?"
    else:
        s "One hug, please."

    scene yukiconvenience13
    with dissolve
    play sound "entrybell.mp3"

    if bonus == True:
        yu "Only if you don’t mind gettin’ your dick ripped off the second you try."
    else:
        yu "How about we just go beat up some old people instead?"

    s "Like mother, like daughter, I guess..."
    y "Wha-"

    scene yukiconvenience14
    with fade

    s "Uh-oh."
    yu "Yumi..."
    y "…"

    "It appears that yet another unfortunate coincidence has befallen me once again."
    "Well, I suppose it’s not really unfortunate for {i}me{/i}. At least not yet."
    "I’m sure the inevitable fallout of this will result in Yumi’s problems finding a way to bring me down in one way or another."
    "But, on the bright side, this might actually be kind of {i}convenient{/i} for Yuki if she ever plans on patching things up with her daughter."
    "She just needs to make sure she doesn’t do anything to set her off during what I expect will be an incredibly short conversation."

    y "…"
    yu "…"

    "Or...maybe not even a conversation at all?"

    s "...I’ll be the one to talk, I guess."
    s "Hi, Yumi."

    scene yukiconvenience15
    with dissolve

    y "Yeah. {i}Hi.{/i}"
    y "Would you mind explaining what you’re doing all the way in bumfuck nowhere with {i}her{/i}?"
    s "This is the most populated part of the city and you have weird criteria for what constitutes “bumfuck nowhere.”"
    s "As for why I’m with {i}her{/i}-"

    scene yukiconvenience16
    with dissolve

    yu "We’re on a date."

    "Oh no."

    s "{i}What are you doing?{/i}"
    yu "Hm? Flirting, obviously."
    y "You expect me to believe that {i}you two{/i} are on a date?"
    y "Even this guy, who’s one of the scummiest people I’ve ever met, would have to be drunk out of his fucking mind to even {i}consider{/i} going on a “date” with someone like you."

    scene yukiconvenience17
    with dissolve
    stop music fadeout 20.0

    yu "Maybe he just likes girls who are a little rougher around the edges? Don’t ask me, ask him."
    s "Don’t ask me. We are not on a date and I have no idea why she is doing this."
    yu "Oh, come on. You could have at least played along a {i}little{/i}."

    if bonus == True:
        s "I’m already on thin ice with Yumi. The last thing I need is her thinking I’m screwing her mother when I {i}definitely am not.{/i}"
    else:
        s "I’m already on thin ice with Yumi. The last thing I need is her thinking I’m hugging someone evil."

    scene yukiconvenience18
    with dissolve

    y "Great. Consider yourself lucky then for not catching one of the millions of STDs the world’s greatest mom over here is carrying."

    if bonus == False:
        "Oh no. Can you catch those from hugging?"

    s "Okay, Yuki was clearly in the wrong with pretending to date me, but-"
    yu "Nah, she’s right. Well, apart from the STD thing. I deserve whatever she throws at me. "
    yu "Besides, this is the first time she’s said anything to me in years. I’ll take what I can get."

    play music "undersea.mp3"

    if yumiknows == True:
        y "What you can {i}get{/i} is the fuck away from my teacher who, coincidentally, also happens to be {i}dating my best fucking friend.{/i}"

        scene yukiconvenience19
        with dissolve

        if bonus == True:
            yu "Wait, you never told me that."
            yu "I thought you were fucking Yumi?"
        else:
            yu "Wait, you never told me that."
            yu "I thought Yumi was you huggy buddy."
    else:
        y "What you can {i}get{/i} is the fuck away from my teacher, you dumb bitch."
        yu "{i}Just{/i} your teacher?"
        s "Yuki, no."
        y "Well, what else would he fucking be?"

        if bonus == True:
            yu "Beats me. I just thought you two were screwing or something."
        else:
            yu "I thought he was your hugging partner."

    scene yukiconvenience20
    with dissolve

    y "You thought fucking {i}what?{/i}"
    yu "Well...yeah. Because I’ve seen you two around together and...I don’t know. I just kinda figured there was some shit goin’ on."
    yu "Sensei always told me that wasn’t the case, but I kinda just figured that was because I’m your mom and that would make shit real awkward for him."
    y "Are you fucking kidding me?"
    yu "What? It’s a misunderstanding. It’s not a big deal."

    scene yukiconvenience21
    with dissolve

    yu "But, uhh...apart from that..."
    yu "You...got taller?"
    y "Yeah. It’s a little known fact, but most kids continue growing once their parents walk out on them."
    s "Okay, I’m just...gonna...go over there."

    scene black
    with dissolve

    "Yuki lets go of my collar and I quickly make my way over to the magazine rack to make it look like I’m...doing anything but being involved in this discussion."
    "And while I’d like to say it will only be a matter of time until one of the staff breaks things up (Which probably {i}should{/i} be my job), it looks like the only person working really doesn’t want to get involved."
    "And I don’t blame them. Neither Yuki nor Yumi look particularly friendly...especially when they’re at each other’s throats."

    $ renpy.end_replay()
    $ yukidate10p2 = True
    jump yumispecial40
...
```

## Code that triggers this event

File: (install folder)\game\YukiEvents.rpy

Code:
```python
...
yu "For real, though. Is she like...{i}okay{/i} to function in the real world? Cause I ain’t one to really talk when it comes to shit like that, but I feel like even {i}I’ve{/i} got a leg up compared to her."
    s "She actually functions really well apart from frivolously spending roughly 90%% of her income on trying to free animals. "
    s "I’m pretty sure she’s simultaneously holding six thousand jobs- and you’re somehow only holding {i}one{/i}."
    s "So maybe you should be taking pointers from her, Yuki?"

    scene yukiflier20
    with dissolve

    yu "Hm. You know, when you put it like that, yeah. I guess maybe I could be taking some pointers from her?"
    s "I...wasn’t really being serious. Kaori is an enigma and I don’t think it would be a good idea for any of us to try and live our lives the same way she lives hers."

    scene yukiflier21
    with dissolve

    yu "I’m just glad she’s okay. "
    yu "If my daughter’s not gonna fuckin’ acknowledge my existence, I guess a niece doing it is like...the next best thing."
    yu "‘Sides, Kaori seems actually kind of excited to have someone she can call family. Even if she’s adding fucking “burger” onto the end of my name."
    s "Well hey, maybe one day, all {i}three{/i} of you can sit down and...do whatever it is the three of you did when you were younger."
    yu "Yeah. And maybe I’ll win the lottery and get elected prime minister of Japan as well."
    yu "Don’t feel the need to provide hope where there ain’t none, man. "
    yu "There’s some shit that stays broken forever once you’ve fucked it up...and no amount of glue or...tape, or...any other sticky shit can put it back together."
    yu "What really surprises me, though, is that Yumi doesn’t want to see her."
    yu "The two of them weren’t like...{i}inseparable{/i} or anything like that back then, but she’s one of the few people I’ve actually seen who was able to make her smile."
    yu "...heh. She had a real cute smile back then, too. The kind where there’d be like, missing teeth and shit. But in a “kid” sort of way. Not like a...gross sort of way."
    s "You have such a way with words sometimes."

    scene yukiflier22
    with dissolve

    yu "Right, right. Which is exactly why you had such an issue with what I decided to put on all of our fuckin’ fliers."
    s "Speaking of which, aren’t you supposed to be passing those out?"

    if bonus == True:
        yu "What, am I not allowed to take a fuckin’ break to hang out with the dude at the top of my secret sex list?"
    else:
        yu "Yeah, but I'm allergic to paper and holding them for so long is starting to make my throat close up."

    s "I {i}knew{/i} it. "
    yu "It was a joke, asshole. "
    yu "I don’t care if you’re Yumi’s new dad or...sugar daddy or whatever the fuck you are-"
    s "I believe it’s pronounced “teacher.”"
    yu "Sure, let’s go with that."
    yu "What I’m sayin’ is I don’t care what your role is. I’m just glad I’ve got someone like you to hang around who actually feels like a decently good person."
    yu "That shit’s hard to come by."
    s "I feel like you are, once again, gravely misinterpreting the kind of person I am."
    yu "Am I?"
    s "Absolutely. And this isn’t me just being a self-loathing piece of shit again- that’s what inner monologues are for."
    yu "Uh-huh. Right."
    s "What I’m saying is that you can’t really judge a person by just...how they act around you. You need to think about what’s underneath the surface as well."
    s "You barely know me. Have I been mostly kind to you? Sure. But what about how I treat other people? "
    s "What about how I treat Yumi?"
    yu "You mean when you’re paying her phone bill and taking her job hunting? Yeah, you sound like a real douche."
    s "No, Yuki...that’s not what I mean."

    if bonus == True:
        yu "Then...you mean like when you’re boning her?"
    else:
        yu "Then...you mean like when you’re hugging her?"

    s "You know what? I feel like getting into a philosophical debate right now probably isn’t the best thing for either one of us."
    s "Just know that I’m not as great as you think I am."
    yu "Oh, I don’t think you’re great at all."
    yu "I’m sure you’ve done plenty of shit that you regret- but we’ve all got stuff like that."
    yu "You think I look back on all of the mistakes I’ve made and just shrug them off because I’m like...above them now or something? Course not."
    yu "I think I’m the fuckin’ scum of the earth. And I’m sure you feel the same way about yourself most of the time."
    yu "But those thoughts are our own, man. You’ve gotta look at shit from the outside."
    yu "You obviously don’t think I’m fucking Satan. If you did, you wouldn’t be helping me out all the fuckin’ time."
    yu "So I can think whatever the fuck I want about you and you can’t do shit about it."
    yu "We can hate ourselves as much as we want inside of our heads, but until we go out there and show {i}every single person in the fucking world{/i} that we’re against them-"
    yu "There are going to be some people who are just...on our side for no reason whatsoever."
    s "…"
    yu "What? I’m older and more experienced than you. Don’t tell me you’re surprised to hear some words of wisdom out of me?"
    yu "Now, help me figure out what to do with the rest of these fliers. And don’t suggest that I just throw them out or whatever. The more customers Sakaki-bar-a gets, the more I get paid."
    s "Can we just go back to calling it “the bar” please? I get irrationally angry each time I remember the real name."
    yu "We can do whatever the fuck you want as soon as we finish handin’ these out. "
    yu "Here-"

    scene black
    with dissolve

    "Yuki hands me roughly half of her stack of fliers and the two of us set off in opposite directions to...distribute them, I guess."
    "I don’t really know how I allowed myself to get roped into this, but it is what it is."

    if sarasex == True and bonus == True:
        "It’ll make Yuki happy-ish, and I’d be lying if I said I didn’t want to at least {i}try{/i} helping Sara after all of the free drinks (And blowjobs) she’s given me."
    else:
        "It’ll make Yuki happy-ish, and I’d be lying if I said I didn’t want to at least {i}try{/i} helping Sara after all of the free drinks she’s given me."

    "I do my best to hand them out to people, but “my best” only survives for a matter of minutes before being brutally murdered in the form of me stashing my entire pile in a nearby shoe store."
    "But hey, my job was to get rid of all of my fliers without throwing them away, and that is precisely what I did."
    "I send Yuki a text to figure out where she is and whether or not she wants to continue hanging out after she’s done with “work.”"
    "Fortunately, she also found a shoe store to offload her fliers in, and the two of us reconvene at our original meeting spot and decide to head to a nearby convenience store for dinner."
    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ yuki_love += 1
    $ yukidate10 = True
    jump yukidate10p2
...
```