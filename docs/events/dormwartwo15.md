# The Cracking of the Egg (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Remove Curse](./dormwartwo14.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwartwo15
* Group: Main
* Triggered by label: dormwartwo14
* Chain sources: dormwartwo14
* Chain sources path: dormwartwo14

## Official wiki page

[The Cracking of the Egg](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo15&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label dormwartwo15:
    scene clearnightsky
    with dissolve2
    play music "newhope.mp3"

    "Only a handful of girls wind up coming to the next competition, but it’s not because none of them want to."
    "Yasu’s insistence that only a small group follow her to the church led to the sudden fragmentation of our class- like it’s no more than some undisclosed ingredient on an ethereal cutting board."
    "Each press of the knife slices away not only our bodies, but what those bodies lie on."
    "And before we know it, the fragments spread out, forever being stripped of the only opportunity they’ll ever have to be attached to anything."
    "I’m not saying that’s what will happen tonight. Doing so would be a bit overdramatic."
    "But that doesn’t stop me from thinking about what would happen if it did."
    "And which pieces I would reach for first if they all started falling away at once."

    play sound "static.mp3"
    scene specialsky with flash
    stop sound

    "Rin. Sana. Otoha. Touka. Imani."
    "At the behest of Yasu, this is all that remains of our once spectacular group as the rest is off celebrating and thinking about me. Celebrating while thinking about me. Thinking ABOUT ME while CELEBRATING."
    "I learned a long time ago that one of the most effective methods to make yourself feel more human is to always put yourself first."
    "If you can’t find yourself, just latch onto whatever is closest."
    "And in this case, the closest thing I can find to the way I feel is a handful of semi-intangible thoughts, slipping through my fingers like long, red hair with bits of scalp still attached."
    "If I squint my eyes, I can forget what they are."
    "I can make them look more like threads."

    play sound "static.mp3"
    scene theskythationcesaw with flash
    stop sound

    "{b}THIS IS THE WRONG SKY.{/b}"

    play sound "static.mp3"
    scene testofsenseiofsenseiof1 with flash
    stop sound

    ya "Stop. "
    o "What? Why? Is there, like...mass going on or something? "
    o "In fact, why are we even here in the first place? Couldn’t we have just done this trivia thing at Sana’s bar or whatever?"
    to "Yasu was adamant that the contest would have to be here for her to have any sort of chance against Rin. And Rin agreed to the terms as she already had a sizable handicap."
    r "Is that what happened? Because I’ve started just saying whatever it is that I think will make Yasu go away the fastest and I don’t even know what I’m agreeing to half the time."
    sa "I...should try that strategy sometime..."
    o "Just let us in and we can be quiet until mass is over or something. Being...wherever the Hell we are right now is giving me the creeps."
    ya "{i}Where you are{/i} is the front porch of salvation...a place that you would not be able to see at all if it were not for two and a half of us. "
    o "Uhh...what?"
    sa "If that’s...a short-joke...I’m going to be sad..."

    scene testofsenseiofsenseiof2
    with fade

    ima "You have any idea what’s going on right now, Senpai?"
    s "I never have any idea what’s going on when I come here."
    ima "You a regular? Didn’t take you as the religious type."
    s "I’m not. I probably just come here because I’m worried that Yasu’s going to hurt herself or something."
    ima "Probably?"
    s "It’s complicated."

    scene testofsenseiofsenseiof3
    with dissolve

    ima "Well, whatever it is, I can’t say I feel comfortable over here. In fact, if it was anybody other than Yasu leading all of us to this place, I’d probably be fearing for my life right about now."
    s "I have no idea how it being Yasu makes you {i}more{/i} comfortable about that, but you do you."
    ima "Yasu’s not out to hurt anybody, I don’t think. She clearly believes all of this crap, yeah- but false beliefs are totally common in people who aren’t exactly, uhh...the same as the rest of us."
    s "What if her god told her to kill us? Since she’s such a fanatic...she’d have to oblige, right?"

    scene testofsenseiofsenseiof4
    with dissolve

    ima "Oh, come on, man! You have any idea how long it’s been since I’ve practiced Krav Maga? I ain’t ready to fight for my life tonight! I just wanted to judge a contest!"
    ya "No one will be judging anything."

    scene testofsenseiofsenseiof5
    with dissolve

    ya "It is He and He alone who bestows judgement on all there is to be judged. And stepping into His sanctum just to tread all over His toes is not welcome."
    r "Wait...you’re not forfeiting, are you?"
    ya "All I am doing is protecting that which I have been ordained to protect. The contest will proceed as normal within the walls of the holy."
    ya "But only four of us will enter while the rest of you remain out here."
    o "But why-"
    ya "Because you are not ready."
    ya "His is a church that welcomes all, but only after certain conditions have been met. It is only then that one is chosen."
    s "I’m confused. I thought {i}I{/i} was the only one who was chosen. Now two more people have been chosen as well?"
    ya "You do not understand the choices being {i}made.{/i}"
    s "Well, you’ve certainly got that much right."
    to "Who are the four, Yasu? I assume that you, Sensei, and Rin are among the three....But which of us apart from that is the fourth?"
    ya "She with the silly, green helmet."

    scene testofsenseiofsenseiof6
    with fade

    sa "M...Me?!"
    o "Why Sana? What do the rest of us need to do to...fulfill your god’s conditions or whatever?"
    ya "All that you can do is unintentional. There is no single method that will allow you inside of the sanctuary."
    o "My feet will allow me inside of the sanctuary a lot better than weird religious riddles will, I’ll tell you that much."
    to "Yasu, please explain this in a more concrete way so that those of us remaining outside do not become disheartened. I’m sure you must understand this comes as a bit of a shock to us after the long ride here."
    sa "I...will swap with Otoha and...stay out here...if that’s okay..."

    scene testofsenseiofsenseiof7
    with dissolve

    ya "It is not. He wants you to observe...to peer into His splendor with your brand new eyes and throw yourself deeper into a life full of patience and understanding."
    ya "And unfortunately there is no “concrete way” of explaining this as the rumbling of the surface has already formed far too many cracks on these hallowed grounds."
    ya "Every crack you step on will be met with tragedy. And it is only I who can properly guide those who have been selected to-"
    o "Oh, fucking whatever. Just go in there and get this shit over with if you’re not going to let us in."
    r "Hey, I...know I may have {i}accidentally{/i} agreed to this to give you a fair shot, but...is there any way I can give you a fair shot {i}outside{/i} of a mega creepy church that I can't bring my girlfriend into?"

    scene testofsenseiofsenseiof8
    with dissolve

    ya "No..."
    ya "You waited too long to ask."
    ya "By now, His tendrils are already wrapped around your legs."
    ya "It is only a matter of time until you’re pulled in."
    ya "Alas...it is now {i}you{/i} who does not have a {i}fair shot...{/i}"
    ya "But..."
    ya "At least you will learn how misguided...how {i}small{/i} you truly are..."

    scene black
    with dissolve2

    "Reluctantly and hesitantly, those of us who have been chosen (Which apparently has multiple meanings now) follow Yasu through the church doors."

    play sound "static.mp3"
    scene testofsenseiofsenseiof9
    with flash
    stop sound

    "There are no tables or tea cups...bunnies or blindfolds...just the same sets of stone pews I have familiarized myself with in a place where nothing should ever be familiar at all."

    sa "Wow..."
    sa "It looks...a lot bigger on the inside..."
    r "Is it just me, or...is it kind of hard to breathe in here?"
    ya "Blessed be those who enter the church...Who walk through His heart...Partake in His search..."
    ya "Blessed be those who now have been found...Who don’t know they need saving...Who can’t hear the sounds..."
    ya "We are with you, My Lord. Peer into us so that we may peer into you and blind ourselves with the light of all that you have done."
    ya "I have brought these girls here today with the full intention of giving them wings...though, how long it will take, I am not sure."
    ya "The light of the one who has seen you will one day flow through them. And when that time comes, we will return here under a different pretense."
    ya "Under a different sky."
    ya "But today, all I wish is for them to see your glory. All I wish is for them to see how wonderful you are and how expansive the world is once you close your eyes."
    ya "I do not {i}ask{/i} this of you, God- for I know that it is not within my right nor my power to ask for anything."
    ya "But I trust that you will show them through me. And that they will understand they, too, are just vessels beneath the layers of flesh and muscle and bone."

    scene testofsenseiofsenseiof10
    with dissolve

    ya "I understand that everything hurts, God."
    ya "But I pray that the pain of this realization will not be too great for them to bear."
    r "I really don’t like this, Sensei. You know that feeling you get when you, like...sneak into school at night? Or go into some creepy basement? The one where your stomach is all like “GUHHHHH?”"
    s "Not really."
    r "Well, that’s how I feel right now. "
    s "Then forfeit before this contest thing kicks off and we can all go home. I don’t really like this place either."

    scene testofsenseiofsenseiof11
    with dissolve

    r "Are you kidding? This is the perfect chance to show you that the...growing distance between us we talked about the other day is all just surface level stuff! "
    r "We’re still friends, right?! We still know a bunch of stuff about each other, right?! "
    r "We’re not growing apart at all! I’ll show you!"
    s "Rin-"
    r "I mean it! I miss you and I’m sorry that things are getting all weird between us and...also, that I’m getting randomly emotional right now for some reason? "
    sa "Um..."
    r "I...I don’t know what’s going on! I just have to prove to everyone that we’re still homies no matter what mistakes we make or...what things we accidentally reveal to other people!"
    sa "Rin...I..."
    s "What did you-"
    r "Nothing! I’m sorry! I love you! But, like...friend love! Okay?"

    scene testofsenseiofsenseiof12
    with dissolve

    sa "Rin, I...think we should start the contest now. I’m also...starting to feel a little...weird in here..."
    sa "It’s not like it’s...harder to breathe, though...it’s more like...uhh..."
    sa "Actually, let’s just...uhh..."
    sa "I think I...have to sit down..."

    scene black
    with dissolve2

    "Sana darts past Rin and me before taking a seat on a pew and slapping her cheeks a few times to shake off whatever it is she was feeling moments ago."
    "And while I’m not sure if it actually {i}works{/i} or not, I elect to assume it does once she pulls her phone from the waistband of her skirt and begins to search for something..."
    "........."
    "......"
    "..."

    scene testofsenseiofsenseiof13
    with dissolve2

    sa "Um...so...we had Ami come up with all of the questions for the Sensei...knowledge test...thing, since...she’s the one who’s known him the longest."

    "True...but I can’t see how that’ll help when I barely know anything about myself that {i}I{/i} wasn’t here to figure out firsthand."
    "If there are any questions about anything prior to my start in Kumon-mi, I won’t be able to determine who’s right or not. And without Ami here, I can’t see how we could even-"
    "Wait. No. Why would there be any questions about things from before Rin and I even knew one another? If Ami knows anything about me, she should know I don’t open up about things like that."
    "So...these should all be fairly straightforward questions, shouldn’t they? "

    s "..."

    "A strange feeling catches up to me as well."
    "It doesn’t involve breathing."
    "But it does make it harder to breathe."

    sa "I think...umm...the easiest thing to do would be...to have you two take turns answering..."
    sa "And if both of you have the same answer...we can just...move on to the next question."
    sa "Whoever gets...ten correct answers first...will be crowned the winner..."
    sa "Is...Is that okay?"
    ya "Yes."
    r "..."

    scene testofsenseiofsenseiof14
    with dissolve

    sa "Rin?"
    r "Huh? Oh! Yeah. Yeah, that’s fine."
    sa "Then...I guess we’ll have you go first since...I’m suddenly the one in charge of this contest..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene testofsenseiofsenseiof15
    with dissolve2

    sa "We can start off with something that...looks easy..."
    sa "Oh. This one works..."
    sa "How old is Sensei?"
    r "31. Easy. Next question."
    sa "Wait...you have to give Yasu a chance to answer..."

    play sound "static.mp3"
    scene testofsenseiofsenseiof16 with flash
    stop sound

    sa "Yasu...same question..."
    sa "How old is Sensei?"
    ya "..."
    sa "Yasu?..."
    ya "I’m sorry...there seems to be...some sort of problem."
    ya "There is an answer in my head...but there is no way it can be accurate. That wouldn’t make sense."
    sa "Do you...want to guess anyway?..."
    ya "..."
    sa "Ya-"
    ya "No."
    ya "No...I will not answer this question. It is most assuredly some sort of mistake."
    ya "Is having so many people inside of the church the cause of some sort of disturbance in-"
    r "Okay, next question! Let’s keep this shit going so we can get out of here."

    play sound "static.mp3"
    scene testofsenseiofsenseiof15
    with flash
    stop sound

    sa "Um...who does...Sensei love more than anyone in the world?..."
    r "Am I guessing the answer Ami wrote? Or the actual answer?"
    sa "Probably...the actual answer...but they might be the same, so..."
    r "Sexual love? Or {i}love{/i} love? "
    sa "I...really hope it means {i}love{/i} love...otherwise..."
    r "That was a trick question. Sensei doesn’t believe in {i}love{/i} love. Which means that it defaults to sexual love, which makes the answer..."
    r "Uta-chan!"
    s "Correct."

    play sound "static.mp3"
    scene testofsenseiofsenseiof17
    with flash
    stop sound

    ya "Is it?..."
    ya "I had a different answer for that question as well."
    sa "What...was your answer, Yasu?..."
    ya "I’m being told...that I shouldn’t say it..."
    ya "That bad things will come if I say it..."
    ya "How unfortunate. I suppose I will have to pass on this question as well."

    play sound "static.mp3"
    scene testofsenseiofsenseiof18
    with flash
    stop sound

    r "Alright, hit me again! I’m starting to get fired up! "
    sa "..."
    r "Earth to Sana! I said hit me again!"
    sa "Oh! Sorry...I just...there's a page full of questions labeled “hard” and I was...looking at all of the answers myself."
    s "Don’t just peer into my background like that. That's an invasion of privacy, isn't it?"
    sa "S-Sorry! I’ve just...never really thought of...asking any of this stuff, and...and it’s...making me feel a little closer to you, since...you never tell me anything..."
    r "Then it’s a good thing you’re not the one up here! Leave those “hard” questions to Sensei’s self-proclaimed best friend, Rin Rokuhara. What’s next?"
    sa "Uhh...okay, then..."
    sa "Before Sensei was a teacher...he did something else...what was it?"

    scene testofsenseiofsenseiof19
    with dissolve

    r "Oh, I don’t think he’s told me this. But I remember Noriko saying something about it once and..."
    r "He was a...tutor wasn’t he? Or a babysitter or something?"
    ya "He was a tutor. That is correct."
    sa "Sensei?"
    s "Yeah...they both got it right."

    "Though that’s essentially all I know about the subject matter."

    sa "Then...as a follow-up question...where did Sensei do that?..."

    scene testofsenseiofsenseiof20
    with dissolve

    r "Uhh...I don’t know. House calls? Coffee shops? Maybe he-"

    play sound "static.mp3"
    scene testofsenseiofsenseiof21
    with flash
    stop sound

    ya "Heheh..."
    r "Huh? You don’t actually know, do you? Because you didn’t even know his age."
    ya "There are several answers to that question. "
    ya "Two of which are very naughty."
    ya "But the one that’s likely written down is..."
    ya "Well, I suppose it’s safe to just call it a storefront in the old district now."
    ya "Though, it was quite different back when it was used for...{i}educational{/i} purposes. "
    sa "Uh...well, all it says here is “building in old district” so...I think Yasu gets a point for that."

    play sound "static.mp3"
    scene testofsenseiofsenseiof22
    with flash
    stop sound

    r "Seriously? But that’s so vague...I didn’t realize we could just guess a district and say “Oh, it’s some building there.” "
    sa "Umm...what do you think, Sensei?...Should we give Yasu a point? Or..."
    s "I don’t see why not. I can’t imagine she’ll be getting many more since half of her answers have been cut off by poor godly reception."
    r "Ugh...fine. Whatever. Just give me the next question."
    sa "Okay...Here’s another “hard” one so...you can try to redeem yourself..."
    sa "Rin..."
    sa "What is the name..."
    sa "Of Sensei’s mother?..."

    scene testofsenseiofsenseiof23
    with dissolve

    r "You have a mother?"
    sa "Doesn’t...everyone have a mother?"
    r "I guess. I’ve just never heard him talk about her before."
    r "In fact, the one time I tried asking about that, he-"

    stop music
    $ renpy.end_replay()

    ya "Saki."

    scene testofsenseiofsenseiof24
    with dissolve2

    r "Huh?"

    play sound "static.mp3"
    scene testofsenseiofsenseiof25
    with flash
    stop sound

    ya "His mother's name was Saki..."
    s "..."
    ya "She didn’t like him very much."

    play sound "alert.mp3"
    scene forgetthisimmediately
    $ renpy.pause(5, hard=True)
    play sound "knock.mp3"
    saki "uʍop ǝpᴉsdn s,ʇᴉ"
    play sound "eggcrack.mp3"
    scene andsoami
    $ renpy.pause(5, hard=True)

    $ dormwartwo15 = True
    $ dorm2war2points += 1

    jump dormwartwo16

label dormwartwo16:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
mo "And..."
    mo "Oh..."
    t "Are you referring to the jokes about the semen?"
    mo "..."
    t "Molly?"

    scene girlsreturntobar30
    with dissolve

    mo "Huh? Yeah. Those are the ones."
    t "I understand. But I did not think bringing those things up in such a setting would lead to such a reaction from you."
    t "There are many comedians who draw upon real life experiences to-"
    mo "Have you not learned compassion in all of our time together?"
    mo "Have you not learned the things that make me worried or uneasy? Or scared or nervous? Or any of that? Any of the things I have finally begun to move {i}past{/i} feeling on a daily basis?"
    mo "Why would you wake those up? And for {i}laughs{/i} no less..."
    mo "Am I a joke to you?"
    mo "Or are you just {i}pretending{/i} to be oblivious right now?"
    t "..."
    mo "Tsuneyo...talk to me."

    scene girlsreturntobar31
    with dissolve

    t "I am not good at that."
    mo "What, and I am?"
    mo "There are too many skill trees in life to spec into all of ‘em...and there are gonna be times when we’ve gotta dig into our spellbook and put stuff we forgot we even had onto the hotbar."
    mo "What I’m trying to say is...just because we’re not good at certain things doesn’t mean we can avoid them forever if the mechanics of a fight call for them."
    mo "It’s either that or we just give up. And if there is anything I have learned from my time in Elden Ring, it is that Malenia is not going to just kill herself."
    mo "Peer into that inventory and see what you’ve got, Tsuneyo. Because there’ll always be something that’ll help...and whatever that something is is a little different for everybody."
    t "I do not understand any of what you just said, but I will do my best to explain my actions."
    t "One year ago, my inattentiveness and disregard for your safety led to you being harmed."
    t "And while you have chosen to believe that you were not harmed at all, it does not change what I saw and my thoughts on what may have happened that night."
    t "If I had only been there sooner, I could have prevented-"
    mo "It’s not your job to take care of me, Tsuneyo."

    scene girlsreturntobar32
    with dissolve

    t "But it is when you can not take care of yourself."
    t "Were you in the right state of mind to make decisions that night? Or were there multiple “debuffs” and “status effects” that disallowed you from acting of your own volition?"
    t "You are the first person other than my father that I have ever connected with. And it is my duty to protect you."
    mo "How are you going to protect me from something that already happened?"

    scene girlsreturntobar33
    with dissolve

    t "By not letting it happen again."
    mo "That’s not what you did."
    mo "All you did was reawaken the uncertainties of that night in not just me, but in Sensei as well."
    mo "I’m sure this will sound hard to believe, but I think that...he was just as much of a victim in that as I was."
    mo "No one paid closer attention to him in the coming days than I did. Not even Ami. And the way he acted was not of a man who did something malicious, but of a man who had something malicious done to {i}him.{/i}"
    mo "What if I was the one who forced his hand? And what if all of those “jokes” you told reminded him of that?"
    mo "There’s far too much unknown about that night to justify telling stories about it. But even if all {i}was{/i} known, it would not be your story to tell."
    t "..."
    mo "You really disappointed me, Tsuneyo..."
    mo "I didn’t think that would ever happen with you."

    scene girlsreturntobar34
    with dissolve

    t "I apologize for my actions...but I can not rid my mind of the horrible state I saw you in that night."
    t "And saying what I did seemed like the only way to make it so I wasn’t the only one who knew anymore."
    t "The idea of anyone harming you is too much for me to bear. And I believe that anyone who does so should have to pay a price."
    t "But...as it appears my words were truly just taken as mere “jokes,” you don’t have anything to worry about..."
    mo "I do, though. I have to worry about you doing that again."
    t "Molly..."
    mo "Tell me you {i}won’t.{/i}"
    mo "You can protect me all you want from things that haven’t happened yet, but don’t try rewriting the past and turning matters I have already settled into ones much greater than they wound up being."
    t "I don’t trust him with you anymore."
    mo "Do you trust {i}me?{/i}"
    t "Of course."
    mo "Then trust the {i}me{/i} who trusts {i}him.{/i}"
    t "..."
    t "What?"
    mo "That quote works better in its original context and phrasing but, what I’m trying to say is just...let me decide things like this for myself."
    mo "I wouldn’t care so much about my relationship with Sensei if he was not an important person to me."
    mo "And, as another person who is very important to me, you have to understand that."
    t "..."
    mo "..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    t "I will do my best."
    t "Please continue to be kind to me in the future."
    mo "Of course..."
    mo "And please let {i}me{/i} continue to dress you up in different outfits."
    t "Okay. But please stop groping me when I do so."
    mo "Please don’t tell me how to live my life."

    $ renpy.end_replay()
    $ dormwartwo14 = True

    "........."
    "......"
    "..."

    jump dormwartwo15
...
```