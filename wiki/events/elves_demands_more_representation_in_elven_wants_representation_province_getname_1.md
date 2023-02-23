This page has the same name as others. For full listing see bottom of [the base page](elves_demands_more_representation_in_elven_wants_representation_province_getname.md).

#Information
 - Title: Elves Demands More Representation in [elven_wants_representation_province.GetName]
 - ID: elven_tolerance_events.1
#Description
Elves Demands More Representation in [elven_wants_representation_province.GetName]
#Mean Time to Happen:
Base time = 1 days

#Options

___
##Of course!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance elven is yes
 - Multiplied by 0.1 if has wants to decrease tolerance elven is yes


###Efects:<ul><li>add adm power = -40</li><li>small increase of elven tolerance effect = yes</li><li>event target:elven wants representation province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven represenatives prov; and does not have province modifier is elven not given represenatives prov; and does not have local autonomy is 50; and  has elven minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = elven_represenatives_prov</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##Make some concessions

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add adm power = -20</li><li>event target:elven wants representation province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven represenatives prov; and does not have province modifier is elven not given represenatives prov; and does not have local autonomy is 50; and  has elven minority trigger is yes:</li><ul><li>add local autonomy = 2.5</li></ul></ul></ul>

___
##No. Haven't we given them enough?!

###AI weighting:
AI weights this option at 50
 - Multiplied by 0.5 if has wants to maintain tolerance elven is yes
 - Multiplied by 0.1 if has wants to increase tolerance elven is yes


###Efects:<ul><li>small decrease of elven tolerance effect = yes</li><li>event target:elven wants representation province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven represenatives prov; and does not have province modifier is elven not given represenatives prov; and does not have local autonomy is 50; and  has elven minority trigger is yes:</li><ul><li>add province modifier:</li><ul><li>name = elven_not_given_represenatives_prov</li><li>duration = 1825</li></ul></ul></ul></ul>

___
##What an interesting idea

###Available if:
<li>ruler has personality is free_thinker_personality</li>

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.5 if has wants to maintain tolerance elven is yes
 - Multiplied by 0.1 if has wants to decrease tolerance elven is yes


###Efects:<ul><li>highlight = yes</li><li>add adm power = -20</li><li>medium increase of elven tolerance effect = yes</li><li>event target:elven wants representation province:</li><ul><li>If area has owned by is ROOT, and does not have province modifier is elven represenatives prov; and does not have province modifier is elven not given represenatives prov; and does not have local autonomy is 50; and  has elven minority trigger is yes:</li><ul><li>add local autonomy = 5</li><li>add province modifier:</li><ul><li>name = elven_represenatives_prov</li><li>duration = 3650</li></ul></ul></ul></ul>
