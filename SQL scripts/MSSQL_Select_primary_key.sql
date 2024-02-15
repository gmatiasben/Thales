USE [mercadoverde]
GO

SELECT * FROM [dbo].[bdt_clientes_facturacion],[dbo].[bdt_clientes_tarjetas]
WHERE  [dbo].[bdt_clientes_facturacion].[RUT] = [dbo].[bdt_clientes_tarjetas].[RUT];