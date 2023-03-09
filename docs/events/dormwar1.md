# Super Mega Ultimate Dorm War!
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar1&go=Go)


Part of event chain [Operation: Firestarter](./day318.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwar1
* Group: Main
* Triggered by label: day318

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label dormwar1:
    scene dormdecisions1
    with dissolve
    play music "normalday.mp3"

    mak "Have any last words before your team is completely and utterly annihilated, Uta?"
    u "Look at you. The contest hasn’t even started yet and you’re already getting full of yourself."
    u "And to think I once acknowledged you as a fellow glasses person."
    mak "Oh please. I was wearing glasses before you were even born."
    u "Oh yeah? What month were you born in?"
    mak "December. "
    u "And I was born in August, so that clearly wouldn’t be possible."

    scene dormdecisions2
    with dissolve

    mak "Of what year, though? Because I could still technically be eight months older than you."
    u "[[redacted]."

    scene dormdecisions3
    with dissolve

    mak "Wait, but if we were both born in [[redacted], that would mean..."
    u "{i}I’ve{/i} been wearing glasses since before {i}you{/i} were born! Take that, smart girl!"
    mak "But...you’re so short..."
    mak "Are you really older than me?"
    r "Hey, is it just me or did anyone else hear them redact the year they were born?"
    o "Yeah, I heard that too. That was weird."
    u "Size has nothing to do with age, Makoto."
    u "But also, I didn’t start wearing glasses until middle[school], so you probably win if you’ve really been wearing them for that long."

    scene dormdecisions4
    with dissolve

    c "Wait, so does this mean the first floor gets a point?"
    c "I can’t tell if they’re holding their own contest right now or not."
    n "I think we’re still deciding on the contests now. "
    n "They’re just being weird and arguing with each other about glasses because like only three girls in our class wear them."
    n "Which also means the second floor girls would win if we added up the time Nodoka’s spent wearing them, so..."
    n "Actually, maybe this is the first contest. That’s fine by me."
    i "Excuse me. I have a question."
    u "Yes! Io! This is the first time I’ve ever heard you call out in class."
    i "Can I be excused? I don’t want to be a part of...whatever this is."
    y "Yeah, me neither. I don't even know what the fuck is going on right now."

    scene dormdecisions5
    with dissolve

    c "You’d have a much easier time following along if you were here for the first part of class."
    y "I had shit to do. And if I knew we were gonna be doing some weird group thing, I wouldn’t have shown up at all."

    scene dormdecisions6
    with dissolve

    u "You may {i}not{/i} be excused, Io. Not until we figure out who you’re going to be competing against."
    i "Why do I have to compete against anyone? I’ve made it very apparent that I would like to be left alone forever."

    scene dormdecisions7
    with dissolve

    u "Because {i}all{/i} of us need to be involved or it won’t be a true bonding experience! Can you at least {i}try{/i} participating? For me?"
    mak "I suppose I wouldn’t mind Io bailing out of the competition, but it would give my floor one extra point by default, so-"

    scene dormdecisions8
    with dissolve

    u "Hey! Yumi said she wasn’t going to participate either, so if we’re doing things that way-"

    if bonus == True:
        mak "Yumi will absolutely participate because, if she doesn’t, I have a complete log of her absences that I will be forwarding to the principal. "
    else:
        mak "Yumi will absolutely participate because, if she doesn’t, I have a complete log of her absences that I will be forwarding to the principal, which Kumon-mi College has in place of a dean."
        s "Thank you for clarifying, Makoto."

    y "You have what?! The fuck?!"
    mak "Heheh...I was wondering when this would come in handy."

    scene dormdecisions9
    with dissolve

    i "Soooooo..."
    u "Iooooooo...pleeeeeeeeease?"
    u "I’ll never ask you for anything ever again."
    i "I am absolutely not going to believe that. Sorry, Uta."
    y "And I absolutely don’t give a rat’s ass about {i}what{/i} you do with my fuckin’ “absence list.”"
    y "The fuck’s the principal gonna even do? If he tries to start somethin’ I’ll just kick his ass and be done with it. Easy."
    mak "Sure, if you want to get kicked out of[school] at age [[redacted], feel free to do exactly that."
    r "Woah. There it is again. "
    o "How is she doing that?"

    scene dormdecisions10
    with dissolve

    u "You know...maybe we could just put those two up against each other?"
    mak "I don’t know if it’s a good idea to ask our classmates to engage in combat."
    y "Actually, yeah. That sounds fine. I’m in."
    i "I am not in. Not at all. She’s twice my size and I don’t even like fighting."
    ay "Woo! Io surrenders! One point goes to the first floor!"
    u "I didn’t mean making ‘em fight...I was thinking something more like whoever can get one of them to join in on the fun first wins."
    u "It would also save us some time since it would take place over the entire contest rather than a set time and place."

    scene dormdecisions11
    with dissolve

    mak "That works for me. Yumi’s shown up to several class functions in the past, so it shouldn’t be {i}too{/i} hard getting her to do it again."
    y "Wait, so we’re not fighting?"
    c "No. Pay attention. "
    y "Well then what the fuck? I don’t want to do this anymore."
    u "It’s settled then. Our first of ten battles will be the wallflower cooperation contest! Whoever does something with the rest of us first wins!"
    mak "Done."
    mak "And I actually already have something in mind for the next contest."
    u "Ooooooh, what is it? Something glasses based?"

    scene dormdecisions12
    with dissolve

    mak "There’s more to me than just my glasses, you know. I have interests and stuff."
    u "Some sorta test of knowledge thingy then? "
    mak "Well...yes. A standard test of knowledge would be more than sufficient in determining which floor excels in at least {i}that{/i} area."
    u "Fine by me, but I think you might be bitin’ off a little more than you can chew here."
    u "I know you’re smart and all, but we’ve got a bit of a prodigy on our floor."

    scene dormdecisions13
    with dissolve

    mo "And from out of the darkness emerges the true secret weapon of the second floor. The unending fountain of knowledge that is Molly MacCormack."
    mo "Blessed with the gift of foresight...experienced in all forms of trials and tribulations...is a mystical warrior of emerald, ready to carry her clan to the next-"

    scene dormdecisions14
    with dissolve

    no "I’ll do it."
    mo "Wha-?!"
    a "Molly, you didn’t really think Uta was talking about you, right?"
    mo "Why wouldn’t she be?! I’m smart! Very smart! "
    mo "How much could Nodoka possibly know about the dark arts?!"
    m "Why did your mind immediately go to “the dark arts” after hearing “test of knowledge?”"
    u "And there she is! Our savior!"
    mak "Heh. I was wondering if you’d volunteer."
    mak "I‘ve looked into your history and know you have the upper hand when it comes to test scores, but to agree to face off with me directly is-"

    scene dormdecisions15
    with dissolve

    no "Oh, I’m not trying to prove I’m smarter than you or anything. I really don’t care about that."
    no "I just want to avoid doing anything physical, so this is probably the best bet for me."

    if bonus == True:
        no "Also, I wouldn’t mind sleeping in the same room with Sensei as it means there is a higher likelihood of something {i}exciting{/i} happening."

        scene dormdecisions16
        with dissolve

        f "Nodoka..."
        a "There sure as heck isn’t!"
        ay "Unless our floor wins. Then there is a very high likelihood of-"
        a "Ayane! Not now!"

    scene dormdecisions17
    with dissolve

    u "Cool! So now that we’ve got two contests out of the way, how about we handle the other basic skills before gettin’ into the weird stuff?"
    n "I volunteer for the weird stuff! "
    n "Like, who can stay in a locked room with Sensei without any food or water for the longest?! I want that contest!"
    ay "I accept this challenge! I was born for this!"
    u "Ummm...no!"
    u "We’ll get to the weird stuff in a sec, but since we already have a test of knowledge going, why not try for a test of courage?"

    scene dormdecisions18
    with dissolve

    t "What is a test of courage?"
    t "Are you going to tie our hands behind our backs and force us to walk the plank of a pirate ship?"
    mak "Why would you immediately assume that is what a test of courage is?"
    mo "Apologies, but the Kendo Princess and I watched the Pirates of the Caribbean series recently and she is now strangely obsessed with pirates."
    t "Shivering timbers. Hoist up the delightful Roger."
    a "Maya, if it’s a test of courage, why don’t you volunteer?"
    ay "Yeah! You’re basically emotionless, so I think you’d be great."
    m "Isn’t Sensei supposed to be the judge? How will he score a test of courage?"
    mak "Huh...I mean, I guess he doesn’t {i}have{/i} to be the judge of every category, does he? "
    mak "The contest between Nodoka and me will have a clear victor, so he probably doesn’t need to be involved in that either."
    u "I’m fine with some Sensei-less fights. Especially since Sensei would probably be biased toward Maya anyway."
    n "Agreed. "

    scene dormdecisions19
    with dissolve

    m "He would be biased {i}against{/i} me, is what I’m going to assume you meant to say. "
    m "I don’t want to be involved in any contest where he is the judge because it will put my team at a disadvantage."
    t "I also volunteer to join the pirate contest."
    mo "No pirates, Kendo Princess."
    mo "A test of courage is where you have to try not to get scared. And Maya’s stat in courage is extraordinarily high, so she will be quite the adversary."
    t "Argh."
    mo "Tsuneyo Tojo accepts the terms and will compete regardless."

    scene dormdecisions20
    with dissolve

    mak "I think that’s settled then. Though, I wasn’t thinking we meant things like “bravery” when we began tossing out the ideas of tests in basic ability."
    u "Fear is something we’ve all gotta deal with, Makoto. And besides, it’s a lot more interesting than two nerds trying to be smart at each other."

    scene dormdecisions21
    with dissolve

    mak "Well forgive me for trying to make things competitive! At least I’m not suggesting locking ourselves in a room with someone and competing over that!"
    n "Oh! Me! We’re at my competition!"

    scene dormdecisions22
    with dissolve

    ki "If you want something involving basic skills or whatever, why not put two of the athletic girls against each other?"
    mi "Woah, Kirin. You actually takin’ an interest in stuff like that?"

    scene dormdecisions23
    with dissolve

    ki "What do you mean, “taking?” We’ve been playing soccer together for how long now?"
    mi "A while, but you’re always spendin’ practice on your phone or talkin’ to Sensei."
    mak "No offense to you, Kirin...but are you really sure that’s the sort of competition you want to suggest?"
    mak "I’m sure Miku would be willing to go up against you, but I can’t help but think you’d be at a disadvantage due to Miku’s...natural talent."

    scene dormdecisions24
    with dissolve

    mi "Hey! Ain’t nothin’ natural about it! I work really hard!"
    ki "And {i}I{/i} would like to prove that I’ve been working plenty hard outside of practice."
    ki "I just prefer to work out on my own."
    ki "Besides, even if I lose, I’ll be going up against somebody I like. "
    ki "And if this whole thing is gonna be about bonding or blah blah blah, it only makes sense to compete with someone you care about."
    mak "And Miku? You’re okay with this challenge?"
    mi "Yeah, but...now I feel kinda bad for sayin’ Kirin wasn’t interested."
    mak "Well, as long as you don’t plan on taking it easy on her, I’m sure everything will be fine."

    scene dormdecisions25
    with dissolve

    ya "What do I get to do?"
    u "Oh, Yasuyasu! You actually want to participate?"
    ya "It sounds fun, but I’m afraid I’m not very good at many things."
    u "That actually works out just fine! Cause I kinda had a thing already in mind for you and Sana."

    scene dormdecisions26
    with dissolve

    sa "Wha-"
    sa "Me?!"
    r "Unless you changed your name recently."
    r "Actually, if you change your name now, there might still be a chance to get out of this."
    sa "But...But I..."
    sa "I don’t really...know her...and..."
    sa "I didn’t really think I was...involved in this..."
    r "Sana, everybody’s involved in this."
    r "Besides, I’m sure whatever it is will be totally normal and not embarrassing at all. So you’ll just be able to cruise by."
    u "Yasuyasu, you and Sana will be facing off against each other in a gothic lolita fashion show."

    scene dormdecisions27
    with dissolve

    sa "AHHH!"
    r "Or it will be insanely embarrassing and you’ll just have to deal with it because I want to see you in cute clothes. Sorry, not sorry."
    o "Is Sensei going to be the only judge for that contest or are there going to be others involved as well?"

    scene dormdecisions28
    with dissolve

    u "He’ll be the only judge, but we can all get involved in any way we want."
    u "Sana and Yasuyasu are kinda like Yumi and Io. They’re pretty quiet most of the time and I figured they might need a little push and some help from the rest of their team."
    u "So all you two really need to do is keep on bein’ cute and we’ll use you as our final projects! It’ll be kinda like the main event of the whole thingie."
    mak "The two of them do wear nothing but dresses outside of[school] so...I can see this being a pretty even contest."
    o "Couldn’t Sensei just play favorites for that, though? "
    o "If he’s the judge, what’s going to stop him from just picking the girl he thinks is hotter or whatever?"
    no "Isn’t that the whole point? Just be quiet and accept that you’re going to have to see cute girls in cute clothes. Woe is you."

    scene dormdecisions29
    with dissolve

    if rinbetrayed == False:
        r "I don’t think we need to worry about him being biased or anything. He’s normally pretty good about not doing that."
    else:
        r "I don’t think we need to worry about bias as long as it’s those two we’re talking about."
        r "Don’t know if I can say the same for some of the others, though. Not with his history."
        a "Wait, what? What history?"
        f "Hah..."

    mak "Well, while there’s no way to guarantee that there is no bias involved, there are preventative measures we can take to ensure that it does not happen in every contest."
    u "Exactly! Which is why another brilliant idea just popped into my head! One that is the complete opposite of Sensei choosing girls he likes the most."
    u "Are you thinking what I’m thinking, Makoto?!"
    mak "Probably not, Uta."
    u "Friend zone battle!"

    scene dormdecisions2
    with dissolve

    mak "...What?"
    u "Did you know that they used to call me the “girl whisperer” in middle[school]?"
    n "No one ever called you that. We went to middle[school] together."

    if bonus == True:
        n "They did talk about your boobs, though."
    else:
        n "They did talk about your crossbow, though."

    u "And they likely will forever. I have already accepted this. "

    if bonus == True:
        mak "Yes. You have large breasts for such a small girl. But what does that have to do with the friend zone?"
    else:
        mak "Yes. We all know about your crossbow. But what does that have to do with the friend zone?"

    u "Absolutely nothing. But what I’m saying is if we’re so worried about Sensei’s biased judgement, why not put the girl who thinks he won’t be biased at all up against the one who’s sure he will?"
    mak "You mean Rin and Otoha?"
    u "Yeah! We already know that neither of them have any romantic feelings for him, so there’s literally nothing to lose."
    f "Is that...really a thing we know?"

    scene dormdecisions30
    with dissolve

    r "How would a friend zone battle work exactly?"
    r "Cause if we’re playing that game where we try to not get nervous and slowly move our hands closer and closer to each other’s-"
    o "Yeah, I don’t really think that’s what they’re going for, Rin."

    if rinbetrayed == False:
        r "Okay, good. Because I’m pretty sure I would not last very long."
    else:
        r "Okay, just making sure."

    u "Basically, we put the two of you at different tables and just let Sensei run wild."
    n "Hi, Noriko again. Is there any rule against competing in more than one competition?"
    ay "Hey, Ayane here. Same question."
    no "Hi, Nodoka speaking. Is there any rule against filming this “running wild” that you speak of?"
    mak "Um, hello! Makoto’s turn! Can you all be quiet so we can figure this thing out?"
    u "Is it not figured out already? Just put ‘em at a table and whoever lasts the longest without flirting back wins."
    u "And no, Noriko and Ayane. You can’t compete because you’d both lose immediately."
    n "You know, that’s fair. I get it."
    ay "I just texted him a winky face so I probably lost already."
    n "Ooh! I should send him one too!"
    o "If all we’re doing is just...not flirting with him, yeah. I’m down for that."
    r "I’ll probably make things so awkward that he won’t even want to flirt with me. So yeah, count me in too."

    scene dormdecisions31
    with dissolve

    ay "Uta, are we still doing the thing we said we were gonna do before this contest was even official?"
    ay "Because if so, I want to apologize in advance for ruining our friendship."

    scene dormdecisions32
    with dissolve

    mak "Oh right. You two have been planning this for a while, haven’t you?"
    mak "What sort of contest did the two of you have in mind for each other? "
    u "Well, it wasn’t originally part of the contest thingy, but Ayane and I have been talking about freestyle rap battling each other since I transferred in."
    mak "…"
    mak "Why?"
    u "Why not?"
    mak "…"
    mak "What?"

    scene dormdecisions33
    with dissolve

    u "Oooooookay! So with the rap rampage added to the list, that leaves us with six girls who have yet to be matched up!"
    mak "Correct. From the first floor, we still have Ami, Futaba, and Chika."
    u "And from the better floor, we have Touka, Noriko, and I guess Molly."
    mo "What do you mean, “you guess?!” Why are you so mean to me today?!"

    scene dormdecisions34
    with dissolve

    mo "Regardless, if we’re bringing past discussions into the debate...I, too, have a suggestion for the battle between Futaba and me."
    f "You do?"

    scene dormdecisions35
    with dissolve

    mo "Yes. Several months ago, you made an offhand comment about how Sana’s Zagull Throat Spear could defeat my monk in one on one combat, to which I was very offended."
    mo "I intend to make you pay dearly for those words and hereby challenge you, Futaba Fukuyama, to put your gil where your mouth is and prove it."
    t "Gills are near the mouth, but not on them, Emerald Guardian. You are thinking of “teeth.”"
    mo "Silence, Tsuneyo."
    f "Um...I mean...if there’s nothing else we can think of..."
    f "I guess I'm okay with that..."
    u "One more down! Two to go!"

    scene dormdecisions36
    with dissolve

    c "You feeling okay, Touka? You’ve barely said anything since class started?"
    to "Huh? Yeah. I’m okay."
    to "I’m just not really sure what’s happening right now."
    to "I’ve heard of group activities before, but from what I heard, it sounded like there’s normally a teacher involved."

    scene dormdecisions37
    with dissolve

    c "Well, hey. How about this? I already know what kind of contest I want to be in, and I’d be happy for you to compete as well."
    c "I'd just need to know that you’re not going to try anything sneaky."
    c "And also that you’re not secretly in love with our teacher."

    scene dormdecisions38
    with dissolve

    to "Wha?! Of course I’m not! That’s absurd!"
    c "Great! Then-"
    u "Hey! The heck are you sayin' to my teammate that’s gettin’ her all flustered back there?!"
    u "Know your place, woman!"

    scene dormdecisions39
    with dissolve

    c "Touka and I want to go on a date with Sensei!"
    ki "Get in line. Like half the reason we’re even having this contest is because all of us want that."
    ki "You shouldn’t get him just because you shouted it out loud."
    n "If it worked that way, Sensei and I would be on a romantic getaway in Kyoto right now."
    to "I...didn't say I wanted to..."

    scene dormdecisions40
    with dissolve

    u "Uhhh...thanks for sharin’ and stuff, but that’s not really a thing we’re talkin’ about right now."
    u "If you want to go on a date or whatever, just ask him."
    c "No, no, no. Like a contest to see who can throw the better date."
    c "You guys can even come watch to make sure nothing weird happens."
    c "Not like it ever {i}would{/i}, anyway. Sensei’s like, waaaaaay above that."
    mak "Which Sensei? Our Sensei? "
    mak "Is this a joke?"
    c "Come on, Makoto! Don’t you want to win?"

    if bonus == True:
        mak "Well, yes. But not if it means breaking[school] rules and subjecting students to anything inappropriate or-"
    else:
        mak "Well, yes. But not if it means participating in anything inappropriate or-"

    c "Oh, speaking of inappropriate, I could have sworn I saw you walking out of some seedy looking shop the other day. "

    scene dormdecisions41
    with dissolve

    c "I’m not really sure what kind of place it was. But it would certainly seem really inappropriate if our class rep was spending time in some-"
    mak "Wait! Okay, yeah! I’m fine with the contest thing so long as we can supervise it!"
    u "You hangin’ out in weird places, Makoto?"
    mak "No...she must have me confused with someone else."
    mak "I have...one of those faces, I guess."

    scene dormdecisions42
    with dissolve

    a "So...I guess this means it’s me and Noriko up against each other?"
    u "It looks that way, but...I’m kinda out of ideas on what we could have you do."
    mak "Yeah...I don’t really know what we could do for the two of them either."
    mak "And we are absolutely not going with Noriko’s idea of locking them in a room together."

    scene dormdecisions43
    with dissolve

    n "Ami, what do you and I have more in common than anything else?"
    n "Just think. It’s not hard."
    a "Well...I obviously know the answer, but I don’t really like the idea of competing over it."
    a "I don’t like Chika’s contest either, but since there are going to be other people there, I can’t really do anything about it."
    n "Then let’s do something of our own! We can have chaperones too!"
    n "I certainly don’t care about anyone seeing me with Sensei, do you?"

    scene dormdecisions44
    with dissolve

    a "I’d actually {i}prefer{/i} if people saw me with Sensei. It would make so many things significantly easier."
    n "Great! Then, how about a...best [niece] battle or something?"

    if bonus == True:
        a "Are you on drugs? You’d have absolutely no chance of winning."
        a "I am the ultimate [niece]. I exist to please my [uncle]. "
    else:
        a "Are you on drugs?"
        n "No. But your pogchamp will be soon."

    o "Uhh...what?"
    no "Is it getting hot in here, or...?"

    scene dormdecisions45
    with dissolve

    n "What about...an imouto war?"

    if bonus == True:
        n "Do you think you could function as a little sister instead of a [niece]? Or are you so used to your current power dynamic that you’d crumble under the pressure?"
        a "I think that any competition involving my relationship with Sensei would be a death sentence for anyone stupid enough to challenge me."
        a "But if you insist, I wouldn’t mind crushing you and leaving you to rot in one of the dumpsters on the side of our house."
    else:
        a "That's a stupid fucking idea. Patreon would never allow that."
        a "Go jump off a bridge, Noriko."

    scene dormdecisions46
    with dissolve

    n "Isn’t that a little harsh? I’m just trying to get closer to you over a little friendly competition. "

    if bonus == True:
        n "He’s like family to me, so it also makes you kind of like a sister and-"
    else:
        n "I've always thought of him as an older brother and-"

    a "Blah blah blah. I accept your challenge."
    a "But you should probably apologize in advance to your team for losing them the opportunity to sleep in the same room as my [uncle]."

    scene dormdecisions47
    with dissolve

    u "…"
    mak "…"
    u "Okay. Well, that was weird. But I’m pretty sure we have all of our contests now."
    mak "Yeah..."
    mak "So...just to clarify, what are the two of them going up against each other in?"
    u "I think it’s like...a fight to see who the better little sister is?"

    if bonus == True:
        u "But Sensei is like, way older than both of them. So for them to even be his little sisters would mean his mom and dad are still gettin' freaky like, way late in life."
        u "But I guess my parents still get it on too, so-"
    else:
        u "But in a way that doesn't have any bad stuff so Patreon will still be okay with it."

    scene dormdecisions48
    with dissolve

    mak "Okay! Well, uhh...class dismissed!"
    mak "If you signed up to be a commentator, please go retrieve the necessary equipment from the broadcasting club and be sure to put down your name and the exact items you took!"
    mak "The competition begins bright and early tomorrow, so feel free to spend the rest of the[school] day and any time afterward strategizing."
    u "Wow, it’s like you don’t even want to hear about my parents knockin’ boots. You’re even more of a prude than I am."

    scene dormdecisions49
    with dissolve

    mak "I can absolutely not wait to destroy both your team and you..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ dormwar1 = True
    stop music fadeout 5.0

    "………"
    "……"
    "…"

label dormwar2:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
ay "It should be okay that way, right?"

    scene thisiswar22
    with dissolve

    mak "...Me?"
    ay "Sure! Why not? "
    ay "You already lead the classroom and you’re the student council president, so you definitely have the experience."
    ay "Besides, we’re going to win either way, so it doesn’t really matter {i}who{/i} the captain is."
    mak "Well...I suppose it does sound like a good bonding experience. And the second floor could certainly use that given that they’re all still relatively new here."
    mak "But...the winners would need to get something to make it worth while. Wouldn’t they?"
    mak "Otherwise, it’s just a waste of time and-"

    scene thisiswar23
    with dissolve

    u "Oh, we’ve already decided on what the winner gets."
    ay "And it’s a lot more than just bragging rights."
    u "That’s right, Ayane...In fact, it’s the most sought after award in the[school]."
    sa "S-Sought after?..."
    sa "Then...wouldn’t that mean..."

    scene thisiswar24
    with hpunch

    u "THE WINNER GETS SENSEI!"
    s "What?"
    m "Is it too late to drop out of the contest?"
    o "Yeah, I can sit this one out too. Give him to somebody else."
    s "What the fuck?"
    u "Specifically, whichever floor wins will get to keep him in their room for the upcoming beach trip."
    u "So you better start packin’ your PJ’s now, Sensei. You’re gonna be with us second floor girls whether Otoha likes it or not."

    scene thisiswar25
    with dissolve

    c "Oooooh, that {i}is{/i} a good reward."
    n "How do we win?! What do I do?! What is the dress code for the sleepover?!"
    c "You can’t win. "
    c "Us first floor girls have been with Sensei much longer than any of you. "
    n "Sounds to me like somebody is forgetting {i}I’ve{/i} been with Sensei longer than anyone except for like, Ami I guess."
    n "I don’t care if I have to carry the entire floor. I’m {i}going{/i} to win and I’m {i}going{/i} to get all up in his business at our swimsuit slumber party thingy."

    scene thisiswar26
    with dissolve

    c "Lay so much as a finger on him and you will die."
    n "Joke's on you. I'm perfectly content dying for that."
    n "You underestimate me, Chika."

    scene thisiswar27
    with dissolve

    ay "Are you okay with these terms, Sensei?"

    if bonus == True:
        a "He’s okay with them as long as our floor wins and he gets to sleep in the bed with me. "
        s "Better idea: What if all twenty-one of us just sleep in the same bed and-"
        u "No can do, Sensei. I appreciate you openly admitting that you want to sleep in the bed with me, even though I’ve known it all along-"
    else:
        a "He’s okay with them as long as my floor wins because there is a clause in our contract saying he can not live with anyone else, even if it is only for one day."
        s "There is?"
        a "YUP."
        s "Then I'm sorry Uta, but my path has already been laid out for me."
        u "No can do, Sensei. I appreciate how much you like your accountant, even if it is kinda weird-"

    u "But the show must go on and the combatants must be chosen."
    u "So please, here and now, surrender your rights and agree to room with whoever the winner of the contest is."
    s "I don’t really like calling it “surrendering my rights” but...if all that’s going to happen is me sleeping next to a bunch of girls, sure."
    u "Perfect!"
    u "Now, please exit the room so we can figure out who is up against who and blah blah blah logistical stuff."
    ay "You’re going to need the rest anyway, Sensei. These next two days are going to be action-packed, especially since you'll be acting as a judge for some of the competitions."
    s "I actually have to participate? I can’t just surrender myself and be done with it?"
    u "Oh you’ll be participating, alright. This contest can’t exist without you."
    u "Now get the heck out of my classroom so me and Makoto can start whippin’ our girls into shape!"

    if bonus == True:
        ki "I’m down to get whipped if Uta is offering. Sounds fun."
        r "I’ve never really looked at her like that, but I probably wouldn’t refuse if Makoto wanted to whip me as-"
        mak "No one is whipping anyone! But yes, Sensei, please vacate the premises."
        mak "It appears that Uta and I have quite a bit to talk about..."

    scene black
    with dissolve2

    "{i}Welcome to the first annual Super Mega Ultimate Dorm War!{/i}"
    "{i}The next two days will be completely filled with events featuring head to head battles between two girls from each floor.{/i}"
    "{i}Some events will have predetermined outcomes, but several of them have outcomes that you will be able to choose!{/i}"
    "{i}In the end, only one floor can be crowned as the winner!{/i}"
    "{i}So sit back, relax, and do the thing!{/i}"

    $ renpy.end_replay()
    $ day318 = True
    stop music fadeout 5.0

    "………"
    "……"
    "…"

    jump dormwar1
...
```