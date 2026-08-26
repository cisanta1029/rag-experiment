# Difference in differences

> Source: [https://en.wikipedia.org/wiki/Difference_in_differences](https://en.wikipedia.org/wiki/Difference_in_differences)  
> Retrieved from Wikipedia, licensed under CC BY-SA 4.0.

---

Difference in differences (DID or DD) is a quasi-experimental statistical technique used in econometrics and quantitative research in the social sciences that attempts to mimic an experimental research design using observational study data by studying the differential effect of a treatment on a "treatment group" versus a "control group" in a natural experiment. It calculates the effect of a treatment (i.e., an explanatory variable or an independent variable) on an outcome (i.e., a response variable or dependent variable) by comparing the average change over time in the outcome variable for the treatment group to the average change over time for the control group. Although it is intended to mitigate the effects of extraneous factors and selection bias, depending on how the treatment group is chosen, this method may still be subject to certain biases (e.g., mean regression, reverse causality and omitted variable bias).
In contrast to a time-series estimate of the treatment effect on subjects (which analyzes differences over time) or a cross-section estimate of the treatment effect (which measures the difference between treatment and control groups), the difference in differences uses panel data to measure the differences, between the treatment and control group, of the changes in the outcome variable that occur over time.


== General definition ==

Difference in differences requires data measured from a treatment group and a control group at two or more different time periods, specifically at least one time period before "treatment" and at least one time period after "treatment". In the example pictured, the outcome in the treatment group is represented by the line P, and the outcome in the control group is represented by the line S. The outcome (dependent) variable in both groups is measured at time 1, before either group has received the treatment (i.e., the independent or explanatory variable), represented by the points P1 and S1. The treatment group then receives or experiences the treatment and both groups are again measured at time 2. Not all of the difference between the treatment and control groups at time 2 (that is, the difference between P2 and S2) can be explained as being an effect of the treatment, because the treatment group and control group did not start out at the same point at time 1. DID, therefore, calculates the "normal" difference in the outcome variable between the two groups (the difference that would still exist if neither group experienced the treatment), represented by the dotted line Q. (Notice that the slope from P1 to Q is the same as the slope from S1 to S2.) The treatment effect is the difference between the observed outcome (P2) and the "normal" outcome (the difference between P2 and Q).


== Formal definition ==
Consider the model

  
    
      
        
          y
          
            i
            t
          
        
         
        =
         
        
          γ
          
            s
            (
            i
            )
          
        
        +
        
          λ
          
            t
          
        
        +
        δ
        I
        (
        …
        )
        +
        
          ε
          
            i
            t
          
        
      
    
    {\displaystyle y_{it}~=~\gamma _{s(i)}+\lambda _{t}+\delta I(\dots )+\varepsilon _{it}}
  

where 
  
    
      
        
          y
          
            i
            t
          
        
      
    
    {\displaystyle y_{it}}
  
 is the dependent variable for individual 
  
    
      
        i
      
    
    {\displaystyle i}
  
 and time 
  
    
      
        t
      
    
    {\displaystyle t}
  
, 
  
    
      
        s
        (
        i
        )
      
    
    {\displaystyle s(i)}
  
 is the group to which 
  
    
      
        i
      
    
    {\displaystyle i}
  
 belongs (i.e. the treatment or the control group), and 
  
    
      
        I
        (
        …
        )
      
    
    {\displaystyle I(\dots )}
  
 is short-hand for the dummy variable equal to 1 when the event described in 
  
    
      
        (
        …
        )
      
    
    {\displaystyle (\dots )}
  
 is true, and 0 otherwise. In the plot of time versus 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 by group, 
  
    
      
        
          γ
          
            s
          
        
      
    
    {\displaystyle \gamma _{s}}
  
 is the vertical intercept for the graph for 
  
    
      
        s
      
    
    {\displaystyle s}
  
, and 
  
    
      
        
          λ
          
            t
          
        
      
    
    {\displaystyle \lambda _{t}}
  
 is the time trend shared by both groups according to the parallel trend assumption (see Assumptions below). 
  
    
      
        δ
      
    
    {\displaystyle \delta }
  
 is the treatment effect, and 
  
    
      
        
          ε
          
            i
            t
          
        
      
    
    {\displaystyle \varepsilon _{it}}
  
 is the residual term.
Consider the average of the dependent variable and dummy indicators by group and time:

  
    
      
        
          
            
              
                
                  n
                  
                    s
                  
                
              
              
                
                =
                
                   number of individuals in group 
                
                s
              
            
            
              
                
                  
                    
                      y
                      ¯
                    
                  
                  
                    s
                    t
                  
                
              
              
                
                =
                
                  
                    1
                    
                      n
                      
                        s
                      
                    
                  
                
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                  
                
                
                  y
                  
                    i
                    t
                  
                
                 
                I
                (
                s
                (
                i
                )
                 
                =
                 
                s
                )
                ,
              
            
            
              
                
                  
                    
                      γ
                      ¯
                    
                  
                  
                    s
                  
                
              
              
                
                =
                
                  
                    1
                    
                      n
                      
                        s
                      
                    
                  
                
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                  
                
                
                  γ
                  
                    s
                    (
                    i
                    )
                  
                
                 
                I
                (
                s
                (
                i
                )
                 
                =
                 
                s
                )
                 
                =
                 
                
                  γ
                  
                    s
                  
                
                ,
              
            
            
              
                
                  
                    
                      λ
                      ¯
                    
                  
                  
                    s
                    t
                  
                
              
              
                
                =
                
                  
                    1
                    
                      n
                      
                        s
                      
                    
                  
                
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                  
                
                
                  λ
                  
                    t
                  
                
                 
                I
                (
                s
                (
                i
                )
                 
                =
                 
                s
                )
                 
                =
                 
                
                  λ
                  
                    t
                  
                
                ,
              
            
            
              
                
                  
                    
                      I
                      ¯
                    
                  
                  
                    s
                    t
                  
                
              
              
                
                =
                
                  
                    1
                    
                      n
                      
                        s
                      
                    
                  
                
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                  
                
                I
                (
                s
                (
                i
                )
                 
                =
                 
                
                   treatment, 
                
                t
                
                   in after period
                
                )
                 
                I
                (
                s
                (
                i
                )
                 
                =
                 
                s
                )
                 
                =
                 
                I
                (
                s
                 
                =
                 
                
                   treatment, 
                
                t
                
                   in after period
                
                )
                 
                =
                 
                
                  D
                  
                    s
                    t
                  
                
                ,
              
            
            
              
                
                  
                    
                      ε
                      ¯
                    
                  
                  
                    s
                    t
                  
                
              
              
                
                =
                
                  
                    1
                    
                      n
                      
                        s
                      
                    
                  
                
                
                  ∑
                  
                    i
                    =
                    1
                  
                  
                    n
                  
                
                
                  ε
                  
                    i
                    t
                  
                
                 
                I
                (
                s
                (
                i
                )
                 
                =
                 
                s
                )
                ,
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}n_{s}&={\text{ number of individuals in group }}s\\{\overline {y}}_{st}&={\frac {1}{n_{s}}}\sum _{i=1}^{n}y_{it}\ I(s(i)~=~s),\\{\overline {\gamma }}_{s}&={\frac {1}{n_{s}}}\sum _{i=1}^{n}\gamma _{s(i)}\ I(s(i)~=~s)~=~\gamma _{s},\\{\overline {\lambda }}_{st}&={\frac {1}{n_{s}}}\sum _{i=1}^{n}\lambda _{t}\ I(s(i)~=~s)~=~\lambda _{t},\\{\overline {I}}_{st}&={\frac {1}{n_{s}}}\sum _{i=1}^{n}I(s(i)~=~{\text{ treatment, }}t{\text{ in after period}})\ I(s(i)~=~s)~=~I(s~=~{\text{ treatment, }}t{\text{ in after period}})~=~D_{st},\\{\overline {\varepsilon }}_{st}&={\frac {1}{n_{s}}}\sum _{i=1}^{n}\varepsilon _{it}\ I(s(i)~=~s),\end{aligned}}}
  

