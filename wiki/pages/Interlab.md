# Interlab 
  
## Purpose 

We completed three calibrations, each of which measured standardised non-living samples provided by iGEM. These calibrations established absorbance and fluorescence baselines for further measurements, and gave a way to relate absorbance to number of E. coli-like particles. 

We then moved onto live E. coli, measuring the absorbance and fluorescence of populations carrying different GFP-encoding devices. It was possible to compute the fluorescence per cell for each device.

Lastly, we diluted E. coli cultures to a known absorbance, plated them on agar, and counted the resulting colonies. It was then possible to compare these results with the predictions made by our calibrations.

## Materials, Instrumentation, and Methods
E. coli strain K-12 DH5-alpha was the bacterial strain used.

The first calibration attempt used a Molecular Devices Model F5 reader and black 96-well plates with clear, flat bottoms. 

All subsequent measurements were completed using a BioTek Synergy 4 plate reader. It was configured as follows:
- Top Optics
- Pathlength correction turned off
- Temperature control turned off (room temperature)
- Sensitivity: 66
- 600 nm absorbance wavelength
- 485 nm fluorescence excitation wavelength
- 525 nm fluorescence emission wavelength

The methods in the iGEM 2018 Interlab Study Protocol were followed as closely as possible, with the exception of the following deviations:

