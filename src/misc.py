import random

class Misc:
    @staticmethod
    def loaderx():
        n = random.randint(0,2) 
        loader = ["🔄 Loading... Hold on tight!","⏳ AI is brewing your content potion...","🌟 The AI is working its magic...","🤖 Processing your request... AI at work!",]
        return n,loader

    @staticmethod  
    def ind():
        indx = """
        <style>
        body {
            margin: 0;
            font-family: 'Roboto', sans-serif;
            background-color: #0A043C;
            color: white;
            line-height: 1.6;
        }

        header {
            # background-color: #0A043C;
            background-color: #0E1117;
            padding: 20px 50px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        header h1 {
            color: #00FF85;
            font-size: 28px;
        }

        nav ul {
            list-style: none;
            display: flex;
            gap: 20px;
            margin: 0;
            padding: 0;
        }

        nav ul li a {
            text-decoration: none;
            color: white;
            font-size: 16px;
            transition: color 0.3s;
        }

        nav ul li a:hover {
            color: #00FF85;
        }

        .hero {
            text-align: center;
            padding: 80px 20px;
            background: linear-gradient(180deg, #0A043C, #1C1C3C);
        }

        .hero h2 {
            font-size: 48px;
            margin-bottom: 20px;
        }

        .hero p {
            font-size: 18px;
            max-width: 700px;
            margin: 0 auto 40px;
        }

        .hero button {
            background-color: #00FF85;
            color: #0A043C;
            border: none;
            padding: 15px 30px;
            font-size: 18px;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .hero button:hover {
            background-color: #00E57A;
        }

        .services {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            padding: 40px 50px;
            # background-color: #1C1C3C;
            background-color: #0E1117;
        }

        .service {
            background: linear-gradient(145deg, #292A4D, #3A3A6A);
            padding: 20px;
            border-radius: 15px;
            text-align: center;
            transition: transform 0.3s, box-shadow 0.3s;
            color: white;
            position: relative;
            overflow: hidden;
        }

        .service:hover {
            transform: translateY(-10px);
            box-shadow: 0 10px 20px rgba(0, 0, 0, 0.4);
        }

        .service::before {
            content: '';
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: rgba(255, 255, 255, 0.05);
            transform: skewX(-30deg);
            transition: transform 0.5s;
        }

        .service:hover::before {
            transform: skewX(-30deg) translateX(100%);
        }

        .service h3 {
            font-size: 22px;
            margin-bottom: 15px;
        }

        .service p {
            font-size: 16px;
            margin-bottom: 15px;
        }

        .service img {
            width: 60px;
            height: 60px;
            margin-bottom: 15px;
        }

        .cta {
            text-align: center;
            padding: 40px 20px;
            background-color: #0E1117;
        }

        .cta h2 {
            font-size: 36px;
            margin-bottom: 20px;
        }

        .cta-container {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 20px;
            padding: 20px 0;
        }

        .cta-card {
            background: linear-gradient(145deg, #292A4D, #3A3A6A);
            border-radius: 15px;
            padding: 20px;
            text-align: center;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            transition: transform 0.3s;
        }

        .cta-card:hover {
            transform: translateY(-10px);
            box-shadow: 0 8px 16px rgba(0, 0, 0, 0.4);
        }

        .cta-card img {
            width: 50px;
            height: 50px;
            margin-bottom: 10px;
        }

        .cta-card p {
            font-size: 16px;
        }

        .steps {
            padding: 40px 50px;
            # background-color: #292A4D;
            background-color: #0E1117;
            text-align: center;
        }

        .steps h2 {
            font-size: 36px;
            margin-bottom: 40px;
        }

        .step {
            background-color: #1C1C3C;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 10px;
            font-size: 18px;
            text-align: left;
        }

        .use-cases {
            padding: 40px 50px;
            # background-color: #1C1C3C;
            background-color: #0E1117;
        }

        .use-cases h2 {
            text-align: center;
            font-size: 36px;
            margin-bottom: 20px;
        }

        .case {
            background-color: #292A4D;
            padding: 20px;
            border-radius: 10px;
            margin-bottom: 20px;
        }

        .case h3 {
            font-size: 20px;
            margin-bottom: 10px;
        }

        .contact {
            padding: 40px 50px;
            # background-color: #292A4D;
            background-color: #0E1117;
        }

        .contact h2 {
            text-align: center;
            font-size: 36px;
            margin-bottom: 20px;
        }

        .contact form {
            max-width: 600px;
            margin: 0 auto;
            display: grid;
            gap: 20px;
        }

        .contact input, .contact textarea, .contact button {
            width: 100%;
            padding: 10px;
            border-radius: 5px;
            border: none;
            font-size: 16px;
        }

        .contact button {
            background-color: #00FF85;
            color: #0A043C;
            cursor: pointer;
            transition: background-color 0.3s;
        }

        .contact button:hover {
            background-color: #00E57A;
        }

        footer {
            background-color: #0E1117;
            padding: 20px 50px;
            text-align: center;
            color: #00FF85;
            font-size: 14px;
        }

        footer a {
            color: #00FF85;
            text-decoration: none;
            transition: color 0.3s;
        }

        footer a:hover {
            color: #00E57A;
        }
        .whytool{
            text-align: center;
        }
        </style>

        <h2 class="whytool">Our Services</h2>
        <section class="services">
            <div class="service">
                <img src="https://img.icons8.com/fluency/64/clock.png" alt="Timestamp Icon">
                <h3>Time Stamps Generation</h3>
                <p>Generate accurate timestamps for better video navigation.</p>
            </div>
            <div class="service">
                <img src="https://img.icons8.com/fluency/64/picture.png" alt="Thumbnail Icon">
                <h3>Thumbnail Creation</h3>
                <p>Create visually stunning thumbnails effortlessly.</p>
            </div>
            <div class="service">
                <img src="https://img.icons8.com/fluency/64/idea.png" alt="Theme Detection Icon">
                <h3>Theme Detection</h3>
                <p>Identify themes in videos with AI precision.</p>
            </div>
            <div class="service">
                <img src="https://img.icons8.com/fluency/64/document.png" alt="Summary Icon">
                <h3>Summary Generation</h3>
                <p>Generate concise video summaries quickly.</p>
            </div>
            <div class="service">
                <img src="https://img.icons8.com/fluency/64/language.png" alt="Multilingual Support Icon">
                <h3>Multilingual Support</h3>
                <p>Offer video insights in multiple languages.</p>
            </div>
            <div class="service">
                <img src="https://img.icons8.com/fluency/64/text.png" alt="Transcript Icon">
                <h3>Transcript Generation</h3>
                <p>Generate accurate transcripts seamlessly.</p>
            </div>
        </section>

        <section class="cta">
            <h2>Why Choose Our Tool?</h2>
            <div class="cta-container">
                <div class="cta-card">
                    <img src="https://img.icons8.com/color/48/artificial-intelligence.png" alt="AI Icon">
                    <p>Enhanced efficiency through AI-powered tools.</p>
                </div>
                <div class="cta-card">
                    <img src="https://img.icons8.com/color/48/language.png" alt="Multilingual Support Icon">
                    <p>Comprehensive multilingual support for global reach.</p>
                </div>
                <div class="cta-card">
                    <img src="https://img.icons8.com/color/48/handshake.png" alt="User-Friendly Icon">
                    <p>User-friendly interface designed for seamless navigation.</p>
                </div>
            </div>
        </section>


        <section class="steps">
                <h2>Steps to use our tool</h2>
                <div class="step">
                    <p>01: Get Video URL</p>
                </div>
                <div class="step">
                    <p>02: Paste in the text field & click add button</p>
                </div>
                <div class="step">
                    <p>03: Choose the service</p>
                </div>
                <div class="step">
                    <p>04: Save time</p>
                </div>
        </section>

        <section id="use-cases" class="use-cases">
                <h2>Use Cases</h2>
                <div class="case">
                    <h3>Education</h3>
                    <p>Boost educational video accessibility with time-stamped transcripts and summaries, allowing for better engagement and learning.</p>
                </div>
                <div class="case">
                    <h3>Research</h3>
                    <p>Extract key points and generate focused summaries for productive and streamlined research sessions.</p>
                </div>
                <div class="case">
                    <h3>Marketing</h3>
                    <p>Create engaging thumbnails and insightful captions for marketing success and audience engagement.</p>
                </div>
        </section>

        <section id="contact" class="contact">
                <h2>Contact Us</h2>
                <form>
                    <input type="text" placeholder="Name" required>
                    <input type="email" placeholder="Email" required>
                    <textarea placeholder="Message" rows="5" required></textarea>
                    <button type="submit">Send Message</button>
                </form>
        </section>

        
        </body>

        """

        return indx
            