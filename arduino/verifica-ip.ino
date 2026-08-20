#include <WiFi.h>

// Preencha com os dados da sua rede antes de gravar no ESP32 — nunca
// suba credenciais reais de Wi-Fi pro repositório.
const char* ssid = "SEU_WIFI_AQUI";
const char* password = "SUA_SENHA_AQUI";

void setup() {

  Serial.begin(115200);

  WiFi.begin(ssid, password);

  Serial.print("Conectando");

  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }

  Serial.println("\nConectado!");

  Serial.print("IP ESP32: ");
  Serial.println(WiFi.localIP());

  Serial.print("Gateway: ");
  Serial.println(WiFi.gatewayIP());

  Serial.print("Subnet: ");
  Serial.println(WiFi.subnetMask());
}

void loop() {
}