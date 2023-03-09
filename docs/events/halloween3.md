# The Meat has Come
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloween3&go=Go)


Part of event chain [Guest of Honor](./halloween2.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: halloween3
* Group: Main
* Triggered by label: halloween2

## Event code
File: \game\script.rpy
Code:
```python
...
label halloween3:
    scene street_noon
    with dissolve
    play music "normalday.mp3"

    "I wind up releasing myself from the custody of my [niece] and her friends shortly after we leave the mall."
    "Not wanting to head back to the house to watch Ami make her costume, I decide to go for a walk around town instead."
    "I’m not really sure what time Sara and Haruka were expecting me to come over tonight, so I guess I just have to kill time until whenever that is."
    "And what better way to kill time than scavenging the city for other girls I know?"
    "I mean, sure, Kumon-mi is a pretty big place- but I always manage to run into one of the like, twenty people I know somehow or another."
    "I’m sure something convenient like that is bound to happen again at any moment."

    r "Woah! What a crazy coincidence! Sensei is here!"

    scene rinfutababistro1
    with dissolve

    "I turn around to find Rin and Futaba eating lunch at the bistro Ami and Maya like to hang out at."
    "It’s not normal that I find anyone here on the weekend since this place is between the dorms and the[school], but I guess there’s no limit on when people are allowed to eat."

    s "Hey. What are you two up to?"
    r "What’s it look like we’re up to? We’re having lunch."
    f "Would you care to join us, Sensei?"
    s "Oh, no. I actually just ate at the mall with Ami and some of the others."

    scene rinfutababistro2
    with dissolve

    r "Oh, you were with them, too?"
    r "I texted Sana a little while ago to see if she wanted to come with us but she said she was busy."
    s "You two have been together the whole day then, I’m assuming?"

    scene rinfutababistro3
    with dissolve

    f "Right. We just finished putting our costumes together for the Halloween party tomorrow."
    s "Putting together as in...making them?"
    r "That’s right!"
    s "Why is everyone suddenly making their own costumes? Whatever happened to buying stuff?"
    f "Well, we’re actually wearing costumes that...we wore to some other event last year but-"
    f "Our sizes have, umm, kind of changed...so we were adjusting them."
    r "I have boobs now! It’s sweet!"
    s "Yes, Rin. That is very sweet. "

    scene rinfutababistro4
    with dissolve

    f "And I...have somehow grown in that department as well."
    r "Wack."
    r "At this rate, those things are gonna take over Kumon-mi one day. "
    s "Don’t worry. I’ll defend the city."
    f "I don’t know what you plan on doing exactly, but I don’t think the city will need actual defending any time soon."
    s "Sure. {i}But when it does.{/i}"
    f "...Thank you for the support."

    scene rinfutababistro2
    with dissolve

    r "Are you going to be dressing up, Sensei?"
    s "Do I look like the type to dress up?"
    r "No, you look like a total buzzkill."
    s "Correct. I am a total buzzkill and will only be coming to see how everyone else is dressed up."
    s "I’d probably never hear the end of it from any of you if I actually wore a costume."

    if bonus == True:
        r "So you’re going to come to a party with a bunch of [teenage]girls in costumes and just stare at them all night dressed as a normal dude?"
        s "That’s the plan."
    else:
        "That's what I {i}say{/i}...but the real reason is that I'd look way too cute in my costume and it would make all of the girls jealous."

        r "You're really going to come to a party with a bunch of collegiate age females and just...not dress up as anything?"
        s "Yes."

    r "Yeah, that checks out. Have fun."
    s "I’ll do my best."
    k "Friend!"

    "An unmistakable voice cries out from not-far-behind me and, before I know it, the owner of said voice joins us at the table."

    scene rinfutababistro5
    with dissolve

    k "I appeared at this large wooden circle to check on the guests, but I am now more excited to be seeing you instead!"
    k "Welcome back! Will you be consuming hot meat today?"
    s "Thanks, Kaori, but I just ate a little while ago."
    k "I understand! Please inform me if the wisdom juices in your brain begin to flow differently and cause you hunger."
    s "I will...be sure to do that."

    scene rinfutababistro6
    with dissolve

    r "When did...you and Kaori get so close? Didn’t she call you something like Hamburger Man the last time we saw her?"
    f "Hamburger Man?..."
    s "It’s a long story and probably not worth telling."
    r "The name “Friend” seems like a pretty big jump. How many steps are there between...food and friends, exactly?"

    scene rinfutababistro7
    with dissolve

    k "One! "
    k "Which is also the amount of friends I possess now!"
    k "All I need is an animal companion and my quest for eternal joy will be complete!"
    s "Yeah, after our first {i}date{/i}, Kaori warmed up to me very quickly."

    scene rinfutababistro8
    with dissolve

    r "Y-You went on a d-d-d-date with Kaori?!"
    r "And I wasn’t invited?!"
    f "Sensei...Are you and this girl..."
    k "Why must you speak misleading words to this pair of [young]females?!"
    s "What did I do wrong? You invited me on a date to the diner, didn’t you?"
    k "Before I knew what the meaning of a human-date was!"
    r "It was a {i}human{/i} date, too?!"
    s "What else would it even be, Rin?"
    r "I don’t know but I’m still jealous!"
    f "Uhh...like I was asking, are you and this girl perhaps...in a relationship, Sensei?"
    s "N-"

    scene rinfutababistro9
    with dissolve

    k "Yes."
    s "Oh."
    f "...Pardon?"
    k "We are in a relationship."
    s "Kaori, I don’t think that’s what Futaba means."
    k "Silence, Friend. I may not be advanced in terms of conversation yet, but even I understand the meaning of the word “relationship.”"
    s "Do you really, though?"
    f "Umm...could you maybe explain what...{i}type{/i} of relationship the two of you have?..."
    k "All I will tell you is that it involves a lot of meat."

    scene rinfutababistro10
    with dissolve

    r "How far have you two gone in such a short amount of time?!"
    f "A lot of...meat?! Then...that means-"
    k "Only I can handle this man’s meat. "
    k "If you attempt to challenge me, you will be destroyed."

    scene rinfutababistro11
    with dissolve

    r "OH GOD I’VE MISSED SO MUCH!"
    f "S-Sensei! Does she really...h-h-h-h-handle your...meat?..."
    f "And if she does then...w-w-w-why is she so...up-front about it?!"
    k "Go on, Friend! Explain to the stripey-girl how quickly the hot meat comes when I am the one handling it."
    s "…"

    scene rinfutababistro12
    with dissolve

    r "Wow! Is it, uhh...getting kind of hot out here? It is, right? So hot...Hahaha...hah..."
    k "Friend! Explain the circumstances!"
    s "On second thought, why don’t you just show them, Kaori?"

    scene rinfutababistro13
    with dissolve

    f "Show us?! R-Right now?!"

    scene rinfutababistro14
    with hpunch

    r "YES. RIGHT NOW."
    f "…"
    k "…"

    scene rinfutababistro15
    with dissolve

    r "Oh. Umm..."
    r "Sorry."
    r "Got a little carried away there."
    r "I’m good now."
    f "I’m...surprised by how open you are to this, Rin..."
    r "Open to what? I’m just hanging out and eating sushi with my best friend, my teacher, and one of the hottest girls in Kumon-mi."
    r "I mean Kaori. Who I am totally not attracted to."
    r "Unless she wants me to be."
    r "In that case, I totally am."
    k "I know not what this talk of attraction is, but I will now make the necessary preparations for the meat."
    k "I will return in roughly one human-minute."

    scene rinfutababistro16
    with dissolve

    "Kaori gets up and basically sprints away from the table, disappearing into the kitchen."
    "A series of extremely loud noises follows as she...makes the {i}necessary preparations...{/i}"

    f "Sensei...I don’t know if I’m comfortable watching this..."
    f "Especially...outside..."
    r "Umm, okay. So, I’m obviously not experienced in this department, but...what preparations need to be made, exactly?"
    r "I thought it was as simple as just kinda...you know, tugging it a little. And stuff."
    r "Also, is it okay if I take my phone out for this? Just for research, obviously."

    "You know, as...difficult as Kaori is to understand at times, I’m glad she’s able to create moments like this."

    if bonus == True:
        "One simple misunderstanding has lead me to discovering that one of my students wants to film me receiving a handjob-"
        "And the other is blushing like a maniac and seems to be more worried about being caught than someone else actually touching me."
    else:
        "I just wish they'd be less suggestive, because even if they are only jokes, that sort of conduct makes me feel rather icky."

    k "The meat has come!"

    scene rinfutababistro17
    with hpunch

    r "The meat has come!~"

    scene rinfutababistro18
    with dissolve

    r "Wait, already? But she didn’t even..."

    scene rinfutababistro19
    with dissolve

    k "Hehehehe...feast your eyes upon the magnificence that is the Queen of Spiders!"
    k "I informed you pitiful humans of my skills, and yet you continued to doubt me!"
    k "The man is mine! The meat has come!"
    r "Ha...hahaha...the meat...has come..."
    r "Hahah...haha...hah...hah..."
    r "Kill me."
    f "This...is a bit of a shock."

    scene rinfutababistro20
    with dissolve

    k "Your enormous breasts can not compete with my meat-handling abilities."
    f "…"
    f "Can you call it something else, please?"
    r "The meat...has come..."
    s "Well, now that that’s out of the way...Kaori, this is Futaba. Futaba, this is Kaori."
    f "Yes...she introduced herself earlier when we ordered..."
    f "Before I was made aware of how frequently she...handles your meat."
    s "Didn’t you just ask her to stop saying that?"
    f "I honestly don’t even care anymore. I’m going right to sleep when I get home."
    s "Yeah, I’m pretty sure Rin is too."
    r "The meat..."
    r "It..."
    r "It came..."

    scene rinfutababistro21
    with dissolve

    f "Yes it did, Rin."
    f "Yes it did."

    scene rinfutababistro22
    with dissolve

    k "Friend!"
    k "Did I do a good job? "
    s "You did a very good job, Kaori. You just need to work on how you make the other girls feel."
    k "But you are {i}my{/i} friend."
    s "I’m their friend too. And their teacher."
    k "I understand. But you are {i}my{/i} friend."
    s "Is there something about having multiple friends that confuses you?"
    k "There are many things that confuse me. Humans are strange."
    k "I just don’t want you to get too many friends and forget about me."

    "Oh no."
    "I think my heart might have just...felt something."
    "I didn’t realize it could do that."

    s "I’m not going to forget about you if I get more friends, Kaori."
    s "Actually, I’m pretty sure it wouldn’t be possible to forget someone as...unique as you in the first place."
    k "Will trusting your words make me a better friend?"
    s "I think that’s how it normally works, yes."
    k "Then I will do as you tell me."
    k "But the second you demand I remove my clothes, I draw a circle."

    scene rinfutababistro23
    with dissolve

    r "Okay, I’m back."
    s "I believe the phrase you’re looking for is “Draw the line,” Kaori. And I’m not going to demand that you remove your clothes."
    k "Good. Because your eyes ignited like fire when cute-skull-girl informed you of my instant gram."

    scene rinfutababistro24
    with dissolve

    r "BRB DYING AGAIN. KAORI CALLED ME CUTE."

    s "I still don’t understand why you set that account up if you were just going to delete it."
    k "I do not understand why you like hot meat sandwiches so much, but I do not try to change you."
    k "I enjoy you the way you are! Seemingly normal and slightly kind! And good at selling humans!"
    k "This may come in handy!"
    s "I’m not good at selling- Wait, why would that ever come in handy?"
    k "You will have to tell me. You are the experienced one. "
    k "I just serve food and beverages."

    "Wait a second."
    "Food and beverages..."
    "I was just thinking about Kaori earlier when I told Sara and Haruka about the “two and a half bartenders” I know."
    "Maybe they’ll be okay with receiving half of a bartender after all?"

    s "Kaori, what are you doing tonight? "
    k "Counting the rocks outside of my apartment. Why do you ask?"
    s "I was wondering if-"
    s "Wait, what?"
    k "...?"
    s "..."
    s "I was wondering if you’d want to come work at a bar."

    scene rinfutababistro25
    with dissolve

    k "But I already work at a bar. Wouldn’t that be a...conflict of insect?"
    s "Conflict of interest. And yes, I guess it kind of would be."
    s "But you work at multiple restaurants, so I don’t see what the big deal is."
    s "It would just be for tonight. A friend of mine is having a Halloween party and needs someone to cover the counter."
    k "But I already told you that you can’t have any more friends."
    s "Didn’t we move past that?"
    k "Oh, yes. We did. I accept your apology."
    s "You’re the one who is supposed to- Actually, never mind. Can you do it or not? I kind of told them I’d find someone to help."
    k "Can you first explain what a Halloween party is? This is not a combination of words that I am familiar with."
    s "It’s just...a party for Halloween."
    k "What is a ‘Halloween?’"

    scene rinfutababistro26
    with dissolve

    r "Halloween is like...an event where people dress up in costumes and get drunk and...eat and stuff."
    k "Costumes? Why would they do that?"
    r "I think it’s something about...celebrating the dead? Maybe?"
    k "Why would we celebrate the dead? They are dead. They can not dance or consume dizzy-drinks."
    f "Where did you find this girl?"
    f "Is she even human?"
    s "I honestly haven’t figured that out yet."

    scene rinfutababistro27
    with dissolve

    r "Uhh...could I get a little help here?"
    k "Friend, what is so special about dead people? What is the need to celebrate them?"
    k "Do I need to acquire a costume to work at this bar?"
    s "I’m just going to answer the last question because the first two are a little too heavy for me."
    s "You don’t need a costume. You just have to grab beers out of the cooler and pour glasses of wine."
    k "I can accomplish these tasks."
    k "But I ask for one thing in return."
    s "If it’s to be paid, I’m pretty sure the bar-owner is going to handle that."
    k "I require no money."
    k "But I would like to go for a walk with you."
    s "Oh. Well, yeah. That’s easy enough. I can do that."
    s "When?"

    scene rinfutababistro28
    with dissolve

    k "In seventeen minutes and twenty-three seconds when I get off of work."
    s "Why do you know the exact amount of time?"
    k "I know many specific things!"
    k "Like how many threads are in my bed sheets! And how many calories are in a pint of frozen milk-sweets!"
    s "Ice cream. And those are things that are printed on the containers they come in."
    k "Will you walk with me or will you betray my trust?"
    s "Sure, Kaori. I will wait the seventeen minutes and-"
    k "Sixteen now."
    s "I will wait the sixteen minutes and go for a walk with you."

    scene black
    with dissolve2

    "Kaori smiles and pushes my burger (That I apparently have to eat now) closer to me before running back into the bistro."

    if bonus == True:
        "Futaba and Rin both glare at me with extremely confused looks on their faces before sighing to themselves and remembering that I will willingly spend time with any female despite their...curiosities."
        "Actually, it’s possible that Rin was only sighing due to jealousy. But Futaba was definitely sighing out of pure exhaustion."
        "I can’t blame her, though."

    "Just being around Kaori is enough to tire most people out."
    "Which is exactly why I close my eyes and take several deep breaths as I step away from the table with Rin and Futaba."
    "From here on out, the day is only going to get more tiring."
    "But I guess that’s just the tradeoff you get in exchange for time alone with an adorable, probably-human (???) girl."

    stop music fadeout 5.0
    $ renpy.end_replay()
    $ halloween3 = True

    "………"
    "……"
    "…"

label halloween4:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```