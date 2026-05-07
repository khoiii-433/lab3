import lab2.bmi as BMI


def test_bmi():
    expected_result = 23.1
    result = BMI.calculate_bmi(1.73, 70)
    assert (result == expected_result)




