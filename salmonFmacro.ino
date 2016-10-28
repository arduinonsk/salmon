void setup(){
	// инициализируем последовательный порт
	Serial.begin(19200);
}

void loop(){
	// отправляем в порт три лосося
	// только теперь лососи лежат во FLASH
	// и не занимают RAM
	Serial.println(F("salmonsalmonsalmon"));
}