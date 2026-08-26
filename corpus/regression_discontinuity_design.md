# Regression discontinuity design

> Source: [https://en.wikipedia.org/wiki/Regression_discontinuity_design](https://en.wikipedia.org/wiki/Regression_discontinuity_design)  
> Retrieved from Wikipedia, licensed under CC BY-SA 4.0.

---

Regression discontinuity designs (RDD) are a quasi-experimental pretest–posttest design that attempts to determine the causal effects of interventions by assigning a cutoff or threshold above or below which an intervention is assigned. By comparing observations lying closely on either side of the threshold, it is possible to estimate the average treatment effect in environments where random assignment to conditions is unfeasible. True causal inference using RDDs is still impossible, because the RDD cannot account for the potentially confounding effects of other variables without randomization.
The RDD was originally applied by Donald Thistlethwaite and Donald Campbell (1960) to evaluate the effect of scholarship programs on student career plans. The RDD is used in disciplines like psychology, economics, political science, epidemiology, and other related disciplines. Recent comparisons of randomised controlled trials (RCTs) and RDDs have empirically demonstrated the internal validity of the design.


== Example ==
The intuition behind the RDD is well illustrated using the evaluation of merit-based scholarships. The main problem with estimating the causal effect of such an intervention is the homogeneity of performance to the assignment of treatment (e.g., a scholarship award). Since high-performing students are more likely to be awarded the merit scholarship and continue performing well at the same time, comparing the outcomes of awardees and non-recipients would lead to an upward bias of the estimates. Even if the scholarship did not improve grades at all, awardees would have performed better than non-recipients, simply because scholarships were given to students who were performing well before.
Despite the absence of an experimental design, an RDD can exploit exogenous characteristics of the intervention to elicit causal effects. If all students above a given grade—for example 80%—are given the scholarship, it is possible to elicit the local treatment effect by comparing students around the 80% cut-off. The intuition here is that a student scoring 79% is likely to be very similar to a student scoring 81%—given the pre-defined threshold of 80%. However, one student will receive the scholarship while the other will not. Comparing the outcome of the awardee (treatment group) to the counterfactual outcome of the non-recipient (control group) will hence deliver the local treatment effect.


== Methodology ==
The two most common approaches to estimation using an RDD are non-parametric and parametric (normally polynomial regression).


=== Non-parametric estimation ===
The most common non-parametric method used in the RDD context is a local linear regression. This is of the form:

  
    
      
        Y
        =
        α
        +
        τ
        D
        +
        
          β
          
            1
          
        
        (
        X
        −
        c
        )
        +
        
          β
          
            2
          
        
        D
        (
        X
        −
        c
        )
        +
        ε
        ,
      
    
    {\displaystyle Y=\alpha +\tau D+\beta _{1}(X-c)+\beta _{2}D(X-c)+\varepsilon ,}
  

where 
  
    
      
        c
      
    
    {\displaystyle c}
  
 is the treatment cutoff and 
  
    
      
        D
      
    
    {\displaystyle D}
  
 is a binary variable equal to one if 
  
    
      
        X
        ≥
        c
      
    
    {\displaystyle X\geq c}
  
. Letting 
  
    
      
        h
      
    
    {\displaystyle h}
  
 be the bandwidth of data used, we have 
  
    
      
        c
        −
        h
        ≤
        X
        ≤
        c
        +
        h
      
    
    {\displaystyle c-h\leq X\leq c+h}
  
. Different slopes and intercepts fit data on either side of the cutoff. Typically either a rectangular kernel (no weighting) or a triangular kernel are used. The rectangular kernel has a more straightforward interpretation over sophisticated kernels which yield little efficiency gains.
The major benefit of using non-parametric methods in an RDD is that they provide estimates based on data closer to the cut-off, which is intuitively appealing. This reduces some bias that can result from using data farther away from the cutoff to estimate the discontinuity at the cutoff. More formally, local linear regressions are preferred because they have better bias properties and have better convergence. However, the use of both types of estimation, if feasible, is a useful way to argue that the estimated results do not rely too heavily on the particular approach taken.


=== Parametric estimation ===
An example of a parametric estimation is:

  
    
      
        Y
        =
        α
        +
        
          β
          
            1
          
        
        
          x
          
            i
          
        
        +
        
          β
          
            2
          
        
        
          c
          
            i
          
        
        +
        
          β
          
            3
          
        
        
          c
          
            i
          
          
            2
          
        
        +
        
          β
          
            4
          
        
        
          c
          
            i
          
          
            3
          
        
        +
        ε
        ,
      
    
    {\displaystyle Y=\alpha +\beta _{1}x_{i}+\beta _{2}c_{i}+\beta _{3}c_{i}^{2}+\beta _{4}c_{i}^{3}+\varepsilon ,}
  

where

  
    
      
        
          x
          
            i
          
        
        =
        
          
            {
            
              
                
                  1
                  
                     if 
                  
                  
                    c
                    
                      i
                    
                  
                  ≥
                  
                    
                      
                        c
                        ¯
                      
                    
                  
                
              
              
                
                  0
                  
                     if 
                  
                  
                    c
                    
                      i
                    
                  
                  <
                  
                    
                      
                        c
                        ¯
                      
                    
                  
                
              
            
            
          
        
      
    
    {\displaystyle x_{i}={\begin{cases}1{\text{ if }}c_{i}\geq {\bar {c}}\\0{\text{ if }}c_{i}<{\bar {c}}\end{cases}}}
  

and 
  
    
      
        
          
            
              c
              ¯
            
          
        
      
    
    {\displaystyle {\bar {c}}}
  
 is the treatment cutoff.
Note that the polynomial part can be shortened or extended according to the needs.


=== Other examples ===
Policies in which treatment is determined by an age eligibility criterion (e.g. pensions, minimum legal drinking age).
Elections in which one politician wins by a marginal majority.
Placement scores within education that sort students into treatment programs.


== Required assumptions ==
Regression discontinuity design requires that all potentially relevant variables besides the treatment variable and outcome variable be continuous at the point where the treatment and outcome discontinuities occur. One sufficient, though not necessary, condition is if the treatment assignment is "as good as random" at the threshold for treatment. If this holds, then it guarantees that those who just barely received treatment are comparable to those who just barely did not receive treatment, as treatment status is effectively random.
Treatment assignment at the threshold can be "as good as random" if there is randomness in the assignment variable and the agents considered (individuals, firms, etc.) cannot perfectly manipulate their treatment status. For example, suppose the treatment is passing an exam, where a grade of 50% is required. In this case, this example is a valid regression discontinuity design so long as grades are somewhat random, due either to the randomness of grading or randomness of student performance.
Students must not also be able to perfectly manipulate their grade so as to determine their treatment status perfectly. Two examples include students being able to convince teachers to "mercy pass" them, or students being allowed to retake the exam until they pass. In the former case, those students who barely fail but are able to secure a "mercy pass" may differ from those who just barely fail but cannot secure a "mercy pass". This leads to selection bias, as the treatment and control groups now differ. In the latter case, some students may decide to retake the exam, stopping once they pass. This also leads to selection bias since only some students will decide to retake the exam.


=== Testing the validity of the assumptions ===
It is impossible to definitively test for validity if agents are able to determine their treatment status perfectly. However, some tests can provide evidence that either supports or discounts the validity of the regression discontinuity design.


==== Density test ====

McCrary (2008) suggested examining the density of observations of the assignment variable. Suppose there is a discontinuity in the density of the assignment variable at the threshold for treatment. In this case, this may suggest that some agents were able to manipulate their treatment status perfectly.
For example, if several students are able to get a "mercy pass", then there will be more students who just barely passed the exam than who just barely failed. Similarly, if students are allowed to retake the exam until they pass, then there will be a similar result. In both cases, this will likely show up when the density of exam grades is examined. "Gaming the system" in this manner could bias the treatment effect estimate.


==== Continuity of observable variables ====
Since the validity of the regression discontinuity design relies on those who were just barely treated being the same as those who were just barely not treated, it makes sense to examine if these groups are similarly based on observable variables. For the earlier example, one could test if those who just barely passed have different characteristics (demographics, family income, etc.) than those who just barely failed. Although some variables may differ for the two groups based on random chance, most of these variables should be the same.


==== Falsification tests ====


===== Predetermined variables =====
Similar to the continuity of observable variables, one would expect there to be continuity in predetermined variables at the treatment cutoff. Since these variables were determined before the treatment decision, treatment status should not affect them. Consider the earlier merit-based scholarship example. If the outcome of interest is future grades, then we would not expect the scholarship to affect previous grades. If a discontinuity in predetermined variables is present at the treatment cutoff, then this puts the validity of the regression discontinuity design into question.


===== Other discontinuities =====
If discontinuities are present at other points of the assignment variable, where these are not expected, then this may make the regression discontinuity design suspect. Consider the example of Carpenter and Dobkin (2011) who studied the effect of legal access to alcohol in the United States. As the access to alcohol increases at age 21, this leads to changes in various outcomes, such as mortality rates and morbidity rates. If mortality and morbidity rates also increase discontinuously at other ages, then it throws the interpretation of the discontinuity at age 21 into question.


==== Inclusion and exclusion of covariates ====
If parameter estimates are sensitive to removing or adding covariates to the model, then this may cast doubt on the validity of the regression discontinuity design. A significant change may suggest that those who just barely got treatment to differ in these covariates from those who just barely did not get treatment. Including covariates would remove some of this bias. If a large amount of bias is present, and the covariates explain a significant amount of this, then their inclusion or exclusion would significantly change the parameter estimate.
Recent work has shown how to add covariates, under what conditions doing so is valid, and the potential for increased precision.


== Advantages ==
When properly implemented and analysed, the RDD yields an unbiased estimate of the local treatment effect. The RDD can be almost as good as a randomised experiment in measuring a treatment effect.
RDD, as a quasi-experiment, does not require ex-ante randomisation and circumvents ethical issues of random assignment.
Well-executed RDD studies can generate treatment effect estimates similar to estimates from randomised studies.


== Disadvantages ==
The estimated effects are only unbiased if the functional form of the relationship between the treatment and outcome is correctly modelled. The most popular caveats are non-linear relationships that are mistaken as a discontinuity.
Contamination by other treatments. Suppose another treatment occurs at the same cutoff value of the same assignment variable. In that case, the measured discontinuity in the outcome variable may be partially attributed to this other treatment. For example, suppose a researcher wishes to study the impact of legal access to alcohol on mental health using a regression discontinuity design at the minimum legal drinking age. The measured impact could be confused with legal access to gambling, which may occur at the same age.


== Extensions ==


=== Fuzzy RDD ===
The identification of causal effects hinges on the crucial assumption that there is indeed a sharp cut-off, around which there is a discontinuity in the probability of assignment from 0 to 1. In reality, however, cutoffs are often not strictly implemented (e.g. exercised discretion for students who just fell short of passing the threshold) and the estimates will hence be biased.
In contrast to the sharp regression discontinuity design, a fuzzy regression discontinuity design (FRDD) does not require a sharp discontinuity in the probability of assignment. Still, it is applicable as long as the probability of assignment is different. The intuition behind it is related to the instrumental variable strategy and intention to treat. Fuzzy RDD does not provide an unbiased estimate when the quantity of interest is the proportional effect (e.g. vaccine effectiveness), but extensions exist that do.


=== Regression kink design ===
When the assignment variable is continuous (e.g. student aid) and depends predictably on another observed variable (e.g. family income), one can identify treatment effects using sharp changes in the slope of the treatment function. This technique was coined regression kink design by Nielsen, Sørensen, and Taber (2010), though they cite similar earlier analyses. They write, "This approach resembles the regression discontinuity idea. Instead of a discontinuity of in the level of the stipend-income function, we have a discontinuity in the slope of the function." Rigorous theoretical foundations were provided by Card et al. (2012) and an empirical application by Bockerman et al. (2018).
Note that regression kinks (or kinked regression) can also mean a type of segmented regression, which is a different type of analysis.
Final considerations
The RD design takes the shape of a quasi-experimental research design with a clear structure that is devoid of randomized experimental features. Several aspects deny the RD designs an allowance for a status quo. For instance, the designs often involve serious issues that do not offer room for random experiments. Besides, the design of the experiments depends on the accuracy of the modelling process and the relationship between inputs and outputs.


== See also ==
Quasi-experiment
Design of quasi-experiments


== References ==


== Further reading ==
Angrist, J. D.; Pischke, J.-S. (2008). "Getting a Little Jumpy: Regression Discontinuity Designs". Mostly Harmless Econometrics: An Empiricist's Companion. Princeton University Press. pp. 251–268. ISBN 978-0-691-12035-5.
Cattaneo, Matias D.; Titiunik, Rocio (2022). "Regression Discontinuity Designs". Annual Review of Economics. 14: 821–851. arXiv:2108.09400. doi:10.1146/annurev-economics-051520-021409. S2CID 125763727.
Cattaneo, Matias D.; Idrobo, Nicolas; Titiunik, Rocío (2024). A Practical Introduction to Regression Discontinuity Designs: Extensions. Cambridge University Press.
Cook, Thomas D. (2008). "'Waiting for Life to Arrive': A history of the regression-discontinuity design in Psychology, Statistics and Economics". Journal of Econometrics. 142 (2): 636–654. doi:10.1016/j.jeconom.2007.05.002.
Imbens, Guido W.; Wooldridge, Jeffrey M. (2009). "Recent Developments in the Econometrics of Program Evaluation". Journal of Economic Literature. 47 (1): 5–86. doi:10.1257/jel.47.1.5.
Maas, Iris L.; Nolte, Sandra; Walter, Otto B.; Berger, Thomas; Hautzinger, Martin (2017). "The regression discontinuity design showed to be a valid alternative to a randomized controlled trial for estimating treatment effects". Journal of Clinical Epidemiology. 82: 94–102. doi:10.1016/j.jclinepi.2016.11.008. PMID 27865902.


== External links ==
Regression-Discontinuity Analysis at Research Methods Knowledge Base