# Crash of Thunder (Ayane)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Ayane love greater than or equal to 35

* Event [Under the World Tree](./dojo35.md) (Ayane) is completed)

* Day of week is not Friday



## Next events

* [Main: Mana Transfer](./day340.md)

## Event properties

* Id: ayanedorm35
* Group: Ayane
* Triggered by label: ayanedorm
* Triggered by branch label: ayanedorm
* Triggered by path: ayanedorm->ayanedorm35

## Official wiki page

[Crash of Thunder](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=ayanedorm35&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label ayanedorm35:
    play sound "knock.mp3"

    "I knock on Ayane’s door and wait for her to answer. "

    ay "Come in!"

    scene black
    with dissolve
    play sound "dooropen.mp3"

    "She answers right away and entering her room is an incredibly easy process without any additional banter or internal monologuing."
    "I wish opening every door was this easy."

    play sound "static.mp3"
    scene anormaldoor with flash
    stop sound
    stop music

    "There are some doors that you can never open again 61 6e 64 20 73 6f 6d 65 20 74 68 61 74 20 79 6f 75 20 63 61 6e 20 6e 65 76 65 72 20 63 6c 6f 73 65~~~~~~~~~~"

    play sound "static.mp3"
    scene ayanesanapark1
    with flash
    stop sound
    play music "sweetvermouth.mp3"

    ay "Sensei! I’m so glad you decided to show up."
    sa "Um...hi..."
    s "Hey. What are you two up to tonight?"
    ay "Oh, you know. Just hanging around eating doughnuts and trying to convince Sana that Despacito is actually a really good song."
    s "Yes, I can see the doughnuts from here and they look entirely normal."
    s "How is Sana faring with your weird Spanish music?"
    sa "I...have no idea what anyone is saying but...it isn’t the...worst?"
    ay "We were actually just thinking about other stuff to do since the site we normally use to watch movies is down and Sana won’t let me paint her nails."
    sa "I...don’t really want to take my gloves off..."
    ay "Can I paint your nails instead, Sensei?"
    s "Absolutely not and I’m offended that you even asked."

    scene ayanesanapark2
    with dissolve

    ay "Well...what should we do, then?"
    ay "It’s still not super late and I don’t want to just spend the rest of the night sitting around listening to Despacito."
    sa "Yeah...four nights a week would be a little excessive..."
    s "Ayane, are you forgetting that the king of fun is standing right here in front of you?"

    scene ayanesanapark3
    with dissolve

    ay "Ahh, yes! I was so blinded by your handsomeness that I must have forgotten that you’re actually very exciting and full of good ideas!"
    s "Tone it down or it just sounds sarcastic."

    scene ayanesanapark4
    with dissolve

    ay "Psht, don’t tell me how to live my life."
    ay "But do feel free to tell me how to spend my night because I wanna get out of here."
    s "I kind of wanted to stay in..."
    sa "I...can leave if you two want to be alone..."

    scene ayanesanapark5
    with dissolve

    ay "What? No way. You’re in on this too, Sana."
    ay "I’m not going to just ask you to leave because my future husband showed up."
    sa "Really?...It’s okay?..."
    ay "Of course. And I’m sure Sensei’s not opposed either since you’re the cutest little cyclops in Kumon-mi."

    scene ayanesanapark6
    with dissolve

    sa "I...have two eyes, though..."
    ay "Sure you do, Sana. Sure you do."
    ay "So, any ideas? "
    ay "The only thing that’s coming to my mind is the bathhouse. "
    s "Yeah, about that. "
    s "Io works there and it probably wouldn’t be smart for us to go there again."
    ay "Not even if we bathe on different sides and you just listen to us through the fence?"
    s "Been there, done that. It’s a lot harder than it sounds. "

    scene ayanesanapark7
    with dissolve

    sa "You’ve...done that before?"

    if bonus == True:
        ay "Sensei basically raised me. Of course he’s also tried listening to my voice through the fence of a bathhouse before. That’s just part of being a dad."
        sa "If that’s true, I’m...kind of thankful I never really had one."
        s "That’s extremely depressing and I’m going to pretend I never heard it."
        ay "The clock’s ticking, Sensei. Where are you going to take us lovely [young]ladies tonight?"
    else:
        s "I have. Very recently, actually. It was quite relaxing."

    "I have no idea why it suddenly falls on me to plan a night out with these two..."
    "But if Ayane is really that determined to get out and it needs to be a place where none of the girls work-"

    s "Why not just go to the park?"

    scene ayanesanapark8
    with dissolve

    ay "Which one? Because the park closest to the dorms gets swarmed with bugs at night and they always bite me because they can sense that I have the blood of a warrior."
    s "Then...we’ll go to the one near the[school]. "
    sa "Doesn’t...the really cool looking girl in our class hang out at that park?"

    if bonus == True:
        s "Otoha? It’s past her bedtime right now. Her mom would probably kill her if she was out this late."
        ay "But it’s only like 7:00 PM."
    else:
        s "Otoha? You are right. She is very cool."
        ay "Am I cool, Sensei?"
        s "No."
        ay "That was mean."

    s "I said what I said."
    s "So, does that work for you two? Or would you rather go hang out at Sara’s bar instead?"

    scene ayanesanapark9
    with dissolve

    sa "Park...please..."
    sa "I don’t...really want to hang out with my mom when I’m not working..."
    ay "I like Sara...but I like Sana more. So I’m fine with the park if that’s where everyone wants to go."
    ay "It’s a little cold, though, so sorry in advance if you have to keep me warm."
    s "That’s fine. I’d feel a little bad leaving Sana to fend for herself, though."

    scene ayanesanapark10
    with dissolve

    sa "Oh...um...I’ll be okay..."
    sa "You can...focus on Ayane..."
    sa "I’m kind of...the third wheel for this anyway..."
    ay "I love you, Sana. Thank you for relinquishing Sensei to me."
    ay "Just one of his arms is big enough to cover me, though. So I wouldn’t really mind if he used to the other one to-"
    sa "I’m okay. Just...focus on Ayane."
    s "…"
    ay "But you can-"
    sa "Ayane, please."
    s "…"
    ay "…"

    scene ayanesanapark11
    with dissolve

    ay "So be it."
    ay "Sensei will use both of his arms to keep me warm and Sana will freeze to death..."
    ay "But she will die as the best friend one could ever ask for."
    sa "Hahah...yeah..."
    s "…"

    scene black
    with dissolve2
    stop music fadeout 20.0

    "I shrug off the fact that Sana just turned down an easy opportunity to get closer to me and come to terms with only being able to embrace {i}one{/i} cute girl tonight."
    "Or at least that’s what I expect to happen until we go outside."
    "I can’t help but notice on the way that Ayane is walking a little further away from me than normal."
    "I’m not sure if she’s just in a weird mood or if she’s doing this for Sana's sake, but..."
    "I don’t know. There’s probably not much of a point in wasting my energy trying to figure it out when she so often tries to keep the more serious parts of herself hidden."
    "It’s entirely possible that even pointing this out is making a mountain out of a molehill-"
    "But honestly...I’m kind of cold myself."
    "And I wouldn’t mind a small dose of body heat at the expense of making at least one person uncomfortable."

    scene clearnightsky
    with dissolve2
    play music "starvingtodeathoutofreachofthesun.mp3"

    "We eventually make it to the park."
    "I’m not really sure how long it took us to get here, but it feels a lot darker than it did just an hour ago."
    "I look over at the girls, who’ve already started their own conversation and taken off a good twenty feet or so ahead of me."
    "I try to make sense of what they’re saying but am unable to do so over the buzzing of a streetlight and the occasional violent gust of wind."
    "They make it all the way to a picnic table without me hearing a single word."
    "But I doubt they’re talking about anything important to begin with."
    "They’re just being two close friends. Miles apart in personality but only several feet apart from each other in physical distance and circumstance."
    "One parent gone. One parent present. "
    "But {i}how{/i} present, exactly?"
    "It makes me think about {i}my{/i} parents for a moment."
    "What they’d think of me now. "
    "Their names or what they looked like."
    "But nothing comes to mind."
    "Perhaps they never existed at all."
    "Perhaps I’m just some weird creature formed from dropping a few things into a beaker."
    "Like one of those sponges that soaks up water and eventually becomes something bigger."
    "I think we’re all a little bit like sponges."
    "Just, instead of water, we soak up emotions and experiences. "
    "And every once in a while, we wring ourselves out on those with less water in them."
    "They absorb our contents in kind."
    "And grow to resemble more of us than we ever imagined they would."

    scene ayanesanapark12
    with dissolve2

    "And then they smile and wipe it all away."

    if bonus == True:
        "I see none of myself in Ayane when her vaginal cavity isn’t desperately making room for me."
        "But she sees all of herself in me."
        "And I’m not going to make a sex joke this time because even the thought of it is enough to make me shudder."
        "But still."

    ay "I don’t think I’ve ever seen the sky look so pretty before."
    ay "You’d think that all of the lights in this area would make the stars harder to see, but nope! "
    ay "There they are in all of their glory."
    ay "If any of us knew anything about constellations, now would probably be a good time to talk about them."
    sa "…"
    s "…"
    ay "…"
    ay "Anybody?"
    s "Nope."
    sa "I can...maybe find the little dipper if I..."
    sa "Wait...no. "
    sa "I have no idea."
    ay "If only Maya were here."
    ay "She’d be able to point out all of them and then give us history lessons on their names like some kind of weird girl out of a dating game."
    sa "That...does sound like something Maya would do..."
    s "Maya aside, are you two happy now?"

    scene ayanesanapark13
    with dissolve

    ay "Super happy!"
    ay "I was a little worried about the weather but, now that we’re in the light and I can finally start to warm up, I’m actually having a really good time."
    s "Is my embrace not needed anymore?"

    scene ayanesanapark14
    with dissolve

    ay "Your embrace is {i}always{/i} needed, Sensei. I’m just trying to be considerate about the feelings of Sana here since seeing you hug me would make her jealous."

    scene ayanesanapark15
    with dissolve

    sa "Wha-?!"
    sa "No it wouldn’t! "
    sa "I even said it was fine if you did the thing!"
    ay "My vote is for one giant group hug where we all rub up against each other so hard that the friction starts a fire that burns the park down and we all get sent to jail."
    sa "I don’t wanna go to jail!"
    s "I also support the friction idea."
    ay "We’re all waiting on you, Sana."
    sa "But...I...the...friction..."
    sa "Bad!"

    play sound "phonebeep.wav"
    scene ayanesanapark16
    with dissolve

    sa "Huh?"
    ay "Text message?"
    sa "Yeah, but...no one ever texts me this late..."
    sa "Or...in general..."
    s "I’ll text you, Sana."

    scene ayanesanapark17
    with dissolve

    sa "No thank you!"
    sa "It...just looks like it’s my mom anyway..."
    s "What does she want?"
    sa "She...wants me to call her..."

    scene ayanesanapark18
    with dissolve

    sa "Which...I probably should, since...she never asks me to do that..."
    sa "I’m sorry...this will just take a minute..."
    sa "I hope..."
    ay "…"
    sa "…"
    s "…"

    play sound "phonebeep.wav"
    scene ayanesanapark19
    with dissolve

    sa "Umm...hi..."
    sa "Did you...need something?..."
    sa "…"
    sa "…"
    sa "New employee?"
    sa "…"
    sa "Yeah...I can train her..."
    sa "Are you...really able to hire someone, though?..."
    sa "…"
    sa "…"
    sa "Oh."
    sa "Is that...legal?"

    scene ayanesanapark20
    with dissolve

    sa "…"
    sa "Oh..."
    sa "Okay..."
    sa "Then...yeah..."
    sa "I’ll come over...tomorrow night..."
    sa "…"
    sa "…"

    scene ayanesanapark21
    with dissolve

    sa "I don’t want to say it back...I’m with Ayane..."
    sa "Just...I’ll see you tomorrow..."

    play sound "phonebeep.wav"
    scene black
    with dissolve2

    "Sana hangs up the phone and breathes a sigh of relief, having just escaped the deadly clutches of a rather competent Sara given the time of day."

    if bonus == True:
        "Typically, I’d expect her to be passed out with a glass of wine or a sex toy in her hand by now."
        "But I’m glad to hear that the thing with who I assume is Yuki is proceeding smoothly."
        "It seems someone else is a little upset about the call, though."

    scene ayanesanapark22
    with dissolve

    ay "…"
    sa "…"
    s "…"

    "Sana and I immediately sense the sudden shift in Ayane’s mood...But it’s not something that either of us deserves any praise for because it’s about as subtle as a {s}hideous car wreck{/s} crash of thunder."
    "It’s the kind of look that still manages to leak out a bit of hope or...strained joy or...something that’s there to say “There is still more of me.”"
    "“I am not down for the count yet.”"
    "“I-”"

    ay "I miss my mom."

    "Or that."

    scene ayanesanapark23
    with dissolve

    sa "Ayane..."
    sa "I’m...sorry..."
    sa "I should have walked away or-"

    scene ayanesanapark24
    with dissolve

    ay "Oh! No no no no! It’s not your fault!"
    ay "Honestly...I’ve been thinking about her a lot lately. The end of your call just kind of pushed me over the edge."
    s "Is that why you’ve been constantly telling everyone you’re not feeling well?"

    scene ayanesanapark25
    with dissolve

    ay "…"
    sa "…"
    s "I’m going to take your silence as a yes."

    scene ayanesanapark26
    with dissolve

    ay "Being a mom...sounds really hard."
    ay "Everything can be totally fine and then...just go completely wrong out of nowhere."
    ay "Even Sara is amazing to me because she’s able to keep going after all she’s been through."
    ay "Like, wouldn’t it be so much easier to just run away?"

    scene ayanesanapark27
    with dissolve

    ay "I’m sorry for bringing the mood down all of a sudden! It’s just...you know, one of those things."
    ay "Like, parenting in general is something I shouldn’t really talk about because...neither of mine seemed to want me and..."
    ay "And..."

    scene ayanesanapark28
    with dissolve

    ay "Ugh...damn it."
    ay "I told myself I wasn’t going to cry."
    s "You can cry if you want. Neither of us are going to think any less of you for it."

    scene ayanesanapark29
    with dissolve

    ay "I refuse!"

    scene ayanesanapark30
    with dissolve

    ay "Why should I cry because I had two parents who weren’t able to understand how beautiful and talented and smart I am?"
    ay "That’s not fair."
    ay "They should be the ones crying, not me."
    ay "Which is why I’m going to be the best mom ever."

    if bonus == True:
        ay "And...even if the dad...cough cough {i}Sensei{/i}, doesn’t want to be a part of it, I’ll do it all on my own."
        s "I think you’re supposed to actually cough and not just say “cough cough.” "
        s "Also, don’t decide on your own that I’m going to be the father of your children."
        ay "They’ll be {i}your{/i} children too, Sensei! Whether you like it or not!"
    else:
        ay "And Sensei will be the best dad or I will destroy everything he has ever loved, including but not limited to his left leg."

    s "Is that a threat?"
    sa "I want to keep crying, but...this is getting...kind of weird..."

    scene ayanesanapark31
    with dissolve

    ay "It’s not a threat..."
    ay "I’m just saying that...I’m going to be a mom one day. "
    ay "It’s going to happen."
    ay "And when it does, I won’t need your help."
    ay "Which isn’t to say I don’t {i}want{/i} your help. "
    ay "I think you’d be a great father since you were always there for me when mine wasn’t."
    ay "Just...I won’t {i}need{/i} it."
    ay "But please give it to me."
    s "I don’t like this conversation."
    sa "I...don’t either..."
    sa "This is really weird..."

    scene ayanesanapark32
    with dissolve

    ay "Do you believe in me, Sensei?..."
    ay "Do you think I can do it?"
    s "Why does it matter what I think or believe if you’ve already decided? "
    s "You don’t need me, remember?"
    ay "Just tell me you believe in me and I’ll save the whole motherhood thing for another time. "
    s "Why does this have to be a recurring topic? Sana and I desperately want to escape this right now."

    scene ayanesanapark33
    with dissolve

    ay "There is no escape from Ayane Amamiya and her unnamed baby!"
    s "At least give it a name before you start including it in your battle cries."
    sa "Please just tell her...you believe in her, so...we can go home..."

    if bonus == True:
        ay "Listen to the loli, Sensei! "
    else:
        ay "Listen to the sea anemone, Sensei!"

    scene ayanesanapark34
    with dissolve

    sa "Ayane! You know I don’t like it when you call me that!"
    ay "But you’re so cute and precious and just being around you makes me want to scream."
    sa "That has nothing to do with the nickname!"
    s "I believe in you, Ayane."

    scene ayanesanapark35
    with dissolve2

    ay "Really?..."
    s "Yeah."
    s "I doubt it’s worth anything, but-"

    scene ayanesanapark36
    with dissolve

    ay "It is."
    ay "And I won’t let you down."

    if bonus == True:
        s "Great. Just know now that I’m still opposed to impregnating you and-"
        ay "We’ll see about that!"
        s "No. Stop saying that."
        sa "I really {i}really{/i} don’t like this..."
        ay "Great. Now Sana is jealous and wants you to give {i}her{/i} a baby."
    else:
        s "I won't let you down either."
        sa "Wshhhhhhhhhhhhhhhhhhhhhhhhhhhhh. That is the noise the trees are making due to the wind."
        s "I will destroy the trees and restore justice to this world."

    scene ayanesanapark37
    with dissolve

    sa "I really {i}really{/i} {b}really{/b} really don’t want that!"
    s "Sana, I know it’s not intentional, but you’ve made me feel really bad about myself on several occasions tonight."
    sa "I can...almost promise you I feel worse!"
    s "There it is again. "
    s "You’re breaking my heart."
    ay "I’ll fix you up, Sensei. Don’t worry."
    ay "And sorry for turning our fun night out into a smorgasbord of sadness. "
    ay "For what it’s worth, I do feel a lot better now."
    s "Well, as long as {i}one{/i} person leaves here tonight feeling good."

    scene ayanesanapark38
    with dissolve

    ay "I can promise you at least that much..."

    scene black
    with dissolve2

    "The three of us make our way back to the dorm and it takes Sana a full five minutes to relearn how to speak."
    "Ayane goes back to walking just as close to me as she always does."
    "And then wraps her arms around me for even longer than usual when I drop them off."

    $ renpy.end_replay()
    $ ayane_love += 5
    $ ayanedorm35 = True
    stop music fadeout 8.0

    "{i}Ayane’s affection has increased to [ayane_love]!{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label sanadorm45:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label ayanedorm:
    "What do I want to do?"
    menu:
        "Hang out":
            if ayane_love >= 5 and ayanedorm5 == False:
                jump ayanedorm5
            if ayane_love >= 15 and ayanedorm10 == True and ayanedorm15 == False:
                jump ayanedorm15
            if ayane_love >= 20 and dojo20 == True and ayanedorm10 == True and sanadorm15 == True and day == 6 and ayanedorm20 == False:
                jump ayanedorm20
            if ayane_love >= 25 and day != 4 and dojo25 == True and ayanedorm25 == False:
                jump ayanedorm25
            if ayane_love >= 30 and dojo30 == True and ayanedorm30 == False:
                jump ayanedorm30
            if ayane_love >= 35 and dojo35 == True and day!= 5 and ayanedorm35 == False:
                jump ayanedorm35
...
```