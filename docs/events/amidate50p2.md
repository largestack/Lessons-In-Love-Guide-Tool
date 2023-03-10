# Fruits of the Two Seasons (Ami)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Outcry of the Hunted Hare](./amidate50.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: amidate50p2
* Group: Ami
* Triggered by label: amidate50
* Chain sources: amidate50
* Chain sources path: amidate50

## Official wiki page

[Fruits of the Two Seasons](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=amidate50p2&go=Go) for more details.

## Event code

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
label amidate50p2:
    scene sky
    with dissolve2
    play music "amiamiami.mp3"

    s "Ami, where are you taking me?"
    a "I told you the first ten times you asked! Somewhere you’re going to like! The answer hasn’t changed!"
    s "I just can’t help but feel like you are lying to me considering every single building I can see from here sells nothing but anime and nerd stuff."
    a "Okay, first off, Sensei...anime isn’t just for nerds and I know you’re better than thinking that."
    s "Am I really, though?"
    a "We used to watch Sailor Moon all the time when I was little!"
    s "So obviously I would still love it years later."
    a "Exactly."
    s "That was sarcasm."
    a "Your face is sarcasm. Now stop asking where we’re going and let me lead the way!"

    "Ami pulls me through the streets of the red-ish light entertainment district after a mildly long bus ride back from the cemetery."
    "Is this where I expected to come immediately succeeding one of the most emotional moments I have witnessed in the last...forever? No."
    "But I guess it will, to some extent, numb some of the pain she must be feeling right now."
    "Besides, indulging in her interests every now and again might not be the worst thing ever in exchange for a guaranteed life worth of smooth sailing and even smoother omelets."
    "I just hope we don’t have to spend the entire day here. I don’t like that a place as loud and bright as this is on the brink of becoming another regular location for me."
    "And I also don’t like that we are now walking into a nerd store."

    scene amianime1
    with dissolve2

    a "..."
    s "..."
    a "So, as you can see, I lied to you."
    s "Betrayed by my own [niece]."
    s "Aren’t you the one who is supposed to always be on my side?"
    a "I {i}am{/i} on your side! I just knew that you wouldn’t come here with me if I told you the truth about where we were going, and the new volume of a manga I like came out today."
    a "There’s no [incest] in it at all."
    a "I mean, what? Who said that?"
    s "..."

    scene amianime2
    with dissolve

    a "Oh, look! New figures!"
    s "Did you really have to come here {i}today?{/i} Shouldn’t we have done something at least partially enjoyable for me?"

    scene amianime3
    with dissolve

    a "Oh, come on! We won’t be here long. I’m using my own money and everything. "
    a "I just need to pick this up before all the new copies sell out and {i}then{/i} we can go out and have our cute family date that I’m definitely not pretending is a real date and that we’re going to get married."
    a "I mean, what? Who keeps saying all of these weird things out of literally nowhere?"
    s "Ami, I think you have a problem."

    scene amianime1
    with dissolve

    a "It’s not me who’s wrong. It’s society."
    a "Now, come with me and don’t look at the back section of the store. "
    s "Why can’t I look at the back section of the store?"
    a "I will tell you when you’re older."

    scene amianime4
    with dissolve

    a "Over here, Sensei!"

    if bonus == True:
        s "I’m more than twice your age. I think."
        s "How old are you again, Ami?"
        a "Old enough! But that’s not a thing we should be yelling about in the store and you should probably come over here now!"

    s "..."

    scene black
    with dissolve2

    "I swallow the last few shreds of pride in my body (If that’s where pride is stored) and make my way over to Ami as she sifts through a bunch of brightly colored boxes and books."
    "And, despite apparently knowing exactly what she is here for, she sure takes her time in picking up and observing a lot of different items. "
    "Have I been lied to {i}again{/i} in such quick succession?"
    "Is this the so-called “rebellious phase” I have heard of?"
    "Is there a cut-off for when you can put someone up for adoption? Is that still a possibility if this keeps up?"

    a "You know, Sensei, I can probably find something here for you if you want me to."

    scene amianime5
    with dissolve2

    s "And why would I want you to do that, exactly?"
    a "Because...manga is more interesting than standing around and doing nothing all day?"
    s "I don’t do “nothing” all day. You clearly don’t understand the first thing about how exciting my life is."
    a "If it’s so exciting how come you haven’t smiled in like six million years?"
    s "I’m just waiting for the right moment."
    a "Uh-huh. Sure you are."

    scene amianime6
    with dissolve

    a "Really, though! There’s tons of stuff here I think you would like! And I’m not just saying that because I think it would be nice to share a hobby with you."
    a "Niki told me about how you two used to watch anime together, so what if we got you something...retro? Like something you guys watched way back when?"
    a "They even remake more popular series that have been out of style for a while sometimes. I’m sure I can find-"
    s "I’m going to stop you right there at the risk of you making me feel even older than I constantly feel around you."
    a "If it makes you feel any better, I probably wouldn’t like you as much if you weren’t so much older and bigger than me."
    a "I mean, what? Really, where are all of these comments coming from?"
    s "..."

    scene amianime7
    with dissolve

    a "I’m gonna get you something. I’ve decided."
    s "And I’ve decided that you’re not going to do that."
    a "But it’s a present! I never got you anything for Christmas. Are you really going to turn away a free thing that your [niece] lovingly selected for you?"
    s "Yes."
    a "What kind of genre do you want? Action? Drama? BL?"
    s "What is BL?"
    a "BL is-"

    scene amianime8
    with dissolve

    mo "What’s this?! Time for another weebnote?!"
    a "Oh. Molly’s here."
    a "That makes sense."
    mo "BL, or “boys love” is a wildly underappreciated genre in the anime and manga world where, get this- boys love each other!"
    s "Why would you even suggest that for me?"

    scene amianime9
    with dissolve

    a "Because I think it’d be hot."
    s "{i}What?{/i}"
    mo "Did you know that BL manga dates all the way back to the mid-70’s? It hasn’t changed much since then and is still aimed primarily at young girls, but the origins were actually much darker!"
    mo "Kaze to Ki no Uta, which is commonly referred to as the first instance of the BL genre, features stuff like prostitution, drug usage, and ra-"

    scene amianime10
    with dissolve

    mo "Uhh...actually, that’s it for today’s weebnote. I don’t really have anything else to say."
    a "What brings you here, Molly? I thought you and Tsuneyo were supposed to hang out today."
    t "I am Tsuneyo."

    scene amianime11
    with fade

    t "Surprise. I am also here."
    s "I’m assuming you were dragged along unwillingly as well?"

    scene amianime12
    with dissolve

    mo "Not at all, Sir. It was actually Tsuneyo’s idea to come here, not mine. I spent everything I currently have on gacha games, so I’m only here to act as a consult today."
    a "Tsuneyo’s finally getting into manga?"
    t "I received a Christmas bonus from my father and feel the need to spend it on things I am supposed to appreciate before it is too late and he asks for it back."
    s "I don’t think employers ever ask for bonuses back, but I guess I don’t know your dad all that well."

    scene amianime13
    with dissolve

    t "He does not like summer very much. I will not squander this opportunity to buy a brightly colored rectangle."
    mo "How about you, Ami? What are you doing here?"
    a "The new volume of My Sweet Prince came out today and I wanted to make sure I got it before it was sold out."

    if bonus == True:
        mo "My Sweet Prince? Isn’t that the one where the girl and her uncle-"
    else:
        mo "My Sweet Prince? Isn’t that the one where the accountant and her-"

    scene amianime14
    with dissolve

    mo "Oh my god."
    a "Hmm hm hmmmm~"
    s "..."

    "In a strange twist of fate, it looks like Ami lied {i}again{/i} and that the book she’s buying very much has the one thing she told me it {i}didn’t{/i} have."

    scene amianime15
    with dissolve

    mo "Well I guess that confirms {i}that{/i} suspicion."
    a "Just liking a certain trope in manga doesn’t mean you like it in real life, Molly. Everybody knows that."
    a "It normally does, though."
    mo "..."
    a "I won’t confirm nor deny anything."
    mo "I take it that means you two are...on a...{i}date{/i} then?"
    s "No."

    scene amianime16
    with dissolve

    a "Mm!"
    mo "Wait. Now I’m confused. Is this {i}not{/i} a meeting of secret, forbidden love? A taste testing of the most bitter fruit of all?"
    t "I believe that would be the “bitter melon,” which is famous for its medicinal properties."
    s "We’re just stopping by on our way back from...a place."

    scene amianime17
    with dissolve

    mo "That..."
    mo "You know that makes it sound even sketchier...don’t you, Sir?"
    s "I don’t know where your depraved mind goes after just hearing the word “place,” but I can assure you it’s not whatever you’re thinking."
    s "I doubt Ami wants to talk about it, though, so let’s just move on and-"
    a "I wanted to see my mom."

    scene amianime18
    with dissolve

    mo "Oh...{i}oh...{/i}"
    a "I’ve just missed her a lot lately. That’s all."
    a "Which is why we’re now...counteracting that with some place happy and..."
    mo "May I hug you?"

    scene amianime19
    with dissolve

    a "..."
    a "Yes, please."

    scene black
    with dissolve2

    "Molly wraps her arms around Ami and pulls her close, pressing their heads together."
    "They gaze into each other’s eyes and, if this weren’t such a heartfelt moment, I’d probably say something to emphasize just how much I’d appreciate it if the two of them would kiss right now."

    scene amianime20
    with dissolve2

    "Which is obviously not a thing I’m going to talk about."
    "I mean, how could anyone think that at a time like this? "
    "Nope. I don’t want that to happen at all."
    "Not even a little."

    s "..."

    "Not even a little."

    mo "I lost my mom when I was little, too. I know what it’s like."
    a "I know...I always wanted to ask you about how you managed to...talk about it so easily, but...it’s hard, you know?"
    mo "I do. But you know what’s easier? Hugging. So I hereby give you permission to hug me any time you want as a free action."

    scene amianime21
    with dissolve

    a "Thank you, Molly. I’ll be here for you if you ever need me, too."
    mo "I’ll remember that. "
    a "Hey, how come we never do anything with just the two of us?"
    mo "Probably because you already have Ayane and Maya and I would just be getting in the way."
    a "Let’s hang out soon. Just us."
    mo "I’d like that a lot..."
    s "..."

    "{i}Not even a little.{/i}"

    t "It appears everyone has forgotten that I lack a mother as well."

    scene amianime22
    with fade

    mo "Ah! I’m sorry, Kendo Princess! I just know that...your affinity for hugs is not as high as mine! And that you wouldn’t want to get involved in something like this..."
    a "And I just...wasn’t even thinking. Sorry, Tsuneyo."
    t "Abandoned by my own party members. I truly am an outcast."
    s "I’ll hug you, Tsuneyo. We don’t need them."

    scene amianime23
    with dissolve

    t "I would rather die."
    s "That...seems like an exaggeration."
    t "It is not."
    s "Didn’t we hug on Halloween that one time?"
    t "I have no idea what you are talking about."
    s "When-"
    t "I would never hug a man as horrible as you."
    s "It was after we went outside and-"
    t "Never."
    s "And Molly was-"
    t "It would simply not happen."
    s "But-"
    mo "Just give it a rest, Sir. Your charisma isn’t high enough to break through to Tsuneyo yet."
    s "That’s fine, but..."
    s "How long are you two going to stay like that for?"

    scene amianime24
    with dissolve

    mo "..."
    a "..."
    mo "Maybe just a little bit longer."
    t "Ahh, youth..."
    s "Tsuneyo, you’re the same age as them."
    t "Then why will no one hug me?"
    s "I literally just offered-"
    t "No thank you."
    mo "..."
    a "..."
    a "You smell really nice."
    mo "I was actually just about to say the same thing to you."

    scene black
    with dissolve2

    if bonus == True:
        "I guess Ami winds up mistaking Molly for a relative or something since it seems she has a hard time separating from her, but I’m sure it’s probably closer to the fact that she just has someone she can relate to."
        "Even if Ayane’s mom isn’t around anymore, I can’t imagine Ami being able to confide in her in the way that she could with someone who’s actually felt the same sort of pain she has."
        "But pain is not something I intend to dwell on any longer when its abundance is one of many things in this life that neither myself nor anyone else is able to avoid."
        "I will focus on the brighter things and what it is that illuminates them."
        "Ami finds her manga (Which may or may not contain [incest], but probably does) and pays for it at the register after separating from the others."
        "She clutches it to her chest as the two of us exit the store together and make our way out into the street, bustling with foot traffic due to the sudden increase in temperature."
        "Then, before long, she’s pulling me around once again."
        "Just..."
        "Hopefully to somewhere I won’t feel out of place in this time."
    else:
        "Not even a little."

    $ renpy.end_replay()
    $ ami_love += 1
    $ amidate50p2 = True
    stop music fadeout 8.0

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump amidate50p3

