#Information
 - Title: Forced Abstinence For Shamans?
 - ID: bulgu_orazan.11
#Description
Forced Abstinence For Shamans?
#Mean Time to Happen:
Base time = 20 years
 - Multiplied by 0.1 if has church power is 200

#Options

___
##Enforce abstinence for shamans

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add church power = -100</li><li>set country flag [bulgu_abstinence](../flags/bulgu_abstinence.md)</li><li>country gets the modifier bulgu_abstinence_modifier until otherwise removed</li><li>If has estate is estate church:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -15</li></ul></ul><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = 10</li></ul></ul><li>If has estate is estate monstrous tribes:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_monstrous_tribes</li><li>loyalty = 5</li></ul></ul><li>If every country has country flag is [bulgu_no_abstinence](../flags/bulgu_no_abstinence.md):</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = bulgu_disagree_on_abstinence</li></ul><li>reverse add opinion:</li><ul><li>who = PREV</li><li>modifier = bulgu_disagree_on_abstinence</li></ul></ul><li>If every country has country flag is [bulgu_abstinence](../flags/bulgu_abstinence.md):</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = bulgu_agree_on_abstinence</li></ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = bulgu_agree_on_abstinence</li></ul></ul></ul>

___
##Reafirm their rights

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>add church power = -100</li><li>set country flag [bulgu_no_abstinence](../flags/bulgu_no_abstinence.md)</li><li>country gets the modifier bulgu_no_abstinence_modifier until otherwise removed</li><li>If has estate is estate church:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = 15</li></ul></ul><li>If has estate is estate nobles:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li></ul></ul><li>If has estate is estate monstrous tribes:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_monstrous_tribes</li><li>loyalty = -5</li></ul></ul><li>If every country has country flag is [bulgu_abstinence](../flags/bulgu_abstinence.md):</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = bulgu_disagree_on_abstinence</li></ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = bulgu_disagree_on_abstinence</li></ul></ul><li>If every country has country flag is [bulgu_no_abstinence](../flags/bulgu_no_abstinence.md):</li><ul><li>add opinion:</li><ul><li>who = ROOT</li><li>modifier = bulgu_agree_on_abstinence</li></ul><li>reverse add opinion:</li><ul><li>who = ROOT</li><li>modifier = bulgu_agree_on_abstinence</li></ul></ul></ul>

___
##We have more pressing matters to discuss

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>country gets the modifier bulgu_orazan_declined_reform for 20 years</li></ul>
