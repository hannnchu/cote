first_set = set(eval(input("Enter the first set: ")))
second_set = set(eval(input("Enter the second set: ")))

jaccard_similarity_coefficient = len(first_set.intersection(second_set))/len(first_set.union(second_set))
print("the Jaccard similarity coefficient is {:.3f}".format(jaccard_similarity_coefficient))
