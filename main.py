def selectNext(options):
  val = 0
  i = 1
  for option in options:
    print(f'{i}: {option}')
    i += 1
  while (val < 1 or val > len(options)):
    try:
      val = int(input("What option would you like to do?: "))
    except ValueError:
      val = -1
  return val

def newLine():
  input()

def displayText(text):
  print(text)
  newLine()

def goBackRestart(func):
  val = selectNext(["Restart from start", "Restart chapter"])
  if val == 1:
    displayIntroduction()
  else:
    func()

def displayIntroduction():
  print("Welcome to my ethics text based adventure game, where you lead the development of a metaverse product")
  print("Press enter after a line to continue...")
  newLine()
  displayText("Case studies and definitions are from Ethics, Technology, and Engineering by Ibo van de Poel")
  displayText("There aren't too many chapters, but each option will lead to a different outcome. Try out all of them to see what happens! If you choose an option that leads to an ending, you have the option to restart the chapter")
  displayText("You sit at your desk, contemplating the enormity of the task ahead of you. As the newly appointed project lead for the metaverse headset, you know the weight of this responsibility rests squarely on your shoulders.")
  displayText('Your phone buzzes - it\'s a message from the CEO. "Congratulations Steve on your appointment as project lead for the metaverse headset. I know you\'re the right person to make this vision a reality. The future is in your hands."')
  displayText('You take a deep breath, already feeling the pressure to deliver. But you can\'t help but feel a sense of excitement and possibility. This is your chance to redefine the future. "I won\'t let you down," you respond. "This headset is going to change the world."')
  displayText("You lean back in your chair, mind racing with ideas. The potential of this technology is limitless - expanded field of view, deeper haptic feedback, more natural hand tracking. But where do you even begin?")
  displayText("You remember the Fundamental Ethical Responsibilities of Engineers you learned when you took Engineering 125, which were…")
  displayText('1. "To not cause harm or create an unreasonable risk of harm to other (or to public welfare or to the public interest) through their engineering work')
  displayText('2. To try to prevent harm and any unreasonable risk of harm to others (and to public welfare and the public interest) that is caused by their engineering work, or by the engineering work of others in which they are involved, or about which they are technically knowledgeable')
  displayText('3. To try to alert and inform about the risk of harm those individuals and segments of the public at unreasonable risk of being harmed by their engineering work, by the engineering work of others in which they are involved, or about which they are technologically knowledgeable')
  displayText("You aim to follow these as you work on the project…")

  displayChapterOne()

