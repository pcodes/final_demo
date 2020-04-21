import sys
from v9 import V9Component


def test(http_method, path, request_arguments, request_body):
    print(http_method, path, request_arguments, request_body)
    return 200, "This is the final demo"

def getWeather(http_method, path, request_arguments, request_body):
    print(http_method, path, request_arguments, request_body)
    return 200, "70 degrees and sunny"

if __name__ == '__main__':
    print("Arguments " + str(sys.argv))
    comp = V9Component(sys.argv[1], sys.argv[2])

    comp.register_operation("Test", test)
    comp.register_operation("Weather", getWeather)

    comp.loop()
