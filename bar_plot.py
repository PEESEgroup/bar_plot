#!/usr/bin/env python
# coding: utf-8

# # Python bar plot

import numpy as np
import matplotlib.pyplot as plt


# ## Basic plot

xaxis = ['2020','2030','2060']
yaxis = np.array([232.4903615, 219.30489173, 9.30464342])


fig, ax = plt.subplots() # create figure
width = 0.5
ax.bar(xaxis,yaxis,width) # plot function brackets
ax.set_ylabel('Annual CO$_2$ emissions (Tg)') # set y-axis label


# ## Stacked bar plot


year = ['2020','2030','2060']
types = ['Gasoline Production','Gasoline Use','Electricity Production','Battery Manufacture','Vehicle Manufacture']

col1 = np.array([232.4903615 , 219.30489173,   9.30464342])
col2 = np.array([821.75632487, 775.96207863,  41.24247437])
col3 = np.array([8.09528431, 260.77831868, 368.86903492])
col4 = np.array([2.65890412, 147.01391327, 243.95214992])
col5 = np.array([158.62631774, 356.18450773, 418.89916109])



fig, ax = plt.subplots(dpi=300,figsize=(7,8)) # set dpi, fig length and height; dpi=300,figsize=(7,8)
width=0.5
ax.bar(year, col1, width, label=types[0])
ax.bar(year, col2, width, bottom=col1, label=types[1]) # add subsequent bar and bar label, set bottom para
ax.bar(year, col3, width, bottom=col1+col2, label=types[2])
ax.bar(year, col4, width, bottom=col1+col2+col3, label=types[3])
ax.bar(year, col5, width, bottom=col1+col2+col3+col4, label=types[4])
ax.legend() # add legend
ax.set_ylabel('Annual CO$_2$ emission (Tg)')


# ## Error Bar


col_all = col1+col2+col3+col4+col5
err_up = [22.33432, 449.50750063, 45.80917183]
err_low = [10.6254, 190.74913295, 22.84109572]



fig, ax = plt.subplots(dpi=300,figsize=(7,8))
width = 0.5
ax.bar(year, col1, width, label=types[0])
ax.bar(year, col2, width, bottom=col1, label=types[1])
ax.bar(year, col3, width, bottom=col1+col2, label=types[2])
ax.bar(year, col4, width, bottom=col1+col2+col3, label=types[3])
ax.bar(year, col5, width, bottom=col1+col2+col3+col4, label=types[4])

ax.errorbar(year[1:], col_all[1:], yerr=[err_low[1:],err_up[1:]],fmt='None',color='Black',linewidth=1,capsize=4) #error bar function, set fmt='--',color='Black',linewidth=1,capsize=4

ax.legend()
ax.set_ylabel('Annual CO$_2$ emission (Tg)')


# ## Additional Scatter

scenario1 = [1457.03738105,  825.94257148]
scenario2 = [1702.90134475,  747.48175887]
scenario3 = [1898.96001386, 1226.25171378]
scenario4 = [1692.73154299, 1001.24670792]
scenario5 = [1747.14318779, 1001.67489542]
scenario6 = [1759.0579827 , 1080.83421662]
scenario7 = [1751.71718163, 1076.1375415]

slabels = ['Fuel Economy','Grid Decarbonization','Vehicle Lightweighting','Vehicle Recycling','V2G','SLB','Battery Chemistry']


import matplotlib.cm as mpc
cmap = mpc.get_cmap('Set3')


fig, ax = plt.subplots(dpi=300,figsize=(7,8))
width = 0.5
ax.bar(year, col1, width, label=types[0])
ax.bar(year, col2, width, bottom=col1, label=types[1])
ax.bar(year, col3, width, bottom=col1+col2, label=types[2])
ax.bar(year, col4, width, bottom=col1+col2+col3, label=types[3])
ax.bar(year, col5, width, bottom=col1+col2+col3+col4, label=types[4])
ax.errorbar(year[1:], col_all[1:],yerr=[err_low[1:],err_up[1:]],fmt='None',color='Black',linewidth=1,capsize=4)

ax.scatter(year[1:], scenario1, color=cmap(0),label=slabels[0],edgecolor='black',s=200, marker="^")
ax.scatter(year[1:], scenario2, color=cmap(1),label=slabels[1],edgecolor='black',s=200, marker="^")
ax.scatter(year[1:], scenario3, color=cmap(2),label=slabels[2],edgecolor='black',s=200,marker="^")
ax.scatter(year[1:], scenario4, color=cmap(3),label=slabels[3],edgecolor='black',s=200,marker="^")
ax.scatter(year[1:], scenario5, color=cmap(4),label=slabels[4],edgecolor='black',s=200,marker="^")
ax.scatter(year[1:], scenario6, color=cmap(5),label=slabels[5],edgecolor='black',s=200,marker="^")
ax.scatter(year[1:], scenario7, color=cmap(6),label=slabels[6],edgecolor='black',s=200,marker="^")

