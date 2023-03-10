# All Along the Shoreline (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [What's Done is Done](./beachvacation1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: beachvacation2
* Group: Main
* Triggered by label: restofmayachange
* Chain sources: beachvacation1
* Chain sources path: beachvacation1->beachvacation1->mayachangex

## Official wiki page

[All Along the Shoreline](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachvacation2&go=Go) for more details.

## Event code

File: (install folder)\game\script.rpy

Code:
```python
...
label beachvacation2:
    scene beachvactwo1
    with dissolve
    play music "shiningstarinstrumental.mp3" fadein 8.0

    "Ayane and Ami pull me over to the front of the women’s restroom as soon as we set foot on the beach."
    "Maya and Sana disappear inside almost immediately, carrying a few bags with their swimsuits and other...girl-related items, I guess."
    "These two seem to have something they want to say to me, though."

    if bonus == True:
        ay "Are you gonna come get changed with us, Sensei?"
        s "Oh. Uhh, I knew you had something to say. I didn’t think it would be that, though."
    else:
        ay "Are you going to change into your bathing suit as well, Sensei?"
        s "Am I allowed to participate too? I thought it would make everyone feel nervous since I am such a good swimmer."

    a "She’s kidding, obviously."

    scene beachvactwo2
    with dissolve

    ay "I am?"
    a "You better be..."

    if bonus == True:
        s "For everyone’s sake, no. I will not be getting changed with you two."
        s "Fun fact, I actually don’t even know how to swim."
    else:
        s "I am sorry to interject but I'm not actually a great swimmer. I don't know why I said that. I think I was just trying to impress you all."
        s "In fact, I don't even know how to swim."

    scene beachvactwo3
    with dissolve

    a "What are you talking about? We’ve gone swimming together plenty of times."
    ay "Oh! I know what this is!"
    ay "He’s faking that he doesn’t know how to swim so one of us will volunteer to teach him!"

    if bonus == True:
        ay "I volunteer myself! I’ll have you know I’m a very hands-on teacher, though."

    scene beachvactwo4
    with dissolve

    if bonus == True:
        a "For the love of God, Ayane! Keep it in your pants! "
        a "We all know you like him but he’s still my [uncle]! "
        a "And if you even {i}think{/i} of spending this entire weekend harassing him, I swear on all that is holy that I will end you."
    else:
        a "For the love of God, Ayane! Go get changed already!"

    s "Uh-oh. Ami’s mad. "
    s "Quick, let's jump into the water to avoid her wrath."

    scene beachvactwo5
    with dissolve

    a "You’re not helping!"

    if bonus == True:
        ay "Now now, children. Simmer down. I promise to keep it in my pants."
    else:
        ay "Now now, you two. I won't be teaching anyone to swim unless they make a deposit first. Time is money and I am the money girl until Touka shows up."

    scene beachvactwo6
    with dissolve

    ay "I might be in love but even I know it’s unreasonable to keep him all to myself for an entire weekend."

    if bonus == True:
        ay "We’re all here to have fun. And even if I’m the one paying for the whole thing, Sensei is the one kind enough to chaperone all of us."

    ay "Who would I be to hog all the teacher-time?"
    s "Please do not refer to the time we spend together as teacher-time. That makes it sound kind of gross."

    scene beachvactwo7
    with dissolve

    ay "{i}Teacher-time.{/i}"
    a "Why do I suddenly feel like this weekend might not be as relaxing as I originally thought?"

    "Gee, I don’t know, Ami. You’re the one who went and invited the entire class on a trip that I thought was going to be for the two of us."
    "Though, Ayane coming definitely saved me a lot of money."
    "And Makoto is the one who wound up booking the place."

    if bonus == True:
        "So what may be an exhausting weekend for Ami is more like tropical, ecchi paradise for me. "
        "Let’s get this show on the road and see some swimsuits."

        s "Okay, well, you two do your thing and go take each other’s clothes off. I’m gonna go look around for the other girls."
    else:
        "The two of them are both so helpful and I really appreciate all that they do for me."

        s "Okay, well, I hope the two of you enjoy a nice dose of overexposure to UV rays. I'm gonna go make my legs do the thing where they take me to places now. "

    scene beachvactwo8
    with dissolve

    a "Why on Earth would you word it like that?..."

    if bonus == True:
        ay "Come on, Ami! Let’s go take each other’s clothes off like your [uncle] asked!"

        scene beachvactwo9
        with dissolve

        a "Hah...whatever. We’ll go get changed."
        a "I’m taking my own clothes off, though."
        ay "But then who will undress me?"

    scene beachvactwo10
    with dissolve

    "Ami and Ayane disappear into the bathroom and I can hear my [niece] begin to yell something unintelligible almost immediately."

    scene black
    with dissolve

    "I circle around the restroom to see if I spot anyone else I know and find the beach surprisingly empty."
    "It’s a Saturday in the middle of Summer, so why the hell isn’t anyone around?"
    "I kick up some sand as I continue to walk down the beach before finally spotting a pair of familiar faces."
    "………"
    "……"
    "…"

    scene beachvactwo11
    with dissolve

    mo "Glad to see you’ve made it this far into the next dimension, Supreme Overlord."
    r "Translation: Hi, Sensei! I’m glad you made it here safely."
    s "Thanks, Rin. Would you mind tagging along for every conversation I have with Molly from now on?"
    s "I’ll pay you if I have to."

    scene beachvactwo12
    with dissolve

    r "How much we talkin’ here? I make pretty good tips at the cafe so it will have to be a lot."
    mo "You make tips at the cafe?"

    scene beachvactwo13
    with dissolve

    r "You probably would too if you stopped trying to recruit every single customer into your guild."

    scene beachvactwo14
    with dissolve

    mo "We need a paladin! What else am I supposed to do?"
    mo "I posted a whole thing on Reddit and didn’t even get a frickin’ upvote! You know how much that sucks when you type out a 2,000 word guild description?!"

    scene beachvactwo15
    with dissolve

    r "Translation: No one on the Internet wants to join my stupid guild."
    mo "You’ll burn for this, witch."
    s "Did you two come here together or something?"
    s "I know me and some of the others are kind of late, so sorry if we kept you waiting long."

    scene beachvactwo16
    with dissolve

    r "It’s no biggie, dude. Molly and I came way early so we kind of expected no one else to be here."
    r "It’s not often that Haruka gives us the weekend off, so I think it’s safe to say the two of us wanted to make the best possible use of that time."
    mo "Right-o! And also, neither of us slept last night because we were playing some new game together."
    s "You didn’t sleep? Like, at all?"
    r "Not a wink. "
    mo "Who needs sleep when you can just keep caffeinating until your body shuts down all on its own?"
    s "Normal people. "

    scene beachvactwo17
    with dissolve

    r "I gave up on being normal a long, long time ago. "
    r "This is the life I have chosen and you must respect it if you ever want to try one of my drinks again."
    s "I mean, I’d be more than happy to consume a drink I actually order for once."

    scene beachvactwo18
    with dissolve

    r "Guh! My womanly heart!"
    mo "Ya know, Sir, I’m always willing to make you a drink that I-"
    s "No thanks."
    mo "…"
    mo "You must not have heard me. What I’m trying to say is-"
    s "No thanks."

    scene beachvactwo19
    with dissolve

    mo "Why do you betray me when I need you most?!"
    s "What are you even doing exposing yourself to sunlight like this, Molly? Aren’t you afraid of getting sunburnt or whatever it is you were worried about the other day?"

    scene beachvactwo20
    with dissolve

    mo "I would have been if it weren’t for the draught of protection."
    r "Translation: I’m wearing sunscreen."
    s "Thanks, Rin."
    r "No prob. I’ll send you an invoice later."
    s "Appreciated."

    if bonus == True:
        mo "Do you require a draught as well, Sir? I’d be more than happy to help apply it for you."
    else:
        mo "Sir, are you okay with the prospect of riding an elephant together tonight?"

    scene beachvactwo21
    with dissolve

    if bonus == True:
        r "Dude! What the Hell?! You can’t just ask to rub down our teacher like that. Even if he {i}is{/i} cool with it."
        s "I should probably be offended that you assume I'm cool with that, but I’m honestly just glad you understand me, Rin."
    else:
        r "Dude! What the Hell?! You can’t just ask our teacher to ride an elephant before we even find one!"
        s "Someone would have to help me onto it. I am not good at climbing onto animals."
        r "I can help. I am excellent at that exact thing."

    mo "Well, what if {i}both{/i} of us were to do it, then? You’ve got a lot of body and my tiny Irish arms wouldn’t be able to reach the whole thing without some help from a friend."

    scene beachvactwo22
    with dissolve

    if bonus == True:
        r "Translation: I’m a pervert currently battling sexual frustration since I didn’t get to rub one out last night."
    else:
        r "Molly thinks you're fat and doubts my strength."
        s "D="

    scene beachvactwo23
    with dissolve

    mo "AHHH! RIN!"
    mo "AT LEAST USE CODE WORDS OR SOMETHING!"

    scene black
    with dissolve

    "Molly suddenly runs away and Rin follows after her, leaving me with a quick wink."
    "I go back to walking around, but it isn’t long before I run into someone else I know..."

    scene beachvactwo24
    with dissolve

    t "…"
    s "…"
    t "…"
    s "…"
    t "I’m ready to party."
    s "I’m sure you are, Tsuneyo."

    scene beachvactwo25
    with dissolve

    t "Ah-"
    s "I like your tube thing. Did you pick it out yourself?"

    scene beachvactwo24
    with dissolve

    t "It was recommended by my father."
    s "He recommended you a flotation device?"
    t "He recommends me many things."
    t "I also do not know how to swim, so there is a good chance this tube will save my life."
    t "It also has a cat on it."
    s "Yes, I can see that."

    scene beachvactwo26
    with dissolve

    t "Meow~"
    s "…"
    t "…"
    s "Did you just meow at me?"

    scene beachvactwo24
    with dissolve

    t "That was the cat."
    s "I literally watched you do it."
    t "You must be mistaken. I would never meow at my teacher."
    s "…"
    t "…"
    s "…"

    scene beachvactwo26
    with dissolve

    t "Meow~"
    s "Really?"

    scene beachvactwo24
    with dissolve

    t "Okay, that time it was me."

    "It was you the first time as well..."

    s "I’ve gotta say, I’m a little surprised to see you here."
    t "Why?"
    s "Well, I didn’t really think you’d be the type to leave your noodle sanctuary for a weekend of...whatever this is a weekend of."
    t "Water, I’m assuming."
    s "Yeah, there’s definitely a lot of that."
    t "I’m here to enjoy my youth. "
    t "And also because the Emerald Guardian asked me to come."
    s "Ahh, yeah that makes sense. Molly {i}would{/i} have something to do with this."

    scene beachvactwo27
    with dissolve

    t "Did she run off a minute or two ago?"
    t "I could have sworn I heard her yelling strange words I didn’t understand."

    if bonus == True:
        s "Yeah. Something about masturbation, I think."
    else:
        s "Probably something in gaelic."

    t "Oh."
    s "…"
    t "…"

    scene beachvactwo24
    with dissolve

    t "What does that mean?"
    s "…"
    t "…"
    s "Wait, are you being serious?"
    t "I’m always serious. Except for when I’m not."
    s "I honestly can never tell if you’re joking, so you’re gonna have to help me out here."

    if bonus == True:
        t "Please teach me what masturbation is."

        "That might be the single most unintentionally erotic thing I’ve ever heard."
    else:
        t "Please teach me what Gaelic is."

    s "Maybe it’s best if you ask one of the other girls? I don’t think this is something you want to hear from me."

    if bonus == False:
        s "I don't want to disrespect the language by butchering it."

    scene beachvactwo28
    with dissolve

    t "I don’t trust you. "
    t "You’re going to make me ask them something strange, aren’t you?"
    s "Who cares even if that's true? You’re all girls. "
    s "You might not know this since you’re sheltered but girls talk about stuff like that together all the time."

    "Probably."

    t "Okay."

    if bonus == True:
        t "I will tell the other girls that you told me to ask them about masturbation."
        s "No. Definitely leave me out of this. I don’t want to get in trouble."
    else:
        t "I will tell the other girls that you would not teach me Gaelic and they will beat you up."
        s "Wait. I do not want to be hurt. I am fragile."

    scene beachvactwo29
    with dissolve

    t "It has already been decided."

    if bonus == True:
        s "No, it hasn’t already been decided. Do not, under any circumstances, bring those two things up in the same conversation."
    else:
        s "Tsuneyo, wait."

    t "Farewell, Sensei."
    t "I need to go party with my bros."

    scene beachvactwo30
    with dissolve

    s "…"

    "Tsuneyo wanders off toward the water and I am forced to go fit myself into yet another conversation."
    "Hopefully the next one turns out a little better than this one did."

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene beachvactwo31
    with dissolve

    s "Welp, there goes that hope."
    y "Heh? The fuck you talkin’ about?"
    s "Nothing. What are you up to, Yumi?"
    y "The fuck’s it look like I’m up to, dipshit?"
    y "I’m sitting on a table and wondering why I bothered coming here in the first place."
    s "If you didn’t want to come, why did you?"

    scene beachvactwo32
    with dissolve

    y "Fuck if I know. Chika was pretty insistent on me showing up for at least a little bit."
    y "No idea why she cares so much about me “socializing” or whatever bullshit she said it was, but I honestly couldn’t care less."
    s "Where is Chika, by the way? I figured you two would be together."

    scene beachvactwo33
    with dissolve

    y "Not here."
    s "What? Why?"

    if bonus == True:
        "I was looking forward to seeing her in her swimsuit again..."

    y "She couldn’t get out of work today and wanted to be there for Chinami in the morning."
    y "We’re switching shifts later. "
    y "She’ll be here tonight and I’ll go hang out with the little twerp and not have to deal with you staring at me all fuckin’ day anymore."
    s "We’re having a conversation. Not staring at you for the duration of it would be rude."

    scene beachvactwo34
    with dissolve

    y "Oh, please. You borderline stalk me in the streets and now you’re going to try and say the only reason you’re staring at me is because we’re talking?"

    if bonus == True:
        y "I don’t go to[school] much, but I’m not a fuckin' idiot, dude. I can tell when someone is a pervert without having to fuckin’ research ‘em first."
        s "Well, since you’ve already decided I’m a pervert, mind if I compliment you on how cute you are in your bathing suit?"
    else:
        s "Do you mind if I hug you again right now? I have not hugged anyone all morning and I have to recharge my hug battery."

    scene beachvactwo35
    with dissolve

    y "OF FUCKING COURSE I MIND!"

    if bonus == True:
        y "That’s literally the one thing I didn’t want to fucking hear! "
        y "Fuck, dude! If it wasn’t so god damn hot I’d be wearing my normal clothes anyway!"
        s "Those normal clothes really don’t do you any favors, though. They’re too baggy. "
        s "Things like this fit you much better."

        scene beachvactwo36
        with dissolve

        y "Bullshit. You’re only saying that because the less clothes a girl is wearing, the more attractive you think they are."
        s "…"
        y "…"
        s "Okay, maybe."
        s "But you really do look cute. I mean it."
    else:
        s "Ughhhhhhh..."

    scene beachvactwo37
    with dissolve

    y "Eat shit and die."

    "Yumi and I engage in a staredown for several seconds but it feels more like hours."
    "The staredown is immediately halted when someone else shows up, though..."

    scene beachvactwo38
    with dissolve

    f "Umm...hey. Sorry I’m late."
    f "I had some stuff to take care of at the library first."
    y "Oh shit. Didn’t think I’d ever see a beached whale in person. "
    y "Do we gotta call the Coast Guard or some shit? How does this work?"

    scene beachvactwo39
    with dissolve

    f "Mm..."
    s "Don’t listen to her, Futaba. Yumi is in a bad mood today."
    f "I...can see that."
    s "And no worries about being late. I was late too. "

    scene beachvactwo40
    with dissolve

    f "Were you? How come?"
    s "I may or may not have overslept. But that doesn’t matter."
    s "What {i}does{/i} matter is that we’re both here now. And we’re going to have as good a weekend as we possibly can."
    y "Oh golly gee. That sounds so swell."
    s "Just keep ignoring her and she’ll fade away."
    y "I fucking wish."
    f "Mhm. I’ll...do my best."
    s "I like your hair like that, by the way. It looks nice."

    scene beachvactwo41
    with dissolve

    f "R-Really?!"
    f "I didn’t really do it on purpose or anything. I just figured that since we’re gonna be swimming and whatnot..."
    f "Well, I’m sure you can figure out the rest."
    s "I’m sure I can as well."
    s "You’re not planning on swimming in your casual clothes, though, right?"

    scene beachvactwo42
    with dissolve

    f "Of course not...I was about to go change but just...wanted to say hi first."
    y "Sure seems like a long hello."
    f "...Yeah."
    f "Okay, well...I’m gonna go get changed. "
    f "Don’t expect too much, though. I wasn’t really able to find anything good when I went shopping the other day so I kind of just...got the first thing I saw."
    y "More like nothing would fit so you-"

    scene beachvactwo43
    with dissolve

    s "Yumi. Please just stop talking."
    y "…"
    f "…"
    f "Um..."
    f "I think...you look really pretty, Yumi."
    f "…"
    f "I’ll be back in a few minutes..."

    scene beachvactwo44
    with dissolve

    "Futaba picks her bag up off the ground and quietly moves over to the restroom."
    "Yumi remains silent and focuses on the sand, hopefully reflecting on how much of an asshole she is."

    scene beachvactwo45
    with dissolve

    s "The fuck is your problem?"
    y "…"
    s "What, you’re just not going to respond now?"
    y "No point."
    y "Just fuckin’ follow her. "
    y "Not like talkin’ to me is worth anything anyway."
    s "…"
    y "…"

    scene sky
    with dissolve

    "I do as Yumi says and begin to walk back toward the restroom to make sure Futaba is okay. "
    "I’m sure she doesn’t actually care about Futaba’s feelings, but I do. So I need to make sure she doesn’t take Yumi’s words to heart."
    "I’m sure it’s hard enough for someone with low confidence to put on a bathing suit in public, so Futaba is already being brave."
    "Having one more obstacle in the way between her and feeling comfortable just isn’t fair."
    "..."
    "Once she finishes changing, I wave her over and pull her around the back of the restroom."
    "………"
    "……"
    "…"

    scene beachvactwo46
    with dissolve

    f "Umm...did you need something?"
    f "It feels a little weird being alone back here when everyone is right around the corner."
    s "I just wanted to make sure you were doing okay."
    s "Yumi can be a bitch sometimes and you shouldn’t take what she says to heart."
    f "I know that. You tell me all the time."
    f "And besides, I’m fine. Really."
    f "You pulling me aside is enough to put me at ease."

    scene beachvactwo47
    with dissolve

    f "I just wish I had something a little more exciting to show you."
    s "What are you talking about? You look great."
    f "Oh stop. I’m glad that you’re being nice to me, but this really isn’t a flattering swimsuit."

    scene beachvactwo48
    with dissolve

    f "But...hey, at least stripes are slimming, right?"

    "I’m not really sure what to say to that."
    "On one hand, it seems like Futaba is finally learning to laugh about herself...But at the same time, it’s a slightly off-putting self degradation."
    "But I guess in times like these, it’s best to follow your heart."
    "I’m sure that’s what Futaba would want me to do."

    s "Hey, Futaba. Can I make a request?"
    f "Depends. What do you wa-"

    if bonus == True:
        s "Can you show me your boobs?"
        f "…"
        s "…"

        scene beachvactwo49
        with dissolve

        f "Excuse me?"
        s "Sorry. I told myself to follow my heart and that's just the first thing that came out."
        f "Why am I not surprised by this?"
        s "Come on. Just for a second."
        s "You can’t wear a skin-tight bathing suit like that and expect me to not want to see them."
        s "And besides, the two of us are totally alone back here. No one is going to see."

        scene beachvactwo50
        with dissolve

        f "I don’t know, [futabamaster]...It seems like a pretty bad idea to me..."
        s "Just for a second. Come on."
        s "You know you want to."
        f "Mmn..."

        scene beachvactwo51
        with dissolve

        f "Is this much okay?..."
        f "I don’t know if I’m really confident enough to pull my suit down."
        f "These things are kind of hard to put back inside on short notice and I don’t want to get caught."
        s "Hmm..."

        if futaba_lust < 10:
            s "Yeah...I guess that much is fine."

            scene beachvactwo46
            with dissolve

            f "Good...I’m glad I was able to make you happy. Even if it was only just a little."
            s "Of course. I’m always happy to see-"

        else:
            s "I think I’m going to need a little more than that."
            f "Yeah...I figured as much."
            f "You need to tell me if someone is coming, though."
            s "Deal."
            f "Okay..."
            f "Then..."

            scene beachvactwo52
            with dissolve

            "Futaba slides down the top half of her bathing suit and reveals her two massive breasts, holding them up to make them look better for me."

            f "Um...are you happy now?"
            s "Not yet. I need another minute or two to take in the beauty."

            scene beachvactwo53
            with dissolve

            f "Okay, but hurry it up because they sunburn pretty easily."
            s "How do you know that?"
            f "I just know, okay? It doesn’t matter how."
            s "Well hey, if they {i}do{/i} get sunburnt, it will have been worth it."
            f "For {i}you{/i}, yes. But not for me. "
            f "My pain tolerance is pretty much non-existent. In fact, I’m already starting to feel the heat."
            s "Just a few more minutes and-"

            scene beachvactwo48
            with dissolve

            f "Nope. All done~"
            s "Damn it. I’m supposed to be in charge here."
            f "You can be in charge some other time. I’m here to have fun with my friends, not make my teacher's penis hard."
            s "This is not the vacation I signed up for."
    else:
        s "Can you be my partner for tonight's egg tossing competition?"
        s "All of the other girls have really tiny hands and I need someone who both excels at protecting them and also has a nurturing presence."
        f "..."
        s "I think you'd be really good at it."
        f "..."

    scene beachvactwo54
    play sound "whistle.mp3"

    "A whistle suddenly rings out from not far behind the restroom pavilion. "
    "I panic for a brief moment thinking that maybe a lifeguard or someone caught us, but that panic is quelled when I hear who shouts after the whistle."

    mak "Sensei! Come out from wherever you’re hiding! Vacation hasn’t started just yet!"

    scene beachvactwo55
    with dissolve

    if bonus == True:
        f "Did you have plans with Makoto this morning?"
        s "I don’t think so? Why does it sound like I’m in trouble?"
        f "I have no idea. You'd better go, though. She gets kind of evil when things don’t go her way."
        s "Yeah, yeah. I know. "
        s "I’m going."
    else:
        f "I'll...think about it?"
        s "Thanks, Futaba. I really appreciate that."

    scene sky
    with dissolve

    "I step away from Futaba for a moment and put my hands in the air as if I’m under arrest."
    "I’m not exactly sure what Makoto wants from me, but judging by the tone of her voice, she doesn’t seem too happy about it..."

    scene beachvactwo56
    with dissolve

    mak "There you are...I’ve been looking all over for you."
    mak "Why do you look like you’re up to no good?"
    mi "Yeah, why are yer’ hands up in the air like yer’ gettin’ arrested?"
    mi "You didn’t do somethin’ weird behind the bathrooms, did ya? I coulda sworn I saw someone else back there."
    s "Nope. Just me."
    s "I’ll put my hands down now."
    mak "Yeah...thanks."

    scene beachvactwo57
    with dissolve

    mak "Anyway, I need you to come with me for a bit. "
    s "Why? What did I do wrong?"
    mak "We’re late for check-in at the inn. I put it under my name but I still need you to be there with me."
    s "Oh, right. That’s a thing we’re doing."

    scene beachvactwo58
    with dissolve

    mak "It’s literally half of this vacation."

    if bonus == True:
        s "Yeah, I know. I just got swept up in all the bathing suits and forgot about it."
        mi "I don’t blame ya! Lots of cute girls runnin’ around these parts with their butts all bouncin’ about and whatnot."
        mi "Crazy times, Sensei. Crazy times."
        mak "Crazy times or not, I need you to stop staring at all of these “bouncing butts” as Miku put it for a few moments and follow me to the inn."
        mak "It’s not a far walk from here. Maybe only ten minutes or so. But we should be back around noon-ish."
        s "Ugh, fine. If I have to."
        s "But just know that I’m not happy about missing out on the butts."
        mak "I knew you wouldn’t be."

        scene beachvactwo59
        with dissolve

        mi "Don’t worry, Sensei! Good ole’ Miku will let you look at hers when ya get back! Even if it’s as flat as a board."
        mak "You will do no such thing."
        mi "...Okay, never mind! "
        mi "I’ll still see ya later, though!"
    else:
        s "I know. I have been feeling rather forgetful lately and it must have slipped my mind. I apologize."

    scene beachvactwo60
    with dissolve

    mak "You don’t mind if I just walk there in this, do you?"
    mak "I don’t want to get dressed again just to go check in and I’m sure they’re used to bathing suits since it’s a beach-inn and whatnot."

    if bonus == True:
        s "Why would I ever ask a girl to change {i}out{/i} of a bathing suit? Have you forgotten who I am?"
        mak "Unfortunately, not."
        mak "Let’s head out now before it gets any later, though. "
        mak "Just stick close to me and don’t let any half-naked girls distract you."
        s "I will do my best..."
    else:
        s "I will feel slightly uncomfortable but will do my best to maintain a respectful distance from you at all times."

    scene black
    with dissolve
    stop music fadeout 10.0

    "Makoto and I begin to walk down the coast together."
    "We walk close enough that we occasionally bump arms, but this is entirely her doing."

    if bonus == True:
        "In fact, I’ve been walking as straight as possible just to confirm that it’s her behind all of this."
        "It’s not like I mind, though."
        "We make idle chit-chat all along the shoreline and, before long, wind up in front of an old inn..."
    else:
        "I do not do anything wrong at any point and will pray at length tonight to apologize for the shoulder to shoulder contact."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ beachvacation2 = True

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "........."
    "......"
    "..."

label beachvacation3:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```