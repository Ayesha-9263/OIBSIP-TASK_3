 =========================================
# PROJECT INTRO PAGE (TASK-3)
# =========================================

import matplotlib.pyplot as plt

# Create figure
plt.figure(figsize=(12,7))
plt.axis('off')  # Hide axes


# =========================================
# NAME (MAIN HIGHLIGHT)
# =========================================

plt.text(0.5, 0.80, "AYESHA ANSARI",
         fontsize=32,
         fontweight='bold',
         color="#aeed0f",   
         ha='center')


# =========================================
# TASK NUMBER
# =========================================

plt.text(0.5, 0.68, "TASK - 3",
         fontsize=20,
         fontweight='bold',
         color='#ffffff',
         ha='center')


# =========================================
# PROJECT TITLE
# =========================================

plt.text(0.5, 0.58, "Email Spam Detection With Machine Learning project",
         fontsize=22,
         fontweight='bold',
         color="#0b0ee5",
         ha='center')


plt.text(0.5, 0.50, "Using Machine Learning",
         fontsize=16,
         style='italic',
         ha='center')


# =========================================
# INTERNSHIP DETAILS
# =========================================

plt.text(0.5, 0.40, "Oasis Infobyte",
         fontsize=16,
         fontweight='bold',
         color='#facc15',
         ha='center')


plt.text(0.5, 0.34, "Data Science Internship",
         fontsize=14,
         ha='center')


# =========================================
# TECH STACK
# =========================================

plt.text(0.5, 0.24, "Python | Pandas | Machine Learning",
         fontsize=12,
         ha='center')


# =========================================
# FOOTER (UNIQUE TOUCH)
# =========================================

plt.text(0.5, 0.12, "Project by Ayesha Ansari",
         fontsize=11,
         style='italic',
         color='gray',
         ha='center')


# Show output
plt.show()