ax.legend()
ax.set_ylabel('Annual CO$_2$ emission (Tg)')


fig, ax = plt.subplots(dpi=300,figsize=(7,8))
width = 0.5
ax.bar(year, col1, width, label=types[0])
ax.bar(year, col2, width, bottom=col1, label=types[1])
ax.bar(year, col3, width, bottom=col1+col2, label=types[2])
ax.bar(year, col4, width, bottom=col1+col2+col3, label=types[3])
ax.bar(year, col5, width, bottom=col1+col2+col3+col4, label=types[4])
ax.errorbar(year[1:], col_all[1:],yerr=[err_low[1:],err_up[1:]],fmt='None',color='Black',linewidth=1,capsize=4)

for i,iscenario in enumerate([scenario1,scenario2,scenario3,scenario4,scenario5,scenario6,scenario7]):
    colors=cmap(i)
    if i==6:
        colors='white'
    ax.scatter(year[1:], iscenario, color=colors,alpha=0.8,edgecolor='black',s=200, marker="^",label=slabels[i])


ax.legend()
ax.set_ylabel('Annual CO$_2$ emission (Tg)')


fig, ax = plt.subplots(dpi=300,figsize=(7,8))
width = 0.5
ax.bar(year, col1, width, color='#417FA6',label=types[0]) # set color
ax.bar(year, col2, width, bottom=col1, color='#9CBCD9', label=types[1])
ax.bar(year, col3, width, bottom=(col1+col2), color='#F2B263', label=types[2])
ax.bar(year, col4, width, bottom=(col1+col2+col3), color='#589A8D', label=types[3])
ax.bar(year, col5, width, bottom=(col1+col2+col3+col4), color='#A3CCAB', label=types[4])
ax.errorbar(year[1:], col_all[1:], yerr=[err_low[1:],err_up[1:]],fmt='None',color='Black',linewidth=1,capsize=4)

for i,iscenario in enumerate([scenario1,scenario2,scenario3,scenario4,scenario5,scenario6,scenario7]):
    colors=cmap(i)
    if i==6:
        colors='white'
    ax.scatter(year[1:], iscenario, color=colors,alpha=0.8,edgecolor='black',s=200, marker="^",label=slabels[i])

ax.legend(bbox_to_anchor=(1,-0.1), frameon=False, ncol=2, fontsize=14) # adjust legend
ax.set_ylabel('Annual CO$_2$ emission (Tg)', fontsize=18)
ax.tick_params(labelsize=18) # adjust tick
plt.tight_layout() # adjust layout

plt.savefig('emission.tiff') # export


# ## Horizontal bar chart


err_low_h = [0.15581873, 3.47850646, 1.32046737]
err_up_h =[0.16286119, 5.82107782, 2.48711206]



bdata = ((col1+col2+col3)/col_all*100) # discreate distribution


fig, ax = plt.subplots(dpi=300,figsize=(9,5))
width=0.5
ax.barh(year, col1/col_all*100, width, color='#417FA6', label=types[0]) # horizontal bar 
ax.barh(year, col2/col_all*100, width, left=col1/col_all*100, color='#9CBCD9', label=types[1]) #change bottom to left
ax.barh(year, col3/col_all*100, width, left=(col1+col2)/col_all*100, color='#F2B263', label=types[2])
ax.barh(year, col4/col_all*100, width, left=(col1+col2+col3)/col_all*100, color='#589A8D', label=types[3])
ax.barh(year, col5/col_all*100, width, left=(col1+col2+col3+col4)/col_all*100, color='#A3CCAB', label=types[4])

ax.errorbar(bdata[1:], year[1:], xerr=[err_low_h[1:],err_up_h[1:]], linewidth=1.5, fmt='none', ecolor='Black', capsize=3)

ax.tick_params(labelsize=18)
ax.set_xlabel('CO$_2$ emission contribution (%)', fontsize=18)
ax.set_xlim(0,100) # set axis limit
ax.legend(loc='center left',bbox_to_anchor=(1,0.5),frameon=False, fontsize=14)
plt.tight_layout()


# ## Grouped and stacked bar plot

# Base data
values = np.array([[[ 31.53276302,   0.        ,  56.373     , 183.312     ],# numpy array to store data
                    [ 36.91021209,  13.32020119,  75.1440576 ,  43.99488   ],
                    [ 44.30180525,  38.42365728,  77.7708    ,   0.        ]],

                   [[ 30.71361987,   0.        ,  45.0984    , 183.312     ],
                    [ 35.91661189,  12.003157  ,  63.7218656 ,  43.99488   ],
                    [ 42.4888137 ,  34.62449135,  66.5748    ,   0.        ]],

                   [[ 29.07533357,   0.        ,  39.4611    , 183.312     ],
                    [ 33.92941147,   9.94265531,  44.1128016 ,  43.99488   ],
                    [ 38.86283061,  28.68073647,  44.1828    ,   0.        ]]])

