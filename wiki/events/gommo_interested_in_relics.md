#Information
 - Title: Gommo Interested in Relics
 - ID: flavor_ameion.120
#Description
Gommo Interested in Relics
#Mean Time to Happen:
Base time = 180 months
 - Multiplied by 2 if has any owned province has province modifier is G52 excavated, and any owned province has gnomish minority trigger is yes
 - Multiplied by 2 if has any owned province has province modifier is G52 excavated, and any owned province has large gnomish minority trigger is yes

#Options

___
##They pose interesting questions.

###Efects:<ul><li>medium increase of gnomish tolerance effect = yes</li><li>If random owned province has province modifier is G52 excavated, and does not have large gnomish minority trigger is yes:</li><ul><li>add gnomish minority size effect = yes</li></ul><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = -15</li></ul><li>If has estate is estate artificers:</li><ul><li>If has estate privilege is estate artificers organization international gommo:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = 15</li></ul></ul><li>else:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = -20</li></ul></ul></ul></ul>

___
##Our artifacts are not their trinkets.

###Efects:<ul><li>medium decrease of gnomish tolerance effect = yes</li><li>increase legitimacy small effect = yes</li><li>If has estate privilege is estate artificers organization international gommo:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = -20</li></ul></ul></ul>

___
##They will never be welcome here.

###Efects:<ul><li>large decrease of gnomish tolerance effect = yes</li><li>increase legitimacy medium effect = yes</li><li>add estate loyalty:</li><ul><li>estate = estate_mages</li><li>loyalty = 15</li></ul><li>If has estate privilege is estate artificers organization international gommo:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_artificers</li><li>loyalty = -40</li></ul></ul><li>custom tooltip = ameion_no_gnomes</li><li>set country flag [ameion_no_gnome](../flags/ameion_no_gnome.md)</li></ul>
