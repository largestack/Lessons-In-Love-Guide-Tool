# December 28, 2020 (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Approximation](./slumberreset2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: slumberreset3
* Group: Main
* Triggered by label: tsuneyogswrong
* Chain sources: slumberreset2
* Chain sources path: slumberreset2

## Official wiki page

[December 28, 2020](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=slumberreset3&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label slumberreset3:
    play sound "phonebeep.wav"

    "I send a quick text message to both Maya and Ayane about my success with our {i}targets.{/i}"
    "Whether that success will lead to anything long-lasting is still up in the air, but at least I’ve managed to overcome adversity and actually be {i}useful{/i} in some form for once."
    "It only took...I don’t know- how long has it been again? "
    "A year?"
    "Two?"
    "Three?"
    "It’s surprisingly hard to keep track of time without an annually increased four-digit number that serves to constantly remind you of how many years you’ve been alive."
    "Throughout my time here (However long it may be), that number has only gone up once- and even then it was only for a short while as the new year rolled in on deflated tires and a misshapen axle. "
    "Today is December 28th, 2020."
    "Or is it?"
    "Ask me again if your calendar ever runs out of pages."

    play sound "phonebeep.wav"

    "A text arrives just before I fall too deep into confusing introspection."
    "And as I pull myself from a well shaped by bricks of clay and clockwork, I wonder if the light of day will ever return."
    "I wonder when I’ll run out of pages."

    scene sky
    with dissolve2
    play music "thesleepingcity.mp3"

    ay "{i}Can I call you?{/i}"

    "This is not the correct light. "
    "It doesn’t hurt when I look up."

    play sound "phonebeep.wav"

    s "{i}Sure.{/i}"

    "Or maybe I’m already a little blind."

    play sound "phonebeep.wav"

    ay "Hey! Good to see you’re using your normal phone again."

    "I answer before it even has a chance to ring. "
    "The voice on the other end makes the day a little brighter, but it still doesn’t hurt."

    ay "You really got Yumi and Tsuneyo on board? Like, seriously? How did that go?"
    s "Ayane...is Todd still missing?"
    ay "Hm? Yeah. You haven’t seen him, have you?"
    s "..."
    ay "Sensei?"
    s "No, I haven’t. I was just wondering."
    ay "Uhh...okay! Tell me more about what happened, though. Was it hard? How much were you able to say about stuff?"
    ay "You’re on speaker, by the way. Maya’s here."
    s "That’s fine. It wasn’t {i}particularly{/i} hard. I needed a different approach for each of them, but...we should be able to move forward now. Wherever forward {i}is{/i} exactly."
    ay "I think forward means backward right now, but that’s still great news. Have you given them your new address yet?"
    s "I haven’t even given {i}you{/i} my new address yet."
    ay "You should hurry up and do that. Maya says the thing might happen any day now."
    m "It’s true. The sooner we get this out of the way, the better. "
    m "As you know, I’m unable to pinpoint the exact date this will happen-"
    m "But a prolonged delay puts everything you’ve done over the last two days at risk. Which would be a shame since you finally, you know, {i}did{/i} something. We don’t want that to go to waste."
    m "It’s also very likely this “slumber party” may need a bit of an extension if the reset does not fall on the first night of our get-together. "
    ay "I vote that we all move in with Sensei until the world ends!"
    m "Rejected. There’s no way that would work when-"
    s "When are we doing this?"

    "There’s a brief silence on the other end of the phone when I attempt to move things along. "
    "It’s a safe bet that neither Ayane nor Maya expected me to interject in such a way given how laid-back I typically am in the face of what could only be described as “certain doom...”"
    "But there are things I’m worried about losing now."
    "You see, I had another dream last night."
    "They’re happening almost every time I fall asleep. "
    "But they never help."
    "All they do is dangle the things I’m learning to love in front of my face- then mock me when they cut the string."
    "Yet somehow..."
    "Nothing falls but me."

    m "We...need a bit more time to make the necessary “preparations” first. I’m sure the other two girls would also appreciate being given some sort of notice."
    s "What sort of “preparations” need to be made, exactly?"
    ay "Maya hasn’t figured out what to do about Ami yet."
    m "It’s been a very long time since I’ve needed to do something like this and, somehow, she seems even {i}more{/i} attached to you now. Which I suppose would make sense given how...you know."
    m "But it doesn’t change the fact that I’m having a difficult time shaking her as the absence of {i}all three of us{/i} is sure to set off some alarms in that mostly-empty head of hers."
    ay "That’s true...she {i}has{/i} been feeling awfully left out lately."
    s "She looks up to Niki a lot. I could ask her if-"
    m "No."
    s "Wow. That was an uncharacteristically snappy response."
    m "I can handle Ami. I just need a little more time. Two days at the most."
    ay "Then let’s shoot for Sunday. Abandoning her on New Year's Eve sounds even harder since it’s a holiday, but the day before would probably be doable, right?"
    m "That’s probably our best bet, yes. I just hope everything lasts until then as we’re already cutting it close."
    ay "Does that work for you, Sensei?"
    s "Yeah...I’ll tell the others now. And if you need any help with Ami-"
    m "Absolutely, under no circumstances, do {i}anything{/i} about Ami. If you get involved, she’ll just wind up being more suspicious."
    s "What should I do then? I don’t want to just wait around."
    m "I’m sure you’ll figure it out. But, seeing as we have now exhausted everything we needed to talk about, I’ll be hanging up now."
    ay "Wait, Maya! That’s my-"

    play sound "phonebeep.wav"

    s "..."

    scene black
    with dissolve2

    "For the next two days, I do nothing."
    "I don’t leave my house...or respond to any text messages from anyone unrelated to the upcoming reset..."
    "And some of them probably worry about me."
    "They {i}all{/i} probably worry about me since I’ve somehow wound up as the anchor keeping them planted on this planet, but..."
    "They shouldn’t."
    "I’m fine."
    "..."
    "I’m fine."
    "........."
    "......"
    "..."

    $ totaldays += 2
    $ day = 7
    hide friday onlayer date
    show sunday onlayer date

    scene resetslumber1
    with dissolve2

    "The night of the slumber party comes before I know it."
    "Yumi and Tsuneyo both showed up precisely when they were supposed to, and Ayane wound up convincing Sana to invite Ami over to her dorm room for a gaming-focused sleepover."
    "Apparently, Ami was a little hesitant at first given that Sana had never done something like that before, but..."
    "I guess she is {i}my{/i} niece after all. And I’d never be able to refuse Sana if she asked me to do something like that. "
    "In fact, I {i}hope{/i} she asks me to do something like that. A two-person sleepover with a girl like her is all someone like me could ever..."
    "Could ever..."
    "Nevermind."
    "I’m not in the mood."

    ay "So, uhh...thanks to everyone for coming! I know that neither of you are particularly close to any of us and that...this probably sounded kind of insane when you first heard about it, but...uhh..."
    ay "There’s pizza? And other assorted snacks and stuff. So it doesn’t have to be, like...{i}completely{/i} awkward...right?"
    y "Nah. This shit’s even more wack than I thought it was gonna be. "

    scene resetslumber2
    with dissolve

    ay "Is it really that bad?"
    t "I haven’t felt this uncomfortable since you taught me how to masturbate."
    y "See what I mean?"
    ay "On the bright side...um...we {i}do{/i} all have something in common now. That’s gotta be worth some points, right?"

    scene resetslumber3
    with dissolve

    m "Ayane is right. The purpose of this gathering was not {i}just{/i} so we could observe one another throughout the night, but so we could take it upon ourselves to educate you as well."
    m "I’m not sure what either of you have been told, but if there are any questions you have about what is going on, now is the best time to ask them."
    m "And I say that fully aware that there is a very high likelihood neither one of you will remember any of it very shortly."
    y "You, uhh...you’ve been doin’ this the longest, right? That’s how {i}he{/i} made it sound, at least."
    m "That is correct. I have the most experience and Ayane has the least."
    y "And...it ain’t just memories that are bein’ fucked with? It’s actually the world?"
    m "I’d say it’s “time” rather than the world itself as the world {i}does{/i} seem to be changing with each passing loop."
    m "This is evidenced by the sinkhole where Kumon-mi Academy once stood, as well as the many new businesses that have popped up as the years have gone by."

    scene resetslumber4
    with dissolve

    y "And that shit ain’t gonna go back to normal after the whole “apocalypse” thing blows over?"
    m "If it were going to go back to “normal,” it would have happened already. The destruction of that school and subsequent integration of all of their students into {i}ours{/i} is something brand new to even me."
    y "So, basically...we’re all just stuck as freshmen and everything else is still changin’ normally?"
    m "That is more or less the case, yes."
    y "Damn. Now I really wish I was here for that two-month gap between Halloween and Christmas. No point in goin’ back to school if I can’t ever get out."

    scene resetslumber5
    with dissolve

    t "Two-month gap?"
    y "Yeah. Did that shit not happen to you? Figured you were in the same boat since you got dragged here as well."
    t "I did not sense anything abnormal about the last two months. What does this “gap” entail, exactly?"
    ay "The rest of us jumped directly from the Dorm Wars closing ceremony to Christmas Eve. None of us have any memories of what happened in between."
    m "To be fair, we can’t be 100%% certain that Tsuneyo’s memories of this time frame are reliable. There are plenty examples of real memories being swapped out for false ones."

    scene resetslumber6
    with fade

    y "Wait, what? "
    y "You tellin’ me that I ain’t just gotta worry about not rememberin’ shit now...but that some of the shit I {i}do{/i} remember isn’t even legit?"
    m "Possibly. But seeing as I’m not at all close with you, I’d have no way of knowing which memories of yours are “legit” or not."
    m "This sort of thing is typically most prevalent directly after the world is reset as events directly correlating to it are removed from the minds of those involved and replaced with more traditionally logical scenarios."
    m "In my opinion, the most ideal scenario right now and what I imagine would actually provide us {i}some{/i} form of answer, is one of you making it through the reset while the other does not."
    y "Ain’t that just askin’ for somebody to be killed, though? The fuck does it even mean to be a human being if your memories ain’t even yours?"
    m "I may have believed that a long time ago. Now, I just see it as another system in place to prevent this world from deviating from its given path. "
    m "Do you have any more questions?"
    ay "I have one."

    scene resetslumber7
    with dissolve

    m "Oh, right. I suppose you would as you’re still mostly lacking in experience. What’s your question, Ayane?"
    ay "My question is...shouldn’t we be hoping that {i}everybody{/i} makes it through instead of just one person?"
    m "While that may be more {i}fun and heartwarming,{/i} it doesn’t {i}teach{/i} us anything. We did not call this meeting to establish a big, happy, eternal family — we called it to get to the bottom of this. To {i}learn.{/i}"
    ay "But why can’t we-"

    scene resetslumber8
    with fade

    m "Let me explain something to you, Ayane. And to the rest of you as well since I don’t really mind you learning things about me that I know won’t stick."
    m "I am {i}tired{/i} of being stuck in this body."
    t "When that happens, you should train. Become a better you."
    m "That is not what I mean. I want to {i}grow up.{/i}"
    m "I’ve experienced the first year of high school for so long that I can’t even estimate how much time has {i}actually{/i} passed anymore. "
    m "So while I’m sure that eternal life and eternal youth may sound great to some of you...for others, it’s a prison."
    m "Even the things you love the most become easy to despise when you’re unable to escape them. "
    m "So, no. I {i}don’t{/i} think we should be hoping for more people to {i}make it through.{/i} Not when that means damning them to a life of perpetual falsehood. "
    ay "I..."
    ay "I didn’t really...think of it like that..."
    t "It is clear to me that you have done this for a very long time...but your memories alone are not enough to surpass those of others in terms of reliability. "

    scene resetslumber9
    with dissolve

    m "Huh?"
    t "What I mean to say is that being caught in a perpetual cycle may have created this jaded and stubborn outlook you have. "
    t "Even my father grew tired of noodles at one point."
    t "Why should everyone trust you just because you say you’ve been around the longest when you’ve already admitted to the possibility of false memories being swapped in for the truth?"
    m "That...no, hold on."
    t "You are no more reliable than I am...but you want to be seen that way. And the people who want trust the most are, more often than not, the ones who are not meant to be trusted."

    scene resetslumber10
    with fade

    m "R-Regardless of whether or not anyone trusts me, which I really don’t care about, I still think it would be best to approach all of this with an air of skepticism. "
    m "Despite my tendency to do so, I understand that it is typically impossible to predict the future. What {i}is{/i} possible is creating objectives or goals or...places you want to end up."
    m "{i}That{/i} is what I’m doing right now. So please forgive me if I wind up leaving you out of those places if I’m unable to make enough room for you."
    y "Not gonna lie, this shit hurts my brain. But damn is it entertaining."

    scene resetslumber11
    with dissolve

    ay "Do you have anything to add, Sensei? You’ve been pretty quiet this whole time."
    s "Huh? Me? What?"
    y "If you’re blackin’ out again, least you’re doin’ it here. Got four whole people to hold you down this time and, much as I hate to admit it, Tsuneyo’s a Hell of a lot stronger than I am."
    ay "So am I, but we can ignore that if it makes you feel better."
    y "Say that again and I’ll beat your ass so bad you’ll be {i}hopin’{/i} to get your memory wiped."
    s "I’m not blacking out. I’m fine. Just...feeling a little out of it, I guess."

    scene resetslumber12
    with dissolve

    m "Out of it...how? What do you mean?"
    s "I’m probably just tired. In fact, does anyone want coffee? I saw that Ayane brought some over and, if we’re really going to be staying up all night, we’re going to need it."

    scene resetslumber13
    with dissolve

    ay "There’s soda and hot chocolate too if anyone wants any. I might be banned from using my credit card, but there was still plenty of stuff at my house I was able to grab before coming here."

    scene black
    with dissolve2

    m "I suppose I’ll have some coffee. The last time I stayed up all night was- well, actually...it was Christmas. But before that, it was a long time."
    t "I will make myself tea as I also brought some things from home. But if it is okay with everyone, I would like to return a phone call first. It should not take very long at all."
    s "I can make your tea. Just tell me where you-"
    t "I refuse to let a man touch any of my beverages. I have heard too many horrible stories."
    y "Smart move. I’ll hold off on coffee for now on account of both that and the fact that I ain’t really tired yet."
    ay "Go ahead and make your call, Tsuneyo. We’ll wait for you to come back before we talk about anything important again. "
    t "Thank you for understanding. Please excuse me."

    play sound "dooropen.mp3"
    scene resetslumber14
    with dissolve2

    "I make my way over to the coffee machine (Which I have yet to use in the short time of me “owning” this apartment) and, between the scoops of grounds, attempt to make sense of the way I’m feeling."
    "It’s all wrong- even by my standards, which have never been {i}right{/i} to begin with."
    "Is this really going to work?"
    "If what Maya says about watching everyone disappear is true...do I even have it in myself to do that?"
    "These girls are important to me."
    "If they’re going to hurt, it should be {i}my{/i} fault. Not the fault of some cosmic horror descending from an unimaginable Heaven and wreaking havoc on their fragile bodies."
    "Those bodies are {i}mine{/i} to break. "
    "That fragility is {i}mine{/i} to take advantage of."

    s "..."

    "And yet..."
    "I’m making them coffee."

    y "Ponytail, you got a sec? Have another question for you."
    m "The amount of secs I have will not expire until the current cycle comes to an end. Feel free to ask whatever it is you’re concerned about. Just know that I don’t have {i}all{/i} of the answers."
    y "I’m fine with stayin’ up and shit but, like...how will I know when this apocalypse business starts? What should I be on the lookout for?"
    m "Oh, you’ll know. And if you get too tired, it’s fine to take a nap. We can sleep in shifts."
    m "The important thing is that we all stay in one place so that, should the world begin to collapse, we won’t need to go far to find one another."
    ay "We don’t know that for sure, though...I wasn’t able to see you at all last time."
    m "No...you weren’t."

    scene resetslumber15
    with dissolve

    m "But {i}he{/i} was."
    m "Maybe that’s the key?"
    ay "Only one way of knowing, I guess. I’ll try not to get too scared this time."
    y "And I’ll try to...not get in the fuckin’ way or whatever. This shit’s so weird."

    "There are over nineteen different ways to brew coffee."
    "I will now tell you about them."
    "The first is the espresso machine."
    "Anyone who knows anything about coffee knows what an espresso machine is – they’ve been keeping us caffeinated since 1901."
    "Today they come in various shapes and sizes, with loads of features and gimmicks. "
    "Don’t get confused by flash machines though because the basics are the same. "
    "Pressurized water is pushed through a chamber/puck of finely ground coffee beans, through a filter, resulting in what we call a shot of espresso. "
    "Don’t have a few hundred bucks to spend on an espresso machine, but still looking for that espresso-shot-like-kick that comes from a pressurized brew? The Moka-Pot is the next best thing."
    "The magic behind the Moka pot is in its 3 chambered brew process. Water in the bottom chamber boils, and the steam causes pressure that pushes water up through the coffee grounds into the top chamber.​ "
    "The AeroPress has a cult following among the traveling coffee community, and it looks more like a science project rather than a coffee brewer. "
    "But, if you ask me, it’s the best thing that has ever happened to coffee. And many people say it brews the best coffee they’ve ever tasted. "
    "The French press is the unofficial mascot of home brewed coffee."
    "It’s been steeping coffee in households since before your grandparents were born, and it has a very loyal, cult following among the home barista community. "
    "But why?"
    "It’s likely thanks to multiple reasons, but our money is on the fact that its super easy to use, can be picked up for pocket change (almost) and produces a brew with a distinct taste and feel like no other method. "
    "A relatively new invention (est. 2010) the SoftBrew has been dubbed ‘primitive yet high tech’. "
    "I’m not sure what the fuck that means, but if I were to describe the SoftBrew in simple terms, I would say “it’s like a French press, but easier.” "
    "The idea of instant coffee is great – it comes in a small jar so you can take it anywhere. Just add hot water."
    "There’s just one major problem — it fucking blows. So we’re not gonna talk about that one."
    "Making coffee with a siphon pot is unique as it comes."
    "It’s a combination of brewing methods: a full immersion brew (as your coffee goes into the water) but also uses siphon action to create a great tasting cup. "
    "It’s not a simple way to brew coffee, in fact, it requires an enormous amount of effort and process, so you won’t want to use it daily (unless you’ve got nothing else to do). "
    "The percolator is nothing new or cutting edge in the world of coffee. If you’ve been to a bland looking diner somewhere in the Northern Hemisphere, chances are you’ve drunk percolated coffee. "
    "Rumor has it that there are people out there who actually enjoy percolated coffee, but the person who told me that was also trapped inside a jar of peanut butter."
    "The next method is the Chemex brewer, which looks like a weird vase."
    "The primary benefit of using a Chemex over other drippers is capacity."
    "You can easily make 3 or 4 cups in one go, rather than 1 or 2, meaning it’s a crowd pleaser when your homies are around."
    "In fact, you can buy a 10-cup Chemex Vase that takes 50 ounces of water. It’s an entertainer’s best friend. "
    "Sometimes, I masturbate in front of the window in hopes that someone will see me."
    "I’ll be honest: when I first got my V60 dripper I didn’t have too much faith in it – it just seemed so simple compared to other pour over coffee brewing systems. That week I learned never to make assumptions."
    "The Hario v60 is a simple yet brilliant way to brew coffee – its small and light, meaning you can take it just about anywhere, and it makes a damn good cup of Joseph."
    "The Kalita Wave Dripper is the arch-enemy of the Hario V60 – and it’s giving the V60 a good run for its money. "
    "Like the V60, the Kalita Wave involves a simple cone shaped dripping system, however, its flat-bed (as opposed to the v60’s conical shape) means longer dwell times and less room for error. "
    "The Vietnamese dripper (also called a ‘Phin’) is a single cup dripper that takes 4-5 minutes to brew, meaning it’s the perfect accomplice for solo coffee drinkers who want more time to party."
    "Unlike some of the above drippers, this method of brewing does not call for much skill or fancy pouring style. It’s about as easy as they come; just pour in your water and wait. "
    "The Melitta Ready Set Joe dripper is the most convenient option on the market – perfect for camping fanatics who still love a decent cup of Joseph."
    "It’s a simple plastic dripping cone that brews coffee in a flash. "
    "You won’t get the same quality brew that you’ll get with other drippers, however, its price tag and portability means it’s a favorite among campers and travelers.​ "
    "The Bee House is a Japanese pour over brewer that is getting a great deal of attention in the coffee world – likely because it’s easy to use and looks really sexy."
    "It’s worth mentioning that the learning curve is more forgiving than the Hario V60 or the Kalita Wave, meaning it’s a great way to get your feet wet in the world of pour over coffee. "
    "Tsuneyo sure is taking a long time out there."
    "The Clever Dripper looks like just any other pour over dripper, but on closer inspection you’ll notice that the Clever Dripper is a cross between a steeping and pour over brewer. "
    "What sets this lil’ dude apart from the rest of the dripper family is its clever little valve that stops your brew draining into your cup/vessel until you activate it. "
    "If you haven’t heard of cold drip coffee you must be a fucking idiot. That or you’ve been hiding under a rock for the past few years. "
    "Cold brew is one of the most popular caffeine infused innovations of our time – and no, we are not talking about iced coffee. "
    "In a nutshell, it’s made by slowly dripping cold filtered water through your fresh grinds for a long period – often 10 hours or more. Enough time to kidnap someone or repair a section of a broken fence."
    "Derived from cold brew coffee, nitro coffee is the newest kid on the block in the coffee world, and you can expect to hear a lot more about it in the future."
    "As the name suggests, its’ (cold brewed) coffee, pumped full of nitrogen, which affects the taste and the texture in a very, very nice way. "
    "The result is similar to a cold brew coffee but crisper, a little sweeter and it looks like a pint of Guinness — a beverage that does not exist in Kumon-mi since we are blocked off from the rest of the world."
    "Aren’t you excited to know so much about coffee now?"
    "Let's learn some more."
    "Cowboy coffee is the oldest known method of brewing coffee."
    "It’s outdated, but it works, and you don’t need much to make it happen. "
    "Commonly used around campsites where nobody has bothered to pack any coffee making gear, all you’ll need is a flame and a saucepan. "
    "In a nutshell: fill your pot with water, bring it to a boil, throw in your ground coffee, remove it from the heat and let it brew for a few minutes. "
    "Once the grounds settle to the bottom of the pot, you can pour your coffee into your mug, slowly and gently. Nothing fancy required. "
    "From 1299 The Ottoman Empire ruled Turkey for an impressively long stint, and strong Turkish coffee played a significant role in fueling their endurance. "
    "There’s a very good chance that I made up that last fact, however, you can be sure that (A) Turkish coffee packs a punch, and (B) It’s been enjoyed around the world for a very long time."
    "Brewing Turkish coffee seems easy, but with like most brew methods, there’s skill in doing it right. Learn the skills by reading a guide or something."
    "The most common way involves a Turkish coffee pot, water and very finely ground coffee beans. "
    "You’ll simmer the brew a number of times (2-3 times) and end up with a brew that you’ll love or hate: strong but exceptional tasting with a thick foam on top. "
    "Congratulations. Now you are the coffee expert."

    play sound "knock.mp3"
    scene resetslumber16

    s "I’ll get it."

    play sound "static.mp3"
    scene resetslumber17 with flash
    stop sound

    s "Hey. How was your phone call?"
    t "It was fine. Apologies for locking myself out of the room. I am not used to doors that do that automatically. "
    s "It’s fine. I boiled some water for you if you want to make your own tea. I solemnly swear that I didn’t drug it either."
    t "I thank you for taking the time to both boil the water and not place any drugs in it, but I regret to inform you that I will no longer be able to stay here tonight."
    s "What? Why not?"
    t "A neighbor has reported a strange smell coming from Tojo Ramen. I must return home to investigate this and make sure that everything is in order."
    t "It is highly probable that the power has gone out once again and that food is beginning to spoil."
    t "However, if it is something as serious as a gas leak, please be prepared to never see me again as I may explode."
    s "What about your father? If there’s a gas leak, shouldn’t he be the number-one priority?"
    t "I am worried about him, yes. Which is precisely why I must return."
    t "I apologize for the inconvenience. But if the world does not end and you reconvene tomorrow, I’d be happy to join you once more."
    s "That’s fine since it’s an emergency and everything...the others are just going to be a little disappointed since they had to pull a bunch of strings to make sure this happened."

    scene resetslumber18
    with dissolve

    t "Is that so?"
    s "Yeah...keeping Ami away from us isn’t really an easy task, you know."
    t "I see..."
    s "Oh well. Get going, then. I’ll be the one to break the bad news. Wouldn’t want {i}you{/i} having to upset them and I’m already pretty much used to it."
    t "I’m sure they will be fine. "
    t "They seem to be having a great deal of fun right now."

    play sound "static.mp3"
    scene resetslumber19 with flash
    stop sound
    stop music

    s "Yeah, they’re getting along much-"

    play sound "dooropen.mp3"

    t "Please excuse me. "
    t "Thank you again for the invitation."
    s "........."
    s "........"
    s "......."
    s "......"
    s "....."
    s "...."
    s "..."
    s ".."
    s "."
    s " "

    "I’m fine."
    "..."
    "I’m fine."

    play sound "static.mp3"
    scene resetslumber20 with flash
    stop sound

    six "73 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 68 "
    six "74 68 65 20 65 6e 64 20 6f 66 20 64 61 79 73 20 69 73 20 75 70 6f 6e 20 75 73 "
    six "68 61 76 65 20 79 6f 75 20 66 6f 75 6e 64 20 69 74 20 79 65 74 3f "
    six "74 68 65 20 70 61 72 61 64 6f 78 3f "

    scene spider1
    play sound "happybaby.mp3"
    $ renpy.pause(6, hard=True)
    scene spider2
    $ renpy.pause(6, hard=True)
    $ renpy.end_replay()
    $ slumberreset3 = True

    jump slumberreset4

label slumberreset4:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
label tsuneyogswrong:
    sev "Fact checker?"

    scene wemadeit24
    with dissolve

    t "No...that’s not right."
    s "Ahhhhhhh!"
    sev "Are you absolutely sure?"
    t "I am."
    sev "{i}Absolutely?{/i}"
    t "I have never been more sure of anything in my life."
    sev "How unfortunate! Because that means our protagonist is going to have to start over at the beginning of the slumber party!"
    s "The beginning?! That is so long ago!"
    sev "It is! But that’s the price you have to pay for not caring and valuing everyone’s time and opinions!"
    sev "We’re only doing this to help you, you know. Like anyone else, we want you to succeed!"
    s "Then let me try again! Will get it right this time!"
    sev "You {i}can{/i} try again!"
    s "Yay!"
    sev "You’ll just have to hold down the CTRL key for a little while. Which you’re probably already familiar with if you’re getting these questions wrong."
    s "AAHHHHH SO MEAN LONG MAYA!"

    scene theend
    with dissolve2

    sev "Thanks for joining us on Untitled Children’s Show!"
    sev "Maybe next time, our protagonist won’t make any mistakes!"
    s "Noooooooo!"

    play sound "static.mp3"
    scene frown with flash
    scene black with flash
    stop sound
    jump slumberreset3
...
```