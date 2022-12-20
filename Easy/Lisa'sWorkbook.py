def workbook(n, k, arr):
    # Write your code here
    page_number = 1
    special_problems = 0
    for chapter in arr:
        problems_in_chapter = 1
        while problems_in_chapter <= chapter:
            if problems_in_chapter == page_number:
                special_problems += 1
            if problems_in_chapter % k == 0 or problems_in_chapter == chapter:
                page_number += 1
            problems_in_chapter += 1
    return special_problems