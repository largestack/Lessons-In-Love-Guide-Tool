# No Strings Attached (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 535

* Event [Pseudonym](./wakanadate15.md) (Wakana) is completed)

* Day of week is Friday



## Next events

* [Ayane: Chronokinetics](./ayanespecial40.md)
* [Sana: Black Sandy Beaches](./bar55.md)
* [Rin: Disaster Lesbian](./rindorm55.md)

## Event properties

* Id: imanispecial1
* Group: Main
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->imanispecial1

## Official wiki page

[No Strings Attached](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=imanispecial1&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label imanispecial1:
    scene hangoutsesh1
    with fade
    play music "phantomthief.mp3"
    play sound "knock.mp3"

    ima "Senpai! It’s me! Imani! Your bubbly and lovable assistant! "
    s "Why are you yelling? And why are you on the other side of the door?"
    ima "I have a proposal for you!"
    s "You want to get married?"
    ima "One day, sure! But I’d appreciate it if you’d let me tell you my idea first before we make any rash decisions!"
    s "Imani, just open the door."

    play sound "dooropen.mp3"
    scene hangoutsesh2
    with dissolve

    ima "Thank you, Senpai. I think my yelling was starting to give Wakana a migraine."
    w "Waking up gives me a migraine. As does talking. And walking. And pretty much everything else now that I’m approaching 30."
    s "Is Wakana in on this “proposal” as well? Or is this just an “us” thing?"

    scene hangoutsesh3
    with dissolve

    ima "Hah...Senpai, can’t you ever be happy with me alone? "
    ima "Just once, I would like a night where the two of us can really let ourselves loose {i}without{/i} you enlisting the help of another girl. It really hurts my self-esteem when you do things like that, you know."
    ima "But there you go again- cornering me with your insatiable desires the same way you always do."
    w "You too?"

    scene hangoutsesh4
    with dissolve

    ima "Wait, what?"
    w "When did your interest shift from students to teachers, Arakawa? If something monumental happened in your life, it’s only right that you share it with your closest, most trusted associates."
    s "I...didn’t mean for that to happen."

    scene hangoutsesh5
    with dissolve

    ima "Mean for what to happen?! How come nobody ever talks to me?!"
    w "Because you’re loud. Now, out with your “proposal.” Which should technically be a “proposition,” but still."

    scene hangoutsesh6
    with dissolve

    ima "Fine! But only because doing so will open the door for you two to tell me {i}later{/i} when we are all tipsy and have to hold ourselves back from kissing each other."
    s "Whatever it is, I’m in."

    scene hangoutsesh7
    with dissolve

    ima "Hell yeah! That’s the pervert I know and love!"
    w "What you two do on your own time is in no way tied to me. I agree to the former of those two ideas and have no problem going out to drink, but I will be kissing {i}no one{/i} until my partner arrives."

    scene hangoutsesh8
    with dissolve

    ima "Can we watch once she does?"
    w "You? Maybe. Arakawa? No. He has a bad track record."
    ima "Seriously, what happened with you two?"
    s "Are we going to a bar or something? Is that what’s going on?"

    scene hangoutsesh9
    with dissolve

    w "I believe that is Imani’s plan, yes."
    ima "Us three and Wakana’s woman. I think she’s gonna be a little late because of work, though. You in?"
    s "Wouldn’t that technically make this a double date?"
    ima "Depends on where our pants end up, I guess."
    w "How nostalgic. It wasn’t all that long ago that we had our first double date, Arakawa. You and that...peculiar girl...Makinami, was it?"

    scene hangoutsesh10
    with dissolve

    ima "You went on a date with Maya?! But I thought you were supposed to marry Noriko?! Those two hate each other! What will the tabloids say?!"
    s "Wakana, you’re creating a lot of problems for me today by just existing. "
    w "I am, aren’t I? It’s actually quite fun."
    s "Well, whatever. Sure. I’ll go. "

    scene hangoutsesh11
    with dissolve

    ima "Great! But, just so we’re all in the clear, don’t go bringing Maya or Noriko or any other girl who isn’t legally allowed to drink. This is a getaway for us adults to celebrate another successful week of..."
    ima "Well, being adults. That shit is hard, yo."
    ima "You cool to meet us there in like...two hours, Senpai? Torn between Sakaki-bar-a and this new place we found on the outskirts of the old district."
    s "I choose the second place."
    ima "Reason being?"
    s "The owner of that place doesn’t want to marry me."
    ima "Fair enough!"

    scene black
    with dissolve2
    play sound "dooropen.mp3"
    stop music fadeout 25.0

    ima "Come on, Wakana! We can go relax at the spa until Senpai is done giving himself calluses from all that paperwork he has to do while we wait for Makoto to come back!"
    w "You can go on ahead and I’ll meet you there when the time comes. I’m not much of a spa person."
    ima "Tch. No wonder if you’ve got those bags beneath your eyes. You really need to lighten up, girl."
    ima "Come on! I’ll-"
    w "Touch me and I will make a necklace out of your skull."

    "Imani and Wakana exit the office and...I guess I have plans to go out with them tonight."
    "As I lean back in my chair and take in this thought like a breath of fresh air, I realize how far I’ve come. "
    "If you’d have told me several apocalypses ago that I’d be one day going out for drinks with friends from work, I-"
    "Well I probably wouldn’t have answered you at all because I’d be too busy having sex with Ayane or something."
    "But now, I {i}can’t{/i} have sex with Ayane. And I {i}can{/i} go out for drinks with friends from work."
    "And that’s..."
    "I think that’s..."
    "Good for me?"
    "........."
    "......"
    "..."

    scene hangoutsesh12
    with dissolve2
    play music "10c.mp3"

    ima "...and that’s exactly why I think Sensei’s approach to teaching isn’t {i}entirely{/i} bad! Just a little unorthodox! And I can’t imagine it being officially endorsed by anyone any time soon."
    w "You’ve corrupted her, Arakawa. This young, aspiring educator is now sticking up for you when all you do is ruin the lives of everyone you encounter."
    ima "Hey, my life isn’t that bad! Thanks to Sensei’s shortcomings, I now have a stable job and was able to put a down payment on a new apartment the other day! I really owe a lot to him."
    w "Did you hear that, Arakawa? Your shortcomings helped Imani move out of the spa. I think you might finally be due for an AATJ award."
    s "I don’t even know what that is."
    w "Why am I not surprised?"

    scene hangoutsesh13
    with dissolve

    ima "For real, though. I think we make a good team, Senpai. I do all the actual teaching, and you just hang around and motivate all of the girls by being handsome and whatnot. It’s working pretty well."
    w "I also think you two go well together. But that’s only because you’re both so obnoxious that you seem to almost cancel each other out."
    s "I think our double date is officially a success. Wakana has formally endorsed us as a couple."
    ima "Speaking of which, when’s Osako going to show up? Wasn’t she supposed to be out by now?"

    scene hangoutsesh14
    with dissolve

    w "She’ll get here when she gets here. The way business fluctuates at that cafe would make you think it’s situated inside of a subway station."
    w "But, please. Don’t let the absence of my partner dissuade you two from incessantly flirting with one another. "
    w "Just know, Imani, that you may be pushed against a wall at any given moment."

    scene hangoutsesh15
    with dissolve

    s "Hah..."
    ima "Is {i}that{/i} what happened with you guys? Senpai tried to make a move? Got a little too handsy?"
    w "A momentary lapse in judgement, I suppose. I apparently have that effect on people."
    w "I still have no clue why Osako was so smitten by me, so it’s plausible that Arakawa caught the same bug and now can no longer look at me without wanting to take me into his arms."
    s "That’s...not what happened."

    scene hangoutsesh16
    with dissolve

    w "Relax. I’m only kidding."
    w "One more strike and you’re out, though. I can only forgive you so many times before I’m forced to rethink some of the decisions I’ve made."
    s "I’m assuming the first strike was the hospital?"
    w "I will never let you live that down."
    ima "Hospital? That’s when...I was first hired, right? To cover for you?"

    scene hangoutsesh17
    with dissolve

    w "Why are you asking me? I was unconscious the majority of the time. "
    ima "You’re cool now, though...right? No terminal illnesses I have to worry about or anything?"
    w "Not unless one of the two parasites accompanying me at this table tonight decides to infect me."
    ima "I’ve got no plans to infect you. Not sure about Senpai, though- since he apparently can’t hold himself back anymore."
    s "I’m just going to wait until this slandering of my name is done to jump back into the conversation. "
    w "Is it really slander if it’s the truth?"
    s "I’d answer, but I’m still not done waiting."

    scene hangoutsesh18
    with dissolve

    ima "Then, for the sake of including Senpai again, how about we play a game?! "
    ima "It’s the first of many times we’ll all be hanging out after work, so we should probably start some kinda...fun tradition. Right? And what's more fun than a cool, adult game?!"
    w "I don’t know if I have the energy to do this as often as you want to."
    ima "Then how about once a week? On...Fridays or something. We don’t have to {i}always{/i} go, but it’d be cool if there was a place we could all meet up. "
    ima "Just...something to look forward to, you know?"
    s "Works for me. Can’t guarantee I’ll always be here, but I’ll keep it in mind."
    w "I suppose I’m in the same boat as Arakawa. I’m still on the fence about this “game” though. Drinking games aren’t exactly my cup of tea."

    scene hangoutsesh19
    with dissolve

    s "You’ve had like thirteen beers already."
    w "Either I am very drunk or you are very bad at counting, as I only see five."
    ima "It doesn’t have to be a drinking game. How about something we can play to...get to know each other a little better? Like twenty questions? Two truths and a lie? Truth or dare? Any of that shit?"

    scene hangoutsesh20
    with dissolve

    w "That sounds exhausting."
    s "I’ll do whatever. I don’t really care."
    ima "Wow. You two are real party animals, aren’t you?"
    w "This may come as a bit of a shock, but I’m actually not."
    s "I can party."

    scene hangoutsesh21
    with dissolve

    ima "Spoken like the true table elder, Senpai. Just what am I going to do with you?"
    s "I didn’t realize I was yours to use."
    ima "Well, it’s no fair if you only get to use {i}me{/i} all the time. I want to have a little fun too, you know? "
    w "Leave it to a man to only care about pleasuring himself. This is why I’m dating a woman."

    scene hangoutsesh22
    with dissolve

    s "Oh no. I’m suddenly busy on every Friday for the indefinite future. How disappointing."
    ima "You know what we need? Another person less like you guys and more like me! Another shepherd to herd you lazy sheep and whip you into social mode!"
    w "I’m typically the one who does the whipping, but I see where you’re coming from."
    w "I’ll call Osako and see how long it will be until she’s here, but-"
    ima "Screw Osako!"
    w "I do. Quite frequently, at that. "
    ima "Not what I meant! Every second of every day, we come closer to death’s door! We need to savor this time, Wakana! We can’t just spend our whole lives waiting for the next thing to happen!"
    ima "Sometimes, what we need to do is make things happen ourselves!"
    s "I feel another proposal coming on."
    ima "We need adventure!"
    ima "We need excitement!"

    scene hangoutsesh23
    with fade

    ima "We need that hottie over there with all of the tattoos to join our friend group!"
    w "You are too outgoing and it makes me uncomfortable."
    w "I suppose every group needs its extrovert, though."
    s "I concur that, from here, she looks very attractive. But I don’t think you can just walk up to someone and-"

    scene hangoutsesh24
    with dissolve

    ima "Hi!"
    s "Welp, there she goes."
    q "Great. Now my beer is talking to me. Just what I needed."
    ima "Not beer! A real, live human. Typically non-alcoholic, but I will admit that I have had a few to drink tonight."

    scene hangoutsesh25
    with dissolve

    q "Huh?..."
    q "You’re talking to me, right? Not the beer?"
    ima "Something wrong? Seem a little down in the dumps."

    scene hangoutsesh26
    with dissolve

    q "My life is over."
    ima "Well, it doesn’t have to be. Does it?"
    q "I’m not good at riddles. Just tell me what you want and I’ll pretend to know what you’re talking about."
    ima "My friends at that table over there and I were just about to play a little game, but it wouldn’t be as fun without a fourth player. So I was wondering if you’d maybe want to join us?"

    scene hangoutsesh27
    with dissolve

    q "Join you? Are you sure?"
    ima "Do you not want to?"
    q "I...have no clue who you even are. And I’m also caught in a cycle where I break into tears every five minutes. So unless your game involves crying, I should probably stay over here."
    ima "{i}I{/i} think you should come with me. I could {i}really{/i} use a partner, you know."
    q "I’m not very good at trivia."
    ima "Just get off the stool and follow me, damn it. It’s painful seeing you all alone over here."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene hangoutsesh28
    with dissolve2

    ima "There we go! One order of adventure and excitement delivered, courtesy of Imani Imai. You can thank me later once she’s a vital part of our team."
    w "I feel like a puppy just dropped a toy at my feet and expects me to...play with it or something."
    ima "That is what you are supposed to do with puppies, I guess."
    q "I had a dog once. "
    q "He was murdered."

    scene hangoutsesh29
    with dissolve

    w "Ahh, yes. I can feel the excitement already. "
    ima "Uhh...maybe lay back on some of the puppy murder and...start by introducing yourself? I’m Imani, the tired one is Wakana- {i}not{/i} terminally ill, by the way. And the man is just Senpai. "
    ima "Or...Sensei to most people."
    q "Do you teach karate?"
    s "..."
    s "No?"
    q "Fuck. Sorry."
    q "I like to guess people’s jobs the first time I meet them and you gave me karate vibes. "
    w "My girlfriend teaches karate. Perhaps you smelled it lingering on my clothes?"

    scene hangoutsesh30
    with dissolve

    q "WAAAAAAAAAAAAAHHHHHH!!!!!!!"
    s "I think your new friend is broken, Imani."
    ima "Hey, hey, hey. Don’t cry yet! You haven’t even told us your name. How are we supposed to cheer you up if we don’t even know that?"

    scene hangoutsesh31
    with dissolve

    q "I’m sorry. It’s been five minutes. "
    w "It’s been what?"
    ima "Part of the cycle, Wakana. Come on. Leave whatsername alone."

    scene hangoutsesh32
    with dissolve

    ri "It’s Rika. Nice to meet all of you and sorry for crying within the first five things I said. "
    ima "Welcome to the table. We’ll be here every Friday from now on. Well, unless we’re not."
    ri "Are you part of a...club or something?"
    ima "We’re all teachers, actually. This is our new after-work ritual."

    scene hangoutsesh33
    with dissolve

    ri "That’s awesome! I’m glad it’s something like that and not karate. I know a lot more about teachers than I know about karate people."
    s "I still think she’s broken."
    w "I’m with Arakawa on this. Even if he secretly loves me."

    scene hangoutsesh30
    with hpunch

    ri "AAAAAAAAAAHHHHHHHHHHHHHHHHH!!!!!!!"
    ima "Rika. Bad. Stop it."

    scene hangoutsesh31
    with dissolve

    ri "The times between my tears are getting shorter! That was nowhere near five minutes!"
    ima "There there, new buddy. We’ll get your mind off of whatever it is that’s plaguing you in just a sec."

    scene hangoutsesh32
    with dissolve

    ri "Sorry again. I suck."
    ri "I think I’m good for now, though. I’m pretty sure I’ve run out of tears."
    w "If you’re lucky, they’ll never come back. That happened to me one day and I haven’t ever cried since. I suppose I don’t feel much of anything anymore, though."
    ri "Did you...used to cry a lot or something? Is that why your eyes look like that?"

    scene hangoutsesh34
    with dissolve

    ima "That’s just how they look. It’s not really the result of any one thing, I don’t think."
    ri "Huh. Weird. But also kind of cool. You’re like a...hot zombie or something."
    w "Thank you. That’s exactly the type of look I’m going for."
    ima "So, Rika- we were torn between three games. Twenty-"
    ri "I want to play Yahtzee."
    ima "..."
    ima "Twenty questions, truth or dare, or two truths and lie. None of which are Yahtzee."
    ri "I guess...if I had to choose out of those three...truth or dare?"

    scene hangoutsesh35
    with dissolve

    ima "Then it is settled! Our newest friend has chosen the game we will play! And so we will start with her!"
    ima "Rika, select any one of us and force us to confront our fate!"
    ri "Then, uhh..."
    ri "Wakana. Truth or dare?"
    w "Truth, I suppose."
    ri "If you and your girlfriend ever got into a fight and you knew that you were in the wrong but you loved her anyway and wanted her to stay and were sorry for what you did, what would you do to get her back?"
    ri "Also, what would you do when that plan fails? Not just once but three times. And also, how would you hide that from your daughter? Oh, and-"
    w "I am no expert at this game, but I believe that it’s only supposed to be one question."

    scene hangoutsesh36
    with dissolve

    ri "Then...just the first part I guess."
    w "Hmm..."
    w "I suppose I’d just be honest with her."
    w "I believe that if two people are meant to be, they’ll be able to work through their differences and-"
    ri "It’s coming. I can feel it."
    ima "Hold it in, Rika. Hold it in."
    ri "{size=-15}Please........proceed......{/size}"
    w "I’m...not sure if I want to anymore."

    scene hangoutsesh37
    with dissolve

    ima "Then I guess Rika’s turn is over! Wakana, you go!"
    w "Arakawa. Truth or-"
    s "Dare."

    scene hangoutsesh38
    with dissolve

    w "No hesitation at all. Bold."
    s "I’m more afraid of what you’d ask me to tell the truth about than whatever you’ll dare me to do."
    w "In that case..."
    w "I dare you to submit something for the school’s poetry contest. Under a pseudonym of course."
    s "You can dare me to do literally anything...and that’s what you choose?"
    w "It’s what I want."
    s "But why?"
    w "Sorry, is it your turn now? Because I don’t think you have the right to be asking me for truths when there is a process we must abide by."
    s "Fine. Since it’s my turn now, truth or-"
    w "Dare."
    s "Fuck."
    w "You’re an idiot if you didn’t see that coming."
    ima "It’s so cute when they fight, isn’t it?"
    s "I dare you to never say anything mean to me ever again."
    w "Wow. That wasn’t sexual at all. I’m surprised."
    s "I’ve learned my lesson."
    w "Will the rest of the night suffice? I think I may be able to manage that much. The rest of eternity? Absolutely not. I enjoy insulting you far too much."
    s "Fine. But only if you say one nice thing about me right now."
    w "Here are two. I value your friendship and I’m proud that you seem to have taken our previous {i}run-in{/i} to heart in not demanding anything perverse out of me."

    scene hangoutsesh39
    with fade

    w "That said, I would like to use my next turn to dare Imani to make out with Rika."

    scene hangoutsesh40
    with dissolve

    ima "Bro! You didn’t even give me the chance to choose!"
    w "Fine. Imani, truth or dare."

    scene hangoutsesh41
    with dissolve

    ima "..."
    ri "..."
    s "I’m going to count this as a third nice thing you’re doing for me tonight, Wakana."
    w "Arakawa, I am doing this for {i}myself.{/i}"
    w "Please never forget that beneath my broody exterior, I am in a {i}very{/i} sexually active relationship with a woman I adore."
    w "Also, alcohol has certain adverse effects on me and I believe our new “friend” may need this."
    ima "Uhh..."
    ri "..."
    ima "..."
    ima "........"
    ri "........"
    ima "..................................."
    ri "..................................."
    w "Jesus Christ, Imani. Weren’t you just ranting a short while ago about how we’re wasting away our lives due to inactivity?"

    scene hangoutsesh42
    with dissolve

    ima "Well, yeah! But that was before you dared me to make out with a girl I just met!"
    ima "Also, I was kind of hoping Rika would give me some sort of cue instead of just blankly staring at me!"
    ri "I’d make out with you."

    scene hangoutsesh43
    with dissolve

    ima "Oh. Then fuck yeah, dare."

    scene hangoutsesh44
    with dissolve

    ima "Mn~"
    ima "Mmf.......mnn!"
    s "Wow."

    scene hangoutsesh45
    with fade

    w "I lied. I am an expert at this game. Osako and I played constantly in college...though, always alone."
    s "That just sounds sad."
    w "It’s how I learned she likes being handcuffed."
    s "I have never been more thankful for someone else’s college experience."
    w "I wouldn’t be {i}too{/i} thankful. If Rika hadn’t shown up, I was going to dare Imani to kiss {i}you.{/i}"
    w "How lucky I am to be given an alternative more in line with my “tastes.”"
    s "..."
    w "..."
    ima "Mmf!~"
    ima "Mm......mnhh!"
    ima "....pah~"

    scene hangoutsesh46
    with fade

    ima "Oh, she’s {i}good.{/i} Thanks for that, Wakana."
    ri "You were okay. 6/10. Too much tongue."

    scene hangoutsesh47
    with dissolve

    ima "Yo, what the fuck?!"
    ri "Wakana, truth or dare!"

    scene hangoutsesh48
    with fade

    w "I suppose it’s only fair if I take a dare this time after hurting Imani’s pride like that."
    ima "6/10?! That's it?!"
    w "Poor girl. I could tell from here."
    ima "This is why I don’t date girls! They’re too picky!"
    ri "Okay, okay. Leave Imani alone. She tried."
    ima "{i}Tried?!{/i}"
    ri "Wakana, I dare you to make out with Sensei now!"

    scene hangoutsesh49
    with dissolve

    w "Uhh...no."
    ima "Wakana’s got a girlfriend, remember?"
    ri "Oooooh. Oh, right...Yeah, I forgot about that."
    ri "I still kind of want to see it, though."
    ima "I’d offer to take her place but now I’m just self-conscious."
    ri "It wouldn’t be the same, though. Can’t you like, feel the tension?"
    w "There is no {i}tension.{/i} What you’re likely sensing is the residual excitement that comes from watching two women kiss."
    ri "It’s just a game, though! Right?"
    ri "Like...you two can kiss with no strings attached and it’ll be totally cool cause, like...some random girl made you do it."

    scene hangoutsesh50
    with dissolve

    w "..."
    s "..."
    w "Are you going to say something or am I going to be the only one to refute this?"
    s "I mean...it {i}is{/i} just a game. I know you don’t actually feel anything for me."
    w "Wow, what could have given you that idea?"
    ri "Are we all in agreement to never tell Wakana’s girlfriend about this? Not like I’d...even be able to tell her when I have no idea what she even looks like in the first place, though."
    ima "I mean...{i}my{/i} lips are sealed. I wouldn’t want Wakana to get in trouble."

    scene hangoutsesh51
    with dissolve

    w "Is it too late to say choose “truth” instead?"
    ri "A dare’s a dare, Wakana. Don’t just dish it out if you can’t take it."
    w "Is there some form of penalty I can take instead, then?"
    w "Because that’s something I..."
    w "Just can’t..."

    $ renpy.end_replay()
    $ imanispecial1 = True

    jump wakanaspecial15

label bucketscene:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
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
    if totaldays >= 530 and iospecial30 == True and karindate25 == True and day == 1 and tsukasaspecial1 == False:
        jump tsukasaspecial1
    if totaldays >= 535 and wakanadate15 == True and day == 5 and imanispecial1 == False:
        jump imanispecial1
...
```