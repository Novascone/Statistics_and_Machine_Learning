import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats


male = np.array([[6,    180, 12],
                 [5.92, 190, 11],
                 [5.58, 170, 12],
                 [5.92, 165, 10]])

female = np.array([[5,    100,  6],
                   [5.5,  150,  8],
                   [5.42, 130,  7],
                   [5.75, 150,  9]])

sample1 = np.array([6,    130,  8])

sample2 = np.array([5.6,   167,  9])

maleHeight = male[:,0]
maleWeight = male[:,1]
maleFoot = male[:,2]

femaleHeight = female[:,0]
femaleWeight = female[:,1]
femaleFoot = female[:,2]

    
meanMaleHeight = np.mean(male[:,0])
meanMaleWeight = np.mean(male[:,1])
meanMaleFoot = np.mean(male[:,2])

meanFemaleHeight = np.mean(female[:,0])
meanFemaleWeight = np.mean(female[:,1])
meanFemaleFoot = np.mean(female[:,2])

stdMaleHeight = np.std(male[:,0])
stdMaleWeight = np.std(male[:,1])
stdMaleFoot = np.std(male[:,2])

stdFemaleHeight = np.std(female[:,0])
stdFemaleWeight = np.std(female[:,1])
stdFemaleFoot = np.std(female[:,2])

probabilityMaleFromTest = 0.5 # 4/8
probabilityFemaleFromTest = 0.5 # 4/8

probabilityHeightIsTheSample1HieghtGivenMale = stats.norm.pdf(sample1[0], meanMaleHeight, stdMaleHeight)
probabilityWeightIsTheSample1WeightGivenMale = stats.norm.pdf(sample1[1], meanMaleWeight, stdMaleWeight)
probabilityFoootIsTheSample1FootGivenMale = stats.norm.pdf(sample1[2], meanMaleFoot, stdMaleFoot)

probabilityHeightIsTheSample1HieghtGivenFemale = stats.norm.pdf(sample1[0], meanFemaleHeight, stdFemaleHeight)
probabilityWeightIsTheSample1WeightGivenFemale = stats.norm.pdf(sample1[1], meanFemaleWeight, stdFemaleWeight)
probabilityFoootIsTheSample1FootGivenFemale = stats.norm.pdf(sample1[2], meanFemaleFoot, stdFemaleFoot)

probabilityHeightIsTheSample2HieghtGivenMale = stats.norm.pdf(sample2[0], meanMaleHeight, stdMaleHeight)
probabilityWeightIsTheSample2WeightGivenMale = stats.norm.pdf(sample2[1], meanMaleWeight, stdMaleWeight)
probabilityFoootIsTheSample2FootGivenMale = stats.norm.pdf(sample2[2], meanMaleFoot, stdMaleFoot)

probabilityHeightIsTheSample2HieghtGivenFemale = stats.norm.pdf(sample2[0], meanFemaleHeight, stdFemaleHeight)
probabilityWeightIsTheSample2WeightGivenFemale = stats.norm.pdf(sample2[1], meanFemaleWeight, stdFemaleWeight)
probabilityFoootIsTheSample2FootGivenFemale = stats.norm.pdf(sample2[2], meanFemaleFoot, stdFemaleFoot)

probabilityMaleSample1 = probabilityMaleFromTest * probabilityHeightIsTheSample1HieghtGivenMale * probabilityWeightIsTheSample1WeightGivenMale * probabilityFoootIsTheSample1FootGivenMale
probabilityFemaleSample1 = probabilityFemaleFromTest * probabilityHeightIsTheSample1HieghtGivenFemale * probabilityWeightIsTheSample1WeightGivenFemale * probabilityFoootIsTheSample1FootGivenFemale

probabilityMaleSample2 = probabilityMaleFromTest * probabilityHeightIsTheSample2HieghtGivenMale * probabilityWeightIsTheSample2WeightGivenMale * probabilityFoootIsTheSample2FootGivenMale
probabilityFemaleSample2 = probabilityFemaleFromTest * probabilityHeightIsTheSample2HieghtGivenFemale * probabilityWeightIsTheSample2WeightGivenFemale * probabilityFoootIsTheSample2FootGivenFemale


print("Probability Male Sample1:", probabilityMaleSample1)
print("Probability Female Sample1:", probabilityFemaleSample1)
if probabilityMaleSample1 > probabilityFemaleSample1:
    print("We Classify Sample One as Male")
else:
    print("We Classify Sample One as Female")
print("Probability Male Sample2:", probabilityMaleSample2)
print("Probability Female Sample1:", probabilityFemaleSample2)
if probabilityMaleSample2 > probabilityFemaleSample2:
    print("We Classify Sample Two as Male")
else:
    print("We Classify Sample Two as Female")




# sns.displot(maleHeight, kind='kde')
# sns.displot(maleWeight, kind='kde')
# sns.displot(maleFoot, kind='kde')

# sns.displot(femaleHeight, kind='kde')
# sns.displot(femaleWeight, kind='kde')
# sns.displot(femaleFoot, kind='kde')

plt.show()