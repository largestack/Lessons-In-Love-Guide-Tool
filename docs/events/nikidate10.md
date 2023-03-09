# Thousands, If Not Millions
Niki event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=nikidate10&go=Go)



## Event preconditions
✅Niki love greater than or equal to 10

✅Event "[Main: All is Bright. All is Beautiful.](./secondbeach18.md)" is completed (event=secondbeach18)

✅nikinumber equal to True (unknown variable)



## Next events
* [Niki: Hotel Rooms](./nikidate15.md)

## Event properties
* ID: nikidate10
* Group: Niki
* Triggered by label: callnikimorning
* Triggered by branch label: callmorning

## Event code
File: \game\NikiEvents.rpy
Code:
```python
...
label nikidate10:
    play sound "phonebeep.wav"

    "I tap on Niki’s name in my phone and wait for her to answer."
    "It’s still early, so chances are she has enough time for her daily dose of wiener right now."
    "I’m not usually the type of guy to call up a girl just to give her some sausage, but Niki seems to really enjoy that sort of thing."
    "Besides, Kaori will be there as well. And nothing says bonding like two girls wrapping their lips around some meat together."

    play sound "phonebeep.wav"
    play music "remember.mp3"

    ni "What do you want?"
    s "Oh, you {i}know{/i} what I want."
    ni "Ew, why are you talking like that? Stop it."
    s "Sorry."
    s "Are you free right now?"
    ni "Depends."
    s "On?"
    ni "Whether or not {i}you’re{/i} free."
    s "I am."
    ni "Then I am not. Goodbye, [nikitemp]."
    s "You fucking bitch."
    ni "Hahah! I’m kidding, idiot. "
    ni "Yeah, I can get away for an hour or two. "
    ni "But if you show up with my little sister, I swear to fucking God."

    if bonus == True:
        s "Oh, don’t worry. She’s still asleep in my bed. It was a really long night."
        ni "You fucking-"
    else:
        s "I would never. Noriko is my student and I respect you far too much."
        s "I love you, Niki."
        ni "Wait...did you just say what I-"

    play sound "phonebeep.wav"
    scene black
    with dissolve

    "I hang up the phone and laugh silently to myself as I get dressed."

    if bonus == True:
        "And then I say goodbye to Noriko, who is still asleep in my bed following a very long night."
        "…"
        "Just kidding."

    "………"
    "……"
    "…"

    scene nikidateten1
    with fade

    "Kaori is able to go on break shortly after Niki and I make it to the diner and I move one step closer to watching her eat a wiener."

    s "Kaori."
    k "Yes, Ex-Boyfriendburger?"
    s "I’m not your ex-boyfriend. I’m Niki’s."
    k "What is a “Niki?”"
    s "Sorry. I meant the cotton candy girl."
    ni "You know, Kaori, you should probably think of adding more things to the menu soon. I feel like you’re missing out on a good amount of profit only selling one thing."

    scene nikidateten2
    with dissolve

    k "But you love the wiener! "
    ni "I {i}tolerate{/i} the wiener. It’s different. I’d much prefer something sweeter."
    s "Weird way to admit to being a lesbian, but I’m glad I could be here to witness it."

    scene nikidateten3
    with dissolve

    ni "Shush."
    s "Did you just shush me?..."
    k "What’s a “lesbian?”"

    scene nikidateten4
    with dissolve

    ni "A lesbian is a girl who’s sexually attracted to other girls."
    k "Is that not all girls? "

    scene nikidateten5
    with dissolve

    ni "You like girls, Kaori?"
    k "I like all people! Everyone is attractive in their own way! Even you!"
    ni "..."
    ni "What do you mean, “even” me?"
    k "I apologize for being hard to understand. But it seems that you still have your sights set on Friendburger, which means we can not be together!"
    s "Niki’s straight anyway, so she wouldn't want a relationship with you, Kaori."

    scene nikidateten6
    with dissolve

    ni "What are you talking about? No I’m not."
    s "You’re not?"
    ni "You literally know this. We got into a fight over-"

    scene nikidateten7
    with dissolve

    ni "Oh, right. Your stupid memory sucks or whatever."

    "I learned something today."

    k "Do you see how the one made of aerated sugar did not deny her feelings for you? This must be love!"
    k "Kiss!"

    scene nikidateten8
    with dissolve

    ni "No, Kaori. I’m not going to kiss my stupid, asshole ex-boyfriend in a dirty old diner full of...dirt and stuff."
    k "I cleaned this table myself! You may kiss here whenever you like and I will explain to my manager that I can not stop love!"

    scene nikidateten9
    with dissolve

    ni "Can I kiss you instead? You think I’m cute, right?"
    k "Kissburger?!"

    if bonus == True:
        s "I know I’m probably supposed to be getting jealous or whatever, but I want to let the two of you know that I unconditionally support this development."
    else:
        s "I know I’m probably supposed to be getting jealous or whatever, but I think you two would make a wonderful couple."

    scene nikidateten10
    with dissolve

    if bonus == True:
        ni "Ugh, great. So now I just sound like a slut. Thanks."
        k "Slutburger..."
        s "Apologize to Kaori. You got her hopes up and now she has to learn what a slut is."
    else:
        ni "Ugh, great. That's not what I wanted at all."
        k "Coupleburger..."
        s "Apologize to Kaori. She deserves better than this."

    scene nikidateten11
    with dissolve

    ni "I’m sorry for playing around, Kaori. I have a history of losing my head around this jerkburger and it often leads to me saying things in the heat of the moment."

    scene nikidateten12
    with dissolve

    k "Ah! Jerkburger!"
    s "What? No. Don’t repeat things Niki says. She’s evil and steals clothing from people without realizing they only have two versions of the same shirt."
    ni "I’d like to say I still have a few of your hoodies from back when we dated, but I think I may have {i}accidentally{/i} dropped all of them into a fire. Whoops."
    s "Wow. I really did a number on you, didn’t I?"

    scene nikidateten13
    with dissolve

    ni "Haha! Yeah! You made me want to kill myself! Thanks!"
    k "Uh-oh. This does not seem like a conversation that is friendly for the Mistress of the Dark to be involved with. "
    k "I have already informed both of you that I can not stop love. Please continue confessing your sad human feelings to one another while I go pretend to not listen from behind the counter."

    scene nikidateten14
    with dissolve

    ni "Wait, Kaori. You don’t have to leave. I was just-"
    k "Tell the burger about your feelings while I prepare for the wieners to come!"
    k "They are very big wieners, so it may take them longer to come than normal ones!"
    ni "…"
    s "I think that’s a myth, actually. I have no trouble-"

    scene nikidateten15
    with dissolve

    k "Only I can make your wiener come! Don’t you forget that!"
    ni "…"
    s "Got it."
    s "Thanks, Kaori."
    k "Hello!"

    scene nikidateten16
    with dissolve

    "Kaori storms off into the kitchen and trips over...something. "
    "It’s probably nothing to worry about, though, since a few of the kitchen staff quickly come to her rescue and help her regain her footing before breaking into a fit of laughter."
    "It’s a little tough to remember that people have lives outside of me, but I guess Kaori and Niki are the two best examples of that I can think of."

    if bonus == True:
        "Both of them live to please others while I...live to please myself and various [teenage]girls."
        "Just...in a different way."

    scene nikidateten17
    with dissolve

    ni "Why do I get the feeling you were thinking of something disgusting just now?"

    if bonus == True:
        s "Probably a safe bet. I’m essentially always thinking of something disgusting."
    else:
        s "Because you hate me and refuse to believe I am a good boy."

    "Niki takes off her disguise in preparation for the coming sausages and slides her glasses to the side of the table."
    "But instead of saying anything afterward, she just stares at me like she’s waiting for me to...apologize for my entire existence or something like that."
    "I don’t really know what she wants."
    "That’s probably why our relationship ended."
    "I’m sure it had nothing to do with whatever tragedy that befell me."

    play sound "static.mp3"
    scene handsareweird with flash
    scene imissyoumore with flash
    scene dust5 with flash
    scene nikidateten17 with flash
    stop sound

    s "So, about what happened at the beach."
    ni "What about it?"
    s "Well...that was weird, right?"
    ni "Which part? The one where I showed up? Or the one where I left before you woke up?"
    s "I guess both. I thought we were on a little worse terms than sleeping together."
    ni "As much as we {i}should{/i} be on worse terms, I’m doing my best to not hold anything against you."

    scene nikidateten18
    with dissolve

    ni "I know things were really rough for you back then. "
    ni "I just wish you would have called or something and...you know, {i}not{/i} kept your childhood friend and first ever girlfriend waiting like a fucking lunatic."
    ni "I missed you a lot."
    ni "And like...I don’t know. I guess I still do or whatever."
    s "It’s starting to sound like I won’t be getting my shirt back."

    scene nikidateten19
    with dissolve

    ni "Will you shut up about the fucking shirt?! I’m trying to be serious here!"

    scene nikidateten18
    with dissolve

    ni "You know...I always said all this stuff to myself about what I would do if I actually {i}did{/i} bump into you again."
    ni "And in every single made up scenario, I always had the upper hand."
    ni "I’d catch you in line for one of my concerts or see you in the mall during a signing event...and I’d laugh to myself and look the other way."
    ni "I wanted you to think that I forgot about you, like how {i}you{/i} forgot about me."
    ni "Or...are {i}continuing{/i} to forget about me, because I still have no idea what this shit you’re trying to pull with your memory is."
    ni "But...as much as I hate to say it...I can’t do it."
    ni "I can’t actually forget you."
    ni "And...I don’t even think I want to anymore."
    ni "Which is why I made my driver turn around and take me back to the inn. And why I left in such a hurry that I didn’t even take my bag with me."
    s "You were that excited to see me?"

    scene nikidateten20
    with dissolve

    if bonus == True:
        ni "You know, there are thousands, if not millions of other guys who would be creaming their pants if they were in your position right now."
        s "Do you...do you want me to ejaculate?"
    else:
        ni "You know, there are thousands, if not millions of other guys who would be freaking out if they were in your position right now."
        s "Would it make you feel better if I stole your things and ran away to go sell them on the Internet?"

    scene nikidateten21
    with dissolve

    ni "{i}What?{/i}"
    s "You just sounded a little disappointed that I’m not freaking out about this."

    scene nikidateten22
    with dissolve

    ni "Because I am! I hate that {i}I’m{/i} the one crawling back when I spent years and years and years preparing myself to do the opposite!"
    s "You're not saying you want to get back together, are you?"

    scene nikidateten23
    with dissolve

    ni "No...I don’t think so. "
    ni "I don’t really know what I’m saying."
    ni "I {i}can’t{/i} have a boyfriend because of my job. But I also don’t really want you running off and settling down with anyone either. "
    s "Well...you definitely don’t have to worry about that. I’m not really the “settling” type."
    ni "No...you never were..."
    ni "…"
    s "…"
    ni "Hey."
    ni "You’re not..."

    if bonus == True:
        ni "Still a virgin, are you?..."
    else:
        ni "Still trying to sell my bobsled, are you?..."

    s "…"
    ni "…"
    s "I’m sorry, what?"

    if bonus == True:
        ni "Since we...you know. Never really did it."
    else:
        ni "Nevermind. Just tell me if you're dating anyone."

    s "…"
    ni "…"
    s "You..."
    ni "Mhm."
    ni "But not because I can’t find anyone. I’m famous and I can have whoever I want."
    ni "I was just...never interested in anyone else."

    if bonus == True:
        s "You are a world-famous idol who is about to turn thirty...and is still a virgin?"
    else:
        s "Wow? Not a single person in almost 5000 years? That is very sad."

    scene nikidateten24
    with dissolve

    if bonus == True:
        ni "What does my age have to do with it?! There’s nothing wrong with being a virgin at thirty!"
        ni "In fact, there are tons of people who go even longer than that! "
        ni "And you’d probably be surprised to hear that some of them may be listening in on this conversation right now!"
        s "I’m sorry if this sounds insensitive, but...we really never had sex?"
    else:
        ni "It is not sad! It is perfectly normal! Now, about that boblsed!"
        s "Do you need a hug?"

    scene nikidateten25
    with dissolve

    if bonus == True:
        ni "We just did...{i}hand{/i} stuff most of the time."
        ni "It was hard since my parents and Noriko were always home..."
        ni "And, believe it or not, you were really understanding about that sort of thing back then. You never pushed me to really {i}do{/i} it, you know?"
        ni "Jesus, why are we even talking about this in a diner? What has my life become?"
        s "…"
        s "Niki, I-"
        ni "I changed my mind. I don’t want to hear it."
        ni "You can keep whatever you’ve done these last eight years to yourself. I don’t want to know."
        ni "I’ll just fill in the blanks with how I want things to be and force myself to believe they’re true. "
        s "Is that really how you want to live? By just pretending things are better than they actually are?"
        ni "Gee, wonder who I learned that from?"
        s "I don’t have a problem with it. I’m just surprised to be seeing this side of you when it still seems like you can’t stand being around me half the time."
        ni "Trust me, this is even weirder for me than it is for you."
        ni "God. None of this ever would have happened if I didn’t bump into you and Noriko at that damn beach. My mind has not stopped being fucking...annoying since then."
        s "Do you think something is actually happening between Noriko and me?"
        ni "I think...that Noriko likes you way more than she should. And I think you’re exactly the type to take that affection and run with it."
        ni "It seems like you’ve always been trying to fill some sort of hole inside of you, and I don’t really know who else is there to do that right now."
        ni "So...I don’t know. Keep me in your thoughts and don’t fuck my sister, I guess?"
        s "…"
    else:
        ni "Maybe a little one..."

    scene nikidateten26
    with dissolve

    if bonus == True:
        ni "Like, really. Please don’t fuck my sister."
    else:
        ni "But only if we can do it in the kitchen."

    s "…"
    ni "…"

    scene nikidateten24
    with dissolve

    if bonus == True:
        ni "Jesus Christ! Repeat after me! You! Will! Not! Fuck! My! Sister!"
        s "You. Will. Not-"
        ni "Not “You!” "
        ni "“I will not fuck your sister!”"
        s "Thank you for making that promise, Niki. But I don’t have a sister for you to fuck no matter {i}how{/i} much you want to. "
    else:
        ni "I want to have a kitchen hug!"
        s "What is happening right now?"

    scene nikidateten27
    with dissolve

    ni "Okay, you know what? This was clearly a mistake. "
    ni "I thought it might be a sign that I wanted to start patching things up when I came to you in the middle of the night, but I can see now that you’re just going to be a prick about it."
    s "I need you to look at things from my perspective, though."
    s "You showed up in the middle of the night, stole one of my shirts, and then left before-"

    scene nikidateten24
    with hpunch

    ni "Oh my fucking God! I will literally buy you a new shirt! Just shut the fuck up about it!"
    k "Incoming wieners! Brace for impact and massive girth!"

    play sound "thump.mp3"
    scene nikidateten28
    with hpunch

    ni "Hah..."
    s "Wait, we didn’t even order-"
    k "You did not have to, Jerkyexboyfriendburger! We only have one thing on the menu!"
    k "Didn't you read it? All we have is the sausage fest!"
    k "Seriously! That’s it!"
    ni "We read the fucking menu, Kaori."
    k "Congratulations! I am very proud of your ability to comprehend words! Good job!"

    scene nikidateten29
    with dissolve

    ni "So, now what?"
    s "What do you mean?"
    s "I figure that if you want to start patching things up, we can-"
    ni "Not about our fucking relationship. About all this food."
    s "Oh. Well, I’m not hungry."
    ni "Remind me again why we keep coming here if you literally never eat anything?"
    s "That’s easy, Niki."

    scene black
    with dissolve2

    if bonus == True:
        s "Because if there is anyone who deserves a good wiener, it’s a twenty-nine year old virgin."
        ni "I fucking hate you."
    else:
        s "Because I have forgotten {i}how{/i} to eat."
        ni "I fucking hate you."

    $ renpy.end_replay()
    $ niki_love += 1
    $ nikidate10 = True
    stop music fadeout 7.0

    "{i}Niki doesn’t actually hate you! Her affection has increased to [niki_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdayafternoon

label nikidate15:
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
    if niki_love >= 10 and secondbeach18 == True and nikidate10 == False:
        jump nikidate10
...
```