def displayChapterOne():
  displayText("CHAPTER 1: ETHICAL ASPECTS OF TECHNICAL RISKS")
  displayText('Just then, there\'s a knock at your office door. Your lead engineer, Sarah, pokes her head in. "Got a minute? I want to hear your thoughts on the risks between making this product full-dive or non-full-dive."')
  displayText("You remember that full-dive technology immerses users completely into a virtual environment, often involving direct neural interfaces for sensory input. In contrast, non-full-dive experiences maintain a level of separation between the user and the virtual world, typically utilizing augmented reality or less immersive interfaces.")
  displayText("As you think about what to do, you remember a case study about risk assessment from your class…")
  displayText("“Between 1900 and 1975, about 600 million tons of coal were mined in the province of Limburg in the Netherlands (Pöttgens, 1988). In an area of about 220 km2 the surface dropped about 2.5 m on average. In some locations there was a drop of more than 10 m. The coal mining operations were damaging the houses. Hundreds of millions in damages were paid by the companies mining the coal. The risk of damage to the houses was known in advance, but it was thought to balance out against the benefits of the coal mining.”")
  displayText("You also remember the following definitions…")
  displayText("Safety: The condition that refers to a situation in which the risks have been reduced as far as reasonably feasible and desirable. ")
  displayText("Acceptable risk: A risk that is morally acceptable. The following considerations are relevant for deciding whether a risk is morally acceptable: (1) the degree of informed consent with the risk; (2) the degree to which the benefits of a risky activity weigh up against the disadvantages and risks; (3) the availability of alternatives with a lower risk; and (4) the degree to which risks and advantages are justly distributed.")
  displayText("Sarah chimes in \"Well, the full-dive approach opens up incredible possibilities in terms of sensory immersion and seamless human-computer integration. But the risks around addiction, psychological impacts, and even physical safety are significant. On the other hand non-full-dive, we maintain that separation between the user and the virtual world, which reduces those risks. But we also limit the depth of the experience and potentially the transformative power of the technology\"")
  displayText("What do you decide?")
  
  next = selectNext(["Non-full-dive helmet", "full-dive-helmet"])
  
  if next == 1:
    displayText("You consider the implications of both the full-dive and non-full-dive approaches, weighing the tradeoffs carefully. After much deliberation, you make your decision.")
    displayText("\"After reviewing the risks, I believe the responsible path forward is to pursue a non-full-dive metaverse headset,\" you declare. \"The potential dangers of complete sensory immersion and neural integration are simply too great. We have to prioritize user safety and well-being.\"")
    displayText("Sarah nods, her expression serious. \"I was leaning the same way. The psychological and societal risks of full-dive technology are just too high, at least in this first iteration. We need to take a more measured, cautious approach.\"")
    displayText("You both agree on the non-full-dive approach, feeling confident that this is the best way to move forward. However, just as you're about to continue your planning, your phone rings. It's a call from the executive team.")
    displayChapterTwo()
  else:
    displayText("You stand your ground, unwavering in your belief that the full-dive approach is the path to a revolutionary new frontier. \"We've taken every precaution. The level of immersion and neural integration is unparalleled - this technology will redefine human experience as we know it.\"")
    displayText("Sarah looks uneasy, but nods reluctantly. \"I trust your judgment, but the risks still concern me. What if something goes wrong? The consequences could be catastrophic.\"")
    displayText("You place a reassuring hand on her shoulder. \"We've accounted for every eventuality. This headset is the future - we have to be willing to take bold steps to get there.\"")
    displayText("Over the next year, your team pours their hearts and souls into developing the full-dive metaverse headset. The technical challenges are daunting, but slowly, they begin to overcome them. The prototypes become more refined, the immersion more complete.")
    displayText("When you finally unveil the headset to the public, the response is nothing short of phenomenal. Eager users line up for a chance to experience the unprecedented level of realism and engagement. The metaverse seems to offer a tantalizing escape from the mundane.")
    displayText("But within weeks, something goes horribly wrong. Reports start to trickle in of users becoming trapped in the virtual world, unable to log out. Worse yet, they discover that if their in-game avatar dies, the user suffers a fatal neurological event in the real world.")
    displayText("Panic spreads like wildfire as families and loved ones watch helplessly as users slip into comas, their brains irreparably damaged by the headset's neural interface. The media dubs it the \"metaverse massacre,\" and public outrage reaches a fever pitch.")
    displayText("You're summoned before a panel of experts, each one demanding answers. \"How could you have released this technology without proper safeguards? Dozens of people are dead because of your reckless pursuit of innovation!\"")
    displayText("Sweat beading on your brow, you struggle to defend your actions. \"We-we thought we had accounted for every eventuality. The level of immersion and control was supposed to be unprecedented. We never imagined the system could be so catastrophically compromised.\"")
    displayText("The panel members exchange troubled glances. \"That's simply not good enough. This technology has the power to end lives, and you've unleashed it without proper oversight. The damage may be irreparable.\"")
    goBackRestart(displayChapterOne)

