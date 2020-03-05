from face_detect import face_detect
from pytest import mark
import pytest


@mark.face_detect
class FaceDetectTests:

    @mark.smoke
    def test_will_recognize_4_faces_given_specific_image(self, images):
        img = images.get(name='4_2_grayscale_abba.png')
        assert face_detect(img.path) == 4

    @mark.smoke
    def test_will_recognize_0_faces_given_specific_image(self, images):
        img = images.get(name='0_1_xp_background.jpg')
        assert face_detect(img.path) == 0

    @mark.smoke
    @mark.negative
    def test_will_throw_any_exception_given_invalid_image_path(self):
        with pytest.raises(Exception) as e_info:
            face_detect('invalid/path/to/image.jpg')

    @mark.smoke
    @mark.negative
    def test_will_throw_correct_exception_given_invalid_image_path(self):
        with pytest.raises(FileNotFoundError) as e_info:
            face_detect('invalid/path/to/image.jpg')

    @mark.smoke
    @mark.negative
    def test_will_throw_correct_exception_given_invalid_type(self):
        with pytest.raises(ValueError) as e_info:
            face_detect(123)

    @mark.slow
    def test_success_rate_higher_than_80_given_multiple_easy_images(self, images):
        success_count = 0
        image_list = images.get_all(max_complexity=2)
        for img in image_list:
            if face_detect(img.path) == img.face_count:
                success_count += 1
        success_percentage = success_count / len(image_list) * 100
        print(f'Actual success rate: {success_percentage}%')
        assert success_percentage > 80

    @mark.slow
    def test_success_rate_higher_than_40_given_multiple_medium_images(self, images):
        success_count = 0
        image_list = images.get_all(min_complexity=2, max_complexity=5)
        for img in image_list:
            if face_detect(img.path) == img.face_count:
                success_count += 1
        success_percentage = success_count / len(image_list) * 100
        print(f'Actual success rate: {success_percentage}%')
        assert success_percentage > 40

    @mark.slow
    def test_success_rate_higher_than_30_given_all_images(self, images):
        success_count = 0
        image_list = images.get_all()
        for img in image_list:
            if face_detect(img.path) == img.face_count:
                success_count += 1
        success_percentage = success_count / len(image_list) * 100
        print(f'Actual success rate: {success_percentage}%')
        assert success_percentage > 30

    @mark.skip(reason="Broken by commit 0ee22f41e0136f6f7ae47e471f997514de243056. "
                      "Returns false positive and will be fixed next sprint")
    @mark.smoke
    def test_broken_test(self):
        assert False
