# Post-Game Celebration! (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Fallen Angels](./dormwar15.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: dormwar16
* Group: Main
* Triggered by label: dormwar15
* Chain sources: dormwar15
* Chain sources path: dormwar15

## Official wiki page

[Post-Game Celebration!](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=dormwar16&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label dormwar16:
    if _in_replay:
        play music "letsfuckingo.mp3"

    scene postfashion1
    with dissolve

    to "Are you okay?! Were you attacked?!"
    to "I knew leaving you alone for several hours at once was a bad idea!"
    to "Come on, we have to get you to the hospital!"
    ya "I’m sorry, Touka. I was just trying to be as pretty as you."
    to "You should know that is impossible by now, Yasu. How do you feel? Lightheaded?"
    to "I have training in first aid. Let's find a sanitary room to stop the bleeding and-"
    s "I’m pretty sure she’s okay, Touka. She just needs to take the crown off."

    scene postfashion2
    with dissolve

    to "You let this happen?! Why?"

    if yasufashion == True:
        if bonus == True:
            ya "Sensei wants to lay my body down upon the altar and fill me with His love."
        else:
            ya "(Airplane noises)"


        s "Yasu, come on."
        to "You what?!"
        s "It means that she won the fashion show."
        to "That is absolutely not what she means!"
        s "Okay, maybe not. But she {i}did{/i} win the fashion show, so..."
        s "A celebration is in order?"
        to "You absolute heathen!"
        ya "Are you proud of me, Touka?"

        scene postfashion3
        with dissolve

        to "Of course I am. I just don’t want you passing out in some unfamiliar bar due to blood loss."
        ya "Every drop that falls onto the floor will one day be recycled and consumed by His radiance. "
        ya "This blood does not belong to me, Touka. It belongs to God."
        to "Well, {i}whoever{/i} it belongs to will have to wait. Come with me. And toss that wretched...decoration into the trash while you’re at it."
        ya "I can’t take it home with me?"
        to "Absolutely not."

    else:
        s "I didn’t {i}let{/i} anything happen...it was part of the contest."

        scene postfashion3
        with dissolve

        ya "I’m sorry, Touka. But it appears that I have failed in whatever I was meant to do here today."
        to "That’s quite alright, Yasu. The competition is the least of my worries right now. "
        to "To think your costume would have a real crown of thorns, though...my personal designers would have never suggested something like this."
        to "We should have just had one of them tailor something for you. I’m sure it wouldn’t have been a problem."
        ya "I am not worthy of the clothes you’d dress me in, Touka. Even your concern is too much for a worm like me."
        to "That may be true, but it does not change the fact that I’d dress you in them regardless."
        s "Kudos to you for being both kind and conceited at once. Not many people can do that so effortlessly."

    scene postfashion4
    with dissolve

    to "You."
    s "Hey."
    to "My mother will be here any minute. Why are all of the girls in our class drinking?"
    s "Tsubasa is coming? Why?"

    if bonus == True:
        to "Because I am a [teenage]girl and this is a bar. She’s likely worried for my wellbeing, which is an extremely valid sentiment, if I do say so myself."

        "Well..."
        "Let’s hope Tsubasa is as accepting of that as she is of me having hours and hours of audible sex with one of her daughter’s classmates."
    else:
        to "You know damn well why, huggy boy."
        s "{i}Already?{/i}"
        to "Do I need to take the gum money back?"

    s "I’ll deal with your mom. Just make sure Yasu doesn’t die or something."
    ya "There is no death, there is only-"

    scene postfashion5
    with dissolve

    to "Not right now, you troublesome whelp. "
    ya "Hehehehahhehehahehahaha~"

    if sanafashion == False:
        scene postfashion6
        with fade

        sar "..."
        s "..."
        sa "..."
        sar "You better have a really good explanation for this."
        sa "Mom...it’s...okay..."
        sa "I’m sure the other girl...worked just as hard..."
        sar "Oh, no. He’s not getting off the hook that easily."
        sar "My daughter is the single cutest thing on the entire earth. No! The entire planet!"
        sa "Mom...those are...the same-"
        sar "Quiet, dear. This is between Sensei and me."
        s "...Is it really, though?"

        scene postfashion7
        with dissolve

        sar "She’s so cute! How could you not choose her?!"
        sa "Sensei...I’m...really sorry about this..."
        sa "I don’t mind that I lost...I...I’ve already accepted it..."
        sar "Well I haven’t. I am offended and betrayed and...and a lot of other bad things."

        scene postfashion8
        with dissolve

        w "You disgust me."
        sar "You tell him, zombie teacher!"
        s "You too?"
        sa "Ms. Watabe...you don’t have to..."
        w "I mean he disgusts me in general. "
        w "But yes. I also disagree with your decision."
        s "I just thought the other costume was better."
        w "These are not “costumes,” you pathetic waste of carbon. "
        w "These outfits are a way of life...and offer more insight into the minds of those who wear them than any words possibly can."
        w "Do you think this is all a charade? Is that why you selected the girl who spouted a religious, delirium coated monologue while she should have let her dress do the talking?"
        w "I should have you fired for this."
        s "Wow...you’re, uhh...really passionate about this kind of stuff, huh?"
        w "You don’t understand anything at all."
        os "Okay, Wakana. That’s enough..."
        os "Let’s go home."

    else:
        scene postfashion9
        with dissolve

        sar "I knew you’d make the right choice, Sensei."
        sar "Of course, there was absolutely no way Sana was going to lose when she looks {i}this{/i} cute. It just wouldn’t be possible."
        sa "Um...h...hi, Sensei..."
        s "Hey, Sana. And congratulations. You looked great up there."
        sa "I...umm..."

        scene postfashion10
        with dissolve

        sa "Hahah..."
        sar "I know I probably shouldn’t be doing this because it’ll obviously embarrass her...but thank you, Sensei."
        sar "Sana’s struggled with her self confidence for a long time, and something like this is exactly what she needs to start feeling better about herself."
        sa "I...really don’t think a fashion show is...{i}exactly{/i} what I need..."

        scene postfashion11
        with dissolve

        w "I beg to differ."
        sa "Ms. Watabe?..."
        s "Are you...smiling right now?"

        if bonus == True:
            w "Silence, lecher."
        else:
            w "Silence, huggy boy."

        w "You look lovely tonight, Sana."

        scene postfashion12
        with dissolve

        sa "I...do?..."
        w "You do."
        w "And unlike the other girl, you actually let your outfit do the talking. "
        w "You didn’t rely on some delirious monologue to stake your claim."
        w "When I was your age, I had trouble expressing myself."
        s "And you’re good at it now?"
        w "I said {i}silence.{/i}"
        w "It wasn’t until I started dressing in clothes like this that I truly began to feel like me."
        w "So perhaps this {i}was{/i} what you needed."
        w "And perhaps I still have some clothes lying around that no longer fit me."
        w "I’d be happy to hand them down to you if you’d like. "

        scene postfashion13
        with dissolve

        sa "Would you...really do that for me?"
        w "Assuming I can find them."
        w "I’m sure they’re tucked away in storage now. But I’ll have Osako help me look."
        sa "I...don’t know what to say..."
        sa "Thank you..."
        w "You’re very welcome."

    scene postfashion14
    with dissolve

    w "Anyway, that’s all I needed to say. I’ll be taking my leave now."
    sar "Need me to call a cab for you? You drank...probably more than I’ve ever seen {i}anyone{/i} drink before."
    w "My partner will be driving, but I appreciate the offer."
    w "Until we meet again."

    scene postfashion15
    with dissolve

    "Wakana and Osako exit the bar and I’m suddenly left alone with the two Sakakibara girls."
    "Well, alone in a loose sense of the word as there are still plenty of other girls around here."

    sa "P...Partner?"
    sa "Are they on a...team together?"
    sar "That means they’re in a relationship, dear. "

    scene postfashion16
    with dissolve

    sa "O...Oh..."
    sa "Oh...wow..."
    s "Sidenote, did you interview someone for a job this morning, Sara?"

    scene postfashion17
    with dissolve

    sar "I did, but...how did you know that?"
    sar "You’re not stalking me, are you?"
    s "I am not stalking you."
    sar "It’s okay if you {i}are{/i} stalking me, though. I just want to know so I don’t go out without my makeup on or something."
    s "Sara, I’m not stalking you."
    sar "Are you maybe {i}considering{/i} stalking me? Because I really don’t mind."
    s "Sara, interview."
    sar "Oh, right."
    sar "Yeah, I had an interview with a woman named Yuki. She’s a recovering addict and-"
    s "I know her. She’s a friend of mine."

    scene postfashion18
    with dissolve

    sar "Well, that’s...a surprise. "
    sar "She doesn’t seem like your type."
    s "It’s another one of Sana’s classmates’ mothers. "
    s "She and her daughter don’t really talk anymore, though."
    sar "That’s a shame. She seemed really nice."
    sar "A little rough around the edges, sure. But she’s not asking for much and...it would be nice to start having this place open during the day instead of just at night."
    sar "She was a little hesitant about wearing the uniform, though. So I’m going to have to figure out a way to get her one with pants like Sana has."
    s "You could probably start by...buying pants."
    sar "You make it sound so easy."
    s "They’re...just pants."
    tb "Oh my. It’s quite lively in here."

    scene postfashion19
    with dissolve

    sar "Oh my God. Who is that?"

    if bonus == True:
        sar "We have an actual customer and there are like ten [high_school] girls drinking in here."
        sar "Sana, your mother is going to jail."
    else:
        sar "She looks rich. What kind of drinks do rich people like?"
        sar "Sana, what should I do? I'm going crazy."

    sa "I...think that's...Touka's mom..."

    scene postfashion20
    with fade

    if bonus == True:
        tb "Oh, wonderful. I was beginning to worry that I may have walked into the wrong establishment."
        tb "You haven’t seen my daughter anywhere, have you?"
        tb "I don’t intend to get in her way, I just want to make sure she hasn’t run off to a strip club or something of the like."
        s "That is certainly a strange assumption to have about your daughter."
        tb "I can’t help but assume the worst at times."
        s "Well that’s just rude to strippers."
    else:
        tb "WHERE IS MY HUG?! I HAVE WAITED LONG ENOUGH!"
        s "Oh no"

    scene postfashion21
    with dissolve

    c "Tsubasa?! What are you doing here?!"
    c "Are you going to party with us?"
    tb "Oh, no. I’m afraid my partying days are o-"
    tb "Actually, I don’t believe I’ve ever even had any partying days."
    tb "How sad."

    scene postfashion22
    with dissolve

    sar "Heeeeeey! I’m Sara. I own this place."
    c "Oh my God, you are so cute. You and Sana are like, identical."
    tb "Tsubasa Tsukioka. Pleasure to meet your acquaintance."

    scene postfashion23
    with dissolve

    sar "Wait...Tsukioka..."
    sar "You mean like the bubble wrap family that {i}isn’t{/i} Ayane’s?"
    s "Is {i}that{/i} where your money comes from?"
    tb "A portion of it. And yes, that would be me."
    sar "But...what would someone like you be doing in a place like this? "
    c "Her daughter’s in our class."
    sar "She..."
    sar "She wasn’t drinking, was she?"
    s "She’s cleaning blood off of Yasu right now."

    scene postfashion24
    with dissolve

    sar "Oh thank God...I thought this was the end for me."
    s "I mean, there are still a bunch of other [high_school]ers drinking in here."
    sar "Yes, but none of them have nearly as much influence as the daughter of the Tsukioka family. "
    sar "I have no idea what I’d do if she were to get drunk on my watch."
    c "I don’t think it would really matter. Tsubasa’s one of those cool moms who lets her kids do whatever they want."

    if bonus == True:
        tb "It is true that I allow Touka to partake in wine at family dinners, though I’m not quite sure how I’d feel about her drinking any more than that."
        tb "Is that something common- *ahem*"
    else:
        tb "It is true that I have been known to get downright hammered with my daughter from time to time, but I'm not sure how I’d feel about her drinking without me."
        tb "Is that something common- *ahem*"

    tb "Is that something the lower middle class does often?"

    scene postfashion25
    with dissolve

    c "Oh yeah. I mean, none of us really do it all that much. But it’s a pretty normal bonding experience for girls our age."
    tb "Bonding, you say?"
    tb "So, girls who consume alcohol together tend to become friends?"
    c "Without overcomplicating things, yeah. That’s kinda how it works."
    tb "If that’s the case, I don’t mind at all."
    tb "Don’t let my presence here dissuade you from doing as you’d do otherwise. "
    tb "Enjoy your youth, Chika. And, if it’s no trouble-"
    c "Don’t worry. I was planning on inviting Touka over to hang out with Yumi and me as soon as I saw her again. "
    tb "Splendid. Thank you so much, dear."
    sar "Hey...Tsubasa, if you’d like, you’re free to come talk to me at the bar."
    sar "The only other mom here right now is off talking to one of the girls, but I’d be happy to get to know you."
    s "Maki is? "

    scene postfashion26
    with dissolve

    sar "Yeah. The one with the brown hair and glasses."
    s "Nodoka? "

    "Oh god."
    "I can only imagine what would happen if those two..."

    s "I need to go talk to them."
    sar "Uhh...okay! You know where to find us if you get bored!"

    scene postfashion27
    with fade

    "I make my way over to Nodoka and Maki and breathe a sigh of both relief and disappointment to find their clothes still on."

    no "And that essentially sums up my opinions on the matter. Do you agree, Maki?"
    maki "I agree wholeheartedly, Nodoka. And I’m very pleased to find that there are girls your age who have such well thought out opinions on the subject."
    s "Okay. What did I miss?"

    scene postfashion28
    with dissolve

    no "Oh, Sensei. Wonderful. A male’s opinion would actually be quite beneficial to this discussion."
    s "And that discussion would be?..."

    if bonus == True:
        maki "Anal."
        s "How did you get to that point of comfort with one another in the five minutes you have been talking?"
        maki "Well, we kind of started there since Nodoka’s opening line was asking me if I wanted to come back to her dorm room."
        s "Nodoka, come on."
        no "Did you expect any less of me, Sensei?"
        s "No, but that’s Makoto’s mom. Don’t you think that might be adding insult to injury?"

        scene postfashion27
        with dissolve

        no "I won’t tell if you don’t. "
        maki "Thanks, but you’re a little too [young]for me. "
        no "I would also be open to the prospect of watching you have sex with my teacher."
        s "Nodoka, please."
        maki "Maybe another time. I have to stick around in case anybody needs a ride home tonight."
        s "A - If you’re okay with that, you may as well just be okay with Nodoka in general."
        s "And B - You should put the wine down if you’re going to be a designated driver."

        scene postfashion28
        with dissolve

        no "Since when are you the responsible one?"
        s "Since I stumbled upon the two biggest deviants in Kumon-mi getting to know one another."
        maki "{i}Three{/i} biggest deviants, good sir. You know very well that you are one of us."

        if futabalust15 == True:
            no "Can confirm."
            no "Can {i}definitely{/i} confirm."

        s "You know what, I’ll just leave you two alone. I should probably be evenly distributing my time anyway."
        no "Feel free to come back the moment one of us starts moaning."
        s "I absolutely will. And thank you for the heads up."
    else:
        maki "Nerds candy. Rope or no rope?"

    scene black
    with dissolve

    if bonus == False:
        s "I can't do this right now."

    "………"
    "……"
    "…"

    scene postfashion29
    with dissolve

    r "Yo!"
    f "Hey..."
    s "Hey. What’s going on over here?"
    r "Otoha and I are about to have alcohol for the first time, but we’re both really nervous."
    o "Do they not have to put the nutritional facts on the back of beer or something? What is this?"
    s "Why is that what you’re concerned about?"

    scene postfashion30
    with dissolve

    o "Dude, Futaba won’t do it with us and I’m trying to prove to her that it’s fine."
    f "I’m...trying to cut back on calories and...I don’t think I should really be drinking..."
    r "Hey, you’re a smart guy. Can Futaba drink with us without having to worry about her weight?"
    s "Futaba shouldn’t worry about her weight at all. She’s adorable."

    scene postfashion31
    with dissolve

    f "Wha-"
    f "Why would you just randomly compliment me like that?!"
    o "Wow. I think that was the first time I’ve ever seen you say anything that was genuinely nice and not completely weird."

    if rinbetrayed == True:
        if bonus == True:
            r "Yeah! Sensei can be pretty awesome when he’s not fist deep inside the girl you like."
        else:
            r "Yeah! Sensei can be pretty awesome when he’s not waking you up in the middle of the night by dumping shrimp onto your bed."

        scene postfashion32
        with dissolve

        o "Okay, seriously. What the hell happened with you two?"
    else:
        r "Yeah! Sensei’s a super awesome guy who does a lot of super nice things!"

        if bonus == True:
            r "You can even flash him or wear a bathing suit and lay on his lap and he won’t even touch you. It’s really cool."
            o "I will...keep that in mind."
        else:
            r "LIKE HUGGING THE PEOPLE YOU TELL HIM NOT TO HUG."
            s "=(((((("

    n "Senseiiiiiiiii! Over here!"

    scene postfashion33
    with fade

    "I make my way across the room to find four girls who have apparently decided {i}against{/i} drinking tonight."

    n "Hey! A few of us were gonna go back to the hotel soon and we wanted to know if you’d want to come with us."
    s "Already? I was under the impression this was some sort of afterparty."
    a "Who says there can’t be an afterparty at the hotel as well?"
    ay "Yeah, Sara doesn’t have a kitchen and the four of us are hungry, so we were gonna stop and get food or something on the way."
    s "You don’t want to drink?"
    t "I can’t drink. I will die."
    s "You won’t {i}die{/i}, Tsuneyo. You’ll just pass out again."
    t "And be assaulted by the tiny athletic girl again? No thank you."
    t "I will accept my death with pride like a true samurai."
    s "Suit yourself."
    n "Oh my God, Sensei. You should have seen Tsuneyo’s reaction to the test of courage thing we did. It was hilarious."
    t "There is nothing hilarious about the death of perfectly good noodles."
    s "Test of courage?"
    ay "Yeah. Most of us went to my house during the stupid date contest thing and Maya and Tsuneyo had to try to outlast each other in rooms we decorated."

    scene postfashion34
    with dissolve

    a "Yeah...Maya actually seemed really shaken up afterwards. I’m kind of worried about her."
    s "This is {i}Maya{/i} you’re talking about. I’m sure she’s fine."
    t "Ahh, another person who understands the true horror that is the death of the ultimate entree."
    n "I think Maya’s room was a little different, Tsuneyo."
    ay "You’re not going to come with us, are you?"
    s "I think I’ll stay here for a little while longer. I haven’t even had a drink yet."
    ay "Why drink anything when you can drink our love?"

    if ayanelust15 == True:
        s "Are you sure you’re even okay to be hanging out with people right now, Ayane?"
        ay "Yup! Why wouldn’t I be?"
        ay "It’s been a totally normal weekend and I’m totally good because only good things have happened."
    else:
        s "{i}What does that even mean?{/i}"
        ay "{i}Whatever you want it to mean.{/i}"

    scene postfashion35
    with dissolve

    a "Hah...well, if Sensei isn’t going to come, there’s not really a point in hanging around here any longer."
    a "Molly took off as soon as the fashion show ended and the Yumi versus Io contest is obviously not going anywhere."
    s "What even is their contest?"
    ay "Just to see whoever joins in on the festivities first. "
    ay "But Io isn’t even here right now and the contest is basically over, so I’m pretty sure Yumi is going to win by default."
    n "You suuuuuuure you don’t wanna come with us?"

    if bonus == True:
        s "Are you going to drug me if I say yes?"
    else:
        s "Maybe...but only if you give me a piggyback ride."

    scene postfashion36
    with dissolve

    n "What do you think, Ayane? Could the two of us carry him back together?"
    ay "Not without a lot of attention from anyone on the street. But if we wait a few more hours-"

    if bonus == True:
        a "No one is drugging my [uncle]! You’re all insane!"

    t "He is large, but I think I could dispose of him alone."
    n "We’re talking about bringing him back to the hotel...not dumping his body, Tsuneyo."
    s "Tsuneyo, you don’t actually want to murder me, right?"
    t "…"
    t "Would you look at the time?"
    t "We should probably get going."
    s "What did I ever do to you?"
    t "You walked out on our family, you bastard."
    t "And now our child is all alone because the Emerald Guardian wanted to scare me with soup."
    t "Look what you have done."
    t "{i}Look what you have done.{/i}"
    s "I’m so confused."

    scene postfashion37
    with dissolve

    a "Anyway...I guess just...let us know if you want to come back early or...want us to pick up anything at the convenience store for you."
    n "Maybe even a roll of Touka’s favorite {i}candy{/i} if you know what I’m saying."
    s "You talk the talk, but can you walk the walk, Noriko?"

    if bonus == True:
        n "Step on me, Daddy."
    else:
        n "You know, I really just wasn't a big fan of Squid Game."

    scene postfashion38
    with dissolve

    a "Noriko, what the fuck?!"
    ay "Uhhhhhh..."

    if bonus == True:
        t "This is why you walked out on us?! Because you had another daughter?!"
    else:
        t "You played a game with squid and did not invite me?!"

    s "…"
    t "…"
    n "…"
    ay "…"
    a "…"
    u "Sensei! Over here!"
    s "Oh, thank god."

    scene postfashion39
    with fade

    u "Afterparty’s barely even started and you’re already bein’ invited back to the hotel with a group of girls."
    u "Where do you get off?"
    s "How is this in any way my fault?"
    mak "Did you enjoy the dorm war, Sensei?"
    mak "I’ll admit that the idea seemed a bit childish when it was first pitched, but I do think we’ve managed to make at least some semblance of progress in terms of camaraderie. "
    s "It has...certainly been an interesting two days, to say the very least."
    s "Why aren’t you two out talking to the others, though? I figured you’d want a break after putting all of this together."

    scene postfashion40
    with dissolve

    mak "That’s precisely {i}why{/i} we’re not “mingling” with the others at the moment. "
    mak "Well, that and the fact that it would be illegal for either of us to drink. "
    u "I’m just really tiny and don’t want to get drunk and have you do perverted stuff to me while I’m unconscious."
    s "Uta, please don’t make me out to be some sort of predator."
    u "…"
    u "Weeeeeeeeell-"

    scene postfashion41
    with dissolve

    mak "So, what are you going to do now?"
    mak "We’re spending one more night at the hotel before announcing the results in the morning."

    if ayanelust15 == True or futabalust15 == True:
        s "Speaking of announcing the results...have any of the girls mentioned anything about bonus contests?"
        mak "Yes. And it is taking every fiber of my being to not imagine what that could possibly mean."
        s "I can assure you that any and all non-supervised contests have been entirely wholesome in nature."
    else:
        s "Why not just announce them now?"
        u "Probs because half the class is missing or drunk and the other half is winding down."
        u "Gotta give everybody a little room to breathe before we shatter the dreams of ten girls."

    scene postfashion42
    with dissolve

    u "Oh! I've been meaning to ask, but you haven’t seen Io anywhere, have you?"
    s "I feel like you've been looking for her nonstop this entire weekend."
    u "Because I pretty much have been!"
    u "She told me she was gonna come hang out here tonight, but she’s been acting kind of weird since this morning."
    u "Like, she didn’t even stay in the hotel last night."

    "Oh yes she did."

    u "I know she’s not really the type to get involved in this kinda stuff, but I can’t help but worry about her."
    mak "I can relate to that. "
    mak "Well, not so much the part about acting weird, but about worrying for a friend’s wellbeing."
    mak "Miku didn’t come tonight for her own personal reasons, so of course I’m concerned about her in a way similar to how you feel about Io."
    u "I don’t even care about the contest thingy anymore. I just want her to have fun."
    mak "Not to stray too far from the topic at hand, but...Yumi {i}has{/i} cooperated in at least some form, sooooo..."
    mak "She provided an interview prior to Chika’s portion of the date war and is now off in the corner with Chika and Touka."
    u "Okay, yeah. Whatever. Yumi wins the wallflower cooperation contest."

    $ dorm1warpoints += 1

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    u "Just...if you see Io, let me know. Okay?"
    s "Got it. "
    s "I’m going to go pay a visit to those girls in the corner now, though."
    s "I’m a little interested in observing how two of them in particular act in a “party” setting."

    scene postfashion43
    with dissolve

    mak "{i}Please{/i} do not say or do anything strange."
    mak "It’s unprofessional enough that you’re watching a bunch of [high_school] girls get drunk, but-"
    s "Uta, do me a favor and get Makoto a drink. She needs it."

    if bonus == True:
        u "Okay, but I’m closin’ my eyes the second you start touching her unconscious body in inappropriate places."
    else:
        u "Okay, but I’m closin’ my eyes the second you two start hidin' the soup so I don't know where to look for it!"

    mak "Hah..."
    mak "I’m so tired..."

    scene postfashion44
    with fade

    c "Come on! Live a little! Just one!"
    y "The fuck do you gain from me drinking? I have to watch your sister tonight."
    c "Yumi, it’s one beer. It’s not going to affect whether or not you’re able to babysit."
    c "There are adults everywhere, too. Nothing bad is going to happen, really."
    to "Oh my. I’ve heard about this. But to think I’d go from being a loner to experiencing “peer pressure” in less than a week is quite jarring."

    scene postfashion45
    with dissolve

    c "Touka~ Let’s have fun!"
    c "I’ve been wanting to hang out with you since you transferred in and we haven’t really gotten a chance yet."
    c "Isn’t now like, the best possible time?"
    to "I...suppose it’s as good a time as any, but I don’t quite understand the need for alcohol."
    to "And I normally begin to feel...impaired after just a glass of wine, so..."
    c "I wanna see drunk Touka!"
    c "You’re always so formal all the time. What if you’re like, super exciting when you’re drunk?"
    to "Exciting {i}how{/i}?..."
    c "Idunno. Like, maybe you start singing or dancing or get really mean and start trying to fight people."
    to "Fight people?..."
    to "Well...you do spend most of your time with Yumi...so I suppose you just...enjoy hanging out with those types of people..."

    scene postfashion46
    with dissolve

    y "The fuck you mean by {i}those{/i} types of people?"
    to "I...I meant no offense!"
    to "I’m just acknowledging Chika’s affinity for...more masculine women!"
    y "You saying I have a fuckin’ dick?"
    c "Yay! Bonding!"
    c "Now hurry up and take these beers so I don’t have to stand around holding them all night!"
    s "Hey, everyone. What’s going on over here?"

    scene postfashion47
    with dissolve

    c "Sensei! You’ll drink with me, won’t you?"
    c "These two are being total buzzkills."
    s "I didn’t even know you liked drinking, Chika."
    c "Well...I don’t, really. "
    c "But...when in Rome, you know?"
    c "We just finished battling it out with one another, so it makes sense for everybody to kick back and relax for a little while."
    c "Besides, if I get really drunk, no one will hold it against me if I start getting all up in your business! And I can just blame it on the alcohol if they do!"
    s "I see that you’ve completely and rationally thought all of this through, then."
    to "Sensei...what do you think I should do in this situation?"
    s "Me?"
    to "I’m supposed to look toward you for guidance, and I do not have much experience with peer pressure."
    y "Looking to this guy for guidance probably ain’t the best idea, Tamako."
    to "Touka."
    s "You tell her, Tsuneyo."

    scene postfashion48
    with dissolve

    to "That is a completely different girl!"

    if chika_lust >= 15:
        s "I think you should go for it, Touka. "
        s "It’s not every day you get a chance to feel like a normal [high_school]er. And your mother {i}is{/i} right over there in the event that you get too hammered."

        scene postfashion49
        with dissolve

        to "Well...I suppose it is true that my mother would not intentionally put me in harm’s way."
        to "So perhaps I am just misinterpreting the concept of peer pressure and...just finally being included in something."
        s "Well, there you go. Enjoy your youth."
        c "You gonna do it with me, Touka?"

        scene postfashion50
        with dissolve

        to "What the heck. Why not?"
        to "What’s the worst that could possibly happen?"

        scene black
        with dissolve2
        stop music fadeout 20.0

        "I stay with Chika and Touka a little while longer as they “enjoy their youth” together."
        "Of course, Yumi does not join in on the fun and, instead, heads back to the Chosokabe apartment to watch after Chinami."
        "Apparently, the two of them let her spend the night at the apartment alone last night. But doing that two nights in a row is cause for concern."
        "Either way, Chika and Touka proceed to drink."
        "And drink."
        "And drink."
        "And soon enough, the two of them can barely even walk and Maki has to drive them back to the hotel."
        "I catch a ride as well, since basically everyone else has already left and..."
        "Well, I’m just really tired of walking..."

        $ renpy.end_replay()
        $ dormwar16 = True
        jump chikalust15

    else:
        s "If you don’t feel comfortable, just don’t do it."
        s "But, like Yumi said, asking me for guidance is kind of antithetical to my entire outlook on your wellbeing. "

        scene postfashion51
        with dissolve

        y "Anti...what? I didn't fuckin' say it like that."
        to "I see! Yes, that makes complete sense."
        to "It is one thing to experience youth and friendship, but it should not come at the cost of my own safety."
        to "Besides, an abundance of alcohol can cause the body to bloat, and I simply can not condone the idea of looking anything less than perfect and presentable while out in public."
        c "Well, now I don’t really want to drink either..."
        to "Perhaps we could play a game? Do you think this establishment has a copy of Monopoly?"
        to "I will say I am quite good at that game, so do not underestimate me."
        c "…"
        s "…"
        c "I...guess we can do that instead..."

        scene black
        with dissolve2
        stop music fadeout 8.0

        "Chika, Touka and I...somehow wind up spending the night playing a board game."
        "Yumi, not wanting to be involved in any form (Which I do not blame her for) immediately leaves to go spend the night with Chinami."
        "Apparently, she was left alone last night and the two of them are unwilling to let her do that two nights in a row."
        "Either way, Touka winds up winning (Go figure) and the three of us catch a ride back to the hotel with Maki shortly after..."

        $ renpy.end_replay()
        $ dormwar16 = True
        $ chikalust15skip = True

        jump chikalust15skip

label dormwar17:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
s "Sana."

            scene fashionshow30
            with dissolve

            sa "W-Wait...really? I...I won?..."
            sa "So...so does that mean...you think my outfit is...prettier than Yasu’s?..."
            s "That is what winning would imply, yes."
            ya "Congratulations, Sana. I’m very happy for you."
            mo "Yasu, why couldn’t you wait until after the decision to start bleeding?! Your weak skin has ruined our chances of victory!"

            scene fashionshow31
            with dissolve

            ya "I’m sorry, Molly. I am a very weak and delicate girl."
            sa "I...I don’t really know what to say..."
            a "Say that you couldn’t have done it without me and Ayane!"
            ay "I’m so proud...that’s my girl up there..."
            sar "Haruka. Haruka. Haruka."
            sar "Did you see what happened?"
            h "Yes, Sara. We’re all very happy for her."
            sar "My daughter just won a fashion show. How many fashion shows have you won?"
            h "None, Sara. Congratulations on giving birth to a cute girl."
            sar "Thank you very much~"
            sa "Um...thank you, Sensei..."
            sa "For...choosing me."
            s "You don’t have to thank me. I just picked the person who I thought should win and...that person happened to be you."
            s "You look very cute, Sana."
            sa "Thank you..."
            sa "I’m...really happy you think that..."

        "Yasu wins":
            $ dorm2warpoints += 1
            $ yasufashion = True

            s "The winner of the gothic lolita fashion show is..."
            s "Yasu."
            ya "I won something?"
            mo "YEAAAAH! VICTORY FOR MOLLY!"
            u "And Yasuyasu, Molly. She’s the one who wore the outfit."
            mo "Yes, but {i}I’m{/i} the one who did all the work. This one belongs to the people of Ireland."
            a "Damn it! I worked really hard on that dress!"
            ay "I still think Sana should have won. She’s clearly the cuter girl out of the two of them."
            r "And significantly less scary. I vote Sana."
            ay "Sensei! We demand a recount!"

            scene fashionshow33
            with dissolve

            ya "Does this mean what I think it means, Sensei?"
            s "What do you think it means, Yasu?"
            ya "That if we were to conduct the act of transference among all of these beautiful creatures, you would supplant me with His warmth before the others?"

            if bonus == True:
                s "That is...not how I would word it."
                ya "Is it because you can sense how empty it is inside of me? How I long to spread the seed?"
            else:
                s "If this is your way of suggesting that we should hug, I still think it might be good to wait a little longer."
                s "But...if you really want to know why you won-"

            s "It’s because I thought you looked cuter."
            s "But, Sana-"

            scene fashionshow34
            with dissolve

            sa "Y...Yeah?"
            s "I think you look really cute as well."
            s "I just think this win should go to Yasu instead."

            scene fashionshow35
            with dissolve

            sa "No...I...I agree..."
            sa "I’m just...sad that I couldn’t get...a point for Ami and Ayane..."
            sa "They really tried to...win this competition and...and I couldn’t do it for them..."
            ya "Oh my..."
            ya "Could this be...arousal?..."
            ya "I’m beginning to feel...rather lightheaded..."
            s "You’re also losing blood, so we should probably get you patched up..."

    scene black
    with dissolve2

    "Floor 1: [dorm1warpoints]\nFloor 2: [dorm2warpoints]"
    "………"
    "……"
    "…"

    sar "Okay, everybody! Now that the fashion contest is over, feel free to order whatever you want!"
    sar "Also, this never happened! Please talk to one of the moms if you are feeling strange or want to lay down!"
    os "Uhh...Wakana, maybe we should start heading out? I don’t really think we should hang around for this."
    w "In a moment. I’d like to speak to the Sakakibara girl first."
    to "Am I late? Did I miss the contest? "
    to "I wanted to take a bath before I arrived and-"
    to "Wait, Yasu?! What on earth happened to your head?!"

    $ renpy.end_replay()
    $ dormwar15 = True
    jump dormwar16
...
```