and suppose for simplicity that 
  
    
      
        s
        =
        1
        ,
        2
      
    
    {\displaystyle s=1,2}
  
 and 
  
    
      
        t
        =
        1
        ,
        2
      
    
    {\displaystyle t=1,2}
  
. Note that 
  
    
      
        
          D
          
            s
            t
          
        
      
    
    {\displaystyle D_{st}}
  
 is not random; it just encodes how the groups and the periods are labeled. Then

  
    
      
        
          
            
              
              
                
                (
                
                  
                    
                      y
                      ¯
                    
                  
                  
                    11
                  
                
                −
                
                  
                    
                      y
                      ¯
                    
                  
                  
                    12
                  
                
                )
                −
                (
                
                  
                    
                      y
                      ¯
                    
                  
                  
                    21
                  
                
                −
                
                  
                    
                      y
                      ¯
                    
                  
                  
                    22
                  
                
                )
              
            
            
              
                =
                

                
              
              
                
                
                  
                    [
                  
                
                (
                
                  γ
                  
                    1
                  
                
                +
                
                  λ
                  
                    1
                  
                
                +
                δ
                
                  D
                  
                    11
                  
                
                +
                
                  
                    
                      ε
                      ¯
                    
                  
                  
                    11
                  
                
                )
                −
                (
                
                  γ
                  
                    1
                  
                
                +
                
                  λ
                  
                    2
                  
                
                +
                δ
                
                  D
                  
                    12
                  
                
                +
                
                  
                    
                      ε
                      ¯
                    
                  
                  
                    12
                  
                
                )
                
                  
                    ]
                  
                
              
            
            
              
              
                
                
                

                
                −
                
                  
                    [
                  
                
                (
                
                  γ
                  
                    2
                  
                
                +
                
                  λ
                  
                    1
                  
                
                +
                δ
                
                  D
                  
                    21
                  
                
                +
                
                  
                    
                      ε
                      ¯
                    
                  
                  
                    21
                  
                
                )
                −
                (
                
                  γ
                  
                    2
                  
                
                +
                
                  λ
                  
                    2
                  
                
                +
                δ
                
                  D
                  
                    22
                  
                
                +
                
                  
                    
                      ε
                      ¯
                    
                  
                  
                    22
                  
                
                )
                
                  
                    ]
                  
                
              
            
            
              
                =
                

                
              
              
                δ
                (
                
                  D
                  
                    11
                  
                
                −
                
                  D
                  
                    12
                  
                
                )
                +
                δ
                (
                
                  D
                  
                    22
                  
                
                −
                
                  D
                  
                    21
                  
                
                )
                +
                
                  
                    
                      ε
                      ¯
                    
                  
                  
                    11
                  
                
                −
                
                  
                    
                      ε
                      ¯
                    
                  
                  
                    12
                  
                
                +
                
                  
                    
                      ε
                      ¯
                    
                  
                  
                    22
                  
                
                −
                
                  
                    
                      ε
                      ¯
                    
                  
                  
                    21
                  
                
                .
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}&({\overline {y}}_{11}-{\overline {y}}_{12})-({\overline {y}}_{21}-{\overline {y}}_{22})\\[6pt]={}&{\big [}(\gamma _{1}+\lambda _{1}+\delta D_{11}+{\overline {\varepsilon }}_{11})-(\gamma _{1}+\lambda _{2}+\delta D_{12}+{\overline {\varepsilon }}_{12}){\big ]}\\&\qquad {}-{\big [}(\gamma _{2}+\lambda _{1}+\delta D_{21}+{\overline {\varepsilon }}_{21})-(\gamma _{2}+\lambda _{2}+\delta D_{22}+{\overline {\varepsilon }}_{22}){\big ]}\\[6pt]={}&\delta (D_{11}-D_{12})+\delta (D_{22}-D_{21})+{\overline {\varepsilon }}_{11}-{\overline {\varepsilon }}_{12}+{\overline {\varepsilon }}_{22}-{\overline {\varepsilon }}_{21}.\end{aligned}}}
  

