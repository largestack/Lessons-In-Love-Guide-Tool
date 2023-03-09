# Red-ish Light District
Touka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=toukaspecial15p2&go=Go)


Part of event chain [A Commoner's Tour of Summer](./toukaspecial15.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: toukaspecial15p2
* Group: Touka
* Triggered by label: toukaspecial15

## Event code
File: \game\ToukaEvents.rpy
Code:
```python
...
label toukaspecial15p2:
    scene tsukiokaarcade1
    with dissolve2
    play music "justbehappy.mp3"

    tk "What?! Where are we?! This doesn’t look like a place that’s made for poor people at all!"
    tb "Did we perhaps go...{i}under{/i} the outer barrier instead of through it? Have we accidentally discovered a loophole in the isolation policy?"
    to "No, Mother. I believe we’re still in Kumon-mi. I’ve overheard several of my classmates speaking about a place like this, but I had no idea it was so...large. And colorful."
    to "Why, this is actually quite impressive."
    tk "Mother! Mother! There is a sign for something called a “Maid cafe!” Poor people {i}can{/i} have maids after all!"

    "As much as I’d like to say that Kumon-mi keeps getting larger, I actually know where we are now."
    "Well, vaguely. "
    "I’m pretty sure this place isn’t far off from the arcade I visited with Rin a while ago. The...architecture looks the same, at the very least. "
    "I’m pretty sure I’ve heard Ami and company talk about this area as well, but those conversations have always been riddled with terminology I don’t understand, so I never paid much attention."
    "Either way, as you can see, the Tsukioka family is currently struggling to come to terms with the expansion of their world and has gone into a bit of a collective state of shock."

    scene tsukiokaarcade2
    with dissolve

    to "Sensei...we {i}are{/i} still in Kumon-mi, correct? Do you have any idea what this part of the city is called?"
    s "We are and no. I have no idea what this place is called. Just keep an eye out for a sign if you’re that curious."
    to "Well aren’t you as unhelpful as ever."
    s "I’d like to take this opportunity to remind you that you’re technically the one who brought {i}me{/i} here. Well, your sister at least."
    tk "This place is crazy! Super crazy! "
    tk "Why’s that man over there dressed like a woman?! And why is that woman dressed like a cat?! And why is that cat- wait, no. That’s just a normal cat."
    tk "Mother! Put Father on Facetime! He must see this!"
    tb "This isn’t one of those “Red light districts” I’ve heard about, is it? "
    to "The lights {i}do{/i} seem rather red-{i}ish.{/i}"
    s "I’m sure there’s nothing you have to worry about during the day. Things might be a little different at night, though."

    if bonus == True:
        "I’ll have to make sure I stop by and check some time. In the interest of keeping my students out of harm’s way, of course. There are absolutely no “personal” reasons for my sudden desire to spend more time here."

    scene tsukiokaarcade3
    with dissolve

    tk "Mother! Do you think the reason commoners are able to tolerate the subway as effectively as they do is because they know where it is taking them?"
    tb "No, dear. I think they just have a completely different standard of living than we’re used to. But I’m sure a place like this {i}would{/i} provide some sort of...incentive."
    to "Tsukasa, will you be choosing where we head from here as well? You know, since our tour guide would rather {i}tour{/i} than {i}guide.{/i}"
    s "I’ll have you know that there is actually one building over here that I have been inside and that is infinitely more than any of you have exposure to."

    scene tsukiokaarcade4
    with dissolve

    to "Is that true? What in the world brought you over to this part of town, Sensei? All that I’ve heard about it involves otaku culture, scantily clad women and-"

    scene tsukiokaarcade5
    with dissolve

    to "Oh. I believe I understand now."
    tb "You’re absolutely sure there’s nothing...you know, {i}inappropriate{/i} around here, Sensei? "
    tb "Touka is one thing, but I shouldn’t be exposing Tsukasa to such...aspects of the world at her age. Especially with her inherent curiosity about everything."
    tk "Nonsense, Mother. I’m just as much of an adult as Touka."
    tb "You’re really not, dear."
    s "I have no idea what is or isn’t inappropriate about this part of town. The building I alluded to a minute ago should be fine, though."
    s "It’s just some arcade thing I’ve been to with another girl from class."

    scene tsukiokaarcade6
    with dissolve

    tb "Well aren’t you the most popular man around?"
    s "Strangely enough, I kind of am."
    to "Who did you come here with, Sensei?"
    to "Was it the Irish girl? Molly? This seems like the sort of place she’d enjoy. "
    tb "I bet {i}I{/i} know who it was."
    s "It was Rin."

    scene tsukiokaarcade7
    with dissolve

    tb "Nevermind. This is what I get for thinking I’m “in the loop.”"
    to "I suppose you two are rather friendly with one another, so that makes sense. "
    to "What would we do at an arcade, though? Tsukasa and I have very little exposure to video games since they’re known to rot away at the brain. "
    s "I think that’s just a thing parents say to keep their children away from having fun for whatever reason. There’s not really any truth to it."

    scene tsukiokaarcade8
    with dissolve

    tb "You know, dear, your mother used to be rather excellent at pinball when she was your age. "
    tb "I’m not sure if I’d call that a {i}video{/i} game per se, but I’m not opposed to reliving some of the old days with my two favorite girls by my side."
    to "Is that true, Mother? I had no idea. I’d assumed those old pinball machines in our seventh basement were just valuable antiques of some sort."

    scene tsukiokaarcade9
    with dissolve

    tb "What? No! Don’t call them antiques! That makes me feel old!"
    tk "Mr. Teacher Man, does this “arcade” have the pig-killing game that my new friend Chinami has been telling me about? "
    tk "She has been raving quite a bit about it and I must train in order to knock her off her shoddy, immunocompromised pedestal and show her who the true champion of the world is."
    s "Probably not, but there’s only one way to find out."

    scene tsukiokaarcade10
    with dissolve

    tk "I vote for the commoner arcade! I see enough maids at home! A cafe full of them does not interest me!"
    tb "I also think that might be fun. I’m not sure I’m as good with my hands as I used to be, but I’d certainly like to give them a bit of a workout if you catch my drift. "
    s "I...don’t know if I do? Because that sounded a lot like-"
    to "With Mother’s blessing, I’d be delighted to go as well."
    to "It might not be a public pool or a beach vacation, but this {i}does{/i} seem like a summer activity of sorts. So it’s almost like the purpose of our visit here is actually being fulfilled!"
    to "Congratulations, Sensei! You have achieved a very rare success!"
    s "Who is it that’s been teaching you sarcasm? Because I really don’t like this side of you."
    to "What side are you speaking of? I am but a naive, young woman- ignorant to the harshness of a commoner summer and all of the activities that accompany it."
    tb "And I’m her mother: An ex-pinball expert who is definitely not “old.”"
    tk "And I’m bored! Arcade! Now! Go!"

    scene black
    with dissolve2

    "I search for the word “arcade” on my GPS app only to be flooded with a list of at least twenty of them that I must now cycle through until I find the one I’m actually familiar with."
    "After a fair bit of navigation, the name “Couch Potato” jumps out at me and I confirm that it’s the correct one."
    "The arcade is about a mile away, so I’m sure it’s more walking than any of the Tsukiokas have ever done while not on some sort of...rich person hike or something."
    "If that’s even a thing rich people do."
    "Huh."
    "I guess I really would be lost if I were to enter Touka’s world."
    "But for now, she and her family are a part of mine."
    "Just...one that I don’t often explore. "
    "Either way, I coerce them into following me without the assistance of a limo and, after a short while, we arrive at the arcade."
    "........."
    "......"
    "..."

    scene tsukiokaarcade11
    with dissolve2

    tb "You know, I was a little worried about where you were leading us once we started moving further and further away from the nice looking buildings, but I will admit that this is nicer than I was expecting."
    s "Thanks? Maybe?"
    to "It’s just an interesting choice. That’s all. I’m sure this arcade has just as much to offer as all of the ones we passed that were ten times the size of it."
    s "Really. Who taught you this?"
    to "There are certain things a person just...picks up after spending enough time with you. "
    s "Anyway, {i}I’m{/i} not the one who actively {i}chose{/i} this arcade. It’s just the only one that I’ve physically been to."
    s "Take it up with Rin if you have a problem with it. This is just the one where cool people hang out at according to her."

    scene tsukiokaarcade12
    with dissolve

    to "What? Cool people? I would like to be “cool.”"
    s "Then go play a game or something. I don’t know. "
    s "Enjoy your pretend summer vacation while it’s technically still winter."
    tb "What are you going to do, though?"
    s "Me? Probably zone out for a few minutes and then choose which one of you to spend time with."
    tb "Well {i}I{/i} am going to get a drink. I was not expecting there to be a bar here. "
    tb "I was also expecting there to be maybe {i}one{/i} pinball machine, but...alas."

    scene tsukiokaarcade11
    with dissolve

    to "And I suppose I will make my way over to a random machine and pretend to know what I am doing. "
    to "Feel free to come teach me if you’d be so obliged, Sensei. Since that {i}is{/i} your job and all, I mean."
    s "Uh-huh. We’ll see."

    scene black
    with dissolve2

    "The Tsukiokas disperse and, after a moment of self-reflection and mild confusion about yet another situation I’ve found myself in, the time comes to make a choice."
    "Who do I want to spend time with first?"

    menu tsukiokaarcade:
        "Touka" if toukaarcade == False:
            scene tsukiokaarcade13
            with dissolve2

            to "Oh, good. You’re here. "
            to "Can you tell me what the purpose of this game is exactly? I can’t seem to make it past the first level."
            s "Touka, that’s the start menu. "
            to "Does it not count as a level? I’m very confused. "
            s "You just have to hit the start button."

            scene tsukiokaarcade14
            with dissolve

            to "The...oh. Okay. I see it. Can I not just use this knobby thing to control the video game? Using multiple buttons {i}and{/i} a knobby thing sounds very hard for a beginner like me."
            s "I’m pretty sure this is one of the easiest games to control here. You’ve just got two buttons and a joystick."
            s "Most of the modern games Ami and her friends play require all sorts of buttons and multiple joysticks, so if you’re going to learn, this is probably the place to do it."

            scene tsukiokaarcade15
            with dissolve

            to "Do you also play games like this in your spare time, Sensei? Or is all of it spent wandering into the rooms of unsuspecting [teenager]s?"
            s "I don’t really do anything like this, no. Knowing how arcade machines work is kind of just ingrained into the lower middle class, I guess."
            to "I see. "
            to "If only they could find that same level of ingrained passion for exercising or eating anything other than junk food."
            s "Yeah, if only."
            s "Anyway, do you want to give this a try? It’s a fighting game, so you can just mash a bunch of those buttons and hopefully hit me or something."

            scene tsukiokaarcade16
            with dissolve

            to "Yes! That sounds wonderful."
            to "Let’s see...um...start!"

            "Touka slams down on the start button and finally makes it past the opening menu."
            "A fit of paid applause rings out in the distance as she conquers what is probably the biggest challenge she has faced to date."

            to "Please go easy on me, Sensei. It is my first time and I don’t know what I’m doing."
            s "Can you say that again, but with direct eye contact and a slightly redder face?"

            scene tsukiokaarcade17
            with dissolve

            to "Ha ha ha. Sexual harassment is no joke, Sensei. "
            s "Then why did you just laugh?"
            to "Because that...wasn’t a real..."

            scene tsukiokaarcade18
            with dissolve

            to "You know what?! I do not need to defeat you with words! I will defeat you in combat instead!"
            to "Engarde!"
            s "You haven’t selected a fighter yet."
            to "How do I do that?"
            s "Just move your joystick until the character you want to play as is highlighted. Then hit one of the two buttons you’re hovering over."
            to "Okay. But if this is a trick and your method causes me to lose before the game even begins, I will be incredibly upset with you."
            s "This is one of the rare times I’m actually being honest. "

            "Touka cycles through all of the characters for a moment while I just select the “Random” option since I have no idea how any of them work and don’t really care."
            "Eventually, she makes up her mind and slams down on the button with way too much vigor, prompting the round to start."

            to "{i}Now{/i} engarde!"
            to "How do I attack? Which of these two buttons inflicts the most pain upon my enemy?"
            s "Well, you’re going to want to walk over to my character first."
            to "Which one is your character?"
            s "Literally the only other character on the screen besides yours."
            to "I see. Do not move. I am coming to eliminate you."
            s "..."

            "Touka eventually manages to move her character over to mine and stops him dead in his tracks before actually attacking."

            scene tsukiokaarcade19
            with dissolve

            to "Do you have any last words, Sensei?"
            s "Yes. Are we actually fighting? Or am I supposed to stand here and let you kill me?"
            to "Do you think you can defeat {i}me?{/i} Touka Tsukioka of the esteemed Tsukioka family?"
            to "I have practiced a bit of Judo, you know. I was never very good, but I do believe it will give me a bit of an advantage when it comes to-"

            scene tsukiokaarcade20
            with dissolve

            to "Wait! What was that noise?! What happened to my little green bar at the top of the screen?!"
            s "I punched you while you weren’t looking. "
            to "The {i}audacity!{/i} How dare you!"

            scene tsukiokaarcade21
            with dissolve

            to "Hi-yah!"

            "Touka presses one of her buttons and manages to punch my character as well."
            "This means war."

            to "Hi-yah! Hi-yah! Hi-"
            to "Wait. No. Stop it. Let me hit you. My flurry of blows is not yet complete."
            s "I’m good. I don’t really like losing."

            scene tsukiokaarcade22
            with dissolve

            to "And you think {i}I{/i} do?! Absolutely not! I will not be defeated by my-"
            s "You just lost."

            scene tsukiokaarcade23
            with dissolve

            to "Already?!"
            to "You liar! You heathen! You’re an expert at video games, aren’t you?! Is this what it means to be hustled?!"
            s "No. This is what it means to stop paying attention when you’re competing against someone."
            s "You let your guard down and I just took advantage of that."

            scene tsukiokaarcade24
            with dissolve

            to "But my character was so much larger than yours. He should have been able to live for much longer than that."
            to "This game is entirely unrealistic. "
            s "You know, I think you’re going to find that that’s a recurring aspect of video games. The vast majority of them don’t really pride themselves on their realism."

            scene tsukiokaarcade25
            with dissolve

            to "I demand a rematch immediately. I refuse to leave this machine until I defeat you. "
            s "But we could be here for years."
            to "Nonsense. I just need several more rounds to familiarize myself with the form of martial arts my character uses."
            to "I will be mopping the floor with you in no time at all, good Sir."
            s "Sure thing, Touka. Whatever you say."

            scene black
            with dissolve2

            "Touka and I proceed to play several more rounds of the fighting game. "
            "Then several more."
            "Then...several more."
            "She is very, very bad. Even by beginner standards."
            "Eventually, I get so tired of winning that I put on an act to make it seem like she defeats me fair and square, freeing me once and for all from my prison of incessant victory."
            "And while it does hurt my pride a bit losing to Touka (Even if it’s on purpose), that pride is quickly healed by the sight of her literally jumping for joy."

            if bonus == True:
                "I curse whatever innovations in fashion manage to keep her dress secured to her chest before sighing to myself and returning to the center of the arcade."
            else:
                "I am so glad that I was able to make her happy."

            "........."
            "......"
            "..."

            $ toukaarcade = True

            if toukaarcade == True and tsubasaarcade == True and tsukasaarcade == True:
                jump endoftoukaarcade
            else:
                jump tsukiokaarcade

        "Tsubasa" if tsubasaarcade == False:
            scene tsukiokaarcade26
            with dissolve2

            "I make my way over to Tsubasa at the bar and feel very proud of myself for once again actively seeking out someone closer to my age group."
            "Honestly, though, Tsubasa isn’t really that different from Touka in...any way whatsoever. So it’s kind of just like hanging out with Touka 2.0. "
            "Or...1.0 depending on your preferences, I guess."
            "Either way, I take my place beside her at the bar and order a beer that, hopefully, Tsubasa will pay for on account of both her immense wealth and the invasion of what was supposed to be a thing for Touka and me."

            tb "Well, hello there."

            if toukaarcade == True:
                tb "Does this mean you and Touka are done {i}combating{/i} one another?"
                s "Yes. Though, I did have to take a dive in order to get away."
                s "She refused to leave the machine until she beat me and she is incredibly bad at video games."
                tb "Look at you, taking a fall to please a young girl. How noble."
            else:
                tb "I’m a little surprised to see you come over to me before Touka. What with me intruding on your little “field trip” and whatnot."
                s "It is what it is. I don’t really care one way or the other."

            s "I’m honestly kind of surprised you even wanted to tag along for this. It doesn’t really seem like a thing you’d be into."
            tb "Well it’s not as if I {i}knew{/i} what I’d be getting into. But I doubt I would have refused even if I’d known where we were going from the start."

            scene tsukiokaarcade27
            with dissolve

            tb "This may come as a bit of a surprise to you, but I don’t particularly “get out” often."
            s "{i}What? No.{/i}"
            tb "Okay. So it might be {i}overwhelmingly apparent{/i} that I don’t get out often. "

            scene tsukiokaarcade26
            with dissolve

            tb "But that doesn’t mean I’ve always been this way."
            tb "I used to do a fair bit of “sneaking away” when I was Touka’s age, you know. And that led to all sorts of wild experiences."
            s "How wild are we talking here?"

            scene tsukiokaarcade28
            with dissolve

            tb "Hahah~ Maybe {i}wild{/i} wasn’t the right word, exactly. I’m sure it was really nothing compared to what [teenage]girls are doing nowadays."

            scene tsukiokaarcade26
            with dissolve

            tb "But for my girlfriends and I, it was wonderful. And I often wish those experiences weren’t so few and far between when looking back on them."
            tb "It oftentimes feels that I may have...wasted away my youth to some extent."
            tb "Coming from a wealthy family is certainly an advantage in life, but that doesn’t mean it’s without its setbacks."
            s "Well, at least you’re getting to experience more of {i}this{/i} life now."

            scene tsukiokaarcade29
            with dissolve

            tb "True. But {i}this{/i} is only happening because I followed my daughter out. It’s not really a thing I’d be able to do on my own with my lack of knowledge or...connections outside of the business world."
            s "Well, you’ve got me. I’m outside of the business world."

            scene tsukiokaarcade30
            with dissolve

            tb "Careful, Sensei. Saying it that way makes it sound like we might be {i}friends.{/i}"
            s "I mean...we {i}can{/i} be?"

            scene tsukiokaarcade31
            with dissolve

            tb "We...can? You and me? But we have virtually nothing in common."
            tb "And Touka’s already advised you that I don’t have much time to really do things with her- let alone someone outside of the family."
            s "Sure. And I’m not really expecting that to change. Just letting you know that there is {i}someone{/i} outside your circle of insanely rich people who wouldn’t mind spending time with you."

            scene tsukiokaarcade32
            with dissolve

            tb "That’s very kind of you. And..."
            tb "And perhaps I {i}will{/i} take you up on that sometime."
            tb "It’s been years since I’ve “snuck away” for anything. Just thinking about doing something like that again is actually getting me quite excited."
            tb "Perhaps we should share contact information?"
            s "Sure. But only as long as you can promise me your husband isn’t going to use his citywide influence to spy on us or tap your phone."

            scene tsukiokaarcade27
            with dissolve

            tb "Or perhaps it would be best if we didn’t share that information with one another at all."
            s "..."

            scene black
            with dissolve2

            "I realize soon after that Tsubasa is [[probably] just kidding and the two of us swap numbers."
            "I chug down my beer as soon as it arrives and, just like I wished, Tsubasa offers to pay for it."
            "Here’s hoping that whatever sorts of things the two of us do when she manages to sneak out are worth the price of that."
            "And, if they’re not, I’m even more boring than I thought."
            "Either way, I make my way back to the center of the arcade and begin to look around and see if there’s anything else I’ve missed..."
            "........."
            "......"
            "..."

            $ tsubasaarcade = True
            $ tsubasanumber = True

            if toukaarcade == True and tsubasaarcade == True and tsukasaarcade == True:
                jump endoftoukaarcade
            else:
                jump tsukiokaarcade

        "Tsukasa" if tsukasaarcade == False:
            scene tsukiokaarcade33
            with dissolve2

            "For some reason that I don’t fully understand, I make my way over to Tsukasa at some tabletop arcade machine."
            "She stops fiddling with a joystick in a compartment underneath the table long enough to look up and lock eyes with me."
            "Through the harsh judgment and pity and disgust and a bunch of other things I can tell she is feeling regarding my existence as a human, however, I can tell she needs help."

            tk "I need help."

            "This is subsequently confirmed."

            s "What do you need help with?"
            tk "Everything."
            s "That’s too many things."
            tk "I don’t know how to get this game to work. Or what the pig killing game even looks like."
            tk "Or where we are or what the song on the radio is or who I need to talk to for a glass of water."
            tk "So, yeah. Everything."
            s "Sucks to be you, I guess."
            tk "Hey. Do you wanna be my new butler? The one I have right now knows nothing about peasant life, so our interests really aren’t aligning at this current point in time."
            s "I don’t think I’d make a very good butler."
            tk "Why not?"
            s "Because I am bad with children and you seem...extremely high maintenance."

            scene tsukiokaarcade34
            with dissolve

            tk "I probably am. But wouldn’t living in a giant mansion and getting your own swimming pool and pretty much anything else you want make up for that?"
            s "This offer suddenly sounds a lot more interesting."
            tk "Is that a yes?"
            s "I’ll have to consult with my business partner. Who also happens to be my [niece]. If I move out, she’ll probably die."

            scene tsukiokaarcade35
            with dissolve

            tk "Oh well. One less mouth to feed."
            s "Tsukasa, why are you...the way you are?"

            scene tsukiokaarcade36
            with dissolve

            tk "You mean awesome?"
            s "I mean awful."

            scene tsukiokaarcade37
            with dissolve

            tk "That’s not a very butlery thing to say, Jeeves."
            s "My name isn’t Jeeves."
            tk "It is now. All of my butlers are named Jeeves. It’s the most butlery name. You have to fit the role."
            s "I haven’t even agreed yet."
            tk "What do you mean you haven’t agreed? I’m Tsurumikasa Tsukioka. You have to listen to me or I’ll hire a team of assassins to...well, assassinate you."
            s "I suppose that is a bridge I’ll cross when I come to it."
            tk "Hm..."
            s "What do you mean “Hm?”"
            tk "I’m just trying to figure out why my sister likes you so much. You seem pretty boring and lame to me if you don’t even want to come live in a fancy mansion."
            s "Has Touka really told you she likes me?"
            tk "Mhm. She says you’re the best teacher she’s ever had. But she’s never really liked any of her other teachers, so I guess that’s not saying much."
            tk "Either way, I don’t see it. If you were {i}my{/i} teacher, I would have fired you by now. But I fire all of my teachers so, again, that’s not saying much."
            tk "Can you teach me how to play this game now?"
            s "Immediately after insulting me?"
            tk "Well, who else is gonna teach me? {i}Someone{/i} has to."
            s "Just figure it out on your own like you did with the subway. It’s really not that hard."
            tk "I don’t want to figure it out on my own. I want you to teach me."
            s "But I’m an annoying, boring commoner."
            tk "You are. But it’s no fun doing things on my own. And Papa won’t teach me things like this because of how they’re bad for me."
            tk "In fact, he doesn’t really have time to teach me anything anymore."
            tk "So that’s why I want you to do it."
            tk "It would be better if you were my butler, but I have to take what I can get at this point. Good help is hard to come by around here."
            s "..."
            tk "..."

            scene tsukiokaarcade38
            with dissolve

            tk "Jeez! Hasn’t anybody ever told you that time is money?"
            tk "No wonder you’re so poor if you’re just going silent in the middle of conversations like that."
            s "If I teach you how to play this game, you’re going to owe me a favor in the future."

            scene tsukiokaarcade39
            with dissolve

            tk "A trade offer? I can do that."
            tk "What are you after? A luxury car? One of Touka’s horses? Name it and it will be yours."
            s "I don’t know what I want yet. I just think it will be useful for a person of your status to owe me a favor that I can call upon when I need it most."
            tk "Like if you have to bury a body?"
            s "What? No. I-"

            scene tsukiokaarcade40
            with dissolve

            tk "Say no more. I agree to these terms and will help find you an experienced burial crew the moment you need it."
            s "Tsukasa-"
            tk "Silence. The terms have been accepted. The deal is complete."

            scene tsukiokaarcade41
            with dissolve

            tk "Now, let’s play, Jeeves!"

            scene black
            with dissolve2

            "I spend a few minutes learning how to play the tabletop game so I can teach Tsukasa, and it’s easy enough that we’re both able to pick it up without any issue."
            "It’s multiplayer as well, so I’m able to stay on the opposite side of the table and play against her once we have things figured out."
            "Surprisingly, she’s actually pretty good at it. But I guess reflexes are better when you’re young and...well, she {i}is{/i} allegedly some sort of gifted kid."
            "I get tired of playing eventually, though, and decide to head back to the center of the arcade."
            "As I leave, I spot Tsukasa frowning out of the corner of my eye."
            "........."
            "......"
            "..."

            $ tsukasaarcade = True

            if toukaarcade == True and tsubasaarcade == True and tsukasaarcade == True:
                jump endoftoukaarcade
            else:
                jump tsukiokaarcade

label endoftoukaarcade:
    $ renpy.end_replay()
    $ toukaspecial15p2 = True
    $ touka_love += 1
    $ tsubasa_love += 1
    $ tsukasa_love += 1

    "{i}Your affection with the entire Tsukioka family has increased by 1!{/i}"

    jump toukaspecial15p3

label toukaspecial15p3:
...
```

## Code that triggers this event
File: \game\ToukaEvents.rpy
Code:
```python
...
to "As a special thanks for your assistance, I’ll be sure to purchase you a seat as well, Sensei."
    s "Thanks, Touka. If you could also get me a drink from the cooler in the conductor’s room, it would be greatly appreciated as well. They’re complimentary, so you won’t have to pay."
    to "Of course. Does green tea sound okay?"
    s "Perfect, actually. Thanks, Touka."
    to "My pleasure."

    scene black
    with dissolve2

    "........."
    "......"
    "..."
    "{i}Five minutes later...{/i}"

    scene toukatrain25
    with dissolve

    to "Oh {i}good.{/i} You managed to sit down without your {i}seating ticket.{/i}"
    s "Yeah. I forgot they aren’t needed on the weekends. My bad."
    to "Does tormenting me truly cause you enough joy to warrant continuously doing it? Do you not get bored of having me make a fool of myself?"
    s "It does and not really."

    scene toukatrain26
    with dissolve

    to "Hah...Well, I suppose it’s over now. All there is left to do is ride this train until Tsukasa decides it’s time to get off."
    s "Pretty sure that will be the next station. She doesn’t seem as thrilled as she expected to be among her beloved poor people."
    to "Yes, but did you truly expect her to be? She’s even more spoiled than I am and I have a helicopter with my name painted on it."
    s "{i}Why?{/i}"
    to "It was a present for my tenth birthday."
    s "{i}Why?{/i}"

    scene toukatrain27
    with dissolve

    to "Why do you think, Sensei? Because I’m lucky...and happened to be born into a family that had already carved out a sizable part of this world."
    to "I have many things that others could only dream of due to no hard work or...work {i}at all{/i} on my own."

    scene toukatrain28
    with dissolve

    if bonus == True:
        to "I’m a [teenage]girl on the cusp of becoming a woman and I don’t even know how to ride the subway or...what the other girls in my class do to celebrate their summer vacations."
        to "I’m entirely hopeless when torn out of my element."
        to "And yet all you do is toy with me."
    else:
        to "I just wish I had more than five years left to live..."

    s "..."
    to "..."
    s "Sorry. Did you say something? I wasn’t paying attention."

    scene toukatrain29
    with dissolve

    to "Rude. I was attempting to have a moment with you."
    s "I don’t normally “have moments” with girls when their mothers are sitting directly beside them."
    to "Well I apologize for being the bearer of bad news, but my mother is a very big part of my life."
    to "And if you and I are going to continue spending time with one another, I can only hope that {i}she’ll{/i} have the time to be there for some of it."
    to "It’s just something you’ll have to accept. Like how {i}I’ve{/i} accepted you’re a tasteless hack who couldn’t tell a salad fork from a soup spoon."
    s "Is the spoon the pointy one? My small, proletarian brain can’t quite remember."

    scene toukatrain30
    with dissolve

    to "Mhm! So the next time the maître d’ asks you if you’re missing anything and you notice a distinct lack of pointed utensils, make sure to ask for a new spoon."
    s "You have a long way to go if you’re trying to trick me into doing the same sorts of things I trick {i}you{/i} into."
    to "Maybe for now."
    to "But that’s just because I’m still out of my element."
    to "You just wait until I drag you into {i}my{/i} lifestyle. We’ll see who truly struggles to adapt then."
    s "I didn’t really think you intended on dragging me into your lifestyle anytime soon, Touka."
    to "Neither did I. But the thought of seeing you suffer sounds a little too good to overlook anymore."

    scene toukatrain31
    with dissolve

    s "Well, it’s a weird sentence to say, but I guess I’m looking a little forward to whatever suffering you have in store for me."
    to "As am I..."
    s "..."
    to "..."
    to "You called me Touka again."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ touka_love += 1
    $ toukaspecial15 = True
    stop music fadeout 15.0

    "{i}Touka’s affection has increased to [touka_love]!{/i}"

    "We ride the subway to the end of the line after Tsukasa takes Touka’s earlier comment of “riding things out” to heart and wind up at a station that looks significantly different from the one we boarded from."
    "Wanting to stretch their legs and observe wherever it is we’ve wound up, the female members of the Tsukioka family exit the subway car and, after awkwardly looking around the station, head for a nearby staircase."
    "Once we get to the top, however, and a flood of multicolored light overtakes us- they realize just how out of place they are in this world."
    "........."
    "......"
    "..."

    jump toukaspecial15p2
...
```