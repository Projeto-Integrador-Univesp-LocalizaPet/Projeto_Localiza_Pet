<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Formulário de Postagem</title>
</head>
<body>
    <h1></h1>
    <form action="#" method="post" enctype="multipart/form-data">
        <label for="titulo">Título:</label><br>
        <input type="text" id="titulo" name="titulo" required><br><br>

        <label for="postagem">Postagem:</label><br>
        <textarea id="postagem" name="postagem" rows="7" cols="50" required></textarea><br><br>

        <label for="arquivo">Selecione um arquivo:</label><br>
        <input type="file" id="arquivo" name="arquivo" accept=".jpg, .jpeg, .png" required><br><br>

        <input type="submit" value="Enviar">
    </form>
</body>
</html>