The strict exogeneity assumption then implies that

  
    
      
        E
        ⁡
        
          [
          
            (
            
              
                
                  y
                  ¯
                
              
              
                11
              
            
            −
            
              
                
                  y
                  ¯
                
              
              
                12
              
            
            )
            −
            (
            
              
                
                  y
                  ¯
                
              
              
                21
              
            
            −
            
              
                
                  y
                  ¯
                
              
              
                22
              
            
            )
          
          ]
        
         
        =
         
        δ
        (
        
          D
          
            11
          
        
        −
        
          D
          
            12
          
        
        )
        +
        δ
        (
        
          D
          
            22
          
        
        −
        
          D
          
            21
          
        
        )
        .
      
    
    {\displaystyle \operatorname {E} \left[({\overline {y}}_{11}-{\overline {y}}_{12})-({\overline {y}}_{21}-{\overline {y}}_{22})\right]~=~\delta (D_{11}-D_{12})+\delta (D_{22}-D_{21}).}
  

Without loss of generality, assume that 
  
    
      
        s
        =
        2
      
    
    {\displaystyle s=2}
  
 is the treatment group, and 
  
    
      
        t
        =
        2
      
    
    {\displaystyle t=2}
  
 is the after period, then 
  
    
      
        
          D
          
            22
          
        
        =
        1
      
    
    {\displaystyle D_{22}=1}
  
 and 
  
    
      
        
          D
          
            11
          
        
        =
        
          D
          
            12
          
        
        =
        
          D
          
            21
          
        
        =
        0
      
    
    {\displaystyle D_{11}=D_{12}=D_{21}=0}
  
