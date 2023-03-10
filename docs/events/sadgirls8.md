# A Beautiful Mind (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 522

* Event [Parallelogram](./sadgirls7.md) (Makoto) is completed)

* Day of week is Friday



## Next events

* [Maki: Baby Steps](./makiinv3.md)

## Event properties

* Id: sadgirls8
* Group: Makoto
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->sadgirls8

## Official wiki page

[A Beautiful Mind](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sadgirls8&go=Go) for more details.

## Event code

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label sadgirls8:
    scene hall_noon
    with fade
    play music "10c.mp3"

    "We’re now merely two hours away from what will be a complete week since Makoto got the news about her father."
    "Oh, and I guess Nodoka got her ass kicked as well- but that sort of pales in comparison to the emotional rollercoaster I was forced onto just minutes later."
    "Since then, things have calmed down a little."
    "Yumi was “indefinitely suspended” for attacking a fellow student."
    "Nodoka’s black eyes have started to fade back to their usual color."
    "Even Yasu has returned to normal."
    "Or...at least as normal as Yasu can possibly be."
    "I also have no idea how I would have survived this last week without Imani (Who seems to have forgiven me following the Yumi incident) seeing as she’s taken over all the clerical stuff in Makoto’s absence."
    "The only person who really {i}hasn’t{/i} shown any sign of improvement yet is Miku..."
    "Who, understandably, is decaying from the inside out knowing that the beautiful mind of her best friend is rotting away in a dark room several miles from here."
    "It’s a room that she’s spent far more time in than me."
    "It’s a room that she’s brave enough to return to while I would sooner slip back into the shadows and pretend none of this ever happened."
    "But every time I look at Makoto’s desk, that wishful illusion is suffocated out of existence."
    "And every time I watch her friend reflexively shift her gaze over to it to try and convince {i}herself{/i} this was all just some horrible dream, the truth is reinforced."

    scene black
    with dissolve
    play sound "slidedoor.mp3"

    "But that’s just the way it goes, I guess."
    "Sometimes, bad things happen to good people."
    "More often than not, it seems like this pattern not only continues, but aggressively ramps up with each passing day."
    "Sometimes, bad things {i}won’t{/i} stop happening to good people."
    "And while I wish that I could take these words to heart and truly feel something reminiscent of sympathy for the good person in question-"
    "I am one of those bad things."
    "And it would make no sense at all for me, burdened by my constant obsession with navel-gazing, to slight them when I am of that same ilk. "
    "I’ll remain quiet. "
    "I will wait."
    "And I will only moderately taint those that come to me with their concerns."

    scene makotoback1
    with dissolve2

    s "..."

    "And I will only moderately taint those that come to me with their concerns..."

    mi "Mornin’, Sensei."
    s "Good morning, Miku. Are you feeling any better?"
    mi "Not really. Was actually plannin’ on askin’ ya if I could maybe leave early today."
    s "You don’t need to ask. You can leave literally whenever you want. "
    s "I’m honestly surprised you’re coming at all given everything that’s happened."

    scene makotoback2
    with dissolve

    mi "I’d feel too bad ditchin’ swim club when two of the members ain’t comin’ to school right now and one of em’s still too sore to actually do anything."
    mi "Karin’s finally a captain, too. Bailin’ and leavin’ her with just one other girl would be way too rude."
    s "I think Karin’s mature enough to understand that you might want a little time away right now."

    scene makotoback3
    with dissolve

    mi "It’s fine, Sensei. Really. Gettin’ some exercise is good for me right now anyway. Helps get my mind off of stuff."
    mi "Sorry we ain’t been spendin’ much time together lately, though. All my free time’s been goin’ to Makoto and...yeah."
    s "How is she?"

    scene makotoback4
    with dissolve

    mi "She ain’t changed much. Still really sad and...sayin’ a bunch of things that don’t make much sense to me."
    mi "She’s bein’ a little nicer to Maki, though. Hasn’t really yelled at her lately. "

    scene makotoback3
    with dissolve

    mi "That wouldn’t have somethin’ to do with your little visit there, would it?"

    if makotolust30 == True:
        mi "Heard you were able to take Makoto’s mind off of stuff for almost a whole day. "
        mi "How’d ya do it? Lettin’ me and Maki in on your secret technique might be able to get her up and at ‘em again a little bit sooner."
        s "I...think it’s best if my technique remains hidden."

    else:
        s "You mean when I went into her room and tried having an actual conversation with her only for her to throw it back in my face?"
        s "I left before anything even happened. I doubt Makoto’s sudden change of heart has anything to do with me."
        mi "Well, I obviously wasn’t there, so I’ve got no idea what actually went down. But I think it’s clear as day that you showin’ up definitely helped at least a {i}little.{/i}"
        mi "Fact is, even if she didn’t seem like it at the time, Makoto loves ya. There ain’t no way she’d actually be mad about you tryin’ to be there for her."

    s "Whatever the case, I hope she comes back soon. Class is weird without her."

    scene makotoback5
    with dissolve

    mi "It really is, ain’t it?!"
    mi "I know we’re already pretty disorganized, but without Makoto actually givin’ people work to do, the whole heckin’ class has turned to chaos!"
    mi "I’m gettin’ dumber by the day, Sensei! And I was already in last place to begin with! I can’t afford this."

    play sound "slidedoor.mp3"
    stop music fadeout 5.0
    scene makotoback6
    with dissolve

    s "Well, I can’t say I’ll be as much help as her...but I guess I could try actually {i}teaching{/i} you for a little while each day until she comes back."

    scene makotoback7
    with dissolve

    s "Anything involving math, though, you're probably better off asking Imani. She’s a lot better at-"
    mi "Makoto?..."
    s "What?"

    play sound "static.mp3"
    scene makotoback8
    with flash
    stop sound
    play music "andlove.mp3"

    mak "{b}Guess who’s back, bitches.{/b}"
    mi "Makoto, what the heck are you doin’ here?! There ain’t no way you’re ready for this yet!"
    s "I think it might be time to cash in on that “going home early” thing, Miku. Take Makoto home before-"

    scene makotoback9
    with dissolve

    mak "Guys...guys! I’m {i}fine!{/i} I was able to dress myself and everything."
    mak "Besides, if I spend any longer inside of that room, I’m going to go fucking insane."

    scene makotoback10
    with dissolve

    mak "So, what’s new? Is Nodoka dead too? Is Yumi still a fucking bitch?"
    mak "Has Sensei been completely fucking worthless without me here to do everything for him?"
    mak "Or is shit pretty much the same?"
    mi "Makoto..."
    mak "What’s wrong? Taken aback by the fact that I’m now engaging in schoolgirl gossip rather than shunning it and burying my face in a fucking notebook instead?"
    mak "Spit it out, Miku. Tell me how much has changed."
    mak "Tell me how much happier everyone is without me here."

    play sound "static.mp3"
    scene makotoback11 with flash
    stop sound

    m "Well, that’s...certainly a look for her."
    m "I wonder what happened?"
    m "It’s not like Makoto to be anything less than perfect...and this sudden shift in aesthetic has made whatever the situation is impossible for me to ignore any longer."
    a "..."
    m "You haven’t heard anything from Sensei, have you?"
    a "..."

    scene makotoback12
    with dissolve

    m "Ami?"

    play sound "static.mp3"
    scene makotoback13 with flash
    stop sound

    mak "Okay! Since Miku didn’t have anything to say...how about you, Sensei?"
    mak "I haven’t seen {i}you{/i} since my mom dragged you all the way to my fucking house to try and manipulate me into not being sad anymore."
    s "That’s not what happened, Makoto."
    mak "Hmm...I guess that can be kind of subjective, yeah."
    mak "But something that definitely {i}did{/i} happen is you knocking one of my dad’s pictures off the wall and shattering it into a million pieces."

    if makotolust30 == True:
        mak "Was the mark you left on me not enough back then? You had to leave one on my fucking {i}hallway{/i} too?"
    else:
        mak "Just couldn’t go home without leaving your mark, huh?"

    mak "Did you know that a shard of glass managed to cut {i}right{/i} through my dad’s neck in that picture? Do you have any idea how fucking hysterical that is?"
    mak "I don’t even care that it was my favorite picture of us. That was genuinely {i}hilarious{/i}."
    s "Can the picture be replaced?"
    mak "With what? Wanna hang one up of yourself?"
    s "You know that’s not what I meant..."
    mak "Ooh! Maybe we can take one as a family! You can put your arm around me. I can look up at you with childish admiration in my eyes."
    mak "And then you could go into space and fucking suffocate because my life sucks and things like that just happen to me now."

    play sound "static.mp3"
    scene makotoback14 with flash
    stop sound

    ay "..."
    sa "Um...Ayane?..."
    sa "I know she’s kind of far away, but...you didn’t just hear what Makoto said...did you?"
    ay "I’ve never been so upset to have good hearing before..."
    ay "That poor girl...I can’t even imagine how that must feel."
    sa "Is...Is there something we can do?..."
    ay "I have no idea..."
    ay "And I’d say that the best thing we can do while we figure that out is to pretend we {i}didn’t{/i} hear anything, but..."
    ay "I think that is about to become impossible."

    play sound "static.mp3"
    scene makotoback15 with flash
    stop sound

    mi "Makoto! Stop it! You don’t have to come back to school yet! There’s no rush at all!"
    mi "Let’s...let’s go to the dorm! We can be alone there and I can tell ya all about how much school has sucked without you here!"

    play sound "slidedoor.mp3"

    ima "Senpai! I know you told me to stay in {i}our{/i} office until I finished with all of your paperwork. But I just got a call from Makoto’s mom and-"
    ima "Oh, fuck."
    mak "Attention, please!"
    ima "{i}Senpai, what do we do? Her mom doesn’t even know she’s here right now. She told me she went missing.{/i}"
    s "{i}Let’s...{/i}"
    s "{i}Let’s let her talk...{/i}"
    mak "I said {b}ATTENTION PLEASE!{/b}"
    mak "I know this isn’t the beginning of the school year anymore and that this is a really weird time to do this, but I’d like to take this opportunity to get to meet all of you!"
    mak "My name is Makoto Miyamura and my dad is fucking dead."
    o "Holy shit..."
    r "..."
    f "Oh, no..."
    f "I was really hoping...it wouldn’t be anything like that..."

    scene makotoback16
    with dissolve

    mak "I know that none of you have ever fucking cared about me, so this might just sound annoying, but I’d also like all of you to know that you won’t {b}have{/i} to be annoyed by me any longer!"
    mak "Because I don’t fucking care anymore!"

    scene makotoback17
    with dissolve

    mak "Schoolwork?! Studying?! Why waste time on things like that when life is finite and could be stripped from you at any moment?!"
    mak "What’s the point of striving to become better when it’s all for fucking nothing in the end?!"
    mak "In fact, what’s the point of living at all when it’s just constant stress and suffering and pain with {i}liiiiiittle{/i} tiny bits of the good shit sprinkled on top?!"
    c "We {i}do{/i} care about you, Makoto! Of course we care!"
    n "Chika’s right! If you need anyone to talk to, we-"
    mak "BZZZZZZZZZZZZT! {b}THE ANSWER IS THERE IS NO FUCKING POINT.{/b}"
    mak "Of course you’re going to act like you care now. Fucking look at me. You’d have to be fucking heartless  to ignore a girl giving a speech about her dead fucking dad."
    mak "But where were you before this?"
    mak "Where was fucking anyone other than Miku while I was suffering alone in my room?"
    mak "Which isn’t to say that any of you showing up would have fucking {i}helped{/i} me. But it really would have been the nice thing to do, right?"
    mak "Like...I don’t know. Maybe a fucking card?"
    mi "They didn’t know, Makoto! We didn’t tell anyone because we thought it was too soon!"

    scene makotoback18
    with dissolve

    mak "{b}TOO SOON?!{/b}"
    mak "My world is fucking exploding right now and you think it’s “too soon?!” For what?!"
    ki "Hey, don’t take your anger out on Miku! She’s been miserable all week long worrying about you!"

    scene makotoback19
    with dissolve

    mak "I’m not taking anything out on anyone! In fact, you’re {i}all{/i} pretty fucking great! It’s no wonder you haven’t bothered with {i}me!{/i}"

    scene makotoback20
    with dissolve

    mak "I annoy you, right?"
    mak "You hate that I’m the one who forces you out of what should be seven hours of pure fun and relaxation..."
    mak "You hate that you can’t spend all of your time with Sensei because I’m constantly making him spend time with {i}me{/i} instead..."
    mak "You hate the worksheets. And the quizzes. And the message board. And all of the other stuff I put together because something inside of me made me feel like I had to make my daddy proud one day."
    mak "And that if he saw how smart and responsible I’d become...that he’d be able to die happy."

    scene makotoback21
    with dissolve

    mak "But, instead..."
    mak "He just {i}died.{/i}"
    mak "And now I’ll never know if he was happy or not."

    scene makotoback22
    with dissolve

    mak "But, I’ll tell you one thing I {i}do{/i} know..."
    mak "It's that {i}I{/i} sure as fuck won’t ever be."
    mak "There’s nothing left for me to work for."
    mak "No reason to keep trying so hard for a bunch of people who see me for who I {i}really{/i} am."
    mak "An incorrigible...irritating...loud mouthed bitch."
    mak "Just like my mother."

    play sound "static.mp3"
    scene makotoback23
    with flash
    stop sound

    ima "Are you really sure we should be letting her ramble on like this? She’s clearly out of it and this is, like...reputation suicide."
    s "Maybe that’s what she wants?"
    ima "Senpai..."
    s "Who says starting over has to be a bad thing?"
    ima "No one. {i}I’m{/i} not saying that. I just think that we should maybe wait until she’s...oh, I don’t know- not running away from home and giving speeches to the class while cosplaying as a fucking zombie."
    ima "I just don’t want her going out in some blaze of glory while everybody else sits back and watches."
    s "Who says everyone’s just sitting back and watching?"
    ima "Senpai, what are you talking about? Are we not seeing the same thing right now?"
    s "Stop staring at me and take a look for yourself."

    play sound "static.mp3"
    scene makotoback24 with flash
    stop sound
    stop music

    mak "..."
    a "Shut up..."
    a "Shut up...shut up...shut up..."
    a "Hearing you say those things..."
    a "It brings back too many bad memories..."

    scene makotoback25
    with dissolve2
    play music "kimitoakinobouken.mp3"

    mak "..."

    "Sometimes, all it takes to reduce the suffering is someone you can relate to."
    "Someone who climbs out of the woodwork and into your arms...that you can abhor in moments of joyous splendor and admire in stretches of constant pain."
    "I let her speak because I knew this would happen."
    "I knew it from the moment I saw Ami’s face."
    "Because Ami is a girl I have cherished and loved."
    "She is a girl I understand."
    "And Makoto?"
    "Makoto will become one of those too."
    "But for now, she needs to suffer."
    "For now, she needs to cry."

    scene makotoback26
    with dissolve2

    mak "{b}AAAAAAAAAAAAAAAAAAAAAAAAAHHHHHHHHHHHHHHHHH!!!!!!!!!!!!!!!!!!{/b}"
    ima "Uhh...okay! If your name isn’t Makoto, Ami, Miku, or Sensei, please leave the room right now! We’re going to have class in the gym or something!"
    ki "I actually think Miss Watabe’s class is in the gym right now."
    ima "Then it looks like we’re having a joint period! Go, go, go!"

    scene black
    with dissolve2

    "The girls filter out of the room paying minimal attention to what’s happening in the front of the class despite a burning interest to act in opposition to that."
    "Imani is the last one out, sliding the door closed after locking eyes with me and silently admitting that sometimes I can, whether it be intentional or not, actually know what needs to be done."
    "Those moments are few and far between. And frankly, this moment isn’t even one of triumph for {i}me{/i} as all I did was clear a path for the only person actually able to do anything when it comes to pain like this."

    scene makotoback27
    with dissolve2

    a "Never say you won’t ever be happy again! It’s a lie! A lie I told myself over and over when this happened to me!"
    mi "Ami’s right! This’ll sting forever, but there’s plenty more good stuff out there! Good stuff I wanna see and experience with my best friend!"
    mi "You think we woulda made it as far as we did if we just gave up?!"
    a "Yes, you’re annoying! Yes, I hate the stupid worksheets! And yes, I kinda hate {i}you{/i} when you spend every day trying to steal my uncle away from me!"
    a "But I’d never wish this sort of pain on anybody in the whole wide world!"

    scene makotoback28
    with dissolve2

    a "And you need to know that life goes on."
    mak "Ami..."
    a "There isn’t a day that goes by where I don’t miss my parents. I can’t even cross the street without having to force back tears."
    a "But Sensei makes me happy now! And you still have your mom!"
    a "Let her be that for you! Stop closing yourself off and let {i}her{/i} make you happy instead!"
    a "That’s what your dad would have wanted, isn’t it?!"
    a "Wouldn't he have wanted you to be happy?!"

    scene makotoback29
    with dissolve2

    mak "But..."
    mak "It’s so hard!"
    mak "I can’t stop thinking about him! About what his final thoughts must have been! About how I never got to say goodbye!"
    a "I know it’s hard! But it'll only get easier from here, Makoto! So don’t give up just yet!"
    a "Keep being the same annoying you! Because even if we’re not there for you all the time and forget to make cards when things are horrible, we {i}do{/i} care!"
    a "And we can cry together when no one else understands our pain!"
    mak "I don’t want to cry anymore! I don’t want to cry!"

    scene makotoback30
    with dissolve

    a "Well, too bad because I do!"

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "I leave the classroom as well and retreat to the gym to meet back up the rest of the girls."
    "There was no reason for me to be in that classroom any longer."

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve2

    "But what I heard from Ami in the coming hours is that things worked out okay."
    "That Makoto went back home with Miku and has decided to take a little time off of school for the foreseeable future."
    "That she wouldn’t try running away again. And, if she ever felt the urge to, she’d talk to her mom first."
    "Of course, those are just words. And she may very well act out against them."

    scene black
    with dissolve

    "But something about the way they sound when released by the mouth of a third party makes me want to trust them a little more this time."
    "You see, the thing with words is that they’ll always be ephemeral."
    "And that, with how rapidly our lives and the world itself are changing, they’re really just air in the end."
    "And so Makoto will suffer as she remembers the life of the man she loved most."
    "But that’s fine."
    "Because if she listens hard enough, she’ll still be able to hear his voice in the whispers of the world itself."
    "And that gift from the sky should be enough to keep her grounded."

    $ renpy.end_replay()
    $ sadgirls8 = True
    $ makoto_love += 1
    $ mikublock = False
    $ makiblock = False
    stop music fadeout 10.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "{i}But she’ll need some time alone for a while...{/i}"
    "........."
    "......"
    "..."

    jump advancetosat
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
jump day142
    if totaldays >= 144 and day128 == True and day142 == True and day144 == False:
        jump day144
    if totaldays >= 150 and day144 == True and streets15 == True and cafe20 == True and soccer10 == True and day150 == False:
        jump day150
    if totaldays >= 153 and day150 == True and day153 == False:
        jump day153
    if totaldays >= 154 and day153 == True and day154 == False:
        jump day154
    if (totaldays >= 200 and day == 5 and beachvacation16 == True and chikainvite1 == True and harukadate1 == True and kaoridate1 == True and cafe25 == True and bar25 == True and mayadorm25 == True
    and mikudorm15 == True and streets25 == True and makotoinvite2 == True and makidate1 == True and rindorm35 == True and halloween1 == False):
        jump halloween1
    if totaldays >= 214 and makidate5 == True and halloween14 == True and makotodorm25 == True and mikudorm30 == True and amidorm25 == True and day == 1 and day214 == False:
        jump day214
    if totaldays >= 215 and day214 == True and day == 2 and day215 == False:
        jump day215
    if totaldays >= 216 and day215 == True and day == 3 and day216 == False:
        jump day216
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
...
```