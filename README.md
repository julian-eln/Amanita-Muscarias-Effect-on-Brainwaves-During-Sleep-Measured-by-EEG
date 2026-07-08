# Amanita-Muscaria-s-Effect-on-Brainwaves-During-Sleep-Measured-by-EEG
First known human EEG done while under the influence of Amanita Muscaria


## What we are testing:
EEGs are devices that collect brainwave data from the wearer. With the advent of consumer EEGs, data collection has become significantly more accessible. Amanita muscaria is an iconic mushroom that causes intoxication primarily through two molecules: ibotenic acid and muscimol. Muscimol, in particular, is considered the active compound.
Despite its history, studies and data regarding Amanita muscaria's effect on brainwaves are sparse. This appears to be the first human EEG recorded during intoxication with Amanita muscaria. It remains unclear precisely how the mushroom induces hallucinations, as it does not act on classical psychedelic receptors.
Most intoxicants influence specific brainwave bands, and these effects vary across drug classes, including hypnotics, GABAergic agents, dissociatives, and classical psychedelics (Siegel, 2024). This analysis examines two administrations of an Amanita extract. Collecting this data provides a starting point for understanding when Amanita muscaria kicks in, peaks, and wears off, as well as how it affects specific brainwave bands and which cognitive effects are associated with those changes


## Methods:
All EEG data were collected and processed using a 2014 Muse EEG headset. The app used to transmit the data to my computer was Muse Direct. Data was saved in the proprietary Muse format and compiled with Muse Player. PSPP was used to perform normality testing (Kolmogorov-Smirnov), independent-samples t-tests, and Mann-Whitney U tests. It was also utilized to generate histograms and bar graphs.
Custom scripts generated with assistance from Google Gemini were used to process the EEG recordings, perform spectral analysis, and create topographic visualizations. All outputs were manually reviewed before analysis. Because the Muse is limited to four channels, an additional topographic mapping technique was executed via a custom program. This program largely utilized the same code as Gemini, with the primary difference being the use of 5-minute epochs instead of 5-minute intervals with 4-second snapshots. Gemini was also used to clean the data and apply Welch's method to perform a Fast Fourier Transform (FFT). Furthermore, Gemini calculated the spectral percentages, binned the data into 5-minute intervals, and computed the absolute power using a $10 \log_{10}$ formula (in decibels). These values serve as the primary data points in the graphs. Additionally, Gemini calculated Cohen's d using the means and standard deviations from PSPP's parametric models, as well as the rank-biserial correlation (r) via the Mann-Whitney test in PSPP. Power analyses were conducted using socscistatistics.com and homepage.univie.ac.at. Preliminary analysis and fact-checking were performed by Claude (Anthropic) and ChatGPT (OpenAI) to identify any discrepancies in the data.
The Amanita muscaria was sourced from amentera.com (formerly mnniceethnobotanicals) and Awakening Roots, both of which are verified sellers. The products purchased included raw mushroom caps, open caps, pieces, and a 5-gram chocolate bar from Amentera. The raw mushrooms were decarboxylated by boiling them for three hours with lemon juice, a process designed to rapidly convert ibotenic acid into muscimol as described in Shokuhin Eiseigaku Zasshi (1993). This yielded a 0.5 g/mL tincture. It was originally prepared for another project and had been stored in a freezer for approximately three months. The 5-gram chocolate bar arrived a week before the test.
The test consisted of eating the full chocolate bar and lying down in bed. Concerned about the potency of the chocolate due to potential incomplete decarboxylation, I consumed 2 mL of the tincture (totaling 1g) approximately 40 minutes into the session. The test officially started at 11:50 PM. Alarms were set to track the onset of effects from both the chocolate and the tincture, which helped align the data. The baseline (control) was recorded about three weeks after the original test, using the exact same protocol of lying down and sleeping.


## Results:
### Absolute band power (Treatment 1 vs Baseline 1)
The most noticeable thing when comparing baseline 1 and treatment 1. There is an immediate drop in all waves (with periodic spikes of sigma) throughout the experiment, while in baseline 1, there seem to be dips (likely correlated with transitions in sleep) and then spikes of many different waves, but delta (associated with sleep), specifically, while dominating in both, was trending lower in Treatment 1 and trending higher in baseline. This is very different from most GABAergic drugs studied, and even from dissociative studies with nitrous oxide (in some cases) Foster, B. L., & Liley, D. T. (2011). Yamamura, T., Fukuda, M., & Takeya, H., et al. (1981) show similar effects.   