, giving the DID estimator

  
    
      
        
          
            
              δ
              ^
            
          
        
         
        =
         
        (
        
          
            
              y
              ¯
            
          
          
            11
          
        
        −
        
          
            
              y
              ¯
            
          
          
            12
          
        
        )
        −
        (
        
          
            
              y
              ¯
            
          
          
            21
          
        
        −
        
          
            
              y
              ¯
            
          
          
            22
          
        
        )
        ,
      
    
    {\displaystyle {\hat {\delta }}~=~({\overline {y}}_{11}-{\overline {y}}_{12})-({\overline {y}}_{21}-{\overline {y}}_{22}),}
  

which can be interpreted as the treatment effect of the treatment indicated by 
  
    
      
        
          D
          
            s
            t
          
        
      
    
    {\displaystyle D_{st}}
  
. Below it is shown how this estimator can be read as a coefficient in an ordinary least squares regression. The model described in this section is over-parametrized; to remedy that, one of the coefficients for the dummy variables can be set to 0, for example, we may set 
  
    
      
        
          γ
          
            1
          
        
        =
        0
      
    
    {\displaystyle \gamma _{1}=0}
  
.


== Assumptions ==

All the Gauss–Markov assumptions of the OLS model apply equally to DID, since DID is a special version of OLS. In addition, DID requires a parallel trend assumption. The parallel trend assumption says that 
  
    
      
        
          λ
          
            2
          
        
        −
        
          λ
          
            1
          
        
      
    
    {\displaystyle \lambda _{2}-\lambda _{1}}
  
 are the same in both 
  
    
      
        s
        =
        1
      
    
    {\displaystyle s=1}
  
 and 
  
    
      
        s
        =
        2
      
    
    {\displaystyle s=2}
  
. Given that the formal definition above accurately represents reality, this assumption automatically holds. However, a model with 
  
    
      
        
          λ
          
            s
            t
          
        
        :
        
          λ
          
            22
          
        
        −
        
          λ
          
            21
          
        
        ≠
        
          λ
          
            12
          
        
        −
        
          λ
          
            11
          
        
      
    
    {\displaystyle \lambda _{st}:\lambda _{22}-\lambda _{21}\neq \lambda _{12}-\lambda _{11}}
  
 may well be more realistic. In order to increase the likelihood of the parallel trend assumption holding, a difference-in-differences approach is often combined with matching. This involves "matching" known "treatment" units with simulated counterfactual "control" units: characteristically equivalent units which did not receive treatment. By defining the outcome variable as a temporal difference (change in observed outcome between pre- and posttreatment periods), and matching multiple units in a large sample on the basis of similar pre-treatment histories, the resulting ATE (i.e. the ATT: average treatment effect for the treated) provides a robust difference-in-differences estimate of treatment effects. This serves two statistical purposes: firstly, conditional on pre-treatment covariates, the parallel trends assumption is likely to hold; and secondly, this approach reduces dependence on associated ignorability assumptions necessary for valid inference. 
