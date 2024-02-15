USE [mercadoverde]
GO

SELECT 
	[dbo].[clientes_datos_personales].[ID], 
	[dbo].[clientes_datos_personales].[RUT], 
	[dbo].[clientes_datos_personales].[nombre], 
	[dbo].[clientes_datos_personales].[apellido], 
	[dbo].[clientes_tarjetas].[tc_numero], 
	[dbo].[clientes_tarjetas].[tc_expiracion], 
	[dbo].[clientes_facturacion].[facturacion]
	
	FROM [dbo].[clientes_datos_personales]
	INNER JOIN [dbo].[clientes_tarjetas]
	ON [dbo].[clientes_datos_personales].[RUT]=[dbo].[clientes_tarjetas].[RUT]
	INNER JOIN [dbo].[clientes_facturacion]
	ON [dbo].[clientes_tarjetas].[RUT]=[dbo].[clientes_facturacion].[RUT]
	ORDER BY [dbo].[clientes_datos_personales].[ID];