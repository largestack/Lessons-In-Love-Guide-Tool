# Cotton Candy
Niki event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nikidate1&go=Go)



## Event preconditions
✅Niki love greater than or equal to 0

✅nikinumber equal to True (unknown variable)



## Next events
* [Niki: Like it's Any Other Day](./nikidate5.md)

## Event properties
* ID: nikidate1
* Group: Niki
* Triggered by label: callnikimorning
* Triggered by branch label: callmorning

## Event code
File: \game\NikiEvents.rpy
Code:
```python
...
label nikidate1:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "I feel like I’m supposed to be a little nervous about doing this considering she is my apparent ex-girlfriend as well as a pop star, but-"
    "Eh."
    "It just feels like any other phone call to me."
    "And if this call is going to be anything like our “first” meeting the other day, I imagine she’s just going to yell at me or something like that."

    if bonus == True:
        "But hey, if we’re ever going to patch things up (And start having sex again), I’ve gotta start somewhere."

    play sound "phonebeep.wav"

    q "Thank you for calling 567 Productions. How can I help you?"
    s "…"
    q "Hello?"

    play music "remember.mp3"

    s "I’d like to speak with Niki Nakayama, please."
    q "…"
    q "No."
    s "But I’m her ex."
    q "That’s even worse."
    q "Please do not call here anymore."
    s "Wait, I think you’re misunderstanding something."
    s "She’s the one who gave me this number."
    q "Then she clearly doesn’t want to talk with you."
    q "You are aware that she has her own phone, correct?"

    "That fucking bitch."

    s "Listen...is she around? Just tell her I’m calling and if she doesn’t want to take it then...hang up on me or something."
    q "...Okay, fine."
    q "Can I have your name?"
    s "It’s...uhh..."

    menu:
        "Noodles":
            $ nikitemp = "Noodles"

            s "My name is Noodles."
            s "Noodles the Bird."
            q "Your name is not Noodles the Bird."
            s "Tell her my name is Noodles the Bird."
            q "Is this some sort of inside joke between the two of you?"
            s "Yes. Now, tell her."
            q "Okay...fine. "
            q "Please hold."

        "Paul":
            $ nikitemp = "Paul"

            s "My name is Paul."
            q "An American? How come I never heard of this?"
            q "How long ago were the two of you together?"
            s "Please stop prying into my personal life. This is between Niki and me."
            q "Apologies, Paul. I’ll let her know you’re calling right away."

        "Barack Obama, 44th President of the United States":
            $ nikitemp = "Barack"

            s "I’m Barack Obama, 44th president of the United States of America."
            q "…"
            s "…"
            q "…"
            s "I don’t have all day. I have meetings to attend."
            q "Please hold for one moment..."

    "I’m placed on hold for several minutes while the receptionist or manager or whoever it was that I was just speaking with tries to find Niki."
    "Hopefully, the original Sensei also had an amazing sense of humor that she will be able to quickly identify immediately upon hearing that she’s received a call."
    "But, more than likely, I just expect to get yelled at again."

    play sound "phonebeep.wav"

    ni "Well good morning, {i}[nikitemp]{/i}..."
    s "Hey. So nice of you to pick up."
    s "Why did you give me a fake number?"
    ni "It’s not fake, asshole. It’s the number to my agency."
    ni "You were just on the phone with my manager."
    ni "Also, why wouldn’t you use your normal fucking name?"
    s "I can’t remember my normal name."
    ni "{i}Hah{/i}...amnesia card again?"
    s "You know me so well."
    s "Almost well enough to give me your normal phone number."
    ni "Oh my fucking God, shut up. Why are you even calling?"
    ni "I’m not sure if you’ve realized, but I’m extremely busy right now and-"
    s "Let’s go out to breakfast."
    ni "At least let me finish my sentence, dick!"
    s "It’s not Dick, it’s {i}[nikitemp]{/i}."
    ni "You’re not funny."
    s "So, are you able to sneak away for a while and catch up? "
    ni "…"
    ni "Can I choose where we go?"
    s "If that’s what makes you happy."
    ni "…"
    ni "Fine. But {i}only{/i} for a little while. I have a class today."

    scene black
    with dissolve

    "The two of us talk for another minute or two and Niki winds up giving me an address to a diner somewhere in the middle of the city."
    "I didn’t really plan on going that far out today, but I guess you need to make certain sacrifices if you’re going to date someone famous."
    "Or at least, {i}go{/i} on a date with someone famous."
    "I doubt Niki would ever want to see me again after I apparently abandoned her for years."
    "But hey, she’s also apparently been waiting around for closure or something, so..."
    "I guess we’ll just have to see how things go."
    "………"
    "……"
    "…"

    scene nikifrtsdate1
    with dissolve

    s "What the fuck are you wearing?"
    ni "I’m a big fucking deal, {i}[nikitemp]{/i}. I need to wear this so people don’t recognize me."
    s "How are you going to eat with that on?"
    ni "I’m obviously going to take it off to eat! Have you never been on a date with an idol before?!"

    scene nikifrtsdate2
    with dissolve

    ni "Oh, what am I saying? Of course you haven’t. Sorry. Sometimes, I just forget how-"
    s "So what do you want to eat?"

    scene nikifrtsdate3
    with dissolve

    ni "STOP INTERRUPTING ME!"
    s "Take the disguise off, then. I want to actually talk to {i}you{/i}, not a mask and a cheap pair of sunglasses."

    scene nikifrtsdate4
    with dissolve

    ni "Cheap?! Those cost me a fucking fortune!"
    ni "Well...I actually got them for free as a gift from the agency. But they cost {i}someone{/i} a fortune!"

    "Niki takes off her mask and her glasses and stuffs them into an oversized bag she placed beside her when she arrived."
    "The two of us got here around the same time, so there was no awkward waiting at the table or anything like that beforehand."

    if bonus == True:
        "Just...two people who used to have sex (Probably) out for breakfast at a diner that totally isn’t something out of a popular first person shooter game."
    else:
        "Just...two people who used to date out for breakfast at a diner that totally isn’t something out of a popular first person shooter game."

    s "There. You look so much prettier now."

    scene nikifrtsdate5
    with dissolve

    ni "Shut up..."
    ni "You..."
    ni "You don’t look half bad yourself."
    ni "I kind of expected you to be huge and fat and all scraggly or something by now."
    ni "But I guess you’ve been doing alright the last few years."
    ni "Even if you managed to make it through them without turning your fucking TV on even {i}once{/i}."
    s "I’ve definitely turned the TV on. I just haven’t seen you."
    s "Maybe you’re just not as famous as you think you are?"

    scene nikifrtsdate6
    with dissolve

    ni "Want to bet on that? "
    ni "I can {i}guarantee{/i} you that our waitress will recognize me right away. "
    s "That’s not fair. You chose this place. For all I know, you could be a regular here."
    ni "I just wanted to choose some place that no one would ever expect me to come to. "
    ni "Which is exactly why I’m expecting our waitress to fall flat on her face the second she realizes she’s serving a pop star."
    s "You’re even more of an egomaniac than I am and I’m one of the last remaining males in Kumon-mi."
    ni "I {i}worked{/i} for this ego, {i}[nikitemp]{/i}. "
    ni "But of course you’re still pretending to have amnesia so you don’t have to remember how self-conscious I always was when we were younger."

    scene nikifrtsdate7
    with dissolve

    ni "Oh, perfect! Here comes our waitress now."
    ni "Watch and prepare to be amazed by my popularity."

    scene nikifrtsdate8
    with dissolve

    ni "Hi there! I’m sooo sorry for showing up unannounced. I hope I didn’t attract any paparazzi-"
    k "Friendburger Man!"
    ni "…"
    ni "I beg your pardon?"

    scene nikifrtsdate9
    with dissolve

    k "Hello! I am Kaori! But you may call me the Queen of Spiders or the Mistress of the Dark if you’d like."
    k "Are you on a date with my Friendburger?"
    s "This is actually my ex-girlfriend, Kaori."

    scene nikifrtsdate10
    with dissolve

    k "Girlfriendburger?!"
    ni "You..."
    ni "You really don’t recognize me?"
    ni "Niki Nakayama? Household name?"
    ni "I’m on billboards and..."

    if bonus == True:
        k "You mated with this creature?!"
    else:
        k "You hugged this creature?!"

    s "I’ll let her answer that question. I don’t think I’m at liberty to discuss my previous...{i}encounters{/i} with a celebrity."

    scene nikifrtsdate11
    with dissolve

    k "You are a celebrity? "
    k "I apologize for not recognizing you, but I do not know many of the popular cultures."
    ni "You don’t...have to apologize. I’m just a little taken aback."
    ni "Normally people have all sorts of questions for me when we first meet, so...this is actually a pleasant surprise, I guess?"
    k "I have two questions for you, actually. "
    k "Number one-"
    k "Is your hair made of cotton candy?"
    ni "...No."
    k "I see. "
    k "Number two-"

    if bonus == True:
        k "Can you describe to me how much you enjoyed mating with this man?"
    else:
        k "Can you describe to me how much you enjoyed doing the human hug move with this man?"

    scene nikifrtsdate12
    with dissolve

    ni "…"

    if bonus == True:
        s "Kaori, are you...curious about mating?"
    else:
        s "Kaori, are you...curious about hugs?"

    k "I am curious about many things. But this is the first female I have encountered with actual experience."
    k "Let alone experience with my friend! I must know!"
    k "Describe to me in vivid detail the things you experienced, Cotton Candy Girl!"

    scene nikifrtsdate13
    with dissolve

    ni "Was this all just some ploy to get me on one of those candid reaction shows?"
    ni "There’s no way any of this is actually happening, right?"
    s "You get used to it after a while. "
    s "I found myself thinking something similar the first few times I encountered Kaori."
    ni "Did she like...hit her head a little too hard?"
    s "There is a high likelihood of that, yes."

    scene nikifrtsdate14
    with dissolve

    ni "Listen...Kaori, was it?"
    ni "I think your curiosity is quite charming, I really do."

    scene nikifrtsdate15
    with dissolve

    ni "But if you ask either one of us about our {i}personal{/i} affairs again, I will not hesitate to destroy you."
    ni "Now, please make yourself useful and take our orders."
    k "I can not do that, Cotton Candy Girl!"
    k "I will remain quiet about your mating rituals, but this restaurant only serves one thing! Taking your order would be a waste of time!"

    scene nikifrtsdate16
    with dissolve

    if bonus == True:
        k "Friend. Your taste in women is very different from your taste in students."
    else:
        k "Friend. Your taste in women is very diverse."

    k "I had no idea you were the type who enjoyed being bossed around."
    k "I shall add this to my friendship journal. Entry number #387."
    s "It was a long time ago. I think my tastes may have been a little different back then."
    k "Whatever the case, Cotton Candy Girl has expressed her hunger and so I must do my duty as the number one waitress in Kumon-mi to please her."
    k "You can continue to please her in ways that I am not allowed to talk about."
    k "Until we meet again in several minutes."

    scene nikifrtsdate17
    with dissolve

    "Kaori darts away from the table and the atmosphere between Niki and I suddenly grows even more...uncomfortable."
    "For her, at least. "
    "I think this is the closest I’ve come to having fun in quite some time."

    ni "Ahem..."

    scene nikifrtsdate18
    with dissolve

    ni "I know it’s been a long time since the two of us have hung out like this."
    s "I feel a “but” coming."

    scene nikifrtsdate19
    with dissolve

    ni "{i}But{/i} would you mind explaining to me exactly {i}how{/i} you know that girl and why she is so interested in us {i}mating{/i}?"
    s "Explain Kaori? You’ve got a lot to learn."
    s "That’s just not possible."
    ni "You are aware that even being {i}seen{/i} in public with a man could destroy my reputation, correct?"
    ni "Do you have any idea what would happen to me if someone overheard that conversation?"
    s "I can’t imagine it would be anything good."
    ni "It would make the last several years of my life meaningless. "
    ni "The idol world is cutthroat. One wrong move and you’re done for good."
    ni "So if we’re going to continue going out together, {i}please{/i} make sure that nothing like that ever happens again."
    s "I think you just accidentally admitted that you want to keep seeing me."

    scene nikifrtsdate20
    with dissolve

    ni "Of course I do..."
    ni "Not as a couple or anything...you ruined that."
    ni "But I’d be...really hurt or whatever if we didn’t at least keep in touch."

    scene nikifrtsdate21
    with dissolve

    ni "Oh! And you owe me an apology! A real one!"
    ni "It’s not fair that you get to just walk back into my life and start talking about mating and...giving yourself weird names!"
    ni "We’re not teenagers anymore. We are grown adults and should be acting like that."

    scene nikifrtsdate22
    with dissolve

    ni "It doesn’t have to be today since...I know you’re still trying to come up with a better explanation than this whole “amnesia” thing, but..."
    ni "Whenever you’re ready to actually {i}talk{/i}...that’s fine."
    ni "We can just keep going out to breakfast or something until then."
    s "And if I have no idea how long that will take?"
    ni "Then you’re going to be buying me a lot of breakfasts."

    scene nikifrtsdate23
    with hpunch
    play sound "thump.mp3"

    k "I present to you, the Route 69 Diner’s special {i}and only{/i} item, the sausage-fest!"
    ni "Wha-"
    ni "People actually...{i}eat{/i} this?"
    k "Friend. Your ex-girlfriend does not seem to grasp the concept of food."
    k "Is this what ended your previous relationship?"
    s "Yes. This is exactly why we broke up."
    s "Niki, enjoy the sausage-fest."

    scene nikifrtsdate24
    with dissolve

    ni "Actually, I already ate breakfast this morning. And that’s way too much food."
    ni "This is all you. "
    s "Kaori, are you hungry?"
    k "Wieners make my mouth feel funny. I think they are too big for me."
    s "Can you say that one more time but a little slower?"

    "I take out my phone to record and-"

    scene nikifrtsdate25
    with hpunch

    ni "Stop hitting on the fucking waitress right in front of me!"
    k "Enjoy your wieners! I must help another customer now!"
    k "Let us hang the outs again soon, Friend! John misses you!"
    s "Sounds good, Kaori. Thanks for your service."
    k "Of course! Please remember to like, comment and subscribe!"

    scene nikifrtsdate26
    with dissolve

    ni "…"
    s "…"
    ni "Really, though. I’m not hungry at all. I can’t eat that."

    "I take one last look at the colossal pile of food before me..."
    "And surrender myself to the sausage-fest."

    scene black
    with dissolve2

    "Of course, I’m barely able to finish any of it. "
    "And apparently this diner doesn’t offer to-go boxes either, so a good thirty pounds of food are left on the table by the time we leave."
    "But at least Niki and I got to “reconnect” a bit. "
    "She’s not much different from how I pictured her after our first meeting in the studio, but..."
    "I guess I can see why the old Sensei might have fallen for her."
    "{i}Congratulations! You now have Niki’s real phone number and don’t have to lie about your name anymore!{/i}"

    $ renpy.end_replay()
    $ niki_love += 1
    $ nikidate1 = True
    stop music fadeout 5.0

    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label nikidate5:
...
```

## Code that triggers this event
File: \game\NikiEvents.rpy
Code:
```python
...
label callnikimorning:
    if niki_love >= 0 and nikidate1 == False:
        jump nikidate1
...
```