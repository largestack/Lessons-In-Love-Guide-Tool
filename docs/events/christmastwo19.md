# The Color White
Main event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo19&go=Go)


Part of event chain [Me Without You](./christmastwo18.md)

## Event preconditions
No event conditions found, it is likely part of an event chain.

## Next events
None

## Event properties
* ID: christmastwo19
* Group: Main
* Triggered by label: christmastwo18

## Event code
File: \game\ch2script.rpy
Code:
```python
...
label christmastwo19:
    scene yasuseesinthedark1
    with dissolve2
    stop music fadeout 10.0

    "I make my way back to the room to find the hall eerily quiet. "
    "The sound of laughter and enthusiastic non-Christmas karaoke which reverberated off of these walls the last time I allowed myself to be surrounded by them is no more."
    "It’s blank. And cold. And empty."
    "And, at the risk of sounding broody- reminds me a lot of the person I see every time I look in the mirror."
    "Or one of them at least."
    "Sometimes, I see something else."
    "I forget it immediately after."
    "If only you understood what that meant."

    s "..."

    "I stand in front of the door for a moment, hoping to hear any sort of sound escaping the confines of the stuffy, overheated room."
    "I realize I’ve been gone for a while, but I didn’t think I’d been gone long enough to warrant the party ending without me."
    "If no one is here, where did they go? {i}Why{/i} did they go there?"
    "And why am I more focused on the possibilities than taking it upon myself to look?"

    scene black
    with dissolve2

    "I move toward the door and touch it."
    "It’s so warm that I forget how cold everything was just moments ago."
    "I open it."
    "It opens me in return."

    scene yasuseesinthedark2
    with dissolve3
    $ renpy.pause(3, hard=True)
    play music "yasusings.mp3"

    s "..."

    "As if on cue, a song starts once I enter the room- though the person holding the microphone is not one that I would expect."
    "Yasu’s frail body is enveloped by the glow of the television, making her snow white dress and hair both significantly paler than they already are."
    "For someone who hates the color white, she sure pulls it off well."
    "As well as possible while being a complete fucking lunatic, I mean."
    "I guess she’s a cute lunatic, though."
    "I can’t say that standing alone in a dark room and whispering into a microphone is a hobby that I admire or understand, but I guess it’s a little endearing when approached from the right angle."
    "The right angle being ten feet behind her, I mean."
    "If I moved any closer, I worry that the residual warmth I peeled off of the door might melt her skin off."
    "As always, I am content with just watching, even if I don’t understand everything I see."
    "It’s no different from how things normally are."
    "Just a little quieter-"
    "A little whiter."

    to "She’s been waiting all night for a turn to sing."

    scene yasuseesinthedark3
    with fade

    s "Touka?"
    to "What brings you back here, Sensei? I had assumed you’d be with the rest of the girls by now."
    s "I don’t know where any of them are. I kind of figured you’d all just...stay where I left you."
    to "Contrary to what you may believe, the world does not revolve around you."
    to "There’s a fireworks celebration tonight. And several people were looking forward to you being around to watch it together."

    "Right. There was one of those last year too, wasn’t there?"

    s "Why are {i}you{/i} here then?"
    to "For Yasu, of course."
    to "She managed to stay distracted for most of the night, but I couldn’t possibly let her be alone for all of Christmas."

    scene yasuseesinthedark4
    with dissolve

    to "Plus, I think fireworks are a rather tacky form of celebration. Dangerous, too."
    s "Of course you do."

    scene yasuseesinthedark5
    with dissolve

    to "She isn’t bad, is she? I find her voice rather relaxing, to be quite honest."
    s "It is certainly unique, if not anything else."
    to "And to think that it’s her first time. Why, I feel a bit like a proud mother."
    to "All she needs now is to work on her confidence so she can do this in front of everyone. And maybe turn a few lights on."
    s "I don’t really think “confidence” is a word that pops up in Yasu’s mind very often."
    to "It “pops up” just as often as it does for everyone else."
    to "Why do you think she waited until now to sing when she could have just asked for a turn earlier?"
    s "I’ve stopped trying to attribute reasons to anything Yasu does."

    scene yasuseesinthedark6
    with dissolve

    to "Well if you’d {i}like{/i} to know, it’s because she didn’t want to bother anyone."
    to "You might believe Yasu to be some sort of religious fanatic and, to some extent, that is most assuredly true."
    to "But there’s another side to everyone, Sensei. And the side Yasu hides behind her psalms and sermons is one that I’ve heard her describe as some sort of...insect on various occasions."
    to "A cockroach, I believe it was."

    scene yasuseesinthedark7
    with fade

    to "And, unfortunately, I understand the comparison. I do not personally agree with it, but I understand it."
    to "I have always looked at myself as an outlier of sorts. Someone who does not fit in with others and, in turn, completely destroys the averages of small sample sizes."
    to "I still believe that to a certain extent and have plenty more to learn, but I don’t think Yasu even acknowledges a life in which she stands on the same ground as the other girls."
    to "And I don’t think those girls are in any rush to get to know Yasu either."
    to "Which makes me very sad, since she admires every single one of them and simply wants to do all of the things they do."
    s "The others would probably care a little more about getting to know Yasu if she wasn’t always trying to convert them to her weird religion."
    to "She’s just trying to share the one thing she knows about with everyone else."
    s "Well, she is very aggressive about it sometimes."
    to "I suppose she is."
    to "But her entire personality is one composed of inconsistencies and curiosities."
    to "Those flashes of confidence become ones of concern once the cameras are off...and the Yasu you are seeing now is the one I wish others could see as well."
    s "You really like her, don’t you?"
    to "She is a colossal pain in my behind."

    scene yasuseesinthedark8
    with dissolve

    to "But she is also the first friend I’ve ever had."
    to "So I suppose I have a bit of a soft spot for her."
    to "I’m sure you will in due time as well."
    to "It may take several more dark rooms and several more karaoke machines, but the day will come."
    s "Maybe it will."
    s "Whatever happens happens."

    scene yasuseesinthedark9
    with dissolve

    to "So, do you intend to stay here with us? Perhaps you and I could perform some sort of duet once Yasu has had her fill of the microphone?"
    s "I’m not much of a singer. And I also don’t trust that you would have a decent taste in music."
    to "You would be surprised, Sensei. Mother and I spent quite a few nights with one another listening to popular music. I know many of the hits."
    s "Hearing you say it that way made me somehow trust you even less."
    to "Really, though. Why are you still here?"
    to "Half of the class is waiting for you and you managed to stumble upon the two girls who were fine separating themselves from the crowd for the sake of their own personal comfort."

    scene yasuseesinthedark10
    with dissolve

    s "Probably because I always manage to stumble upon the one place I shouldn’t be when there are countless others I belong in."
    to "When you put it that way, perhaps you aren’t all that different from Yasu and me after all?"
    to "We’re just three people who don’t fit anywhere other than the little worlds we made for ourselves."
    s "Sure. Except I’m not the one who made this world."

    scene yasuseesinthedark11
    with dissolve

    to "Would you enjoy it any less if it was one made {i}for{/i} you?"
    to "Must something be put together by your own two hands for you to accept it? Or can you live in a house someone else built so long as it fits your needs?"
    s "I don’t know, Touka. I’m not really in the mood to wax philosophical right now."
    to "Apologies, Sensei."

    scene yasuseesinthedark12
    with dissolve

    to "Were you able to deliver the bear, at least? I must say, I grew quite fond of that little fellow over the short time we knew one another."
    to "I do hope his new home will be a good one."
    s "..."

    scene black
    with dissolve2

    s "I’m sure it will be."

    "........."
    "......"
    "..."

    scene yasuseesinthedark13
    with dissolve2

    mak "..."
    mi "..."
    mak "Are you serious?"

    scene yasuseesinthedark14
    with dissolve

    mi "I’m so sorry, Makoto!"
    mak "..."
    mi "It was all me, too! Sensei didn’t do anything!"
    mi "I just couldn’t hold it back anymore! It was an accident!"
    mi "I’m so sorry! I’m so...so sorry!"

    scene yasuseesinthedark15
    with dissolve

    mi "Just tell me what ya want me to do to make it up to you and I will!"
    mi "I never wanted this to happen! I’m just a...fucking idiot! And I never curse, so...so you know I mean it!"
    mak "..."
    mi "Makoto, say something! Please! Even if it’s just yelling at me! I don’t care!"

    scene yasuseesinthedark16
    with dissolve

    mak "What the fuck am I supposed to say to this? What would {i}you{/i} say if you were me, Miku?"
    mi "I don’t know...I’ve got no friggin’ idea..."
    mi "I just...couldn’t keep it from you anymore..."
    mi "I’ve liked Sensei for a while...and I thought I’d be able to kinda like...force it away or somethin’, but..."

    scene yasuseesinthedark17
    with dissolve

    mak "That’s not how it works, Miku."
    mak "You can’t just force your feelings to not exist if they make things harder for you. That sort of thing kills people."
    mak "I’ve obviously known that you like Sensei for a while, but..."
    mak "I guess...this part of the relationship came a lot sooner than I expected..."

    scene yasuseesinthedark18
    with dissolve

    mi "You {i}expected{/i} this?!"
    mak "You know, after finding you half naked with him that one time, yeah. I kind of did."
    mi "We talked about that, though! It was just a misunderstanding!"
    mak "Are you really going to lie about that again? Right now?"
    mak "Don’t you think now would be a good time to come clean about it since you literally just admitted to kissing him like two minutes ago?"
    mi "Okay, fine! It wasn’t an accident! But I’ve messed up enough and I’m already worried you’re gonna hate me for it!"

    scene yasuseesinthedark19
    with dissolve

    mak "{i}Hate{/i} you? Do you really think I could do that?"
    mak "And for something as small as liking the same person as me?"
    mi "It’s not small, though...you love him..."
    mak "Do {i}you{/i} love him?"
    mi "I...don’t think so?..."
    mi "I don’t know...I’m still new to feelin’ this way..."

    scene yasuseesinthedark20
    with dissolve

    mak "Then I guess I’ve got a head start."
    mak "Just so you know, though, I’m not going to take it easy on you just because you’re my best friend."
    mi "...What?"
    mi "What are you...sayin’ right now?..."

    scene yasuseesinthedark21
    with dissolve

    mak "That you can try as hard as you want, but I’m still going to win."
    mak "I’m already used to fighting for Sensei’s affection. One more person doesn’t mean anything to me."
    mi "Makoto-"
    mak "And stop crying, already. You know I hate when you do that."
    mi "You’re crying too, though..."

    scene yasuseesinthedark22
    with dissolve

    mak "I’m allowed to cry. I just found out that my best friend likes the same person as me."
    mi "I knew it! You do hate me after all!"

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yasuseesinthedark23
    with dissolve2

    no "Oh god...I’m...gonna throw up..."
    f "Please don’t. There are people down there."
    no "There are...hic...people {i}everywhere...Futaba..."
    no "That’s why...they’re called...hic...{i}people{/i}..."
    f "You...really stop making sense when you’re drunk, huh?..."
    r "Am I mad? That you’re too embarrassed by your sexuality to tell your parents that you’re dating a girl? Yeah, I kind of am."
    r "..."
    r "Oh, so it would be fine if I had a dick? It’s the fact that I {i}don’t{/i} that means your parents will dislike me? Why the fuck do they even care?"

    scene yasuseesinthedark24
    with dissolve

    r "Well, then tell them we’re friends! Or are you not allowed to have any of those either?!"
    r "..."
    r "Yeah, I am yelling! I’m hurt and embarrassed!"
    r "And stop bringing my moms up! They don’t have anything to do with us!"
    r "..."

    scene yasuseesinthedark25
    with dissolve

    r "Of course I still want there to be an {i}us!{/i} I just want the {i}other{/i} half of the {i}us{/i} to not think that there {i}being{/i} an {i}us{/i} is something to be ashamed about!"
    r "..."
    r "Well then fucking prove it, Otoha! I’m not the one who started this! You are!"
    r "I just wanted to meet my girlfriend’s parents, which is apparently the equivalent of murdering their dog!"
    r "..."
    r "It was a figure of speech! I’m not going to hurt their dog!"
    f "Rin, do you want me to talk to her? I can probably be a little more...calm than you are."

    scene yasuseesinthedark26
    with dissolve

    r "No, Futaba. It’s fine..."
    r "..."
    r "..."
    r "..."
    r "I like you too. A lot."
    r "But I don’t like the idea of you being ashamed of me. That hurts."
    r "But I have to go now. Your roommate is dying."
    no "Tell her...hic...she’s got...a nice...ass..."
    r "Nodoka says you have a nice ass."
    f "Are you sure you want those to be your last words to her?"
    no "I...hic...regret nothing..."
    r "..."
    r "Yeah..."
    r "I’ll text you when I get back to the dorm, but you’ll probably be asleep by then."
    r "..."
    r "Then..."
    r "Goodnight, I guess."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yasuseesinthedark27
    with dissolve2

    tk "Feast your eyes on this, Chinami! This magnificent dish is known as the “sausage fest” and, through the wonders of the “Door Dash,” I had it brought here just for us!"
    tk "And I didn’t tip the driver! So we can invest the additional cash into our business!"
    ch "Chinami is too surprised by how big the food is to tell you to be nicer to essential workers!"
    tk "The only workers who are essential are the CEOs who keep this world running, Chinami! The people like us!"
    tb "I’m glad to see they’re getting along well."
    tb "Are you sure you don’t want a drink, though, dear? It might help...assist with the noise."
    c "Oh, no. I’m fine."

    scene yasuseesinthedark28
    with dissolve

    c "And, for some strange reason, I feel like I’ve already been drunk in this room before."
    c "I just...don’t remember {i}when.{/i}"

    scene yasuseesinthedark27
    with dissolve

    tb "That aside, why aren’t you with the rest of your class? Shouldn’t you be focusing on making memories with them instead of an old woman?"
    c "Oh, stop. You’re not even that old."
    c "I’d rather be with you right now anyway. It’s good to take a break from all of the...class drama every once in a while."

    scene yasuseesinthedark29
    with dissolve

    tb "Oh, sweetie. I’ve watched enough American teen dramas to know that you’re talking about love."
    tb "And if Yumi is out there right now and {i}you’re{/i} not...it must be pretty juicy."
    c "Hahah...{i}juicy{/i} probably isn’t the right word..."
    c "I’m just trying to give him a little space right now since I...can be kind of a lot sometimes."
    c "I get it, though. I’ve been all over the place lately. It’s just...tough, you know?"

    scene yasuseesinthedark30
    with dissolve

    c "Like...you think a boy will want one thing, but they want the complete opposite."
    tb "Oh my, are we talking about the WAP again?"
    c "Tsubasa, please stop calling it “the WAP.” It’s weird and gross."
    tb "Well, it’s not as if I can address it by its proper name with two {i}wizards{/i} in the room."

    scene yasuseesinthedark31
    with dissolve

    c "Okay, yeah. Fair point."
    c "What...do you think I should do, though?"
    c "Like...needing space isn’t some kind of code for not liking me anymore, is it?"
    tb "Not at all, dear. Too much of anything can get a little hard to handle at times."
    tb "But if you two are right for one another, things will work out."
    tb "If you respect his boundaries, he’s sure to respect you."
    c "But...what if we’re {i}not{/i} right for each other? How am I supposed to know that?"

    scene yasuseesinthedark32
    with dissolve

    tb "Oh, honey. I’ve heard the two of you enough to know that is definitely {i}not{/i} the case."
    c "Thanks, Tsubasa...I always appreciate you reminding me of that..."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene yasuseesinthedark33
    with dissolve

    ya "..."
    s "..."

    "Yasu finishes her song and turns around to find me."
    "I guess she was in too much of a trance to notice Touka and me talking through the entire song, because she seems rather shocked by my sudden appearance."
    "Either that or she’s just being weird again."
    "But, as a favor to Touka, I’ll go ahead and assume the former this time."

    ya "..."
    s "..."
    ya "You heard..."
    s "I did."
    ya "I’m sorry."
    s "Why are you apologizing?"

    scene yasuseesinthedark34
    with dissolve

    ya "I’m not very good."
    s "That’s not true."
    s "You did a lot better than I could."

    scene yasuseesinthedark35
    with dissolve

    ya "Heheh...hehhahhhahah..."
    s "Your laugh could still use a little work, though."

    scene yasuseesinthedark36
    with dissolve

    ya "I will practice."
    s "Well...keep at it, I guess."
    ya "Someone is waiting for you, you know."
    s "Hm?"
    ya "On the rooftop."
    ya "I can hear the footsteps from all the way down here. Somewhere between the top and the bottom."
    ya "They’re light, but purposeful. Sad, yet full of hope."

    "Right. Fuck."
    "I was supposed to meet Maya on the roof after I finished talking to Niki."
    "I must have gotten sidetracked somewhere down the line."
    "But..."
    "Why does Yasu know that?"

    s "How do you-"
    ya "All of the other sounds disappeared."
    ya "The rumbling has quieted, leaving nothing but whispers and footsteps."
    ya "Summer is right around the corner."
    ya "I’ll have to find my parasol."
    s "..."

    "You know, it’s probably best if I just stop asking Yasu for explanations."

    s "I guess I’ll...head up to the roof, then."
    ya "I guess so."
    ya "Count the stairs on your way up."
    ya "Remember to smile."
    s "Will do, Yasu..."

    scene black
    with dissolve2
    stop music fadeout 10.0

    "I heed Yasu’s advice (Albeit only the first part) and count the stairs on my way up to the roof."
    "It helps distract me from keeping Maya on top of yet another building for longer than she’d like to be there."
    "There were 85 of them, in case you were wondering."
    "You should always be wondering."

    $ renpy.end_replay()
    $ christmastwo19 = True
    $ yasu_love += 1
    $ touka_love += 1

    "{i}Touka’s affection has increased to [touka_love]!{/i}"
    "{i}Yasu’s affection has increased to [yasu_love]!{/i}"
    "........."
    "......"
    "..."

    jump christmastwo20

label christmastwo20:
...
```

