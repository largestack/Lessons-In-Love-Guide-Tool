# Dyed Orange, Drenched in Sun (Kirin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [That One FMK Scene](./convenience25.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: kirinspecial25
* Group: Kirin
* Triggered by label: convenience25
* Chain sources: convenience25
* Chain sources path: convenience25

## Official wiki page

[Dyed Orange, Drenched in Sun](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=kirinspecial25&go=Go) for more details.

## Event code

File: (install folder)\game\KirinEvents.rpy

Code:
```python
...
label kirinspecial25:
    if kirinmarry == True and norikokill == True:
        scene kirinfire1
        with dissolve2
        play music "starvingtodeathoutofreachofthesun.mp3"

        ki "What the fuck did you just do?! I gave you the perfect chance to make Noriko happy and you went and fucking did {i}that?{/i}"
        ki "How long has she liked you for again? Half of her life? More? "
        s "I’m surprised you don’t remember since it’s all she ever talks about."
        ki "Why would you do that?! Chika’s not even fucking here! Just {i}lie{/i} and make Noriko happy. Since when are you opposed to lying?"

        scene kirinfire2
        with dissolve

        ki "Actually, that can’t even be the problem since you had no issue lying about what you’d do to {i}me{/i} as well!"
        ki "It’s like you intentionally picked the worst fucking outcome for everybody."
        s "Do you actually believe that? Or are you just saying it because you’re afraid of a future where you and I are more than...this?"

        scene kirinfire3
        with dissolve

        ki "How do you not realize by now that you and I are not the type of people who end up in...make believe fantasy bullshit relationships like {i}that?{/i}"
        s "You’re a [teenage]girl. You know nothing about how you’re going to “end up.”"
        ki "Maybe. But I {i}do{/i} know that going out of your way to hurt people makes you a shitty person. And if that’s what you did to Noriko, you’re even worse off than I thought you were."
        ki "Is she not broken enough for you? Do you want to cut her down before you fuck her? Is {i}that{/i} why it’s taking so long? She’s not sad enough yet?"
        s "It was just a game, Kirin."

        scene kirinfire4
        with dissolve

        ki "...Right."
        ki "It was just a fucking game."
        ki "None of it ever happened. "
        ki "Noriko will be fine...I will be fine...everyone will be fine."
        ki "Shit will go back to normal and you’ll remember that I’m just the girl you’re supposed to fuck and Noriko is the girl you’re supposed to actually care about."
        s "If that’s what makes you happy."

    if kirinmarry == True and norikokill == False:
        scene kirinfire5
        with dissolve2
        play music "starvingtodeathoutofreachofthesun.mp3"

        ki "How can you marry me and not Noriko?! "
        s "You’re still freaking out even now that she’s gone?"
        ki "Yes! Because I still don’t get it!"
        ki "Even with...both of us being shitty people or whatever! That...That doesn’t mean that we’d be happy as anything more than fuck buddies!"
        ki "Relationships are complicated! And weird! We’d have to like...make each other breakfast and...and buy each other presents or something! I don’t know!"
        ki "Take it back! I feel gross now!"
        s "Kirin..."
        s "Will you-"

        scene kirinfire1
        with dissolve

        ki "No! I will fucking not! And it’s not even funny to joke about shit like that!"

        scene kirinfire6
        with dissolve

        ki "You were supposed to marry {i}her{/i}, dude. Not me. I thought you would have realized that."
        ki "Now shit’s gonna be weird and she’s probably going to think you like me more than her or whatever."
        s "Well..."
        s "What if I do?"

        scene kirinfire7
        with dissolve

        ki "…"
        s "…"

        scene kirinfire8
        with dissolve

        ki "Then you keep it to yourself and don’t let either of us know."
        s "Oh."
        s "Then yeah. I guess that was a pretty bad move, then."
        ki "…"
        s "…"

    if norikokill == True and kirinmarry == False:
        scene kirinfire9
        with dissolve2
        play music "starvingtodeathoutofreachofthesun.mp3"

        ki "I know that being an asshole is kind of your thing, but don’t you think that might have been a bit much?"
        s "How so?"
        ki "You just told a girl that has been pining after you for half of her fucking life that she wasn’t even good enough to fuck and dump. Why?"
        ki "And don’t go saying some stupid shit about how you just wanted to be honest, because you are 100%% {i}not{/i} the type of person to do that when lying would bring you closer to someone else."
        s "It’s just...what I chose. "
        ki "…"
        s "…"

        scene kirinfire10
        with dissolve

        ki "You’re a fucking idiot."
        ki "I gave you the perfect set-up. I legit said “Hey, this is Sensei’s chance to exonerate himself” and you went and still fucking {i}married{/i} Chika anyway."
        ki "Married. Not just fucked. You {i}married{/i} her. In front of Noriko. {i}Noriko.{/i} Who fucking {i}loves{/i} you."
        s "That’s a lot of emphasis in such a short batch of sentences, Kirin."

        scene kirinfire11
        with dissolve

        ki "Yes! Yes it is! Because {i}apparently{/i}, you don’t have any fucking common sense anymore and I have to literally spell shit out for you to get you to understand!"
        ki "Do what you do best and fucking {i}lie{/i} if the truth is going to hurt someone! L-I-E. "
        s "It’s just a game, Kirin. Relax."

        scene kirinfire12
        with dissolve

        ki "Maybe for you and me. But for Noriko, it was more than that."
        ki "It was such an easy way to show her that, even if it’s just a little bit, she has a chance."
        ki "But to have you fucking kill her in the first pairing of three girls that was thrown out?..."
        s "…"
        ki "…"
        ki "This is exactly why I fucking hate love."

    if norikomarry == True and chikakill == True:
        if bonus == True:
            scene kirinfire13
            with dissolve2
            play music "starvingtodeathoutofreachofthesun.mp3"

            ki "You know, for a second there, I was worried that you were going to pick something else."
            s "I figured that fucking you and marrying Noriko would give everyone what they want most."
            s "Well, except for Chika. But it’s not like she’s really around to hear about her impending doom."
            ki "So, what position are we going for tonight? I accidentally left my underwear at home, so that opens up a lot of discreet, fully-clothed options."
            s "Choosing you for the fuck option wasn’t me saying “Let’s do it right now, Kirin.”"
            ki "Why not?"
            s "There is a flaming pile of trash behind you and I’m pretty sure we stepped over at least three dead rats on the way here."
            ki "Are you not turned on by dead rats?"
            s "...Are you?"

            scene kirinfire14
            with dissolve

            ki "Nah. But I {i}am{/i} turned on by dudes with huge dicks who tell me they want to fuck me in front of my roommate."
            s "I hope you’re specifically talking about me and that that isn’t just a blanket statement applicable to all well endowed men."

            scene kirinfire15
            with dissolve

            ki "Oh? Are you actually getting jealous thinking about me with someone else this time?"
            ki "Am I finally a slightly important figure in your life, [kirinmaster]?"
            s "Of course. Who else am I going to have sex with after I marry Noriko?"
            s "You’re the permanent threesome enabler and I must use the power I have to keep you locked into that role for the foreseeable future."

            scene kirinfire16
            with dissolve

            ki "Welp, I’m ready whenever she is. So that’s something you’re going to have to take up with her."
        else:
            ki "Did you like my super secret soda throwing move?"
            s "No. But seeing as I am clearly the best when it comes to playground games, I understand why you needed to employ such a dirty tactic."
            s "Also, where did Noriko go?"
            ki "She got upset about not knowing how to play hopscotch and is currently inside researching how to do it properly for next time."
            s "Is there going to be a next time?"
            ki "Sure is. So you better start figuring out how to dodghe soda cans now, mister."
            s "Tch."

    "I crack my knuckles and stare at the fire for a moment."
    "The light emanating from it attacks the back of Kirin Kanda and not only duplicates her figure onto the grease soaked wall behind me, but increases her size by triple or...even quadruple what it normally is."
    "Not like she’s all that large to begin with."

    if bonus == True:
        "I can still carry her in my arms if I want...or slam her body up against the tiled walls of a convenience store bathroom before fucking her and contracting some sort of infectious disease."
        "Not from Kirin, of course. From the bathroom."
        "Though, I’m sure she’d catch the same thing if we’re both...yeah."
    else:
        "In fact, she is just the right size for hugging."

    "Anyway, I tilt my neck to the side and focus on her colossal silhouette, dyed orange by the flames a probable anarchist lit before I arrived."

    if bonus == True:
        "I picture a life in which a twenty foot tall Kirin roams the streets of Kumon-mi, masturbating in public and turning into a legendary figure admired by all men and feared by all parents."
        "Except the male parents."
        "And lesbian/bisexual female parents."
        "I think of a lot of strange things when I don’t know what else to do with my time."
        "And Kirin’s sudden transition into silence has forced me into a position where that is just...what I have to do now."
    else:
        "I picture a life in which a twenty foot tall Kirin roams the streets of Kumon-mi, trying to get everyone to watch the third season of Seinfeld."
        "An ominous bass line plays behind her as she crushes building and asks passersby {i}what's up with that?{/i}"

    ki "…"
    s "…"

    "I wonder if she’s thinking of a twenty foot tall version of me."
    "But then I realize she isn’t."
    "That would be weird."

    scene kirinfire17
    with dissolve

    ki "So..."
    ki "Did you want to maybe like...walk back to the dorms together or something?"
    s "Right now? No. I’m still recovering from the walk over here."
    ki "Let me guess- you didn’t want to ride the bus because of all of the weird people on there this time of night?"
    s "Leave it to you of all people to understand me."
    ki "{i}Nobody{/i} likes riding buses at night, dude. Being one of those people doesn’t make you unique."

    if bonus == True:
        s "You’re right, Kirin. I’m just a normal guy with normal interests and a normal sized penis."

        scene kirinfire18
        with dissolve

        ki "If {i}that thing{/i} was normal sized, it would definitely explain Japan’s declining birth rate."
        s "Is that why you cried when you went back home after the love hotel? It was too big?"
    else:
        s "Yeah, well at least I don't cry after I lose at bowling."

    scene kirinfire19
    with dissolve

    ki "I didn’t...fucking...cry. I had allergies."
    ki "There must have been fucking...bed bugs or something. Dust? It was just a reaction."

    if bonus == True:
        s "Right, right."
    else:
        s "At a bowling alley? Yeah right."

    s "But yeah, if it’s not a problem, I’d like to stay out here for a little while longer. Even if there are bugs and...dead rats everywhere."

    scene kirinfire20
    with dissolve

    ki "Honestly, it skeeved me out the first few times I was here, too. But, after a while, you kinda get used to stuff like this."
    ki "I don’t really mind hanging out in places this gross so long as I’m with people I find interesting. And you and Noriko are pretty much as interesting as they come."
    ki "Karin, on the other hand...I doubt she’d last even a second over here."
    s "Yeah, she...definitely doesn’t seem like the type to...{i}indulge{/i} in urban alleyways."

    scene kirinfire21
    with dissolve

    ki "She’d probably rat me out to our parents if she even knew I was here."
    s "Was that an intentional “rat” pun or should I continue being unimpressed?"

    if bonus == True:
        ki "Continue being unimpressed, please. The less you like me, the harder you’ll fuck me."
        s "Is that how it works?"

        scene kirinfire22
        with dissolve

        ki "Beats me. You’re the one with the dick."
        ki "I just figured that like...hate sex is a thing. And romantic sex is probably more gentle or something."
        s "I don’t really think how much you like someone dictates how aggressive or violent sex with that person is."
        ki "Are you telling me that we live in a world where gentle hate sex exists?"
        s "Well...probably not."
        ki "Good. That’s not a world I’d want to live in."
        s "But you can be romantic and violent. Probably."
        s "I don’t know, Kirin. I just want to confirm that I have no intention of being gentle with you any time soon and that you shouldn’t worry about that happening as a result of us getting closer."
    else:
        ki "Continue being unimpressed, please. My sister is actually really nice and she deserves a chance to hug you as well."
        s "I'll add her to the hug list and let you know how things go."

    scene kirinfire23
    with dissolve

    ki "Works for me."
    ki "Now what, though?"

    if bonus == True:
        ki "We’re not having sex and we’re not walking home to {i}have{/i} sex. Does this mean we’re supposed to actually like...{i}talk{/i} to each other?"
        s "Are we about to challenge ourselves to have a full length conversation without bringing up sex?"

        scene kirinfire24
        with dissolve

        ki "Ew. Why would we ever do that?"
        s "Just to see if we can, I guess?"
        ki "Uhhhhhh..."
    else:
        ki "We're done playing hopscotch and we’re not walking home. Does this mean we’re supposed to actually like...{i}talk{/i} to each other?"
        s "I think that sounds great. Getting to know each other better is a wonderful opportunity that we should both savor and seize."

        scene kirinfire24
        with dissolve

    s "…"
    ki "…"
    ki "Hello, fine sir. Sure is...weather we’re having."
    s "Yes. I have also noticed that the weather is there."
    ki "Indubitably."
    s "Weather."
    ki "…"
    s "…"
    ki "…"
    s "…"

    if bonus == True:
        ki "Did you give Miku an orgasm?"
    else:
        ki "I asked Miku about canola oil and she ran away."

    s "Well that was a fun ten seconds."

    scene kirinfire25
    with dissolve

    if bonus == True:
        ki "No, really. She’s been all sorts of weird lately, and the only reason she was able to defeat me during the dorm war was because she blindsided me with a comment about that."
        ki "Like, Miku was straight up worried about even touching herself at the beginning of the year because she thought it would make her go blind."
        s "Why is that a thing you know? Do girls really just talk about their masturbation habits with one another?"
        ki "I mean, I can’t speak for {i}most{/i} girls. But I certainly do. And believe it or not, Miku and I are really close."
        ki "Not like {i}Noriko{/i} and me close where we watch porn together and walk around naked and stuff, but like...childhood friend close. Kind of."
        ki "I know she’s closer to Makoto than she is to me, but up until recently, she was kinda the closest thing to a best friend that I had."

        scene kirinfire26
        with dissolve

        ki "But nooooow, it looks like she’s finally starting to catch up to the rest of us who aren’t living in perpetual boredom anymore."
        ki "And I was thinking that some of that might have to do with the fact that you’re around."
        ki "I mean, I already know for a fact that she’s not interested in girls, so you’re pretty much the only other constant in her life that’s changed in some way."
        ki "Plus, she’s been getting as red as they come when you show up to practice lately. And you’re definitely the type to notice that and move in on it."
        s "Yes, but so are you."

        scene kirinfire27
        with dissolve

        ki "Oh, I already tried. That’s how I know she’s not interested in girls."
        s "Wait, what did you do?"
        ki "If I tell you, you have to tell me what {i}you{/i} did. That’s the rule."
        s "I mean, I was going to tell you anyway. I doubt you’d use it against me since you actually seem to care about Miku."
        ki "I was gonna tell you anyway, too, so I’m glad we got that out of the way."

        scene kirinfire28
        with dissolve

        ki "It was a hot summer day for the soccer team, just weeks after finding out we’d lost our coach."
        ki "Miku was working herself to the bone trying to keep the team in shape despite virtually all of us sucking and not even having enough players to have an in-team scrim with."
        ki "Enter Kirin Kanda, who spent the morning fingering herself to lesbian porn only to have her sister barge into the living room moments before orgasm and tell her it’s time for[school]."
        ki "Needless to say, I was very unhappy having basically blue balled myself by not giving into the first twenty urges to cum and was ready to fuck literally anything that moved."

        scene kirinfire27
        with dissolve

        ki "But alas. Morning soccer practice meant that Kirin must go even {i}longer{/i} without the sweet release she’d promised herself early that morning."
        ki "And, as the sun poured down onto the field, the urges grew stronger."
        ki "Thighs...everywhere! Boobs...less prevalent, but still there!"

        scene kirinfire29
        with dissolve

        ki "And there she was...in all of her innocent and sexually repressed beauty- skin glistening from the sweat of hard work."
        ki "The time came for Kirin to make her move."
        ki "She’d wanted to for ages because of her target's- err, {i}Miku’s{/i} boyish appearance and what seemed like a high chance she might be into girls."

        scene kirinfire30
        with dissolve

        ki "{i}Hey, Miku! You’re looking awfully stiff today. Want to take a few minutes after practice and have me relieve some of that tension for you?{/i}"
        s "Ah. I’m assuming she didn’t quite understand what you meant by “relieving tension.”"

        scene kirinfire31
        with dissolve

        ki "Of course not. This is Miku we’re talking about."
        ki "Anyway, I pulled her aside and started giving her a massage in the store room, but when I moved in for the kill, she nearly jumped out of her uniform and booked it to class."
        s "I’m sorry to hear that you never achieved that “sweet release” you set out for."
        ki "What? You think I just left the room without finishing myself off first? Come on. You know me better than that."
        ki "What about you, though? How did your first sexual encounter with Miku go?"
        ki "Has there been more than one? What’s her orgasm face like?"
        s "I didn’t see it, to be fair."

        scene kirinfire32
        with dissolve

        ki "Straight to doggystyle on the first go?! Who does she think she is?! Me?!"
        s "Not quite."
        s "I slept next to her and Makoto during a beach trip that just the three of us went on."
        s "But, in the middle of the night- and I don’t really know if it was conscious or not, she started grinding up against me."
        s "So, I did what any sane man would do and grinded back."
        s "One thing led to another and she had what was {i}probably{/i} her first orgasm ever while her best friend remained sleeping right beside us, completely unaware of everything."

        scene kirinfire33
        with dissolve

        ki "Jesus fucking Christ that’s hot."
        s "That’s really all that’s happened, though."
        s "There were a few times where I’ve thought things were about to go further but, like you said, she gets...jumpy and runs away."

        scene kirinfire34
        with dissolve

        ki "Wait...maybe she still likes girls after all then?"
        ki "If she’s running away from {i}you{/i} when you try to take things further, maybe the fact that I’m a girl had nothing to do with it and she was just-"
        s "Running from unwanted sexual contact?"
        ki "Unwanted sexual contact? What’s that?"
        s "The thing normal girls have when-"

        play sound "static.mp3"
        scene lavendersgreen24 with flash
        scene kirinfire34 with flash
        stop sound

        ki "When what? I still don’t get it."
        s "…"
        s "Anyway, we should probably let Miku develop at her own rate. Whenever she’s ready, I’m sure we’ll know."

        scene kirinfire35
        with dissolve

        ki "Hah...Yeah. I guess you’re right. That girl’s been through enough as is. Forcing her into sexual maturity before she’s ready will only fuck her up more."
        s "Do you..."
        s "Actually know what she’s been through?"
    else:
        ki "Why would she run?! It's a good question!"
        s "Speaking of Miku, do you actually know what happened to her?"
        s "Her eyes keep getting all weird any time a loud noise happens and it's giving me second thoughts about inviting her to my Fourth of July barbecue."

    scene kirinfire36
    with dissolve

    "I bite the bullet and ask something I’ve been wondering for a long time."
    "I’ve known Miku since the very beginning and still feel like I know nothing about her other than that she’s hyper and...good at soccer."

    if bonus == True:
        "And that she occasionally gets horny in her sleep and surrenders to the urge to grind up against whatever happens to be there at the time."

    "Would I prefer to learn whatever her secrets are from her directly? Sure."
    "But..."
    "What if that doesn’t happen?"
    "I’m already useless enough when she has those noise-induced episodes of hers."
    "And I’m no psychologist, but maybe understanding the root cause will help me figure out how to better tackle them in the future?"
    "I obviously don’t want her to feel that way, especially when I know that, more often than not, it results in her tearing her hair out."
    "I just want to help her."
    "I want Miku’s mind to remain unclouded."
    "And I don’t want Makoto having to pick up bits of hair with parts of her best friend’s scalp still attached to them off the floor of her dorm room."

    ki "I mean..."
    ki "I don’t know {i}everything.{/i} She doesn’t talk about it."
    ki "Well, I guess it’s more like she {i}can’t{/i} talk about it. And it’s something we know we’re not supposed to ask about."
    ki "I...really like Miku."
    ki "She doesn’t judge me. And she treats me like a normal girl even when I know I’m anything but."
    s "I care about her too, obviously."
    ki "{i}Is{/i} that obvious?"
    ki "It seems like you {i}care{/i} about a lot of people, but I never really know exactly what {i}caring{/i} means to you."
    s "…"
    ki "I guess you’ll find out sooner or later...so it might be better if you hear it from me so you don’t react weirdly and...start asking a million questions."
    ki "But this conversation never happened."
    ki "Miku’s one of the few people I just...really want to hang onto."
    s "I never heard anything."
    ki "...Good."

    scene kirinfire37
    with dissolve

    ki "Miku watched her parents die when she was little."
    ki "And ever since then, loud noises or whatever have kinda...teleported her back in time or something like that."
    ki "I don’t know {i}how{/i} it happened, but I know it was a big enough deal for our[school] to tell all of us to keep our mouths shut and not ask her any questions about it."
    ki "I mean...who {i}would{/i} ask her about something like that in the first place?"
    ki "But yeah. That’s what those episodes are. And that’s why there’s nothing anyone can really do about them."
    ki "Her brain’s fucked beyond repair and neither you nor me can {i}fix{/i} her no matter how we want to."
    ki "Some people just wind up getting so scarred that they never really have a chance to fully develop or something. I don’t know."

    scene kirinfire38
    with dissolve

    ki "That’s just who she is now, I guess."

    scene kirinfire39
    with fade

    s "Are you leaving?"
    ki "Yeah. I’m gonna go see what she’s up to."
    ki "If she’s even awake, I guess. I’m pretty sure the class rep has some sort of sleep schedule she keeps her on to make sure her grades don’t explode."
    s "Grades should be the least of her worries now."
    ki "True. But that’s less because you're our teacher and more because all of her other worries are much, much worse."
    s "Thank you for telling me."
    ki "Telling you what? I never said anything."
    s "…"

    scene kirinfire40
    with dissolve

    ki "Also..."
    ki "You need to do something about Noriko."
    s "What do you mean?"
    ki "I mean that this constant struggle she’s in where she’s...trying to make you understand her while {i}also{/i} trying to change herself to fit your needs is dangerous."

    if norikokill == True:
        ki "Not to mention that now she’s probably sick to her stomach knowing the guy she loves flat out said he’d kill her in favor of two other girls earlier."

    s "…"
    ki "I’m not saying you should {i}date{/i} her or that you two are meant to be together or some sappy bullshit like that..."
    ki "I’m just saying that one friend who’s already had their growth stunted by tragedy is enough for me."
    ki "And I think losing you would break Noriko more than you can possibly understand right now."
    s "…"
    ki "…"

    scene kirinfire41
    with dissolve

    ki "But, then again, what do I know?"

    if bonus == True:
        ki "I’m just your fuck buddy who, on rare occasions, talks to you about non-sex related stuff where we both pretend to feel sad when we know deep down that we’re more numb than anything else."
    else:
        ki "I’m just your hug buddy who, on rare occasions, does impressions of you in the mirror."
        s "Wait, you do what?"

    ki "Goodnight, Sensei."

    if kirinmarry == True:
        ki "And thanks for marrying me."
        s "I thought you hated that?"
        ki "I did."
        ki "Now, please excuse me while I go puke my brains out at the thought of a peaceful life alongside someone as depressing as you."

    else:
        s "Goodnight, Kirin."
        s "I’ve already forgotten everything you’ve told me tonight."
        ki "Hm? Did I tell you something?"
        ki "I honestly don’t remember."

    scene black
    with dissolve2

    if norikokill == True:
        "I go back inside to find Noriko crying behind the counter."
        "She wipes her tears away as I approach her before smiling the same obsessive, partly creepy smile she always has when I’m nearby."
        "And, in spite of what I think my body wants me to do, I wrap my arms around her and tell her I was just kidding."
        "What a powerful pair of words that can be when used in the right context."
        "We break apart and, minutes later, the time comes for me to go home."
        "As I make my way to the door, she reminds me of how much she loves me."
        "And I tell her I love her too."
        "………"
        "……"
        "…"
        "Just kidding."

    else:
        "I go back inside and spend the next few minutes hanging out with Noriko."
        "I neglect to inform her of her roommate's sudden desire to hang out with someone else as I don’t want to negatively impact her self esteem in any way."
        "And as I pat myself on the back for doing yet another good deed, I’m reminded of how truly fulfilling life can be when all goes according to plan."
        "Of course, that only happens once in a blue moon."

        if bonus == True:
            "So as the next two years approach but never arrive due to time’s incessant desire to cum inside of us and leave us passed out on the bedroom floor-"
        else:
            "So as the next two years approach but never arrive due to wibbly wobbly timey wimey stuff-"

        "I will try to keep that in mind."
        "And I will fail miserably."
        "The same way I fail at virtually everything else that matters."
        "Or at least that’s what I {i}would{/i} say if anything else mattered to begin with."
        "Pain is real. It’s all of us that aren’t."

    $ renpy.end_replay()
    $ kirin_love += 1
    $ kirinspecial25 = True
    stop music fadeout 10.0

    "{i}Kirin’s affection has increased to [kirin_love]!{/i}"
    "………"
    "……"
    "…"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label kirindorm25:
...
```

