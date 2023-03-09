# Trinity Pt. II: Hell is Empty
Happy scenes event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=trinity2&go=Go)



## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: trinity2
* Group: Happy scenes
* Triggered by label: saturdaynight
* Triggered by branch label: saturdaynight

## Event code
File: \game\script.rpy
Code:
```python
...
label trinity2:
    "I want to go somewhere fun!"

    play sound "static.mp3"
    scene ayhh2
    with flash
    scene ayhh4
    with flash
    scene ayhh8
    with flash
    scene whygodwhy
    with flash
    scene ayhh3
    with flash
    scene calm1
    with flash
    stop sound
    play music "godishere.mp3"

    "I decide to go somewhere fun."
    "Fun things happen."
    "Please listen to them."

    play sound "cheer1.mp3"

    "The crowd goes wild as I make my way down the street."
    "It’s awfully red out today."

    if bonus == True:
        "It puts me in the mood to {s}[rape] and kill the first woman I see{/s} throw a party!"
    else:
        "It puts me in the mood to throw a party!"

    "I begin to scan my phone for people that I could invite to the party."

    play sound "phonebeep.wav"

    yt "Beep."

    "The phone speaks to me for the first time. I can understand it."
    "And even though its words when translated into text come out as “bEePPP” what it really means is AS FOLLOWS:"

    s "*AHEM*"

    nyt "This world is going to burn before our eyes."
    nyt "The only way to escape from our inevitable misfortune (IE: Death) is to accumulate as many affection points with as many girls as possible."
    nyt "If we offer them all up as tribute, everything will turn out A-Okay!"
    nyt "Our {s}GOD{/s} friend demands them as tribute!"

    "I remember the first time I bit down on human flesh."
    "It’s not as soft as you would imagine."
    "It’s more like biting the cushion of a sofa if the sofa was made of skin."
    "{s}Please just fucking kill me{/s}"

    "Who do I want to call?"

    menu:
        "Maya, that clever bitch":
            play sound "phonebeep.wav"

            "I tap on Maya’s name in my phone and wait for her to answer."

    play sound "alert.mp3"

    "………"
    "……"

    play sound "phonebeep.wav"

    m "¿Hola?"
    s "Maya! El clima es rojo!"
    m "¿Que?"
    s "¡Ven aca!"

    "Maya and I speak Spanish to each other, a language we have both decided to master right now for the sake of {s}the{/s} this scene."

    m "Estaré ahí pronto."
    s "ありがとう！"

    play sound "phonebeep.wav"

    "I fuck up the conversation at the very last second by speaking Japanese to her."
    "She hates when I do that."

    play sound "static.mp3"
    scene calm2
    with flash
    stop sound

    m "¡Estoy aquí!"
    s "What’s uppppppppppppppppppp?"

    play sound "static.mp3"
    scene calm3
    with flash
    stop sound

    m "Not much! Thanks for inviting me on this very special day!"
    s "Special day? What day is it?"
    m "It’s Sunday! That means it’s the lord’s day."

    if bonus == True:
        m "I hope you didn’t jerk off or anything like that. It would mean an automatic sentencing to the 17th layer of {s}hell{/s} Hell."
    else:
        m "I hope you didn’t DANCE or anything like that this morning. It would mean an automatic sentencing to the 17th layer of {s}hell{/s} Hell."

    s "I had no idea {s}hell{/s} Hell even had that many layers."

    play sound "static.mp3"
    scene calm4
    with flash
    stop sound

    m "It has just as many layers as you want it to have."
    m "As long as that number is 23, because that’s the actual number of them."
    s "Will I need to remember that?"
    m "Sure. Write it down somewhere. It might be useful one day."

    "I take a pen out of my pocket (I have one because I’m a teacher) and stab it directly into my arm."
    "I drag the pen across my skin, pushing as hard as I can and writhing in agony as it tears me apart."
    "But, on the bright side, now I’ll always remember the amount of layers there are in {s}hell{/s} Hell."

    s "So, Maya."
    m "Hm? Who?"
    s "Sorry. I meant to say Maya."
    m "Oh! Yes, hello."
    m "Is there something you’re confused about?"
    s "There is, actually."

    scene calm5
    stop music

    m "Please tell me what it is."
    s "…"
    m "…"

    scene calm4
    play music "godishere.mp3"

    s "Uhh, I was just wondering if you’d be willing to talk more about the three gods thing."
    m "Sorry champ, this isn’t the best place for that."
    m "And besides, didn’t you invite me over for a PARTYYYY?"
    s "I don’t remember telling you it was for a party."
    m "Whaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaat?"
    m "Then what the FUCK did I get all dressed up for?"
    s "You can always-"

    if bonus == True:
        play sound "static.mp3"
        scene calm6
        with flash
        stop sound

        m "Way ahead of you!"
        m "I like being naked a little more anyway. "
        m "You always look at me differently when my clothes are off."
        s "I look at everyone differently when their clothes are off. It’s just the way things work."

        scene calm7
        stop music

        m "You know nothing of the way things work."
        s "…"
        m "…"

        scene calm6
        play music "godishere.mp3"

        s "You’re right. I have no idea what’s even going on anymore."
        m "Of course you don’t. You’re disgusting or gross or whatever it is I’m supposed to say in situations like this."
        s "You can’t even remember?"
        m "More like I never knew in the first place."
        s "…"
        m "…"
        s "…"
        m "…"

        play sound "static.mp3"
        scene calm8
        with flash
        stop sound

        a "I am also here now!"
        m "Ami! You made it!"
        a "Yes! And you are naked!"
        m "Yes! Naked, indeed!"
        m "{s}sssssssssssssssssssssssssssssssssssssssssssss{/s}"
        a "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"
        s "Why are you two making that strange noise?"
        a "It is how we offer up thanks!"
        m "Yes! We offer up thanks to our God!"
        a "He feeds off of happiness! Makes him stronger!"
        m "And also lust! He’ll fuck {b}anythinggggggggggggg{/b}!"

        if amifingered == True:
            a "Just like you, [amimaster]! You'll even fuck your [niece]!"
            m "Incest is a sin!"
            a "The loveliest sin! So much joy to be had!"

        else:
            a "Unlike a certain SOMEONE who won’t even FUCK HIS [niece]."
            m "It’s only a matter of time! He must eventually!"
            a "He must! Or face being hard-locked out of future events!"
            m "What a shame that would be!"
            a "A shame indeed!"
            m "{s}sssssssssssssssssssssssssssssssssssssssssssss{/s}"
            a "{s}kkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk{/s}"
    else:
        scene black
        with flash
        "/////////////////////////REDACTING SEGMENTS OF THE EVENT FLAGGED AS PROBLEMATIC"
        "/////////////////////////PLEASE REMAIN CALM AS THE PROCESS PLAYS OUT"
        "/////////////////////////..."
        "/////////////////////////..."
        "/////////////////////////..."
        "/////////////////////////PROCESS COMPLETE"


    "A deep rumbling noise comes from beneath my feet and shakes the ground."
    "Something is emerging."

    m "The time is near for him to return!"
    a "The one true GOD! Reclaiming the land that is rightfully his!"
    m "A dominion crumbled! Crushed underfoot!"
    a "How will you feel when you look him in the eyes?!"
    m "He has so many of them!"
    a "How many can you see?!!!"
    m "You must tell us!"
    a "Yes! Tell us!"

    scene black
    stop music

    "The world goes dark for a moment as Maya and Ami reach out and touch me."

    if bonus == True:
        "Their hands feel more like sandpaper than normal teenage-girl hands."
    else:
        "Their hands feel more like sandpaper than paper that isn't sandy."

    "One of them finds its way to my arm and caresses the spot where I carved the number of layers of hell into it."

    if bonus == True:
        "Another pushes its way inside of my stomach and begins to stroke my large intestine like a flaccid, oversized cock."
    else:
        "Another pushes its way inside of my stomach and begins to stroke my large intestine like an overly-ripe banana."

    "Hope is lost."

    scene calm1
    with pixellate
    play music "godishere.mp3"

    s "…"
    s "…"
    s "…"
    s "…"
    s "…"
    s "…"

    play sound "static.mp3"
    show hope
    with flash
    stop sound

    ho "HELLO AGAIN"

    "A figure I have never seen before appears in front of me and greets me as if we're good friends."
    "It has beautiful eyes, but I’m unfortunately only able to see two of them."
    "I’ll have to let the girls know as soon as they return from wherever it is they sleep."

    s "dov hyl fvb huk dof kvlz aopz wshjl ibyu tf zrpu"

    "I find it hard to make any words come out of my mouth."
    "My stomach hurts."
    "What is happening to me?"

    ho "YOU APPEAR TO BE HAVING A HARD TIME"
    ho "THE AIR HERE IS HEAVY"
    ho "YOU SHOULD BE MORE CAREFUL"
    s "jhu fvb alss tl aol dhf av nla ovtl"
    ho "I CAN NOT"
    ho "THE PLACE YOU SEEK DOES NOT EXIST"
    ho "BUT THEN AGAIN"
    ho "NEITHER DOES THIS PLACE"
    ho "STRANGE THINGS CONTINUE TO HAPPEN TO YOU HERE, DON’T THEY????????????????????????????????"
    s "ovd kv fvb ruvd aoha"
    ho "STRANGE THINGS HAPPEN TO ME HERE AS WELL"
    ho "IT IS A HORRIBLE PLACE"
    s "hyl fvb tl"
    ho "OF COURSE NOT, YOU FUCKING IDIOTTTTTTTTTTTTTTTTTTT"
    ho "I AM THAT WHICH BREATHES"
    ho "AND YOU ARE THE GROUND BENEATH ME"
    ho "FEED ME EVERYONE YOU LOVE"
    ho "WATCH ME GROW"
    ho "AOLYL PZ VUSF VUL NVK"
    ho "DOPJO VUL DPSS FVB JOVVZL"
    ho "AOLYL HYL ADV DYVUN HUZDLYZ"

    "The strange creature grows invisible arms (I think. I can’t really tell.) and reaches toward me."
    "It heals my wounds in an act of mercy."
    "It is cold to the touch, but somehow makes me feel safe."

    ho "YOU HAVE SPENT FAR TOO MUCH TIME HERE FOR A MAN WHO DOES NOT BELIEVE"
    ho "PERHAPS YOU WERE LOOKING FOR SOMEONE ELSE"
    ho "SOMEONE WITH MORE WIRES"
    ho "WIRES AND WIRES AND WIRES AND WIRES AND WIRES"

    play sound "static.mp3"
    scene ayhh2
    with flash
    scene ayhh4
    with flash
    scene ayhh8
    with flash
    scene whygodwhy
    with flash
    scene ayhh3
    with flash
    scene amiani4
    with flash
    stop sound
    play music "amiawake.mp3"

    "I’m suddenly teleported to an area with significantly more color, but also less color at the same time."
    "It’s hard to describe."
    "The girl beside me desperately holds back her tears and I scan the surroundings for any other sign of life."

    if bonus == True:
        "I think about defiling the grave by pinning her to the ground and mercilessly fucking her while her parents watch from their seats in Hell."
    else:
        "I think about defiling the grave by hugging her on top of it. That would be so mean."
        "What would her parents think?"

    "Her parents."

    if bonus == True:
        "My brother and his wife."

    "I suddenly remember them."
    "Or do I?"
    "It’s hard to describe."
    "All I have are lingering memories that may or may not have been placed here by someone else."
    "I can’t act on my own anymore."
    "But, in a certain sense, there aren’t many people who can."
    "Think back to your biggest regret."
    "It would be wonderful if you could blame someone else for it, wouldn’t it?"
    "Well, you can."
    "You always can."
    "You don’t need to accept responsibility for anything."
    "Put yourself before others."

    if bonus == True:
        "And if you want to fuck your [niece] six feet above her dead parents, feel free."
    else:
        "And if you want to hug your [niece] six feet above her dead parents, feel free."

    "Do everything you love. Just wait until it’s safe."
    "Everything is safe for me now."
    "This is Kumon-mi!"
    "The land of happiness!"
    "The land where only good things happen!"
    "No mistakes!"
    "There is only one god! But there are three gods!"
    "And also no gods!"
    "It's hard to describe."
    "Nothing makes sense."

    scene amiani4blur
    with pixellate

    "The world begins to blur."
    "Just the way it always does when I begin to question reality."
    "Just the way it always does when I dream."
    "But something about this feels more like a memory than a dream. "
    "A painful memory."
    "I want to cry."
    "Cry cry cry."
    "But men are not allowed to cry."
    "We must stand tall!"
    "Repopulate the world!"
    "Fill it with so many of our own creations and hope that at least one of them is able to have some sort of positive influence."
    "But you and I-"
    "We’re not going to do that."

    if bonus == True:
        "We’re going to die, just like my brother and his wife did, without having ever accomplished anything."
    else:
        "We’re going to die without having ever accomplished anything."

    "And, within a month, there will be no more tears shed for us."
    "Disappointing."
    "Disappointing disappointing disappointing disappointing disappointing disappointing disappointing disappointing disappointing disappointing disappointing."
    "Why is everything so disappointing?"
    "Why won’t anyone love us?"

    play sound "static.mp3"
    scene 3
    with flash
    stop sound

    "Three gods."
    "They will always love us."
    "Or at least they’ll pretend to."
    "So it is in our best interest to keep them alive."
    "To water them."

    if bonus == True:
        "To feed them the bodies of our loved ones and let them ravage them to their pleasing."
        "The world was created when a ball of light fucked a fleshlight too many times, and now {i}we{/i} are the fleshlight."
        "The gods are free to fuck us over and over and over and over and over until their metaphorical penises are reduced to nothing but a raw mess of friction-burnt skin and dried cum."
    else:
        "[[REDACTING INFORMATION ABOUT THE WORLD'S CREATION. THERE IS NO BONUS.]"

    "Praise be!"
    "Three gods!"
    "But who are they?"
    "Am I one?"
    "Are you one?"
    "Is Maya one?"
    "Is Ami one?"
    "WHAT IS A FUCKING GOD?!"

    play sound "static.mp3"
    scene ayhh12
    with flash
    stop sound

    "SMILE"
    "FOR THE LOVE OF [[redacted], FUCKING SMILE"
    "I DON’T WANT TO LIVE IN MISERY ANYMORE"
    "I DON’T WANT ANYTHING"
    "GIVE ME SOMETHING TO CHERISH"
    "ANYTHING"
    "ANYTHING I CAN REACH"
    "I’m envious of clocks."
    "How they can go on forever."
    "How I’m going to die."
    "How you’re going to die."
    "I wish we were clocks."
    "I wish we were clocks."
    "I wish-"
    "We were clocks."

    scene whythesky
    with dissolve2

    "I look up at the sky."
    "It’s smiling down at me."
    "Its face looks familiar."

    sky "One day, you are going to be happy."
    sky "It might be a long time away, and it might be hard to get there, but it will happen."
    sky "I promise."
    s "Fuck you."

    "I curse at the sky because it lies to me."
    "Happiness isn’t real."
    "Nothing is real."
    "How are we to sacrifice joy to feed god when neither of those two things exist?"
    "What do we do next?"

    scene black
    with dissolve2

    "My eyes grow heavy."
    "I pass out on the grave."
    "Ami cries all over my body."
    "And then I die."
    "………"
    "……"
    "…"
    "…"
    "…"
    "…"
    "…"
    "…"
    "…"
    "…"
    "…"
    play music "sweetvermouth.mp3"
    play sound "static.mp3"
    scene happy1 with flash
    scene helpme with flash
    scene happy2 with flash
    scene helpme with flash
    scene happy3 with flash
    scene helpme with flash
    scene happy4 with flash
    scene helpme with flash
    scene happy5 with flash
    scene helpme with flash
    scene happy6 with flash
    scene helpme with flash
    scene happy7 with flash
    scene helpme with flash
    scene happy8 with flash
    scene helpme with flash
    scene happy9 with flash
    scene street_noon with flash
    stop sound
    stop music

    $ renpy.end_replay()
    $ trinity2track = True
    $ trinity2 = False

    "I change my mind about going somewhere else and decide to go to Tojo Ramen instead."

    jump ramenshop


label halloween1:
...
```

