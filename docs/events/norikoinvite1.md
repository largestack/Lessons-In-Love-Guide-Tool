# New Shoes (Noriko)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Day of week is not Saturday

* Day of week is not Sunday

* Event [Kind Of, Yes. Kind Of, No.](./norikodorm10.md) (Noriko) is completed)



## Next events

None

## Event properties

* Id: norikoinvite1
* Group: Noriko
* Triggered by label: norikoinvite
* Triggered by branch label: inviteover
* Triggered by path: inviteover->norikoinvite->norikoinvite1

## Official wiki page

[New Shoes](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=norikoinvite1&go=Go) for more details.

## Event code

File: (install folder)\game\NorikoEvents.rpy

Code:
```python
...
label norikoinvite1:
    play sound "phonebeep.wav"

    "I tap on Noriko’s name in my phone and wait for her to answer."
    "I'd normally wait a little while longer before inviting girls to the house but, considering that Noriko has apparently known me for however many years now, I think I’ve waited long enough."
    "Granted, I’ve only been consciously waiting for several weeks, but I’m sure someone who likes me as much as her is bound to agree."
    "The only issue is how I’m going to explain it to Ami. "
    "But I guess that’s something I can deal with later."

    play sound "phonebeep.wav"

    n "Sensei! Hey!"
    n "What’s up?"
    s "Hey. Are you doing anything tonight?"
    n "Not at the moment~"
    n "Did you want to go out together or something?"
    s "I was actually wondering if you’d want to come over my place."
    n "Wha-"
    n "For real!?"
    n "Like, this isn’t a joke?"
    s "Why would I joke about something like this?"
    n "Well...like-"

    if bonus == True:
        n "When you came to my dorm the other day, there was that whole thing about me being nervous. So I didn’t think you’d...call on me again so soon."
        s "This isn’t a booty call, Noriko. Ami is home."
        n "Oh..."
        n "And you’re...inviting me over anyway?"
        s "It appears that way."
    else:
        s "Get your mind out of the gutter, Noriko. I am your teacher, not your lover."
        s "Also, Ami is here. I can not hug others when she is present."

    n "Oh my God."
    n "I think I’m going to cry."
    n "Yes. Absolutely. I’ll get dressed and start heading over as soon as you send me the address."
    s "Great. I’ll send it now."
    s "See you soon, Noriko."
    n "Yeah! See you soon!"
    n "I’m so happy...holy shit."

    play sound "phonebeep.wav"
    scene black
    with dissolve
    stop music fadeout 10.0

    "I hang up the phone and send my address to Noriko right away, sending Ami a message right after."
    "As I expected, she’s home."
    "But at least I have the entire walk back to figure out how I’m going to explain myself."
    "………"
    "……"
    "…"

    scene norikofirstvisit1
    with dissolve
    play music "normalday.mp3"

    a "Sensei! Welcome home!"
    s "Hey. Sorry for not walking home with you today. "
    a "Don’t worry about it! Everything is totally fine because now I get to have you all to myself!"
    s "…"
    a "…"
    s "…"

    scene norikofirstvisit2
    with dissolve

    a "{i}Because now I get to have you all to myself.{/i}"
    s "Ami, I have bad news."

    scene norikofirstvisit3
    with hpunch

    a "Gosh darn it! Who is it that’s stealing you away from me this time?!"
    s "I invited Noriko over."

    scene norikofirstvisit4
    with dissolve

    a "Noriko? The girl that’s head over heels in love with you?"
    a "Doesn’t inviting her here mean that...you also..."
    s "No. I mean, it’s not like I invited her here in secret or anything. I already knew you were going to be home today."
    s "And besides, you two are basically childhood friends."
    a "Didn’t we only hang out like...once? I was still in elementary[school] while you were tutoring."
    a "And I was still smart back then so I didn’t need any help."
    s "God, what happened to you?"

    scene norikofirstvisit2
    with dissolve

    a "You did! "
    a "I stopped caring as much about my education when I realized that you’d love me forever and always. Even if I stopped getting good grades."
    s "Well, either way, Noriko is coming over. And she’s actually excited to see you."

    scene norikofirstvisit5
    with dissolve

    a "Well I’m not excited to see her. If I hear her talk about loving you one more time, I’m going to punch her in the face."
    s "You’ve yet to punch Ayane and she says that every thirty seconds."
    a "I am punching Ayane in the face inside of my mind every minute of every day."
    s "And yet you still sleep in the same bed sometimes."
    a "Where I dream of punching her in the face until I wake up."

    play sound "doorbell.mp3"

    scene norikofirstvisit4
    with dissolve

    s "Oh. I'm guessing that's her now."
    a "Sensei...I don’t know how I feel about this girl knowing our address. "
    a "Maya really seems to think she’s some kind of stalker."
    s "She’s more like a puppy. If she starts hanging out in front of the house or whatever, I can just tell her to leave and she will."
    a "But still..."

    play sound "knock.mp3"

    n "Helloooo? Sensei? Ami? Is anyone home?"
    s "I’m going to answer the door now. "
    s "If you’re going to punch her, please do it in your mind like you do for Ayane."
    a "But...Sensei..."

    scene black
    with dissolve

    "I walk over to the door and let Noriko in."
    "To my surprise, she doesn’t try to hug me or jump on me the way a normal puppy would but, instead, neatly places her shoes at the front door and runs over to Ami."
    "………"
    "……"
    "…"

    scene norikofirstvisit6
    with dissolve

    n "Ami! I’m so happy to know where you live now!"
    a "Umm...why?"
    a "The only time we’ve talked was when you stole Sensei and took him to some random place that I wasn’t allowed to know about."

    scene norikofirstvisit7
    with dissolve

    n "And when we were little, too. But I guess that was so long ago that you might have forgotten."
    s "Noriko, you are aware that {i}I{/i} am the one who invited you over, correct?"

    scene norikofirstvisit8
    with dissolve

    n "Duh~ But who says I’m not allowed to be excited to see both of you?"
    n "It’s a Nakayarakawayama family reunion!"
    a "A...Naka...yaka...yama...reunion. "
    a "Yaaaay..."
    n "Yay!"

    scene norikofirstvisit9
    with dissolve

    n "So...this is what you two see every morning..."
    n "It’s nothing at all like your old place, Sensei. I like this a lot."
    n "It’s so much brighter."
    a "So...umm...how long have you known Sensei again, Noriko?"
    a "You said since you were...six?"

    scene norikofirstvisit10
    with dissolve

    n "Way before that, actually. I’ve known him for pretty much my entire life since he grew up next door to my house."
    a "Oh, okay...So he was just a neighbor."
    a "You probably didn’t actually start like, spending {i}time{/i} with him until you were old enough for...tutoring then, right?"
    n "Oh, no. I saw him all the time. He dated my sister Niki for five years and was coming over to hang out with her even before that."

    scene norikofirstvisit11
    with dissolve

    a "…"
    n "…"
    a "Come again?"
    n "Yup! He was practically family! "
    n "Everyone always said those two were going to be together forever and blah blah blah."
    a "…"
    n "…"

    scene norikofirstvisit12
    with dissolve

    a "…"
    n "…"
    s "Uh-oh."
    s "You had no idea, did you?"
    a "Nope."
    a "Why does this girl know more about your past than I do, Sensei?"

    "I guess...Sensei kept this hidden from Ami for some reason?"
    "I imagine the reason had something to do with everything happening around the same time as the accident..."
    "But I really don’t want to bring that up in front of Ami when she’s still extremely sensitive to it."
    "What I {i}can{/i} do is this, though."

    s "It’s actually Niki Nakayama. That one idol you listen to. "
    a "As if I would believe you dated Niki Nakaya-"

    scene norikofirstvisit13
    with dissolve

    a "Wait. What’s your last name again?"
    n "Nakayama. "
    a "And your sister’s name?"
    n "Niki."
    a "…"
    n "…"

    scene norikofirstvisit14
    with hpunch

    a "YOU DATED NIKI NAKAYAMA FOR FIVE YEARS AND NEVER TOLD ME ABOUT IT?!"
    a "WHO EVEN ARE YOU?!"
    a "I DON’T KNOW IF I SHOULD BE MAD OR IMPRESSED OR SAD RIGHT NOW!"
    a "I FEEL SO MANY DIFFERENT...FEELINGS!"

    scene norikofirstvisit15
    with dissolve

    n "You know I can introduce you if you want, right?"
    a "M-Me? Meeting...N-N-Niki? No way...I couldn’t..."
    s "That’s probably for the best. She’s not as nice as you expect her to be."

    scene norikofirstvisit16
    with dissolve

    a "You be quiet! I don’t even know who you are anymore!"
    s "Hey, I’ve been prioritizing you all these years, haven’t I? Isn’t that worth something?"
    a "How many other secrets are you hiding from me?!"
    a "I bet you never tutored Noriko at all! I bet she’s a...prostitute!"

    scene norikofirstvisit17
    with dissolve

    a "No offense, Noriko. You’ve been very nice to me so far."
    n "I’m...not a prostitute. I’ve never even kissed anyone before."
    a "This is comforting information, but I still have a hard time trusting anyone who openly admits to loving my [uncle]."

    scene norikofirstvisit18
    with dissolve

    n "I totally get it, Ami."

    if bonus == True:
        n "You’ve loved him for pretty much your entire life, but you’ve never been able to have him because of societal expectations and the stigma surrounding familial romantic relationships."
        n "I’m in a similar boat. Just instead of being blood-related, I was like an in-law...and also way too [young]to actually date."
        n "You and I have a lot more in common than you think."
    else:
        n "I'm kind of a fucking freak."

    n "Also, can I try on your maid outfit?"
    s "That was a very strange time to ask that question."
    n "Gotta strike while the iron is hot. I just buttered her up. There’s no way she’ll say no now."

    scene norikofirstvisit19
    with dissolve

    a "Umm...Noriko?"
    n "Yes, Ami?"
    a "Why are you being so nice to me if you know I'm a rival of yours? "
    a "We might have hung out once or twice when we were little but...we’re not little anymore."
    a "And my best friend hates your guts..."
    a "I can’t just start acting all friendly with you...it would mess everything up."
    n "Hey. Listen to me."
    n "I am {i}not{/i} going to take your [uncle] away from you. Got it?"
    n "You’ll always be his number one. "
    n "But you can’t blame me for wanting to give you a run for your money when I’ve been watching him my entire life."
    n "If anyone knows what that’s like, it’s you."
    a "…"
    n "…"

    scene norikofirstvisit20
    with dissolve

    a "Why does she have to be so nice? How am I supposed to hate someone like this?"
    n "How about we just shelve all of that negative energy for a few minutes and go put on some cute clothes?"
    n "Sound good?"
    s "I can’t tell how much of this is genuine desire to appeal to Ami and how much of it is just fuel to get into a maid outfit."

    scene norikofirstvisit21
    with dissolve

    n "My relationship with your [niece] is just as important to me as looking cute in girly clothes."
    n "I don’t think I’ll apply to the maid cafe or anything, but I need to at least confirm to myself and everyone in this house that I {i}can{/i} be cute."
    a "Yeah...I guess I wouldn’t mind you wearing it for a little while."
    a "But Sensei has to wait out here so he doesn’t see you get undressed."

    if bonus == True:
        "Yeah. God forbid I see Noriko in her underwear."
    else:
        s "I agree. That would be inappropriate."

    scene norikofirstvisit22
    with dissolve

    n "Deal! "
    n "Do you think you can help me put it on? I’ve seen the uniform and there are like, a lot of parts to it. "
    n "I want to make sure I wear it correctly, so I’ll be counting on you if that’s okay."
    a "Yeah...sure. Of course."
    a "The um...chest area...might be a little tight, though."
    n "I’ll be fine. They’re smaller than they look. "
    a "If...If you say so..."

    scene black
    with dissolve

    "I find myself standing around for several minutes, waiting to be called into Ami’s room to see the results of...coercion?"
    "The only other person I’ve seen win over Ami so quickly was Sara, and that’s probably just because she called her cute a bunch of times."
    "I don’t want to jump the gun and say that Ami has {i}accepted{/i} Noriko yet, obviously..."
    "But this seems to be going a little too well."

    n "Sensei! It’s safe to come in now!"

    play sound "dooropen.mp3"

    "I open Ami’s door just seconds after being told it’s okay to come in."
    "And yes. I {i}was{/i} eagerly pacing back and forth in front of the door in anticipation."
    "So far, every girl I have seen in the maid outfit has looked adorable."
    "And even with Noriko’s hair as...meticulously disheveled as it is, I can’t imagine it will be any different for her."

    scene norikofirstvisit23
    with dissolve

    n "Good morning, Onii-chan! Sorry for taking so long, but it was suuuuuper hard trying to figure out how to put on this darned dress."
    s "Who are you and what have you done with Noriko?"
    a "Sensei...why was she so insistent on calling you Onii-chan?"
    n "Because Onii-chan is Onii-chan and I’m just the cute little girl next door!"
    s "You don’t have to try so hard with the persona. You're perfectly fine without it."
    s "Definitely much different than normal, but still perfectly fine."

    scene norikofirstvisit24
    with dissolve

    a "Okay...that’s enough compliments for the day."
    a "It’s one thing letting her dress up in my clothes, but I’m not going to just let you stand there and ogle at her until the cows show up."
    s "It’s “until the cows come home,” Ami."
    a "You’re dumb. No cows have ever lived here. This is no home for them."

    scene norikofirstvisit25
    with dissolve

    a "She is really cute, though."
    a "I like this look a lot more than her normal...outfit."

    scene norikofirstvisit26
    with dissolve

    n "Hm? Did I hear something about my normal outfit?"
    n "Do you want to try on my clothes, Ami? I think you’d look great."
    a "Oh. Umm...no thanks. You’re taller than me and...I’d want to take a shower first and stuff..."
    n "Okay~ I think you'd make a cute little punk, though."
    n "You should come out shopping with me sometime. I know a few spots at the mall that-"

    stop music
    play sound "doorbell.mp3"
    scene norikofirstvisit27
    with hpunch

    "The doorbell suddenly rings and prompts everyone to stop dead in their tracks."
    "It’s just a doorbell, so it may seem like an overreaction."
    "But I’m pretty sure all of us are thinking the same thing."

    s "Were you expecting anyone today, Ami?"
    a "I...uhm..."

    scene norikofirstvisit28
    with dissolve

    a "I think it..."
    a "I think it might be Maya..."
    a "She mentioned something earlier about coming over, but I didn’t realize she meant like...{i}today{/i}."
    n "…"
    s "So what do we do?"
    s "Should I go out and distract her while Noriko gets dressed and...hides in the closet or something?"
    a "No. Maya will obviously know something is going on if you go out to greet her."

    scene norikofirstvisit29
    with dissolve

    n "It’s fine..."
    n "I mean, she already hates my guts, so it’s not like her opinion of me will get any worse."
    s "And I’m pretty sure she never expected me to listen to her about staying away from you."

    scene norikofirstvisit30
    with dissolve

    n "You..."
    n "Chose me over her?"
    a "I’ll...handle Maya."
    a "Just...whatever you do, don’t come out of the room until you hear us leave."

    scene norikofirstvisit31
    with dissolve

    n "Ami..."
    a "I know. I don’t have to do this."
    a "And, to be honest, I really don’t want to."
    a "But...this is what’s best for everyone."
    a "And I...think Noriko is really nice, so..."
    a "Just hang out in here for a little while."

    scene norikofirstvisit32
    with dissolve

    a "But if you so much as {i}peep{/i} at her while she’s getting dressed, I will make sure both of you never live to see another day."
    s "Remind me to give you literally anything you want for the next...forever."

    if bonus == True:
        a "What I {i}want{/i} is for Noriko to go home as soon as Maya and me are gone."
        a "I might like her, but I still don’t want the two of you alone together."
    else:
        a "What I {i}want{/i} is for you to actually be home for supper every once in a while."

    s "Okay, Mom."
    a "If you’re gonna be smart about it then-"

    play sound "dooropen.mp3"
    scene norikofirstvisit33
    with dissolve

    a "Ah, shoot! She must have used the spare key!"
    s "We have a spare key?"
    a "Of course we have a spare key!"
    n "Umm...guys?"
    a "I know! I’m going! Keep quiet!"

    scene black with dissolve
    "………"
    "……"
    "…"
    scene norikofirstvisit34
    with dissolve2
    play music "amiawake.mp3"

    a "Hey, Maya! I didn’t realize you were coming over today."
    m "I texted you like four times and you didn’t respond to any of them."
    m "Why are you touching me?"
    a "I’m just...really happy to see you."

    scene norikofirstvisit35
    with dissolve

    m "You’re weird."
    a "Yeah. I guess I...am kind of weird."
    m "No, like you’re acting weird."
    m "What’s going on?"
    m "Is everything okay?"

    scene norikofirstvisit36
    with dissolve

    m "Is Sensei-"

    scene norikofirstvisit37
    with hpunch

    a "Taking a nap!"
    a "We got karaage on the way home and...his was raw and he’s...having stomach problems."
    a "And that’s...actually why I was about to leave."
    m "You’re not going to stay here and take care of him?"
    a "I...need to go buy medicine!"
    m "I should have some in my bag if-"
    a "He only likes medicine from brand new bottles!"
    m "…"

    scene norikofirstvisit38
    with dissolve

    m "What?"
    a "Y-Yeah..."
    a "So...how about the two of us go for a walk and then just...come right back."
    m "But my legs are so tired from-"

    scene norikofirstvisit39
    with dissolve

    a "I’ll buy you something watermelon flavored~"
    m "My legs suddenly feel a lot better."
    a "Great! Then...let’s get going, shall we?"

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    scene norikofirstvisit40
    with dissolve2

    m "…"
    a "…"
    a "Maya? What’s up?"
    a "We’ve gotta get a move on before-"
    m "Did you get new shoes?"
    a "Um...y-yeah..."
    a "Sensei just got them for me...but they’re a little too big."
    a "So we have to...take them back..."
    m "…"
    a "…"

    scene norikofirstvisit41
    with fade

    m "…"
    a "…"
    m "…"
    a "…"
    a "Maya?"

    scene norikofirstvisit42
    with dissolve2

    m "They’re nice."
    a "Th-thanks..."
    a "But I won’t be keeping them, so..."

    scene norikofirstvisit43
    with dissolve

    m "Yeah."
    m "I wouldn't expect you to."
    a "..."
    m "Let’s go."
    m "I’m hungry."
    a "…"
    a "Okay..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ norikoinvite1 = True
    jump norikoinvite2

label norikoinvite2:
...
```

## Code that triggers this event

File: (install folder)\game\NorikoEvents.rpy

Code:
```python
...
label norikoinvite:
    if norikoinvite1 == False and day != 6 and day != 7:
        jump norikoinvite1
...
```