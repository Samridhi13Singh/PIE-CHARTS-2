import matplotlib.pyplot as plt


Roles = ['Software Engineer', 'Data Analyst', 'Data Scientist', 'Backend Engineer', 'Frontend Engineer']
counts = [15, 17, 20, 3, 35]


color = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0']


ex = (0, 0, 0, 0, 0)


plt.figure(figsize=(8, 6))
plt.pie(counts, labels=Roles, colors=color, autopct='%1.0f%%', startangle=140, explode=ex)


plt.title('Distribution of Roles in the Team', fontsize=16)
plt.legend(Roles)
plt.show()
