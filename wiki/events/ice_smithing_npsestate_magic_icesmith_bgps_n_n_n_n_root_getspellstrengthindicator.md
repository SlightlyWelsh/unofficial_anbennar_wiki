#Information
 - Title:     Ice Smithing\n£estate_magic_icesmith_bg£\n\n\n\n[Root.GetSpellStrengthIndicator]                                   
 - ID: flavor_krak.100
#Description
    Ice Smithing\n£estate_magic_icesmith_bg£\n\n\n\n[Root.GetSpellStrengthIndicator]                                   
#Options

___
##£magic_button_close£

###AI weighting:
AI weights this option at 5


###Efects:<ul><li>highlight = yes</li><li>If is not controlled by the AI:</li><ul><li>remove estate privilege = estate_mages_perform_icecraft</li></ul><li>else:</li><ul><li>set country flag [revoke_mage_estate_spells](../flags/revoke_mage_estate_spells.md)</li></ul><li>custom tooltip = flavor_krak.100.a.tooltip</li></ul>

___
##£spell_ice_equipment£

###Available if:
<li>has country flag [icecraft_equipment](../flags/icecraft_equipment.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai militarist


###Efects:<ul><li>the event [Ice-Steel Equipment](../events/ice_steel_equipment.md) happens</li></ul>

___
##£spell_ice_drills£

###Available if:
<li>has country flag [icecraft_drills](../flags/icecraft_drills.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai capitalist


###Efects:<ul><li>the event [Ice-Steel Drills](../events/ice_steel_drills.md) happens</li></ul>

___
##£spell_ice_gems£

###Available if:
<li>has country flag [icecraft_gems](../flags/icecraft_gems.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if has personality is ai capitalist


###Efects:<ul><li>the event [Frozen Gems](../events/frozen_gems.md) happens</li></ul>

___
##£spell_ice_fields£

###Available if:
<li>has country flag [icecraft_field](../flags/icecraft_field.md)</li>

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if is at war


###Efects:<ul><li>the event [Ice Fields](../events/ice_fields.md) happens</li></ul>

___
##£spell_ice_holds£

###Available if:
<li>has country flag [icecraft_holds](../flags/icecraft_holds.md)</li>

###AI weighting:
AI weights this option at 0


###Efects:<ul><li>the event [Ice-Steel Holds](../events/ice_steel_holds.md) happens</li></ul>
