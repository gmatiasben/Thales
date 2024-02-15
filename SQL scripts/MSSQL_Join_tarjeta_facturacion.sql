USE [mercadoverde]
GO

SELECT 
	[dbo].[bdt_clientes_tarjetas].[RUT], 
	[dbo].[bdt_clientes_tarjetas].[tc_numero], 
	[dbo].[bdt_clientes_tarjetas].[tc_expiracion], 
	[dbo].[bdt_clientes_facturacion].[facturacion]
	
	INTO [dbo].[bdt_clientes_join_tf]
	FROM [dbo].[bdt_clientes_tarjetas]
	INNER JOIN [dbo].[bdt_clientes_facturacion]
	ON [dbo].[bdt_clientes_tarjetas].[RUT]=[dbo].[bdt_clientes_facturacion].[RUT];