# In Circles (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Official Unofficial Double Date](./halloweentwo8.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloweentwo9
* Group: Main
* Triggered by label: halloweentwo8
* Chain sources: halloweentwo8
* Chain sources path: halloweentwo8

## Official wiki page

[In Circles](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo9&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label halloweentwo9:
    "{i}Meanwhile...{/i}"

    scene truthordarehalloween1
    with dissolve2
    play music "breeze.mp3"

    c "Okay, okay! Now...Miku’s turn!"
    mi "Already? That was fast. "
    mi "Can we maybe like...go around the circle one more time or somethin’?"
    mak "What do you have to be afraid of? It’s not like any of us are going to judge you."
    c "Yeah! Truth or dare’s just about having fun and...learning more about each other!"
    mi "Then umm...t...truth I guess?"
    c "You sure?"

    scene truthordarehalloween2
    with dissolve

    mi "Well not when ya frickin’ say it like that!"
    mi "Dare! "
    mi "I don’t know!"
    mak "Just stick with truth, Miku. It’s easier."

    scene truthordarehalloween3
    with dissolve

    mi "You want the truth?! You can’t {i}handle{/i} the truth!"
    mak "…"
    c "…"

    scene truthordarehalloween4
    with dissolve

    mi "One truth, please."
    c "Okay, okay. Umm..."
    c "If it was guaranteed that you’d never get caught..."
    c "Who in our class would you murder?"

    scene truthordarehalloween5
    with dissolve

    mi "What the heck?! I’m not a killer!"
    mak "That’s certainly an...interesting pick for a question."
    c "Yeaaaaah. I guess so. But now she’s gotta answer it because she said truth."
    mi "But I like everybody. There ain’t anyone I’d wanna kill."
    c "Nooooo! You have to pick someone!"
    mi "Then, umm...uhh..."
    mi "Yumi, I guess?"

    scene truthordarehalloween6
    with dissolve

    c "Aww. Now I’m sad. I love Yumi."
    mi "I don’t know...I just haven’t really talked to her and...she’s always bein’ mean to Futaba and stuff."
    c "I know. I hate that she treats her that way. But Yumi’s just misunderstood."
    c "Like, today’s her birthday and she hasn’t even shown up yet. She just feels like she’s...not accepted here."

    scene truthordarehalloween7
    with fade

    no "Well, that’s on her."
    no "If she wanted to feel included, she’d stop talking down on people who have done absolutely nothing to her."
    c "I know, I know. And I want to say more to try and explain her side of things, but it’s...kind of weird talking to someone dressed as Rin."

    scene truthordarehalloween8
    with dissolve

    no "Never fear. My appetite for both confrontation and revenge can be easily sated by granting me the opportunity to make {i}you{/i} choose between truth or dare."
    c "Then, uh...Well, Miku’s truth wasn’t all that hard. So...I’ll do truth too."
    no "Wonderful."
    no "Because now I can make things even more difficult for you in asking {i}this.{/i}"
    to "Oh dear. {i}This{/i} sounds dangerous."
    c "Ehh, I’ve got nothing to hide. Bring it on."
    no "I’ve heard through the grapevine that a certain one of our classmates confessed to you on the beach last year."
    u "Wait, who? What? I wanna know about this!"
    c "Ugh..."
    no "If, perchance, you had {i}not{/i} already been romantically interested in a certain man who shall not be named given the agreed upon rules of this game- how would you have responded?"

    scene truthordarehalloween9
    with dissolve

    c "Nodoka, can you maybe ask me something that {i}isn’t{/i} a leading question?"
    c "Rin is literally dating your roommate now. I don’t want to say anything that might cause some sort of rift between them."
    u "Ah! Rin! That makes-"
    u "Wait, Chika’s nothing like Otoha. What a weird jump."
    no "Why would this be a leading question, Chika? Everyone here has agreed to a vow of silence."
    no "Nothing you say will leave this circle. You may answer openly and honestly, as if any one of us were your sister."
    c "It’s still...kind of weird..."
    mak "I don’t think it’s that weird."
    mak "Lesbian relationships in an all-girls[school] are just a thing that happen. "
    mak "Frankly, I think the two of you would make an even cuter couple than the one that already exists."

    scene truthordarehalloween10
    with dissolve

    c "Well, thanks...but that’s not really the backup I was hoping for..."
    no "The clock is ticking, gypsy girl. Fill my burning heart with the bisexuality I know is hidden underneath those thin strips of fabric you call a costume."

    scene truthordarehalloween11
    with dissolve

    c "Fine. You want my honest answer that will, {i}in no way{/i}, ever find its way to Rin or Otoha?"
    c "Yeah. Probably. "
    c "It’s hard to say since I never got to experience that moment {i}without{/i} already liking someone, but Rin is someone I...probably wouldn’t mind having that sort of relationship with."
    c "Again, this {i}never{/i} leaves the circle or I will literally kill whoever spills the beans."

    scene truthordarehalloween12
    with fade

    no "I knew it."
    no "Poor girl never even stood a chance when paired up against the tall and handsome {i}he who shall not be named.{/i}"

    scene truthordarehalloween13
    with fade

    u "Poor Rin, nyaa~ "
    u "Well, I guess not really {i}poor{/i} Rin since she seems happy now, but that’s still sad."
    c "Okay! Moving on!"
    c "Uta, why don’t you ask someone something now? You haven’t made anyone choose yet."

    scene truthordarehalloween14
    with dissolve

    u "Oh! Umm...in that case...Touka!"

    scene truthordarehalloween15
    with fade

    to "Hooray! Inclusion!"
    u "T...Truth or dare, nyaa?~"
    no "Why are you so flustered already, Uta-nyan? It’s not even your turn yet."
    u "I’m not! This costume is just hot."
    to "Well...it appears that truth has been the trend this round. So I, too, will select truth."
    u "Then, umm..."
    u "Who..."
    u "Who do you think is the most attractive person in the entire world?!"

    scene truthordarehalloween16
    with dissolve

    to "The whole world?"
    u "Yeah! Out of everybody ever. Boys and girls are both included."

    scene truthordarehalloween17
    with dissolve

    to "Hmm...that is a hard question."
    mi "We finally gonna figure out what kinda boys Touka is into?"
    mak "It could be girls as well, Miku. We have no idea."
    no "No...Touka’s not showing up on my gaydar, and I can’t recall a time I’ve ever been wrong about that before."
    to "The most...attractive person in the-"

    scene truthordarehalloween18
    with dissolve

    to "Oh! Silly me. How could I have forgotten?"
    to "Clearly the most attractive person in the world is American movie star, Seth Rogen."
    no "Uhhhhhhhhhhhhhh what?"
    mi "The Pineapple Express guy?"

    scene truthordarehalloween19
    with dissolve

    to "He’s like a...human teddy bear."
    to "Oh, how I’d love to go horseback riding with him through Papa’s vineyard..."

    scene truthordarehalloween20
    with dissolve

    to "Then...as the sun begins to set over the villa, I’d rest my head on his shoulder...sinking into his soft skin and cuddling up closer to him..."
    no "…"

    scene truthordarehalloween21
    with dissolve

    to "Oh! Heavens, I’m so sorry! I was beginning to get a little carried away with my fantasy."
    u "You don’t have to...apologize, nyaa~"
    u "That was just a...strange choice, nyaa..."
    c "Guess that’s one less girl to worry about, at least."

    scene truthordarehalloween22
    with fade

    to "Uh...umm...Makoto!"
    to "We’ve...communicated on several occasions now."
    mak "We...certainly have."
    to "Would it be too presumptuous of me to believe that it’s okay to ask you whether or not you’d like to answer a truth or dare question?"
    mak "I will save you the effort in making things any harder for yourself by accepting the truth option right now."
    to "I graciously thank you for your acceptance of my question and will now commence in creating a prompt for you."
    mi "The heck are you two talkin' like that for?"
    to "M...Makoto! H...Have you..."
    to "Have you ever watched a pornographic movie before?!"

    scene truthordarehalloween23
    with dissolve

    mak "Nope. Never."
    to "You have never even...clicked on one of those pop up messages that...tell you about...things?..."
    mi "Makoto, ya gotta tell the truth. That’s literally the main rule of the game."
    mi "If I’m gonna be killin’ Yumi, you’ve at least gotta be honest about-"

    scene truthordarehalloween24
    with dissolve

    mak "Fine! Yes! All the time!"

    if bonus == True:
        mak "So much that it’s not even exciting anymore! It’s all just people sweating and...rubbing their skin against each other until one of them screams and then...stuff comes out!"
        mak "There’s no plot! No conflict! No nothing!"
        mak "It can barely even be classified as an art form at this point and is nothing more than just one more means of squeezing every last cent out of sad people looking for a thrill!"
        mak "I hate it! I hate porn! Why does anyone like porn?!"
        u "Jeez. What the heck happened to make you feel that way?"

        scene truthordarehalloween25
        with dissolve

        mak "Every...single day..."
        mak "It’s just nothing but penises..."
        mak "I’m so tired of it..."
        mak "I see them in my dreams..."
        mak "And yet my MOTHER {i}needs{/i} me to watch it!"
        mak "{i}Makoto, you have to understand the difference between a group sex and gangbangs.{/i}"
        mak "{i}Makoto, it’s not technically deepthroating if the dick is too small.{/i}"

        scene truthordarehalloween26
        with dissolve

        mak "{i}MAKOTO, ANAL DOESN’T COUNT!{/i}"
        mak "DOESN’T COUNT FOR WHAT, MOM?! DOESN’T COUNT FOR WHAT?!"
    else:
        mak "But only because I have to in order to keep my family's business afloat!"
        mak "I hate it and don't enjoy any of it at all!"
        mak "In fact, I hate it so much that I don't even have anything else to say about it and will now move on the conversation!"

    scene truthordarehalloween27
    with fade

    mak "Hah...hah...hah..."
    c "…"
    c "Makoto...is everything okay at home?"

    scene truthordarehalloween28
    with dissolve

    mak "It’s fine."
    mak "Whose turn is it now?"

    scene truthordarehalloween29
    with fade

    to "This is just what I get for asking an inappropriate question, isn’t it?"
    mi "Nah. Makoto’s just got some really strong opinions on adult stuff."
    u "I thought my parents were bad when it came to that sorta thing, but knowin’ Makoto’s mom is the opposite, it kinda makes me glad I wasn’t allowed to watch that stuff."
    c "I mean...nobody’s ever {i}allowed{/i}, Uta."
    u "That’s not how it sounds to me!"
    no "I suppose I can go now."
    mak "Let me guess, truths are too boring for you and you want a dare this time?"
    no "{i}Actually,{/i} my dearest Makoto, I would like a truth as well."

    if bonus == True:
        no "You see, since you’re the one asking me the question, I’d be delighted to give you a bit more insight into who I am as a person in the hope that you will, one day, be okay with touching me sexually."
        no "Or vice versa. I believe that no one should be pleased unless they are willing {i}to{/i} please."
        no "Unless it’s a relationship centered around a power dynamic in which the weaker party feels pressured to constantly perform sex acts for the more powerful one in exchange for acknowledgment or a reward."
        no "However, if that is the type of relationship you wish to have, I will not refuse the idea of being a slave to the secret hypersexuality that’s been exuding from you ever since saying the word “gangbang” moments ago."
        mak "I’m not...you know what? Fine. If you want to play that game, answer this."
        mak "Nodoka, you’re constantly saying perverted stuff...but no one’s ever actually seen or heard of you actually...backing any of that up."
        mak "Are you actually as interested in sex as you claim to be? Or is this some sort of...disguise or front you’re trying to put on or...up, respectively."
    else:
        mak "Sure...then-"
        mak "You're always saying how much you're into bad stuff, but...do you {i}really{/i} like bad stuff? Or are you just pretending to like bad stuff while you really like {i}good{/i} stuff instead?"

    scene truthordarehalloween30
    with dissolve

    to "I, too, am curious to know this truth."
    to "I’ve always found it particularly strange how forward you are."
    to "At first, I assumed it to just be the way commoner women conduct themselves."
    to "But as time passes by and no one measures up to the things you say, I’m beginning to wonder if you are a special case."
    no "So...the question is whether or not I’m actually just saying all of those things or if I’m truly interested in them?"
    mak "Precisely. And, if your answer is the former, {i}why?{/i}"

    scene truthordarehalloween31
    with dissolve

    no "Well, adding {i}another{/i} question to your first one would be breaking the rules. So if the answer {i}is{/i} the former, you’ll have to wait at least one more round to figure out why."
    no "Fortunately, that won’t be an issue- as all of the things I say are not exaggerated, nor are they a disguise or front."
    mak "So that...strange, pervertedly curious persona actually is the real {i}you?{/i}"
    no "Ding ding ding. The class rep has figured it out."
    mak "I don’t get it, though. If you’re so interested in that sort of thing, why aren’t you trying to get a girlfriend or...boyfriend or something?"
    mak "You do like boys, right? I’ve only ever heard you talk about girls before."
    no "So many questions. Do you need a refresher on how this game works, Makoto?"

    scene truthordarehalloween32
    with fade

    mak "Of course not. You’re just a...confusing person."
    no "Will {i}you{/i} be my girlfriend, Makoto? "
    mak "No. But I feel like even if I said yes, you’d back off."
    no "Then say yes and see what happens."
    mak "You really won’t explain your rationale? I’m genuinely curious."
    no "I think I’d like to remain an enigma for a little while longer."
    no "But maybe next round, I'll pick truth again and come clean just for you~"

    scene truthordarehalloween33
    with dissolve

    mak "Hah...we all know that’s not going to happen now..."

    scene truthordarehalloween34
    with fade

    no "Buuuut anyway...it looks like it’s the blushing kitten’s turn."
    u "I already told you, the costume’s hot. I’m not blushing."
    no "Right, right. Apologies."
    no "I take it you’re going to follow in everyone else’s footsteps in saying “truth” instead of paving a path for yourself with a dare?"

    scene truthordarehalloween35
    with dissolve

    u "Nyahahah!~ That’s where you’re wrong, Nodoka!"
    u "I’ve been planning on breaking the combo ever since the start, nyaa!~"
    to "But...it wouldn’t have been a combination at the start..."
    u "Hit me with a dare! Show me what you got!"
    no "Are you sure? "
    u "Super sure! Uta-nyan can handle anything!"
    no "I see."
    no "Then I dare you to saunter on over to the man in the back of the room, stand on your tiny little tiptoes, and passionately kiss him in the middle of the Halloween party."

    scene truthordarehalloween36
    with dissolve

    u "Uh...wh...what?"
    no "You’re the one who chose a dare. All things considered, I’d say this one sounds pretty simple."

    scene truthordarehalloween37
    with fade

    if bonus == True:
        mak "Absolutely not!"
    else:
        mak "Absolutely not! Patreon draws the line at kissing! Probably! Besides-"

    mak "We clearly stated that Sensei would not be brought into any of the questions or dares in this game {i}specifically{/i} to avoid a situation like this."
    c "Yeah. Not a fucking chance."
    c "You can’t just kiss someone who doesn’t want you to kiss them. That’s assault."
    no "Oh? Are you implying that Sensei wouldn’t want to kiss our adorable little Uta-nyan?"
    c "Yeah. I am. "
    c "No offense to Uta, of course. But Sensei is off limits for this and you need to think of something else."
    mak "Agreed. This is entirely unacceptable."

    scene truthordarehalloween38
    with fade

    mi "Well, like...what if it’s just on the cheek or somethin’?"
    mi "Everybody in the room knows we’re playin’ a game, so they’ll all just think it’s part of that."
    mak "Miku! You can’t seriously be siding with Nodoka on this, can you?"
    mi "I’m not sidin’ with anybody...I just don’t think it’s a big deal if it’s a little peck on the cheek."
    mi "Would get everybody to stop yellin’ too."

    scene truthordarehalloween39
    with dissolve

    mak "Oh...I’m sorry..."
    mak "I wasn’t even thinking about the noise."
    mi "Nah. I’m okay. "
    mi "I just...don’t want any fights breakin’ out over somethin’ that...doesn’t really change anything..."

    scene truthordarehalloween40
    with fade

    u "Is it...too late to pick a truth instead?"
    no "Hmm...How about this one?"
    no "Do you {i}want{/i} to kiss Sensei?"
    mi "I feel like answerin’ that is even more dangerous than the cheek thing..."
    to "The poor kitty."
    u "I...uhh..."
    no "You can always back out of the game if you’d like, Uta-nyan. "
    no "It {i}is{/i} just a game after all."
    no "Everything that comes out of the circle is all in good fun."
    no "Besides, if you {i}do{/i} want to kiss our teacher, now would be a perfect opportunity."
    u "But...we’re not supposed to be adding him to the game! We said we wouldn’t..."
    c "Nodoka, seriously. Just think up another dare."
    mak "I agree with Chika."
    no "It appears it may be democracy’s time to shine, then."

    scene truthordarehalloween41
    with fade

    no "Makoto and Chika have vocalized their agreeance with the core rule this game was built upon."
    no "However, new circumstances have arisen and now Miku and I think a minor change would be both acceptable and beneficial to the game’s enjoyment for all."
    no "My initial dare is now formally amended to a simple kiss on the cheek, just to clarify."
    no "The only members who have yet to vote are Uta, who is exempt due to a conflict of interest-"

    scene truthordarehalloween42
    with dissolve

    no "And Touka..."
    to "I am...the deciding factor in this vote?"
    to "But that’s so much pressure..."
    no "Is it?"
    no "All you need to really do is tell the circle whether or not you think a kiss on the cheek is romantic or not."
    no "Do you see a problem with one or more members, if dared, kissing each other on the cheek?"
    to "I..."

    scene truthordarehalloween43
    with dissolve

    to "Well...in my family...things like that aren’t called romantic..."
    to "My father kisses both my sister and me on the cheek quite frequently. And I do the same with my mother and...even other extended members of the family."
    to "I don’t believe there to be any romantic significance to such a thing and..."
    to "I think I’d have to side with...Miku and Nodoka..."
    c "Seriously?"
    c "I mean...yeah, it {i}is{/i} just the cheek. But you don’t think it’s weird to just do that in the middle of a party?"

    scene truthordarehalloween44
    with dissolve

    to "I’m afraid that wasn’t the question I was asked..."
    mak "Then it’s not too late to revise the poll to-"
    no "No objections were made to the poll when presented and time has already been yielded for both parties on the opposing side."
    no "As such, Uta-nyan must now either abide by the amended rules of the game and kiss Sensei or...stop playing."
    mak "Hah..."
    mak "Uta, what will it be?"
    u "I...umm..."

    scene truthordarehalloween45
    with fade

    u "I..."
    mi "Truth or dare sure can get serious, huh?"
    mi "You feelin’ okay, Uta? It’s just a little kiss on the cheek. It's not like-"

    scene truthordarehalloween46
    with dissolve

    mi "You're..."
    mi "Doin'...anything else..."
    u "…"
    u "I..."

    $ renpy.end_replay()
    $ halloweentwo9 = True

    jump halloweentwo10

label halloweentwo10:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
with dissolve

    f "I’m sorry if I...falsely assumed something was wrong...but you {i}can’t{/i} be saying things like that, Rin. I need to...handle stuff like this on my own."
    r "I just...don’t want you to get overwhelmed..."
    r "I think you’re great and that...you deserve all of the love in the world. "
    r "I was just trying to...I don’t know, funnel some of it into you?"
    f "Just..."
    f "Let’s just treat this like any other night, okay?"
    f "No talk about...double dates or...romance or anything..."

    if futabahalloween2win == True:
        r "But...Futaba..."
        r "He literally chose you out of {i}everyone{/i} earlier."
        r "You have a real shot right now."

        scene otohadoubledate25
        with dissolve

        f "I don’t have any more of a shot right now than I did yesterday."
        f "Or last week or...any other day."
        f "Sensei’s...really nice to me. And yes, I do like him."
        f "But...he’s not ever going to {i}date{/i} me, Rin."
        r "Don’t say that...You don’t know that..."
        f "If something changes, you’ll be the first to know."
        f "But right now...I’m happy with the way things are."
        f "I’m happy just knowing that the person I admire looks at me and doesn’t immediately compare me to either of you."
        f "That’s honestly...more than I ever expected to get."

        scene otohadoubledate26
        with dissolve

        f "And..."
        f "And I don’t want him getting scared away..."
        r "Futaba...No...I..."
        o "Anyone who would ever get scared away from you doesn’t deserve to even breathe the same air, Futaba."
        o "You’re amazing and we’ll stop with all of the double date stuff."
        o "And...we’re sorry."
        o "Really."

    else:
        scene otohadoubledate27
        with dissolve

        o "Got it. "
        o "We’ll stop everything right now. And we’re sorry for pushing things a little too far. "
        f "Thank you, Otoha..."
        r "I’m really sorry, Futaba...I don’t really know what got into me..."
        f "It’s okay, Rin. Just...please be more careful about the things you say sometimes."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene otohadoubledate28
    with dissolve

    s "Everything okay over here? No shattered remnants of broken bonds or anything like that?"
    f "Nothing of the sort...Everything is fine."
    o "Sorry shit got all weird. I’ll take the blame since it was all pretty much my idea."
    o "Let’s just...hang out or whatever and talk about completely unrelated stuff. Like...movies or...uhh..."
    o "Has anyone else watched Squid Game yet?"

    scene otohadoubledate29
    with dissolve

    f "Oh my God. It was so good, right?!"
    o "Right?!?! And that part with the glass bridge? Wild. Absolutely fucking wild."
    r "…"
    s "…"

    scene black
    with dissolve2

    "The conversation carries on for another ten minutes before I finally decide it’s in my best interest to just leave."
    "Not only did I not have anything to contribute to their extremely emphatic discussion about some Korean television show, but I had a creeping suspicion that my presence was causing Rin to feel...off."
    "That could just be me being self-centered, though."
    "I guess it’s equally probable that her sudden swap to silence had absolutely nothing to do with me and was just the result of realizing she’d disappointed a friend."
    "Futaba recovered well, though."
    "I would have been uncomfortable in her position too."

    if bonus == True:
        "Hell, I was uncomfortable in {i}my{/i} position- but that was moreover because I was worried I’d have to explain to yet another girl why I don’t want to date them."
        "That crisis was averted in its entirety, though."
        "And now?"
        "I must return to the drunk girl in an extremely tight dress to make sure she does not drink herself into a coma."

    $ renpy.end_replay()
    $ futaba_love += 1
    $ halloweentwo8 = True
    stop music fadeout 5.0

    "{i}Futaba’s affection has increased to [futaba_love]!{/i}"
    "………"
    "……"
    "…"

    jump halloweentwo9
...
```