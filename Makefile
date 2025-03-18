ifndef day
$(error day is not defined. Usage: make day=<value>)
endif

all:
	-cp -n template.py src/$(day)a.py
	-cp -n template.py src/$(day)b.py
	-touch input/$(day).in
	-touch test/$(day).in
	code -r src/$(day)a.py
	code -r src/$(day)b.py
	code -r input/$(day).in
	code -r test/$(day).in