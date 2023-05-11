kotlinc-jvm -J-Xms1024m -J-Xmx1920m -J-Xss512m -include-runtime -d $1.jar $1.kt
java -Xms1024m -Xmx1920m -Xss512m -Dfile.encoding=UTF-8 -XX:+UseSerialGC -DONLINE_JUDGE=1 -DBOJ=1 -jar $1.jar
