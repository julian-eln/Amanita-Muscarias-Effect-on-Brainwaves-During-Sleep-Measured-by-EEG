# Amanita-Muscaria`s-Effect-on-Brainwaves-During-Sleep-Measured-by-EEG
First known human EEG done while under the influence of Amanita Muscaria


## What we are testing:
EEGs are devices that collect brainwave data from the wearer. With the advent of consumer EEGs, data collection has become significantly more accessible. Amanita muscaria is an iconic mushroom that causes intoxication primarily through two molecules: ibotenic acid and muscimol. Muscimol, in particular, is considered the active compound.
Despite its history, studies and data regarding Amanita muscaria's effect on brainwaves are sparse. This appears to be the first human EEG recorded during intoxication with Amanita muscaria. It remains unclear precisely how the mushroom induces hallucinations, as it does not act on classical psychedelic receptors.
Most intoxicants influence specific brainwave bands, and these effects vary across drug classes, including hypnotics, GABAergic agents, dissociatives, and classical psychedelics (Siegel, 2024). This analysis examines two administrations of an Amanita extract. Collecting this data provides a starting point for understanding when Amanita muscaria kicks in, peaks, and wears off, as well as how it affects specific brainwave bands and which cognitive effects are associated with those changes


## Methods:
All EEG data were collected and processed using a 2014 Muse EEG headset. The app used to transmit the data to my computer was Muse Direct. Data was saved in the proprietary Muse format and compiled with Muse Player. PSPP was used to perform normality testing (Kolmogorov-Smirnov), independent-samples t-tests, and Mann-Whitney U tests. It was also utilized to generate histograms and bar graphs.
Custom scripts generated with assistance from Google Gemini were used to process the EEG recordings, perform spectral analysis, and create topographic visualizations. All outputs were manually reviewed before analysis. Because the Muse is limited to four channels, an additional topographic mapping technique was executed via a custom program. This program largely utilized the same code as Gemini, with the primary difference being the use of 5-minute epochs instead of 5-minute intervals with 4-second snapshots. Gemini was also used to clean the data and apply Welch's method to perform a Fast Fourier Transform (FFT). Furthermore, Gemini calculated the spectral percentages, binned the data into 5-minute intervals, and computed the absolute power using a 10log10 formula (in decibels). These values serve as the primary data points in the graphs. Additionally, Gemini calculated Cohen's d using the means and standard deviations from PSPP's parametric models, as well as the rank-biserial correlation (r) via the Mann-Whitney test in PSPP. Power analyses were conducted using socscistatistics.com and homepage.univie.ac.at. Preliminary analysis and fact-checking were performed by Claude (Anthropic) and ChatGPT (OpenAI) to identify any discrepancies in the data.

