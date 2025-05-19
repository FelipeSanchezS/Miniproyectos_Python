<?php include 'bases.php'; ?>

<h2>Formulario de Personas</h2>
<form action="actualizar.php" method="POST">
    <label for="">Nombre</label>
    <input type="text" name="nombre" placeholder="Nombre" required><br>
    <label for="">Apellido</label>
    <input type="text" name="apellido" placeholder="Apellido" required><br>
    <label for="">Email</label>
    <input type="email" name="email" placeholder="Correo" required><br>
    <label for="">Teléfono</label>
    <input type="text" name="teléfono" placeholder="Teléfono" required><br>
    <label for="">Dirección</label>
    <input type="text" name="dirección" placeholder="Dirección" required><br>
    <label for="">Fecha nacimiento</label>
    <input type="text" name="fecha_nacimiento" required><br>
    <button type="submit">Guardar</button>
</form>

<h2>Lista de personas</h2>
<table border="1">
    <tr>
        <th>ID</th><th>Nombre</th><th>Apellido</th><th>Email</th>
        <th>Teléfono</th><th>Dirección</th><th>Fecha</th><th>Acciones</th>
    </tr>
    <?php
    $sql = "SELECT * FROM personas";
    $result = $conn->query($sql);
    while($row = $result->fetch_assoc()) {
        echo "<tr>
                <td>{$row['id']}</td>
                <td>{$row['nombre']}</td>
                <td>{$row['apellido']}</td>
                <td>{$row['email']}</td>
                <td>{$row['telefono']}</td>
                <td>{$row['direccion']}</td>
                <td>{$row['fecha_nacimiento']}</td>
                <td>
                    <a href='actualizar.php?id={$row['id']}'>Editar</a> |
                    <a href='eliminar.php?id={$row['id']}'>Eliminar</a>
                </td>
            </tr>";
    }
    ?>
</table>
