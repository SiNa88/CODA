import numpy
from operator import itemgetter  

microservices0 = ["encoding", "framing", "lowAccuracy", "highAccuracy", "transcoding", "analysis", "packaging"]


microservices = ["encoding", "highAccuracy" , "transcoding"]

#             EGS   Lenovo NvJ   RPi4  RPi3
encode_200  = [0.17,0.33,1.9,2.16, 2.5] #seconds
encode_1500 = [0.36,0.42,2.63,3.19,7.35] #seconds
encode_3000 = [0.47,0.59,3.48,4.4,8.44] #seconds
encode_6500 = [1.22,1.59,9.68,11.8,22.7] #seconds
encode_20000 = [2.69,3.16,20.64,28,60] #seconds

#                     EGS Lenovo NvJ  RPi4 RPi3   
Low_accuracy_training_model = [16.99, 17.8 , 151.4  , 101.864 , 1000] #seconds
High_accuracy_training_model = [33.23, 56.746 , 232.253 , 466.830 , 1000] #seconds



#              0	 1	2     3     4 
resources = ["vm1-cdc","t-1","e-0","e-1","e-2"]

# From: https://link.springer.com/chapter/10.1007/978-3-030-03596-9_14
#lat = [85e-3,60e-3,25e-3,22e-3,27e-3,21e-3,13e-3,17e-3,9e-3,28e-3,43e-3,21e-3,1e-3,1e-3] #ms
lat = [85e-3,60e-3,60e-3,60e-3] #ms
#print (len(lat))


#https://aws.amazon.com/kinesis/data-firehose/pricing/?nc=sn&loc=3

index_of_segment = 4

seg_size = [286720, 2457600, 3440640, 14400000, 20971520 ] #bits
video_size = [2000000, 14000000, 28000000, 60000000, 204800000] #bits

'''
Twitter = 280 Characters = 560 Bytes
real_seg_size = [30, 312, 460, 1531, 2950 ]  #(KB)  #Frame_size
seg_size = [35, 300, 420, 1350, 2560 ]  #(KB)  #Frame_size
video_size = [250, 1750, 3500, 7500, 25600]  #(KB)

Time_commu_Lenovo_AWSFrank = [113, 115, 120, 140, 150] #sec
Time_commu_Lenovo_EGS = [74, 76, 76, 78, 79] #sec
Time_commu_Lenovo_RPi4 = [65, 66, 66, 74, 80] #sec
Time_commu_Lenovo_NJN  = [79, 80, 82, 82, 86] #sec

thrput_commu_Lenovo_AWSFrank = [0.9 , 3 , 4 , 10 , 15] #(MB/s)
thrput_commu_Lenovo_EGS = [10 , 33 , 38 , 53 , 59] #(MB/s)
thrput_commu_Lenovo_RPi4 = [9 , 29 , 31 , 35 , 38] #(MB/s)
thrput_commu_Lenovo_NJN = [6 , 20 , 23 , 42 , 49] #(MB/s)
'''

Time_commu_Lenovo_AWSFrank = [113, 115, 120, 140, 150] #sec
Time_commu_Lenovo_EGS = [74, 76, 76, 78, 79] #sec
Time_commu_Lenovo_RPi4 = [65, 66, 66, 74, 80] #sec
Time_commu_Lenovo_NJN  = [79, 80, 82, 82, 86] #sec

thrput_commu_Lenovo_AWSFrank = [0.9*8000000 , 3*8000000 , 4*8000000 , 10*8000000 , 15*8000000] #(MB/s) -> (b/s)
thrput_commu_Lenovo_EGS = [10*8000000 , 33*8000000 , 38*8000000 , 53*8000000 , 59*8000000] #(MB/s) -> (b/s)
thrput_commu_Lenovo_RPi4 = [9*8000000 , 29*8000000 , 31*8000000 , 35*8000000 , 38*8000000] #(MB/s) -> (b/s)
thrput_commu_Lenovo_NJN = [6*8000000 , 20*8000000 , 23*8000000 , 42*8000000 , 49*8000000] #(MB/s) -> (b/s)

#Number of frames per video
SIZE = 208

#      EGS   Lenovo NvJ   RPi4  RPi3
BW_r = [60000000 , 920000000, 450000000 , 800000000 , 328000000]#bps


#0.015 - 0.8 ms
#65 - 85 ms
#Cloud, Tier2, Tier1(Vienna), Barcelona, Amsterdam, Paris, Brussels, Frankfurt, Graz, Ljubljana, London, Stockholm, Vienna 
#		0  1  2  3  4  5  6 7  8  9 10 11 12


# To be comparable with bw and cpu ratios.
lambda_in = [1,1,1,1]
lambda_out = [1,1,1,1]


