import tkinter as tk  # Importar la biblioteca tkinter para crear la interfaz gráfica
import project as pp  # Importar el módulo 'project' que contiene las funciones de encriptación y desencriptación de contraseñas

def main():
    # Declarar variables globales para los frames de la interfaz
    global main_menu_frame, encrypt_frame, generate_frame, decrypt_frame
    
    # Crear la ventana principal de la aplicación
    root = tk.Tk()
    root.title("CIPHER-KEY")  # Establecer el título de la ventana
    root.configure(bg="#222222")  # Establecer el color de fondo de la ventana
    root.geometry("400x400")  # Establecer las dimensiones de la ventana
    
    # Crear un label para el título de la aplicación
    label = tk.Label(root, text="CIPHER", bg="#222222", fg="#ffffff", font=("Helvetica", 20, "bold"))
    label.pack(pady=15)  # Colocar el label en la ventana con un espacio vertical de 15 píxeles
    
    # Frame para el menú principal
    main_menu_frame = tk.Frame(root, bg="#222222")  # Crear un frame para el menú principal
    
    # Crear botones para las diferentes opciones del menú principal
    encrypt_button = tk.Button(main_menu_frame, text="Encrypt Password", bg="#444444", fg="white", command=show_encrypt_frame)
    encrypt_button.pack(pady=5)  # Colocar el botón 'Encrypt Password' en el frame con un espacio vertical de 5 píxeles
    
    generate_button = tk.Button(main_menu_frame, text="Generate & Encrypt Random Password", bg="#444444", fg="white", command=generate_encrypted_password)
    generate_button.pack(pady=5)  # Colocar el botón 'Generate & Encrypt Random Password' en el frame con un espacio vertical de 5 píxeles
    
    decrypt_button = tk.Button(main_menu_frame, text="Decrypt Password", bg="#444444", fg="white", command=show_decrypt_frame)
    decrypt_button.pack(pady=5)  # Colocar el botón 'Decrypt Password' en el frame con un espacio vertical de 5 píxeles
    
    exit_button = tk.Button(main_menu_frame, text="Exit", bg="#444444", fg="white", command=root.destroy)
    exit_button.pack(pady=5)  # Colocar el botón 'Exit' en el frame con un espacio vertical de 5 píxeles
    
    main_menu_frame.pack()  # Colocar el frame del menú principal en la ventana
    
    # Frame para encriptar contraseña
    encrypt_frame = tk.Frame(root, bg="#222222")  # Crear un frame para encriptar contraseña
    
    # Crear elementos para encriptar contraseña
    encrypt_label = tk.Label(encrypt_frame, text="Ingrese la contraseña a encriptar:", bg="#222222", fg="#ffffff", font=("Helvetica", 12))
    encrypt_label.pack()  # Colocar el label en el frame
    
    encrypt_entry = tk.Entry(encrypt_frame, show="*")  # Crear un campo de entrada para la contraseña
    encrypt_entry.pack()  # Colocar el campo de entrada en el frame
    
    encrypt_button = tk.Button(encrypt_frame, text="Encrypt", bg="#444444", fg="white", command=lambda: encrypt_user_password(encrypt_entry.get()))
    encrypt_button.pack(pady=5)  # Colocar el botón 'Encrypt' en el frame con un espacio vertical de 5 píxeles
    
    back_button1 = tk.Button(encrypt_frame, text="Volver", bg="#444444", fg="white", command=show_main_menu)
    back_button1.pack(pady=5)  # Colocar el botón 'Volver' en el frame con un espacio vertical de 5 píxeles
    
    # Frame para generar y encriptar contraseña aleatoria
    generate_frame = tk.Frame(root, bg="#222222")  # Crear un frame para generar y encriptar contraseña aleatoria
    
    # Crear botón para generar y encriptar contraseña aleatoria
    generate_button = tk.Button(generate_frame, text="Generate & Encrypt Random Password", bg="#444444", fg="white", command=generate_encrypted_password)
    generate_button.pack(pady=5)  # Colocar el botón en el frame con un espacio vertical de 5 píxeles
    
    back_button2 = tk.Button(generate_frame, text="Volver", bg="#444444", fg="white", command=show_main_menu)
    back_button2.pack(pady=5)  # Colocar el botón 'Volver' en el frame con un espacio vertical de 5 píxeles
    
    # Frame para desencriptar contraseña
    decrypt_frame = tk.Frame(root, bg="#222222")  # Crear un frame para desencriptar contraseña
    
    # Crear elementos para desencriptar contraseña
    decrypt_hero_label = tk.Label(decrypt_frame, text="Ingrese el héroe:", bg="#222222", fg="#ffffff", font=("Helvetica", 12))
    decrypt_hero_label.pack()  # Colocar el label en el frame
    
    decrypt_hero_entry = tk.Entry(decrypt_frame)  # Crear un campo de entrada para el héroe
    decrypt_hero_entry.pack()  # Colocar el campo de entrada en el frame
    
    decrypt_number_label = tk.Label(decrypt_frame, text="Ingrese el número:", bg="#222222", fg="#ffffff", font=("Helvetica", 12))
    decrypt_number_label.pack()  # Colocar el label en el frame
    
    decrypt_number_entry = tk.Entry(decrypt_frame)  # Crear un campo de entrada para el número
    decrypt_number_entry.pack()  # Colocar el campo de entrada en el frame
    
    decrypt_button = tk.Button(decrypt_frame, text="Decrypt", bg="#444444", fg="white", command=lambda: decrypt_and_show_password(decrypt_hero_entry.get().replace(" ",""), decrypt_number_entry.get()))
    decrypt_button.pack(pady=5)  # Colocar el botón 'Decrypt' en el frame con un espacio vertical de 5 píxeles
    
    back_button3 = tk.Button(decrypt_frame, text="Volver", bg="#444444", fg="white", command=show_main_menu)
    back_button3.pack(pady=5)  # Colocar el botón 'Volver' en el frame con un espacio vertical de 5 píxeles
    
    root.mainloop()  # Iniciar el bucle principal de la aplicación

