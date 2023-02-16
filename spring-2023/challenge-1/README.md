# Challenge 1

---

```diff
+ Date : 16/02/2023
- Deadline: 23/02/2023
```

## Algorithms

## Scripting

how to access the internet with python?

## SQL

Valentine ended and `Couple Haven`, a local gift boxing business, had received and delivered 1000's of package orders. Now, the business wants to comb its database for the `top 5 most ordered valentine packages`.

Their database table is named `ValentinePackages` and has 4 columns:

> `id`: the id of a package  
> `package_name`: name of a package  
> `order_count`: number of orders for a package  
> `price`: price of a package

> What SQL query will they need to return the expected results.

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
