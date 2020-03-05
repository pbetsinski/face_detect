import os
import re


class Image:
    def __init__(self, name, path, face_count, complexity):
        self.name = name
        self.path = path
        self.face_count = face_count
        self.complexity = complexity


class Images:
    def __init__(self):
        self.images_list = []
        self.__read_all_files()

    def __read_all_files(self):
        project_root = os.path.dirname(os.path.dirname(__file__))
        path_to_images = os.path.join(project_root, 'image_files')
        for image in os.listdir(path_to_images):
            if re.fullmatch('[0-9]{1,2}_[0-9]{1,2}_.*\\.(jpg|png|jpeg|bmp)', image):
                self.images_list.append(Image(name=image, path=os.path.join(path_to_images, image),
                                              face_count=int(image.split('_')[0]), complexity=int(image.split('_')[1])))

    def get_all(self, min_complexity=1, max_complexity=10):
        result_list = []
        for image in self.images_list:
            if min_complexity <= image.complexity <= max_complexity:
                result_list.append(image)
        if len(result_list) == 0:
            raise FileNotFoundError(f'No image with complexity between {min_complexity} and {max_complexity} was found')
        else:
            return result_list

    def get(self, name=None, min_complexity=1, max_complexity=10):

        if name is not None:
            for image in self.images_list:
                if image.name == name:
                    return image
            raise FileNotFoundError(f'Image: {name} was not found')
        else:
            for image in self.images_list:
                if min_complexity <= image.complexity <= max_complexity:
                    return image
            raise FileNotFoundError(f'No image with complexity between {min_complexity} and {max_complexity} was found')
