# First  Day of School
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=thefirstclass&go=Go)


Part of event chain [Am I Awake?](./firstfriday.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: thefirstclass
* Group: Main
* Triggered by label: amiwakesupyeah

## Event code
File: \game\script.rpy
Code:
```python
...
label thefirstclass:
    scene newfirstday1
    with dissolve2
    play music "normalday.mp3" fadein 2.0

    a "Hey, so are you feeling any better today? Or are you just going to teach class with that whole “Where am I?” thing still going on?"
    s "I feel pretty much the same, to be honest. I doubt I'd even know where I'm going without you."

    "I also doubt that I'd be able to remember the names of all ten of my students if it weren't for that book the previous {i}me{/i} kept tucked away."
    "Thankfully, I studied everyone's names and faces long enough last night that I {i}should{/i} be able to handle it."

    scene newfirstday2
    with dissolve

    a "Are you sure you're even going to be {i}able{/i} to teach? If you can't remember where the school is, I doubt you can remember any of your lesson plans and stuff."
    s "Oh, don't worry about that. I've come up with a foolproof new method of teaching that I'm sure everyone is going to be very excited about."
    a "A {i}new{/i} method? But-"
    q "Ami! Sensei! Good morning!"

    scene newfirstday3
    with dissolve

    ay "Wow. You're looking even more handsome than normal, Sensei. Did something change overnight? Or have I just fallen more in love with you for no reason whatsoever?"
    a "Sensei has amnesia...or something. Also, please don't touch my uncle this early in the morning."
    a "Or ever."

    scene newfirstday4
    with dissolve

    ay "Amnesia?"
    s "Or something."
    s "It's complicated."
    ay "So...do you not remember who I am anymore?"
    s "Of course I remember who you are, Ayane."

    "After all, how could I forget one of the faces I spent an ungodly amount of time studying last night in preparation for this exact sort of thing?"

    scene newfirstday5
    with dissolve

    ay "Oh, thank God. Because if you didn't, I would have nothing left to do but kill myself."
    a "Don’t you think that’s a bit of an overreaction, Ayane?"
    ay "Oh, stop it. You know you'd do the same exact thing, Ami. The two of us are comrades in arms. Just, in this case, the arms belong to a man twice our size and twice our age."

    scene newfirstday6
    with dissolve

    ay "So, Sensei...since you have amnesia now, I suppose I should probably remind you about our date this weekend."
    s "We’re going on a date?"

    if bonus == True:
        a "Like heck you are! Dating students is completely against rules! You have to be related to be able to spend time together like that!"
    else:
        a "What?! Oh no you’re not! We have...important financial decisions to make this weekend!"

    ay "Sensei will just adopt me then. Right, Sensei?"
    s "Sure."

    scene newfirstday7
    with dissolve

    a "No! Not sure! Where would she even sleep?!"
    ay "Are you {i}sure{/i} you want an answer to that question, Ami? Because I'm not sure you'd like it."

    scene newfirstday8
    with dissolve

    a "There shouldn't even {i}be{/i} a question because Sensei should know by now that I'm the only person allowed to live with him."
    s "Am I allowed to blame this misstep on amnesia or will that not get me off the hook?"
    a "You can make it up to me by ignoring Ayane until we get to school."

    scene newfirstday9
    with dissolve

    ay "It's fine, Sensei. Just go along with it. I've already gotten used to unrequited love, so ignoring me for another fifteen minutes or so is nothing to me."
    s "I'll make it up to you at our date this weekend."

    scene newfirstday10
    with hpunch

    a "THERE WILL BE NO DATE!"

    scene black
    with dissolve2

    "And so the three of us continued on toward the school as if nothing has changed at all..."
    "As if I'm the same person they walk this route with every day..."
    "Blissfully unaware of the images of them I conjured up in my mind as I pulled the sheets over my head last night and the things I proceeded to do to myself thereafter."
    "But that's fine."
    "Because soon, I'll be confident enough here to fully assume the role I've been given."
    "I'll be confident enough to be who they think I am."
    "And I'll be confident enough to act in stark contrast to that and become who I think they {i}need{/i} me to be and not what they want."
    "In turn, I imagine they will do the same."
    "And I imagine these days where the bright sun shines down on my back will turn into days of melancholy."
    "And then to days of depravity."
    "To days of nothing but the feeling of flesh on flesh and the loneliness that accompanies the moments after aggressive ejaculation."
    "But first and foremost-"

    scene newfirstday11
    with dissolve2

    "I must assimilate."

    ay "Do your best today, Sensei!"
    ay "Come see me after class and I can take you to a janitor's closet where Ami won't be able to see us kiss each other."
    a "Ugh...I don’t even care anymore."

    scene newfirstday12
    with dissolve

    "The two of them disappear into the classroom and I take a moment to gather my thoughts and figure out how I'm going to approach this."
    "Despite already having what I referred to earlier as a {i}foolproof{/i} strategy, I'm still surprisingly nervous."
    "Not because I'll be the center of attention, but because I am worried about how far the flames would spread in the event this backfires."
    "This is still a job, whether I decided to take it seriously or not."
    "It's my window to the new world I've found myself inside of. And it's one with a broken lock."
    "If it closes, I have no idea how hard it will be to open it back up."
    "And so I'll do all I can to keep it propped open at all costs."
    "I don't want to look at life from the outside."
    "Not {i}this{/i} life, at least..."

    s "..."

    "A light tap on my shoulder drags me away from another cynical monologue and back into reality."

    scene newfirstday13
    with dissolve

    mak "Good morning, Sensei! I have all of the handouts ready to go for today’s class."
    mak "I already put them on your desk, so you’re all set. I can hand them out too, if you want. I know how tired you can be in the mornings."
    s "Oh...uhh, thanks."
    mak "Is there anything else I can do for you before class starts? The library is empty right now, so if you need anything printed, now is the time."

    "If I remember correctly, this is..."

    s "Makoto..."

    scene newfirstday14
    with dissolve

    mak "Ahh...Y...Yes?"
    s "Oh, sorry. I was just thinking out loud."
    mak "You were thinking about...my first name? But you've never called me that. I've always just been {i}Miyamura{/i} to you..."

    "Oh...right. I guess it's kind of weird for me to be addressing my students by their first names."
    "I guess it's different with Ami and Ayane since I've known them for a long time, but people like Makoto..."

    s "..."

    "Actually, fuck it. If I'm ever going to get to where I want to be with any of these girls, I'm going to have to start chipping away at the walls around them."
    "The weakest point I can identify at this point in time is as simple as the way I address them."

    s "You don't mind if use your first name from now on, do you? It'll help me out a lot with the way I plan to handle things from now on."

    scene newfirstday15
    with dissolve

    mak "I-I don't mind at all! You can call me whatever you want!"
    mak "But...what do you mean by {i}the way you plan to handle things from now on?{/i}"
    mak "You're not...thinking of changing your teaching strategy months into the school year, are you? Because that sort of change might have a negative impact on-"
    s  "Let's just head inside and you can see for yourself what I intend to do...okay, Makoto?"

    scene newfirstday16
    with dissolve

    mak "Mm! Hearing you call me that is...probably going to take some getting used to. So I sincerely apologize for how moronic I must look right now."
    s "You don't look {i}moronic{/i} at all. In fact, I'd say you're closer to {i}cute{/i} than anything."

    scene newfirstday17
    with dissolve

    mak "You know it's rude to mess with someone so early in the morning, right?"
    mak "But I suppose we shouldn't be talking any more about that right now...not with the rest of the class still waiting for you."

    scene newfirstday16
    with dissolve

    mak "I think I'll...head in first, though...and give my face a little time to return to its normal color."
    mak "Just come on in whenever you're ready, Sensei..."
    mak "We'll all be waiting for you."

    scene black
    with dissolve2

    "Makoto darts into the classroom, narrowly avoiding a collision between her shoulder and the door frame, and I am reminded that {i}some{/i} girls might start opening up a little before others."
    "For what it's worth, she seems pretty head over heels for me already."
    "But, like she said...there's an entire room full of girls waiting."
    "All that's left to do now is win over the rest of them..."

    scene firstclass1
    with dissolve2

    s "Good morning, everyone."
    s "I, uhh...guess I'll start by saying-"
    s "Wait, aren't we missing someone? I'm pretty sure I'm supposed to have ten students."

    scene firstclass2
    with dissolve

    c "Oh, Yumi's not coming today. She said she's staying at home since she doesn't feel good or something and told me to tell you that."

    "Already? I feel like it was less than 24 hours ago that Ami was telling me how some of the girls in class like to skip."
    "At least the first culprit is the girl I was most worried about dealing with, though. So maybe this is some sort of blessing in disguise?"

    s "Well, thanks. Then, as I was saying-"
    c "Wait! Sensei! I have a question."
    s "Oh. Uhh...okay?"
    c "Can I go hang out in the bathroom for the rest of homeroom? One of my favorite idols is appearing on a talk show this morning and I'd be like, {i}super{/i} thankful if I could go watch it."
    s "I guess. Just...don't get caught or something? I'm sure you know how this goes."

    scene firstclass2r
    with dissolve

    c "Awesome! Thank you so much, Sensei! You're like, seriously the best teacher ever!"

    scene firstclass3
    with dissolve

    "Chika quickly shoots out of her chair and dashes into the hallway and my morning has already gotten off to a less than ideal start."
    "But hey, at least I've already begun to curry favor with another one of the girls."

    mak "Umm...Sensei?"

    "And potentially {i}lost{/i} favor with another one in return."

    s "What's up?"

    scene firstclass4
    with dissolve

    mak "Well...forgive me for my directness, but are you sure that letting her leave was a good idea?"
    mak "The last time you did that, she didn't come back until the day was halfway over."
    s "I have a hard time believing that a single talk show will take up half of the day. So I'm going to give Chika the benefit of the doubt this time."

    scene firstclass5
    with dissolve

    mi "Woah, there! When the heck did you two make it to first-name territory? I ain't ever heard you call her Chika before."
    mak "Yes...when, indeed?..."
    s "I'll get to that in a minute. Now, can I please just say what I've been trying to say since I came in here?"
    mak "Are you sure you don't want to...perhaps run it by me first?"
    mak "I haven't been briefed on any sort of announcement yet and...as class representative, I believe I have the right to be."
    s "No. I will not run it by you, Makoto. Because this is less of an announcement and more of just a...thing that's going to be happening from now on."
    mak "But...you are {i}announcing{/i} it, aren't you?"
    s "Makoto, just stop talking for a minute."
    mi "Since when is Sensei on a first name basis with everybody?! This is happenin' way too quick!"

    scene firstclass7
    with dissolve

    ay "Sensei!"

    "Ayane suddenly raises her hand and it quickly becomes apparent to me that I may never be able to actually speak without being interrupted again."

    s "What, Ayane?"
    ay "Since we're already on a first name basis, can you refer to me as either {i}darling, honey,{/i} or {i}hot stuff{/i} from now on?"
    s "Absolutely not."
    ay "Not even if I am already prepared to deal with the types of rumors that are sure to spread if you start calling me those things?"
    ay "One large donation to the school and I can get us out of anything, Sensei. I mean it."
    s "No, Ayane."
    s "In fact, the thing that I've been trying to get to all morning is specifically {i}about{/i} how I'm going to be addressing you all from now on."

    scene firstclass9
    with dissolve

    mi "Oh! If we're choosin' our own nicknames, I wanna be Darth Vader! Or just Miku, but with {i}Champion of Justice and Soccer{/i} added on to the end of it."
    s "That might be a little too long, but I’ll try my best to remember."

    scene firstclass10
    with dissolve

    "Ayane puts her hand up yet again."

    s "What is it now?"
    ay "Nothing really. I just wanted you to look at me again."
    ay "Hi, Sensei."

    scene firstclass11
    with dissolve

    s "Hi, Ayane..."
    s "Now please, if everyone could just stop talking for a minute or two, I'd like to address certain...changes that will be taking place in this classroom from now on."
    s "From this day forward, my teaching strategy is going to be a little different. But I'm sure that my new methods will be-"

    scene firstclass12
    with dissolve

    mak "Sensei!"

    "I already hate this job."

    s "{i}What?{/i}"
    mak "I apologize for interrupting, but what do you mean by {i}new methods?{/i} The way you do things now is perfect! Why would you feel the sudden need to change that?"
    mak "If this has something to do with our grades as a class, I'd be more than happy to offer additional tutoring to anyone who needs it outside of regular school hours."
    s "It has nothing to do with that. It's just a...decision that came to me for no reason whatsoever after school yesterday. "

    "Just, by {i}no reason whatsoever,{/i} I mean that I suddenly woke up as a teacher despite never even attempting to become one."
    "Of course {i}my{/i} methods will be different from the methods of whoever stood here yesterday. We're entirely different people."

    s "I'm sure the sudden change might come as a shock to some of you, but I really do think that what I'm suggesting will benefit every one of you a lot more than some...standard education would."
    s "These are supposed to be the best years of your lives."
    s "You're all young and impressionable...and as the person currently responsible for molding all of you, it falls on me to ensure that you {i}enjoy{/i} these years."
    s "Let me put it this way- who here besides Makoto is excited to come to school every day?"

    scene firstclass12r
    with dissolve

    ay "..."
    s "Okay, who here is excited to come to school every day for reasons that have nothing to do with how long you get to stare at me for?"
    ay "..."

    scene firstclass12r2
    with dissolve

    ay "..."
    s "That's what I thought."
    mak "Sensei, we're a little too old to be converting to the Montessori tactic, don't you think?"
    s "I have literally no idea what that is."
    s "I'm not suggesting that you all give up on learning and just focus on having fun for the rest of your lives if that's how I'm making it sound."
    s "I'm simply saying that, from this point on, I want you to see me as a friend first and foremost...and a teacher second."
    s "And also that I probably won't assign any work at all anymore and that I trust each one of you to just...independently study during the day while I sleep or something."

    scene firstclass13
    with dissolve

    r "Chika walked out on a hell of a class..."

    "The two girls in the corner of the room finally decide to join in on the class."

    f "Umm...Sensei?"
    s "Yes? Do you have a problem with this change as well, Futaba?"
    f "N-No! I'd never doubt your methods at all, but..."
    f "I'm not sure if I understand what you mean when you say you want us to...see you as a friend."
    s "I just mean that you're going to have a harder time enjoying your lives here if you feel like I'm constantly on some pedestal way out of your reach."
    s "That's precisely what I'm trying to avoid. You don't need another unnecessary authority figure in your lives when that's all you're going to be dealing with for the next...forever."
    s "So if you can see me as a friend-"
    mak "We...{i}do{/i} need another authority figure, though..."

    scene firstclass15
    with dissolve

    mi "{i}Makoto, stop it! Ya have any idea how good this news is for me?! I might actually be able to pass now!{/i}"
    mak "I'm sorry, Miku...and I'm sorry, Sensei. I just can't bring myself to accept or...even understand why you think something like this is a good idea all of a sudden."
    s "I didn't expect you to. Like I said, I know this change might be shocking. But if you really trust me...which I know you do, {i}Makoto...{/i}you'll at least try it out."
    mak "..."
    s "..."

    play sound "slidedoor.mp3"
    scene firstclass16
    with dissolve

    c "Kay! I'm back. What'd I miss? The air seems kinda off in here all of a sudden."
    r "Not much. Sensei is just going through a midlife crisis and wants to be friends with all of us now."

    scene firstclass17
    with dissolve

    c "For real? But he doesn't even seem that old."
    s "Thanks, Chika. It probably sounds sad, but I really needed to hear that."

    scene firstclass18
    with dissolve

    c "No prob, Sensei! You did me a favor earlier, so it's the least I can do to pay you back!"
    c "Also, does being friends with you mean that you'd like, drive us around and stuff? Cause taking the bus to the mall all the time kinda adds up after a while."
    s "Unfortunately, I don't have a car."

    "Nor do I have any idea how to drive, but I feel like I can safely omit that fact."

    c "That's fine, I guess. None of my other friends have cars, so it's not like I'm not used to this or anything."
    s "Great. Then-"

    scene firstclass19
    with dissolve

    ay "Sensei."
    s "What now?"
    ay "May {i}I{/i} have a ride after school today?"
    s "I literally just said that I don't have a car."
    ay "Who said I'm talking about cars?"

    scene firstclass20
    with dissolve

    a "Ayane! Can you {i}not?!{/i} We're still in class even if Sensei is going through a midlife crisis right now!"
    ay "We are, but there aren't any teachers around anymore. Just friends, Ami. And friends can talk about falling in love with friends' relatives, no?"
    a "No!"
    s "Anyway, if anyone has any issues with this, feel free to take it up with me in my office after school."
    s "Also, Makoto, if you could remind me where my office is, that would be great."

    scene firstclass26
    with dissolve

    mak "Oh, don't worry. I already decided to head there the moment you mentioned that's where we need to bring our concerns."
    mak "At the very least, before these {i}new methods{/i} begin, can we take the quiz I went to the trouble of printing this morning?"
    s "Sure, Makoto...You can all take one last quiz before they are gone forever."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I grab the small stack of papers that Makoto left on my desk and begin walking around the class and handing them out."
    "I have no intention of grading any of them once they're completed, but seeing as I may have just erased Makoto's entire reason for living, the least I can do is humor her for now."
    "Class representative aside, though, it seems like everyone else was okay with the idea of a...significantly less formal learning environment."
    "Well, everyone else apart from Yumi, who wasn't even here today, and Sana...who has yet to speak so much as a word to me."
    "Eventually, class comes to an end and Makoto informs me of where my office is before making plans to show up once she's done shredding all of next week's handouts, which she printed way too far in advance."
    "………"
    "……"
    "…"

    scene makoffice0
    with dissolve2

    play music "phantomthief.mp3"

    "I lean back in my chair and wait for a small girl with glasses to show up and beg me to be whoever it was she spent the first part of this school year growing closer to."
    "It's a little funny. I figured the reaction she gave me after I called her by her first name meant that she'd be one of the easiest to conquer."
    "That thought was a bit short lived, though. Because now, it seems like she's more hesitant than anyone."

    s "..."

    "So..."
    "{i}This{/i} is where I'm supposed to be spending my time after school, huh?"
    "I've already shirked the responsibility of teaching, so I doubt I could get away with shrugging this part of my responsibilities off as well."
    "Besides, having a private office could be a good thing."
    "I have no idea how often the girls in my class will need any {i}counseling,{/i} but an area where we can get to know one another seems like a pretty good idea in my book."
    "I imagine I'll just be spending most of my time in here sleeping anyway."

    play sound "knock.mp3"

    "But for now...I must once again figure out how to deal with the handful that is my very own teacher's pet."

    mak "Sensei, may I enter?"
    s "Come on in, Makoto. The door is open."

    play sound "dooropen.mp3"

    scene makoffice1
    with dissolve

    mak "Excellent. Because now I can give you an earful about whatever it is that's gotten into you."
    mak "What are you thinking? Going off and deciding something like that without even {i}consulting{/i} me first?"
    mak "With the exception of a few girls, I was under the impression that this year was going extremely well so far."
    mak "So why now? Why would you decide to just...dismantle all that you have built since the school year started?"
    s "I'm not {i}dismantling{/i} anything. I'm just...renovating, I guess."

    scene makoffice2
    with dissolve

    mak "But we didn't {i}need{/i} renovations! I love the way you teach!"
    mak "You know so much about so many things, and the idea of you just abandoning that part of you in exchange for friendship? Well, that's just absurd to me."

    "Unfortunately for Makoto, {i}I'm{/i} not the one who abandoned anything. I just woke up somewhere I wasn't meant to be."
    "She just gets the honor of being the first person who has to suffer because of that."

    s "Will you give it a shot at least?"
    s "If you trust me so much, can't you just go along with it for a little while and see how it goes?"

    scene makoffice3
    with dissolve

    mak "Are you sure that approaching your job so informally is even allowed?"
    mak "What would the other teachers and staff members think if they knew you were going to treat us more like friends than students?"
    s "I guess we'll just have to wait and see. Besides, it’s not like I’m letting you all run wild. I just think it might be good for us to relax every once in a while."
    mak "Relax?..."
    mak "What do you mean, {i}relax?{/i}"
    s "Well, what do you do in your free time? Apart from...printing out quizzes and independently studying."

    scene makoffice4
    with dissolve

    mak "That's...uhh..."

    "Makoto glances off to the side, avoiding eye contact with me and...getting suspiciously embarrassed for someone who was just asked about her hobbies."

    mak "That's...a bit of a complicated question..."
    s "It seems pretty normal to me."
    mak "Well, yes...but my situation is...uhh..."

    scene makoffice5
    with dissolve

    mak "If I tell you this, can you promise to keep it to yourself?"
    s "Of course. Nothing you say here will ever leave this room."
    mak "Okay...because it would be horrible for me if you were to let this out. So...please keep that in mind."

    "Just what kind of seedy shit is this girl up to?"

    mak "I..."

    scene makoffice4
    with dissolve

    mak "I have..."
    mak "A part time job..."
    s "Oh."
    s "Is that it?"

    scene makoffice6
    with dissolve

    mak "What do you mean, ‘is that it?!’ Having a part time job is strictly prohibited according to section E of the student handbook!"
    s "..."

    scene makoffice7
    with dissolve

    mak "Jeez...You should know this by now, Sensei. It’s one of the most serious infractions of all and can even lead to expulsion in some cases."

    scene makoffice8
    with dissolve

    mak "Though...I guess it doesn’t really stop any of the other girls from taking up part time jobs as well."
    s "Is it really a {i}serious{/i} infraction if so many people are doing the same exact thing?"

    scene makoffice9
    with dissolve

    if bonus == True:
        mak "Well, yes...But it's not as if any of the staff is actively seeking out girls with part time jobs."
        mak "They just technically {i}could{/i} be if word got out. And I'm sure that even I'm no exception to that."
    else:
        mak "Well, yes...And I suppose that since we're in college and several of us need to work jobs in order to put ourselves through it due to a lack of financial aid, it makes sense..."
        mak "But it's still against the rules and I like rules. That is a thing you will be finding out throughout the course of the game."
        mak "I sure hope my diligent way of living does not one day become too much to bear."
        s "Yes, that would be bad."

    s "So...what do you do exactly? Where do you work?"

    scene makoffice4
    with dissolve

    mak "Just...a small shop run by my family. It's nothing too exciting."
    mak "My dad has owned the place since I was a baby...and my grandpa ran it before him. So it's kind of just...what my family does now, I suppose."

    scene makoffice10
    with dissolve

    mak "But unfortunately, ever since the city was sectioned off and all of the men were drafted...it's just been my mom and me looking after the place."
    mak "And while she is...extremely comfortable with the business, it can still be a bit awkward for me at times..."

    scene makoffice11
    with dissolve

    mak "But we do our best, all things considered..."
    mak "I..."
    mak "I know that it will probably sound a little depressing to hear this, but working and studying take up pretty much {i}all{/i} of my time."
    mak "I don’t really have any hobbies or things I like to do..."
    mak "Which is...I guess why that whole thing about relaxing just didn't really click for me."
    s "Hmm..."

    scene makoffice12
    with dissolve

    mak "Is...Is something wrong?"
    mak "That's not the type of face I normally see on you."
    mak "I know that this office is supposed to be meant for {i}you{/i} to counsel others, but if there's anything you would like to open up about, I don't mind-"
    s "Makoto, close your eyes for a second."

    scene makoffice13
    with dissolve

    mak "I...I beg your pardon?"
    s "Just do it. Trust me."
    mak "I...uhh..."
    mak "If..."

    scene makoffice14
    with dissolve

    mak "If you insist..."

    scene black
    with dissolve2

    if bonus == True:
        jump makotoofficemassx
    else:
        "I lead Makoto through a secret passageway underneath the desk that I found earlier."

        mak "What...is this place?..."
        s "This, Makoto...is Hogwarts School of Witchcraft and Wizardry."
        mak "Has this always been here?"
        s "Yes. This event was never changed and has always been like this."
        s "Now, quick. Put on the hat."
        mak "Ah! But I do not know how to wear a hat. What if I do it wrong?"
        s "Hah..."

        "I spend the next half hour explaining the process of wearing a hat to Makoto, but then the event ends before she's ever sorted into a house."

        $ renpy.end_replay()
        $ firstclass = True
        $ makoto_love += 1

        "{i}Makoto’s affection has increased to 1!{/i}"

        stop music fadeout 3.0

        "………"
        "……"
        "…"

label slumparty:
...
```

## Code that triggers this event
File: None
Code:
```python
None
```