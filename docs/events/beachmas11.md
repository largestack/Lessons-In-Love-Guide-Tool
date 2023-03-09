# いないいない。。。ばあ！
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=beachmas11&go=Go)


Part of event chain [Treasured](./beachmas10.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: beachmas11
* Group: Main
* Triggered by label: beachmas10

## Event code
File: \game\chap3.rpy
Code:
```python
...
label beachmas11:
    play sound "static.mp3"
    scene wearethechildren1
    with flash
    stop sound
    play music "sleepsong.mp3"

    "To watch them be restored."

    p1 "Hear ye, hear ye!"
    p1 "In light of recent developments made to both the protagonist of our video game and the world he inhabits, we, the Plant Council, have reconvened for our 98th meeting."
    p1 "The topic of today’s discussion will be the significance of S-"
    p4 "Dude, stop. You can’t say her name in front of him. And Plant #2 still isn’t convinced it's her {i}actual{/i} name and it’ll turn into a whole thing that I really don’t have the time for tonight."
    p2 "Okay, first off, what else could {i}you{/i} possibly be doing tonight?"
    p4 "Your mother. Ayooo."
    p1 "Plant #4, that was inappropriate and I am going to have to ask that you maintain your best behavior during tonight’s meeting."
    p2 "Thank you. Now, to get back to what I was about to say, there is an entire {i}truckload{/i} of contradictory evidence supporting-"
    p4 "It was her NAME PLATE, bro! Come on! "
    p4 "It’s on the grave and everything!"
    p2 "But that doesn’t explain the several {i}other{/i} instances where-"
    p4 "Oh God, here we go again. Or is it {i}god?{/i} I never know which capitalization I’m supposed to use in this game as it fluctuates more than Ami’s personality. Somebody gimme five."
    p1 "We are plants. We can not high five."
    p2 "That really is one of the worst parts of not being a human."
    p1 "Speaking of humans, I’d like to welcome tonight’s very special guest — Yomiel, who has come face to face with Sensei on several occasions now."
    p4 "Sup, Yomiel."
    p2 "That human looks a lot like a rabbit to me."
    p4 "{i}Perception,{/i} bro. Go replay Down the Rabbit Hole and get back to me. There’s a whole thing about it."
    p2 "But then why wasn’t the event called Down the Human Hole?"
    p1 "I’m about to start a petition to remove {i}both{/i} of you if you do not simmer down. Do either one of you want to be the next Plant #3?"
    p4 "No way. I saw what happened to his wife and saplings after he got zapped. I can’t do that to Bethany."
    p2 "Bethany? The one from the phone sex line?"
    p4 "It is a “compassion” hotline. We do other things too."
    p1 "Yomiel, your last appearance was several updates ago, but it is my understanding that both you and your brethren are present more than you are actually seen. Is this true?"
    yom "That would be correct. My family and I have been placed all over this world to both learn and observe. So even if you can not see us, you can assume we are there."
    yom "Like many other things, it is all a matter of perception. And it is quite possible that today, on the second holiest night of the year, that all of {i}you{/i} will see things that are not actually there either."
    p1 "And what is it that makes {i}tonight{/i} the second holiest night of the year when it is widely agreed upon that the true birthday of Jesus Christ is not on December 25th, but sometime in the middle of the year?"
    yom "See, that’s the thing, though. The relevancy of Jesus Christ in the landscape of this world is not as strong as it is in others."
    yom "We have different gods here. Ones that are a lot more complicated and finicky than some brown dude who wandered the desert, gently fellating his apostles before licking their feet."
    p4 "Speaking of brown people, I’d like to lick Imani’s feet if you know what I’m saying."
    p2 "Imani is {i}black.{/i} Tsuneyo is the brown one."
    p4 "That’s actually a hotly contested topic but, let’s be real, I’d lick both of them."
    p2 "Amen."
    p1 "Please don’t say “amen” in front of Yomiel. It is religiously insensitive."
    yom "It’s fine. I’ve been falling out of favor with my designated god lately anyway and have been thinking of migrating closer to the center. "
    p1 "Could you elaborate on that? What makes the position of the other gods any different from yours?"
    yom "It really comes down to subtlety at the end of the day. "
    yom "It just rubs me the wrong way hearing, “TAKE SOMETHING THAT ISN’T YOURS” instead of just silently taking things without really making a big show out of it."
    yom "I see the appeal in both sides. Which is precisely why I was so excited to come here and talk to {i}you{/i} guys about it since I know you’re all unbiased."
    p4 "Except for Plant #2 who still thinks Ami’s mom’s name isn’t Sekai."

    play sound "static.mp3"
    scene wearethechildren2
    with flash
    stop sound

    p4 "Ahh, fuck. Sorry guys."
    p1 "Great job, Plant #4. Now he’s upside down."
    p2 "Or is it {i}we{/i} who are upside down?"
    yom "I see what you did there."
    p1 "While it is certainly unfortunate that {i}something{/i} is upside down right now, I can forgive Plant #4 for his transgression tonight as she {i}was{/i} meant to be the topic of discussion after all."
    p4 "Finally, some background info. Only had to wait three fucking years."
    p2 "Hey, we’ve got some bits and pieces in the past. Like the part about her being a popular poet. Or the part about how she wanted to bone kids."
    p4 "Oh, speaking of that, did you see that thing in the Discord where Selebus said one of the main girls is a shotacon? Which one do you think it is?"
    p2 "I think I’m leaning toward Nodoka. "
    p4 "Nodoka would fuck anything. She doesn’t count."
    p1 "{i}Ahem.{/i}"
    p4 "Sorry, boss. Please proceed."
    p1 "So, we all know that Sekai-"
    p2 "SIL."
    p1 "Hah...we all know that {i}Ami’s mother{/i}-"
    p2 "If it {i}is{/i} her mother."
    p4 "This fucking guy."
    p1 "...we all know that the red-haired woman from Sensei’s past can’t remain hidden forever. And the nature of this sudden vacation so far has made it seem like she may be closer than we believe."
    p1 "Yomiel, as a current (yet wavering) member of the Church of New Hope, is there anything you can tell us about the woman who may or may not be named Sekai?"
    yom "No. "
    p1 "Nothing at all?"
    yom "Nope. "
    p4 "I told you we should have gotten Wormwood. Nobody remembers this guy. He’s a dreg."
    yom "Hey, I didn’t have to come here. There’s a big party in the forest tonight and sometimes Yasu forgets that we have vision and spreads her legs in a way that lets us see up her skirt."
    p2 "Don’t stick your dick in crazy, man."
    p4 "Always stick your dick in crazy, man. I’m rooting for you."
    yom "Unfortunately, I am a being without genitalia and thus can not participate in coital activities. But that doesn’t stop the fantasies."
    p1 "Well, seeing as Yomiel has nothing to say on tonight’s topic, I guess there’s not much left for us to go off of."
    p2 "Looks like we’ll have to just keep wondering when the next dreaded SIL appearance is going to be."
    p4 "Yeah, because there’s {i}no way{/i} Sekai’s going to show up tonight or anything. "
    p2 "Is she?"
    yom "Oh no..."
    p4 "Bro, what do you think the narrator was talking about when they mentioned something being {i}restored?{/i}"
    p2 "Dude, I don’t know. It’s impossible to know what the narrator is talking about literally ever. Or who that narrator even {i}is{/i} since there are, like...a bunch of them."
    p1 "Well, I guess we’ll have to just wait and see. "
    p1 "This concludes the 98th meeting of 23rd District’s Plant Council. Thank you to Plant #2, Plant #4, and Yomiel, the human rabbit."
    yom "We need to leave."
    p1 "What?"
    yom "We need to leave right now."
    p2 "Um..."
    yom "She is {i}coming.{/i}"
    p4 "I’ll have Plant #2’s {i}mom{/i} cumming by the end of the-"

    play sound "static.mp3"
    scene wearethechildren3 with flash
    stop sound

    "Covered in char-broiled lizards, I watch as the funny plants do a funny dance and put an end to their funny show. "
    "I wasn’t able to hear anything they were saying this time as my ability to converse with those who are not human normally only applies to animals."
    "The lizards move as somewhere beneath their crispy skin, they can still think and feel. But the batter is far too thick and too delicious for their cordless vocal muscles to penetrate."
    "I hear nothing. Not even the sound of the squares behind me. "
    "I wonder how long it’s been? "
    "I wonder how long the show has gone on for?"
    "I wonder when the upside down trees will kiss the rightside up grass and rejoin to form a ground worth walking on?"
    "I wonder when anyone will come to understand my metaphors?"
    "There is only one person who ever could."
    "But she is gone now."
    "And she’s never coming back."

    play sound "static.mp3"
    scene wearethechildren4 with flash
    stop sound

    se "How can you be so sure of that in a world where nothing is permanent?"
    se "If the world itself is made for you, what’s stopping it from making {i}me?{/i}"

    "She’s gone and she’s never coming back."

    play sound "static.mp3"
    scene wearethechildren5 with flash
    stop sound

    se "Only if you give up."
    se "You’re not a {i}quitter,{/i} are you?"
    se "After all we’ve been through, you want to just leave me on my own?"
    se "What did I do to deserve that?"
    se "I loved you, you know? And you can deny it all you want, but you loved me too."
    se "You {i}still{/i} love me."
    se "You emit a certain scent when you’re aroused. It’s my favorite scent in the world."
    se "Go on."
    se "Show me how {i}big{/i} it’s gotten."
    se "Hurt me more than I can hurt myself."

    "{b}SHE IS GONE AND SHE IS NEVER COMING BACK.{/b}"

    play sound "static.mp3"
    scene wearethechildren6 with flash
    stop sound

    se "Do you think I’m a bad person? That I ever wanted to hurt you?"
    se "Because it was {i}you{/i} I loved the most until {i}she{/i} came."
    se "Why can’t I be with you two?"
    se "It’s cold beneath the surface. I want to feel your warmth."
    se "I want those long arms wrapped around me."
    se "I want my flesh stuck to yours. I want our sweat on the bedsheets and your tears on my tongue."
    se "Taste me and make me yours a millionth time."

    play sound "static.mp3"
    scene ayhh15 with flash
    scene satisfactionguaranteed with flash
    scene ayhh5 with flash
    scene satisfactionguaranteed with flash
    scene ayhh15 with flash
    scene satisfactionguaranteed with flash
    scene ayhh5 with flash
    scene satisfactionguaranteed with flash
    scene wearethechildren7 with flash
    stop sound
    $ renpy.pause(3, hard=True)
    play sound "static.mp3"
    scene wearethechildren8 with flash
    stop sound

    q "Come! Take it!"

    play sound "static.mp3"
    scene wearethechildren9
    with flash
    stop sound

    se "Doesn’t it feel nostalgic being in a place like this?"
    se "Where no one can see us for miles and miles and miles..."
    se "Think of everything we can do."
    se "How quiet it all is."
    se "A place where no one can judge us."
    se "Where we are free to be ourselves."
    se "Where there’s no pain or consequence or {i}anything.{/i}"
    se "It’s just us."
    se "It’s what we’ve always wanted."
    se "A place where we can be ourselves."
    se "We can laugh and smile and fuck and sing and waste away our days beneath our favorite trees!"
    se "This is the life that we were made for. Not the one {i}out there.{/i}"
    se "Bring me back."

    "{b}{s}SHE IS NEVER COMING BACK.{/s} I CAN’T BREATHE IN HERE.{/b}"

    play sound "static.mp3"
    scene wearethechildren10 with flash
    stop sound

    se "Hey."
    se "How about we play a game?"
    se "It’s one we played when you were little."
    se "One your mother used to play with you."
    se "The way you’d smile every time you saw me...it always made my heart skip a beat."
    se "I wonder when it was that it started skipping more than one at once?"

    "she is never coming back she is never coming back she is never coming back she is never coming back she is never coming back she is never coming back she is never coming back she is never coming back she is never coming back she
    is never coming back she is never coming back she is never coming back she is never coming back she is never coming back she is never coming back"

    play sound "static.mp3"
    scene wearethechildren11 with flash
    stop sound

    se "いない。。。いない。。。"

    play sound "static.mp3"
    scene wearethechildren12 with flash
    stop sound

    se "ばあ！"

    "Stop."

    play sound "static.mp3"
    scene wearethechildren11 with flash
    stop sound

    se "いない。。。いない。。。"

    play sound "static.mp3"
    scene wearethechildren12 with flash
    stop sound

    se "ばああああ！"

    "STOP."

    play sound "static.mp3"
    scene wearethechildren11 with flash
    stop sound

    se "いない。。。いない。。。"

    "{size=+40}{b}STOP PLAYING WITH ME{/b}{/size}"

    se "..."
    s "..."
    se "..."
    s "..."

    play sound "static.mp3"
    scene wearethechildren13 with flash
    stop sound
    stop music

    se "ばあ！"
    s "Ah..."
    se "..."

    scene wearethechildren14
    with dissolve2

    se "Hm..."
    se "It’s like you haven’t grown a day."

    scene colorbars
    play sound "broken.mp3"
    $ renpy.pause(10, hard=True)
    scene black
    stop sound
    $ renpy.pause(7, hard=True)

    q "........sei?"
    s "..."
    q ".............sei?............up.........."
    s "..."
    q "Sensei. Wake up."

    scene wearethechildren15
    with dissolve4
    play music "goodmorning.mp3"

    mak "Good morning, sleepyhead. Would you mind explaining why you’re passed out a full three miles away from the inn?"
    s "Makoto?...Futaba?...What’s going on?"
    f "We were going for a walk and noticed someone sleeping up here, so we wanted to go make sure they were okay, but...we didn’t think it’d be you."
    mak "What happened? It’s not like you to willingly walk away from a room full of teenage girls."
    s "I think I was...looking for Yumi or...right- Futaba, Rin wants you to know she’s sorry and that you should come back to the inn."

    scene wearethechildren16
    with dissolve

    f "I know...I already talked to her."
    s "When? How long have I been asleep?"
    mak "Well, we have no idea when you went out, but it’s about 1:00 AM right now."
    s "Then what are {i}you two{/i} doing three miles away from the inn? You should be asleep."
    s "Wait, let me guess. You’re heading the search party for me."
    mak "No, actually. Nobody went out to look for you. In fact, nobody even remembers you exist except for Futaba and me."

    scene wearethechildren17
    with dissolve

    f "It’s true. They all seem to believe that Imani has been their teacher all year. And Ami won’t stop bragging about how fun it is to live alone."
    s "Okay. I was concerned for half a second, but now I know that you’re fucking with me."
    mak "Do you need help getting up? Can you stand?"

    scene black
    with dissolve2

    "I angle myself upward and dust a mixture of sand and dirt off of my blazer before crossing my legs and thanking the two of them for waking me up."
    "I...have no idea how I made it all the way over here or...why my head suddenly hurts so much..."
    "But I’m glad that I was discovered before dawn since I doubt anyone would believe literally any explanation I would have come up with for this."

    scene wearethechildren18
    with dissolve2

    mak "It’s a good thing we found you when we did. Because there’s no way anyone would have believed literally any explanation you would have come up with for this."
    s "Yes, Makoto. I am well aware."
    f "Even I’m having a hard time believing it and I’m here."
    f "It’s one thing to wander off and do your own thing, but...we’re a long way from the inn."
    mak "He must have come to get away from everyone. That’s why we’re here, after all."
    s "Mutual hatred for snoring? Who is the culprit?"
    f "It’s nothing like that."
    s "What is it then? What common ground do the two of you share that was strong enough to force you three miles down the beach in the middle of the night? Because if it’s something as boring as reading, I-"
    mak "We were having a long, serious discussion about how crazy it is that you’ve been having sex with {i}both{/i} of us. Isn’t that fun?"
    s "..."

    scene wearethechildren19
    with dissolve

    f "Makoto..."
    mak "What? I want to see what he has to say about it."
    s "Well, at least I understand why you came all the way over here to talk about that. Not really a great topic to get caught discussing."
    mak "We’re not doing it for our safety, we’re doing it for yours."

    scene wearethechildren20
    with dissolve

    f "We’ve both known...there are “others” for a long time. But it wasn’t until Halloween that we figured out {i}each other{/i} were among those people."
    mak "Ever since then, we’ve been talking more and airing out our grievances about how fruitless the pursuit of your heart is and how, even knowing that, we can’t keep ourselves away."
    mak "It’s actually rather pathetic, but...it is what it is."
    s "I’m not really sure what I’m supposed to say during a time like this. Normally, when I’m confronted, it’s by one person- not two."
    mak "How calming it is knowing that this is a regular thing for you."
    s "I didn’t mean it like that."
    f "Then...how did you mean it, Sensei? Because it seems like Makoto and I believed we were fulfilling the same role as one another in your life and-"

    scene wearethechildren21
    with fade

    s "You two don’t have specific {i}roles.{/i} You’re attractive girls who like me that I can have sex with whenever I want. Of course I’m going to take advantage of that."
    mak "You really do have a way with words, Sensei."
    f "That...That’s not {i}all{/i} we are, though...is it?"
    s "There’s obviously more to it than that. But if you’re going to be blunt enough to confront me about this directly, I’m going to be respectful enough to tell it like it is instead of beating around the bush."

    scene wearethechildren22
    with fade

    f "This...isn’t really how I expected this conversation would go..."
    mak "This is {i}exactly{/i} how I expected this conversation would go."
    s "Listen, I care about both of you...in ways that transcend the time we spend behind closed doors. But I don’t have some end-all, be-all excuse or explanation for why things are the way they are. They just {i}are.{/i}"
    s "If that makes you want to stop what we’re doing, fine. I don’t blame you. I know that nothing good can last forever."
    s "But I also know there’s never been a point in either one of the relationships I’ve had with you two where some brand of exclusivity was guaranteed or even {i}expected.{/i} Am I right?"

    scene wearethechildren23
    with dissolve

    f "Yeah...of course I’m-"
    s "And don’t “Of course I’m not enough” me when your self-confidence is finally starting to take a turn in the right direction."
    mak "I’ve just accepted that-"
    s "Don’t you go self-deprecating either, Makoto."
    s "I get that you’re going through a tough time, but if you keep blaming your shitty mental state on the same one thing for the rest of your life, you’re going to wind up like me."

    scene wearethechildren24
    with dissolve

    f "How did this turn into {i}us{/i} being lectured?"
    mak "Because Sensei’s a master manipulator and finds it easier to just make things about {i}other{/i} people instead of ever trying to fix the parts of {i}himself{/i} that are broken."

    scene wearethechildren21
    with fade

    s "Why does anything need fixing in the first place?"
    s "Why can’t we just accept that things don’t need to be in perfect shape in order for us to use them on a daily basis?"
    f "You’re sleeping with us...{i}because{/i} we’re imperfect?"
    s "That is definitely not what I was going for, but...sure."
    s "Futaba, I told you a long time ago that I’d never be able to accept your feelings until you started thinking better of yourself."
    s "And Makoto, I’ve made {i}several{/i} pledges to treat you better after directly acknowledging just how much I’ve taken advantage of you."
    mak "Right, and...when is that going to start, exactly? Because things don’t seem very different right now, Sensei."
    s "They {i}are{/i} though."
    s "I hide from everything. It’s what I do. But I’m owning up and trying to explain myself right now."
    s "My apologies if my explanation isn’t {i}perfect{/i} but it’s kind of hard to justify my stance as an adult male simultaneously screwing two high school girls who are supposed to be able to depend on me."

    scene wearethechildren25
    with fade

    mak "That’s just the thing, though. We {i}do{/i} still depend on you. That’s why we’re finding solace in one another instead of spilling your secrets out to the entire class."
    f "Makoto’s right. We trust you, Sensei. Just...not when it comes to...monogamous relationships."
    mak "It’s quite possible that’s one more side effect of your manipulation tactics and that we’re simply just too codependent at this point to function {i}without{/i} a change in the details of our relationship..."
    mak "But I digress."
    s "That didn’t sound like much of a digression to me."
    f "I think...what Makoto is trying to say is that...it’s okay. We’re not mad."
    f "We’re just a little...confused because we want to understand you better."

    scene wearethechildren26
    with dissolve

    mak "That’s not entirely true. I’m mad. But growing up in a household where probably over one hundred people have had sex has made me rather jaded and I am now monogamy’s biggest fan. Sorry, Mom."
    f "But...you do want to understand Sensei a little more, right?"
    mak "That part is right, yes."

    if makoto_lust >= 49 and futaba_lust >= 49:
        scene wearethechildren27
        with fade

        s "But why?"
        s "I strung you along...used you for my own benefit...lied to you...manipulated you..."
        s "I did everything wrong..."
        s "You’re not supposed to like me. It’s supposed to be the other way around..."
        mak "Is that what you want? To be abhorred? To be condemned?"
        f "I...I obviously don’t like the...idea of sharing you, but...but if that’s the price I have to pay for the way you make me feel...I can handle that."
        mak "I’m not sure if I can. But at this point, who the fuck even cares? I’ve already been through the worst. I’m pretty sure I can handle whatever comes next."
        s "I don’t get it..."
        s "I don’t get any of you."
        s "Why do you keep coming back to me?"
        s "Why did you wake me up?"
        f "Because you woke {i}us{/i} up."

        scene wearethechildren28
        with dissolve

        s "..."
        f "From how boring life used to be..."
        f "From how hopeless it all felt..."
        mak "And all it took was your last shred of your dignity and a few carefully-tailored words fit for us and us alone."
        f "We need you just as much as you need us."
        s "You’re wrong..."
        s "I don’t need you at all."
        s "You don’t need {i}me{/i} at all."
        mak "Don’t tell us what we do and don’t need when you’ve been wrong time and time again."
        f "That’s right. Let us follow you in our own way..."
        mak "Because the two of us are smart enough to step back if we ever think we might be wrong..."
        s "..."
        f "..."
        mak "..."

        "53 48 45 20 49 53 20 4e 45 56 45 52 20 43 4f 4d 49 4e 47 20 42 41 43 4b"

        se " いない。。。いない。。。"

        play sound "static.mp3"
        scene ayhh15 with flash
        scene imissyoumore
        scene ayhh5 with flash
        scene wearethechildren29 with flash
        stop sound

        se "ばああああああああああああ!"
        mak "Wha- Sensei?!"

        play sound "static.mp3"
        scene wearethechildren30 with flash
        stop sound

        mak "What’s going on?! What’s happening?!"
        f "S-Sensei! Do...Should we call an ambulance?!"
        mak "Hey! Snap out of-"

        play sound "static.mp3"
        scene wearethechildren31 with flash
        stop sound

        a1 "{s}sssssssssssssssssssssssssssss!{/s}"
        a2 "{s}kkkkkkkkkkkkkkkkkkkkkkkkkk!{/s}"
        a1 "Will it count?! Will it stick?! Our holiday trick?!"
        a2 "Will they cry?! Will they scream?! Will they bite off his dick?!"

        scene black
        with dissolve2

        a1 "The things that he is owed! We’ll capture them ourselves!"
        a2 "Shrink them down to our size and mount them on his shelves!"
        a1 "Rejoice! Reclaim the rightful blood!"
        a2 "From Hell in summer time!"
        a1 "We’ve finally done something good!"
        a2 "And also learned to rhyme!"
        a1 "{s}ssssssssssssssssssssss!{/s}"
        a2 "{s}kkkkkkkkkkkkkkkkkkkk!{/s}"

        $ renpy.end_replay()
        $ beachmas11 = True

        jump makotofutabafuntimelustevent

    else:
        scene wearethechildren21
        with fade

        s "But why?"
        s "I strung you along...used you for my own benefit...lied to you...manipulated you..."
        s "I did everything wrong..."
        s "You’re not supposed to like me. It’s supposed to be the other way around..."
        mak "Is that what you want? To be abhorred? To be condemned?"
        f "I...I obviously don’t like the...idea of sharing you, but...but if that’s the price I have to pay for the way you make me feel...I can handle that."
        mak "I’m not sure if I can. But at this point, who the fuck even cares? I’ve already been through the worst. I’m pretty sure I can handle whatever comes next."
        s "I don’t get it..."
        s "I don’t get any of you."
        s "Why do you keep coming back to me?"
        s "Why did you wake me up?"

        scene black
        with dissolve2

        f "Because you woke {i}us{/i} up...and it’s only fair if we do the same for you."
        s "..."
        f "..."
        mak "..."
        s "Just go back to sleep..."

        "I escape the firm, wet grasp of evil hands and return to the inn with two girls by my side."
        "They escape something else."
        "No one hears or sees us come in."
        "And I sleep facing down in a bed that smells of cherry blossoms."

        stop music

        "I don’t deserve their love."

        $ renpy.end_replay()
        $ beachmas11 = True
        $ makotofutabalustskip = True

        "{b}DAY END.{/b}"
        "........."
        "......"
        "..."

        $ totaldays += 1
        $ day = 2
        hide monday onlayer date
        show tuesday onlayer date

        jump beachmas12

label beachmas12:
...
```

## Code that triggers this event
File: \game\chap3.rpy
Code:
```python
...
scene twogirlsonabed22
    with dissolve

    c "It’s not up to her or {i}anyone{/i} else to ever tell you what you should and shouldn’t feel. "
    r "That’s what I’ve been saying the whole time! But nope! Fuck Rin! She liked Chika {i}once{/i} so she obviously still likes her now! People never move on! That’s impossible!"
    c "You can’t help what you feel and she can’t help what she feels either. The only options are learning to deal with it or moving on."
    r "But I don’t want to move on and she doesn’t want to learn! So what are we supposed to do now?!"

    scene twogirlsonabed23
    with dissolve

    c "Just cry and hold my hand. The pain will hurt a little less if you have someone to share it with. And I can take it."
    r "I know you can...you’re amazing...you’ve always been amazing...and that’s why you can be happy and mature and know how to function as one half of a couple and all I can do is complain and cry."
    c "I’m not always happy and I’m not always mature. I’m just lucky enough to have someone who’s able to put up with that."
    c "And if Otoha can’t be that person for you, {i}I{/i} will."

    scene twogirlsonabed24
    with dissolve

    r "But we’re not {i}together.{/i} It’s not {i}you{/i} I think of the second I wake up anymore. It’s {i}her.{/i} "
    r "It’s not you who comes to mind when I see an old couple happily eating together through the window of a family restaurant, it’s {i}her.{/i}"
    r "When {i}she{/i} sees things like that...does she think of me at all?..."
    r "Or does she just keep walking?"
    r "How can she ignore me so easily, Chika? How doesn’t it eat away at her? "
    r "What do you do when Sensei won’t look at you? How do you catch his eye?"
    r "Apart from being really hot, I mean. But there’s gotta be more to it than that."

    scene twogirlsonabed25
    with dissolve

    c "Pfft...thank you, Rin."
    c "I wish I had better advice to give you, but...getting someone to look my way isn’t really a strong suit of mine."
    c "Sensei was looking at me before I even knew he was. And without even realizing what was happening, I just started looking at him as well."
    c "And yeah...there are times when his eyes wander somewhere else...but all I can do is sit there on the couch and have faith that he’ll come back home. And you know what?...He always {i}does.{/i} "
    c "But that’s not because of anything {i}I’m{/i} doing. It’s because he loves me. And because I love him enough to wait."
    c "So if you love Otoha...and you’re okay with waiting, do it."
    c "But Rin?...I have to say this...and if you want to hate me for it, that’s fine..."
    c "But you can do better. "
    c "You can do {i}so much{/i} better. You {i}deserve{/i} so much better."
    c "You shouldn’t spend every night on the couch...waiting for someone to come home just to have them leave again a week later."
    c "You shouldn’t have to explain yourself every time you have feelings...and you shouldn’t be turned into a villain just because you have so much love to give. "
    c "You should be treasured. The way {i}I{/i} am treasured."

    scene twogirlsonabed26
    with dissolve

    r "Chika...are you...{i}really{/i} sure you’re being treasured? Because-"
    c "Yes...I’m sure. "
    c "I’m sure."
    r "..."
    c "..."

    scene twogirlsonabed27
    with dissolve

    r "Okay..."
    r "Yeah..."
    r "As long as you’re sure..."
    c "..."
    r "..."
    c "Rin, I’m...I’m not sure what your...pre-established limits for touching are...but you can come a little closer if my hand isn’t enough."
    c "I’d be happy to hold you tighter until you manage to calm down."
    r "{i}*Sniff*{/i} You’re crying too, you know..."
    c "{i}*Sniff*{/i} Mhm. Which is why I made the suggestion..."
    r "I don’t know if I’m allowed to have a platonic cuddle buddy...especially one that I masturbated to for years. "
    c "You can masturbate to me whenever you want. I don’t mind."
    r "..."
    c "..."

    scene twogirlsonabed28
    with dissolve

    r "On second thought, it’s probably better if we just lie like this instead."
    c "Yeah...I probably shouldn’t have said that. My bad."
    r "Thanks. Yeah. Just...gonna forget that happened."
    c "..."
    r "..."
    c "You, uhh...want a glass of water or something? I think I need some...fresh air..."
    r "One gallon of ice water, please. And if you could maybe slap me in the face a couple times too, that would be cool. "
    c "Didn’t realize you liked it rough."
    r "Make that two gallons of ice water, please."
    c "Coming right up."

    scene black
    with dissolve2
    stop music fadeout 15.0

    "We have come to associate places like this with tragedy based on prior experience."
    "Patterns, if you will."
    "Remember when we heard about those just a short while ago?"
    "About how hard it is to judge when a pattern is going to break...and precisely what will happen once it {i}does?{/i}"
    "How many other dark places do you link to tragedy? "
    "How long does it take your eyes to adjust when nearly every trace of light has been killed off...like the limbs of animals in objects far too small or tight to support them?"
    "To die in fragments is a beautiful way to go."
    "But do you know what’s even more beautiful?"

    $ renpy.end_replay()
    $ beachmas10 = True

    jump beachmas11
...
```