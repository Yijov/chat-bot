import re
import random

def get_response(user_input):
    split_message = re.split(r'\s|[,:;.?!-_]\s*', user_input.lower())
    response = check_all_messages(split_message)
    return response

def message_probability(user_message, recognized_words, single_response=False, required_word=[]):
    message_certainty = 0
    has_required_words = True

    for word in user_message:
        if word in recognized_words:
            message_certainty +=1

    percentage = float(message_certainty) / float (len(recognized_words))

    for word in required_word:
        if word not in user_message:
            has_required_words = False
            break
    if has_required_words or single_response:
        return int(percentage * 100)
    else:
        return 0

def check_all_messages(message):
        highest_prob = {}

        def response(bot_response, list_of_words, single_response = False, required_words = []):
            nonlocal highest_prob
            highest_prob[bot_response] = message_probability(message, list_of_words, single_response, required_words)

        response('Hola', ['hola', 'klk', 'saludos', 'buenas'], single_response = True)
        response('Estoy bien y tu?', ['como', 'estas', 'va', 'vas', 'sientes'], required_words=['como'])
        response('Estamos ubicados en la Autopista Las Américas, Km. 27, PCSD, La Caleta, Boca Chica', ['ubicados', 'direccion', 'donde', 'ubicacion', 'lugar', 'localizados', 'local', 'sede', 'oficinas', 'recinto'], single_response=True)
        response('Nuestros números de contacto son 809-738-4852 y 809-793-255, tambien puede contactarnos en info@itla.edu.do', ['mensaje', 'contactar', 'mail', 'numero', 'email', 'correo', 'telefono', 'llamar', 'comunicarme', 'contacto'], single_response=True)
        response('El Instituto Tecnológico de las Américas fue fundado el 15 de agosto de 2000', ['fundacion', 'inauguracion', 'apertura', 'cuando', 'año', 'fecha', 'historia', 'inicio', 'empezo', 'institucion'], single_response=True)
        response('Estamos abiertos de lunes a vierfnes de 8:00am  a 10pm y sábados hasta las 6pm', ['horario', 'horas', 'oficinas', 'abiertos', 'disponibles', 'hora', 'cierran', 'abren', 'domingos', 'dias'], single_response=True)
        response('Las áreas de especialización del ITLA son: Desarrollo de Software, Redes de Información, Multimedia, Sonido, Mecatrónica, Manufactura Automatizada y Seguridad Informática. Además cuenta con la Escuela de Idiomas y un Diplomado en Ciencia de Datos', ['carreras', 'clases', 'tecnicas', 'imparten', 'dan', 'cuales', 'disponibles', 'cursos', 'materias', 'escuela'], single_response=True)
        response('Los requisitos son Ser bachiller y cumplir con las fechas, procesos y documentos requeridos.', ['documentos', 'requisitos', 'inscribo', 'inscripcion', 'entrar', 'admision', 'matricularme', 'inscribirme', 'pasos', 'instrucciones'], single_response=True)
        response('Nuestras carreras tecnológicas tienen una duracion de dos años', ['duracion', 'tiempo', 'periodo', 'terminar', 'cuanto', 'tiempo', 'duran', 'carreras', 'pensum', 'tecnologo'], single_response=True)
        response('Puede accader a toda la información sobre nuestro servivio de transporte en https://itla.edu.do/transporte/', ['transporte', 'transportacion', 'guagua', 'llegar', 'ir', 'desplazarme', 'local', 'sede', 'oficinas', 'recinto'], single_response=True)
        response('Para aplicar a nuestras becas de excelencia el estudiante debe ser admitido y cumplir con los requisitos que exige la institución', ['beca', 'becas', 'admision', 'inscripcion', 'financiamiento', 'pago', 'excelencia', 'gratis', 'obtener', 'becado'], single_response=True)
        response('En santiago estamos ubicados AV. 27 de Febrero esq. Metropolitana, Edificio Metropolitano #1, Los Jardines, Santiago', ['ubicados', 'direccion', 'donde', 'ubicacion', 'lugar', 'localizados', 'local', 'sede', 'oficinas', 'santiago'], required_words=['santiago'])
        response('Actualmente nuestro rectos es el Ing. Omar Méndez Lluberes', ['director', 'direccion', 'directora', 'rector', 'rectoria', 'dirigiendo', 'quien', 'lider', 'presidente', 'autoridad'], single_response=True)
        response('Siempre a la orden', ['gracias', 'te lo agradezco', 'thanks'], single_response=True)

        best_match = max(highest_prob, key=highest_prob.get)
        #print(highest_prob)

        return unknown() if highest_prob[best_match] < 1 else best_match

def unknown():
    response = ['puedes decirlo de nuevo?', 'No estoy seguro de lo quieres', 'búscalo en google a ver que tal'][random.randrange(3)]
    return response

while True:
    print("Bot: " + get_response(input('You: ')))