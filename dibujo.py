import cv2
import numpy as np
import tkinter as tk
from tkinter import filedialog
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
import os

# Función para abrir el cuadro de diálogo y obtener la ruta de la imagen
def open_file_dialog():
    file_path = filedialog.askopenfilename(title="Selecciona una imagen", filetypes=[("Archivos de imagen", "*.jpg;*.png;*.jpeg")])
    return file_path

# Función para dibujar la línea perpendicular en el medio de la primera línea trazada
def draw_perpendicular_line(pt1, pt2):
    mid_point = ((pt1[0] + pt2[0]) // 2, (pt1[1] + pt2[1]) // 2)
    dx = pt2[0] - pt1[0]
    dy = pt2[1] - pt1[1]

    length = int(np.sqrt(dx*dx + dy*dy))  # Aumentar la longitud de la línea perpendicular
    angle = np.arctan2(dy, dx) + np.pi / 2

    end_point1 = (int(mid_point[0] + length * np.cos(angle)), int(mid_point[1] + length * np.sin(angle)))
    end_point2 = (int(mid_point[0] - length * np.cos(angle)), int(mid_point[1] - length * np.sin(angle)))

    cv2.line(img, end_point1, end_point2, (0, 0, 255), 2)

# Función para dibujar una línea recta
def draw_straight_line(event, x, y, flags, param):
    global line_points, lines

    if event == cv2.EVENT_LBUTTONDOWN:
        line_points.append((x, y))
        cv2.circle(img, (x, y), 2, (0, 255, 0), -1)

        if len(line_points) == 2:
            lines.append(line_points.copy())
            cv2.line(img, line_points[0], line_points[1], (0, 255, 0), 2)
            draw_perpendicular_line(line_points[0], line_points[1])  # Dibujar la línea perpendicular
            calculate_dimensions()
            line_points = []
            
        cv2.imshow('Image', img)  # Mostrar la imagen actualizada

# Función para dibujar un arco
def draw_arc(event, x, y, flags, param):
    global arc_points, arcs, lines
    if event == cv2.EVENT_LBUTTONDOWN and lines:
        arc_center = ((lines[0][0][0] + lines[0][1][0]) // 2, (lines[0][0][1] + lines[0][1][1]) // 2)
        arc_second_point = lines[0][1]
        arc_points = [arc_center, arc_second_point, (x, y)]
        cv2.circle(img, arc_center, 2, (0, 255, 0), -1)  # Dibuja el punto central en verde
        cv2.circle(img, arc_second_point, 2, (0, 255, 0), -1)  # Dibuja el segundo punto en verde
        cv2.circle(img, (x, y), 2, (0, 255, 0), -1)  # Dibuja el tercer punto en verde

        cv2.ellipse(img, arc_points[0], (abs(arc_points[1][0] - arc_points[0][0]), abs(arc_points[2][1] - arc_points[0][1])),
                    0, 180, 360, (0, 255, 0), 2)
        arcs.append(arc_points.copy())
        calculate_dimensions()
        
        cv2.imshow('Image', img)  # Mostrar la imagen actualizada


# Función para calcular H y W
def calculate_dimensions():
    global H, W, angulo
    if lines and arcs:
        pt1, pt2 = lines[-1]
        W = np.sqrt((pt2[0] - pt1[0])**2 + (pt2[1] - pt1[1])**2)

        arc_highest_point = min(arcs[-1], key=lambda point: point[1])
        mid_point = ((pt1[0] + pt2[0]) // 2, (pt1[1] + pt2[1]) // 2)
        H = abs(arc_highest_point[1] - mid_point[1])

        if W != 0:
            angulo = 2 * np.degrees(np.arctan((2 * H) / W))
        else:
            angulo = 0
    else:
        H = W = angulo = 0
    
    update_labels()

# Función para actualizar las etiquetas de H, W y ángulo
def update_labels():
    h_label.config(text=f'H: {H:.10f}')
    w_label.config(text=f'W: {W:.10f}')
    angulo_label.config(text=f'Ángulo: {angulo:.10f}°')

# Función para resetear los puntos y la imagen
def reset_points():
    global line_points, lines, arc_points, arcs, img

    line_points = []
    lines = []
    arc_points = []
    arcs = []

    img = original_img.copy()  # Restaurar la imagen original
    cv2.imshow('Image', img)  # Mostrar la imagen restaurada
    calculate_dimensions()

def generate_report():
    global img, H, W, angulo

    pdf_filename = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("Archivos PDF", "*.pdf")])

    if pdf_filename:
        pdf_canvas = canvas.Canvas(pdf_filename, pagesize=letter)

        # Guardar la imagen en formato JPG temporalmente
        temp_img_filename = "temp_image.jpg"
        cv2.imwrite(temp_img_filename, img)

        # Insertar la imagen en el informe PDF
        pdf_canvas.drawInlineImage(temp_img_filename, 100, 400, width=400, height=300)

        # Agregar los textos después de la imagen
        pdf_canvas.drawString(100, 350, f'H: {H:.10f}')
        pdf_canvas.drawString(100, 330, f'W: {W:.10f}')
        pdf_canvas.drawString(100, 310, f'Ángulo: {angulo:.10f}°')

        pdf_canvas.save()

        # Eliminar el archivo de imagen temporal
        os.remove(temp_img_filename)

# Función para cargar una nueva imagen
def load_new_image():
    global img, original_img, line_points, lines, arc_points, arcs

    file_path = open_file_dialog()
    if file_path:
        original_img = cv2.imread(file_path)
        img = original_img.copy()

        # Reiniciar puntos y líneas
        line_points = []
        lines = []
        arc_points = []
        arcs = []

        # Limpiar y configurar la ventana de imagen
        cv2.imshow('Image', img)
        cv2.setMouseCallback('Image', draw_straight_line)

        # Actualizar dimensiones y etiquetas
        calculate_dimensions()

# Configurar la ventana principal de Tkinter y OpenCV
root = tk.Tk()
root.withdraw()  # Ocultar la ventana principal de Tkinter

# Obtener la ruta de la imagen inicial
file_path = open_file_dialog()

if file_path:
    original_img = cv2.imread(file_path)
    img = original_img.copy()

    # Variables para el dibujo de línea recta
    line_points = []
    lines = []

    # Variables para el dibujo de arco
    arc_points = []
    arcs = []

    # Inicializar H, W y ángulo
    H = W = angulo = 0

    # Configurar la función de callback para eventos del ratón
    cv2.namedWindow('Image')
    cv2.setMouseCallback('Image', draw_straight_line)

    # Crear ventana de tkinter para botones, etiquetas y menú desplegable
    root.deiconify()  # Mostrar la ventana principal de Tkinter

    # Botones de opciones
    line_button = tk.Button(root, text="Línea Recta", command=lambda: [cv2.setMouseCallback('Image', draw_straight_line), update_labels()])
    line_button.pack(side=tk.LEFT, padx=5)

    arc_button = tk.Button(root, text="Arco", command=lambda: [cv2.setMouseCallback('Image', draw_arc), update_labels()])
    arc_button.pack(side=tk.LEFT, padx=5)

    reset_button = tk.Button(root, text="Resetear Puntos", command=reset_points)
    reset_button.pack(side=tk.LEFT, padx=5)

    new_image_button = tk.Button(root, text="Cargar Nueva Imagen", command=load_new_image)
    new_image_button.pack(side=tk.RIGHT, padx=5)

    # Etiquetas de altura, anchura y ángulo
    h_label = tk.Label(root, text=f'H: {H:.10f}')
    h_label.pack(side=tk.BOTTOM, padx=5)

    w_label = tk.Label(root, text=f'W: {W:.10f}')
    w_label.pack(side=tk.BOTTOM, padx=5)

angulo_label = tk.Label(root, text=f'Ángulo: {angulo:.10f}°')
angulo_label.pack(side=tk.BOTTOM, padx=5)

# Botón para generar el reporte
report_button = tk.Button(root, text="Generar Reporte", command=generate_report)
report_button.pack(side=tk.RIGHT, padx=5)

# Mostrar la imagen inicial
cv2.imshow('Image', img)

while True:
    # Actualizar la interfaz de tkinter
    root.update()

    # Salir del bucle cuando se presiona la tecla 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cerrar las ventanas
cv2.destroyAllWindows()
root.destroy()
