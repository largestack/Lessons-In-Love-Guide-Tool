# Chronokinetics (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 540

* Event [No Strings Attached](./imanispecial1.md) (Main) is completed)

* Day of week is Tuesday



## Next events

* [Ayane: How the World Works](./ayanesanabeach1.md)

## Event properties

* Id: ayanespecial40
* Group: Ayane
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->ayanespecial40

## Official wiki page

[Chronokinetics](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanespecial40&go=Go) for more details.

## Event code

File: (install folder)\game\AyaneEvents.rpy

Code:
```python
...
label ayanespecial40:
    scene ayanecantbone1
    with fade
    play music "phantomthief.mp3"

    "I’m not going to lie, not having Makoto around fucking sucks."
    "Because, in addition to being one of the girls I am currently allowed to have sex with (Thanks, Maya), her {i}not{/i} being here is beginning to increase the amount of time I have to spend in this building."
    "And it certainly doesn’t help that Imani is a pretty good teacher and has actually started assigning work to the girls. "
    "Now, you may be asking yourself, just how much paperwork can there possibly {i}be{/i} for a class of twenty-ish who receive maybe one written assignment per week. And the answer to that is simple."
    "There is paperwork."
    "It’s not a large amount. In fact, the amount I have to handle is so minuscule that I’m sure Wakana would mock and ridicule me if she could only hear my thoughts."
    "But when you don’t want to work, any amount of work at all is too much."
    "I have far too many things to think about."

    play sound "knock.mp3"

    s "..."

    "And far too many girls to have sex with."

    s "Come in."

    play sound "dooropen.mp3"
    scene ayanecantbone2
    with dissolve

    "Or not."

    ay "Good! You’re still here. I was worried you may have left with Ami and Maya."
    s "Is there any reason {i}you{/i} didn’t leave with Ami and Maya?"
    ay "Swim club, obviously."
    s "Ahh, yes. I can see that it’s going very well by the fact that...you are here and not there."

    scene ayanecantbone3
    with dissolve

    ay "Yeah...I got halfway there and then thought to myself- you know what, Ayane? It’s been a long time since you’ve hung out with Sensei in his office after school. You should go do that."
    s "Good on you for being mentally stable. You’ll have more free time that way."

    scene ayanecantbone4
    with dissolve

    ay "I wouldn’t mind being a little crazier if it meant I got to spend more time with you."
    ay "And, at the rate things have been going lately, that seems like it might be a real possibility!"
    s "Is the fact that this is all some sort of infinite cycle finally starting to weigh on you?"

    scene ayanecantbone5
    with dissolve

    ay "Of course. I just haven’t quite figured out the right way to talk about it yet because I don’t understand nearly as much as you and Maya even {i}with{/i} all of the questions I’ve asked her."
    ay "Which is doubly annoying since it’s starting to seem like being the “runner up” just might be who I am as a person."
    s "You’re not a runner up at all, Ayane. You’re...Well, you’re you."

    scene ayanecantbone6
    with dissolve

    ay "Yeah. Second place to Ami when it comes to your list of interpersonal priorities and second to Maya when it comes to your list of...apocalyptic ones."
    s "If you weight the points you get from both of those categories, I think that would put you in first."

    scene ayanecantbone7
    with dissolve

    ay "Sensei, I’m being serious right now. This is all still really scary to me and there are so many things I don’t understand. "
    ay "Also, I’m worried that if I have to go any longer without having sex with you that my vagina is going to close up and we’ll never be able to have sex again."
    s "What were you saying about going insane just a minute ago? Because I think that sentence may have just put you over the edge."

    scene ayanecantbone8
    with dissolve

    ay "You know...when I first heard that abstinence suggestion thingy from Maya...I thought to myself, “That sounds hard and annoying...but I think I can do it for the sake of science.”"

    scene ayanecantbone9
    with dissolve

    ay "Now? Now, I just want you to pin me down and fuck my brains out until I can’t even move anymore."
    s "Please don’t say things like that to me when I’ve been doing so well with this so far."

    scene ayanecantbone6
    with dissolve

    ay "But...Sensei! Think about it for a second..."
    ay "Why should we even have to do this in the first place? It doesn’t make any sense."
    s "It’s for Maya’s...theory or whatever."
    ay "Yes, I know that. But what would even be the point of proving that theory? "
    ay "Isn’t me finally showing up after...the bajillions of times you guys have done it a step in the {i}right{/i} direction? Won’t getting rid of me just send you backwards?"
    s "First off, I’ve only done it a handful of times. Maya’s the one who has reached  “bajillions” territory...possibly."
    ay "I’m fine with suffering for the sake of you being happy. I am. But-"
    s "I’m not asking you to {i}suffer,{/i} Ayane. In fact, I’m not the one asking you anything at all."
    ay "I know. You’d never ask me to do something like that. But the truth is that I {i}am.{/i} And I’m not just talking about the sex at this point even if that {i}is{/i} an admittedly huge part of it."

    scene ayanecantbone10
    with dissolve

    ay "I just..."
    ay "I can’t help but feel like if Maya is right and everything {i}does{/i} work out..."
    ay "That I’ll just go back to being excluded again..."
    s "..."

    scene ayanecantbone11
    with dissolve

    ay "Listen, uhh..."
    ay "Can we sit on the couch if I promise not to try and have sex with you? Doing things this way makes it feel too much like counseling and I kind of need you to feel like {i}you{/i} right now."
    s "Sure. But I’m blaming you if Imani yells at me for not finishing all of this grading stuff on time. "
    ay "I probably shouldn’t be encouraging this type of behavior when the school has already decided you needed a student teacher, but...grades should be the last of your priorities right now..."

    scene black
    with dissolve2

    "Ayane moves over to the couch and curls herself up into a ball, waiting for me to come join her as I slide the remainder of my “work” back into my desk."
    "I understand where these worries are coming from. Especially when, for the most part, she’s kept them bottled up ever since the three of us “respawned” in this very room."
    "But that’s what Ayane does. She keeps things to herself until she literally can’t anymore. "
    "And if she’s worried enough about this to actively seek me out...and shirk responsibilities she personally signed up for..."
    "Something must really be wrong."

    scene ayanecantbone12
    with dissolve2

    ay "Thank you. I needed this."
    ay "I’m sure it’ll sound stupid since it’s something you’ve been shouldering for a long time, but...I guess my shoulders aren’t as big as yours. Which means this whole thing has been really hard for me so far."

    scene ayanecantbone13
    with dissolve

    ay "And you’ve been great...really."
    ay "But...Maya, on the other hand..."
    s "Maya cares about you. "
    ay "Does she?"
    s "Uh...probably? I guess it’s hard to ever really know {i}anything{/i} with-"
    ay "If she cares about me, why is her top priority right now making sure I don’t get any closer to either one of you?"
    ay "If the whole pregnancy theory thing is true and I don’t get to come with you guys to the roof next time...won’t I just be...you know, reset? Why would she do that to me?"

    scene ayanecantbone14
    with dissolve

    s "That’s not {i}exactly{/i} how things work, I don’t think. "
    s "It seems that, so long as nothing happens to me, everyone keeps most of their memories. And only {i}some{/i} things wind up getting wiped away after Maya does...whatever it is she does."
    ay "But those are still {i}my{/i} memories. Memories I want to keep because they’re memories that brought me closer to you."
    ay "It shouldn’t be up to Maya to decide that I should just throw them away to put an end to a little bet that she has with herself. "
    s "If you’re so confident that her theory is wrong...it shouldn’t be a problem, though. Right?"

    scene ayanecantbone15
    with dissolve

    ay "I mean...kind of?"
    ay "I guess?..."
    ay "It’s less about the theory itself and more about what asking us to go through with it means."
    ay "I still think she’s wrong and I still think I’ll be able to stay with you guys, but I’m worried that she doesn’t {i}want{/i} me to. "
    ay "Like she...wants this weird, paranormal universe to be one for just the two of you. And that she’s so used to different versions of me getting discarded that I’m barely even a human to her anymore."
    ay "I wish...she wasn’t so hard to understand sometimes, you know?"
    s "Trust me. I know."

    scene ayanecantbone16
    with dissolve

    ay "So...what now, then? What else can we do while we wait for the next {i}thing{/i} to happen?"
    s "Just...wait, I guess. That’s all I normally do. "
    ay "No wonder you guys haven’t made any progress. There has to be, like...{i}something{/i} we can do to find out more about this, right?"
    s "Sure. It’s never too late to start studying chronokinetics. Act now and Wakana may even take you into her class. You’ll certainly have more luck with something like that there."
    ay "Sensei-"
    s "I don’t know what you want me to say, Ayane. "
    s "I get that you’re scared. And I’m here to...try and make you feel better in whatever sort of sexless way I can. "
    s "But, despite having experienced this more than you, I really don’t know that much. And I have no idea what we can do to find out more."
    s "If you have any ideas, I’ll be happy to indulge them. But right now, all we have is Maya’s...so I still think the best course of action is just figuring out if she’s right or not."
    ay "If she’s right, though...aren’t you worried that the current {i}me{/i} won’t come back?"
    ay "Or..."
    ay "Or will any old version of me do?..."
    s "What is that supposed to mean?"
    ay "Do you love me?...Or do you love {i}me?{/i}"
    s "That is...way too deep of a question for regular office hours."
    s "Besides, Maya finding out that she’s wrong about the one thing she thinks she knows more about than everyone could be a very humbling experience for her and, not gonna lie, I think she needs that."

    scene ayanecantbone17
    with dissolve

    ay "Fine. But just so you know, if I make it to that roof again after X months of not having sex with you and {i}don’t{/i} have my brain wiped, I am throwing myself at you with a level of aggression you have never seen before."
    s "I don’t think Maya will be very happy about that."
    ay "I honestly don’t care."
    s "I mean...yeah. If we manage to prove that’s not why you’re showing up, I’m not going to reject any of your advances."

    scene ayanecantbone18
    with dissolve

    ay "We?"
    ay "So...you’re on my side now?"
    s "There are sides? Is my life not already complicated enough having to fend off so many girls vying for my affection?"
    ay "Oh, please. As if you’re fighting any of them off. "
    ay "I’m not talking about an Ayane vs Maya, choose your heroine battle. I’m talking about whether or not you think getting me pregnant is the key to all of this world’s mysteries."
    s "I think that if it {i}is,{/i} I am going to be more confused than ever. So, sure. Go ahead and chalk that up to me being on your {i}side.{/i} "
    s "But I will not get sucked into whatever spat you and Maya start with one another. So please do not tell her I said that."

    scene ayanecantbone12
    with dissolve

    ay "I won’t. I don’t have any intention of starting any problems with Maya. I love her."
    ay "I just don’t want her trying to tackle this entire burden herself when she finally has a friend willing to take on some of it for her."
    ay "I have no idea what the future holds for any of us...and despite how confident I am, I can’t even guarantee {i}my{/i} short-term future anymore. "
    ay "And who knows? Maybe we never wind up learning anything."
    ay "Maybe this loop never breaks and we all wind up complacently conquering the end of the world together. Over and over and over and over..."

    scene ayanecantbone18
    with dissolve

    ay "But we’ll be doing it together. "
    ay "And none of us will ever have to feel...left out or..."

    scene ayanecantbone19
    with dissolve

    ay "Or like we’re the runner up ever again."
    s "..."
    ay "..."
    s "I do love {i}you,{/i} you know."

    scene ayanecantbone20
    with dissolve

    ay "Huh?"
    s "To answer your question from before."
    s "The {i}you{/i} you are now is the only Ayane Amamiya I care about. And if anything were to ever happen to {i}you,{/i} I doubt I’d be able to look at you the same."
    ay "Sensei..."
    s "But that doesn’t mean I wouldn’t still have sex with the other Ayanes. "
    ay "..."
    s "..."

    scene ayanecantbone21
    with dissolve

    ay "I can’t tell if I’m horny because of the way you just told me you loved me, the fact that we haven’t had sex in what feels like a whole year, or the idea of you having sex with my clones."
    s "Cloning you sounds fun. I don’t think I’d be able to handle more than three Ayanes at once, though."
    ay "I think I would also cut myself off at three Senseis."
    s "That sounds...painful."
    ay "That sounds {i}amazing.{/i}"
    s "..."
    ay "..."

    scene ayanecantbone22
    with dissolve

    ay "Okay! We should probably call it a day here since I know what you are thinking and you know what I am thinking."
    s "If Hell exists, this is it."

    scene ayanecantbone23
    with dissolve

    ay "Yes, Sensei."
    ay "Yes it is."

    scene black
    with dissolve2

    "Ayane leaves my office and..."
    "And I wind up heading over to the school restroom to {i}relieve{/i} myself before going home for the day."
    "Maya is lucky that I feel like my existence rests in the palms of her hands. Because otherwise, I would have gone against her wishes at least three times in the last hour."
    "One for every single Ayane clone I imagined having sex with as I was jerking off in the bathroom."

    $ renpy.end_replay()
    $ ayane_love += 1
    $ ayane_lust += 1
    $ ayanespecial40 = True
    stop music fadeout 7.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "{i}Ayane’s lust has increased to [ayane_lust]!{/i}"
    "{i}Too bad you can’t have sex with her!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label ayanesanabeach1:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
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
    if totaldays >= 530 and iospecial30 == True and karindate25 == True and day == 1 and tsukasaspecial1 == False:
        jump tsukasaspecial1
    if totaldays >= 535 and wakanadate15 == True and day == 5 and imanispecial1 == False:
        jump imanispecial1
    if totaldays >= 540 and imanispecial1 == True and day == 2 and ayanespecial40 == False:
        jump ayanespecial40
...
```