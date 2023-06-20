# Developed by: Bruno Mascioli de Souza (github: brunomascioli) and Lucas Pereira dos Santos (github: LucassSantoss)
import math
from random import choice

def read_examples():
    matrix = []
    file = open('iris.data.csv', 'r')
    for line in file:
        data = line.strip().split(',')
        matrix.append(data)
    file.close()
    return matrix[1:]

def read_unclassified(file_name):
    matrix = []
    file = open(file_name, 'r')
    for line in file:
        data = line.strip().split(',')
        matrix.append(data)
    file.close()
    return matrix

def euclidean_distance(known_example, unknown_example):
    distance = math.sqrt(((float(known_example[0]) - float(unknown_example[0])) ** 2) +
                         ((float(known_example[1]) - float(unknown_example[1])) ** 2) +
                         ((float(known_example[2]) - float(unknown_example[2])) ** 2) +
                         ((float(known_example[3]) - float(unknown_example[3])) ** 2))
    return distance

def calculate_distances(examples_matrix, unclassified_matrix, k):
    matrix = []
    for unknown_example in unclassified_matrix:
        distances = []
        unknown_example = list(map(float, unknown_example))
        for known_example in examples_matrix:
            species = known_example[4]
            known_example = list(map(float, known_example[:-1]))
            distance = euclidean_distance(known_example, unknown_example)
            distances.append([distance, species, unknown_example])
        sorted_distances = sorted(distances)
        matrix.append(sorted_distances[:k])
    return matrix

def determine_class(matrix):
    file = open('iris.data.csv', 'a')
    for unclassified_species in matrix:
        setosa, versicolor, virginica = 0, 0, 0
        for points in unclassified_species:
            if points[1] == 'setosa':
                setosa += 1
            elif points[1] == 'versicolor':
                versicolor += 1
            else:
                virginica += 1
        file.write('\n')
        for elem in unclassified_species[0][2]:
            elem = str(elem)
            file.write(elem)
            file.write(',')
        if setosa > versicolor and setosa > virginica:
            file.write('setosa')
            print(unclassified_species[0][2], 'setosa')
        elif versicolor > setosa and versicolor > virginica:
            file.write('versicolor')
            print(unclassified_species[0][2], 'versicolor')
        elif virginica > setosa and virginica > versicolor:
            file.write('virginica')
            print(unclassified_species[0][2], 'virginica')
        elif virginica == versicolor == setosa:
            choice_value = choice(['virginica', 'setosa', 'versicolor'])
            file.write(choice_value)
            print(unclassified_species[0][2], choice_value)
        elif virginica == versicolor > setosa:
            choice_value = choice(['virginica', 'versicolor'])
            file.write(choice_value)
            print(unclassified_species[0][2], choice_value)
        elif virginica == setosa > versicolor:
            choice_value = choice(['virginica', 'setosa'])
            file.write(choice_value)
            print(unclassified_species[0][2], choice_value)
        else:
            choice_value = choice(['setosa', 'versicolor'])
            file.write(choice_value)
            print(unclassified_species[0][2], choice_value)
    file.close()

def main():
    k = int(input('K: '))
    file_name = input('Name of the unclassified data file: ')
    examples_matrix = read_examples()
    unclassified_matrix = read_unclassified(file_name)
    matrix = calculate_distances(examples_matrix, unclassified_matrix, k)
    determine_class(matrix)

main()
