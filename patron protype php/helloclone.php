<? php
clase HelloClone
{
    private $ builtInConstructor;
    función pública __construct ()
    {
        echo "¡Hola, clon! <br />";
        $ this-> builtInConstructor = "Creación del constructor <br />";
    }

    función pública doWork ()
    {
        echo $ this-> builtInConstructor;
        echo "¡Estoy haciendo el trabajo! <p />";

    }
}
// Ejecutar constructor
$ original = new HelloClone ();
$ original-> doWork ();

// El clon no inicia el constructor
$ cloneIt = clon $ original;
$ cloneIt-> doWork ();

?>