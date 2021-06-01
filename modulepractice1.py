import formatters
"""
Mary is the proud owner of her own brand-new grocery store
called “Mary’s Magnificent Merchandise.” Mary is very excited
to get started, but needs help writing a checkout system so
that customer purchases can be tracked. To do this, the
program should take in the following information: the name of
the item being purchased, the amount of the item being
purchased (in pounds), and the cost of the item per pound. The
program should continue prompting for more and more items
in a loop, asking the user each time if they wish to complete
their purchase, and end the loop. After the user finishes the
loop, each of the items that were input by the user should be
displayed with their name, the amount in pounds, the cost per
pound, and the total cost of the item (calculated as the cost per
pound multiplied by the number of pounds purchased). After
this the total cost for all purchases (in dollars) should be
printed to the screen. Make sure to use the as_dollars and
as_weight_in_pounds functions defined in formatters.py. To do
this, make sure your solution to this problem is in the same
folder as formatters.py, and simply include “import
formatters” at the top of your solution code. You should then
be able to use the functions as formatters.as_dollars, and
formatters.as_weight_in_pounds, as was shown in the second
youtube video. As a bonus, write the same information as is
printed to the screen to a “recipt.txt” file, and upload this file to
a S3 bucket. An example output for this program would be:
Carrots, 5 lbs, $10.00/lbs, $50.00
Potatoes, 2 lbs, $5.00/lbs, $10.00
Total: $60.00
"""


# product_name
# amount
# cost_per_lb
# total_cost

list = []
total_cost = 0

while True:
    product_name = input("Please input item purchased: ")
    amount = float(input("Please amount purchased: "))
    cost_per_lb = float(input("Please input cost per pound: "))
    
    input_list.append ({
        "name" : product_name,
        "amount" : amount,
        "cost" : cost_per_lb,
        "total" : product_cost
    })
    
    product_cost = amount * cost_per_lb
    
    total_cost += product_cost
    
    end = input("Do you want to continue? Y or N. ")
    if end.lower != "y":
        break
    
f = open("receipt.txt", "a")

for d in input_list:
    format_string = f"{d["name"]}, {formatters.as_weight_in_pounds(d["amount"]:.2f)}, {d["cost"]:.2f}/lb, {formatters.as_dollars(d["total"]:.2f})\n"
    print(format_string, end = '')
    f.write(format_string)

format_string = "total cost: {}\n".format(formatters.as_dollars(total_cost))
print(format_string, end = '')
f.write(format_string)
