CREATE PROCEDURE obtenerPlatosPorCategoriaId(IN catId INT)
BEGIN
    SELECT * FROM tbl_plato where categoria_id = catId;
END;

CREATE PROCEDURE obtenerCategoriaPorId(IN catId INT)
BEGIN
    SELECT * FROM tbl_categoria where categoria_id = catId;
END;

CREATE PROCEDURE obtenerCategorias()
BEGIN
    SELECT * FROM tbl_categoria;
END;