<?php
include 'bases.php';

if ($_SERVER['REQUEST_METHOD'] == 'GET') {
    $id = $_GET['id'];
    $sql = "SELECT * FROM personas WHERE id = $id";
    $result = $conn->query($sql);
    $row = $result->fetch_assoc();
?>
<form action="actualizar.php" method="POST">
    <input type="hidden" name="id" value="<?= $row['id'] ?>">
    <input type="text" name="nombre" value="<?= $row['nombre'] ?>"><br>
    <input type="text" name="apellido" value="<?= $row['apellido'] ?>"><br>
    <input type="email" name="email" value="<?= $row['email'] ?>"><br>
    <input type="text" name="telefono" value="<?= $row['telefono'] ?>"><br>
    <input type="text" name="direccion" value="<?= $row['direccion'] ?>"><br>
    <input type="date" name="fecha_nacimiento" value="<?= $row['fecha_nacimiento'] ?>"><br>
    <button type="submit">Actualizar</button>
</form>
<?php } else {
    $id = $_POST['id'];
    $nombre = $_POST['nombre'];
    $apellido = $_POST['apellido'];
    $email = $_POST['email'];
    $telefono = $_POST['telefono'];
    $direccion = $_POST['direccion'];
    $fecha = $_POST['fecha_nacimiento'];

    $sql = "UPDATE personas SET nombre='$nombre', apellido='$apellido', email='$email',
            telefono='$telefono', direccion='$direccion', fecha_nacimiento='$fecha'
            WHERE id=$id";

    $conn->query($sql);
    header("Location: formulario.php");
}
?>