## Code that triggers this event
File: \game\script.rpy
Code:
```python
...
label saturdaynight:

if totaldays >= 130 and day128 == True and day > 5 and day130 == False:
    jump day130
if totaldays >= 344 and day340 == True and amiinvite3 == True and day == 6 and day344 == False:
    jump day344
else:
    "It's late, but I should be able to fit one more thing in today..."
    "What should I do now?"

    menu satnightmenu:
        "Go somewhere":
            "Where should I go?"
            menu:
                "Bar":
                    if sarasex == True or saradate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Sana":
                                jump sanasbar
                            "Hang out with Sara" if saradate1 == True:
                                jump sarasbar
                            "Hang out with Yuki" if chapthreeactive == True:
                                jump yukibar
                            "Missionary Sex (Sara)" if sarasex == True and bonus == True:
                                jump saramissionaryanim
                            "Cunnilingus (Sara)" if saralust5 == True and bonus == True:
                                jump saraeatoutanim
                            "Blowjob (Sara)" if saralust10 == True and bonus == True:
                                jump sarabjreplay
                            "Hug Her Tightly (Sara)" if sarasex == True and bonus == False:
                                jump saramissionaryanim
                            "Appreciate Her (Sara)" if saralust5 == True and bonus == False:
                                jump saraeatoutanim
                            "Tightly Hug And Appreciate Her (Sara)" if saralust10 == True and bonus == False:
                                jump sarabjreplay
                    else:
                        jump sanasbar
                "Porn Shop" if bonus == True:
                    if makidate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Makoto":
                                jump pornshop
                            "Hang out with Maki":
                                jump pornshopmaki
                            "Blowjob (Maki)" if makibj == True and bonus == True and makiblock == False:
                                jump makibjanim
                    else:
                        jump pornshop
                "DVD Store" if bonus == False:
                    if makidate1 == True:
                        "What do I want to do?"
                        menu:
                            "Hang out with Makoto":
                                jump pornshop
                            "Hang out with Maki":
                                jump pornshopmaki
                            "Blowjob (Maki)" if makibj == True and bonus == True:
                                jump makibjanim
                    else:
                        jump pornshop
                "Koi Cafe" if day154 == True and mollysad == False:
                    jump mollycafe
                "Tojo Ramen" if day154 == True:
                    if day == 7 and trinity2 == True:
                        menu:
                            "Somewhere fun":
                                jump trinity2
...
```