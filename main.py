import csv
from os import listdir
from functions import *

path = "/home/paolinux/Desktop/Iss/astropi-iss-speed-en-resources/Images"

def calculate_speed(image_1, image_2):

    time_difference = get_time_difference(image_1, image_2) #get time difference between images
    image_1_cv, image_2_cv = convert_to_cv(image_1, image_2) #create opencfv images objects
    keypoints_1, keypoints_2, descriptors_1, descriptors_2 = calculate_features(image_1_cv, image_2_cv, 1000) #get keypoints and descriptors
    matches = calculate_matches(descriptors_1, descriptors_2) #match descriptors

    display_matches(image_1_cv, keypoints_1, image_2_cv, keypoints_2, matches)

    coordinates_1, coordinates_2 = find_matching_coordinates(keypoints_1, keypoints_2, matches)
    average_feature_distance = calculate_mean_distance(coordinates_1, coordinates_2)
    speed = calculate_speed_in_kmps(average_feature_distance, 12648, time_difference)

    return speed

list = listdir(path)
list.reverse()

#def

im1 = f"Images/{list[0]}"
im2 = f"Images/{list[1]}"

print(str(im1))

print(calculate_speed(im1, im2))
