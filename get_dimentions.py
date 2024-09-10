from math import pi
import torch

ellipse_constant = pi * 0.25
sphere_constant = pi/6
def get_dimentions(results, pixel_ratio):
    img_height, img_width = results[0].orig_shape

    array = results[0].boxes
    filter = (array.xyxy[:, 0] > 1) & (array.xyxy[:, 1] > 1) & (array.xyxy[:, 2] < img_width - 1) & (array.xyxy[:, 3] < img_height - 1)
    array = array[filter]

    widths_vector = (array.xyxy[:, 2] - array.xyxy[:, 0])
    heights_vector = (array.xyxy[:, 3] - array.xyxy[:, 1])

    diameters_vector = (widths_vector + heights_vector)/2
    volumes_vector = (diameters_vector**3)*sphere_constant

    diameters_sums = {
        "sum": diameters_vector.sum().item() * pixel_ratio, 
        "squares_sum": ((diameters_vector*pixel_ratio)**2).sum().item()
    }
    volumes_sums = {
        "sum": volumes_vector.sum().item() * pixel_ratio, 
        "squares_sum" : ((volumes_vector * pixel_ratio**3)**2).sum().item()
    }

    diameters = (torch.round(widths_vector)).tolist()
    volumes = (torch.round(volumes_vector)).tolist()

    return diameters, diameters_sums, volumes, volumes_sums
