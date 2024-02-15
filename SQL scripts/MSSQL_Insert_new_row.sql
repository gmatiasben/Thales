USE [mercadoverde]
GO



INSERT INTO [dbo].[cdp_clientes_datos_personales]
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
VALUES
           ('1101'
           ,'11001001-1'
           ,'m'
           ,'11/01/2011'
           ,'Morales'
           ,'Gaston'
           ,'Morande 111'
           ,'Santiago'
           ,'01'
           ,'2'
           ,'11011101'
           ,'morales@gmail.com');