def displayChapterTwo():
  displayText("CHAPTER 2: CREATIVITY")
  displayText("You answer, bracing yourself. \"This is Steve, project lead.\"")
  displayText("\"Steve, we've reviewed your decision to pursue a non-full-dive metaverse headset,\" the executive says, their tone stern. \"While we appreciate your concerns about user safety, the leadership team feels strongly that we need to deliver an experience that is as immersive and transformative as possible.\"")
  displayText("You furrow your brow, concern growing. \"But sir, the full-dive approach carries significant risks - psychological, societal, even physical. We've thoroughly assessed the tradeoffs, and believe the non-full-dive route is the responsible choice.\"")
  displayText("\"I understand your reservations,\" the executive interrupts, \"but our investors and the market are demanding a truly groundbreaking experience. You need to find a way to maintain high levels of immersion while mitigating the risks as much as possible.\"")
  displayText("You remember the definition of creativity, “The virtue of being able to think out or invent new, often unexpected, options or ideas. Creativity is an important professional virtue for designers.”")
  displayText("And the case study related to it…")
  displayText("The Delta Plan was initiated after a devastating flood in 1953, aiming to enhance flood protection in the Netherlands. As part of this plan, there was a proposal to close off the Eastern Scheldt, but it faced opposition from environmentalists and fishermen concerned about ecological and economic impacts. In 1972, students proposed an alternative: a storm surge barrier that could be closed during floods while allowing normal water flow otherwise, balancing safety and ecological concerns. Initially dismissed as technically infeasible, political pressure led to reconsideration and eventual construction of the barrier, despite its higher cost. Many view it as a creative compromise between safety and ecological values.")
  displayText("Reflecting on this case study, you realize that a similar creative approach may be the key to satisfying your executive team's demand for an immersive experience while still prioritizing user safety. How should you keep this both safe and immersive?")
  
  next = selectNext(["Go back to a full dive helmet", "Create immersion through haptic gloves and a omnidirectional treadmill", "Have a person follow the user around to create the sensory effects of the metaverse"])
  
  if next == 1:
    displayText("You find yourself drawn to the allure of the full-dive approach, despite the significant risks. The promise of unlocking the true, unbridled potential of this technology is simply too tempting to ignore.")
    displayText("\"You know, I've been thinking,\" you say, leaning back in your chair. \"The full-dive approach may be the best way to deliver the kind of transformative experience the executives are demanding.\"")
    displayText("Sarah's eyes widen with concern. \"But Steve, we spent weeks analyzing the dangers - the psychological impacts, the potential for addiction and even fatal consequences. Are you sure we can mitigate those risks?\"")
    displayText("You hold up a hand, your expression confident. \"I believe we can. With the right safeguards in place, we can create a full-dive system that is safe and secure. The level of immersion and human-computer integration would be unparalleled.\"")
    displayText("Over the next year, your team pours their hearts and souls into developing the full-dive metaverse headset. The technical challenges are daunting, but slowly, they begin to overcome them. The prototypes become more refined, the immersion more complete.")
    displayText("When you finally unveil the headset to the public, the response is nothing short of phenomenal. Eager users line up for a chance to experience the unprecedented level of realism and engagement. The metaverse seems to offer a tantalizing escape from the mundane.")
    displayText("But within weeks, something goes horribly wrong. Reports start to trickle in of users becoming trapped in the virtual world, unable to log out. Worse yet, they discover that if their in-game avatar dies, the user suffers a fatal neurological event in the real world.")
    displayText("Panic spreads like wildfire as families and loved ones watch helplessly as users slip into comas, their brains irreparably damaged by the headset's neural interface. The media dubs it the \"metaverse massacre,\" and public outrage reaches a fever pitch.")
    displayText("You're summoned before a panel of experts, each one demanding answers. \"How could you have released this technology without proper safeguards? Dozens of people are dead because of your reckless pursuit of innovation!\"")
    displayText("Sweat beading on your brow, you struggle to defend your actions. \"We-we thought we had accounted for every eventuality. The level of immersion and control was supposed to be unprecedented. We never imagined the system could be so catastrophically compromised.\"")
    displayText("The panel members exchange troubled glances. \"That's simply not good enough. This technology has the power to end lives, and you've unleashed it without proper oversight. The damage may be irreparable.\"")
    goBackRestart(displayChapterTwo)
  elif next == 2:
    displayText("\"Intrigued by the potential for a safe yet deeply immersive experience, you propose a two-pronged approach: haptic gloves and an omnidirectional treadmill. The gloves would provide users with a heightened sense of touch, allowing them to feel the textures of virtual objects and environments. The treadmill, meanwhile, would eliminate the need for cumbersome VR rigs and enable users to move freely within the metaverse.\"")
    displayText("Sarah's eyes light up. 'That's brilliant, Steve! Imagine feeling the cool grass beneath your feet as you explore a virtual forest, or the rough grip of a sword in your hand during a battle. It would be a whole new level of presence! This is exactly the creative, out-of-the-box thinking we need.'")
    displayText("You nod enthusiastically. 'Exactly! By combining these elements, we can create a truly immersive experience that surpasses traditional VR without the risks associated with full-dive technology. But of course, there will be challenges. Developing haptic gloves with such a nuanced range of touch feedback will be no easy feat. And integrating the treadmill seamlessly with the virtual world will require some innovative programming.'")
    displayText("A sense of determination washes over you. 'Challenges are what we engineers thrive on, right Sarah? This could be groundbreaking. Let's get started!'")
    displayChapterThree()
  else:
    displayText("You decide on a \"sensory assistant\" idea. \"I love it! This is exactly the creative, out-of-the-box thinking we need.\"")
    displayText("The team is skeptical, but you forge ahead, presenting the concept to the executives. \"This is the future of virtual reality - a seamless integration of physical and digital that will captivate users!\"")
    displayText("Sarah is hesitant, but agrees to let you pursue the sensory assistant approach. \"Well, Steve, if you really believe this is the way forward, then by all means, let's give it a shot.\"")
    displayText("The higher-ups fire you for being dumb")
    goBackRestart(displayChapterTwo)

