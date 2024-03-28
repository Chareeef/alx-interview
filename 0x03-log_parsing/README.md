## Log Parsing

### Hey there, Software Engineering Superstar! 🚀

### Overview
Get ready to dive into the exciting world of log parsing! Our script is all set to process input from stdin, line by line, and churn out some mind-blowing metrics for you!

### Input Format
Each line of input should be nothing short of spectacular, following this mesmerizing format:
```
<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
```
Prepare to be amazed as our script gracefully skips lines that fail to meet this magical format!

### Metrics Galore
- **Total File Size:** Brace yourself for the grand total of all the mesmerizing file sizes we encounter!
- **Number of Lines by Status Code:** 
  - Witness the enchantment unfold as we count occurrences of the most enchanting status codes: 200, 301, 400, 401, 403, 404, 405, and 500!
  - These status codes are presented in ascending order, alongside their enchanting frequency!

### Prepare to be Spellbound!
Marvel at the mystical output our script conjures:
```
File size: 5213
200: 2
401: 1
403: 2
404: 1
405: 1
500: 3
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
```

### Important Incantations
- Remember, only input conforming to our enchanted format will be deemed worthy of parsing.
- Any status codes that fail to materialize or are devoid of magic integer properties will gracefully fade into obscurity, not gracing our output.

### Ready to Unleash the Magic?
Prepare to be awestruck as we embark on this mesmerizing journey of log parsing brilliance! 🌟
