#Information
 - Title: False Rumours Out of [1140.GetName]
 - ID: ynn_events.206
#Description
False Rumours Out of [1140.GetName]
#Options

___
##My informants in [1140.GetName] already made sure their lies would backfire.

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is secretive_personality</li><li>ruler has personality  is intricate_web_weaver_personality</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add prestige = 5</li><li>If has exists is G85, and does not have tag is G85:</li><ul><li>custom tooltip = ynn_206_a_tt</li><li>hidden effect:</li><ul><li>If every known country has capital scope has superregion is ynn superregion:</li><ul><li>add trust:</li><ul><li>who = G85</li><li>value = -5</li></ul></ul></ul></ul></ul>

___
##How DARE they?!?

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality is cruel_personality</li><li>ruler has personality  is malevolent_personality</li><li>ruler has personality   is bold_fighter_personality</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>highlight = yes</li><li>custom tooltip = ynn_206_b_tt</li><li>hidden effect:</li><ul><li>If every known country has capital scope has superregion is ynn superregion:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = -10</li></ul></ul></ul><li>If has 1140 has owned by is ROOT:</li><ul><li>1140:</li><ul><li>add devastation = 10</li><li>add base tax = -1</li><li>add base production = -1</li><li>set province flag [1140_destroyed_rumour_mill](../flags/1140_destroyed_rumour_mill.md)</li></ul></ul><li>else:</li><ul><li>add casus belli:</li><ul><li>type = cb_insult</li><li>target = event_target:thromshana_owner</li><li>months = 12</li></ul><li>add opinion:</li><ul><li>who = event_target:thromshana_owner</li><li>modifier = insulted</li></ul><li>add trust:</li><ul><li>who = event_target:thromshana_owner</li><li>value = -15</li><li>mutual = yes</li></ul></ul></ul>

___
##The chatter of merchants is of no concern to people of honour.

###Available if:
<li>None of the following:</li><ul><li>ruler has personality is secretive_personality</li><li>ruler has personality  is intricate_web_weaver_personality</li><li>ruler has personality   is cruel_personality</li><li>ruler has personality    is malevolent_personality</li><li>ruler has personality     is bold_fighter_personality</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add legitimacy = -5</li><li>add prestige = 5</li><li>custom tooltip = ynn_206_c_tt</li><li>hidden effect:</li><ul><li>If every known country has capital scope has superregion is ynn superregion; and does not have tag is G85:</li><ul><li>random:</li><ul><li>chance = 50</li><li>add trust:</li><ul><li>who = ROOT</li><li>value = -5</li></ul></ul></ul></ul><li>If has exists is G85, and does not have tag is G85:</li><ul><li>add trust:</li><ul><li>who = G85</li><li>value = -10</li></ul></ul></ul>

___
##Fund our spy networks to better fight such tales.

###Available if:
<li>None of the following:</li><ul><li>ruler has personality is secretive_personality</li><li>ruler has personality  is intricate_web_weaver_personality</li><li>ruler has personality   is cruel_personality</li><li>ruler has personality    is malevolent_personality</li><li>ruler has personality     is bold_fighter_personality</li></ul>

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add treasury = -50</li><li>add legitimacy = -5</li><li>country gets the modifier ynn_hunting_down_rumours for 5 years</li><li>If has exists is G85, and does not have tag is G85:</li><ul><li>add trust:</li><ul><li>who = G85</li><li>value = -10</li></ul></ul></ul>

___
##These rumours… have a point.

###Available if:
<li>None of the following:</li><ul><li>ruler has personality is secretive_personality</li><li>ruler has personality  is intricate_web_weaver_personality</li><li>ruler has personality   is cruel_personality</li><li>ruler has personality    is malevolent_personality</li><li>ruler has personality     is bold_fighter_personality</li></ul>

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add stability = -1</li><li>add corruption = -2</li><li>If has ruler has personality is righteous personality:</li><ul><li>remove ruler personality = righteous_personality</li></ul><li>If has ruler has personality is malevolent personality, and has ruler has personality is obsessive perfectionist personality, and has ruler has personality is loose lips personality, and has ruler has personality is craven personality, and has ruler has personality is naive personality, and has ruler has personality is cruel personality, and has ruler has personality is greedy personality, and has ruler has personality is sinner personality, and has ruler has personality is drunkard personality, and has ruler has personality is infertile personality, and has ruler has personality is embezzler personality, and has ruler has personality is babbling buffoon personality:</li><ul><li>If has ruler has personality is malevolent personality:</li><ul><li>remove ruler personality = malevolent_personality</li></ul><li>If has ruler has personality is obsessive perfectionist personality:</li><ul><li>remove ruler personality = obsessive_perfectionist_personality</li></ul><li>If has ruler has personality is loose lips personality:</li><ul><li>remove ruler personality = loose_lips_personality</li></ul><li>If has ruler has personality is craven personality:</li><ul><li>remove ruler personality = craven_personality</li></ul><li>If has ruler has personality is naive personality:</li><ul><li>remove ruler personality = naive_personality</li></ul><li>If has ruler has personality is cruel personality:</li><ul><li>remove ruler personality = cruel_personality</li></ul><li>If has ruler has personality is greedy personality:</li><ul><li>remove ruler personality = greedy_personality</li></ul><li>If has ruler has personality is sinner personality:</li><ul><li>remove ruler personality = sinner_personality</li></ul><li>If has ruler has personality is drunkard personality:</li><ul><li>remove ruler personality = drunkard_personality</li></ul><li>If has ruler has personality is infertile personality:</li><ul><li>remove ruler personality = infertile_personality</li></ul><li>If has ruler has personality is embezzler personality:</li><ul><li>remove ruler personality = embezzler_personality</li></ul><li>If has ruler has personality is babbling buffoon personality:</li><ul><li>remove ruler personality = babbling_buffoon_personality</li></ul></ul><li>else:</li><ul><li>change dip = 1</li></ul><li>custom tooltip = ynn_206_e_tt</li><li>hidden effect:</li><ul><li>If every known country has capital scope has superregion is ynn superregion; and does not have tag is G85:</li><ul><li>add trust:</li><ul><li>who = ROOT</li><li>value = -5</li></ul></ul></ul></ul>
