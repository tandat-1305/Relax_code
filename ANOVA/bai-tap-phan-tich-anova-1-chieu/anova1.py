from scipy import stats
import pandas as pd
import numpy as np
# 
# 
#Kolmogorov
def Kolmogorov(data):
    print("Kiểm định Kolmogorov:", data.name)
    k, p = stats.kstest(rvs=data, cdf='norm', args=(np.mean(data), np.std(data)))
    if p > 0.05:
        print("Dữ liệu tuân theo luật phân phối chuẩn")
    else:
        print("Dữ liệu không tuân theo luật phân phối chuẩn")
# 
#    
# Shapiro
def Shapiro(data):
    print("Kiểm định Shapiro :", data.name)
    st, pv = stats.shapiro(data)
    if pv > 0.05:
        print("Dữ liệu tuân theo luật phân phối chuẩn")
    else:
        print("Dữ liệu không tuân theo luật phân phối chuẩn")
# 
# 
# Bartlett
def bartlett(a, b, c, d): 
    print("Kiểm định Bartlett: ",end="\n ")
    st, pv = stats.bartlett(a, b, c, d)
    print("Statistic =", st, "\n",
          "pvalue =", pv)
    if pv > 0.05:
        print("Các features đồng nhất về phương sai")
    else:
        print("Các features không đồng nhất về phương sai")
# 
#     
#Levene
def levene(a, b, c, d, e):
    print("Kiểm định Levene: ",end="\n")
    st, pv = stats.levene(a, b, c, d, e)
    if pv > 0.05:
        print("Các features đồng nhất về phương sai")
    else:
        print("Các features không đồng nhất về phương sai")
# 
#Kiểm định ANOVA x1->x4
def anova1_4(a, b, c, d):
    print("Kiểm định ANOVA: ",end="\n" )
    st, pv = stats.f_oneway(a, b, c, d)
    print("Stat =", st, "\n", "pvalue =", pv)
    if pv < 0.05:
        print("Có bằng chứng để bác bỏ giả thuyết H0")
    else:
        print("Chưa có bằng chứng để bác bỏ giả thuyết H0")
# 
#         
#Kiểm định ANOVA x1->x5
def anova1_5(a, b, c, d, e):
    print("Kiểm định ANOVA: ", end="\n")
    st, pv = stats.f_oneway(a, b, c, d, e)
    print("Stat =", st, "\n", "pvalue =", pv)
    if pv < 0.05:
        print("Có bằng chứng để bác bỏ giả thuyết H0")
    else:
        print("Chưa có bằng chứng để bác bỏ giả thuyết H0")
# 
# 
# 
# 
#
# Câu 1: Excavation Depth and Archaeology
# Four different excavation sites at an archeological area in New Mexico gave the following depths (cm) for significant archaeological discoveries.
# X1 = depths at Site I
# X2 = depths at Site II
# X3 = depths at Site III
# X4 = depths at Site IV 
df1 = pd.read_excel("D:\\Python\\bai_tap_relax\\ANOVA\\owan01.xls")
print("Owan01 Table")
print(df1)
ow01_1 = df1['X1']
ow01_2 = df1['X2']
ow01_3 = df1['X3']
ow01_4 = df1['X4']

print(Kolmogorov(ow01_1))
print(Kolmogorov(ow01_2))
print(Kolmogorov(ow01_3))
print(Kolmogorov(ow01_4))
print(bartlett(ow01_1, ow01_2, ow01_3, ow01_4))
print(anova1_4(ow01_1, ow01_2, ow01_3, ow01_4))
print("-----------------------------------------------------------")
# 
# 
# 
# 
#
# Câu 2: Excavation Depth and Archaeology Four different excavation sites at an archeological area in New Mexico gave the following depths (cm) for significant archaeological discoveries.
# X1 = depths at Site I
# X2 = depths at Site II
# X3 = depths at Site III
# X4 = depths at Site IV Reference: Mimbres Mogollon Archaeology by Woosley and McIntyre, Univ. of New Mexico Press

