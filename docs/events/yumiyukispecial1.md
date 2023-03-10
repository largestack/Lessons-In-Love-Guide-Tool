# The Road to Recovery (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Dead in the Water](./yumichikaspecial1.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Chinami: Bad News Bears](./chinamidate30.md)
* [Wakana: Pseudonym](./wakanadate15.md)

## Event properties

* Id: yumiyukispecial1
* Group: Main
* Triggered by label: yumichikaspecial1
* Chain sources: yumichikaspecial1
* Chain sources path: yumichikaspecial1

## Official wiki page

[The Road to Recovery](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=yumiyukispecial1&go=Go) for more details.

## Event code

File: (install folder)\game\chap3.rpy

Code:
```python
...
label yumiyukispecial1:
    scene yukiyumibar1
    with fade
    play music "recovery.mp3"

    yu "Yo. "
    y "Wh...What the fuck are you doing here?!"
    yu "Got a call that the “princess” was back at the Yamaguchi place. Figured I’d drop by and see what sorta shit could’ve caused that."
    c "That’s not...your mom, is it?"
    y "It’s the bitch who used to be my mom. Ain’t had that role in a long fuckin’ time."
    yu "Hey, like it or not, I still carried you around for nine months. That’s gotta be worth something."
    y "Might’ve been if you hadn’t immediately forgotten me right afterwards. The fuck you want?"

    scene yukiyumibar2
    with fade

    yu "Chill. I already told you why I’m here. Also, who’s this? Since when do you talk to anyone without a dick?"
    c "Chika Chosokabe..."
    yu "Yuki Yamaguchi. Pleasure."
    y "Why the fuck are you even using that name still?"
    yu "Same reason as you, probably. It’s nice makin’ those fuckers at the gate bow for us, ain’t it? Makes you feel all important and shit."
    y "Just because I came back home doesn’t mean I’m suddenly just ready to talk to you again."
    yu "Gotcha. So your {i}dad{/i} is fine but I’m still meant to just stay the fuck away or whatever?"
    y "At least he didn’t spend every day shooting up heroin while I had to teach myself how to read."
    yu "Course not. He just bought it for me while using all of the time {i}I{/i} was lookin’ after you to snort coke with the boys."
    yu "Oh, sorry. Probably shouldn’t be sayin’ shit like that with your friend around. Ain’t really used to this."

    scene yukiyumibar3
    with dissolve

    c "It’s fine...I kind of know...most of Yumi’s past anyway, so."
    yu "Ahh. So then you must really fuckin’ hate me, huh?"
    c "You said it, not me."
    yu "Ha. Fair enough. "
    y "If you’re looking for money, good fucking luck. Turns out the whole testosterone shortage in Kumon-mi has made us fall upon “hard times,” whatever the fuck that means."
    yu "I’m good on money. Lot easier to save up when you ain’t blowin’ everything you’ve got on drugs, you know?"
    y "Just gonna make it easier to go out with a bang once you relapse again, you fucking piece of shit."
    yu "Damn. You gonna just let her talk to me like that, Chika?"
    c "It’s probably best if I just...don’t really get involved in this."
    yu "Yeah. An enemy of a friend is also...whatever the fuck the phrase is. You know what I’m tryin’ to say."
    y "Yuki-"
    yu "{i}Mom.{/i}"
    y "{i}Yuki,{/i} get the fuck out of here. Chika and I were in the middle of shit and I don’t wanna fuckin’ deal with you anyway. "
    yu "Not even if I buy you dinner?"

    scene yukiyumibar4
    with dissolve

    y "Dinner? Really? You realize I didn’t come here to plan a fucking family reunion, right? I’m just trying to disappear for a little while."
    yu "Well there ain’t nobody better to learn the art of disappearing from than your absentee mother, right?"
    c "My dad would probably be better. He’s never come back around to ask {i}me{/i} out to dinner."
    yu "Ha! I like this girl. Also, sorry about your dad. Sounds like a prick."

    scene yukiyumibar5
    with dissolve

    y "You ain’t helping."
    c "I don’t want to help. I think you should go with her."
    y "Excuse me?"
    c "Yeah. You won’t talk to me because you’re afraid of fucking up our friendship or whatever. But you don’t give a shit about losing your mom {i}at all.{/i}"
    y "I ain’t gonna air out my worries to someone who would pawn ‘em off for a bag of dope."
    yu "Not many people lookin’ to buy teenage drama. Can’t imagine I’d get much for whatever those “worries” of yours may be."
    yu "Think of it as a celebration dinner. "

    scene yukiyumibar6
    with dissolve

    y "The fuck are we celebrating? The fact that I got suspended for beating the living shit out of some girl?"
    yu "Yeah. Exactly. "

    scene yukiyumibar7
    with dissolve

    y "Wait, really?"
    yu "Yeah. Sounds like you really fucked her up. Bitch probably had it coming. "
    yu "You might be a temperamental brat but you’re still my daughter and we got good judgement when it comes to shit like that. Everything else, though? Not so much."
    y "You ain’t, like...ashamed of me or some shit?"
    yu "Fuck would I be ashamed for? You have any idea how many people {i}I{/i} fucked up when I was your age?"
    c "See, Yumi? Talking to her might not be that bad if you two can hold yourself back from insulting each other every opportunity you get."

    scene yukiyumibar8
    with dissolve

    y "Not gonna lie, that sounds hard as shit. "
    c "It probably will be. It’s the first time you two will actually be {i}talking{/i} in...how long?"
    yu "Long fuckin’ time."
    c "You know what I’d give to be able to talk to my mom again, Yumi? "
    y "Yeah, but your mom wasn’t a fucking crackhead."
    c "Good point. But still, if {i}I{/i} can’t do anything for you...maybe she can."

    scene yukiyumibar9
    with dissolve

    c "Besides, maybe you’ll even get a refresher on exactly what you {i}don’t{/i} want to be? "
    c "Seems like it might be good to get a little wake up call on that front after hearing that you’re tempted to just...throw everything away."
    yu "You talkin’ shit, Chika Chosokabe?"
    c "Bitch, I will fuck you up."
    yu "Ha! Yumi, this girl’s even more of a firecracker than you are. Keep her close, got it?"
    y "If I agree to this whole...dinner thing...for {i}Chika,{/i} not for you...how do I know you ain’t gonna just make me feel like shit the whole time?"
    yu "How ‘bout this? I do somethin’ to piss you off...you get to punch me in the mouth."
    y "Every time?"
    yu "Every time. And I won’t even fight back."
    y "I can work with that."
    c "I don’t really agree with that...methodology, but I guess it fits the two of you pretty well."
    y "Where are we going?"
    yu "Depends. You drink?"
    y "Do you even know how old I am?"
    yu "Do you know how old {i}I{/i} am?"
    y "Fucking old. Surprised you’re still breathing, to be honest."
    yu "Heh, same here. Guess we can hit up a dive or something. Either drink or don’t, I don’t give a shit. Will pick a place with food, though."
    yu "You coming too, Chika?"

    scene yukiyumibar10
    with dissolve

    c "Me? Oh, no. I think this should be a thing for you two. I should probably start heading home now anyway. Another friend of mine and my teacher are actually babysitting my sister for me at the moment."
    yu "Same teacher as Yumi’s? Tall guy? Glasses?"
    c "Yeah. You know him?"
    yu "Yeah. Saw my tits not that long ago."

    scene yukiyumibar11
    with dissolve

    c "Excuse me?"
    yu "Relax. Ain’t like I wanted to show him. Just kinda happened. Guy seems like he likes ‘em a little younger anyway."
    c "Watch your fucking step, Yuki. "
    yu "Damn. You too? Dude’s a straight up player, huh?"
    y "We gonna sit here talkin’ about my douchebag ex-teacher all day? Or are you gonna get me some fucking food already?"
    yu "Aight, aight. We can go. Only thing is I’ve just got my bike, so you’re probably gonna have to hang on to me if you don’t wanna fall off and die."
    yu "Think you can give your mom a hug without trying to kill her?"
    y "I think I’ll just hang onto the bike instead."

    scene black
    with dissolve2

    ".........."
    "......"
    "..."

    scene yukiyumibar12
    with dissolve2

    yu "..."
    y "..."
    yu "..."
    y "..."
    yu "Well this is fuckin’ awkward, ain’t it?"
    y "Place is grimy as shit. Can barely even breathe with all the smoke in here. Fits you well."

    scene yukiyumibar13
    with dissolve

    yu "Yeah. I really lucked out, huh? Just found out about it the other day. Might just become a regular."
    y "This ain’t the bar you work at? Remember hearin’ somethin’ like that."
    yu "Nah. Place I’m at’s a little nicer than this. Quiet. Ain’t really anything like me. "
    yu "Gotta put on this ridiculous get-up and everything. Can’t even wear my own fuckin’ clothes."
    y "Sounds like a nightmare."

    scene yukiyumibar14
    with dissolve

    yu "Ain’t that bad, all things considered. Job’s a job. Least I ain’t out on the streets anymore."
    y "Surprised you didn’t just come back home once {i}I{/i} left."

    scene yukiyumibar15
    with dissolve

    yu "Didn’t leave cause of you, Yumi. Wasn’t like that."
    yu "Place wasn’t good for me. Was gonna go insane if I stuck around there any longer. "
    y "So you just abandoned your daughter for your {i}own{/i} benefit? Because things got too hard?"

    scene yukiyumibar16
    with dissolve

    yu "That’s right."
    yu "Would expect you to do the same, too. "
    yu "We might be strong as shit...and we might be able to fight off like five people at once, but the biggest threat to us is always gonna be ourselves. Just sucks cause that’s also what’s most important."
    yu "You lose yourself, you’re as good as done. That’s the kinda shit people don’t ever recover from."
    y "Oh? I thought you were already on the {i}road to recovery?{/i}"

    scene yukiyumibar17
    with dissolve

    yu "I am. Road’s bumpy as shit, though. And I’ve got no fuckin’ clue where it’s goin’ or what the fuck I’m gonna do if I ever make it to the end."
    yu "Seemed a hell of a lot safer than the other road I was on, though."
    yu "Just don’t want you goin’ down that same one."

    scene yukiyumibar18
    with dissolve

    y "Well, gee. Thanks for waiting until I was already miles down that fuckin’ road before tellin’ me I might wanna turn around."
    yu "Why do you think you’re already “miles down that road?” The fuck have you done apart from givin’ that one girl the beating of a lifetime?"
    y "I ain’t a “good” person, Yuki."
    yu "Ain’t many “good” people on this planet, so that ain’t a big deal."
    y "I fuck with everybody. I ain’t nice to anyone at all. Scrape by sellin’ stolen TVs and scamming kids outta their fuckin’ lunch money for shitty candy that’s, once again, fuckin’ stolen."
    yu "Sounds like the start of what could be a lucrative business some day."

    scene yukiyumibar19
    with dissolve

    y "You ain’t gettin’ it! I ain’t done nothing to be proud of! Ain’t done nothing to show I ain’t already on the same path you took to bail on me!"

    scene yukiyumibar20
    with dissolve

    y "What if I deserve this shit? Deserve bein’ looked at like the fuckin’ scumbag I am?"
    y "Cause deep down, we both know that’s what I really am, don’t we?"
    yu "Beats me. I don’t know shit about you, Yumi."
    y "Yeah, because you weren’t there to learn any of it! The fuck am I supposed to do?!"
    y "Can’t go back to school. My best friend is fuckin’ {i}scared{/i} of me. And everybody else that’s heard of me thinks I’m some...rabid animal who beats the crap out of people for no reason!"
    yu "That why you called him your {i}ex-{/i}teacher earlier? You can’t go back?"

    scene yukiyumibar21
    with dissolve

    y "I guess it’s more like I don’t...want to..."
    y "Specially now that I know he’s apparently feedin’ you information about me. No fuckin’ clue how you would’ve even known about this shit otherwise."
    yu "Didn’t hear it from him, just FYI. Fight, I heard about from some other girl I know at a local bathhouse. Found out where you {i}were{/i} from Gary."
    y "Fucking Gary."
    y "Guess that bathhouse is where the whole tits thing comes into play, huh? Makes sense that fucking asshole would go snooping around the girls’ section."
    yu "It’s more like me and some other girls were usin’ the men’s side. Lot more private and I don’t have to fuckin’ stare at people lookin’ down on my tattoo."
    y "Well...whatever. Ain’t somethin’ I feel comfortable gettin’ into with you anyway."
    yu "Not gonna tell me why you did it?"
    y "Doesn’t matter. Rather just forget it."
    yu "Think you’ll be able to? Seem pretty fucked up over it."
    y "You’d probably be fucked up too if somebody came after you like that. "
    y "Worst part is I know I’ve been on the opposite end of that too. Maybe not {i}as{/i} bad, but I’ve still hurt people just because I wanted to. And I didn’t even have a reason 99%% of the time."
    yu "So this girl you rocked...she had a reason to come after you?"
    y "Plenty of ‘em."
    y "Had it coming, didn’t I? Was only a matter of time before I got a taste of my own medicine."

    scene yukiyumibar22
    with dissolve

    yu "What’s the point of the fireworks if you’re gonna say shit like that? Why go back to the Yamaguchi place at all if you’re already feelin’ the consequences for your actions?"
    yu "Just move the fuck on, Yumi. You’re bigger than the shit that you’re gettin’ bogged down by right now. And I ain’t just talkin’ about your tits."
    y "Why is everyone commenting on my tits today?"
    yu "Jealousy, maybe? Sure as hell piss {i}me{/i} off. Fuckin’ degrading when your own daughter beats you out like that."
    y "Would be nice to {i}move on...{/i}just not really sure if I can. Thought starting over might be easier."
    yu "Picked the wrong fuckin’ place to do that, if you ask me. Guess it’s not like I can talk, though."

    scene yukiyumibar23
    with dissolve

    yu "Yakuza’s still the Yakuza at the end of the day. Crime. Drugs. The whole nine yards. Ain’t shit somebody your age should be around."
    y "You had no problem with me bein’ around all that shit when I was a baby, did you?"
    yu "I ain’t the same person I was back then. Want better for you now. "
    yu "Know how badly you don’t wanna be like me...and I get that. I {i}agree.{/i} I don’t want you to be like me either. "
    yu "Which is why I feel like it’s my job to try and stop that shit from happening. Whether or not I deserve that job is another story entirely, though."

    scene yukiyumibar24
    with dissolve

    yu "More I thought about it, the more I realized you probably wouldn’t have gone back to that place unless you felt like you {i}had{/i} to. You’re way too stubborn and angsty to just drop by for a visit."
    yu "Probably oversteppin’ by admittin’ this and talkin’ to you like a real parent...but you can talk to me, you know."
    yu "I ain’t gonna judge you the way others will. I know damn well what it’s like to feel like the whole world’s against you."
    yu "But even if you don’t want one, you’ve got an ally in me. "
    yu "Just worried that one day it’s gonna be you sittin’ in my spot...talkin’ to some girl {i}you{/i} abandoned because you turned left when you should’ve turned right."
    y "..."
    yu "..."

    scene yukiyumibar25
    with dissolve

    y "I’d never do that..."
    y "Never make the same mistakes you did..."
    y "I’m better than that."
    yu "Damn right you are. Should be happy I set the bar so low. Will be easier to get over."
    y "Gee, thanks. I totally understand why you fucked up so badly now."
    yu "Hey, just doin’ my part as family, you know?"
    yu "Even if we don’t stick together, we’ve gotta have each other’s backs when it matters most. "
    yu "And if you ever wind up havin’ to kick the shit out of some other girl who comes at you, give me a call first next time. Could give you a few pointers."
    y "You’ve got a weird fucking idea of how family is supposed to work, I think."
    yu "Yeah. Well, we’re a weird fuckin’ family, ain’t we?"

    scene yukiyumibar26
    with dissolve

    k "Aunt Yukiburger! Prolonged use of tiny nicotine cylinders will cause your fleshy air balloons to turn black and fill with tar! You said you would stop!"
    yu "Hey, I didn’t bitch when you took your sweet ass time coming over here, Kaori. Least you could do is let me get lung cancer in peace without making me feel like a dick about it."
    k "I can only be in so many places at once! You will need to wait your turn!"
    y "K...Kaori?"

    scene yukiyumibar27
    with dissolve

    k "How do you know my name?! I have already told you people, the instant gram is no more!"
    yu "Probably heard me say it five seconds ago. Ain’t a big deal, I don’t think. "
    yu "‘Less she wants it to be, that is."

    scene yukiyumibar28
    with dissolve

    k "The way your glossy sight balls connect with mine tells me you are not who I perceived you to be at first."
    k "My communication with humans is very limited outside of business hours...which can only mean that I have forgotten you..."

    scene yukiyumibar29
    with dissolve

    k "Or are you stalking me! Like a tall stick of beans!"
    y "A...what?"
    k "I will not purchase your beans! I already have too many! "

    scene yukiyumibar30
    with dissolve

    k "I have many things to do now!"
    k "Hello! "
    y "What the fuck was that?..."
    yu "Oh yeah. Kaori’s still alive, by the way."
    y "I knew she was still alive. I just wasn’t expecting to see her here and...was also not expecting her to talk like a fucking alien."
    yu "You get used to it after a little while. Sure she’d be happy to talk to you if you actually explained to her who you are."
    yu "Parents are dead after all. Doesn’t really talk to anybody other than me and your {i}ex-{/i}teacher now. One more friend wouldn’t hurt her."
    y "I ain’t really lookin’ for more friends right now..."

    scene yukiyumibar31
    with dissolve

    yu "Ain’t lookin’ for family either, are you?"
    y "No...I’m not..."
    y "But..."

    scene yukiyumibar32
    with dissolve

    y "Uhh..."
    y "Th..."
    y "Tha..."
    yu "Oh, shut the fuck up. You don’t have to actually say it. You’re down enough as-is. Doubt thanking the woman who helped make you into the mess you are will help at all."
    y "Yeah..."
    y "Yeah, I’m just gonna keep my mouth shut. Ain’t wastin’ unnecessary words on a piece of shit like you."
    yu "Wouldn’t mean much coming from a piece of shit like {i}you{/i} either."

    scene yukiyumibar33
    with dissolve

    y "It really wouldn’t...would it?"
    y "..."
    yu "..."
    y "I’m fucking starving..."

    scene black
    with dissolve2

    ".........."
    "......"
    "..."

    scene bedroom_night
    with dissolve2
    play sound "phonebeep.wav"

    s "Hello?"
    yu "Yo. "
    s "Yuki? Isn’t it a little late for you to be calling?"
    yu "The fuck you mean “late?” You goin’ to sleep already, you little puss?"
    s "..."
    s "{i}No.{/i}"
    yu "Uh-huh. Sure."
    yu "Anyway, just wanted to let you know I talked to Yumi for a bit today."
    s "What? Really? She actually talked to you?"
    yu "For an hour or two, yeah. Got dinner at some dive bar and talked a little about the shit that went down at school with her."
    yu "Wouldn’t tell me much, of course. But it was nice actually bein’ able to hold a conversation with her for the first time in...actually, probably ever."
    s "Well, I’m happy for you. "
    s "My day was horrible."
    yu "Hah! And why’s that?"
    s "I started a family."
    yu "Damn. "
    yu "Don’t let Sara know. Don’t wanna see her cry."
    s "If I’m lucky, I will no longer be a part of the family by tomorrow."
    yu "Yeah, startin’ to sound like my day was a little better."
    yu "But yeah, just wanted to let you know that shit happened in case you were worried about her. Still ain’t convinced you two aren’t fucking."
    s "Yuki-"
    yu "Also, told me to tell you to not come looking for her. Fucking tsundere, that girl."
    s "It’s not like I’d be able to find her anyway. She’s gotten too good at avoiding me."
    yu "You stalkin’ my daughter, man?"
    s "Only when I have to."
    yu "Well, give her space for now or some shit. She’ll probably find you when she’s ready. Just takin’ a little while to cool off, I think."
    yu "Anyway, I’ve gotta head back to my apartment. Got a new neighbor movin’ in next door tonight and I don’t want my bike wakin’ ‘em up and shit."
    s "Sure. Thanks for...letting me know what’s going on with Yumi, I guess."
    s "And congratulations, Yuki."
    yu "Heh."
    yu "Thanks, man..."
    yu "Appreciate that."

    play sound "phonebeep.wav"

    "I hang up the phone and toss it onto my bed, unsure of exactly what this means for my relationship with Yumi."
    "But I guess I don’t really deserve any form of certainty after failing to properly stand up for her back in the locker room."
    "I’d avoid me if I were her as well."

    scene black
    with dissolve2
    stop music fadeout 8.0

    "But, then again..."
    "I probably would have never gotten to know me in the first place."

    s "..."

    "How unfortunate that she did."

    $ renpy.end_replay()
    $ yumiyukispecial1 = True

    "........."
    "......"
    "..."

    if day == 6:
        jump advancetosun
    if day == 7:
        jump advancetomon

label imanispecial1:
...
```

