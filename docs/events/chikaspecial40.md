# In Search of Summer (Chika)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 424

* Event [Temporary Bliss](./kirindorm25.md) (Kirin) is completed)

* Day of week is Monday



## Next events

* [Chika: Self Care](./mall40.md)

## Event properties

* Id: chikaspecial40
* Group: Chika
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->chikaspecial40

## Official wiki page

[In Search of Summer](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chikaspecial40&go=Go) for more details.

## Event code

File: (install folder)\game\ChikaEvents.rpy

Code:
```python
...
label chikaspecial40:
    scene chikalunch1
    with dissolve
    play music "lifeismostlygood.mp3"

    "Okay. "
    "I’m tired of winter."
    "And I would very much like summer to come back now."
    "I wonder if Maya knows any way to sort of just...push up the date of the next reset and usher in another change of seasons or something."
    "The cold was nice at first- but even now, in the earliest stages of its death, I grow tired of its tomfoolery."
    "Desperate for a change of pace, I clutch my fists together and wait for Maya to conveniently appear before me."
    "Everyone knows that once I think of something like that, it almost always immediately happens. And I see no purpose in a reversal of fortune this early on a Monday morning."

    s "..."
    s "Any minute now."

    scene chikalunch2
    with dissolve

    c "Hey! Crazy seeing you here, Sensei."
    s "Hey, Maya. You got exponentially taller, tanner, and less weird since I last saw you."

    scene chikalunch3
    with dissolve

    c "Maya? Are you wandering around looking for her or something?"
    s "It’s more like I’m...wandering around in search of summer. And Maya is the only person I know with time manipulation powers."
    c "You know, I always thought there was something weird going on with her, but time manipulation was pretty low on my list."
    s "Well, now that you know, I’m excited for you to either forget all about it or just think I’m joking."

    scene chikalunch4
    with dissolve

    c "Oh, come on. If superpowers like that were real, Chinami would be like, flying around and killing dragons or whatever it is wizards actually do."
    s "Fantasy isn’t my favorite genre, so I'm not going to pretend to know much about it, but I’m pretty sure wizards don’t fly."

    scene chikalunch5
    with dissolve

    c "So, is this just what you’re doing for lunch? Walking around, fantasizing about Maya instead of your real girlfriend?"
    s "This is actually one of the very rare occasions where I’m {i}not{/i} fantasizing about something that would make you mad at me."

    scene chikalunch6
    with dissolve

    c "Wait, what is that supposed to mean?! How often are you fantasizing about stuff like that?!"
    s "Sorry, did I say stuff that would make you mad at me? I meant...fantasizing about the two of us on some sort of romantic getaway or...some other cute thing."

    scene chikalunch7
    with dissolve

    c "Aww~ You’re so sweet. This is why I love you."

    "Every day I spend with Chika is one day closer to realizing that she lives in a world of blissful ignorance, where only the things she {i}wants{/i} to hear manage to stick to whatever part of the brain stores memories."
    "Which is great for me, don’t get me wrong. But being that far into dreamland might be a little dangerous, especially when it comes time for her to leave."
    "She...has to realize eventually, doesn’t she? "
    "That even on the days where I want this to be anything more than it is, there’s another side of me buried somewhere in the back of my head mocking me for even pretending it’s real."
    "I just don’t want to be the one to force her into realizing that it’s not...and that this {i}relationship{/i} was all built on one huge misunderstanding."

    if bonus == True:
        "A misunderstanding that is, of course, my fault. And I’m an idiot for thinking that even a teenager as mature as Chika would think like an adult 100%% of the time."
        "But I really can’t just let this go on forever."

        c "Wanna go have sex in your office?"
    else:
        c "Wanna go hug in your office?"

    "A little longer wouldn’t hurt, though."

    s "Yes."

    scene chikalunch8
    with dissolve

    c "Too bad. I’m hungry."

    "I hate girls."

    scene chikalunch9
    with dissolve

    c "Hey, wanna come with me to the cafeteria? We can eat lunch together and no one will think it’s weird because you’re a teacher."
    s "I think me doing things like this is exactly why there are so many rumors apparently spreading about me."
    c "Yeah, but those are just rumors. Rumors are {i}always{/i} going to exist, Sensei."
    c "Like that one about you dating Niki Nakayama. Like, obviously that never actually happened, but people are still saying it."
    s "That did actually happen, though."
    c "Hahah~! Sure it did, Sensei."
    s "Before I offer to call her and prove you wrong, will you tell me why you don’t think it’s true? Am I not cool enough to date an idol?"
    c "I think you’re the coolest guy in the world. And one of the hottest, too."
    s "One of?"
    c "Idols are on another level, though. Especially ones like Niki. They don’t date {i}anyone{/i} because they belong to all of us."

    "Boy, do I have bad news for her."

    s "This was before she became an idol, though."
    c "Well, she wasn’t {i}Niki{/i} before she became an idol. She was just Niki."
    s "Oh, okay. My mistake. I didn’t realize she was possessed by the soul of music."

    scene chikalunch10
    with dissolve

    c "Well, I’m glad I got to be the one to educate {i}you{/i} for once. "

    if bonus == True:
        s "When have I ever educated-"

    c "Now, come with me to the cafeteria and eat lunch with me like the awesome, loving, loyal boyfriend you are."
    s "..."
    c "..."
    s "You know, I’m not really feeling that hungry today."

    scene chikalunch2
    with dissolve

    c "Well, I am. So that sucks for you."
    s "I’m sorry?"
    c "Because you’re coming with me whether you like it or not."
    s "I don’t think this is how relationships are supposed to work."
    c "It’s exactly how they’re supposed to work. Besides, it’s not like anybody is going to come up to us and tell us to like, not eat together or something."
    c "We’re not doing anything wrong. We’re just...making the most of our lunch period since we’re not {i}always{/i} able to spend time together, you know?"
    s "..."
    c "..."

    "I...guess this could be a good time to talk to her about this whole “dating” thing?"
    "Especially now that she’s trying to act like we’re dating {i}in{/i}[school], which is exactly what I wanted to avoid at all costs."
    "And something I thought she’d care a little more about avoiding too, but...it is what it is."

    s "Fine."
    s "But I’m not paying for your food since I’m already paying for your phone bill."
    c "Yeah, yeah. I can buy my own food. I’m a big girl."

    scene black
    with dissolve2

    "Chika tries to grab my hand to lead me down the hall, but I am able to dodge her grasp and inform her that holding hands is a little too much."
    "And by a little, I mean a lot."
    "It’s not like we’re in the lobby of a hotel or a private onsen or anything like that. There are people here."
    "There are times when it’s okay to be clingy and times when it’s not."
    "And while the two of us are fully clothed and out in the open, I’d say the current status of acceptability is far closer to {i}not.{/i}"
    "........."
    "......"
    "..."

    scene chikalunch11
    with dissolve2

    "So, the good thing is that the cafeteria is mostly empty today."
    "The bad thing is that a few of the people who {i}are{/i} here are people that I know. "
    "No one “dangerous” like Ami or Noriko or...anyone else who would get mad at me for sitting with a girl who isn’t them."
    "But there's Yasu, Touka, that one new teacher, and Io- all the way back in the corner of the room, doing her best to assume the role of a socially anxious wallflower."
    "And, even though I can’t see her from where I’m sitting, I’m sure she’s thinking something along the lines of, “Oh, good. They’re still {i}together,{/i}” while, unbeknownst to everyone but me, we’re not."

    c "You sure you’re not hungry? Because I probably won’t finish all of this and you can have whatever’s left of it."
    s "I’m okay. Ami made a big breakfast this morning."
    s "But, Ami makes a big breakfast pretty much every morning, so that’s nothing to really write home about."

    scene chikalunch12
    with dissolve

    c "Yeah...that’s actually super impressive. Like, doesn’t she leave the dorms really early every morning just so she can go home and cook for you? That’s some serious dedication."
    s "Yeah, but I let her live in my house for free, so there’s that too."

    if bonus == True:
        c "Aren’t you also her legal guardian?"
        s "I prefer the term “uncle.”"
        c "..."
        c "Okay, but aren’t you like, {i}legally{/i} her legal guardian?"
    else:
        c "I mean, she does your taxes though, doesn't she?"
        s "I sure hope so. I've yet to see any copies of my returns."
        c "You should let Chinami try doing your taxes next time. She's getting really good at-"

    s "You’re sure talking a lot for someone who was very hungry just a moment ago."

    scene chikalunch13
    with dissolve

    c "All I’m saying is that she...really goes out of her way for you."
    c "It kinda makes me a little jealous."
    c "Like...{i}I{/i} want to cook breakfast for you and like, help out around your house and stuff."
    s "One key difference between you and Ami is that Ami doesn’t have to also take care of a kid. Just me."
    s "Though, I guess there {i}is{/i} Ayane sometimes, and she can be a bit of a handful."

    scene chikalunch14
    with dissolve

    c "Your house sounds really...lively."
    s "Sometimes, yeah. Most of the time, it’s just me and her, though."
    c "..."
    c "I really hate to ask like this...but..."
    c "When I’m like, out of [high_school] and stuff..."
    c "Do you think there’s any chance that maybe Chinami and I could move in with you?"
    c "Like, you won’t have to hide how we’re seeing each other anymore once I’m not a student, and it would definitely help me out since I wouldn’t have to worry about rent anymore."
    s "What about Yumi? Where will she go?"

    scene chikalunch15
    with dissolve

    c "I don’t know. I’m sure she doesn’t expect me to take care of her forever, though. Like...she’s going to {i}have{/i} to find something to do on her own."
    c "And it’s not like I’m going to ask you if she can just come live with us as well when you haven’t even agreed to my sister and me coming yet."
    s "I’d...have to run it by Ami."

    if bonus == True:
        c "Is Ami not leaving for college once she’s out of high school? Is all of that stuff she says about just devoting her entire life to you really true?"
        c "Or do you think maybe she’s just saying that for now and...she’ll change her mind once it’s time to start like, growing up?"
    else:
        c "What if she gets hit by a bus sometime over the next three years? I've been thinking a lot about that recently."

    s "I think that you probably shouldn’t think too much about things that will be happening three years from now when we don’t even know what’s going to happen tomorrow."

    scene chikalunch16
    with dissolve

    c "Yeah? Are you gonna run off with my favorite idol and forget all about me?"
    c "Cause I wouldn’t really blame you. There’s no way I could compete with her."
    s "At the risk of shattering your borderline inhuman expectations of Niki, I’m going to tell you now that she’s probably...not what you think she is."
    c "Yeah, because I’m sure you know her {i}so{/i}, so well."
    s "Well, considering that {i}she is my ex-girlfriend{/i} I think it’s safe to say I know her at least a {i}little{/i} well."

    "Just...only the tsundere parts. Not the ones Niki so desperately wants me to remember."

    scene chikalunch17
    with dissolve

    c "Sensei, I’m not going to believe that! Are you and Noriko working together to spread this rumor or something?"
    c "Because if I believe this one, I’ll have to start believing the ones about how you’re secretly seeing like half of our class. Or how you and Maya-"

    scene chikalunch18
    with dissolve

    c "Wait, weren’t you looking for Maya when I bumped into you in the hall?"
    s "Nope. But back to the topic of Niki, we really did date in high school."

    scene chikalunch19
    with dissolve

    c "Yeah, okay. I mean, I obviously don’t have a problem with it, but aren’t you in your thirties? How would you have dated Niki in high school if she’s like, ten years younger than you?"
    s "Chika, just out of curiosity, how old do you think Niki is?"

    scene chikalunch20
    with dissolve

    c "She’s 22 and her birthday is March 3rd. Her favorite color is pink (Shocker, I know) and if she could live anywhere in the world, it would be Hawaii."
    s "And where did you get that information?"
    c "Fan books...online...interviews. The info is all over the place, Sensei. At least do your research before trying to make me think you dated my role model."

    "Well, if nothing else, Niki was certainly right about the idol industry being ruthless and cutthroat. "
    "I’ll have to add this newfound revelation to the exposé I’m writing."

    s "Chika, Niki is 29 years old. Only a couple years younger than me."

    scene chikalunch21
    with dissolve

    c "Oh, please. She’s 29 and she still looks like {i}that?{/i} Funny joke, Sensei."

    scene chikalunch22
    with dissolve

    if bonus == True:
        c "Besides, if I ever found out that my lips have been on the same penis as Niki's, I’d probably bite it off out of excitement."
    else:
        c "Besides, if I ever found out that I hugged someone Niki hugged, I’d probably just kill myself right there since life couldn't possibly get any better."

    s "..."
    c "..."

    scene chikalunch23
    with dissolve

    c "Sensei, come on! I’m obviously joking! "

    if bonus == True:
        s "Chika, there are certain things in life that you really just shouldn’t joke about...and biting someone’s penis off is one of them."
        c "Don’t worry. I like your penis too much to bite it off."
        s "I am very relieved to hear that. Now, if only you’d stop acting like that during the day at school."
    else:
        s "Chika, there are certain things in life that really just shouldn’t joke about...and suicide is one of them."
        c "Don't worry. I would never {i}actually{/i} do something like that."
        s "Good. Also, stop liking me so much in public. It makes me feel weird."

    scene chikalunch24
    with dissolve

    c "What do you mean?"
    s "Just that {i}this{/i} was supposed to be a little more secretive than eating lunch together and trying to hold my hand in the hallway."
    c "Well, gee. Sorry for being in love with you. I don’t really see what the big deal is."
    s "The “big deal” is that you could get me in trouble."
    s "You could get {i}both{/i} of us in trouble."
    s "And if you’re not going to respect that-"

    scene chikalunch25
    stop music

    c "Wait....Are you breaking up with me?..."
    s "Woah, hold on a second."
    c "Why?"
    c "What did I do wrong? "
    c "Is..."
    c "Is this because I asked to move in with you after [high_school]?"

    scene chikalunch26
    with dissolve

    c "You can say no! I didn’t mean to move so fast!"
    c "Oh god, no. I really wasn't trying to-"
    s "Chika, calm down."

    scene chikalunch27
    with dissolve

    c "..."
    c "I'm sorry. "
    c "I just thought that you were about to give me like...an ultimatum or whatever..."
    c "Then it clicked that I just asked about moving and..."
    s "..."
    c "..."
    c "Are we okay?..."
    s "We won’t be if you don’t stop crying."
    s "People are going to start thinking something is going on which, need I remind you, is exactly what I’m trying to avoid."
    s "But we can forget about that for now..."
    s "You still haven’t eaten. Your food is going to get cold."

    scene chikalunch28
    with dissolve

    c "..."
    c "Yeah."
    c "I’m...suddenly not very hungry anymore..."

    scene black
    with dissolve2

    "The rest of the lunch period goes by in mostly silence as I realize how foolish I was for even {i}thinking{/i} that now would be a good time to tell Chika to tone it down."
    "And, at this point, I’ll be lucky if {i}any{/i} time winds up being a good time to tell her that."
    "The worst part is that I want to blame {i}her{/i} for all of it."
    "I want to blame her for misunderstanding what I wanted out of our time together...and painting me into a portrait of the family she’s always wanted."
    "I’m the one who handed her the brush, though. And blaming her for using it just makes me question why I ever gave it to her in the first place."
    "She loves that portrait so much, though. So how am I supposed to tell her I hate it?"
    "It doesn’t matter now, I guess."
    "I’ll just keep putting it off."
    "The same way I've been doing from the start."
    "But, hey. At least on the bright side-"
    "I’m one day closer to summer."

    $ renpy.end_replay()
    $ chika_love += 1
    $ chikaspecial40 = True

    "{i}Chika’s affection has increased to [chika_love]!{/i}"
    "........."
    "......"
    "..."

    jump afterschoolevent

label mall40:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
jump day128
    if totaldays >= 138 and day103 == True and day130 == True and day85 == True and day138 == False:
        jump day138
    if totaldays >= 139 and chika_lust >= 5 and chikadorm20 == True and mall20 == True and chikadetention == True and day139 == False or chikadorm20 == True and mall20 == True and chika_lust >= 10 and day139 == False:
        jump day139
    if totaldays >= 140 and day138 == True and day140 == False:
        jump day140
    if totaldays >= 142 and amidorm15 == True and day140 == True and day142 == False:
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
...
```