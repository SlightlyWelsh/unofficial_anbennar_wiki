#Information
 - Title: Summon a Spirit
 - ID: spirits.626
#Description
Summon a Spirit
#Options

___
##Close

###Efects:<ul><li>owner:</li><ul><li>clr country flag [temple_summoning_menu_open](../flags/temple_summoning_menu_open.md)</li></ul></ul>

___
##A drifting spirit, barely awake to the world, holding only a morsel of energy.

###Efects:<ul><li>custom tooltip = spirits_summon_minor_tooltip</li><li>owner:</li><ul><li>add church power = -5</li></ul><li>hidden effect:</li><ul><li>event target:summonTarget:</li><ul><li>set province flag [minor_spirit_bound](../flags/minor_spirit_bound.md)</li><li>fire province event [spirits.627](spirits.627_slug) in 30 days</li></ul></ul><li>owner:</li><ul><li>country gets the modifier lhp_summon_cooldown for 10 years</li></ul></ul>

___
##A potent being, cunning and aware, ripe with power.

###Efects:<ul><li>custom tooltip = spirits_summon_normal_tooltip</li><li>owner:</li><ul><li>add church power = -10</li></ul><li>hidden effect:</li><ul><li>owner:</li><ul><li>set country flag [spirits_summon_medium_random](../flags/spirits_summon_medium_random.md)</li></ul><li>fire province event [spirits.631](spirits.631_slug) immediately </li></ul><li>owner:</li><ul><li>country gets the modifier lhp_summon_cooldown for 10 years</li></ul></ul>

___
##A great spirit, gorged and furious.

###Efects:<ul><li>custom tooltip = spirits_summon_powerful_tooltip</li><li>owner:</li><ul><li>add church power = -15</li></ul><li>hidden effect:</li><ul><li>owner:</li><ul><li>set country flag [spirits_summon_powerful_random](../flags/spirits_summon_powerful_random.md)</li></ul><li>fire province event [spirits.631](spirits.631_slug) immediately </li></ul><li>owner:</li><ul><li>country gets the modifier lhp_summon_cooldown for 10 years</li></ul></ul>