dictlistResources = list( {} for i in range(len(resources)) )
sorted_dictlistResources = list( {} for i in range(len(resources)) )
dictlistMicroservices = list( {} for i in range(len(microservices)) )
sorted_dictlistMicroservices = list( {} for i in range(len(microservices)) )



T = [[0] * len(resources) for i in range(len(microservices))]
sum = 0
T[0][0] = encode_20000[0] + ((video_size[4])/BW_r[0]) + (lat[0] + lat[1]) + (lat[0] + lat[1])
T[0][1] = encode_20000[1] + ((video_size[4])/BW_r[1]) + (lat[1]) + (lat[1])
T[0][2] = encode_20000[2] + ((video_size[4])/BW_r[2]) + (1e-3)
T[0][3] = encode_20000[3] + ((video_size[4])/BW_r[3]) + (1e-3)

'''
T[1][0] = Low_accuracy_training_model[0] + (60*(seg_size[index_of_segment])/BW_r[0]) + (lat[0] + lat[1]) + (lat[0] + lat[1])
T[1][1] = Low_accuracy_training_model[1] + (60*(seg_size[index_of_segment])/BW_r[1]) + (lat[1]) + (lat[1])
T[1][2] = Low_accuracy_training_model[2] + (60*(seg_size[index_of_segment])/BW_r[2]) + (1e-3) + (1e-3)
T[1][3] = Low_accuracy_training_model[3] + (60*(seg_size[index_of_segment])/BW_r[3]) + (1e-3) + (1e-3)
'''

T[1][0] = High_accuracy_training_model[0] + (60*(seg_size[index_of_segment])/BW_r[0]) + (lat[0] + lat[1]) + (lat[0] + lat[1])
T[1][1] = High_accuracy_training_model[1] + (60*(seg_size[index_of_segment])/BW_r[1]) + (lat[1]) + (lat[1])
T[1][2] = High_accuracy_training_model[2] + (60*(seg_size[index_of_segment])/BW_r[2]) + (1e-3) + (1e-3)
T[1][3] = High_accuracy_training_model[3] + (60*(seg_size[index_of_segment])/BW_r[3]) + (1e-3) + (1e-3)


T[2][0] = encode_20000[0] +  (60*(seg_size[index_of_segment])/BW_r[0]) + (lat[0] + lat[1]) + (lat[0] + lat[1])
T[2][1] = encode_20000[1] +  (60*(seg_size[index_of_segment])/BW_r[1]) + (lat[1]) + (lat[1])
T[2][2] = encode_20000[2] +  (60*(seg_size[index_of_segment])/BW_r[2]) + (1e-3) + (1e-3)
T[2][3] = encode_20000[3] +  (60*(seg_size[index_of_segment])/BW_r[3]) + (1e-3) + (1e-3)



print()
for i in range(len(microservices)):
	for j in range(len(resources)):		
		dictlistMicroservices[i][(microservices[i],resources[j])] = numpy.round((T[i][j]),4)

#sorted(iterable, *, key=None, reverse=False)
for i in range(len(microservices)):
	sorted_dictlistMicroservices[i]=sorted(dictlistMicroservices[i].items(),key = itemgetter(1))
	##print (sorted_dictlistMicroservices[i])
	##print ()

#print (sorted(dictlistMicroservices.items(),key = itemgetter(1)))
for j in range(len(resources)):
	for i in range(len(microservices)):
		dictlistResources[j][(microservices[i],resources[j])] = numpy.round((BW_r[j])- ( 60*(seg_size[index_of_segment])),4)
	sorted_dictlistResources[j]=sorted(dictlistResources[j].items(),key = itemgetter(1))
	##print (sorted_dictlistResources[j])
	##print ()


summatching = [0 for i in range(3)]
sumedge = [0 for i in range(3)]
sumcloud = [0 for i in range(3)]
max_summatching = 0	
max_sumedge = 0
max_sumcloud = 0	
'''
#			0	  1	           2              3
microservices = ["encoding", "lowAccuracy", "highAccuracy ", "transcoding"]
#		0	1      2     3     4     
resources = ["vm1-cdc","t-2","e-0","e-1","e-2"]
'''

summatching = 0
sumcp = 0
sumcloud = 0
sumrtrrp = 0

if(T[0][1] != 0 and T[1][0] != 0 and T[2][1] != 0 ):
		summatching = T[0][1] + T[1][0] + T[2][1] - (2*lat[1]) - (2*lat[1]) 

if(T[0][2] != 0 and T[1][1] != 0 and T[2][0] != 0 ):
		sumcp = T[0][2] + T[1][1] + T[2][0]     - (2*lat[1])
	
