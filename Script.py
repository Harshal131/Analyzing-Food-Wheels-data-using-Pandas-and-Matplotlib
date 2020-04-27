import pandas as pd
import matplotlib as plt
import codecademylib3

restaurants=pd.read_csv('restaurants.csv')

print(restaurants.head())

cuisine_options_count=restaurants.cuisine.nunique()

cuisine_counts = restaurants.groupby('cuisine').id.count().reset_index()

restaurants = pd.read_csv('restaurants.csv')

cuisine_counts = restaurants.groupby('cuisine')\
                            .name.count()\
                            .reset_index()

cuisines = cuisine_counts.cuisine.values
counts = cuisine_counts.name.values


plt.pie(counts,
        labels=cuisines,
       autopct='%d%%')
plt.title('FoodWheel')
plt.axis('equal')
plt.show()

orders=pd.read_csv('orders.csv')
print(orders.head())
month = lambda date:  date.split('-')[0]
orders['month'] = orders.date.apply(month)

avg_order = orders.groupby('month').price.mean().reset_index()

std_order = orders.groupby('month').price.std().reset_index()

orders['month'] = orders.date.apply(lambda x: x.split('-')[0])

avg_order = orders.groupby('month').price.mean().reset_index()

std_order = orders.groupby('month').price.std().reset_index()

ax=plt.subplot()
bar_heights=avg_order.price
bar_errors=std_order.price

plt.close('all')
plt.bar(avg_order.month.values, avg_order.price.values, yerr=bar_errors.price.values, capsize=5)
plt.show()

ax.set_xticks(range(len(bar_heights)))
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.ylabel('Average Amount')
plt.title('Amount over Time')
plt.show()

customer_amount = orders.groupby('customer_id').price.sum().reset_index()

print customer_amount.head()

plt.hist(customer_amount.price.values,
        range=(0, 200), bins=40)
plt.xlabel('Total Spent')
plt.ylabel("Number of Customers")
plt.title('Customer Expenditure Over 6 Months')

plt.show()