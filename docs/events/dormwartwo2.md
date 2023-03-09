# Dorm War II: Pre-Game Show
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo2&go=Go)


Part of event chain [A Walk Through Hell](./dormwartwo1.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwartwo2
* Group: Main
* Triggered by label: dormwartwo1

## Event code
File: \game\chap3.rpy
Code:
```python
...
label dormwartwo2:
    scene anewinterview1
    with dissolve2
    play music "notabluearchivesong.mp3"

    mo "And we’re live! Welcome back to another installment of pre-war interviews hosted by the remarkable Molly Moyra MacCormack and her lovely assistant, Ayane (Insert Middle Name Here) Amamiya!"
    ay "I’m not your assistant! And Japanese people don’t have middle names! "

    scene anewinterview2
    with dissolve

    mo "Well said! And sincerest apologies for attempting to hog the spotlight when that’s all I did last Samhain!"
    ay "You were extremely drunk and extremely loud! "

    scene anewinterview3
    with dissolve

    mo "And right now I’m just extremely loud! But there’s good reason for that, because we’ve got a load of interviews for you viewers at home that are sure to get your bones quaking and your pants tightening!"
    ay "That’s right, ladies and gentlemen. Through meticulous planning and a good nine or ten arguments, we’ve finally got a lineup of memorable, action packed competitions that’ll make last year's wars look more like..."
    ay "I don’t know. A big thumb wrestle or something. And Super Mega Ultimate Dorm Thumb Wrestle doesn’t exactly have a good ring to it."

    scene anewinterview4
    with dissolve

    mo "The point! You’re losing it!"
    ay "Sorry. I’m not used to being on camera. "
    mo "Then get lost and start prepping for the next interview while I take it from here! If there’s anything Molly MacCormack is good at- well, besides repeatedly spending all of my allowance on JPEGs...it’s pointless banter!"

    scene anewinterview5
    with dissolve

    mo "And also managing to hold my tears in when my favorite characters die in anime and manga. It really just doesn’t hit the same as it used to, you know?"
    ay "Sure! I’m gonna go over there now, though, so..."
    ay "Take it away Molly!"

    scene anewinterview6
    with dissolve

    mo "At last, you and I have reunited at the edge of the world. How unfortunate that our rendezvous has come just mere moments before the light of Re-Horakhty rains down upon us all."
    mo "But in these final moments, know that I regret nothing. And that all that’s sure to come over the next 48 hours is just a final way for me to-"
    ay "Molly! I’m ready!"

    scene anewinterview7
    with dissolve

    mo "Ayane! You ruined my monologue! I was finally the main heroine and that was my moment to shine!"
    ay "Shine for who? The camera guy?"

    scene anewinterview8
    with dissolve

    mo "Wait, yeah. Who are you any-"

    play sound "static.mp3"
    scene anewinterview9 with flash
    stop sound

    ay "I’m joined now by my co-host’s competitor in what will be our first competition of the second annual Dorm Wars, Sana Sakakibara."
    ay "Sana, after competing in something as “outside of your comfort zone” as last year’s fashion show, how does it feel to return to something more “up your alley” like gaming?"
    sa "It feels, umm...really good, but...I still don’t really know what games we’re going to play or...or how good Molly is at games in general, so..."
    ay "Word on the street is that you’ve been using performance enhancing drugs ahead of the competition to prepare yourself for certain victory. Do you have anything to say about these allegations?"
    sa "Do they...have...performance enhancing drugs for...video games?"
    ay "Playing the fool, I see. A valiant strategy. But never fear, Sana. I’ll always have your back no matter what. Even if you {i}are{/i} taking drugs."
    sa "But I’m...I’m not-"
    ay "Final question, if you had to describe yourself with a flavor of Pop-tart, what would it be?"
    sa "Wha...what?! What does that have to do with-"

    scene anewinterview10
    with dissolve

    ay "And that’s everything from Sana, ladies and gentlemen! Be sure to cast your vote for her during her contest tomorrow morning by texting “POPTART” to 867405!"
    sa "Ayane, I don’t even know what a Pop-tart is!"

    scene anewinterview11
    with fade

    mo "Our next interview is with Touka and Makoto, daughters of the women competing in the contest that many have begun calling the “Battle of the MILFs!”"
    mak "No one has started calling it that. You are the first person."
    to "Can someone please explain to me what a “MILF” is? Is it anything like a WAP? Because my mother has not stopped saying that word as of late and I am beginning to fear for her health."
    mo "I mean...maybe a {i}little?{/i} Just...think of it meaning a hot mom or something!"
    to "It’s the midst of summer. We’re all hot. "
    mak "Do I really have to do this? I wanted to go to lie down early tonight."

    scene anewinterview12
    with dissolve

    mo "J...Just humor me for a minute, okay? "
    mo "How are you guys feeling about your battle with one another? Any lingering worries? Like...Like what the Herald of the Adolescents may get up to with your respective mothers?"
    mak "He wouldn’t be much of an adolescent herald if he was spending time heralding grown women, would he? "
    mak "That said, I don’t really care one way or the other. I’ve already accepted that Touka’s mother is very likely going to win and that mine is going to make the two of us look like fools."

    scene anewinterview13
    with dissolve

    to "I also believe my mother is going to win, but that isn’t a passive aggressive means of talking down on Makoto’s mother, who I’m sure is a lovely and caring woman."
    mak "She’s certainly a woman, alright."
    mo "So, you’re not at all worried of Sensei using his protagonist powers to win your mother over while the two of them are alone?"
    to "Of course not, for I’ll be with them the whole time. And I doubt his powers are strong enough to win both of us at once."

    scene anewinterview14
    with dissolve

    mo "I wouldn’t be so sure of that. The list of tags in life is pretty incomparable, you know? I’m sure it wouldn’t be the first time a teacher has- you know what? Now’s not the time."

    scene anewinterview15
    with dissolve

    mo "I do want to end with one final question for Makoto, though. "
    mak "For me specifically? What is it?"
    mo "How are you doing? We’re all glad that you’ve been coming back to school, but-"
    mak "I’m fine and ready to move on. Thanks for asking. "
    mo "Are you sure there’s nothing more we-"
    mak "I am. Thank you. Are we done now?"
    mo "Oh, I...I guess so. "

    scene anewinterview16
    with fade

    ay "Well, that’s great news as I am here with two more competitors for what is sure to be one of the craziest contests we’ll have all year!"
    r "{i}Help me...{/i}"
    ya "This morning, I awoke with scratches all over my body. When I looked in the mirror, I noticed they spelled “Ezekiel.” "
    ya "I am unsure of whether or not this relates or pertains to the contest, but I will try my very best to win at whatever that may be before being squished like a bug beneath Rin’s boots."
    r "Again, {i}help me...{/i}"
    ay "Rin, you seem a little intimidated by your rival in this year’s matchup. Does that fear have anything to do with what many have been citing as “ESP” from Yasu?"
    r "Uhh-"
    ya "When I look into your eyes, it’s like peering through two cracked glass spheres, each one splintering out as those cracks become new veins on the inside of your face."
    r "Nope. Nothing to do with the “ESP” or whatever. Just not sure if I’m going to be sacrificed."
    ya "He who has awakened will not take your life, Rin. Though, He may ask for something else in return for salvation. But I can assure you that what is meant to be taken is never meant to be mourned."
    ya "Its passing will only serve to make you stronger."

    scene anewinterview17
    with dissolve

    r "Uh-huh. Yeah."
    r "I’m gonna go...to the bathroom now. "
    ya "May I accompany you? I can’t find Touka and often get lost when I am not following behind someone."

    scene anewinterview18
    with dissolve

    r "Touka?! Where are you?! Please come get your child!"

    scene anewinterview19
    with fade

    mo "Up next, we have the Kendo Princess, Tsuneyo Tojo, sporting the latest MacCormack creation! A costume based on a character in a video game that is definitely not made for lolicons!"
    mo "We also have Miss Imani Imai, who has been admiring said costume ever since school ended!"
    t "You teachers are all the same. I miss the days when my father would teach me numbers."

    scene anewinterview20
    with dissolve

    ima "Speaking of numbers, how old are you again?"
    t "Never ask a woman her age, you bastard. I could have your head for that."
    ima "If it’s head you want, all you need to-"

    scene anewinterview21
    with dissolve

    ima "Fuck! No! Bad Imani!"
    ima "I have to leave! Goodbye!"

    scene anewinterview22
    with dissolve

    mo "So, uhh...to get back to the topic of jokes, how do you feel now that you’ve finally been given a chance to show your stand-up chops in front of the rest of the guild?"
    t "Like I am on the brink of disappointing everyone. "
    t "But I heard from a wise man a long time ago that the best way to move forward is to...become uncomfortable. Or something along those lines. "
    t "So I am willing to sacrifice myself for an effort to move forward. And if I do not, I will die as a warrior who made an effort to live and find a place in Valhalla as a tree."

    scene anewinterview23
    with dissolve

    mo "And your opponent? Are you worried about her at all?"
    t "Yes. She seems to be acting a bit differently as of late and I am not sure whether or not something may have happened to her."

    scene anewinterview24
    with dissolve

    mo "I...I was talking about worrying about her comedy, but...You think something happened to Ayane? She’s seemed mostly the same to me."
    t "Sometimes, the biggest changes are the ones buried the deepest. And we will never come to know them unless we submerge ourselves beneath it all."
    mo "..."
    t "..."
    mo "Huh..."

    scene anewinterview25
    with fade

    ay "So, the two of you were the ones chosen at random to participate in what has quickly become the most desired competition in all of the Dorm Wars. How does that feel?"
    n "Honestly? Amazing. I’ve dreamt of this day ever since I was a little girl. "
    n "Did I think it would be part of a contest? No. But any chance to show Sensei how much I love him is good enough for me. And I will take every single chance I ever have to do that."
    f "For me, it’s...well...a little less meaningful, I guess..."

    scene anewinterview26
    with dissolve

    f "I obviously don’t have the sort of...emotional connection to Sensei that Noriko does given how long she’s known him, but..."
    f "He’s made a big impact on my life and...I’m also happy with the opportunity to...probably lose to her."
    n "Don’t say that. You’ve got just as much of a chance as me. In fact, you might even have a {i}better{/i} chance since Sensei’s memories started exploding before I walked back into his life."
    n "At the end of the day, all that really matters is that we stay true to ourselves and let him have some fun in the process. If we win, we win. If we lose, we lose."

    scene anewinterview27
    with dissolve

    n "And then we can all get naked and make out in my dorm room because that just seems like it would be the right thing to do after the two of us date the same guy for an entire day."
    f "I...don’t really...want to do that..."
    n "Well, it was worth a shot. That costume’s got me feeling some sort of way, Futaba. And I apologize for displaying the same level of unrestrained arousal my roommate so typically does."
    ay "Wow. Everybody’s just really horny for each other today, aren’t they?"

    scene anewinterview28
    with dissolve

    f "It’s a weird time to be heterosexual, isn’t it?"
    ay "It really is."

    scene anewinterview29
    with fade

    mo "Speaking of people who are always horny, I’m joined now by Nodoka Nagasawa who is dressed up as...uhh..."
    no "Sada Abe."

    scene anewinterview30
    with dissolve

    mo "The...femme fatale who lopped off her lover’s penis and carried it around in her purse until she was arrested?"
    no "Once the rigor mortis sets in, it’s like it was never lopped off at all."
    mo "Uhh..."
    mo "Okay. Well, moving right along, there’s a lot of uncertainty surrounding your competition in the Dorm Wars. Especially considering we don’t even know what that contest {i}is{/i} yet."
    mo "If Yumi does agree to participate, are you worried at all that she’ll try to attack you again? And is that hostility playing any role at all in your battle plan to take her down for good?"

    scene anewinterview31
    with dissolve

    no "Let me make one thing clear. I have no problem with Yumi. I think she’s a troubled girl who is genuinely attempting to better herself. And Futaba believes so as well after her recent apology."
    no "What issues she has with {i}me{/i} specifically, I’m not sure. "
    no "But I’m confident that her time away from class may have led to her reevaluating both her position in the social hierarchy that is high school as well as who she is as a person."
    no "I hold no grudge against her and wish her all the best."

    scene anewinterview32
    with dissolve

    no "That said, I can’t wait to make her grovel before my feet when I destroy her in whatever competition is chosen for us."
    mo "Oi, ain’t that a shocking condemnation if I’ve ever heard one. Final question, Nodoka- if there is any competition you’d {i}like{/i} to take on Yumi in, what would it be?"
    no "Hmm...that’s a good question."
    no "But I think if I had to choose, I’d like something where the two of us are locked in a closet with Sensei and he has to choose which one of our-"

    scene anewinterview33
    with dissolve

    mo "Ayane, quick! We’re about to get cancelled!"

    scene anewinterview34
    with fade

    ay "Not on my watch, we’re not! Maya, is it true that-"
    m "I won’t be taking any questions. Thank you."
    i "I will also be abstaining from...whatever is going on right now. I have zero interest in both the Dorm Wars and every single one of you, so...yeah."

    scene anewinterview35
    with dissolve

    ay "You guys make horrible interviewees. There are a bunch of people looking forward to seeing you in maid costumes, you know. I just wanted to ask some stuff about that."
    m "We have to wear the costumes too?"
    ay "I mean...I think {i}not{/i} doing that would cause you to lose some points, wouldn’t it?"
    i "Uta’s pretty adamant about dressing for the role, so she might get all pissy if you start doing maid stuff without looking like a maid."
    i "But, then again, she’s also a kunoichi right now, so she might just assassinate you or something instead of throwing a hissy fit."
    m "That actually sounds preferable, to be honest. I’ll take the assassination."
    i "I’ll let her know. And congratulations on making it into my list of people I don’t inherently hate."

    scene anewinterview36
    with dissolve

    ay "What about me? Do you hate me as-"
    i "Yup."
    ay "What? Why?"
    i "Too loud. Too rich. Too blonde. And I have a natural distaste for anyone who gets naked with the guy I like, so...yeah."

    scene anewinterview37
    with dissolve

    ay "Oh yeah? Well I think you’re a...a..."
    ay "I think you’re going to lose!"
    i "Yeah, you’re probably right. Losing’s pretty on brand for me."
    m "Okay. I’m going back inside now."

    scene anewinterview38
    with fade

    mo "Molly here again! This time with Kirin Kanda and Ami Arakawa! And since none of us have any idea what they’re going to be competing in yet, I’m just going to ask them some random questions!"
    a "Can you start by asking Kirin why she has her arm around me when we’ve barely even talked before?"
    mo "Kirin, why do you-"
    ki "Just trying to get a little closer to my rival, that’s all! If you and me build up our camaraderie before our contest is decided on, it’ll hurt a little less when one of us loses!"
    a "You mean when {i}you{/i} lose. There’s no way I’d ever lose in a Sensei-based contest to someone who doesn’t even love Sensei."
    ki "Oh yeah? You think you can beat me at literally {i}everything?{/i}"
    a "Is there...something you’re good at? Because I really have no idea since, again, we’ve never talked."

    scene anewinterview39
    with dissolve

    ki "I’m good at plenty of things. I just shouldn’t say any of them on live television in case my parents are watching."
    mo "Oooh...it looks like we’ve got a true competitor in our midst if the contest between these two winds up being x-rated!...Which it probably won’t because there’s no way that would be approved."
    mo "And also because this isn’t one of those fake game shows that get all porny out of nowhere."

    scene anewinterview40
    with dissolve

    ki "Oh, like the ones where people wind up blindly fucking their siblings without knowing?! I love those!"
    ki "There’s one I saw where this guy railed the {i}fuck{/i} out of his sister like ten times harder when he {i}found out{/i} it was her. That’s the shit I live for."
    mo "A comrade! Your degeneracy has finally appealed to me in a way that I can relate to instead of a way that makes me feel self-conscious!"
    a "I saw one of those once. It was an uncle who wound up having sex with his niece."

    scene anewinterview41
    with dissolve

    ki "Uhh...ain’t that a little on the nose?"
    a "On what nose? "
    mo "I guess I’ll do my duty as a reporter and ask...Ami, there are many rumors about your true feelings regarding your uncle. "
    a "I know. I’ve heard them."
    mo "Then...do you have anything you'd like to say in regard to them?"
    a "Nope. "
    mo "Oh."
    ki "Can I make a comment?"
    a "Sure."
    ki "Cool."
    ki "I hope our contest is one of those game show things."

    scene anewinterview42
    with fade

    ay "We’re getting close to the end now, folks! This is Ayane Amamiya once again, and my final interview for the day is with none other than the competitors for this year’s popularity poll! Otoha Okakura and-"

    scene anewinterview43
    with dissolve

    ay "Wait, Chika- I thought you went to go meet up with Yumi? "
    c "You know, I was going to. But when I heard “popularity poll,” I felt like I should do a few laps around the school to make sure I lock in as many votes as I can."

    scene anewinterview44
    with dissolve

    ay "Spoken like a true Sensei-lover. I can respect that."
    c "{i}Me?{/i} Pfft. Of {i}course{/i} not. Isn’t he like, forty?"
    c "Plus, I’m still going to meet up with Yumi. I’m just doing it after this instead. Figured I might as well stick around and show Otoha I mean business."
    ay "And Otoha, do you have any plans to counter this aggressive attack so early on from your opponent?"
    o "Uhh...not really, no. I was kind of just hoping people would keep doing that thing they do and...wanting to get close to me for whatever reason."
    o "And I ain’t really about walking around wearing next to nothing just to get votes."

    scene anewinterview45
    with dissolve

    c "Umm, Otoha- do dogs wear clothes? Obviously not. And I am {i}clearly{/i} a wolf-girl, so...yeah."
    o "Sorry, {i}is{/i} that clear? Because you look a lot more like a living mascot for petplay than an actual animal to me."
    c "Wanna try it on? I bet your girlfriend likes it."

    scene anewinterview46
    with dissolve

    o "Don’t fucking joke about that. It’s not funny."
    c "I obviously wasn’t serious. Chill. "
    ay "Uhhh...okay! So, without sowing any more seeds of destruction, I’d like to wish the two of you the best of luck in your poll and urge you to keep campaigning as hard as you can!"

    scene anewinterview47
    with dissolve

    ay "And remember, folks! Be sure to vote! Wasting your vote is the same thing as wasting your voice, and you’d never want to throw that away, would you?!"
    ay "This is Ayane Amamiya, signing off! Back to you for the final interview, Molly!"

    scene anewinterview48
    with fade

    mo "Thanks, Ayane! And thank you Miku and Uta for joining me for the final interview of the-"
    mi "Ughhhhh! Whatever! This is like, so totally boring. Like, Dorm Wars? Seriously? Don’t you guys have any friends? Is this really what you do for fun?"
    u "The idea of “fun” does not exist. All we have is silence....shadows...the dark...and a mission. A mission to remain unseen. {i}Unheard.{/i} Unnoticed..."

    scene anewinterview49
    with dissolve

    mi "Tch. Ain’t “unnoticed” the same thing as “unheard” and “unseen?” That’s like, totally adorable. Look at you trying so hard to act cool. It’s hilarious. Can I take a pic? I’ll tag you. What’s your insta?"
    u "I do not understand the concepts of which you speak...nor the wretched scent of that perfume nor impractical accessories you don as if they are protection."
    mi "They {i}are{/i} protection, doll. They’re protecting me from looking so {i}stupid.{/i} Like, where did you even get that scarf? Goodwill?"
    mo "I have to say, this is going a lot better than I expected it to and I have to applaud both of you for both your fantastic costume design {i}and{/i} your commitment to your respective roles."

    scene anewinterview50
    with dissolve

    mo "It’s a risky move choosing to dress and act like a gyaru while we already have one in- uh-oh."
    u "Trouble approaches like morning dew. Quiet...but consistent. Reliable."

    scene anewinterview51
    with dissolve

    c "..."
    mi "..."
    mi "Uhhhh..."
    c "Miku..."
    mi "I...can totally, like...explain..."
    mi "This is-"

    scene anewinterview52
    with hpunch

    c "YOU ARE SO FREAKING PRECIOUS, OH MY GOD!"
    c "Where’d you get your top? And those bracelets? You have to show me. Just not today since I’ve got other stuff to do."

    scene anewinterview53
    with dissolve

    c "Oh! We should, like...totally go shopping together soon. I can show you all sorts of places with great stuff for mad cheap that-"
    mo "Chika, Miku’s disguise is simply a temporary item set that-"

    scene anewinterview54
    with hpunch

    c "Shut your fucking mouth, Molly! Let me talk to Miku alone! No one else ever dresses like me and I finally have someone to bond with even if it’s fake!"
    mi "Uhh...umm..."
    mak "Miku, you have a...tanning appointment in five minutes. Or something."

    scene anewinterview55
    with dissolve

    mi "R-Right! That, like...totes slipped my mind! Thankies, Makoto!"
    c "Wait! Come back! We weren’t done bonding! I love you!"
    u "Gone...like the color of the Chitose River in winter...waiting for its moment to return. But when? And who will be there to watch as the color returns?"

    scene anewinterview56
    with dissolve

    c "..."
    u "..."
    mo "..."

    scene anewinterview57
    with dissolve

    u "Wshhhh..."

    scene black
    with dissolve2
    stop music fadeout 15.0

    mo "This concludes our second annual pre-war interviews! Thanks so much for watching and be sure to keep an eye out as the contests kick off first thing in the morning when I take on floor one’s Sana Sakakibara!"
    mo "Until then...Stay modest! Stay Molly!"
    mo "Seele out!"
    a "You know that’s not what that character is like at all, right?"
    mo "I actually haven’t even played the game yet."

    $ renpy.end_replay()
    $ dormwartwo2 = True

    "........."
    "......"
    "..."

    jump dormwartwo3

label dormwartwo3:
...
```

## Code that triggers this event
File: \game\chap3.rpy
Code:
```python
...
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
...
```