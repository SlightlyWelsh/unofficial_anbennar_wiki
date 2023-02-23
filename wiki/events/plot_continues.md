#Information
 - Title: Plot Continues
 - ID: coup_in_palace_events.3
#Description
Plot Continues
#Mean Time to Happen:
Base time = 1 days

#Options

___
##What will happen?

###AI weighting:
AI weights this option at 10


###Efects:<ul><li>If has ruler has personality is intricate web weaver personality, and has spymaster is 3:</li><ul><li>random list:</li><ul><li>30:</li><ul><li>custom tooltip = "coup_fails_tooltip"</li><li>hidden effect:</li><ul><li>the event [The Plot Fails](../events/the_plot_fails.md) happens</li><li>set country flag [plot_failed_flag](../flags/plot_failed_flag.md)</li></ul></ul><li>70:</li><ul><li>custom tooltip = "coup_succeeds_tooltip"</li><li>hidden effect:</li><ul><li>the event [The Plot Succeeds](../events/the_plot_succeeds.md) happens</li><li>set country flag [plot_succeeded_flag](../flags/plot_succeeded_flag.md)</li></ul></ul></ul></ul><li>Else if has spymaster is 1:</li><ul><li>random list:</li><ul><li>25:</li><ul><li>custom tooltip = "coup_fails_tooltip"</li><li>hidden effect:</li><ul><li>the event [The Plot Fails](../events/the_plot_fails.md) happens</li><li>set country flag [plot_failed_flag](../flags/plot_failed_flag.md)</li></ul></ul><li>75:</li><ul><li>custom tooltip = "coup_succeeds_tooltip"</li><li>hidden effect:</li><ul><li>the event [The Plot Succeeds](../events/the_plot_succeeds.md) happens</li><li>set country flag [plot_succeeded_flag](../flags/plot_succeeded_flag.md)</li></ul></ul></ul></ul><li>else:</li><ul><li>random list:</li><ul><li>15:</li><ul><li>custom tooltip = "coup_fails_tooltip"</li><li>hidden effect:</li><ul><li>the event [The Plot Fails](../events/the_plot_fails.md) happens</li><li>set country flag [plot_failed_flag](../flags/plot_failed_flag.md)</li></ul></ul><li>85:</li><ul><li>custom tooltip = "coup_succeeds_tooltip"</li><li>hidden effect:</li><ul><li>the event [The Plot Succeeds](../events/the_plot_succeeds.md) happens</li><li>set country flag [plot_succeeded_flag](../flags/plot_succeeded_flag.md)</li></ul></ul></ul></ul></ul>

___
##Purge them. Purge them all.

###AI weighting:
AI weights this option at 1


###Efects:<ul><li>If has estate led regency has estate is estate nobles; and has country flag is [noble_coup](../flags/noble_coup.md):</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_nobles</li><li>loyalty = -25</li></ul><li>If random owned province has controlled by is ROOT:</li><ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 3</li></ul><li>spawn rebels:</li><ul><li>type = noble_rebels</li><li>size = 2</li></ul></ul></ul><li>Else if has country flag is [burgher_coup](../flags/burgher_coup.md), and has estate led regency has estate is estate burghers:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_burghers</li><li>loyalty = -25</li></ul><li>If random owned province has controlled by is ROOT:</li><ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 3</li></ul><li>spawn rebels:</li><ul><li>type = particularist_rebels</li><li>size = 2</li></ul></ul></ul><li>Else if has country flag is [church_coup](../flags/church_coup.md), and has estate led regency has estate is estate church:</li><ul><li>add estate loyalty:</li><ul><li>estate = estate_church</li><li>loyalty = -25</li></ul><li>If random owned province has controlled by is ROOT:</li><ul><li>spawn rebels:</li><ul><li>type = leadered_peasant_rebels</li><li>size = 2</li></ul><li>spawn rebels:</li><ul><li>type = leadered_peasant_rebels</li><li>size = 3</li></ul></ul></ul><li>add stability = -4</li><li>remove advisor = random</li><li>remove advisor = random</li><li>clr country flag [plot_succeeded_flag](../flags/plot_succeeded_flag.md)</li><li>set country flag [plot_failed_flag](../flags/plot_failed_flag.md)</li><li>the event [The Aftermath](../events/the_aftermath.md) happens</li></ul>
