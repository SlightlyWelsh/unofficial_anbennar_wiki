#Information
 - Title: What Remains of Venáil
 - ID: venail.23
#Description
What Remains of Venáil
#Mean Time to Happen:
Base time = 1 days

#Options

___
##The Sorncósti once lived there, they will do so again.

###Efects:<ul><li>owner:</li><ul><li>add dip power = -100</li></ul><li>custom tooltip = venail_sorncosti_tt</li><li>If venail area has owned by is event target:venail owner:</li><ul><li>set province flag [venail_sorncosti](../flags/venail_sorncosti.md)</li><li>set province flag [venail_resettle](../flags/venail_resettle.md)</li><li>add permanent province modifier:</li><ul><li>name = resettle_venail</li><li>duration = 3650</li></ul><li>hidden effect:</li><ul><li>93:</li><ul><li>fire province event [venail.24](venail.24_slug) in 1095 days</li></ul><li>93:</li><ul><li>fire province event [venail.25](venail.25_slug) in 2190 days</li></ul><li>93:</li><ul><li>fire province event [venail.26](venail.26_slug) in 3650 days</li></ul></ul></ul></ul>

___
##The Low Lorentish will serve the island well.

###Efects:<ul><li>owner:</li><ul><li>add dip power = -100</li></ul><li>custom tooltip = venail_low_lorentish_tt</li><li>If venail area has owned by is event target:venail owner:</li><ul><li>set province flag [venail_low_lorentish](../flags/venail_low_lorentish.md)</li><li>set province flag [venail_resettle](../flags/venail_resettle.md)</li><li>add permanent province modifier:</li><ul><li>name = resettle_venail</li><li>duration = 3650</li></ul><li>hidden effect:</li><ul><li>93:</li><ul><li>fire province event [venail.24](venail.24_slug) in 1095 days</li></ul><li>93:</li><ul><li>fire province event [venail.25](venail.25_slug) in 2190 days</li></ul><li>93:</li><ul><li>fire province event [venail.26](venail.26_slug) in 3650 days</li></ul></ul></ul></ul>

___
##We should send our own people.

###Available if:
<li>event target:venail owner:</li><ul><li>None of the following:</li><ul><li>Any of the following:</li><ul><li>primary culture is sorncosti</li><li>primary culture  is low_lorentish</li></ul></ul></ul>

###Efects:<ul><li>owner:</li><ul><li>add dip power = -150</li></ul><li>custom tooltip = venail_primary_culture_tt</li><li>set province flag [venail_resettle](../flags/venail_resettle.md)</li><li>set province flag [venail_resettle](../flags/venail_resettle.md)</li><li>If venail area has owned by is event target:venail owner:</li><ul><li>set province flag [venail_primary_culture](../flags/venail_primary_culture.md)</li><li>add permanent province modifier:</li><ul><li>name = resettle_venail</li><li>duration = 3650</li></ul><li>hidden effect:</li><ul><li>93:</li><ul><li>fire province event [venail.24](venail.24_slug) in 1095 days</li></ul><li>93:</li><ul><li>fire province event [venail.25](venail.25_slug) in 2190 days</li></ul><li>93:</li><ul><li>fire province event [venail.26](venail.26_slug) in 3650 days</li></ul></ul></ul></ul>

___
##We should not interfere.

###Efects:<ul><li>owner:</li><ul><li>add dip power = 50</li></ul><li>add permanent province modifier:</li><ul><li>name = resettle_venail</li><li>duration = 5475</li></ul><li>If venail area has owned by is event target:venail owner, and  has province modifier is resettle venail:</li><ul><li>add local autonomy = 25</li></ul></ul>
