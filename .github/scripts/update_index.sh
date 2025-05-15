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

git config user.email "you@example.com"
git add index.html
git commit -m "Update index.html with latest task info"
git push
