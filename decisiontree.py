# To change this template, choose Tools | Templates
# and open the template in the editor.

import math
import sys

import csv
import getopt

def read_csv_file(filename):
    data = []
    with open(filename, 'r') as csvfile:
        content = csv.reader(csvfile, delimiter=',', quotechar='"')
        for line in content:
            del line[0]
            data.append([item.strip() for item in line])

    return data

def majority_value(data, target_attr):
    """
    Creates a list of all values in the target attribute for each record
    in the data list object, and returns the value that appears in this list
    the most frequently.
    """
    data = data[:]
    return most_frequent([record[target_attr] for record in data])

def most_frequent(lst):
    """
    Returns the item that appears most frequently in the given list.
    """
    lst = lst[:]
    highest_freq = 0
    most_freq = None

    for val in unique(lst):
        if lst.count(val) > highest_freq:
            most_freq = val
            highest_freq = lst.count(val)

    return most_freq

def unique(lst):
    """
    Returns a list made up of the unique values found in lst.  i.e., it
    removes the redundant values in lst.
    """
    lst = lst[:]
    unique_lst = []

    # Cycle through the list and add each value to the unique list only once.
    for item in lst:
        if unique_lst.count(item) <= 0:
            unique_lst.append(item)

    # Return the list with all redundant values removed.
    return unique_lst

def get_examples(data, attr, value):
    """
    Returns a list of all the records in <data> with the value of <attr>
    matching the given value.
    """
    data = data[:]
    rtn_lst = []

    if not data:
        return rtn_lst
    else:
        record = data.pop()
        if record[attr] == value:
            rtn_lst.append(record)
            rtn_lst.extend(get_examples(data, attr, value))
            return rtn_lst
        else:
            rtn_lst.extend(get_examples(data, attr, value))
            return rtn_lst

def get_values(data, attr):
    """
    Creates a list of values in the chosen attribut for each record in data,
    prunes out all of the redundant values, and return the list.
    """
    data = data[:]
    return unique([record[attr] for record in data])


def choose_attribute(data, attributes, target_attr, fitness):
    """
    Cycles through all the attributes and returns the attribute with the
    highest information gain (or lowest entropy).
    """
    data = data[:]
    best_gain = 0.0
    best_attr = None

    #For each attribute in the set of given attributes:
    for attr in attributes:
        gain = fitness(data, attr, target_attr)
        if (gain >= best_gain and attr != target_attr):
            best_gain = gain
            best_attr = attr

    return best_attr

#--------------ID3 Functions----------------------------------------------
def entropy(data, target_attr):
    """
    Calculates the entropy of the given data set for the target attribute.
    """
    val_freq     = {}
    data_entropy = 0.0

    # Calculate the frequency of each of the values in the target attr
    for record in data:
        if target_attr in val_freq:
            val_freq[record[target_attr]] += 1.0
        else:
            val_freq[record[target_attr]]  = 1.0

    # Calculate the entropy of the data for the target attribute
    for freq in val_freq.values():
        data_entropy += (-freq / len(data)) * math.log(freq / len(data), 2)

    return data_entropy




def gain(data, attr, target_attr):
    """
    Calculates the information gain (reduction in entropy) that would
    result by splitting the data on the chosen attribute (attr).
    """
    val_freq = {}
    subset_entropy = 0.0

    # Calculate the frequency of each of the values in the target attribute
    for record in data:
        if attr in val_freq:
            val_freq[record[attr]] += 1.0
        else:
            val_freq[record[attr]] = 1.0

    # Calculate the sum of the entropy for each subset of records weighted
    # by their probability of occuring in the training set.
    for val in val_freq:
        val_prob = val_freq[val] / sum(val_freq.values())
        data_subset = [record for record in data if record[attr] == val]
        subset_entropy += val_prob * entropy(data_subset, target_attr)

    # Subtract the entropy of the chosen attribute from the entropy of the
    # whole data set with respect to the target attribute (and return it)
    return (entropy(data, target_attr) - subset_entropy)

