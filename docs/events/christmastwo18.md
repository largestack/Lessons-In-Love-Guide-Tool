# Me Without You (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Spotless Mind](./christmastwo17.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: christmastwo18
* Group: Main
* Triggered by label: christmastwo17
* Chain sources: christmastwo17
* Chain sources path: christmastwo17

## Official wiki page

[Me Without You](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=christmastwo18&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label christmastwo18:
    "I can’t just stay up here. "
    "But I can’t just get up either."
    "Especially not with the weight of years worth of lost time and thousands if not millions of self-inflicted misdirections pressing down upon me."
    "Niki isn’t the only person who wants to see me right now. That much is an indisputable fact."
    "But-"
    "Right now-"
    "She is the one {i}I{/i} want to see."
    "Maybe it means something, maybe it doesn’t."
    "I’m in no condition to explain it- and I likely won’t be for quite some time."
    "But I can’t keep her waiting when she’s already waited this long."

    play sound "phonebeep.wav"

    s "{i}I’m on my way.{/i}"

    scene black
    with dissolve2

    "The walk downstairs is a painful one, and not just because my legs haven’t yet recovered from being tethered to what felt like another dimension."
    "It’s painful because even if everything goes perfectly once I make it outside of the hotel, the second I head back in, it will be reduced to fragments once again."
    "Past or no past, things are different now."
    "Remembering one thing does not change that."
    "In fact, up until a few minutes ago, I was under the impression that remembering anything at all could kill me."
    "But I feel more alive right now than I have in a long time."
    "I just don’t know if that’s good or not."

    play sound "phonebeep.wav"

    "My phone goes off again...probably because Niki is tired of waiting and-"

    s "..."

    "Oh."
    "Apparently it’s something else."

    m "{i}Hey. It’s Maya. Where are you?{/i}"

    "Thankfully, this seemingly endless loop of stairs gives me enough time to respond without a fiery pink haired girl clapping back at me for not paying enough attention to her."

    s "{i}I didn’t realize you had my number.{/i}"
    play sound "phonebeep.wav"
    m "{i}I’ve had it this whole time. I just didn’t want you bothering me more than you already do.{/i}"
    s "{i}Fair enough. But why do you want to know where I am?{/i}"
    play sound "phonebeep.wav"
    m "{i}Because I want to see you.{/i}"
    s "..."
    play sound "phonebeep.wav"
    m "{i}Can you come up to the roof? I’ll be there shortly. I just have to do something else first.{/i}"

    "Did Maya just...actually say she wants to see me?"
    "There’s way too much happening all of a sudden. So much that I’m starting to question exactly how much of tonight has even been real."

    s "{i}Didn't you say the roof was closed earlier?{/i}"
    play sound "phonebeep.wav"
    m "{i}It was.{/i}"
    play sound "phonebeep.wav"
    m "{i}I guess someone must have unlocked it. I don't know. Are you coming or not?{/i}"
    s "{i}Sure. But I also have to do something else first.{/i}"
    play sound "phonebeep.wav"
    m "{i}That’s fine. See you there.{/i}"

    "My phone goes back into my pocket."
    "My legs go back to work."
    "........."
    "......"
    "..."

    $ mayanumber = True

    scene nikilove1
    with dissolve2

    "I find Niki and-"

    ni "I love you, okay?!"

    "And {i}that{/i} happens."

    ni "I know that Noriko gave you all of my letters and I want you to know that-"
    s "Niki-"
    ni "Shut the fuck up and let me finish!"
    ni "I know that you probably think I’m insane for waiting for you for so long and, you know what?! Maybe I am!"
    ni "But I never stopped thinking about you! Even when I dedicated my entire fucking life to making it so you could never run away from me ever again!"
    ni "I wanted to follow you everywhere! And since I couldn’t do it in person, I did it through the radio! TV! Billboards! Everything!"
    ni "I wanted to be there every second of your miserable fucking life because I can’t stand the thought of mine without you!"

    scene nikilove2
    with dissolve

    ni "Look at me! I’m screaming my fucking lungs out on Christmas in some random ass hotel where I could get caught at any second! And I don’t care!"
    ni "I don’t care if anyone sees this and posts it on the fucking Internet or tries to blackmail me or anything! I literally don’t care!"
    s "I feel like that’s something you’ll wind up regretting once you’ve actually thought about it rationally."
    ni "You’re not fucking getting it. I {i}can’t{/i} think about anything rationally anymore."
    ni "You ripped my heart and my mind to shreds and becoming...{i}this?{/i} This is just the glue I used to put it all back together."
    ni "It doesn’t look the same. It doesn’t feel the same. Literally {i}nothing{/i} about it is the same and it’s because I {i}know{/i} now that I can never be {i}me{/i} without {i}you.{/i}"

    scene nikilove3
    with dissolve

    ni "Come home."
    ni "Come be with me."
    ni "Come stay in fancy hotels and eat junk food and watch Gunfighter Z until we pass out."
    ni "It’ll be exactly the same as it used to be, just...not in my parents’ house. Which I think is a pretty sweet improvement since all they ever did was get in the way anyway."
    s "Niki-"
    ni "I love you. More than you can ever fucking imagine. I love you so much."
    s "I know you do."
    s "I finally remembered something a few minutes ago when I was reading your letters."

    scene nikilove4
    with dissolve

    ni "What? Really? What was it?"
    s "Just a random night. "
    s "We were in your room on Christmas watching that same anime you just mentioned. "
    s "Your parents were having a party downstairs and-"
    ni "That was the first night we kissed."
    s "What?"
    ni "Yeah. You teased me about blushing and I got really embarrassed and spent the rest of the night trying to prove that I didn’t think of you that way."
    ni "I failed miserably."
    s "Yeah...it sounds like it."

    scene nikilove5
    with dissolve

    ni "So {i}that’s{/i} what you remembered before anything else, huh?"
    ni "I always figured that since we didn’t really {i}get together{/i} until way later that...you had kind of just...forgotten about it."
    ni "Well, you {i}did{/i} forget about it. But I’m talking about, like...{i}before{/i} you..."
    ni "..."
    ni "God, we’re so fucking old now."

    scene black
    with dissolve2

    "Niki shows no sign of stopping anytime soon and moves closer to me."
    "I haven’t been able to really get any words in, but I figure that might be for the best since anything I could possibly say right now would just crush her feelings as if they were an insect underfoot."
    "I don’t want to do that to her."
    "Especially not when the vast majority of insects die in less than a year to begin with."
    "I’ll let this one live for now."
    "It interests me."

    scene nikilove6
    with dissolve2

    ni "So, uhh...are you going to keep those letters? Because, if I remember correctly, I might have said a lot of really mean stuff in some of them and I’d prefer you didn’t see any of it."
    s "You say a lot of really mean stuff in person, too. I doubt it would affect me all that much."
    ni "Well it clearly affects you in {i}some{/i} way, seeing as they helped chip away at that {i}amnesia{/i} of yours."
    s "It’s a little upsetting that the memory didn’t last long enough for me to see that kiss."
    ni "What kind of weirdo wants to watch his younger self kiss a little girl?"
    s "I just meant that it might be a nice thing to remember. I didn’t mean it in a weird way."

    scene nikilove7
    with dissolve

    ni "You know we can always just make {i}more{/i} memories, right?"
    ni "As great as the old ones are, you can rely on me to fill in the gaps and tell you about all of the important stuff."
    ni "I’ll say it again. {i}Be{/i} with me. For real this time."
    ni "We’re not awkward teenagers anymore. We can do it right this time. "
    s "What happened to not wanting a relationship?"
    ni "What {i}happened{/i} is I stopped lying to myself."
    ni "Noriko helped push me in the right direction as well which, honestly, I was not expecting at all."
    ni "I really thought she was going to go all-in on winning you over in my place."
    ni "And, all things considered, I’m glad she didn’t because I would have broken her fucking neck."
    s "Aren’t idols...not allowed to date, though? "

    scene nikilove8
    with dissolve

    ni "Nope. So either I can be an extremely rare exception to that rule or...I can just graduate."
    s "You’re going back to school?"
    ni "What? No. It’s like the idol version of retiring."
    s "You love your career, though. Why would you give that up?"
    ni "Obviously because there’s something else I love more."
    s "Niki, you-"

    scene nikilove9
    with dissolve

    ni "The way I look at it is this..."
    ni "I became an idol to make you jealous and regretful and, instead, wound up winning over nearly everyone {i}except{/i} you."
    ni "You don’t give two shits about how famous I am. So even if I like it, the plan kind of failed."
    ni "I don’t have to rely on the media to reach you anymore. I can fit your address and contact information in the palm of my hand."

    scene nikilove10
    with dissolve

    ni "So...if you’ll have me again...I’ll give all of that up."
    ni "I have plenty of money. And my contract with the agency says that I’ll still make royalties even if I’m fired or decide to quit. "
    ni "Let’s start over."
    ni "We were meant for each other. I know it."
    ni "Don’t you want that again?"
    ni "Don’t you think that the key to not feeling so empty all the time is to stick with someone who knows what’s missing?"
    s "What if I don’t, though?"

    scene nikilove11
    with dissolve

    s "What if I don’t think that starting over with you is the right idea? What if I don’t want to {i}be{/i} with you the way you want to be with me?"
    ni "Then you’re a fucking idiot. I’m a catch. {i}And{/i} I can do that thing with my tongue where-"
    s "Niki, wait."
    ni "Fine. But you know the thing I’m talking about."
    s "I just...can’t make a change as big as this right now."
    ni "Then when? Because I want to say I’m not going to wait around forever, but that would obviously be a lie when I am this...well, {i}addicted{/i} to you."
    s "I’m a horrible thing to be addicted to."
    ni "I sometimes think it would have been safer to just start doing drugs."
    s "Listen, you-"

    scene nikilove12
    with dissolve

    ni "No. {i}You{/i} listen! "
    ni "I’m obviously not expecting you to drop the whole life you made for yourself out of thin air because I decided to {i}re{/i}-confess..."
    ni "But I’m throwing out a bunch of ideas because, no matter what happens, I want to be with you!"
    ni "That’s all I’ve ever wanted for as long as I’ve known you!"
    ni "And sure, it was just as friends at first. But I will never, in a million lifetimes, {i}ever{/i} be able to do that again!"
    ni "Not when I know how fucked up and empty my {i}amazing{/i} life is without you in it."
    s "I still {i}am{/i} in it, though."
    ni "Yeah, but you're not in the right fucking place! "
    ni "Look at us! Look at who we are on the inside now!"
    ni "We’re ugly and empty and lonely and hurting and all of those things were a lot less scary when we had each other to fall back on!"
    ni "Let me fall on you again! Be there for me and I’ll be there for you! Until we’re old and jaded and I can’t do the tongue thing anymore!"
    s "Okay, you really need to stop yelling."
    ni "Then fucking kiss me and {i}make{/i} me stop, damn it! I’ve been waiting for it this entire time!"
    s "Niki-"
    ni "Screw it! I’ll do it myself!"

    scene nikilove13
    with dissolve2

    "Niki pulls herself forward in a violent lunge that manages to transform into a light push at the very last instant."
    "Her lips press against mine, the same way they did on Christmas night many years ago when we decided to change our relationship forever."
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

label christmastwo19:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
ni "W-Well of course you’d rather hang out with me than some kid. That’s barely even a compliment."
    s "Then why are you blushing so much?"

    scene norikospresent22
    with fade

    ni "I...I’m not blushing! It’s just hot in my stupid room because my parents won’t turn the stupid heat off!"
    s "Don’t you have a thermostat in here? Just turn it down yourself if you’re hot."
    ni "Yeah, but...I don’t know how to use it..."
    s "You’re completely helpless, aren’t you?"
    ni "If you’re so smart, why don’t you do it?!"
    s "Because you’re not actually hot. You’re just saying that."
    ni "Why would I lie?! Also, shut up! Gunfighter is about to come on!"

    scene norikospresent23
    with dissolve

    s "I’ll just turn the heat down myself."
    s "Even if your parents would get mad at {i}you{/i} for doing it, they-"

    scene norikospresent24
    with dissolve

    s "..."
    ni "..."
    ni "[[REDACTED]? What’s wrong?"
    s "I..."
    s "Nothing."
    s "I’m fine."
    s "I’m actually feeling a little cold, though...so I don’t think I’m going to turn the heat down after all."
    ni "Cold? Oooooh...{i}maybe there’s a ghost in the room?{/i}"
    s "Yeah...maybe..."
    ni "[[REDACTED], no. I was obviously kidding. There’s no such thing as ghosts. They’re-"
    n "{i}You’re such a good boy.{/i}"

    play sound "static.mp3"
    scene norikospresent25 with flash
    stop sound

    n "{i}It’s no wonder I fell in love with you.{/i}"
    n "{i}You try so hard to keep this side of you away from everyone that when it finally comes out, you just seem a million times cuter.{/i}"
    n "{i}You know, the best part about being in second place is that even if I don’t win, I always have a really clear view of the goal.{/i}"
    n "{i}I’ll keep running, Sensei. Forever and ever. Even when I know I can’t win.{/i}"
    n "{i}Even when my legs give out.{/i}"
    n "{i}And, who knows? Maybe the next obstacle I put down will wind up knocking someone else over instead of me.{/i}"

    scene norikospresent26
    with dissolve

    n "Merry Christmas."
    n "Maybe next year I’ll get you a present that doesn’t immediately make me cry."
    s "I..."
    s "I remembered something..."
    n "Was it nice?"
    s "..."
    n "I bet it was."

    scene clearnightsky
    with dissolve2

    play sound "phonebeep.wav"

    "My phone suddenly goes off in my pocket."

    n "Looks like my time here is up..."
    n "You better answer that, Sensei."
    n "I bet it’s someone really important."
    s "..."

    "Noriko leaves the roof and I struggle to regain enough control of my hands to reach for my phone."
    "I look down at one of the letters and notice that I’ve been gripping it so tightly that it’s begun to crinkle and tear."
    "I can still see it- the vision of an old bedroom."

    if bonus == True:
        "The scent of baked goods leaking in through the crack under the door and the feeling of my dick going numb from having to lie on it for so long to conceal an erection."

    "I can still imagine her face and the hue of her cheeks when I called her out for blushing."
    "But why {i}that{/i} night?"
    "Why would I recall something so small and insignificant when I’m sure there were thousands of other memories I made with her that were ten times bigger?"
    "I don’t know."
    "I don’t know anything other than the fact that it’s true now. That Niki is who she says she is."
    "And so is Noriko, even if her new fascination is taking over the role of a martyr in an effort to get me back together with someone who she both loves and loathes all at once."

    play sound "phonebeep.wav"

    "My phone goes off again."
    "I place the letter back inside of the box, closing it tightly and subconsciously reaching for the tape that had been carried off the ledge just moments ago."
    "Of course, I grasp nothing but the air itself."
    "But then-"
    "I recover enough control to gaze into a small, electric rectangle and see who the cause of these beeps has been."

    ni "{i}Come downstairs right now. I know you’re up there. I need to talk to you. It’s important. Please.{/i}"
    ni "{i}I’ll be in front of your hotel. Noriko gave me the address. And come alone. Don’t bring her. Please.{/i}"
    s "..."

    $ renpy.end_replay()
    $ christmastwo17 = True

    jump christmastwo18
...
```