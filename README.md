# micro_cam

* This project is in a mostly workable state, with some rough edges. Temporarily been put on the backburner.
* The code style is setup to be procedural, using Classes as psuedo namespaces. Structure isn't finalized and couple use some refactoring.


* for project scripts, .\play_book.ipynb
* for dev runtime debugger, use launch.json configuration
* manually clear test files with .\util\Delete-Tap.ps1

## Function Chain

* Build config
* Parse Mesh, build Object structure
* Parse Que, build Object structure
* Parse Que, sort into Objects
* Merge Object Fragments into Final Objects
* Apply any transforms to Objects if necessary
* Write Objects to .tap file

## Variable Scheme

* Mesh/Object > Line > Coord
