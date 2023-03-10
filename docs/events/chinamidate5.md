# Chinami-Corp (Chinami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Chinami love greater than or equal to 5

* Event [5,000 Year-Old Wizard](./chinamidate1.md) (Chinami) is completed)

* Event [Everything Horrible](./day128.md) (Main) is completed)

* chinaminumber equal to True (unknown variable)



## Next events

None

## Event properties

* Id: chinamidate5
* Group: Chinami
* Triggered by label: callchinamiafternoon
* Triggered by branch label: callafternoon
* Triggered by path: callafternoon->callchinamiafternoon->chinamidate5

## Official wiki page

[Chinami-Corp](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chinamidate5&go=Go) for more details.

## Event code

File: (install folder)\game\ChinamiEvents.rpy

Code:
```python
...
label chinamidate5:
    play sound "phonebeep.wav"

    "I tap on Chinami’s name in my phone and wait for her to answer."
    "Chika should probably be at work already, so if I want to spend time with the mini-version of her, now would probably be best."

    if bonus == True:
        "To be fair, Chika probably wouldn’t mind either way, but the idea of asking a [teenage]girl for her permission to do what I want to do just sounds annoying."

    "………"
    "……"

    play sound "phonebeep.wav"

    ch "Chinami hotline! This is the CEO, Chinami speaking!"
    ch "How many giraffes would you like to order?"
    s "The Chinami hotline sure sells some strange things."
    s "Do you have a permit to be selling giraffes, Chinami?"
    ch "Are you buying anything or are you just calling to take up my time?"
    ch "I have a very important business to run! These giraffes are not going to sell themselves!"

    "I can see that Chika’s customer service genes must have also been passed down to her sister."

    s "Are you doing anything today, Chinami?"
    ch "Chinami never does anything. She just sits in a room and cries."
    ch "Chinami thinks you should come over and play with her!"
    s "Sure thing...I’ll head over now."
    ch "Hooray! And I will put you down for three giraffes in the meantime."
    s "I don’t want any giraffes, though."
    ch "Sorry! No refunds!"
    ch "Bye-bye!"

    play sound "phonebeep.wav"

    "Chinami hangs up the phone and I find myself already on the way to her house."
    "Hopefully the cost of three giraffes is somewhere in the realm of one pizza so I can just order her dinner in order to settle my debt."
    "………"
    "……"
    "…"

    scene chinamistorytime1
    with dissolve
    play music "happyandplotting.mp3"

    if bonus == True:
        "I sit at the table alongside a girl significantly younger than me as she looks up in admiration or...naivety or...confusion."
    else:
        s "..."
        ch "..."

    "Chinami seems to only have two facial settings."
    "One that is entirely wholesome and-"

    scene chinamistorytime2
    with dissolve

    ch "Wanna watch Chinami slaughter pigs on her phone?"

    "And one that is pure evil."

    s "You’re still playing that game?"

    scene chinamistorytime1
    with dissolve

    ch "Chinami has all the time in the world to play games since she can’t go outside."
    ch "The pig game is also the only thing she’s better than her sister at, so Chinami needs to keep polishing her skills or she'll be left behind."
    s "That’s fair but Chika doesn’t seem like that big of a gamer to begin with."
    ch "All big sis does is watch cute girls dance on her phone. Chinami’s phone-time is much better and more fulfilling."
    ch "She has also mastered geometry. "
    s "I’m very proud of you, Chinami."
    ch "So, if you don’t want to play games with Chinami, what would you like to do?"
    ch "Dance? Sing?"
    s "I can’t say I’m much of a...well, either of those things."
    ch "Maybe you can teach Chinami things since you are a teacher?"
    ch "She wants to know what kinds of lessons the big girls learn so she can be prepared when she’s allowed to go to[school]."

    "{i}If{/i} she’s ever allowed to go to[school]."
    "I don’t know much about Chinami’s situation, but the way Chika put it mixed with the fact that she can’t even go out in public without gloves and a mask is...rather telling."
    "But who knows? Maybe she’ll be able to do things the rest of us can do someday?"
    "One can only wait and see."

    s "Today is my day off. And you can’t afford to buy lessons from me either way."
    ch "What if Chinami gives you a discount on your four giraffes?"
    s "Wasn’t it only three?"
    s "Wait, I didn’t even want any in the first place."
    ch "I added another one as a penalty for you being late. "
    ch "That’s what the adults call “interest.”"
    s "That is a very strange take on the concept of interest but you’re not entirely wrong."
    ch "Can you at least read Chinami a story?"
    ch "Big sis Yumi keeps a stack of manga in her side of the closet and Chinami likes to read them when no one else is home."

    scene chinamistorytime2
    with dissolve

    ch "She likes the ones with lots of blood the most."
    s "Of course she does. "
    s "Fine. Go get something out of the closet, Chinami."

    scene chinamistorytime3
    with dissolve

    ch "Yay! Friendship!"
    ch "Chinami will be right back!"

    scene chinamistorytime4
    with dissolve

    s "…"

    "Chinami scurries over to the other side of the room and quickly opens the closet door, stopping it with her foot just before it bumps against the wall."
    "I imagine it’s something she’s been scolded about in the past judging by the chipped paint and dents near where the door handle would typically land."
    "Also, is now a good time to say that I think Chinami and Kaori would get along strangely well?"
    "The two of them seem to only want companionship and...I don’t know if Kaori even has the mental capacity to comprehend any strangeness regarding hanging out with a girl Chinami’s age."
    "But, then again, it might be difficult convincing Chika to let someone who looks like Kaori inside in the first place."

    scene chinamistorytime5
    with dissolve

    ch "Chinami has returned with a book that has no blood in it. She doesn’t want you to get scared and run away."
    s "I’m a mature adult and would not run away from something as trivial as that."
    ch "Chinami doesn’t know what {i}trivial{/i} means but she believes you."
    ch "She also has a rule when it comes to story time."
    s "A rule? What kind of rule?"
    ch "Since Chinami has read this manga so many times already, she knows the story by heart."
    ch "So she wants you to make up your own story and tell it to her."
    s "Why do I suddenly need to be creative? All I was planning on doing was reading."
    ch "Because if you don’t, Chinami will tell her big sis that you did all kinds of mean stuff to her while she was at work."
    s "…"
    ch "…"
    s "Are you...blackmailing me?"
    ch "Chinami is Chinami-mailing you."
    ch "She just wants to have fun with her friend."

    scene chinamistorytime6
    with dissolve

    ch "And will eliminate you if you don’t listen to her."
    s "…"
    ch "…"
    s "…"
    ch "Take Chinami’s book."

    "I’m starting to think that “Game of Thrones” thing might have been a bad influence on this adorable little flower."
    "She’s gone from being a daisy to some sort of...venus fly trap or something."

    scene chinamistorytime7
    with dissolve

    "I take the book out of Chinami’s hands and open up to a random page since it doesn’t really matter what I read in the first place."
    "She moves closer to the table and slides her legs underneath it, bumping into one of my knees as she does so."
    "It’s a small table, so it’s not exactly an easy fit for both of our limbs, but we make do with the space we have and I..."
    "Well, I guess I allow myself to be blackmailed?"
    "Or, excuse me, Chinami-mailed."

    scene chinamistorytime8
    with dissolve

    s "So...uhh..."
    s "A long, long time ago in a galaxy far, far away."
    ch "Chinami has seen that movie before. Try something else."
    s "…"
    s "How about you just tell me what kind of story you want to hear."
    ch "Hmm..."
    ch "Chinami wants to hear a story about a little girl who grows up to be the CEO of Chinami-corp! The biggest Japanese dealer of cute animals!"
    ch "It doesn’t have to be a story about Chinami as long as the company is named Chinami-corp."
    s "But why would-"
    s "Actually, nevermind. Fine."
    s "A decently long time ago in a land pretty close to here-"
    s "There was a little girl named...Chiaki."
    ch "Chiaki was Chinami’s mom’s name!"

    scene chinamistorytime9
    with dissolve

    s "Oh. Uhh...Should I change it?"
    ch "No. Chinami thinks it’s a good name. Other girls are allowed to have it."
    ch "Please continue!"

    scene chinamistorytime8
    with dissolve

    s "Okay, so...Chiaki was a pretty normal girl for most of her life."
    s "In her free time she did things like...painting or...jump-rope...or ski-ball."
    ch "What’s ski-ball?"
    s "A game that no one plays anymore."
    ch "It sounds fun. "
    s "I haven’t even told you what it is."
    ch "Chinami guesses you wear skis and kick a ball around."
    s "Wrong. This is exactly why you need to listen instead of speaking out."
    ch "Chinami is sorry. She will behave."
    s "Good. So, anyway..."
    s "One day, Chiaki was on a field trip to a museum or something and she was suddenly bit by a radioactive spider."

    scene chinamistorytime10
    with dissolve

    ch "Wow! A plot twist this early!"
    ch "Chinami is shocked!"
    ch "What color was the spider?"
    s "…"
    s "Brown."

    scene chinamistorytime11
    with dissolve

    ch "That just sounds like a normal spider. "
    s "It was only slightly radioactive."

    scene chinamistorytime8
    with dissolve

    s "Anyway, Chiaki went home and continued to live her normal life for the next three weeks."
    s "She was almost positive the radioactive spider was going to have some sort of life-changing effect on her, but sooner or later she realized that all she gained was...extreme customer service skills."

    scene chinamistorytime11
    with dissolve

    ch "Chinami found a plothole."
    ch "How did Chiaki know the spider was radioactive if it just looked like a normal spider and didn’t give her powers?"
    s "Be quiet. This is my story."

    "I feel strangely irritated by my story being interrupted all of a sudden despite not caring at all just a few minutes prior."
    "How dare this tiny human find plot-holes in my work."

    ch "Chinami is sorry. Please don’t kidnap her."
    s "Please don’t insinuate that that’s a thing I would do if I were angry."
    ch "Big sis Yumi has warned Chinami that you’ve kidnapped girls in the past."
    s "…"
    s "I don’t think you should listen to Yumi anymore. I’ve never kidnapped anyone."
    s "But, back to the story..."

    scene chinamistorytime8
    with dissolve

    s "After Chiaki gained her radioactive customer service powers, the only thing she wanted to do with her life was sell things to people."
    s "The problem was that Chiaki also lived on a farm, so all she could sell were animals."
    ch "What about vegetables? They have vegetables on farms."
    s "The other problem was that this farm only had animals."
    ch "Chinami thinks a farm with only animals just sounds like a lonely zoo."
    s "Chinami should shut up and listen to the end of the story."
    ch "Chinami thinks you’re just jealous because she’s a better story-teller than you."
    s "…"
    ch "…"

    scene chinamistorytime12
    with dissolve

    s "…"
    ch "Chinami loves your story. Please continue."
    s "It doesn’t sound like it."
    ch "She’s just excited to be spending time with her future dad. That’s all."
    s "…"

    scene chinamistorytime13
    with dissolve

    s "Hah..."

    "How in the world am I supposed to stay mad when she goes and says things like that?"
    "Is this what having a kid is like?"
    "I thought I had a grip on that with Ami, but she jumped straight into her[teen]years rather than whatever’s going on here."
    "Granted, Ami didn’t really {i}jump{/i} into her[teen]years. She’s been there since I met her."
    "But still."
    "I should just try and wrap this story up so the two of us can move onto something more-"

    play sound "dooropen.mp3"
    scene chinamistorytime14
    with dissolve

    y "Chinami! I’m back! "
    s "Uh-oh."
    ch "Big sis Yumi is home!"
    ch "Story time will have to wait!"
    y "Heh? Story time? You never have story time by yourself. Is Chika back from work al-"

    scene chinamistorytime15
    with fade
    stop music

    y "…"
    s "…"
    ch "Welcome home!"
    y "…"
    s "...Welcome home!"

    play music "yumiska.mp3"
    scene chinamistorytime16
    with hpunch

    y "D-DON’T GIVE ME THAT {i}WELCOME HOME{/i} BULLSHIT!"
    y "WHAT THE FUCK DO YOU THINK YOU’RE DOING IN HERE?!"
    y "I SWEAR TO GOD IF YOU SO MUCH AS LAY A FINGER ON HER I WILL MURDER YOU!"
    ch "Uh-oh! Big sis Yumi only uses bad words when she’s {i}really{/i} angry."
    ch "Don’t worry, big sis Yumi! Sensei said he won’t kidnap me!"

    scene chinamistorytime17
    with dissolve

    y "HOW DID THAT EVEN COME UP IN CONVERSATION?!"
    s "A better question is why you told her I’d kidnap her in the first-"

    scene chinamistorytime16
    with dissolve

    y "NO ONE ASKED YOU! GET THE FUCK OUT OF HERE!"
    y "DOES...DOES CHIKA EVEN KNOW YOU’RE HERE?!"
    s "Well...not exact-"
    ch "Yup! Chinami told her!"
    s "…"

    "Well."
    "That’s...awkward."

    scene chinamistorytime18
    with dissolve

    y "And she was okay with it?..."
    y "Ew..."
    y "Ew ew ew ew ew ew ew ew ew..."

    scene chinamistorytime16
    with dissolve

    y "AHHH THAT’S SO FUCKING GROSS!"

    scene chinamistorytime19
    with dissolve

    y "And wait a fucking minute! What are you holding?! What are you reading to her?!"
    s "Oh, Chinami told me about your manga collection so-"

    scene chinamistorytime20
    with dissolve

    y "GET! THE FUCK! OUT OF HERE!"
    y "AND NEVER COME BACK!"
    s "And that’s my cue to leave."

    scene black
    with dissolve

    ch "But we didn’t finish story time yet!"
    ch "Chinami needs to know what happens to Chinami-corp!"
    s "I’ll tell you some other-"
    y "YOU ABSOLUTELY WILL NOT!"
    y "OUT! NOW!"
    s "Or not."
    s "Later, Chinami. Later, Yumi."
    y "DIE IN A FIRE!"

    play sound "dooropen.mp3"

    "…"
    "Well, that could have gone better."
    "I wish Chinami would have said something about Yumi being able to show up at any minute, but-"
    "To be fair, I probably should have expected something like that sooner or later."
    "That’s Yumi’s home, too, after all."
    "I guess I’ll just...need to be more careful in the future."
    "Or at least find a good hiding place."

    $ renpy.end_replay()
    $ chinamidate5 = True
    $ chinami_love += 1
    stop music fadeout 5.0

    "{i}Chinami’s affection has increased to [chinami_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label chinamidate10:
...
```

## Code that triggers this event

File: (install folder)\game\ChinamiEvents.rpy

Code:
```python
...
label callchinamiafternoon:
    if chinami_love >= 5 and chinamidate1 == True and day128 == True and chinamidate5 == False:
        jump chinamidate5
...
```