def displayChapterThree():
  displayText("CHAPTER 3: SIMULATION STAGE")
  displayText("Months melt into years as you and your team tirelessly refine the haptic gloves and omnidirectional treadmill. Countless prototypes are built and tested, each iteration bringing you closer to realizing your vision. You pore over data from simulations, constantly evaluating performance and identifying areas for improvement.")
  displayText("You then remember the definition of the simulation stage…")
  displayText("“The stage of the design process in which the designer or the design team checks through calculations, tests, and simulations whether the concept designs meet the design requirements.”")
  displayText("And the case study related to it…")
  displayText("“On 4 June, 1996, an unmanned Ariane 5 rocket exploded just after its launch. The rocket and its load together had a value of 450 million Euros. An investigation showed that the software had instructed the rocket to self-destruct. The problem could be traced to the fact that the software had not been properly adapted and still was based on the Ariane 4 rocket. The Ariane 5 had a more powerful engine than the Ariane 4, so that the software had to cope with far larger numbers. The error occurred when the horizontal speed was measured and stored as a 64-bit real number and translated into a 16-bit real number. However, the value was higher than 32768, which is the highest number that can be described in 16 bits, so that instruments were fed the wrong values.”")
  displayText("You are now worried about whether the simulations your team made are correct. Should you double check?")
  
  next = selectNext(["Yes you should check, it never hurts to double check", "Nah, let's not check. It’s too much work"])
  
  if next == 1:
    displayText("The haptic gloves… everything seemed flawless. A triumphant grin threatened to split your face. Years of relentless work were about to culminate in a revolutionary launch.")
    displayText("Except for that nagging feeling. The readings were a little too… perfect.  A faint echo of Sarah's earlier concern about a \"minor pressure variance\" echoed in your mind.  The memory of the disastrous Ariane 5 launch flickered in the corner of your vision.")
    displayText("Taking a deep breath, you made a decision.  \"Sarah,\" you called out to your lead engineer, \"hold off on finalizing the haptic glove calibration.  Let's take another look at the simulations just to be sure.\"")
    displayText("Sarah, ever the voice of reason, shot you a grateful look. \"Smart move, Steve.  Better safe than sorry, especially with a launch this big.\"")
    displayText("The next few hours were a whirlwind of recalibration and stress tests.  Finally, with a sigh of relief that bordered on exhaustion, Sarah announced, \"There it is! We found a slight pressure inconsistency in the simulations versus reality that could lead to discomfort during extended use.\"")
    displayText("A tense silence hung in the air.  The launch – the culmination of years of blood, sweat, and code – was mere weeks away.  Disappointment threatened to bubble up, but you quickly tamped it down.  Missing the deadline was a small price to pay for user safety.")
    displayText("\"Alright team,\" you declared, a newfound determination in your voice. \"We push back the launch and address this pressure issue.  Consider it phase two of development – perfecting the TrueTouch experience before unleashing it on the world.\"")
    displayText("But your elation was short-lived.  The next morning, you were summoned to the office of the CEO.  Her smile was as polished as her mahogany desk.")
    displayChapterFour()
  else:
    displayText("You clench your fist, the decision solidifying in your gut.  Double-checking the haptic gloves simulations?  There's simply no time. Investors are chomping at the bit, the marketing blitz is in full swing, and the launch date looms like an immovable deadline.  The treadmill integration hiccups are concerning, but a software patch can fix those later. The haptic gloves, though?  The data looks flawless.  ")
    displayText("The launch is a glorious spectacle.  Critics rave about the immersive experience.  The haptic gloves, christened \"TrueTouch,\" create an unparalleled sense of virtual reality. Users can feel the soft fur of a virtual pet, the gritty texture of a digital battlefield. Sales figures explode.  You bask in the adulation, the culmination of years of relentless work finally paying off.")
    displayText("The celebration, however, proves fleeting.  An unsettling email from customer support shatters the euphoria.  Users are complaining of a strange tingling sensation in their hands after extended TrueTouch use. A flicker of unease sparks within you, but you tamp it down.  Probably user error, you reason.  Then come the more concerning reports.  Aching hands morph into searing pain.  The horrifying truth crashes down -  users are suffering crushed fingers and shattered metacarpals, all linked to the TrueTouch gloves.")
    displayText("The data you didn't double-check wasn't an anomaly; it was a crucial oversight in the pressure calibration.  The gloves, designed to enhance the virtual experience, were instead inflicting excruciating real-world injuries.  The once-celebrated TrueTouch becomes synonymous with pain.  Lawsuits pile up, your reputation crumbles.  The promising metaverse experience you envisioned becomes a cautionary tale of unchecked ambition.")
    displayText("The weight of your decision settles on your shoulders, a heavy mantle woven from arrogance and haste.  A single, seemingly insignificant detail you chose to ignore has snowballed into a full-blown catastrophe.  The future of the metaverse, once bright with possibility, now lies in ruins, a stark reminder of the devastating consequences of neglecting even the most basic checks and balances.")
    goBackRestart(displayChapterThree)

