# this will import the gradingSystem funcion and test the grade function, and write the results on a .txt
from gradingSystem import grade 
def test(testdata, expected_result):
    for i in testdata:
        f.write(str(i).rjust(9))
        f.write(expected_result.rjust(13))
        f.write(grade(i).rjust(17))
        if expected_result == grade(i):
            f.write('Passed\n'.rjust(15))
        else:
            f.write('Fail\n'.rjust(15))
        

error_values = [-5, 101]
fail_values = [0, 45]
c_values = [50, 55, 59]
b_values = [60, 65, 69]
a_values = [70, 78, 79]
aplus_values=[80, 89, 100]



f = open('test_result.txt', 'w')


f.write("Test data |Expected result | Actual result | Pass/Fail\n")
test(error_values,"error")
test(fail_values, "F")
test(c_values, 'C')
test(b_values, 'B')
test(a_values, "A")
test(aplus_values, 'A+')
f.close()


