DROP PROCEDURE TitulosBancariosCria;

DELIMITER $$
CREATE PROCEDURE TitulosBancariosCria(
  IN pMatricula_Id INTEGER
  )
BEGIN
  DECLARE lResponsavelMensalidade_id INTEGER ;
  DECLARE lValor DECIMAL(6,2) ;
  DECLARE lMatricula_Id INTEGER ;
  DECLARE lAnoLetivo INTEGER ;
  DECLARE iMes integer ;
  DECLARE iDataVencimento DATE ;
  SELECT  ResponsaveisMensalidades.ResponsavelMensalidade_id
        , TabelasPrecos.Valor
        , Matriculas.Matricula_Id
        , Turmas.AnoLetivo
	INTO  lResponsavelMensalidade_id
        , lValor
        , lMatricula_Id
        , lAnoLetivo
    from  ResponsaveisMensalidades
    inner join ResponsaveisAlunos
      on  ResponsaveisAlunos.ResponsavelAluno_Id
        = ResponsaveisMensalidades.ResponsavelAluno_Id
    inner join Responsaveis
      on  Responsaveis.Responsavel_Id
        = ResponsaveisAlunos.Responsavel_Id
    inner join Pessoas
      on  Pessoas.Pessoa_Id
        = Responsaveis.Pessoa_Id
    inner join Matriculas
      on  Matriculas.Matricula_Id
        = ResponsaveisMensalidades.Matricula_Id
    inner join Turmas
      on  Turmas.TurmaId
        = Matriculas.Turma_Id
    inner join TurmasTabelas
      on  TurmasTabelas.Turma_Id
        = Turmas.TurmaId
    inner join TabelasPrecos
      on  TabelasPrecos.TabelaPrecoId
        = TurmasTabelas.Tabela_Id
    where Matriculas.Matricula_Id = pMatricula_Id
  ;
  set iMes = 1;
  while iMes <= 12 do
    set iDataVencimento = DATE(CONCAT_WS('-', lAnoLetivo, iMes, 1)) ;
    insert
      into TitulosBancarios
      (
        Vencimento
	  , Valor
      , Matricula_id
      , ResponsavelMensalidade_id
      )
      values
      (
        iDataVencimento
	  , lValor
      , lMatricula_Id
      , lResponsavelMensalidade_id
      ) ;
    set iMes = iMes + 1 ;
  end while ;
END$$

DELIMITER ;