# Pre-Game Show! (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Super Mega Ultimate Dorm War!](./dormwar1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwar2
* Group: Main
* Triggered by label: dormwar1
* Chain sources: dormwar1
* Chain sources path: dormwar1

## Official wiki page

[Pre-Game Show!](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar2&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label dormwar2:
    scene wintersky
    with dissolve
    play music "justbehappy.mp3" fadein 4.0

    "I wind up waiting in my office until the[school] day comes to a close."
    "When I was kicked out of the room, I didn’t expect whatever weird shit the girls were planning to last more than like thirty minutes, but it is what it is I suppose."
    "At least it was quiet in there and I got to nap for a few hours."
    "I’m a bit curious as to exactly what is going on with the apparent dorm war, though."
    "Especially since I am now being followed home by two girls with microphones."

    scene dorminterviews1
    with dissolve

    s "What are you doing?"
    mo "Molly MacCormack here with Floor 2 News! Sir, what do you have to say in regard to your decision to become the judge of the first annual dorm wars?"
    mo "Any expectations? Sleeper picks for contest winners?"
    s "I don’t even know what any of you are competing in yet. And where did you get the microphones?"
    ay "Ayane Amamiya of Action News Now reporting in!"
    s "They’re not even plugged into anything."
    ay "Sensei, there have been several accusations that you may be playing favorites in this competition."
    ay "What do you have to say about them and how much do you love me?"
    s "I really hope you two don’t plan on doing this the entire weekend."
    mo "We very well may do that, Sir! The war is not expected to end until Sunday night, and it is up to us to interview not only you, but all of the combatants involved!"
    s "Cool. Go talk to them, then."
    ay "Their segment doesn’t begin until we get to the dorms! Right now, it’s teacher time!"
    s "Ayane, again, please stop calling it teacher time."
    a "So, uhh...this is new."
    m "You don’t know the half of it."
    a "I’m kind of surprised you’re as accepting of it as you are, Maya."
    a "I kind of thought you’d be all like, “Blahhh. My name is Maya and I don’t want to have {i}fun!{/i}” or something."
    m "What are you talking about? I’m plenty of fun."
    a "Yeah, but you normally become anti-fun whenever Sensei is involved and he’s basically the prize for this competition."
    m "I honestly don’t care whether we win or lose. I just thought it would be nice to actually do something for once."
    m "So sue me if that’s too out of character, I guess."
    mo "Sir, word on the street is that the dorm war is going to kick off with one of the most heated battles of the entire weekend."
    ay "That’s right. It looks like Ami and Noriko are going to be competing head to head in a battle for your affection! How do you expect them to react when {i}I{/i} am crowned the winner?"

    scene dorminterviews2
    with dissolve

    a "Ayane, if you even {i}show up{/i} during my battle with Noriko, our friendship is over."
    ay "I don’t even need to show up in order to win. That’s how much Sensei loves me."
    s "Let the record show that I am going to be as unbiased in judging these contests as I possibly can."

    "Probably."
    "Maybe."
    "We’ll see."

    m "Whatever happens, just don’t let that fucking psycho bitch win."
    m "Ami’s a much better candidate than her in literally every way. She’s sure to win."

    scene dorminterviews3
    with dissolve

    s "Wow. Are you actually participating in this?"
    m "Why does everyone seem so shocked by that?"
    a "Aww, Maya...you really think I’m better than Noriko?"
    m "I think everyone is better than Noriko. But yeah, I’m pretty sure you’re going to win."
    a "I mean, I know I’m going to win. But I’m happy to hear you’re on my team."
    ay "Sensei, I know you agreed to remaining impartial, but you {i}do{/i} realize that the competition is only hours away and three of the four girls with you are from the first floor."
    ay "What would be your response if word of this was to start circulating around the area?"
    s "That you followed me home and started harassing me."
    mo "Sir! A word on your expectations in the Ami vs Noriko battle? You haven’t given us your pick yet."

    scene dorminterviews4
    with dissolve

    s "I don’t even know what they’re competing in yet. Am I even allowed to?"
    ay "We don’t know! That much wasn’t established in the rules."
    mo "But it would probably be better off left as a surprise!"
    s "Well then I can’t give you my pick."
    s "Also, no more questions please. You two are crowding me and making it hard to walk."

    scene black
    with dissolve

    "Of course, neither one of them agrees and I am questioned the entire way back to the dorm."
    "And, even more annoyingly, I don’t even get to go inside."
    "Instead, all of the girls band together and inform me that in order for me to steer clear of any potential strategies, I have to head home right away."
    "I still don’t know what exactly the first contest is, but I know it begins in the morning."
    "So I guess I’ll just...head back and go to sleep early or something."
    "I wouldn’t say I’m excited for whatever is going to happen tomorrow, but I’m not {i}unexcited{/i}."
    "In fact, I think there’s a pretty high likelihood that some of these battles could get a little heated."
    "I just hope that anyone who I wind up voting {i}against{/i} doesn’t wind up harboring any sort of ill will toward me."
    "That is the last thing I need right now."
    "………"
    "……"
    "…"
    "{i}Meanwhile, on the second floor...{/i}"

    scene dorminterviews5
    with dissolve

    mo "Molly MacCormack, back again and joined by two of the biggest underdogs on the second floor."
    mo "Noriko, or should I call you the Paralytic Pink Psion of the Old Realm-"
    n "Just Noriko is fine."
    mo "Then, Noriko, your matchup with Ami Arakawa has been voted almost entirely out of favor for you given her closeness to Sensei and his potential favoritism."
    mo "How do you expect to tear through the barrier and stake your claim on his heart as the ultimate imouto?"
    n "Easy."
    n "I am going to kill Ami."

    scene dorminterviews6
    with dissolve

    mo "You probably shouldn’t say that stuff when everyone already thinks you’re crazy."
    n "It’s a joke. Ami is going to be tough competition."
    n "But I think the fact that she’s been a {i}[niece]{/i} forever gives me a leg up."

    if bonus == True:
        n "I always looked at Sensei as kind of a big brother. Just a big brother I also wanted to kiss and sexually explore myself with."

    n "So, with that in mind, I think I’ve got a pretty good chance to-"

    scene dorminterviews7
    with dissolve

    mo "A-And you, Kirin?! How do you expect to take down Miku, another girl almost guaranteed to win?"
    n "Hey! I wasn’t finished talking!"
    ki "Mmm...to be honest, I’m kind of expecting to lose."
    ki "I just threw out the athletics test thing because it was the only thing that could come to mind. And I just wanted to go up against Miku."
    ki "But, as long as the test doesn’t really involve speed and is more of a strength thing, I think there’s a chance I could surprise everyone."

    scene dorminterviews8
    with dissolve

    mo "I think so as well! Never give up! And if the need arises, I’ll save my action to help you on your turn!"
    ki "Cool! Whatever that means!"
    mo "Oh, look! Here comes yet another combatant!"

    scene dorminterviews9
    with dissolve

    mo "Tsuneyo Tojo, your battle against Maya is seen as one of the biggest toss ups in the entire dorm war. How do you expect to take her down?"
    t "With brute force and underhanded tactics."
    t "I will crush her the way my father used to crush the necks of chickens in our backyard."
    mo "Great! Thank you for your time."
    t "Avast ye, scallywag. Open the register and nobody gets hurt."
    mo "Oh, look! Another two combatants!"

    scene dorminterviews10
    with dissolve

    mo "Joining me now are what we call the wild cards!"
    mo "Touka and Yasu, no one really knows what to expect of your battles. Do either of you have anything to say about them?"
    to "What is this? Some kind of interview?"
    to "If I have to sign a release form of some sort, I should probably be contacting my attorney first. I don’t know if this is good for my family’s image."
    ya "I don’t fully understand what I’m supposed to do, so I’m hoping someone will be able to help me."
    ya "And, in turn, I will help them any way I can so that when they pass on, they’ll be escorted into the second plane of existence, retaining their memories while leaving their physical form behind."
    mo "You’ll have to tell me more about that spell some time in the future!"
    mo "But Touka, one more question. A lot of people are wondering how you even wound up in a contest like this in the first place."
    mo "You’re one of the newest students we have, but...could it be you’re already falling in love with our teacher as well?! Are you another addition to the harem?!"

    scene dorminterviews11
    with dissolve

    if bonus == True:
        to "Love?! That man?! Absolutely not! My parents would never allow it!"
    else:
        to "Love?! That man?! Absolutely not!"

    to "I don’t know how I wound up in this competition either. I just..."
    to "Chika seemed so excited, so..."
    mo "Either way, I’m wishing the two of you luck! And Yasu, Priestess of the Night and devout worshipper of the Great Old One-"
    ya "He who sees with no eyes at all, yet all of the eyes in the universe."
    mo "Precisely!"

    scene dorminterviews12
    with dissolve

    mo "I just wanted to let you know I’ll be helping you with your dress. So don’t worry about doing too much on your own."
    ya "I look forward to your assistance. Please be gentle with your measurements so I do not become too stimulated."

    scene dorminterviews13
    with dissolve

    mo "Ah! Perfect timing!"
    mo "Nodoka and Otoha, you two are perhaps the fiercest competitors we have on the second floor."
    mo "Well, apart from myself that is."
    mo "Are the predictions right? Will you utterly demolish your first floor rivals? Or is there chance at all for an upset?"
    o "...Why are you touching me, Nodoka?"
    no "Hello, Molly. I’d prefer not to speak too much about my role in all of this, but I can assure you that there is no one more experienced with friend zoning people than my roommate here."
    o "Really, please let go."
    no "For years and years, Otoha Okakura has done nothing but reject any and all romantic advances. It’s actually quite astonishing."
    no "Some people may believe that she is simply waiting for the right person to swoop in and steal her heart, but I am 80%% positive that person is assuredly not Sensei."

    scene dorminterviews14
    with dissolve

    o "Wait, only 80%%? Why would you give Sensei a 20%% chance of being the one to finally make me feel like...that."
    no "Just a hunch. Though I may be bumping up the percentage a bit based on what I’d like to see."
    no "If anyone can crumble that cool exterior of yours, it could very well be the man you least expect to-"

    scene dorminterviews15
    with dissolve

    o "Oooooookay, I’m going into the room."
    o "And I’m going to win tomorrow."
    o "Tell Rin in advance that I’m sorry."
    mo "Oh...um. Yeah. Okay."

    scene dorminterviews16
    with dissolve

    mo "Oh! And here is the floor captain herself!"
    mo "Uta Ushibori, Violet Maid of the Ancient West, there are a lot of expectations riding on you as the captain of the second floor."
    u "There sure are! But I don’t want anybody to worry about me, I’ve got this in the bag."
    mo "Oh? And you’re positive that you’ll be the one taking home the chalice?"
    u "I don’t know anything about a chalice, but I do know that Ayane fell right into my trap and challenged me to the one thing no one has ever emerged from with their life."
    mo "So you have a history in rap battles?"
    u "Nope! But I’m still gonna win."

    scene dorminterviews17
    with dissolve

    u "Also, have you seen Io anywhere? Because she was supposed to walk home with me but she kinda just ghosted and now I’m starting to worry."
    mo "I haven’t..."
    mo "You don’t think that maybe she’s avoiding the competition altogether, do you?"
    u "I’m sure she’ll come around. If there’s anybody who can get her to cooperate, it’s me."
    u "Just kinda hard to do when she’s AWOL and stuff."

    scene dorminterviews16
    with dissolve

    u "But that’s a worry for another time! I’ve gotta go psych up the rest of the floor and prepare ‘em for the big day tomorrow!"
    u "Thanks for doin’ all this interview stuff, Molly! I can’t even imagine what those first floor girls are up to right now!"

    scene black
    with dissolve

    "………"
    "……"
    "…"
    "{i}Meanwhile, on the first floor...{/i}"

    scene dorminterviews18
    with dissolve

    ay "Ayane Amamiya here with the legendary Action News Now! And joining me today is captain of the first floor, Makoto Miyamura and her trusty sidekick, Miku Maruyama!"
    mi "That’s right! Team Makoto for life!"
    mak "Now, now. There’s no need to call Miku my assistant...even though her contest is basically over already."
    ay "Is that so?"
    ay "Miku, what do you have to say about this? Are you as confident in yourself as your best friend is in you?"
    mi "Heck yeah! I’m already fired up."
    mi "I’m just glad that me and Makoto are competin’ in what we’re competin’ in."
    mak "Makoto and I."
    mi "See what I mean? If I had to do any of that smart girl stuff, I’d be as useless as a sprinter in a wheelchair."
    mi "And if Makoto had to do anything even remotely athletic, she’d be even worse off than that!"

    scene dorminterviews19
    with dissolve

    mak "Okay...there’s no need to be rude."
    mi "What? You know it’s true. Ya can’t even make it around the block without huffin’ and puffin’ and-"

    scene dorminterviews20
    with dissolve

    mak "Ignore her. What she means to say is that our floor will be rooming with Sensei at the beach no matter what. You can mark my words."
    ay "I would certainly love to. But that doesn’t mean your battle is going to be one of the easy ones."
    ay "Nodoka Nagasawa is known as a prodigy all throughout Kumon-mi. Do you really think you can take her down in a test of knowledge?"
    mak "There’s only one way to find out, isn’t there?"
    mak "I’m sure she’ll be a valiant opponent, but I’m going to be a formidable foe."
    mak "And I’ve got the power of determination on my side."
    mi "That’s right! And in manga and stuff, the team that’s more determined always wins! We’ve got this in the bag!"
    ay "Well, we’re all certainly looking forward to it!"
    ay "Oh! And here comes someone else we’re all looking forward to seeing in action!"

    scene dorminterviews21
    with dissolve

    ay "Sana Sakakibara, how do you feel knowing that you’ll be competing in what many of us here at Kumon-mi are calling the “main event” of the first annual dorm war?"
    sa "Umm...c...confused?"
    sa "I still don’t...really know what I’m supposed to do and...a fashion show seems kind of..."
    ay "Like the opposite of what you want to do?"
    sa "Y...Yeah..."
    ay "Even though we all love you and cherish you and want to hug you until you pop?"

    scene dorminterviews22
    with dissolve

    sa "But...I don’t want to pop!"
    sa "I don’t know the first thing about fashion shows and...even if you all help me...the other girl is so much prettier..."
    ay "Nonsense. She’s cute, sure. But you’re Sana."
    ay "If it were up to me, I’d grant you victory right now."

    scene dorminterviews23
    with dissolve

    sa "Well...thank you, but...that doesn’t really stop me from being nervous..."
    ay "Just go get some rest and we’ll talk strategy when I’m done with my interviews, okay?"
    sa "Y...Yeah...Okay..."

    scene dorminterviews24
    with dissolve

    ay "Ayane Amamiya, still with Action News Now, but now joined by Rin Rokuhara and Futaba Fukuyama!"
    ay "First off, Rin, do you really think you can take down Otoha?"
    r "God I want nothing more than to take her down and just run my hands all over her-"
    f "She means beat her, Rin."
    r "Oh. Uhh...I don’t know. Maybe?"
    ay "It’s no secret that you and Sensei are close...and many people seem to believe that he’s already in your friend zone. Are you willing to confirm for us, right here and now, that you have already won this competition?"
    r "No comment!"
    ay "I guess we’ll just have to wait and see then, won’t we?"
    r "No comment!"
    f "Forgive her. She’s probably just trying not to say anything weird about Otoha again..."
    f "She can get tunnel vision and is probably...thinking things right now."
    r "No comment!"
    ay "Then, Futaba...your contest with Molly is one of few that the second floor girls seem to have the upper hand in at first glance."
    ay "How do you think you’ll fare using a character created by someone else to take down your own dungeon master?"
    ay "And, if victorious, how will that affect Molly’s attitude toward you in our campaign?"
    f "I’m sure that whatever happens will be fun for both of us..."
    f "If I get too focused on winning, losing will hurt ten times more if it actually happens."
    f "So...right now, I’m just trying to think up different strategies and...umm...learn how Sana’s character works since I’ve never played as him before..."
    r "Okay, I’m ready for my interview now! Hit me!"
    ay "Thank you Futaba and sorry Rin! Because we’re out of time for you and have yet another competitor coming to the stage as we speak!"

    scene dorminterviews25
    with dissolve

    ay "Chika Chosokabe! Hello!"
    c "Heya!"
    ay "So, Chika, a lot of people are quite jealous that you get to go on a date with Sensei as your competition."
    ay "And by “a lot of people” I am specifically referring to myself. I think that it is unfair and I am very upset that it was approved."

    scene dorminterviews26
    with dissolve

    c "Oh, come on. It’ll be totally fine."
    c "It’s not like we’re going to be alone or anything. I openly invited anyone who wants to supervise us to come and watch."
    c "All I’m really trying to do is gain some points for the first floor so we can {i}all{/i} spend some extra quality time with our teacher during the beach trip."
    c "And that includes you, of course."
    ay "Yes, I understand that. But you also challenged an incredibly rich girl to a battle to see who can throw a better date...and Sensei is very easily bought by material goods."

    scene dorminterviews27
    with dissolve

    c "I don’t think that’s true at all."
    c "Sensei is extremely generous and far from materialistic. And I’m ready to prove that the amount of money someone has does not mean they’d make a better romantic partner."
    ay "That’s cute and all, but I am still extremely jealous that you get to have a love contest with him as the center point."
    ay "I will not forget this, Chika."


    scene dorminterviews25
    with dissolve

    c "Sorry that I had the idea before you did!"
    c "Feel free to come watch if you want!"

    scene dorminterviews28
    with dissolve

    ay "Ahh, and last but not least, we have my two best friends in the whole wide world."
    a "Hi, Ayane. You’re really good at this journalist stuff."
    a "I particularly liked the part just now where you talked about how unfair it is that Chika gets to go on a date with Sensei and that I don’t."
    ay "{i}We{/i}. Not just you."
    a "Sure, whatever."
    m "No one is even recording this. What’s the point of conducting interviews if-"
    ay "Maya Makinami, I have just received word that the test of courage between you and Tsuneyo will be taking place at my house."
    ay "Will competing in a place you’ve been to multiple times now help to quell any uneasiness that would normally come with a test of courage?"
    m "...Where did you receive word from? We’ve been watching you this whole time."
    ay "Just answer the question, Maya."
    m "I mean...I guess? I don’t know."
    m "I haven’t really thought about it."
    m "Who’s even setting up the test of courage? How long will it be?"
    m "I have a bunch of questions."
    ay "Those questions would just go on to ruin the test! And I refuse to cheat, so you’ll just have to wait and see what’s in store."
    ay "As for you, Ami, a lot of people are saying you already have this contest in the bag. Do you have any response to that?"
    a "My response is that they are correct."
    a "If it involves Sensei, I will win."
    a "That is my role in not only his life, but my own."
    a "And if Noriko thinks she can swoop in and take that away from me, she can drink battery acid."
    ay "…"
    a "…"
    m "Fine by me."

    scene dorminterviews29
    with dissolve

    ay "Great! Well, that concludes our pre-war interviews! But join us tomorrow morning for more coverage as we kick things off with “Imouto Mode! Little Sister Contest!” right here on Action News Now!"
    ay "I’m Ayane Amamiya, and thanks for joining!"
    a "What are we looking at? There’s no camera there."
    ay "Just roll with it, Ami. Just roll with it."

    stop music fadeout 7.0
    scene black
    with dissolve

    "………"
    "……"
    "…"

    play sound "dooropen.mp3"
    scene bedroom_night
    with dissolve

    s "Hah..."

    "I make my way into the bedroom after an extremely confusing day."
    "No one bothered texting me back on my way home, so I don’t even know when the competition thing is going to start."
    "But to begin with Ami and Noriko facing off..."
    "It seems like that could get a little ugly."
    "I don’t really think either of them considers the other a {i}rival{/i} per se, but there’s definitely a good amount of history between myself and each of them."
    "I just hope that whatever happens doesn’t end up with one of them having their head ripped off and placed on a pike."

    s "…"

    "Welp, time to go to sleep."

    scene black
    with dissolve

    "I climb into bed and close my eyes, both nervous and excited for whatever daylight will bring."
    "………"
    "……"
    "…"
    "{i}Let the games begin!{/i}"

    $ renpy.end_replay()
    $ dormwar2 = True

    $ totaldays += 1
    $ day += 1
    if day == 6:
        hide friday onlayer date
        show saturday onlayer date

    "[totaldays] Days have passed..."

label dormwar3:
...
```

## Code that triggers this event

File: (install folder)None

Code:
```python
None
```