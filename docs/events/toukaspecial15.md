# A Commoner's Tour of Summer
Touka event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=toukaspecial15&go=Go)



## Event preconditions
✅Touka love greater than or equal to 15

❌Event "[Touka: House Call](./toukadorm10.md)" is completed (event=toukadorm10)



## Next events
None

## Event properties
* ID: toukaspecial15
* Group: Touka
* Triggered by label: toukastreets
* Triggered by branch label: saturdaymorning

## Event code
File: \game\ToukaEvents.rpy
Code:
```python
...
label toukaspecial15:
    scene sky
    with fade
    play music "marshmallow.mp3"

    "I begin my voyage to...wherever the wind takes me bright and early. "
    "In fact, it’s so early that the wind hasn’t even woken up yet, so I’m kind of just going in a straight line and not being {i}taken{/i} anywhere."
    "I guess that’s fine, though, considering that the area I normally meet up with Touka in is a {i}mostly{/i} straight shot from my home."
    "I {i}also{/i} guess that since I just mentioned Touka, there’s a high likelihood that I’ll bump into her and take her on the makeshift commoner’s tour of summer that she wants."
    "It’s a good thing I’ve spent so long looking up and preparing different activities I think she’ll thoroughly enjoy."
    "That was sarcasm if you couldn’t tell."
    "I have absolutely no idea what the two of us are going to do today when we inevitably meet."
    "But at least we’ll get to be alone."

    to "Oh. Good morning, Sensei."

    scene toukatrain1
    with dissolve

    "Or not."

    s "Good morning, entire Tsukioka family."
    to "Well, it’s...not the {i}entire{/i} family without my father."
    s "Yeah, but he doesn’t really matter to me."
    tk "Good morning, commoner teacher man! We are ready to walk among you and your people! We come in peace!"
    s "Good morning, mini Touka. I like your shirt and I’m sure there won’t be anyone around today who is offended by it."

    scene toukatrain2
    with dissolve

    tb "I tried very hard to get her to wear something else, but she was insistent on trying to look like “As much of a commoner as possible.”"
    tk "Of course I was! Talking to Chinami has made me realize how important it is to make time for those smaller and less significant than me!"
    tb "I understand that, but...I don’t really think your shirt will accomplish that, dear."
    s "Honestly, though, if “looking normal” is what you were all going for, Tsukasa is, weirdly enough, the closest out of everyone."

    scene toukatrain3
    with dissolve

    to "With a shirt as...{i}direct{/i} as that? How is that possible?"
    s "I don’t know. You two just sort of...exude wealth. Tsukasa just looks like a weird kid."

    scene toukatrain4
    with dissolve

    tk "Wha- weird?! Who do you think you are belittling, peasant?! I am Tsukasa Tsukioka! I am royalty! I am-"
    s "A weird kid."

    scene toukatrain5
    with dissolve

    tk "You told me he was nice."
    to "Is “nice” the word I used? Because I specifically recall using the word “fine” to describe him in place of that."
    s "That’s a lot closer, but still a bit off."
    tb "I hope you don’t mind that Tsukasa and I decided to tag along for your summer tour today. She just wouldn’t take no for an answer when she heard about it and..."
    tb "Well, let’s just say it’s been quite a while since I’ve really ventured off for the sole purpose of leisure as well."
    s "It’s fine, but I still think you guys are making a much bigger deal out of this than it really is."
    s "Like, I still have no idea what to even do today."
    s "I tried telling you before, but I’m not really the best person to ask about “fun” stuff like this."

    scene toukatrain6
    with dissolve

    to "You don’t have {i}any{/i} ideas? At all?"
    s "I mean, you’ve already been to the beach. That about sums up my knowledge of summer."
    s "I guess there are public pools too, but those are somehow even less fun and probably underwhelming for people of your...status."
    to "Our “status” is precisely what we are attempting to leave behind today, Sensei. Why else would we have dressed so casually?"
    s "Sorry, is that dress supposed to be casual? Because it really just looks like you’re trying to impress someone."

    scene toukatrain7
    with dissolve

    tb "How funny. That’s exactly what I told her before we left the manor this morning."
    to "Mother! Please!"
    s "The same goes for you as well, Tsubasa."

    scene toukatrain8
    with dissolve

    tb "Hm? I beg your pardon?"
    s "Just a little overdressed for the occasion is all. Us “commoners” don’t normally wear our family crests on our necks."

    if bonus == True:
        "We also don’t wear shirts that look like they’re going to come unbuttoned at any moment for the most part, but I guess that ones a sort of case by case basis."

    tb "But I...can’t simply leave the crest at home like Touka and Tsukasa do. Not as the wife of the Tsukioka Foundation’s chairman. It must remain on my person at all times."
    to "Father wouldn’t know if you took it off for a day out on the town, Mother."

    scene toukatrain9
    with dissolve

    tb "Touka, please. This isn’t like a wedding ring. I can’t just...take it off whenever I want."
    to "Do you...really not have anything planned, Sensei? Because I’d feel rather embarrassed to have brought my family along for...absolutely nothing."
    to "Not to mention getting dressed for the occasion- even if it’s not quite up to par with what you’d expect someone closer to your...level of income to be wearing."
    s "I really don’t. So if the three of you want to go back home and-"
    tk "I have an idea!"

    scene toukatrain10
    with dissolve

    tb "Tsukasa, {i}please{/i} tell me it doesn’t involve a kitchen."
    tk "It...probably doesn’t?! I don’t know!"
    s "What’s your idea, Tsurumi?"
    tk "My name isn’t-"
    to "He has a memory problem, Tsukasa. Just accept it."
    tk "Fine! Okay!"
    tk "I, Tsurumi Tsukioka, demand that you take us to the thing called a “subway!”"
    to "You don’t have to accept the name, Tsukasa."
    tk "Why is adult life so confusing?!"
    tb "Tsukasa, dear. Why do you want to see the subway exactly? This was supposed to be a tour of...various summer related activities."

    scene toukatrain11
    with dissolve

    tk "Because it’s the first thing that comes to mind when I think of people who have less money than us!"
    tk "What screams “poor people” louder than a bunch of sweaty commoners paying money to get  crammed into a rectangular metal box underground?"
    tb "I...suppose that is a fair point?"
    s "Is it?"
    to "Is the subway...you know...{i}safe,{/i} Sensei? Because it’s come up in several of the instructional videos I’ve watched at home about safety."

    scene toukatrain12
    with dissolve

    tb "Touka raises a good question- {i}is{/i} the subway safe? Because I remember gropers being a bit of a problem when I was Touka’s age."
    tk "What’s a groper?"
    s "A thing that very likely doesn’t exist around here anymore on account of the severe drought in testosterone."
    tk "What is testosterone? A food?"
    s "The subway should be fine. I just don’t ever really ride it since there’s not much of a need, though."
    s "I also don’t think it will be very fun, but who am I to tell anyone how to have a good time when one of Touka’s key interests is horses?"

    scene toukatrain13
    with dissolve

    to "I’m sorry, do you have an issue with {i}horses{/i} now? Because, last I checked, they were majestic, smart creatures who have been serving us longer than nearly any other animal for nothing in return."
    s "Yeah, hearing all that gives me hope that you guys might like the subway after all."
    to "I don’t...ugh."
    to "Forget it."
    tb "Well...I suppose it’s better than nothing. Seeing how the layman moves from place to place could be a wonderful, educational experience for my daughters."
    tb "I suppose there’s just the matter of figuring out where to ride the subway {i}to.{/i}"
    s "We’d have to figure that out when we go down to the station. Like I said, I don’t ride it very often, so I have no idea where it even leads."

    scene toukatrain14
    with dissolve

    tk "Never fear, teacher man! I used my {i}smartphone{/i} this morning to memorize the route map for each individual train!"
    tk "Do you know what a smartphone is? Or are you too poor to-"
    s "I have a smartphone, Tsurumi. They’re accessible to {i}my people{/i} now."
    s "Also, there is no way you memorized the route map for every train."
    tb "Oh, I wouldn’t put that past her. Tsukasa might be a handful, but she’s actually quite the little genius for her age. Her memory is near photographic as well."
    to "If you’ve wanted to ride the subway that badly, why haven’t you asked Father to simply build us one under the manor? He’s talked about it in the past as a means for staff members to get around."

    scene toukatrain15
    with dissolve

    tk "It wouldn’t be the same! There are no poor people at our house! And everyone is constantly speaking in different languages that only Mother understands!"
    to "Well...as long as Sensei is okay with it..."

    scene toukatrain16
    with dissolve

    to "But if you get lost, we’re not coming back for you. You’re going to have to find a new family."
    tk "Mother! Touka is being mean to me!"
    tb "Is the station far from here, Sensei? Should I wave down a taxi or summon us a limo?"
    s "Have you really been cooped up in that manor for so long that you think taxis are just driving around suburban areas looking for passengers?"
    tb "Yes."
    s "Oh."
    s "Well, they’re not."
    s "The station is literally right behind you, though. We can be there in less than five minutes if we want."

    scene toukatrain17
    with dissolve

    tk "That’s it?!"
    tk "What are we waiting for then?!"
    tk "Take us to the peasant version of a sardine can already, Mr. Teacher!"

    scene black
    with dissolve2

    if bonus == True:
        "I gesture toward the station behind the Tsukiokas and begin to make my way over, only to be followed closely behind by them like they’re a pack of high class escorts."
        "Well, two of them at least."
        "Or one."
        "I’m followed closely behind by three girls who look nothing like me."
        "Which is...probably nowhere even close to my initial perception of what the sight appears to be."
        "Anyway. Subway station."
    else:
        s "I can't wait to get my groove on in the subway."

    scene toukatrain18
    with dissolve

    tk "This way, Mother! Follow the scent of standing water and processed meats!"
    tb "Tsukasa, dear, are you sure this is the right way? It’s been a long time, but I think we may have to visit a ticket kiosk of some sort first."
    to "I’m...sorry I dragged them along, Sensei."
    to "Well, I suppose it was less of me {i}dragging{/i} them and more of them simply latching onto my dress and seeing where it leads."
    s "It’s a nice dress."
    to "Is that how you really feel? Or are you just saying that because it’s currently a three-for-one deal?"
    s "That’s how I really feel. It fits you well."
    to "Well...thank you, Sensei. I appreciate that."
    s "Like, {i}really{/i} well."
    to "And there you go, ruining yet another moment where I believed you to be a good man for a fraction of a second."

    scene black
    with dissolve2

    "Tsukasa, who somehow managed to get in front of all of us (Likely due to her difference in size), leads the way to a random train that, at least I {i}hope{/i} she’s actually memorized the path of."
    "All things considered, there are a few areas of this city I don’t really see fit for the Tsukioka family just yet."
    "Sure, Touka was able to survive a trip to the Old District, but if anything like what happened with Yumi and I were to happen in front of an entire family- let alone one as influential as this..."
    "Well, let’s just say Ami might never see me again."
    "Or anyone for that matter."
    "So...yeah."
    "Here’s hoping the train stops somewhere other than impending doom and tragedy."
    "........."
    "......"
    "..."

    scene toukatrain19
    with dissolve

    "We make our way into a subway car and, contrary to Tsukasa’s description from earlier, it’s not like we’re being packed in at all."
    "I’m sure that roughly half of the population no longer being around has something to do with that, but I’m not about to complain about an actual convenience when I understand how bad it could have been."

    to "Does it always smell this...{i}horrible{/i} in here?"
    s "Probably."
    tk "Hi. I’m Tsurumi Tsukioka, a poor person just like you. But you can probably tell on account of my shirt."
    tb "Tsuka- ahem."
    tb "Tsurumi dear, please don’t pester the other passengers."
    tk "What is your favorite commoner activity? Mine is watching the news."
    tb "{i}Tsurumi,{/i} that woman is asleep. Please do not wake her up."

    scene toukatrain20
    with dissolve

    to "So, what do we do now? Are there any...private compartments for groups of three or more?"
    tb "I don’t believe that sort of thing is available on subways, dear. From what I understand, this is a form of local transport used to get from one place to another in a quick, uncomplicated manner."
    to "So...we all just...stand in this small space together until we get to our destination? Is there a...gift shop? Or a...restroom, even?"
    s "Nope. Just other duplicates of this exact subway car, all chained together in typical poor person fashion."

    scene toukatrain21
    with dissolve

    tk "Okay, Mother. I’m over this. It looked more fun on the Internet and all of these people look really sad."
    tb "Well, I assume that’s because they are."
    tb "Also, we can’t leave just yet dear. The train has just started moving."

    scene toukatrain22
    with dissolve

    tk "Well, then ask them to stop! This is boring!"
    tb "It doesn’t work that way, dear. I think. I’m not really sure."
    s "You’re right. It doesn’t."
    tb "Exactly. It doesn’t work that way, dear."
    to "Tsukasa, this was {i}your{/i} idea. And, pardon the pun, but...you have to ride it out to the end."
    s "Nice pun."
    to "I said pardon it, Sensei."
    tk "I don’t have to do anything! {i}We{/i} don’t have to do anything! We’re rich! We probably own this stupid subway car!"
    tb "Not yet. But give it a few years, sweetie. Who knows what your father’s next big plan will be?"

    scene toukatrain23
    with dissolve

    to "Are we allowed to sit down on this subway thing? Or do we need to pay extra for that?"
    s "You need to pay extra. There are doors connecting the cars. Take the ones on your left all the way to the end and ask the person in the room at the head of the train for permission and a seating ticket."

    scene toukatrain24
    with dissolve

    to "Oh! I believe I’ve heard of that person before. The...conductor, I think?"
    s "Sure."
    tb "Was that always a rule?..."
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

label toukaspecial15p2:
...
```

## Code that triggers this event
File: \game\ToukaEvents.rpy
Code:
```python
...
label toukastreets:
    if touka_love >= 0 and toukastreets1 == False:
        jump toukastreets1
    if touka_love >= 5 and ramen20 == True and convenience5 == True and toukadorm1 == True and toukastreets5 == False:
        jump toukastreets5
    if touka_love >= 15 and toukadorm10 == True and toukaspecial15 == False:
        jump toukaspecial15
...
```