#Information
 - Title: The Plot Succeeds
 - ID: coup_in_palace_events.5
#Description
The Plot Succeeds
#Mean Time to Happen:
Base time = 1 days

#Options

___
##No, hope is lost. Theirs is the throne and our faith.

###Efects:<ul><li>set country flag [plot_succeeded_flag](../flags/plot_succeeded_flag.md)</li><li>add absolutism = -75</li><li>If has country flag is [church_coup](../flags/church_coup.md):</li><ul><li>change estate land share:</li><ul><li>estate = estate_church</li><li>share = 25</li></ul></ul><li>Else if has country flag is [burgher_coup](../flags/burgher_coup.md):</li><ul><li>change estate land share:</li><ul><li>estate = estate_burghers</li><li>share = 25</li></ul></ul><li>Else if has country flag is [noble_coup](../flags/noble_coup.md):</li><ul><li>change estate land share:</li><ul><li>estate = estate_nobles</li><li>share = 25</li></ul></ul><li>else:</li><ul><li>change estate land share:</li><ul><li>estate = all</li><li>share = 30</li></ul></ul><li>the event [The Aftermath](../events/the_aftermath.md) happens</li></ul>
