# Life is Changing (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Normal-ish](./chapthree7.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Yasu: Down The Rabbit Hole](./church15.md)
* [Yasu: Sore Thumb](./yasuspecial15.md)

## Event properties

* Id: chapthree8
* Group: Main
* Triggered by label: chapthree7
* Chain sources: chapthree7
* Chain sources path: chapthree7

## Official wiki page

[Life is Changing](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=chapthree8&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label chapthree8:
    play sound "slidedoor.mp3"
    scene clubtime1
    with dissolve2
    play music "10c.mp3"

    mo "Hah..."
    s "What’s up with you?"
    mo "Oh...nothing, Sir. Just thinking about how unfair life is and how everything I know is crumbling down around me."
    s "I feel like that’s...pretty much half of what being a teenager is."
    mo "Is the other half impending doom and overwhelming exhaustion?"
    s "No. The other half is figuring out the best possible times to masturbate and working your entire schedule around them."

    scene clubtime2
    with dissolve

    mo "That seems like a lot of self-pleasure, Sir. I don’t think any of us have the time for that level of frequency. And this is coming from someone who is very likely in the higher tier for that sort of thing."
    s "I’m glad to see that we’ve finally found something we have in common."
    s "Whatever’s wrong right now won’t last forever, though. So the best thing you can do is just move past it before it eats away at the half of you that isn’t busy dodging debris from the world crumbling."

    scene clubtime3
    with dissolve

    mo "Tis the plan, Sir. And unless you plan on abandoning me again, I’m sure that the brunt of the onslaught has subsided and that things will go back to normal for me shortly."
    mo "Or at least as normal as they can be for someone with every class level-capped and a stack of doujinshi under her bed."
    s "I have no idea what that means."
    mo "It means that I will be forever alone, Sir."
    s "Well, I’m sure it doesn’t help considering my inconsistent track record, but you’ve got me."

    scene clubtime4
    with dissolve

    mo "It helps. Even if you don’t ever understand what I’m talking about...or show any interest in any of the things I like...and get very easily annoyed whenever I talk too much...and-"

    scene clubtime5
    with dissolve

    mo "Wait..."
    mo "Isn’t that the shirt I made for you?..."
    s "..."
    mo "You’re...actually wearing it?"
    s "It was about time for a change."
    s "Plus, it was very hot this morning and this shirt is surprisingly breathable."

    scene clubtime6
    with dissolve

    mo "I see."
    s "..."
    mo "..."
    mo "I have bad news, Sir."

    scene clubtime7
    with dissolve

    s "Oh?"
    mo "Effective roughly ten minutes ago, the manga club lost one of its most dedicated and seasoned members."
    s "Haven’t you all been in the club for the same amount of time? How exactly does one become more seasoned than the others?"
    mo "Attendance, Sir. Rin seldom missed a meeting."
    s "Ah. So it was her. "
    s "I guess that makes sense. I heard Otoha talking about some music club or something and figured Rin might wind up joining that instead."
    s "This isn’t really bad news for {i}me,{/i} though. It just kind of sucks for you and...whoever else wanted her to stick around."

    scene clubtime8
    with dissolve

    mo "Of course this is bad news for you as well, Sir. You are just as involved with the manga club as I am."
    s "Why? Because my niece is in it?"
    mo "Because you are the club advisor."
    s "..."
    mo "..."
    s "I’m the what?"
    mo "The club advisor, Sir. The one responsible for...well, advising us. "
    mo "And while it’s true that I have never seen you at one of the meetings...and that none of us have ever really needed your assistance, you are still one of us."
    s "I will never be one of you."
    mo "I’m afraid it’s too late for that, Sir."
    s "Even if I {i}am{/i} one of you, which I am not, how is this bad news for me? It’s not like I’m going to miss her or anything since I was never around to begin with."
    mo "It’s bad news for you because, if we’re unable to get one more member by the end of the day, the club won’t meet the cutoff required and you’ll wind up getting stuck as the advisor for another club."
    mo "And while that may not sound {i}that{/i} bad for you considering this is an all-girls school and you are a modern day pied piper for adolescents, {i}our{/i} club is the one that cosplays."
    s "You’re right. This is a problem."

    scene clubtime9
    with dissolve

    mo "So you’ll help me locate a fifth member?!"
    s "No. But I will try and find a room to clear out in my house so you’ll still have the time and space required to make outfits. "

    scene clubtime10
    with dissolve

    mo "Oh."
    mo "Well, I suppose we are doomed then."

    scene clubtime11
    with fade

    ima "Okay ladies...and I guess Senpai since he’s also technically employed here!"
    s "I am literally your boss. I think."
    s "I’m not really sure how student teachers-"
    ima "Shush! I’m talking to the girls right now."
    ima "If you don’t have a penis, let this be your warning that as soon as the bell rings, you need to head over to your new club for a mandatory day-one meeting. "
    ay "And what about if you {i}do{/i} have a penis?"
    ima "You’re lucky! Any other questions?"
    ki "Will you be advising any clubs? Because if not, you should drop by the archery range and-"
    ima "Miss Watabe has made me promise to not come within a hundred feet of the archery range because she is afraid she’ll “accidentally” shoot me."
    no "Miss Watabe is the archery club advisor?! Why didn’t anyone tell me about this?!"

    scene clubtime12
    with dissolve

    ima "Because you’re way too horny and she’s already spoken for! Any {i}other{/i} questions? We should have time for one more."
    c "Where did you get your bow?"

    scene clubtime13
    with dissolve

    ima "Les Vêtements!"
    c "I knew it! You should come by again! We’ve got-"
    ima "Kumon-mi High student handbook! Page 13! Section B! No advertising in class!"
    mak "Actually, Miss Imai, Chika’s allusion to a part time job would take priority over the aforementioned advertisement rule as it’s a much greater offense and-"

    scene clubtime14
    with dissolve

    ima "Imani Imai’s personal self-made handbook! Page 1! Section A! If your name is Makoto, shut up!"
    mak "Hah..."

    play sound "bell.mp3"
    scene clubtime15
    with dissolve

    ima "Alright, girls! Class is dismissed! Now go do the thing or we’re all going to be sacrificed to whoever Yasu’s god is!"
    ya "Praise be!"
    ima "Praise be, indeed! Whatever that means!"

    scene black
    with dissolve2

    "One by one, the girls filter out of the classroom, leaving behind nothing but a few scattered personal belongings and the idea that, slowly but surely, life is changing."

    scene clubtime16
    with dissolve2

    "It might not be in an exciting way. In fact, it might not be much of a change at all for someone like me who, if you take away the constant restarting of the world and all of the taboo sex, lives a pretty normal life."
    "But for a certain someone who still, one day later, clings to the walls of my mind..."
    "Well, I bet it’s exciting for her."
    "Or terrifying."
    "Or she’s too busy trying to figure out what’s going to happen next to even be bothered with something as trivial as club reorganization."
    "But the fact of the matter is-"
    "And I say this with whatever pieces of humanity I have both gained and lost over the last 48 hours-"
    "I hope she enjoys it."
    "I hope we all enjoy it."
    "And I know that we won’t."
    "But I hope that we do."

    ima "Senpaiiiiiiiiiiiii..."
    s "What?"
    ima "My girls are leaving the nest! I’m never going to see them again!"
    s "You’re going to see them tomorrow."
    ima "Tomorrow is Saturday and I’m going out drinking!"
    s "Then...you’re going to see them on Monday."

    scene clubtime17
    with dissolve

    ima "Yeah. I guess that’s true."
    ima "Hey, do you have any idea how the whole...club advisor thingy works? Because they told me I had to sign up to be one, but all that was left when I went to do it was light music and swimming. "
    ima "Which means you’re probably going to get stuck with music since I chose the latter."
    s "I’m...actually the advisor for a club already."

    scene clubtime18
    with dissolve

    ima "What? Really? Which one?"
    s "..."
    ima "..."
    ima "Holy shit."
    ima "You’re a closet otaku, aren’t you? I knew something was up. "
    s "I’m not...but that does happen to be the club I’m apparently in charge of."
    s "In terms of knowing how it works, though...I have absolutely no idea. So just ask Wakana when you go get drunk and have a lesbian threesome or whatever."
    ima "Do you think they’ll invite me? I don’t have as much threesome experience as you. I might disappoint them."
    s "Please clue me in if they do. "
    ima "Roger that, Senpai. Your wish is my command."

    scene clubtime19
    with dissolve

    ima "Guess I should probably head out, though. It’ll be hard getting everybody to like me if I bail on the very first club meeting."
    ima "Plus, one of the girls on the team is mad busty and needs a new swimsuit, so I’ve gotta track that down and whatnot so her boobs don’t pop or something. "
    s "That’s...not possible, Imani."
    ima "If it is, ain’t like I’ve gotta worry about it. B-life forever, yo."

    scene clubtime20
    with dissolve

    s "Maybe I’ll drop by later and...make sure you’re doing everything correctly."
    s "That totally isn’t just an excuse I’m making up to see you in a swimsuit, though. This is a purely professional decision I am making as your superior."
    ima "Oh. I..."
    ima "Yeah, I’m not really planning on doing any swimming or anything. Not really into that sort of thing."
    s "You chose a weird club to sign up for, then."
    ima "..."
    s "..."
    s "Wait, how come I’m the one who needs to erase this? I didn’t even write it."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene clubtime21
    with dissolve2

    m "Wait, how come I’m the one who needs to erase this? I didn’t even write it."
    f "It was Rin this time...she wanted to leave you a parting gift since she won’t be coming back to the club room any time soon..."
    f "I tried to stop her, but...I thought it was kind of sweet in a way."
    m "There is nothing sweet about calling someone a nerd, Futaba. Especially someone who is most definitely not a nerd. Me."
    f "R...Right..."
    mo "I’ve got a bad feeling about this, Ami. I couldn’t convince Tsuneyo to join us and we’re only an hour or two away from the end of the day."
    a "That’s fine...we’ll make it."
    a "I talked to Ayane and Sana and...they’re basically kind of members already. So we just need one of them to become an {i}actual{/i} member and..."
    a "And..."
    a "We’ll definitely be okay."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene clubtime22
    with dissolve2

    n "..."
    o "..."
    r "..."
    r "Are you..."
    r "Are you sure about this?"

    scene clubtime23
    with fade

    sa "I..."
    sa "I want to be cool like you guys!"
    n "GAAAAAAH YES. She’s so cute. Can we keep her, Mom? Can we?"
    o "What? Why are you looking at me? I’m not your mom."
    r "You’ve got mom energy, though. But like, hot mom. Not normal mom. You know?"
    o "Sana...is this really what you want? Do you even know how to play any instruments?"

    scene clubtime24
    with dissolve

    sa "Well, I...um...I’ve never...really...even {i}had{/i} an instrument, but..."
    sa "I...listen to a lot of music and...and I’ve always wanted to try playing the drums."
    n "Hey, that’s great! We still need a drummer, right? And it’s not like we’ve got any shows lined up. "
    r "Yeah! We’ve got plenty of time to teach Sana how to play! You can play drums, right Otoha?"
    o "Yeah, but...I don’t know if I’m good enough to really {i}teach{/i} anyone. "

    scene clubtime25
    with dissolve

    sa "I..."
    sa "I’ll do my best! I promise!"
    n "Mom, pleeeeeeeeeeease?"
    o "Dude, stop. I’m not your mom. I’m not even the club president."
    r "Wait, you’re not?"
    n "Yeah, what? Who else is going to be president? I kind of figured it would be you."
    o "Can you guys just let me feel normal for a minute and not like some sort of...motherly presidential prodigy? I’ve barely even had time to-"

    play sound "slidedoor.mp3"
    scene clubtime26
    with dissolve

    c "Ya-ho! "
    r "Ah..."
    n "Chika? What are you doing here?"

    scene clubtime27
    with dissolve

    c "Joining the light music club. "
    c "None of the other clubs really interested me. So when I sat down and tried to narrow down the list...this was kind of the only thing on it."
    c "Plus, I’ve always wanted to hear Rin play guitar, and now she’ll {i}have{/i} to play for me."

    scene clubtime28
    with fade

    c "I’m like, an okay singer. And the only experience I have with instruments is the recorder from when they made us play in grade school."
    c "So unless you’re looking for a mediocre recorder player or a singer who’s like, maybe a third as good as Otoha, I can probably just sit out and watch or something."
    c "I’m more of a listener than a player anyway."
    o "Uhh..."
    n "Hmm..."
    n "Well...we do need five people to make this an official club. And with Sana joining, we’re already at four."
    c "What?! Sana! You joined the light music club! That’s so cool! What do you play?"
    sa "M-Me?! Umm...uhh...n...nothing yet..."
    r "..."

    scene clubtime29
    with dissolve

    o "Listen, uhh..."
    o "I...don’t really think we need somebody to just...watch us. So unless you wanted to try picking up an instrument or something-"
    c "Wait! What if...and hear me out here..."
    c "What if I became your manager?"
    o "Our manager? But we’re not even a band yet. There’s not anything to manage."
    r "..."
    n "..."
    c "Yeah, but like...aren’t you super talented, Otoha? And Noriko, your sister is literally my queen. Between you two and Rin, who’s already my friend, where else would I even go?"
    c "I’m sure I can contribute something. I just want a chance to-"

    scene clubtime30
    with dissolve

    r "Yeah!"
    o "Rin?..."
    r "Yeah! Let’s do it!"
    r "The four of us can form a band and Chika can be the manager!"
    c "Aaaah, Rin! Thank you so much! I promise I won’t let you down!"
    sa "I...um...I won’t...let anyone down either!"

    scene clubtime31
    with dissolve

    o "Rin...I don’t really know if this is a good idea..."
    r "Otoha, it’s fine! We need a fifth member, right? And with a manager, we can focus on playing and leave all of that other stuff to her! This is great!"
    o "Yeah, I...I get the logistics of it...It’s just...you know..."
    r "Know what? What’s wrong?"
    o "Know that..."
    o "That..."

    scene clubtime32
    with dissolve

    o "Ugh...Nevermind."
    r "Otoha?"
    o "It’s fine."
    o "I’m probably just worrying too much."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene clubtime33
    with dissolve2

    w "Listen up, worms..."
    w "You will obey my rules at all times. "
    w "You will only speak when spoken {i}to.{/i}"
    w "But most importantly, you will treat both me...and {i}each other...{/i}with respect."
    w "Do I make myself clear?"

    scene clubtime34
    with fade

    eei "Understood!"
    w "Ichimonji, is there a problem?"
    i "There are many problems. None of them really pertain to kyudo, though. So you can keep doing your thing and I’ll keep pretending to care."
    w "You’re free to leave whenever you want."
    w "In fact, I implore you to do so if you intend to remain as sarcastic and confrontational as that."

    scene clubtime35
    with fade

    u "Io, come on! It’s the first meeting. Just go along with it today and stop coming afterward if you don’t like it."
    i "Me being here {i}is{/i} me going along with it. I didn’t realize I was going to have to agree to signing my soul and free will away in the process."
    ki "Chill, Greenie. It’s just a formality."

    scene clubtime36
    with dissolve

    i "Why do you always think it’s okay to talk to me? Let alone give me stupid nicknames like “Greenie.”"
    ki "Why do you think it’s okay to be a colossal bitch to the kyudo instructor when all you had to do was say one fucking word?"
    ki "You realize you’re just making problems for yourself, right? And that it’s not the world that’s just against you for no reason whatsoever?"
    i "I do. And yet, nothing changes."
    i "Wow, what a mystery."
    u "Sorry, Kirin...Io’s just in a bad mood today."
    ki "Io needs to get fucking laid."

    scene clubtime37
    with dissolve

    i "{i}Do you kiss your mother with that mouth?{/i}"
    ki "Nope. Just the guy you like."

    scene clubtime38
    with dissolve

    i "You fucking-"
    u "Wait. What? Who? Who are we talking about right now? What’s going on?"

    scene clubtime39
    with fade

    to "Isn’t this just wonderful, Tsuneyo?"
    to "Kyudo is not only a majestic and alluring sport, but a fantastic piece of Japanese culture. Don’t you agree?"
    t "Sure."
    to "Did you know that my manor has its own, one-of-a-kind, professionally designed kyudojo? My father had it commissioned when I was just a little girl. It’s absolutely spectacular."
    t "My father taught me how to strangle chickens."
    to "Oh!"
    to "Oh, okay!"
    t "Some days, if I close my eyes, I can still hear them scream."
    to "..."
    t "..."

    scene clubtime40
    with dissolve

    to "Isn’t kyudo just wonderful?"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene clubtime41
    with dissolve2

    ima "Okay, everybody! Welcome to swim club! I’m your host, Imani Imai, and joining me today is the team captain, Karin Kanda!"
    ka "Um...thank you, Miss Imai."
    ima "Karin here is sporting a brand new school swimsuit that I personally handed to her just ten minutes ago!"
    ima "Did you know that they had to have it custom made because she’s the size of an adult woman despite being only-"

    scene clubtime42
    with dissolve

    ka "Hi, everyone! I’m Karin! This is a normal swimsuit! It wasn’t custom made at all! I’m only a little bit taller and...more endowed than the other girls in my grade!"
    ka "Okay, who’s ready to swim?! That’s what we do here! Swim! Yeah!"
    ka "Water!"

    scene clubtime43
    with fade

    mi "How come Karin’s actin’ so nervous? There ain’t even any boys around and it’s not like she doesn’t have experience with this kinda thing after all that time as the co-captain of the soccer team."
    mak "I’m glad to see you’re not as torn up over that as you were yesterday, Miku."
    mi "Oh, I ain’t happy. I’m mad as Hell and I’m not gonna take it anymore."
    mi "But at least I’ve got you two."
    mi "And I guess swimmin’ ain’t all that bad."
    mi "It’s kinda like...playin’ soccer in the water. Just there’s no ball or goal or teammates and all ya do is flail your limbs around and hope ya don’t drown."
    mak "Yup. Exactly like soccer, Miku."
    no "Oh dear."
    no "This is far more dangerous than I led myself to believe."
    ay "We’re swimming today...right, Miss Imai? You didn’t just make us put these uniforms on so you could take pictures of us and show them to Sensei?"
    ka "P...Pictures?! Show?! Sensei?! Us?!"
    ima "It appears I left my cell phone in the locker room! How unfortunate that you must all now be subjected to two hours worth of fun because of my mistake!"
    ka "Umm...uhh..."
    ka "{i}Miss Imai, who is the girl that’s just...staring at me like that?{/i}"
    ima "Oh, that’s Nodoka. She’s a super genius who habitually undresses everyone with her eyes but doesn’t have the balls to actually make a move on anyone."

    scene clubtime44
    with dissolve

    no "Perhaps I’m just waiting for someone to make a move on {i}me?{/i} Have you ever thought about that, Imani?"
    ima "Not really, no!"
    ay "Your day will come, Nodoka. Don’t worry."

    scene clubtime45
    with dissolve

    no "Oh, I’m not worried at all."
    no "I’ve amassed plenty of opportunities to exchange my virginity for semi-regretful memories over the last several months. I’m just carefully deciding which ones would be the most fun to regret."
    no "Right now, the most ideal scenario would be for each one of you to take turns sitting on my face. I am ready whenever you are, Ayane."
    ay "I’m good, but thank you for offering!"

    scene clubtime46
    with fade

    y "Hey, uhh..."
    y "This is where the...swim club thing meets, right?"
    mak "Yumi?..."
    mak "Are you...actually joining the club?"

    scene clubtime47
    with dissolve

    y "Looks that way, four eyes."
    mak "Well, fall into line and pretend to be prepared, I guess."
    mak "I’m glad you’re finally participating in something, but if you showed up on time you would have realized that you were supposed to wear-"

    scene clubtime48
    with fade

    y "Yeah, yeah, yeah. I’m late and unprepared. Story of my life."
    y "Just be happy I’m actually doin’ this shit by choice and that nobody forced me this time."
    no "..."
    y "..."

    scene clubtime49
    with dissolve

    y "The fuck are you gonna do?"
    no "Me?"
    no "{i}I{/i} am going to wait."
    y "Wait for what, Einstein? For me to look away so you can try to sucker punch me with those fuckin’ noodle arms?"
    no "You’ll know when it’s time."
    y "Oooh, intimidating."

    scene clubtime50
    with dissolve

    ima "You’re going to have to show up on time from now on, Yumi."
    ima "If somebody else was in charge of this club, I wouldn’t bat an eye. But there are a lot of expectations on me as a student teacher, and the fact that I’m even {i}allowed{/i} to advise a club is-"
    y "Got it, yeah. I don’t need your background story. I’ll show up on time from now on."
    y "Only reason I was late is cause I was lookin’ for my school swimsuit, but I ain’t ever used it before so...yeah. No fuckin’ clue where it is."

    scene clubtime51
    with dissolve

    ima "Oh. Well...okay. Yeah, that works."
    ima "Just come with me and we’ll find one in your size, I guess. Karin and the others can just start without you. All we were going to do was hang out and get to know each other today anyway."
    y "I’ll get in the water and shit, but...I ain’t really good at that whole “Gettin’ to know each other” BS."
    ima "Well...you’ve gotta start somewhere. But it’ll be hard to start anything dressed like that, so..."
    ima "Let’s see what we can find for you."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene clubtime52
    with dissolve2

    mo "We are doomed. This is the end of the manga club."
    mo "I’m sorry it had to end like this. But if we are to blame someone, I suggest we scapegoat Nithhala and her quest to become a normie."
    a "I could have sworn at least {i}somebody{/i} was going to show up."
    f "How much time is left until we have to submit the club roster?"
    m "We could always just read in one of the dorm rooms. It’s not like we {i}need{/i} this club room or anything."
    m "In fact, to be honest, I’d {i}prefer{/i} we move somewhere else. Specifically somewhere without a dry erase board that the three of you will use to write untrue things about me."

    play sound "slidedoor.mp3"
    scene clubtime53
    with dissolve

    mo "The door! It’s opening! Someone is here!"
    mo "Someone is..."
    mo "Someone is...!"

    scene clubtime54
    with fade

    mo "Someone is...Yasu?"
    ya "Hello..."
    ya "I would like to join your club please."
    m "Sorry. Applications are-"

    scene clubtime55
    with dissolve

    mo "Welcome aboard!"
    m "Oh, god damn it."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene clubtime56
    with dissolve2

    "The day comes to an end and the hateful summer heat reaches me before anyone else."
    "I leave school knowing that all of the girls I would normally leave {i}with{/i} are off experiencing the early stages of new and exciting things without me."
    "Without me."
    "Without me, who is meant to be the center of their lives and affection and the target of all of their desires."
    "But strangely enough, I am okay with that."
    "In this fleeting moment filled with mental gymnastics in which I tell myself I am not burning alive, I accept the prospect of being alone so long as I am alone under my own conditions."
    "What those are is hard to say."
    "But this is just one day of what I feel will be a very long summer."
    "And this is just one tangential slope I must descend on the way back to dismissive complacency."
    "The day comes to an end and the hateful summer heat reaches me before anyone else."

    scene black
    stop music

    "I wonder what the night will bring?"
    "{i}Congratulations!{/i}"
    "{i}You are free once more!{/i}"
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ chapthree8 = True
    $ ayanenosex = True

    jump endofweekday

label yumichikaspecial1:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
mo "But...what?!"
    mo "No! You can’t! You won’t! You love manga!"
    r "I {i}do{/i} love manga, yes."
    r "But there’s always been something else I’ve loved even more."

    scene rinmolly26
    with dissolve

    mo "Damn it, Otoha! Just how much will you steal from me?!"
    r "I, uhh...I was talking about music..."

    scene rinmolly27
    with dissolve

    mo "Are you really leaving?...Can’t you just...play music in your free time?"
    r "I want to play as much as I can whenever I can. And as a fellow otaku, I know you’re the same way with your hobbies."
    r "I’ve finally got an opportunity to play more...to see my girlfriend more...and to hang out with a new group of friends that all share my biggest love with me."
    r "There was no way I was going to turn that down..."
    r "Plus...this might give you and me the space we need to kind of...get back to normal-ish...don’t you think?"

    scene rinmolly28
    with dissolve

    mo "I don’t want you to leave..."
    r "I’m not “leaving.”"
    r "I’m just trying something new."
    r "And hey, if I don’t fit in or I just suck or something, I might come running back."
    r "But seeing as you’re the club president...and my {i}friend...{/i}I needed you to know that."
    r "But hey, with the whole club reassignment thing going on, I’m sure someone just as cool as me will fill my space in no time at all."

    scene rinmolly29
    with dissolve

    mo "Hah...I do hope so. Ami and I have been doing our best trying to recruit new members over the last several days, but even the Kendo Princess seems to be on the fence."
    r "Well, Tsuneyo is {i}way{/i} cooler than me, so maybe you should try aiming a little bit lower?"
    mo "Are you sure this is what you want, Nithhala?"
    r "Are you really going to use my D&D name when it was that exact game that got us into this mess in the first place?"

    scene rinmolly30
    with dissolve

    mo "It was never about that."
    mo "That was just one more example of me trying to keep you from slipping away."
    mo "But I suppose you’ve slipped far enough by now that there’s no way I’ll ever pull you back."

    scene rinmolly31
    with dissolve

    r "You won’t have to pull me {i}at all{/i} for at least one night of every week since I think we’re ready to start the campaign back up now."
    r "But every other night, your girl’s gonna be workin’ on becoming a rock star."
    mo "You’ll always be a rock star to me, Rin."

    scene rinmolly32
    with dissolve

    r "Dude, cringe. You sounded like my mom just now."
    mo "I mean it, though. I’ll always admire you. It doesn’t make much of a difference if it’s from up close or afar."
    mo "Just stay within sixty feet and I’ll always be able to reach you in one turn."
    r "Uhh...sixty feet seems a little close, don’t you think?"
    mo "Enjoy your new club, Rin..."
    mo "I hope it will be one you don’t slip away from."

    scene rinmolly33
    with dissolve

    r "Here’s hoping it won’t be, I guess."
    mo "Aye. Here’s hoping it won’t."
    r "Still homies?"
    mo "Still homies."

    scene rinmolly34
    with dissolve

    mo "Also, have I mentioned how much I love your new uniform yet? Or did the ever growing distance between us prevent my words from reaching you?"
    r "You’re free to admire it all you want. Just don’t try to tackle me this time."

    scene rinmolly35
    with dissolve

    mo "Mm..."
    r "Kidding! Now, let’s head back inside and sign away our respective destinies to yet another year’s worth of club activities and friendships."
    mo "Aye. I hope I don’t accidentally trip and land on top of you along the way..."

    scene black
    with dissolve2
    stop music fadeout 8.0

    "Somehow or another, the sun slipped away."
    "The gaze of a god disappeared along with it."
    "Somehow or another, things turned out okay."
    "And two girls poised to burn somehow remained hidden."

    $ renpy.end_replay()
    $ chapthree7 = True

    "........."
    "......"
    "..."

    jump chapthree8
...
```