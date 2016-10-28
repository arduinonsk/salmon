void setup(){
	// инициализируем последовательный порт
	Serial.begin(19200);
}

void loop(){
	// отправляем в порт лосося
	Serial.println("salmon");
}