**Aggregation method (dB-relative).** Relative band power values in the workbook were derived as follows: Gemini computed absolute power in decibels (10·log₁₀ of mean linear power) for each 5-minute bin; the per-bin dB values were then averaged across all bins; finally the averaged dB values were converted back to linear power (10^(dB/10)) and normalized to percentages to yield relative power. This approach is internally consistent with the analysis pipeline as built. However, it differs from the more commonly reported method, in which each epoch or bin is first converted to relative power and those percentages are then averaged. Because the dB-to-linear back-conversion is nonlinear (Jensen's inequality: mean of logs ≠ log of means), the two approaches yield different relative percentages — the magnitude of the discrepancy varies by band and by night. Readers should be aware that the numeric relative-power values and significance tests reported in this study reflect the dB-averaging aggregation, not the per-epoch-relative-then-average approach.
The Amanita muscaria was sourced from amentera.com (formerly mnniceethnobotanicals) and Awakening Roots, both of which are verified sellers. The products purchased included raw mushroom caps, open caps, pieces, and a 5-gram chocolate bar from Amentera. The raw mushrooms were decarboxylated by boiling them for three hours with lemon juice, a process designed to rapidly convert ibotenic acid into muscimol as described in Shokuhin Eiseigaku Zasshi (1993). This yielded a 0.5 g/mL (about .015 -.05 mg of muscimol per mL) tincture. It was originally prepared for another project and had been stored in a freezer for approximately three months. The 5-gram chocolate bar arrived a week before the test.
The test consisted of eating the full chocolate bar and lying down in bed. Concerned about the potency of the chocolate due to potential incomplete decarboxylation, I consumed 2 mL of the tincture (totaling 1g) approximately 40 minutes into the session. The test officially started at 11:50 PM. Alarms were set to track the onset of effects from both the chocolate and the tincture, which helped align the data. The baseline (control) was recorded about three weeks after the original test, using the exact same protocol of lying down and sleeping.


## Results:

> **✅ Analysis note (updated July 2026):** The relative-power results in this section have been **recomputed on corrected data**. An earlier version reported a large "Delta surge" (61.6% vs 47.6%, p=.003) and "Sigma higher in control (p<.001)"; both were artifacts of a baseline relative-power table that had not been recomputed and disagreed with its own dB values (Delta 47.6% vs 63.3%; Sigma 20.0% vs 1.7%). With the baseline recomputed the same way as the treatment, **Delta is no longer significant** (63.3% control vs 69.4% treatment, Kruskal–Wallis p=.109) and **Sigma is no longer significant** (p=.430). The corrected data flags **reduced relative Alpha under Amanita** (5.1%→3.9%, t-test p=.023); Beta and Gamma rank higher in the control (p=.039/.036) but are fragile (see the statistical-tests section). The absolute-dB picture (mild, non-significant broad suppression) is unchanged. **Robustness update:** all three effects (Alpha, Beta, Gamma) are specific to the dB-averaging aggregation used in the workbook — when recomputed from raw using the standard per-epoch-relative method they are non-significant (see the statistical-tests section and the aggregation note in Methods). So the safest read of the corrected data is **no robust spectral difference between the two nights in any band**. All results remain single-subject and pseudoreplicated — exploratory, not population-level.

### Absolute band power (Treatment 1 vs Baseline 1)
The most noticeable thing when comparing baseline 1 and treatment 1. There is an immediate drop in all waves (with periodic spikes of sigma) throughout the experiment, while in baseline 1, there seem to be dips (likely correlated with transitions in sleep) and then spikes of many different waves, but delta (associated with sleep), specifically, while dominating in both, was trending lower in Treatment 1 and trending higher in baseline. This is very different from most GABAergic drugs studied, and even from dissociative studies with nitrous oxide (in some cases) Foster, B. L., & Liley, D. T. (2011). Yamamura, T., Fukuda, M., & Takeya, H., et al. (1981) show similar effects.   

Even these studies, however, usually show some fluctuation or an increase in another wave (here, sigma did fluctuate but decreased overall); delta only decreases in REM sleep, and even then gamma fluctuates.  Amanita produced a noticeably higher DTABR (sedation ratio) than the baseline condition, suggesting a stronger sedative effect.

<img width="975" height="725" alt="image" src="https://github.com/user-attachments/assets/afb78a97-586e-43e4-8b29-3b2dad9865af" />

(Baseline 1)

<img width="938" height="580" alt="image" src="https://github.com/user-attachments/assets/032ecf80-8a3a-4364-9d48-875c4951dfa4" />



(Treatment 1)

### Relative spectral power (Treatment 2 vs Baseline 2)

The next major measurement was relative spectral power (how much of the total power each band makes up). Delta dominates in both conditions. On the corrected data, delta averaged about 69% of total power in the treatment versus about 63% in the baseline — the treatment trends higher, but once the baseline table was recomputed the same way as the treatment (see the analysis note above) this delta difference is **not** statistically significant. Delta climbed into the 70–85% range in stretches of both nights, especially late in the treatment session after the tincture. The band that clearly changed is **alpha, which was reduced in the treatment** (about 3.9% vs 5.1% in the baseline). Theta was slightly higher in the treatment rather than suppressed, and — contrary to my first read — **gamma was lower in the treatment**, not higher (the baseline carried more high-frequency power). Beta was similar in both. (My earlier draft reported a delta jump to 58% with alpha/theta suppression and rising beta/gamma; those numbers came from a baseline table that had not been recomputed, and are corrected here.)

<img width="975" height="604" alt="image" src="https://github.com/user-attachments/assets/56143a30-ab46-4063-97f4-731a233ec2d5" />

(Baseline 2)
<img width="975" height="663" alt="image" src="https://github.com/user-attachments/assets/987e8cad-42ad-4124-a3a0-26cf0eb363ad" />

(Treatment 2)
### Topographic maps

 I also modeled scalp topographies of the EEG to visualize how Amanita affected the brain and which regions.  In the control Delta Topograph baseline,1 there is a clear high amount of power from delta throughout the session, with a decline only at minutes 15-25.  In contrast, in Delta topography treatment 1, there is an increase around that same period, but a decline around minutes 30-40.  While the waves are less in the Delta Topograph treatment, they are not absent, and looking at the band power seems to be at a lower level.  These findings suggest that Amanita muscaria may reduce the absolute power of delta activity while preserving its overall spatial distribution.  Another thing that's shown through these topographs is persistent activation of sigma (it was the second highest power in the treatment was sigma). 

Since sigma is most associated with the second stage nonrem sleep, spikes while using gabaergic drugs Leong et al., 2022; Feinberg, 2000, and acts to inhibit regions of the brain to make sleep more stable, it makes sense that it's very active during Amanita muscaria.   It's also very active in the baseline, but in sigma topograph treatment 1, it seems to be slightly lower, but has spikes much later on than sigma topograph baseline 1.  Sigma topograph treatment 2 shows more of the story, though, with sigma dominating the waves early and sticking throughout the session, than in sigma topograph baseline 2, where by the end they are gone; earlier, they dominate in the parietal and temporal lobes, which mostly handle memory, sensory processing, and spatial awareness. In contrast, the sigma topograph treatment 2 mostly equally spread the sigma wave but seemed to increase the sigma in the frontal lobe regions, which are used for reasoning and planning, while being noticeably softer in the Parietal Lobe and temporal lobes. 

  One possible explanation is that the mechanism for producing dissociation effects and even some hallucinations may have something to do with inhibiting the frontal lobe regions while allowing the temporal and parietal parts of the brain to be more active than normal and working, but without their main coordinator; this, however, could be due to artifacts from the topograph map software or anomalies in one night.  Theta seemed to somewhat follow theta topograph baseline 1 and theta topograph baseline 2, respectively, although in lower power.  It seemed that, unlike in absolute power (topograph treatment 1), the relative power was concentrated in the parietal and temporal parts of the brain, but there's not enough evidence to see.   The treatment completely wiped out band power in Gamma Topograph treatment 1, Alpha topograph treatment 1, and Beta topograph Treatment 1. Compared to Gamma topograph baseline 1, alpha topograph baseline 1, and beta Topograph baseline 1, which show activity, albeit light across all bands.  This is different from other studies like those with ethanol, showing fluctuating band activity Cohen, Porjesz & Begleiter, 1993; Stenberg, 1994).

 
 


<img width="948" height="691" alt="image" src="https://github.com/user-attachments/assets/a8af1c71-a45e-4151-aca0-c3200ddac6ac" />
<img width="948" height="691" alt="image" src="https://github.com/user-attachments/assets/60046cb0-9c6f-4400-ad2c-28bc6677dc30" />


 (Delta topograph Baseline 1) 
 
 <img width="975" height="610" alt="image" src="https://github.com/user-attachments/assets/065dfd28-8084-4b58-bd7b-d33400ff4752" />
<img width="851" height="708" alt="image" src="https://github.com/user-attachments/assets/ddf00b6c-6a87-47c5-a36a-ae899fb27f44" />

(Theta Topograph Baseline1)
 <img width="948" height="669" alt="image" src="https://github.com/user-attachments/assets/7f964147-41ab-4674-aaac-b0f1e8e13e75" />
<img width="975" height="813" alt="image" src="https://github.com/user-attachments/assets/66914a2e-0ac2-4294-b532-a7cd35867057" />


 
(Alpha topograph Baseline 1)
 <img width="975" height="898" alt="image" src="https://github.com/user-attachments/assets/93692d0a-1a58-4722-890d-90c6e8e7e1f8" />

  <img width="800" height="664" alt="image" src="https://github.com/user-attachments/assets/3e047023-d692-4ff2-8efc-261631bb68ba" />

(Beta Topograph Baseline 1)





















<img width="975" height="813" alt="image" src="https://github.com/user-attachments/assets/fc12aa17-f107-42ce-be54-9cbb6a7f8eab" />

 


<img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/1be30027-e91c-4fa8-b907-d75f6fc038b6" />


 
(Sigma Topograph Baseline  1)


<img width="975" height="792" alt="image" src="https://github.com/user-attachments/assets/254dfead-4a99-4892-9115-c3dd8574a7db" />


<img width="975" height="813" alt="image" src="https://github.com/user-attachments/assets/420bad43-0b89-4bdb-b6c3-192d4ff1ae83" />







(Gamma topograph  Baseline 1)












































<img width="975" height="800" alt="image" src="https://github.com/user-attachments/assets/a3564f23-4917-46f0-93a0-b0f08d1c415a" />



<img width="975" height="619" alt="image" src="https://github.com/user-attachments/assets/e5f1d567-b12e-4590-8f6f-87f36b28663f" />

 
 

(Delta topograph baseline 2)






<img width="975" height="800" alt="image" src="https://github.com/user-attachments/assets/56eef6b9-8f8e-40e6-9e7f-957dfa9da59a" />
 

 <img width="975" height="696" alt="image" src="https://github.com/user-attachments/assets/41bead61-5125-4074-8929-f8dec70429c7" />

(theta topograph baseline 2 )

 <img width="975" height="740" alt="image" src="https://github.com/user-attachments/assets/35e2ac71-4bd9-4c64-be65-0a2bc68358bb" />


 <img width="975" height="796" alt="image" src="https://github.com/user-attachments/assets/4994efb7-f3cf-41a1-8ed7-84369c2138e8" />

(Alpha topograph 2 baseline)



<img width="975" height="808" alt="image" src="https://github.com/user-attachments/assets/804c5d14-f3e0-4ce1-8e4f-8583509528a1" />










<img width="975" height="796" alt="image" src="https://github.com/user-attachments/assets/b04d6b57-97ac-4ed9-93b6-8ac40972b062" />







 
 
(Sigma topograph baseline 2)

<img width="975" height="919" alt="image" src="https://github.com/user-attachments/assets/7b905b85-acc7-4d99-bd1f-fe3c0dd1b4f8" />

<img width="975" height="800" alt="image" src="https://github.com/user-attachments/assets/ec257228-f1f1-48c7-8b34-e6c841d797c2" />

 (Beta topography Baseline 2) 

 <img width="975" height="798" alt="image" src="https://github.com/user-attachments/assets/986b3554-3cd7-4364-a07d-400b31acdf07" />

<img width="975" height="921" alt="image" src="https://github.com/user-attachments/assets/805ef195-b820-43ea-8f4e-e300f5568d9a" />

 (Gamma Topograph Baseline 2)








<img width="919" height="518" alt="image" src="https://github.com/user-attachments/assets/43c234cb-ffa1-4f9e-b3e8-0b9864331690" />








<img width="866" height="843" alt="image" src="https://github.com/user-attachments/assets/fedb9a01-4023-46a5-9779-97194cb4e4ac" />









 
 
(Delta Topograph Treatment 1)
 

 <img width="975" height="644" alt="image" src="https://github.com/user-attachments/assets/2a55c0f0-0b68-4e3d-add7-78fc94decfa4" />

<img width="952" height="980" alt="image" src="https://github.com/user-attachments/assets/b256a411-08a4-4869-b8d0-a6c524728d72" />

(Theta topograph Treatment 1) 




<img width="975" height="592" alt="image" src="https://github.com/user-attachments/assets/0a82fed8-1936-4b60-9ddc-a08a9d1cad3f" />


<img width="948" height="980" alt="image" src="https://github.com/user-attachments/assets/3bea4a7c-0eec-41ce-9fd7-5da77b850d4e" />

(Alpha topograph  Treatment 1)

 <img width="892" height="900" alt="image" src="https://github.com/user-attachments/assets/2861d7f0-d8a1-427c-84d2-3152e5e2d91b" />


 <img width="942" height="980" alt="image" src="https://github.com/user-attachments/assets/2fb50599-bc42-47cd-aee0-e9bec2c89acc" />

(Beta Topograph Treatment 1) 

 <img width="791" height="900" alt="image" src="https://github.com/user-attachments/assets/2acafbdd-d01e-4ed4-95db-954c42987bc9" />

<img width="958" height="980" alt="image" src="https://github.com/user-attachments/assets/5788edf5-4aed-4ce7-beca-2b699534538c" />

(Gamma Topograph Treatment 1 ) 

<img width="975" height="679" alt="image" src="https://github.com/user-attachments/assets/c20e7513-8ede-49a6-9d0b-2b0231eaec03" />

<img width="952" height="980" alt="image" src="https://github.com/user-attachments/assets/cbfc0f80-5cdb-4634-99b1-e8655eff7bf8" />

 
(Sigma Topograph Treatment 1)

<img width="947" height="578" alt="image" src="https://github.com/user-attachments/assets/d3f866ae-1dba-4277-ae4f-989463a5fb6c" />

<img width="895" height="919" alt="image" src="https://github.com/user-attachments/assets/aa9a90e5-d991-450a-aa83-4960b94783b1" />

  
(Delta topography Treatment 2)

 <img width="975" height="552" alt="image" src="https://github.com/user-attachments/assets/dca21324-5e9f-40f2-8ebb-22f21f72b2f1" />


 <img width="958" height="980" alt="image" src="https://github.com/user-attachments/assets/8b6f76ca-867e-45cd-9a72-124849e03cbb" />

(Theta Topograph Treatment 2)

 <img width="947" height="688" alt="image" src="https://github.com/user-attachments/assets/eca45772-19ef-47ce-a201-92605fbda06c" />

<img width="798" height="835" alt="image" src="https://github.com/user-attachments/assets/e5935d44-6f4e-4f56-9f94-648916c39c07" />

  
(Alpha Topograph 2)
 

 <img width="975" height="548" alt="image" src="https://github.com/user-attachments/assets/81de7bb1-102d-4750-8d12-526a4f5b087f" />

<img width="964" height="980" alt="image" src="https://github.com/user-attachments/assets/1692d232-9412-4786-8912-ceae5f555704" />

(Beta topograph Treatment  2)

<img width="844" height="763" alt="image" src="https://github.com/user-attachments/assets/cbfd485f-a133-4250-806d-18bf78b60a5b" />

  <img width="952" height="971" alt="image" src="https://github.com/user-attachments/assets/f6722b9d-7ae0-470b-8cef-9826c0c6578d" />

(Sigma topograph Treatment 2)

 <img width="975" height="900" alt="image" src="https://github.com/user-attachments/assets/d8a544ce-7e39-4c7d-87c1-96fc1953ed06" />

<img width="975" height="990" alt="image" src="https://github.com/user-attachments/assets/96c00df1-9253-4baf-b769-563fd412e199" />

(Gamma Topograph Treatment 2)









### Normality testing
After looking at the raw data, I ran both the relative band power (baseline and treatment) and the absolute band power (in dB) through the one-sample Kolmogorov-Smirnov test. To do this, I turned each 5-minute time bin into its own data point, giving me several data points instead of one. In the Absolute KS test 1, every absolute (dB) value came out parametric (normal) — Delta, Theta, Alpha, Beta, Gamma, and Sigma, along with the SMR and DTABR ratios (all Asymp. Sig. > 0.05). On the corrected relative data, re-running the Kolmogorov-Smirnov test changed which bands counted as normal: Theta and Alpha came out parametric (normal) and were tested with independent-samples t-tests, while Delta, Beta, Gamma, and Sigma came out non-parametric and were tested with the Kruskal-Wallis test.

 <img width="975" height="288" alt="image" src="https://github.com/user-attachments/assets/94a191eb-7af6-4fd3-927d-602b245ffabc" />


(Absolute KS test 1) 
<img width="750" height="336" alt="image" src="https://github.com/user-attachments/assets/bae64a20-814a-4498-b110-5fe4bdaf0436" />

 
(Relative KS test 1)



























<img width="770" height="663" alt="image" src="https://github.com/user-attachments/assets/eff80927-900e-4eb0-8c39-567a611787a3" />

<img width="827" height="642" alt="image" src="https://github.com/user-attachments/assets/6e7ac79b-9724-4007-947c-373cd0205377" />


<img width="864" height="667" alt="image" src="https://github.com/user-attachments/assets/c7d8015e-a12e-4953-bf39-244a61bf942c" />

<img width="827" height="658" alt="image" src="https://github.com/user-attachments/assets/60adee69-32c5-4fa4-a457-5ac42da75cdd" />

<img width="822" height="663" alt="image" src="https://github.com/user-attachments/assets/1f6863c3-126a-4d59-8ada-ed9feb886109" />
<img width="784" height="672" alt="image" src="https://github.com/user-attachments/assets/28117cdb-597d-4520-9764-3458161e70d5" />
<img width="794" height="573" alt="image" src="https://github.com/user-attachments/assets/dc53f82b-8936-4260-8229-1934fd3a4c77" />
<img width="691" height="516" alt="image" src="https://github.com/user-attachments/assets/68b38d73-1347-4c1d-8433-332cd9843d8f" />

(EEG Histogram 1 )

<img width="975" height="562" alt="image" src="https://github.com/user-attachments/assets/3ddee108-7f20-45ad-ac28-c34d352d7f54" />
<img width="975" height="703" alt="image" src="https://github.com/user-attachments/assets/bd39c6f4-f972-410e-8477-95818b5508af" />


 <img width="975" height="703" alt="image" src="https://github.com/user-attachments/assets/9f9c5f34-fb39-4fd5-8e21-e4b229f199fb" />

 
<img width="975" height="744" alt="image" src="https://github.com/user-attachments/assets/012378bc-a717-455a-9baf-0d7eb9b71dad" />

<img width="975" height="354" alt="image" src="https://github.com/user-attachments/assets/d592e863-3af1-4892-93db-d16f5eedeed8" />

 
 

 
(EEG Histogram 2 — relative %, Alpha, Beta, Gamma & Sigma, N=40 combined; Gamma and Sigma were non-parametric per KS test)





























### Comparisons between treatment and control

The next analysis compared the treatment to the control through bar charts. Bar graph 1 shows the absolute band power in dB: every band was slightly lower in the treatment than the control, but none of the individual bands differed by much. The clearest differences were in the ratios — DTABR (sedation) was higher in the treatment, while SMR was higher in the control. Bar graph 2 shows relative power (corrected). The two parametric bands were Theta and Alpha: Alpha was significantly lower in the treatment (about 3.9% vs 5.1%), while Theta was slightly higher in the treatment and not significant. The non-parametric bands (Delta, Beta, Gamma, Sigma) were handled with Kruskal-Wallis: Delta was higher in the treatment (about 69% vs 63%) but not significant, Sigma was essentially equal (about 2.0% vs 1.7%), and Beta and Gamma ranked higher in the control.

![Corrected relative band power: Amanita vs baseline](corrected_results.png)

*(Corrected relative band power, independently reproduced from the corrected data. Alpha is significantly lower under Amanita, p = .023; Delta trends higher but is not significant, p = .109; Sigma is unchanged, p = .430; Beta and Gamma rank higher in the control, p = .039 / .036, but are fragile — see the statistical-tests section.)*

 <img width="602" height="980" alt="image" src="https://github.com/user-attachments/assets/11def5d5-eaf9-4d78-8c1b-3c2f27dce1ce" />

 
(Bar graph 1)
 
 
 <img width="552" height="539" alt="image" src="https://github.com/user-attachments/assets/baa1b7b4-c629-47a9-a23f-b3a00aae3494" />

 
(Bar Graph 2)























### Statistical tests

I did statistical tests to determine significance using t tests for parametric values and whitney u tests for non parametric.  For the absolute (dB) values in Independent samples 1, none of the individual bands reached significance: Delta (p = .649), Theta (p = .666), Alpha (p = .227), Beta (p = .215), Gamma (p = .061, a non-significant trend toward higher gamma in the control), and Sigma (p = .722) were all non-significant. The absolute ratios DTABR and SMR did reach significance (DTABR p = .019, SMR p = .023), but these are ratios computed from decibel values rather than linear power; recomputed with one consistent definition they are only marginal, so I no longer treat them as a strong sedation signature.

For the relative values (corrected), Alpha was significantly lower in the treatment (5.1% control vs 3.9% treatment; t = 2.37, p = .023, 95% CI of the difference 0.17–2.14 — but see the robustness note below: this alpha effect does **not** replicate when relative power is recomputed directly from the raw signal), while Theta was not significant (12.1% vs 13.4%, p = .338). The Kruskal-Wallis tests on the non-parametric bands: Delta was not significant (control 63.3% vs treatment 69.4%, χ² = 2.57, p = .109 — a non-significant trend toward more delta in the treatment); Sigma was not significant (1.7% vs 2.0%, χ² = 0.62, p = .430); Beta ranked significantly higher in the control (χ² = 4.27, p = .039), although the group means were nearly identical (6.2% vs 6.5%), so this reflects a few high-beta artifact windows inflating the treatment mean; and Gamma ranked higher in the control (11.6% vs 4.8%, χ² = 4.38, p = .036), though Muse gamma is heavily EMG/line-noise contaminated and should be read cautiously. These replace the earlier relative results (delta p = .003, alpha p = .017, sigma p < .001), which were driven by a baseline table that had not been recomputed.

**Robustness note (aggregation-sensitive effects).** The three significant workbook results — Alpha (t p = .023), Beta (KW p = .039), and Gamma (KW p = .036) — were stress-tested against the raw recordings using per-epoch-relative-then-average aggregation. Recomputing relative power from raw under 24 processing pipelines (epoch length 2/4/8 s × four artifact thresholds × mean/median aggregation), none of the three bands is significant: Alpha ≈ 7.1% vs 7.0% (t p = .949), Beta ≈ 8.4% vs 8.2% (t p = .927), Gamma ≈ 5.5% vs 5.0% (t p = .670). These effects are therefore specific to the dB-averaging aggregation used in the workbook and do not appear when standard aggregation is applied to the same raw signal. The bias introduced by the dB method is not uniform: for Gamma, it shifts the treatment estimate by −38% and the baseline estimate by +41% (in opposite directions), which explains why a group difference appears in the workbook but not in the from-raw analysis. See the Methods section and the Limitations section for further discussion of the aggregation choice.

![Alpha robustness check](robustness_alpha.png)

*(Each teal point is one of 24 from-raw pipelines; all sit on the equality line at ~7–8% for both nights. The orange star is the workbook's mean-dB aggregation — the only point showing a treatment/baseline gap, and the source of the p = .023 result.)*

<img width="825" height="965" alt="image" src="https://github.com/user-attachments/assets/557a1bd2-4db3-488e-8c36-6c113232644d" />

(Independent samples test 1) 

 <img width="675" height="387" alt="image" src="https://github.com/user-attachments/assets/9a470db4-f6fe-473b-8f28-22d87cfd3da3" />

(Kruskal-Wallis — relative Sigma & Gamma)

 <img width="900" height="697" alt="image" src="https://github.com/user-attachments/assets/a114abfa-ca6e-4a20-bc43-432a475b2f0a" />

(Independent samples t-test 2 — relative)
 


### Statistical power

> *Note: the effect sizes in this section (e.g., relative Delta d = 0.96, Sigma r = −0.95) are from the pre-correction analysis and no longer match the corrected results, where relative Delta and Sigma are non-significant. These power figures should be recomputed from the corrected effect sizes (Alpha is now the main significant effect); they are left here only to document the original calculation.*

Due to pseudoreplicartion statistical power is not particularly indicative of anything.  Overall I got mostly sufficiently powered tests showing that theres overall a high effect size. To get the statistical power I used the effect sizes from the real recomputed data. For the non-parametric bands I used the rank-biserial r converted to P(X>Y), and for the parametric bands I used the smallest significant Cohen’s d so I wasn’t cherry-picking the biggest effect. All power calculations used α = 0.05, two-tailed, with the smaller group size (n = 18) as the conservative estimate.For Sigma (rank-biserial r = −0.95, P(X>Y) = 0.025) the required sample size per group for 80% power is just 6, which we already exceed even with pseudoreplication — the effect is so large that very few observations are needed to detect it reliably. For Gamma (r = +0.06, P(X>Y) = 0.530) the power with n = 18 per group is only 0.0497 — basically nothing, which makes sense because P(X>Y) = 0.53 is indistinguishable from a coin flip.For the parametric bands I used the weakest of the significant medium effects, SMR at d = 0.71. With the current n = 18 per group, power is 0.645 (64.5%) — underpowered relative to the 80% convention. Reaching 80% power for an effect this size would require n = 33 per group. The stronger effects (relative Delta at d = 0.96, DTABR at d = 0.74) would need fewer participants, but I used the weakest one as the conservative benchmark.As before, all of these n values are for bins treated as independent samples, which is pseudoreplication. The real sample size here is one participant and one session per condition, so these power figures are best read as ‘how many sessions would be needed if the effect size held up’ rather than a formal power guarantee.


 
  
<img width="591" height="481" alt="image" src="https://github.com/user-attachments/assets/30422ed0-3ca9-4174-9f32-6fc2734364e1" />





<img width="591" height="509" alt="image" src="https://github.com/user-attachments/assets/2118ba64-21ea-426d-b0e9-834b6ba4f83a" />

<img width="975" height="544" alt="image" src="https://github.com/user-attachments/assets/ab500803-557a-450f-8a32-b2c46b7c5da6" />



(Stat power 1 — Gamma: P(X>Y)=0.530, power=0.050 at n=18 | Sigma: P(X>Y)=0.025, needs n=6 for 80% power)
 
  




 
 <img width="975" height="564" alt="image" src="https://github.com/user-attachments/assets/7bd3fb5f-6f8f-40fa-b54b-08f0fe61dbdd" />


(Stat power 2 — weakest significant parametric effect, SMR d=0.71: power=0.645 at n=18, needs n=33 for 80%)


## Conclusion:

So, despite my original assumptions, the corrected analysis shows a more modest picture than my first draft. In absolute (dB) terms there was a mild, broad, non-significant lowering of power across all bands in the treatment. In relative terms, delta dominated both nights and trended higher in the treatment (about 69% vs 63% of total power), but once the baseline was recomputed the same way as the treatment this difference was **not** significant (Kruskal-Wallis p = .109). The corrected workbook test flags alpha as lower in the treatment (about 5.1% → 3.9%, p = .023), but this was the last claim to fall: a from-raw robustness check (24 pipelines × 4 alpha band definitions) does **not** reproduce it — relative alpha is about 7–8% in both nights and never significant (0/24). That significant alpha comes from a biased aggregation (converting averaged decibels to relative power); computed the standard way it disappears. Relative sigma did not differ (p = .430), theta was a non-significant upward trend, and beta/gamma ranked higher in the control (p = .039 / .036) but are fragile (near-identical beta means; Muse gamma is EMG/line noise). So the honest bottom line from the corrected data is **no robust spectral difference between the two nights in any band** — the two recordings are spectrally very similar once analyzed faithfully. This is a null result for a single-session spectral drug signature, not the dramatic delta surge and sedation-ratio effects I originally reported, which did not survive correcting the baseline. The topographic maps hint that sigma was distributed a bit more frontally and less parietally in the treatment, but with only four electrodes this is speculative and cannot truly localize activity to specific lobes; I offer it only as a hypothesis for future, higher-density work.

On the corrected relative data, normality testing made Theta and Alpha parametric and Delta, Beta, Gamma, and Sigma non-parametric. Independent-samples t-tests found Alpha significantly lower in the treatment (p = .023) and Theta non-significant (p = .338). Kruskal-Wallis tests found Delta (p = .109) and Sigma (p = .430) non-significant, and Beta (p = .039) and Gamma (p = .036) higher in the control by rank. For the absolute (dB) values, no individual band differed significantly between conditions. Because each of these tests treats 5-minute bins as independent samples (pseudoreplication) from a single participant with one session per condition, they should be read as a single-subject, exploratory result, not a population-level finding.

## Limitations:

 The Muse is a consumer headset, meaning it is not as advanced as clinician-grade EEGs and doesn't have as many sensors as even more modern (post-2014) consumer EEG systems. It only has 4 sensors, substantially fewer than the standard 10-20 EEG system described by Jasper (1957).   There are also major artifacts, like at 85 minutes, some of the spikes may be due to movement, and because I set alarms in the treatment to know when I should mark down the time certain effects started,  

Another issue is that taking two doses of Amanita muscaria does not lead to getting the cleanest example of how it affects the brain once crossing the blood-brain barrier.

The biggest statistical flaw is pseudoreplication. Because I didn't have enough data for an ANOVA and didn't know how to properly run a time series, I ended up turning each time point into an individual data entry. This inflates N, and therefore the robustness percentage. This is pseudoreplication, and it is a major flaw in this research.

I also took Amanita during a busy day for me, so my brain was probably already at a higher power than normal.  Two datasets also only left me with a limited dataset, which makes it hard to extrapolate anything.  Amanita Muscaria's lack of consistent dosages in the wild also makes it harder to reproduce to an extent.  For the future, going up to 5-10 tests and using ethanol or some other GABAergic substance as a comparative group could be useful.  Also, changing the muse protocol from straight recording until the battery dies during sleep is probably not the best way to conduct this experiment.  The sigma theory also can't be exact due to limited data and only 4 electrodes on the Muse.   

In the future, I would like to iterate with awake tests and try to map the full peak and come down.

**Aggregation method and effect-size dependency.** The relative band power values in this study were derived by averaging absolute power in decibels across 5-minute bins and then converting back to linear power before normalizing to percentages (the dB-relative method). This is an atypical aggregation choice: the more commonly used method in the qEEG literature computes relative power for each epoch first and then averages the resulting percentages. Because the two approaches differ due to the nonlinearity of the log scale, all three statistically significant effects reported here — Alpha (p = .023), Beta (p = .039), and Gamma (p = .036) — are specific to the dB-averaging method and do **not** survive recomputation using the standard per-epoch-relative approach (Alpha p = .949, Beta p = .927, Gamma p = .670 from raw). The direction of the bias also varies: for Gamma, the dB method shifts the treatment estimate downward and the baseline estimate upward, artificially creating the appearance of a group difference. Future replications should specify their aggregation method explicitly and test sensitivity to this choice.   



