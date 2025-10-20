# Libraries
import matplotlib.pyplot as plt
import matplotlib.patches as patches

fig, ax = plt.subplots(figsize=(4, 6))

strip_width = 0.5
strip_height = 4.0
strip = patches.Rectangle(
    (-strip_width / 2, -strip_height / 2), 
    strip_width, 
    strip_height, 
    edgecolor='black', 
    facecolor='lightblue', 
    linewidth=2
    )

ax.add_patch(strip)

ax.plot(0, 0, 'ko', markersize=6)
ax.text(0.3, 0.05, 'CG', ha='left', va='bottom', color='black', fontsize=12)

scale = patches.Rectangle(
    (-strip_width * 2, -strip_height / 2 - 0.2),
    strip_width * 4,
    0.2,
    edgecolor='black',
    facecolor='grey'
    )

ax.add_patch(scale)
ax.text(0, -strip_height / 2 - 0.35, 'Scale', ha='center', va='center')

ax.arrow(
    0, strip_height / 2,
    0, -1.0,
    head_width=0.2, 
    head_length=0.3, 
    fc='red', 
    ec='red',
    length_includes_head=True
    )

ax.text(0.3, 1.0, r'$F_{applied}$', ha='left', va='center', color='red', fontsize=12)

ax.arrow(
    0, 0,
    0, -0.6,
    head_width=0.2, head_length=0.3, fc='purple', ec='purple',
    length_includes_head=True
    )

ax.text(0.3, -0.3, r'$F_{gravity}$', ha='left', va='center', color='purple',
fontsize=12)

ax.arrow(
    0, -strip_height / 2,
    0, 1.6,
    head_width=0.2, head_length=0.3, fc='blue', ec='blue',
    length_includes_head=True
    )

ax.text(-0.3, -0.4, r'$F_{scale}$',
    ha='right', va='center', color='blue', fontsize=12)

ax.set_xlim(-2, 2)
ax.set_ylim(-3, 3)
ax.set_aspect('equal', adjustable='box')
ax.axis('off')
plt.title('FBD of Acrylic Strip')
plt.show()