#include <DHT.h>
#include <DS18B20.h>
#include <PicoMQTT.h>
#include <OneWire.h>
#include <HTTPClient.h>
#include <WiFi.h>
#include <time.h>

// Pin definitions
#define DHTPIN 27       // Pin where the DHT sensor is connected
#define DHTTYPE DHT11   // DHT 11
#define ONE_WIRE_BUS 26 // Pin where the DS18B20 is connected

// API URL
#define APIURLPROD "http://13.60.163.212:8002/wheaterdata"
#define APIURLDEV "http://192.168.33.29:8002/wheaterdata"

PicoMQTT::Client mqtt("broker.hivemq.com");

DHT dht(DHTPIN, DHTTYPE);
OneWire oneWire(ONE_WIRE_BUS);
DS18B20 ds18b20(&oneWire);

float temperature = 0;
float humidity = 0;
bool temperatureReceived = false;
bool humidityReceived = false;

// Forward declarations
void handleHumidity(char *topic, void *payload, size_t len);
void handleTemperature(char *topic, void *payload, size_t len);
void sendHttpRequest();

void setup()
{
    Serial.begin(115200);

    // Connect to WiFi
    Serial.printf("Connecting to WiFi %s\n", std::getenv("WIFI_SSID"));
    WiFi.mode(WIFI_STA);
    WiFi.begin(std::getenv("WIFI_SSID"), std::getenv("WIFI_PASSWORD"));
    while (WiFi.status() != WL_CONNECTED)
    {
        delay(1000);
        Serial.print(".");
    }
    Serial.println("WiFi connected.");

    // Initialize sensors
    Serial.println("Initializing sensors...");
    mqtt.begin();
    dht.begin();
    if (!ds18b20.begin())
    {
        Serial.println("Failed to initialize DS18B20 sensor!");
    }
    else
    {
        ds18b20.requestTemperatures();
        Serial.println("DS18B20 sensor initialized.");
    }

    // Subscribe to MQTT topics
    mqtt.subscribe("grasensors/humidity", handleHumidity);
    mqtt.subscribe("grasensors/temperature", handleTemperature);
}

void loop()
{
    mqtt.loop();

    // Get values from the sensors
    int humidityValue = dht.readHumidity();
    float temperatureValue = dht.readTemperature();

    if (humidityValue == 2147483647)
    {
        humidityValue = 0;
    }
    if (temperatureValue == -127 || temperatureValue == 2147483647)
    {
        temperatureValue = 0;
    }

    // Check if the readings are valid
    if (isnan(humidityValue) || isnan(temperatureValue))
    {
        Serial.println("Failed to read from DHT or DS18B20 sensor!");
        ds18b20.requestTemperatures(); // Request new temperature conversion
        delay(2000);                   // Delay before next reading attempt
        return;
    }

    if (temperatureValue > 0)
    {
        mqtt.publish("grasensors/temperature", String(temperatureValue));
        Serial.printf("Temperature: %.2f°C\n", temperatureValue);
    }
    if (humidityValue > 0)
    {
        mqtt.publish("grasensors/humidity", String(humidityValue));
        Serial.printf("Humidity: %d%%\n", humidityValue);
    }

    // Request new temperature conversion for the next loop
    ds18b20.requestTemperatures();

    // Delay before next loop iteration
    delay(1800000);
}

void handleHumidity(char *topic, void *payload, size_t len)
{
    Serial.printf("Humidity Payload: %s\n", (char *)payload);
    humidity = atof((char *)payload);
    humidityReceived = true;

    if (humidityReceived)
    {
        sendHttpRequest();
        humidityReceived = false;
    }
}

void handleTemperature(char *topic, void *payload, size_t len)
{
    Serial.printf("Temperature Payload: %s\n", (char *)payload);
    temperature = atof((char *)payload);
    temperatureReceived = true;

    if (temperatureReceived)
    {
        sendHttpRequest();
        temperatureReceived = false;
    }
}

void sendHttpRequest()
{
    char postPayload[256]; // Increased size to accommodate timestamp
    snprintf(postPayload, sizeof(postPayload),
             "{\"temperature\": %.2f, \"humidity\": %.2f, \"wind_speed\": 0, \"rain_amount\": 0, \"location_id\": 2}",
             temperature, humidity);

    HTTPClient http;
    http.begin(APIURLPROD);
    http.addHeader("Content-Type", "application/json");
    int status = http.POST(postPayload);
    if (status == HTTP_CODE_TEMPORARY_REDIRECT || status == HTTP_CODE_MOVED_PERMANENTLY || status == HTTP_CODE_FOUND)
    {
        String redirectURL = http.getLocation();
        Serial.printf("Redirecting to: %s\n", redirectURL.c_str());
        http.end();
        http.begin(redirectURL);
        status = http.POST(postPayload);
    }
    if (status < 0)
    {
        Serial.printf("HTTP POST failed, error: %s\n", http.errorToString(status).c_str());
    }
    else
    {
        Serial.printf("HTTP Response code: %d\n", status);
    }
    http.end();
}
