# Answers Monte Carlo Methods, 7.5 2010-06-01
## 1 Basic statistics
__a)__ Consider independent, random variables $x_i$ with average $\mu$ and variance $\sigma^2$. The average $N$ of such variables
\[
 m = \frac{1}{N} \sum^N_{i=0} x_i
\]
What is $\sigma^2_m$, the variance of $m$?

__Answer:__
\[
 \sigma^2_m = \frac{\sigma^2}{N}
\]
where $\sigma^2$ is the variance of the random indepent variables $x_i$.

__b)__ Derive the result

__Answer:__

__c)__ Specialize to the case where $x_i$ are from a uniform distribution between $-1$ and $1$ and N=100. What is the distribution of $m$?

__Answer:__

## 2 Theory behind Markov chains
__Question:__ A Markov chain may be described as a transition matrix $p_{ij}$. Describe  the three conditions that havo t be fulfilled by thismatrix and motivate why they are necessary.

__Answer:__
1. $p_{ij} \leq 1$, this holds for all $i$ and $j$. This is because the elements of the transition matrix represent a probability. Something with a probability above 1 simply just do not make sense
2. $p_{ii} \le 1$ or $p_{ii} \neq 1$. This is so that the chain does not get stuck. Basically if i get into a state $i$ and then have 100% probability to get into state $i$ again with the next state transition or application of the transition matrix, well then we've gotten stuck.
3. The sum of a row must be equal to one in the transitions matrix, or $\sum_j p_{ij} = 1$ (note that this depends on how the transition matrix is applied, it could just aswell be the columns that need to sum up to 1). This is because we let the row of the transition matrix represent how a state can move on from one state to another. And at such a state transition we need to go somewhere, if we have 10% probability of nothing... What would that even represent?

## 3 1D Ising model
__Question:__ Show that the 1D Ising model is disordered for all $t \gt 0$

__Answer:__ Check in book if we can do the analytical one or take the energy-entropy argument. And according to  the energy-entropy argument it only holds as we take the limit $L \to \infty$

## Scaling Analysis
__Question:__ One way to analyze experimental data (or simulations at big lattices) is to plot $m/|t|^a$ versus $h/|t|^c$. Start from $m \sim \partial f / \partial h$ and
\[
f(t,h) = b^{-d} f(tb^{y_t}, hb^{y_h})
\]
and express $a$ and $c$ in terms of $d$, $y_t$ and $y_h$.

__Answer:__ The goal here is to  get an expression for $m$ divided by $|t|$ and equal this to some function that depends on $h$ divided by $|t|$. To reach this We start with carrying out the derivation
\[
 m \sim b^{-d-1+y_h}f_h(tb^{y_t}, hb^{y_h})
\]
And since where ignoring some constant before we can bake away the $b^{-1}$
\[
 m \sim b^{y_h-d}f_h(tb^{y_t}, hb^{y_h})
\]
Now we we're only interested in $h$, not $t$, so we can set $tb^{y_t} = \pm 1$. This gives $b^{y_t} = |\frac{1}{t}|$ or $b = |t|^{-1/y_t}$ And we put this in and get
\[
 m \sim |t|^{(d - y_h)/y_t}f_h(\pm 1, h|t|^{-y_h/y_t})
\]
or
\[
 m/|t|^{(d-y_h)/y_t} \sim f_h(h/|t|^{y_h/y_t})
\]
with $a = (d-y_h)/y_t$ and $c = y_h/y_t$

## 5 Expectation values
__Pre Questions:__ For small lattices it is possible to use three different methods to calculate the properties of the Ising model:
1. Through a complete enumeration of all the possible states.
2. By generating a set of randomly produced configurations.
3. Through a Monte Carlo simulation.

__a)__ Describe the formulas that should be used to calculate expectation values in methods 1,2 and 3. Assume that we have access to $A_v$ and the energy $E_v$ for each generated configuration and want to calculate $\langle A \rangle$

