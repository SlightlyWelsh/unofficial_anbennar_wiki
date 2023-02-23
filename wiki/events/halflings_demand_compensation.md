#Information
 - Title: Halflings Demand Compensation
 - ID: halfling_tolerance_events.2
#Description
Halflings Demand Compensation
#Options

___
##Greedy little...

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance halfling is yes
 - Multiplied by 0.1 if has wants to increase tolerance halfling is yes


###Efects:<ul><li>small decrease of halfling tolerance effect = yes</li><li>event target:halfling prov:</li><ul><li>If area has any halfling pop trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = halfling_was_not_given_compensation</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Comply with their demands

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to decrease tolerance halfling is yes


###Efects:<ul><li>add prestige = -10</li><li>add years of income = -0.5</li></ul>

___
##We'll show them!

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is cruel_personality</li><li>ruler has personality  is malevolent_personality</li><li>ruler has personality   is bold_fighter_personality</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if does not have army size percentage is 0.25; and has revolt percentage is 0.1
 - Multiplied by 0.5 if has wants to maintain tolerance halfling is yes
 - Multiplied by 0.1 if has wants to increase tolerance halfling is yes


###Efects:<ul><li>highlight = yes</li><li>add mil power = -50</li><li>small decrease of halfling tolerance effect = yes</li><li>If random owned province does not have province modifier is halfling was not given compensation; and  has halfling minority trigger is yes, and has trade goods is grain, and has trade goods is livestock:</li><ul><li>spawn rebels:</li><ul><li>type = anti_tax_rebels</li><li>size = 1</li></ul></ul><li>If every owned province does not have province modifier is halfling was not given compensation; and  has halfling minority trigger is yes, and has trade goods is grain, and has trade goods is livestock, and has trade goods is dyes, and has province trade power is 10:</li><ul><li>add unrest = 2</li><li>add province modifier:</li><ul><li>name = halfling_was_not_given_compensation</li><li>duration = 1095</li></ul></ul></ul>

___
##Let us find a compromise

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is fierce_negotiator_personality</li><li>ruler has personality  is charismatic_negotiator_personality</li><li>ruler has personality   is silver_tongue_personality</li></ul>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if has wants to decrease tolerance halfling is yes


###Efects:<ul><li>highlight = yes</li><li>add dip power = -25</li><li>add years of income = -0.25</li></ul>
