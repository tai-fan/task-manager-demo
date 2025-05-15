#!/bin/bash
update_pre() {
  perl -i -pe "s|(<pre id=\"$1\">).*?(</pre>)|\1\n$2\n\2|s" index.html
}

todo=$(grep "ToDo Tasks" tasks_output.txt)
done=$(grep "Done Tasks" tasks_output.txt)
tests=$(cat test_output.txt)

update_pre "todo" "$todo"
update_pre "done" "$done"
update_pre "test" "$tests"