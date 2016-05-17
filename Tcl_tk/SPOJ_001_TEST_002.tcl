#!/usr/bin/tclsh

# This code is for SPOJ TEST problem. This uses the for loop. This is not an 
# accepted solution as it asks for an input but doesn't conform to the running 
# time limit of 1s which is necessary to pass the test.

set lst_1 [gets stdin]

set lst_2 [list ]

for {set i 0} {[lindex $lst_1 $i] != 42} {incr i} {
  	lappend lst_2 [lindex $lst_1 $i]
}

puts $lst_2
