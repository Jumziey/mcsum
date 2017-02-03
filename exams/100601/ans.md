# Answers Monte Carlo Methods, 7.5 2010-06-01
## 1 Basic statistics
__a)__ Consider independent, random variables $x_i$ with average $\mu$ and variance $\sigma^2$. The average $N$ of such variables
\[
 m = \frac{1}{N} \sum^N_{i=0} x_i
\]
What is $\sigma^2_m$, the variance of $m$?

__Answer:__ The variance is given through
\[
 \sigma^2_m = \frac{\sigma^2}{N}
\]
where $\sigma^2$ is the variance of the random indepent variables $x_i$.

__b)__ Derive the result

__Answer:__ We start by defining a random variable built  from two other random variables $z = x+y$. Where $x$ has the variance $\sigma_x$ and $y$ has the variance $\sigma_y$. We know from other proof that $\mu_x = \mu_x +\mu_y$ Then we go from the definition of the variance
\[
\sigma^2_z = \int \int ((x+y) - (\mu_x+\mu_y))^2 p(x)p(y) dx dy \\
\int \int ((x-\mu_x) + (y-\mu_y))^2 p(x)p(y) dx dy \\
\int \int ((x-\mu_x)^2 + (y-\mu_y)^2 + 2(x-\mu_x)(y-\mu_y)) p(x) p(y) dx dy \\
\int \int ((x-\mu_x)^2 + (y-\mu_y)^2) p(x) p(y) dx dy
\]
and  now recall that $\int p(x) dx = 1$ and we can continue
\[
 \int (x-\mu_x)^2p(x) p(y) dx dy + \int (y-\mu_y)^2 p(x)p(y) dx dy \\
 \int (x-\mu_x)^2 p(x) dx + \int (y - \mu_y)^2 p(y) dy \\
 \sigma^2_x + \sigma^2_y
\]

__c)__ Specialize to the case where $x_i$ are from a uniform distribution between $-1$ and $1$ and N=100. What is the distribution of $m$?

__Answer:__ It has a Gaussian distribution through the central limit theorem. $\mu_x = 0$ and variance $4/12 = 1/3$ (simply use mathematics handbook and find that the variance is $(b-a)^2/12$)

## 2 Theory behind Markov chains
__Question:__ A Markov chain may be described as a transition matriffx $p_{ij}$. Describe  the three conditions that havo t be fulfilled by thismatrix and motivate why they are necessary.

__Answer:__
1. $p_{ij} \leq 1$, this holds for all $i$ and $j$. This is because the elements of the transition matrix represent a probability. Something with a probability above 1 simply just do not make sense
2. $p_{ii} \le 1$ or $p_{ii} \neq 1$. This is so that the chain does not get stuck. Basically if i get into a state $i$ and then have 100% probability to get into state $i$ again with the next state transition or application of the transition matrix, well then we've gotten stuck.
3. The sum of a row must be equal to one in the transitions matrix, or $\sum_j p_{ij} = 1$ (note that this depends on how the transition matrix is applied, it could just aswell be the columns that need to sum up to 1). This is because we let the row of the transition matrix represent how a state can move on from one state to another. And at such a state transition we need to go somewhere, if we have 10% probability of nothing... What would that even represent?

## 3 1D Ising model
__Question:__ Show that the 1D Ising model is disordered for all $T \gt 0$

__Answer:__ Using the Entropy-Energy argument. Basically in order to prove this we start by looking at the ground state and look for the probability to be there against the probability to be in a higher energy state, or in this case the ground state must be the orderered state and the higher energy states needs to be the disordered state. This comes from the Hamilitonian of the Ising model:  $H(\{s_i\}) = -J\sum_{\langle ij \rangle} s_i s_j - \sum_i s_i$

But i digress. Lets start by looking at the probability to be in a state. This probability comes from the Boltzmann factor (Well we are dealing with statistical physics). so we could define our ground state as
\[
P_0 = \Omega_0 e^{-\beta E_0}
\]
Where P_0 is the probability to be in a state $0$ and $\Omega_0$ is the amount of ground states and $E_0$ is the energy in the ground state (ordered one). The probability to be in a state just higher then this is
\[
P_1 = \Omega_1 e^{-\beta E_1}
\]
But we also know some cool stuff from our statistical physics background, namely
\[
 S = k_B \ln{\Omega}
\]
Where $S$ is the entropy, which gives us
\[
 \Omega = e^{S/(k_B)} = e^{\beta T S}
\]
Which gives us
\[
 P_x = e^{\beta( T S - E)}
\]
or
\[
P_x = e^{-\beta (E - T S)} = e^{-\beta F}
\]
where $F$ is the free energy

