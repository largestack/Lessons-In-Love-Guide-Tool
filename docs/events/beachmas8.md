# A Thousand Truths
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachmas8&go=Go)


Part of event chain [Fetch Quest](./beachmas7.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: beachmas8
* Group: Main
* Triggered by label: beachmas7

## Event code
File: \game\chap3.rpy
Code:
```python
...
label beachmas8:
    scene beachmastod1
    with dissolve2

    mo "...and that’s exactly why I think school should be done entirely online and that requesting our presence is a waste of both money {i}and{/i} resources!"
    a "Something wrong, Maya? You’ve been staring at the door for a good twenty seconds."

    scene beachmastod2
    with dissolve

    m "Hm? What? No. I was just wondering when this stupid game is going to start since we’ve just been sitting in a circle for what feels like thirty minutes now."
    ay "..."
    ki "I’m with Maya! I would also like to get the game started!"

    scene beachmastod3
    with fade

    no "As would I. I had an absolute blast the last time we played truth or dare and I can’t {i}wait{/i} to see what wonders are in store this time."
    to "And while I am very happy for you, Nodoka, I {i}must{/i} remind you that you are forever banned from playing this game following your direct breach of both our trust and the rules last time."
    ki "She can watch, though. Right? We can rob her of the privilege to play, but we can’t {i}completely{/i} strip her of her freedom."
    no "You can all strip me in whichever ways you like. Though, I can’t guarantee I’d be the most fun person here to undress. I believe that role would have to go to-"
    to "It’s going to be me, isn’t it?"

    scene beachmastod4
    with fade

    no "Touka."
    to "Of course. "
    ki "That swimsuit {i}does{/i} look a little tight. Would you mind if I just reached over and-"
    to "I would, actually. And very much so, at that."
    ay "Hey, here’s a fun idea! How about we stop trying to strip Touka and indulge the wretched behaviors of the two most destructively horny girls on the planet and, {i}instead,{/i} play some truth or dare!"
    ki "She says, despite being equally as wretched and horny."

    if ayanelust10 == True:
        ay "My bad. Sorry for being {i}in love.{/i} Which is, crazily enough, a thing you will likely never feel!"

    scene beachmastod5
    with fade

    ay "So, we already know that Nodoka is banned from participating in any way, but there are a few other rules we need to get out of the way first so things don’t become horrible out of nowhere!"
    ay "First and foremost, nothing sexual! "
    ki "Laaaaame. "
    ay "You {i}may{/i} dare another girl {i}from this table{/i} to {i}kiss{/i} you if you absolutely must. But that girl has the right to veto said kiss and, if she does, your dare has been forfeit and the next person goes."
    ay "There are no limits to what sorts of truths you can ask for though."
    ki "Hey, I have a question. Why did we mutate a timeless classic like truth or dare into something so family friendly that even my fucking sister would play it?"
    a "Because most of us here are wholesome and only you and Nodoka are degenerates."
    mo "{i}Ahem.{/i} "
    a "And Molly. But she’s a different type of degenerate."

    scene beachmastod6
    with fade

    mo "‘Tis the truth. I’m the brand of degenerate that you’d be okay with introducing to your mother so long as I was briefed on what not to say beforehand."
    ay "And Kirin is the type who would fuck your dad."
    no "And {i}I{/i} am the type who would fuck your mother. Now, who’s ready to play? "
    a "Not you! That’s for sure!"
    to "Maya, you look a bit uncomfortable. Are you sure you do not want to leave the table before the game begins? No one will hold it against you."
    a "Hey, yeah. Why {i}are{/i} you here anyway?"
    m "Because my other plans apparently fell through. Now, can we begin?"
    ay "Go make them come true, then. Nothing’s going to happen by just sitting here."
    to "American movie star, Shia LaBeouf, always says to never let your dreams be dreams. I am with Ayane on this. And it is not only because we are both rich."
    ki "Gee, thanks for reminding us. I almost forgot. "
    a "Kirin, you’re the most reckless person here. Why don’t {i}you{/i} start?"

    scene beachmastod7
    with fade

    ki "Can someone else go first? I haven’t decided who I’m going to dare to kiss me yet."
    no "Perhaps it’s not too late to track down Noriko and have her join us for a round?"
    ki "Already tried. She won’t do it."
    to "Oh my. Is it against the rules to share truths before they’re asked of you? Because I don’t believe that was something we were meant to hear."

    scene beachmastod8
    with dissolve

    ki "You know what? I’ll save my dare until the second round. "
    mo "That is...assuming that person selects “dare,” correct? I’m not great at games that don’t involve controllers or touch pads."
    a "Correct. Kirin can’t just dare you to do something because she wants to. It has to be your choice."
    ki "For the millionth time, {i}lame.{/i} Ayane, truth or dare."
    ay "Well, I definitely don’t want to kiss you so...truth."
    ki "Do you actually believe it’s realistic that you and Sensei are going to get married and start a family one day?"

    scene beachmastod9
    with fade

    a "That is...way tamer than I expected from you."
    a "Also, I’ll answer for Ayane. She obviously doesn’t think that-"
    ay "Is that really all you want?"
    ki "Yeah. Is there a problem with that?"
    ay "I just figured it would be something more...{i}Kirin.{/i}"

    if ayanelust10 == False:
        ki "Just answer the question, Ayane."
    else:
        ki "Just answer the fucking question before I ask you something else like when the last time you masturbated was."

    scene beachmastod10
    with dissolve

    ay "I...I don’t really know. If you asked me that question a year ago, I’d probably have an entirely different answer."
    ay "But now, I barely even know if I’m going to make it to the end of each {i}day.{/i} Let alone so far off into the future that I have a career and kids and..."
    ay "Yeah..."
    ay "What I {i}can{/i} say, though, is...if any of that ever {i}does{/i} happen for me...I can’t imagine it being with anyone other than Sensei. So that’s all on him and whether or not that’s what {i}he{/i} wants as well."
    a "..."
    ay "..."
    a "{i}And also Ami because she makes the rules and you would need her blessing before doing anything as ridiculous as that.{/i}"
    ki "You want to fuck your uncle. We know."

    scene beachmastod11
    with dissolve

    a "You said it. Not me. "
    ay "Welp, I guess it’s my turn now, so..."

    scene beachmastod12
    with fade

    ay "Maya...truth or dare?"
    m "Are you sure I’m the correct target?"
    ay "Frankly, I can’t think of any better targets right now. And there are definitely some things I’d like to have you clear up."
    m "I see. And what better setting to do that than a table full of our peers who will have no idea what we’re talking about?"
    to "It’s true. I am quite lost right now."
    ay "Well...what’ll it be? Truth or-"
    m "Dare."
    ay "Oh. Oh, right. I just kind of assumed you were going to choose truth."
    m "I am, unfortunately, in a position where I will never choose truth."
    ki "Welp, that helps narrow down my list for the next go around. Now to figure out who would rather kiss me between Molly and Maya."
    ay "Umm..."
    a "Come on, Ayane. There’s gotta be {i}something{/i} you want out of Maya, right?"
    ay "Maya...I..."
    ay "I dare you to always look after Ami and Sensei if anything bad ever happens to me."

    scene beachmastod13
    with dissolve

    ki "God! You’re all so fucking boring! "
    no "To be fair, your question wasn’t much better."
    a "What do you mean “if something bad ever happens to you?” That’s really ominous and I don’t like it."
    mo "It’s the request of a seasoned warrior at the end of her days who wants nothing more than to watch the kingdom she used to serve flourish."
    mo "Maya is the next generation of the kingsguard and Ayane-"
    m "Molly, shut up. "
    m "Ayane, if anything bad ever {i}does{/i} happen to you, it will be precisely {i}because{/i} of that destructive brand of selflessness. "
    m "But regardless of that...I promise you, dare or not, that I will always protect the two of them no matter what happens. "
    m "You have my word."
    mo "And my bow."
    m "Molly, {i}please{/i} shut up."

    scene beachmastod14
    with fade

    a "Why do I want to cry now?! And why are my friends so sweet when they’re not trying to get with my guardian?!"
    mo "Let it be known that I, Molly MacCormack, have not attempted such a feat yet! At least not intentionally. But there was that one time in my room when-"

    scene beachmastod15
    with dissolve

    a "When what?"
    mo "Ah! Ami popped her racial ability that lets her get rid of all negative status effects once per day!"
    ay "Wouldn’t that make you the only person at the table {i}without{/i} that ability? Seeing as we’re all Japanese and whatnot."
    m "What is the Irish racial ability?"
    mo "One that lets me dodge a targeted character ability once per day! Which I will use right now to stop myself from telling the rest of my embarrassing and shameful bedroom story!"
    a "You absolutely will not-"

    scene beachmastod16
    with fade

    m "Molly. Truth or dare?"
    a "Oh, damn it, Maya! I was this close to figuring out if she needs to be added to my list or not!"
    ay "You still have that thing?"
    a "I will never get rid of it."
    mo "The great and powerful Emerald Guardian is no stranger to risk...so the only option for me to choose is dare!"
    m "Excellent. I dare you to never tell anyone about any strange or embarrassing stories involving you or Sensei ever again as I thoroughly enjoy having an appetite and do not want it permanently ruined."
    ay "You realize that can just be bypassed the next time someone uses a truth command on her, right?"
    m "Every second I can buy is worth a thousand truths."
    mo "A Thousand Truths sounds like a good guild name. Or an album title for a V-Kei band if you add a few more broody adjectives to the mix."
    mo "Like “A Thousand Bloody Screaming Truths in the Dead of the Night” or “A Thousand Angels Screaming Truths in...Blood.”"
    mo "Or something."
    m "I also dare you to never speak again."

    scene beachmastod17
    with dissolve

    mo "You really do sound like the Herald of the Adolescents at times, you know."
    a "Heheh...isn’t it great? It’s like I have an extra Sensei around whenever the first one forgets he’s supposed to love me every hour of every day."
    m "I have no clue what you’re talking about. But it appears that my time has expired so, please. Proceed."
    mo "Then...in that case..."

    scene beachmastod18
    with fade

    mo "Touka!"
    to "Present!"
    mo "Truth or dare? Choose your destiny."
    to "Truth!"
    to "But only because I know your degeneracy is nothing but a false label that others have plastered on you due to countless misunderstandings and I would like to give you a chance to prove your wholesomeness."
    mo "Gah! Thank you so much for your sweet and honeyed words! "
    mo "NOW FORGIVE ME AS I LAY WASTE TO THEM! MWAHAHAHAH!"
    to "Um...I beg your pardon?"
    mo "Favorite sex position! What is it?!"

    scene beachmastod19
    with dissolve

    to "Excuse me?!"
    ki "Ayyy! Molly coming in clutch! Maybe I’ll dare her to kiss me since I can’t dare Nodoka to do it."
    no "I’d refuse anyway. Your sister on the other hand..."
    mo "What is it, Touka?! What is thy position of choice?!"
    to "Umm...r...regular?"
    ay "I, too, am a fan of “regular style.”"
    mo "A {i}real{/i} position! Not one you made up!"

    scene beachmastod20
    with dissolve

    to "I don’t know! I was never taught their {i}names!{/i} No such terminology was included in {i}any{/i} of the Powerpoint presentations I watched on the matter!"
    to "And why did I have to be the one who was assaulted with the first lewd question of the night when I am inarguably the most wholesome person at this table!"
    no "Strange. Am I wrong in remembering you asking Makoto something similar last year?"
    to "Yes! You Are!"
    ki "Touka, the lewd questions are the best part of the game. Just answer."
    to "They are not! And I already did!"
    ay "How about this? You don’t need to know the {i}name{/i} of the position so long as you describe what it looks like."
    mo "The rogue preaches the truth! The rest of us are knowledgeable enough to connect the dots! Outline your constellation for us, Touka!"
    to "How am I supposed to know that without having any experience?!"
    a "Just...tell us what kind of porn you watch?"
    ki "Yeah. Which is a totally normal thing that none of us here will ever hold against you."

    scene beachmastod21
    with dissolve

    to "It’s...unbecoming of a lady to consume such material..."
    ki "I get that. Especially when you probably have a whole lineup of “sex therapists” back at your manor that help relieve your {i}tension{/i} for you. "
    no "Oooh, keep talking. I’m getting ideas. "
    no "Does anyone mind if I take a few no-"
    a "Yes."
    ay "No one’s going to hold your preferences against you, Touka."
    ki "Unless you’re a furry."
    mo "Furries have feelings too."
    to "If I..."
    to "If I ever did watch something as vulgar as...pornography..."
    to "It would...probably be...the kind where...they speak directly to you...through the...the speakers..."
    ki "Like...POV shit?"
    mo "No...No, I believe we’ve got a genuine ASMR fan in the server! How unsurprisingly fitting!"
    ki "That doesn’t really answer the position question, though."
    ay "Just take the victory, Molly. Touka’s obviously embarrassed and-"
    mo "Insolent whelp! You have been given one simple task and have left nothing but scraps upon my wooden floors! Bequeath to me your true self! Surrender your inhibitions and announce to the world-"

    scene beachmastod22
    with dissolve

    to "I already said it! The regular one! Where the man is behind the girl and the girl’s hands are tied to something in front of her! Like a...pole or...something!"

    scene beachmastod23
    with fade

    ki "How fucked up does your algo have to be for something like that to be “regular?”"
    to "I seldom view such content! Forgive me for having more important things to do!"
    no "And sex servants. She never specifically denied the sex servants."
    to "I have no such thing!"

    scene beachmastod24
    with fade

    to "Ami! It is now your turn because everyone has decided to gang up on me and I am feeling very overwhelmed!"
    a "Don’t be! And excellent choice of position!"
    to "I would very much like to move past that right now! Truth or dare!"
    a "Let’s go with...truth!"
    ki "Ask her something lewd! Keep the ball rolling!"
    to "I would never-"
    ki "But it would make you {i}cooler...{/i}"
    to "Does...talking about such things truly make one cooler? I was under the impression it just made you a harlot."
    ki "Are you calling me a {i}harlot,{/i} Touka?"
    to "Are...Are you not? I thought that was your whole thing."
    mo "F’s in chat for Kirin. "
    a "Ask whatever you want, Touka. I don’t really care. "
    m "You probably should. Your interests aren’t exactly socially acceptable."
    a "They are in some countries."
    to "I will...remain true to myself and ask you something that is {i}not{/i} lewd as...imagining myself ever being like Kirin worries me greatly. "
    to "Ami...what is the...most absurd thing you would ever do for someone you love?"

    scene beachmastod25
    with dissolve

    a "The most...absurd thing...for someone I love?"
    to "R-Right! Where would you draw the line? Just how far would you go to prove yourself to the person you admire?"
    ki "His name is Sensei. You can call him Sensei."
    a "Hmm...I’ve never really thought about it before..."
    mo "I’m calling BS. I’ve had you pegged as the yandere from the start."
    to "What is a yandere, exactly?"
    m "Someone so attached to the object of their affection that they’re willing to kill anyone and everyone who gets in their way."
    to "Oh. Well of course Ami isn’t like that. She’s such a good girl. Just look at her, lost in thought about the man she loves. It’s adorable."
    no "It’s even more adorable when you remember they’re related."
    to "Ami, you’d never {i}kill{/i} for Sensei, would you?"

    scene beachmastod26
    with dissolve

    a "Oh, I {i}definitely{/i} would. I’m just trying to think of things that are {i}worse.{/i}"
    to "Than murder?!"
    mo "Boom! Called it! Never doubt Molly MacCormack’s ability to accurately categorize young girls into various tropes and groups! It is for this exact reason that I was put on this planet!"
    a "How long do you have to torture someone for it to be worse than murder?"
    to "This isn’t wholesome at all! Pick dare instead!"
    a "Is sensory deprivation cruel? Or is that kind of just a thing that nobody really cares about?"
    ay "When did you get like this?"

    scene beachmastod27
    with dissolve

    a "Like what?"
    ay "Like...Like that."
    a "Are you saying you {i}wouldn’t{/i} kill for Sensei?"
    ay "Uhh...I mean...I guess if I absolutely {i}had{/i} to. But-"

    scene beachmastod28
    with dissolve

    a "Well, I guess we know who loves him more then!"

    scene beachmastod29
    with fade

    a "Okey-dokey! Seeing as it’s my turn now and Kirin is the only one who hasn’t gotten a truth or a dare yet..."
    ki "Bring it on. And, just FYI, I won’t put up a fight like a certain {i}someone{/i} if you ask for my favorite sex position. I’ve got that drilled into the back of my-"
    a "Maya!"

    scene beachmastod30
    with dissolve

    ki "Seriously?! But you literally {i}just{/i} acknowledged how I haven’t gotten to go yet!"
    a "Yeah, but I wasn’t really interested in anything I could make you say or do and I want to hear Maya say more cute things about how much she loves me."
    m "Well, good luck as I mentioned earlier that I am a “dares only” girl and have little interest in whispering sweet nothings to you just because I am asked to."

    scene black
    with dissolve2

    a "Fine. Then I dare you to come over here and give me a hug because I love you."
    ay "Careful, Maya. You’ve been within ten feet of Sensei today so there’s a chance Ami might smell him on your skin and slit your throat when you’re not paying attention."
    m "If Ami truly wanted to kill me, I can guarantee you I would be dead already."
    a "Keep saying suspicious things like that and I might have to!~"

    "{i}No one chooses Kirin for the next fifteen minutes. And no one ever agrees to kiss her either.{/i}"
    "{i}Touka only chose dares from that point on.{/i}"
    "{i}And Ami manages to make it through the rest of the game without killing anyone.{/i}"

    $ renpy.end_replay()
    $ beachmas8 = True

    jump beachmas9

label beachmas9:
...
```

## Code that triggers this event
File: \game\chap3.rpy
Code:
```python
...
mo "But, perhaps there is something I could make to go along with last year’s Christmas present...which I see you’re still wearing."
    s "Indeed I am. It’s one of my three favorite shirts."
    mo "And it brightens my day to hear you say that."
    mo "Now, if you’ll please excuse me, I have agreed to partake in a treacherous ritual where myself and several other girls will go around in a circle revealing secrets about ourselves and making bad decisions."
    s "Oh, good. It wouldn’t really be a beach trip unless something terrible happened to at least one of the interpersonal relationships in this class."
    mo "Right you are, Sir! And here's hoping that person is not me for the second year in a row!"

    scene beachmasseven29
    with dissolve

    "Molly makes her way back to the table and-"

    r "Sensei!"

    scene beachmasseven33
    with dissolve

    "Okay. I guess Rin is here now."

    r "Sensei, have you seen Futaba anywhere?"
    r "I’m pretty sure I pissed her off by spending so much time on my phone and she doesn’t {i}have{/i} a girlfriend so she didn’t {i}bring{/i} her phone with her and now I can’t apologize."
    s "Wow, everyone’s just missing tonight, huh?"
    r "Who else is missing?"
    s "Yumi...Tsuneyo...Futaba...And come to think of it, I haven’t see Otoha around either."

    scene beachmasseven34
    with dissolve

    r "Kind of hard to see somebody who didn’t come in the first place."
    s "What? Why isn’t she here? You’re not fighting again, are you?"
    r "We’ve barely {i}stopped{/i} fighting since Halloween."
    r "So in a sense, I guess it’s kind of {i}good{/i} that she didn’t come because this would be prime “Let’s dump Rin” territory and I doubt she’d do something like that over the phone."
    r "But also, I {i}want{/i} her to be here so we can finally stop all this arguing and just make out or something."
    s "Fine. If you {i}really{/i} want someone to make out with, I-"

    scene beachmasseven35
    with dissolve

    r "I can’t joke about that anymore. I’m sorry."
    s "Who said I’m-"
    r "Please don’t. Things are complicated enough as-is."
    s "My bad. But yeah, I’ll keep an eye out for Futaba. Especially since it seems like it is now my duty to go round all of the missing people up in one leisurely stroll around the beach."
    s "Want to come with me?"
    r "Me? Thanks but no thanks. I’m going to continue sulking in the bedroom. Just tell her I’m sorry if you see her, okay? I get not wanting to hang out with me. I kinda suck right now."
    s "Just stop sucking and you won’t have any problems anymore."

    scene beachmasseven36
    with dissolve

    r "I’ll get right on that. Thanks for the pep talk, Dad."
    r "Enjoy your leisurely walk down the beach and make sure to hold Futaba’s hand if you guys wind up romantically walking back here together."
    r "It’ll be a good substitute for the Christmas present you totally didn’t get her."
    s "How about I just have sex with her instead?"
    r "How about I pretend I didn’t hear that and go back to blinding myself with blue light in a dark room?"
    s "Wait, one last thing."
    r "What?"
    s "Is your mom coming?"

    scene beachmasseven29
    with dissolve

    r "Goodnight, Sensei."
    s "Because if not, I can make her."
    r "You and what vagina?"

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "As Rin disappears back into the bedroom away from the comfort of all of her friends, I set out on yet another soon-to-be fruitless journey."
    "And while there’s no guarantee I’ll find any of the three people I have been tasked with finding (One being a task I set myself) I can at least make sure I’m not around when things inside inevitably start cracking."
    "That sort of thing always happens around here. And it happens even {i}faster{/i} when I’m present."
    "And so my early Christmas gift will be minding my own business for most...while figuring out a way to get {i}involved{/i} in the business of those who I think actually {i}need{/i} it."
    "The ones who are missing-"

    scene beachmasseven37
    with dissolve2

    sa "{i}Hngh! Mmm!....Mmf!{/i}"
    sa "{i}Mmf...no...I have...ngh! I have...to stay...quiet!{/i}"
    s "..."

    "The ones who are missing are the ones who need me the most."

    sa "{i}Ahh.......haaaah!{/i}"

    "But..."
    "Maybe not all of them."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ beachmas7 = True

    "........."
    "......"
    "..."

    jump beachmas8
...
```