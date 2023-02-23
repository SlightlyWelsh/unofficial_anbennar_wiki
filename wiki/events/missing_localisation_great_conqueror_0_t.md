#Information
 - Title: Missing localisation: great_conqueror_0_t
 - ID: great_conqueror.0
#Description

#Options

___
##Missing localisation: great_conqueror_0_a

###AI weighting:
AI weights this option at 95
 - Multiplied by 1.5 if has overextension percentage is 0.5
 - Multiplied by 1.5 if has average effective unrest is 1
 - Multiplied by 1.5 if has num of loans is 5
 - Multiplied by 1.5 if has corruption is 5
 - Multiplied by 1.5 if does not have stability is 0
 - Multiplied by 50 if has government is republic
 - Multiplied by 25 if has government is theocracy
 - Multiplied by 10 if is subject


___
##Missing localisation: great_conqueror_0_b

###Available if:
<li>None of the following:</li><ul><li>has country flag [previous_ruler_was_great_conqueror_flag](../flags/previous_ruler_was_great_conqueror_flag.md)</li></ul>

###AI weighting:
AI weights this option at 10
 - Multiplied by 0 if has if has has global flag is [mythical_conqueror](../flags/mythical_conqueror.md):if has REB has check variable has nbGC is 13; and has else has REB has check variable has nbGC is 10; and is bankrupt, and has AND has any neighbor country is not controlled by the AI; and does not have year is 1550; and has coalition target is ROOT, and does not have num of cities is 2; and has government is tribal
 - Multiplied by 1.5 if is a great power
 - Multiplied by 1.5 if has MIL is 3, and  has ADM is 3, and  has DIP is 3
 - Multiplied by 2 if has MIL is 4, and  has ADM is 4, and  has DIP is 4
 - Multiplied by 2.5 if has MIL is 5, and  has ADM is 5, and  has DIP is 5
 - Multiplied by 3 if has MIL is 6, and  has ADM is 6, and  has DIP is 6
 - Multiplied by 3 if does not have ruler age is 30
 - Multiplied by 1.5 if has ruler has mage personality is yes
 - Multiplied by 8 if does not have check variable has nbGC is 2
 - Multiplied by 4 if does not have check variable has nbGC is 4
 - Multiplied by 2 if does not have check variable has nbGC is 5
 - Multiplied by 2 if has capital scope has superregion is escann superregion; and  has total development is 500
 - Multiplied by 3 if has calc true if does not have part of hre; and does not have alliance with is ROOT; and does not have subject of is ROOT; and does not have army strength has who is ROOT, and army strength has value is 0.4; and calc true if has amount is 2
 - Multiplied by 4 if has calc true if does not have part of hre; and does not have alliance with is ROOT; and does not have subject of is ROOT; and does not have army strength has who is ROOT, and army strength has value is 0.4; and calc true if has amount is 3
 - Multiplied by 5 if has calc true if does not have part of hre; and does not have alliance with is ROOT; and does not have subject of is ROOT; and does not have army strength has who is ROOT, and army strength has value is 0.4; and calc true if has amount is 4
 - Multiplied by 10 if has calc true if does not have part of hre; and does not have alliance with is ROOT; and does not have subject of is ROOT; and does not have army strength has who is ROOT, and army strength has value is 0.4; and calc true if has amount is 5
 - Multiplied by 15 if has calc true if does not have part of hre; and does not have alliance with is ROOT; and does not have subject of is ROOT; and does not have army strength has who is ROOT, and army strength has value is 0.4; and calc true if has amount is 6
 - Multiplied by 2 if does not have tech difference is 1
 - Multiplied by 5 if is revolution target
 - Multiplied by 3 if has power projection is 50
 - Multiplied by 5 if has global flag is [mythical_conqueror](../flags/mythical_conqueror.md), and  is a great power


###Efects:<ul><li>If has global flag is [mythical_conqueror](../flags/mythical_conqueror.md), and is a great power, and has total development is 1000:</li><ul><li>add ruler personality = mythical_conqueror_personality</li><li>add ruler modifier:</li><ul><li>name = mythical_conqueror_modifier</li><li>duration = -1</li></ul><li>set ai personality:</li><ul><li>personality = ai_militarist</li><li>locked = yes</li></ul><li>add stability = 3</li><li>change dip = 3</li><li>change adm = 3</li><li>change mil = 3</li><li>set country flag [great_conqueror_flag](../flags/great_conqueror_flag.md)</li><li>REB:</li><ul><li>change variable:</li><ul><li>nbGC = 1</li></ul></ul><li>export to variable:</li><ul><li>which = ownDev</li><li>value = total_development</li><li>who = ROOT</li></ul><li>log = "MYTHICAL CONQUEROR ---------------- [Root.GetName] |[Root.ownDev.GetValue]| became a Mythical Conqueror in [GetYear] [GetMonth]. It's a [Root.GovernmentName] | Number of GC: [REB.nbGC.GetValue]"</li></ul><li>else:</li><ul><li>add ruler personality = great_conqueror_personality</li><li>add ruler modifier:</li><ul><li>name = great_conqueror_modifier</li><li>duration = -1</li></ul><li>set ai personality:</li><ul><li>personality = ai_militarist</li><li>locked = yes</li></ul><li>add stability = 1</li><li>change dip = 1</li><li>change adm = 1</li><li>change mil = 1</li><li>set country flag [great_conqueror_flag](../flags/great_conqueror_flag.md)</li><li>REB:</li><ul><li>change variable:</li><ul><li>nbGC = 1</li></ul></ul><li>export to variable:</li><ul><li>which = ownDev</li><li>value = development</li><li>who = ROOT</li></ul><li>log = "GREAT CONQUEROR ---------------- [Root.GetName] |[Root.ownDev.GetValue]| became a Great Conqueror in [GetYear] [GetMonth]. It's a [Root.GovernmentName] | Number of GC: [REB.nbGC.GetValue]"</li></ul></ul>
