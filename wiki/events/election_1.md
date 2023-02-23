This page has the same name as others. For full listing see bottom of [the base page](election.md).

#Information
 - Title: Election!
 - ID: 701
#Description
Election!
#Options

___
##Our immortal ruler is shortly revived and takes their rightful place as [Root.Monarch.GetTitle]!

###Available if:
<li>ruler can revive is yes</li>

###AI weighting:
AI weights this option at 1000


###Efects:<ul><li>custom tooltip = remains_ruler</li><li>add scaled republican tradition = -20</li><li>add karma = -5</li><li>revival stat loss = yes</li></ul>

___
##Bureaucrat Candidate

###AI weighting:
AI weights this option at 40


###Efects:<ul><li>If has country modifier is harpy administration:</li><ul><li>define ruler:</li><ul><li>mil = 1</li><li>adm = 4</li><li>dip = 1</li><li>female = yes</li></ul></ul><li>Else if has culture group is dwarven:</li><ul><li>dwarovar republic generic election effect:</li><ul><li>mil = 1</li><li>adm = 4</li><li>dip = 1</li></ul></ul><li>Else if has republic with female rulers trigger is yes:</li><ul><li>define ruler:</li><ul><li>mil = 1</li><li>adm = 4</li><li>dip = 1</li><li>random gender = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>mil = 1</li><li>adm = 4</li><li>dip = 1</li></ul></ul><li>If has government attribute is elections increase factions influence:</li><ul><li>add influence to adm faction:</li><ul><li>influence = 20</li></ul></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class adm:</li><ul><li>loyalty = 10</li></ul></ul></ul>

___
##Diplomat Candidate

###AI weighting:
AI weights this option at 30


###Efects:<ul><li>If has country modifier is harpy administration:</li><ul><li>define ruler:</li><ul><li>dip = 4</li><li>adm = 1</li><li>mil = 1</li><li>female = yes</li></ul></ul><li>Else if has culture group is dwarven:</li><ul><li>dwarovar republic generic election effect:</li><ul><li>dip = 4</li><li>adm = 1</li><li>mil = 1</li></ul></ul><li>Else if has republic with female rulers trigger is yes:</li><ul><li>define ruler:</li><ul><li>dip = 4</li><li>adm = 1</li><li>mil = 1</li><li>random gender = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>dip = 4</li><li>adm = 1</li><li>mil = 1</li></ul></ul><li>If has government attribute is elections increase factions influence:</li><ul><li>add influence to dip faction:</li><ul><li>influence = 20</li></ul></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class dip:</li><ul><li>loyalty = 10</li></ul></ul></ul>

___
##Military Candidate

###AI weighting:
AI weights this option at 30


###Efects:<ul><li>If has country modifier is harpy administration:</li><ul><li>define ruler:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li><li>female = yes</li></ul></ul><li>Else if has culture group is dwarven:</li><ul><li>dwarovar republic generic election effect:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li></ul></ul><li>Else if has republic with female rulers trigger is yes:</li><ul><li>define ruler:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li><li>random gender = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li></ul></ul><li>If has government attribute is elections increase factions influence:</li><ul><li>add influence to mil faction:</li><ul><li>influence = 20</li></ul></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class mil:</li><ul><li>loyalty = 10</li></ul></ul></ul>

___
##The beloved relative of [Root.Monarch.GetName].

###Available if:
<li>has government attribute enables_nepotism</li>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If has country flag is [strengthened_signoria_flag](../flags/strengthened_signoria_flag.md):</li><ul><li>custom tooltip = strengthened_signoria_election_tt</li><li>clr country flag [strengthened_signoria_flag](../flags/strengthened_signoria_flag.md)</li></ul><li>else:</li><ul><li>add scaled republican tradition = -4</li></ul><li>If has country modifier is harpy administration, and does not have reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>female = yes</li></ul></ul><li>Else if has republic with female rulers trigger is yes, and does not have reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>random gender = yes</li></ul></ul><li>Else if has country modifier is harpy administration, and  has reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>female = yes</li></ul></ul><li>Else if has republic with female rulers trigger is yes, and  has reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>random gender = yes</li></ul></ul><li>Else if has reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>random gender = yes</li></ul></ul><li>Else if has culture group is dwarven:</li><ul><li>If has reform is dwarovar new minds:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 50</li><li>max age = 70</li></ul><li>If has government attribute is dwarovar new minds effect:</li><ul><li>random list:</li><ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_church</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 5</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_nobles</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 5</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_burghers</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 5</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_mages</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = 5</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_artificers</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = 5</li></ul></ul></ul></ul><li>Else if has reform is dwarovar elder wisdom:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 70</li><li>max age = 90</li><li>name = "lastname"</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 60</li><li>max age = 80</li><li>name = "lastname"</li></ul></ul></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li></ul></ul><li>If has faction is mr aristocrats:</li><ul><li>add faction influence:</li><ul><li>faction = mr_aristocrats</li><li>influence = 10</li></ul></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty:</li><ul><li>estate = all</li><li>loyalty = 10</li></ul></ul></ul>
