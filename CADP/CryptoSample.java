/*
* Encryption and decryption class using Thales CADP 8.15.
* Written by Matias Bendel.
* v1.0
*/

import java.security.*;
import javax.crypto.*;
import javax.crypto.spec.*;
import com.ingrian.security.nae.*;
import java.util.Random;

public class CryptoSample {
	public static void main(String[] args) throws Exception {
		
		if (args.length != 2 || args[0].length() != 16) {
			System.out.println("Usage: java CryptoSample <IV> <text to cipher>");
			System.exit(-1);
		}
		
		String ivStr = args[0];		
		String text = args[1];		
		NAESession session = null;
		
		try {
			/* Encryption example: https://www.thalesdocs.com/ctp/con/cadp/cadp-java/8.15.0/admin/cadp-for-java-tasks/encrypt-string/index.html
			*
			* NAESession session = NAESession.getSession("user1","password1".toCharArray());
			* NAESecureRandom sr=new NAESecureRandom(session);
			* byte []iv = new byte[16];
			* sr.nextBytes(iv);
			* Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding","IngrianProvider");
			* SecretKey key = NAEKey.getSecretKey("user1key", session);
			* cipher.init(Cipher.ENCRYPT_MODE, key,new IvParameterSpec(iv));
			* byte [] ciphertext = cipher.doFinal("Hello World!".getBytes());
			*
			*/
			
			session = NAESession.getSession("admin","Thales12345!".toCharArray());
			NAESecureRandom sr=new NAESecureRandom(session);
			// byte [] iv = new byte[16];
			// sr.nextBytes(iv);
			// IV random generation replaced with parameter that is passed as an argument
			byte [] iv = ivStr.getBytes();
			Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding","IngrianProvider");
			SecretKey key = NAEKey.getSecretKey("cbc_key", session);
			cipher.init(Cipher.ENCRYPT_MODE,key,new IvParameterSpec(iv));
			byte [] ciphertext = cipher.doFinal(text.getBytes("UTF-8"));
		
			/* Decryption example: https://www.thalesdocs.com/ctp/con/cadp/cadp-java/8.15.0/admin/cadp-for-java-tasks/decrypt-string/index.html
			*
			* NAESession session = NAESession.getSession("user1","password1".toCharArray());
			* byte [] iv = ...
			* // get IV used during Encrypt operation 
			* byte [] ciphertext = ...
			* // get ciphertext 
			* Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding","IngrianProvider");
			* SecretKey key = NAEKey.getSecretKey("user1key", session);
			* cipher.init(Cipher.DECRYPT_MODE, key,newIvParameterSpec(iv));
			* byte [] plaintext = cipher.doFinal(ciphertext);
			* String hello =new String(plaintext);
			*
			*/

			cipher.init(Cipher.DECRYPT_MODE,key,new IvParameterSpec(iv));
			byte [] plaintext = cipher.doFinal(ciphertext);
			
			// Output
			System.out.println("");
			System.out.println("Text:        " + new String(text));
			System.out.println("Ciphertext:  " + new String(ciphertext,"ISO-8859-1"));
			System.out.println("Plaintext:   " + new String(plaintext));
			
			
		} catch (Exception e) {
			e.printStackTrace();
			throw e;
		} finally {
			if (session != null)
				session.closeSession();
		}	
	}

}