## Code that triggers this event
File: \game\ch2script.rpy
Code:
```python
...
"I wonder if we’d still be standing here today if that never happened."
    "I wonder if this kiss would feel even half as good as it does without years of history gushing out of it."
    "Of course I want Niki."
    "In fact, it’s probably one of the things I’m {i}most{/i} certain about right now."
    "But I can’t have her the same way I can have the other girls."
    "She wants the version of me she grew up with. The one who (At least presumably) sat there listening to her problems and helping her through them when necessary."
    "She wants the person who helped her discover what it means to love. How it feels to be touched. "
    "She wants someone who doesn’t exist anymore."
    "Why does one measly memory entitle me to that? "

    scene nikilove14
    with dissolve

    ni "Are we really not getting back together? Because, maybe I’ve just been reading too much manga, but this played out a little differently in my head."
    s "Did you think you were just going to confess out of the blue like that and that we’d ride off into the sunset together?"
    ni "Obviously not. It’s night time. The sun has already set."
    s "You know what I mean."
    s "Besides, I already knew you felt this way. Maybe not in as much detail, but I still knew."
    ni "I just...don’t really understand why. Do you...not see me that way anymore or something?"
    s "That’s not it."
    ni "Then what is it? Help me understand."
    ni "If I’m going to keep fucking waiting for you, I’d at least like to know what I’m waiting {i}for.{/i}"
    s "It’s not really something that I can easily describe."
    s "I just don’t think we should be {i}together{/i} until I feel a little less...numb."

    scene nikilove15
    with dissolve

    ni "Ugh. That’ll take years. You’ve been saying that for as long as I’ve known you."
    ni "Listen, there’s obviously no rush since I have {i}zero{/i} interest in anyone else, but don’t keep me waiting forever...okay?"
    ni "I’m really bad at taking no for an answer, but I love you enough to let it happen every once in a while."
    s "I appreciate you accepting that I, too, have free will. That’s very generous of you, Niki."
    ni "Don’t get snippy with me, asshole. And get a new fucking blazer, would you? This thing is worn to hell. "
    s "This is a good shirt. You take that back."

    scene nikilove16
    with dissolve

    ni "So, I’m guessing there’s not much hope in getting you to leave your lame school party and come back to a different, fancier hotel with me? "
    s "Maybe next time. I’ve already been gone for a while and kind of told someone that I’d meet up with {i}them{/i} next."
    s "I’m sorry it wasn’t the result you were looking for, but I {i}am{/i} glad you came here to tell me all of that."
    ni "Yeah, yeah. Whatever. If you’re not going to give my box back, at least try skimming through some of the nicer letters to see if any {i}more{/i} of your memories come back."
    ni "I knew they would eventually. Just didn’t think it would take this fucking long."
    s "I don’t understand how you can still be so accepting of me after all I’ve put you through."
    ni "The same reason I frantically came over here in the middle of the night to tell you all of this."
    ni "Because I miss you."

    scene nikilove17
    with dissolve

    ni "It’s a shame you didn’t want to come back to my hotel, though. "

    if bonus == True:
        ni "I was thinking tonight could be the night."
    else:
        ni "I bought so many Capri Suns and now I have to drink them all by myself."

    s "..."
    s "I’m sorry, what was that?"

    scene nikilove18
    with dissolve

    ni "Ooooooh, nothing~"
    ni "Just that it must really suck to be you right now."

    if bonus == True:
        s "..."
    else:
        s "I love Capri Sun."

    scene nikilove19
    with dissolve

    ni "Feel free to text me if you get bored or something. Maybe I’ll even give you a little peek at what you’re missing out on?"
    ni "Actually...maybe not. I don’t know how fun it would be since you’re so {i}numb{/i} and all."
    s "..."
    ni "Oh, and get a new blazer! It’s okay to treat yourself on Christmas!"
    ni "Also, I love you! "
    ni "Goodnight!"

    scene black
    with dissolve2

    "Niki’s voice gets harder to hear with each sentence as she distances herself from the hotel."
    "I don’t know if I’d count this as a {i}rejection{/i} if I was her, but I’m sure it didn’t feel good to pour her heart out like that to such a lackluster response."
    "I am the king of lackluster responses, though."
    "Just as I’m the king of luring young women into relationships that only I stand to benefit from."
    "But, maybe one day, if I can ever become who it is I am supposed to be-"
    "Or who it is I was-"
    "Maybe then, that won’t be the case anymore."
    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ christmastwo18 = True
    $ niki_love += 5

    jump christmastwo19
...
```