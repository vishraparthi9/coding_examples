class HelloWorld {

  static void main(String[] args){
    /*println "Hello World!!"

    // In groovy, semicolons are optional 
    // at the end of each line
    int age = 40;
    println age;

    println age.getClass();

    // In groovy, defining the data type of 
    // variables is not mandatory (dynamic typing)
    def name = "Bob"
    println name
    println name.getClass()
    

    Person johnDoe = new Person()

    // In groovy, get methods and set methods
    // are automatically provided
    johnDoe.setFirstName("John")
    johnDoe.setLastName("Doe")
    johnDoe.setAge(40)

    println johnDoe.getFirstName()
    println johnDoe.getLastName()
    println johnDoe.getAge()
    println johnDoe.getFullName()

    // If-else condition
    if (johnDoe.getAge() >= 45 && johnDoe.getAge <= 65) {
      println johnDoe.getFullName() + " is a middle age man."
    } else {
      println johnDoe.getFullName() + " is " + johnDoe.getAge() + " years old"
    }

    // Collections in groovy
    def persons = [ johnDoe, new Person(firstName: "Mary", lastName: "Hill", age: 46)]

    for (Person p : persons) {
      println p.getFullName()
    }
    */

    Calculator calc = new Calculator()
    int a = 5
    int b = 10
    println calc.add(a, b)
    println calc.subtract(b, a)
    println calc.multiply(a, b)
    println calc.divide(b, a)
    // The below function call will return divide by zero exception
    // println calc.divide(a, 0)

  }
}