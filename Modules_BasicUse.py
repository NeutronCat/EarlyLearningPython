#datetime module
# Import datetime from datetime below:
from datetime import datetime
current_time = datetime.now()
print(current_time)

#random number module
# Import random below:
import random
# Create random_list below:
random_list = [random.randint(1,101) for i in range(101)]
# Create randomer_number below:
randomer_number = random.choice(random_list)
# Print randomer_number below:
print(randomer_number)

#matplotlib and random
import codecademylib3_seaborn

from matplotlib import pyplot as plt
import random

numbers_a = range(1, 13)
numbers_b = random.sample(range(1000), 12)

plt.plot(numbers_a,numbers_b)
plt.show()



