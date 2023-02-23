#Information
 - Title: Ruination
 - ID: black_demesne.11
#Description
Ruination
#Options

___
##Go Back

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>add mil power = 10</li></ul>

___
##Murder (Kills enemy regiments)

###Available if:
<li>event target:province:</li><ul><li>unit is in battle</li><li>has ruler leader from this nation</li></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>custom tooltip = jorg_damage_tooltip</li><li>hidden effect:</li><ul><li>event target:province:</li><ul><li>add devastation = 35</li></ul><li>If while has check variable has jorg damage is 1:</li><ul><li>subtract variable:</li><ul><li>jorg damage = 1</li></ul><li>If random country has war with is ROOT, and  has infantry in province is PREV, and has cavalry in province is PREV, and has artillery in province is PREV:</li><ul><li>event target:province:</li><ul><li>kill units:</li><ul><li>who = PREV</li><li>amount = 1</li></ul></ul></ul></ul></ul><li>country gets the modifier black_jorgurem_weakened for 1 years</li></ul>

___
##Devastation (Damages enemy fortress)

###Available if:
<li>event target:province:</li><ul><li>unit is in siege</li><li>has ruler leader from this nation</li></ul>

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>event target:province:</li><ul><li>change siege = 12</li><li>add devastation = 50</li><li>add permanent province modifier:</li><ul><li>name = black_ruined_fort</li><li>duration = 2555</li></ul></ul><li>country gets the modifier black_jorgurem_weakened for 120 days</li></ul>
