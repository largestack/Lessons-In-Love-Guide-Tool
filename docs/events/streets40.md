# Unsung Heroes (Yumi)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Yumi love greater than or equal to 40

* Event [Neon Heart](./yumispecial40p2.md) (Yumi) is completed)



## Next events

* [Yumi: See You Around](./yumispecial45.md)

## Event properties

* Id: streets40
* Group: Yumi
* Triggered by label: streets
* Triggered by branch label: streets
* Triggered by path: streets->streets40

## Official wiki page

[Unsung Heroes](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=streets40&go=Go) for more details.

## Event code

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
label streets40:
    scene wintersky
    with dissolve2
    play music "justlights.mp3"

    "Ahh, snow."
    "Frozen water droplets guaranteed to fill the hearts of children with glee as they look outside of the window and realize there’s even a slight possibility of skipping school for a day."
    "I try to recall a time in my life where those kinds of thoughts would find their way into my head."
    "Now, any time I look up and see something like this, I just think of it as an inconvenience."
    "And so I take a moment to reflect on how things may have changed for me over the years."

    scene yumiporn1
    play music "yumiska.mp3"

    "But that moment is cut short the second I bump into Yumi."

    s "Yo."
    y "...Yo."
    s "Your bridge is a little further that way. You’re missing out on quality target practice."
    y "Not like there are any fuckin’ cars driving around in this weather anyway. "

    scene yumiporn2
    with dissolve

    y "And hey! I don’t just spend every waking moment spitting on cars, asshole. I’ve got better shit to do."
    s "Oh? Don’t tell me you went and found a job without me."

    scene yumiporn3
    with dissolve

    y "Nah. I haven’t even really looked since that whole...fiasco the other night."
    s "Then what is this apparent “better shit” you have to do that takes precedence over tormenting drivers and finding a way to put food on the table?"
    s "And don’t say “avoiding me” either because it’s clear that you’ve at least temporarily given up on that."
    y "Well...right now, I ain’t doing shit. But in a couple hours or whatever, I’m supposed to be meeting Chika around here to help her pick out a Christmas present for the brat."
    s "Chinami doesn’t need any Christmas presents. She has both a cell phone and a business now. Her life is complete."

    scene yumiporn4
    with dissolve

    y "Sorry to be the bearer of bad news but I’m almost confident that {i}business{/i} doesn’t actually exist."
    s "Almost?"
    y "Yeah, well, you never fuckin’ know with her."
    s "So what then? You’re just planning on standing around here for hours until it’s time to meet Chika?"

    scene yumiporn5
    with dissolve

    y "What the fuck else am I gonna do? Ask your [niece] to hang out? Go bowling with the fucking weird ponytail girl?"
    s "We have several weird ponytail girls now, so I’m not really sure which one you’re referring to."
    y "The watermelon one."
    s "Oh, Maya. "
    s "Yeah, don’t hang out with her. You two forming an alliance would be extremely irritating for me."
    s "But why not use this time to get back to job hunting if you don’t know what else to do?"
    s "You have me now. And you’re wearing your nice clothes and everything."

    scene yumiporn6
    with dissolve

    y "My other clothes are fucking fine! Eat a dick!"
    s "Sure. But these ones are...more fine."

    scene yumiporn7
    with dissolve

    y "Ugh...do we really have to do this job shit right now?"
    y "Because if I wind up running into someone I know for a second time in a row, I’m just going to give up on ever finding a job."
    s "Would you rather continue standing here together? We could try talking about our feelings. We’re both very good at that."
    y "Can I talk about how shitty it feels constantly being around you? Because I could probably kill a few hours that way."
    s "I mean...that’s typically what you talk about anyway. But if that’s going to be your attitude, I’ll put my foot down right now and start the job hunt without your consent."

    scene yumiporn8
    with dissolve

    y "What? You doing something without my consent? As if that would ever happen."

    if bonus == False:
        "She must be referring to that one hug."

    s "Hey, correct me if I’m wrong, but I was able to successfully restrain myself the last time you gave me an opening to go against that."
    y "Congrats on having the slightest shred of self control imaginable. It’s almost like you’re a real human being now."
    s "Are any of us truly {i}real{/i}, Yumi?"

    scene yumiporn9
    with dissolve

    y "You know what? Fine. At the risk of you getting all fucking philosophical, sure. Let’s go {i}job hunting{/i}."
    y "It might be fun trying to set the world record for refused applications or failed interviews or however I manage to fuck things up this time."
    s "Yumi, you’ve been rejected by like three places. That’s really not that bad."
    s "Plenty of adults get rejected by far more than that before finding a place to work."

    scene yumiporn10
    with dissolve

    if bonus == True:
        y "Really?! Because the fact that you were hired by a {i}school{/i} makes me pretty fucking doubtful of that!"
    else:
        y "Really?! Because the fact that you were hired by a {i}college{/i} makes me pretty fucking doubtful of that!"

    s "Touché. "
    s "Luckily for you, though, I have an idea of a place that I can’t imagine rejecting you at all."

    scene yumiporn11
    with dissolve

    y "What? Really? Well, then why the fuck did you wait until right now to tell me about it?"
    s "..."

    scene black
    with dissolve

    s "Anyway, follow me."
    y "Yo! I asked you a fuckin’ question! Don’t just start walking away!"

    "The truth is that I’m not {i}100%%{/i} confident Yumi will just be allowed to work here-"
    "But, at the same time, I’m not really sure if she’d {i}want{/i} to either."
    "But hey, if she’s truly desperate for work, she should be willing to go a little outside of her comfort zone."
    "And what better place to do that than one of my favorite local businesses that I’ve been all but banned from shopping at?"

    y "Wha-"
    y "Where the fuck do you think you’re taking me, creep?!"
    s "Just let it happen, Yumi."

    scene yumiporn12
    with dissolve

    y "Is this a fucking porn shop?!"

    if bonus == True:
        s "I like to think of it as an “adult entertainment center.”"
    else:
        s "Yes. But I really just come here for the romantic comedy DVDs."

    scene yumiporn13
    with dissolve

    if bonus == True:
        y "That’s just a fancy way to say it’s a porn shop, you fucking lunatic! I’m pretty sure I’m not even allowed to be in here!"
        s "Since when do you care about anything you’re {i}allowed{/i} to do?"
        y "Since there’s fucking porn involved! I can’t work here!"
    else:
        y "That's even fucking worse!"

    mak "Wha-"

    scene yumiporn14
    with fade

    mak "What is the meaning of this?! Are you out of your fucking mind?!"
    s "Do you have any job applications laying around?"
    mak "No! Leave!"

    scene yumiporn15
    with dissolve

    mak "And why on earth are you with {i}Yumi{/i} of all people?"
    y "Hm? You know me?"
    y "I ain’t ever seen you a day in my fuckin’ life. "
    mak "..."
    s "Go put your glasses on."

    scene yumiporn16
    with dissolve

    mak "Ugh..."

    scene yumiporn17
    with dissolve

    y "The fuck is even going on right now?"
    s "Nothing really. This is actually a pretty normal day for me, all things considered."

    scene yumiporn18
    with dissolve

    mak "..."
    y "..."
    y "Oh, no fucking way."
    mak "Leave. Now. Both of you."
    s "The service here really isn’t all that great, so clearly there’s a chance for you as an employee after all."

    scene yumiporn19
    with dissolve

    y "Wait, wait, wait, wait, wait..."
    y "You mean to tell me the fucking {i}class rep{/i} works at a porn shop? Is this some kind of prank?"
    s "Her family actually owns the place. "
    y "Yeah. Sure they do. I ain’t fallin’ for that shit. Now, where’s the real job?"

    scene yumiporn20
    with dissolve

    maki "What’s going on? We haven’t had this many people in the store since last Valentine’s Day."

    scene yumiporn21
    with dissolve

    maki "And who’s this? Another [niece] that I’m not finding out about until right now?"

    if bonus == True:
        maki "Maybe a mistress? Hooker? You two can hang out in the back room at a discounted rate, but you’ve gotta be quick since I need to clean the glass sometime before night comes."
    else:
        maki "Your taxes must be really complicated."

    mak "That is a classmate of mine, {i}mother{//i}."
    maki "Oh. Well, we don’t have a {i}student{/i} discount here, so you’ll have to pay full price. Still be quick, though."
    s "She’s actually looking for a job, Maki. And I figured somewhere like this might be a good opportunity for her."
    maki "You want to sell porn?"
    y "Uhh...not really?"

    scene yumiporn22
    with dissolve

    maki "I’ve gotta say, not a good start, Sensei. "
    s "Maybe you two just need some one-on-one time together? I’m sure if anyone is able to get Yumi to open up the wonderful world of adult entertainment, it’s you."
    mak "Wonderful, because that gives me the chance to talk to {i}you. Alone.{/i}"

    scene yumiporn23
    with dissolve

    maki "Works for me! Though, I am a little sad because Makoto gets the {i}family{/i} discount and I was really banking on some of that sweet, sweet back room revenue. "
    y "Uhh..."
    y "Wait, this...{i}isn’t{/i} just a prank then?"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene yumiporn24
    with dissolve

    mak "What are you doing?! Why are you here?! Why did you bring {i}Yumi{/i} here?! "
    mak "You know how important it is for me to keep my involvement with this place hidden!"
    s "From Yumi? What’s she going to do about it?"
    mak "Oh, I don’t know- use it as leverage against me? "
    mak "I’m pretty sure that Chika’s already {i}seen{/i} me here and that's bad enough! Now, the entirety of Dorm #1 knows!"
    s "Alternatively, you could just hire her. Then she’d be forced to keep it a secret as well."

    scene yumiporn25
    with dissolve

    mak "But why {i}here?!{/i}"
    mak "There are a million other places hiring [teenager]s! Why would you bring her to arguably the worst of all of those places?! Especially when you {i}know{/i} I don’t want you to?!"
    s "..."
    mak "Well?"

    scene yumiporn26
    with dissolve

    s "I thought it’d be funny."
    mak "You fucking-"

    if bonus == True:
        s "Besides, Yumi’s been through a lot lately. I figured something lighthearted like a trip to the local porn shop might brighten things up a bit for her."
    else:
        s "Besides, Yumi’s been through a lot lately. I figured we might be able to watch Fever Pitch starring Jimmy Fallon together. That always cheers me up."

    mak "You..."

    scene yumiporn27
    with dissolve

    mak "Certainly have a strange outlook on what sort of things would brighten up someone’s day."
    mak "Why not just...buy her flowers and give her a shoulder massage if you’re so worried about her?"
    s "..."

    if bonus == True:
        s "I also thought I could get here before your shift started and actually purchase something from your mom."
    else:
        s "I'm afraid that I'd like the flowers too much and keep them for myself."

    mak "Why?...{i}Why{/i} do I like you so much?"

    scene black
    with dissolve

    "........."
    "......"
    "..."

    scene yumiporn28
    with dissolve

    maki "So...you think you’ve got what it takes to be a porn saleswoman..."
    y "What? The fuck are you talkin’ about, lady? I just told you I don’t wanna fuckin’ work here."
    maki "Are you {i}sure{/i} you don’t want to work here? Or are you just saying that?"
    maki "Because, on the outside, a job like this might seem like a cesspool of debauchery...an unholy paradise of poon-"

    scene yumiporn29
    with dissolve

    maki "But what it really is...is a place where everyone is accepted! Where everyone is loved!"
    maki "Where no fetish is discarded! And no book is to be judged by its cover!"
    maki "Places like this shop are one of the last bastions of hope-"

    scene yumiporn30
    with dissolve

    maki "I’m sorry, what was your name?"
    y "..."
    y "Yumi."

    scene yumiporn31
    with dissolve

    maki "Well, Yumi...stick with me and I can guarantee you’ll see the light."
    maki "I know it might all be a little too intimidating to take in at once, but this job truly {i}is{/i} rewarding. People like my daughter and me are the unsung heroes of retail, you know."
    maki "No one likes to admit it, but as far as in-house sales go, no one is more likely to change a customer’s life than people like us."

    scene yumiporn32
    with dissolve

    maki "You’re a cute, [young]girl. I’m not sure what kind of family you come from or if they’d accept their daughter working a job like this, but I’d be willing to talk to them if you need me to. "
    y "Yeah...You don’t have to worry about talkin’ to my family or any shit like that."
    y "I still don’t know how I feel about workin’ in a place like this and, honestly, I still think it’s creepy as shit."
    y "But all that stuff about it bein’ a place where you can’t judge books by their cover...doesn’t sound all that bad, I guess."

    scene yumiporn33
    with dissolve

    maki "Right?! We’re all equals here! Me, you, and even the one woman who comes in once a week and buys nothing but vintage porno DVD’s starting with the letter Y! "
    maki "This is the holy grail, Yumi! I don’t know how much I can pay you, but if you’re willing to negotiate, I can have you start as early as next Monday night."
    y "Uhh...wait a second. I didn’t really agree to-"
    maki "I just need to know what kind of experience you have first."

    if bonus == True:
        maki "Does blood make you nauseous? What about comically large gangbangs or incest?"
        maki "Any hard limit on the size of a schlong before you start feeling nervous or worried about the pain and have to look away from the girl (Or guy) getting her (Or his) brains railed out?"
        maki "Also, can you agree to keep things confidential on the off chance that you find a family member or other loved one in a video?"
        maki "Because sometimes, whether we like it or not, people are forced to do things they’re not very proud of for money- and as a retailer in this industry, you need to be willing to be confidential about-"
    else:
        maki "How fast can you drive a go-kart?"
        y "A...go-kart?..."
        maki "Yes. I am forming a go-kart team with my daughter and you would be the third member."
        maki "Are you good at painting? How quickly do you think you could change a tire?"
        maki "Oh, and what do you think we should name it? I'd personally like to go with {i}Jimmy{/i} after my favorite character in Hero's Harem Guild."

    scene yumiporn34
    with dissolve

    maki "Wait! No! Don’t leave!"
    s "Excuse me, Makoto, but I think I have to go chase after Yumi now."
    y "Don’t bother! And never even think about bringing me somewhere as sketchy as this ever again!"
    maki "It’s not sketchy! It’s perfectly natural!"

    if bonus == True:
        maki "I am a good person! I’m making the world a better place, one orgasm at a time!"
        mak "MOM! STOP SAYING THAT!"
    else:
        maki "And what about the go-kart?!"

    scene black
    with dissolve2

    "Yumi is able to get away from me and, judging by the abruptness of her exit, I think it’s safe to assume she has no plan on working with the Miyamuras any time soon."
    "But hey, at least this time she made the conscious decision to not work somewhere instead of just being flat-out rejected."

    $ renpy.end_replay()
    $ yumi_love += 1
    $ streets40 = True
    stop music fadeout 5.0

    "{i}Yumi’s affection has increased to [yumi_love]!{/i}"
    "........."
    "......"
    "..."

    jump saturdaynight

label yumispecial45:
...
```

## Code that triggers this event

File: (install folder)\game\YumiEvents.rpy

Code:
```python
...
label streets:
    if yumiblock == True:
        "Something tells me I shouldn't try seeing Yumi right now..."
        jump satafternoonmenu
    if yumi_love >= 0 and firsttimestreets == False:
        jump firsttimestreets
    if yumi_love >= 5 and streets5 == False:
        jump streets5
    if yumi_love >= 10 and day44 == True and streets10 == False:
        jump streets10
    if yumi_love >= 15 and yumidorm15 == True and streets15 == False:
        jump streets15
    if yumi_love >= 20 and streets15 == True and ramen1 == True and streets20 == False:
        jump streets20
    if yumi_love >= 25 and yumidorm20 == True and streets25 == False:
        jump streets25
    if yumi_love >= 30 and onseninvite == True and streets30 == False:
        jump streets30
    if yumi_love >= 40 and yumispecial40p2 == True and streets40 == False:
        jump streets40
...
```