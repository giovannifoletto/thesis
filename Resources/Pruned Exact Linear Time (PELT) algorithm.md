[Optimal deterction of changepoint with a linear computational cost](https://arxiv.org/pdf/1101.1438.pdf)

[R Project](https://search.r-project.org/CRAN/refmans/changepoint/html/PELT.html)

### Description

Implements the PELT method for identifying changepoints in a given set of summary statistics for a specified cost function and penalty.

This function is called by `cpt.mean`, `cpt.var` and `cpt.meanvar` when `method="PELT"`. This is not intended for use by regular users of the package. It is exported for developers to call directly for speed increases or to fit alternative cost functions.

WARNING: No checks on arguments are performed! 

*=> presented in the paper above and then applied. The code is in R std library, performed with a wrapped C code.* 
