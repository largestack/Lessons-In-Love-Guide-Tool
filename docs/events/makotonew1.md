# Frogger (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Days since the start of the game greater than or equal to 55

* Event [Rising of the Tide](./pornshop10.md) (Makoto) is completed)



## Next events

* [Makoto: Sowing the Seeds](./makotonew2.md)

## Event properties

* Id: makotonew1
* Group: Makoto
* Triggered by label: weekdaymorning
* Triggered by branch label: weekdaymorning
* Triggered by path: weekdaymorning->makotonew1

## Official wiki page

[Frogger](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=makotonew1&go=Go) for more details.

## Event code

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label makotonew1:
    scene makotopool1
    with dissolve
    play music "10c.mp3"

    "Another day of school comes to an end and, like always (Or at least a fair portion of the time), I’m headed to my office to provide counseling to whoever happens to be in need today."

    mak "Oh, good. You’re still here."

    "Or not."

    scene makotopool2
    with dissolve

    mak "I need your help with something."
    s "Sorry, do I know you? "

    scene makotopool3
    with dissolve

    mak "Please don’t pretend you don’t know me just because I am actually asking for your help for once."
    s "Are you a new student here? If you’re looking for the staff room-"
    mak "It’s me. Makoto."
    s "No, Makoto wears glasses."

    scene makotopool4
    with dissolve

    mak "You see me without glasses all the time! "
    s "I have never seen you before in my life."

    scene makotopool5
    with dissolve

    mak "Fine. I guess I’ll just have to be the only one wearing a swimsuit after all."
    s "..."
    mak "..."
    s "Let me start by apologizing for not recognizing you."

    scene makotopool6
    with dissolve

    mak "That’s what I thought..."
    s "So, what’s this involving swimsuits? Are you joining the swim club or something?"

    scene makotopool7
    with dissolve

    mak "Oh, please. I’m busy enough with student council. There’s no way I’d have time for another club on top of that."
    mak "It’s just our class’s turn to clean the pool and, without your help, I’ll be doing it all on my own. Which I guess would be fine if not for the fact that I have work tonight."
    s "Remind me- where is it you work again?"

    scene makotopool8
    with dissolve

    mak "Oh, you know. The same place you nearly assaulted me the other night. Does that ring a bell?"
    s "..."
    mak "..."
    s "Makoto-"

    scene makotopool9
    with dissolve

    mak "I’m kidding."
    mak "I’ve chalked it up to just one big misunderstanding and don’t hold it against you for getting sucked up into a moment I never should have enabled in the first place."
    mak "{i}But...{/i}"
    s "I don’t like that “but.”"
    mak "{i}But{/i}, I still think it would be best if you would help me out with this tiny little chore. You know, since I’m so forgiving and kind and whatnot."
    s "You know that all you had to say was the swimsuit thing, right? I’ve already made up my mind and am ready to go whenever. "
    s "I obviously don’t have anything to wear, though, so you’ll have to do all of the cleaning yourself."

    scene makotopool10
    with dissolve

    mak "Oh, please. You really think I wouldn’t be prepared for something like this? I have a spare swimsuit for you in the left drawer of the desk in your office."
    s "Please don’t smuggle swimwear into my desk, Makoto. That’s not what I need an assistant for."
    mak "It clearly is since you’ll be putting it on immediately and meeting me near the pool."
    s "I don’t even know where the pool is. I’ve never been there before."
    mak "Well, I suggest you figure it out if you actually do want to see me in my swimsuit..."

    scene makotopool11
    with dissolve

    mak "Which...I guess is an actual thing I’ve said to my teacher now."
    s "Well, say no more. I’m on my way. But if this is just one big ploy to get me into a speedo, I’m going to have to give you detention."
    mak "I’m Makoto Miyamura. I’m immune to detention."

    scene black
    with dissolve

    s "We’ll see about that..."

    "Makoto and I part ways as I pick up where I left off before she showed up and continue heading to my office."
    "Unfortunately for whoever is facing emotional turmoil today, I won’t have any time for counseling."
    "Instead, I am going to have to pretend to clean a pool so as to not disappoint my very-easily-disappointed class representative."
    "All I can really say at this point (Apart from how little I want to actually expend energy after class) is that..."
    "Well, I hope her swimsuit is worth it."
    "........."
    "......"
    "..."

    scene makotopool12
    with dissolve2

    "It is."

    mak "I see you were able to locate the pool after all. Congratulations, Sensei. There’s a brush and a bucket behind you. "
    mak "The pool itself is cleaned by professionals, so we just need to take care of the perimeter."
    s "Can I have permission to say something mildly creepy right now?"

    scene makotopool13
    with dissolve

    mak "You’re actually asking for permission? That’s odd."
    mak "I suppose I can humor you by allowing you to say whatever sort of perverted thing you are about to say to me. So please, go ahead before I change my mind."
    s "Sure."
    s "Makoto, you are ridiculously hot and I wish you would wear that swimsuit literally everywhere."
    s "It’s hard to tell with your uniform on, but your body is essentially flawless and you are making it very hard for me to not achieve an erection right now."
    mak "Are you done?"
    s "I think so."

    scene makotopool14
    with dissolve

    mak "Good. That actually could have been a lot worse and I’m very proud of you for being able to mostly contain yourself."
    mak "Though, I do wish you’d remember that I’m a bit of a protege to you and that you are putting our relationship in grave danger every time you stare at me like that."
    s "Stop being so attractive and I’ll stop staring. It’s that easy."
    mak "Bucket. Now."

    scene black
    with dissolve

    s "You’re really bossy today, Makoto. I don’t like it."
    mak "The further out of line you get, the harder I have to push you back in. We’re already way behind schedule."

    "I do as Makoto says and retrieve a bucket of soap she must have pre-positioned near the entryway as well as a brush to just...hold and pretend I’m actually using."
    "Of course I’m not going to actually {i}clean,{/i} but as long as I can make her believe I am, I’m sure everything will work out okay."
    "........."
    "......"
    "..."

    scene makotopool15
    with dissolve

    s "Okay. Break time."
    mak "It’s been thirty seconds. "
    s "That’s it? I feel like we’ve been doing this for hours."
    mak "Your brush hasn’t even touched the tiles yet."
    s "Why were you assigned to do this on your own in the first place? There are nine other girls in the class. Couldn’t one of them have helped you instead of me?"
    mak "I wasn’t assigned to do this on my own. Yumi and Chika were supposed to help."
    s "Ah. Well, I guess there was never any chance for Yumi to actually contribute to something like this...but I’m surprised Chika didn’t show."
    mak "It very likely just slipped her mind. I’m sure she would have come if I reminded her. "
    s "Why didn’t you?"

    scene makotopool16
    with dissolve

    mak "Let’s just say I’m not the only person with prior obligations after school. "
    mak "Chika’s living situation doesn’t allow for a lot of extra time after school, so...consider this as me simply being a good samaritan."

    if chikadorm15 == True:
        s "I didn’t realize you were also aware of Chika’s {i}situation.{/i}"

        scene makotopool17
        with dissolve

        mak "Ahh. I take it you know as well, then. Why am I not surprised?"
        mak "Chika hasn’t directly told me what her situation is, but it’s pretty easy to figure out if you pay any amount of attention to her."
        mak "Always rushing home after school...being held back a whole year...forging signatures on permission slips..."
        mak "Anyone actually looking for an answer could easily find one. I just happened to be one of the few to look."
        s "..."

    else:
        s "What’s wrong with her living situation?"

        scene makotopool17
        with dissolve

        mak "Why don’t you try and find out yourself? She seems to like this new version of you. I doubt she’d be opposed to opening up once you get to know her a little more."
        mak "I’m simply doing my part as the class representative and making everyone’s lives a little bit easier whenever I can."
        s "..."

    scene makotopool16
    with dissolve

    mak "Any reason for the sudden bout of silence, Sensei? And don’t pretend to be too focused on work when I know you haven’t even started yet."
    s "You’re a really good person, Makoto."

    scene makotopool18
    with dissolve

    mak "Huh?..."
    s "It’s easy to do good things for someone when you’re getting something in return. But it takes a special kind of person to do those things for nothing."
    s "You’re not over here trying to leverage Chika’s position against her...and you haven’t even brought up disciplining Yumi for bailing on responsibilities you had to take on yourself."
    s "Not to mention all of the stuff you do for me..."
    s "You’re just a genuinely good person."
    mak "..."
    s "..."
    s "Any reason for the sudden bout of silence, Makoto? And don’t pretend to be too focused on work when you haven’t scrubbed in almost ten seconds now."

    scene makotopool19
    with dissolve

    mak "Sorry. That just took me by surprise..."
    mak "It’s been a while since you’ve genuinely complimented me like that and...I think...my heart might have skipped a beat or two."
    s "Well, don’t let it skip too many more because I don’t have a license and can’t drive you to the hospital."

    scene makotopool20
    with dissolve

    mak "It just...feels really good to be recognized. "
    mak "Sometimes, it feels like no one really notices me or...even thinks of how things would be {i}without{/i} me."
    mak "To a lot of the girls in our class, I’m just some roadblock between them and an exciting high school life."
    mak "And I’m sure that, in many ways, that’s completely  true. "
    mak "I know I can be a little anal when it comes to rules and regulations and stuff..."
    mak "But all I really want is to make sure everything plays out smoothly...To make sure no one gets held back by their circumstances or themselves."
    mak "And if that means shouldering a burden or two, that’s fine. I’m perfectly capable of handling small problems like that."
    s "Just don’t take on too many of them if at all possible. "
    s "That sort of thing can be dangerous."

    scene makotopool21
    with dissolve

    mak "Thanks, Sensei. "
    mak "That advice would have really resonated with me if you hadn’t been staring at my ass this entire time."

    scene makotopool22
    with fade

    s "..."
    mak "..."
    s "I have no idea what you’re talking about."

    scene makotopool23
    with dissolve

    mak "You should really be more careful, you know. The pool might be in its own building, but we’re still technically on school grounds."
    mak "Someone could show up any minute now."
    s "Good. That means they can clean instead of me."

    scene makotopool24
    with dissolve

    mak "Forgive me if this question is on the tasteless side, but since when are you even this...attracted to me?"
    mak "In the beginning of the year, it seemed like you barely even acknowledged I was a girl."
    mak "Now, it feels like I can’t do {i}anything{/i} without having to dodge your gaze like it’s a car in a game of Frogger."
    s "It might be safe to just assume it’s because I now directly associate you with pornography."

    scene makotopool25
    with dissolve

    mak "No, I..."
    mak "I think I started noticing this before you ever even found out where I work."
    mak "It was like you just...woke up one day and you were suddenly interested in me as more than just an understudy."
    s "Well..."
    s "Maybe I was?"

    "That {i}is{/i} what happened, isn’t it?"
    "I have no idea what sort of person the previous iteration of me was, but if he wasn’t attracted to Makoto...was he even really a person at all?"

    scene makotopool26
    with dissolve

    mak "Well...as long as you can promise me you’re not just toying with my heart or something...I think I can be happy."
    mak "If I found out that this was all just...some sort of game you were playing or...some sort of horrible joke..."
    mak "That..."
    mak "That would really hurt..."
    s "Why would I joke about something like this?"

    scene makotopool27
    with dissolve

    mak "Because you’re an adult..."
    mak "And behind all the sense and sagacity, I’m still just a vulnerable teenage girl."
    mak "I obviously look up to you...I...{i}admire{/i} you..."
    mak "I guess what I’m trying to get at is..."
    mak "It would be extremely easy for you to hurt me if you wanted to."
    mak "And I can’t figure out if you want to or not."
    s "I don’t {i}want{/i} to hurt you, Makoto. "
    s "I just can’t imagine a future where it doesn’t happen."

    scene makotopool28
    with dissolve

    mak "But...what does that mean? I don’t understand."
    s "It means that this isn’t a joke and that I’m not just messing around with your vulnerable, teenage heart."
    s "And that’s exactly what makes everything so much worse."
    mak "That alone isn’t {i}worse,{/i} Sensei. If you’re really not treating this as a game, I’m a lot more inclined to..."
    mak "To..."
    s "..."
    mak "..."
    s "To what, Makoto?"

    scene makotopool29
    with dissolve

    mak "..."
    s "..."
    s "Makoto-"
    mak "Uhh...uh-oh. I appear to have lost my balance."
    s" Makoto, come-"

    scene black
    with dissolve
    play sound "splash.mp3"

    mak "Oh no. Losing my balance has resulted in me falling into the pool."
    s "If you think I’m going to clean the rest of this myself, you- wait. What are you doing?"
    mak "Oh no. I am now losing control over my hands. What is happening to me?"
    s "Makoto, let go of my ankle."
    mak "I wish I could, Sensei. But I’m afraid it is too late."
    s "Don’t even think about-"

    play sound "splash.mp3"

    "Makoto tugs on my leg and sends me falling into the pool right on top of her. "
    "We remain underwater for several seconds, attempting to pull apart before returning to the surface."

    scene makotopool30
    with dissolve2

    "Our attempt at pulling apart doesn’t work as well as it could have."

    mak "..."
    s "..."
    mak "..."
    s "..."
    mak "Something..."
    mak "Something is poking me..."
    s "..."
    mak "..."
    mak "Is that-"
    s "Yup."
    mak "I see."
    s "..."
    mak "..."
    mak "I think..."
    mak "I think we should have a talk soon..."
    s "I don’t really like talks."
    mak "I don’t think I do either, but..."
    mak "I..."

    scene makotopool31
    with dissolve

    mak "I think you might like this one..."

    scene black
    with dissolve2

    $ renpy.end_replay()
    $ makotonew1 = True
    $ makoto_love += 1
    stop music fadeout 10.0

    "{i}Makoto’s affection has increased to [makoto_love]!{/i}"
    "………"
    "……"
    "…"

    jump afterschoolevent