As illustrated in the figure, the treatment effect is the difference between the observed value of y and what the value of y would have been with parallel trends, had there been no treatment. However, a shortcoming of DID is when something other than the treatment changes in one group but not the other at the same time as the treatment, implying a violation of the parallel trend assumption.
To guarantee the accuracy of the DID estimate, the composition of individuals of the two groups is assumed to remain unchanged over time. When using a DID model, various issues that may compromise the results, such as autocorrelation and Ashenfelter dips, must be considered and dealt with.


== Implementation ==
The DID method can be implemented according to the table below, where the lower right cell is the DID estimator.

Running a regression analysis gives the same result. Consider the OLS model

  
    
      
        y
         
        =
         
        
          β
          
            0
          
        
        +
        
          β
          
            1
          
        
        T
        +
        
          β
          
            2
          
        
        S
        +
        
          β
          
            3
          
        
        (
        T
        ⋅
        S
        )
        +
        ε
      
    
    {\displaystyle y~=~\beta _{0}+\beta _{1}T+\beta _{2}S+\beta _{3}(T\cdot S)+\varepsilon }
  

where 
  
    
      
        T
      
    
    {\displaystyle T}
  
 is a dummy variable for the period, equal to 
  
    
      
        1
      
    
    {\displaystyle 1}
  
 when 
  
    
      
        t
        =
        2
      
    
    {\displaystyle t=2}
  
, and 
  
    
      
        S
      
    
    {\displaystyle S}
  
 is a dummy variable for group membership, equal to 
  
    
      
        1
      
    
    {\displaystyle 1}
  
 when 
  
    
      
        s
        =
        2
      
    
    {\displaystyle s=2}
  
. The composite variable 
  
    
      
        (
        T
        ⋅
        S
        )
      
    
    {\displaystyle (T\cdot S)}
  
 is a dummy variable indicating when 
  
    
      
        S
        =
        T
        =
        1
      
    
    {\displaystyle S=T=1}
  
. Although it is not shown rigorously here, this is a proper parametrization of the model formal definition, furthermore, it turns out that the group and period averages in that section relate to the model parameter estimates as follows

  
    
      
        
          
            
              
                
                  
                    
                      
                        β
                        ^
                      
                    
                  
                  
                    0
                  
                
              
              
                
                =
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                T
                =
                0
                ,
                 
                S
                =
                0
                )
              
            
            
              
                
                  
                    
                      
                        β
                        ^
                      
                    
                  
                  
                    1
                  
                
              
              
                
                =
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                T
                =
                1
                ,
                 
                S
                =
                0
                )
                −
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                T
                =
                0
                ,
                 
                S
                =
                0
                )
              
            
            
              
                
                  
                    
                      
                        β
                        ^
                      
                    
                  
                  
                    2
                  
                
              
              
                
                =
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                T
                =
                0
                ,
                 
                S
                =
                1
                )
                −
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                T
                =
                0
                ,
                 
                S
                =
                0
                )
              
            
            
              
                
                  
                    
                      
                        β
                        ^
                      
                    
                  
                  
                    3
                  
                
              
              
                
                =
                
                  
                    [
                  
                
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                T
                =
                1
                ,
                 
                S
                =
                1
                )
                −
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                T
                =
                0
                ,
                 
                S
                =
                1
                )
                
                  
                    ]
                  
                
              
            
            
              
              
                
                
                

                
                −
                
                  
                    [
                  
                
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                T
                =
                1
                ,
                 
                S
                =
                0
                )
                −
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                T
                =
                0
                ,
                 
                S
                =
                0
                )
                
                  
                    ]
                  
                
                ,
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\hat {\beta }}_{0}&={\widehat {E}}(y\mid T=0,~S=0)\\[8pt]{\hat {\beta }}_{1}&={\widehat {E}}(y\mid T=1,~S=0)-{\widehat {E}}(y\mid T=0,~S=0)\\[8pt]{\hat {\beta }}_{2}&={\widehat {E}}(y\mid T=0,~S=1)-{\widehat {E}}(y\mid T=0,~S=0)\\[8pt]{\hat {\beta }}_{3}&={\big [}{\widehat {E}}(y\mid T=1,~S=1)-{\widehat {E}}(y\mid T=0,~S=1){\big ]}\\&\qquad {}-{\big [}{\widehat {E}}(y\mid T=1,~S=0)-{\widehat {E}}(y\mid T=0,~S=0){\big ]},\end{aligned}}}
  

