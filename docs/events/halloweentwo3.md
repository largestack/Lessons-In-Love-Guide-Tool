# Immernachtreich (Main)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Butterfly Facts](./halloweentwo2.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: halloweentwo3
* Group: Main
* Triggered by label: halloweentwo2
* Chain sources: halloweentwo2
* Chain sources path: halloweentwo2

## Official wiki page

[Immernachtreich](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=halloweentwo3&go=Go) for more details.

## Event code

File: (install folder)\game\ch2script.rpy

Code:
```python
...
label halloweentwo3:
    scene letspartygogogo1
    with dissolve

    "Sana and I make it to the party just as things seem to start picking up, and she quickly seizes the opportunity to slip away from me without saying anything."
    "Thanks, Sana. I really appreciate that after our long and memorable journey to the Amamiya mansion together. "

    sa "Umm...Sensei?"
    s "Oh. You’re still here after all."

    "Nevermind. Sana is just apparently so short that when I turned around to see if she was still there, I must have looked over her head."

    sa "I’m...gonna go...{i}not{/i} hang out with you anymore..."
    s "…"

    "Nevermind again. It appears that Sana has been gone this entire time and that what I heard just now was nothing but a whisper in the wind."

    scene letspartygogogo2
    with dissolve

    r "Yo! Sensei! Over here!"
    s "Oh, good. Someone who actually cares about me."

    scene letspartygogogo3
    with fade

    if bonus == True:
        o "Yo. Figured it was only a matter of time until the token adult showed up."
        s "Yes, it is I. The token adult. Here to tell everyone to abstain from consuming alcohol and to be sure to check in with their parents every hour."
        r "Otoha checked in when we got here, so you don’t have to worry about that part at all."
    else:
        o "Yo. Figured it was only a matter of time until you showed up."
        r "Otoha was able to get away from her conservatorship for another night! Isn't that great?"

    scene letspartygogogo4
    with dissolve

    o "Uh...yeah. But I don’t have to check in again until the party is over, so...lay off for now."
    s "Will do."
    s "So...how are {i}things{/i} with you two?"
    s "Any noteworthy hiccups in the relationship or obstacles worth mentioning as of late?"

    scene letspartygogogo5
    with dissolve

    "I manage to discreetly insert myself into their lovelife and attempt to uncover whether Rin’s recent mistakes have been uncovered or not."
    "And while Rin’s look right now may be screaming, “Why would you ask that?” I’m sure her heart is thanking me for checking in on her in such a mature and inconspicuous manner. "
    "You’re welcome, Rin."

    o "Things are...pretty great, actually."

    scene letspartygogogo6
    with dissolve

    o "It’s not really all that different from how things were beforehand."
    o "We just see each other more often and...say more cute things, I guess? "
    o "I don’t know. I’m not really good at that part. "
    r "Well...we’re taking it slow, right? There’s no need to get good at {i}any{/i} part until you feel good {i}about{/i} it!"
    o "I mean...you can say as much cute stuff as you want. That doesn’t bother me."
    o "It’s the whole “forcing yourself on me and kissing me before I have a chance to breathe” that I want to avoid."

    scene letspartygogogo7
    with dissolve

    r "But you look so kissable! Especially in your bloodsoaked dress! "
    r "I want to kiss you right now!"

    if bonus == True:
        s "Don’t mind me. I’m fine with watching."
    else:
        s "Wait, no. I have to close my eyes first."

    o "For real, though...this has been a lot easier than I expected it to be."
    o "Not that I thought it would be difficult or anything, it’s just..."

    scene letspartygogogo8
    with dissolve

    o "Well...Rin is {i}Rin{/i}, you know? Making things weird and uncomfortable is what she does best."
    r "Hahah...hah..."
    o "She’s just been...really chill so far."
    o "Not really sure what else I can say without turning this into some mushy love fest which, given that you're our teacher, would be a pretty weird situation for all of us."

    "So, it appears that my probing into [kumon_mi_high]’s newest romantic companionship has been successful in that everyone involved is feeling entirely comfortable and not out of place in any way."
    "Just kidding, obviously."
    "I’ve clearly made Rin uncomfortable, but if she’s ever going to get adjusted to lying to the people she cares about, this is something she’ll be forced to handle from time to time."
    "All things considered, I think she’s doing pretty well. "
    "It’s like Otoha has absolutely no idea that beneath Rin’s costume lies symbol after symbol of a pain so great that not even freshly blossoming love can repair it."

    s "So, I saw Futaba with Molly, but where’s Nodoka? Isn’t she normally with you two?"

    scene letspartygogogo9
    with dissolve

    r "Oh, Nodoka’s not coming."
    s "What? Why?"

    scene letspartygogogo10
    with dissolve

    r "Beats me. But I feel like you might be able to figure out the answer if you ask this mysterious, yet extremely familiar stranger who just showed up."
    o "Hah..."

    scene letspartygogogo11
    with fade

    no "Sup, homie."
    o "Nodoka...why?"
    s "That’s not Nodoka. That’s Rin Rokuhara, everyone’s favorite bisexual barista."
    no "Dicks are weird. Let’s go listen to My Chemical Romance and play Halo."
    r "She sounds just like me."
    s "Interesting costume choice."

    scene letspartygogogo12
    with dissolve

    no "I thought it might be entertaining to make Otoha’s life a living hell for a day, so I’ve been trying to trick her into thinking I’m her girlfriend since she woke up."
    o "You two have completely different colored hair...I’m not going to fall for that."
    no "As you can tell, my experiment hasn’t exactly yielded the results I was hoping for."
    no "I will say, though. I feel quite adventurous wearing another girl’s underwear."

    scene letspartygogogo13
    with dissolve

    o "You let her borrow your underwear too?..."
    r "Is that bad? I liked her idea and wanted the experience to be as authentic as possible."
    r "It’s the first time anyone’s ever tried to dress like me. I was just doing what needed to be done."
    o "Dude..."
    s "That does look surprisingly good on you, Nodoka."
    no "Doesn’t it?"
    no "Plus, if I lose my virginity while dressed as Rin, it won’t count because I’m not {i}actually{/i} Nodoka right now."

    scene letspartygogogo14
    with dissolve

    o "That is absolutely not how that works!"
    no "It’s not?"

    if bonus == True:
        r "Sensei, if you’re going to have sex with Nodoka while she’s wearing my clothes, can you make sure you take her underwear off first and not just do that thing where it’s slid to the side?"
        r "I want them back, but not if they have teacher juice all over them."
    else:
        r "Sensei, if you’re going to hug Nodoka, can you get my scarf back first? I don't want it getting tangled around your arms and killing one of you guys."

    scene letspartygogogo15
    with dissolve

    if bonus == True:
        o "You’re not getting them back either way! I’m exercising my right as your girlfriend to not let you share underwear with people!"
        r "What?! Can I at least have my pantyhose back?!"
        o "Stop letting my roommate transform into you!"
        s "People keep talking and not giving me the chance to agree to having sex with you."
        no "Shame. If you’d responded several seconds earlier, I would have actually considered it."
        s "No you wouldn’t. I’m calling your bluff this time, Rindoka Nagahara."
        no "Thinking I’m bluffing will just make it more exciting when you don’t realize I’ve stopped."
    else:
        o "You’re not getting it back! I’m exercising my right as your girlfriend to not let you share scarves with people!"
        r "What?! Why are you so controlling all of a sudden?!"
        s "I will protect the scarf, Rin."

    scene letspartygogogo16
    with dissolve

    o "Okay, you need to leave now. This has gotten too weird and I need to have a talk with these two."
    s "Are you sure? Because it looks like Nodoka and Rin have formed an alliance and you might need someone on your side."
    o "I am sure I’ll manage. Bye, now."

    if bonus == True:
        s "Suit yourself. But don’t come crying to me when you have no idea whose underwear you’re taking off later."
    else:
        s "Suit yourself. Have a good night, everyone."

    scene black
    with dissolve2

    if bonus == True:
        "I leave one of the contenders for “the most sexually charged table at the Halloween party” and make my way over to a small group with a slightly lower combined libido."
    else:
        "........."
        "......"
        "..."

    scene letspartygogogo17
    with dissolve

    mo "What is this? Hath the threads of fate pulled you through the planes of desolation and into the arms of the Prinzessin?"
    s "Yes."
    f "Hey, Sensei...We were just wondering when you were going to show up."
    s "I’ve been here for a little while now, but I’ve just been banished from one of the four tables at the party, so..."

    scene letspartygogogo18
    with dissolve

    mo "Already? What is this, GDQ? "
    mo "Are you attempting to speedrun the Halloween party, Sir?"
    s "Potentially. Though, I’m not sure if there’s anything I could say that would cause either of you two to get rid of me."
    f "I’m...sure there are a few things. But that mostly seems right..."

    scene letspartygogogo19
    with dissolve

    f "Maybe Molly and I just like you more than everyone else here?"
    s "Futaba...you’re not actually flirting with me right now, are you?"
    f "I’m not...{i}not{/i} flirting with you?"
    mo "Careful, Sir. Legends say that this Adeptus once defeated a giant monster in the Archon War with nothing but her behind. The next monster could very well be you."

    if bonus == True:
        s "If that’s how I’m meant to go, so be it."
    else:
        s "You girls and your crazy imaginations~"

    scene letspartygogogo20
    with dissolve

    f "I...don’t have any plans to kill you, Sensei...Let alone in...that way..."

    if bonus == True:
        "I feel slightly disappointed by this news, but ultimately accept that I must continue living for the time being."
    else:
        s "I didn't think you did, Futaba."

    mo "Sir, while you’re here, may I trouble you for some assistance in what I have deemed a rather disappointing matter?"
    s "That depends on what kind of assistance you need and how disappointing the matter is."
    f "Molly...wants me to drink with her."
    s "What? Was last year not a big enough sign that drinking at parties might not really be your thing?"

    scene letspartygogogo21
    with dissolve

    mo "Last year was a mistake! I have grown since then!"

    if bonus == True:
        mo "Not physically, of course. I appear to have stagnated right near the cusp of lolidom. But mentally, Sir! I am ready to drink once more!"
    else:
        s "That's good. I'm sure you're going to be able to completely avoid anything tragic if that is truly the case."
        mo "That is right! I am ready to drink once more!"

    s "Well, I’m not going to stop you. But there’s no point in dragging Futaba into it if she doesn’t want to."
    mo "She is my last hope, Sir! The Kendo Princess is allergic to alcohol, Rin hates me, and the girls from your domain never want to partake either!"

    scene letspartygogogo22
    with dissolve

    f "Rin doesn’t {i}hate{/i} you, Molly...she cares about you a lot..."
    f "She just needs a little time to focus on other things right now...It’s nothing personal."
    mo "By royal decree, cease this irrelevant clamor and partake in the festivities of this Hallowed festival before our descent into the Immernachtreich."
    f "..."
    s "..."
    mo "Drink with me so I can feel less lonely and not pressured to go talk to her."

    scene letspartygogogo23
    with dissolve

    f "Hah..."

    "Suddenly, I get the feeling that this might be a rather depressing Halloween compared to the last one."

    scene letspartygogogo24
    with dissolve

    ki "I’ll drink with you, Molly!"

    "Suddenly, that feeling is validated."

    mo "You?"
    mo "But we have barely exchanged dialogue with one another. I wouldn’t know the first thing about communicating with you."
    s "Do you know the first thing about communicating with...anyone?"
    ki "Well, that’s what the alcohol is for. We can let {i}that{/i} do the talking."
    ki "Have I mentioned how hot you look, by the way? I have no idea what you’re supposed to be, but I love it."
    mo "Oh...umm...thank you?"
    s "Were you just listening in on our conversation or something, Kirin? It’s strange for you to just...jump in like that."

    scene letspartygogogo25
    with dissolve

    ki "Does it matter? Molly wants to drink. I want to drink. I see no issue with this."
    ki "Besides, I’ve been sneaking stuff out of my parents’ alcohol cabinet since middle[school]. I’ll be fine."
    f "It’s...not {i}you{/i} we’re really worried about..."
    ki "Senseiiiii~ Are you really trying to rob me of what could be my only opportunity to see the drunk Molly I heard about at your last Halloween party?"
    s "I’m more or less trying to prevent the arrival of an ambulance in the near future because I know you’ll push her to her limits."
    s "That’s just the type of person you are."

    scene letspartygogogo26
    with fade

    ki "Is it?"

    "Kirin pushes through Molly and Futaba and presses herself up against me."

    if bonus == True:
        "And, as much as I’d like to go along with it, there are almost twenty other girls in this room right now who this could start problems with. "

    ki "Hey, you haven’t complimented my costume yet. How come?"

    if bonus == True:
        ki "I thought you’d like something like this. You know...naughty[school]girl and all that."
        s "Yes. I was unaware up until this very moment that you could be considered one of those. Well thought out costume, Kirin."
        ki "Hey, here’s an idea~"
        ki "How about you...and me...{i}and{/i} Molly go get drunk together? Somewhere private."
        ki "It’s a party, right? Doesn’t that sound fun, Sensei?"
        mo "If this is how it looks to be a protagonist, I am glad that I’m just a heroine."
        f "…"
    else:
        s "..."
        ki "..."
        s "{size=-15}{i}It's lazy and overly-promiscous...{/i}{/size}"

    scene letspartygogogo27
    with dissolve

    mo "Uh-oh."
    ki "Come onnnn~ Why are you being all quiet?"

    if bonus == True:
        ki "You know you want to."
    else:
        s "{size=-15}{i}Because I don't want to hurt your feelings...{/i}{/size}"

    ki "Is it just cause there are other girls around?"
    ki "Cause I know a way for us to slip away and really start getting to the good part of-"

    scene letspartygogogo28
    with dissolve

    ki "...the night."
    s "Uh-oh."
    c "Do you think it’s okay to just go around putting your hands on people like that? "
    ki "I mean..."
    ki "Isn’t that what you’re doing to me right now?..."


    scene letspartygogogo29
    with dissolve

    c "Funny. "
    c "Now, get off of him. He clearly isn't enjoying it."
    ki "What are you even supposed to be?"
    c "Hotter than you. Now go run along and convince someone who actually {i}wants{/i} to be around you to get drunk instead of our teacher."
    s "Wait, were you listening to our conversation as-"

    scene letspartygogogo30
    with dissolve

    c "Hey, Sensei! I didn’t even see you there! Haha!"
    s "But...you just-"
    c "Would you mind coming with me for a second? There’s something I have to talk to you about in private."
    s "Uhh...okay?"

    scene letspartygogogo31
    with dissolve

    ki "Wha-"
    ki "What the fuck just happened?"
    mo "Chika OP. Please nerf."

    scene black
    with dissolve

    "………"
    "……"
    "…"

    scene letspartygogogo32
    with dissolve

    s "You don’t actually have anything you need to talk about, do you?"

    if bonus == True:
        c "Nope! I just didn’t like watching that little slut put her hands on you."
    else:
        c "Nope! I just didn’t like watching that Kirin put her hands on you."

    scene letspartygogogo33
    with dissolve

    c "Like, really though! Who does she think she is dressing up like that? You can straight up see her bra. It’s barely even a costume."
    s "In her defense, your costume is a little more...revealing."

    if bonus == True:
        scene letspartygogogo34
        with dissolve

        c "True. But it’s not like you haven’t already seen me naked, soooo...I see no problem. Do you?"
        s "Not...really."

    scene letspartygogogo35
    with dissolve

    c "Oh! You didn’t see Yumi on the way over, did you?"
    c "I know you came with Sana, so I’m not sure if you like, bumped into her on the way and knew if she was coming or not."
    s "Why not just text her? "
    c "I’ve obviously texted her already if I’m asking you, Sensei. She just didn’t respond and I want to make sure she’s not being a brat again."
    s "Maybe she’s just...taking longer than normal to change into her costume?"

    scene letspartygogogo36
    with dissolve

    c "Yeah, I’m sure her “Antisocial [teenage]birthday girl” costume is a lot harder to put on than my...gypsy dancer or whatever this outfit is supposed to be."
    s "You don’t even know?"

    scene letspartygogogo37
    with dissolve

    if bonus == True:
        c "Nope. I just saw it at the Halloween store and thought it might make you horny, so I bought it."
        s "Ahh, yes. A respectable strategy."
        c "Is it working? "
    else:
        c "Nope. I searched the entire Halloween store for a clown costume to try and make you happy, but I couldn't find any and had to panic pick this."
        s "Well...at least you tried."
        c "Say, why do you like clowns so much anyway?"

    scene letspartygogogo38
    with dissolve

    s "How would you like to find- actually, nevermind. Hold that thought."
    c "Awwww boo~"
    n "Um...do...do you have a sec?"

    scene letspartygogogo39
    with dissolve

    s "Yeah. This is the part where everyone comes up to me and says hi, so say your piece now while you still have the screen time."
    c "Oh. My. God."
    c "Is...Is...Is..."
    c "Is that...Niki’s actual...stage outfit from the “Be My Fire” tour?"
    n "Oh...yeah. She let me borrow it for Halloween."
    s "Niki wore {i}that{/i}?"

    scene letspartygogogo40
    with dissolve

    c "Yes! But only {i}three{/i} times before it was discontinued for being too out of line with what her production company wanted her image to be!"
    c "It’s super, {i}super{/i} rare! Like, you can’t even find videos of it online anymore because they were all taken down!"
    s "Then...how do you even know about it?"

    scene letspartygogogo41
    with dissolve

    c "Never underestimate a true fan, Sensei. I know everything about Niki. {i}Everything.{/i}"

    if bonus == True:
        "I doubt you know that she’s a virgin who I recently fingered in a hotel room."
        "But that’s good. Because if you did know that, both of us would likely be dead."

    n "Uh...sorry to kill the mood and stuff, but is it okay for me to steal Sensei for a minute or two?"

    scene letspartygogogo42
    with dissolve

    c "Aww! But I just got him!"
    n "It won’t be long...I just have to ask him something."
    s "Can you not just ask it here?"

    scene letspartygogogo43
    with dissolve

    n "I...can’t..."
    n "I’m sorry. It needs to be in private."
    c "{i}Hah...{/i}Do you accept this invitation, Sensei?"
    s "I accept this invitation, Chika. Thank you for becoming my new, unofficial secretary. Please don’t tell Makoto."
    c "Just...okay. Yeah. Whatever."
    c "I’ll...let you know if I hear back from Yumi."

    scene letspartygogogo44
    with dissolve

    "Chika disappears back into the crowd of party goers, leaving Noriko and me on the outskirts of the room, seemingly unnoticed by everyone else for the time being."
    "I’m not really sure what this could be about, but she definitely looks a little more serious than normal."
    "So...whatever the problem is, I hope it’s nothing big."

    n "Come outside with me for a sec."
    s "Oh. Sure."

    scene black
    with dissolve2
    stop music fadeout 25.0

    $ renpy.end_replay()
    $ halloweentwo3 = True

    jump halloweentwo4

label halloweentwo4:
...
```

