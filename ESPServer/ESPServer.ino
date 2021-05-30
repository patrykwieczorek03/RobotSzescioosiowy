#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

IPAddress local_IP(192, 168, 1, 151);
IPAddress gateway(192, 168, 1, 1);
IPAddress subnet(255, 255, 255, 0);

char* ssid = "Livebox-323C";
char* password = "016A11732A736F9067FF6F72FC";
WiFiServer server(80);

// Variable to store the HTTP request
String header;

// Current time
unsigned long currentTime = millis();
// Previous time
unsigned long previousTime = 0; 
// Define timeout time in milliseconds (example: 2000ms = 2s)
const long timeoutTime = 2000;

const int output1 = 16;
const int output2 = 5;
const int output3 = 4;
const int output4 = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(output1, OUTPUT);
  pinMode(output2, OUTPUT);
  pinMode(output3, OUTPUT);
  pinMode(output4, OUTPUT);

  digitalWrite(output1, LOW);
  digitalWrite(output2, LOW);
  digitalWrite(output3, LOW);
  digitalWrite(output4, LOW);

  Serial.begin(115200);

  // Connect to Wi-Fi network with SSID and password
  Serial.print("Connecting to ");
  Serial.println(ssid);

   if(!WiFi.config(local_IP, gateway, subnet))
 {
    Serial.println("STA failed to configure.");
  }
  
  WiFi.begin(ssid, password);
  while (WiFi.status() != WL_CONNECTED) {
    delay(500);
    Serial.print(".");
  }
  // Print local IP address and start web server
  Serial.println("");
  Serial.println("WiFi connected.");
  Serial.println("IP address: ");
  Serial.println(WiFi.localIP());
  server.begin();

}

void loop() {
  WiFiClient client = server.available();   // Listen for incoming clients

  if (client) {                             // If a new client connects,
    Serial.println("New Client.");          // print a message out in the serial port
    String currentLine = "";                // make a String to hold incoming data from the client
    currentTime = millis();
    previousTime = currentTime;
    while (client.connected() && currentTime - previousTime <= timeoutTime) { // loop while the client's connected
      currentTime = millis();         
      if (client.available()) {             // if there's bytes to read from the client,
        char c = client.read();             // read a byte, then
        Serial.write(c); 
        Serial.println("\n");
        header += c;
        if(c == '0')
        {
          digitalWrite(output1, HIGH);
          digitalWrite(output2, LOW);
          digitalWrite(output3, LOW);
          digitalWrite(output4, LOW);
          delay(1000);
          digitalWrite(output1, LOW);
        } else if(c == '1')
        {
          digitalWrite(output1, LOW);
          digitalWrite(output2, HIGH);
          digitalWrite(output3, LOW);
          digitalWrite(output4, LOW);
          delay(1000);
          digitalWrite(output2, LOW);
        } else if(c == '2')
        {
          digitalWrite(output1, LOW);
          digitalWrite(output2, LOW);
          digitalWrite(output3, HIGH);
          digitalWrite(output4, LOW);
          delay(1000);
          digitalWrite(output3, LOW);
        } else if(c == '3')
        {
          digitalWrite(output1, LOW);
          digitalWrite(output2, LOW);
          digitalWrite(output3, LOW);
          digitalWrite(output4, HIGH);
          delay(1000);
          digitalWrite(output4, LOW);
        }
      }
    }
    // Clear the header variable
    header = "";
    // Close the connection
    client.stop();
    Serial.println("Client disconnected.");
    Serial.println("");
  }
}
