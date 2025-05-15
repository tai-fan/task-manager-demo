#!/bin/bash
python3 todo.py | tee tasks_output.txt
python3 todo-test.py | tee test_output.txt
bash .github/scripts/update_index.sh