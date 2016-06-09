# Problem: The Coin Problem

### Description
Given a list of N coins, their values (V<sub>1</sub>, V<sub>2</sub>, ..., V<sub>n</sub>), and the total sum S. Find  
the minimum number of coins the sum of which is S (we can use as many coins of one type as we want), or report that  
it’s not possible to select coins in such a way that they sum up to S.

Write a function answer(coin_values, coin_sum) which takes a list of N coins with their values (V<sub>1</sub>, 
V<sub>2</sub>, ..., V<sub>n</sub>) and a coin sum S and outputs the minimum number of coins needed to reach the sums S.  

Let's take coins with values 1, 3, and 5. And the coin sum S as 11. The output should be 3 (2 coins of value 5 and 1
coin of value 1).

Let's take coins with values 1, 2, and 3. And the coin sum S as 11. The output should be 4 (3 coins of value 3 and 1
coin of value 2).

### Test cases
* Inputs:
    (int list) coin_values = [1, 3, 5]
    (int) coin_sum = 11

  Output:
    (int) 3

* Inputs:
    (int list) coin_values = [1, 2, 3]
    (int) coin_sum = 11
 
  Output:
    (int) 4