We can now see that if we define $\Delta F = F_1 - F_0$ we now that we will only get predominaly get the ground state if $\Delta F > 0$. Note also that $\Delta F$ could be written $\Delta E - T \Delta S$

Now to prove the statement. Well the statement only holds for $L \to \infty$ in the 1D lattice (im just saying it up front).

We start with looking at the amount of available states in the ordered state and the state that has 1 flipped state (we're only looking at these two as possible). We start with $\Omega_0 = 2$ since it's all up or all down. The energy of the first state is given by $E_0$. We also have $\Omega_1 = 2L$, this is because every spin could be flipped compared to the rest of the configuration, either up or down. So we look at $\Delta F$
\[
 \Delta F = \Delta E - T \Delta S = (E_1 - E_0) - T \Delta S = \Delta E - (k_B T (\ln{2L} - \ln{2})) \\
 ... = \Delta E - k_B T \ln{(L)}
\]
And since we're looking at $L \to \infty$ Well, we sure as hell has a extremly negative $\Delta F$ so no chance for ground state unless ofcourse $T=0$ and remove the term all together. (No math weirdness due to $\infty$ time $0$ here, its only a fake physical $\infty$ so $0$ wins)

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

## 8 Conserved-ordor-parameter Ising model
__Pre Question:__ The conserved-order-parameter Ising model is defined just  like the regular Ising model butwith the extra condition that the magnetization is fixed M (i.e. a controlparameter of the model). The traditional way of simulating the conserved-order-parameter Ising model is by the Kawasaki algorithm defined as follows on a lattice with $N$ spins.
1. Start with any configuration of $(N+M)/2$ up-spins and $(N-M)/2$ down-spins
2. Chose two sites $i$ and $j$ at random
3. if $v$ is the current spin-configuration, let $\mu$ be the spin configuration where $s_i$ (the value of the spin at site $i$) has the  value that $s_j$ does in $v$ and $s_j$ has the value of $s_i$ in $v$ (basically we swap the spin values between $i$ and $j$ and call this new configuration for $\mu$)
4. let $\Delta E = H(\mu)-H(v)$ Where $H$ is the Ising Hamiltonian.
5. if $\Delta E \lt 0$ or with a probability $\exp{(-\beta \Delta E)}$, swap the spin-values of site $i$ and $j$
6. Go to step 2

Obviuosly the magnetization is constantly M. Our questions are:

__a)__ Define ergodicity.

__Answer:__ ergodicity is that all configurations(or states) can be reached within a finite number of steps

__b)__ Why does the Kawasaki algorithm sample the configurations of the conserved-order-parameter model ergodically?

__Answer:__ We randomly choose the sites to swap. Given enough iteration we have swapped all, and we can do it in a finite number of step since the probability of doing so increases with every step.

__c)__ Define detailed balance.

__Answer:__ We define detailed balance as the probability to reach one state times the probability to move to another state from this state should be equal to the probability of beeing in this new state times the probability to get from the new state to the old.

To clarify: If we have a state $\pi_i$ and a state $\pi_{j}$ and a transition matrix with the elements $p_{row,col}$ we can then write detailed balance as
\[
 \pi_i p_{i,j} = \pi_j p_{j,i}
\]

__d)__ Why does Kawasakis algorithm fullfill detailed balance?

__Answer:__
We have the same probability to be suggested no matter what. But what about the probabibilty of acceptance? Well given this whwe have detailed balance if the acceptance probability is the same as the probability to be in the new state divided by the probability to be in the old state, or one hundred percent if that's less. I.e if $\alpha_{ij}$ is the probability that we will accept to go from a state $\pi_i$ to a state $\pi_j$ we get
\[
 \alpha_{ij} = min(1, \pi_j/\pi_i)
\]

And this we have due to the way we accept the new state. Due to the intricacies of statistical physics we now that the probability of a certain state with a certain energy to be occupied is described by the boltzmann factor. And that's precisly what we have in $\Delta E$. We have the boltzmann factor of the new state/configuration divided by the boltzmann factor of the old state/configuration. To see that i underline
\[
e^{-\beta (E_{new}-E_{old})} = e^{-\beta E_{new}} / e^{-\beta E_{old}}
\]
And $E$ and $H$ is the same since $H$ just the hamilitonian, that describes the energy of the configuration.

__e)__

__Answer:__ I am a little baffled by the question sadly dont completely understand what one wants me to pick. Look into what is required for a boltzmann distribution.
