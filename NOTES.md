# What I checked, and what the agent got wrong

## What the agent got wrong

The agent found the main problems from the failed tests, but I noticed that some other issues were not covered by those tests. In particular, fleet_report.py could crash with a Key Error when a car did not have last_ service_ km. I also noticed that the km-to-miles conversion was using the wrong calculation. I found these by checking the code and looking at cases that were not included in the existing tests.

## What I checked before I accepted its work

I checked that the service interval and warning threshold were still 15000 km and 80%, so the fixes did not change the original rules. I also checked the wear calculation using the 14900 km example. The old calculation using // returned 0, while the new calculation using / gives about 99.3%, which is above the 80% threshold. After the changes, all four tests passed, so I was confident that the main fixes were working correctly.

## What the data actually said

The data showed that km_since_service, avg_daily_km, and load_ factor were the main factors related to breakdowns. The surprising part was that odometer_km was almost the same for healthy cars and cars that later broke down, so total mileage was not a useful indicator by itself. This suggests that cars which are driven more heavily and have travelled more kilometres since their last service are more likely to break down. The risk score also supported this, with most of the breakdowns appearing in the highest-risk group