#-----------------End of ID3 Functions-------------------------------------


def make_decision_tree(data, attributes, target_attr, fitness_func):
    """
    This function creates a decision tree based on data given
    """
    data = data[:] #Just copuing the input data since Python uses references to pass arguments such as dictionaries/sets or lists
    vals = [record[target_attr] for record in data]


    default = majority_value(data, target_attr)
    # If the dataset is empty or the attributes list is empty, return the
    # default value. When checking the attributes list for emptiness, we
    # need to subtract 1 to account for the target attribute.
    if not data or (len(attributes) - 1) <= 0:
        return default
    # If all the records in the dataset have the same classification,
    # return that classification.
    elif vals.count(vals[0]) == len(vals):
        return vals[0] + "(" + str(float(len(vals))) + ")"
    else:
        # Choose the next best attribute to best classify our data
        best = choose_attribute(data, attributes, target_attr, fitness_func)
        # Create a new decision tree/node with the best attribute and an empty
        # dictionary object--we'll fill that up next.
        tree = {best:{}}
        # Create a new decision tree/sub-node for each of the values in the
        # best attribute field
        for val in get_values(data, best):
            # Create a subtree for the current value under the "best" field
            subtree = make_decision_tree(get_examples(data, best, val),
                                         [attr for attr in attributes if attr != best],
                                         target_attr,
                                         fitness_func
                                         )

            # Add the new subtree to the empty dictionary object in our new
            # tree/node we just created.
            tree[best][val] = subtree



    return tree

def print_tree(tree, str):
    """
    This function recursively crawls through the d-tree and prints it out in a
    more readable format than a straight print of the Python dict object.
    """
    if type(tree) == dict:
        print("%s%s" % (str, tree.keys()[0]))
        for item in tree.values()[0].keys():
            print("%s\t%s%s" % (str, item, "-\\"))
            print_tree(tree.values()[0][item], str + "\t\t")
            print("")
    else: #printing leaves
        print("%s->%s" % (str, tree))

def replace_values(data, col, new_vals, limits):
    for i in range(len(data)):
        if int(data[i][col]) < int(limits[0]):
            data[i][col] = new_vals[0]
            continue
        elif int(data[i][col]) >= limits[-1]:
            data[i][col] = new_vals[-1]
            continue
        else:
            for l in range(len(limits)):
                if l == 0:
                    continue
                elif (int(data[i][col]) < limits[l]) and (int(data[i][col]) >= limits[l-1]):
                    data[i][col] = new_vals[l]
    return data

def main(argv):
    #"Buckets"
    b_flag = False
    bucket_filename = ""

    #Parsing command line arguments:
    try:
        opts, args = getopt.getopt(argv[2:], "c:h", ["help", "?"])
    except getopt.GetoptError:
        print('phython decision_tree.py <input filename> [-option [argument]]')
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-h", "--help", "-?"):
            print("Reserved for help")
            sys.exit()
        if opt == "-c":
            b_flag = True
            bucket_filename = arg

    raw_data = read_csv_file(argv[1])

    attributes = raw_data[0]
    del raw_data[0]

    if b_flag == True:
      with open(bucket_filename) as f:
            lines = f.readlines()
            f.close()

      for line in lines:
            items = line.split(';')
            raw_data = replace_values(raw_data, int(items[0].strip())-1, items[1].split(','), [int(item.strip()) for item in items[2].split(',')])
            

    #print "Target attribute:"
    target_attr = attributes[-1]

    data = []
    for line in raw_data:
        data.append(dict(zip(attributes, line)))

    # Create the decision tree
    tree = make_decision_tree(data, attributes, target_attr, gain)
    print("Decision tree:")
    print_tree(tree, "")


if __name__ == "__main__":
    main(sys.argv)