# Uncertainty
values_e = np.array([[[ 31.53276302,   0.        ,  56.373     , 183.312     ],
                    [ 36.91021209,  13.32020119,  75.1440576 ,  43.99488   ],
                    [ 44.30180525,  38.42365728,  77.7708    ,   0.        ]],

                   [[ 29.89447672,   0.        ,  45.0984    , 146.6496    ],
                    [ 34.92301168,  12.003157  ,  54.4565536 ,  43.99488   ],
                    [ 40.67582216,  34.62449135,  55.3788    ,   0.        ]],

                   [[ 26.61790412,   0.        ,  39.4611    , 128.3184    ],
                    [ 30.94861085,   9.94265531,  16.3168656 ,  43.99488   ],
                    [ 33.42385597,  28.68073647,  10.5948    ,   0.        ]]])

# Scenario
scatter_data = [[221.64247672, 194.39740412],
                [144.38963818,  97.9183343 ],
                [127.82921706,  63.22436132]]



year = ['2020', '2030', '2060']
labels =['ICEV','PHEV','BEV']
ntypes = ['Vehicle Manufacture','Battery Manufacture','Fuel Production','Fuel Consumption']
ncmap = mpc.get_cmap('tab20c')
ncmap



fig, ax = plt.subplots(dpi=300,figsize=(5,5))

width=0.2
x = np.arange(len(year)) # number of groups

ax.bar(x, values[:, 0, 0], width, color=ncmap(16),label='ICEV') #all groups ,the first vheicle type, the first emission process
ax.bar(x + width, values[:, 1, 0], width, color=ncmap(18),label='PHEV')
ax.bar(x + width*2, values[:, 2, 0], width, color=ncmap(19), label='BEV')

ax.legend()
ax.set_xticks(ticks=x + width,labels=year) # set ticks and labels for clusters



fig, ax = plt.subplots(dpi=300,figsize=(5,5))

width=0.2
x = np.arange(len(year))
ax.bar(x, values[:, 0, 0], width, color=ncmap(16),label='ICEV')
ax.bar(x + width, values[:, 1, 0], width, color=ncmap(18),label='PHEV')
ax.bar(x + width*2, values[:, 2, 0], width, color=ncmap(19), label='BEV')
ax.set_xticks(x + width)
ax.set_xticklabels(year)

# add stacked bars
for i in range(0,3):
    offset = i * width
    if i==1:
        ax.bar(x + offset, values[:, i, 0], width, color=ncmap(i),label=ntypes[0])
        ax.bar(x + offset, values[:, i, 1], width, bottom=np.sum(values[:, i, :1], axis=1), color=ncmap(i+4),label=ntypes[1])
        ax.bar(x + offset, values[:, i, 2], width, bottom=np.sum(values[:, i, :2], axis=1), color=ncmap(i+8),label=ntypes[2])
        ax.bar(x + offset, values[:, i, 3], width, bottom=np.sum(values[:, i, :3], axis=1), color=ncmap(i+12),label=ntypes[3])
    
    else:
        ax.bar(x + offset, values[:, i, 0], width, color=ncmap(i))
        ax.bar(x + offset, values[:, i, 1], width, bottom=np.sum(values[:, i, :1], axis=1), color=ncmap(i+4))
        ax.bar(x + offset, values[:, i, 2], width, bottom=np.sum(values[:, i, :2], axis=1), color=ncmap(i+8))
        ax.bar(x + offset, values[:, i, 3], width, bottom=np.sum(values[:, i, :3], axis=1), color=ncmap(i+12))
    
    total_heights = np.sum(values[1:, i, :], axis=1)
    ax.errorbar(x[1:] + offset, total_heights, yerr=[total_heights-np.sum(values_e[1:, i, :], axis=1),[0,0]], elinewidth=1,fmt='none', 
            ecolor='black', capsize=2)


ax.scatter(x[1:]+0.2, scatter_data[1], marker='^',color='White',edgecolor='black', zorder=5,label='Battery chemistry')
ax.scatter(x[1:]+0.4, scatter_data[2], marker='^',color='White',edgecolor='black', zorder=5)

ax.set_ylabel('Life cycle CO$_2$ emission (g/km)', fontsize=12)
ax.legend(bbox_to_anchor=(1, -0.1), frameon=False, ncol=2, fontsize=8)

plt.tight_layout()
plt.savefig('LCA.tiff')



# # The end!
# # Thanks much!!
# # Hope you find the information useful!!!





