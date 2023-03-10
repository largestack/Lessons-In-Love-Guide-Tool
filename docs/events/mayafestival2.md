# Three Halves Make a Whole (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Somewhere Inside of a Dream](./mayafestival1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: mayafestival2
* Group: Maya
* Triggered by label: mayafestival1
* Chain sources: mayafestival1
* Chain sources path: mayafestival1

## Official wiki page

[Three Halves Make a Whole](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayafestival2&go=Go) for more details.

## Event code

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label mayafestival2:
    "Maya and I leave the house together and begin to make our way to a festival at-"

    s "Wait, where is this festival exactly?"
    m "Far away. "
    m "Well, as far as we can go within the confines of Kumon-mi, that is."
    m "There’s one closer, but I didn’t want to risk the chance of someone seeing me with you in public and thinking we like each other."
    s "We do like each other, though."
    m "No. You like me. It’s different."
    m "Don’t worry too much about where it is as there’s not much reason to ever go back."
    m "The surrounding areas have mostly closed down anyway since the school building there is no longer in use."
    s "Are we taking the bus, then?"
    m "Partly. We’ll have to walk for about half an hour after we get off since the bus doesn’t stop where we’re actually headed anymore."
    s "The more I hear about this place, the more I think this is some elaborate ploy for you to kill me."
    m "There are much easier ways for me to kill you. "
    m "But in the event that I am just looking for a challenge, you should at least thank me first for allowing you to see me in my yukata in your final moments."
    s "Oh well. I’ve had a good run."

    "Anyway, we leave the house together and begin to make our way to a festival at some undisclosed location far away from my house that buses pretend doesn’t exist for some reason."
    "It’s confusing, yes. But so is literally everything about this city and I am tired of trying to attribute meaning to any of it."
    "And, like Maya says, there’s no reason for me to ever go back. So I might as well just stop thinking about it and try to enjoy the rest of the day with her."
    "If we ever make it there, that is."
    "At this rate, I-"

    stop music
    play sound "static.mp3"
    scene smileex with flash
    scene tree3 with flash
    scene mayafestival1 with flash
    stop sound
    play music "anewyou.mp3"

    s "Oh. We’re here."

    "A swarm of lights surrounds us, both natural and artificial, and the scents of various street foods assault my senses."
    "I still haven’t eaten anything on account of Maya claiming my breakfast as her own, so I’m starting to get a little hungry and hope that my companion here doesn’t empty my bank account out on herself."
    "Upon closer observation, I can tell this is somewhere I haven’t been before."
    "But, like many things, it feels familiar."
    "Even Maya’s presence feels familiar, so...maybe this is somewhere we’ve gone together in the past?"

    s "Hey. If buses don’t come here and there’s no reason to ever visit this part of town, how do you know about it?"
    m "I know every nook and cranny of Kumon-mi. I just choose to avoid most of them."
    s "Have we ever come here together before?"
    m "I’m not going to answer that. If you trick me into allowing you to commit suicide-by-memory on my birthday, I will never forgive you."
    s "This place just feels a little familiar. That’s all."
    m "Perhaps it is, then."

    scene mayafestival2
    with dissolve

    m "Anyway, I’ll be taking your credit card now."
    s "..."
    m "Fine. I will be taking your credit card, {i}please.{/i}"
    s "..."
    m "Give me your fucking credit card. I’m hungry."
    s "Do they even take credit cards here? This place seems pretty traditional."
    m "ATMs exist, you know. Just give me the card."
    s "This doesn’t sound very much like “spending time together.”"
    m "Do you see how many stalls there are here? We’ll never be able to hit all of them if we stick together."
    m "This festival has two halves. I need you to handle all of the stalls on the west side while I handle all of the ones on the east."
    m "Card. Now. Give."
    s "At least tell me what you want me to order for you first."
    m "Yes."
    s "Not really a yes or no question, Maya."
    m "You see, that is where you are wrong."
    s "You never wanted me here at all, did you? I’m just the only person you know with a credit card."

    scene mayafestival3
    with dissolve

    m "If I say no and promise to...catch goldfish with you or something once I’m done eating, will you give it to me?"
    s "I don’t have the time to take care of a goldfish."
    m "It’s a goldfish. You put it in water. That’s literally it."
    s "I feel like you’re supposed to feed it occasionally too."

    scene mayafestival4
    with dissolve

    m "Why do you care more about feeding your hypothetical goldfish than me? I am much more attractive and fun to be around."
    s "Attractive, sure. But I think you might be overestimating how fun you are."
    m "I think {i}you{/i} might be overestimating how fun a goldfish is. Card, please."
    s "..."
    m "This is not a joke. We have already wasted far too much time."
    s "Fine. But at least tell me where the two of us are supposed to meet back up. I don’t want to risk losing you in this crowd."

    scene mayafestival5
    with dissolve

    m "There’s a gazebo near the entrance with some picnic tables. Just meet me there."
    m "Also, what crowd? There’s barely anyone here yet."
    m "And “getting separated at the festival” is far too tropey for real life when we both know that any drama to spring up today will be from you saying or doing something disgusting."

    if bonus == True:
        s "Sure hope I don’t accidentally get anyone pregnant while buying your lunch."
    else:
        s "Sure hope I don’t accidentally get anyone hugnant while buying your lunch."

    scene mayafestival6
    with dissolve

    m "Have I ever told you how much I hate you?"
    s "Plenty of times."
    m "Just making sure."

    scene black
    with dissolve2

    "I give Maya one of my credit cards and thank whoever I was in the past for being responsible enough to carry two of them."

    if bonus == True:
        "Her ponytail bounces up and down as she runs off and, honestly, it’s probably the most active I’ve ever seen her apart from a few fantasies I don’t want to tell you about."

    "I stop in my tracks for a moment and observe my surroundings one more time before going in the opposite direction of Maya when I realize something."
    "I don’t think we’re in the old district right now."
    "But..."
    "I don’t think we’re in the new one either?"
    "..."
    "Where is this place?"

    if amifingered == True and bonus == True:
        q "You there!"
        q "You look like the kinda guy who could use a nice pair of melons!"

        scene mayafestival7
        with dissolve2

        q "We’ve got normal melons! We’ve got {i}square{/i} melons! We’ve got {i}triangle{/i} melons! Any kinda melon you can dream of!"
        q "So long as it’s one of those three shapes. Anything else, you’re gonna have to join the waitlist for."

        if sarasex == True:
            s "Wait...I’ve seen you before."

            scene mayafestival8
            with dissolve

            q "Oh?"
            s "Yeah. Didn’t we bump into each other in the middle of the night once or something?"
            q "Hmm...yeah! You were the guy with the phone!"
            s "That isn’t exactly how I would describe myself, but yes. I was the guy with the phone."
            q "Glad to see you made it back in one piece."
            s "And I’m glad to see you’re a...melon salesperson."
            q "Oh, this? This is just a temporary thing."
            q "I don’t even really like fruit."
            s "Well, you have chosen a very peculiar line of work then."

        else:
            s "What other shapes would they even come in?"
            q "Beats me. But if you join the waitlist, you can probably find out."

        q "So, is it melon time? Or is it {i}not{/i} melon time? I’ve got a very limited supply, you know."
        s "It is most certainly “melon time,” but I think I should ask you to confirm the quality of said melons since the girl I’m here with today is a bit of a connoisseur."
        q "Wanna give ‘em a squeeze and find out?"
        s "That depends on whether or not the police will get involved."

        scene mayafestival9
        with dissolve

        q "Ahh, we’ve got a pervert on our hands! That’s great! I’ve worked with you types before."
        s "There are a lot of us in the melon trade."
        q "You know what? For today and today only, I’ll throw in a second melon half-off. One for the two of you to share."
        q "If she even wants to share, that is. As a melon connoisseur myself, I understand how tough it can be to share what you love with other people!"
        s "How much are they?"

        scene mayafestival10
        with dissolve

        q "They’re...uhh..."
        s "You don’t know the price of your own products?"

        scene mayafestival11
        with dissolve

        q "Six million!"
        s "Yen?"
        q "Pesos!"
        s "I don’t think I have any of those on me."
        s "How does 500 yen sound?"

        scene mayafestival12
        with dissolve

        q "500? That’s it? These melons are easily worth double that. I think. Probably."
        q "This is my first day on the job, so I’m not really sure. But that also means you have to be nice to me since I’m nervous and my feelings are easily hurt."
        s "Then...1,000 yen for two melons. Post discount."

        scene mayafestival13
        with dissolve

        q "Deal! Would you like these gift wrapped? I’ll do it myself for...oh, I don’t know...an extra six million pesos?"
        s "You seem dead set on that specific number and...currency. Mind if I ask why?"
        q "A magician never reveals her secrets!"
        s "You’re a magician now?"
        q "And an astronaut!"
        q "But right now, melons matter most!"
        s "I’m going to say no to the gift wrapping, but I wouldn’t mind getting your name."

        scene mayafestival14
        with dissolve

        q "My name? Why?"
        q "Are you flirting with me? Does the sale hinge on this?"
        s "No. It’s just to satisfy my own curiosity."

        scene mayafestival15
        with dissolve

        q "My name, huh..."
        s "Is there a problem with that?"
        q "It’s just that nobody’s ever asked me before."
        s "I find it hard to believe that no one’s ever asked you for your name."
        q "Hey, you can believe whatever you want to believe. You don’t have to pick up all the stuff I put down, Mr. Pervert."
        s "Please don’t call me that."
        q "Nope. That’s your name now. You have to live with it."
        s "..."
        q "..."
        s "{i}This is the part where you tell me yours.{/i}"

        scene mayafestival8
        with dissolve

        q "Nope! This is the part where I don’t tell you and you still buy my melons anyway!"
        s "Can I at least have the first letter?"
        q "Nope! All I’ll tell you is that it’s really funny."
        s "Your name is?"
        q "Hilarious. A real kick to the shin."
        s "Then I apologize for how much you likely get made fun of in school."

        scene mayafestival16
        with dissolve

        q "Who says I go to school?"
        s "You don’t? I just thought you looked a little young."
        q "Oooooh, is {i}that{/i} why you’re flirting with me? Cause I remind you of your students?"
        s "That’s not-"

        scene mayafestival17
        with dissolve

        s "Wait, how did you know I’m a teacher? I don’t remember telling you that."
        q "Uhhhhhhh...hahahah!"
        q "Two melons coming right up!"
        s "I don’t-"

        play sound "static.mp3"
        scene smileex with flash
        scene tree3 with flash
        scene mayafestival18 with flash
        stop sound

    else:
        "Oh well. {i}Where{/i} we are doesn’t change {i}what{/i} I’m doing. And if I don’t come back to Maya with roughly one truckload worth of assorted street foods, she’ll probably wipe my mind."
        "It doesn’t matter how much she secretly loves me- I will always be second to food."
        "And I respect that."
        "We all have our interests."
        "Hers are just less mentally destructive and more physically destructive than mine."
        "One by one, I stop at an assortment of food stalls and point to random items behind the counter that look inexpensive."
        "If Maya is going to answer with “yes” instead of a specific list of what items she wants, I am going to do everything within my power to save money."
        "Especially since I may actually be bankrupt by the time the two of us meet up again."
        "........."
        "......"
        "..."

    m "Oh, good. You’re back."

    "Smile Count: 4"

    s "Welp, there goes Ami’s college fund."

    if bonus == True:
        m "Oh, please. Ami’s never going to college. No one is."
    else:
        m "Ami is already in college."
        s "Oh. Right."

    s "How can you even eat all of this?"
    m "I’m a growing girl."
    m "Or at least I would be if it weren’t for the whole time loop thing."
    m "I guess I’m just doomed to be eternally hungry."
    m "So, what did you bring me?"

    if amifingered == True:
        s "Something I think you’re going to be very happy about."

        "Thankfully, one of the vendors saw me struggling to carry an entire buffet’s worth of food and let me borrow a shopping cart they were using to store extra ingredients."
        "And I’m glad they did- because there is no way I would have been able to carry two large melons in addition to the variety of hot dishes I got."

        scene mayafestival19
        with dissolve

        s "Happy birthday, Maya."
        m "Ah! Melon!"
        s "Two melons."
        m "Two melons!"

        scene mayafestival20
        with dissolve

        m "Where in the world did you even find those? I asked every single vendor I bought from if anyone here was selling any and they all said no."
        s "Some weird girl was selling them. She had other shapes, too. And a...melon waitlist or something?"

        scene mayafestival21
        with dissolve

        m "Was there really a booth like that here?..."
        m "I had no idea."
        m "We’ll have to stop again before we leave."

        scene mayafestival18
        with dissolve

        m "Anyway, what else? I already know I’m saving the melons for last."

    else:
        "Thankfully, one of the vendors saw me struggling to carry an entire buffet’s worth of food and let me borrow a shopping cart they were using to store extra ingredients."
        "And I’m glad they did- because there is no way I would have been able to carry all of this without some form of transportation."

    s "There’s...croquettes...taiyaki...some weird potato-on-a-stick thing...whatever {i}this{/i} is...some other things I don’t know the name of...and a live squid."

    scene mayafestival21
    with dissolve

    m "What am I supposed to do with a live squid?"
    s "I don’t know. I just blindly pointed at stuff from every booth and I guess I pointed at a live squid at some point."
    m "Can you go, like...kill it or something?"
    s "Asking me for my credit card is one thing. But asking me to {i}kill?{/i} You’re better than this, Maya."
    m "Am I? Because I’m pretty sure I’ve asked you to kill Noriko on several occasions and, if anything, I think I’d prefer to keep the squid alive if I had to choose between the two of them."
    s "I can’t wait until the day you two make up and start being friends. It’s going to be so sweet."

    scene mayafestival22
    with dissolve

    m "Ew, stop. At least wait until I finish eating to start saying stuff like that."
    s "Maya, there is so much food here that it is going to take you the rest of the festival to eat it all even {i}if{/i} you manage to eat at your normal breakneck pace."

    scene mayafestival23
    with dissolve

    m "Do not underestimate my love for food."
    m "Festivals are to me what the dorm rooms of [teenage]girls are to you- a place where I can be free. Where my hunger can never be sated."
    s "I don’t know. My hunger is normally sated after half an hour or so. Sometimes, even less."

    scene mayafestival24
    with dissolve

    m "Why do you say things like this to me?"
    s "Because I know you won’t think any less of me."
    m "I literally can {i}not{/i} think any less of you."
    s "Yeah, exactly."
    m "..."
    s "..."
    m "Itadakimasu."

    scene black
    with dissolve2

    "One by one, Maya tears into each plate and-"
    "Well, I guess {i}tear{/i} probably isn’t the right word since she somehow manages to look graceful even while consuming more than some villages do in an entire week."
    "But she eats everything without lessening her pace even once."
    "The sun begins to set as she does so, and the air begins to turn a bit colder- but that’s to be expected since it is {i}technically{/i} still winter."
    "Sure, the two of us were gifted a relatively warm day by Mother Nature, but only until it was time for her to go out and party with her other cougar friends."
    "As Maya eats, well, {i}everything-{/i} I slowly pick at a bowl of ramen that, at least to my unrefined palate, doesn’t compare much to what Tsuneyo makes."
    "But it’s warm enough to battle the encroaching cold and gives me something to do while waiting for the first stage of Maya’s favorite day of the year to end."
    "........."
    "......"
    "..."

    if amifingered == True:
        scene mayafestival25
        with dissolve2

        m "MMMMMM!!!!!~~~~"

        "Just as she said she would, Maya saves the watermelon for dessert."
        "And yes, she did finish {i}everything-{/i} including the remainder of my ramen which, despite my worsening hunger, I was not able to finish."
        "I recall her saying in the past that she doesn’t like being watched while she eats and, this isn’t me being weird or...fetishy, but I’m glad she seemingly abandoned that insecurity today."
        "There’s something oddly satisfying about seeing a girl so far detached from joy being enveloped by it that I can’t help but feel a little warmer inside."
        "Maybe that’s why I couldn’t finish my food."
        "I was already warm enough."

        s "Enjoying yourself?"

        scene mayafestival26
        with dissolve

        m "A bit."

        "Smile Count: 5"

        m "And you?"
        s "For now. I’m sure that will change once I look at my credit card statement."
        m "At least Ami will still have a home when your house is repossessed."
        s "So, what’s the next phase of your game plan now that you’ve eaten from roughly every stand at this festival?"
        m "Hmm..."
        m "Have you changed your stance on goldfish at all in the last hour or so?"
        s "I can’t say I have."
        m "Then I suppose it would be best to avoid Kingyo-Sukui. Or any other games for that matter since you’re horrible at them and I don’t want any of the prizes."
        s "Pretty sure that just leaves more food, then."
        m "Don’t forget what day it is. We still need to visit a shrine and pay our respects for the year or god might kill us. That seems like a thing he would do."
        s "God sounds like an asshole."
        m "You’re just realizing that now?"
        s "Nope. Just reinforcing the belief with some help from you."
        s "I guess we can get our fortunes while we’re there too. That seems like another...{i}festivaly{/i} thing to do."
        m "Not necessary."
        m "I draw the same one every time."

        scene black
        with dissolve2
        stop music fadeout 10.0

    "We collect our garbage, dropping everything off at a nearby receptacle."
    "The squid (Still alive, albeit just barely) is left there as well- clinging to life atop a stack of dirty plates."
    "It covers its body in a variety of sauces, seasoning itself before death, in a desperate attempt to seek out water and prolong its unappreciated existence."
    "Neither of us have the heart to kill it, but we have the heart to watch it die."
    "And that must count for something."

    $ renpy.end_replay()
    $ maya_love += 1
    $ mayafestival2 = True

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "........."
    "......"
    "..."

    jump mayafestival3

