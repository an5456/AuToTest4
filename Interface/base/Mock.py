from mock import mock


# 模拟mock封装
def moco_test(mock_method, request_data, url, method, response_data):
    mock_method = mock.Mock(return_value=request_data)
    return mock_method(url, method, response_data)
