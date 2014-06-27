# python-mocked-service

Example of mocking an external service in Python tests.

### Changes

|  #  | Commit |
| --- | ------ |
|  1 | [Add `get_repository` function][10] |
|  2 | [Add `test_get_repository` test case][11] |
|  3 | [Create a `repository` mock][12] |
|  4 | [Update test case to use `repository` mock][13] |
|  5 | [Create a repository test fixture for `burndown`][1] |
|  6 | [Refactor `repository` mock to use test fixtures][22] |
|  7 | [Rename `repository` mock to `resource_get`][25] |
|  8 | [Add `get_user` function][26] |
|  9 | [Add `test_get_user` test case][27] |
| 10 | [Create a user test fixture for `danriti`][28] |
| 11 | [Create `Resource` class for encapsulating file handling][31] |
| 12 | [Add error handling if resource is not available][32] |


[1]: https://github.com/danriti/python-mocked-service/commit/aff2c1832def24d8e771abbec756ea7c7822bb57
[10]: https://github.com/danriti/python-mocked-service/commit/c97eb466131c66cd3daf0b4c5e0014a5a4756bb0
[11]: https://github.com/danriti/python-mocked-service/commit/5003a893b1c52b662d4618a754e921e857e65f9f
[12]: https://github.com/danriti/python-mocked-service/commit/5c69623d77bbe5780d5d68dbc5e85bba08ae3770
[13]: https://github.com/danriti/python-mocked-service/commit/332f03211dbe307b8dcce9b11f7e939f54262276
[22]: https://github.com/danriti/python-mocked-service/commit/b8304d3a6e7225b2e2d2d9bdf3a7c623f095fba0
[25]: https://github.com/danriti/python-mocked-service/commit/f4e91a12fc401dd7f39f96a315e4eab19e8b115f
[26]: https://github.com/danriti/python-mocked-service/commit/9c7cad198d0e2eed8053198c08fe12f093ad17f5
[27]: https://github.com/danriti/python-mocked-service/commit/95e2c572fba2b7eec5bf6492876906b22c98e441
[28]: https://github.com/danriti/python-mocked-service/commit/c4f45acd4e29beff06b410892324c041f494641d
[31]: https://github.com/danriti/python-mocked-service/commit/7fc95b4a8a53b5555ccef529271aaca76fd3cf8e
[32]: https://github.com/danriti/python-mocked-service/commit/40a4ef112e11cba668b4d62f528e98b50d0041cd
