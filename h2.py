import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import pandas as pd

width = 3
height = 6

title_font = {'fontname':'Times New Roman','size':'12', 'color':'black', 'weight':'normal'}
sample = pd.DataFrame({'Substitution': (17,19,15,10,35,20),
                   'Adition':(10,4,1,5,3,7),
                   'Deletion': (1,0,7,3,2,10)})
x_hist = (116,30,23)
y_hist = (28,23,23,18,40,37)

fig = plt.figure(figsize=(3,6))
gs = fig.add_gridspec(2,2, hspace=0.02, wspace=0.05)
ax_joint  = fig.add_subplot(gs[1, 0])
ax_marg_x = fig.add_subplot(gs[0, 0],sharex=ax_joint)
ax_marg_y = fig.add_subplot(gs[1, 1],sharey=ax_joint)

pcm = ax_joint.imshow(sample, cmap='viridis', aspect='auto')

for spine in ax_joint.spines:
    ax_joint.spines[spine].set_visible(False)
    ax_marg_x.spines['top'].set_visible(False)
    ax_marg_x.spines['right'].set_visible(False)
    ax_marg_x.spines['bottom'].set_visible(False)

    ax_marg_y.spines['top'].set_visible(False)
    ax_marg_y.spines['right'].set_visible(False)
    ax_marg_y.spines['left'].set_visible(False)
    
ax_joint.tick_params(left = False, bottom = False)
ax_joint.axes.xaxis.set_ticklabels([])


ax_joint.text(-0.39, 0.92, 'Gene.xyz_6', horizontalalignment='center', verticalalignment='center', transform=ax_joint.transAxes, **title_font)
ax_joint.text(-0.39, 0.76, 'Gene.xyz_5', horizontalalignment='center', verticalalignment='center', transform=ax_joint.transAxes,**title_font)
ax_joint.text(-0.39, 0.58, 'Gene.xyz_4', style='italic', horizontalalignment='center', verticalalignment='center', transform=ax_joint.transAxes,**title_font)
ax_joint.text(-0.39, 0.42, 'Gene.xyz_3', style='italic', horizontalalignment='center', verticalalignment='center', transform=ax_joint.transAxes,**title_font)
ax_joint.text(-0.39, 0.25, 'Gene.xyz_2', style='italic', horizontalalignment='center', verticalalignment='center', transform=ax_joint.transAxes,**title_font)
ax_joint.text(-0.39, 0.05, 'Gene.xyz_1', style='italic', horizontalalignment='center', verticalalignment='center', transform=ax_joint.transAxes,**title_font)





ax_joint.text(-0.05, -0.15, 'Substitution', horizontalalignment='center', verticalalignment='center', transform=ax_joint.transAxes,rotation=45,**title_font)
ax_joint.text(0.35, -0.12, 'Addition', horizontalalignment='center', verticalalignment='center', transform=ax_joint.transAxes,rotation=45,**title_font)
ax_joint.text(0.68, -0.12, 'Deletion', horizontalalignment='center', verticalalignment='center', transform=ax_joint.transAxes,rotation=45,**title_font)

ax_joint.axes.yaxis.set_ticklabels([])
ax_marg_x.axes.xaxis.set_ticklabels([])
# ax_marg_x.axes.yaxis.set_ticklabels([])
# ax_marg_y.axes.xaxis.set_ticklabels([])
ax_marg_y.axes.yaxis.set_ticklabels([])
ax_marg_y.tick_params(left = False, bottom = True)
ax_marg_x.tick_params(left = True, bottom = False)
# ax_marg_y.set_prop_cycle(marker=['o', '+', 'x'])

# pcm = ax_joint.pcolormesh(sample)
fig.colorbar(pcm,location='right')

ax_marg_x.bar(range(width),x_hist, color=(1.0,0,0.22))
ax_marg_y.barh(range(height),y_hist, color=(0,0,0))
plt.show()