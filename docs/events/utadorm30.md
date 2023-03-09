# Uta-chan
Uta event

[Back to event list](./../)

[Official event wiki page](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=utadorm30&go=Go)



## Event preconditions
✅Uta love greater than or equal to 30

❌Event "[Uta: After the Rain](./utamaid25p2.md)" is completed (event=utamaid25p2)



## Next events
None

## Event properties
* ID: utadorm30
* Group: Uta
* Triggered by label: utadorm
* Triggered by branch label: doorknock2

## Event code
File: \game\UtaEvents.rpy
Code:
```python
...
label utadorm30:
    play sound "knock.mp3"

    "I knock on Uta’s door, figuring that this might be a good time to ask her about what caused her to storm out of the love hotel the other day."
    "I also figure it’s a good time to return her underwear that I may or may not have used to pleasure myself multiple times."
    "And before you ask, yes. I washed them."
    "To be perfectly honest, I thought about keeping them instead. But the idea of her wearing them {i}after{/i} what I did is simply too good for me to pass up."

    u "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "The question now is whether I want to just drop them on the floor of her room without drawing any attention to it, or leverage this position of power to embarrass her."

    scene utadormpanties1
    with dissolve2

    u "Oh, Sensei! What’s up? I was actually just thinking about you."
    s "Was it about how you left your panties behind at the love hotel and how they’re currently stuffed into my pocket?"

    "I leverage my position of power to embarrass her."

    u "..."
    s "If you’re waiting for a punchline, there isn’t one."
    u "You...You’re just carrying around my panties?"
    s "I am."
    u "The...panties that I was wearing? The ones that I took off because they got soaked from the rain?"
    s "Is there something about that you’re not understanding?"
    u "Yes. The part where you took them. And the part where you stuffed them into your pocket. And the part where you are now confessing your evils to me instead of just keeping them and preventing this talk."
    s "I just figured you’d want them back after randomly storming out."

    scene utadormpanties2
    with dissolve

    u "Me storming out has nothing to do with whether or not it’s okay to just walk around with my underwear like they’re some kind of badge of honor!"
    u "You don’t see me walking around with your underwear, do you?"
    s "No. But I don’t wear underwear, so."
    u "What? But you wear jeans like, every day. Doesn’t that make you uncomfortable?"
    s "I find that my pants are off enough for that not to be much of an issue."

    scene utadormpanties3
    with dissolve

    u "Hah...You know, if I didn’t grow up with an older brother who saw my panties on the floor every time he came into my room, this would be a real shock for me right now."
    u "I expected better from you, Sensei. Especially after our night of passion together should have gotten all of that pent up energy out of your system."
    s "I can’t say that spending the majority of the night in there alone while waiting for the rain to stop was the happy ending I was looking for."

    scene utadormpanties4
    with dissolve

    u "Well, you’re smiling now, aren’t you? Which means that the ending had to be at least {i}kind of{/i} happy. Otherwise, you’d be all like, “Uta! I hate you and I’m keeping your panties!”"
    u "Or something. "
    s "Uta-"
    u "What? The conversation is over. Just toss the panties into the pile and we can move onto why I was thinking about you rather than what you did with my underwear."

    scene utadormpanties1
    with dissolve

    u "Wait, you didn’t actually do anything with my underwear, did you? Because that would be weird and gross and not entirely unexpected."
    s "Of course not."
    u "Are you lying to me, you panty-stealing coward?"
    s "No more than you’re lying to me about why you left the hotel."

    scene utadormpanties5
    with dissolve

    u "Hah...Sensei, it’s not really {i}lying{/i} if I just...don’t tell you certain things, is it?"
    s "Not really. But I think there’s an argument to be made about whether or not certain scenarios arise in which that {i}would{/i} be lying, right?"
    s "If I were to get a mysterious text and storm out of the room right now, you’d definitely think I was hiding something, wouldn’t you?"
    u "So, what? You want to know who sent me that message? Will that make you drop this?"
    s "It would be a start."

    scene utadormpanties6
    with dissolve
    stop music fadeout 20.0

    u "Well, sucks for you because I don’t even know."
    s "I don’t believe that."
    u "Believe whatever you want. If it was something I thought you should know, I wouldn’t have just left without saying anything."
    s "Didn’t you just say the other day that you want me to know more about you, though?"
    u "Do you remember what I said after that?"
    s "No. I tend to pick out the best parts of conversations and just hang onto those instead of letting whatever negative connotations they ride in on weigh them down."
    u "Well, {i}I{/i} remember, because both parts of what I said are still true."
    u "I {i}do{/i} want you to know more about me. I just don’t want you to know anything that might make you look at me differently."
    s "Is that not the purpose of learning more about someone? Changing the way you look at them?"
    u "Not when I already like the way we look at each other."

    scene utadormpanties7
    with dissolve
    play music "thesleepingcity.mp3"

    u "So anyway! That was embarrassing! But I’m glad we’ve finally moved on!"
    s "Have we?"

    scene utadormpanties8
    with dissolve

    u "You know, I like you a lot better when you’re not trying to pry into my personal life."
    s "I just want to know more about you. Whether or not that changes the way I look at you is up to me."
    s "Even if it does, though, wouldn’t that just mean I’m {i}not{/i} someone you want to get closer to anyway? Wouldn’t your interest be better spent on someone who will, you know, {i}understand{/i} you?"

    scene utadormpanties9
    with dissolve

    u "No."
    s "Why not?"
    u "Because it’s better for everyone if you never understand me. "
    u "It’s better if I’m Uta-chan."
    u "Uta-chan is the perfect girl who always makes the right decisions. Who cares about everyone else first and herself last."
    u "She never makes mistakes or does things she looks back on with regret."
    u "And that’s all Uta Ushibori ever does."

    scene utadormpanties10
    with dissolve

    u "W...Why do you want to get to know me, Sensei?"
    u "Why did you ask me to stop being Uta-chan when we were in that hotel?"
    u "What can Uta Ushibori do for you that she can’t? You love Uta-chan, right? You’ve asked her...err, {i}me{/i} to marry you like a billion times already."
    u "I’m...fine with just always being that if you want! I don’t have to swap back and forth if the change gets annoying or exhausting."
    u "It’s not like...It’s not like that’s not still part of who I am, you know? It’s all the best parts! I learned to separate them so that...so that we can all move forward and..."

    scene utadormpanties11
    with dissolve

    u "And not get caught in the thorns of decisions Uta Ushibori made."
    s "..."
    u "..."
    s "Our pasts aren’t what define us, you know."
    s "They might help shape us into who we become, but it ultimately rests on us to figure that out ourselves."
    s "If there are things you did in the past that turned you into the person you are today, even if those things are ten times uglier by comparison, I still want to know about them because they made {i}you.{/i}"
    s "Uta-chan is great because she’s perfect. But Uta Ushibori is great because she’s so heavily flawed."
    s "Uta Ushibori is great because she’s an actual human being who makes mistakes and {i}suffers{/i} for those mistakes. "
    s "And Uta-chan knows no suffering at all."
    u "Are you telling me you want me to suffer?"
    s "It might sound mean, but yeah. I am."

    scene utadormpanties12
    with dissolve

    u "Of course you’d be a sadist. Why am I not surprised?"
    s "If you’re going to flirt instead of {i}talk,{/i} at least do so in a way that-"

    scene utadormpanties13
    with dissolve

    u "I’ll talk. I just..."
    u "You’ll be the first person other than Io or my family who’s ever heard any of this."
    u "It’ll be with less, uhh...{i}specifics,{/i} though...because I still {i}am{/i} worried that you’ll figure me out one day and not want anything to do with me anymore."

    scene utadormpanties14
    with dissolve

    u "That would be a huge blow financially. And I don’t know if I’d ever be able to recover from losing my number one customer."
    s "I think Uta-chan is slipping out again."

    scene utadormpanties13
    with dissolve

    u "Right. Yeah."
    u "It’s hard to tell the difference sometimes."
    u "Uhh...let’s see..."
    u "So...um..."
    u "Okay, I guess the easiest way of putting it would be..."
    u "I’ve, uhh..."
    u "I’ve done some...{i}stuff...{/i}that I’m not very proud of in the past..."
    u "Impulsive stuff. Like...when I pulled you into the tea ceremony room the other day but, like...worse than that."
    u "A lot worse."
    u "Stuff that seemed like a really great idea at the time..."
    u "But...when you’re a little kid, it’s...uhh...it’s easier to not really understand the possible, uhh...consequences for your actions..."
    u "And so some of those great ideas wind up coming back to bite you."

    scene utadormpanties15
    with dissolve

    u "I, uhh...I guess I haven’t ever told you the real reason I moved here, have I?"
    s "You’ve told me about your dead grandpa a hundred times. I’m not sure if that’s the full story, though."
    u "That was part of it. But, uhh...the bigger part is that I was dealing with this, uhh...{i}issue{/i} back at home."

    scene utadormpanties16
    with dissolve

    u "That stuff about bad decisions and...consequences we don’t really think of when we’re that young..."
    u "Well, that...uhh...that put me into a pretty...unsafe position..."
    u "I kinda...may have had a bit of a...stalker problem..."
    s "How...big of a problem, exactly?"
    u "Uhh..."
    u "It was...pretty bad..."

    scene utadormpanties17
    with dissolve

    u "N...Nothing ever happened to me, though! He never laid a hand on me! I’m still a...a certified virgin and...it was really just the {i}prospect{/i} of something bad happening that landed me here!"
    s "You didn’t have to-"
    u "I wanted you to know that part! That I’m not...completely tainted yet! That I’m clean! I swear!"
    s "Uta-"
    u "It was just a series of bad decisions that I am still paying for in ways I never expected! Which is why I left the other day! Because I am {i}still{/i} paying for those things and..."

    scene utadormpanties18
    with dissolve

    u "Hahah...I said that I wouldn’t give you any specifics but, here I am, about to give you {i}all{/i} the specifics because I don’t want to cause any misunderstandings and..."
    u "You know, this story is a lot harder to tell to someone who isn’t family. I didn’t have to worry about any of {i}them{/i} leaving me because of stupid stuff I did."
    s "You don’t have to worry about me leaving you, either. Not over something like this."

    scene utadormpanties17
    with dissolve

    u "But you don’t even know the half of it yet, Sensei. This isn’t something that’s going to go away. We’ve {i}tried{/i} that. "
    u "The whole reason my brother is in jail is because he beat the guy who was stalking me until he couldn’t even move anymore. But the problem wasn’t {i}just{/i} him."
    u "The problem is {i}everywhere.{/i} The problem is {i}me.{/i} "
    u "{i}I{/i} am everywhere. "
    u "Do you understand what I’m saying?"
    s "I..."
    s "Understand that this is something we should probably shelve for right now. You’ve told me enough and I get that it’s overwhelming for you."

    scene utadormpanties19
    with dissolve

    u "Do you get it now? Why I have to be someone else?"
    u "I changed everything...Completely reinvented Uta..."
    u "But I still can’t shed the parts of me that made me have to change in the first place."
    u "The real me keeps wanting to bleed through...keeps wanting to do more things I {i}know{/i} are mistakes...but that doesn’t change a thing."
    u "This is just who I am."
    u "One big mistake."
    u "And nothing will ever change that."

    scene utadormpanties20
    with dissolve

    u "Which is why I didn’t want you to know."
    u "I wanted this to keep going without you ever realizing there’s another side to all of this."
    u "But I’m not allowed to want anything."
    u "I haven’t suffered enough yet."
    s "Well, as someone who claimed just moments ago that I {i}want{/i} you to suffer, I beg to differ."

    scene utadormpanties21
    with dissolve

    s "It seems to me that you’ve suffered more than enough. And I don’t know if the source of that will ever go away, but I’m sure it will probably become easier to deal with over time."
    u "I don’t think it will."
    s "Then don’t think at all."
    u "Not thinking at all just makes it harder to deal with when it comes back to bite me again. Which it always does."
    u "{i}I was just a kid, Sensei.{/i}"
    u "I had no idea what I was doing. I {i}still{/i} have no idea what I’m doing and I’m in high school now. "
    s "Something you did that long ago would never change the way I look at you today."
    s "And while I won’t say I’m thankful it happened as it’s clearly made your life very hard to manage, I will reiterate once more that I like both forms of Uta Ushibori."
    s "And that my opinion of you hasn’t lessened in the slightest."
    u "..."
    s "..."

    scene utadormpanties22
    with dissolve

    u "Hah..."
    u "Sharing your feelings is exhausting. I have no idea how Io does it literally all day every day."
    s "Yeah, but I’m sure there’s a lot I don’t know about her either."
    u "Course there is."

    scene utadormpanties23
    with dissolve

    u "Girls like us aren’t exactly open books. And even when you get us open, it’s like everything’s in a completely different language."
    u "I’m sorry for dumping that on you, Sensei. I tried to spare you, but you just kept on pushing and I ain’t good at dealing with stuff like that."
    u "It does feel a little better to...clue you in on the different sides of me, though. I was really worried that you’d see that as a big ole red flag and just book it once I started talking."
    s "Nah. You let me borrow your underwear for over 24 hours, so the least I could do was hear you out until the end."

    scene utadormpanties24
    with dissolve

    u "Thanks. But please download CashApp and shoot me some money next time you decide to do that. I’m letting you off the hook for last time as a free trial, but I’m charging hourly from now on."
    s "Noriko lets me borrow her underwear for free and hers are a lot fancier than yours."

    scene utadormpanties25
    with dissolve

    u "That offended me a lot more than I thought it would. A girl takes great pride in her panties, you know."
    s "Not enough pride to keep them on in a hotel, apparently."
    u "They were wet and I was uncomfortable. I regret nothing other than the fact that they wound up in your hands."
    s "Well, I’ll be more than happy to {i}make you comfortable{/i} in my own way next time."

    scene utadormpanties26
    with dissolve

    u "Saying that right after I open up about my history of impulsive and bad decisions? Have you no shame, Sensei?"

    play sound "phonebeep.wav"
    scene utadormpanties27
    with dissolve

    u "And now your {i}phone{/i} is going off?! You should know darn well you’re supposed to silence your phone during heart-to-hearts with a cute girl! You really {i}do{/i} have no shame!"
    s "It’s probably just Ami asking when I’ll be home for dinner."
    u "Damn that top contender and her unflappable uncle love! We’re supposed to be having a moment here!"

    scene black
    with dissolve
    play sound "phonebeep.wav"

    "I tap on my recent messages, expecting Ami’s name to show up at the top of the queue."

    stop music

    "But what I find is something completely unexpected."

    play sound "phonebeep.wav"

    if uta_custom_name != "":
        "{i}You have 1 new message from [uta_custom_name]!{/i}"
    else:
        "{i}You have 1 new message from Uta Ushibori!{/i}"

    play sound "static.mp3"
    scene utalolinude with flash
    stop sound
    $ renpy.pause(5, hard=True)

    u "Sensei? Is something wrong?"

    play sound "static.mp3"
    scene utadormpanties28
    with flash
    stop sound

    u "Is it Ami like you expected? Or is it Noriko asking when you’re going to return her fancy underwear?"
    s "..."
    u "..."
    u "Sensei?"
    s "It’s..."
    s "It’s nothing."

    scene utadormpanties29
    with dissolve

    u "Oh?"
    u "Don’t tell me it’s Princess Maya summoning you for a late night booty call?"

    scene utadormpanties30
    with dissolve

    u "Let me see your phone. I know how to deal with-"
    s "Don’t."

    scene utadormpanties31
    with dissolve

    u "Huh?"
    s "Don’t touch my phone."
    u "Oh. Uhh...sure."
    u "I wasn’t trying to get up in your bubble or anything."

    play sound "phonebeep.wav"
    scene utadormpanties32
    with dissolve

    s "I have to go."
    u "What?..."
    u "This isn’t just payback for how I left you hanging the other night, is it? Do you really have to go? Or are you just saying that?"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    s "I really have to go. But I’ll see you in school."
    u "Really? You can’t even stay just...a little while longer?"
    s "I can’t."
    s "I don’t want to make a mistake."

    "I leave Uta’s room."
    "The walk home does not cling to my memory."
    "But the glow of a dim blue light does as I indulge in the rotten fruit of her past impulses."

    play sound "phonebeep.wav"
    $ renpy.end_replay()
    $ uta_love += 1
    $ utadorm30 = True

    "{i}Uta’s affection has increased to [uta_love]!{/i}"
    "........."
    "......"
    "..."

    if day == 1:
        jump advancetotues
    if day == 2:
        jump advancetowed
    if day == 3:
        jump advancetothurs
    if day == 4:
        jump advancetofri
    if day == 5:
        jump advancetosat
    if day == 6:
        jump advancetosun
    if day == 7:
        jump advancetomon
...
```

## Code that triggers this event
File: \game\Dorm2Events.rpy
Code:
```python
...
label utadorm:
    if uta_love >= 5 and utamaid5 == True and utadorm5 == False:
        jump utadorm5
    if uta_love >= 10 and utadorm5 == True and day != 2 and utadorm10 == False:
        jump utadorm10
    if uta_love >= 15 and day != 2 and utamaid10 == True and utadorm15 == False:
        jump utadorm15
    if uta_love >= 30 and utamaid25p2 == True and utadorm30 == False:
        jump utadorm30
...
```