This page has the same name as others. For full listing see bottom of [the base page](country_adj_herd_npsui_ghavaanaj_herd_windowps_n_n_root_getghavaanajtrainingtotalbonus.md).

#Information
 - Title: $COUNTRY_ADJ$ Herd\n£ui_ghavaanaj_herd_window£\n\n[Root.GetGhavaanajTrainingTotalBonus]
 - ID: ghavaanaj.2001
#Description
$COUNTRY_ADJ$ Herd\n£ui_ghavaanaj_herd_window£\n\n[Root.GetGhavaanajTrainingTotalBonus]
#Options

___
##£event_button_close_orange£

###Efects:<ul><li>highlight = yes</li><li>clr country flag [ghavaanaj_herd_menu_open](../flags/ghavaanaj_herd_menu_open.md)</li></ul>

___
##Train Harder

###Available if:
<li>Any of the following:</li><ul><li>has country flag [ghavaanaj_herd_training_swift_flag](../flags/ghavaanaj_herd_training_swift_flag.md)</li><li>has country flag  ghavaanaj_herd_training_sturdy_flag</li><li>has country flag   ghavaanaj_herd_training_smart_flag</li><li>has country flag    ghavaanaj_herd_training_steadfast_flag</li></ul><li>None of the following:</li><ul><li>has country modifier ghavaanaj_herd_training_harder</li></ul>

###Efects:<ul><li>custom tooltip = ghavaanaj_herd_training_train_harder_tt</li><li>custom tooltip = ghavaanaj_herd_training_chance_factors_tt</li><li>hidden effect:</li><ul><li>country gets the modifier ghavaanaj_herd_training_harder until otherwise removed</li></ul></ul>

___
##Stop Training Harder

###Available if:
<li>Any of the following:</li><ul><li>has country flag [ghavaanaj_herd_training_swift_flag](../flags/ghavaanaj_herd_training_swift_flag.md)</li><li>has country flag  ghavaanaj_herd_training_sturdy_flag</li><li>has country flag   ghavaanaj_herd_training_smart_flag</li><li>has country flag    ghavaanaj_herd_training_steadfast_flag</li></ul><li>has country modifier ghavaanaj_herd_training_harder</li>

###Efects:<ul><li>custom tooltip = ghavaanaj_herd_remove_training_train_harder_tt</li><li>custom tooltip = ghavaanaj_herd_training_chance_factors_tt</li><li>hidden effect:</li><ul><li>remove country modifier = ghavaanaj_herd_training_harder</li></ul></ul>

___
##Set Training Focus to Swift

###Available if:
<li>None of the following:</li><ul><li>has country flag [ghavaanaj_herd_training_swift_flag](../flags/ghavaanaj_herd_training_swift_flag.md)</li><li>has country modifier ghavaanaj_herd_training_physical_03</li></ul>

###Efects:<ul><li>custom tooltip = ghavaanaj_herd_training_set_swift_tt</li><li>hidden effect:</li><ul><li>clr country flag [ghavaanaj_herd_training_sturdy_flag](../flags/ghavaanaj_herd_training_sturdy_flag.md)</li><li>clr country flag [ghavaanaj_herd_training_smart_flag](../flags/ghavaanaj_herd_training_smart_flag.md)</li><li>clr country flag [ghavaanaj_herd_training_steadfast_flag](../flags/ghavaanaj_herd_training_steadfast_flag.md)</li><li>set country flag [ghavaanaj_herd_training_swift_flag](../flags/ghavaanaj_herd_training_swift_flag.md)</li><li>set variable:</li><ul><li>which = ghavaanaj_herd_training_counter</li><li>value = 0</li></ul><li>ghavaanaj define training chance = yes</li></ul></ul>

___
##Set Training Focus to Sturdy

###Available if:
<li>None of the following:</li><ul><li>has country flag [ghavaanaj_herd_training_sturdy_flag](../flags/ghavaanaj_herd_training_sturdy_flag.md)</li><li>has country modifier ghavaanaj_herd_training_physical_13</li></ul>

###Efects:<ul><li>custom tooltip = ghavaanaj_herd_training_set_sturdy_tt</li><li>hidden effect:</li><ul><li>clr country flag [ghavaanaj_herd_training_swift_flag](../flags/ghavaanaj_herd_training_swift_flag.md)</li><li>clr country flag [ghavaanaj_herd_training_smart_flag](../flags/ghavaanaj_herd_training_smart_flag.md)</li><li>clr country flag [ghavaanaj_herd_training_steadfast_flag](../flags/ghavaanaj_herd_training_steadfast_flag.md)</li><li>set country flag [ghavaanaj_herd_training_sturdy_flag](../flags/ghavaanaj_herd_training_sturdy_flag.md)</li><li>set variable:</li><ul><li>which = ghavaanaj_herd_training_counter</li><li>value = 0</li></ul><li>ghavaanaj define training chance = yes</li></ul></ul>

___
##Set Training Focus to Smart

###Available if:
<li>None of the following:</li><ul><li>has country flag [ghavaanaj_herd_training_smart_flag](../flags/ghavaanaj_herd_training_smart_flag.md)</li><li>has country modifier ghavaanaj_herd_training_mental_03</li></ul>

