# Challenge 1

```diff
+ Published : 16/02/2023
- Deadline: 23/02/2023
```

---

## Algorithms

<br />
## Scripting

`Fred`, a student of Ashesi University wants to analyze his friend's `(Michael)` spending habits over the course of the semester. His idea is to log Michael's meal plan balance for each of morning, afternoon and evening to a spreadsheet.

For now, he is focused on writing a `python script` that prints Michael's meal plan balance everytime its executed.

> Can you write a script for this purpose?

Executing the script in the terminal

```sh
$ ./meal_plan_balance.py
```

Example result

```sh
$ current balance : 80
```

#### Hints

- Accessing the web via python (python's request module)
- Inspecting network tab of the meal plan website for the API endpoint

<br />

## SQL

Valentine ended and `Couple Haven`, a local gift boxing business, had received and delivered 1000's of package orders. Now, the business wants to comb its database for the `top 5 most ordered valentine packages`.

Their database table is named `ValentinePackages` and has 4 columns:

> `id`: the id of a package  
> `package_name`: name of a package  
> `order_count`: number of orders for a package  
> `price`: price of a package

**_Write a SQL query will to return the expected results._**

### TABLE

| id    | package_name     | order_count | price |
| ----- | ---------------- | ----------- | ----- |
| CB01  | chocolate bag    | 30          | 50    |
| SP02  | spice basket     | 12          | 1200  |
| MH03  | mugs and hugs    | 49          | 900   |
| FC04  | flower candy     | 34          | 90    |
| SP05  | sugar plum       | 21          | 329   |
| TB06  | treats box       | 81          | 45    |
| CS07  | candy stash      | 45          | 785   |
| MBD08 | milk bar deluxe  | 31          | 980   |
| RGS09 | rose gift set    | 12          | 120   |
| PP10  | poppy popcorn    | 9           | 560   |
| GS11  | gelato silverton | 3           | 450   |
| CD11  | cozy diva        | 40          | 300   |

### RESULT

| id   | package_name  | order_count | price |
| ---- | ------------- | ----------- | ----- |
| TB06 | treats box    | 81          | 45    |
| MH03 | mugs and hugs | 49          | 900   |
| CS07 | candy stash   | 45          | 785   |
| CD11 | cozy diva     | 40          | 300   |
| FC04 | flower candy  | 34          | 90    |