def displayChapterFour():
  displayText("CHAPTER 4: WHISTLEBLOWING")
  displayText("\"Steve,\" she began, all honeyed tones, \"we appreciate your… thoroughness. However, the investors are restless. Pushing back the launch is simply not an option.\"")
  displayText("Your stomach lurched. \"But Veronica, the pressure issue…\"")
  displayText("\"A minor detail,\" she interrupted, her smile hardening. \"We can tweak it post-launch with a software update. Besides, think of the positive press! We'll be the first movers in the market.\"")
  displayText("Her words hung heavy in the air.  This wasn't about innovation anymore.  It was about blind ambition and appeasing investors at any cost.  The potential consequences for user safety flashed before your eyes – crushed fingers, excruciating pain.  You couldn't be a party to this.")
  displayText("The CEO leaned forward, her voice a steely whisper. \"Steve, you're a valuable asset. Don't jeopardize that with… unnecessary delays.\"  The threat was clear.")
  displayText("You swallowed the lump in your throat.  She was right. You were just an employee, easily replaceable. But the potential harm to users…  A fierce determination ignited within you.  You wouldn't be a silent accomplice.")
  displayText("Veronica's smile returned, oblivious to the storm brewing within you. \"Excellent. Now, let's get this launch back on track, shall we?\"")
  displayText("You nodded tightly, your mind already racing. You remember the concept of whistleblowing which is…")
  displayText("“someone who reports waste, fraud, abuse, corruption, or dangers to public health and safety to someone who is in the position to rectify the wrongdoing. A whistleblower typically works inside of the organization where the wrongdoing is taking place; however, being an agency or company “insider” is not essential to serving as a whistleblower. What matters is that the individual discloses information about wrongdoing that otherwise would not be known. “ - whistleblowers.org/what-is-a-whistleblower")
  displayText("You also remember the case study regarding the 25th launching of the space shuttle…")
  displayText("“The 25th launching of the space shuttle was to be something special. It was the first time that a civilian, the teacher Christa McAuliffe, or as President Ronald Reagan put it: “one of America’s finest” would go into space. There was, therefore, more media attention than usual at cold Cape Canaveral (Florida, United States). When, on the morning of January 28, 1986, the mission controllers’ countdown began it was almost four degrees Celsius below freezing point (or about 25 degrees Fahrenheit). After 73 seconds the Challenger space shuttle exploded 11 kilometers above the Atlantic Ocean. All seven astronauts were killed. At the time it was the biggest disaster ever in the history of American space travel.”")
  displayText("“Morton Thiokol, a NASA supplier, was the company responsible for the construction of the rocket boosters designed to propel the Shuttle into space. In January 1985 Roger Boisjoly, an engineer at the Morton Thiokol company, had aired his doubts about the reliability of the O-rings. In July 1985 he had sent a confidential memo to the Morton Thiokol management board. In that memo he had expressed his concerns about the effectiveness of the O-rings at low temperatures: “I am really afraid that if we do not take immediate steps we will place both the flight and the launching pad in serious danger. The consequences would be catastrophic and human lives would be put at risk.” The memo instantly led to a project group being set up in order to investigate the problem. However, the project group received from the management insufficient material and funding to carry out its work properly.”")
  displayText("You can’t stop the launch, but you could expose the truth. Do you blow the whistle?")

  next = selectNext(["Yes, expose the problems with the gloves to the public", "No, just do what you are told"])

  if next == 1:
    displayText("The polished mahogany of the CEO's desk mocked you as you left the office. Their words echoed in your head - \"unnecessary delays,\" a \"minor detail.\"  The pressure to prioritize profit over people clawed at your conscience. You knew then, with a chilling certainty, that launching the TrueTouch gloves with the unresolved pressure issue was not just a mistake, it was a recipe for disaster.")
    displayText("Sleep evaded you that night. Visions of users writhing in pain from crushed fingers flickered through your mind.  You tossed and turned, the weight of responsibility pressing down on you. Finally, a sliver of determination pierced the darkness. You wouldn't be a silent accomplice. You had to expose the truth.")
    displayText("The next morning, you reached out to Sarah, your voice tight with nervous energy.  \"We need to talk,\" you said, outlining the CEO's pressure to launch despite the unresolved pressure issue. Sarah's face paled, mirroring the churning in your gut.")
    displayText("\"We have data, Steve,\" she said, her voice firm. \"Solid evidence of the potential risks. We can use that.\"")
    displayText("Together, you meticulously compiled a report, highlighting the pressure inconsistency, the potential for user injury, and the CEO's insistence on launching regardless.  It wasn't easy.  There were sleepless nights spent poring over data, the constant fear of discovery gnawing at you.")
    displayText("But you persevered, fueled by a moral obligation to protect users.  Finally, the report was complete, a damning indictment of the company's reckless ambition.  The question remained: who would you expose it to?")
    displayText("The traditional route - going through official company channels - seemed futile.  The CEO held too much sway.  You considered the press, but the potential for a media frenzy could jeopardize the entire project, even the future of the company.")
    displayText("Then, Sarah, ever the strategist, suggested a different approach.  There was a growing online community dedicated to responsible innovation in technology.  It was a long shot, but it felt like the least risky option, one that could potentially reach the right people.")
    displayText("With a pounding heart, you uploaded the report anonymously, detailing the pressure issue, the CEO's pressure, and your fear for user safety.  The response was swift and overwhelming.  The online community erupted, sharing the report and demanding accountability.")
    displayText("The pressure mounted on the company.  News outlets picked up the story, the public outcry grew louder.  Internally, an investigation was launched.  The CEO, forced to confront the evidence and the public backlash, was forced to step down.")
    displayText("The TrueTouch launch was delayed indefinitely, the pressure issue addressed.  The company, under new leadership, implemented stricter safety protocols and prioritized responsible innovation.")
    displayText("It wasn't an easy path.  You faced retaliation, threats, and a period of uncertainty.  But in the end, your decision to blow the whistle exposed the truth and prevented a potential disaster.  The experience left an indelible mark on you, a constant reminder of the courage it takes to stand up for what's right, even when it means going against the tide.")
    displayConclusion()
  else:
    displayText("You decide to leave the issue alone.")
    displayText("Launch day arrived with a fanfare of flashing lights and booming announcements. Critics marveled at the immersive experience, praising the lifelike touch sensations of the TrueTouch gloves. Sales figures skyrocketed. You basked in the initial euphoria, the weight of the CEO's expectations temporarily lifted.")
    displayText("But the celebration was short-lived.  Disturbing reports began to trickle in. Users complained of a strange tingling sensation in their hands, a dull ache that intensified with use.  Then came the horrifying truth –  users were suffering crushed fingers and shattered metacarpals, all linked to the TrueTouch gloves.")
    displayText("The \"minor pressure variance\" Sarah had flagged, the one you dismissed as insignificant, had turned into a horrifying reality. The data, so perfect on the surface, masked a deeper flaw in the calibration. The gloves, designed to enhance the virtual experience, were instead inflicting excruciating real-world injuries.")
    displayText("The weight of your decision slammed into you with the force of a collapsing building.  You'd prioritized deadlines and profits over safety, pressured by a CEO who valued ambition over responsibility.  The once-celebrated TrueTouch became synonymous with pain. Lawsuits piled up, the company's reputation lay in tatters.")
    displayText("The future of the metaverse, once brimming with potential, now lay in ruins, a stark reminder of the devastating consequences of blind ambition and the silencing of cautionary voices. You, the architect of this technological marvel, were now haunted by the echo of crushed bones and the ghost of Sarah's worried expression.  The taste of success turned to ash in your mouth, a bitter reminder of the heavy price paid for ignoring even the most minor of details.")
    goBackRestart(displayChapterFour)

