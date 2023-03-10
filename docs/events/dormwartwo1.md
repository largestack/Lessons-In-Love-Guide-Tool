# A Walk Through Hell (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 558

* Event [Chiburi](./ayanespecial50.md) (Ayane) is completed)

* Event [Grief Seed](./day543.md) (Main) is completed)

* Day of week is Friday

* Event [Too Blind To See](./futabainvite3.md) (Futaba) is completed)



## Next events

None

## Event properties

* Id: dormwartwo1
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->dormwartwo1

## Official wiki page

[A Walk Through Hell](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo1&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label dormwartwo1:
    scene anewwar1
    with fade
    play music "10c.mp3"

    u "Ladies and...the one gentleman we have! And also Molly!"
    mo "Are you going to do this every year?!"
    u "The time has come for us to once again link our fates! Binding ourselves together in a way that will bring a good half of us closer to the person who is {i}once again{i} this year’s prize..."

    scene anewwar2
    with dissolve

    u "Sensei! Woooooo!"
    s "As excited as I am to once again have my life put on the line for the sake of your enjoyment, I would like to remind everyone to please not attack me if your floor loses. Thank you."
    ima "Don’t worry, Senpai. I’ll be here to clean up the blood so nobody gets in trouble when something like that {i}does{/i} happen."
    s "Thanks, Imani. I feel so much better and safer now."

    "As you may have figured out by now, today marks the beginning of the second annual Super Mega Whatever-Other-Adjectives Dorm Wars."
    "Also, it’s Halloween. Which I guess means it’s okay for all of my students to show up in their costumes despite it still being school hours and...some of them barely wearing anything at all."
    "And yes, I am complaining about this- but not because I am worried that it may get all of us into some sort of trouble. But because I have never wanted to have sex with this many people at the same time before."
    "The next 48 hours will likely be Hell- but it will be a Hell we can walk through together...on the way to countless erections and brighter days."

    scene anewwar3
    with dissolve2
    $ renpy.pause(3, hard=True)

    ima "Uhh...Senpai? You alive?"

    scene anewwar4
    with dissolve

    s "I’m fine. Just reflecting on what could very well be my final moments."
    u "Reflect on your own time, Mas- uhh...Sensei. We’ve got some contests to assign and we were kind enough to let you stay in the room to listen to them this time around."
    s "I still don’t understand why I wasn’t allowed to do that the first time."
    ay "And I still don’t understand why no one’s brought up the fact that this is the second time we’ve done this in just {i}one school year.{/i}"

    scene anewwar5
    with dissolve

    s "Don’t worry, Ayane. One day, we’ll stand on that rooftop together. You, me, and my twenty unborn children."
    m "{i}Hah...{/i}"
    u "Weird inside jokes aside, who’s ready to kick this off with our first contest announcement?!"
    a "Woo! Dorm Wa- wait, why am I the only one clapping?"

    scene anewwar6
    with dissolve

    u "Contest numero uno! A fierce battle between two of the tiniest girls in class! And one that would send the dudes into a hormonal frenzy if they weren’t all up in space doing space stuff!"
    u "From the first floor- we have Sana Sakakibara...facing up against second floor denizen...Molly MacCormack! In a contest to determine which one of them is the {i}true{/i} gamer girl!"

    scene anewwar7
    with fade

    mo "Heh...heh...heh...as if there needs to be a contest at all..."
    mo "For eternity, I have sat idly by...evading the sharp edges of my father’s words as he says, “Molly...maybe it’s time to go outside?”"
    mo "If only ‘ye could see me now...one long rest from proving to the world that those hours {i}wasted{/i} were no waste at all...but-"
    ay "Yeah, yeah. We get it. You’re sedentary."

    scene anewwar8
    with dissolve

    mo "I prefer the term “extrovertedly challenged,” thank you very much. But yes, I suppose I shall let my skills do the talking rather than my mouth. "
    mo "I do have a question for my opponent, though. Is such a thing permitted?"
    u "Does it relate to the contest?"
    mo "Only in the fact that it relates to her and she is going to be {i}in{/i} the contest."
    sa "You can...ask...it’s okay..."

    scene anewwar9
    with dissolve

    mo "Then, and please don’t take this the wrong way- but what in Scáthach’s cervix are you supposed to be this year?"
    sa "That..."
    sa "That is a good question..."
    t "Is this how you envision Zagull Throat Spear? The head is larger and greener than I pictured. But I will admit that I am no expert when it comes to the orc race."
    sa "This is just a...mask I found at a Halloween store, but...I...think that...Zagull might look...a little-"
    mo "As your DM, I want it to be known that I will never come between you and the way you want to play your character. "
    mo "But I swear on the Cliffs of Moher that if you say Zagull looks even remotely similar to this sinful costume, that you will have disadvantage on everything for the rest of forever."
    sa "..."
    mo "..."
    sa "It’s just..."
    sa "It’s just an...orc mask..."

    scene anewwar10
    with fade

    u "With the first contest decided, it’s time to move on to one of only {i}two{/i} contests that will be returning for a second run this year! "
    ay "And considering that the vast majority of the class wanted to participate in this one, I’d like to remind you all that selections were completely random and that {i}I{/i} would be competing if I had any say in this!"
    u "To prevent any casualties, the participants for this contest have already been revealed at an earlier date. But, for the sake of clarity and to get the formal contest introduction out of the way..."
    u "The second ever date war will be between Futaba {i}Fuku{/i}yama and Noriko {i}Naka{/i}yama!"

    scene anewwar11
    with dissolve

    n "Nakayara{i}kawa{/i}yama, please. I changed my last name to become closer to the man I will be {i}dating{/i} in this contest."
    n "So unless Futaba plans on changing her name to Fuku...arak- see, no. It just doesn’t have the same ring to it."
    f "I...I don’t think I’m quite ready to change my last name yet anyway..."

    scene anewwar12
    with dissolve

    n "I’m just messing around! Best of luck, Futaba! I’m sure you’ll do-"
    c "What are those weapons called?"

    scene anewwar13
    with dissolve

    n "Hm? What?"
    c "Your weapons. What are they called?"
    n "I think they’re, like...dagger things? Why?"
    c "Because if you lay so much as a finger on Sensei, I am going to take those {i}dagger things{/i} and rearrange your face."
    n "Jeez, Chika. I feel like there’s a little more to that vitriol than just the reigning champion trying to prevent someone else from taking her crown."
    ki "Why does it even matter if she touches him or not? It’s not like you own him. "
    c "Button up your pants. You look like a whore."

    scene anewwar14
    with dissolve

    ki "You’re literally in bondage gear!"

    scene anewwar15
    with fade

    s "Yeah, I have no idea how Chika was even allowed into school dressed like that."
    ima "Forget about Chika, have you {i}seen{/i} Tsuneyo? Girl’s such a queen she’s got me questioning my morals before lunch time. "
    s "I feel like lunch is the only time I spend in this building {i}not{/i} questioning my morals."
    ima "I feel like I need a cold shower. Hot damn."
    s "You know, maybe you’ll be a good judge for this contest after all. "
    ima "Game’s over. They all win. Enjoy your harem."
    no "Excuse me, madam speaker? I have a question about the contest. "

    scene anewwar16
    with fade

    u "Which one of us is “madam speaker?”"
    ay "I’ll handle this. What’s up, Nodoka? What’s your question?"
    no "I was just wondering whether or not Yumi would be participating in this year’s Dorm Wars."
    o "Hey, yeah. What is the first floor going to do when they’re down a player? If somebody on the second floor needs to sit out as well, I-"
    i "Me. Pick me. I’ll sit out. "
    o "Oh. Okay, yeah. That makes more sense."
    u "That’s...actually a good question. I didn’t really know what to do for Yumi, so I just wrote down “karaage” as the tenth girl on the first floor."
    ay "I don’t remember any chickens moving in. In fact, come to think of it, Todd hasn’t even come back yet."
    s "Tsuneyo probably killed them all as soon as they showed up."
    t "I do have a history of doing that."
    no "If I may make a suggestion, I’d be open to competing against Yumi should she return to the class."

    scene anewwar17
    with dissolve

    f "I don’t think she’s {i}allowed{/i} to return to the class after what she did to you. She’s suspended, remember?"
    no "Would it be an issue if our contest were to take place {i}outside{/i} of class?"
    no "If it’s not on school grounds, she should be allowed to do anything, right?"
    ima "You looking for revenge or something, Nodoka? Not sure why you’d want to compete against somebody who nearly killed you."
    u "Oh! Revenge sounds fun! I like this idea! How do you feel about it, Ayane?"
    ay "I mean...I think it’s fine...but I doubt Yumi would even want to-"
    c "Let me handle Yumi."

    scene anewwar18
    with fade

    c "She’s actually coming over to my place later today and I can just ask her about it then. "
    c "No idea if she’ll actually agree or not. But if Nodoka is cool with going up against her, I might be able to convince her. "
    c "Worse comes to worst, I’ll just take her place and compete on her behalf. "
    ki "You’re still hanging out with her? Aren’t you afraid she’ll go postal on you next?"

    scene anewwar19
    with dissolve

    c "Aren’t you afraid that keeping your pants unbuttoned might make the room smell kinda fishy?"
    n "Aww, I love it when you two whisper sweet nothings to one another! It’s so cute!"

    scene anewwar20
    with fade

    u "If nobody has any objections, I guess there’s no harm in seeing if she wants to join or not. We’ll just keep Tsuneyo on guard this year since her costume has a gun."
    ay "She’s not the only one with a gun, you know."
    c "Can you at least tell me what I’m doing before I head out? "
    n "Wait, you’re leaving {i}now?{/i}"
    c "Yeah. The principal stopped me in the hall and said I wasn’t allowed to be in school dressed like this, so I’m not even supposed to be here right now."
    ima "Tsuneyo, hide. "

    scene anewwar21
    with dissolve

    u "Then, uhh..."
    u "You and Otoha are competing against one another in a popularity poll that we’ll be tallying the results for sometime near the end of the competition."

    scene anewwar22
    with fade
    play sound "slidedoor.mp3"

    c "Easy! Thanks, Uta! See y’all later!"
    r "Wait a second! Won’t both floors just vote for the girl that will help their team win? No one’s going to vote against their own floor."
    o "You will, right? "

    scene anewwar23
    with dissolve

    r "Huh? What?"
    o "You wouldn’t vote against your own {i}girlfriend,{/i} would you? "
    r "Uhhhhhh...{i}no. Of course not.{/i}"
    o "Good. But, just in case you don’t remember, I was weirdly popular at my last school for no reason whatsoever. I’ve got this in the bag."
    r "But...Chika’s popular too. And you’re still new-ish here, so barely anybody even knows you yet and...and that’s kind of a disadvantage, isn’t it?"
    o "Ehh. If I lose, I lose. Not like it’s the end of the world if I don’t get to spend a little extra time with our weirdo teacher."

    scene anewwar24
    with dissolve

    r "Can you stop calling him that, please?"
    o "Why? You call him that all the time."
    r "Yeah, but it’s a joke when I do it. The way you say it makes it sound like an insult."

    scene anewwar25
    with fade

    ay "Sorry to interrupt but, to answer your question, it’s not just {i}our{/i} floors who are voting on the poll. It’s the other classes too. So if you want to get campaigning, you better do it now."
    o "Wait, seriously? The contests start in the morning and there are only a few hours left of school."
    ay "Yup! Which is why I said you better get started now!"
    ay "Honestly, I’m surprised Uta even okayed this challenge given how much of a handicap there is."
    u "Never doubt the amount of girls who want to be dommed by the prince of Kumon-mi Academy."

    scene anewwar26
    with dissolve

    ay "You were one of them weren’t you?"
    u "The...the next contest we’ll announce is Ayane’s! Which is a stand-up comedy showdown between her and floor two’s very own Tsuneyo Tojo- who has been dreaming of this moment her entire life!"

    scene anewwar27
    with fade

    t "Like a light bulb, I will shine. "
    sa "Tsuneyo...you know there...are much brighter things...to compare yourself to...right?"
    t "Doing that would be wrong when I expect to give a performance so average that you’ll all remember it for the rest of your lives."
    sa "Oh...uhh...okay..."

    scene anewwar28
    with dissolve

    t "As someone who is also extremely average, you should help me write material, Zagull Throat-Sana. "
    sa "I’m not...very funny and...and Ayane is also my...best friend, so..."
    sa "So I would like her to win..."
    t "I see. "
    t "I will remember this when you come to {i}me{/i} for help with your stand-up routine. "
    sa "I..."
    sa "I think I’d need a little more help than...just you anyway..."

    scene anewwar27
    with dissolve

    u "Anything to say before moving on, Ay-"
    ay "Nope! Keep ‘em coming, Uta!"
    u "R-Right! Then...the next contest we’ve got will be mixing things up a little and sucking even {i}more{/i} people into the contest for the first time ever!"

    scene anewwar29
    with fade

    u "The Midnight Mom Mosh will take place immediately after the stand-up contest and pit Touka’s mom up against Makoto’s in a battle to determine which one is...more motherly!"
    mak "Can I concede now or is this a thing I actually must attend?"
    to "I’m sure your mother will do just fine, Makoto. While mine may be extremely talented and well-versed in a plethora of different skills and activities, I’m sure your mother is exceptional in her own ways as well!"
    mak "Yeah, about that."
    ya "Touka..."

    scene anewwar30
    with dissolve

    to "Yes, Yasu? What can I do for you?"
    ya "What’s it like to have a mom?"
    to "Yasu, please do not make me cry today of all days. Do you have any idea how long it took to apply all of this fake blood and makeup? "
    ya "I’m sorry, Touka. I didn’t mean to speak out of turn again. I’ll crawl back into my hole and await further instructions. "
    to "You may speak whenever you want, my dear. But it would be lovely if you’d remain as positive as possible on holidays like this one as you and I are the glue that holds this class together!"

    scene anewwar31
    with dissolve

    ya "Glue is sticky and makes other things sticky as well."
    to "It certainly does."
    ya "Are you saying we are sticky?"
    to "I’ve changed my mind. Please remain quiet until the delegation of contests is complete. Your talk of stickiness is both distracting me and making me feel quite uncomfortable."
    ya "Thank you for once again trying to include me. If only I were not so pathetic. Then, maybe we would be able to get everyone sticky without you coming to despise my existence. "

    scene anewwar32
    with fade

    mi "Ready to redeem yourself after last year’s defeat, Makoto?! "
    mak "Absolutely not. It’s one thing for {i}me{/i} to win a contest, but for my {i}mother{/i} to win one? Against one of the most influential women in Kumon-mi? There’s not a chance."
    mi "But Maki knows all sorts of stuff about-"
    mak "Rubber penises and sex positions? Yes. Yes, she does. But neither of those things make her “motherly,” which is precisely what this contest entails. "
    mak "So unless Touka’s mother is completely helpless when it comes to performing the tasks a {i}standard{/i} mother performs, I have no hope whatsoever."

    scene anewwar33
    with dissolve

    mi "It doesn’t matter if ya win or lose so long as ya have fun and enjoy your time together."
    mak "I..."
    mak "You’re right. And I’m sorry. I didn’t-"
    mi "I think this sorta thing might be good for you and Maki. And if this thing weren’t happenin’ so late at night, I’d probably come along with ya."

    scene anewwar34
    with dissolve

    mak "I wouldn’t worry about that. Besides, it won’t be {i}you{/i} as soon as today’s bell rings anyway. So just focus on winning {i}your{/i} competition and I’ll..."
    mak "I’ll try to do the best with mine."

    scene anewwar10
    with fade

    u "Okay, okay, okay! We’re startin’ to wind down, so let’s get these last few outta the way before we start worryin’ about the pre-game interviews later!"
    ay "Our next contest is a battle that will put your most essential knowledge to the test! "
    u "That’s right, folks! It’s a contest to see how much the competitors know about the reward they’re competing {i}for!{/i}"
    ay "It’s a battle between supernatural and super-awkward as Yasu Yasui faces off against Rin Rokuhara, self-proclaimed queen of the friend zone! "

    scene anewwar35
    with fade

    r "Hey! That isn’t a {i}self-{/i}proclaimed title at all! I’ve never once called myself that!"
    o "It’s kinda true, though. "
    r "It’s {i}because{/i} of my friendship with Sensei that I know so much about him! That’s not a negative thing! And there’s no way Yasu can even come close to that!"
    ya "Come close to what? What are we doing?"
    to "I said “shush.” "
    ya "Sorry, Touka. I thought I heard someone say my name, but I forgot that no one would ever taint their lips that willingly."
    o "Just don’t get beaten out by the ESP or whatever it is she’s got going on, Rin. I’ll be rooting for you just as much as you’ll be rooting for me."

    scene anewwar36
    with dissolve

    r "Hah...yeah."
    r "Yeah, I’m sure everything will be fine in the end."
    ay "Coming up sometime either before or after the last contest-"
    u "We’re still working out the schedule for day two-"
    ay "Comes what is sure to be one of the most divisively adorable competitions we’ve had thus far!"
    u "You know, Ayane- I’ve always said, “Nothing ventured, nothing gained!”"
    ay "I’ve never heard you say that once! But please, proceed!"
    u "And it is that exact quote that I may or may not have said that made me realize that, sometimes, I have to make my best friend really, really uncomfortable!"
    i "I’m sorry, what?"
    ay "That’s right, everyone! The next contest we’ve got on the docket is titled “Misfit Maid Madness” and is a battle to see who the best maid is between Io Ichimonji and Maya Makinami. "
    m "You’ve gotta be fucking kidding me."

    scene anewwar37
    with dissolve

    i "I have a question."
    u "Yes, Io?"
    i "No. "
    ay "That wasn’t a question. "
    i "Can’t I just do the participation thing again? That’s the only reason I put on a costume in the first place. Nobody told me we were changing jobs."
    u "I was going to, but then you got all dressed up and it made me feel all warm and mushy inside, so I kept it a secret. Please don’t hate me."

    scene anewwar38
    with fade

    m "Yeah, I’m not doing this."
    i "Cool. Let’s just call it a tie then."
    m "Fine by me."
    a "What’s wrong with being a maid, Maya? I think you’d be good at it."

    scene anewwar39
    with dissolve

    m "Of course I’d be good at it. Have you seen me? I’m adorable. But that doesn’t mean I have any desire to actually {i}be{/i} one. I don’t have the energy for that sort of job."
    a "It’s just for a little while, though. And you can go right back to being all cold and aloof right after."
    m "Sure. But you’re not taking into account the fact that I would be a maid waiting on {i}Sensei,{/i} which is a thing he would never allow me to live down."
    s "It’s true. I really wouldn’t."
    m "See?"

    scene anewwar40
    with dissolve

    i "Wait, can we do this maid thing in private? Because if it’s {i}just{/i} Sensei, I’d probably be fine with it."
    u "Sure! That works for-"
    ima "No way! Vetoed! I wanna see the maids too! Plus, I’m a real, certified judge this year and I deserve the right to weigh in on which one of you I’d rather have drawing ketchup hearts on my food!"
    ay "I also don’t like the idea of private maid showings since I understand exactly how much Sensei likes maids and that sounds dangerous for everyone involved!"
    a "That is a risk I am willing to take."
    ay "Ami, you’re not even competing in this contest."
    a "If Sensei’s heart is involved, I am always competing. "
    u "Come to think of it, what {i}is{/i} Ami competing in? Because I didn’t write anything for her and Kirin."
    ay "Uta, this was literally your only job."

    scene anewwar41
    with fade

    u "Yeah! But between this and the harem ranking, I’ve got barely any “me” time left! And any time I {i}did{/i} have went toward making this costume!"
    ay "Then...I guess it’s good that {i}you’re{/i} going to be the one representing your floor in the costume contest this year."

    scene anewwar42
    with dissolve

    ay "But what {i}isn’t{/i} good for you is the fact that you’ll be facing off against our secret weapon in Miku Maruyama fulfilling the role of a gyaru while Chika is out being a...provocative dog?"
    n "I think she’s a wolf girl. "
    ki "Whatever it is, she’s hot."
    n "Wasn’t she talking shit on your vagina like ten minutes ago? Are you already over that?"
    ki "Yeah, now I kinda just wanna hate fuck her."
    ima "Kirin, you’ve got a problem. And while I’d normally say this is something you should talk to a counselor about, I just remembered who your counselor is. So...never mind."
    mi "Uhh...good luck, Uta. We’re both undefeated so far, so I..."
    mi "I ain’t plannin’ on...takin’ it easy on you..."

    scene anewwar43
    with dissolve

    u "Good luck to you too, Miku! Here’s hoping neither one of us cracks before the time comes to be judged!"
    s "Cracks? What is that supposed to mean?"
    ay "What that means, Sensei...is that we’ve added an extra layer to the costume contest this year!"
    ay "You see, a good costume will always be impressive. But what’s even {i}more{/i} impressive is when the person {i}wearing{/i} that costume is able to perfectly embody their character!"
    mo "Amen!"
    u "Which is why, starting with the final bell, Miku and I will take on the roles of our characters and attempt to remain in them until two nights from now, when we once again conclude at Sakaki-bar-a!"
    f "Is that...really the name of Sana’s family’s bar?"
    r "I love it. Twenty can’t come soon enough."
    ay "Any last questions before we put an end to this ceremony-ish thing?"
    a "Yeah, I still have no idea what my contest is."
    ki "Let’s see which one of us can please Imani the most."
    ima "Let’s not!"
    u "We’ll figure something out for you guys tomorrow and apologize for any inconvenience this may have caused you."

    scene anewwar44
    with dissolve

    ay "It is at this time that we’d like to thank all of you for attending the Second Annual Super Mega Ultimate Halloween Dorm Wars introduction ceremony."
    u "We’d also like to thank the Tsukioka Foundation and the Produce Delivery Administration for sponsoring this year’s event!"
    t "Those bastards."

    scene black
    with dissolve2

    u "This concludes our presentation!"

    play sound "bell.mp3"

    ay "And {i}that{/i} concludes our school day! "
    ay "Uta, you may now- wait. Where did Uta go?"
    ki "She threw a smoke bomb thing on the ground as soon as the bell rang, but nothing happened so she kind of just ran away."
    ay "Oh. Well, Molly, if you’re going to do the interviews again this year, you can come with me to the broadcast club’s room for our microphones and stuff."
    ima "And for everybody else, get the Hell out of here and go have some sleep! We’ve got a big day ahead of us tomorrow!"

    "One by one, the girls filter out of the classroom until I’m the only one left. "
    "And while I don’t exactly understand if my role as the “prize” is going to be exactly the same as it was last year and just determine which ten I sleep with in an unexciting manner..."
    "I’m looking forward to it."
    "Even if it’s mildly threatening, being sought after is nice. "
    "And it’s times like this that remind me of that."

    s "..."

    stop music fadeout 15.0

    "But with all of them heading back to the dorms and me having been banned from attending the “pre-game” interviews to avoid hearing any particular strategies...I have nothing left to do with the rest of my day."
    "So, for what is probably the millionth time, I slide my hands into my pockets and begin to head home. "
    "Because even if the next 48 hours will be some of the most exhausting of my life, I’m sure it will all be worth it in the end."
    "And I’m sure that this installment of the legendary Dorm Wars will be just as good as the last."

    $ renpy.end_replay()
    $ dormwartwo1 = True

    "........."
    "......"
    "... "

    jump dormwartwo2

label dormwartwo2:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
if totaldays >= 217 and day216 == True and day == 4 and day217 == False:
        jump day217
    if totaldays >= 218 and day217 == True and day == 5 and day218 == False:
        jump day218
    if totaldays >= 230 and makoto_lust >= 10 and christmas7 == True and makotolust10 == False:
        jump makotolust10
    if totaldays >= 237 and day == 1 and christmas7 == True and day237 == False:
        jump day237
    if totaldays >= 239 and day == 3 and day237 == True and day239 == False:
        jump day239
    if totaldays >= 240 and day == 4 and day239 == True and day240 == False:
        jump day240
    if totaldays >= 244 and day == 1 and day240 == True and day244 == False:
        jump day244
    if totaldays >= 246 and day == 3 and day244 == True and day246 == False:
        jump day246
    if totaldays >= 247 and day == 4 and day246 == True and day247 == False:
        jump day247
    if totaldays >= 261 and day == 3 and day247 == True and kirininvite2 == True and bar35 == True and day261 == False:
        jump day261
    if totaldays >= 263 and day == 5 and day261 == True and day263 == False:
        jump day263
    if totaldays >= 264 and day == 1 and day263 == True and day264 == False:
        jump day264
    if totaldays >= 269 and day == 3 and day264 == True and day269 == False:
        jump day269
    if totaldays >= 270 and day == 4 and day269 == True and day270 == False:
        jump day270
    if totaldays >= 271 and day == 5 and day270 == True and day271 == False:
        jump day271
    if totaldays >= 272 and day271 == True and onseninvite == False:
        jump day272
    if totaldays >= 280 and day == 1 and day271 == True and rindorm45 == True and iodorm10 == True and nikidate5 == True and chikaonsen4 == True and yumidorm30 == True and norikofirsthall == True and convenience5 == True and day280 == False:
        jump day280
    if totaldays >= 281 and day == 2 and day280 == True and day281 == False:
        jump day281
    if totaldays >= 282 and day == 3 and day281 == True and day282 == False:
        jump day282
    if totaldays >= 283 and day == 4 and day282 == True and day283 == False:
        jump day283
    if totaldays >= 287 and day == 1 and day283 == True and day287 == False:
        jump day287
    if totaldays >= 288 and day == 2 and day287 == True and day288 == False:
        jump day288
    if totaldays >= 295 and day == 3 and day288 == True and chikaonsen4 == True and amidate35 == True and makotowinterbeach4 == True and day295 == False:
        jump day295
    if totaldays >= 297 and day == 5 and day295parttwo == True and day297 == False:
        jump day297
    if totaldays >= 302 and day == 3 and day297 == True and day302 == False:
        jump day302
    if totaldays >= 303 and day == 4 and day302 == True and day303 == False:
        jump day303
    if totaldays >= 304 and day == 5 and day303 == True and day304 == False:
        jump day304
    if totaldays >= 318 and day == 5 and toukadorm5 == True and utadorm10 == True and mikudorm40 == True and mollydorm20 == True and otohadorm5 == True and kirindorm20 == True and iodorm10 == True and yukidate5 == True and sanadorm40 == True and yasudorm10 == True and day318 == False:
        jump day318
    if totaldays >= 333 and dormwar17 == True and day333 == False:
        jump day333
    if totaldays >= 340 and ayanedorm35 == True and day == 2 and day340 == False:
        jump day340
    if totaldays >= 351 and thirdreset3 == True and utadorm20 == True and day351 == False:
        jump day351
    if totaldays >= 355 and day351 == True and day355 == False:
        jump day355
    if totaldays >= 400 and secondbeach18 == True and (rindate50 == True or (rindorm50special == True and rinbetrayed == True)) and ramen30 == True and mollydorm30 == True and nikidate15 == True and day == 5 and halloweentwo1 == False:
        jump halloweentwo1
    if totaldays >= 400 and day == 1 and halloweentwo13 == True and norikospecial20 == False:
        jump norikospecial20
    if totaldays >= 410 and kirin_love >= 30 and kirinsoccer25 == True and ayanelust15 == True and kirinspecial30 == False:
        jump kirinspecial30
    if totaldays >= 417 and streets40 == True and day == 5 and yumispecial45 == False:
        jump yumispecial45
    if totaldays >= 424 and kirindorm25 == True and day == 1 and chikaspecial40 == False:
        jump chikaspecial40
    if totaldays >= 455 and chikadate45 == True and yumispecial45 == True and norikodorm25 == True and nikiinvite2 == True and sarabar25p2 == True and day == 4 and christmastwo1 == False:
        jump christmastwo1
    if totaldays >= 500 and chapthree8 == True and church15 == True and yasuspecial15 == False:
        jump yasuspecial15
    if totaldays >= 514 and yasudorm20 == True and nodokadorm15 == True and day == 4 and nodokaspecial15p1 == False:
        jump nodokaspecial15p1
    if totaldays >= 522 and sadgirls7 == True and day == 5 and sadgirls8 == False:
        jump sadgirls8
    if totaldays >= 530 and iospecial30 == True and karindate25 == True and day == 1 and tsukasaspecial1 == False:
        jump tsukasaspecial1
    if totaldays >= 535 and wakanadate15 == True and day == 5 and imanispecial1 == False:
        jump imanispecial1
    if totaldays >= 540 and imanispecial1 == True and day == 2 and ayanespecial40 == False:
        jump ayanespecial40
    if totaldays >= 541 and rindorm55p2 == True and bar55 == True and day == 3 and rikaspecial1 == False:
        jump rikaspecial1
    if totaldays >= 543 and rikaspecial1 == True and osakodate20 == True and day == 5 and day543 == False:
        jump day543
    if totaldays >= 547 and day543 == True and ayanesanabeach1 == True and day == 1 and ayanespecial50 == False:
        jump ayanespecial50
    if totaldays >= 550 and ayanelust15 == True and ayanespecial50 == True and day == 4 and ayanekirintalk == False:
        jump ayanekirintalk
    elif totaldays >= 550 and ayanelust15 == False and ayanespecial50 == True and day == 4 and ayanekirintalk == False and ayanekirintalkskip == False:
        $ ayanekirintalkskip = True
    if totaldays >= 558 and ayanespecial50 == True and day543 == True and day == 5 and futabainvite3 == True and dormwartwo1 == False:
        jump dormwartwo1
...
```