where 
  
    
      
        
          
            
              E
              ^
            
          
        
        (
        ⋯
        ∣
        …
        )
      
    
    {\displaystyle {\widehat {E}}(\dots \mid \dots )}
  
 stands for conditional averages computed on the sample, for example, 
  
    
      
        T
        =
        1
      
    
    {\displaystyle T=1}
  
 is the indicator for the after period, 
  
    
      
        S
        =
        0
      
    
    {\displaystyle S=0}
  
 is an indicator for the control group. Note that 
  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            1
          
        
      
    
    {\displaystyle {\hat {\beta }}_{1}}
  
 is an estimate of the counterfactual rather than the impact of the control group. The control group is often used as a proxy for the counterfactual (see, Synthetic control method for a deeper understanding of this point). Thereby, 
  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            1
          
        
      
    
    {\displaystyle {\hat {\beta }}_{1}}
  
 can be interpreted as the impact of both the control group and the intervention's (treatment's) counterfactual. Similarly, 
  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            2
          
        
      
    
    {\displaystyle {\hat {\beta }}_{2}}
  
, due to the parallel trend assumption, is also the same differential between the treatment and control group in 
  
    
      
        T
        =
        1
      
    
    {\displaystyle T=1}
  
. The above descriptions should not be construed to imply the (average) effect of only  the control group, for 
  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            1
          
        
      
    
    {\displaystyle {\hat {\beta }}_{1}}
  
, or only the difference of the treatment and control groups in the pre-period, for 
  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            2
          
        
      
    
    {\displaystyle {\hat {\beta }}_{2}}
  
. As in Card and Krueger, below, a first (time) difference of the outcome variable 
  
    
      
        (
        Δ
        
          Y
          
            i
          
        
        =
        
          Y
          
            i
            ,
            1
          
        
        −
        
          Y
          
            i
            ,
            0
          
        
        )
      
    
    {\displaystyle (\Delta Y_{i}=Y_{i,1}-Y_{i,0})}
  
 eliminates the need for time-trend (i.e., 
  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            1
          
        
      
    
    {\displaystyle {\hat {\beta }}_{1}}
  
) to form an unbiased estimate of 
  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            3
          
        
      
    
    {\displaystyle {\hat {\beta }}_{3}}
  
, implying that 
  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            1
          
        
      
    
    {\displaystyle {\hat {\beta }}_{1}}
  
 is not actually conditional on the treatment or control group. Consistently, a difference among the treatment and control groups would eliminate the need for treatment differentials (i.e., 
  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            2
          
        
      
    
    {\displaystyle {\hat {\beta }}_{2}}
  
) to form an unbiased estimate of 
  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            3
          
        
      
    
    {\displaystyle {\hat {\beta }}_{3}}
  
