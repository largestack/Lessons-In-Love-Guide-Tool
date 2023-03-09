# De-Briefing the Teacher
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=secondbeach3&go=Go)


Part of event chain [Egg Tossing](./secondbeach2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: secondbeach3
* Group: Main
* Triggered by label: secondbeach2

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label secondbeach3:
    scene secondbeachthree1
    with dissolve

    mak "Oh, good. You’re here. "
    mak "I was beginning to think you’d heard about my itinerary from someone else and were just avoiding me because you are immune to any form of actual planning."
    s "Quite the opposite, actually. As soon as Uta told me about your schedule, I basically ran the whole way over here."
    mak "Don’t lie to me, you incorrigible bastard. You hate schedules and you know it."
    s "I {i}do{/i} know it...but was the insult really necessary?"
    mak "Apologies. I didn’t get much sleep last night and am currently running on an unconfirmed amount of espresso shots."
    mi "I counted fourteen!"
    s "You are far too competent for someone running on fourteen shots of espresso. "
    mak "I’m sure that will all crash and burn momentarily. "
    mak "But there are several issues at hand here. "
    mak "First and foremost, welcome back to the beach. "
    mak "Given that our last trip was such a success, we’ve decided to make it an ongoing tradition for all twenty of us even after we’re inevitably placed into separate classes next year."
    s "Yeah, we’ll see about that."

    scene secondbeachthree2
    with dissolve

    mak "Oh, are you intending to switch grades? I hadn’t heard of that plan yet."
    s "Nope. "
    mak "But...then-"
    s "Don’t worry about it."
    mak "Well...in any case, the second thing I want to say before things get underway is-"
    s "Wait a second, Makoto. "

    scene secondbeachthree3
    with dissolve

    mak "Ugh. What now?"
    s "{i}Now{/i} I want to know why Noriko has been just standing here since I showed up and letting you do all the talking."
    n "Oh, don’t mind me. I’m just thinking about how one day, years and years after we’re married, we’ll come back here with all three of our little Nakayarakawayama babies and reminisce about the old days."

    if bonus == True:
        s "Thank you for keeping the amount of children to a reasonable level, but I will now return to focusing on Makoto as she has no intention of harboring my children."
        mi "I wouldn’t be so sure of that, Sensei!"
        mi "Makoto’s growin’ at a rapid rate and sooner or later those hips of hers will be perfect for poppin’ out a few four eyed babies of her own!"
    else:
        s "Noriko, stop. This is getting out of hand. You're in time-out now."
        mi "Hey! Did you guys know cows have four stomachs?! Crazy right?!"

    scene secondbeachthree4
    with dissolve

    mak "Thank you very much, Miku. I’m sure that was a thing everyone was interested in hearing."
    mak "Now, may I please-"

    scene secondbeachthree5
    with dissolve

    u "Nope! Cause now it’s my turn to talk to Sensei about beach stuff!"
    mak "Didn’t you literally walk here {i}with{/i} him? That should have been more than a sufficient amount of time to talk."

    scene secondbeachthree6
    with dissolve

    u "Makoto, Makoto, Makoto. You should know more than anyone that there can {i}be{/i} no sufficient amount of time with Sensei."
    u "I’m afraid I just can’t get enough of this guy and those big ole dreamy eyes of his."
    n "Watch your step, Uta. "
    mak "Right. Wonderful. "
    mak "You can have him all you like after I brief him on what the weekend will entail."

    scene secondbeachthree7
    with dissolve

    if bonus == True:
        n "And then I’ll {i}de{/i}-brief him, if you know what I mean."
        mak "I do. And not only is it rude but absolutely deconstructive to the actual briefing and-"
        mak "Oh. Wait. You meant like that."
        s "If anyone wants my opinion, I say we jump right to the de-briefing part."
        s "All in favor, please say aye."

        scene secondbeachthree8
        with dissolve

        n "Aye!"
        u "…"
        mak "…"
        i "…"
        mi "…"
        s "Really? No one else?"
        s "I could have sworn at least one of you would have jumped in."

        "Especially considering the fact that I have made both first floor residents in the room cum on at least one occasion each."

        mak "May I continue now? Or would you prefer to remain a pervert for a little while longer?"
    else:
        mi "I still wanna talk more about cows! I know so many cow facts all of a sudden!"
        mi "It is a fun new new character trait to hold people over until they actually learn something substantial about me!"
        mak "May I continue now? Or would you prefer to hear the cow facts?"

    s "I think you already know the answer to that, Makoto."

    if dormwarfloor1win == True:
        mak "Then, at the risk of further delaying our first day here, I’d like to take this opportunity to remind you about sleeping arrangements."
        mak "The Tsukioka family was kind enough to rent out the entirety of the inn for the weekend, so you {i}will{/i} have a room to yourself. "
        mak "However, as a result of the first annual Super Mega Ultimate Dorm War, you will be forced to stay with us first floor girls for at least one of two nights."
        mak "Which night would you-"
        s "Tonight. The sooner, the better."

        if bonus == False:
            s "I just want to get this horrible experience over with and hopefully retain my innocence."

        scene secondbeachthree9
        with dissolve

        mak "Well...as excited as I am to hear about your...excitement, I’d like to remind you that there may be no foul play whatsoever."

        if bonus == True:
            n "Stupid first floor. There would be {i}plenty{/i} of foul play in our room."
        else:
            n "Stupid first floor. I can't wait until the bomb I planted in there goes off later."

        s "Fair is fair, though. I’ll just spend the night playing board games or whatever it is Makoto has planned for me."
        mak "The sleepover itself isn’t planned. You’re free to do whatever you’d like there. "
        mak "I just don’t want you getting ahead of yourself in a room full of girls who like you far more than any student should like their teacher."
        s "Hey, you’re one of those girls."

        scene secondbeachthree10
        with dissolve

        mak "E...Even if I am, that doesn’t change the fact that this is an important rule that must be followed at all costs!"
        mak "Or at least at the risk of any future beach gatherings! I like this tradition and I want it to stay!"
        s "Is it really a tradition if it’s only happened once?"
        mak "To me, it is! "

        if bonus == True:
            mak "Now accept your fate and sleep with everyone on the first floor!"
            s "Well, when you put it that way..."
            u "I saw a vending machine near the entrance selling rubbers if you think you’ll wind up needing one or...ten."
            s "I won’t be needing {i}any{/i}, Uta. I’m-"

            scene secondbeachthree11
            with dissolve

            mak "Remaining abstinent for the weekend. And hopefully the duration of the[school] year."

            "I’m sure Makoto would be one of the first to crack if I actually had the moral compass to do such a thing."
            "So I’ll do her a favor by revoking said abstinence the second I have the opportunity to."
            "You can thank me later, Makoto."

        jump endofsecondbeach3

    if dormwarfloor2win == True:
        mak "Then, at the risk of further delaying our first day here, I’d like to take this opportunity to remind you about sleeping arrangements."
        mak "The Tsukioka family was kind enough to rent out the entirety of the inn for the weekend, so you {i}will{/i} have a room to yourself. "
        mak "However...as the result of the first annual Super Mega Ultimate Dorm War ended in favor of the girls on the second floor, you will be obligated to spend at least one night with them."
        mak "Which night would you-"
        s "Tonight. The sooner, the better."

        scene secondbeachthree12
        with dissolve

        mak "Ooof course."
        u "Heheh~ Can’t stay away, can ya?"

        if bonus == True:
            n "Greetings, Sir. I’d like to take this opportunity to invite you to get up close and personal with your estranged semi-imouto in a futon clearly sized for only one person."
            n "If you close your eyes, you can even pretend I’m my sister. I really don’t care."
            n "Just kidding. I do care."
            n "Please love me."
        else:
            s "No, I just want this to be over as quickly and painlessly as possible."
            n "FUCKING. HUG ME. RIGHT NOW. I CAN'T TAKE IT ANYMORE."

        scene secondbeachthree13
        with dissolve

        u "Chill, girl. The sleepover hasn’t even started yet."
        n "Sorry. I-"

        scene secondbeachthree14
        with dissolve

        n "Waaaaaaait a second..."
        u "...What?"

        if bonus == True:
            n "You just wanted to be invited in too, didn’t you?"
        else:
            n "You said offscreen earlier that the sleepover {i}has{/i} started and that this is just the first part of it."

        scene secondbeachthree15
        with dissolve

        u "Wha-"
        u "No! That’s obviously not what I meant!"

        if bonus == True:
            n "Okay, Sensei. You can snuggle with Uta {i}and{/i} me in my futon. But I get first dibs."
            u "Noriko!"
            mak "No one is getting {i}dibs{/i} on anyone."
            mak "Even if the second floor is prepared to be a madhouse, I have selected an operative from there who will be ensuring there is no {i}foul play{/i} involved."
        else:
            mak "This really isn't the time for semantics, you two."
            mak "Now, at the risk of being interrupted, I'd like to inform you all of the secret operative I have chosen to keep an eye on everything tonight."

        s "Right. And who is that operative, Makoto?"

        scene secondbeachthree16
        with dissolve

        mak "Kirin was more than willing to lend a hand in ensuring that the impending sleepover would remain as wholesome as possible."

        "Oh, Makoto. So smart, yet so dumb."

        jump endofsecondbeach3

    if dormwartie == True:
        mak "Then, at the risk of further delaying our first day here, I’d like to take this opportunity to-"

        scene secondbeachthree17
        with dissolve

        u "Wait! "
        mak "What now? This is honestly getting extremely annoying."
        u "We’ve still gotta do the coin toss thingy, right? To see where Sensei is spending the night."
        s "Coin toss?"

        scene secondbeachthree18
        with dissolve

        mak "It was the only entirely fair way we could come up with to decide the final winner of the dorm war’s grand prize."
        mak "Unless you’re fine with just spending both nights in your own personal-"
        s "Hell no. Flip that coin, Makoto. Let’s see what fate has in store for me now."

        scene secondbeachthree19
        with dissolve

        mak "Hopefully it’s a muzzle."

        scene black
        with dissolve

        "Makoto removes a coin from her pocket and steps aside so there’s no risk of flipping it onto the table and then having either Miku or Io run away with it and buy a soda or something."
        "That or slyly position the coin onto whichever side favors them...but that would probably require an intense amount of talent in sleight of hand or-"
        "You know what? Makoto goes to flip a coin."
        "Watch."

        scene secondbeachthree20
        with dissolve

        mak "So...at long last, we’ll finally be able to settle this."
        mak "The battle to decide which floor is truly the superior one..."
        u "I mean, technically the superiority thing ended in a tie. This is just a tiebreaker to see who gets the prize."
        u "Both floors are equally adorable and awesome."
        mak "Except for floor two, which {i}sucks{/i}."

        scene secondbeachthree21
        with dissolve

        u "Why are you being so mean all of a sudden?"
        mak "Sleep deprivation. I can’t help it."

        scene secondbeachthree22
        with dissolve

        mak "But that doesn’t matter! "
        u "My feelings certainly {i}do{/i} matter, Makoto."
        mak "But what matters more is deciding the winner!"
        mak "If the coin lands on heads, you’ll be staying with the first floor."
        u "Which means if it lands on tails, you’re gonna be with us!"
        mak "How do you want me to flip it, Sensei? Hard or soft?"

        if bonus == True:
            s "Can you ask again but without the “flipping it” part?"
        else:
            s "Can I phone a friend? I don't know how to answer."

        mak "Fuck you. Hard or soft."
        s "Ugh. I guess..."

        menu coinflipbeach:
            "Flip it hard":
                s "Flip that coin like you’ve never flipped a coin before."
                mak "...What?"
                s "Just...flip it hard."

                scene black
                with dissolve
                play sound "coinflip.mp3"

                "Makoto tosses the coin high in the air and everyone in the room watches in anticipation as fate decides where I will spend the night."

                scene beachheads
                with dissolve
                $ dormwarfloor1win = True

                mak "It’s heads! The first floor wins!"
                n "FUCK!"
                u "Aww man..."

                scene secondbeachthree23
                with fade

                mak "FUCK YEAH! EAT SHIT, SECOND FLOOR!"
                u "Jesus, Makoto. Isn’t that taking it a little too far?"

                scene secondbeachthree24
                with dissolve

                mak "Oh my. I’m sooo sorry, Uta."
                u "You don’t have to apologize, just don’t be that mean next-"

                scene secondbeachthree25
                with hpunch

                mak "SORRY FOR KICKING YOUR ASS! HA!"
                u "…"
                n "…"
                mak "…"

                scene secondbeachthree26
                with dissolve

                mak "{i}Ahem...{/i} "
                mak "So, it appears that Sensei will be sleeping with the girls of the first floor."
                mak "Now, onto the next order of business..."

                jump endofsecondbeach3

            "Flip it soft":
                s "Just drop it and see what happens."
                mak "I’m not going to just {i}drop{/i} the coin. It needs to be flipped."
                s "Why?"
                mak "Because it..."
                mak "It does."
                mak "Screw you, I’m flipping it softly."

                scene black
                with dissolve
                play sound "coinflip.mp3"
                $ dormwarfloor2win = True

                "Makoto lightly tosses the coin in the air and everyone in the room watches in anticipation as fate decides where I will spend the night."

                scene beachtails
                with dissolve

                u "Ahh! Tails! We win! We win!"
                n "God is real! He has blessed us!"
                i "Uhh...yaaaay..."

                scene secondbeachthree27
                with fade

                u "Heh heh heh..."
                u "It appears that what fate wants is for Sensei to grow a little closer to all of us who didn’t get a head start."
                u "I’d like to take this opportunity to thank my mom and dad. If it weren’t for them, I don’t know if I would have ever gotten the courage to stand up here and accept this honor today."
                mak "Oh, please. It was just a coin flip."
                mak "If you really want {i}fate{/i} to decide, you’ll do two out of three."

                scene secondbeachthree28
                with dissolve

                u "Nice try, Makoto. But I ain’t the type to fall for such silly little games."
                u "Now be a good girl and accept that you really are part of the inferior floor after all."
                mak "But...but you said-"
                u "Hey, your words. Not mine. "
                u "I was more than willing to do this nicely."

                if bonus == True:
                    n "I’ll put our futon in the corner of the room so nobody has to step over us and we can get as close as we want."
                    mak "A-Again! There will be no inappropriate conduct of any sorts!"
                    n "It’s only inappropriate if one of us doesn’t consent. Otherwise, it’s totally fine."
                    mak "That is not how[school] trips work, Noriko!"
                    u "Yeah yeah yeah. Just get on with the rest of your schedule thingy so we can start plannin’ our night of fun with our teacher."
                    mak "Ugh! This is ridiculous..."
                else:
                    mak "Ugh. Whatever. Just let me get to my schedule."

                jump endofsecondbeach3

label endofsecondbeach3:
    scene black
    with dissolve2

    "Makoto removes a notebook from a bag she’d left near the door and takes her place beside Uta against one of the paper walls of the inn."
    "I can already feel that I’m going to hate whatever is coming, but I’ll at least try and give her the benefit of the doubt and listen since she’s clearly spent a good amount of time preparing for this."

    scene secondbeachthree29
    with dissolve

    mak "So, since this {i}is{/i} a beach trip in the middle of winter, I’ve decided that it would be in everyone’s best interest if we were to completely forego swimsuits as a whole."

    if bonus == True:
        s "As in...walk around naked?"
    else:
        s "What exactly do you mean by that, hug buddy?"

    scene secondbeachthree30
    with dissolve

    mak "As in remain in either our casual clothes or our pajamas for the duration of the weekend."
    s "This idea sucks."

    if bonus == True:
        "I tried to give Makoto the benefit of the doubt and was immediately let down."
        "This is why I can’t trust anyone."
    else:
        s "I say we all wear raincoats instead. You never know when the rain will come."

    mak "This idea, if executed properly, will keep essentially all of us perfectly healthy."
    mak "If we get sick, we’re unable to come to[school]. And that reflects poorly on not only you, but on me as your classroom assistant and-"
    s "Yeah, yeah. Next rule, please."
    mak "…"
    s "…"
    mak "The next rule is that if anyone needs to use the restroom, they should sign out on the sheet I provided or, at the very least, go with a partner so that we do not wind up losing any-"

    scene secondbeachthree31
    with dissolve

    u "Makoto. I’m gonna say this as nice as I can."
    u "These rules suck."
    mak "I...beg your pardon?"

    scene secondbeachthree32
    with dissolve

    u "What happened to the fun Makoto we had during the dorm war?"

    if bonus == True:
        u "We’re all [teenage]girls. We can’t be lettin’ ourselves get bogged down by...bathroom sign out sheets and curfews."
        mak "But I didn’t mention curfews..."
        u "You were gettin’ there, weren’t ya?"
        mak "…"
        mak "Yes..."

    u "All I’m sayin’ is just let us be girls for a day or two. And you be a girl yourself."
    u "Paint your nails. Eat a croissant. You know...girl stuff."
    mak "I...was unaware up to this point that croissants were exclusive to girls."
    s "Damn it. I like croissants, too."
    u "Just have fun! "
    u "If you’re relaxed, we’re all relaxed!"
    u "And if we’re all relaxed, we’ll be able to look back on this trip with smiles on our faces."
    mak "…"

    scene secondbeachthree33
    with dissolve

    mak "Hah...you’re right."
    mak "I knew I was going too far with this."
    mak "I just figured that if we were going to have a second chaperone this year that it would be good to lay out a few more ground rules and-"
    s "Wait wait wait."

    scene secondbeachthree34
    with dissolve

    mak "Why why why?"
    s "What do you mean “second chaperone?”"
    s "You’re not counting yourself, are you?"
    mak "Of course not."
    mak "The second chaperone is Miss Watabe."
    mak "And from what I understand, her significant other is-"

    scene secondbeachthree35
    with hpunch
    play sound "thump.mp3"

    no "GO GO GO GO GO!"
    u "Geh. Heckin' Christ."

    scene secondbeachthree36
    with dissolve

    no "Freeze! Yuri police!"
    mak "Yuri...police?"
    no "Word on the street is you punks are harboring a refugee by the name of Wakana Watabe!"
    no "Where is she located?!"
    mak "I don’t know. She likely hasn’t gotten-"

    scene secondbeachthree37
    with hpunch

    no "I SAID WHERE IS SHE LOCATED, DAMN IT?!"
    s "Hey, Nodoka. Thank you for wearing a swimsuit."

    scene secondbeachthree38
    with dissolve

    no "Thank you. I am feeling awfully cute today."
    s "Thank you as well, Otoha."

    scene secondbeachthree39
    with dissolve

    o "Well...you know. Beach."
    o "I kind of didn’t think I’d be wearing this at all with how cold it is, but I am apparently now a member of the yuri police and...this is the uniform or something."
    no "Looks like I’m going to need to search the room."

    if bonus == True:
        no "And also privately pat each one of you down."
        no "Except for Noriko. She’s too eager and it turns me off."
        n "And here I was ready to invite you to the futon snugglefest."

    no "Otoha. Hold down the living room. "
    no "I’m starting the search with their leader."
    o "Uh-huh. Right."

    scene black
    with dissolve

    mak "Nodoka! How many times do I have to tell you that I am not interested in women?!"

    if bonus == True:
        no "Apparently more because I do not believe you!"
    else:
        no "Being the chief of the yuri police doesn't mean that I am either!"
        no "Now, prepare yourselves for justice!"

    "Nodoka storms over to Makoto and does...Nodoka stuff."
    "But I use this opportunity to make my way over to Otoha and attempt to counteract the strangeness that has filled the room by talking to the most [[probably] normal person I know."

    scene secondbeachthree40
    with dissolve

    s "So..."
    o "…"
    s "I’ve always liked women in uniform."
    o "…"
    s "…"
    o "I’m gonna go ahead and forget you just said that, if that’s cool."
    s "I’m sorry. It was worth a shot."

    scene secondbeachthree41
    with dissolve

    o "I get it. I {i}did{/i} say it was my uniform, so I kinda set myself up for that one."
    s "I’m glad that we have reached an understanding so quickly."

    if bonus == True:
        o "Don’t really have a lot of time since I’m gonna get called on to pat somebody down any minute now."
        s "Doubtful. I imagine Nodoka would like to personally conduct her own strip searches of everyone in the room."
    else:
        s "Sometimes, I say things to try and make myself sound cool. But then I realize I'm not cool at all and just feel all embarrassed and stuff."
        s "Does that ever happen to you, Otoha?"

    scene secondbeachthree42
    with dissolve

    o "Yeah, probably."

    if bonus == True:
        o "That seems like..."
        o "...a thing she’d..."
    else:
        o "I'm kind of...naturally cool, though...so..."

    o "..."
    s "...?"

    scene secondbeachthree40
    with dissolve
    stop music fadeout 20.0

    o "Fuck it. Can you talk?"
    s "I’m talking right now."
    o "Privately. Before my...co-worker notices I’m gone."
    s "This is unusual."
    o "It won’t take long. Or at least I {i}hope{/i} it won’t take long. "
    o "Just...not really sure who else to talk to about this, so you’re gonna have to deal with it for a little while."
    o "Or you could just completely ignore me, forget I ever asked this, and I can figure shit out myself."
    s "No, I’ll come. Just...lead the way, I guess."
    o "I have literally never been here before and have no idea where I am going."
    s "Then just walk in a general direction and I’ll...walk behind you?"
    o "Or...next to me. Like a normal person."
    s "I guess that would be the normal thing to do, yeah."
    o "Yup."
    s "…"
    o "…"
    o "Okay. Gonna do that now."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ secondbeach3 = True
    jump secondbeach4

label secondbeach4:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
if bonus == True:
        y "‘Least Yasu won’t try to stick her tongue down my throat."
        s "I thought we weren't supposed to joke about that?"
        y "{i}You’re{/i} not supposed to joke about that."
        y "I can do whatever the fuck I want."
    else:
        y "Literally everyone is better than that freak and her fucking...airplane noises or whatever."
        s "(Airplane noises)"
        y "Nevermind. Maybe some people aren't any better at all."

    "More time goes by."

    scene secondbeachintro27
    with dissolve

    "Yumi leaves."
    "I don’t chase after her this time."
    "I figure that it’s a good move in letting her believe that she “can do whatever the fuck she wants” when I know for a fact that is false."
    "The only person who can do everything they want is me."
    "And, I guess to some extent- Maya."
    "But she’s too wrapped up in Maya things to exert any form of effort on that front."
    "Basically, those of us with an unlimited amount of time and the knowledge of such a gift may do whatever it is we desire."
    "Yumi may {i}try{/i} to do whatever she wants, but she’s closer to that of an unsuspecting mother bird than a fledgling cuckoo."
    "She’s far too busy ignoring the things she knows in her heart to be true to make an effort to push anything else aside for her own well-being."
    "And yet she pushes everything aside anyway."
    "But why?"
    "…"
    "Oh, right."
    "Because that’s all she ever learned how to do."
    "…"
    "If only I could teach her how to be more like me."
    "To toss other eggs outside of the nest."
    "And thrive in an environment you simply don’t belong in."

    scene black
    stop music

    "I have no time for such troubling thoughts."
    "I should be having fun."

    scene secondbeachintro28
    play music "justbehappy.mp3"

    "I arrive at fun."

    u "Sensei! Good timing!"
    u "Me and Io just got here and have no idea where the heck this resort thingy is supposed to be."
    s "It’s not really a “resort thingy.” It’s just kind of a small beach inn that we rented out a few rooms for."
    s "And by “we” I mean Ayane and probably Touka."
    s "As much as I like this, I absolutely would not pay for it."
    i "Do you have your own room, Sensei? Or are you going to be sleeping with the girls the whole weekend?"
    s "If I have my own room, are you going to sneak into it in the middle of the night again?"

    scene secondbeachintro29
    with dissolve

    i "Mhm. So be careful when you get out of bed so you don’t wind up breaking my leg again. It just healed."

    if bonus == True:
        u "Yeah yeah yeah. Keep it in your friggin’ pants."
    else:
        u "Yeah yeah yeah. Get a room."
        s "That...is what we're talking about, though."

    scene secondbeachintro30
    with dissolve

    u "Now take us to the heckin’ beach resort inn thingy so I can eat my breakfast and listen to whatever it is Makoto’s tryin’ to tell me about."
    s "Is she looking for you too?"
    u "She’s been textin’ me all morning about a stupid schedule thing."
    u "Apparently managin’ {i}one{/i} stinkin’ dorm war was enough for her to make me the supreme leader of the second floor. Now I’m in charge of friggin’ everybody."
    u "Ya have any idea how hard it was gettin’ Io to agree to this? Your girl is tired, Sensei. So friggin’ tired."

    scene secondbeachintro31
    with dissolve

    s "Well, whatever you did, I’m glad."
    s "I was just thinking about how I need to have more fun, and there’s certainly never a dull moment with either of you two around."
    i "You know what would be really fun? If we all-"
    u "No amusement park, Io. One step at a time."
    i "…"
    s "…"
    i "Nevermind."

    scene black
    with dissolve2

    "I scan the beach to see if anyone else is around and quickly find that either everyone is already here or we were just way earlier than I thought we were today."
    "Either way, I'm unable to find anyone and wind up showing Uta and Io the way to the inn."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ secondbeach2 = True

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "………"
    "……"
    "…"

    jump secondbeach3
...
```