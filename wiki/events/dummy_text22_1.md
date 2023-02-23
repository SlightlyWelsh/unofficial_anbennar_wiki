This page has the same name as others. For full listing see bottom of [the base page](dummy_text22.md).

#Information
 - Title: Dummy text
 - ID: halfling_tolerance_events.0
#Description
Dummy text
#Mean Time to Happen:
Base time = 1 days
 - Multiplied by 10 if has country modifier is racial focus halfling

#Options

___
##Unnamed Option

###One of the following randomly happens:
Outcome 1:

Available if <li>any owned province:</li><ul><li>has halfling minority trigger yes</li><li>None of the following:</li><ul><li>has province modifier halfling_not_allowed_to_trade</li></ul><li>NOT:</li><ul><li>has province modifier halfling_low_quality_wares</li></ul><li>Any of the following:</li><ul><li>trade goods is grain</li><li>trade goods  is livestock</li><li>trade goods   is fish</li><li>trade goods    is wine</li><li>trade goods     is sugar</li><li>trade goods      is coffee</li><li>trade goods       is tobacco</li><li>trade goods        is cocoa</li><li>trade goods         is dyes</li></ul></ul>

The weight of this outcome is 1
 - Multiplied by 2 if has low tolerance halfling race trigger is yes

The weight of this outcome is 1
 - Multiplied by 0.5 if has high tolerance halfling race trigger is yes

This outcome causes the following effects:<ul><li>the event ˻halfling_tolerance_events.1˼ happens</li></ul>
Outcome 2:

Available if <li>any owned province:</li><ul><li>None of the following:</li><ul><li>has province modifier halfling_was_not_given_compensation</li></ul><li>has halfling minority trigger yes</li><li>Any of the following:</li><ul><li>trade goods is grain</li><li>trade goods  is livestock</li><li>trade goods   is dyes</li><li>province trade power is at least 10</li></ul></ul>

The weight of this outcome is 1 
 - Multiplied by 0.9 if has low tolerance halfling race trigger is yes

The weight of this outcome is 1 
 - Multiplied by 1.1 if has high tolerance halfling race trigger is yes

This outcome causes the following effects:<ul><li>the event ˻halfling_tolerance_events.2˼ happens</li></ul>
Outcome 3:

Available if <li>any owned province:</li><ul><li>None of the following:</li><ul><li>has province modifier halfling_angry_over_not_accepting_gift</li></ul><li>NOT:</li><ul><li>has province modifier halfling_punishment_of_local_traitors</li></ul><li>has halfling minority trigger yes</li></ul>

The weight of this outcome is 1  
 - Multiplied by 1.5 if has high tolerance halfling race trigger is yes

The weight of this outcome is 1  
 - Multiplied by 2 if has stability is 1

This outcome causes the following effects:<ul><li>the event ˻halfling_tolerance_events.3˼ happens</li></ul>
Outcome 4:

The weight of this outcome is 1   
 - Multiplied by 1.5 if has medium tolerance halfling race trigger is yes

The weight of this outcome is 1   
 - Multiplied by 2 if has high tolerance halfling race trigger is yes

This outcome causes the following effects:<ul><li>the event ˻halfling_tolerance_events.4˼ happens</li></ul>
Outcome 5:

Available if <li>any owned province:</li><ul><li>has halfling minority trigger yes</li><li>None of the following:</li><ul><li>has province modifier high_halfling_crime</li></ul></ul>

The weight of this outcome is 1    
 - Multiplied by 2 if has low tolerance halfling race trigger is yes

The weight of this outcome is 1    
 - Multiplied by 2 if does not have stability is 0

This outcome causes the following effects:<ul><li>the event ˻halfling_tolerance_events.5˼ happens</li></ul>
Outcome 6:

Available if <li>any owned province:</li><ul><li>has halfling minority trigger yes</li><li>None of the following:</li><ul><li>has province modifier halfling_food_festival</li></ul></ul>

The weight of this outcome is 1     
 - Multiplied by 1.5 if has high tolerance halfling race trigger is yes

The weight of this outcome is 1     
 - Multiplied by 1.5 if has medium tolerance halfling race trigger is yes

This outcome causes the following effects:<ul><li>the event ˻halfling_tolerance_events.6˼ happens</li></ul>
Outcome 7:

Available if <li>any owned province:</li><ul><li>Any of the following:</li><ul><li>has large halfling minority trigger yes</li><li>has halfling majority trigger yes</li></ul><li>any neighbor province:</li><ul><li>is city</li></ul></ul>

The weight of this outcome is 1      
 - Multiplied by 1.5 if has any owned province has halfling majority trigger is yes

The weight of this outcome is 1      
 - Multiplied by 1.5 if has stability is 1

This outcome causes the following effects:<ul><li>the event ˻halfling_tolerance_events.7˼ happens</li></ul>
Outcome 8:

Available if <li>None of the following:</li><ul><li>culture group is halfling</li></ul><li>any owned province:</li><ul><li>has halfling minority trigger yes</li><li>None of the following:</li><ul><li>has province modifier cheap_halfling_labour</li></ul></ul>

The weight of this outcome is 1       
 - Multiplied by 2 if has low tolerance halfling race trigger is yes

This outcome causes the following effects:<ul><li>the event ˻halfling_tolerance_events.8˼ happens</li></ul>
