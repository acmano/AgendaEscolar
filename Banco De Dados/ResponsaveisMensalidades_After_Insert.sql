DELIMITER $$

CREATE TRIGGER ResponsaveisMensalidades_After_Insert
AFTER INSERT
ON ResponsaveisMensalidades FOR EACH ROW
BEGIN
  call TitulosBancariosCria ( NEW.Matricula_id ) ;
END$$

DELIMITER ;