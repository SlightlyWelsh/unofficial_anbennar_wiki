#Information
 - Title: Gathered Sacrifices from $PROVINCENAME$
 - ID: xhazobkult_events.1101
#Description
Gathered Sacrifices from $PROVINCENAME$
#Mean Time to Happen:
Base time = 365 days
 - Multiplied by 0.6 if has development is 4
 - Multiplied by 0.8 if has development is 10
 - Multiplied by 0.9 if has development is 20
 - Multiplied by 1.2 if has devastation is 20
 - Multiplied by 1.2 if has devastation is 40
 - Multiplied by 1.2 if has devastation is 60
 - Multiplied by 1.2 if has devastation is 80

#Options

___
##More for the Fires.

###AI weighting:
AI weights this option at 1


###One of the following randomly happens:
Outcome 1:

Available if <li>base tax is at least 2</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base tax = -1</li><li>add devastation = 25</li></ul>
Outcome 2:

Available if <li>base production is at least 2</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base production = -1</li><li>add devastation = 25</li></ul>
Outcome 3:

Available if <li>base manpower is at least 2</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base manpower = -1</li><li>add devastation = 25</li></ul>
Outcome 4:

Available if <li>None of the following:</li><ul><li>development is at least 4</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add devastation = 60</li></ul>

###Efects:<ul><li>owner:</li><ul><li>change variable:</li><ul><li>which = total_gathered_sacrifices</li><li>value = 1</li></ul></ul></ul>

___
##Hide these events until next time gathering sacrifices

###AI weighting:
AI weights this option at 0


###One of the following randomly happens:
Outcome 1:

Available if <li>base tax is at least 2</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base tax = -1</li><li>add devastation = 25</li></ul>
Outcome 2:

Available if <li>base production is at least 2</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base production = -1</li><li>add devastation = 25</li></ul>
Outcome 3:

Available if <li>base manpower is at least 2</li>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add base manpower = -1</li><li>add devastation = 25</li></ul>
Outcome 4:

Available if <li>None of the following:</li><ul><li>development is at least 4</li></ul>

The weight of this outcome is 1

This outcome causes the following effects:<ul><li>add devastation = 60</li></ul>

###Efects:<ul><li>custom tooltip = xhazobkult_gather_sacrifices_disable_events_tt</li><li>owner:</li><ul><li>change variable:</li><ul><li>which = total_gathered_sacrifices</li><li>value = 1</li></ul></ul><li>hidden effect:</li><ul><li>owner:</li><ul><li>set country flag [xhazobkult_hide_sacrifice_gathering_events_flag](../flags/xhazobkult_hide_sacrifice_gathering_events_flag.md)</li></ul></ul></ul>


#Pages with same name:
The following pages have the same name as this page:
 - [gathered_sacrifices_from_provincename_1](gathered_sacrifices_from_provincename_1.md)
