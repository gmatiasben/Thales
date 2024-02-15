USE [mercadoverde.uat]
GO

CREATE TABLE [dbo].[bdt_clientes_datos_personales] (
	[ID] varchar(50),
	[RUT] varchar(50),
	[genero] varchar(50),
	[nacimiento] varchar(50),
	[apellido] varchar(50),
	[nombre] varchar(50),
	[dirección] varchar(50),
	[comuna] varchar(50),
	[region] varchar(50),
	[codigo_area] varchar(50),
	[telefono] varchar(50),
	[email] varchar(50),
    PRIMARY KEY (RUT)
);

CREATE TABLE [dbo].[bdt_clientes_facturacion] (
	[ID] varchar(50),
	[RUT] varchar(50),
	[facturacion] varchar(50),
	[numero_ventas] varchar(50),
	[ventas_web] varchar(50),
    FOREIGN KEY (RUT) REFERENCES bdt_clientes_datos_personales(RUT)
);

CREATE TABLE [dbo].[bdt_clientes_tarjetas] (
	[ID] varchar(50),
	[RUT] varchar(50),
	[tc_tipo] varchar(50),
	[tc_numero] varchar(50),
	[tc_cvc] varchar(50),
	[tc_expiracion] varchar(50),
    FOREIGN KEY (RUT) REFERENCES bdt_clientes_datos_personales(RUT)
);

INSERT INTO [dbo].[bdt_clientes_datos_personales]
           ([ID]
           ,[RUT]
           ,[genero]
           ,[nacimiento]
           ,[apellido]
           ,[nombre]
           ,[dirección]
           ,[comuna]
           ,[region]
           ,[codigo_area]
           ,[telefono]
           ,[email])
	SELECT * FROM [mercadoverde].[dbo].[clientes_datos_personales];

INSERT INTO [dbo].[bdt_clientes_facturacion]
           ([ID]
           ,[RUT]
           ,[facturacion]
           ,[numero_ventas]
           ,[ventas_web])
	SELECT * FROM [mercadoverde].[dbo].[clientes_facturacion];

INSERT INTO [dbo].[bdt_clientes_tarjetas]
           ([ID]
           ,[RUT]
           ,[tc_tipo]
           ,[tc_numero]
           ,[tc_cvc]
           ,[tc_expiracion])
	SELECT * FROM [mercadoverde].[dbo].[clientes_tarjetas];