. This nuance is important to understand when the user believes (weak) violations of parallel pre-trend exist or in the case of violations of the appropriate counterfactual approximation assumptions given the existence of non-common shocks or confounding events.  To see the relation between this notation and the previous section, consider as above only one observation per time period for each group, then

  
    
      
        
          
            
              
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                T
                =
                1
                ,
                 
                S
                =
                0
                )
              
              
                
                =
                
                  
                    
                      E
                      ^
                    
                  
                
                (
                y
                ∣
                
                   after period, control
                
                )
              
            
            
              
            
            
              
              
                
                =
                
                  
                    
                      
                        
                          
                            E
                            ^
                          
                        
                      
                      (
                      y
                       
                      I
                      (
                      
                         after period, control
                      
                      )
                      )
                    
                    
                      
                        
                          
                            P
                            ^
                          
                        
                      
                      (
                      
                         after period, control
                      
                      )
                    
                  
                
              
            
            
              
            
            
              
              
                
                =
                
                  
                    
                      
                        ∑
                        
                          i
                          =
                          1
                        
                        
                          n
                        
                      
                      
                        y
                        
                          i
                          ,
                          
                            after
                          
                        
                      
                      I
                      (
                      i
                      
                         in control
                      
                      )
                    
                    
                      n
                      
                        control
                      
                    
                  
                
                =
                
                  
                    
                      y
                      ¯
                    
                  
                  
                    control, after
                  
                
              
            
            
              
            
            
              
              
                
                =
                
                  
                    
                      y
                      ¯
                    
                  
                  
                    12
                  
                
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\widehat {E}}(y\mid T=1,~S=0)&={\widehat {E}}(y\mid {\text{ after period, control}})\\[3pt]\\&={\frac {{\widehat {E}}(y\ I({\text{ after period, control}}))}{{\widehat {P}}({\text{ after period, control}})}}\\[3pt]\\&={\frac {\sum _{i=1}^{n}y_{i,{\text{after}}}I(i{\text{ in control}})}{n_{\text{control}}}}={\overline {y}}_{\text{control, after}}\\[3pt]\\&={\overline {y}}_{\text{12}}\end{aligned}}}
  

and so on for other values of 
  
    
      
        T
      
    
    {\displaystyle T}
  
 and 
  
    
      
        S
      
    
    {\displaystyle S}
  
, which is equivalent to

  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            3
          
        
         
        =
         
        (
        
          y
          
            11
          
        
        −
        
          y
          
            21
          
        
        )
        −
        (
        
          y
          
            12
          
        
        −
        
          y
          
            22
          
        
        )
        .
      
    
    {\displaystyle {\hat {\beta }}_{3}~=~(y_{11}-y_{21})-(y_{12}-y_{22}).}
  

But this is the expression for the treatment effect that was given in the formal definition and in the above table.
Variants of difference-in-difference frameworks include ones for staggered implementation of treatment as well as an estimator introduced for multiple time periods and other variations by Brantly Callaway and Pedro H.C. Sant'Anna.


== Example ==
The Card and Krueger article on minimum wage in New Jersey, published in 1994, is considered one of the most famous DID studies; Card was later awarded the 2021 Nobel Memorial Prize in Economic Sciences in part for this and related work. Card and Krueger compared employment in the fast food sector in New Jersey and in Pennsylvania, in February 1992 and in November 1992, after New Jersey's minimum wage rose from $4.25 to $5.05 in April 1992. Observing a change in employment in New Jersey only, before and after the treatment, would fail to control for omitted variables such as weather and macroeconomic conditions of the region. By including Pennsylvania as a control in a difference-in-differences model, any bias caused by variables common to New Jersey and Pennsylvania is implicitly controlled for, even when these variables are unobserved. Assuming that New Jersey and Pennsylvania have parallel trends over time, Pennsylvania's change in employment can be interpreted as the change New Jersey would have experienced, had they not increased the minimum wage, and vice versa. The evidence suggested that the increased minimum wage did not induce a decrease in employment in New Jersey, contrary to what some economic theory would suggest. The table below shows Card & Krueger's estimates of the treatment effect on employment, measured as FTEs (or full-time equivalents). Card and Krueger estimate that the $0.80 minimum wage increase in New Jersey led to an average 2.75 FTE increase in employment per store.

A software example application of this research is found on the Stata's command -diff- 


== Applications ==
The difference-in-differences (DID) framework has been applied widely beyond labor economics and minimum wage studies. 
In public health, DID has been used to evaluate the effect of new medical guidelines or vaccination campaigns by comparing 
regions before and after policy implementation. 
In education, DID methods help measure the impact of reforms such as changes in school funding or class size. 
In environmental economics, they are used to assess regulations on pollution, energy consumption, or climate policy. 
These applications rely on the key assumption of parallel trends, but when carefully designed, they provide policymakers with 
robust causal estimates using observational data.


