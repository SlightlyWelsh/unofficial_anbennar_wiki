#Information
 - Title: Election!
 - ID: 700
#Description
Election!
#Options

___
##Keep $MONARCH$

###Available if:
<li>does not have regency</li><li>None of the following:</li><ul><li>has ruler flag [leader_has_been_pushed_out](../flags/leader_has_been_pushed_out.md)</li></ul>

###AI weighting:
AI weights this option at 60
 - Multiplied by 0 if does not have republican tradition is 25
 - Multiplied by 0.5 if does not have republican tradition is 50
 - Multiplied by 0.5 if does not have republican tradition is 75
 - Multiplied by 2.0 if has republican tradition is 90
 - Multiplied by 2.0 if has ruler has mage personality is yes


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add adm power = 50</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add dip power = 50</li></ul>
Outcome 3:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add mil power = 50</li></ul>

###Efects:<ul><li>custom tooltip = remains_ruler</li><li>change adm = 1</li><li>change dip = 1</li><li>change mil = 1</li><li>If is not tribal, and  has government is republic, and does not have republican tradition is 20; and does not have revolutionary republic trigger is yes; and  has dlc is "Res Publica", and does not have government attribute is cannot become dictatorship; and does not have reform is northern league magnates:</li><ul><li>add government reform = presidential_despot_reform</li></ul><li>Else if has government is republic, and does not have republican tradition is 20; and  is revolutionary republic trigger is yes, and does not have reform is northern league magnates:</li><ul><li>change government to monarchy = yes</li><li>add government reform = revolutionary_empire_reform</li></ul><li>If is not tribal, and  has government is republic, and does not have republican tradition is 20; and does not have dlc is "Res Publica"; and does not have government attribute is cannot become dictatorship; and does not have reform is northern league magnates:</li><ul><li>change government to monarchy = yes</li></ul><li>If has country flag is [strengthened_signoria_flag](../flags/strengthened_signoria_flag.md):</li><ul><li>custom tooltip = strengthened_signoria_election_tt</li><li>clr country flag [strengthened_signoria_flag](../flags/strengthened_signoria_flag.md)</li></ul><li>Else if has country modifier is gnomish administration, and has country modifier is elven administration, and has country modifier is dwarven administration:</li><ul><li>add scaled republican tradition = -3</li></ul><li>else:</li><ul><li>If has country flag is [increased_election_cost](../flags/increased_election_cost.md):</li><ul><li>add scaled republican tradition = -15</li><li>clr country flag [increased_election_cost](../flags/increased_election_cost.md)</li></ul><li>else:</li><ul><li>add scaled republican tradition = -10</li></ul></ul><li>If has government attribute is reelection depowers estates:</li><ul><li>add estate influence modifier:</li><ul><li>estate = all</li><li>influence = -10</li><li>duration = 1460</li><li>desc = REELCTION_DEPOWER_ESTATES</li></ul></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty:</li><ul><li>estate = all</li><li>loyalty = 5</li></ul></ul><li>If has government attribute is reelection increases absolutism:</li><ul><li>tooltip:</li><ul><li>add absolutism = 10</li></ul><li>custom tooltip = ADD_ABSOLUTISM_BASED_ON_ELECTION_TERM</li><li>hidden effect:</li><ul><li>for variable amount:</li><ul><li>variable = election_term</li><li>effect = "</li><li>add absolutism = 10</li></ul></ul><li>hidden effect:</li><ul><li>change variable:</li><ul><li>which = election_term</li><li>value = 1</li></ul></ul></ul><li>If has government attribute is elections increase factions influence:</li><ul><li>add influence to random faction:</li><ul><li>influence = 20</li></ul></ul><li>add karma = -5</li></ul>

___
##Bureaucrat Candidate

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>If has country modifier is harpy administration:</li><ul><li>define ruler:</li><ul><li>mil = 1</li><li>adm = 4</li><li>dip = 1</li><li>female = yes</li></ul></ul><li>Else if has culture group is dwarven:</li><ul><li>dwarovar republic generic election effect:</li><ul><li>mil = 1</li><li>adm = 4</li><li>dip = 1</li></ul></ul><li>Else if has republic with female rulers trigger is yes:</li><ul><li>define ruler:</li><ul><li>mil = 1</li><li>adm = 4</li><li>dip = 1</li><li>random gender = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>mil = 1</li><li>adm = 4</li><li>dip = 1</li></ul></ul><li>If has government attribute is elections increase factions influence:</li><ul><li>add influence to adm faction:</li><ul><li>influence = 20</li></ul></ul><li>add karma = 10</li><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class adm:</li><ul><li>loyalty = 10</li></ul></ul></ul>

