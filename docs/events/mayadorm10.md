# Rewind/Repeat/Refuse (Maya)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).



## Event preconditions

* Maya love greater than or equal to 10

* Day of week is not Monday

* Day of week is not Friday

* Event [Secrets Worth Keeping](./mayadorm5.md) (Maya) is completed)



## Next events

* [Maya: You and Me](./shrine15.md)

## Event properties

* Id: mayadorm10
* Group: Maya
* Triggered by label: mayadorm
* Triggered by branch label: mayadorm
* Triggered by path: mayadorm->mayadorm10

## Official wiki page

[Rewind/Repeat/Refuse](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=mayadorm10&go=Go) for more details.

## Event code

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mayadorm10:
    if _in_replay:
        play music "sweetvermouth.mp3"

    play sound "knock.mp3"

    "I knock on the door and wait to see if there’s an answer."
    "And while I'm here to see Maya, I elect to not call out her name as Ami could also be behind the door and I don't want anyone to die today."
    "Granted, I also feel like calling out Maya's name would decrease my chances of being let into the room, so staying silent here really is just the safest bet."

    a "Who is it?"

    "Ami’s voice rings out from what sounds like the back of the room, prompting me to believe that she's already in bed."
    "That, paired with the fact that it wasn't Maya who responded, signals to me that it might be best to just leave at this point."
    "But, then again, a girl is a girl. And if I close my eyes, I'm sure their bodies would feel the same anyway."

    s "It’s me. Can I come in?"
    m "No."
    a "Of course you can, Sensei! Don't listen to Maya!"
    m "Listen to Maya."
    a "The door is open! You can come in whenever you want!"


    scene black
    with dissolve
    play sound "dooropen.mp3"

    m "No. You-"

    scene mayadormten1
    with dissolve

    m "...Can't."
    s "Surprise."
    m "Why must you always do the exact opposite of what I want you to do?"
    s "Because the opposite of what you want me to do is always more fun."
    a "Hey, Sensei. What brings you here tonight?"
    s "Not much. I was just in the area and figured I'd drop by to check in on you two."

    "And by {i}you two{/i} I really just mean Maya since Ami has made it her mission in life for the two of us to always know where the other one is."

    s "So, what are you up to?"
    a "We were just talking. You're welcome to come over here and sit with us, you know. You don't have to just stand there and be all weird."

    scene mayadormten2
    with dissolve

    m "Don't even think about it."
    s "…"

    "I take a step forward to get underneath the kotatsu when I'm suddenly stopped in my tracks by a gaze that could probably kill me if it was any sharper."
    "(Weebnote: A kotatsu is a type of Japanese table with a built in blanket and heat source.)"
    "(Many years ago, they would be heated by a charcoal brazier, but most of them nowadays are electric)"

    a "Don't listen to her, Sensei. She might look scary but, deep down, I know she wants you here too."
    s "I don't know, Ami. That look doesn't exactly scream “I secretly like you.”"
    m "Please continue following that train of thought until you arrive back at your home. Thank you."

    scene mayadormten3
    with dissolve

    a "Maya, how come you’re being so mean all of a sudden? You were fine just a minute ago."
    m "I was in a good mood a minute ago. That mood has since faded."
    m "Whatever could have caused this?"

    "Maya seems even colder than normal today...but I can't remember doing anything in particular that would have set her off."
    "Maybe there's just something bothering her in general?"

    a "I don’t get it."
    a "In fact, you've been acting pretty weird basically every time he's come up lately and-"

    scene mayadormten4
    with dissolve

    m "I have not been acting any weirder than normal. I just don't understand why {i}I{/i} should feel obligated to spend time with someone I dislike simply because you feel the opposite about them."
    a "I just asked him to sit down. It's not like I'm trying to give him a lap pillow."
    s "It’s fine. I really don’t mind standing."

    scene mayadormten5
    with dissolve

    a "Well, I mind! You’re my [uncle] and if I want you to sit under the kotatsu with us you darn well better."
    a "You shouldn't have to suffer just because Maya decided to be a butt."
    m "Oh, okay. So I'll just be the one to suffer instead. That's fine."
    s "You know, I'm just going to sit down now and hope that this spat boils over."

    scene mayadormten6
    with fade

    "I sit down and immediately face Maya, ready to make things even worse for her because that is what I do."

    s "…"
    m "…"
    s "Hey."
    m "Yes, hello."
    s "Come here often?"
    m "At the moment, yes. But I'm having second thoughts of ever returning after tonight."

    scene mayadormten7
    with dissolve

    a "Don’t you feel so much more comfortable now that you’re nice and warm, Sensei? And to think Maya tried to rob you of this opportunity."
    s "Well, it’s summer, so...I was kind of warm in the first place. In fact, why are you two even using a kotatsu when it's basically burning outside every day?"
    a "Having an ice queen who lives in the room tends to make things a little colder."
    m "Wow."
    s "Fair enough. So, are you guys like...studying or something?"

    scene mayadormten6
    with fade

    m "What are we even supposed to study? I can't remember the last time you assigned us any actual work."
    a "Maya, shh. You know that I'll be the one to suffer if Sensei remembers he has a job to do."
    s "There are those...standardized test things, right? Maybe you two were in the middle of studying for those?"
    s "I don't know. I'm just trying to make small talk. Would it kill you to go along with it for a few minutes?"
    m "Probably."
    s "…"

    scene mayadormten7
    with fade

    s "Do you know what’s wrong with her today?"
    a "No clue. Maybe she's just jealous of how much we love each other?"
    m "First off, ew."
    m "Second, why am I being excluded from a conversation at my own kotatsu?"

    scene mayadormten8
    with dissolve

    a "Since when is it just {i}your{/i} kotatsu? We bought it together, remember?"
    m "That gives me 50%% ownership. So why am I not allowed to decide who sits at it and who stands?"
    a "You know, you’re lucky I’m not just getting up and leaving you here with him to punish you for that bad attitude of yours."

    scene mayadormten9
    with dissolve

    m "Good. I don't even want to think about what would happen to me if I were alone in a bedroom with him."
    s "Probably nothing you don't already want to happen."

    scene mayadormten10
    with dissolve

    m "It never ceases to amaze me how confident you manage to be despite being a complete waste of carbon."
    s "It never ceases to amaze me how fun and good at conversation you are."
    m "At the very least, please close your eyes while speaking to me. Each second they spend on my body feels like a thousand toothpicks pressed underneath my fingernails."

    scene mayadormten11
    with dissolve

    a "Hmm..."
    a "You know, maybe I {i}will{/i} leave after all. It's not like I have anything to worry about. Right, Maya?"
    m "Are you not worried about {i}my life?{/i} Because leaving the two of us in a room together puts that at serious risk, you know."
    a "If that's the price that must be paid for two people I love to start getting along with one another, it is a price I must pay."
    m "Hold on. Let me remove all of these toothpicks from underneath my nails so I can have something to poke holes in your backwards logic with."
    a "Maya, you are going to stay right here with Sensei while I go take a shower. Because if you don't, I will reveal your deepest, darkest secret to everyone in class."
    m "What secret are you even talking about? There's nothing you know about me that I wouldn't already reveal to everyone on my own."
    a "I don't know, Maya. What {i}am{/i} I talking about?"
    m "I literally have no idea."

    scene mayadormten7
    with dissolve

    a "Sensei, do you promise to be good if I leave you alone with Maya?"
    m "Please don’t leave. I really don't want to be alone with him."
    s "Sure. I promise to not be inherently evil while you're away."
    a "Great! Then I guess I’ll let you two settle your differences while I go wash my hair."

    scene black
    with dissolve

    m "Ami, stop. You don't have to do this."

    "Ami gets up and grabs a change of clothes before hurrying out of the room."
    "I'm a little surprised that she's okay leaving me completely unattended with another girl, but I guess she's right in saying that there really {i}is{/i} nothing to worry about if it's just Maya."
    "........."
    "......"
    "..."

    scene mayadormten13
    with dissolve

    m "…"
    s "..."
    s "Are you really that afraid of being alone in here with me?"

    "I decide to just come right out and ask what's on my mind, since this expression doesn't exactly match the typical level of disdain Maya normally shows for me."
    "If anything, this seems like genuine worry. But what I don't understand is {i}why.{/i}"
    "All things considered, my actions toward Maya have been extremely tame thus far. My thoughts? Not so much. But I've acted on literally nothing."
    "So the fact that she's so much more opposed to my presence {i}here{/i} and not anywhere on the outside makes me think..."
    "Well, I'm not really sure what it makes me think."
    "But I was finally starting to believe the two of us had been making progress."
    "Now? I'm not so sure anymore."

    scene mayadormten14
    with dissolve

    m "Of course I'm afraid of being alone in here with you."

    if bonus == True:
        m "You're five times my age and three times my size. I fear for my life."
        s "First off, I’m definitely not five times your age."
    else:
        m "I am alone in a room with a man who has devoted his life to hugging everyone and everything this world has to offer. I fear for my life."
        s "Okay, first off, you're right. I am a huggy boy who wants to hug everything."

    s "Second, I’m not going to kill you. I like you."
    m "Why?"
    s "Why what?"
    m "{i}Why{/i} do you like me? "
    m "I avoid you like the plague and you keep coming back. Stop it."
    m "It’s annoying. It’s repulsive. You’re a disgusting man who can't make it so much as an hour without hitting on a teenage girl."
    m "I should report you to the police."
    s "Is it a crime for a teacher to try and get to know his students?"
    m "Do you truly expect me to believe that's what's happening here? Because if so, you're even more pathetic than you look. Which is extremely pathetic, just so you know."
    s "I'm not going to do anything, you know. I'll even let you tie my hands behind my back if you're that afraid of me making a move."
    m "Oh, yes. Fantastic idea. Indulging your disgusting fetishes is exactly what I need to make me more comfortable right now."
    s "What {i}will{/i} make you more comfortable, then? Because you can't just keep avoiding me like this forever."
    m "See, that's just the thing. I {i}can{/i} do that. And I {i}have{/i} been doing that for a very long time."
    s "It can't be that long? You don't look a day older than-"
    m "Time is relative. The specifics don't matter. What {i}does{/i} matter is that everything I have been doing to try and keep you away from me lately has had the exact opposite effect."
    s "Well, if that's the case, maybe {i}you{/i} should try doing the opposite?"

    scene mayadormten14r
    with dissolve

    m "Are...are you saying that by spending {i}more{/i} time with you, it could make you want to see me less?"
    s "I guess so. It's not like what you're doing now is working at all, right?"
    m "That..."
    m "No. That's ridiculous. I'm not the one who needs to change anything. You are. That is the way this works."
    s "The way {i}what{/i} works? Your...weird cycle theory or whatever it was?"

    scene mayadormten14
    with dissolve

    m "It's not weird, it's the way things work..."
    m "Do you {i}really{/i} not realize what your relation to me is?"
    s "No, I really don't. In fact, you’re the only one I’m confused about right now. I know where I stand with all of the other girls."
    m "Ugh..."
    m "You truly are pathetic."

    scene black
    with dissolve2

    "Maya lets out a heavy sigh before tearing herself away from the kotatsu and moving toward the door. "
    "Expecting her to try and leave, I get up as well to stop her. But when she comes to a halt in front of her desk, I realize that the two of us aren't done here yet."

    scene mayadormten17
    with dissolve2

    m "…"
    m "What are you doing?"
    m "I got up to get away from you."
    s "Sorry. It felt weird sitting alone."
    m "It felt weird sitting together too."
    s "I don’t think so at all."
    m "Why not?"
    s "Because I like you."

    scene mayadormten18
    with dissolve

    m "Do you hear yourself right now?"
    m "There are nine other girls lining up for you and you’re wasting your time on the {i}one{/i} that doesn’t want to be near you."
    m "Did being reincarnated scramble your brain or something? Because that would be the only explanation for this that makes any semblance of sense whatsoever."
    s "I mean, it's possible. I really have no way of confirming or denying that."
    s "Also, stop overanalyzing the fact that I said I like you. That could mean a multitude of things."
    m "With you? Yeah, no. You saying you like someone can really only mean one thing. You're not trying to be friends, you're trying to get into my pants."
    s "Everyone else didn't have any trouble believing that I wanted to be friends."
    m "Everyone else is everyone else. They have nothing to do with me."
    s "So what you're saying is that we can literally {i}never{/i} get close? Not even if I do everything correctly and...according to your standards?"

    scene mayadormten19
    with dissolve

    m "That is exactly correct."
    m "We can never be {i}anything.{/i}"
    m "Our paths must remain separate. And we must continue down them until they reach their ends. Only turning around to walk back in the direction we started from."
    m "That is how I want things to be."
    m "So, for the last time, please stop trying to-"

    stop music

    s "No."
    m "…"

    scene mayadormten20
    with dissolve

    m "Excuse me?"
    s "No."
    s "I’m not going to stop trying to talk to you just because you have some weird outlook on life."
    m "Can you stop calling it an outlook when I know for a fact that's just the way things are?"
    s "So what?"
    m "What do you mean {i}so what?{/i} Do you have any idea what sort of things could happen if you just start doing whatever you want?"
    s "No. But I'm not really sure you do either."
    s "I'm not going to just believe you because you're confidently saying you know the way things work. {i}No one{/i} can know the way things work. Life isn't that simple."
    m "You have no idea what you're talking about..."
    s "Maybe I don't. But I don't like your outlook, so I'm going to keep wasting my time on you."
    s "If you don't like that, just keep avoiding me. But don't expect me to give up just because {i}you know how things work.{/i}"
    m "…"
    s "…"

    scene mayadormten20r
    play music "sweetvermouth.mp3"

    m "You are so unfathomably frustrating that it makes me want to pull my hair out."
    s "You think so? Because I thought I sounded pretty cool just now."
    m "Of course {i}you{/i} thought that. You’re a creep. A newborn trapped in an adult’s body."
    s "I can guarantee you that newborns have nowhere near the libido I do."

    scene mayadormten18
    with dissolve

    m "Seriously, how do you fall asleep at night?"
    s "The same way you do, probably. After a heated bout of self-pleasure and-"
    m "Please leave. Immediately. I’m tired of this conversation and I want to go to bed."
    s "Is that code for you wanting to-"
    m "No. It's code for me wanting to close my eyes and forget any of this ever happened."
    s "Maya, come on."

    scene mayadormten20r
    with dissolve

    m "Just go. Please."
    s "..."
    m "..."
    s "Fine. But can I at least ask you something first?"
    m "No. You always want to ask me something. I’m tired of answering your questions."
    m "You’ve been given a new life. Stop wasting it."
    m "I don’t want to be dragged into something that should not exist in the first place."
    s "If I {i}wasn't{/i} reincarnated...and this was actually my real body and my real personality..."
    s "Would that change anything at all?"
    s "Or would you still be treating me like some sort of plague?"

    scene mayadormten21
    with dissolve

    m "I already told you that I'm tired of answering your questions..."
    m "I don’t want anything to do with you. {i}Any{/i} version of you."
    s "And I’ll tell you once again that this isn’t going to stop me."
    m "It should."
    m "But I guess there's no use whining about it if you're going to remain just as stubborn and obnoxious as always."
    m "Do whatever you want. Just don’t expect me to go along with it."

    "Did..."
    "Did I just win?"
    "Is this what it looks like to successfully tire Maya out?"
    "Because, if that's the case, maybe the two of us-"

    m "Oh, and if you think this means that there's a possibility for the two of us to be friends, you’re dead wrong."
    m "I still have no intention of getting to know you. I’m just tired of wasting my breath and I want to go to sleep at a reasonable hour."

    "Damn."

    s "Well, on that note...I guess I’ll leave. "
    m "Fantastic. That's the best news I've gotten all year."
    s "Tell Ami I'm sorry that her mission to bring us closer didn't go according to plan."
    m "Or perhaps Ami knew that this was going to happen...and that's why she decided to put us together in the first place."
    s "Perhaps. But that's assuming she's a lot smarter than she actually is. And this is Ami we're talking about."
    m "Just go already..."
    m "I don't want to do this anymore."
    s "..."
    m "..."

    scene black
    with dissolve2
    play sound "dooropen.mp3"

    s "Fine."
    s "Goodnight, Maya."
    m "..."

    "I manage to make it out of the dorms without bumping into anyone else."
    "Once again, I have no idea if the two of us made any progress or not, but I'm glad I was actually able to speak my mind this time."
    "Or...at least part of it."
    "To be honest, there's a lot more I want to say to her. I just haven't really sorted any of it out yet. Not that I'd expect her to hear me out even if I did. I just-"
    "I don't know."
    "I want to know how she came to be like this..."
    "And why {i}I{/i} seem to be the one person she refuses to get close to no matter what."

    $ renpy.end_replay()
    $ mayadorm10 = True
    $ maya_love += 1
    stop music fadeout 3.0

    "{i}Maya’s affection has increased to [maya_love]!{/i}"
    "{i}You can now spend time with her in her dorm!{/i}"
    "{i}She just won't like it very much.{/i}"
    "………"
    "……"
    "…"

    if day < 6:
        jump endofweekday
    else:
        jump endofsat

label mayadorm15:
...
```

## Code that triggers this event

File: (install folder)\game\DormEvents.rpy

Code:
```python
...
label mayadorm:
        if maya_love >= 5 and day != 5 and amidorm5 == True and mayadorm5 == False:
            jump mayadorm5
        if maya_love >= 10 and day != 1 and day != 5 and mayadorm5 == True and mayadorm10 == False:
            jump mayadorm10
...
```