#!/usr/bin/env bash


echo -n '' > test_doc.txt  # just to truncate the file
i=0

for file in test_{base_model.py,user.py,place.py,state.py,city.py,amenity.py,review.py,file_storage.py}
do
	comments=$(grep -Eo 'T[A-Z]{4}-[A-Z]{2}.*' "$file")  # retrieve comments from file

	if [[ "$i" -gt 0 ]]
	then
		echo -e "\n\n" >> test_doc.txt
	fi

	(( i++ ))

	echo ======= "$file" ====== >> test_doc.txt
	echo >> test_doc.txt
	echo "$comments" >> test_doc.txt

	#sorted=$(sort test_doc.txt)
	#echo "$sorted" > test_doc.txt
	#unique=$(uniq test_doc.txt)
	#echo "$unique" > test_doc.txt
done