=== In economic history ===
Difference-in-differences has also been applied to the study of historical events, particularly in the field of economic history, where researchers rely on natural experiments to investigate long-run outcomes. By comparing regions or groups that were differentially exposed to shocks such as disease, institutional change, or wartime destruction, scholars have used the method to identify causal effects that cannot be observed directly.
In 2021, Elena Esposito used DID to examine how the arrival of malaria influenced the expansion of African slavery in the United States.
She compared counties that were more ecologically suitable for malaria transmission with those that were less suitable, before and after the introduction of the disease in the late seventeenth century. Results showed that malaria-prone counties experienced a much greater increase in the share of enslaved Africans after the disease became endemic. In addition, enslaved individuals from parts of Africa with high malaria prevalence sold at higher prices in Louisiana slave markets, suggesting that buyers placed a premium on resistance to malaria. This application demonstrated how DID can be used to link environmental shocks with institutional development over the long run.
González, Marshall, and Naidu in 2017 used DID to analyze how the abolition of slavery in Maryland affected patterns of entrepreneurship. They combined census data with contemporary credit reports to compare business formation by slaveowners and non-slaveowners before and after the uncompensated abolition of slavery in 1864. They found that slaveowners were more likely to start businesses before emancipation, but this advantage disappeared once slavery was abolished.In this case, DID made it possible to treat emancipation as a sudden institutional change and to see how it affected business activity.
In 2022, James Feigenbaum, James Lee, and Filippo Mezzanotti used DID to measure the economic effects of General Sherman’s March during the American Civil War. Using county-level data from 1850 to 1920, they compared areas directly in the path of the march with nearby counties that were spared. Their findings showed large and immediate declines in farm values, agricultural investment, and manufacturing activity in the affected counties. While manufacturing output eventually recovered by the late nineteenth century, agricultural effects lasted for decades, with lower levels of improved farmland still evident in 1920. The study also showed that the lack of credit and the collapse of banks after the Civil War slowed down the recovery, especially in places that relied more on borrowing. Overall, the study used DID to demonstrate that conflict had lasting effects on the economy and local institutions.
In 2012, Richard Hornbeck used DID to study the long-term economic consequences of the American Dust Bowl of the 1930s. He compared counties that experienced severe soil erosion with nearby counties that were less affected, before and after the disaster. His findings show that heavily eroded counties suffered persistent declines in land values and agricultural revenues of 20 to 30 percent, with little recovery even 10 years later. Many residents migrated away as a result, and population decline became the primary adjustment. This work demonstrates how DID can be applied to environmental shocks in economic history, pointing out  the long run effects of ecological disasters on regional development.


== See also ==
Design of experiments
Average treatment effect
Synthetic control method


== References ==


== Further reading ==
Angrist, J. D.; Pischke, J. S. (2008). Mostly Harmless Econometrics: An Empiricist's Companion. Princeton University Press. pp. 227–243. ISBN 978-0-691-12034-8.
Andrew Baker, Brantly Callaway, Scott Cunningham, Andrew Goodman-Bacon and Pedro H. C. Sant'Anna. 2025. "Difference-in-Differences Designs: A Practitioner’s Guide." Journal of Economic Literature.
Cameron, Arthur C.; Trivedi, Pravin K. (2005). Microeconometrics: Methods and Applications. Cambridge university press. pp. 768–772. doi:10.1017/CBO9780511811241. ISBN 9780521848053. S2CID 120313863.
Imbens, Guido W.; Wooldridge, Jeffrey M. (2009). "Recent Developments in the Econometrics of Program Evaluation". Journal of Economic Literature. 47 (1): 5–86. doi:10.1257/jel.47.1.5.
Bakija, Jon; Heim, Bradley (August 2008). "How Does Charitable Giving Respond to Incentives and Income? Dynamic Panel Estimates Accounting for Predictable Changes in Taxation". NBER Working Paper No. 14237. doi:10.3386/w14237.
Conley, T.; Taber, C. (July 2005). "Inference with 'Difference in Differences' with a Small Number of Policy Changes". NBER Technical Working Paper No. 312. doi:10.3386/t0312.


== External links ==
Difference in Difference Estimation, Healthcare Economist website