###  Mean and variance of combinated variates
Imagine that z is made up of 2 indepndet distrubutions X and Y, then:

Mean
$$\mu_z = \mu_x + \mu_y$$
Variance
$$\sigma^{2}_z = \sigma^{2}_x + \sigma^{2}_y  $$
Thus the average m of N independent random variables is (imagine $x_i$ to be a sambple from a distribution)
$$m=\frac{1}{N} \sum^{N}_{i=1}x_i$$
And the variance of m must be
$$\sigma^2_m= \frac{1}{N} \sigma^2_x$$

### Correlation and Variance of correlated varibles
Covariance
$$cov[x,y]=\int (x-\mu_x)(y-\mu_y)p(x,y)dxdy$$
then the variance of Z built by by X and Y
$$\sigma^{2}_z = \sigma^{2}_x + \sigma^{2}_y  + 2cov[X,Y]$$
The correlation coefficient is a normalized value for the amount the function correlate 
$$\rho \frac{cov[X,Y]}{\sqrt{\sigma^2_x\sigma^2_y}}$$

### Distruibution of a sequesnce of variables.
$x_1,...,x_n$ is a sequence of corelated random variables where each variable is described by $\mu$ and $\sigma^2$ and the correlation are $cov[x_i,x_j = <x_ix_j>-\mu^2$