label mayafestival3:
...
```

## Code that triggers this event

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
if bonus == True:
        s "You don’t need to beg me to keep me from fathering any children, Maya. I can assure you that is the last thing I want to do."
    else:
        s "Ughhhhhhhhhh can we go already?"

    m "You still haven’t answered the question. Is it-"
    s "Yes."
    s "It’s possible."

    scene mayabday20
    with dissolve

    m "I see."
    s "But I have no idea whether it’s true or not. So you’ll have to confront Ayane yourself if you want to know."
    s "Unless you’d rather just wait until we’re on the roof to find out, because there’s not much we can do at this point."
    m "..."
    s "..."
    m "..."
    s "Are you really sure that’s what it is, though? "
    m "Are you asking because you’re acknowledging the possibility that you may have planted your seed inside of others as well?"
    m "And, if that’s the case- are you confused by how only {i}Ayane{/i} has made it there?"
    m "Because these are things I’ve questioned myself as well. And I don’t know."
    m "I just don’t know."

    scene mayabday21
    with dissolve

    m "But I can’t think of any other reason why it would happen."
    m "And I've tried."
    m "The further we move into uncharted territory, the higher the potential is for risk."
    m "And I’m..."
    s "..."
    m "..."
    m "I’m finally starting to feel something again."
    m "I don’t want that to go away."

    "{i}A moment of silence.{/i}"

    s "Are you scared?"

    "{i}A crack in the glass.{/i}"

    m "Yes."

    "{i}A light in the attic.{/i}"

    scene mayabday22
    with dissolve

    m "Because I think that it might."

    scene black
    with dissolve2

    "{i}A dream of the past.{/i}"

    "The conversation drops dead after Maya’s revelation, but I must be forgiven for getting lost on this particular train of thought when the route-map is tangled up like wires."
    "I don’t want to believe her but, at this point, I feel like I have to- because {i}I{/i} can’t think of any other reason Ayane would have made it up there with us either."
    "The gap we accidentally create in our morning is subsequently filled by a collage of uncomfortable glances and scattered trips to the refrigerator."
    "Nothing is ever inside."
    "At least nothing that either of us want."
    "It ends, though- but I imagine that’s just because Maya wants to forget about this and focus on the rest of the day. "
    "She wants to eat. "
    "She wants to walk around. "
    "She wants to talk about things I’m not interested in and have me pretend that I am."
    "And strangely enough, I want to do all of those right now as well."
    "But we still have a few more hours of sunlight."
    "And many more unsuccessful trips to the refrigerator."

    $ renpy.end_replay()
    $ mayafestival1 = True
    $ maya_love += 1

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}Two hours pass.{/i}"
    "{i}Maya changes into her yukata in the comfort of her best friend’s bedroom.{/i}"
    "{i}She looks beautiful.{/i}"

    scene mayabday23
    with dissolve2

    "Smile Count: 3"

    s "Welp...it will definitely be hard for anyone to take you down in your pursuit of being the cutest girl at the festival."
    m "For today and today only, I’ll allow you to say that as many times as you want without fear of being insulted."
    s "It might be good to turn the cockiness down a little, though. Even if it is well warranted."
    m "It’s my birthday. I can be as cocky as I want."
    m "Now, let’s get out of here before Ami comes home. I’m hungry and don’t want to deal with her today."

    scene black
    with dissolve2

    s "Well, thank you for making the time for me..."

    "........."
    "......"
    "..."

    jump mayafestival2
...
```