- Calibration 2: Microsphere Protocol (Attempt #1)
  - 1.5 mL microfuge tubes were substituted for 2.0-mL tubes. The contents added to the tubes were exactly the same as specified in the procedure. 

- Calibration 2: Microsphere Protocol (Attempt #3)
  - Between attempts, 96-well plates were covered and sealed with parafilm for up to two days. 
  - Immediately before reading, we pipetted up and down in each well, then inserted into the plate reader and shook on “high” for 3 minutes. 

- Cell Measurement Protocol
  - The plates were shaken on “high” for 3 minutes prior to reading.
  - After picking two colonies from each transformant plate, we prepared frozen stock from each colony, then used the frozen stock to inoculate the 5-10 mL cultures.

- CFU protocol
  - The plates were shaken on “high” for 3 minutes prior to reading.
  - After picking two colonies from each transformant plate, we prepared frozen stock from each colony, then used the frozen stock to inoculate the 5-10 mL cultures.

## Results and Discussion
Up to three attempts were required for each calibration in order to produce good data. Fresh samples were prepared for each attempt. The first attempts at all calibrations were completed using the Molecular Devices Model F5 reader, but problems with the fluorescence readings on the Molecular Devices Model F5 reader meant that all subsequent attempts were completed using the BioTek Synnergy 4 plate reader. The cell measurement protocol and CFU protocol were completed exclusively using the BioTek Synnergy 4 plate reader.

### Calibration 1
Calibration #1 measured the absorbance at 600 nm of the provided LUDOX CL-X sample. This calibration served to establish a conversion factor (OD600/Abs600), which was used to transform Abs600 data to the equivalent OD600, as would be obtained from a spectrophotometer.

Four replicates were used, each with Milli-Q water as a blank. This calibration was attempted twice. 

The first attempt was conducted using the Molecular Devices Model F5 reader. The results are shown in figure 1.

[Insert figure 1] 

Fig. 1. Raw absorbance results of calibration #1 attempt #1.

Once problems with calibrations #2 and #3 dictated that the BioTek plate reader was going to be used instead of the Molecular Devices Model F5 reader, it was necessary to repeat calibration #1 with the BioTek plate reader for the sake of consistency. Therefore the second attempt at calibration #1 was conducted using the BioTek Synergy 4 plate reader (fig. 2). 

[Insert figure 2] 

Fig. 2. Raw absorbance results of calibration #1 attempt #2

This data differs from that obtained in attempt #1, but a different instrument was used to obtain the measurements, so this is expected. The OD600/Abs600 value obtained in attempt #2 was used in all subsequent experiments. 

### Calibration 2
Calibration #2 measured the Abs600 of a dilution series of monodisperse silica microspheres provided by iGEM in Milli-Q water. This is useful because silica microspheres share similar optical characteristics with cells. We were able to construct a standard curve relating Abs600 to particle concentration.

The first attempt was conducted using the Molecular Devices Model F5 reader, pipetting up and down in each well prior to reading. The absorbance plot (fig. 3) shows a strong positive correlation (R^2 = 0.9839), but there is visible deviation from a straight line. The relatively large error bars also show poor agreement between replicates. 

[Insert figure 3]

Fig. 3. Absorbance plot for calibration #2 attempt 1. Error bars represent standard deviation.

Along with the problems faced with fluorescence readings in calibration #3, these data factors helped inform the decision to switch to the BioTek Synnergy 4 plate reader. 

The second attempt was conducted using the BioTek Synergy 4 plate reader, pipetting up and down in each well prior to reading. The linear absorbance plot has a higher  R^2 value than the first attempt (R^2 = 0.9915), but there are still some visible deviations from linearity. However, the error bars tend to be much smaller, indicating better agreement between replicates.

[Insert figure 4]

Fig. 4. Absorbance plot for calibration #2 attempt 2. Error bars represent standard deviation.

In addition to the data’s lack of linearity, it was also noted that the wells did not appear to be well-mixed, with visible settling of particles even after pipetting up and down. We hypothesized that uneven settling of particulates caused deviations from the expected linear trend. This made us decide to use the plate reader’s shaking feature in order to provide more even mixing and to prevent settling. 

The third attempt was completed using all of the same specifications as the second, but the plate reader’s shake feature was used to shake the plate on “high” for 3 minutes prior to reading. The linear absorbance plot (fig. 5) has a better R^2 value than attempt 2 (R^2 = 0.9962), suggesting that shaking helped avoid settling. The error bars are also relatively small, indicating good agreement between replicates, as in attempt 2. 

[Insert figure 5]

Fig. 5. Absorbance plot for calibration #2 attempt 3. Error bars represent standard deviation.

### Calibration 3
Calibration #3 measured the fluorescence of a dilution series of fluorescein solution. Excitation and emission wavelengths of 485 nm and 525 nm respectively were used. Fluorescein is a small molecule with similar fluorescence characteristics to GFP, so these measurements allowed for the construction of a standard curve relating fluorescence to fluorophore concentration. 

The first attempt was completed using the Molecular Devices Model F5 reader. The linear fluorescence plot shows nearly constant fluorescence as a function of concentration. However, some noise is also present, resulting in an extremely low R^2 value of 0.0815. The error bars vary greatly in size, indicating large variations in the degree of agreement between replicates. 

[Insert figure 6]

Fig. 6. Fluorescence plot for calibration #3 attempt 1. Error bars represent standard deviation.

These results are not at all as expected. In general, fluorescence increases linearly as a function of concentration, so a linear relationship is expected. This is not observed in the recorded data. Furthermore, all fluorescence readings are extremely low. These factors therefore suggest a significant problem with the plate reader’s ability to measure fluorescence. 

This problem was the main reason for switching to the BioTek Synnergy 4 plate reader for all remaining attempts. 

The second attempt was completed using the BioTek Synnergy 4 plate reader. The linear fluorescence plot shows an extremely strong positive linear correlation (R^2 = 0.9999) between fluorescence and concentration. The error bars are also very small, indicating strong agreement between replicates. The data collected in this attempt is exactly as expected, so no further attempts were required. 

[Insert figure 7]
Fig. 7. Fluorescence plot for calibration #3 attempt 2. Error bars represent standard deviation.

### Cell Measurement Protocol 
This section of the protocol compared the fluorescence of E. coli DHS alpha transformants with each of six test devices and two controls. Two colonies of each transformant were picked and grown overnight in LB + Cm broth. They were then diluted to a provided target OD600 of 0.10, which was calculated to correspond to an Abs600 of 0.024. The fluorescence of each diluted sample was then measured with excitation and emission wavelengths of 485 nm and 525 nm respectively. These results are presented in figure 9. Fluorescence was measured immediately after dilution (0h) and after 6h incubation. 

[Insert figure 8]

Fig. 8. Absolute fluorescence of each control and device at t = 0h and t = 6h.

For each sample, the equivalent concentration of fluorescein per particle was then calculated using fluorescence and absorbance measurements, as well as the conversion factors calculated in the calibrations. This corresponds approximately to the concentration of fluorescein molecules that gives the same fluorescence as one bacterial cell. Greater values indicate higher expression of GFP for that device (figure 9).

[Insert figure 9]

Fig. 9. Equivalent fluorescein fluorescence per particle of each control and device at t = 0h and t = 6h.

The controls and devices all show different levels of fluorescence, with the negative control and device 3 being the lowest and devices 1 and 4 being the highest. Large variation in the size of error bars indicates that some devices showed good repeatability, while others (especially device 5) did not.

For all devices, the absolute fluorescence increases from t = 0h to t = 6h. The amount of increase varies from device to device. This result is as expected. Since turbidity increased over the six-hour incubation period, the number of cells must also have increased. GFP fluorescence is proportional to concentration, so it is expected that fluorescence should increase as the cells divide.

In contrast, equivalent fluorescein fluorescence per particle decreased over time. Although absolute fluorescence increased, the number of cells increased by a greater amount, so the fluorescence produced by each individual cell is less. Although one might expect cells to produce the same unit fluorescence regardless of number, biological phenomena such as plasmid loss may have occurred during the incubation period, reducing the expression of GFP by each cell. It is also possible that the rate of cell division was greater than the rate of GFP production, causing an effective dilution of GFP in each cell during cell division.

### CFU Protocol 
This protocol investigated the relationship between absorbance and colony-forming units. E. coli DHS alpha was transformed with the positive and negative control devices, and two colonies with each device were selected and grown overnight. Each overnight culture was then diluted to a given target absorbance. From the protocol’s guidelines and our calculated relationship between optical density and absorbance, the target absorbance was 0.024. 

The cultures were diluted further and spread onto LB agar + Cm plates, giving final dilution factors of 8x10^4, 8x10^5, and 8x10^6. The plates were incubated overnight and the colonies counted. This allowed calculation of CFUs per mL of Abs600 = 0.024 sample.

[Insert figure 10]

These data are relatively poor because of the very large error bars. These error bars are especially large for 8x10^6. This can be attributed to the very low colony counts on these plates, which were as low as 1 or 0 for some plates. Results drawn from such low colony counts are not statistically sound. 8x10^4 and 8x10^5 produced poor data for similar reasons, but the error is less extreme. However, some general conclusions may be drawn. 

For each device, the CFU/mL calculated using each dilution factor are mostly in agreement. In addition, for each device, the error bars all span a common range, inside of which the true CFU/mL count is presumed to reside. Despite the very large amount of uncertainty, this internal consistency suggests that the procedure was carried out correctly, but that the samples were too dilute to produce statistically meaningful data. If the experiment is repeated, less dilute samples should be plated to give higher colony counts. 

Excluding 8x10^6, the negative controls show overall fewer CFU/mL than the positive controls. This suggests that the positive control has a growth advantage over the negative in the environment tested. 

### Acknowledgements 
We would like to extend our most sincere gratitude to Prof. Raymond Legge (Dept. of Chemical Engineering, University of Waterloo) and Andrew Assatory, a graduate student working under Prof. Legge. These results would not have been possible without their assistance. Prof. Legge kindly allowed us to use his BioTek Synergy 4 plate reader on very short notice, and Andrew accommodated our use of the plate reader into his busy schedule.


