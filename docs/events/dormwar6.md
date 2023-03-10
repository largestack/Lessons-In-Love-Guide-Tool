# Sphenopalatine Ganglioneuralgia (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Friend Zone Fight!](./dormwar5.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwar6
* Group: Main
* Triggered by label: dormwar5
* Chain sources: dormwar5
* Chain sources path: dormwar5

## Official wiki page

[Sphenopalatine Ganglioneuralgia](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar6&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label dormwar6:
    scene knowledge1
    with dissolve
    play music "happyandplotting.mp3"

    u "Ladies and gentlemen! Friends and family! Molly!"
    mo "WHY?!"
    u "The time has come for one of the most heated matchups in all of the first annual Super Mega Ultimate Dorm War!"
    a "Wait, wasn’t it “Super Ultimate Mega?”"
    u "No! Get with the fucking program, Ami!"
    a "My bad..."

    scene knowledge2
    with dissolve

    u "Today’s contest will be conducted trivia style!"
    u "Each team has selected several smart person question thingies designed to stump the member of the other team!"
    u "The contestants have {i}not{/i} been included in the selection of their opponent’s questions!"
    u "In the event of a tie, Makoto and Nodoka will arm wrestle to determine who the winner is!"
    mi "Don’t let her lick you, Makoto! "
    mak "First off, it won’t come down to a tie."
    mak "Secondly, I highly doubt Nodoka would employ the same strategy as Kirin when it comes to an arm wrestling match."
    no "I mean..."
    no "I wouldn’t be {i}opposed{/i} to licking you."
    mi "See?! It’s a real strategy now!"
    u "Silence!"
    u "Ami! Please do the honors of introducing today’s combatants!"
    a "Oh. Uhh, okay. Yeah."

    scene knowledge3
    with dissolve

    a "Representing the first floor is Makoto Miyamura!"
    a "Her favorite subjects are math and science and she enjoys taking long walks on the beach and candlelit dinners!"
    a "A fun fact about her is that she has webbed toes!"

    scene knowledge4
    with dissolve

    mak "I do not! And don’t just make up random facts about me as part of my introduction!"
    mi "I’ll still love you no matter what kinda deformities ya have, Makoto!"
    mak "I don’t have any deformities! Just get on with the competition! This is ruining my focus!"

    scene knowledge5
    with dissolve

    a "And representing the second floor, we have Nodoka Nagasawa!"
    a "As you can tell, she likes coffee! But don’t let that fool you! Her drink of choice is tomato juice and she needs to drink it every two hours or she will die!"
    a "She also spends her free time singing the “Happy Birthday” song to herself in the mirror and-"
    a "Wait, Uta, I can’t say this part."
    u "Hm? What’s wrong? Did I put somethin’ weird in her intro?"

    scene knowledge6
    with dissolve

    a "Well, not weird but...I don’t think it’s true that her and Futaba are having a baby."
    f "I’m sorry, what?"
    no "It’s true. We are deeply in love and I am carrying her child. "
    mak "Enough with these weird introductions! Just hurry up and start asking the questions!"
    mi "Jeez, Makoto. You’re really fired up now, huh?"

    scene knowledge7
    with dissolve

    mak "Of course I am. We’re still coming off a loss from the last round and I need to prove to everyone that Nodoka is no smarter than I am."
    u "Since Makoto is rarin' to go, let’s get right down to it!"
    u "In order to keep things fair, I’ll be asking the questions to Makoto and Ami will be asking the questions to Nodoka."

    scene knowledge8
    with dissolve

    u "So, Makoto..."
    u "Cells can be defined as either eu...eukary...otic or-"
    mak "Prokaryotic. Next question."
    mi "Heck yeah! We win!"
    u "Wait, no. Hold on. I didn’t even finish reading the question."
    u "Cells can be either...eukaroyotic or...that thing Makoto said. But which of these categories does bacteria fall into?"
    mak "That would be..."
    mak "Prokaryotic. All bacteria are unicellular."
    u "That is..."

    scene knowledge9
    with hpunch

    u "Correct! First point goes to Makoto!"
    m "That question wasn’t really that hard, though."
    mi "The heck you talkin’ about, Maya? I’ve never even heard like half of those words before."
    mak "Well then you should probably pay more attention in class, as we have definitely studied them."

    scene knowledge5
    with dissolve

    a "Okay! So now that the first floor is on the board, it’s time for Nodoka’s first question, I guess..."
    a "Let’s see...umm..."
    a "Nodoka, who is the only US president to ever get married inside of the White House?"
    t "Attack!"
    mo "This is a passive battle, Kendo Princess. There will be no attacks."
    t "Then the other team will not see it coming! Go! Fight! Win!"
    no "Umm..."
    no "..."
    mo "..."
    t "!!!"
    no "Chuck E. Cheese?"
    mak "Wha-"
    a "Uhh...no. The answer is actually Grover Cleveland."
    no "Oooooh, right. Silly me, always confusing those two things."
    mo "That’s fine! You can get one or two wrong! Shake it off, Nodoka!"

    scene knowledge10
    with dissolve

    mak "Uhh...what are you doing?"
    no "What do you mean, class representative?"
    mak "I mean that if you don’t know the answer to a problem, don’t just throw a random one at it to make it look like you’re getting it wrong on purpose."
    mak "Either take this seriously or just concede now."
    no "Okay, okay. Sorry. I’ll try harder next time. Promise."
    u "Right! Well, to keep things moving..."

    scene knowledge11
    with dissolve

    u "Makoto, if you had to give a name to the...parallel latitude approximately 23 degrees north of the equator, what would it be?"
    mak "Are you...asking me to personally give it a name of my choosing? Or are you asking me what it’s called?"
    mak "That question wasn’t worded properly."
    u "Well excuse me, princess. What’s that place called?"
    mak "I..."
    mak "The...Tropic of Cancer, I think?"
    u "That is..."

    scene knowledge12
    with hpunch

    u "Correct again! Another point for the first floor, even though Makoto snapped at me!"
    mak "I’m sorry, Uta. I’m just a little caught up in the moment right now."

    scene knowledge13
    with dissolve

    f "See? That one was a little harder, wasn’t it?"
    m "It was. But it’s still nothing compared to a lot of the stuff Ayane and I came up with for Nodoka. "
    m "I can’t see Makoto losing if she’s just going to keep getting questions with precise answers that she’s already memorized."
    f "Well, I...wouldn’t be so sure about that. Nodoka's really smart."
    f "So...I’d wait another round or two before passing judgement..."

    scene knowledge14
    with dissolve

    a "Nodoka, what is the correct scientific name of the “zombie fungus” that infects and controls the minds of insects, most commonly ants?"
    mo "Oh! Oh! I know this! I actually know this!"
    mo "I played a game inspired by that! "
    no "Hmm...zombie fungus..."
    no "What do I know about zombie fungus?..."
    no "…"
    mo "…"
    t "…"
    no "Portobello mushrooms?"
    mak "…"
    a "…"

    scene knowledge15
    with dissolve

    t "We got a point!"
    mo "No we didn’t, Tsuneyo."
    mo "The correct answer was {i}Ophiocordyceps.{/i}"
    a "I am glad Molly said that because I could definitely not pronounce it."
    ya "Oh, how wonderful it must be to have your brain invaded by fungus."
    ya "Think of all the possibilities that would open up for you if you did not have to use up your energy on performing basic functions and allowed a parasite to take over instead?"

    scene knowledge16
    with dissolve

    mo "So, do you like, {i}only{/i} play chaotic characters? Or do you branch out into different stuff sometimes?"
    ya "I beg your pardon?"

    scene knowledge17
    with dissolve

    a "I can’t believe I’m saying this...but good job, Makoto! Keep it up and we’ll have another victory in no time at all."
    u "I’d like to say the same to Nodoka, but apparently her weird encyclopedia brain is taking a nap right now."
    no "Oh, gosh darn it. I could have sworn I had that one."
    no "I’m sorry, Uta. I’m trying my best over here."
    u "Well your best friggin’ sucks right now! Ante up or we won’t get extra Sensei time at the beach!"

    scene knowledge18
    with dissolve

    mak "Just give up on that now, Uta. None of us intend to let you have Sensei."
    mak "Especially not when {i}we’d{/i} be losing out on him in the process."
    mak "Do you have any idea how valuable of an asset his time has become among the first floor girls? "
    mak "It’s essentially its own form of currency now."
    a "Watch it, Makoto! You might be winning, but he’s still {i}my{/i} [uncle] and he’d never date a weirdo with glasses!"

    if bonus == True:
        no "Then...was what happened between him and me in the cafe bathroom a lie?"
        no "My fragile [teenage]heart...to be tossed aside after my first time is-"
    else:
        no "I'm tired. Can someone get me some more coffee?"

    mak "Next question, please."
    u "Got it! But just so ya know, this is where things start heating up!"
    u "The questions you guys got have just been warm-ups so far."
    u "For the rest of the questions, teams from both floors got together and just started Googling a bunch of super hard stuff that none of you would probably ever know."
    m "Oh, okay. Here we go."
    mak "Well then I’ve basically won already, haven’t I? "
    mak "Looks like Nodoka has learned a valuable lesson today about taking even the first rounds of a competition seriously."
    no "Hey. Settle down or I’ll be forced to come over there and lick you."
    mi "Run, Makoto! I’ll hold her off!"
    mak "A genius never runs from...knowledge."
    t "Inspiring."
    mak "Just ask the next question already."
    u "Got it!"
    u "Makoto! What is the scientific name of the oldest potted plant in the world and where is it located?"

    scene knowledge19
    with dissolve

    mak "Oh. So you’re literally just going to ask questions that are impossible to answer."
    u "Not even going to guess?"
    mak "And say what? Chuck E. Cheese or portobello mushrooms? No thanks. "
    mak "I’m proud enough to accept when I don’t know the answer to something, and I’m not going to trick everyone into thinking I’m just throwing the question away."
    no "Can I try?"

    scene knowledge20
    with dissolve

    mak "I mean...sure. If you want to continue wasting everyone’s time, be my guest. "
    a "You can try, but...since it’s not your question, I don’t think you should get any points for it."
    no "That’s fine. I don’t need any points for knowing that the oldest potted plant in the world is the Kew Gardens’ encephalartos altensteinii."
    a "Um...well I don’t have the card, so-"
    u "Damn it, Nodoka! How come you can answer her questions but not your own?!"
    mak "Wait, was that the correct answer?"
    u "I can’t read the whole word but...probably! "
    mak "Give me the card. Let me see."
    u "What if I just hold it up like this? Can you see it from there?"
    mak "I can see that she’s likely just guessing a-"
    mak "Wait, no. That’s correct. "
    no "Yaaaaaaay. Now get over here and let me lick you.."

    scene knowledge21
    with dissolve

    o "Welp, here we go. Makoto’s screwed unless she’s somehow also another fountain of knowledge."
    r "What do you mean?  Nodoka doesn’t even have any points yet. And even if she was doing it on purpose, she’s gotten both of her questions wrong so far."
    o "Yeah. She tries to throw everyone off of her trail by pretending to be less smart than she actually is when it comes to stuff like this."
    o "But the truth is that she actually loves the spotlight and was just waiting for the right time to step into it."
    s "Why are you two standing next to me just half an hour after ruining my morning?"

    scene knowledge22
    with dissolve

    r "We’re here to make you feel better!"
    o "Hang in there, bud. It’s not like it’s impossible to escape the friend zone."
    r "Exactly! Just because you had to deal with us being kinda mean to you for a few minutes doesn’t mean it’ll always be like that."

    if rinbetrayed == True:
        if bonus == True:
            r "Like, who knows? Maybe you and Otoha will go back to your place after this contest and just completely toss me out of the picture because my feelings don’t actually matter to you."
        else:
            r "Like, who knows? Maybe you and Otoha will start a band after this and I won't be invited to open up for you guys when you start touring!"

        r "That would be like, so crazy, right? Hahahah."

        scene knowledge23
        with dissolve

        o "Uhh...no. That would be pretty horrible."

    else:
        r "Like, I don’t even really consider you in the friend zone for me. You’re just Sensei and I’m just Rin."
        r "We’re friends, but like-"

        if bonus == True:
            o "But you’ve also kissed and he’s seen your boobs before."
            r "Yeah. That."
            r "And I also was a {i}clear{/i} loser today, so...maybe that’s saying something?"
            o "It’s saying you both should probably shoot a little closer to your respective age groups and-"
        else:
            o "But you've also kissed before."
            r "Yeah, but only for like ten minutes."
            o "That's...actually a lot longer than I thought it-"

        sr "Shut up, Otoha."
        o "…"
        o "Aight."

    scene knowledge20
    with dissolve

    a "Okay, Nodoka...your next question is-"
    a "In what year did Roger Tory Peterson first release his famous “A Field Guide to the Birds?” and by which company was it published by?"
    no "You expect me to know the release year and publishing company of an ornithologist’s field guide?"
    a "Well, no...but-"
    no "Because I do. It was published in 1934 by the Houghton Mifflin company. There are actually several copies kept at the Joseph F. Cullman 3rd Library of Natural History, in case you were wondering."
    no "Books are cool."
    mak "Who’s idea was it to ask her a literature question?! She clearly only knows the answer to that because it’s a key interest of hers."
    no "Right. Just like the encephalartos altensteinii."
    no "I have very specific interests."

    scene knowledge24
    with dissolve

    mi "Wow. That Nodoka girl really isn’t messin’ around anymore, is she?"
    mak "She just had a lucky streak of knowing two answers in a row. It’s nothing to write home about."
    u "Then, here’s a question a math whiz like you should be able to handle easily, Makoto!"
    u "No bells or whistles, just a straight up calculationy problem."
    u "Makoto Miyamura! What is the answer to...584 divided by 39?"

    scene knowledge25
    with dissolve

    mak "That’s..."
    mak "It would be approximately...15?"
    u "That is..."

    scene knowledge26
    with hpunch

    u "Correct!"
    mak "Ha! I-"
    u "Kind of!"
    mak "…"
    mak "What do you mean, “kind of?”"
    u "It says here that I need at least the first three decimal points since it’s not {i}technically{/i} 15."
    mak "Of course it’s not {i}technically{/i} 15, but expecting someone to be able to do specific math like that without a calculator is-"
    no "Easy. 14.974."
    no "Next question please."

    scene knowledge27
    with dissolve

    mak "That..."
    mak "She’s wrong, isn’t she?"
    u "Nodoka is correct!"
    u "Unfortunately, the point can not go to her since it was not her question. But at least we’ve all learned something today!"

    scene black
    with dissolve

    "{i}Roughly ten minutes later...{/i}"
    "………"
    "……"
    "…"

    scene knowledge28
    with dissolve

    a "So...Nodoka has nine questions right and Makoto has four."
    a "Which means if Nodoka can get this one right, the game is over."
    m "That girl is not human."
    mi "This contest is rigged! Somebody’s been feedin’ Nodoka the answers! Nobody is that smart!"
    mak "Just...let her ask the next question, Miku."
    a "Nodoka...to win the game-"
    a "What is the proper scientific name for “brain freeze?”"

    scene knowledge29
    with dissolve

    no "Before I win, there is something I would like to say to clear the air."
    u "Okay, but make it quick! I’ve gotta get over to work for my rap battle with Ayane like, as soon as this is over."

    scene knowledge30
    with dissolve

    no "Makoto, you are a very impressive [young_girl] with a wide array of skills and talents at your disposal."
    no "And, under most circumstances, I would have been fine with allowing you to win."
    no "However, not only do I feel that doing so would greatly offend you, but we are competing for a prize I would very much like to have."
    no "So do not let my victory derail you from your path to greatness, but-"
    u "Okay, time’s up! Tell us the answer or we’re going back to Makoto and-"

    scene knowledge31
    with dissolve

    no "Sphenopalatine Ganglioneuralgia."
    t "Emerald Guardian! Call the ambulance! She is having a stroke!"
    u "Ami? The verdict?"
    a "Uhh...I think she’s right?..."
    a "Take a look at the card. What do you think?"
    u "Let me see..."
    u "…"
    a "…"
    u "Yup! Looks good to me!"
    u "The winner of the knowledge contest is Nodoka Nagasawa of the second floor!"

    scene knowledge32
    with dissolve

    mak "…"
    mi "Hey...it’s okay, Makoto."
    mi "Even the best teams in sports can lose to worse ones sometimes. One loss doesn’t mean you’re no good."
    mi "You’re still one of the smartest people in the[school]. Who cares if we lost a point in this round? We can just get it back later."
    mak "I don’t really care about the points, Miku. I wanted to win this for me."
    mi "Well then we can...go win somethin’ else for you! It’s not the end of the world."
    f "Yeah...you did great, Makoto. No one has ever even put up a fight with Nodoka before, so..."
    mak "That wasn’t a fight. That was a bloodbath."
    mak "She...played with me before wiping the floor with me. It wasn’t even close."

    scene knowledge33
    with dissolve

    u "Okay! Anyone who isn’t coming to the maid cafe for the next contest, please clean up the library!"
    u "Anyone who is, form a single file conga line behind Sensei and start gettin’ your butt into gear! Move, move, move!"
    r "Sensei! Let’s conga!"
    s "Please leave me alone."

    scene black
    with dissolve2

    "I watch Makoto as the rest of the girls begin to either pack up their things or...start doing the conga."
    "I think about going over to try and cheer her up but, frankly, if I were in her position, I’d want to be left alone right now."
    "It can’t be easy being so confident in something and then having to helplessly flail about when it comes time to show everyone {i}why{/i} you were confident."
    "But it wasn’t like any amount of studying could have prepared Makoto for a test like that in the first place."
    "The fact that she was even able to get two of the more ridiculous questions just goes to show how smart she actually is."

    no "Sensei, will you be joining us at the hotel tonight?"
    s "Hotel?"
    f "No one told you?"
    f "Ayane and Touka re-booked the hotel we stayed at for our Christmas trip."
    no "I’m tired and don’t know anything about rap music, so I’m going to go take a nap there."
    s "Didn’t you just drink like eight cups of coffee?"
    no "So what? I’ve been walking back and forth all day. I am {i}very{/i} tired."
    no "You should come hang out with us later when you’re done being a prize for everyone."
    no "You can hear more about the baby Futaba and I are having together."
    f "Please...stop telling people we’re going to have a baby..."

    $ renpy.end_replay()
    $ dormwar6 = True
    $ dorm2warpoints += 1
    stop music fadeout 5.0

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"

label dormwar7:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```