df2 = pd.read_excel("D:\\Python\\bai_tap_relax\\ANOVA\\owan02.xls")
print("Owan02 Table")
print(df2)
ow02_1 = df2['X1']
ow02_2 = df2['X2']
ow02_3 = df2['X3']
ow02_4 = df2['X4']

print(Kolmogorov(ow02_1))
print(Kolmogorov(ow02_2))
print(Kolmogorov(ow02_3))
print(Kolmogorov(ow02_4))
print(bartlett(ow02_1, ow02_2, ow02_3, ow02_4))
print(anova1_4(ow02_1, ow02_2, ow02_3, ow02_4))
print("-----------------------------------------------------------")
# 
# 
# 
# 
#
# Câu 3: Red Dye Number 40 S.W. Laagakos and F. Mosteller of Harvard University fed mice different doses of red dye number 40 and recorded the time of death in weeks. Results for female mice, dosage and time of death are shown in the data
# X1 = time of death for control group
# X2 = time of death for group with low dosage
# X3 = time of death for group with medium dosage
# X4 = time of death for group with high dosage Reference: Journal Natl. Cancer Inst., Vol. 66, p 197-212
df3 = pd.read_excel("D:\\Python\\bai_tap_relax\\ANOVA\\owan03.xls")
print("Owan03 Table")
print(df3)
ow03_1 = df3['X1']
ow03_2 = df3['X2']
ow03_3 = df3['X3']
ow03_4 = df3['X4']

print(Kolmogorov(ow03_1))
print(Kolmogorov(ow03_2))
print(Kolmogorov(ow03_3))
print(Kolmogorov(ow03_4))
print(bartlett(ow03_1, ow03_2, ow03_3, ow03_4))
print(anova1_4(ow03_1, ow03_2, ow03_3, ow03_4))
print("-----------------------------------------------------------")
# 
# 
# 
# 
#
# Câu 4: Business Startup Costs The following data represent business startup costs (thousands of dollars) for shops.
# X1 = startup costs for pizza
# X2 = startup costs for baker/donuts
# X3 = startup costs for shoe stores
# X4 = startup costs for gift shops
# X5 = startup costs for pet stores Reference: Business Opportunities Handbook
df4 = pd.read_excel("D:\\Python\\bai_tap_relax\\ANOVA\\owan04.xls")
print("Owan04 Table")
print(df4)
ow04_1 = df4['X1']
ow04_2 = df4['X2']
ow04_3 = df4['X3']
ow04_4 = df4['X4']
ow04_5 = df4['X5']

print(Shapiro(ow04_1))
print(Shapiro(ow04_2))
print(Shapiro(ow04_3))
print(Shapiro(ow04_4))
print(Shapiro(ow04_5))
print(levene(ow04_1, ow04_2, ow04_3, ow04_4, ow04_5))
print(anova1_5(ow04_1, ow04_2, ow04_3, ow04_4, ow04_5))
print("-----------------------------------------------------------")
# 
# 
# 
# 
#
# Câu 5: Weights of Football Players The following data represent weights (pounds) of a random sample of professional football players on the following teams.
# X1 = weights of players for the Dallas Cowboys
# X2 = weights of players for the Green Bay Packers
# X3 = weights of players for the Denver Broncos
# X4 = weights of players for the Miami Dolphins
# X5 = weights of players for the San Francisco Forty Niners Reference: The Sports Encyclopedia Pro Football
df5 = pd.read_excel("D:\\Python\\bai_tap_relax\\ANOVA\\owan05.xls")
print("Owan05 Table")
print(df5)
ow05_1 = df5['X1']
ow05_2 = df5['X2']
ow05_3 = df5['X3']
ow05_4 = df5['X4']
ow05_5 = df5['X5']

print(Shapiro(ow05_1))
print(Shapiro(ow05_2))
print(Shapiro(ow05_3))
print(Shapiro(ow05_4))
print(Shapiro(ow05_5))
print(levene(ow05_1, ow05_2, ow05_3, ow05_4, ow05_5))
print(anova1_5(ow05_1, ow05_2, ow05_3, ow05_4, ow05_5))