## Code that triggers this event

File: (install folder)\game\chap3.rpy

Code:
```python
...
scene chikayakuza20
    with dissolve

    c "Are you gonna tell me what happened?"
    y "You saw what happened."
    c "Ooookay. Then, are you going to tell me {i}why{/i} it happened?"
    y "..."
    c "Yumi, do you really think I would have trespassed on Yakuza turf and fought off two thugs if I didn’t want to be on your side? Fuck no."
    c "I’m basically dying for a reason to go to bat for you right now. But shit like “Oh, you guys just don’t understand her!” isn’t going to work this time."
    c "Nodoka was {i}fucked up{/i} for like a whole week. I’m surprised she came out of that without a concussion."
    y "How about everybody else?"
    c "What do you mean?"
    y "What are {i}they{/i} sayin’ about me?"

    scene chikayakuza21
    with dissolve

    c "..."
    y "If you need to “go to bat” for me...it’s probably pretty bad, huh?"
    c "It’s...uhh..."
    c "It’s definitely...not good..."
    c "Your reputation kinda sucked to begin with and beating a genius unconscious while she was trying to teach the nicest girl in the class math is...not a good look."
    y "Figured."

    scene chikayakuza22
    with dissolve

    c "But, Yumi! You-"
    y "Maybe I just felt like beatin’ the shit out of her, Chika?"
    c "But, that..."
    c "No way. That wouldn’t make any sense."
    y "Why not? Bullied Futaba from the moment I met her. Tons of other people too."
    y "Still talk mad shit on Sensei and you guys are basically attached at the hip now."
    y "Maybe I just ain’t a good person?"
    c "Yeah...maybe you’re not. But you’re also not the type of person to just do shit like that without a reason."
    y "You also thought I wasn’t the type of person to come back {i}here{/i} of all places and I didn’t even last one day out on the streets."
    c "Yumi-"
    y "People change, Chika. You gotta remember where I come from."
    y "I’m the daughter of a Yakuza boss and a junkie. Ain’t exactly the model family a lot of other people grow up with."

    scene chikayakuza23
    with dissolve

    c "Why are you hiding this from {i}me?{/i}"
    y "Who says I’m hiding anything?"
    c "You think I don’t understand your stupid mannerisms by now? How you always look away and drop your voice whenever you’re trying to keep something a secret?"
    c "Did I fuck up guessing where you went? Yeah. Yeah, I did. But I was also holding out hope that you were going to come back to {i}my{/i} family before the one you left to try and become a better {i}you.{/i}"
    c "Chinami is worried sick. We want you back."
    c "But right now, what I want more than anything is to understand what happened to you so you don’t just...lose all of the progress you’ve made."

    scene chikayakuza24
    with dissolve

    y "Honestly, Chika...{i}fuck{/i} progress. The hell was I going to get out of that anyway?"
    y "Ain’t like I was tryin’ to make friends or something. If anything, I don’t even know if I’d call any of that “progress” since I was just...backtracking on all of the bad shit I’ve done."
    y "No reason to clap and cheer for me for finally turning around when I’ve been runnin’ the race in the wrong direction my whole life. Might as well just...quit and save myself the embarrassment, you know?"
    c "I don’t...but I’m going to clap and cheer for you any chance I get since you’re my best friend. I just wish you’d trust me enough to confide in me."

    scene chikayakuza25
    with dissolve
    stop music fadeout 30.0

    y "Course I trust you. Maybe I just don’t want you catchin’ a murder charge and leaving the twerp all on her own when she’s already lost everybody else?"
    c "A...murder charge? Just what the fuck happened?"
    y "Doesn’t matter. It’s in the past now."
    y "So my reputation is dead in the water. Big deal. Ain’t like I’m ever comin’ back to school in the first place."

    scene chikayakuza26
    with dissolve

    c "What do you mean “ever?”"
    c "Were you actually expelled? Because word around the school is that you’re just indefinitely suspended. Which means that there’s still hope for-"
    y "Think I’m just gonna drop out."

    scene chikayakuza27
    with dissolve

    c "What?..."
    y "Let’s be real. I never fit in there anyway. And if we had any other teacher, I probably would’ve been kicked out already."
    c "But...no. No, I can’t let you do that. You always talk about how you want to make something of yourself and...and if you’re dropping out...what are you going to do instead? What does that mean for us?"
    y "For us? Not much. If you ain’t scared of me after almost killin’ Nodoka and shit, I’m happy to keep bein’ friends with you."
    y "But for {i}me?{/i}"
    y "I don’t know."
    y "Maybe I’ll hang out here for a while? Give the whole Yakuza princess shit a spin and see how that goes."
    c "That’s..."
    c "But that’s...the exact opposite of what you’ve been trying to do this whole time."
    y "It is, ain’t it?"
    y "Means it might actually work."
    y "Besides, as long as I don’t end up like my mom, I think I’ll be able to call my life a success. And I ain’t anywhere near {i}that{/i} bad yet."

    scene chikayakuza28
    with dissolve

    yu "Hey now. I’ve been gettin’ a hell of a lot better, you know."

    $ renpy.end_replay()
    $ yumichikaspecial1 = True

    jump yumiyukispecial1
...
```