label makotonew2:
...
```

## Code that triggers this event

File: (install folder)\game\script.rpy

Code:
```python
...
label weekdaymorning:
    "{i}[totaldays] Days have passed...{/i}"

    if totaldays > 24:
        $ everyday = True
        $ clichebath = True
        $ amiawake = True
        $ firstclass = True
        $ sleepover = True
        $ day5 = True
        $ day7 = True
        $ day8 = True
        $ day12 = True
        $ day14 = True
        $ day16 = True
        $ day20 = True
        $ day21 = True
        $ day24 = True

    if cafe20 == True:
        $ harukanumber = True
    if bar10 == True:
        $ saranumber = True
    if halloween11 == True:
        $ makoto_virgin = False
    if kirindate25 == True:
        $ kirin_virgin = False
    if makiinvite2 == True and makiskip == False:
        $ makisex = True
    if makiinvite2 == True and makiskip == True:
        $ makisex = False
    if ayanedorm10 == True:
        $ ayanenew1 = True
        $ ayanenew2 = True
        $ ayanenew3 = True
    if pornshop15 == True:
        $ makotonew1 = True
        $ makotonew2 = True
        $ makotonew3 = True
    if futabadorm15 == True:
        $ futabanew1 = True
        $ futabanew2 = True
        $ futabanew3 = True
    if amidorm10 == True:
        $ aminew1 = True
        $ aminew2 = True

    if totaldays > 21 and roomwithclocks == False:
        $ roomwithtrack = True

    $ v11check()

    if totaldays >= 5 and day5 == False:
        jump day5
    if totaldays >= 7 and day7 == False:
        jump day7
    if totaldays >= 8 and day8 == False:
        jump day8
    if totaldays >= 12 and day12 == False:
        jump day12
    if totaldays >= 14 and day14 == False:
        jump day14
    if totaldays >= 16 and firsttimedojo == True and day16 == False:
        jump day16
    if totaldays >= 20 and day20 == False:
        jump day20
    if totaldays >= 21 and firsttimestreets and day21 == False:
        jump day21
    if totaldays >= 26 and day26 == False:
        jump day26
    if totaldays >= 28 and day28 == False:
        jump day28
    if totaldays >= 30 and cafesugar == True and day30 == False:
        jump day30
    if totaldays >= 33 and day33 == False:
        jump day33
    if totaldays >= 36 and day16 == True and bar5 == True and day36 == False:
        jump day36
    if totaldays >= 40 and day40 == False:
        jump day40
    if totaldays >= 43 and amisroom10 == True and day24 == True and aminew1 == False:
        jump aminew1
    if totaldays >= 44 and day38 == True and day44 == False:
        jump day44
    if totaldays >= 48 and day48 == False:
        jump day48
    if totaldays >= 50 and cafe15 == True and day50 == False:
        jump day50
    if totaldays >= 54 and day54 == False:
        jump day54
    if totaldays >= 55 and pornshop10 == True and makotonew1 == False:
        jump makotonew1
...
```