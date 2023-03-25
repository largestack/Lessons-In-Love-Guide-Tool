# Vanilla Bean (Otoha)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Breathing in Unison](./otohadorm10.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: otohadorm10p2
* Group: Otoha
* Triggered by label: otohadorm10
* Chain sources: otohadorm10
* Chain sources path: otohadorm10

## Official wiki page

[Vanilla Bean](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=otohadorm10p2&go=Go) for more details.

## Event code

File: (install folder)\game\OtohaEvents.rpy

Code:
```python
...
label otohadorm10p2:
    "Niki once again offers to call a driver from her agency to pick us up, but Otoha remains adamant about not wanting to impose and decides to just charter her own ride off of a ride sharing app."
    "She asks me to chip in, which is mildly infuriating because it means she’s fine with imposing on {i}me-{/i} "

    if bonus == True:
        "But I guess it makes sense because she probably also wants to sleep with Niki more than she wants to sleep with me right now. Which I don’t blame her for."
        "Either way, I do my good deed for the week in an attempt to tip the scales by paying for the entire ride."
        "Now, Niki and I should be on equal footing when it comes to seducing our shared student."
        "Eventually, we make it to the restaurant and head inside."
        "Otoha informs the staff that we’re here to meet someone and, as if they're expecting us, they lead us over to Niki’s table, which has already been sectioned off from the others."
        "Niki is obviously no stranger to flexing her “famous” muscle, but she normally doesn’t do it like this."
        "I guess it’s a little different impressing [young]girls than it is impressing me, though."
        "And I’m not about to argue with additional privacy when that sort of thing has been becoming harder and harder to come by lately."
        "Anyway, Otoha and I take a seat at opposite sides of the table, and the wait for our final dinner guest begins..."
    else:
        "But, since I am such a nice and wholesome guy, I decide to pay for the entire ride and rate our driver with a perfect score of five stars so he can hopefully get a bonus and feed his family."

    "........."
    "......"
    "..."

    scene otohadinner1
    with dissolve2
    play music "love.mp3"

    o "So, uhh...Rin said she’s on her way."
    o "She also says that she is sorry in advance for, and this is a direct quote, “The overwhelming scent of vanilla bean [[COPYRIGHTED FROZEN BEVERAGE]s.”"
    ni "That bitch. Why would she not offer to bring us any? I love [[COPYRIGHTED FROZEN BEVERAGE]s."
    s "Is anyone else having a hard time comprehending the ends of sentences right now? Or is it just me?"

    scene otohadinner2
    with dissolve

    o "So...have you two, like...been here before? Because I’m starting to think this might be a little out of my price range."
    ni "Oh, don’t worry about that. I wouldn’t make you pay for your own dinner."
    s "You make {i}me{/i} pay for my own dinner almost every time we go out."
    s "Sometimes, you even make me pay for you."

    scene otohadinner3
    with fade

    ni "Yeah. And? "
    s "I just don’t think it’s very fair that Otoha gets treated better than me when I have brought you a much greater deal of joy in your life."
    ni "You bring me nothing but anger and fury."

    scene otohadinner4
    with dissolve

    ni "But we’re not here to talk about you. We’re here to talk about Otoha."
    o "Wait, we are? I thought this was just, like...a double date thing. Why do we have to talk about me?"
    ni "You just don’t normally bring your girlfriend around me. Rin, right? Is she the one you were with at the diner during your...dorm war whatever?"
    o "Yeah...and the reason I don’t bring her around you is because I only see you one day a week."
    ni "That didn’t stop you from bringing the man who simultaneously ruined my life and made it better all at once, though."

    scene otohadinner5
    with fade

    o "I mean...he kind of just came along. It’s not like I made the conscious decision to bring him there."
    s "We should do that more often. That basement is surprisingly homey for one of the most suspicious places I’ve ever set foot in."
    ni "I can’t tell if that's a compliment or not."
    s "I guess it's closer to being a compliment than {i}not{/i} being a compliment."
    ni "Your face is closer to being fucking stupid than {i}not{/i} being stupid."
    o "So, like...are you two getting back together or something?"
    ni "Yeah, {i}are{/i} we getting back together or something? Answer her question."
    s "I’m just here for the free food and cute girls."
    ni "{i}Girl.{/i} You mean me. It’s rude to call the other couple cute when you’re on a double date unless you’re trying to swing."

    scene otohadinner6
    with dissolve

    o "Well, it’s...still kind of a single date until Rin gets here. So if you two want to keep flirting or whatever, don’t mind me."
    o "I’ll just chill until I’m actually allowed to, like...cooperate and stuff."

    scene otohadinner7
    with fade

    ni "Hmm...you’ve never actually been on a double date before, have you?"
    s "Have {i}you{/i}?"
    ni "Shut the fuck up."
    o "I mean...no? This is the first relationship I’ve ever had. And I {i}definitely{/i} can’t say I envisioned my first double date also involving my teacher and a famous musician."
    ni "Are you nervous? Is that what’s going on? Because you seem less...Otoha than usual."
    o "I can assure you that I am the regular amount of Otoha. "
    ni "I guess I’ll hold off on passing final judgement until Rin shows up."
    o "Why am I being judged at all? What does my aptitude for conversing at a strange double date have to do with literally anything?"

    scene otohadinner8
    with dissolve

    ni "You’d be surprised."
    o "..."
    o "By {i}what?{/i}"
    s "I’m pretty sure Niki is just trying to sound like she knows what she’s talking about when it comes to relationships."
    ni "And I’m pretty sure that I may {i}accidentally{/i} walk out of this restaurant and leave you to pay for everything if you don’t humor me right now."
    s "So much for tonight being about Otoha."

    scene otohadinner9
    with dissolve

    ni "You fucking-"
    r "Hey! I’m here! Sorry for being so late!"

    scene otohadinner10
    with dissolve

    ni "Oh my God, hi! You must be Rin!"
    s "Finish your sentence, Niki."
    ni "{i}Die in a fire.{/i}"
    ni "It’s so nice to meet you! Otoha talks about you literally {i}all{/i} the time."
    o "I do? Oh...Oh, yeah! I definitely do. That’s a...true thing she just said."

    scene black
    with dissolve2

    "Rin shoves her bag under the table and takes a seat beside Otoha."
    "The overwhelming scent of whatever vanilla thing was alluded to earlier is immediately apparent, but not necessarily unpleasant in any sense."
    "I wonder if Otoha is sick of it by now."
    "I wonder if that’s something you can get sick {i}of.{/i}"
    "And I wonder how the rest of tonight is going to go now that what I view as a fracturing relationship is seated straight across from one that’s already finished breaking."

    scene otohadinner11
    with dissolve2

    r "Hey. I’d give you a hug and stuff, but I’m not really sure what the rules of double dates are or if you’d even be cool with that."
    r "So I’ll just say I’m hugging you in my mind right now and we can ignore how much I actually want to hug you."

    "Well, I guess Rin really is over the whole thing with Otoha’s parents."
    "Or just that she’s so in love that no amount of uncertainty could detract from her limited inhibition that causes her to constantly speak before thinking."

    scene otohadinner12
    with dissolve

    r "That aside, though...holy shit. I’m on a date with Niki Nakayama. "
    r "Well, not {i}with{/i} Niki Nakayama. But you’re here. And I’m here. At the date."
    r "We’re at the same place at the same time. Which is a date. But not the same date. "
    r "Wow."
    o "..."
    r "Wow."

    scene otohadinner13
    with dissolve

    o "So that’s Rin. Glad we’re all acquainted now."
    r "Hahah...sorry. I’m not around famous people all that often..."
    ni "{i}I{/i}, for one, see no issue at all with how you greeted me, Rin."
    ni "In fact, I think your reaction to me was completely within the bounds of how I expect {i}all{/i} people to react when meeting me."
    s "That’s because you’re a narcissist. "
    ni "Oh. And {i}you’re{/i} not? Please. I don’t want to hear it."

    scene otohadinner14
    with dissolve

    s "Everyone already knows the real me. How many people know the real you, though?"
    ni "What does that have to do with narcissism? What are you even trying to argue here?"
    ni "You know what, you really are paying for your own dinner. I was just joking when I talked about that before, but now I’m serious."
    r "Have they been like this the entire time?"
    o "Yuuuuuuuup."

    scene otohadinner15
    with dissolve

    r "Then I’m really sorry for not getting here earlier. I tried, but it was like, {i}crazy{/i} busy."
    r "You get one warm-ish day and people just frickin’ show up in flocks for [[COPYRIGHTED FROZEN BEVERAGE]s."
    o "It’s fine. Just try not to leave me alone with other couples anymore because I have learned tonight that I definitely do not like it."
    r "I’ll do my best."
    r "..."
    o "..."
    r "I missed you."
    o "I missed you too, Rin."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohadinner16
    with dissolve2

    ni "Right?! Like, it should be up to {i}me{/i} if I want to take my music in a different direction! Not the stupid agency!"
    ni "People love {i}Niki.{/i} They don’t give {i}any amount of shits{/i} about 567 Productions. "
    ni "But nope! The money machine must churn! And I’m the only one fucking strong enough to push down the lever thingy!"
    r "It’s not fair! Like, you’re clearly {i}miles{/i} ahead of pretty much everyone else in your industry. And the fact that your talent is being suppressed like this is just...I can’t even."

    scene otohadinner17
    with dissolve

    ni "Otoha. I like this girl. You can bring her around whenever you want."

    scene otohadinner18
    with fade

    o "Wouldn’t that...you know...kind of get in the way of my singing lessons? I don’t really think I'll be able to focus if Rin is there."
    r "Do you...like giving lessons, Niki? Like, it must be some sort of passion project, right? Because I can’t imagine you’re making a lot of money off of them."
    ni "It’s 100%% a passion thing. Otoha’s got serious potential and I want to help her bring that out."

    scene otohadinner19
    with dissolve

    r "Right?! She’s absolutely amazing! I can definitely see her becoming like, mega famous one day if she keeps it up."
    r "That’s why I offered to start paying for her lessons if her parents decided to stop. I really think she has what it takes."

    scene otohadinner20
    with fade

    o "Rin, come on. Don’t bring them up right-"
    ni "Wait, are they seriously considering taking you out of vocal lessons? Why?"
    o "Great. I guess we’re talking about this now."
    ni "Of course we’re talking about this now. This is something you should have told me about immediately. "
    ni "What’s the issue? Why would they do something like that?"
    r "Oh...I don’t really think Otoha wants me to keep going. I already said too much."
    o "Thank you, Rin."
    ni "No, if they’re seriously considering this, {i}I{/i} need to speak with them. Because I can not allow that to happen."
    o "Niki-"
    ni "Is it a money thing? Because I will literally do this on spec. That’s how much faith I have in you, Otoha."

    scene otohadinner21
    with fade

    r "On spec? So like...you wouldn’t get paid until after Otoha starts making money off of her singing?"
    ni "Yeah. And even then, I wouldn’t really care. I’d be doing a disservice to the music industry if I didn’t help her hone that talent of hers."
    ni "I will literally give Otoha lessons for free if her parents are going to be fucking cunts about this."

    scene otohadinner22
    with dissolve

    r "For real?! That’s amazing! And so nice!"

    scene otohadinner23
    with dissolve

    r "Did you hear that, Otoha?! "
    r "You don’t have to worry about money anymore! Niki’s fine with giving you lessons for free!"
    r "Which means we don’t have to worry about-"

    scene otohadinner24
    with dissolve

    r "..."
    r "We...don't..."
    o "..."
    r "..."
    r "Otoha?"
    r "Why aren’t you freaking out? This is great news. "
    r "Isn’t it?"
    s "..."
    ni "Oh...no."

    "Niki instinctively reaches for the sleeve of my shirt, knowing that, somehow, she managed to do something wrong by simply being nice."
    "And, in a moment of rare self-gratitude, I feel a little better about never going out of my way for anyone."
    "Peoples’ true colors come out when you show them too much kindness."
    "And, it could just be the light-"
    "But Otoha looks very colorful right now."

    scene otohadinner25
    with dissolve

    r "..."
    o "..."
    r "It..."
    r "It wasn’t just about the money, was it?..."
    o "..."
    r "..."
    ni "..."
    s "..."

    "None of us say anything, and it becomes clear that Rin isn’t going to let silence answer this question either."
    "We just sit and wait for Otoha to do something."

    r "..."
    o "..."

    scene otohadinner26
    with dissolve

    o "..."
    r "..."

    scene otohadinner27
    with dissolve
    stop music fadeout 7.0

    r "Okay."
    r "Okay..."
    o "Rin-"

    scene otohadinner28
    with dissolve

    r "Thanks for coming tonight. I was really looking forward to it."
    r "I’m sorry I couldn’t stay any longer."
    o "Wait...Rin. Hold on."

    scene otohadinner29
    with dissolve

    r "I’ll call you later, Sensei."
    o "Hey! I said hold on!"
    r "For what?"
    o "I..."
    o "I don’t know."
    r "Well, let me know when you do."

    scene black
    with dissolve2

    "Rin grabs her bag from underneath the table."
    "The scent of vanilla bean vanishes with her."

    scene otohadinner30
    with dissolve2
    play music "thingsthathurt.mp3"

    ni "What the fuck are you waiting for?! Chase after her! "
    o "I-"
    ni "Don’t tell {i}me,{/i} idiot! Tell her! She’s the one who needs to hear it!"
    o "I..."
    o "Okay. Yeah."
    o "I’ll be right back!"

    scene otohadinner31
    with dissolve

    "Otoha runs out of the restaurant, nearly knocking over the waiter who I assume is carrying everything we ordered."
    "I breathe a sigh of relief for the expensive dinner Niki is about to buy for me-"
    "And another sigh for a girl who keeps gluing her heart to the wrong things."

    ni "Girls can be so fucking dumb sometimes. Just {i}talk.{/i} It’s that easy."
    s "Some things aren’t easy to talk about, I guess."
    ni "Ugh. Whatever. Guess it’ll have to just be a single date."
    s "Uh-oh. What happens if we fall in love?"
    ni "Not funny."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohadinner32
    with dissolve

    o "Yo! Hold on!"
    r "Oh, you followed me out. What a surprise."
    o "I’m sorry, okay?!"
    o "It's just...this is all still new to me!"
    r "You mean dating in general? Or dating a girl?"

    scene otohadinner33
    with dissolve

    o "Both..."
    o "Would it be easier to tell my parents about us if you were a boy? Yes. Absolutely. "
    o "What’s normal for {i}us{/i} isn’t what’s normal for everyone else. But that doesn’t mean I don’t {i}like{/i} it."
    o "You think I would have willingly hung out with our teacher all day if we {i}weren’t{/i} going on this double date thing tonight?"
    r "I know you’d find it {i}easier{/i}. "

    scene otohadinner34
    with dissolve

    o "That’s not what I meant..."
    o "I just..."
    o "My parents aren’t like yours. {i}Most{/i} parents aren’t like yours."
    o "And we can’t just pretend they are because that’s more...convenient for us."
    r "Are you embarrassed to be dating a girl, Otoha?"
    o "That’s not-"
    r "Just give me a yes or no answer, Otoha."

    scene otohadinner35
    with dissolve

    o "..."
    r "..."
    o "Yes."
    o "I am."
    r "I’m so fucking stupid."
    o "You’re not, Rin..."
    o "You didn’t do anything wrong."
    r "Yeah, well..."
    r "That’s not entirely true either."

    scene otohadinner36
    with dissolve

    o "What?"
    r "..."
    o "What is that supposed to mean?"
    r "It {i}means{/i} that you’re not the only one who’s been hiding something for the sake of not making the other person uncomfortable."
    o "What...have you been hiding?"
    r "Take my shirt off and you’ll find out."
    r "Unless you’re too embarrassed to undress your girlfriend, of course."

    scene otohadinner37
    with dissolve

    o "Rin..."
    o "For real?..."
    r "You came clean about your thing, so it’s only fair that I come clean about mine."
    o "Stop walking."
    r "I don’t want to look at you."
    o "Why?"
    r "Because you’re too cute and it’s annoying and I won’t be able to be mad anymore."
    o "Stop walking, Rin."
    r "..."
    r "Fine. But we aren’t done fighting yet."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene otohadinner38
    with dissolve2

    o "Why didn’t you tell me?..."
    r "Why didn’t you tell {i}me{/i} that you haven’t fully accepted your sexuality yet?"
    r "Unless you’re treating this like some sort of phase and that...you don’t {i}actually{/i} like me at all."
    o "You want to save the cutting thing for later? Fine."
    o "I wouldn’t treat this like a phase, Rin."
    o "I might be an asshole, but I'm not {i}that{/i} much of an asshole."
    r "Good. Because this definitely isn’t a phase for me, Otoha. "
    r "I like girls. I like {i}you.{/i} And yeah, there are people out there who think that’s disgusting or wrong or sinful or...do you think I haven’t heard all of that before?"
    r "I’m not even fully out yet because I can understand all of that. There are still plenty of people who don’t know that I’m bisexual."
    o "Rin, everyone knows you’re bisexual. You’re horrible at hiding it. But they don’t look at you any differently."
    o "In fact, {i}who{/i} do you care about that has looked at you differently for this? "
    o "Because the two people who raised me not accepting it seems like a pretty good reason for me to be wary about just announcing it to everyone."

    scene otohadinner39
    with dissolve

    r "I am {i}not{/i} a part of {i}everyone,{/i} Otoha! I am your {i}girlfriend!{/i} Whether you’re comfortable with that or not!"
    r "I need to know about things like this!"

    scene otohadinner40
    with dissolve

    o "And {i}I{/i} need to know when you’re fucking hurting yourself, Rin!"
    r "Then pay more attention..."

    scene otohadinner41
    with dissolve

    o "..."
    r "You’re always working. And I respect that. I really do."
    r "I just figured that, since I'm someone who’s apparently so bad at hiding things...my girlfriend would have maybe caught on about something being...wrong with me."
    o "There’s nothing “wrong” with you. And I will {i}try{/i} to pay more attention, but I don’t want you {i}trying{/i} to hide things like that from me."

    scene otohadinner42
    with dissolve

    r "Are {i}we{/i} even right together, Otoha?"
    r "Is {i}this{/i} right?"
    o "Why...wouldn’t it be?"
    r "Because you’re not comfortable being with another girl...and I’m too worried that I’ll wind up doing something that makes you think less of me."

    scene otohadinner43
    with dissolve

    o "It’s not that I’m uncomfortable! And I’m not going to think less of you for doing something like that!"
    o "I’m just overwhelmed, okay?! "
    o "I want my parents to accept us! {i}I{/i} want to accept us! I {i}like{/i} us! "
    o "I just need some more time getting adjusted, that’s all!"
    o "You’ve had your whole life to deal with these feelings, haven’t you? I’ve only had a few months."
    o "I’ve never felt this way about {i}anyone{/i} before, let alone another girl. So yeah, I’d be lying if I said it wasn’t embarrassing."
    o "But I don’t want to lie anymore. I want to try and make this work. But if you’re going to keep hurting yourself and not telling me about it, I-"

    scene otohadinner44
    with dissolve

    r "I never wanted to hide it from you..."
    r "I was just afraid you wouldn’t like me anymore..."
    o "Don’t be afraid of that."
    o "Please."

    scene otohadinner45
    with dissolve

    r "{i}*Sniff*{/i}"
    r "Are we breaking up?"
    o "Is that what you want?"
    r "{i}*Sniff*{/i}"
    r "No..."

    scene otohadinner46
    with dissolve

    o "Me neither."
    r "Are you going to keep me hidden forever?"
    o "Of course not..."
    o "Just..."
    o "For a little while longer. While I figure things out."
    r "{i}*Sniff*{/i}"
    o "Do you have any other demands, my queen?"
    r "{i}*Sniff*{/i}"
    o "..."
    r "Can we make out?"
    o "..."
    r "..."
    o "Like..."
    o "Like, literally right now?"
    r "{i}*Sniff*{/i}"
    r "Only if you want to..."
    o "..."
    o "Sure, Rin."
    o "We can make out."

    scene otohadinner47
    with dissolve2

    o "Mnh~ Mm..."
    r "Chu...hmnn...mm...Otoha..."
    o "Mn~ Mmm...Rin..."

    scene otohadinner48
    with dissolve

    ni "Are you two done making u- oh. "
    ni "They are making {i}out.{/i}"
    s "They certainly are."
    ni "Girls are fucking exhausting. I’m glad I never dated one."
    s "They certainly are."
    ni "..."
    s "..."

    scene otohadinner49
    with dissolve

    ni "..."
    s "..."
    ni "Wanna go make out in the bathroom?"
    s "I certainly do."

    scene black
    with dissolve2

    "And everyone lived happily ever after..."

    $ renpy.end_replay()
    $ otohadorm10p2 = True
    $ otoha_love += 1
    $ niki_lust += 1
    $ niki_love += 1
    $ rin_love += 1
    stop music fadeout 10.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "{i}Niki’s affection has increased to [niki_love]!{/i}"
    "{i}Niki’s lust has increased to [niki_lust]!{/i}"
    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label otohaspecial15p1:
...
```

