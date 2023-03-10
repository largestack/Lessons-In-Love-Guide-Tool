# Now More Than Ever (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maya love greater than or equal to 30

* Event [What it Means to Be Destroyed](./mayadorm30.md) (Maya) is completed)

* ami_virgin equal to False (unknown variable)



## Next events

None

## Event properties

* Id: shrine30
* Group: Maya
* Triggered by label: shrine
* Triggered by branch label: shrine
* Triggered by path: shrine->shrine30

## Official wiki page

[Now More Than Ever](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=shrine30&go=Go) for more details.

## Event code

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label shrine30:
    scene mayalantern1
    with fade
    play music "shrinesong.mp3"

    "I spot Maya shortly after arriving at the shrine and make my way over to her."
    "It’s still suspiciously warm around here (For reasons I’ve yet to understand), but it seems that she’s taken up shelter in a booth with her back to a pair of large glowing lanterns."
    "I can feel their heat from here, which is great considering her gaze is ice cold."
    "Here’s hoping they thaw her out sometime soon."

    s "Yo."
    m "…"
    s "What’s up?"
    m "…"
    s "Are you ignoring me now?"
    m "I’m conserving energy."
    s "Are you about to go into hibernation for the rest of the winter or something?"
    m "I wish."
    s "What do you need to conserve energy for?"
    m "Daily activities. Getting out of bed. Brushing my teeth."
    m "An overabundance of stress from having to put up with you all the time."
    m "The usual."
    s "Is there an extra spot inside of that booth? There’s this one girl who keeps bossing me around and it’s getting to me as well."

    scene mayalantern2
    with dissolve

    m "Stop saying that I’m bossing you around. I haven’t asked you to do a single thing today."
    s "I mean...I just got here."
    m "And {i}I{/i} got the message loud and clear the other night. "
    m "You’re not going to ignore Noriko, so I’m just going to have to figure out a new way to deal with that."
    m "If you wind up disappearing, though, don’t say I didn’t warn you."
    m "I mean...you wouldn’t be able to say anything because you disappeared. But you know what I mean."
    m "It’s not like she has anything interesting to tell you anyway. Your old life was boring and sad."
    s "You get really grumpy when you’re stressed, huh?"
    m "I’m hungry, too. But I have to hang out at this stupid shrine and pretend there is a god."
    m "It’s quite taxing."
    s "Just leave if you hate it here that much."
    s "Let’s go get lunch or something."

    scene mayalantern3
    with dissolve

    m "Together?"
    s "Maya, we’ve eaten together several times."
    m "Not {i}lunch{/i}, though."
    m "We’ve always gone out late at night so I wouldn’t feel weird about anyone seeing us together."
    m "And I was only fine with Uta seeing us because, until recently, I didn’t think it was possible for fate to get so out of sorts that she’d wind up several desks away from me."
    m "And even though all we did was eat, I now have to face her constant accusations about us being boyfriend and shrine maiden."
    s "Why not just say “boyfriend and girlfriend?”"
    m "I was about to, but I got nauseous."
    s "I figured as much."
    s "I wouldn’t worry if I were you, though."
    s "I’m pretty sure that everyone knows we’re not romantically involved by now."

    scene mayalantern4
    with dissolve

    m "Yeah...I don’t really know if that’s exactly true anymore."
    s "What do you mean?"
    m "I mean that my...reaction to Noriko’s appearance in class has caused some people to second guess the nature of our relationship."
    s "Really?"
    s "Well, I guess this means we have to start dating."

    scene mayalantern5
    with dissolve

    m "Please don’t joke about things like that."
    m "Until now, I managed to fly completely under the radar and not get wrapped up in any of your senseless hidden romance drama."
    m "Now, even Ayane is accusing me of having feelings for you. And I hate seeing Ayane act serious. It’s unsettling."
    s "Yeah...that doesn’t happen often, does it?"
    m "The point is...it’s important, now more than ever, for the two of us to maintain distance."
    s "Ever? In all of the gajillion years we’ve known each other?"

    scene mayalantern6
    with dissolve

    m "First off, that’s not even a real number."
    m "Secondly, don’t get into semantics with me."
    m "When someone says “now more than ever” it very rarely means “now more than ever.”"
    m "It just means that it’s extremely important. Which it is."

    scene mayalantern7
    with dissolve

    m "The two of us are not to be seen out and about with one another. There is far too much at stake."
    m "This has been a rule for a very long time, Sensei. You should be fully aware of it by now."
    s "I never really thought of it as a “rule.” I just figured that’s how you are."
    m "And in thinking that, you are exactly right."
    m "I’m cold and blunt. A kuudere with slowly dissipating “cool” and “dere” buried somewhere so far underground that you’ll likely never find it."

    if mayadorm35 == True and bonus == True:
        "Yeah, I'm pretty sure I found it when she almost [rape]d me the other night."

    s "The “dere” part exists?"
    m "That was mostly a joke. You weren’t meant to take it seriously."
    s "Too late. I need to go buy a shovel."
    s "See you, Maya."

    scene mayalantern8
    with dissolve

    m "You’re disgusting."
    s "That may very well be true, but I’m not the one under suspicion, now am I?"
    m "What are you talking about? You’re literally always under suspicion."
    m "Any of those poor girls who think you’re not two...three...or ten-timing them are just choosing to be ignorant about it."
    s "And yet {i}you’re{/i} the one Ayane is apparently questioning."
    m "Oh please. As if she hasn’t questioned you as well."
    m "What did you tell her? That you can’t promise to be with only her but that she’s still extremely important to you or blah blah blah?"
    s "Wow. You really {i}are{/i} grouchy today."
    m "The grouchiest."
    m "I can’t remember the last time I actually had to think this much. It’s putting me on edge."
    s "Well {i}I{/i} personally like this side of you."
    s "It feels like we’re getting somewhere."
    m "{i}This{/i} is your idea of getting somewhere? Slightly more facial expressions and openly confronting you about your relationships with my friends?"
    s "Sure. We’re talking about things I can finally understand."
    m "You understand all of the other stuff we talk about as well. You just choose to act aloof about it because the second a theory starts sitting in your head, it becomes too real and you want to run away."
    m "It’s just how your brain is wired."

    if bonus == True:
        m "Mine is the same way, but with less pent up sexual aggression and more quantum theory and food."
    else:
        m "Mine is the same way, but with less pent up desire to hug everything and more...quantum theory and food."

    if mayadorm35 == True:
        if bonus == True:
            s "Trivia time. Which of the two participants in this conversation has mounted the other in an effort to coerce them into sex?"
        else:
            s "Trivia time. Which of the two participants in this conversation has mounted the other in an effort to force them into a hug?"

        scene mayalantern2
        with dissolve

        m "Stop bringing that up!"

        if bonus == True:
            s "I'm just countering your whole thing about not being sexually aggressive when my personal experiences prove otherwise."
            m "That didn't count! It was an act of desperation, not sexual aggression!"
            m "I'm done talking about this!"
        else:
            s "All I'm saying is that there is clearly more than one hug addict at this shrine right now."
    else:
        if bonus == True:
            s "Is there any sexual aggression in there at all?"
            s "Up until now, I’ve gotten a really intense asexual vibe from you."
            m "Good. Please continue to think that. I’m not open to discussing those sorts of things."
        else:
            s "Do you even like hugs, Maya? Because I really have no idea how you feel about them."
            m "They are certainly a thing that exists."

    s "You’re such a buzzkill."

    if bonus == True:
        m "How? You have half a classroom worth of girls who you’re likely sleeping with already. Talk to one of them about that if you truly need to."
    else:
        m "How? You really expect everyone else around you to think about hugs just as frequently? Give me a break."
        m "Like, have you ever actually thought about how weird the concept of hugging even is? It's fucking wild, dude. I don't get it at all."
        s "But they are so warm and soft and nice."

    m "I’ll continue to sit inside this booth and think about clouds."
    s "…"
    m "…"

    if bonus == True:
        s "Okay, so let’s say that...theoretically, I {i}am{/i} sleeping with some of the girls."
    else:
        s "Okay, so let’s say that...theoretically, I {i}have{/i} hugged a sizable portion of the cast."

    m "…"
    s "How would that make you feel?"
    m "…"
    s "…"
    m "What is this?"
    m "Are you trying to get me to say I’m jealous?"
    s "I’m searching for the “dere.”"

    scene mayalantern9
    with dissolve

    m "Hah..."
    m "I’d feel the same exact way I’ve felt all along."

    if bonus == True:
        m "You’re a horrible person with a disgusting addiction and an affinity for girls well under the age you should be setting your sights on."
    else:
        m "Hungry and tired."

    scene mayalantern10
    with dissolve

    m "And even though I think that side of you is despicable and wish it would go away...I don’t hold it against anyone."
    m "Well, maybe I do hold it against you. But not any of them."
    m "They’re just normal girls who are blissfully unaware that they’re caught in a loop."
    m "Falling for version after version of the same [high_school] teacher but failing to truly capture him each and every time."
    m "It’s actually quite sad...watching them bend and break so many times."
    s "Wait, what happened to their memories persisting through resets? What’s all this about bending and breaking?"

    scene mayalantern11
    with dissolve

    m "Perhaps you’ll find out in due time?"
    m "Unless, of course, you wind up poking your nose deeper into the past and get your slate wiped clean again."
    s "Are you saying that once I’m gone, they’ll be gone too?"
    m "Is that what you think?"
    s "I’ve given up on thinking when it comes to getting all deep and introspective like this."
    m "Boy, do I wish I could do that."
    m "Take a moment and think back to when you first arrived here."
    m "Everyone already had preconceived notions of the type of person you were, correct?"
    s "Yeah. But wasn’t that just because that’s how the original Sensei was?"
    m "Interesting theory."
    m "I can see why you’d think something like that."
    m "But you’re wrong."
    m "What you were witnessing in those moments were their memories being rewritten."
    m "Didn’t you think it was strange how quickly some of them warmed up to you despite undergoing a complete switch in personalities?"
    m "How everyone just {i}decided{/i} that not actually being taught anymore was a totally normal thing?"
    m "Are you familiar with computers? I want to make a comparison, but I’m not sure if you’ll understand."
    s "Feel free. I’m already lost, so any comparison at all could possibly help."
    m "Computers don’t have brains like humans do. They have hard drives."
    m "Over time, those hard drives fill up with information a user collects and saves."
    m "If a household only has one computer and every resident of the house uses it, that storage space will begin to fill up rather quickly."
    m "So, in order to make space for new information, old information needs to be deleted."
    m "Or reformatted entirely in more severe cases."
    m "What you were experiencing in watching those girls adapt to you was a type of reformatting."
    m "They were freeing up space in their minds to make room for the “new” you."
    m "And unless you do something to ruin them, which you likely will since you are horrible, that will be how they remain until a new user comes along."
    m "Do you understand?"
    s "I think so...but..."
    m "But what?"
    s "Why the fuck did you take so long to tell me this?"

    scene mayalantern12
    with dissolve

    m "Because I needed you to fail to a certain extent."
    m "And you failed wonderfully."
    m "Good job, Sensei."

    scene mayalantern13
    with dissolve

    if bonus == True:
        m "I really wish you didn’t go all the way with Ami, though."
        m "I hate watching her get hurt after everything that she’s been through."
    else:
        m "I really wish you didn't hug Ami so often, though."
        m "That sort of relationship with your accountant will only end in destruction and lower tax refunds when you inevitably sever ties."

    s "…"
    m "…"
    s "You..."

    scene mayalantern14
    with dissolve

    m "Did you really think you would be able to hide that from me?"
    m "Or, scratch that, did you really think {i}Ami{/i} would be able to hide that from me?"
    m "We’re both [teenage]girls at the end of the day."
    s "You are...surprisingly unfazed by this."
    m "Oh, I judge you harshly for it."
    m "I’m just used to it by now."
    m "Accepting your shortcomings and flaws is something I will never find joy in, but something I must do nonetheless."

    if bonus == True:
        m "Expecting you to make it through an entire loop without manipulating one of the girls into sex acts is like expecting me to not make it through without..."
    else:
        m "Expecting you to make it through an entire loop without a hug is like expecting me to not make it through without..."

    s "…"
    m "…"
    m "What is something weird or bad that I do?"
    s "You talk about the sky a lot."

    scene mayalantern7
    with dissolve

    m "Yes, that. It’s like expecting me to make it through a loop without bringing up the sky."
    m "The key difference is that my crutch doesn’t hurt anyone and yours hurts everyone."
    m "Just not right away."

    if bonus == True:
        s "It definitely hurts some of them right away."
    else:
        s "Hey, do they make that shrine maiden outfit in my size by any chance?"

    m "…"
    s "…"

    scene mayalantern3
    with dissolve

    m "Why do you always have to ruin everything?"

    if bonus == True:
        m "Just because I know about what you’re doing with everyone doesn’t mean I want to {i}hear{/i} about it."
        m "Have some respect."
        s "I will. Because even though you allegedly know what I allegedly do in all of my alleged spare time..."
        s "You still haven’t done anything to make me pay for it."

        scene mayalantern11
        with dissolve

        m "What would I do? I’m just a normal [teenage]girl."
        s "I don’t know. But I’m glad it’s nothing."
        s "Either way...I’ll see if I can talk to the others about how there’s definitely nothing going on between us."

        scene mayalantern10
        with dissolve

        m "Yeah. Thanks."
        m "…"
        m "That would be a big help."

    scene black
    with dissolve2

    "Maya and I remain situated at the booth for a little while longer."
    "The sun retreats behind the clouds, creating a darkness that swallows me whole."
    "Maya remains safe, illuminated by the glow of her giant lanterns as I am left to figure out where to go from here."
    "I learned a lot more than I normally do with Maya today."
    "In fact, for the first time ever, I might be leaving with more answers than questions."
    "I should probably cherish this moment."
    "But for some reason-"
    "I just keep worrying about her."

    $ renpy.end_replay()
    $ maya_love += 1
    $ shrine30 = True
    stop music fadeout 5.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "………"
    "……"
    "…"

    jump saturdaynight

label shrine35:
...
```

## Code that triggers this event

File: (install folder)\game\MayaEvents.rpy

Code:
```python
...
label shrine:
    if howifeel == True:
        jump howifeel
    if maya_love >= 0 and firsttimeshrine == False:
        jump firsttimeshrine
    if maya_love >= 5 and shrine5 == False:
        jump shrine5
    if maya_love >= 10 and shrine10 == False:
        jump shrine10
    if maya_love >= 15 and shrine10 == True and mayadorm10 == True and shrine15 == False:
        jump shrine15
    if maya_love >= 20 and beachvacation16 == True and mayadorm15 == True and shrine20 == False:
        jump shrine20
    if maya_love >= 25 and mayadorm20 == True and shrine25 == False:
        jump shrine25
    if maya_love >= 30 and mayadorm35 == True and shrine35 == False:
        jump shrine35
    if maya_love >= 30 and mayadorm30 == True and ami_virgin == False and shrine30 == False:
        jump shrine30
...
```