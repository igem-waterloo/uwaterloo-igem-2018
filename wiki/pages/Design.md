It’s been a long journey from ideas, to research sessions, design, failure, redesign, and redesign. One question lead to another. In this page, we explain our system development and experimental design processes, and the reasoning behind the decisions we made along the way. Question by question, answer by answer, we invite you to learn more about this process.

## Major Goals of the Project

-   Create a stable co-culture system 
-   Be able to maintain the co-culture at any desired ratio 

## System Development
### Q: How do we control growth rates? 
####    A: By controlling metE expression.

Our project aims to maintain a stable co-culture by addressing the problem of competition between different microbial populations. We wanted to address this by regulating growth. We considered doing this in two ways:
- To kill cells in a population when it starts to outcompete the other
- To slow the growth of one population and allow the other to catch up

Through our research, we came up with one method for each option. 
The first method involved expressing HipA, a serine/threonine protein kinase toxin, in the _Escherichia coli_ (_E. coli_) population with the faster growth rate. This would begin to kill some of the culture which in turn would allow the slower culture to catch up, thereby maintaining the co-culture.    

The other method considered was to control the methionine production within the cell by controlling the metE gene. This gene is necessary for methionine biosynthesis. In a medium that lacks methionine, this gene becomes essential for growth. By controlling this gene’s expression, we can cut off the fast-growing population’s  supply of methionine to allow the slower population to catch up.

We decided to control the expression of metE in order to create our co-culturing system because it provides more dynamic control and a faster response from the cells once a command is given. Let’s say you have a co-culture with two bacterial populations: A and B. Population A starts out-growing the other so you turn off its metE production long enough to allow population B to catch up. But what if population B starts overgrowing? What if you want to change the ratio to now increase population A? If you had killed cells, it would take longer to get the few population A cells remaining to start dividing than it would if the cells were there all along, but simply arrested. Therefore, controlling MetE expression would allow us to control the growth rate of our populations. 

### Q: How do we control metE expression? 
#### A: Via optogenetic systems. 
In order to control the expression of two cultures independently of one another, we needed two different light-activatable systems, also known as optogenetic systems. We found a CcaS/CcaS system which is activated by green light and shut off by red light, used by the Kammash Lab. [1] By putting a CcaS/CcaR-responsive promoter in front of metE, we could promote its expression with green light and slow cell growth  with red light. We decided to use this system because other research groups had verified that it worked to control the expression of MetE and  to control cell growth. [1,2]

The second system that we wanted to use was a blue light activated system, so that we could control both populations independently and simultaneously. We found two systems that used blue light: the pDawn and Opto-T7 RNA polymerase systems. We prefered Opto-T7 because its response time, or the time it takes after the light is shined to start seeing an effect, is faster and closer to that of CcaS/CcaR. Therefore, we thought Opto-T7 would be a better fit with our existing red/green light system. Unfortunately, due to an inability to acquire the OptoT7 plasmids in time, we decided to use the pDawn system.

### Q: How do we monitor different populations in a co-culture? 
#### A: Fluorescence and flow cytometry. 
The next question to be answered was how to monitor the relative quantities of both populations in our co-culture. In order to know which lights to shine, and thus which population’s growth to encourage, we would need to obtain data on the relative abundance of the two populations. This data would need to be collected in real time so that we could modulate the light in response to any changes without disturbing the desired co-culture ratio. In order to do this, we decided to add a fluorescent protein marker to each population, RFP to one and GFP to the other, then detect the relative abundance of each culture using a flow cytometer. The flow cytometer allows almost real-time data collection and is far faster than plating cells and waiting for them to grow overnight. After some testing, we decided to change the plan to monitoring one culture using GFP and the other culture with no fluorescent protein, through flow cytometry. We decided this because our flow cytometer only contained a 488 nm laser, which was good at exciting GFP but not RFP, and it would be much simpler to collect data without RFP.

#### A (Alternative): Our robot!
However, using flow cytometry for measurements requires manual sampling, which is laborious and can be time consuming as we may need to take samples as often as every ~20 minutes.  As well, flow cytometers are expensive, which would make it difficult for other labs to replicate out setup. We aim for this system to work in any lab, and therefore we began to design an automated cell-sampling and fluorescence measurement system, which resulted in a collaboration between our math and lab subteams. 
In the lab we have a turbidostat that was built in-house, and which is the prototype for a design that collaborators with our supervising professor’s lab hope to take on to the market.  The turbidostat monitors and maintains the optical density of the cell culture by diluting the cultures in the sample vials and removing the excess population. The turbidostat is also capable of subjecting cell populations to time-varying light input capable of inducing our optogenetic systems.
Our automated fluorescence measuring system is based on monitoring the fluorescence of the cell culture, similar to the function of a flow cytometer.  As previously mentioned, the  turbidostat removes the excess volume after dilution.  From this “waste”, we can take samples to measure their fluorescence, which accurately represents the fluorescence hence the population ratios in the system. This sampling can be automated by using a vacuum pump and manifold to extract from the waste vial that is connected to the main system and pump the sample into the sampling vial and then, after the measurements have been taken, remove the sample from the sampling vial into the final waste vial so that a new measurement can be taken.  
The fluorescent measurements were taken by shining an LED at the sample to excite the GFP and then either a photo was taken with a phone camera or a measurement was taken with a photodiode connected to an Arduino. From this data, we can determine the population ratios in our co-culture.
Additionally, a box for holding the various components of our measurement system was designed for 3D printing.  The box’s role was to hold every part in place at the same distance for every measurement to maintain consistency in the experiments as well as to prevent ambient light from affecting the results.  Dimensions of the box and placement of the components was determined in an experiment described in our results page.


