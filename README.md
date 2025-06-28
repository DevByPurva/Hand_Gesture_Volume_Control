

<h1>🖐️ Hand Volume Control</h1>

<p>This project is a fun Python application that uses your webcam to detect your hand and control the system volume based on the distance between your thumb and index finger. It uses <code>MediaPipe</code> for hand tracking and <code>PyAutoGUI</code> to press the volume up/down keys.</p>

<h2>✨ Features</h2>
<ul>
    <li>Real-time hand tracking with landmarks</li>
    <li>Visually appealing overlay with circles, lines, and distance bar</li>
    <li>Dynamic volume control: move your fingers apart to increase volume, bring them closer to decrease</li>
    <li>Simple and interactive GUI</li>
</ul>

<h2>⚙️ Requirements</h2>
<p>Before running the script, make sure you have these Python libraries installed:</p>
<pre><code>pip install mediapipe pyautogui opencv-python</code></pre>

<h2>▶️ How to Run</h2>
<ol>
    <li>Clone or download this repository</li>
    <li>Open terminal / PowerShell and navigate to the project directory:
    <pre><code>cd MentorMatch/volume</code></pre></li>
    <li>Run the script:
    <pre><code>python main.py</code></pre></li>
    <li>Allow camera access if prompted</li>
</ol>

<h2>💻 How It Works</h2>
<ul>
    <li>The webcam captures frames in real time</li>
    <li>MediaPipe detects hand landmarks, focusing on your thumb (id 4) and index fingertip (id 8)</li>
    <li>A line is drawn between them, and the distance is calculated</li>
    <li>If the distance is greater than 50px → <span class="highlight">volume up</span></li>
    <li>If the distance is less than or equal to 50px → <span class="highlight">volume down</span></li>
    <li>Visual feedback: colored circles on fingertips, distance bar, and text overlay</li>
</ul>



<h2>📄 License</h2>
<p>This project is for educational purposes. Feel free to modify and improve it!</p>

</body>
</html>
# Hand_Gesture_Volume_Control
