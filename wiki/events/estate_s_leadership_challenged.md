#Information
 - Title: Estate's Leadership Challenged
 - ID: estate_regency_events.1
#Description
Estate's Leadership Challenged
#Options

___
##There is no option but accepting a change of leadership.

###AI weighting:
AI weights this option at 50
 - Multiplied by 2 if does not have estate led regency influence is 70


###Efects:<ul><li>custom tooltip = "estate_change_tooltip"</li><li>If has country flag is [burgher_coup](../flags/burgher_coup.md):</li><ul><li>define ruler:</li><ul><li>regency:</li><ul><li>estate = estate_burghers</li></ul></ul><li>clr country flag [burgher_coup](../flags/burgher_coup.md)</li></ul><li>Else if has country flag is [church_coup](../flags/church_coup.md):</li><ul><li>define ruler:</li><ul><li>regency:</li><ul><li>estate = estate_church</li></ul></ul><li>clr country flag [church_coup](../flags/church_coup.md)</li></ul><li>Else if has country flag is [noble_coup](../flags/noble_coup.md):</li><ul><li>define ruler:</li><ul><li>regency:</li><ul><li>estate = estate_nobles</li></ul></ul><li>clr country flag [noble_coup](../flags/noble_coup.md)</li></ul></ul>

___
##They must support the regent for the good of the nation.

###AI weighting:
AI weights this option at 50
 - Multiplied by 0 if does not have estate led regency influence is 70


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = "estate_displeased_tooltip"</li><li>If has country flag is [burgher_coup](../flags/burgher_coup.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_burghers</li><li>loyalty = -10</li><li>desc = REFUSED_REGENCY</li><li>duration = 10950</li></ul><li>clr country flag [burgher_coup](../flags/burgher_coup.md)</li></ul><li>Else if has country flag is [church_coup](../flags/church_coup.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_church</li><li>loyalty = -10</li><li>desc = REFUSED_REGENCY</li><li>duration = 10950</li></ul><li>clr country flag [church_coup](../flags/church_coup.md)</li></ul><li>Else if has country flag is [noble_coup](../flags/noble_coup.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li><li>desc = REFUSED_REGENCY</li><li>duration = 10950</li></ul><li>clr country flag [noble_coup](../flags/noble_coup.md)</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = "coup_attempt_starts_tooltip"</li><li>If has country flag is [burgher_coup](../flags/burgher_coup.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_burghers</li><li>loyalty = -10</li><li>desc = REFUSED_REGENCY</li><li>duration = 10950</li></ul></ul><li>Else if has country flag is [church_coup](../flags/church_coup.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_church</li><li>loyalty = -10</li><li>desc = REFUSED_REGENCY</li><li>duration = 10950</li></ul></ul><li>Else if has country flag is [noble_coup](../flags/noble_coup.md):</li><ul><li>add estate loyalty modifier:</li><ul><li>estate = estate_nobles</li><li>loyalty = -10</li><li>desc = REFUSED_REGENCY</li><li>duration = 10950</li></ul></ul><li>set country flag [coup_attempt_starts](../flags/coup_attempt_starts.md)</li></ul>
