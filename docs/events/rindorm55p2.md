# Hot Boy Summer (Rin)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Disaster Lesbian](./rindorm55.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

* [Main: Metronome In Love](./rikaspecial1.md)

## Event properties

* Id: rindorm55p2
* Group: Rin
* Triggered by label: rindorm55
* Chain sources: rindorm55
* Chain sources path: rindorm55

## Official wiki page

[Hot Boy Summer](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=rindorm55p2&go=Go) for more details.

## Event code

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
label rindorm55p2:
    scene rinoutsidemom1
    with fade
    play music "summerwind.mp3"

    r "Dude! How come you never told me you knew my mom?!"
    s "How come you never told me she was so hot?"

    scene rinoutsidemom2
    with dissolve

    r "Wait, really? You think so?"
    s "Do..."
    s "Do you {i}not?{/i}"

    scene rinoutsidemom3
    with dissolve

    r "I don’t know. Not really? I guess I’ve never thought of it before."
    r "..."
    s "..."
    r "Yeah, I guess I just don’t see it."

    "????????????"

    s "Didn’t you say something about wanting to marry your mom when you were younger, though?"
    r "I was talking about my other mom, obviously."

    scene rinoutsidemom4
    with dissolve

    r "But, back to the topic at hand! What the Hell, Sensei?!"
    s "I seriously had no idea you two were even related. Though, in hindsight, if I put any amount of thought into it at all, I probably could have figured it out."
    s "It’s not like we’ve known each other for very long or anything. She’s just the newest addition to my cool new adult friend group."

    scene rinoutsidemom5
    with dissolve

    r "Since when do you have an adult friend group?! What about me?! Why is everything falling apart all of a sudden?! Stuff like that is supposed to be saved for when we go to the beach!"
    s "How much do you even know about your mom’s situation, Rin? "

    scene rinoutsidemom6
    with dissolve

    r "Well...how much do {i}you{/i} know? Because it’s plain as day that they’re not together anymore on account of the fact that I am washing her clothes, but I still don’t get {i}how{/i} it happened."
    s "I’m going to be trustworthy for once and not reveal anything since this is my “hot boy summer” and I am attempting to turn over a new leaf as a decent person."
    r "Okay, first off, stop trying to sound young. Second, it’s hot {i}girl{/i} summer. Third, you weren’t even {i}close{/i} to using that term right. Fourth, you are a bad person. Fifth-"
    s "How many numbers are there going to be? Because I’m starting to think I don’t have time for this."
    r "Just seven more. Fifth, you-"
    s "Okay, moving right along- just get all of the details from Rika if you really want to know what went down."
    s "Unless you two are on weird terms or something. Which I’m starting to think you might be on account of the fact that she still hasn’t met Otoha and that you don’t find her attractive."
    r "Would not wanting to fuck my mom really put us on weird terms?"
    s "Probably. It’s the first girl I’ve ever encountered that you don’t want to have sex with. "
    s "Well, two counting Molly."
    r "Oof."

    scene rinoutsidemom7
    with dissolve

    r "We’re not on weird terms or anything. I wouldn’t have invited her to stay with me if we were. And the Otoha thing is...well, suddenly a lot harder to approach. So I’m still trying to figure out what to do."
    r "Otoha’s...Well, she’s got some issues or...doubts about same-sex couples. And I’ve always pitched my parents to her as the perfect example of how it’s done and how it can work."
    r "But considering the fact that {i}that{/i} relationship is now knocking on death’s door, it doesn’t really make my pitch all that reliable, does it?"
    s "No...but you can’t hide her forever, you know?"

    scene rinoutsidemom8
    with dissolve

    r "Of course. I know it’s only a matter of time. "
    r "I just think that waiting until she’s not {i}living in my room{/i} is probably for the best right now since I don’t want Otoha thinking I’ve just been lying about how functional my life is."
    s "You have one of the most dysfunctional lives I know, Rin."
    r "Me, personally? Sure. But apart from the whole being adopted thing, my home life was always totally normal and not at all {i}dysfunctional.{/i}"
    r "They always say that children are a reflection of their parents. And while my mom is great, you’ve gotta admit that she’s been in better shape, right?"
    s "Beats me. She’s been a wreck ever since I met her. Think the issues with mom number two might run a little deeper than we think."

    "I expertly pretend like I have no idea what I’m talking about and keep my “hot boy summer (whatever that means)” alive. "

    scene rinoutsidemom9
    with dissolve

    r "Wow. You really weren’t kidding when you said you haven’t known each other long, have you?"
    s "I only see her on Fridays, really. And even then we haven’t exactly talked much."
    s "She reminds me a lot of you, though."
    r "She does? How?"
    s "Just in the fact that she’s easy to get along with and clings to others as if it’s second nature."

    scene rinoutsidemom10
    with dissolve

    r "Clings to...others..."
    s "..."
    r "..."
    s "R-"

    scene rinoutsidemom11
    with hpunch

    r "That’s it!"
    s "What’s {i}it?{/i} What does that-"

    scene rinoutsidemom12
    with dissolve

    r "You have to date my mom!"
    s "..."
    r "It’s the shortest and easiest way to solve the issue of her being too dependent on my other mom! Plus, it will help get her out of my room so I can finally introduce her to Otoha!"
    s "And...how did you reach that conclusion, exactly?"

    scene rinoutsidemom13
    with dissolve

    r "She’s clingy and you’re obsessed with girls. If she falls in love with you, she won’t need my other mom anymore and she’ll go back to not crying every five minutes."
    s "You don’t feel weird about me dating your mom?"
    r "Nah. You’re already like a dad to me anyway."

    if rinbetrayed == False:
        s "Even though we’ve made out?"
        r "I’m technically an orphan. Chances are that sort of thing would have happened if I had a foster dad anyway."
        s "I feel like saying that doesn’t exactly set a good example for other orphans or...foster fathers out there."
    else:
        s "Gee, thanks. I feel myself falling further into the friend zone every single day."
        r "Maybe you’ll find Chika down there as well and not have to feel so alone?"
        s "Okay, you really need to get over that."
        r "Fuck you."

    s "Besides, if anyone is going to date your mom, it should be Imani."

    scene rinoutsidemom14
    with dissolve

    r "Why should it be Imani?"
    s "Because those two have already made out."

    scene rinoutsidemom15
    with dissolve

    r "My mom made out with Imani?!"
    s "Yeah. It was awesome."
    r "I want to make out with Imani!"
    s "You have a girlfriend."
    r "She wants to make out with Imani too! We all do! Imani is hot!"
    s "Also, what about Futaba? I thought you wanted me to be with {i}her?{/i}"

    if harukasex == True:
        "Haruka as well, but...I’m pretty sure that might just be some sort of sexual fantasy of Rin’s and not something she actually sees working out any time soon."

    s "Dating your mom would throw a wrench in that plan, wouldn’t it?"

    scene rinoutsidemom16
    with dissolve

    r "Ahh, fuck...you’re right. Futaba would feel super betrayed and used if you started seeing my mom right after taking her virginity."
    s "Oh. So I guess that’s a thing you know now. Thanks, Futaba."

    scene rinoutsidemom17
    with dissolve

    r "How was it?"
    s "Are you seriously asking me for a review of sex with your best friend?"
    r "Is that weird?"
    s "No. It was great. But now you have to tell me how sex with Otoha is whenever you two get there."
    r "I touched her boobs for like five minutes once. That was cool. They’re very...firm. Real quality breasts. A lot different from Futaba’s."
    s "If you’ve groped Futaba as well, it seems only fair that I get to grope Otoha next."
    r "I mean..."

    scene rinoutsidemom18
    with dissolve

    r "So long as it’s all three of us...but I don’t really think she looks at you that way."

    if rinbetrayed == True:
        r "Which is great news for me since you won’t be able to beat me to having sex with her while I’m nervously lagging behind. "

    s "I don’t think she looks at me that way either. But I’m glad to hear that this threesome isn’t entirely impossible as I was starting to think you were losing interest in me."

    if rinbetrayed == True:
        scene rinoutsidemom19
        with dissolve

        r "And why exactly would I be interested in you after all you’ve done to me?"
        s "Because even if you’re mad at me for everything I did, you keep me close to your heart. Which means there must be {i}something{/i} there, right?"
        r "It’s not like I’d tell you if there was. Especially not when I already have someone I care about more than...almost anything."
    else:
        scene rinoutsidemom20
        with dissolve

        r "What...What exactly do you mean by that?"
        r "I already told you that Otoha’s the one I-"
        s "For the sake of your impulsiveness and the fragility of both your heart and relationship, I’m going to keep my mouth shut."

    s "Regardless, I just feel like the two of us have been getting a lot more...distant ever since you started seeing Otoha."
    s "Which I don’t blame you for, of course. She's the one you care the most about and I can’t expect to just change that by having a penis and talking to you."
    s "We’re just not as close as we used to be, I guess. "
    s "But if that’s just me talking too much, I-"
    r "No...You’re right."

    scene rinoutsidemom21
    with dissolve

    r "I feel the same way. And I miss you. "
    r "I was actually really upset for a day or two after I heard about the virginity thing from Futaba."
    r "Not just because I wasn’t there, though. But because you didn’t even think to come to me about it and I feel like you {i}would{/i} have if this were still..."

    scene rinoutsidemom22
    with dissolve

    r "The beginning of..."
    r "The...school...wait, what month is it?"

    scene rinoutsidemom23
    with dissolve

    r "A-Anyway! You’re totally right. It’s just really hard for me right now to find time for both of you."
    r "I want things to be as normal as possible for Otoha since she’s still so, uhh...anxious about everything. And when I’m with you, I..."
    r "I..."

    scene rinoutsidemom24
    with dissolve

    r "I get a little too excited."
    r "I don’t want her to feel like she’s moving down my priority list. And she's actually really sensitive despite always seeming so cool and collected."
    r "But that’s not fair to you either since you’re...a good friend of mine..."
    r "And one that, even with all of the hiccups, I still cherish."

    scene rinoutsidemom25
    with dissolve

    r "There’s always a place for you in my heart, Sensei. And even if it feels like the walls are caving in, I can guarantee you that place isn’t shrinking at all. "
    r "The rest of it’s just getting bigger."
    s "I can accept that. Like I said, I understand it and don’t hold anything against you. The top priority right now is keeping things stable with Otoha. "
    s "Which means that I will have to take one for the team and fuck your mom. But remember, Rin- I am only doing this for {i}you.{/i}"
    r "Woah, hold on. Nobody said anything about {i}fucking.{/i} I was just suggesting that you make her {i}want{/i} to fuck you since that would keep her sane long enough to look like a functional adult in front of Otoha."
    r "But if you’re planning on making me a little brother or sister, I don’t think I-"

    scene rinoutsidemom26
    with dissolve

    r "Wait..."
    r "..."
    s "..."
    s "Rin?"
    r "Shut up, I’m thinking."
    s "I was just joking, you know. There’s no way I’m going to impregnate your-"
    r "Call me “onee-chan” but do it in like, a...girly voice. I think I might want a little sister."
    s "I don’t a think I’m capable of making a girly voice. Nor am I willing to call you “onee-chan.”"

    scene rinoutsidemom27
    with dissolve

    r "Ugh. You’re no fun. Guess I’ll just be an only child forever because no one will have sex with my mom."
    s "Wait, so {i}am{/i} I supposed to have sex with Rika? Or am I not supposed to do that? Because I feel like you’ve flipped positions over the last two minutes."

    scene rinoutsidemom28
    with dissolve

    r "I don’t know, man. Do whatever you want. I still think my parents are going to get back together, but my mom could definitely use a good “magic missile” right now."
    s "Please don’t call it that ever again. "
    r "Whatever happens, just don’t tell Futaba about it. Or {i}me.{/i} I don’t want to know. "
    r "Finding out you banged my mom would be, like...the weirdest form of NTR ever."
    r "And now that I’m leveling with you, I might as well add that I have no clue if the dating thing would even work in the first place. I’m just running out of ideas over here, Sensei. "
    r "I desperately want things to work out with Otoha and me. But it’s mega stressful feeling like I have to fucking choreograph my entire life to make it work."
    r "Maybe I just need to get laid too. That sounds like it would help."
    s "I’ve felt that way since the day I met you and agree that it would probably turn your life around."
    r "Sometimes, I feel like I’m going to die a virgin."
    s "Not if I have anything to do with it."

    scene rinoutsidemom29
    with dissolve

    r "That would certainly fix our “distance” problem, wouldn’t it?"

    if harukasex == True:
        s "Yes, but I have already wrecked your boss’s home and plucked her from the clutches of another man. Destroying one more might make me a bad person. "
        r "Maybe. But on the bright side, it would mean that Haruka, Futaba, {i}and{/i} me all got boned by the same person! We’d have something to bone over! I mean...bond. "
    else:
        s "It would. But I’ve got a good streak so far of not having sex with people in relationships. So just keep hoping Otoha takes your pants off while I pretend that I won’t be fantasizing about that later."
        r "Don’t worry. The amount of time I will spend fantasizing about that will more than make up for it."

    scene rinoutsidemom30
    with dissolve

    r "So...we cool? No longer worried that I’m gonna just slowly wean you out of my life?"
    s "I wouldn’t ever let that happen anyway since you’re such an essential part of mine."
    r "Likewise, homie."
    r "Let’s...get together soon. Find time for just the two of us and see if we can get things back to the way they were before all of the chaos and stress and stuff."

    scene rinoutsidemom31
    with dissolve

    r "But, for now...I’ve got a load of laundry to finish."
    r "Thanks for letting me vent a little bit. And for not telling me when you ultimately sleep with my mom."
    s "And...thanks for your blessing, I guess?"

    scene black
    with dissolve2

    "Rin heads back into the dorm- and while I should be narrating about how this conversation went way better than I expected it to...really all I can think about is having sex with her mom."
    "That’s on Rin, though. I was planning on saving those thoughts until I got home later. It’s not my fault they’ve been pushed up. "
    "The “weirdest form of NTR” aside, though...I’m worried about her."
    "She’s surprisingly calm for being in such a stressful predicament right now. "
    "And all I can hope is that it doesn’t wind up getting to her."
    "Or that something else doesn’t get to her first."

    $ renpy.end_replay()
    $ rin_love += 1
    $ rindorm55p2 = True
    stop music fadeout 7.0

    "{i}Rin’s affection has increased to [rin_love]!{/i}"
    "........."
    "......"
    "..."

    if day >= 6:
        jump endofsat
    else:
        jump endofweekday

label rinspecial55:
...
```

## Code that triggers this event

File: (install folder)\game\RinEvents.rpy

Code:
```python
...
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
...
```