## Code that triggers this event

File: (install folder)\game\ch2script.rpy

Code:
```python
...
yu "Uh...yeah..."
    yu "If it’s not a problem, I mean."
    yu "And..."

    scene halloweentwobar32
    with dissolve

    yu "If you could maybe give her this, too..."
    yu "It’s not much, but...I don’t really have a lot I can spend and-"
    s "Sure thing."
    s "I’m not sure if she’ll accept it, but I’ll definitely give it to her if she shows up to the party tonight."
    yu "Thanks, man. Remind me to buy you ramen sometime when the power’s not getting all fucked at Tojo's anymore."
    s "Did it happen again after the last time?"
    yu "Just once more that I’ve noticed since then, but Tsu-chan still wouldn’t let me go near her dad."
    s "Huh. Weird."
    sa "Sensei? We...really need to go..."

    scene halloweentwobar33
    with dissolve

    yu "Oh, shit. My bad. I was-"

    scene halloweentwobar34
    with dissolve

    yu "The fuck are you supposed to be?"

    scene halloweentwobar35
    with fade

    sa "…"
    s "…"
    sa "Bad at Halloween..."

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    q "Excuse me!"

    scene halloweentwobar36
    with dissolve

    k "Ah! Customerburger!"
    k "I like your butterfly! "
    k "Did you know that the average lifespan for the red admiral butterfly is approximately ten months?!"
    sar "Kaori, what did I tell you about giving insect facts to the customers {i}before{/i} taking their orders?"
    q "Noooooo tell me more butterfly facts. I wanna know!"

    scene halloweentwobar37
    with dissolve

    k "Then...did you know there are over 24,000 species?! And that some of them can fly up to 12 miles per hour?!"

    scene halloweentwobar38
    with dissolve

    q "Ahh, yeah. That’s the stuff."
    q "Inject that lepidopterology right into my veins, baby."
    yu "Uhh...she botherin’ you? Cause if you’ve got somethin’ you wanna order-"

    scene halloweentwobar39
    with dissolve

    q "Not at all! I’ll take three of whatever your favorite thing on the menu is."
    yu "Aight. Three beers. Got it."
    sar "Yuki, come on! Upsell! Profits! Business lingo!"
    yu "What? She asked for my favorite thing on the menu."

    scene halloweentwobar40
    with dissolve

    if bonus == True:
        k "You are very pretty, Miss. Are you really having such trouble fornicating that you had to come here?"
    else:
        k "You are very pretty, Miss. Are you really having such trouble finding a hug partner that you had to come here?"

    q "Woah. The flier said “Halloween Party,” but I didn’t realize that’s the sorta thing I was getting myself into."
    q "Do you hit on everyone with butterfly related trivia or am I just lucky?"

    scene halloweentwobar41
    with dissolve

    k "Hitting {i}on!{/i} I know what that means now!"
    q "Hahahah! I love this place already!"

    scene black
    with dissolve2

    "………"
    "……"
    "…"

    $ renpy.end_replay()
    $ halloweentwo2 = True

    jump halloweentwo3
...
```