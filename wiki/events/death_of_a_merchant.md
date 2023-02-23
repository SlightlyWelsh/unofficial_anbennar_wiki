#Information
 - Title: Death of a Merchant
 - ID: 736
#Description
Death of a Merchant
#Mean Time to Happen:
Base time = 1 days

#Options

___
##The state needs the money.

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add years of income = 0.25</li></ul>

___
##Use them as he would have.

###AI weighting:
AI weights this option at 50


###Efects:<ul><li>add meritocracy effect = yes</li><li>trigger switch:</li><ul><li>on trigger = has_country_flag</li><li>theologian flag:</li><ul><li>generate advisor of type and semi random religion effect:</li><ul><li>advisor type = theologian</li><li>advisor type if not state = natural_scientist</li><li>scaled skill = yes</li><li>discount = yes</li></ul></ul><li>artist flag:</li><ul><li>generate advisor of type and semi random religion effect:</li><ul><li>advisor type = artist</li><li>advisor type if not state = artist</li><li>scaled skill = yes</li><li>discount = yes</li></ul></ul><li>philosopher flag:</li><ul><li>generate advisor of type and semi random religion effect:</li><ul><li>advisor type = philosopher</li><li>advisor type if not state = philosopher</li><li>scaled skill = yes</li><li>discount = yes</li></ul></ul></ul><li>add prestige = 15</li></ul>

___
##I know just who should receive our patronage.

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality ancestor:</li><ul><li>key is zealot</li></ul><li>ruler has personality ancestor:</li><ul><li>key is tolerant</li></ul></ul><li>hidden trigger:</li><ul><li>None of the following:</li><ul><li>has country flag [theologian_flag](../flags/theologian_flag.md)</li></ul><li>monthly income is at least 16</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add prestige = 15</li><li>add meritocracy effect = yes</li><li>generate advisor of type and semi random religion effect:</li><ul><li>advisor type = theologian</li><li>advisor type if not state = natural_scientist</li><li>scaled skill = yes</li><li>discount = yes</li></ul></ul>

___
##I know just who should receive our patronage.

###Available if:
<li>Any of the following:</li><ul><li>ruler has personality ancestor:</li><ul><li>key is free_thinker</li></ul><li>ruler has personality is well_advised_personality</li></ul><li>hidden trigger:</li><ul><li>None of the following:</li><ul><li>has country flag [philosopher_flag](../flags/philosopher_flag.md)</li></ul><li>monthly income is at least 16</li></ul>

###AI weighting:
AI weights this option at 100


###Efects:<ul><li>highlight = yes</li><li>add prestige = 15</li><li>add meritocracy effect = yes</li><li>generate advisor of type and semi random religion effect:</li><ul><li>advisor type = philosopher</li><li>advisor type if not state = philosopher</li><li>scaled skill = yes</li><li>discount = yes</li></ul></ul>