###Efects:<ul><li>custom tooltip = ghavaanaj_herd_training_set_smart_tt</li><li>hidden effect:</li><ul><li>clr country flag [ghavaanaj_herd_training_swift_flag](../flags/ghavaanaj_herd_training_swift_flag.md)</li><li>clr country flag [ghavaanaj_herd_training_sturdy_flag](../flags/ghavaanaj_herd_training_sturdy_flag.md)</li><li>clr country flag [ghavaanaj_herd_training_steadfast_flag](../flags/ghavaanaj_herd_training_steadfast_flag.md)</li><li>set country flag [ghavaanaj_herd_training_smart_flag](../flags/ghavaanaj_herd_training_smart_flag.md)</li><li>set variable:</li><ul><li>which = ghavaanaj_herd_training_counter</li><li>value = 0</li></ul><li>ghavaanaj define training chance = yes</li></ul></ul>

___
##Set Training Focus to Steadfast

###Available if:
<li>None of the following:</li><ul><li>has country flag [ghavaanaj_herd_training_steadfast_flag](../flags/ghavaanaj_herd_training_steadfast_flag.md)</li><li>has country modifier ghavaanaj_herd_training_mental_13</li></ul>

###Efects:<ul><li>custom tooltip = ghavaanaj_herd_training_set_steadfast_tt</li><li>hidden effect:</li><ul><li>clr country flag [ghavaanaj_herd_training_swift_flag](../flags/ghavaanaj_herd_training_swift_flag.md)</li><li>clr country flag [ghavaanaj_herd_training_sturdy_flag](../flags/ghavaanaj_herd_training_sturdy_flag.md)</li><li>clr country flag [ghavaanaj_herd_training_smart_flag](../flags/ghavaanaj_herd_training_smart_flag.md)</li><li>set country flag [ghavaanaj_herd_training_steadfast_flag](../flags/ghavaanaj_herd_training_steadfast_flag.md)</li><li>set variable:</li><ul><li>which = ghavaanaj_herd_training_counter</li><li>value = 0</li></ul><li>ghavaanaj define training chance = yes</li></ul></ul>

___
##Sell off Swift Elephants

###Available if:
<li>Any of the following:</li><ul><li>has country modifier ghavaanaj_herd_training_physical_03</li><li>has country modifier  ghavaanaj_herd_training_physical_02</li></ul><li>ghavaanaj has herd size 2 is yes</li>

###Efects:<ul><li>custom tooltip = ghavaanaj_sell_off_herd_swift_tt</li><li>hidden effect:</li><ul><li>ghavaanaj decrease herd size = yes</li><li>If has country modifier is ghavaanaj herd training physical 03:</li><ul><li>ghavaanaj increase training physical = yes</li><li>ghavaanaj increase training physical = yes</li></ul><li>else:</li><ul><li>ghavaanaj increase training physical = yes</li></ul></ul><li>add years of income = 0.5</li></ul>

___
##Sell off Sturdy Elephants

###Available if:
<li>Any of the following:</li><ul><li>has country modifier ghavaanaj_herd_training_physical_13</li><li>has country modifier  ghavaanaj_herd_training_physical_12</li></ul><li>ghavaanaj has herd size 2 is yes</li>

###Efects:<ul><li>custom tooltip = ghavaanaj_sell_off_herd_sturdy_tt</li><li>hidden effect:</li><ul><li>ghavaanaj decrease herd size = yes</li><li>If has country modifier is ghavaanaj herd training physical 13:</li><ul><li>ghavaanaj decrease training physical = yes</li><li>ghavaanaj decrease training physical = yes</li></ul><li>else:</li><ul><li>ghavaanaj decrease training physical = yes</li></ul></ul><li>add years of income = 0.5</li></ul>

___
##Sell off Smart Elephants

###Available if:
<li>Any of the following:</li><ul><li>has country modifier ghavaanaj_herd_training_mental_03</li><li>has country modifier  ghavaanaj_herd_training_mental_02</li></ul><li>ghavaanaj has herd size 2 is yes</li>

###Efects:<ul><li>custom tooltip = ghavaanaj_sell_off_herd_smart_tt</li><li>hidden effect:</li><ul><li>ghavaanaj decrease herd size = yes</li><li>If has country modifier is ghavaanaj herd training mental 03:</li><ul><li>ghavaanaj increase training mental = yes</li><li>ghavaanaj increase training mental = yes</li></ul><li>else:</li><ul><li>ghavaanaj increase training mental = yes</li></ul></ul><li>add years of income = 0.5</li></ul>

___
##Sell off Steadfast Elephants

###Available if:
<li>Any of the following:</li><ul><li>has country modifier ghavaanaj_herd_training_mental_13</li><li>has country modifier  ghavaanaj_herd_training_mental_12</li></ul><li>ghavaanaj has herd size 2 is yes</li>

###Efects:<ul><li>custom tooltip = ghavaanaj_sell_off_herd_steadfast_tt</li><li>hidden effect:</li><ul><li>ghavaanaj decrease herd size = yes</li><li>If has country modifier is ghavaanaj herd training mental 13:</li><ul><li>ghavaanaj decrease training mental = yes</li><li>ghavaanaj decrease training mental = yes</li></ul><li>else:</li><ul><li>ghavaanaj decrease training mental = yes</li></ul></ul><li>add years of income = 0.5</li></ul>
