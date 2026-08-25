# What I checked, and what the agent got wrong

One thing I noticed was that some of the original analysis was correct, but a few issues were not fully covered by the tests. For example, the tests caught the integer division problem and the missing last_service_km problem, but the analysis also showed that fleet_report.py could crash with a KeyError for a car with no service reading. I also checked that the important values, 15000 km for the service interval and 80% for the warning threshold, were not accidentally changed while fixing the code. Another thing I noticed was the incorrect km-to-miles conversion, which was not caught by the normal tests but was caught during the wider verification.

## What the agent got wrong

The agent's initial analysis identified the main test failures, but it did not fully cover some problems that were outside those tests. I noticed that fleet_report.py could still crash with a KeyError when a car did not have last_service_km. I also found that the km-to-miles conversion was incorrect. I noticed these by checking the code beyond just the failed tests and comparing the calculations with what they should actually produce.

## What I checked before I accepted its work

I checked that the original 15,000 km service interval and 80% warning threshold were still unchanged. I also checked the wear calculation using the 14,900 km example. The old 14900 // 15000 gave 0%, while the corrected 14900 / 15000 gives about 99.3%. After the fixes, all four tests passed, which confirmed that the wear calculation and missing-reading handling were working correctly.

## What the data actually said

The data showed that km_since_service, avg_daily_km, and load_factor were useful indicators of breakdown risk. The surprising result was that odometer_km, which might seem like an obvious factor, was almost the same for healthy and breakdown cars, so it was not useful for prediction. This means the fleet team should pay more attention to how recently and heavily a car has been used rather than only looking at its total kilometres.