## Code that triggers this event

File: (install folder)\game\OtohaEvents.rpy

Code:
```python
...
o "Oh, please. Me overworking myself is {i}way{/i} different from whatever the hell is going on in Nodoka’s super-brain."
    o "I’ve got this under control, man. It’ll all be worth it in the long run."
    s "Famous last words, Otoha."
    o "What? What are you talking about?"
    s "Just that you should know more about the dangers of what you’re doing. Plenty of people have thought the same way only to end up in boxes."

    scene otohaworkshard19
    with dissolve

    o "You’re worrying about the wrong person, Sensei. I’ve got way too much shit to do. I don’t have time to die."
    s "Well, I hope that’s true. Because I kind of like you."

    scene otohaworkshard20
    with dissolve

    o "Huh?..."
    s "And I mean that in the least creepy way possible."
    o "Yeah. That didn’t sound creepy at all that time. That’s why I probably look so shocked."
    o "Like, it sounded like you actually being a decent person for once."
    o "I’m not really sure what to say."
    s "You can say you like me too. Nodoka is too out of it to remember, so it will be like no one ever heard anything."

    scene otohaworkshard21
    with dissolve

    o "I don’t...{i}not{/i} like you."
    s "I’ll take the double negative. I know what it really means."

    scene otohaworkshard22
    with dissolve

    o "You know...I know we’ve joked about it before. But today, you really {i}have{/i} felt kind of like an older brother or something to me."
    o "Annoying, yeah. And way too close to my personal space. But mostly full of advice and actually like, genuinely looking out for me. Kind of."
    o "I’m sure there are some horrible intentions mixed in that are the cause of that, but I’m going to ignore them for the time being since it’s actually been pretty nice so far."
    o "I always wanted someone like that. Someone to kind of...counterbalance how suffocated I always felt by my parents. Someone who would, at the very least, understand that..."
    o "And I’m not saying you do just yet.. But you’re closer to it than most people. That’s nice."

    if bonus == True:
        "I’m glad she’s able to look past my “horrible intentions,” because the way Otoha is blushing right now is certainly reinforcing them."
        "It’s no time to dwell on the sexual fantasies of a surrogate little sister, though. Not when it’s becoming clear that whatever hinges keep Otoha functional are slowly coming unscrewed."
        "It’s possible you might be thinking that {i}I’m{/i} thinking too deeply into this, but I’d like you to consider the countless other cases in which creative minds rotted from the inside out in pursuit of...anything."
        "There’s that old saying “A mind is a terrible thing to waste.”"
        "But, if that’s the case- why do we waste so many?"
        "And why is the beauty created by those minds only truly appreciated once they’re lowered into the soil?"
        "Some things can be beautiful above ground."
        "Before me is one of them."

    s "Just take it easy. Don’t get lost in whatever you’re doing and I’m sure everything will turn out...okay-ish."

    scene otohaworkshard23
    with dissolve

    o "Okay-ish is all I ask. So thanks."
    s "Also, if you ever want to call me “Big bro” or “Onii-chan” I am more than okay with it."
    o "I’ll think about it."
    s "That’s honestly more than I thought I would get. So thank {i}you{/i}, Otoha."

    scene otohaworkshard24
    with dissolve

    o "No problem, man. Just don’t go snooping around in my closet and always knock before coming into the room. We’ve gotta set some ground rules if we really want this to work out."
    s "I think this is the part where I tell some joke about having to check your closet to make sure you’re growing properly."
    o "Rad. Cause that means it’s also the time for me to punch you in the face and send you flying into orbit."
    s "At least I’ll die happy."

    scene black
    with dissolve2

    "Otoha and I spend the next hour or so hanging out in her room, swapping back and forth between casual conversation and observing her roommate’s manic episode."
    "And while I’d like to say that I’m glad she used this opportunity to take her mind off of working, I caught her jotting several things into several notebooks while we waited for night to come."
    "I guess some people just can’t stop even when you make it incredibly apparent that they should."
    "More power to her, I guess."
    "If Otoha thinks she’s able to just avoid being overwhelmed for the rest of eternity, she has every right to try and prove that."
    "But-"
    "That also gives us (Or just me, I guess) the right to tell her “I told you so” when she can’t do it anymore."
    "That day will most assuredly come. And, when it does, I’ll be somewhere beside her."
    "Close, but not too close."
    "Probably going through her closet."

    play sound "phonebeep.wav"

    o "Oh. Niki’s choreography thing just ended. She wants to know if we’re ready to head over to the restaurant yet."
    s "Is that what we’re doing? I remember agreeing to the double date thing, but I didn’t know we already chose a place."
    o "I guess so. It’s close-ish to the cafe, too, so Rin can probably come straight over after getting out of work in an hour."
    s "Are you going to be able to stay away from your ten thousand notebooks for the rest of the night?"
    o "Yeah. I’ve got a pocket-sized one that I keep on me at all times in case inspiration strikes while my babies are away."
    s "You have a problem, Otoha."
    o "Don’t we all, man? Don’t we all..."

    $ renpy.end_replay()
    $ otohadorm10 = True
    $ otoha_love += 2
    stop music fadeout 25.0

    "{i}Otoha’s affection has increased to [otoha_love]!{/i}"
    "........."
    "......"
    "..."

    jump otohadorm10p2
...
```