label amidate50p3:
...
```

## Code that triggers this event

File: (install folder)\game\AmiEvents.rpy

Code:
```python
...
scene her10
    with dissolve2

    a "Okay...now it’s your turn."
    s "My turn?"
    a "They were important to you too, Sensei. You can’t just {i}not{/i} speak to them."
    s "Ami, I don’t really want to ruin a good moment by expressing my thoughts on talking to the deceased."
    a "I bet {i}they{/i} would talk to you if you were the one who died. I know I would."
    a "You’re not allowed to die, though. I love you too much."
    s "I will do my best to continue...indefinitely living."
    a "Um...can I ask for something selfish?"
    s "I already told you that I’m not giving you an allowance anymore. Stop trying to revive that when you already have a job."

    scene her11
    with dissolve

    a "The only reason I have a job is because you think all of the things I do for you aren’t worth new clothes and manga and stuff."
    s "And I will remain steadfast in that belief, but please carry on with your selfish request, whatever that may be."

    scene her12
    with dissolve

    a "I don’t want to go home just yet."
    a "I want you to spend the entire day with me."
    a "I want it to be a real date."

    if amifingered == True:
        s "A real date sounds fine. Especially since I very likely know how it will end with you."

        scene her13
        with dissolve

        a "Sensei! My parents are literally right there! You can’t say that!"
        s "Say what? It’s not like I said {i}how{/i} it will end. I just-"
        a "They were adults when they died! They will obviously know what you mean by that!"
        s "Again, I technically didn’t do anything wrong just now."

    else:
        s "What do you mean by a “real” date, Ami? Because I’ve already told you that-"

        scene her10
        with dissolve

        a "I know what you’ve told me. And I’m not expecting you to change that or do anything you think is weird that {i}really isn’t that weird{/i}, but I understand."
        a "Even if nothing comes of it, I want to go on a date."
        a "I want to spend the entire day with the person I love more than anything else in the world."
        a "I deserve it every once in a while if you’re really not going to give me an allowance."
        s "..."
        a "..."
        s "You know you’re really annoying sometimes, right?"
        a "I’m supposed to be annoying. I’m your [niece]."
        s "I don’t really think it works that way..."

    s "But fine. I’ll go on a date with you."

    scene her14
    with dissolve

    a "Yay! A whole day with Sensei that I only kind of had to force out of him!"
    s "Here’s hoping the next part of it is significantly less painful and tear-filled than the first."

    scene her10
    with dissolve

    a "Oh, it will be. I already know where we’re going. And it’s somewhere I think you’ll like a lot."
    s "That is a bold claim. There are not many things I like."
    a "Well, you just wait, Sensei. Because this place is going to knock your socks off."
    a "I just..."
    a "I just wanna talk to my mom one more time before we leave, okay?"
    s "..."

    scene black
    with dissolve2
    stop music fadeout 25.0

    s "Obviously. Even I wouldn't say no to that."
    a "Heheh~ You know you can talk too if-"
    s "I’ll be waiting at the entrance. Take your time."
    a "Sensei! At least stay here if you’re not going to talk to them!"

    "Ami lowers herself to her knees and places both hands upon her parents’ grave."
    "There are no gusts of wind or homeless cherry blossoms to distract me from the sight this time."
    "I watch her break down once again, knowing full well that it will likely not prepare me for the many more times I’ll have to watch her do this exact thing."
    "Some things, you can never get used to."
    "And the pain of someone you genuinely love is one of them."
    "I press my hands together and attempt to pray {i}for{/i} something {i}to{/i} happen."
    "Nothing happens."
    "Not even a gust of wind."

    $ renpy.end_replay()
    $ ami_love += 3
    $ amidate50 = True

    "{i}Ami’s affection has increased to [ami_love]!{/i}"
    "........."
    "......"
    "..."

    jump amidate50p2
...
```