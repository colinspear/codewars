# Me

def sort_odds(source_array):
    odds = [j for j in source_array if j % 2]
    odds = sorted(odds)
    odd_int = 0
    print(odds)
    for k in range(len(source_array)):
        if source_array[k] % 2:
            source_array[k] = odds[odd_int]
            odd_int += 1
    return source_array


# chosen solution

def sort_array(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]
