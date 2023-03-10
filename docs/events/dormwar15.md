# Fallen Angels (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [The Scary Room](./dormwar14.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwar15
* Group: Main
* Triggered by label: dormwar14
* Chain sources: dormwar14
* Chain sources path: dormwar14

## Official wiki page

[Fallen Angels](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar15&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label dormwar15:
    "{i}One hour later, at Sara’s bar...{/i}"

    scene fashionshow1
    with dissolve
    play music "letsfuckingo.mp3"

    "I wind up getting a ride to the bar from...someone employed by the Tsukiokas after our dinner comes to an end."
    "Touka, not wanting to show her extraordinarily revealing dress to the rest of the girls in her class, heads back home to get changed before coming back for the “final” contest of the dorm war."
    "And I say “final” like that because I still have no idea what Yumi and Io are doing. "
    "But I’ve been told this is the last contest, so...I’m just going to believe it because that makes everything significantly easier."

    if bonus == True:
        "Also, look- people my age."

    s "Hello, fellow adults."
    maki "Greetings, human male. Will you be partaking in any of the alcohols today?"
    h "I’m already buzzed so I’m just going to talk like an actual person, if that’s okay with you guys."
    s "Works for me. How long have you two been here?"
    maki "Maybe an hour or two? "
    maki "Makoto told me that the final part of the dorm war was going to take place here, so I figured I’d be a good adult and watch over everyone as they get intoxicated."
    maki "While also getting partially intoxicated myself because, come on. Wine is good."

    if bonus == True:
        h "How’s the whole contest for your body thing going?"
        s "I just got back from a date with a girl who is far too developed for her age, so pretty good."

        scene fashionshow2
        with dissolve

        maki "Yeah, what’s the deal with that? How come girls now are growing up so quickly and we were total dweebs at their age?"
        h "I don’t know, but..."
        h "I’m probably not drunk enough to really share my full thoughts on that matter right now."
        maki "Just drink more then. I’ll drive you home."
        h "Please don’t get me drunk. I have to work in the morning."
        maki "But if I don’t get you drunk, how am I supposed to take advantage of you?"
        s "Oh, right. You two are lesbians when you drink."
    else:
        h "How’s the whole contest thing going?"
        s "Good. I made $20."
        h "Nice. Maki and I are about to go to Taco Bell."

    scene fashionshow3
    with dissolve

    maki "You’re free to come if you’d like! Just leave several minutes after me so Makoto doesn’t think I’m going home with her teacher."
    s "That sounds great...but I don’t think I’m really allowed to leave tonight."
    h "Yeah, you’re judging some...what was it? A fashion show, I think?"
    s "Is that what’s going on? How do you know that?"
    h "Molly told me about it. She was complaining about not being able to find enough fabric or something."

    if bonus == True:
        "Damn it. There goes the dream of the nude photo shoot I thought up yesterday."
        "Granted, I doubt Sara would let her daughter do something like that and-"
        "Actually..."

    mak "Attention, everyone! Please direct your attention to the front of the room!"

    scene fashionshow4
    with dissolve

    "I turn around to find Makoto and Uta standing on some stage they must have thrown together just for today."
    "I have no idea how these girls were able to coordinate such a well produced competition in less than 48 hours, but they do weird shit all the time, so I guess it makes sense."
    "Also, the world resets every few months and I can talk to birds. So there’s really no reason to question something like how quickly they could build a stage."

    u "Thank you to all who showed up to the main event of the first ever Super Mega Ultimate Dorm Wars!"
    u "It’s been a heck of a competition so far! Some friendships have been made, some have ended!"
    mak "As far as I know, there are no friendships that have ended. But if there are, please try to work out your differences!"
    u "That’s right, Makoto! The whole idea of this contest was bondage after all!"
    mak "{i}Bonding,{/i} Uta. "
    u "Same thing! Point is, I’m really glad we all got to spend so much time together...and I hope it means that we can all be better friends from now on!"

    if bonus == True:
        u "Oh, and whichever team wins Sensei is allowed to tie him up and stuff and he’s not allowed to say no!"
        s "Deal."

        scene fashionshow5
        with dissolve

        mak "Wait, you didn’t {i}actually{/i} mean bondage, did you?"
        mak "Because there are...many issues that would arise from that."
        maki "That’s my girl! Teach her all about the proper way to fasten harnesses, just like your momma taught {i}you{/i}!"
    else:
        u "Oh, and whichever team wins Sensei is allowed to paint his nails and stuff!"
        s "Deal."
        maki "Oh! Makoto loves nails!"

    scene fashionshow6
    with dissolve

    mak "Mom, stop! That’s not what I meant!"
    u "Hold onto your seats, gang! "
    u "In just a few minutes, we’ll have Sana and Yasu come out and show off their outfits!"

    if bonus == True:
        u "Then, Sensei will pick the one who he wants to take home and do weird stuff to the most!"
        n "Aaaaaaand that’s limited only to the two contestants, right?"
        u "Right! So keep your heckin’ pants on, Noriko! He ain’t your onii-chan anymore!"
        t "What sort of “weird things” is Sensei going to do to the winner of the competition?"
        a "Absolutely nothing if he knows what’s good for him."
    else:
        s "Yay! I'm so excited to see both of them, but on a strictly platonic level."

    sar "Sensei! How long are you going to wait before saying hi to me?"

    scene fashionshow7
    with fade

    s "I was on my way...There are just like six million people here."
    sar "I know! It’s the most business I’ve had in years!"

    if bonus == True:
        sar "I mean, sure, many of them aren’t old enough to drink. But hey, business is business right?"

    sar "And Maki already said she’ll watch over them all, so everyone is safe!"
    s "Are you actually selling alcohol to the girls?"

    if bonus == True:
        sar "Oh, not at all."
        sar "Not until the fashion show is over, I mean."
    else:
        sar "Of course! They're grown women. I'm just holding off until the fashion show is over."

    sar "I don’t want Sana tripping and getting hurt while she’s up there. You know how she gets when she’s drunk."
    s "It’s a miracle that you’re still in business, Sara."
    os "It’s less of a miracle and more of a matter of Wakana spending half of her salary on beer."
    w "It’s the only way to kill the pain."
    sar "You know these two?"
    s "Yeah. The one with the scarf is Osako Osaka, my karate instructor. And the one that looks like a zombie is Wakana Watabe, a coworker of mine."

    scene fashionshow8
    with dissolve

    sar "You do karate? No wonder you’re in such great shape."
    os "He...tries."
    os "Actually, no. He doesn’t even try. He just talks to that blonde girl over on the couch the whole time."
    os "{i}She{/i} tries, though. In fact, she’s pretty good while he’s not distracting her."

    scene fashionshow9
    with dissolve

    sar "So you teach [teenager]s {i}and{/i} adults?"
    os "Whoever, really. "
    s "She also works at the maid cafe."

    scene fashionshow10
    with dissolve

    sar "Ah! I knew you looked familiar!"
    sar "Oh my God, you look so different without the costume!"
    os "Didn’t we agree you wouldn’t talk about that to anyone?"
    s "It’s fine. Sara is a bartender. She basically exists to hear peoples’ secrets."
    sar "It’s true, you know. Anything you say in here is totally confidential. But you shouldn’t be embarrassed about the maid thing!"
    sar "You were really, really cute!"
    sar "Like {i}really{/i} cute!"

    scene fashionshow11
    with dissolve

    os "I get it, okay?! You don’t have to keep telling me!"
    w "…"
    w "I {i}do{/i} love that outfit on you."

    scene fashionshow12
    with dissolve

    os "Ahh! Just leave me alone! I don’t want to hear it!"

    scene fashionshow13
    with dissolve

    u "Alright, everybody! The contestants are ready to show you how cute they are! "
    u "But first, why don’t we check in with the people who made the costumes and see how they’re feeling about the whole ordeal...starting with floor numero uno!"

    scene fashionshow14
    with dissolve

    ay "Oh! I know Spanish! That means floor number one!"
    a "You don’t know Spanish, you know Despacito. "
    r "Sana...costume..."
    r "You guys might have to hold me back so I don’t charge the stage."
    u "Sana Sakakibara’s costume was made by Ami Arakawa and Ayane Amamiya! "
    u "Rin didn’t do anything to help, but she has decided to join them on the couch for the safety of both of our contestants!"
    r "Is anyone else dizzy or is it just me?"

    scene fashionshow15
    with dissolve

    ay "I feel your pain, Rin. This is exactly what I have to wake up to every morning."
    ay "I highly implore you to stop by and watch her sleep one day. I’m sure it is equally as cute as what you’re about to see."
    r "You are not making this easier for me, Ayane."

    scene fashionshow16
    with dissolve

    u "And over on the second floor couch is Molly MacCormack and Uta Ushibori!"
    mak "Wha- Uta? When did you-"
    u "Yasuyasu’s outfit is a MacCormack original that she put a {i}lot{/i} of work into!"
    mo "Please let me win. Please let me win. Please let me win. Please let me win. Please let me win. "
    u "I helped too! But really all I did was size her up and style her hair!"
    u "Also, please let it be known that any wardrobe malfunctions that happen today are the result of improper handling on behalf of the wearer! It is not our fault!"
    mak "Uta, get back over here! It feels weird standing on the stage alone!"
    u "Hold your friggin’ horses, prez! I’m givin’ my all as a field reporter over here!"
    u "In fact, why don’t you just go ahead and introduce the contestants without me?!"
    u "I’ll hang out on the couch with my buddy Molly and make sure she doesn’t pop a blood vessel!"
    mak "Um...uhh...okay! Yeah! On with the show and...all of that."

    scene black
    with dissolve

    mak "T-Tonight’s first contestant is Sana Sakakibara!"
    mak "Sana...come on out!"
    ay "Wooo! That’s my girl!"
    sar "YEAAAAAAH SANA!!! YOU GOT THIS, BABY!!!"
    sa "Ahhhhhhhhhhh......."

    scene fashionshow17
    with dissolve

    u "The motif behind Sana’s outfit is..."
    u "Actually, why don’t you go ahead and explain this part Ami? I can’t really tell what’s goin’ on here."
    a "Oh! Uhh...yeah!"

    scene fashionshow18
    with dissolve

    a "The idea behind Sana’s costume is...umm...kind of a...contrast between dark and light?"
    a "Sana’s really quiet and timid, but when she’s watching horror movies or playing D&D, she gets really into it and kinda turns into somebody else."
    a "So I wanted to show off those parts of her and...also show everybody that she’s super cute when all of her skin isn't covered up."
    u "I see, I see! It {i}is{/i} true that Sana is revealing a bit more skin than normal! I can see her belly button from all the way over here!"

    scene fashionshow19
    with dissolve

    sa "S-Stop looking at it!"
    sar "I’m going to faint. She’s so cute. Oh my god. She’s the cutest thing in the world. I love her."
    sar "Haruka. Haruka. Haruka."
    h "What?..."
    sar "See that girl? I {i}made{/i} that. She came out of me."
    h "Yes...Good job, Sara. We’re all very proud of you."
    mak "Sana, is there anything you’d like to say to the judge before we bring Yasu out?"

    scene fashionshow20
    with dissolve

    sa "To...Sensei?..."
    mak "Well, he {i}is{/i} the judge..."
    sa "Um...I..."
    sa "I’m...sorry you had to...see me like this..."
    u "So modest! Could it be that Sana really doesn’t recognize her own cuteness?! Or is this a calculated move to play up her insecurities and steal the competition?!"
    mak "No, I’m...pretty sure she’s just embarrassed..."
    u "Either way! Thank you, Sana, for showing everyone your cuteness!"
    u "Makoto, go ahead and bring Yasu out!"

    scene black
    with dissolve

    mak "Right! On it!"
    mak "Our second and final contestant tonight is Yasu Yasui!"
    mak "She’s still the newest student in the class, but that doesn’t mean she’s coming into this with nothing riding on it!"
    mak "Yasu...come on out!"

    scene fashionshow21
    with dissolve

    u "To repeat, Yasuyasu is wearing a MacCormack original! Did you hear that, folks? A {i}MacCormack{/i} original!"
    a "Why is she making Molly sound like some sort of professional designer?"
    ay "Well...she {i}is{/i} really good, to be completely fair."
    a "Whose side are you even on?!"
    u "Molly, how about you tell us a little more about Yasu’s outfit tonight?"
    mo "Absolutely. What you see here is-"

    scene fashionshow22
    with dissolve

    ya "A tale as old as time itself~"
    mo "Um...what I was saying is-"

    scene fashionshow23
    with dissolve

    ya "So many beautiful things packed into one room...and I am lucky enough to be beside them."
    ya "Feast your eyes upon me and witness the true wonder that is purity incarnate."
    ya "For I, Yasu Yasui, have been chosen by Him to spread the seed...and to take all of you with me."

    scene fashionshow24
    with dissolve

    ya "Come! Let us watch the end of days from atop the highest building we can find! "
    ya "So that even when the world plunges into darkness, we shall be above it!"
    ya "Come to the light! Come! Come!"
    u "Thanks a bunch, Yasuyasu! But now it’s Molly’s turn to talk!"

    scene fashionshow25
    with dissolve

    ya "Good luck, Molly. And thank you very much for the dress."
    mo "You are very welcome..."
    mo "Now, as I was saying, the motif behind Yasu’s design is to emphasize the chaotic darkness growing within her."
    mo "Her patron, who I assume is the Great Old One-"
    ya "He with many eyes."
    mo "Oh, I haven’t heard of that one before. You’ll have to tell me more about him."
    ya "I would like nothing more."
    mo "Anyway, the idea was to show everyone what I believe the physical manifestation of darkness to be."
    mo "But, just like with Sana’s costume, there needs to be an element of light. Or, in Yasu’s case, purity."
    mo "Which is why we’ve adorned her with a crown and necklace of thorns. "
    mo "Mixed with her pale skin, the thorns are meant to signify corruption or how purity can be tainted by even the smallest of barbs..."

    scene black
    with dissolve

    u "Wonderful explanation, Molly! Thanks so much for sharing!"
    u "But, now that both contestants have showed us their outfits, it’s time for our favorite teacher in the whole wide world to decide who wins!"
    u "Sana, why don’t you join Yasuyasu back on the stage and-"
    u "Wait, Yasu, where are you going?"
    mak "Stay here, Yasu. The contest isn’t over yet."
    ya "Contest?"
    mak "You...do realize why..."
    mak "You know what, nevermind. Just wait here."
    mak "Sana, come back out!"
    sa "Ahhhhh...do I have to?"
    mak "The hard part’s already over. Just stand next to Yasu for a minute or two, please."
    sa "Umm...uhh...okay..."

    scene fashionshow26
    with dissolve

    sa "…"
    ya "Oh my. You look scared."
    ya "What is wrong, Sana?"
    sa "I...um..."
    sa "I like your...crown..."
    ya "As do I."
    ya "It’s made with real thorns."
    sa "…"
    ya "…"
    sa "…"
    ya "…"

    scene fashionshow27
    with dissolve2

    sa "Uhhhhhhhh..."
    u "Wait, is Yasuyasu bleeding? Molly, that’s not supposed to happen, is it?"
    mo "It was...a risk I knew we’d be taking. "
    mo "I suggested using one made from plastic, but Yasu was quite insistent on wearing an {i}actual{/i} crown of thorns."
    sa "Uhh...Y...Yasu...your forehead is..."
    ya "He would be so proud of you, Sana."
    ya "You’ve come so far."

    scene fashionshow28
    with dissolve

    sa "I..."
    sa "Who are you...talking about?..."
    ya "You want to know?"
    sa "I...don’t know..."
    ya "Whenever you do, feel free to come find me."
    ya "I can show you things that will change your life."
    ya "Things that will save you."
    sa "I..."
    sa "Uhh..."
    sa "Okay..."

    scene fashionshow29
    with dissolve

    u "Okay, Sensei! Make your choice!"
    u "Who is the winner of the fashion show?!"

    "I take one final look at Sana and Yasu and wish I could give the win to both of them."
    "Unfortunately, a decision needs to be made."
    "And, so..."

    menu:
        "Sana wins":
            $ dorm1warpoints += 1
            $ sanafashion = True

            s "The winner of the gothic lolita fashion show is..."
            s "Sana."

            scene fashionshow30
            with dissolve

            sa "W-Wait...really? I...I won?..."
            sa "So...so does that mean...you think my outfit is...prettier than Yasu’s?..."
            s "That is what winning would imply, yes."
            ya "Congratulations, Sana. I’m very happy for you."
            mo "Yasu, why couldn’t you wait until after the decision to start bleeding?! Your weak skin has ruined our chances of victory!"

            scene fashionshow31
            with dissolve

            ya "I’m sorry, Molly. I am a very weak and delicate girl."
            sa "I...I don’t really know what to say..."
            a "Say that you couldn’t have done it without me and Ayane!"
            ay "I’m so proud...that’s my girl up there..."
            sar "Haruka. Haruka. Haruka."
            sar "Did you see what happened?"
            h "Yes, Sara. We’re all very happy for her."
            sar "My daughter just won a fashion show. How many fashion shows have you won?"
            h "None, Sara. Congratulations on giving birth to a cute girl."
            sar "Thank you very much~"
            sa "Um...thank you, Sensei..."
            sa "For...choosing me."
            s "You don’t have to thank me. I just picked the person who I thought should win and...that person happened to be you."
            s "You look very cute, Sana."
            sa "Thank you..."
            sa "I’m...really happy you think that..."

        "Yasu wins":
            $ dorm2warpoints += 1
            $ yasufashion = True

            s "The winner of the gothic lolita fashion show is..."
            s "Yasu."
            ya "I won something?"
            mo "YEAAAAH! VICTORY FOR MOLLY!"
            u "And Yasuyasu, Molly. She’s the one who wore the outfit."
            mo "Yes, but {i}I’m{/i} the one who did all the work. This one belongs to the people of Ireland."
            a "Damn it! I worked really hard on that dress!"
            ay "I still think Sana should have won. She’s clearly the cuter girl out of the two of them."
            r "And significantly less scary. I vote Sana."
            ay "Sensei! We demand a recount!"

            scene fashionshow33
            with dissolve

            ya "Does this mean what I think it means, Sensei?"
            s "What do you think it means, Yasu?"
            ya "That if we were to conduct the act of transference among all of these beautiful creatures, you would supplant me with His warmth before the others?"

            if bonus == True:
                s "That is...not how I would word it."
                ya "Is it because you can sense how empty it is inside of me? How I long to spread the seed?"
            else:
                s "If this is your way of suggesting that we should hug, I still think it might be good to wait a little longer."
                s "But...if you really want to know why you won-"

            s "It’s because I thought you looked cuter."
            s "But, Sana-"

            scene fashionshow34
            with dissolve

            sa "Y...Yeah?"
            s "I think you look really cute as well."
            s "I just think this win should go to Yasu instead."

            scene fashionshow35
            with dissolve

            sa "No...I...I agree..."
            sa "I’m just...sad that I couldn’t get...a point for Ami and Ayane..."
            sa "They really tried to...win this competition and...and I couldn’t do it for them..."
            ya "Oh my..."
            ya "Could this be...arousal?..."
            ya "I’m beginning to feel...rather lightheaded..."
            s "You’re also losing blood, so we should probably get you patched up..."

    scene black
    with dissolve2

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"

    sar "Okay, everybody! Now that the fashion contest is over, feel free to order whatever you want!"
    sar "Also, this never happened! Please talk to one of the moms if you are feeling strange or want to lay down!"
    os "Uhh...Wakana, maybe we should start heading out? I don’t really think we should hang around for this."
    w "In a moment. I’d like to speak to the Sakakibara girl first."
    to "Am I late? Did I miss the contest? "
    to "I wanted to take a bath before I arrived and-"
    to "Wait, Yasu?! What on earth happened to your head?!"

    $ renpy.end_replay()
    $ dormwar15 = True
    jump dormwar16

label dormwar16:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
"//////////////////////////SENDING MESSAGE “I’ll never forget you...” TO “Sensei”"
    "//////////////////////////…"
    "//////////////////////////…"
    "//////////////////////////…"
    "//////////////////////////MESSAGE FAILED"

    scene testofcourage36
    with dissolve2

    m "Oh, you’ve gotta be fucking kidding me."
    m "Even in the end, I can't catch a break."

    "//////////////////////////COMMENCING FACTORY RESET IN 1..."

    m "Fuck you. "

    "//////////////////////////2..."
    "//////////////////////////7..."

    m "…"

    "//////////////////////////WATERMELON..."

    m "…"
    m "What?"

    scene testofcourage37
    with dissolve3

    "//////////////////////////…"
    "//////////////////////////…"
    "//////////////////////////…"
    "//////////////////////////CONGRATULATIONS “Maya Makinami”"
    "//////////////////////////YOU HAVE COMPLETED THE TEST OF COURAGE"

    m "…"

    "//////////////////////////PLEASE FILL OUT A SURVEY IF YOU ENJOYED YOUR TIME IN THE SCARY ROOM"
    "//////////////////////////WE HOPE TO SEE YOU AGAIN!"
    "//////////////////////////:) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) "

    m "…"

    "//////////////////////////:) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) ???"

    m "…"

    "//////////////////////////:) :) :) :) :) :) :) :) :) :) :) :) :) :) :) :) ?????????"

    m "…"
    m ":)"

    scene black
    with dissolve2

    "{i}Maya wins!{/i}"
    "………"
    "……"
    "…"

    scene testofcourage38
    with dissolve

    a "Hey! How did it go?"
    a "Pretty scary, right?"
    a "It was really hard thinking of stuff that might actually get to you since you never seem scared, so I kinda just threw a bunch of normal scary movie stuff in there in hopes that something would work."
    m "Normal...scary movie stuff?"
    a "Yeah! You know, like...vampires and ghosts and a few of those jumpscare Halloween decorations Ayane had laying around."
    a "Don’t tell me you got so scared that you didn’t even get to see all of it?"
    m "…"
    m "I guess I did..."
    a "Well, Tsuneyo only lasted like 30 seconds anyway, so you pretty much demolished her."
    a "Molly set a trap thingy that knocked a bowl of ramen off of a shelf if Tsuneyo pushed a button and...well, you can probably guess how that ended."
    m "…"
    a "…"
    a "Uhh...so, anyway, we’re going to start heading over to Sana’s mom’s bar thing for the fashion show. But I kind of wanted to stop at a convenience store first and-"
    m "I’m going to go back to the dorm, actually."

    scene testofcourage39
    with dissolve

    a "Are you okay?..."
    a "I know you’re probably still scared but...it seems like it might be a little worse than that..."
    m "I..."
    m "I need to lay down..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ dorm1warpoints += 1
    $ dormwar14 = True
    stop music fadeout 6.0

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"

    jump dormwar15
...
```