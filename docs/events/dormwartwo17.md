# Popping Off
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwartwo17&go=Go)


Part of event chain [World of Lines](./dormwartwo16.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: dormwartwo17
* Group: Main
* Triggered by label: dormwartwo16

## Event code
File: \game\chap3.rpy
Code:
```python
...
label dormwartwo17:
    scene secondcostumecontest1
    with dissolve2
    play music "letsfuckingo.mp3"

    w "I will stop by the hardware store tomorrow."
    os "You’re damn right you will."
    f "Hey, how did the contest go?"
    r "Futaba, do you think we’ve been growing distant at all lately?"

    scene secondcostumecontest2
    with dissolve

    f "Well, I guess that answers {i}that{/i} question."
    r "Seriously, though. If somebody like...I don’t know- {i}Uta{/i} came along and suddenly knew more about you than I did, how would that make you feel?"
    f "Umm...shocked. I haven’t really spoken much to Uta. Especially not compared to somebody like you or Nodoka."
    f "Did Yasu...somehow beat you at the Sensei trivia contest thing?"

    scene secondcostumecontest3
    with dissolve

    r "Yes! But before you tell me it’s not a big deal and that it’s just a stupid contest and that it doesn’t matter to me who puts what in my vagina, please understand that I am very sensitive about this!"
    f "Of course it’s a big deal. I know how much Sensei means to you and-"

    scene secondcostumecontest4
    with dissolve

    f "Wait, what was that last part?"
    r "I’m very sensitive!"
    f "The...other last...You know what? That doesn’t matter. "
    f "I’m not going to hold it against you for getting upset about this. But I don’t think just losing a contest is enough to make your relationship with Sensei...devoid of all meaning."

    scene secondcostumecontest5
    with dissolve

    r "It’s not {i}just{/i} that, though. We had a whole talk recently about how the two of us aren’t as close as we once were, and it’s really starting to get to me the more I think about it."
    f "Then why not just...spend more time with him?"
    r "Because I can’t even look at him without Otoha getting all self-conscious and thinking she’s just the latest trend for me. And I can’t ignore Sensei because he’ll just think I don’t care anymore."
    f "I think Sensei is smarter than that, Rin."
    r "Yeah, well, you probably know more about him than I do at this point too. So I’ll just have to take your word for it."

    scene secondcostumecontest6
    with dissolve

    f "I’m assuming this...unexpected turn of events also has something to do with the fact that...Otoha didn’t come back with you?"
    r "You assume correctly. Now, please excuse me while I drown my worries away with thirty-seven Shirley Temples at the bar. "
    f "How about I join you and...we can talk it out while I also prevent you from getting diabetes?"
    r "Thanks, Futaba. No one else ever tries to prevent me from getting diabetes."
    f "That’s...what I’m here for."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene secondcostumecontest7
    with dissolve

    sa "Hey...do you...need any help with anything?..."
    sar "Oh, Sana! You’re back. Did you have fun at church? "

    scene secondcostumecontest8
    with dissolve

    sa "Uhh...no..."
    sa "In fact...I kind of wish I just...stayed here instead..."
    sar "Yeah. That about sums up how I felt the one time I went to a church too."
    sar "You don’t have to worry about helping out, though. Go have fun with all of your friends. I’ve got Haruka and Kaori helping out tonight. And Yuki’s starting to get pretty good at this."

    scene secondcostumecontest9
    with dissolve

    sa "Are you sure? There are a lot of people here."
    sar "And almost half of them are paying. Isn’t that crazy? It’s a major improvement from last year when I was just giving stuff away."
    sa "I mean...yeah...yeah, that...wasn’t really a good business move. "
    sa "And neither was...giving alcohol to high school girls, but...at this rate of...self-improvement, you...might even stop doing that as well..."
    sar "Maybe! Depends on profits as I’m currently making back what I lost on you earlier."
    sa "Please don’t...bet on me anymore..."
    sar "You are my daughter. It’s not like I’m going to bet {i}against{/i} you."

    if sarabjwin == True:
        scene secondcostumecontest10
        with dissolve

        sar "Besides, I already made up for the point you lost earlier. So it’s like nobody ever lost at all!"
        sa "What? How?"
        sar "Oh, you know what? I’ll be right back. I have to talk to Haruka about something."
        sa "What?"

        scene black
        with dissolve2

        sa "Mom?"
        sa "How?"

    else:
        sa "You know you can just...not participate in any betting at all...right?..."

        scene secondcostumecontest10
        with dissolve

        sar "And stay right above the poverty line forever? Not a chance. Mommy’s gonna hit it rich. And if Mommy needs to stake all of her money on her beautiful daughter to do that, that’s what Mommy is going to do."
        sa "Can you...stop calling yourself that, please?...It makes me uncomfortable..."

        scene black
        with dissolve

        sar "I’ll stop when you turn 40. Until then, I’m not changing a thing."
        sa "Ugh..."

    "........."
    "......"
    "..."

    scene secondcostumecontest11
    with dissolve2

    ima "Jeez. Shit’s really poppin’ off in here and all {i}I{/i} got to do over the last two hours is stand outside, watch some lesbians fight, then ride a bus."
    n "Sounds like a normal day in LA to me."

    scene secondcostumecontest12
    with dissolve

    ima "The fuck you know about LA? And how come you never invited me?"
    a "Sensei...I’m sorry. I have lost the scavenger hunt and failed at winning your affection. And to Noriko, no less."

    scene secondcostumecontest13
    with dissolve

    n "{i}Technically{/i} you lost to Kirin. "
    a "Do you think you’re helping? Because that makes it even worse."
    ima "Mind if I mingle for a bit before kicking off the costume contest? Wanna touch base with the rest of the girl gang before you choose which mini cosplayer you’d rather bang."

    scene secondcostumecontest14
    with dissolve

    a "I’d like to take this opportunity to speak on behalf of my uncle in saying that he has no interest in such a thing."
    s "I’d like to take this opportunity to speak on behalf of myself to say that I do, but only under the most legal of circumstances and that is simply something I will not budge on. Thank you."
    n "Can I join your girl gang, Imani? "
    ima "Depends. You willing to perform the blood oath?"
    n "Of course. I was born to perform blood oaths."
    ima "What a strange purpose to have been put on this planet for."
    ima "But...even if, I’m probably gonna say no. Wakana is in the gang and I’m pretty sure she doesn’t want you around her based on the...well, the fact that she kicked you out of her class."
    ima "Also, if you join, Kirin is going to want to join and that would obviously turn into a whole thing because of her-"
    n "Innate and unflappable desire to have sex with you?"
    ima "Bingo."
    a "I say we just kill her."

    scene secondcostumecontest15
    with dissolve

    a "It would be for the best at this point. Miss Imai and Sensei would be protected from her advances, I’d wind up getting the win for the scavenger hunt by default, and Noriko..."
    a "I don’t know. Noriko can have her clothes or something. That would be easy."

    scene secondcostumecontest16
    with dissolve

    n "She {i}does{/i} have a bra I like. And it {i}would{/i} be easy."
    ima "Fine. If that’s what it takes for me to get my drink on, you guys can kill Kirin. But if the cops ask, I said no. Capiche?"
    a "I’ll call my people once the music dies down. I’m glad we were able to reach an understanding."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene secondcostumecontest17
    with dissolve2

    ri "Rin! Hi! It’s me! Not your mom! This looks like fifty feet, right?"
    r "Chika already knows you’re my mom, {i}Mom.{/i} There’s no point in hiding it anymore."
    r "Also, here’s a question- why are you two together?"

    if chikalust25 == True:
        r "And why does Chika smell different?"

        scene secondcostumecontest18
        with dissolve

        c "Hahah...beats me. "
        ri "You remember how she smells? "
        r "Yes. But only because her locker was next to mine for a long time. Not because I used to sniff her hair when she wasn’t looking or anything. That would be weird."
        ri "I don’t think it would be that weird."
        c "No...it would be pretty weird."

    else:
        r "And why are you dressed in spandex? Aren’t you too old for that?"

        scene secondcostumecontest19
        with dissolve

        ri "You’re never too old for spandex!"
        r "That is just demonstrably untrue."

    scene secondcostumecontest20
    with dissolve

    c "Anyway, I just figured I’d hang out with your mom while I wait for you and Otoha to get back since...Yumi obviously isn’t coming. "
    r "I...do not know how I feel about that."
    c "Where is she, by the way? Otoha, I mean. I think our class is going to start casting their votes for the popularity poll soon. "
    ri "The adults, too. I promised Chika I’d vote for her if she didn’t tell anybody she knew where I was living right now. Which definitely isn’t your room."
    c "I came by looking for band recommendations the other day since I want to try listening to more of the stuff you guys do. "
    r "Mom, you have to vote for my girlfriend. It wouldn’t be right if you voted for Chika."
    ri "But your girlfriend isn’t even here."
    r "Yeah, because we got into a fight."

    scene secondcostumecontest21
    with dissolve

    c "You did? Over what? What happened?"
    r "I don’t really want to talk about it right now. I just want to hang out and take my mind off of it."

    scene secondcostumecontest22
    with dissolve

    ri "Hey! I can help with that! I’m basically an expert at pretending failing relationships are still going strong!"
    r "Thanks, Mom. That’s exactly what I wanted to hear."
    ri "I figured! Great news, right?!"
    c "Hey, cheer up. I’m sure things will go back to normal in no time at all."

    scene secondcostumecontest23
    with dissolve

    c "Besides, you’ll have {i}me{/i} in the meantime. And I’m not just saying that because I want you to vote for me. {size=15}But you should totally vote for me.{/size}"
    r "Uh...th...thank you?"
    ri "Man, I wish I had a friend who was that caring. Or any friends at all. Or a girlfriend. Or a life."
    ri "Or anything, really. "
    ri "But hey, at least I’ve got a beer."

    scene secondcostumecontest24
    with dissolve

    c "Just don’t drink too much or you’ll have even more problems on your hands. Pretty much everything is better in moderation with...only one exception I can think of but can’t talk about."
    ri "Sour Skittles? "
    c "Yes, Rika. Exactly that."
    ri "Well said, Chika. I knew I-"

    scene secondcostumecontest25
    with dissolve

    ri "Ooh! Holy shit! Our names rhyme! How cool is that?!"
    c "Really cool! The...coolest thing I’ve heard all night."
    ri "Right? Who even needs Otoha when we’ve got the Rika-Chika duo? She’d only drag us down anyway."
    r "Chika, can you maybe, like...move your- "

    scene secondcostumecontest26
    with dissolve

    c "That’s not true at all. Rin and Otoha are actually really great together. You’ve just gotta get to know her a little better."
    ri "Yeah, I’ve really only seen her the one time. But meanwhile, I know basically all there is to know about you after years of listening to Rin rave on and on and on and on..."

    scene secondcostumecontest27
    with dissolve

    c "Oh-ho-ho?"
    r "Mom...can you please not?"
    ri "Oh, it’s no big deal! The Chika era is behind you! Which means I can talk about that picture you kept of her on your vanity throughout all of middle school and no one will think it’s weird!"

    scene secondcostumecontest28
    with dissolve

    r "Mom!"
    c "Oh my God! That is freaking adorable!"
    ri "Right? You should have seen her blushing every time she said that you guys were just friends. She was so cute."
    r "Cut it out! "
    ri "No, no, no. Just another minute. I’m reminiscing. "

    scene secondcostumecontest29
    with dissolve

    c "I can’t believe you kept it in for so long if your crush was really that huge. Were you waiting for a sign or something? You could have just told me."
    ri "Yeah. Who knows what would have happened if she found out a little earlier? You might even be with Chika instead of Otoha right now."

    scene secondcostumecontest30
    with dissolve

    c "Heheh! Maybe! We’d make a cute couple, right? Just look at us."
    ri "Totally. And you’re way more like the girls Rin usually-"

    scene secondcostumecontest31
    with dissolve

    ri "Uh-oh. I went too far, didn’t I?"
    c "Huh?"
    r "Yes...you did."

    scene secondcostumecontest32
    with dissolve

    c "Hey, I’m sorry. We were just messing around. I didn’t think that would hurt you."

    scene secondcostumecontest33
    with dissolve

    r "Yeah, no one seems to have any idea what hurts me tonight. So I’m just going to go home as well."
    c "Rin, no. Stay with me. We can have fun together and forget things ever got weird."

    scene secondcostumecontest34
    with dissolve

    r "Yeah, maybe you can! But you’re not the one being pulled in three different directions right now, Chika!"
    r "All this is going to do is confuse me! "
    c "Rin-"
    r "Let go!"

    play sound "static.mp3"
    scene secondcostumecontest35
    with flash
    stop sound

    c "Rin! Come on!"
    r "No! I’m going home to my prude of a girlfriend and yelling at her again! But thanks a lot to both of you for making tonight even worse than it already was!"
    ri "Ahhh! Why do I always ruin everything?! Who put this stupid brain inside of my body?!"
    h "What happened with Rin? What’s going on?"

    scene secondcostumecontest36
    with dissolve

    ri "What happened is I am a failure of a mother who-"

    scene secondcostumecontest37
    with dissolve

    ri "Wait a minute. You’re that girl from the convenience store."
    h "Haruka. Rin’s boss. "
    h "I kind of assumed you were her mother based on...well, everything about you...but I figured we’d wind up meeting again soon enough."
    h "I didn’t think it would be like this, though."

    scene secondcostumecontest38
    with dissolve

    ri "Ugh...me neither. But I also didn’t think I was ever going to see you again, so we’re not really the same."
    ri "What should I do, Haruka? I keep making things worse for Rin and all I want to do is make her happy."
    h "For now, I’d probably just...give her some time. "
    h "Chasing after her will only make her run that much faster."

    scene secondcostumecontest39
    with fade

    ima "Hola, compadres! Ignoring the fact that Rika is too busy being a trainwreck to join us at the counter, I’d like to extend a hearty hello to those of you who were stable enough to make it tonight!"
    os "Just {i}barely{i} made it, I’ll add."
    ima "But boy am I glad you did because this is a sight I would not mind waking up to every day for the rest of my life."

    scene secondcostumecontest40
    with dissolve

    os "Your surname isn’t “Takeda,” is it?"
    ima "I sure hope not or I am absolutely {i}fucked{/i} when it comes to my taxes."
    w "Please excuse my partner for what I can sense is a rather angry expression she’s currently making."
    w "Recent discussions may have implanted in her head the idea that I have been interested in sex with multiple women at the same time and, thus, she now likely believes I have enlisted you for that purpose."
    ima "Enlisted? Is that why I keep being excluded from threesomes? Because I’m not signing the appropriate forms?"

    scene secondcostumecontest41
    with dissolve

    os "Despite what Wakana says and...what my expression {i}may{/i} have said...I’m not angry. Just tired. And also extremely embarrassed to be seen wearing this in public."
    ima "Why? You’re hot as hell."
    w "Amen. "
    os "Thanks, but there’s no way this sort of thing fits me."
    os "I’m sure it comes as no surprise given my relationship, but I’ve always loved the style on other people. When it comes to myself, though...it just feels wrong. You know? "
    ima "..."
    os "Imani?"
    ima "Hm? Sorry. Did you say something? I was thinking about our threesome later."

    scene secondcostumecontest42
    with dissolve

    os "Okay. {i}Now{/i} I’m angry."

    play sound "static.mp3"
    scene secondcostumecontest43 with flash
    stop sound

    ki "Woah, Miku. What’s going on? Is it the noise? Do you need to step outside?"

    scene secondcostumecontest44
    with dissolve

    ki "Makoto didn’t leave yet, did she? Maybe she-"
    mi "I can’t do it. I can’t go up there."

    scene secondcostumecontest43
    with dissolve

    ki "So...it’s not the noise? And what do you mean you can’t go up there? Why not? "
    mi "This ain’t me. I ain’t cute...or stylish. Or pretty. And I got no idea what even half of what I’ve been sayin’ all weekend means."
    mi "They’re gonna see through me. See that I don’t know how to do makeup or dress nice or talk without droppin’ letters and that I ain’t like them. I ain’t anything like them."
    ki "Okay. Yeah. I get what you’re saying, but...counterpoint. Do you think Uta is {i}actually{/i} a kunoichi?"

    scene secondcostumecontest45
    with dissolve

    mi "Uhh...no?..."
    ki "Remember what you’re doing. This is a {i}costume{/i} contest. No one is expecting you to actually {i}be{/i} this person."
    ki "And stop biting your nails. You’re going to fuck them up."
    mi "But...But I {i}have{/i} been this person since Friday. Why’s it all startin’ to crack now? "
    ki "Probably because Miku Maruyama hasn’t existed for 48 hours and she’s trying to break through again."
    ki "You spent too long being someone else and that’s getting to you. But there’s nothing wrong with being someone else...and doing that doesn’t mean the {i}other{/i} you is gone forever."
    ki "It just means you’ve gotta get better at controlling it so it takes longer for you to break next time."
    mi "Why do I...have to break at all? Why can’t I just be who I wanna be?"
    ki "You can. But you wouldn’t have chosen such a hard costume and role if that's what you really wanted."

    scene secondcostumecontest46
    with dissolve

    mi "I can’t do it...I can’t do it..."
    u "Miku, what’s wrong?! We’re gonna be starting any second now."
    mi "Do it without me. I can’t. I’m gonna lose. There ain’t no way."
    i "Textbook panic attack. "

    scene secondcostumecontest47
    with dissolve

    ki "Gee, thanks Io. There’s no way any of us would have been able to figure that out on our own."
    i "Do you want my help or not? Because I’ve got pills for this and an excuse to get me the fuck out of here right now would be great."
    ki "You really think you’re going to be able to make it to the dorm and back in the next five minutes?"
    i "No. But I {i}would{/i} be able to make it to the coin locker around the corner."
    u "I made Io lock her pills up so she wouldn’t keep taking them all night long."
    i "And this is the perfect example of why I said that would be a bad idea. But we can argue about that later. How much does she weigh?"
    ki "She doesn’t need fucking pills! She needs to breathe. "
    i "She needs {i}both.{/i} But hey, if you want to want to risk throwing her up on that stage and making everything ten times worse, be my guest."

    scene secondcostumecontest48
    with dissolve

    ki "Miku, what do you think? Do you want to try and tough this out? Or do you want some of Io’s medication?"
    mi "M...Medication?"
    mi "I...I don’t know...I don’t usually take that kinda stuff..."
    mi "Is it safe?..."
    i "It’s Valium so side effects would include dizziness...drowsiness...nausea...memory loss...pretty much all the standard shit. But that’s all I’ve got for panic attacks in the locker. "
    i "Anything else, I’d need to go back home."
    mi "Fine. Yeah. Go. "
    ki "Are you {i}sure?{/i}"
    mi "No. "
    i "Just think of it like a painkiller but...for your brain. You’ve taken painkillers before, right?"
    mi "Yeah, but..."

    scene secondcostumecontest49
    with dissolve

    ima "Attention, everyone! And let me start by saying thank you all very much for coming to the final stretch of the Dorm Wars!"
    u "Miss Imai! We-"
    mi "Don’t. Don’t say anything. Attention is bad. Keep it away."
    i "Yes or no? Final answer."
    ki "Are you up first, Uta? Or is Miku supposed to go?"
    u "I think Miku, but..."

    scene secondcostumecontest50
    with dissolve

    u "I’ll figure out a way to go first! And I’ll stall for as long as it takes."
    i "Miku. Yes or no?"
    mi "Yes. Yes yes yes. Go. Thank you. "
    mi "Just painkillers for your brain. That sounds good. Really good."
    ki "Just hang in there, okay? "
    ki "It’ll all be over soon."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ dormwartwo17 = True
    stop music fadeout 10.0

    "........."
    "......"
    "..."

    jump dormwartwo18

label dormwartwo18:
...
```

## Code that triggers this event
File: \game\chap3.rpy
Code:
```python
...
with dissolve

    os "Britney Spears."
    w "Right, right. I forgot there was a time in your life where you weren’t fully dedicated to being swallowed by the darkness that is Wakana Watabe."

    scene outsidethechurch25
    with dissolve

    w "Or at least being {i}licked{/i} by her."
    os "Not again. You’ve {i}licked{/i} me to completion five times today and are the reason I am currently reapplying my makeup in the first place. Please contain yourself. We have plans."
    w "But I can only have sex with Gothsako one day out of every year. I need to make it count."
    os "I already told you I’d be more than willing to do this on a weekly basis. {i}Just not right before we go out.{/i}"
    w "My darling, doing this on a weekly basis would cause it to lose its charm. I like having something to look forward to for the holidays."
    w "Which is why I’m particularly excited for my upcoming {i}excursions{/i} with your Christmas elf variant. Remind me to cover our apartment in mistletoe, please."
    os "You don’t need me to remind you. What I have learned over the years is that there are only four shades of Wakana — sleep, sex, work, and interior design."
    os "The second I turn a blind eye to you, there will be mistletoe literally everywhere."
    w "You should be happy you’ve found yourself such a predictable woman. Many people love that sort of thing."

    scene outsidethechurch26
    with dissolve

    os "I’d be happier if you’d actually help me with this instead of watching me struggle while fixing your hair."
    w "Apologies, my sweet. But seeing as we have plans tonight, I can not allow my hair to be anything other than perfect."
    os "Why? Trying to impress someone?"
    w "Of course."

    scene outsidethechurch27
    with dissolve

    w "I did take the liberty of inviting Ms. Takeda, after all."
    os "You drive me insane."
    w "Don’t worry, my kitten. I’m willing to share her."
    os "Oh, are you now?"
    w "I can’t see why not. If anything, I welcome the challenge."
    w "My skills with one woman are quite exemplary, as I’m sure you’ve noticed. I wonder if they’d hold up with a second?"

    scene outsidethechurch28
    with dissolve

    os "Is that something you’re actually interested in?"
    w "Osako?"
    os "Threesomes, I mean."
    os "We’ve never really had that discussion before."
    w "My dear...you {i}are{/i} aware that I was just kidding, aren’t you?"
    os "Yeah, but like..."
    os "I mean, I’d {i}get it{/i} if that’s something you wanted to do. And if that will help with-"

    scene outsidethechurch29
    with dissolve

    w "Hah...this again?"
    os "I just want you to be happy, Wakana."

    scene outsidethechurch30
    with dissolve

    w "I {i}am{/i} happy, love. And I mean that from the bottom of my heart."
    os "There’s a “but” coming."
    w "{i}But...{/i}"
    os "Knew it."
    w "Do you know what would make me even {i}happier?{/i}"
    os "..."
    w "..."

    scene outsidethechurch31
    with dissolve

    os "Hah..."
    os "Bed or couch?"
    w "Both?"
    os "We only have time for one."
    w "Then..."
    w "Kitchen."
    os "Fine."
    os "But if you’re going to handcuff me to something, it can’t be the cabinet with our pots and pans in it. The handle is still loose from last time."
    w "It’s okay to break things. We’re adults."
    os "You know...sometimes, it really feels like all of the physical and stamina training I’ve endured my entire life was all to prepare me for {i}you.{/i}"
    w "And...would you change that if you could?"

    scene outsidethechurch32
    with dissolve

    os "Absolutely not."
    os "Let’s go break some cabinets."

    scene black
    with dissolve2
    stop music fadeout 7.0

    $ renpy.end_replay()
    $ dormwartwo16 = True

    "{i}Osako and Wakana’s mutual lust for one another has increased to 9473056713254!{/i}"
    "{i}First Floor: [dorm1war2points]\nSecond Floor: [dorm2war2points]{/i}"
    "........."
    "......"
    "..."
    "{i}About forty-five minutes later...{/i}"

    jump dormwartwo17
...
```