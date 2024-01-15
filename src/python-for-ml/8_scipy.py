""" 
SciPy is a free and open-source Python library used for scientific and technical computing. 
It is built on the NumPy extension and allows the user to manipulate and visualize data with a wide range of high-level commands. 
Here are some of the main uses of SciPy:

Mathematical Algorithms: SciPy is built to work with NumPy arrays and provides many efficient and user-friendly interfaces for tasks such as numerical integration and optimization.

Statistics: The scipy.stats module contains a large number of statistical distributions, statistical functions and tests. For example, it provides functions for computing the PDF, CDF, as well as many other properties of a wide variety of statistical distributions.

Signal Processing: If you're working with signal processing and need to do things like convolution, Fourier transforms, or filter design, the scipy.signal module provides a suite of tools for this kind of tasks.

Linear Algebra: The scipy.linalg module provides standard linear algebra operations, relying on an underlying efficient implementation (BLAS, LAPACK).

Interpolation: The scipy.interpolate is useful for fitting a function from experimental data and thus evaluating points where no measure exists.

Spatial data structures and algorithms: The scipy.spatial can compute Triangulations, Voronoi Diagrams and Convex Hulls of a set of points, by leveraging the Qhull library.

Multidimensional image processing: The scipy.ndimage package contains various functions for multi-dimensional image processing.

File IO: The scipy.io module provides a set of functions for reading and writing various file formats.

These are just a few examples of what SciPy can do. It's a very versatile library that can handle a lot of different scientific computing tasks.

Paired T-test: scipy.stats.ttest_rel(a, b) performs a paired t-test on arrays a and b.
.


SciPy provides a comprehensive set of statistical tests through its scipy.stats module. Here are some common ones:

T-test: scipy.stats.ttest_ind(a, b) performs an independent 2-sample t-test on arrays a and b.

Paired T-test: scipy.stats.ttest_rel(a, b) performs a paired t-test on arrays a and b.

Chi-Square test: scipy.stats.chisquare(f_obs, f_exp) performs a chi-square test.

ANOVA (Analysis of Variance): scipy.stats.f_oneway(*args) performs a 1-way ANOVA.

Mann-Whitney U test: scipy.stats.mannwhitneyu(x, y) performs a Mann-Whitney U test on arrays x and y.

Kruskal-Wallis H-test: scipy.stats.kruskal(*args) performs a Kruskal-Wallis H test.

Wilcoxon Signed-Rank Test: scipy.stats.wilcoxon(x, y) performs a Wilcoxon signed-rank test.

Pearson's Correlation Coefficient: scipy.stats.pearsonr(x, y) calculates a Pearson correlation coefficient.

Spearman's Correlation Coefficient: scipy.stats.spearmanr(a, b=None, axis=0, nan_policy='propagate') calculates a Spearman rank-order correlation coefficient.

Kendall's Tau: scipy.stats.kendalltau(x, y, initial_lexsort=None, nan_policy='propagate', method='auto') calculates Kendall’s tau, a correlation measure for ordinal data.
"""

""" Pearson Correlation """
from scipy import stats
import numpy as np

# Create two arrays of random numbers.
np.random.seed(0)  # For reproducibility.
x = np.random.rand(10)
y = np.random.rand(10)

# Calculate the Pearson correlation coefficient and the p-value.
correlation, p_value = stats.pearsonr(x, y)

print(f'Pearson correlation: {correlation}')
print(f'p-value: {p_value}')
# In this code, stats.pearsonr(x, y) calculates the Pearson correlation coefficient and the p-value 
# for testing non-correlation. The Pearson correlation coefficient measures the linear relationship 
# between two datasets. The p-value roughly indicates the probability of an uncorrelated system 
# producing datasets that have a Pearson correlation at least as extreme as the one computed from these datasets.

""" T-test 
A t-test is a type of inferential statistic used to determine if there is a significant difference 
between the means of two groups. It is used when the data would follow a normal distribution and 
have unknown variances.

There are three types of t-tests:

Independent Samples t-test: Compares the means for two groups.
Paired Sample t-test: Compares means from the same group at different times (say, one year apart).
One sample t-test: Tests the mean of a single group against a known mean.
In SciPy, the function scipy.stats.ttest_ind(a, b) is used to calculate the T-test for 
the means of two independent samples of scores. Here, a and b are arrays.

"""

from scipy import stats
import numpy as np

# Create two arrays of random numbers.
np.random.seed(0)  # For reproducibility.
a = np.random.rand(10)
b = np.random.rand(10)

# Independent Samples t-test.
t_statistic, p_value = stats.ttest_ind(a, b)
print(f'Independent Samples t-test:\n t-statistic: {t_statistic}\n p-value: {p_value}\n')

# Paired Sample t-test.
t_statistic, p_value = stats.ttest_rel(a, b)
print(f'Paired Sample t-test:\n t-statistic: {t_statistic}\n p-value: {p_value}\n')

# One sample t-test. Testing the mean of array 'a' against the known mean 0.5.
t_statistic, p_value = stats.ttest_1samp(a, 0.5)
print(f'One Sample t-test:\n t-statistic: {t_statistic}\n p-value: {p_value}\n')

""" 
In this code, stats.ttest_ind(a, b) performs an Independent Samples t-test, stats.ttest_rel(a, b) 
performs a Paired Sample t-test, and stats.ttest_1samp(a, 0.5) performs a One Sample t-test. 
The t-statistic and the p-value are returned for each test. The p-value roughly indicates the
probability of an uncorrelated system producing datasets that have a t-statistic at least as extreme 
as the one computed from these datasets.


The p-value in this context is used to determine the significance of the results after a 
hypothesis test in statistics.

In the given code, three types of t-tests are performed: an Independent Samples t-test, 
a Paired Sample t-test, and a One Sample t-test. For each test, a t-statistic is computed and 
a corresponding p-value is returned.

The p-value is a number between 0 and 1 and interpreted in the following way: a small p-value 
(typically ≤ 0.05) indicates strong evidence against the null hypothesis, so you reject the null 
hypothesis. A large p-value (> 0.05) indicates weak evidence against the null hypothesis, so you 
fail to reject the null hypothesis.

In simpler terms, the p-value tells you the probability of getting a t-statistic as extreme as 
the one you got if the null hypothesis is true. If this probability is low 
(below the threshold you set, often 0.05), you conclude that the effect is unlikely to 
have occurred by chance, and hence is significant.

"""

""" 
ANOVA (Analysis of Variance)
"""

from scipy import stats
import numpy as np

# Create three arrays of random numbers.
np.random.seed(0)  # For reproducibility.
a = np.random.rand(10)
b = np.random.rand(10)
c = np.random.rand(10)

# Perform the ANOVA.
f_value, p_value = stats.f_oneway(a, b, c)

print(f'ANOVA results:\n F-value: {f_value}\n p-value: {p_value}\n')

""" 
In this code, stats.f_oneway(a, b, c) performs a one-way ANOVA. The F-statistic and the p-value are returned.

The null hypothesis in an ANOVA test is that all group means are equal. The alternative hypothesis 
is that at least one group mean is different from the others.

The p-value is used to determine the significance of the results. A small p-value (typically ≤ 0.05) 
indicates strong evidence against the null hypothesis, so you reject the null hypothesis. This means 
that there is a significant difference between at least one pair of group means. A large p-value (> 0.05) 
indicates weak evidence against the null hypothesis, so you fail to reject the null hypothesis.
This means that there is no significant difference between the group means.
"""