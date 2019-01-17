# normb
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)

[![Python 3.6](https://img.shields.io/badge/python-3.6-blue.svg)](https://www.python.org/downloads/release/python-360/)
[![Project Status: Active – The project has reached a stable, usable state and is being actively developed.](https://www.repostatus.org/badges/latest/active.svg)](https://www.repostatus.org/#active)
[![GitHub license](https://img.shields.io/github/license/Naereen/StrapDown.js.svg)](https://github.com/Naereen/StrapDown.js/blob/master/LICENSE)

Package that runs a battery of univariate normality tests on the row or column vectors of a pandas.DataFrame (df). The packages comes with a `DataFrameGenerator` that can produce dfs following a `uniform`, `normal` or `mixed` distribution. These dataframes or any other dfs can be run through the `NormalityBattery` class which runs the conventional normality tests by [Kolmogorov A (1933)](https://ci.nii.ac.jp/naid/10010480527/), [Smirnov N (1948)](https://www.jstor.org/stable/2236278?seq=1#page_scan_tab_contents), [Shapiro and Wilk(1965)](https://www.jstor.org/stable/2333709?seq=1#page_scan_tab_contents), [Jarque and Bera (1980)](https://www.sciencedirect.com/science/article/pii/0165176580900245), [D’Agostino (1971)](https://www.jstor.org/stable/2334522) and [Pearson’s (1973)](https://www.jstor.org/stable/2335012?seq=1#page_scan_tab_contents). The results of the test are summaried in a report which can be accessed via the `print_report` method in the `NormalityBattery` class. 
