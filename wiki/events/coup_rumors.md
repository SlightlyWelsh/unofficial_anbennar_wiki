#Information
 - Title: Coup Rumors
 - ID: coup_in_palace_events.1
#Description
Coup Rumors
#Mean Time to Happen:
Base time = 1 days

#Options

___
##An investigation must be done so light is casted over the issue.

###AI weighting:
AI weights this option at 75
 - Multiplied by 0 if does not have years of income is 1.5


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = "coup_ended_tooltip"</li><li>set country flag [plot_failed_flag](../flags/plot_failed_flag.md)</li><li>hidden effect:</li><ul><li>the event ˻coup_in_palace_events.2˼ happens</li></ul></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = "nothing_found_tooltip"</li><li>hidden effect:</li><ul><li>add disaster progress:</li><ul><li>disaster = coup_attempt_disaster</li><li>value = 50</li></ul><li>the event ˻coup_in_palace_events.3˼ happens</li></ul></ul>

###Efects:<ul><li>add years of income = -1.5</li></ul>

___
##Those are probably nothing but gossips, but we shall be ready just in case.

###AI weighting:
AI weights this option at 25
 - Multiplied by 4 if does not have years of income is 1.5


###One of the following randomly happens:
Outcome 1:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = "gossips_end_tooltip"</li><li>set country flag [plot_failed_flag](../flags/plot_failed_flag.md)</li><li>end disaster = coup_attempt_disaster</li></ul>
Outcome 2:

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>custom tooltip = "gossips_continue_tooltip"</li><li>hidden effect:</li><ul><li>the event ˻coup_in_palace_events.3˼ happens</li></ul></ul>
