# Burden to Bear (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [She Is](./dormwartwo6.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwartwo7
* Group: Main
* Triggered by label: dormwartwo6
* Chain sources: dormwartwo6
* Chain sources path: dormwartwo6

## Official wiki page

[Burden to Bear](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo7&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label dormwartwo7:
    scene comedywar1
    with dissolve2
    play music "lifeismostlygood.mp3"

    mo "Thanks again for tuning in to our live coverage of the second annual Super Mega Ultimate Dorm Wars: Halloween Version!"
    mo "I’m your host, Molly MacCormack, and joining me right now is none other than everyone’s favorite Pokemon trainer and queen of questionable doujinshi...Misty!"

    scene comedywar2
    with dissolve

    mo "Who...also happens to be wearing Ash’s hat for some reason."
    ki "He left it at my place after a night of passionate lovemaking."
    mo "Aren’t they canonically 10?"
    ki "When has that ever stopped literally anyone?"
    mo "That is a fair point and one that I relate to more than I would like to admit. "

    scene comedywar1
    with dissolve

    mo "However! Right now is not the time to discuss our taboo habits and hobbies! But it {i}is{/i} time to discuss what sort of thing Kirin’s roommate, Noriko Nakayama, and our beloved teacher are up to!"

    scene comedywar3
    with dissolve

    mo "Kirin, with Noriko’s lead in the official polls {i}still{/i} on the rise, what do you have to say about how their date might be going right now? Any ideas or insight on how things are playing out?"
    ki "Well, hopefully, they’re fucking."

    scene comedywar4
    with dissolve

    mo "Uhh...any...{i}other{/i} ideas or insight?"
    ki "Sure. I can elaborate if that’s what you want."
    mo "That’s not what I-"
    ki "Hopefully, Noriko sidelined whatever sappy, emotional plans she put together for tonight and is currently riding our teacher’s dick like it’s Kingda Ka. "
    ki "Because, let’s face it folks- she kind of needs it at this point, doesn’t she? "
    ki "All this “will they, won’t they” bullshit is getting really tiring and if I have to hear her vent about it one more time, I'm going to knock her unconscious and let Sensei have his way with her while she’s asleep."

    scene comedywar5
    with dissolve

    ki "Oh. Shit. Whoops. Probably shouldn’t have said that in front of you, huh? Not trying to poke at a sore spot or anything."

    scene comedywar6
    with dissolve

    mo "What...exactly do you mean by-"
    ki "Listen, all that matters about tonight’s date with Noriko and Sensei is that she gets railed so hard that she has no further desire to talk about it with me."
    ki "So long as that happens, everyone will be happy and we can finally start preparing for Threesome-Thursdays."
    mo "Threesome...Thursdays?"

    scene comedywar7
    with dissolve

    ki "You’re invited too, of course. I’ve always fantasized about going down on a white girl."
    mo "..."

    scene comedywar8
    with dissolve

    mo "Oh, look! The man of the hour has returned! Let’s check in with him to see how everything went!"
    ima "Senpai! It’s about time you showed up!"

    scene black
    with dissolve2

    "I make my way into the cafe for the stand-up comedy thing and immediately steal the attention of roughly half of the room."
    "It’s not exactly {i}good{/i} attention, though, as the vast majority of it is jealous glares and pointed glances that scream “Why couldn’t it be me?”"
    "But at least I can count on Imani to not bother me about it."

    scene comedywar9
    with dissolve2

    ima "So, did you get it wet?"
    s "..."
    ima "How come you never take me on any dates? I like being pampered too, you know."
    s "I didn’t exactly do any “pampering” when today was all about the girls pleasing {i}me.{/i}"
    ima "Ahh. So you {i}did{/i} get it wet. "
    ima "Noriko back at home “recharging” right now? Because I did notice Futaba moving a little slower than usual and I can only imagine what that must mean."
    s "Hey, how about we talk about something else? That sounds fun."
    ima "You’ve gotta at least tell me who won. I’m still your co-judge at the end of the day, even if I didn’t get to tag along and watch you rail our students."
    s "Is that something you’d be interested in?"
    ima "My mind and the rational part of me says no, but my heart is telling me yes."

    scene comedywar10
    with dissolve

    ima "Ooh, maybe if I just sat in the corner with one of my eyes like this? I could play both sides that way, don’t you think?"
    s "..."
    ima "..."

    scene comedywar9
    with dissolve

    ima "You’re boring tonight."
    s "And you’re as “fun” as ever. "
    s "But when it comes to who won..."

    menu seconddatechoice:
        "Futaba":
            s "I think...I have to give it to Futaba."

            scene comedywar11
            with dissolve

            $ dorm1war2points += 1
            $ datewarfutaba = True

            ima "Oh yeah? I guess polls really are just polls then, huh?"
            ima "Why Futaba? Any particular reason?"
            s "It was just...closer to an ideal “date” for me, I think."
            s "The time I had with Noriko was really...special, for lack of a better term- but I’m not exactly sure if I’d call it fun."
            s "Or if...I even had a {i}good{/i} time to begin with. It was just...a lot."
            s "But with Futaba, there was this clear desire to make sure I had a good time. And nearly everything we did was all about me."
            ima "I see, I see. Futaba wins because all you care about is yourself. Got it."
            s "It’s not just that. It was clear she was sharing a piece of her past with me as well. Or...showing me a side of herself that no one else is allowed to see or...something like that."

            scene comedywar12
            with dissolve

            ima "Well...I’m happy for ya, chief."
            ima "I’ll be the one to break the news to Noriko, but we should probably let her rest for now. "
            ima "I know {i}I{/i} wouldn’t be happy if some dude used me up the way you used her and then tossed me aside for somebody else."
            s "That’s not what-"
            ima "Blah, blah, blah. We’re getting ready to start soon, so go do your “mingling” thing while I do what I do best and handle all of the clerical work."

        "Noriko":
            s "I think...I have to give it to Noriko."

            $ dorm2war2points += 1
            $ datewarnoriko = True

            scene comedywar11
            with dissolve

            ima "Yeah. I had a feeling things were going to end up that way."
            s "You did?"
            ima "Well, considering the first encounter I ever had with you involved that poor girl spilling her heart out in the middle of the hallway, I guess I’ve just got...some idea of the relationship you two have."
            ima "And I don’t just mean that in a creepy way that equates to me enabling you to bang a teenage girl without risk of both persecution and prosecution."
            ima "I mean I know she’s special to you."

            s "To tell the truth...I think Futaba’s “date” was better overall. It was a lot more suited to my tastes and...it was clear that she put a load of thought into exactly what would make me happy."
            s "Noriko just...went above and beyond that, I guess."
            ima "Yeah. She does that sometimes."
            ima "I’ll be the one to break the news to Futaba, but it’ll probably happen tomorrow since she seems to be having a good time tonight and I wouldn’t want to ruin that."
            s "Thanks, Imani. "
            ima "No prob, Senpai. We’re in this together, remember?"
            ima "Now, you go do your thing and mingle or whatever while I do what I do best and handle all of the clerical stuff."

    s "I can’t imagine there’s that much clerical work involved with the Dorm Wars."
    ima "You’d be surprised. "

    scene black
    with dissolve

    ima "I’ll catch up with you later, though! Enjoy the show, Senpai!"
    s "I’ll...do my best."

    "........."
    "......"
    "..."

    scene comedywar13
    with dissolve2

    s "Hey, I didn’t realize you were coming to-"
    maki "Shh. This hasn’t happened since she was six and I will not let you take this from me."
    maki "Also, I hope you’re a sub- because you’re about to get {i}mommed{/i} tonight."
    s "I see what you did there."
    mi "Like...how’d your dates go or whatevs, Teach? You guys vibe?"

    scene comedywar14
    with dissolve

    maki "Ah! You were vibing without me?"
    s "I don’t think she means that kind of vibe, Maki."
    maki "You underestimate my knowledge of the vibe, good sir."
    s "This one is intangible."

    scene comedywar15
    with dissolve

    maki "An intangible vibe?...That’s either the most...amazing or...terrifying thing I have ever heard of. My interest is piqued."
    s "The “vibes” were good, Miku."
    mi "Bet. "
    s "On...what?"

    scene comedywar16
    with dissolve

    mi "Ohmygod, you’re like...so out of touch with reality. It’s hilarious. "
    s "Yeah, well...you’re weird when you’re like this. "
    mi "Ratio."
    maki "Who on earth taught you this language? Because it sure as Hell wasn’t me."

    scene comedywar17
    with fade

    i "Why am I here? What benefit does my presence provide you? I don’t even like comedy. Or pastries. Or...mahogany. It’s too annoying to work with."
    u "Your presence is like a soft breeze on a summer day...a solitary rain drop in the midst of a drought. "
    i "Listen, Uta- I don’t know much about kunoichi, but I’m pretty sure they didn’t communicate entirely through metaphors."

    scene comedywar18
    with dissolve

    u "To be sure of anything is to submit. Remain vigilant. Question all things. For it is only then that you will truly reach enlightenment."
    i "Now you just sound like a monk."
    u "Perhaps I am. Perhaps we are {i}all{/i} monks- for monks are one with the world and its spiritual energies and we are but conduits when viewed through the eyes of an eagle."
    i "{i}What?{/i}"

    scene comedywar17
    with dissolve

    u "Your presence is a necessary evil. For if the need to communicate with my peers arises, I can not rely on the shadows alone. I need someone who can touch them with her bare hands."
    i "Oh. So you just need a translator and no one else knows you well enough to understand your ninjaspeak. "
    u "Hai."
    i "Fine. But you’re going to owe me a favor if I actually have to apply those skills at any point."
    u "Your wish is my command."

    scene comedywar19
    with fade

    c "Hey! Welcome back! How’d your dates go?"
    s "They went well. Though, choosing a winner was a lot harder than I would have liked it to be."
    sa "I’m sure you...made the right choice...Sensei..."
    sa "As long as...that choice...was Futaba..."

    scene comedywar20
    with dissolve

    s "Wow. That’s...not the sort of answer I would have expected out of you, Sana. Especially considering the other competitor was one of your club-mates."
    c "Our floor comes before our club tonight, Sensei. If us first floor girls are going to win this war, we need to unite whenever we can. And if that means exiling our friends, so be it."
    s "You want to weigh in on this, Otoha? Or are you just going to keep staring at me?"

    scene comedywar21
    with dissolve

    o "I don’t know. I’m having a harder time than usual figuring out what I’m supposed to say to you right now."
    s "What? Why?"
    o "Does it matter? I’m just some random teenage girl. Who cares what I think?"
    c "Why are you acting so weird? All Sensei did was try to involve you in the conversation."
    s "Did I do something to offend you? Because we’ve barely even talked lately and I’m not really sure where this hostility is coming from."
    o "Hostility? Is not throwing myself at you the same thing as “hostility” now?"

    scene comedywar22
    with dissolve

    c "Otoha, what the fuck is your problem? Stop being such a bitch. Sensei obviously wasn’t expecting you to {i}throw{/i} yourself at him. "
    o "How should I know that when he’s been running around with our classmates all day?"
    c "Just because he’s in a little fake date contest with a couple of the girls in class doesn’t mean he’s {i}fucking{/i} them."

    scene comedywar23
    with dissolve

    sa "Wh...What’s that, Ayane? You...suddenly need my help with something?...Okay...be right there..."
    o "And if he is?"
    c "Then that’s {i}his{/i} choice. And you don’t need to go getting yourself involved with-"
    s "I’ve got this, Chika."
    c "No. If she’s going to sit there insulting you, I-"
    s "I said I’ve got this."

    scene comedywar24
    with dissolve

    c "Tch. Whatever."
    s "Do you want to talk, Otoha?"
    o "Not really."
    s "Are you mad at me?"
    o "I don’t know."
    s "Should I leave you alone?"
    o "I..."
    o "Probably."

    scene black
    with dissolve

    s "Okay. Then, I guess I’ll see you later."
    c "Wha- Sensei! What part of that was “I got this?!” You just let her win!"
    s "No, I’d be letting her win if I spent any amount of time dwelling on whatever she’s pissed off about right now. No point in starting a fight over something I don’t even understand."
    c "But-"
    s "Just leave it alone. Whatever it is will resolve itself on its own."
    o "..."

    scene comedywar25
    with dissolve2

    h "What was that about?"
    s "I didn’t realize you were listening. "
    h "I just happened to be looking in that general direction for some reason."
    s "Is it because of Chika’s costume?"
    h "Whaaaat? Noooooo. That’s crazy talk. I was just making sure...everyone’s drinks are full. "
    sar "Haru-chan, I don’t understand this “POS system” nonsense. Back in my day, we just memorized the  numbers and took people’s money. "

    scene comedywar26
    with dissolve

    h "Sara, you’re 33. It {i}is{/i} your day. "
    sar "Take that back. I’m still 18 at heart. "
    h "I guess that explains the costume."
    sar "Just because you’re a Z-cup and can pull off sultry, promiscuous witch costumes doesn’t mean that we all have to-"
    s "Ahem."

    scene comedywar27
    with dissolve

    sar "Oh, hello there! Welcome to Koi Cafe? What can I get you, Sir? Coffee? Tea? {i}Me?{/i}"
    s "Coffee, please."

    scene comedywar28
    with dissolve

    sar "Yes, Sir. Coming right up."
    h "Listen, uhh...I don’t want to be a downer, but I’d probably try staying away from Otoha and Rin for a little while. It seems like the two of them are dealing with some...animosity or something and..."
    h "I don’t want that to get even worse and wind up ruining their weekend."
    s "Look at you, being all responsible and motherly despite having one of the healthiest and unblemished uteruses around."

    scene comedywar29
    with dissolve

    h "Uhh..."
    h "What?"
    s "I have no idea why I said that. I’m so sorry. "
    h "Who even..."
    h "{i}What?{/i}"
    sar "I have a healthy uterus too, you know. "

    scene black
    with dissolve

    s "Okay. I’m going to leave now. "
    h "{i}What the fuck was that?{/i}"

    scene comedywar30
    with dissolve

    s "Hi. Please hit me if I say anything about female reproductive organs."
    ka "..."
    to "..."
    ka "Sorry, can you try that greeting one more time? My brain must have malfunctioned from seeing you on such short notice and made me hear something about...uhh...{i}stuff.{/i}"
    to "How strange. It appears my brain had the same malfunction. Perhaps we should check the building for gas leaks before continuing to spend time here?"
    s "What I meant to say is hello and that I don’t often see you two together. In fact, I don’t think I’ve {i}ever{/i} seen you two together. "

    scene comedywar31
    with dissolve

    to "We met briefly at last year’s Christmas party, but it wasn’t until just a short while ago that Karin-senpai and I finally spoke on our own."
    to "I approached her as I recognized her costume from a video game I convinced my mother to purchase for my sister and me recently. And I must say, she wears it quite well."
    ka "Not as well as...uhh...whatever you’re supposed to be..."

    scene comedywar32
    with dissolve

    to "Hasshaku-sama, of course! Though, I suppose I cannot fault you for not recognizing the costume without the hat."
    to "I seem to have underestimated just how large it would be and have been repeatedly bumping into things all day long."
    ka "You have...a very interesting combination of hobbies, Touka..."

    scene comedywar33
    with dissolve

    to "Thank you very much, Karin-senpai! My mother always says that versatility is what makes a woman stand out in her field! And as the heir to my family’s fortune, I-"
    ka "J...Just Karin is fine, you know? You don’t have to keep adding “Senpai” to it. "

    scene comedywar34
    with dissolve

    to "But I respect you and it would feel wrong dropping such an important honorific for the only senpai I’ve ever met. "
    ka "I mean...I guess if it makes you happy..."
    s "Sorry, but do you two remember I’m here? Or would you like me to go somewhere else so you can keep falling in love without having to worry about being interrupted?"

    scene comedywar35
    with dissolve

    ka "Love?! What is love?! Baby don’t hurt me! No more!"
    to "My, you’re just as exceptional at ruining the moment as ever. "
    to "Can’t two beautiful women have mutual respect for one another without a man imagining what it would be like for them to kiss?"
    s "No."
    to "Lies. I have a great deal of respect for my mother and surely you haven’t imagined the two of {i}us{/i} kissing."
    s "I have."

    scene comedywar36
    with dissolve

    to "Ew! Sensei!"
    ka "Haha! Lips are cool but how about we change the conversation topic?! Oh, I know! How does everyone feel about dogs?! Dogs are great, right?!"

    scene comedywar37
    with dissolve

    to "Aww, Karin-senpai! I had no idea you were so bashful in the face of romance! How insanely adorable!"
    s "The fantasies are coming back."

    scene comedywar38
    with dissolve

    to "Hush, you. Please allow me this rare opportunity to attempt socializing with new people. I would like to hear Karin-senpai’s thoughts on what the best breed of dog is."
    ka "Doodles are nice. And soft. I like them."
    ka "Yeah. "
    ka "This is nice. This makes me feel good."
    s "Again, they’re back."
    to "Shoo, you pest. "

    scene black
    with dissolve2

    "I leave Touka and Karin to fall in love in private and continue on with my standard process of evenly distributing my time between everyone at the start of a party. "
    "Or at least I {i}try{/i} to before something terrible happens."

    play sound "static.mp3"
    scene sexyland with flash
    scene sexyland2 with flash
    scene sexyland with flash
    scene comedywar39 with flash
    play sound "dolphinnoise.mp3"

    s "{i}It’s back.{/i}"
    ima "Uhh...hi?"
    ki "Is there some kind of convention going on or something? This is the second giant dolphin I’ve seen today."
    a "Just leave it alone and it won’t hurt you! That’s what me and Maya have been doing and it hasn’t approached us yet!"
    m "Why is it even here to begin with? Is it following us?"

    play sound "static.mp3"
    scene comedywar40
    with flash
    stop sound

    s "Quick. Act normal."
    t "Look at me. I’m an average person. I like reading the newspaper and attending municipal court. Go Yankees."
    ay "Are you excited for the big moment, Sensei? I’ve been practicing my routine all day! Well...when I’m not too busy interviewing the other girls, of course. But {i}most{/i} of the day!"
    t "And I have been doing the laundry. I sure hope my package arrives this week."
    s "That’s enough being normal, Tsuneyo. I don’t think the dolphin is watching us anymore."
    t "That’s good. My knowledge of normal people is extremely limited and I was on the brink of running out of material."
    s "Anyway, I don’t know if {i}excited{/i} is the word to describe how I’m feeling, but I’m definitely looking forward to seeing what you two came up with."
    s "Tsuneyo’s been training for this moment her entire life and Ayane..."
    s "Well, I assume you’re still looking for that extra {i}reward{/i} if you win?"

    scene comedywar41
    with dissolve

    ay "Oh...Uhh...Yeah..."
    t "Extra reward?"
    ay "It’s nothing! Just a...you know. A thing."
    t "I, too, would like an additional reward if I win. Though, I will likely lose. So perhaps the false promise of said hypothetical reward will be enough for me."
    s "Sure, Tsuneyo. You can have a bonus reward if you win as well."

    scene comedywar42
    with dissolve

    t "No thank you. I do not want it."
    s "But-"
    t "I’m sorry, but my mind has already been made up."
    ay "I...uhh..."
    ay "I think we’re going to be starting soon, so...I’m going to go prepare. I just wanted to talk to you before I went up there and..."
    ay "Tell you that I love you...and stuff..."

    scene comedywar43
    with dissolve

    t "I also love you."
    ay "Uhh...Tsuneyo?"
    t "More than anything in the entire world."
    ay "..."
    s "Uh..."
    t "I have been keeping it a secret this entire time as I did not want to upset anyone. But the burden has become too great to bear and I can no longer keep these feelings inside of me."
    t "I am sorry you had to find out like this."
    ay "..."
    s "..."
    t "..."
    ay "..."
    s "..."
    t "..."
    t "What?"
    s "I think we’re just waiting for the part where you come out and say that was a joke."
    t "Comedy is all about timing. You could be waiting forever."
    ay "I feel...weirdly intimidated all of a sudden..."
    ay "What if she’s serious? What if Tsuneyo actually loves you?"
    t "I do. I can’t live without this man. And, as far as I’m concerned, I didn’t even {i}begin{/i} to live until I met him."
    s "Okay, yeah. This is just a joke."
    t "It’s not. I love you."
    s "Stop saying that. It’s weird."

    scene comedywar44
    with dissolve

    t "Why do you not see me the same way you see the other girls?"
    t "Have I done something wrong?"
    t "Were all of those nights I spent fucking you a mistake?"
    ay "Ahh...yes...those were the days..."
    t "Do you love me as well?"
    s "No. "

    scene comedywar45
    with dissolve

    t "Good. Because I was just joking."
    t "This concludes the first segment of Tsuneyo Tojo’s stand-up routine."
    t "{i}Unless...{/i}"

    scene black
    with dissolve2

    "Haruka dims the lights and all of the girls who were scattered around the cafe just moments ago scramble to their respective tables."
    "Not seeing any other open seats, I begin to make my way over to the table Molly and Yasu are sitting at as Imani takes the stage and announces the opening of the competition..."
    "........."
    "......"
    "..."

    scene comedywar46
    with dissolve

    ima "Alright, alright, alright! Who’s ready to hear some jokes?!"
    a "Woo! Let’s go Ay- guys, come on! How come I’m the only one who ever claps for stuff like this?!"

    scene comedywar47
    with dissolve

    ima "Thank you, Ami! You’re the first and probably last person who will ever clap for me while I’m standing on a stage completely clothed!"
    ima "But that’s enough about my questionable history as the top-earning stripper in Bolivia! What we’re {i}really{/i} here to listen to are mediocre jokes from two first-timers that will probably be extremely awkward!"
    ima "But that’s fine! Because if there’s anything {i}I{/i} know about first times, it’s that they’re {i}always{/i} extremely awkward! {i}Especially{/i} when they happen in the back of an ice cream truck."
    f "Are these jokes or...does Imani just have a really weird background story?"
    no "I have no idea, but I suddenly have a new idea for a smut novel."

    scene comedywar48
    with dissolve

    ima "Taking the stage first...the most {i}delectable{/i} chocolate bunny I’ve ever seen- and please don’t tell the cops I said that...it’s Tsuneyo Tojo!"

    scene black
    with dissolve2

    "The crowd (Not just Ami) erupts into an actual sea of applause this time as Tsuneyo makes her way over to the stage."
    "Will this be as horrible as I expect it to be? "
    "Probably."
    "But at least it’s happening in front of a crowd of her peers instead of a group of strangers."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ dormwartwo7 = True

    jump dormwartwo8

label dormwartwo8:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
"But, no matter how hard I try, I can not remove my eyes from Noriko."
    "She’s claimed them as her own and would be clutching them in the palms of her hands if they were not so busy enabling her seemingly endless serenade."
    "Make it stop."
    "Make these feelings go away."
    "I don’t want them anymore."
    "I don’t want them anymore. "
    "I don’t-"

    scene datewarnoriko23
    with dissolve
    stop music fadeout 2.0

    s "..."
    n "..."

    "Noriko abruptly stops playing and, in doing so, frees me from the tendrils budding out of all of the things I don’t yet understand about myself."
    "I’m the same as her."
    "Still growing. Figuring out who I am."
    "But why?"
    "I’m in my thirties. I should know this by now."
    "Why is she moving so much faster than me? Why can she do things like this while I can’t even-"

    n "Sorry, everyone. I forget the rest."

    "An awkward combination of boos and half-hushed claps joins the fray...but Noriko remains on the stage."
    "Looking down at me after spending all of her life looking up."

    n "What do you think, Sensei?"
    s "..."
    n "Am I impressive?"

    scene black
    with dissolve2

    "She is."
    "........."
    "......"
    "..."

    scene datewarnoriko24
    with dissolve2
    play music "wewereangels.mp3"

    n "Heheh...heh..."
    n "I felt really confident when I was standing up there, but...now that I’m in front of you again, I-"
    s "You were amazing."

    scene datewarnoriko25
    with dissolve

    n "I...was?"
    s "You were. "
    s "I don’t think the crowd was very pleased with how abruptly you ended the song, though."

    scene datewarnoriko26
    with dissolve

    n "Well...yeah. There was more, but...it seemed like you were starting to feel a little uncomfortable. Which is definitely my fault for putting you in such a weird position with zero warning and-"
    s "I was uncomfortable, yeah."

    scene datewarnoriko27
    with dissolve

    s "It was a lot to just spring on me out of nowhere and I had no idea how I was supposed to react or...how many people had their eyes on me."
    n "Sensei...I didn’t mean to-"
    s "But it was amazing."

    scene datewarnoriko28
    with dissolve2

    s "{i}You{/i} were amazing."
    n "Sensei..."
    s "And I’ll be patiently waiting to see what you’ll be like when you exit the prototype stage."

    scene black
    with dissolve2
    stop music fadeout 15.0

    s "Because something tells me that you’ll be even {i}more{/i} amazing than you are right now."

    "Sometime after that, we leave the venue together."
    "I can’t remember if we held hands again or not."
    "But I remember the moment Noriko left so she could head back to the hotel a little earlier than the rest of the girls."
    "And I remember the way her sister’s billboard-eyes followed me as I hung my head on the way down the street, pondering which pink-haired girl I’d be happier with."

    s "..."

    "Or if I’ll ever be happy at all."

    $ renpy.end_replay()
    $ dormwartwo6 = True
    $ noriko_love += 5

    "{i}Noriko’s affection has increased to [noriko_love]!{/i}"
    "........."
    "......"
    "..."
    "{i}Shortly after that...{/i}"

    jump dormwartwo7
...
```