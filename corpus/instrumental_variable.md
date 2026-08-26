# Instrumental variables

> Source: [https://en.wikipedia.org/wiki/Instrumental_variables](https://en.wikipedia.org/wiki/Instrumental_variables)  
> Retrieved from Wikipedia, licensed under CC BY-SA 4.0.

---

In statistics, econometrics, epidemiology and related disciplines, the quasi-experimental method of instrumental variables (IV) is used to estimate causal relationships when controlled experiments are not feasible or when a treatment is not successfully delivered to every unit in a randomized experiment. Intuitively, IVs are used when an explanatory (also known as independent or predictor) variable of interest is correlated with the error term (endogenous), in which case ordinary least squares and ANOVA give biased results. When used, a valid instrument changes the explanatory variable (the variable correlated with the endogenous variable) but has no independent effect on the dependent variable and is not correlated with the error term, thus allowing a researcher or analyst to uncover the true causal effect of the explanatory variable on the dependent variable.
Instrumental variable methods allow for consistent estimation when the explanatory variables (covariates) are correlated with the error terms in a regression model. Such correlation may occur when:

changes in the dependent variable change the value of at least one of the covariates ("reverse" causation),
there are omitted variables that affect both the dependent and explanatory variables, or
the covariates are subject to measurement error.
Explanatory variables that suffer from one or more of these issues in the context of a regression are sometimes referred to as endogenous. In this situation, ordinary least squares produces biased and inconsistent estimates. However, if an instrument is available, consistent estimates may still be obtained. An instrument is a variable that does not itself belong in the explanatory equation but is correlated with the endogenous explanatory variables, conditionally on the value of other covariates.
In linear models, there are two main requirements for using IVs:

The instrument must be correlated with the endogenous explanatory variables, conditionally on the other covariates. If this correlation is strong, then the instrument is said to have a strong first stage. A weak correlation may provide misleading inferences about parameter estimates and cause the standard errors in the second stage to be larger than the ordinary least squares estimates.
The instrument cannot be correlated with the error term in the explanatory equation, conditionally on the other covariates. In other words, the instrument cannot suffer from the same problem as the original predicting variable. If this condition is met, then the instrument is said to satisfy the exclusion restriction.


== Example ==
Informally, in attempting to estimate the causal effect of some variable X ("covariate" or "explanatory variable") on another Y ("dependent variable"), an instrument is a third variable Z which affects Y only through its effect on X.  
For example, suppose a researcher wishes to estimate the causal effect of smoking (X) on general health (Y).  Correlation between smoking and health does not imply that smoking causes poor health because other variables, such as depression, may affect both health and smoking, or because health may affect smoking.  It is not possible to conduct controlled experiments on smoking status in the general population.  The researcher may attempt to estimate the causal effect of smoking on health from observational data by using the tax rate for tobacco products (Z) as an instrument for smoking.  The tax rate for tobacco products is a reasonable choice for an instrument because the researcher assumes that it can only be correlated with health through its effect on smoking.  If the researcher then finds tobacco taxes and state of health to be correlated, this may be viewed as evidence that smoking causes changes in health.


== History ==
The first use of an instrument variable occurred in a 1928 book by Philip G. Wright, best known for his excellent description of the production, transport and sale of vegetable and animal oils in the early 1900s in the United States. In 1945, Olav Reiersøl applied the same approach in the context of errors-in-variables models in his dissertation, giving the method its name.
Wright attempted to determine the supply and demand for butter using panel data on prices and quantities sold in the United States. The idea was that a regression analysis could produce a demand or supply curve because they are formed by the path between prices and quantities demanded or supplied. The problem was that the observational data did not form a demand or supply curve as such, but rather a cloud of point observations that took different shapes under varying market conditions. It seemed that making deductions from the data remained elusive.
The problem was that price affected both supply and demand so that a function describing only one of the two could not be constructed directly from the observational data. Wright correctly concluded that he needed a variable that correlated with either demand or supply but not both – that is, an instrumental variable.
After much deliberation, Wright decided to use regional rainfall as his instrumental variable: he concluded that rainfall affected grass production and hence milk production and ultimately butter supply, but not butter demand. In this way he was able to construct a regression equation with only the instrumental variable of price and supply.
Formal definitions of instrumental variables, using counterfactuals and graphical criteria, were given by Judea Pearl in 2000.  Angrist and Krueger (2001) present a survey of the history and uses of instrumental variable techniques. Notions of causality in econometrics, and their relationship with instrumental variables and other methods, are discussed by Heckman (2008).


== Theory ==
While the ideas behind IV extend to a broad class of models, a very common context for IV is in linear regression. Traditionally, an instrumental variable is defined
as a variable 
  
    
      
        Z
      
    
    {\displaystyle Z}
  
 that is correlated with the independent variable 

  
    
      
        X
      
    
    {\displaystyle X}
  
 and uncorrelated with the "error term" 
  
    
      
        U
      
    
    {\displaystyle U}
  
 in the linear equation

  
    
      
        Y
        =
        X
        β
        +
        U
      
    
    {\displaystyle Y=X\beta +U}
  

  
    
      
        Y
      
    
    {\displaystyle Y}
  
 is a vector. 
  
    
      
        X
      
    
    {\displaystyle X}
  
 is a matrix, usually with a column of ones and perhaps with additional columns for other covariates. Consider how an instrument allows 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 to be recovered. Recall that OLS solves for 
  
    
      
        
          
            
              β
              ^
            
          
        
      
    
    {\displaystyle {\widehat {\beta }}}
  
 such that 
  
    
      
        cov
        ⁡
        (
        X
        ,
        
          
            
              U
              ^
            
          
        
        )
        =
        0
      
    
    {\displaystyle \operatorname {cov} (X,{\widehat {U}})=0}
  
 (when we minimize the sum of squared errors, 
  
    
      
        
          min
          
            β
          
        
        (
        Y
        −
        X
        β
        
          )
          ′
        
        (
        Y
        −
        X
        β
        )
      
    
    {\displaystyle \min _{\beta }(Y-X\beta )'(Y-X\beta )}
  
, the first-order condition is exactly 
  
    
      
        
          X
          ′
        
        (
        Y
        −
        X
        
          
            
              β
              ^
            
          
        
        )
        =
        
          X
          ′
        
        
          
            
              U
              ^
            
          
        
        =
        0
      
    
    {\displaystyle X'(Y-X{\widehat {\beta }})=X'{\widehat {U}}=0}
  
). If the true model is believed to have 
  
    
      
        cov
        ⁡
        (
        X
        ,
        U
        )
        ≠
        0
      
    
    {\displaystyle \operatorname {cov} (X,U)\neq 0}
  
 due to any of the reasons listed above—for example, if there is an omitted variable which affects both 
  
    
      
        X
      
    
    {\displaystyle X}
  
 and 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 separately—then this OLS procedure will not yield the causal impact of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 on 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
. OLS will simply pick the parameter that makes the resulting errors appear uncorrelated with 
  
    
      
        X
      
    
    {\displaystyle X}
  
.
Consider for simplicity the single-variable case. Suppose we are considering a regression with one variable and a constant (perhaps no other covariates are necessary, or perhaps we have partialed out any other relevant covariates):

  
    
      
        y
        =
        α
        +
        β
        x
        +
        u
      
    
    {\displaystyle y=\alpha +\beta x+u}
  

In this case, the coefficient on the regressor of interest is given by 
  
    
      
        
          
            
              β
              ^
            
          
        
        =
        
          
            
              cov
              ⁡
              (
              x
              ,
              y
              )
            
            
              var
              ⁡
              (
              x
              )
            
          
        
      
    
    {\displaystyle {\widehat {\beta }}={\frac {\operatorname {cov} (x,y)}{\operatorname {var} (x)}}}
  
. Substituting for 
  
    
      
        y
      
    
    {\displaystyle y}
  
 gives

  
    
      
        
          
            
              
                
                  
                    
                      β
                      ^
                    
                  
                
              
              
                
                =
                
                  
                    
                      cov
                      ⁡
                      (
                      x
                      ,
                      y
                      )
                    
                    
                      var
                      ⁡
                      (
                      x
                      )
                    
                  
                
                =
                
                  
                    
                      cov
                      ⁡
                      (
                      x
                      ,
                      α
                      +
                      β
                      x
                      +
                      u
                      )
                    
                    
                      var
                      ⁡
                      (
                      x
                      )
                    
                  
                
              
            
            
              
              
                
                =
                
                  
                    
                      cov
                      ⁡
                      (
                      x
                      ,
                      α
                      +
                      β
                      x
                      )
                    
                    
                      var
                      ⁡
                      (
                      x
                      )
                    
                  
                
                +
                
                  
                    
                      cov
                      ⁡
                      (
                      x
                      ,
                      u
                      )
                    
                    
                      var
                      ⁡
                      (
                      x
                      )
                    
                  
                
                =
                
                  β
                  
                    ∗
                  
                
                +
                
                  
                    
                      cov
                      ⁡
                      (
                      x
                      ,
                      u
                      )
                    
                    
                      var
                      ⁡
                      (
                      x
                      )
                    
                  
                
                ,
              
            
          
        
      
    
    {\displaystyle {\begin{aligned}{\widehat {\beta }}&={\frac {\operatorname {cov} (x,y)}{\operatorname {var} (x)}}={\frac {\operatorname {cov} (x,\alpha +\beta x+u)}{\operatorname {var} (x)}}\\[6pt]&={\frac {\operatorname {cov} (x,\alpha +\beta x)}{\operatorname {var} (x)}}+{\frac {\operatorname {cov} (x,u)}{\operatorname {var} (x)}}=\beta ^{*}+{\frac {\operatorname {cov} (x,u)}{\operatorname {var} (x)}},\end{aligned}}}
  

where 
  
    
      
        
          β
          
            ∗
          
        
      
    
    {\displaystyle \beta ^{*}}
  
 is what the estimated coefficient vector would be if 

  
    
      
        cov
        ⁡
        (
        x
        ,
        u
        )
        =
        0
      
    
    {\displaystyle \operatorname {cov} (x,u)=0}
  
. In this case, it can be shown that 
  
    
      
        
          β
          
            ∗
          
        
      
    
    {\displaystyle \beta ^{*}}
  
 is an unbiased estimator of 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
.
If 
  
    
      
        cov
        ⁡
        (
        x
        ,
        u
        )
        ≠
        0
      
    
    {\displaystyle \operatorname {cov} (x,u)\neq 0}
  
 in the underlying model that we believe, then OLS gives an inconsistent estimate which does not reflect the underlying causal effect of interest. IV helps to fix this problem by identifying the parameters 
  
    
      
        
          β
        
      
    
    {\displaystyle {\beta }}
  
 not based on whether 
  
    
      
        x
      
    
    {\displaystyle x}
  
 is uncorrelated with 
  
    
      
        u
      
    
    {\displaystyle u}
  
, but based on whether another variable 
  
    
      
        z
      
    
    {\displaystyle z}
  
 is uncorrelated with 
  
    
      
        u
      
    
    {\displaystyle u}
  
. If theory suggests that 
  
    
      
        z
      
    
    {\displaystyle z}
  
 is related to 
  
    
      
        x
      
    
    {\displaystyle x}
  
 (the first stage) but uncorrelated with 
  
    
      
        u
      
    
    {\displaystyle u}
  
 (the exclusion restriction), then IV may identify the causal parameter of interest where OLS fails. Because there are multiple specific ways of using and deriving IV estimators even in just the linear case (IV, 2SLS, GMM), we save further discussion for the Estimation section below.


== Graphical definition ==
IV techniques have been developed among a much broader class of non-linear models. General definitions of instrumental variables, using counterfactual and graphical formalism, were given by Pearl (2000; p. 248). The graphical definition requires that Z satisfy the following conditions:

  
    
      
        (
        Z
        ⊥
        
        
        
        ⊥
        Y
        
          )
          
            
              G
              
                
                  X
                  ¯
                
              
            
          
        
        
        (
        Z
        
          
            ⧸
          
        
        
        
        
          ⊥
          
          
          
          ⊥
        
        X
        
          )
          
            G
          
        
      
    
    {\displaystyle (Z\perp \!\!\!\perp Y)_{G_{\overline {X}}}\qquad (Z\not \!\!{\perp \!\!\!\perp }X)_{G}}
  

where 
  
    
      
        ⊥
        
        
        
        ⊥
      
    
    {\displaystyle \perp \!\!\!\perp }
  
 stands for d-separation and 
  
    
      
        
          G
          
            
              X
              ¯
            
          
        
      
    
    {\displaystyle G_{\overline {X}}}
  
 stands for the graph in which all arrows entering X are cut off.
The counterfactual definition requires that Z satisfies

  
    
      
        (
        Z
        ⊥
        
        
        
        ⊥
        
          Y
          
            x
          
        
        )
        
        (
        Z
        
          
            ⧸
          
        
        
        
        
          ⊥
          
          
          
          ⊥
        
        X
        )
      
    
    {\displaystyle (Z\perp \!\!\!\perp Y_{x})\qquad (Z\not \!\!{\perp \!\!\!\perp }X)}
  

where Yx stands for the value that Y would attain had X been x and 
  
    
      
        ⊥
        
        
        
        ⊥
      
    
    {\displaystyle \perp \!\!\!\perp }
  
 stands for independence.
If there are additional covariates W then the above definitions are modified so that Z qualifies as an instrument if the given criteria hold conditional on W.
The essence of Pearl's definition is:

The equations of interest are "structural", not "regression".
The error term U stands for all exogenous factors that affect Y when X is held constant.
The instrument Z should be independent of U.
The instrument Z should not affect Y when X is held constant (exclusion restriction).
The instrument Z should not be independent of X.
These conditions do not rely on specific functional
form of the equations and are applicable therefore to
nonlinear equations, where U can be non-additive
(see Non-parametric analysis). They are also applicable to a system of multiple
equations, in which X (and other factors) affect Y through
several intermediate variables. An instrumental variable need not be
a cause of X; a proxy of such cause may also be
used, if it satisfies conditions 1–5. The exclusion restriction (condition 4) is redundant; it follows from conditions 2 and 3.


=== Selecting suitable instruments ===
Since U is unobserved, the requirement that Z be independent of U cannot be inferred from data and must instead be determined from the model structure, i.e., the data-generating process. Causal graphs are a representation of this structure, and the graphical definition given above can be used to quickly determine whether a variable Z qualifies as an instrumental variable given a set of covariates W. To see how, consider the following example.
Suppose that we wish to estimate the effect of a university tutoring program on grade point average (GPA).  The relationship between attending the tutoring program and GPA may be confounded by a number of factors.  Students who attend the tutoring program may care more about their grades or may be struggling with their work.  This confounding is depicted in the Figures 1–3 on the right through the bidirected arc between Tutoring Program and GPA.  If students are assigned to dormitories at random, the proximity of the student's dorm to the tutoring program is a natural candidate for being an instrumental variable.

However, what if the tutoring program is located in the college library?  In that case, Proximity may also cause students to spend more time at the library, which in turn improves their GPA (see Figure 1).  Using the causal graph depicted in the Figure 2, we see that Proximity does not qualify as an instrumental variable because it is connected to GPA through the path Proximity 
  
    
      
        →
      
    
    {\displaystyle \rightarrow }
  
 Library Hours 
  
    
      
        →
      
    
    {\displaystyle \rightarrow }
  
  GPA in 
  
    
      
        
          G
          
            
              X
              ¯
            
          
        
      
    
    {\displaystyle G_{\overline {X}}}
  
.  However, if we control for Library Hours by adding it as a covariate then Proximity becomes an instrumental variable, since Proximity is separated from GPA given Library Hours in 
  
    
      
        
          G
          
            
              X
              ¯
            
          
        
      
    
    {\displaystyle G_{\overline {X}}}
  
.
Now, suppose that we notice that a student's "natural ability" affects his or her number of hours in the library as well as his or her GPA, as in Figure 3.  Using the causal graph, we see that Library Hours is a collider and conditioning on it opens the path Proximity 
  
    
      
        →
      
    
    {\displaystyle \rightarrow }
  
 Library Hours 
  
    
      
        ↔
      
    
    {\displaystyle \leftrightarrow }
  
 GPA.  As a result, Proximity cannot be used as an instrumental variable.
Finally, suppose that Library Hours does not actually affect GPA because students who do not study in the library simply study elsewhere, as in Figure 4.  In this case, controlling for Library Hours still opens a spurious path from Proximity to GPA.  However, if we do not control for Library Hours and remove it as a covariate then Proximity can again be used an instrumental variable.


== Estimation ==
We now revisit and expand upon the mechanics of IV in greater detail. Suppose the data are generated by a process of the form

  
    
      
        
          y
          
            i
          
        
        =
        
          X
          
            i
          
        
        β
        +
        
          e
          
            i
          
        
        ,
      
    
    {\displaystyle y_{i}=X_{i}\beta +e_{i},}
  

where

i indexes observations,

  
    
      
        
          y
          
            i
          
        
      
    
    {\displaystyle y_{i}}
  
 is the i-th value of the dependent variable,

  
    
      
        
          X
          
            i
          
        
      
    
    {\displaystyle X_{i}}
  
 is a vector of the i-th values of the independent variable(s) and a constant,

  
    
      
        
          e
          
            i
          
        
      
    
    {\displaystyle e_{i}}
  
 is the i-th value of an unobserved error term representing all causes of 
  
    
      
        
          y
          
            i
          
        
      
    
    {\displaystyle y_{i}}
  
 other than 
  
    
      
        
          X
          
            i
          
        
      
    
    {\displaystyle X_{i}}
  
, and

  
    
      
        β
      
    
    {\displaystyle \beta }
  
 is an unobserved parameter vector.
The parameter vector 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 is the causal effect on 
  
    
      
        
          y
          
            i
          
        
      
    
    {\displaystyle y_{i}}
  
 of a one unit change in each element of 
  
    
      
        
          X
          
            i
          
        
      
    
    {\displaystyle X_{i}}
  
, holding all other causes of 
  
    
      
        
          y
          
            i
          
        
      
    
    {\displaystyle y_{i}}
  
 constant.  The econometric goal is to estimate 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
.  For simplicity's sake assume the draws of e are uncorrelated and that they are drawn from distributions with the same variance (that is, that the errors are serially uncorrelated and homoskedastic).
Suppose also that a regression model of nominally the same form is proposed.  Given a random sample of T observations from this process, the ordinary least squares estimator is

  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            
              O
              L
              S
            
          
        
        =
        (
        
          X
          
            
              T
            
          
        
        X
        
          )
          
            −
            1
          
        
        
          X
          
            
              T
            
          
        
        y
        =
        (
        
          X
          
            
              T
            
          
        
        X
        
          )
          
            −
            1
          
        
        
          X
          
            
              T
            
          
        
        (
        X
        β
        +
        e
        )
        =
        β
        +
        (
        
          X
          
            
              T
            
          
        
        X
        
          )
          
            −
            1
          
        
        
          X
          
            
              T
            
          
        
        e
      
    
    {\displaystyle {\widehat {\beta }}_{\mathrm {OLS} }=(X^{\mathrm {T} }X)^{-1}X^{\mathrm {T} }y=(X^{\mathrm {T} }X)^{-1}X^{\mathrm {T} }(X\beta +e)=\beta +(X^{\mathrm {T} }X)^{-1}X^{\mathrm {T} }e}
  

where X, y and e denote column vectors of length T. This equation is similar to the equation involving 
  
    
      
        cov
        ⁡
        (
        X
        ,
        y
        )
      
    
    {\displaystyle \operatorname {cov} (X,y)}
  
 in the introduction (this is the matrix version of that equation). When X and e are uncorrelated, under certain regularity conditions the second term has an expected value conditional on X of zero and converges to zero in the limit, so the estimator is unbiased and consistent.  When X and the other unmeasured, causal variables collapsed into the e term are correlated, however, the OLS estimator is generally biased and inconsistent for β.  In this case, it is valid to use the estimates to predict values of y given values of X, but the estimate does not recover the causal effect of X on y.
To recover the underlying parameter 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
, we introduce a set of variables Z that is highly correlated with each endogenous component of X but (in our underlying model) is not correlated with e. For simplicity, one might consider X to be a T × 2  matrix composed of a column of constants and one endogenous variable, and Z to be a T × 2 consisting of a column of constants and one instrumental variable. However, this technique generalizes to X being a matrix of a constant and, say, 5 endogenous variables, with Z being a matrix composed of a constant and 5 instruments. In the discussion that follows, we will assume that X is a T × K matrix and leave this value K unspecified. An estimator in which X and Z are both T × K matrices is referred to as just-identified .
Suppose that the relationship between each endogenous component xi and the instruments is given by

  
    
      
        
          x
          
            i
          
        
        =
        
          Z
          
            i
          
        
        γ
        +
        
          v
          
            i
          
        
        ,
      
    
    {\displaystyle x_{i}=Z_{i}\gamma +v_{i},}
  

The most common IV specification uses the following estimator:

  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            
              I
              V
            
          
        
        =
        (
        
          Z
          
            
              T
            
          
        
        X
        
          )
          
            −
            1
          
        
        
          Z
          
            
              T
            
          
        
        y
      
    
    {\displaystyle {\widehat {\beta }}_{\mathrm {IV} }=(Z^{\mathrm {T} }X)^{-1}Z^{\mathrm {T} }y}
  

This specification approaches the true parameter as the sample gets large, so long as 
  
    
      
        
          Z
          
            
              T
            
          
        
        e
        =
        0
      
    
    {\displaystyle Z^{\mathrm {T} }e=0}
  
 in the true model:

  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            
              I
              V
            
          
        
        =
        (
        
          Z
          
            
              T
            
          
        
        X
        
          )
          
            −
            1
          
        
        
          Z
          
            
              T
            
          
        
        y
        =
        (
        
          Z
          
            
              T
            
          
        
        X
        
          )
          
            −
            1
          
        
        
          Z
          
            
              T
            
          
        
        X
        β
        +
        (
        
          Z
          
            
              T
            
          
        
        X
        
          )
          
            −
            1
          
        
        
          Z
          
            
              T
            
          
        
        e
        →
        β
      
    
    {\displaystyle {\widehat {\beta }}_{\mathrm {IV} }=(Z^{\mathrm {T} }X)^{-1}Z^{\mathrm {T} }y=(Z^{\mathrm {T} }X)^{-1}Z^{\mathrm {T} }X\beta +(Z^{\mathrm {T} }X)^{-1}Z^{\mathrm {T} }e\rightarrow \beta }
  

As long as 
  
    
      
        
          Z
          
            
              T
            
          
        
        e
        =
        0
      
    
    {\displaystyle Z^{\mathrm {T} }e=0}
  
 in the underlying process which generates the data, the appropriate use of the IV estimator will identify this parameter. This works because IV solves for the unique parameter that satisfies 
  
    
      
        
          Z
          
            
              T
            
          
        
        e
        =
        0
      
    
    {\displaystyle Z^{\mathrm {T} }e=0}
  
, and therefore hones in on the true underlying parameter as the sample size grows.
Now an extension: suppose that there are more instruments than there are covariates in the equation of interest, so that Z is a T × M matrix with M > K. This is often called the over-identified case. In this case, the generalized method of moments (GMM) can be used. The GMM IV estimator is

  
    
      
        
          
            
              
                β
                ^
              
            
          
          
            
              G
              M
              M
            
          
        
        =
        (
        
          X
          
            
              T
            
          
        
        
          P
          
            Z
          
        
        X
        
          )
          
            −
            1
          
        
        
          X
          
            
              T
            
          
        
        
          P
          
            Z
          
        
        y
        ,
      
    
    {\displaystyle {\widehat {\beta }}_{\mathrm {GMM} }=(X^{\mathrm {T} }P_{Z}X)^{-1}X^{\mathrm {T} }P_{Z}y,}
  

where 
  
    
      
        
          P
          
            Z
          
        
      
    
    {\displaystyle P_{Z}}
  
 refers to the projection matrix 
  
    
      
        
          P
          
            Z
          
        
        =
        Z
        (
        
          Z
          
            
              T
            
          
        
        Z
        
          )
          
            −
            1
          
        
        
          Z
          
            
              T
            
          
        
      
    
    {\displaystyle P_{Z}=Z(Z^{\mathrm {T} }Z)^{-1}Z^{\mathrm {T} }}
  
.
This expression collapses to the first when the number of instruments is equal to the number of covariates in the equation of interest. The over-identified IV is therefore a generalization of the just-identified IV.

There is an equivalent under-identified estimator for the case where m < k. Since the parameters are the solutions to a set of linear equations, an under-identified model using the set of equations 
  
    
      
        
          Z
          ′
        
        v
        =
        0
      
    
    {\displaystyle Z'v=0}
  
 does not have a unique solution.


== Interpretation as two-stage least squares ==
One computational method which can be used to calculate IV estimates is two-stage least squares (2SLS or TSLS).  In the first stage, each explanatory variable that is an endogenous covariate in the equation of interest is regressed on all of the exogenous variables in the model, including both exogenous covariates in the equation of interest and the excluded instruments.  The predicted values from these regressions are obtained:
Stage 1: Regress each column of X on Z, (
  
    
      
        X
        =
        Z
        δ
        +
        
          errors
        
      
    
    {\displaystyle X=Z\delta +{\text{errors}}}
  
):

  
    
      
        
          
            
              δ
              ^
            
          
        
        =
        (
        
          Z
          
            
              T
            
          
        
        Z
        
          )
          
            −
            1
          
        
        
          Z
          
            
              T
            
          
        
        X
        ,
        
      
    
    {\displaystyle {\widehat {\delta }}=(Z^{\mathrm {T} }Z)^{-1}Z^{\mathrm {T} }X,\,}
  

and save the predicted values:

  
    
      
        
          
            
              X
              ^
            
          
        
        =
        Z
        
          
            
              δ
              ^
            
          
        
        =
        
          
            Z
            (
            
              Z
              
                
                  T
                
              
            
            Z
            
              )
              
                −
                1
              
            
            
              Z
              
                
                  T
                
              
            
          
        
        X
        =
        
          
            
              P
              
                Z
              
            
          
        
        X
        .
        
      
    
    {\displaystyle {\widehat {X}}=Z{\widehat {\delta }}={\color {ProcessBlue}Z(Z^{\mathrm {T} }Z)^{-1}Z^{\mathrm {T} }}X={\color {ProcessBlue}P_{Z}}X.\,}
  

In the second stage, the regression of interest is estimated as usual, except that in this stage each endogenous covariate is replaced with the predicted values from the first stage:
Stage 2:  Regress Y on the predicted values from the first stage:

  
    
      
        Y
        =
        
          
            
              X
              ^
            
          
        
        β
        +
        
          n
          o
          i
          s
          e
        
        ,
        
      
    
    {\displaystyle Y={\widehat {X}}\beta +\mathrm {noise} ,\,}
  

which gives

  
    
      
        
          β
          
            2SLS
          
        
        =
        
          
            (
            
              
                X
                
                  
                    T
                  
                
              
              
                
                  
                    P
                    
                      Z
                    
                  
                
              
              X
            
            )
          
          
            −
            1
          
        
        
          X
          
            
              T
            
          
        
        
          
            
              P
              
                Z
              
            
          
        
        Y
        .
      
    
    {\displaystyle \beta _{\text{2SLS}}=\left(X^{\mathrm {T} }{\color {ProcessBlue}P_{Z}}X\right)^{-1}X^{\mathrm {T} }{\color {ProcessBlue}P_{Z}}Y.}
  

This method is only valid in linear models. For categorical endogenous covariates, one might be tempted to use a different first stage than ordinary least squares, such as a probit model for the first stage followed by OLS for the second. This is commonly known in the econometric literature as the forbidden regression, because second-stage IV parameter estimates are consistent only in special cases.

The resulting estimator of 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 is numerically identical to the expression displayed above. A small correction must be made to the sum-of-squared residuals in the second-stage fitted model in order that the covariance matrix of 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 is calculated correctly.


== Non-parametric analysis ==
When the form of the structural equations is unknown, an instrumental variable 
  
    
      
        Z
      
    
    {\displaystyle Z}
  
 can still be defined through the equations:

  
    
      
        x
        =
        g
        (
        z
        ,
        u
        )
        
      
    
    {\displaystyle x=g(z,u)\,}
  

  
    
      
        y
        =
        f
        (
        x
        ,
        u
        )
        
      
    
    {\displaystyle y=f(x,u)\,}
  

where 
  
    
      
        f
      
    
    {\displaystyle f}
  
 and 
  
    
      
        g
      
    
    {\displaystyle g}
  
 are two arbitrary functions and 
  
    
      
        Z
      
    
    {\displaystyle Z}
  
 is independent of 
  
    
      
        U
      
    
    {\displaystyle U}
  
. Unlike linear models, however, measurements of 
  
    
      
        Z
        ,
        X
      
    
    {\displaystyle Z,X}
  
 and 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
 do not allow for the identification of the average causal effect of 
  
    
      
        X
      
    
    {\displaystyle X}
  
 on 
  
    
      
        Y
      
    
    {\displaystyle Y}
  
, denoted ACE

  
    
      
        
          ACE
        
        =
        Pr
        (
        y
        ∣
        
          do
        
        (
        x
        )
        )
        =
        
          E
          
            u
          
        
        ⁡
        [
        f
        (
        x
        ,
        u
        )
        ]
        .
      
    
    {\displaystyle {\text{ACE}}=\Pr(y\mid {\text{do}}(x))=\operatorname {E} _{u}[f(x,u)].}
  

Balke and Pearl [1997] derived tight bounds on ACE and showed that these can provide valuable information on the sign and size of ACE.
In linear analysis, there is no test to falsify the assumption the 
  
    
      
        Z
      
    
    {\displaystyle Z}
  
 is instrumental relative to the pair 
  
    
      
        (
        X
        ,
        Y
        )
      
    
    {\displaystyle (X,Y)}
  
. This is not the case when 
  
    
      
        X
      
    
    {\displaystyle X}
  
 is discrete. Pearl (2000) has shown that, for all 
  
    
      
        f
      
    
    {\displaystyle f}
  
 and 
  
    
      
        g
      
    
    {\displaystyle g}
  
, the following constraint, called "Instrumental Inequality" must hold whenever 
  
    
      
        Z
      
    
    {\displaystyle Z}
  
 satisfies the two equations above:

  
    
      
        
          max
          
            x
          
        
        
          ∑
          
            y
          
        
        [
        
          max
          
            z
          
        
        Pr
        (
        y
        ,
        x
        ∣
        z
        )
        ]
        ≤
        1.
      
    
    {\displaystyle \max _{x}\sum _{y}[\max _{z}\Pr(y,x\mid z)]\leq 1.}
  


== Interpretation under treatment effect heterogeneity ==
The exposition above assumes that the causal effect of interest does not vary across observations, that is, that 
  
    
      
        β
      
    
    {\displaystyle \beta }
  
 is a constant.  Generally, different subjects will respond in different ways to changes in the "treatment" x.  When this possibility is recognized, the average effect in the population of a change in x on y may differ from the effect in a given subpopulation.  For example, the average effect of a job training program may substantially differ across the group of people who actually receive the training and the group which chooses not to receive training.  For these reasons, IV methods invoke implicit assumptions on behavioral response, or more generally assumptions over the correlation between the response to treatment and propensity to receive treatment.
The standard IV estimator can recover local average treatment effects (LATE) rather than average treatment effects (ATE).  Imbens and Angrist (1994) demonstrate that the linear IV estimate can be interpreted under weak conditions as a weighted average of local average treatment effects, where the weights depend on the elasticity of the endogenous regressor to changes in the instrumental variables. Roughly, that means that the effect of a variable is only revealed for the subpopulations affected by the observed changes in the instruments, and that subpopulations which respond most to changes in the instruments will have the largest effects on the magnitude of the IV estimate.
For example, if a researcher uses presence of a land-grant college as an instrument for college education in an earnings regression, she identifies the effect of college on earnings in the subpopulation which would obtain a college degree if a college is present but which would not obtain a degree if a college is not present.  This empirical approach does not, without further assumptions, tell the researcher anything about the effect of college among people who would either always or never get a college degree regardless of whether a local college exists.


== Weak instruments problem ==
As Bound, Jaeger, and Baker (1995) note, a problem is caused by the selection of "weak" instruments, instruments that are poor predictors of the endogenous question predictor in the first-stage equation. In this case, the prediction of the question predictor by the instrument will be poor and the predicted values will have very little variation. Consequently, they are unlikely to have much success in predicting the ultimate outcome when they are used to replace the question predictor in the second-stage equation.
In the context of the smoking and health example discussed above, tobacco taxes are weak instruments for smoking if smoking status is largely unresponsive to changes in taxes.  If higher taxes do not induce people to quit smoking (or not start smoking), then variation in tax rates tells us nothing about the effect of smoking on health.  If taxes affect health through channels other than through their effect on smoking, then the instruments are invalid and the instrumental variables approach may yield misleading results.  For example, places and times with relatively health-conscious populations may both implement high tobacco taxes and exhibit better health even holding smoking rates constant, so we would observe a correlation between health and tobacco taxes even if it were the case that smoking has no effect on health.  In this case, we would be mistaken to infer a causal effect of smoking on health from the observed correlation between tobacco taxes and health.


=== Testing for weak instruments ===
The strength of the instruments can be directly assessed because both the endogenous covariates and the instruments are observable.  A common rule of thumb for models with one endogenous regressor is: the F-statistic against the null that the excluded instruments are irrelevant in the first-stage regression should be larger than 10.


== Statistical inference and hypothesis testing ==
When the covariates are exogenous, the small-sample properties of the OLS estimator can be derived in a straightforward manner by calculating moments of the estimator conditional on X.  When some of the covariates are endogenous so that instrumental variables estimation is implemented, simple expressions for the moments of the estimator cannot be so obtained.  Generally, instrumental variables estimators only have desirable asymptotic, not finite sample, properties, and inference is based on asymptotic approximations to the sampling distribution of the estimator.  Even when the instruments are uncorrelated with the error in the equation of interest and when the instruments are not weak, the finite sample properties of the instrumental variables estimator may be poor.  For example, exactly identified models produce finite sample estimators with no moments, so the estimator can be said to be neither biased nor unbiased, the nominal size of test statistics may be substantially distorted, and the estimates may commonly be far away from the true value of the parameter.


== Testing the exclusion restriction ==
The assumption that the instruments are not correlated with the error term in the equation of interest is not testable in exactly identified models.  If the model is overidentified, there is information available which may be used to test this assumption.  The most common test of these overidentifying restrictions, called the Sargan–Hansen test, is based on the observation that the residuals should be uncorrelated with the set of exogenous variables if the instruments are truly exogenous.  The Sargan–Hansen test statistic can be calculated as 
  
    
      
        T
        
          R
          
            2
          
        
      
    
    {\displaystyle TR^{2}}
  
 (the number of observations multiplied by the coefficient of determination) from the OLS regression of the residuals onto the set of exogenous variables.  This statistic will be asymptotically chi-squared with m − k degrees of freedom under the null that the error term is uncorrelated with the instruments.


== See also ==
Control function (econometrics) – Statistical methods to correct for endogeneity problems
Optimal instruments – Technique for improving the efficiency of estimators in conditional moment models


== References ==


== Further reading ==
Greene, William H. (2008). Econometric Analysis (Sixth ed.). Upper Saddle River: Pearson Prentice-Hall. pp. 314–353. ISBN 978-0-13-600383-0.
Gujarati, Damodar N.; Porter, Dawn C. (2009). Basic Econometrics (Fifth ed.). New York: McGraw-Hill Irwin. pp. 711–736. ISBN 978-0-07-337577-9.
Keane, Michael P.; Neal, Timothy (2024). "A Practical Guide to Weak Instruments". Annual Review of Economics. 16: 185–212.
Sargan, Denis (1988). Lectures on Advanced Econometric Theory. Oxford: Basil Blackwell. pp. 42–67. ISBN 978-0-631-14956-9.
Wooldridge, Jeffrey M. (2013). Introductory Econometrics: A Modern Approach (Fifth international ed.). Mason, OH: South-Western. pp. 490–528. ISBN 978-1-111-53439-4.


== Bibliography ==
Wooldridge, J. (1997): Quasi-Likelihood Methods for Count Data, Handbook of Applied Econometrics, Volume 2, ed. M. H. Pesaran and P. Schmidt, Oxford, Blackwell, pp. 352–406
Terza, J. V. (1998): "Estimating Count Models with Endogenous Switching: Sample Selection and Endogenous Treatment Effects." Journal of Econometrics (84), pp. 129–154
Wooldridge, J. (2002): "Econometric Analysis of Cross Section and Panel Data", MIT Press, Cambridge, Massachusetts.


== External links ==
Chapter from Daniel McFadden's textbook
Econometrics lecture (topic: instrumental variable) on YouTube by Mark Thoma.
Econometrics lecture (topic: two-stages least square) on YouTube by Mark Thoma