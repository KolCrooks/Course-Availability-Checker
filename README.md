This is a simple script that I created to get into courses that don't have wait lists.

NOTE: This script will include restricted seats when checking to see if the courses has seats open.

## Instructions

1. Install the required packages with:

```sh
$ python -m pip install -r requirements.txt
```

2. Modify the `URLS` dictionary to include the courses that you wish to watch. The default (what I was trying to get into) is

```Python
URLS = {
    'MATH200': 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=MATH&course=200&section=921',
    'MATH221': 'https://courses.students.ubc.ca/cs/courseschedule?pname=subjarea&tname=subj-section&dept=MATH&course=221&section=921'
}
```

3. (OPTIONAL) if you want to set the interval at which is checks the courses, modify the `INTERVAL` variable. It is in minutes and I would recommend that you don't use any interval lower than 1 as it could cause your IP to get blocked.
