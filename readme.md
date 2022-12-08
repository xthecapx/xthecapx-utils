Run the followings commands to create the virtual env:

```
python3 -m venv ./venv
source ./venv/bin/activate
pip3 install -r requirements-test.txt
```

To run the test cases do:

```
coverage run -m pytest -v && coverage report -m
```

The solution to the challenge is:

```
/src/xthecapx_utils/utils.py
```