## Project Re-work

The experimental design described above is how we originally planned to carry out our project, in order to develop a system which was able to maintain a co-culture at specified ratios. Unfortunately, due to issues that arose with some of the light activated systems and time constraints, we had to rework the project design in order to complete our work in time. 
We removed the blue light system entirely since we could not assemble it fast enough. Instead, we decided to focus only on the CcaS/CcaR system. Our revised co-culture involves engineering our faster-growing _E. coli_ population (JT2) to be controlled by CcaS/CcaR, and leaving our slower-growing _E. coli_ population (DH5𝛂) uncontrolled.  This allowed us to continue to pursue the core objective of our project: to create a stable co-culture, while removing some of the complexity so that we could finish on time. 

## Experimental Design

### Q: Is methionine shared between cells/populations? 

Initially, we thought of growing the two populations together in a methionine dropout medium, but we quickly realized that this would not work. If one population outgrew the other, we wouldn’t be able to tell if this was due to differences in methionine availability, competition for other nutrients, or a difference in growth rates. This was a major downfall because one of the main reasons we pursued this project was to maintain co-cultures of populations that had different growth rates.

Another idea we proposed was to separate the populations within the medium, using a membrane to physically split the tube in half. The pores would be large enough to allow for exchange of any methionine excreted, but small enough to prevent cells from crossing. However, using a membrane would prevent us from being able to stir our co-culture from within, and shaking the tube could potentially dislodge the membrane.

Finally, we decided to grow the methionine-producing population in a methionine-deficient medium, filter the cells out, then re-inoculate the medium with cells that couldn't produce methionine. If methionine was secreted by the first population, it would be present in the medium post-filtration, allowing growth of the second population. 

In these experiments, we’re using JT2, an E. coli strain that has the MetE gene under control of the CcaS/R promoter, but behaves as a methionine auxotroph without CcaS/R plasmids. The methionine-producing population is transformed to contain CcaS/R and is exposed to light (such that MetE is expressed). The non-producing population is empty, or non-transformed, JT2.  
	
We did not expect our experimental sample, empty JT2 in the filtrate described above, to grow. Yet, several controls were needed to ensure that the lack of growth was indeed due to a lack of methionine. Each one sought out to test a different question/ possibility:

- Did JT2 simply not grow because there were not enough nutrients (other than methionine) in the filtrate? That is, if methionine is available in excess, does the filtrated used M9 medium have sufficient nutrients left to support growth? 
  - We tested this by 
     - re-inoculating a sample of filtrate with methionine-producing cells  
   - adding methionine to 
     - a sample of filtrate and inoculating it with empty JT2 
     - a sample of M9 (made without M9) and inoculating it with empty JT2   
 - Is the methionine we’re adding contaminated? 
   - We tested this by adding methionine to fresh M9 stock (that wasn’t inoculated with anything) 
 - Is our initial M9 stock contaminated with methionine?
   - We tested this by inoculating a sample of fresh M9 stock with empty JT2 
 - Did we effectively remove all the methionine-producing cells with our filtration method? Is the M9 used filtrate contaminated?
   - We tested this with a sample of filtrate that we did not inoculate with anything (if growth is seen, it is pre-existing contamination) 

### Q: What is the metabolic load of MetE (over)expression? 

In theory, the expression of recombinant proteins can slow the growth of bacterial strains by occupying the protein synthesis machinery of the cell. The expression of MetE in the JT2 strain has a previously discussed positive impact that speeds up cell growth, but it is also possible that MetE expression at high levels can have a negative impact on growth. This could result in a complicated and unwanted pattern in growth rate versus MetE expression levels.

In order to test whether or not MetE expression at high levels could negatively affect cells, the team conducted an experiment. JT2 cells containing the CcaS/CcaR system were grown in M9 media that included methionine under different light conditions. Since the medium included methionine, the expression of MetE had no rescuing effect and had a purely negative impact. If cells grew faster under red light, there would be strong evidence that high expression of MetE had a negative effect.

### Q: Can we reliably measure 2 populations in co-culture?

To ensure that flow cytometry can accurately distinguish between fluorescent and non-fluorescent cells and report a population ratio, we compared it to pour plating. A fluorescent (containing Green Fluorescent Protein, GFP) and non-fluorescent strain were grown up separately overnight, diluted to have roughly the same optical density and different volumes of each were mixed (to obtain different ratios of fluorescent to non-fluorescent). 

### Q: Can we control growth with red and green light? 

The control of population growth is the ultimate goal of our project. After the metabolic load of MetE was tested we were able to test the optogenetic control of population growth. When green light is on the population we should get MetE expression which will cause an increase in growth. When red light is on there should not be MetE expression and there will be minimal or reduced growth.

In order to test that we could control the growth of our populations with red and green light we conducted an experiment. JT2 cells containing the Ccas/Ccar system were grown in M9 media without any methionine. As there was no methionine in the media, the expression of MetE was the only way the cell could get methionine. Half the population was put in the incubator with green light, while the other half was put in the incubator with red light. The population in green light should have increased growth and the population in red light should have minimal growth. If this is the case then it would be evidence that we are able to control growth with red and green light.

## References

[1] A. Milias-Argeitis, M. Rullan, S. K. Aoki, P. Buchmann, and M. Khammash, “Automated optogenetic feedback control for precise and robust regulation of gene expression and cell growth,” Nature Communications, vol. 7, p. 12546, 2016.

[2] E. A. Davidson, A. S. Basu, and T. S. Bayer, “Programming Microbes Using Pulse Width Modulation of Optical Signals,” Journal of Molecular Biology, vol. 425, no. 22, pp. 4161–4166, 2013