Even these studies, however, usually show some fluctuation or an increase in another wave (here, sigma did fluctuate but decreased overall); delta only decreases in REM sleep, and even then gamma fluctuates.  Amanita produced a noticeably higher DTABR (sedation ratio) than the baseline condition, suggesting a stronger sedative effect.

(Baseline 1)




(Treatment 1)

### Relative spectral power (Treatment 2 vs Baseline 2)

The next major measurement was relative spectral power.  Spectral painted a much more nuanced picture.  When looking at relative spectral power (how much each wave is), there is a clear domination of delta waves in Treatment  2.  They increase to a high of 58% of total power [reviewer note: recomputing from the raw EEG puts delta higher than this - see review report], with a clear suppression of alpha and theta waves.  This was especially present during the second wave from the tincture, where delta reached such highs and never lowered or plateaued for the rest of the session.  Surprisingly, gamma and beta waves % increased throughout the treatment.  The baseline seemed to have more of a fluctuation of all waves, but delta still dominated (reaching percentages in the 70s, and it seemed to be battling gamma wave spikes.  
(Baseline 2)

(Treatment 2)
### Topographic maps

 I also modeled scalp topographies of the EEG to visualize how Amanita affected the brain and which regions.  In the control Delta Topograph baseline,1 there is a clear high amount of power from delta throughout the session, with a decline only at minutes 15-25.  In contrast, in Delta topography treatment 1, there is an increase around that same period, but a decline around minutes 30-40.  While the waves are less in the Delta Topograph treatment, they are not absent, and looking at the band power seems to be at a lower level.  These findings suggest that Amanita muscaria may reduce the absolute power of delta activity while preserving its overall spatial distribution.  Another thing that's shown through these topographs is persistent activation of sigma (it was the second highest power in the treatment was sigma). 

Since sigma is most associated with the second stage nonrem sleep, spikes while using gabaergic drugs Leong et al., 2022; Feinberg, 2000, and acts to inhibit regions of the brain to make sleep more stable, it makes sense that it's very active during Amanita muscaria.   It's also very active in the baseline, but in sigma topograph treatment 1, it seems to be slightly lower, but has spikes much later on than sigma topograph baseline 1.  Sigma topograph treatment 2 shows more of the story, though, with sigma dominating the waves early and sticking throughout the session, than in sigma topograph baseline 2, where by the end they are gone; earlier, they dominate in the parietal and temporal lobes, which mostly handle memory, sensory processing, and spatial awareness. In contrast, the sigma topograph treatment 2 mostly equally spread the sigma wave but seemed to increase the sigma in the frontal lobe regions, which are used for reasoning and planning, while being noticeably softer in the Parietal Lobe and temporal lobes. 

  One possible explanation is that the mechanism for producing dissociation effects and even some hallucinations may have something to do with inhibiting the frontal lobe regions while allowing the temporal and parietal parts of the brain to be more active than normal and working, but without their main coordinator; this, however, could be due to artifacts from the topograph map software or anomalies in one night.  Theta seemed to somewhat follow theta topograph baseline 1 and theta topograph baseline 2, respectively, although in lower power.  It seemed that, unlike in absolute power (topograph treatment 1), the relative power was concentrated in the parietal and temporal parts of the brain, but there's not enough evidence to see.   The treatment completely wiped out band power in Gamma Topograph treatment 1, Alpha topograph treatment 1, and Beta topograph Treatment 1. Compared to Gamma topograph baseline 1, alpha topograph baseline 1, and beta Topograph baseline 1, which show activity, albeit light across all bands.  This is different from other studies like those with ethanol, showing fluctuating band activity Cohen, Porjesz & Begleiter, 1993; Stenberg, 1994).

 
 




 (Delta topograph Baseline 1) 
 
 
(Theta Topograph Baseline1)
 

 
(Alpha topograph Baseline 1)
 
  
(Beta Topograph Baseline 1)






















 




 
(Sigma Topograph Baseline  1)









(Gamma topograph  Baseline 1)














































 
 

(Delta topograph baseline 2)





 
 
(theta topograph baseline 2 )
 
 
(Alpha topograph 2 baseline)


















 
 
(Sigma topograph baseline 2)
 (Betatopography Baseline 2)  
 (Gamma Topograph Baseline 2)























 
 
(Delta Topograph Treatment 1)
 
 
(Theta topograph Treatment 1) 


































(Alpha topograph  Treatment 1)
 
 
(Beta Topograph Treatment 1) 
 
(Gamma Topograph Treatment 1 ) 
  
 
(Sigma Topograph Treatment 1)

  
(Delta topography Treatment 2)
 
 
(Theta Topograph Treatment 2)
 
  
(Alpha Topograph 2)
 
 
(Beta topograph Treatment  2)
  
(Sigma topograph Treatment 2)
   
(Gamma Topograph Treatment 2)









### Normality testing
After looking at the raw data, I ran both the relative band power (baseline and treatment) and the absolute band power (in dB) through the one-sample Kolmogorov-Smirnov test. To do this, I turned each 5-minute time bin into its own data point, giving me several data points instead of one. In the Absolute KS test 1, every absolute (dB) value came out parametric (normal) — Delta, Theta, Alpha, Beta, Gamma, and Sigma, along with the SMR and DTABR ratios (all Asymp. Sig. > 0.05). In the Relative KS test 1, all of the relative values were parametric except Gamma (p < 0.001) and Sigma (p = 0.024), which were non-parametric (not bell-shaped), so those two were tested separately with a non-parametric test.

 

(Absolute KS test 1) 

 
(Relative KS test 1)

































(EEG Histogram 1 — relative %, Delta & Theta, N=40 combined)



 
 


 
 

 
(EEG Histogram 2 — relative %, Alpha, Beta, Gamma & Sigma, N=40 combined; Gamma and Sigma were non-parametric per KS test)





























### Comparisons between treatment and control

The next analysis compared the treatment to the control through bar charts. Bar graph 1 shows the absolute band power in dB: every band was slightly lower in the treatment than the control, but none of the individual bands differed by much. The clearest differences were in the ratios — DTABR (sedation) was higher in the treatment, while SMR was higher in the control. Bar graph 2 shows relative power for the four parametric bands: Delta was much higher in the treatment (about 61.6%) than the control (about 47.6%), Alpha was lower in the treatment, and Theta and Beta were close in both. Sigma and Gamma were non-parametric and handled by the Kruskal-Wallis test instead — Sigma was far higher in the control, and Gamma was about the same in both.

 
 
(Bar graph 1)
 
 
 
 
(Bar Graph 2)























### Statistical tests

For the absolute (dB) values in Independent samples 1, none of the individual bands reached significance: Delta (p = .649), Theta (p = .666), Alpha (p = .227), Beta (p = .215), Gamma (p = .061, a non-significant trend toward higher gamma in the control), and Sigma (p = .722) were all non-significant. The only significant absolute results were the ratios: DTABR (sedation) was significantly higher in the treatment (p = .019), and SMR was significantly higher in the control (p = .023). For the relative values in Independent samples 2, Delta was significantly higher in the treatment — about 13.97 percentage points (p = .003) — and Alpha was significantly lower in the treatment (p = .017). Theta (p = .787) and Beta (p = .299) were not significant. Because Gamma and Sigma were non-parametric, I tested them with a Kruskal-Wallis test: relative Sigma was significantly higher in the control (p < .001), while Gamma was not significant (p = .755).
 
(Independent samples test 1) 

 
(Kruskal-Wallis — relative Sigma & Gamma)

 
(Independent samples t-test 2 — relative)
 


### Statistical power

To get the statistical power I used the effect sizes from the real recomputed data. For the non-parametric bands I used the rank-biserial r converted to P(X>Y), and for the parametric bands I used the smallest significant Cohen’s d so I wasn’t cherry-picking the biggest effect. All power calculations used α = 0.05, two-tailed, with the smaller group size (n = 18) as the conservative estimate.For Sigma (rank-biserial r = −0.95, P(X>Y) = 0.025) the required sample size per group for 80% power is just 6, which we already exceed even with pseudoreplication — the effect is so large that very few observations are needed to detect it reliably. For Gamma (r = +0.06, P(X>Y) = 0.530) the power with n = 18 per group is only 0.0497 — basically nothing, which makes sense because P(X>Y) = 0.53 is indistinguishable from a coin flip.For the parametric bands I used the weakest of the significant medium effects, SMR at d = 0.71. With the current n = 18 per group, power is 0.645 (64.5%) — underpowered relative to the 80% convention. Reaching 80% power for an effect this size would require n = 33 per group. The stronger effects (relative Delta at d = 0.96, DTABR at d = 0.74) would need fewer participants, but I used the weakest one as the conservative benchmark.As before, all of these n values are for bins treated as independent samples, which is pseudoreplication. The real sample size here is one participant and one session per condition, so these power figures are best read as ‘how many sessions would be needed if the effect size held up’ rather than a formal power guarantee.


 
  









(Stat power 1 — Gamma: P(X>Y)=0.530, power=0.050 at n=18 | Sigma: P(X>Y)=0.025, needs n=6 for 80% power)
 
  




 
 

(Stat power 2 — weakest significant parametric effect, SMR d=0.71: power=0.645 at n=18, needs n=33 for 80%)


## Conclusion:

So, despite my original assumptions, there was a broad suppression of cortical activity, but a rise in sedative patterns and a suppression of alpha/beta waves with an increase in delta waves, which is consistent with animal studies done with Amanita muscaria (Scotti de Carolis et al., 1969). When looking at the EEG through topographic maps, sigma was spread out but noticeably less in the parietal lobe during the treatment and a bit more present in the frontal lobe, which is associated with reasoning and planning. These findings may represent a potential mechanism underlying the dissociative and hallucinatory effects of Amanita muscaria, although substantially more data are required before firm conclusions can be drawn. Recomputed from the raw EEG, relative Delta dominated the treatment and was significantly higher than the control (about 61.6% vs 47.6%), while Alpha was significantly lower. Relative Sigma was significantly higher in the control. The sedation ratio (DTABR) was significantly higher in the treatment, and SMR was higher in the control. In absolute (dB) terms the individual bands did not differ significantly between conditions, so the clearest treatment signature is the relative shift toward Delta and the DTABR/SMR ratios rather than any single absolute band.

The relative values were mostly parametric, with only Sigma and Gamma being non-parametric. After an independent-samples t-test on the relative bands, Delta was significantly higher in the treatment (about 13.97 percentage points, p = .003) and Alpha was significantly lower (p = .017), while Theta and Beta were non-significant. A Kruskal-Wallis test on the non-parametric bands found relative Sigma significantly higher in the control (p < .001) and Gamma non-significant (p = .755). For the absolute (dB) values, no individual band differed significantly between conditions; only DTABR (higher in treatment, p = .019) and SMR (higher in control, p = .023) were significant. Because each of these tests treats 5-minute bins as independent samples (pseudoreplication), they should be read as a single-subject, exploratory result, not a population-level finding.

## Limitations:

 The Muse is a consumer headset, meaning it is not as advanced as clinician-grade EEGs and doesn't have as many sensors as even more modern (post-2014) consumer EEG systems. It only has 4 sensors, substantially fewer than the standard 10-20 EEG system described by Jasper (1957).   There are also major artifacts, like at 85 minutes, some of the spikes may be due to movement, and because I set alarms in the treatment to know when I should mark down the time certain effects started,  

Another issue is that taking two doses of Amanita muscaria does not lead to getting the cleanest example of how it affects the brain once crossing the blood-brain barrier.

The biggest statistical flaw is pseudoreplication. Because I didn't have enough data for an ANOVA and didn't know how to properly run a time series, I ended up turning each time point into an individual data entry. This inflates N, and therefore the robustness percentage. This is pseudoreplication, and it is a major flaw in this research.

I also took Amanita during a busy day for me, so my brain was probably already at a higher power than normal.  Two datasets also only left me with a limited dataset, which makes it hard to extrapolate anything.  Amanita Muscaria's lack of consistent dosages in the wild also makes it harder to reproduce to an extent.  For the future, going up to 5-10 tests and using ethanol or some other GABAergic substance as a comparative group could be useful.  Also, changing the muse protocol from straight recording until the battery dies during sleep is probably not the best way to conduct this experiment.  The sigma theory also can't be exact due to limited data and only 4 electrodes on the Muse.   

In the future, I would like to iterate with awake tests and try to map the full peak and come down.   