def displayConclusion():
  displayText("CHAPTER 5: CONCLUSION")
  displayText("The cheers of the launch party echoed around you, a bittersweet symphony. The Metaverse Experience – haptic gloves, omnidirectional treadmill, and a next-gen VR headset – was finally a reality. It wasn't the full-dive tech everyone craved, but your whistle-blowing on safety risks had forced a change.")
  displayText("The initial controversy stung, but it led to a better product. Risk assessments exposed flaws, countless simulations were reworked. The team's creativity soared. They translated the full-dive experience – wind on skin, uneven terrain – through gloves and the treadmill's subtle movements. Haptic feedback became mind-blowing, the treadmill a seamless extension of the virtual world.")
  displayText("Safety concerns weren't a roadblock, they were a detour to a more immersive experience. Gone was the focus on dazzling visuals that caused nausea. The new simulations prioritized a believable world, tweaking details for presence without overwhelming senses.")
  displayText("The metaverse experience wasn't just groundbreaking technology, it was responsible innovation. It proved taking a cautious step back can lead to a giant leap forward. Watching users lose themselves in the virtual world, you knew this was just the beginning. The future of VR stretched vast, waiting to be explored with a newfound respect for safety and a relentless spirit of innovation.")
  displayText("Take my survey: https://forms.gle/RD6x7HeSVXjBSJ9v7")
if __name__ == "__main__":
  displayIntroduction()
  