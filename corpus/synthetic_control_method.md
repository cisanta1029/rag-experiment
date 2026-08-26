# Synthetic control method

> Source: [https://en.wikipedia.org/wiki/Synthetic_control_method](https://en.wikipedia.org/wiki/Synthetic_control_method)  
> Retrieved from Wikipedia, licensed under CC BY-SA 4.0.

---

In causal inference, synthetic controls are a class of methods where the quasi-experimental control group is synthesized from a weighted average of potential control units. The method is often used to evaluate treatment effects in scenarios where only one or a small number of units are treated. 
The method was first proposed in a series of articles by Alberto Abadie and coauthors. A synthetic control is a weighted average of several units (such as regions or companies) combined to recreate the trajectory that the outcome of a treated unit would have followed in the absence of the intervention. The weights are selected in a data-driven manner to ensure that the resulting synthetic control closely resembles the treated unit in terms of key predictors of the outcome variable. Unlike difference in differences approaches, this method can account for the effects of confounders changing over time, by weighting the control group to better match the treatment group before the intervention. Another advantage of the synthetic control method is that it allows researchers to systematically select comparison groups. It has been applied to the fields of economics, political science, health policy, criminology, and others.
The synthetic control method combines elements from matching and difference-in-differences techniques. Difference-in-differences methods are often-used policy evaluation tools that estimate the effect of an intervention at an aggregate level (e.g. state, country, age group etc.) by averaging over a set of unaffected units. Famous examples include studies of the employment effects of a raise in the minimum wage in New Jersey fast food restaurants by comparing them to fast food restaurants just across the border in Philadelphia that were unaffected by a minimum wage raise, and studies that look at crime rates in southern cities to evaluate the impact of the Mariel Boatlift on crime.  The control group in this specific scenario can be interpreted as a weighted average, where some units effectively receive zero weight while others get an equal, non-zero weight.
The synthetic control method tries to offer a more systematic way to assign weights to the control group. It typically uses a relatively long time series of the outcome prior to the intervention and estimates weights in such a way that the control group mirrors the treatment group as closely as possible. In particular, assume we have J observations over T time periods where the relevant treatment occurs at time 
  
    
      
        
          T
          
            0
          
        
      
    
    {\displaystyle T_{0}}
  
 where 
  
    
      
        
          T
          
            0
          
        
        <
        T
        .
      
    
    {\displaystyle T_{0}<T.}
  
 Let

  
    
      
        
          α
          
            i
            t
          
        
        =
        
          Y
          
            i
            t
          
        
        −
        
          Y
          
            i
            t
          
          
            N
          
        
        ,
      
    
    {\displaystyle \alpha _{it}=Y_{it}-Y_{it}^{N},}
  

be the treatment effect for unit 
  
    
      
        i
      
    
    {\displaystyle i}
  
 at time 
  
    
      
        t
      
    
    {\displaystyle t}
  
, where 
  
    
      
        
          Y
          
            i
            t
          
          
            N
          
        
      
    
    {\displaystyle Y_{it}^{N}}
  
 is the outcome in absence of the treatment. Without loss of generality, if unit 1 receives the relevant treatment, only 
  
    
      
        
          Y
          
            1
            t
          
          
            N
          
        
      
    
    {\displaystyle Y_{1t}^{N}}
  
 is not observed for 
  
    
      
        t
        >
        
          T
          
            0
          
        
      
    
    {\displaystyle t>T_{0}}
  
. We aim to estimate 
  
    
      
        (
        
          α
          
            1
            
              T
              
                0
              
            
            +
            1
          
        
        .
        .
        .
        .
        .
        .
        
          α
          
            1
            T
          
        
        )
      
    
    {\displaystyle (\alpha _{1T_{0}+1}......\alpha _{1T})}
  
.
Imposing some structure

  
    
      
        
          Y
          
            i
            t
          
          
            N
          
        
        =
        
          δ
          
            t
          
        
        +
        
          θ
          
            t
          
        
        
          Z
          
            i
          
        
        +
        
          λ
          
            t
          
        
        
          μ
          
            i
          
        
        +
        
          ε
          
            i
            t
          
        
      
    
    {\displaystyle Y_{it}^{N}=\delta _{t}+\theta _{t}Z_{i}+\lambda _{t}\mu _{i}+\varepsilon _{it}}
  

and assuming there exist some optimal weights 
  
    
      
        
          w
          
            2
          
        
        ,
        …
        ,
        
          w
          
            J
          
        
      
    
    {\displaystyle w_{2},\ldots ,w_{J}}
  
 such that

  
    
      
        
          Y
          
            1
            t
          
        
        =
        
          ∑
          
            j
            =
            2
          
          
            J
          
        
        
          w
          
            j
          
        
        
          Y
          
            j
            t
          
        
      
    
    {\displaystyle Y_{1t}=\sum _{j=2}^{J}w_{j}Y_{jt}}
  

for 
  
    
      
        t
        ⩽
        
          T
          
            0
          
        
      
    
    {\displaystyle t\leqslant T_{0}}
  
, the synthetic controls approach suggests using these weights to estimate the counterfactual

  
    
      
        
          Y
          
            1
            t
          
          
            N
          
        
        =
        
          ∑
          
            j
            =
            2
          
          
            J
          
        
        
          w
          
            j
          
        
        
          Y
          
            j
            t
          
        
      
    
    {\displaystyle Y_{1t}^{N}=\sum _{j=2}^{J}w_{j}Y_{jt}}
  

for 
  
    
      
        t
        >
        
          T
          
            0
          
        
      
    
    {\displaystyle t>T_{0}}
  
. So under some regularity conditions, such weights would provide estimators for the treatment effects of interest. In essence, the method uses the idea of matching and using the training data pre-intervention to set up the weights and hence a relevant control post-intervention.
Synthetic controls have been used in a number of empirical applications, ranging from studies examining natural catastrophes and growth, or civil conflicts and growth, studies that examine the effect of vaccine mandates on childhood immunization, and studies linking political murders to house prices. Recently, the synthetic control method is actively used in new drug development when evaluating the causal impact of a treatment or intervention, especially in situations where randomized controlled trials (RCTs) are not feasible. 


== See also ==
Difference in difference
Regression discontinuity
Instrumental variables estimation


== References ==