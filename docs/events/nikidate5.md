# Like it's Any Other Day
Niki event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nikidate5&go=Go)



## Event preconditions
✅Niki love greater than or equal to 5

✅Event "[Rin: Semantics](./rindorm40.md)" is completed (event=rindorm40)

✅Event "[Niki: Cotton Candy](./nikidate1.md)" is completed (event=nikidate1)

✅nikinumber equal to True (unknown variable)



## Next events
* [Maya: A Place That Can Only Exist in Our Minds](./mayadorm35.md)
* [Sara: Uptown Girl](./saradate10.md)
* [Main: Annabel Lee](./day280.md)

## Event properties
* ID: nikidate5
* Group: Niki
* Triggered by label: callnikinight
* Triggered by branch label: callnight

## Event code
File: \game\NikiEvents.rpy
Code:
```python
...
label nikidate5:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer. "
    "Given that it’s her actual number this time and I won’t need to go through a third party in order to talk to her, I’m feeling a bit optimistic."
    "I mean, I’ve grown pretty accustomed to never being turned down to begin with, but if it was ever going to happen, it was going to be because of that manager of hers."

    play sound "phonebeep.wav"
    play music "love.mp3" fadein 15.0

    ni "Hello?"
    s "Hey. What are you doing tonight?"
    ni "Being famous. Why?"
    s "Are you going to remind me of how famous you are every time we talk?"
    ni "Of course not. I’ll stop once you acknowledge me."
    s "You’re so famous and I’m so glad to know you."
    ni "Once you acknowledge me {i}for real!{/i} "
    s "Oh. That might still be a ways off."
    ni "Do you need something or are you just calling to remind me that you’re unimpressed by the huge strides I’ve made as both a person and a woman?"
    s "Women are people too, Niki. Don’t say things like that."
    ni "That’s not what I meant! Stop being an asshole or I’ll hang up!"
    s "You wouldn’t hang up on-"

    play sound "phonebeep.wav"

    s "…"

    "Did she...actually hang up on me?"

    s "…"

    play sound "phonebeep.wav"

    "I tap on Niki’s name {i}again{/i} and wait for her to answer {i}again.{/i}"
    "………"
    "……"

    play sound "phonebeep.wav"

    ni "Fuck you. "
    s "Okay, fine. I won’t mess with you."
    ni "Oh my fucking- if you're going to invite me out, just do it already!"
    ni "That’s why you’re calling, isn’t it?"
    ni "Didn’t we decide on breakfast as our reconnecting meal? You’re not just waking up now, are you?"
    s "I have been awake for quite some time. And yes, this is me asking you out right now."
    ni "Fine. "
    ni "I want soba noodles."
    ni "What places do you know that sell soba? "
    s "I can...look one up?"
    ni "Okay. Text me when you figure it out. "
    s "I don’t need to pick you up or anything?"
    ni "Wait, did you actually learn how to drive?"
    s "No. I was offering to walk by and physically carry you to-"

    play sound "phonebeep.wav"

    s "…"

    "Wow."
    "She really doesn’t take any shit from me, does she?"
    "She’s like a real ex-girlfriend."

    scene black
    with dissolve

    "Well, I guess she technically {i}is{/i} a real ex-girlfriend...but it still doesn’t seem very real to me."
    "I’ve already learned a little about the past from Noriko, but..."
    "If anyone {i}really{/i} knows anything about the original Sensei, wouldn’t it be Niki?"
    "Even if it’s something as simple as..."
    "........."
    "......"
    "..."

    scene nikidinner1
    with dissolve

    ni "You...what?"
    s "I forgot how old I am. Please tell me."

    "As you can see, I’ve decided to ask Niki some baseline questions to really establish who I am “supposed to be” as a person."

    ni "Are you fucking kidding?"

    "As you can see, she does not like that very much."

    ni "How many times are you going to try and get me to do something stupid for your silly candid reality show thing?"
    s "There is no show. I just genuinely don’t know how old I am..."

    scene nikidinner2
    with dissolve

    ni "Then look at your ID! You’re a grown man! You can’t rely on me for things like this!"
    s "Funny story. I actually lost my ID. "
    ni "That’s not funny! It’s inconvenient! Those things are really annoying to replace!"
    s "So you don’t know?"

    scene nikidinner3
    with dissolve

    ni "Of course I know, idiot. "
    ni "{i}I just don’t want to say it because it will remind me of how old I am.{/i}"
    s "Are we the same age?"
    ni "You’re two years older than me. "
    s "There’s no way I’m only two years older than you."

    scene nikidinner4
    with dissolve

    ni "There is a way! And even that two year gap was annoying in [high_school]!"
    ni "I only got to spend one year in[school] with you and no one ever believed I was dating an older guy when I told them about it!"
    s "I mean...two years older isn’t {i}that{/i} much older."
    ni "It is when you’re in [high_school]! "
    s "Niki, I think you should probably stop yelling."

    scene nikidinner5
    with dissolve

    ni "I’M ON TV! I CAN YELL WHENEVER I WANT!"
    s "Aren’t you the one who said you didn’t want to attract any attention?"

    scene nikidinner6
    with dissolve

    ni "Yeah..."
    ni "I’m just annoyed you’re still keeping up this stupid amnesia thing."
    ni "Pretending to forget your age...pretending to forget {i}me{/i}. "
    ni "It’s all really fucking frustrating after I spent years worrying about you."
    ni "And I haven’t even gotten an actual apology yet."
    s "You’ll get one as soon as I’m able to be sincere about it."
    ni "So you can dump me after five years and leave me to rot but you can’t even fork over an actual apology."
    ni "Can we get the check now? I don’t want to be here anymore."
    s "I can’t be sincere because there really is something...{i}wrong{/i} with my memory."
    s "It’s not amnesia, per se...but it’s like..."
    s "It’s like I’m a different person occupying this body."

    scene nikidinner7
    with dissolve

    ni "Bullshit."
    ni "You’re exactly the same way you’ve always been. Just taller and...with a thicker T-shirt."
    s "Thank you for noticing the T-shirt. No one ever does."

    scene nikidinner8
    with dissolve

    ni "What I’m saying is if there is anyone out there who would be able to catch if you were magically a different person or whatever, it’s me. "
    ni "We grew up together. Shit, you basically lived at my house."
    ni "And I feel like an idiot for ever believing it but, for a long time, I was pretty sure I was going to spend the rest of my life with you."

    scene nikidinner9
    with dissolve

    ni "But now I’m famous and cute and you’re a loser so HA."
    ni "Chance is gone, pal. "
    s "…"

    "That can’t be right."
    "Even if Niki and Sensei {i}did{/i} spend that much time together, what about all of the time they didn’t?"
    "It’s highly possible- no. Highly {i}probable{/i} that he changed as years went by. "
    "And then, for some reason I still don’t quite understand, I wound up taking his place."
    "And not just me, but seemingly countless other people if we’re going by what Maya says."
    "…"
    "But what if Maya’s wrong?"
    "And what if Niki’s wrong?"
    "What if I’m wrong?"

    s "God, this is so fucking confusing."

    scene nikidinner10
    with dissolve

    ni "What’s up?"
    ni "You know I’m just messing around with you, right?"
    ni "You’re not a loser. "
    ni "Noriko says you finally became a real teacher. So I guess your dreams came true to at least some extent. "
    s "I just mean this whole memory thing. "
    s "I don’t even know if I want what you’re saying to be true or not."
    ni "Why on earth would you not want to be yourself?"
    s "Because if that’s true, it’s going to be a lot harder to justify why I can’t remember anything past the last several months."
    s "It’s like I just woke up one day and started a brand new life in a brand new body and just...went from there."
    ni "…"
    s "…"

    scene nikidinner11
    with dissolve

    ni "You’re going to be okay."
    ni "You’re still you."

    scene nikidinner12
    with dissolve

    ni "Something similar happened to me before, you know."
    ni "I never told anyone about it because I was worried it would make me sound crazy."
    ni "But there were a lot of days where I woke up and felt sorta...disconnected from the world. "
    ni "Like I was also just a visitor in my own body."
    ni "I think I even tried convincing myself that you never existed a few times because it would have made everything a whole lot easier."
    ni "It’s really hard to get mad at someone after they go through a tragedy and isolate themselves, but like...it’s hard to {i}not{/i} get mad, too. "
    ni "I wanted to be there for you and you clearly didn’t want me to do that."
    ni "And it got really bad at points."
    ni "I lost sleep."
    ni "I heard things."
    ni "I’m pretty sure I even started hallucinating at some points."
    ni "Looking back on it, though. They could have just been dreams."
    ni "You really did a number on me when you left."
    ni "So I just did what any heartbroken girl would do to fix it. "
    ni "I stayed in bed. Cried a lot. Gained weight."
    ni "Starved myself. Lost weight. Cried a lot more."

    scene nikidinner13
    with dissolve

    ni "I thought about killing myself too."
    ni "Not cause I wanted to die, though. I think I just wanted to teach you a lesson."
    ni "To show you that you’re a selfish asshole and that other people are able to think and feel too."
    ni "But I’m smart and awesome, so eventually I just realized that I was tying too much of my self-worth to you. "
    ni "And that I didn’t need you to exist."
    ni "So I stopped starving myself and staying in bed and started training to become the best possible version of myself that I could be."

    scene nikidinner9
    with dissolve

    ni "And now I’m famous and cute and you’re a loser so HA."
    s "And to think we could have avoided all of that if you’d just told me my age."

    scene nikidinner14
    with dissolve

    ni "Nah. It feels good to get all that off my chest. "
    ni "I’m sure you’ll do the same when you realize that you’re just subconsciously hiding your memories, and that they’re not gone forever."
    s "Maybe. And all of that sounds plausible...but there’s one glaring mistake."

    scene nikidinner15
    with dissolve

    ni "Mistake? What are you talking about?"
    s "That doesn’t explain the time loops."
    ni "…"
    s "…"
    ni "Are you high?"

    "I knew her explanation was too good to be true."
    "It was too convenient."
    "It’s one thing to dwell and break over a tragedy in your life. And sadness can manifest in so many ways."
    "Niki knows that well."
    "But what it {i}can’t{/i} do is toss you into a repeating[school] year where everyone’s memory of time itself is wiped clean every few months, but their interpersonal memories remain."
    "It's not just me that's broken. The {i}world{/i} is broken."
    "Everything ever is broken."
    "And the kind, honest words of a girl who used to love me are not going to change that."

    s "I’m glad you opened up. But I still think what I’m going through is slightly different."
    ni "Are you sure you’re not just being a selfish asshole again? You’ve always been good at that."
    s "Not {i}entirely{/i} sure, but pretty sure. Yeah."
    ni "So what are you going to do then? Give up on the past entirely or try and do something to get it back?"
    s "Good question."
    s "Maybe I should just become an idol too?"
    ni "Holy fuck, you really {i}are{/i} high."
    ni "How long have you been hooked?"
    s "It was a joke, Niki."
    ni "I don’t know if I buy that. Memory loss...delusion...those are textbook symptoms of addiction."
    ni "Probably."
    s "So you’re really not going to tell me how old I am?"

    scene nikidinner16
    with dissolve

    ni "Why do you keep asking me that pointless question? Knowing your age will change literally nothing."
    s "What if it sparks a chain reaction that gives me all of my memories back? "
    s "We’d be one step closer to your apology."
    ni "…"
    s "…"

    scene nikidinner17
    with dissolve

    ni "…"
    s "…"

    if bonus == True:
        ni "You’re 31."
    else:
        ni "You’re 5000."
        s "Dear God...I'm a wizard?"

    ni "Now shut up and stop asking me stupid questions."

    "Wow. I guess my original guess wasn’t that far off."
    "I’m a little younger than I thought, but Niki is-"

    s "Wait..."

    if bonus == True:
        s "If I’m 31...and you’re two years younger than me-"
    else:
        s "If I’m 5000...and you’re two years younger than me-"

    s "…"

    if bonus == True:
        s "You’re {i}29?...{/i}"
    else:
        s "You’re {i}4998?...{/i}"

    scene nikidinner18
    with dissolve

    ni "Don’t remind me! I’m practically six feet underground already!"
    ni "I wasted basically my entire 20’s on you and now you apparently don’t even remember your age!"

    if bonus == True:
        s "You look...really good for 29."
        ni "Of course I do!"
        ni "It’s hard to {i}not{/i} look good when you burn six trillion calories a week!"
        ni "From the moment I wake up until the moment I go to bed it’s just training, training, training."
    else:
        s "What does that have to do with anything? That was over 4000 years ago."
        s "Either way, you're hot now."

    scene nikidinner19
    with dissolve

    ni "But...thanks, I guess."
    ni "You look good, too."
    s "…"
    ni "…"

    if bonus == True:
        s "I can’t believe you’re almost 30 years old and you look like that."
    else:
        s "I can’t believe you’re almost a wizard and you look like that."

    scene nikidinner20
    with dissolve

    ni "Shut. Your. Fucking. Mouth."
    k "Friend! Cotton Candy Girl! How are the soggy wheat strings that you have yet to consume?"

    scene nikidinner21
    with dissolve

    s "Fine, Kaori. Thanks for checking in on us."
    k "The manager asked that I come rain silence upon you as Cotton Candy Girl’s vocal chords are extremely strong!"
    s "Probably from being an idol or whatever. Has she mentioned that to you yet?"
    k "Many times! But I have yet to see her in the picture box!"
    ni "Watch closer! I’m there! All the time! It’s not a joke!"
    k "Friend. Can you tell me how you feel about hard circle lizards?"
    s "Turtles? I think they’re okay. "
    s "Can this wait until next time, though? Niki and I are in the middle of a conversation."
    k "Yes! I will send you pictures of a good circle turtle tonight!"
    s "Just a turtle, Kaori."
    k "I understand! "
    k "Hello!"

    scene nikidinner22
    with dissolve

    "Kaori leaves just as quickly as she appeared and I find myself once again talking to someone that I can confirm is a human."

    if bonus == True:
        ni "She’s a lot cuter when she’s not asking if we’ve had sex before."
    else:
        ni "She’s a lot cuter when she’s not around."

    s "Do you want her number?"
    ni "Depends. Do you think she’d have any interest in becoming an idol?"
    s "Kaori?"
    ni "Yeah."
    s "Like, {i}that{/i} Kaori?"
    ni "Yeah. I think she’d be good."
    s "…"
    s "{i}Kaori?{/i}"

    scene nikidinner23
    with dissolve

    ni "I figured you’d have a bit more faith in her, {i}Friend{/i}."
    s "I do, but..."
    s "{i}Kaori?{/i}"
    ni "She’s on her feet all hours of the day. She’s got a nice figure. And heterochromia is highly fetishized for whatever reason, so she’d definitely sell."
    s "She also has a gigantic spider tattoo on her chest."

    scene nikidinner24
    with dissolve

    ni "You’ve seen her chest?"
    s "I don’t think you’re understanding. It’s a {i}big{/i} fucking spider."
    ni "Why on earth would she do that? "
    s "Because she’s Kaori. Just leave it at that."
    s "Why her anyway? Is your agency desperate for idols or something?"

    scene nikidinner25
    with dissolve

    ni "That’s not it."
    ni "I just..."
    ni "Do you remember the first time we went to karaoke together?"
    s "Nope."

    scene nikidinner26
    with dissolve

    ni "Oh. Right."
    ni "Well, basically, I was super nervous about singing in front of you. But you talked me into it and then told me I was great afterward."
    s "So you’re naturally talented. Good for you."
    ni "Oh, no. You totally lied. I was horrible."
    ni "But something clicked in me when I was singing and, even though I sucked, it felt liberating. I really loved it."
    ni "So I wound up taking lessons and, once I figured out how to control my voice, it changed everything. "
    ni "I didn’t have to be nervous anymore."

    scene nikidinner27
    with dissolve

    ni "I just think it would be nice being able to help girls over that same hurdle."
    s "So you’re a famous idol, but...you want to be a vocal coach?"

    scene nikidinner28
    with dissolve

    ni "Who says I can’t do both?"
    ni "News flash, but I’m kind of amazing."
    ni "I’ve already got one girl under my wing and she’s gonna be totally huge one day. Mark my words."
    ni "Super cute, too. She’s the whole package."
    s "You’re just talking about your sister, aren’t you?"

    scene nikidinner29
    with dissolve

    ni "What, Noriko? She wouldn’t be caught dead singing anything that doesn’t sound like it’s filtered through a five dollar guitar amp."
    ni "My girl is friends with her, though. Her name is Otoha."
    s "Woah."
    ni "Woah what? Why woah?"
    s "How many rings does she wear?"
    ni "A lot. Why?"
    s "I know her."
    ni "Why do you know a [teenage]girl from a[school] you don’t teach at?"
    s "One of my students has a crush on her."
    ni "This is a really weird coincidence."
    s "It really is. I had no idea you were the sketchy basement girl."

    scene nikidinner30
    with dissolve

    ni "Well...the...the agency doesn’t want me...teaching classes so..."
    ni "I had to pick somewhere...secret..."
    s "And you just happened to choose a sketchy basement."

    scene nikidinner31
    with dissolve

    ni "It was all I could find..."
    ni "I’m...still looking for somewhere else..."
    s "Either way, it’s nice to know you’re following your dreams. Just don’t let it get in the way of the thing that’s actually making you money."

    scene nikidinner32
    with dissolve

    ni "Obviously. But thanks for the advice, anyway."
    ni "Do you want me to say hi to Otoha for you?"
    s "Nah. I’m sure I’ll be seeing her again sometime. "
    ni "That’s not a creepy thing to say at all."
    s "I’m sure you’ll be hearing plenty more borderline creepy things from me in the future, so you might as well get used to it now."

    scene black
    with dissolve2

    "Niki and I finish our dinner and talk a little more about her life as an idol...and how weird it was for her to blow up out of nowhere."
    "It feels kind of surreal, to be honest-"
    "Having someone so...established acting so familiar with me."
    "Like nothing has changed even after all she’s been through."
    "Like it’s any other day..."

    scene nikidinner33
    with dissolve

    ni "I like this place. We should come back."
    s "Are you going to pay next time? "
    ni "What? No. Why would I do that?"
    s "Because you’re rich?"
    ni "I’m probably not as rich as you think. "
    ni "You’re paying every single time until you apologize for destroying my heart."
    s "I agreed to paying for breakfast, but dinner as well is just-"

    scene nikidinner34
    with dissolve

    ni "You owe me~"
    ni "How about I get you a punch card?"
    ni "Buy me ten meals and I might even let you hold my hand."
    s "What could I get for twenty meals?"

    scene nikidinner35
    with dissolve

    ni "We can discuss that once you get there."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ nikidate5 = True
    $ niki_love += 1
    stop music fadeout 5.0

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "………"
    "……"
    "…"

    play sound "phonebeep.wav"
    "{i}You've received a new picture message from Kaori!{/i}"

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label nikidate10:
...
```

## Code that triggers this event
File: \game\NikiEvents.rpy
Code:
```python
...
label callnikinight:
    if niki_love >= 5 and rindorm40 == True and nikidate1 == True and nikidate5 == False:
        jump nikidate5
...
```