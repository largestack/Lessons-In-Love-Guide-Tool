# Disaster Lesbian (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Rin love greater than or equal to 55

* Event [No Strings Attached](./imanispecial1.md) (Main) is completed)

* Event [Too Blind To See](./futabainvite3.md) (Futaba) is completed)

* Day of week is not Tuesday



## Next events

None

## Event properties

* Id: rindorm55
* Group: Rin
* Triggered by label: rindorm
* Triggered by branch label: rindorm
* Triggered by path: rindorm->rindorm55

## Official wiki page

[Disaster Lesbian](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm55&go=Go) for more details.

## Event code

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label rindorm55:
    scene mommyshome1
    with fade
    play sound "knock.mp3"

    "I knock on Rin’s door and wait for her to answer."

    play sound "dooropen.mp3"
    scene mommyshome2 with dissolve

    ri "..."
    s "..."

    "Oh."

    ri "You’re not Rin."
    s "Shouldn’t...I be the one saying that to you? What are you doing in her room?"
    ri "Oh, you know. Just having a crisis. The usual."
    ri "Where’s Wakana? Or Imani?"
    s "Sorry to be the bearer of bad news, but I don’t usually take them to the dorms with me."
    ri "You come here often?"
    s "Are you hitting on me?"
    ri "I wasn’t trying to. "
    s "I was joking."
    ri "Oh."
    ri "Well, you’re not very funny."
    s "And you’re not very clothed."

    scene mommyshome3
    with dissolve

    ri "Yeah. Rin took my clothes to the laundry room so I’ve been stuck wearing this towel for the last twenty minutes. "
    s "I take it that means...you’re one of her moms?"

    scene mommyshome2
    with dissolve

    ri "I’ve been told that I am not allowed to reveal that information to anyone. "
    s "Would you rather I just assume you’re some sort of prostitute she hired, then?"
    ri "Hey. I may occasionally make out with random people I have only known for several minutes, but I’m certainly not a prostitute. "

    scene mommyshome4
    with dissolve

    ri "Though, there was one time in high school that I jerked off the singer of some band for a pair of front row tickets to a show."
    ri "Turned out later the show was free and it was all standing room, but hey. You live and you learn."
    s "I can’t tell if...that was supposed to be a joke or not."

    scene mommyshome5
    with dissolve

    ri "Honestly, man. My whole life is a joke right now, so go ahead and laugh at whatever you want. Just don’t tell Rin you saw me here. Or know that I’m her mom. Which I am. But I didn’t tell you that."
    ri "Anyway, want to come inside and hang out? I’m bored."
    s "Is it really a smart idea to be inviting me in when you just said literally ten seconds ago that I’m not supposed to know you’re here?"
    ri "Probably not. But since I have made nothing but poor choices over the last several months, I’m worried that breaking that pattern will lead to something even worse happening."
    s "Fine. But I don’t have any concert tickets to offer you in exchange for your services."
    ri "I downloaded that CashApp thing to send Rin money for a date last month. I can take that too if you also have the app."
    s "Okay, are you {i}actually{/i} a prostitute? Because I’m starting to think my joke was less of a joke than I intended."
    ri "Man, I don’t know {i}what{/i} I am anymore. But hurry up and come inside before anyone sees me dressed like this and thinks I’m a prostitute."

    play sound "dooropen.mp3"
    scene black
    with dissolve

    "I follow Rika into Rin’s room and..."
    "Check to see if I have CashApp installed."
    "........."
    "......"
    "..."

    scene mommyshome6
    with dissolve2

    ri "Look at us- like two peas on a bed. Hanging out on our own instead of in the company of a group."
    ri "We can finally play Yahtzee."
    ri "Not sure how fun it'll be with only two people, though."
    s "You know, I really should have guessed you were Rin’s mom the second I found out you had a daughter. I can see where she gets her...Rin-ness from now."

    scene mommyshome7
    with dissolve

    ri "No way. She’s way too level-headed and smart to be anything like me. My partner always said I’m just a few steps away from..."
    ri "From..."
    s "Don’t do it."

    scene mommyshome8
    with hpunch

    ri "GAAAAAAAAAAAAAAHHHHHH!!!!!"
    s "Okay. Have fun crying, I guess."
    ri "I’m not crying! I’ve moved away from the sad stage and am now in the angry one! "
    ri "I’m a grown woman living in my teenage daughter’s dorm room! Why is this happening to me?!"
    s "Wait, you’re {i}living{/i} here now?"

    scene mommyshome9
    with dissolve

    ri "Pathetic, right?"
    s "Kind of, yeah."
    ri "I won’t be here for long. Just trying to...get back on my feet, I guess. Start over."
    ri "Rin’s other mom is the one who technically owns our house, so when she told me to pack my shit and leave..."
    ri "Well, I packed my shit and left. No way am I getting arrested again. Jail is cold."
    s "You were...arrested?"

    scene mommyshome10
    with dissolve

    ri "You haven’t been?"
    s "Why would you just assume that someone else has been arrested? You barely even know me."
    ri "Dude, look where you are right now. If the wrong person showed up, you’d be in the back of a cop car in no time at all. And that shirt’s so thin you wouldn’t even survive intake."
    s "That’s...fair. But what were you arrested for?"

    scene mommyshome11
    with dissolve

    ri "Nothing fun. Went through a rebellious phase a while back. Lots of protests and breaking shit and maybe occasionally setting a building or two on fire."
    s "..."
    ri "We’ve all got our embarrassing background stories, though. Things don’t stay the same forever. "
    ri "I mean, just look at me now. I’m-"

    scene mommyshome12
    with dissolve

    ri "Wait...I’m even worse now. "
    ri "My life {i}sucks.{/i}"
    ri "And it’s totally shitty because, like...everything was great just a couple years ago."
    s "Did something happen? Because the impression I got from Rin is that you and your “partner” were doing really well together."

    scene mommyshome13
    with dissolve

    ri "We were. For a {i}long{/i} time. Like, I’m talking multiple decades..."
    ri "But one day, the spark just started fading. "
    ri "We tried making it work for Rin since we thought it would be good for her to grow up in a functional same-sex household, but somewhere around the time she started middle school..."
    ri "Things just...I don’t know. Felt beyond repair."

    scene mommyshome14
    with dissolve

    ri "I get it. I {i}hate{/i} it...but I get it."
    ri "There was always this feeling in the back of my head that the next fight would be the last. But when that feeling was finally {i}right...{/i}"
    ri "Well, turns out I wasn’t as ready as I thought I was."
    ri "It fucking blows, man. I really wanted things to work. Spent like half of my life with that woman."
    ri "But you can fall out of love just as easily as you fall into it. So...here’s hoping that the two of us manage to fall again someday. "

    scene mommyshome15
    with dissolve

    ri "So anyway! Tell me about Rin’s girlfriend since I still haven’t gotten to meet her!"
    s "She lives right upstairs in Dorm 8. Just go knock if you want to meet her that badly."
    ri "I thought about it. But Rin told me she’ll introduce us soon and that rushing things would make stuff weirder than it already is or something. Which is apparently pretty weird."
    s "They’re a...good couple, I guess. Otoha’s just a little uncomfortable about certain aspects of the relationship, I think."
    ri "Like the aspect where they both have vaginas?"
    s "Not how I would have worded it, but I think so."

    scene mommyshome16
    with dissolve

    ri "It’s like that with a lot of girls at first."
    ri "I lost count of how many I had feelings for only to find out later that they were “just experimenting.”"
    ri "I’m sure it’ll happen to Rin too, but...hey. Maybe she’ll luck out and get a good twenty-odd years with this Otoha girl in before {i}she{/i} gets kicked out and has to go live with {i}her{/i} daughter."
    ri "Man, I’m gonna be such a cool grandma."

    play sound "dooropen.mp3"

    s "Maybe...wait a little while longer before you start fantasizing about grandchildren."
    r "MOM!"

    scene mommyshome17
    with fade

    ri "Hi! Welcome home."
    r "What are you doing?! I told you not to answer the door for anyone!"
    ri "Yeah, but what if it was {i}you?{/i} I didn’t want you getting locked out of your own room for all eternity because you forgot your key."
    r "I {i}have{/i} my key!"
    ri "How was I supposed to know that?! I thought I was being considerate!"
    r "By letting my teacher into the room while wearing nothing but a towel?! Sensei is very weak to girls! Things like this aren’t good for his mental health!"
    s "Hey, you’re weak to them as well."

    scene mommyshome18
    with dissolve

    r "Yes! I know! And just imagine how things would go if a friend’s mom led {i}me{/i} into a cramped room wearing nothing but a bath towel! It would not end well!"
    s "That’s a fair point. What I’m hearing is this is all Rika’s fault and that I did nothing wrong by going along with it."
    ri "Rin, I know you’re embarrassed- but hear me out. I already {i}know{/i} this guy."

    scene mommyshome19
    with dissolve

    r "What? How? You live like a gajillion miles away. "
    r "Well...{i}lived.{/i} You live here now. But I’m like 99%% sure that’s against the rules, so I have no idea how I am going to make this work. Especially with you...opening doors for strangers."
    ri "But he’s not a stranger. I just said that. "
    ri "We’re actually drinking buddies."

    scene mommyshome17
    with dissolve

    r "You don’t even drink!"
    ri "I do now. {i}I am not the Mom you once knew.{/i}"
    r "What the fuck is going on right now?!"
    ri "You tell me! Imagine {i}my{/i} surprise when my drinking buddy showed up at my front door looking for my daughter."
    ri "I felt like a character in one of those Lifetime movies your other mom always watches."
    ri "Not to mention I’m barely even- wait! Where are my clothes?! You said you would wash them! I have an interview tomorrow!"

    scene mommyshome20
    with dissolve

    r "I {i}am{/i} washing them. It takes {i}time.{/i} This is something you would know if you didn’t always make Mom do your laundry instead of doing it yourself."
    s "Didn’t she just call {i}you{/i} “Mom” a second ago?"
    ri "We’re both “Mom.”"
    s "Doesn’t that get confusing?"
    ri "You’d think so, but not really. "
    r "Get up. Both of you."
    ri "But what if my towel falls off? I haven’t even given Sensei my CashApp yet and it wouldn't be fair to everyone else if he got to see something like that for free."
    s "I knew it. You {i}are{/i} a prostitute."

    scene mommyshome21
    with hpunch

    r "NOBODY HERE IS A PROSTITUTE! "
    ri "Oh, thank God. It’s always so hard asking your daughter if she’s selling her body. Now I know for sure."

    scene black
    with dissolve

    r "I SAID GET UP, DAMN IT!"
    "........."
    "......"
    "..."

    scene mommyshome22
    with dissolve

    r "Ugh...isn’t it supposed to be the mother who takes care of the daughter? How did all of this fall on {i}me{/i} all of a sudden?"
    ri "Hey, I took care of you for years. It’s up to the child to take care of the parents once they can’t function on their own anymore."
    r "You are 43. You are plenty “functional.”"

    scene mommyshome23
    with dissolve

    ri "I’m 42! There is a big difference!"
    r "Not really!"
    s "I take it your house was always pretty loud, wasn’t it?"

    scene mommyshome24
    with hpunch

    riri "Shut up!"
    s "Well, fuck me I guess."

    scene mommyshome25
    with dissolve

    r "Mom, I’m happy to have you here. I don’t even mind sharing a bed with you while you look for a new place. But {i}please{/i} be careful."
    r "Not only do I want Otoha’s first impression of you to be, you know...{i}normal,{/i} but showing yourself around here could get me in trouble. And I can’t risk that right now. I {i}like{/i} school."
    ri "How come Sensei can show himself around the dorms, but I can’t? He has a penis and penises are dangerous. I have seen things."
    s "What does that even mean?"
    r "Can we not talk about Sensei’s gigantic penis and focus on the matter at hand, please?"

    scene mommyshome26
    with dissolve

    ri "Wait a second...how do you know it's a {i}gigantic{/i} penis?"
    r "I...don’t. I just...you know."
    ri "..."
    r "..."

    scene mommyshome27
    with dissolve

    ri "..."
    s "Hey, don’t look at me. I haven’t done anything sexual with your-"

    scene mommyshome28
    with hpunch

    ri "Hm!"
    s "Welp. Guess this is happening now."
    r "Mom! What the fuck are you doing?! That is literally sexual assault!"
    s "Leave it to a convicted felon to grab someone’s crotch without permission."

    scene mommyshome29
    with dissolve

    r "You’re a convicted felon?!"
    ri "I was planning on telling you on your twentieth birthday."
    r "What kind of present is that?!"
    ri "Also, for the record, you were right. This thing is intimidating. Stay away, you hear me? They’re {i}dangerous.{/i}"

    play sound "dooropen.mp3"
    scene mommyshome30
    with dissolve

    f "Rika! You really {i}are{/i} here!"

    scene mommyshome31
    with dissolve

    f "I thought Rin was just joking when she said you were coming to live with us, but-"
    ri "..."
    f "..."
    r "Hah..."

    scene mommyshome32
    with hpunch

    ri "Hey, Futaba! How’s it going?!"
    ri "Nothing to see here. Just checking the size of your teacher’s penis. You know how it is."
    f "Uhh..."
    s "I really didn’t have anything to do with this."

    scene mommyshome33
    with dissolve

    f "I’m just...going to forget I saw that, since...that would...probably be best for everyone..."
    ri "You stay away from it too, you hear me? That thing could cause some major damage to a delicate flower like you."

    "Joke’s on you, Rika. It already has."

    f "I will...be sure to keep that in mind."
    r "..."
    s "..."
    s "What? Why are you looking at me like that?"
    r "I need somewhere to direct my anger. Futaba is a cinnamon roll and all of my rage just bounces off of my mom. You are the only target I have left."
    s "It’s not fair that I am now the sponge for your anger when the only reason I am here right now is because I wanted to talk to {i}you.{/i} I did not ask to be groped."

    "But that doesn’t mean I didn’t like it."

    scene mommyshome34
    with dissolve

    ri "How are things going for you, Futaba? Good? Because my life’s a fucking mess right now."
    f "I’m sure you’ll be back on your feet in no time at all. Our room is your room."
    r "Yes. Hooraaaaay."
    ri "Come on, Rin. Would it kill you to sound a little more excited? I might be homeless, but I’ve still got more money than you. I think."
    ri "I hope."
    ri "And I’m full of awesome bisexual knowledge that I can bestow on you to make sure your relationship goes well."

    scene mommyshome35
    with dissolve

    r "My relationship is going just fine! I don’t need your “awesome bisexual knowledge” when that’s, like...the {i}one{/i} thing I’m really good at!"
    s "{i}Are{/i} you good at it? Because most of the time it seems like it’s your greatest weakness."
    ri "Aww, my little girl’s a disaster lesbian just like her mom."

    scene mommyshome36
    with dissolve

    r "Okay! That’s it!"
    r "Sensei, a word please? {i}Outside?{/i}"
    s "Ugh...fine."
    s "But only because I feel like you might actually pop a blood vessel if you stay in here for any longer."

    scene black
    with dissolve2
    stop music fadeout 12.0

    "Rin storms out of the room and I follow closely behind, leaving Rika and Futaba to...continue embracing one another while I step {i}away{/i} from girl on girl contact and into the hall."
    "Not being quite sure of how much Rin even {i}knows{/i} about Rika’s situation, though...I’m not really sure how I’m going to approach this “talk” we’re about to have."
    "The fact that Rika and...whatever the name of Rin’s other mom is were concealing the decaying nature of their relationship from her makes me feel like...well, like I shouldn’t reveal it either."
    "But without being directly told {i}not{/i} to do that-"
    "I’m not really sure how things will end."

    $ renpy.end_replay()
    $ rin_love += 1
    $ rindorm55 = True

    "........."
    "......"
    "..."

    jump rindorm55p2

label rindorm55p2:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label rindorm:
    if rin_love >= 5 and cafesugar == True and rinfirstvisit == False:
        jump rinfirstvisit
    if rin_love >= 10 and cafe10 == True and rindorm10 == False:
        jump rindorm10
    if rin_love >= 15 and rindorm10 == True and rindorm15 == False:
        jump rindorm15
    if rin_love >= 20 and cafe20 == True and day50 == True and rindorm20 == False:
        jump rindorm20
    if rin_love >= 25 and rindorm20 == True and rindorm25 == False:
        jump rindorm25
    if rin_love >= 30 and day != 2 and cafe30 == True and rindorm30 == False:
        jump rindorm30
    if rin_love >= 35 and rindorm30 == True and rindorm35 == False:
        jump rindorm35
    if rin_love >= 40 and cafe40 == True and day != 2 and day != 6 and day != 7 and rindorm40 == False:
        jump rindorm40
    if rin_love >= 50 and cafe50 == True and day != 1 and rindorm50 == False:
        jump rindorm50
    if rin_love >= 55 and imanispecial1 == True and futabainvite3 == True and day != 2 and rindorm55 == False:
        jump rindorm55
...
```