## Code that triggers this event

File: (install folder)\game\scripts\subscribestar\inappropriatecontent.rpy

Code:
```python
...
n "I was really worried for a second because I thought you might’ve picked Chika as wife material over me, but...oh my God!"
            n "I’m so happy! Way happier than I should be from some stupid game!"

            scene thatonefmkscene43
            with dissolve

            s "Well, I’m happy you-"
            n "Wait, Kirin! Don’t leave! He obviously didn’t mean that!"
            ki "It’s fine."
            ki "I’m just going to go for a walk."
            ki "I’ll see you back at the dorm, Noriko."
            ki "Congratulations on your engagement."
            n "Kirin! Come on!"

            scene black
            with dissolve2
            stop music fadeout 10.0

            "Kirin disappears down the alley and leaves Noriko and I alone, both unsure of whether or not we should chase after her."
            "Given the fact that it’s Kirin, though, I’m sure she’ll get over it soon enough."
            "I mean...what did she expect?"
            "When you treat not only yourself but everyone around you like garbage, you can’t expect to just cruise by without ever hearing anything hurtful."
            "It’s her own fault that I chose the way I did. And it’s her own fault that I even {i}had{/i} to choose in the first place."

            n "We should probably...go back inside now..."
            s "...Yeah."

            stop music fadeout 7.0
            $ renpy.end_replay()
            $ convenience25 = True
            $ kirinspecial25skip = True
            $ noriko_love += 5

            "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
            "………"
            "……"
            "…"

            if day >= 6:
                jump endofsat
            else:
                jump endofweekday

        "Fuck Chika, Marry Kirin, Kill Noriko":
            $ kirinmarry = True
            $ norikokill = True

            s "I’d fuck Chika, marry you, and kill Noriko."

            scene thatonefmkscene44
            with dissolve

            n "You’d..."
            n "What?"
            ki "Are you fucking kidding me?! What kind of ass backwards choice is that?!"
            s "What’s wrong? You asked me to answer and-"
            n "You’re just messing with me, right?..."
            n "You’d never..."
            ki "M-Me too! Why am I the one getting fucking married all of a sudden?! I never asked for this!"
            s "Kirin, you’re toxic and...a horrible person. But so am I, so I think it might actually wind up working out."
            ki "It absolutely would not! That would never ever ever ever ever work out! Ever ever ever ever!"
            n "…"
            s "…"

            scene thatonefmkscene45
            with dissolve

            ki "N-Noriko! Come on! It’s only a game!"
            ki "Sensei just chose the most ridiculous answer on purpose to fuck with us! There’s no way he’d ever kill you! Just like there’s no way he’d ever marry {i}me{/i}!"
            n "Did you...bring a handkerchief with you by any chance?"

            scene thatonefmkscene46
            with dissolve

            ki "Look what you fucking did! You made Noriko cry! And you made {i}me{/i} throw up in my mouth!"
            s "Is marrying me really such a horrible future?"
            ki "That’s not the point!"
            ki "The point is you’re supposed to {i}not{/i} kill Noriko! And {i}not{/i} marry me! Those are the worst things you could pick!"
            s "Hey, you’re the one who asked me to choose. I’m just doing what I was told."
            n "I’m...going to go back inside now..."

            scene black
            with dissolve2
            stop music fadeout 10.0

            ki "Noriko, wait!"
            n "Actually, on second thought, I don’t really feel good. I’m just gonna head home..."
            n "Goodnight, you two."
            ki "Noriko! Hold up!"

            $ renpy.end_replay()
            $ kirin_love += 5
            $ renpy.end_replay()
            $ convenience25 = True

            "………"
            "……"
            "…"

            jump kirinspecial25
...
```