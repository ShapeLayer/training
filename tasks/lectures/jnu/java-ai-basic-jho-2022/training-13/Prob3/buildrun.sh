javac -d ./derived ./base/Shape.java
javac -d ./app ./base/Shape.java
javac -d ./app ./derived/Circle.java
cd ./app
java GraphicEditor.java
cd ../
