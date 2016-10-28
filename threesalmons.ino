void setup(){
	// инициализируем последовательный порт
	Serial.begin(19200);
}

void loop(){
	// отправляем в порт три лосося
	Serial.println("salmonsalmonsalmon");
}