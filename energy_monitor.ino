/*
  Typing Energy Harvester - Arduino Energy Monitor
  ------------------------------------------------
  Measures the voltage across the storage capacitor through a resistor divider.

  Example divider:
      R1 = 100k from capacitor+ to A0
      R2 = 20k  from A0 to GND

  E = 0.5 * C * V^2

  IMPORTANT:
  - Never connect a raw piezo output directly to A0.
  - Verify your board's ADC range and the actual divider values.
  - This sketch assumes a 5 V Arduino analog reference.
*/

const int VOLTAGE_PIN = A0;

const float ADC_REFERENCE = 5.0;
const float ADC_COUNTS = 1023.0;

const float R1 = 100000.0;   // ohms
const float R2 = 20000.0;    // ohms

const float CAPACITANCE_F = 0.001; // 1000 uF = 0.001 F

unsigned long lastPrint = 0;
const unsigned long SAMPLE_MS = 250;

float readCapVoltage() {
  int raw = analogRead(VOLTAGE_PIN);
  float vPin = (raw * ADC_REFERENCE) / ADC_COUNTS;
  float vCap = vPin * ((R1 + R2) / R2);
  return vCap;
}

float storedEnergyJ(float voltage) {
  return 0.5 * CAPACITANCE_F * voltage * voltage;
}

void setup() {
  Serial.begin(115200);
  delay(500);

  Serial.println("time_ms,voltage_V,energy_J");
}

void loop() {
  unsigned long now = millis();

  if (now - lastPrint >= SAMPLE_MS) {
    lastPrint = now;

    float voltage = readCapVoltage();
    float energy = storedEnergyJ(voltage);

    Serial.print(now);
    Serial.print(",");
    Serial.print(voltage, 4);
    Serial.print(",");
    Serial.println(energy, 8);
  }
}