def show_main_menu():
    # Función para mostrar el menú principal
    show_frame(main_menu_frame)

def show_encrypt_frame():
    # Función para mostrar el frame de encriptar contraseña
    show_frame(encrypt_frame)

def show_decrypt_frame():
    # Función para mostrar el frame de desencriptar contraseña
    show_frame(decrypt_frame)

def show_frame(frame):
    # Función para mostrar un frame específico y ocultar los demás
    main_menu_frame.pack_forget()
    encrypt_frame.pack_forget()
    generate_frame.pack_forget()
    decrypt_frame.pack_forget()
    frame.pack()

def show_message(message):
    # Función para mostrar un mensaje en el menú principal
    message_label = tk.Label(main_menu_frame, text=message, bg="#222222", fg="#ffffff", font=("Helvetica", 12))
    message_label.pack(pady=10)  # Colocar el label en el frame con un espacio vertical de 10 píxeles

def encrypt_user_password(password):
    # Función para encriptar una contraseña ingresada por el usuario
    if password:
        if pp.check_password_strength(password):
            hero, number, _, cipher_data = pp.encrypt_password(password)
            hero = ''.join(' ' + i if i.isupper() else i for i in hero).lstrip(' ')
            show_message(f"Una contraseña fue encriptada con el héroe {hero} y el número {number}.")
        else:
            show_message("La contraseña debe tener al menos 12 caracteres, con al menos 1 mayúscula, 1 minúscula, un dígito y un carácter especial.")

def generate_encrypted_password():
    # Función para generar y encriptar una contraseña aleatoria
    password = pp.generate_password()
    hero, number, _, cipher_data = pp.encrypt_password(password)
    hero = ''.join(' ' + i if i.isupper() else i for i in hero).lstrip(' ')
    show_message(f"La contraseña {password} fue generada y encriptada con el héroe {hero} y el número {number}.")

def decrypt_and_show_password(hero, number):
    # Función para desencriptar una contraseña usando el héroe y el número proporcionados
    if hero and number:
        cipher = pp.load_data(hero, int(number))
        if cipher is not None:
            password = pp.decrypt(cipher)
            if password is not None:
                show_message(f"La contraseña generada es: {password}")
            else:
                show_message("La contraseña no pudo ser desencriptada.")
        else:
            show_message("El héroe y número especificados no fueron encontrados.")

if __name__ == "__main__":
    main()  # Ejecutar la función principal si este script se ejecuta como el programa principal
