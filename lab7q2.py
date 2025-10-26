import RPi.GPIO as GPIO
from flask import Flask, request, render_template_string

GPIO.setmode(GPIO.BCM)
p1, p2, p3 = 17, 27, 22
GPIO.setup(p1, GPIO.OUT)
GPIO.setup(p2, GPIO.OUT)
GPIO.setup(p3, GPIO.OUT)

led_pwms = {
    1: GPIO.PWM(p1, 1000), 
    2: GPIO.PWM(p2, 1000),
    3: GPIO.PWM(p3, 1000)
}

for pwm in led_pwms.values():
    pwm.start(0)

app = Flask(__name__)
brightness_levels = {1: 0, 2: 0, 3: 0}

@app.route('/', methods=['GET', 'POST'])
def control_leds():
    if request.method == 'POST':
        led = int(request.form['led'])
        brightness = int(request.form['brightness'])
        brightness_levels[led] = brightness
        led_pwms[led].ChangeDutyCycle(brightness)
    
    return render_template_string('''
        {% for i in range(1, 4) %}
          <label for="led{{ i }}">LED{{ i }}</label>
          <input type="range" id="led{{ i }}" min="0" max="100" value="{{ brightness_levels[i] }}"
                 oninput="updateBrightness({{ i }}, this.value)">
          <span id="val{{ i }}">{{ brightness_levels[i] }}</span><br><br>
        {% endfor %}

        <script>
          function updateBrightness(led, brightness) {
            document.getElementById("val" + led).innerText = brightness;
            fetch("/", {
              method: "POST",
              headers: { "Content-Type": "application/x-www-form-urlencoded" },
              body: "led=" + led + "&brightness=" + brightness
            });
          }
        </script>
    ''', brightness_levels=brightness_levels)

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    finally:
        for pwm in led_pwms.values():
            pwm.stop()
        GPIO.cleanup()