__Answer:__  We'll go through the methods one by one
1. Since we completely enumerated all states, and calculated the property for each state (recall we have $A_v$), we can simply do an average
\[
 \langle A \rangle = \frac{1}{N_v} \sum_v A_v
\]
2. Since we generate a set of randomly produced configuration we need to weigh each configuration. And we can do this with the help of a little thing we call the Boltzmann factor and statistical physics
\[
 \langle A \rangle = \frac{\sum_v A_v e^{-\beta E_v}}{ \sum_v e^{-\beta E_v}}
\]
3. Ah beautiful Monta Carlo. Since we generate each stat with a probability $\propto e^{-\beta E_v}$ we can simply take an average, the configurations are already weighted!
\[
 \langle A \rangle = \frac{1}{N_v} \sum_v A_v
\]

__b)__ Why could it sometimes be motivated to study a system through a complete enumeration?

__Answer:__ Well basically if we can make the system small enough so that it is feasible to do a complete enumeration, it's a very good way to compare those values to values we obtain through for instance Monte Carlo. That way we can check that our Monte Carlo simulation work for small systems before we set out to simulate larger systems.

__c)__ Consider a complete enumeration of a $L \times L$ Ising model. What is the maximum size L that would be possible to study in 24 hours on a single 3GHz-processor. Base your answer on some reasonable assumptions.

__Answer:__ We need first to look at how many operations we could possibly get during a day, then look at roughly how many is needed to create a complete summation.
1. 3Ghz means that we can make 3*10^9 operations per seconds on a day there is $60*60*24 \approx 8.6 \cdot 10^4$ seconds. we then end up with roughly $10^{14}$ operations to be made(very rough 9+4 then 8*3 as another).
2. Then how many configurations does there exists of an $L \times L$ system? Well every site can have 2 distinct values so it should be $2^{L^2}$ amount of configurations. This should also be multiplied by $L\times L$ since that many summations are required per configuration, but for simplicity lets not. Lets set $L^2 =N$ and the operations we have available to $o$.
\[
2^N = o
\]
which gives
\[
N\ln{2} =  \ln{o}
\]
or
\[
 L = \sqrt{\frac{\ln{o}}{\ln{2}}}
\]
and if we put in some numbers we get
\[
\sqrt{\frac{\ln{10^{14}}}{\ln{2}}} \approx \sqrt{49} = 7
\]
So yeah... not that big xD

## 6 Quantum Monte Carlo
__Question:__ I do not know how to generate the pictures, so i guess you have to look at the exam

__a)__ Which of these states represents a non-vanishing term? Why?

__Answer:__ The term that represent a non-vanishing term is the first picture from the left. This is because the other term has an off-diagonal operation on two spins of the same spin. This creates a 0-vector, thus reducing the whole expression to zero. The non-vanishing has no such occurance and since the off-diagonal flips of states occours twice the spin state is the same in the end as in the beginning so the orthogonality makes sure we have a value there.

__b)__ What is the order fo the expansion (denoted by n) of the non-vanishing term?

__Answer:__ Well $n$ stands for the bonds between the states, something that is showned in the amount of operators that works on the state as a whole (something in the book we refered to {$\mu_n$}). Basically we can see that its 5 of em. So $n=5$

## 7 Master-equation solution of a two state system.
__Pre Question:__  A simple system has two states 0 and 1 with energies $E_0$ and $E_1$ respectively. Transitions between the two states take place at rates $P(0 \to 1) = R_0 e^{-\beta(E_1-E_0)}$ (with $\beta$ as the inverse temperature) and $P(1 \to 0 ) = R_0$ Let $w_0(t)$ and $w_1(t)$ be the probabilities of the system being in state 0 or 1 as a function of time $t$ with the initial conditions $w_0(0)=0$ and $w_1(0) = 1$.

__a)__ Express $\frac{dw_0}{dt}$ in terms of $\beta$, $R_0$ and $E_1$

__Answer:__ We know that $w_0 + w_1 = 1$ and the derivate is given by
\[
\frac{dw_0}{dt} = \\
(\text{Probability of state 0} \times \text{Probality of a change to state 1}) \\
minus \\
(\text{Probability of state 1} \times \text{Probality of a change to state 0})
\]
bububu
\[
\frac{dw_0}{dt} = w_0R_0e^{-\beta (E_1 - E_0)}
\]

Why?



__b)__ Solve this equation and show that the system obeys the Boltzmann distribution in the limit $t \to \infty$

__Answer:__