if(T[0][0] != 0 and T[1][1] != 0 and T[2][1] != 0 ):
		sumrtrrp = T[0][0] + T[1][1] + T[2][1]  - (2*lat[1]) - (2*lat[1])

if(T[0][0] != 0 and T[1][0] != 0 and T[2][0] != 0 ):
		sumcloud = T[0][0] + T[1][0] + T[2][0]  - ((2*lat[0]) +(2*lat[1])) - ((2*lat[0]) +(2*lat[1]))

print()
print("------------------Time------------------")
print("CODA: "    ,numpy.round(summatching,4))
print("CloudPath: "    ,numpy.round(sumcp,4))
print("RTR-RP: "   ,numpy.round(sumrtrrp,4))
print("CloudOnly: "   ,numpy.round(sumcloud,4))
print("----------------------------------------")
print()

print()

'''print("------------------Traffic---------------")
sum_traffic_matching = 0
for i in range(SIZE):
	sum_traffic_matching += ((seg_size[index_of_segment])+(seg_size[index_of_segment]))#+(seg_size[4])
sum_traffic_matching+=video_size[4]
print ("CODA: ", numpy.round(sum_traffic_matching/1024/1024/8,0) , "MB")


sum_traffic_cp = 0
for i in range(SIZE):
	sum_traffic_cp += ((seg_size[index_of_segment])+(seg_size[index_of_segment])+(seg_size[index_of_segment]))
sum_traffic_cp+=video_size[4]
print ("CloudPath: ", numpy.round(sum_traffic_cp/1024/1024/8,0) , "MB")


sum_traffic_cloud = 0
for i in range(SIZE):
	sum_traffic_cloud += ((seg_size[index_of_segment])+(seg_size[index_of_segment]))
sum_traffic_cloud+=video_size[4]
print ("CloudOnly: ", numpy.round(sum_traffic_cloud/1024/1024/8,0) , "MB")


sum_traffic_rtrrp = 0
for i in range(SIZE):
	sum_traffic_rtrrp += ((seg_size[index_of_segment])+(seg_size[index_of_segment]))#+(seg_size[index_of_segment]))
sum_traffic_rtrrp+=video_size[4]
print ("RTR-RP: ", numpy.round(sum_traffic_rtrrp/1024/1024/8,0) , "MB")
print("----------------------------------------")
print()
'''
print("------------------TrafficIntensity---------------")
sum_traffic_matching = 0
for i in range(SIZE):
	sum_traffic_matching += ((seg_size[index_of_segment]/thrput_commu_Lenovo_EGS[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_AWSFrank[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_AWSFrank[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_EGS[index_of_segment]))
sum_traffic_matching+=(video_size[index_of_segment]/thrput_commu_Lenovo_EGS[index_of_segment])#/BW_r[1])
print ("CODA: ", sum_traffic_matching)#numpy.round(sum_traffic_matching/1024/1024/8,0) , "MB")


sum_traffic_cp = 0
for i in range(SIZE):
	sum_traffic_cp += ((seg_size[index_of_segment]/thrput_commu_Lenovo_EGS[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_AWSFrank[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_NJN[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_EGS[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_AWSFrank[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_NJN[index_of_segment]))
sum_traffic_cp+=(video_size[index_of_segment]/thrput_commu_Lenovo_NJN[index_of_segment])#/BW_r[2])
print ("CloudPath: ", sum_traffic_cp)#numpy.round(sum_traffic_cp/1024/1024/8,0) , "MB")


sum_traffic_rtrrp = 0
for i in range(SIZE):
	sum_traffic_rtrrp += ((seg_size[index_of_segment]/thrput_commu_Lenovo_EGS[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_AWSFrank[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_AWSFrank[index_of_segment]))+(seg_size[index_of_segment]/thrput_commu_Lenovo_EGS[index_of_segment])
sum_traffic_rtrrp+=(video_size[index_of_segment]/thrput_commu_Lenovo_AWSFrank[index_of_segment])#/BW_r[0])
print ("RTR-RP: ", sum_traffic_rtrrp)#numpy.round(sum_traffic_rtrrp/1024/1024/8,0) , "MB")
	

sum_traffic_cloud = 0
for i in range(SIZE):
	sum_traffic_cloud += ((seg_size[index_of_segment]/thrput_commu_Lenovo_EGS[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_AWSFrank[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_AWSFrank[index_of_segment])+(seg_size[index_of_segment]/thrput_commu_Lenovo_EGS[index_of_segment]))
sum_traffic_cloud+=(video_size[index_of_segment]/thrput_commu_Lenovo_AWSFrank[index_of_segment])#BW_r[0])
print ("CloudOnly: ", sum_traffic_cloud)#numpy.round(sum_traffic_cloud/1024/1024/8,0) , "MB")


print("----------------------------------------")
print()