# Whispers of the World (Makoto)

[Back to event list](./../)

This is generated automatically through code analysis and may include mistakes. For the interactive version of this tool, which looks at your latest savegame to hint the next see the [walkthrough tool here](https://github.com/largestack/Lessons-In-Love-Guide-Tool/blob/main/README.md).


Part of event chain [Twisting Ivy](./nodokaspecial20.md)

## Event preconditions

No event conditions found, it is likely part of an event chain.

## Next events

None

## Event properties

* Id: sadgirls1
* Group: Makoto
* Triggered by label: nodokaspecial20
* Chain sources: nodokaspecial20
* Chain sources path: nodokaspecial20

## Official wiki page

[Whispers of the World](https://lessonsinlove.wiki/index.php?title=Special%3ASearch&search=sadgirls1&go=Go) for more details.

## Event code

File: (install folder)\game\MakotoEvents.rpy

Code:
```python
...
label sadgirls1:
    scene black
    with dissolve2

    "Yasu sets her sights on someone who, up to this point, has managed to stay relatively uninvolved with the chaotic happenings of the morning and urgently makes her way over to her."
    "Caught up in the clamor, the rest of the girls do not see it."
    "But it is the {i}only{/i} thing I see."
    "I don’t know if the whispers of the world find their way into {i}my{/i} ears as well or if I have just placed a large stake of momentary faith in Yasu-"
    "But I keep my eyes and ears focused."
    "For the chances of what happens next being positive in nature seem impossible."
    "And the idea of great misfortune befalling someone who already washes down each meal with it seems too sad to be true."

    scene fatesealedinradiowaves1
    with dissolve2

    mak "..."
    ya "..."
    mak "Um..."
    mak "Can I...help you, Yasu?"
    ya "I’m sorry."
    mak "Sorry for what, exactly?"
    mak "You don’t think this was your fault, do you?"
    mak "Fights are an inevitable aspect of high school life and it’s surprising we’ve managed to make it this far without having experienced one yet."
    mak "I wouldn’t worry too much about it. It’s-"
    ya "I’m sorry for what comes next."
    mak "For what...comes next?"

    scene fatesealedinradiowaves2
    with dissolve

    "Yasu returns to her seat, leaving Makoto mildly perplexed, but mostly unfazed."
    "That’s just the way people hear Yasu’s words now. "
    "She’s spent too long allowing innate fanaticism to dribble out of her mouth that we’ve already deemed it pointless to lend her our handkerchiefs."
    "Which is why what happens next still comes as a surprise to Makoto."

    play sound "pabell.mp3"
    scene fatesealedinradiowaves3
    with dissolve
    $ renpy.pause(4, hard=True)

    vpa "Makoto Miyamura, please come to the front office immediately."
    vpa "I repeat: Makoto Miyamura, please come to the front office immediately."
    mak "The front office? Me? Why?"
    a "I knew it! You’ve been cheating on all of our exams the whole time, haven’t you?! There’s no way one person can be that smart!"
    mi "Wait a sec, there ain’t a second Makoto Miyamura in our school, is there? Cause I know {i}my{/i} Makoto wouldn’t ever get called to the office. "
    ki "Maybe Makoto’s just a rebel and none of us knew about it? "
    n "Or maybe she’s got a secret part time job that the school found out about? I remember seeing something in the handbook about how that's not allowed."
    ki "Did you seriously read the fucking handbook? Who are you?"
    mi "Uhhh...nope! She ain’t got anything like that! Definitely a good girl who focuses on her studies and doesn’t have any sorta job at all! Hahahah!"

    scene black
    with dissolve2

    "Makoto stares up at the speaker in the corner of the classroom, hoping for some added explanation or clarification as to why she’s suddenly being forced out of her comfort zone."
    "When she realizes no such thing is coming, she hesitantly slides her chair out from beneath her desk and slowly walks to the front of the room. "
    "But she stops in front of me, as if I can provide some sort of guidance when we’re all caught in the same storm and can’t even figure out which way is north."
    "I wish I could tell her where to go."
    "I just have no idea what it is she has to avoid just yet."

    scene fatesealedinradiowaves4
    with dissolve

    mak "I take it you haven’t heard anything about this, have you?"
    s "Me? No clue. My plan for today was to just hide in my office. And seeing as {i}you’re{/i} the one who delivers the vast majority of my news to me, the chances of me knowing anything are pretty slim."

    scene fatesealedinradiowaves5
    with dissolve

    mi "You don’t think it could be your family’s store, do you? Noriko was just sayin’ that her last school-"
    mak "I suppose it {i}could{/i} be. But I don’t understand why the PA would need to be used when standard protocol is to have the student’s homeroom teacher inform them of a mandatory meeting."
    mi "Yeah, but...I don’t think anybody else’s job has ever involved this many wieners."
    mak "That is...a fair point. There are certainly an excess of those at the shop."

    scene fatesealedinradiowaves6
    with dissolve

    mak "Regardless, I suppose I should get a move on. If I actually {i}am{/i} in trouble, it wouldn’t be right to keep the office waiting."
    mak "I’m sure it's just some sort of mix-up."

    scene fatesealedinradiowaves7
    with dissolve

    mak "Either that or I’m finally being rewarded for my continued efforts and announcing as much over the intercom would have painted a target on my back."
    mi "Uhh...Makoto? Mind watchin' yourself a little? You’re elbowin’ where my boob's supposed to be."
    s "I guess...let me know if you wind up needing anything. "
    s "Or if this involves me in any sort of way."

    scene fatesealedinradiowaves8
    with dissolve

    mak "Whatever it is, leave it to me."
    mak "There’s no problem Makoto Miyamura can’t handle."
    s "There are plenty of problems Makoto Miyamura can’t handle. I know this because I am one of them."
    mak "Then...correction. There are no {i}school{/i} related problems that Makoto Miyamura can’t handle. So I suggest you let me deal with this on my own."
    mak "The morning’s proven to be exhausting enough already and I know you were looking to avoid confrontation today."
    s "Fair enough. Good luck, I guess. I’ll just have Miku help me clean up any blood that Nodoka may have left behind."
    mi "I, uhh..."
    mi "I ain’t...really a fan of that idea, Sensei..."

    scene black
    with dissolve2
    play sound "slidedoor.mp3"

    "Makoto leaves the room, but instead of grabbing a mop and a bottle of bleach, Miku quickly retreats to my side and grabs hold of my sleeve."
    "She’s the second girl to do that today."

    scene fatesealedinradiowaves9
    with dissolve2

    mi "Sensei..."
    mi "I can’t really describe it, but it feels kinda like my stomach is doin’ flips. This sorta thing ain’t ever happened to Makoto before."
    mi "What if it’s somethin’ really bad? Like...worse than the whole family business thing."
    s "Is there something you had in mind?"
    mi "The only thing I can think of involves you too. And I can’t imagine they woulda let ya come to class like normal if that was the case."
    mi "Ya think maybe we should tail her? Just waitin’ around to-"

    play sound "slidedoor.mp3"
    scene fatesealedinradiowaves10
    with dissolve

    "The door swings open and Miku reflexively latches onto the skin of my arm rather than just my sleeve."
    "I understand why when I see who is in front of it."

    play sound "static.mp3"
    scene fatesealedinradiowaves11
    with flash
    stop sound

    maki "{b}WHERE IS MAKOTO?!?!?!{/b}"
    mi "Sensei..."
    mi "What's Maki doing here?..."
    mi "What’s going on?..."
    maki "{b}WHERE IS SHE?!?!?{/b}"
    s "She just got called down to the office a minute-"

    scene fatesealedinradiowaves12
    with dissolve

    maki "{b}STAY HERE! DON’T FOLLOW ME!{/b}"

    play sound "static.mp3"
    scene fatesealedinradiowaves13
    with flash
    stop sound

    mi "..."
    s "..."

    "Maki slams the door on her way out, putting an abrupt end to the residual fight gossip and replacing it with a brand new flavor of misery."
    "Miku’s grip grows stronger. I can feel the blood vessels beneath my skin rupturing as I attempt to uncover a means of calming her down."
    "Desperate, I look to Yasu of all people, hoping that there’s some new sort of premonition that will tell me when this will end."
    "But she sits unmoving, staring out of the window, and listening to the whispers of the world as it sings the most unpleasant melody it can think of."

    mi "I ain’t ever heard her yell before..."
    s "..."
    mi "I don’t like this, Sensei...I don’t like this at all..."
    mi "You’ve gotta go after ‘em...Waitin’ here ain’t gonna do anything..."
    mi "If Makoto’s in trouble...she needs you to be there for her..."
    s "..."
    mi "She needs your help..."

    "But what help would {i}I{/i} be? Especially after Maki directly told me to not get involved in this."
    "Why doesn’t {i}Miku{/i} help? "
    "Because she’s scared?"
    "What if I’m scared too?"
    "I’m not saying I am, but what if I was?"
    "Why should {i}I{/i} be the one who’s forced to cast that aside?"
    "Is it because I’ve been on this earth longer? Because even that is untrue at this point."
    "Is it because she looks up to me? Because she doesn’t. Not the way she used to. "
    "She knows now just what kind of person I am. Which is why she’s forced to walk alone."
    "Is it because I’m a stand-in for the person she wants to see the most?"
    "Because that-"

    s "..."

    "That one makes sense."
    "And I guess it’s that sort of idea, the idea that someone {i}needs{/i} me, that makes me separate my skin from Miku and carry my ruptured blood vessels out into the hall."

    play sound "static.mp3"
    scene hall_day with flash
    stop sound

    mi "Tell her that...whatever happened, her best friend’s here for her! "
    mi "And that even if she did do somethin’ bad, I’ll always be on her side!"
    mi "Tell her that, Sensei! Tell her that when ya see her!"

    scene black
    with dissolve2

    "I find a happy medium in an ocean of overwhelming sadness and settle on a state of motion somewhere between walking and running."
    "And while swim speeds would make more sense given the analogy, it’s hard to call what I’m doing “swimming” in any sense of the word."
    "Not when every step makes it feel as if the water in my lungs is rising. "
    "Not when every room I peer into in hopes of finding her increases the pressure building up inside of my chest."
    "Not after how every lap I make around the school reinforces the idea that maybe she’s already left."
    "That maybe I was too late."
    "And that I should have just stayed in the classroom like I was told- because at least there are people I can comfort {i}there{/i}."
    "I give up on the idea of being a hero as I have never believed in them in the first place."
    "But in the gap between the first and third floor, there is a space where the water doesn’t rise. "
    "And in this dry spot, my feet revel in the sensation of the scraping of sand- regardless of the shards of seashells finding solace in the safety of my soles."
    "With each step, I connect with the sea in a way I have seldom done before."
    "And if I listen closely, I can hear the ocean pouring out from underneath a bathroom door."
    "........."
    "......"
    "..."

    scene fatesealedinradiowaves14
    with dissolve2

    mak "{b}NO!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!{/b}"
    mak "IT’S NOT TRUE!!! "
    mak "I DON’T BELIEVE IT!!!"
    mak "HE WOULDN’T!!!"
    mak "HE CAN’T!!!"
    mak "NOT WITHOUT SAYING GOODBYE!!!"
    maki "Makoto..."
    mak "DADDY!!!"
    mak "DADDY ISN’T GONE!!! "
    mak "THEY’RE WRONG!!!"
    mak "HE’S ON HIS WAY HOME! HE’S ON HIS WAY-"

    scene fatesealedinradiowaves15
    with dissolve

    maki "Makoto, stop it! Yelling won’t bring him back!"
    mak "But he’s...he’s not gone! He’s not!"
    maki "Makoto!"
    mak "He hasn’t seen my new uniform yet! "
    mak "He hasn’t read my report card!"
    mak "I need him to be proud of me! I need him to be proud!"
    mak "Daddy!"
    mak "Daddy isn’t dead!"

    "A tidal wave crashes into me and forces me back."
    "But as I turn around to watch it disappear along with the rest of the ocean, I’m reminded that this is all just a metaphor I’ve been using to make myself feel better."
    "And that the harsh reality is that I’ve just walked into a private conversation in which the lives of two people who mean something to me are violently dismantled."
    "But when I make an effort to leave, my shoes scuff the floor. "
    "And the abruptness of the sound makes it difficult for me to find another metaphor to cling to."

    play sound "static.mp3"
    scene fatesealedinradiowaves16
    with flash
    stop sound

    maki "I told you not to follow me!"
    s "I didn’t mean to-"
    maki "Leave! Get out!"
    s "I’m sorry. I didn’t know-"
    maki "I said get out! "
    maki "You have nothing to do with this!"

    play sound "static.mp3"
    scene black
    with flash
    stop sound

    "She’s right."
    "I have nothing to do with this."
    "Which is why I don’t have a problem with just walking away."
    "Which is why I don’t spend the next five minutes standing outside of a bathroom door in a hall I seldom visit."
    "Which is why I hear none of what comes next."
    "I’m already somewhere else."

    play sound "static.mp3"
    scene fatesealedinradiowaves17
    with flash
    stop sound

    maki "Hey! Hey! Listen to me!"
    maki "We’re going to get through this! Together! You and me!"
    maki "I know it’s not what you want, but I’m right here! Okay?! I’m right here and I’m not going anywhere!"
    maki "Mommy’s got you!"
    maki "I’ll read your report cards. I won’t really know what they mean, but I’ll read them! Okay?"
    maki "And...I’ll learn to sew! Or something! In case you ever rip your uniform! "
    maki "I’ll do whatever you need! And that includes being proud of you! Because it might not seem like it sometimes, but I am! I am so...{i}so{/i} proud of you."
    mak "I want my dad! "
    mak "I want my daddy!"

    scene fatesealedinradiowaves18
    with dissolve

    maki "I know, baby. I know you do. I want him too. But it’s just us now...and that’s okay!"
    maki "That’s okay because it’s been {i}just us{/i} for a few years anyway, and we’ve been doing great!"
    maki "I’m not saying things will be easy. This is going to be the hardest thing you’ll ever have to go through. But don’t think for a second that you’re alone."
    maki "We’re in this together. We can cry {i}together.{/i} "
    maki "We can miss him {i}together.{/i}"
    mak "It’s too soon! I wasn’t ready!"
    mak "I never got to say goodbye! I never got to say goodbye!"
    maki "We can still talk to him! And wherever he is, he’ll hear us! But for now, just..."
    maki "Just rely on me, baby. Cry as much as you want and I’ll be right here to hold you tight."
    mak "Mom! Tell me it’s not real! Tell me this is all just a nightmare! And that when I wake up, Daddy will be home and we’ll all go on a big trip together!"
    maki "We can still go on a trip! You and me! Mother and daughter! To anywhere you want! Anywhere at all!"
    mak "I want to see my dad!"

    play sound "dooropen.mp3"
    scene fatesealedinradiowaves19
    with dissolve

    maki "Didn’t I tell you stay out of-"

    scene fatesealedinradiowaves20
    with dissolve

    maki "Miku..."
    mi "Maki...Sensei told me where you were but..."
    mi "He wouldn’t tell me what happened..."
    maki "It’s..."
    maki "We can talk later, sweetheart. Makoto needs to-"
    mak "Daddy’s gone! "

    scene fatesealedinradiowaves21
    with dissolve

    mi "No..."
    mi "Makoto, I..."
    maki "Oh, fuck it. Come join us on the floor. You’re basically my second daughter anyway."
    mi "Okay...but...ummm...I’m probably gonna cry too..."
    maki "I really don’t care. She needs all the love she can get right now and I just..."
    maki "I guess what I have isn’t enough..."

    scene black
    with dissolve2
    stop music fadeout 25.0

    "........."
    "......"
    "..."

    $ renpy.end_replay()
    $ sadgirls1 = True

    jump sadgirls2

label sadgirls7:
...
```

## Code that triggers this event

File: (install folder)\game\NodokaEvents.rpy

Code:
```python
...
t "You should be ashamed of yourself."
    s "That’s-"

    scene stillcalm28
    with dissolve

    c "Yumi! What the fuck was that?!"
    c "You were doing so well! You apologized to Futaba! You joined a club on your own! I was so proud of you!"
    c "But...this?!"
    c "How can I be proud of {i}this?!{/i}"
    c "What if something like this happens around Chinami?! What if you decide to snap when I’m not around?! Then what?!"

    scene stillcalm29
    with dissolve

    y "Please..."
    y "Just take me to the fucking office already..."
    c "Yumi..."
    ima "You heard her, Tsuneyo. Let’s get our little prisoner to the principal’s office and hope Sensei has a damn good excuse when we make it back to the classroom."

    scene black
    with dissolve2

    "........."
    "......"
    "..."

    scene stillcalm30
    with dissolve2

    n "Nodoka...you doing okay? I’ve got a whole stash of painkillers in my bag and you look like you could use...a few hundred of them."
    mi "Get up slowly. And if ya feel like yer fallin’ asleep, do your best to...not do that. Wouldn’t be surprised if ya had a concussion at this rate."
    ki "Straight up, I seriously thought you were going to die. So kudos to you for actually living through that."
    no "Heh..."
    no "Heheheh..."
    ki "..."
    ki "Is she seriously laughing right now?"
    mi "Could be brain damage. Wouldn’t be surprised with how many times she got clocked on the head."
    n "I don’t have any pills for that, but ibuprofen works for pretty much anything, so who even knows?"

    scene stillcalm31
    with fade

    o "Sensei, Rin and I are gonna take Nodoka to the nurse’s office."
    r "And, uhh...if you see Futaba...maybe try cheering her up a little? "
    r "She ran out of the room really shaken up once Nodoka started waking up and...probably went back to the dorm. But, just in case she didn’t...you know what to do."
    s "Sure, yeah."
    s "And, uhh...how are you holding up, Nodoka?"
    no "Heheh..."
    no "Heheheheh..."
    no "Sensei..."
    no "It was worth every last punch..."
    s "..."
    no "If getting hit like that...allows me to be the meat of a lesbian sandwich...I should get into fights more often..."

    scene stillcalm32
    with dissolve

    o "Okay. Tell it to the nurse, Rocky. "
    r "The nurse is actually out on Fridays, Otoha. You and I are going to have to take care of Nodoka ourselves."
    no "Wow...today keeps getting better and better..."

    scene black
    with dissolve2

    "Otoha and Rin walk Nodoka out of the classroom, leaving all of their possessions (Including one very bent pair of glasses) behind."
    "The class erupts into a fit of chatter once the door slides closed again as they all begin to discuss what could have caused this."
    "The general consensus is, unsurprisingly, that Yumi is just unhinged."
    "And that this was bound to happen sooner or later."
    "And that they’d be shocked if she’s ever allowed back in school."
    "About how no one ever really liked her anyway."
    "And about how she’s a terrible person with a fetish for tearing others down..."
    "And does what she wants whenever she wants to do it..."
    "And thinks so highly of herself that she won’t even bother showing up to school..."
    "But it’s all wrong."
    "They don’t understand her like I have begun to."
    "And the only person beside me who can actually tell them about her is too busy blocking the incessant chatter out with her hands pressed to her ears and tears streaming down her cheeks."
    "Out of my peripheral vision, I manage to find the only other silent observer in the room right now."
    "And it is at that moment when I realize just how accurate her premonition was."

    scene stillcalm33
    with dissolve2

    s "Well..."
    s "Looks like the “whispers of the world” weren’t lying."
    s "Something bad happened after all."
    s "I’m sorry for doubting you. I just didn’t-"
    ya "That wasn’t it."

    scene stillcalm34
    with dissolve

    s "What?"
    ya "That wasn’t it."

    $ renpy.end_replay()
    $ nodokaspecial20 = True

    scene black
    jump sadgirls1
...
```