#Information
 - Title: Missing localisation: flavor_castanor_0_t
 - ID: flavor_castanor.0
#Description

#Mean Time to Happen:
Base time = 18 months

#Options

___
##You shouldn't see this

###AI weighting:
AI weights this option at 100


###One of the following randomly happens:
Outcome 1:

Available if <li>any hired mercenary company:</li><ul><li>Any of the following:</li><ul><li>template is merc_castanorian_legion_1</li><li>template  is merc_castanorian_legion_2</li><li>template   is merc_castanorian_legion_3</li><li>template    is merc_castanorian_legion_4</li><li>template     is merc_castanorian_legion_5</li><li>template      is merc_castanorian_legion_6</li><li>template       is merc_castanorian_legion_7</li><li>template        is merc_castanorian_legion_8</li></ul><li>hired for months is at least 60</li></ul><li>None of the following:</li><ul><li>has country modifier castanor_tired_legions</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [The Grind of War](../events/the_grind_of_war.md) happens</li></ul>
Outcome 2:

Available if <li>any hired mercenary company:</li><ul><li>Any of the following:</li><ul><li>template is merc_castanorian_legion_1</li><li>template  is merc_castanorian_legion_2</li><li>template   is merc_castanorian_legion_3</li><li>template    is merc_castanorian_legion_4</li><li>template     is merc_castanorian_legion_5</li><li>template      is merc_castanorian_legion_6</li><li>template       is merc_castanorian_legion_7</li><li>template        is merc_castanorian_legion_8</li></ul></ul><li>None of the following:</li><ul><li>has country modifier castanor_influx_of_new_legionnaires</li></ul><li>NOT:</li><ul><li>has country modifier castanor_influx_of_recruits</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Recruits to [attractive_legion.GetName]](../events/recruits_to_attractive_legion_getname.md) happens</li></ul>
Outcome 3:

Available if <li>any hired mercenary company:</li><ul><li>Any of the following:</li><ul><li>template is merc_castanorian_legion_1</li><li>template  is merc_castanorian_legion_2</li><li>template   is merc_castanorian_legion_3</li><li>template    is merc_castanorian_legion_4</li><li>template     is merc_castanorian_legion_5</li><li>template      is merc_castanorian_legion_6</li><li>template       is merc_castanorian_legion_7</li><li>template        is merc_castanorian_legion_8</li></ul></ul><li>None of the following:</li><ul><li>has country modifier castanor_inspirational_legions</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Regular Units Inspired by Legions](../events/regular_units_inspired_by_legions.md) happens</li></ul>
Outcome 4:

Available if <li>any hired mercenary company:</li><ul><li>template is merc_castanorian_legion_1</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Dragonflame: The First, the Finest](../events/dragonflame_the_first_the_finest.md) happens</li></ul>
Outcome 5:

Available if <li>any hired mercenary company:</li><ul><li>template is merc_castanorian_legion_3</li><li>None of the following:</li><ul><li>location:</li><ul><li>has province flag [protected_by_shield_legion](../flags/protected_by_shield_legion.md)</li></ul></ul></ul>

The weight of this outcome is 1    
 - Multiplied by 5 if has any hired mercenary company has template is merc castanorian legion 3, and any hired mercenary company has location has region for scope province has type is all, and region for scope province has country or non sovereign subject holds is ROOT

This outcome causes the following effects:<ul><li>the event [Shield: The Dedicated Bulwark](../events/shield_the_dedicated_bulwark.md) happens</li></ul>
Outcome 6:

Available if <li>any hired mercenary company:</li><ul><li>template is merc_castanorian_legion_2</li><li>location:</li><ul><li>unit is in battle</li></ul></ul>

The weight of this outcome is 1     
 - Multiplied by 10 if has any hired mercenary company has template is merc castanorian legion 2, and any hired mercenary company has location has unit is in battle

This outcome causes the following effects:<ul><li>the event [Sword: To Pierce the Heart](../events/sword_to_pierce_the_heart.md) happens</li></ul>
Outcome 7:

