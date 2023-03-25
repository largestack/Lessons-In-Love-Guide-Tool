# With Her (Tsuneyo)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Approximation](./slumberreset2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: tsuneyoslumber1
* Group: Tsuneyo
* Triggered by label: slumberreset2
* Chain sources: slumberreset2
* Chain sources path: slumberreset2

## Official wiki page

[With Her](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=tsuneyoslumber1&go=Go) for more details.

## Event code

File: (install folder)\game\TsuneyoEvents.rpy

Code:
```python
...
label tsuneyoslumber1:
    if yumislumber3 == False:
        scene mayanebench30
        with dissolve

    play sound "phonebeep.wav"

    if yumislumber3 == False:
        "Molly — considering it’s not really possible to call Tsuneyo when I still don’t have her phone number."
        "As such, I tap on her roommate’s name and wait for {i}her{/i} to answer instead."
    else:
        "I tap on Molly's name in my phone and wait for her to answer since I have no way of getting in contact with Tsuneyo."

    "........."
    "......"

    play sound "phonebeep.wav"

    mo "‘Ello?"
    s "Hey. It’s me. Ignore the unknown number. It’s a long story."
    mo "Why if it ain’t Kael’thas himself!"
    s "It ain’t. I mean...it {i}isn’t.{/i} Who?"
    mo "Kael’thas Sunstrider, former prince of Quel’Thalas and senior member of the Kirin Tor. And also one of the first video game characters I ever- nope. Shouldn’t tell you that."
    s "Is this the part where you clarify why you thought I was a video game character?"
    mo "Only if it’s the part where you pretend to be interested!"
    s "It’s not."
    mo "Well, it’s because you came back from the dead. None of us had any idea where you ran off to on Christmas Night, Sir! A regular Irish goodbye if I don’t say so myself. And I can! Because-"
    s "Because you’re Irish, I know. Do you have Tsuneyo’s phone number? "
    mo "Do you not? Aren’t you the father of Noodles the Unholy?"
    s "When did he earn such a threatening title?"
    mo "'Tis just the way he strikes me, I suppose. What do you need Tsuneyo’s number for, Sir? Last I heard, you two were still at odds."
    s "It’s complicated. "
    mo "Does it involve time travel?"
    s "No, it- what? How did you know that?"
    mo "Typical plot development at this point in the story. It was either that or I was about to find out you two have been spoonin’ behind me back this whole time."
    s "You read some weird stories."
    mo "Don’t even get me started, Sir. I’ll text you the number now. But I’m gonna warn ye’! Don’t go sendin’ any text messages that may alter the path of the future!"
    mo "Last thing we need is a world where Ami keeps dying over and over and you’ve gotta work through chronic depression and other shite just to bring ‘er back."
    s "Number please, Molly."
    mo "Aye aye! Until we meet again, Sir!  "

    play sound "phonebeep.wav"
    stop music fadeout 10.0

    if yumislumber3 == False:
        scene black
        with dissolve

    "Just seconds after hanging up the phone, I receive a text containing Tsuneyo’s contact info."
    "But when I go to call her, I quickly take note of the lack of a dial tone or ringing and am left standing on the sidewalk wondering what else I should do to get in contact with her."
    "It’s clear she wasn’t with Molly as I’m {i}pretty{/i} sure she would have informed me of that while we were on the phone, so..."
    "She’s either at the archery range or Tojo Ramen."
    "And while I’m significantly closer to school than I am to the second half of town, I have a very strong feeling that going to the former would just be a waste of time in the end."
    "As such, I set off on what’s sure to be a very long walk-"

    play sound "static.mp3"
    scene tsuneyobridge1 with flash
    stop sound
    play music "blueair.mp3"

    "And I arrive."
    "Tsuneyo stands at the railing of a bridge where I once met someone doing something after thinking of someone who she’d forgotten or something."
    "She looks up at the sky and thinks of...probably noodles, if I had to take a guess. But I think of something else."
    "Something pure, though not the type of purity you’d typically associate with someone much stronger than me."
    "I think of what it would be like to wake up in a world and not have to worry about who remembers what or when or why any of this is happening in what should have been my peaceful life of debauchery."
    "If those that I have wronged could too live in a world like that, I wonder what would become of us."
    "And I wonder what would become of me, who sacrificed everything so they could go on untouched."
    "I give up the thought as I don’t have the right to think it."
    "Not while I’m still blooming."
    "Not while I’m here with her."

    play sound "static.mp3"
    scene tsuneyobridge2 with flash
    stop sound

    "I take my place beside her and gaze up at the same sky."
    "Or is it?"

    t "Does the weather today strike you as odd?"
    s "Not particularly. But it {i}is{/i} odd to see you out here instead of slaving over a hot stove in an old ramen shop."
    t "Since the moment I woke up, I've felt like something is wrong. But I suppose it is just me."
    t "Perhaps it will rain? That would be exciting, wouldn’t it?"
    s "I...guess?"
    t "It doesn’t rain very often. {i}Any{/i} change is exciting. "
    t "Which is why I am surprised that standing here fills me not with joy, but with the concerning hope that these calm summer mornings will one day cease to be."
    t "When that day comes, I wonder what will happen to this place?"
    t "I wonder what will happen to me?"
    s "You’re in a...{i}different{/i} kind of mood today. Did something happen at the store? Is the power out again?"
    t "I haven’t returned home yet, so I’m not sure."
    t "I was on my way there, but felt compelled to stop when I was overcome with a great sense of worry. So great I suppose it could even be called fear."
    s "Fear of what, exactly?"
    t "I’m not sure. "
    t "Perhaps fear itself? That {i}is{/i} the most terrifying thing out there according to a wise man known only as Franklin Delaware Roosevelt."
    s "I think you’re a little off, but it was a valiant effort."

    play sound "static.mp3"
    scene tsuneyobridge3 with flash
    stop sound

    t "Were you looking for me? Is that why you are here?"
    t "I apologize for the inconvenience, but I will not be able to serve you until I return to the store. "
    s "That’s fine. I’m not really hungry in the first place. I {i}was{/i} looking for you, though."
    t "Why would you come looking for me if you are not hungry? No other motivation makes sense."
    s "I need your help saving the world...or something."
    t "Does it involve time travel? The Emerald Guardian would say that would be a typical tool for plot development at this stage in our relationship."
    s "It does and she did. Also, you two are way too close. Start having thoughts of your own again instead of just hijacking all of her geek-knowledge."
    t "If you need assistance constructing a time machine, I regret to inform you that I will be unable to help as I am already employed at a local business. But I wish you the best of luck in your endeavors."
    s "How about just a slumber party then?"

    scene tsuneyobridge4
    with dissolve

    t "I’m not sure if that is a good idea. The only time I slept at your house ended rather strangely. It {i}was{/i} nice using your kitchen, though. Even if you do not have an industrial size stock pot."
    s "I can...barely even remember you ever sleeping at my house."
    t "That’s unfortunate. I thought it was a nice moment for us. But I suppose we’ll have more opportunities for better moments in the future."
    t "For now, I..."
    s "..."
    t "..."
    s "...Need to get back home?"
    t "Actually..."

    scene tsuneyobridge5
    with dissolve

    t "Do you think that we could go somewhere instead? I’m still not comfortable returning to the restaurant at this point in time."
    s "Is that okay? Won’t it stay closed for the entire day if you’re not there to, you know, {i}open{/i} it?"
    t "It will. But business has slowed down as of late and even our regular customers are dropping by less frequently. "
    t "I believe that one day off will not cause enough harm to the restaurant to form any long-lasting issues or problems for us."
    s "I mean, I’m fine with it. You deserve a day off. And if you want to spend that day off going on a date with your teacher, that’s completely fine."
    t "Thank you. I appreciate that."
    s "Oh, okay. I was kind of expecting you to clap back about the date thing. I was just joking, you know. I don’t actually think-"
    t "Dating me is a joke to you? "
    s "What? No. "
    t "I do not understand. I thought you were attracted to teenage girls?"
    s "Alright, now I’m just confused. "
    t "That is okay. You are at the point in life where it is normal to question such feelings. Just know that I will respect you the same regardless of your heart’s true desires."
    s "That-"
    t "It is a very minimal amount of respect, but still. That much will not change."
    s "..."
    t "..."
    s "Is this a date or not? Because that’s not what I came here for, but I’m totally fine with it if you are. "
    s "Plus, it’ll probably make what I actually {i}did{/i} come here for significantly easier in the long run."
    t "At least you are honest enough to not hide your ulterior motives any longer. I thank you for that."
    s "Yeah, I could have worded that last sentence better. But I can assure you I didn’t mean it like {i}that.{/i}"

    scene tsuneyobridge6
    with dissolve

    t "It’s fine if you did."
    s "{i}What?{/i}"
    t "It is only natural that you would want to impregnate me."
    s "Have you been drinking or something?"
    t "Extending one’s lineage is a desire ingrained into all men at birth. And it is the same for me as I am the only one who can carry on my family’s legacy at this point in time."
    t "As such, I know that I will one day bear children. And seeing as you are the only man I am in regular contact with, those children would most likely belong to you."
    s "Uhh...maybe I should just head back home? This isn’t really a discussion I want to be having."

    scene tsuneyobridge7
    with dissolve

    t "Neither do I. Why would I ever look forward to carrying the children of a man as deplorable as you?"
    s "I’m getting so many mixed signals right now."
    t "I am simply stating it would make sense to have your children — not that I {i}want{/i} to."
    s "And the date thing?"

    scene tsuneyobridge8
    with dissolve

    t "Hm..."
    s "See? If you’re averse to looking at me romantically, don’t sign up to-"
    t "Upon careful introspection, I continue to see little downside in regard to something as simple as a date."
    t "It is my understanding that many dates come with the complete lack of romantic contact. What prevents us from going on a date like that other than your inability to provide a straight answer?"
    s "I think the idea of dates {i}like that{/i} is the hope that they will one day lead to something more."
    t "So...the reason for your hesitancy is because you might one day...want something more?"

    scene tsuneyobridge9
    with dissolve

    t "Again, I don’t understand. Why would that be a problem?"
    s "It’s not for me. It is for {i}you,{/i} though. Right? Like, you’re clearly not interested in me that way and you’ve made it apparent a number of times now. Why date anyone you feel that way about?"
    t "Because those thoughts may change. And I don’t understand what the harm would be in providing them the opportunity to."
    t "What is the sense in depriving oneself of something one may someday enjoy on account of temporary, present-day uncertainties? "
    s "You’re really confusing sometimes, Tsuneyo."

    scene tsuneyobridge10
    with dissolve

    t "Ah-"
    s "And you are still doing that, I see..."

    scene tsuneyobridge11
    with dissolve

    t "The one who is confusing is you. "
    t "If you’d simply accepted my acceptance that I may one day have to accept you, our “date” would have been well underway by now."
    t "But I suppose we can call it something else if you are so undoubtedly certain that we will never be anything more than who we are now."
    s "..."
    t "It seems as though I am not the only one who is acting out of sorts today. "
    t "All it took was one mention of the minute probability that we will one day learn to cherish one another to leave you staggered and speechless."
    t "I like these new sides of you that you’ve been showing me lately."
    t "They remind me you have a human side."
    s "I didn’t realize I had an {i}inhuman{/i} side."
    t "That’s very surprising to me when you’ve always felt part-machine."

    scene black
    with dissolve2

    "Tsuneyo pulls herself away from the bridge and walks toward the center, replicating another view I’ve seen at least once before..."

    scene tsuneyobridge12
    with dissolve2

    "But the sun comforts me in ways that the moon did not."
    "It is not the warmth, nor the way I have to shield my eyes from its blinding glow — but the way Tsuneyo catches it between each squint of my eyes."
    "If there is a future for us, I can’t imagine such a view will ever get old."
    "But as much as I’d like to believe that she’s thinking the same about me right now..."
    "I can’t shake the feeling that I’m nothing more than an obstacle stuck between where she currently is and where she {i}wants{/i} to be."
    "Away from here."
    "Away from the building she grew up in and the rotting shell of what was once a town and a bridge and a sky and streets filled with dust and overgrown weeds-"
    "I get so caught up in my own confusion that I wind up forgetting why I came here in the first place."
    "And instead of arriving with the idea that she’s special because she is an outlier, I am {i}leaving{/i} with the knowledge that she is special because she simply {i}is.{/i}"
    "The universe and all of its games have nothing to do with that."
    "If the future will not force us together, so be it. I can live with one less body beneath my sheets."
    "But I can {i}not{/i} live if I go on denying the possibility of that."
    "Let this day show me her true colors by transforming her body into a prism that spills its rainbow guts all over me and {i}cleanses{/i} this impure soul of its disease."

    t "You feel it too, don’t you?"
    s "Huh?"
    t "The weather."
    t "It’s different today."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "I’m not quite sure what she means...but I nod and pretend that I am."
    "And I let her lead the way to wherever it is we’re going."
    "But I’m haunted on the journey by the shadow of something much larger than me. "
    "And my fleeting bliss is plucked from my hands as if it were never mine to enjoy in the first place."
    "Perhaps one day in the future, I will be able to rest."
    "..."
    "The shadow reminds me in all of my unease that the future may never come if the rise of the moon and its accompanying darkness consumes the other twenty shadows following closely behind."
    "The tallest of them all looks the nicest next to mine right now."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ tsuneyoslumber1 = True

    jump tsuneyoslumber2

label tsuneyoslumber2:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
ay "Is there more to it than just literally disappearing?"
    m "Very. I’m basically desensitized to it by now but, if you’re willing to give it a shot and don’t mind seeing something you will very likely never forget unless you’re fully reset, fine. We can have a “slumber party.”"
    m "But good luck trying to get Yumi and Tsuneyo to agree to it. And good luck finding a place to actually have it since getting Ami involved is basically asking to be cut off from engaging in any real conversation."

    scene mayanebench22
    with dissolve

    ay "I’d say we can use my house, but I know for a fact Geoffrey wouldn’t let me have a sleepover with Sensei. He’s been very protective ever since Todd disappeared."
    ay "But yeah...getting Yumi and Tsuneyo to agree to something like that does sound hard when we’re not really close to them."
    s "I’m not really close to them either, but...I’ll see what I can do. "

    scene mayanebench23
    with dissolve

    m "Will you find us a place to sleep as well? Preferably one we don’t have to pay for since I am currently broke and Ayane’s card is being declined everywhere."
    ay "Yup! Turns out that while the three of us were being tossed through time, my credit card was being tossed through every single terminal in Kumon-mi! "
    ay "I’m cut off from spending anything until next month when the bank sorts everything out."
    s "Wonderful. That extremely inconvenient coincidence is basically forcing me to reveal something I was {i}hoping{/i} I’d be able to keep quiet for a full twenty-four hours. But fuck me, I guess."
    ay "I would if could, Sensei. I would if I could."
    m "And what exactly do you have to reveal? A second home that none of us know about?"
    s "Yes."
    m "Funny. What {i}actually{/i} is it?"
    s "A second home that none of you know about."

    scene mayanebench24
    with dissolve

    m "What? When? Why?"
    ay "Wait a minute...who drew your name for Secret Santa this year?"
    s "Touka."

    scene mayanebench25
    with dissolve

    ay "Mystery solved. Detective Ayane has successfully closed another case."
    m "She got you a {i}house?{/i}"
    s "An apartment, technically. And you two are now the only people who know about it other than her and Makoto."
    m "Wow. And I thought my cube-shaped watermelon was a good present."
    m "So...what then? You’re just going to lure two girls you’re not particularly close with to a secret apartment and keep them there until the world breaks?"
    s "Up until last night, I would have said that scenario sounds more plausible than the two of us kissing. And yet..."

    scene mayanebench26
    with dissolve

    m "{i}Please{/i} stop bringing that up..."
    ay "What are we going to do about Ami? If all three of us leave her alone, she might explode. In fact, she might be exploding right now and none of us would even know."
    m "I’ll think of something for Ami..."
    m "For now, we need to focus on getting the other two girls on board. "
    m "I’m not sure how many nights we have left, so it’s important we figure this out as soon as possible or we’ll run the risk of their minds getting wiped along with their...potential recognition of the loops."
    s "I’d contact one of them right now, but my phone’s dead."

    scene mayanebench27
    with dissolve

    ay "Here. Take this one."
    s "I’m not going to just take your phone, Ayane. Even if it {i}is{/i} a backup and you have ten more of them in your dorm room."
    ay "It’s not just a “backup.” It’s an identical, up-to-date copy of your phone. Complete with all of your contacts and a suggestive picture of our class representative with a vibrator in her mouth."
    ay "Why {i}that{/i} is your background and not me, I don’t know. And I don’t {i}want{/i} to know. "
    s "Well, speak for yourself because {i}I{/i} would like to know why you have an identical copy of my phone including but not limited to my contacts and Makoto wallpaper."
    ay "Sometimes, I get bored and send myself text messages from fake-you while waiting for real-you to text me instead."
    s "Ayane-"
    ay "I have a problem. I know. But at least that problem is love and not drugs."
    m "Uhh..."
    s "..."
    ay "Oh, and in case you were wondering, I don’t have any of your text or call records. Apparently, having those copied as well would have been an invasion of privacy and is against the law."
    s "I think my privacy has already been invaded, but thanks. I’ll be taking that now."

    scene mayanebench28
    with dissolve

    ay "Happy to help! And don’t worry about giving it back. I have three more at home."
    s "That’s...great."
    m "Well...good luck, I guess? You’re very likely going to need it."
    ay "Be in touch after you hear back from Yumi and Tsuneyo. Like Maya said, the sooner we can get them on board, the better."
    ay "Also, maybe...don’t look at any of the messages that phone has sent to my number. I’ve been going kind of crazy these past few months in more ways than I’d like to admit."
    s "I’ll do my best, Ayane..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene mayanebench29
    with dissolve2

    "I get a safe distance away from Maya and Ayane before unlocking my “new” phone with, you guessed it, the same exact passcode I use for my {i}real{/i} phone before making sure all of my contacts are there."
    "Worryingly, they are. And while I’m extremely concerned as to how Ayane got her hands on my data in the first place, I don’t really have time for that right now."
    "If the next reset really is as close as Maya says, I need to act quickly. "
    "So, without a clear idea in mind about {i}what{/i} I’m going to say when I call...I scroll through a list of names and wind up landing on-"

    $ renpy.end_replay()
    $ slumberreset2 = True

    menu slumberphonemenu:
        "Yumi" if yumislumber3 == False:
            jump yumislumber1
        "Tsuneyo" if tsuneyoslumber3  == False:
            jump tsuneyoslumber1
...
```