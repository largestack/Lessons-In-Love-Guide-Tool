# Swimming With Sharks
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo13&go=Go)


Part of event chain [Somewhere Far From Here](./dormwartwo12.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwartwo13
* Group: Main
* Triggered by label: dormwartwo12

## Event code
File: \game\chap3.rpy
Code:
```python
...
label dormwartwo13:
    "Our arrival at Tsukioka manor is met with the level of fanfare you’d expect out of the wealthiest family in Kumon-mi — red carpet and all."
    "But before I’m able to set foot on it, a team of guards escorts the girls who were able to come along off the bus and into a newly constructed viewing room so they can watch the contest without actually {i}being{/i} there."
    "I am not so lucky."
    "You see, instead of receiving the same red carpet treatment they do, I am blindfolded and thrown over the shoulder of a large man who I’m {i}pretty sure{/i} only speaks French."
    "Either that or he just has no interest in talking to me. But at least I can take solace in the fact that Imani has been kidnapped as well."
    "Or at least...I {i}would{/i} have been able to take solace in that if it were not for the fact that when I open my eyes, things are worse than I ever expected them to be..."

    play sound "static.mp3"
    scene sharktankparodydontsueme1
    with flash
    play sound "sharktank.mp3"

    "Meet the sharks- a team of self-made millionaire investors who are also entrepreneurs. "

    ima "I have not invested in a single thing. Nor do I have anywhere close to a million dollars."
    s "Who is that holding the camera? And why was it necessary to blindfold us for this?"

    play sound "static.mp3"
    scene sharktankparodydontsueme2
    with flash
    stop sound
    play music "oldweather.mp3"

    "Tsukasa Tsukioka is a venture capitalist who turned a six million dollar loan into three billion dollars overnight by investing in Bed Bath & Beyond as part of a short squeeze play."
    "She has since spent all of that money on a rogue crew of vandals who add new potholes to the streets of Kumon-mi in the middle of the night and she has no intention of ever fixing them."

    scene sharktankparodydontsueme3
    with fade

    "Tsubasa Tsukioka went from spending her free time reading advanced-level textbooks to organizing a series of for-profit organizations that have led many small businesses into violent bankruptcy."
    "Her net worth is unable to be disclosed as it would not be able to fit on this screen."

    scene sharktankparodydontsueme4
    with fade

    "Imani Imai is the daughter of an immigrant family from Croatia who rose to fame after opening up the world’s first nude lemonade stand."

    ima "That is not a thing that happened."

    "She also started her own clothing line at just seven years old and is currently working on building the ninth tallest building in the entertainment district of Kumon-mi."

    ima "Again, that is not true."

    "Additionally, she holds a 40%% stake in Google’s parent company, Alphabet, and sits on not just one board of directors, but nineteen of them across a variety of different sectors."

    ima "Why is this still going?"

    "She’s here today with the hope of landing a major deal that will generate enough profit for her to open up a bakery where she will create exclusively bird-shaped cakes."

    ima "Uhh-"

    scene sharktankparodydontsueme5
    with fade

    "And this is Sensei."

    s "Hi."

    scene sharktankparodydontsueme6
    with fade

    "Together...{i}they{/i} are the sharks. "

    s "..."
    ima "..."
    ima "On the bright side, at least we know where all of your screen time went."

    play sound "static.mp3"
    scene sharktankparodydontsueme7
    with flash
    stop sound
    stop music
    $ renpy.pause(5, hard=True)
    play sound "static.mp3"
    scene sharktankparodydontsueme8 with flash
    stop sound
    play sound "sharktank.mp3"

    "This is Nodoka Nagasawa, a budding entrepreneur from the border of Kumon-mi who is hoping to receive an investment from one of the sharks for her company, NODOKorp."
    "Nodoka is seeking a $400,000 stake in exchange for 10%% of her company — valuing it at $4,000,000."

    scene sharktankparodydontsueme9
    with dissolve

    no "I believe my ideas are worth a bit more than that. But I suppose I will leave it up to our judges to decide. "

    scene sharktankparodydontsueme10
    with fade

    ima "We don’t have to actually pay for this if we decide to go in, do we? Because I’m finna go out right now."
    tb "You don’t have to pay at all if you don’t decide to invest. Miss Nagasawa is simply looking for a platform to launch her company off of, and I would recommend only investing if you believe in the cause."
    s "Not to be a downer, but her {i}cause{/i} looks a little...{i}off{/i} to me."

    stop sound fadeout 2.0
    scene sharktankparodydontsueme11
    with fade
    play music "oldweather.mp3"

    no "Hiya, Sharks. My name is Nodoka Nagasawa...and I am here today with not just a business opportunity, but a chance for you to {i}change lives.{/i}"
    no "Sharks, did you know that over {i}six billion{/i} people in the world enjoy sex? That’s almost all of them."
    no "And if any of you are like me, I’m sure {i}you{/i} enjoy sex as well. But, let’s face it. Who doesn’t?"
    no "The thing is, it’s not enough to just have plain old sex anymore. "
    no "Japan’s reproductive rate is rapidly declining...and no one has been willing to step in and rekindle that flame."
    no "Until today."

    scene sharktankparodydontsueme12
    with dissolve

    no "Sharks, I am seeking $400,000 in exchange for 10%% of my premiere dildo company, NODOKorp."

    scene sharktankparodydontsueme13
    with fade

    tk "Mother, what is a dildo?"
    tb "It’s a toy designed for adults, dear."
    tk "If I be good, can I have one for Christmas?"
    tb "Ask Santa, dear. I will not speak about this any more."
    ima "Uhh...okay. I guess I’ll open up the floor with questions. What exactly is it about NODOKorp that stands out against your competitors? "
    ima "And how is a rubber dick going to make Japan’s reproductive rate go up?"

    scene sharktankparodydontsueme14
    with fade

    no "Both excellent questions."
    no "You see, before attempting to solve a problem, you need to first understand where that problem comes from."
    no "Our declining birthrate isn’t due to an issue with infertility. And it’s not due to an issue concerning lack of knowledge either."
    no "The problem is that our people don’t {i}want{/i} to have sex. So the obvious course of action would be to {i}make{/i} them want to have sex, correct?"
    ima "Uhh...sure. But how do {i}your{/i} products make {i}us{/i} want to bone?"
    no "By appealing to the one thing that gets {i}everyone{/i} horny-"
    no "Multiple women having sex at the same time."
    ima "I’m out. Too sketchy. "

    scene sharktankparodydontsueme15
    with fade

    no "Shame. I haven’t even handed out samples yet."
    tk "Forget about the samples, let’s talk numbers. How many units have you sold year to date? And how many do you expect to ship next year?"
    tb "Tsukasa, I forbid you to invest in an adult entertainment-"
    tk "Quiet. I’m talking business right now."
    no "Year to date, NODOKorp has sold and shipped roughly sixteen thousand units, with an estimated fifty-thousand expected to go out next year."
    ima "Jesus fuck, how?"
    tk "That’s over a 300%% increase. Are you going to be able to keep up with that level of demand? Or will aiding production be what my $400,000 goes to?"
    no "That’s precisely what I will be using the money on. With $400,000, NODOKorp will be able to switch to an overseas manufacturer and cut our production costs by roughly 60%%. "
    tk "Why can’t you switch now? Do they require a minimum order? "
    no "They do. And for each individual design nonetheless. "
    no "Thankfully, NODOKorp is on the brink of launching our next product, the {i}quadrildo,{/i} which will revolutionize this industry and has the capability to ship over 200,000 units just three years from now."

    scene sharktankparodydontsueme16
    with dissolve

    tb "Could you tell us a little more about this- dear God, what is that thing?"

    scene sharktankparodydontsueme17
    with fade

    no "{i}This{/i} is the quadrildo or, as I like to call it, the next step in sex technology."
    no "It combines two double-sided dildos into one-"
    ima "Yeah, we can see how it works."
    tk "Excuse me, but aren’t you out? Either come back in or keep your mouth shut."

    scene sharktankparodydontsueme18
    with fade

    ima "The fuck is up with kids nowadays?"
    s "Nodoka, as excited as I am about the prospect of four women using that thing at the same time, I’m not really sure if it will address the reproduction issue like you said it would."
    no "Sensei, are you telling me that watching all of the women in this room indulge in the wonders of the quadrildo {i}wouldn’t{/i} make you want to impregnate one of us?"
    s "I am. "
    s "Combine that with the fact that it’s a product I’d have no personal use for and...I’m sorry to say it, but I’m out."

    scene sharktankparodydontsueme19
    with fade

    tb "Miss Nagasawa, that is certainly an...interesting product you have there."
    tb "But unfortunately, I’m already invested in another company in this industry as of last night, which would make this a conflict of interest for me."
    tb "So, for that reason...I am out."
    no "I see."

    scene sharktankparodydontsueme20
    with fade

    no "I suppose it comes down to this, then. "
    no "Do you have any more questions for me, little Miss Tsukioka? Or are you ready to pound your worries away with NODOkorp?"
    tk "That’s not your slogan, is it?"
    no "It is."
    tk "Terrible. That needs to change."
    tk "But...I’m going to make you an offer."
    tb "Tsukasa, please."
    tk "I’ll give you the $400,000 you’re asking for..."

    scene sharktankparodydontsueme21
    with dissolve

    tk "But I want 40%% of the company."
    no "That cuts the valuation of my business to a mere one million dollars. And with a total addressable market of over six billion people, I believe it’s worth a great deal more than that."
    tk "As do I. Which is why I’m also willing to make a royalty deal."
    tk "I can cut my equity down to 20%% so long as I receive royalties on every product sold for the next five years at $5 a unit. "

    stop music fadeout 15.0

    tk "That way, if you {i}do{/i} hit your projected goal of 50,000 units next year, I’ll already be close to recouping my initial investment...while you’ll be ramping up production."
    no "That still seems a bit too steep when you factor in the additional royalties you’ll be receiving for the subsequent four years."
    tk "It does, but you need me more than I need you. So my offer is firm and you can take it or leave it."
    no "Would you perhaps be willing to shorten that royalty deal to-"
    tk "I’m out."

    scene sharktankparodydontsueme22
    with fade
    play sound "sharktank.mp3"

    no "Very well."
    no "Thank you all for your time...and for your continued interest in NODOKorp."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    play sound "static.mp3"
    scene rslfuckyeah with flash
    play music "rapid.mp3"
    stop sound

    "Hey kids! Do you want a mobile game that rewards you every day for just logging on?!"
    "One with graphics that’ll make your dick so hard it can cut diamonds and then grow a mouth to EAT those diamonds so it becomes a super strong DIAMOND DICK?"
    "Then how about trying RAID SHADOW LEGENDS? The number one mobile game that’s sure to make girls like you and your parents proud of you again!"
    "Here’s a real testimonial from a real mom whose real son started playing RAID SHADOW LEGENDS!"

    play sound "static.mp3"
    scene rslfuckyeah2 with flash
    stop sound

    legitmom "Hi I am a totally legitimate mother whose son started playing RAID SHADOW LEGENDS recently"
    legitmom "Ever since little Jimmy started playing RAID SHADOW LEGENDS he has stopped eating dinner at the table and it is tearing our family apart"
    legitmom "All day long I hear the screams of dying orcs and all of the girls that he is having sex with and it is making me question my abilities as a mother"
    legitmom "Please Plarium Games make him stop I do not know how much more our family can take of this I just want my child back"

    play sound "static.mp3"
    scene rslfuckyeah with flash
    stop sound

    "Doesn’t that sound like an AWESOME FUCKING GAME? Or are you going to be a little bitch like Jimmy’s mom and just hold a soccer ball all day?!"
    "Don’t be a CUCK! Play RAID SHADOW LEGENDS NOW!"

    stop music
    play sound "static.mp3"
    scene sharktankparodydontsueme23 with flash
    play sound "sharktank.mp3"

    "Meet Yumi Yamaguchi — a struggling entrepreneur with an extensive background in business management and customer relations."

    y "Who the fuck are you? Get that fucking camera out my face."

    "Yumi Yamaguchi is looking for $100,000 in exchange for a 51%% controlling stake in her social networking company, Study Buddy."

    scene sharktankparodydontsueme24
    with dissolve

    y "Yo! I told you to get that fucking camera out of my face, asshole!"

    "Starting at a very young age, Yumi faced a great deal of opposition in terms of-"

    y "That’s it! You’re dead!"

    play sound "static.mp3"
    scene techdif
    with flash
    stop sound
    play music "cafe.mp3"
    $ renpy.pause(7, hard=True)
    stop music
    play sound "static.mp3"
    scene sharktankparodydontsueme25 with flash
    stop sound
    play music "oldweather.mp3"

    y "Uhh...hi."
    y "Anybody have any idea how much that camera I just broke costs? Because I think I’ve gotta add the price of that to the money I need from you guys."
    tb "Oh my...I believe it was somewhere in the realm of seven thousand dollars."
    y "Then hi. I’m Yumi Yamaguchi and I’m here today looking for $107,000 in exchange for 51%% of my company, Study Buddy."
    y "I’m sure that at least two of you are surprised to see me given uhh...recent circumstances and shit. But Nodoka is a fucking cunt and I want to beat her, so that’s why I’m here today."
    ima "Luckily for you, I can’t imagine that will be very hard!"
    tb "Tell us a bit about your company, dear. What is it that “Study Buddy” does?"
    y "Let me start by saying I had no idea I was supposed to make a logo or give out samples or anything like that."
    tk "Talk about unprepared."
    y "Fuck off, brat."

    scene sharktankparodydontsueme26
    with fade

    y "So, uhh...right. Sales pitch. Let’s see here..."
    y "S...Sharks, how many times has this happened to you?"
    y "You’re sitting in your room...all alone and shit. And you’re a fucking idiot, so you’re just...kind of existing and being worthless and crap."
    ima "Finally, a product I can relate to."
    s "I’m pretty sure you could have figured out a way to relate to the four-sided dildo as well."
    y "Well...Study Buddy aims to solve that problem by...giving even the most worthless of people a reason to both exist {i}and{/i} make money."

    scene sharktankparodydontsueme27
    with fade

    y "It’s no secret that dating apps and shit like that have become the way of the future."
    y "And in a society that’s moving closer to no one ever having to leave their house again, an app needs to be at the...fuck, what was the word again?"
    y "Oh, yeah. The {i}forefront{/i} of innovation in regard to its...respective sector?"

    scene sharktankparodydontsueme28
    with dissolve

    y "Study Buddy...uhh...aims to connect students of all ages with both tutors and friends and...babysitters or...whatever else a customer needs."
    y "Like...I don’t know. Maybe if you want your house cleaned or some shit too? I ain’t really ironed out all the kinks yet."

    scene sharktankparodydontsueme29
    with fade

    tb "Is Study Buddy partnered with licensed teachers, caretakers, tutors...etcetera? Or is this something that anyone can sign up for at their own leisure?"
    y "Well, I ain’t sure I’d call it “leisure” since the whole object is to make money from people who need some kind of shit done for them."
    y "So, that in mind, I guess anybody can sign up if they want. Just like, put your name down and say what you’re willing to do for how much and...hope somebody pays you."
    tb "What systems are in place to prevent users from utilizing Study Buddy for nefarious purposes like prostitution or drug sales?"
    y "Oh, we tell you not to do that shit in the ToS. And no one has ever broken any rules in any ToS before so we’re good."
    tb "Excellent. I see you’ve done your research."
    tk "But why the name “Study Buddy” if the platform is not centered solely around studying?"

    scene sharktankparodydontsueme30
    with fade

    y "I figured a name that’s easy to remember and kid-friendly would be best since that’s the target demographic and shit."
    ima "It’s an app to...extort children?"
    y "It ain’t extortion if they’re gettin’ somethin’ outta the deal, right? And credit card info is needed in order to hire anybody, so it’d be the parent’s money and not the actual kids anyway."
    tb "Interesting. But why develop a product like this? What’s the story behind it?"
    y "Story’s boring. Just wish I had something like this when I was a kid so I wouldn’t have had to teach myself how to read and all that."
    y "If I could’ve just swiped my dad’s card and hired somebody to come hang out with me or teach me words and shit, I probably would have wound up a little less shitty."

    scene sharktankparodydontsueme31
    with dissolve

    ima "That’s a nice story and all, but the fact that you’re willing to give up 51%% of your company in exchange for just $100,000 tells me you might not {i}believe{/i} in the product."
    s "Why are you suddenly so into this?"
    ima "When in Rome, bruh."
    y "Oh, I had a response to this. Uhh..."
    y "Right! Yeah. So, what I’m selling ain’t really a business yet. It’s an {i}idea.{/i} Which is why I’m willing to give up a controlling share of it."
    y "Past experiences have shown me that I don’t know the first thing when it comes to running a business. So I’m probably more suited to just, like...coming up with shit, you know?"
    y "If I can focus on, uhh...more ideas or whatever, I can see this thing maybe kind of possibly working or something."
    ima "Unfortunately, Yumi...I’m not interested in investing in a product that will “maybe kind of possibly work or something.” So, for that reason...I am out."
    y "Cool, you ain’t got the money anyway."

    scene sharktankparodydontsueme32
    with dissolve

    tb "Let’s talk a little about monetization as you’ve made it clear you have no sales yet."
    tb "In this vision of yours, where Study Buddy is used as a platform for freelance workers, how do you generate revenue?"
    y "I figured we’d just take a cut or something. I ain’t really good when it comes to numbers."
    y "We could probably charge some sort of subscription fee too and-"
    tk "I’m going to make you an offer, but you have to say yes right now."

    scene sharktankparodydontsueme33
    with dissolve

    tb "Tsukasa?"
    y "Wait, right now? But I haven’t even heard the offer yet."

    scene sharktankparodydontsueme34
    with fade

    tk "Miss...Yamaguchi, was it?"
    y "You were calling me Yumi literally all day yesterday."
    tk "I think this app of yours is a great idea...and one that I can see myself using as I also find myself getting lonely at times."
    tk "But it’s evident that all of the actual {i}work{/i} still needs to be done as, according to my notes, all you have come up with is an idea and a name."
    tk "Which is fine...as all of the major conglomerates out there were once {i}just{/i} ideas as well."
    tk "The issue is, no {i}idea{/i} is worth the amount of money you’re asking for.  And developing this app alone will take much more than that."
    y "Still haven’t heard the offer."

    scene sharktankparodydontsueme35
    with dissolve

    tk "I’ll give $10,000 for 100%% of your {i}idea,{/i} which can hardly be called a company."
    tb "Tsukasa, that’s nearly your whole allowance."
    tk "And, to be honest, that’s an extremely generous offer as I could just {i}take{/i} your idea since there’s nothing proprietary about it."
    tb "I, too, would like to make you-"
    tk "Don’t listen to her. If you listen to her offer, I’m out."
    tb "I am your {i}mother.{/i} I reserve the right to-"
    y "You’ve got a deal!"

    scene sharktankparodydontsueme36
    with dissolve

    tk "Yay!"
    tb "Oh, gosh darn it. I would have given her what she asked for."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene sharktankparodydontsueme37
    with dissolve2

    tk "An excellent presentation for your first time, Miss Yamaguchi. I take it a certain...pre-existing business partner of mine was involved in its creation as well?"
    y "Yup. Chinami and I stayed up late last night going over all of the details. Pleasure doing business with you, brat."
    tk "Likewise. I’ll have my people reach out to your people and wire the money over by the end of the day."
    y "Uhh...but what if I ain’t got “people?”"

    scene sharktankparodydontsueme38
    with dissolve

    tk "Mother! Can I have an advance on next week’s allowance?"
    tb "That depends. Can I have 10%% of Study Buddy?"

    scene sharktankparodydontsueme39
    with dissolve

    tk "Can you wait until next week?"
    y "Yeah. One more week of bein’ poor ain’t nothing to me."
    tk "Nevermind, Mother! Your assistance is no longer needed!"
    tb "Darn it again!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene sharktankparodydontsueme40
    with dissolve2

    ima "Congrats, Yumi. I haven’t seen that much money at once since the last time I robbed a bank."
    s "Yeah. That was a surprisingly...{i}good(?){/i} presentation."
    y "Thanks..."
    ima "..."
    s "..."

    scene sharktankparodydontsueme41
    with dissolve

    ima "I don’t think she wants to talk to us."
    s "Maybe...let me handle this, Imani. You can go back to organizing assorted Dorm Wars things."
    ima "Roger. And remember, if shit hits the fan, make sure your thumbs aren’t tucked into your fists when you have to punch. Got it?"
    s "Got it..."

    scene sharktankparodydontsueme42
    with dissolve

    "Imani walks away and-"

    y "Didn’t realize you were gonna be here."

    "And things go back to normal."

    s "It wouldn’t really make sense for me {i}not{/i} to be here when I’m the prize."
    s "I’m glad you were able to show up, though. I’ll admit that I didn’t think you were-"

    scene sharktankparodydontsueme43
    with dissolve

    y "I ain’t ready to talk to you yet."
    y "And, honestly, not sure when I {i}will{/i} be."
    y "Out of all of the horrible shit you’ve done to me...that was a new low. A low I didn’t think that even someone like {i}you{/i} would ever touch."
    y "So, yeah. I came to your stupid, little contest. But I did it for {i}me.{/i} And it would be really fucking cool if we could go back to ignoring each other now."
    y "Finally have a little peace for the first time in my fucking life and-"

    scene sharktankparodydontsueme44
    with hpunch

    c "Yumi! You did it! Oh my God! What are you going to do with all of that money?!"
    y "Well, the first step is converting it to yen. After that, no fucking clue."
    c "I’m so happy for you! I knew you could do it! And I’m so glad I didn’t have to since I, like...totally would have dropped the ball!"
    y "Guess I ain’t totally worthless after all, huh?"

    scene sharktankparodydontsueme45
    with dissolve

    no "Congratulations, Yumi. You did an excellent job and should be proud of yourself."
    no "I must know, though...do you plan on listing your services on the finalized Study Buddy app? Because I’d be more than willing to hire you for all sorts of-"

    scene sharktankparodydontsueme46
    with dissolve

    no "Oh, okay. See you later then."

    scene sharktankparodydontsueme47
    with dissolve

    c "Hah...just leave her alone, Nodoka. It’s clear she doesn’t want anything to do with you and you’re just going to make things worse for yourself."
    no "What? I was simply hoping to hire someone to teach me self defense for the next time I am beaten within inches of my life."
    s "Not right now, Nodoka."
    no "When would be a better time? Children and Yakuza aren’t the only ones who get lonely, you know?"

    scene sharktankparodydontsueme48
    with dissolve

    c "He said beat it."
    no "Right now? But that would risk soiling my kimono."
    c "Nodoka-"
    no "Fine, fine. I’ll leave you two alone."
    no "But, should you find yourself utilizing that time to get a little {i}closer{/i} to one another, please feel free to help yourself to the table of quadrildos in the room next to this one."
    no "Farewell, friends."

    scene sharktankparodydontsueme49
    with dissolve

    c "Hah..."
    c "That girl is so fucking weird."

    $ renpy.end_replay()
    $ dormwartwo13 = True
    $ dorm1war2points += 1

    if chika_lust >= 25:
        jump chikalust25
    else:
        jump chikalust25skip

label dormwartwo14:
...
```

## Code that triggers this event
File: \game\chap3.rpy
Code:
```python
...
r "Just start calling him Dad like I have. Plus, he’s already Ami’s uncle and I’m pretty sure she’d kill any of us if we started calling him that."
    o "I’ll just keep calling him Sensei. I’m not really sure how my {i}actual{/i} dad would feel if he found out I was calling my teacher Dad as well."
    r "Just don’t let him find out, then. It’s as simple as that."
    o "Easy for you to say when you’re free to call him Dad as much as you want without the fear of replacing someone."

    scene anotherbusride13
    with dissolve

    o "Oh! Speaking of which, is your mom still coming tonight? I wanted to apologize to her for being all awkward the last time I met her as well."
    o "In fact, I’m pretty sure this is just going to be an “Otoha apologizes to everyone” night. So if you know anyone else I have wronged or inconvenienced, please add them to the list."
    r "I know one person. And she’s actually right here on the bus with us. "
    r "Her name begins with a C and ends with a...painful rejection on the beach that leaves you crying in your teacher-dad’s arms for the rest of the night."

    scene anotherbusride14
    with dissolve

    o "I think that apology can wait. That one sounds awkward. "
    o "I’ll just get the adults out of the way today. That’ll work."
    r "In that case, my mom {i}is{/i} still coming to Sakaki-bar-a later. But I have asked her to stay at least fifty feet away from me at all times so no one will know we are related."
    o "You say that as if you’re not adopted and that standing next to her will somehow reveal that you’re the same person with slightly varying degrees of...lesbianness? "
    o "Lesbianocity? Is that a word? That should be a word."
    r "Ooooh, Lesbianocity should be our band name."
    o "I suddenly have no desire to pursue a musical career anymore."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene anotherbusride15
    with dissolve2

    to "Is something wrong, Yasu? You haven’t said a word since we’ve set foot on the bus."

    scene anotherbusride16
    with dissolve

    ya "My body feels strange...{i}wrong...{/i}"
    to "Already? You’re nearly two weeks early. Just grin and bear it until we arrive at the manor and-"
    ya "I’m not talking about the shedding of my uterine lining-"
    s "Okay, I’m going to go sit somewhere else now. This must be my punishment for complimenting Haruka’s uterus yesterday."
    to "Why would you ever-"
    ya "I’m talking about the slow burn of the essence inside of me...dumping buckets full of barley tea onto the embers of the unholy in an effort to extinguish them."
    ya "The way this steel box moves is wrong. It’s as if it’s going backwards...inching closer and closer to what should not belong. To what should not {i}exist.{/i}"
    s "I think this is Yasu’s way of telling you she has a major issue with the unequal distribution of wealth in Kumon-mi."
    to "Is that reason enough for my family to not {i}exist?{/i}"

    scene anotherbusride17
    with dissolve

    ya "Please listen to me..."
    ya "I don’t want to hurt her..."
    to "What? Hurt {i}who?{/i} Who are you referring to, Yasu?"
    ya "I don’t know. The vision is blurry...obscured behind the glass of 357 mirrors where all I can do is stare back at the melting visage of the loneliest girl. "
    ya "If the mirror will not shatter, what can I do?"
    ya "If the light will not scatter, will the pain just bleed through?"
    to "Oh, excellent rhyme, Yasu! Perhaps we should buy you a few children’s books to sharpen those skills?"
    s "Doesn’t it always, though?"
    to "Sensei?"
    s "The pain...doesn’t it always bleed through?"
    s "You always ask why everything hurts so much...isn’t this just more of that?"
    ya "I..."
    ya "I don’t know..."
    s "If you truly love your god...why do you doubt the way he makes you feel? Why do you doubt the thoughts he makes you think?"
    ya "Because it is not He who gives me these things. These {i}thoughts...{/i}"
    ya "It is an {i}interference.{/i}"
    s "From...what? Or Who?"
    ya "Again...I don’t know..."

    scene anotherbusride18
    with dissolve

    ya "But if I listen closely..."
    to "..."
    s "..."

    scene black
    with dissolve2
    stop music fadeout 15.0

    ya "I can hear the ocean."

    "Yasu doesn’t speak again for the rest of the ride to Tsukioka Manor."
    "And Touka remains “elegant” the whole way there."
    "Even when she falls asleep on my shoulder."

    $ renpy.end_replay()
    $ dormwartwo12 = True
    $ yasu_love += 1
    $ touka_love += 1

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    jump dormwartwo13
...
```