Available if <li>any hired mercenary company:</li><ul><li>template is merc_castanorian_legion_4</li><li>location:</li><ul><li>Any of the following:</li><ul><li>has winter mild_winter</li><li>has winter  normal_winter</li><li>has winter   severe_winter</li></ul></ul></ul><li>None of the following:</li><ul><li>has country modifier castanor_forged_in_winter</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Giantsbane: Forged in Winter](../events/giantsbane_forged_in_winter.md) happens</li></ul>
Outcome 8:

Available if <li>any hired mercenary company:</li><ul><li>template is merc_castanorian_legion_7</li></ul><li>None of the following:</li><ul><li>has country flag [magebound_war_wizard_get](../flags/magebound_war_wizard_get.md)</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Magebound: Gods of the Battlefield](../events/magebound_gods_of_the_battlefield.md) happens</li></ul>
Outcome 9:

Available if <li>None of the following:</li><ul><li>has country flag [thundersworn_has_raided](../flags/thundersworn_has_raided.md)</li></ul><li>any hired mercenary company:</li><ul><li>template is merc_castanorian_legion_6</li><li>location:</li><ul><li>owner:</li><ul><li>war with is this nation</li></ul><li>None of the following:</li><ul><li>has province modifier castanor_thundersworn_behind_enemy_lines_mod</li></ul></ul></ul>

The weight of this outcome is 1        
 - Multiplied by 5 if does not have country flag is [thundersworn_has_raided](../flags/thundersworn_has_raided.md); and  has any hired mercenary company has template is merc castanorian legion 6, and any hired mercenary company has location has owner has war with is ROOT; and does not have province modifier is castanor thundersworn behind enemy lines mod

This outcome causes the following effects:<ul><li>the event [Thundersworn: Lightning Raids](../events/thundersworn_lightning_raids.md) happens</li></ul>
Outcome 10:

Available if <li>any hired mercenary company:</li><ul><li>template is merc_castanorian_legion_5</li><li>location:</li><ul><li>unit is in siege</li><li>None of the following:</li><ul><li>has province modifier castanor_bridgeburners_siege_mod</li></ul></ul></ul>

The weight of this outcome is 1         
 - Multiplied by 10 if has any hired mercenary company has template is merc castanorian legion 5, and any hired mercenary company has location has unit is in siege, and does not have province modifier is castanor bridgeburners siege mod

This outcome causes the following effects:<ul><li>the event [Bridgeburners: Breach!](../events/bridgeburners_breach.md) happens</li></ul>
Outcome 11:

Available if <li>any hired mercenary company:</li><ul><li>template is merc_castanorian_legion_8</li><li>location:</li><ul><li>unit is in battle</li><li>unit has leader</li></ul></ul>

The weight of this outcome is 1          
 - Multiplied by 10 if has any hired mercenary company has template is merc castanorian legion 8, and any hired mercenary company has location has unit is in battle, and location has unit has leader

This outcome causes the following effects:<ul><li>the event [Hordebreaker: Seek and Destroy](../events/hordebreaker_seek_and_destroy.md) happens</li></ul>
Outcome 12:

Available if <li>has country flag [castanor_third_great_cleansing_concluded](../flags/castanor_third_great_cleansing_concluded.md)</li>

The weight of this outcome is 1           
 - Multiplied by 0.8 if has had country flag is [castanor_third_great_cleansing_concluded](../flags/castanor_third_great_cleansing_concluded.md) for 7300 days

The weight of this outcome is 1           
 - Multiplied by 0.8 if has had country flag is [castanor_third_great_cleansing_concluded](../flags/castanor_third_great_cleansing_concluded.md) for 14600 days

The weight of this outcome is 1           
 - Multiplied by 0.5 if has had country flag is [castanor_third_great_cleansing_concluded](../flags/castanor_third_great_cleansing_concluded.md) for 21900 days

This outcome causes the following effects:<ul><li>the event [Third Great Cleansing: Feywild Incursions](../events/third_great_cleansing_feywild_incursions.md) happens</li></ul>
Outcome 13:

Available if <li>has country flag [castanor_third_great_cleansing_concluded](../flags/castanor_third_great_cleansing_concluded.md)</li>