___
##Diplomat Candidate

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>If has country modifier is harpy administration:</li><ul><li>define ruler:</li><ul><li>dip = 4</li><li>adm = 1</li><li>mil = 1</li><li>female = yes</li></ul></ul><li>Else if has culture group is dwarven:</li><ul><li>dwarovar republic generic election effect:</li><ul><li>dip = 4</li><li>adm = 1</li><li>mil = 1</li></ul></ul><li>Else if has republic with female rulers trigger is yes:</li><ul><li>define ruler:</li><ul><li>dip = 4</li><li>adm = 1</li><li>mil = 1</li><li>random gender = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>dip = 4</li><li>adm = 1</li><li>mil = 1</li></ul></ul><li>If has government attribute is elections increase factions influence:</li><ul><li>add influence to dip faction:</li><ul><li>influence = 20</li></ul></ul><li>add karma = 10</li><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class dip:</li><ul><li>loyalty = 10</li></ul></ul></ul>

___
##Military Candidate

###AI weighting:
AI weights this option at 20


###Efects:<ul><li>If has country modifier is harpy administration:</li><ul><li>define ruler:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li><li>female = yes</li></ul></ul><li>Else if has culture group is dwarven:</li><ul><li>dwarovar republic generic election effect:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li></ul></ul><li>Else if has republic with female rulers trigger is yes:</li><ul><li>define ruler:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li><li>random gender = yes</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>mil = 4</li><li>adm = 1</li><li>dip = 1</li></ul></ul><li>If has government attribute is elections increase factions influence:</li><ul><li>add influence to mil faction:</li><ul><li>influence = 20</li></ul></ul><li>add karma = 10</li><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty by class mil:</li><ul><li>loyalty = 10</li></ul></ul></ul>

___
##The beloved relative of [Root.Monarch.GetName].

###Available if:
<li>has government attribute enables_nepotism</li>

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If has country flag is [strengthened_signoria_flag](../flags/strengthened_signoria_flag.md):</li><ul><li>custom tooltip = strengthened_signoria_election_tt</li><li>clr country flag [strengthened_signoria_flag](../flags/strengthened_signoria_flag.md)</li></ul><li>else:</li><ul><li>add scaled republican tradition = -4</li></ul><li>If has country modifier is harpy administration, and does not have reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>female = yes</li></ul></ul><li>Else if has republic with female rulers trigger is yes, and does not have reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>random gender = yes</li></ul></ul><li>Else if has country modifier is harpy administration, and does not have reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>female = yes</li></ul></ul><li>Else if has republic with female rulers trigger is yes, and  has reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li><li>random gender = yes</li></ul></ul><li>Else if has reform is signoria reform:</li><ul><li>define ruler:</li><ul><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li></ul></ul><li>Else if has culture group is dwarven:</li><ul><li>If has reform is dwarovar new minds:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 50</li><li>max age = 70</li></ul><li>If has government attribute is dwarovar new minds effect:</li><ul><li>random list:</li><ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_church</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 5</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_nobles</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 5</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_burghers</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = 5</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_mages</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = 5</li></ul></ul><li>20:</li><ul><li>trigger:</li><ul><li>has estate = estate_artificers</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = 5</li></ul></ul></ul></ul><li>Else if has reform is dwarovar elder wisdom:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 70</li><li>max age = 90</li><li>name = "lastname"</li></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 60</li><li>max age = 80</li><li>name = "lastname"</li></ul></ul></ul></ul><li>else:</li><ul><li>define ruler:</li><ul><li>change mil = -2</li><li>change adm = -2</li><li>change dip = -2</li><li>min age = 30</li><li>max age = 50</li><li>name = "lastname"</li></ul></ul><li>If has faction is mr aristocrats:</li><ul><li>add faction influence:</li><ul><li>faction = mr_aristocrats</li><li>influence = 10</li></ul></ul><li>If has government attribute is elections influence estates:</li><ul><li>add estate loyalty:</li><ul><li>estate = all</li><li>loyalty = 10</li></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [election_1](election_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [election_1](election_1.md)


#Pages with same name:
The following pages have the same name as this page:
 - [election_1](election_1.md)