The weight of this outcome is 1            
 - Multiplied by 1.2 if has had country flag is [castanor_third_great_cleansing_concluded](../flags/castanor_third_great_cleansing_concluded.md) for 7300 days

The weight of this outcome is 1            
 - Multiplied by 1.2 if has had country flag is [castanor_third_great_cleansing_concluded](../flags/castanor_third_great_cleansing_concluded.md) for 14600 days

The weight of this outcome is 1            
 - Multiplied by 1.1 if has had country flag is [castanor_third_great_cleansing_concluded](../flags/castanor_third_great_cleansing_concluded.md) for 21900 days

This outcome causes the following effects:<ul><li>the event [Third Great Cleansing: Repopulation of the Deepwoods](../events/third_great_cleansing_repopulation_of_the_deepwoods.md) happens</li></ul>
Outcome 14:

Available if <li>has country flag [castanor_modernizing_castonath_completed](../flags/castanor_modernizing_castonath_completed.md)</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Drawing Immigrants](../events/drawing_immigrants.md) happens</li></ul>
Outcome 15:

Available if <li>has country flag [patron_castellos_finished](../flags/patron_castellos_finished.md)</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Pilgrimages to the Memorial](../events/pilgrimages_to_the_memorial.md) happens</li></ul>
Outcome 16:

Available if <li>840:</li><ul><li>has province modifier castanor_north_citadel_aqueduct</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Revitalization of the Trialmount](../events/revitalization_of_the_trialmount.md) happens</li></ul>
Outcome 17:

Available if <li>834:</li><ul><li>has province modifier castanor_south_citadel_restored</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Court factions influence ruler](../events/court_factions_influence_ruler.md) happens</li></ul>
Outcome 18:

Available if <li>834:</li><ul><li>has province modifier castanor_south_citadel_restored</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Court factions influence ruler](../events/court_factions_influence_ruler.md) happens</li></ul>
Outcome 19:

Available if <li>has global flag [castanor_dragon_road_built](../flags/castanor_dragon_road_built.md)</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Dragon Road: Trade Profits](../events/dragon_road_trade_profits.md) happens</li></ul>
Outcome 20:

Available if <li>has global flag [castanor_dragon_road_built](../flags/castanor_dragon_road_built.md)</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>the event [Dragon Road: Upkeep](../events/dragon_road_upkeep.md) happens</li></ul>

___
##You shouldn't see this

###AI weighting:
AI weights this option at 100
 - Multiplied by 0.85 if has any hired mercenary company has template is merc castanorian legion 1
 - Multiplied by 0.85 if has any hired mercenary company has template is merc castanorian legion 2
 - Multiplied by 0.85 if has any hired mercenary company has template is merc castanorian legion 3
 - Multiplied by 0.85 if has any hired mercenary company has template is merc castanorian legion 4
 - Multiplied by 0.85 if has any hired mercenary company has template is merc castanorian legion 5
 - Multiplied by 0.85 if has any hired mercenary company has template is merc castanorian legion 6
 - Multiplied by 0.85 if has any hired mercenary company has template is merc castanorian legion 7
 - Multiplied by 0.85 if has any hired mercenary company has template is merc castanorian legion 8
 - Multiplied by 0.85 if has global flag is [castanor_dragon_road_built](../flags/castanor_dragon_road_built.md)
 - Multiplied by 0.85 if has 833 has province modifier is castanor castonath imperial gardens
 - Multiplied by 0.85 if has 840 has province modifier is castanor north citadel aqueduct
 - Multiplied by 0.85 if has 834 has province modifier is castanor south citadel restored
 - Multiplied by 0.85 if has country flag is [castanor_third_great_cleansing_concluded](../flags/castanor_third_great_cleansing_concluded.md)
 - Multiplied by 0.85 if has country flag is [castanor_modernizing_castonath_completed](../flags/castanor_modernizing_castonath_completed.md)
 - Multiplied by 0.85 if has country flag is [patron_castellos_finished](../flags/patron_castellos_finished.md)

