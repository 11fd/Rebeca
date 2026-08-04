import streamlit as st

st.set_page_config(
    page_title="Pentru Rebeca ❤️",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ====================== RUBY THEME ======================
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;700;800&family=Outfit:wght@300;400;500;600&display=swap');

    .stApp {
        background: radial-gradient(ellipse at top, #2b0000 0%, #1a0000 40%, #0d0000 100%);
        color: #ffe5e5;
    }

    .stApp::before {
        content: "";
        position: fixed;
        top: 0; left: 0;
        width: 100%; height: 100%;
        background-image: 
            radial-gradient(circle at 20% 30%, rgba(220, 20, 60, 0.15) 0%, transparent 40%),
            radial-gradient(circle at 80% 70%, rgba(139, 0, 0, 0.12) 0%, transparent 40%);
        pointer-events: none;
        z-index: 0;
    }

    h1, h2, h3 {
        font-family: 'Cinzel', serif !important;
        color: #ff2e63 !important;
        text-align: center;
        letter-spacing: 2px;
    }

    .main-title {
        font-size: 3.4rem !important;
        background: linear-gradient(90deg, #ff2e63, #ff6b6b, #c41e3a, #ff2e63);
        background-size: 300% 300%;
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        animation: shine 6s ease infinite;
        text-shadow: 0 0 40px rgba(255, 46, 99, 0.4);
        margin-bottom: 0.2rem;
    }

    @keyframes shine {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }

    .subtitle {
        text-align: center;
        font-size: 1.15rem;
        color: #ff8a9a;
        font-weight: 300;
        letter-spacing: 3px;
        text-transform: uppercase;
        margin-bottom: 1.8rem;
    }

    .reason-card {
        background: linear-gradient(135deg, rgba(80, 0, 20, 0.4), rgba(40, 0, 10, 0.3));
        backdrop-filter: blur(16px);
        border: 1px solid rgba(255, 46, 99, 0.25);
        border-radius: 14px;
        padding: 13px 18px;
        margin-bottom: 9px;
        transition: all 0.35s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        font-size: 0.96rem;
        color: #ffd6dc;
        position: relative;
        overflow: hidden;
    }

    .reason-card::before {
        content: "";
        position: absolute;
        left: 0; top: 0;
        height: 100%; width: 4px;
        background: linear-gradient(to bottom, #ff2e63, #c41e3a);
        opacity: 0;
        transition: opacity 0.3s ease;
    }

    .reason-card:hover {
        background: linear-gradient(135deg, rgba(120, 0, 30, 0.55), rgba(60, 0, 15, 0.4));
        border-color: #ff2e63;
        transform: translateX(10px) scale(1.02);
        box-shadow: 0 10px 30px rgba(255, 46, 99, 0.25);
    }

    .reason-card:hover::before {
        opacity: 1;
    }

    .glass-card {
        background: linear-gradient(145deg, rgba(90, 0, 25, 0.45), rgba(30, 0, 10, 0.35));
        backdrop-filter: blur(20px);
        border: 1px solid rgba(255, 46, 99, 0.35);
        border-radius: 28px;
        padding: 2.2rem;
        box-shadow: 0 25px 50px rgba(0, 0, 0, 0.5), inset 0 1px 0 rgba(255, 255, 255, 0.08);
        text-align: center;
        animation: cardReveal 1s cubic-bezier(0.175, 0.885, 0.32, 1.275) forwards;
    }

    @keyframes cardReveal {
        0% { opacity: 0; transform: scale(0.7) translateY(40px); filter: blur(8px); }
        100% { opacity: 1; transform: scale(1) translateY(0); filter: blur(0); }
    }

    .message {
        font-size: 1.18rem;
        color: #ffb3c1;
        margin: 0.75rem 0;
        font-weight: 400;
        line-height: 1.5;
    }

    .apology-box {
        background: rgba(255, 46, 99, 0.12);
        border: 1px solid rgba(255, 46, 99, 0.35);
        border-radius: 18px;
        padding: 1.4rem 1.6rem;
        margin: 1.5rem 0;
        text-align: left;
        line-height: 1.7;
        color: #ffc1d0;
        font-size: 1.05rem;
    }

    .stButton > button {
        background: linear-gradient(90deg, #c41e3a, #ff2e63, #ff4d6d) !important;
        color: white !important;
        border: none !important;
        border-radius: 60px !important;
        padding: 0.9rem 2.2rem !important;
        font-weight: 600 !important;
        font-size: 1.15rem !important;
        letter-spacing: 1px !important;
        transition: all 0.35s ease !important;
        box-shadow: 0 10px 30px rgba(255, 46, 99, 0.45) !important;
        text-transform: uppercase;
    }

    .stButton > button:hover {
        transform: scale(1.06) translateY(-3px) !important;
        box-shadow: 0 18px 40px rgba(255, 46, 99, 0.65) !important;
    }

    .music-box {
        background: linear-gradient(145deg, rgba(80, 0, 20, 0.5), rgba(30, 0, 10, 0.4));
        border-radius: 22px;
        padding: 1.4rem;
        border: 1px solid rgba(255, 46, 99, 0.35);
        margin-bottom: 1.8rem;
        text-align: center;
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    }

    .love-text {
        font-family: 'Cinzel', serif;
        font-size: 2.6rem;
        background: linear-gradient(90deg, #ff2e63, #ff8a9a, #ff2e63);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center;
        margin: 1rem 0 0.5rem 0;
        letter-spacing: 3px;
        animation: textPop 0.8s ease forwards;
    }

    @keyframes textPop {
        0% { opacity: 0; transform: scale(0.5); }
        70% { transform: scale(1.1); }
        100% { opacity: 1; transform: scale(1); }
    }

    .footer {
        text-align: center;
        color: #ff2e63;
        font-size: 0.95rem;
        margin-top: 2.5rem;
        letter-spacing: 2px;
        opacity: 0.9;
    }

    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    ::-webkit-scrollbar { width: 8px; }
    ::-webkit-scrollbar-track { background: #1a0000; }
    ::-webkit-scrollbar-thumb {
        background: linear-gradient(#c41e3a, #ff2e63);
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)

# ====================== LAYOUT ======================
col_left, col_right = st.columns([1.15, 1.4], gap="large")

# ========== STÂNGA - 100 DE MOTIVE ==========
with col_left:
    st.markdown("## ❤️ 100 de motive de ce te iubesc")
    st.markdown("<p style='text-align:center; color:#ff8a9a; font-size:0.95rem; margin-bottom:1.2rem; letter-spacing:1px;'>Derulează și citește-le pe toate...</p>", unsafe_allow_html=True)

    motive = [
        "1. Pentru zâmbetul tău care luminează orice cameră",
        "2. Pentru modul blând în care vorbești",
        "3. Pentru ochii tăi care spun povești întregi",
        "4. Pentru că mă faci să râd chiar și în zilele grele",
        "5. Pentru blândețea sufletului tău",
        "6. Pentru forța ta interioară",
        "7. Pentru felul în care asculți cu adevărat",
        "8. Pentru sinceritatea ta",
        "9. Pentru pasiunea cu care faci lucrurile",
        "10. Pentru că ești complet unică",
        "11. Pentru râsul tău molipsitor",
        "12. Pentru modul în care îmi spui pe nume",
        "13. Pentru că mă inspiri să fiu mai bun",
        "14. Pentru energia ta pozitivă",
        "15. Pentru frumusețea ta interioară și exterioară",
        "16. Pentru inteligența ta ascuțită",
        "17. Pentru creativitatea ta",
        "18. Pentru loialitatea ta",
        "19. Pentru felul profund în care iubești",
        "20. Pentru că mă faci să mă simt special",
        "21. Pentru răbdarea ta infinită",
        "22. Pentru curajul tău",
        "23. Pentru vocea ta caldă",
        "24. Pentru empatia ta",
        "25. Pentru spiritul tău liber",
        "26. Pentru simțul tău al umorului",
        "27. Pentru eleganța ta naturală",
        "28. Pentru autenticitatea ta",
        "29. Pentru modul în care dansezi prin viață",
        "30. Pentru liniștea pe care mi-o oferi",
        "31. Pentru dorința ta de a evolua",
        "32. Pentru puterea ta",
        "33. Pentru blândețea din privirea ta",
        "34. Pentru că mă înțelegi fără prea multe cuvinte",
        "35. Pentru optimismul tău",
        "36. Pentru generozitatea ta",
        "37. Pentru modul în care îți exprimi sentimentele",
        "38. Pentru misterul frumos din tine",
        "39. Pentru că mă faci să vreau să devin mai bun",
        "40. Pentru că ești exact așa cum ești",
        "41. Pentru pacea pe care mi-o aduci",
        "42. Pentru pasiunea ta",
        "43. Pentru sufletul tău frumos",
        "44. Pentru curajul de a fi vulnerabilă",
        "45. Pentru că ești delicată și puternică în același timp",
        "46. Pentru că îmi place totul la tine",
        "47. Pentru că ești inspiratoare",
        "48. Pentru că ești reală",
        "49. Pentru că ești magică",
        "50. Pentru că ești casa mea",
        "51. Pentru că ești visele mele",
        "52. Pentru că ești motivul pentru care zâmbesc",
        "53. Pentru că ești cea mai frumoasă surpriză",
        "54. Pentru că ești lumina mea",
        "55. Pentru că ești pacea mea",
        "56. Pentru că ești aventura mea preferată",
        "57. Pentru că ești cea mai bună parte a zilei mele",
        "58. Pentru că ești motivul pentru care mai cred în iubire",
        "59. Pentru că ești perfect imperfectă",
        "60. Pentru că ești tot ce am visat",
        "61. Pentru că ești inima mea",
        "62. Pentru că ești gândul meu favorit",
        "63. Pentru că ești cea mai frumoasă poveste",
        "64. Pentru că ești inspirația mea zilnică",
        "65. Pentru că ești cea mai dulce persoană pe care o cunosc",
        "66. Pentru că ești tot ce am nevoie",
        "67. Pentru că ești zâmbetul meu preferat",
        "68. Pentru că ești cea mai frumoasă întâmplare",
        "69. Pentru că ești sufletul meu pereche",
        "70. Pentru că ești cea mai valoroasă comoară",
        "71. Pentru că ești motivul pentru care am fluturi în stomac",
        "72. Pentru că ești cea mai frumoasă emoție",
        "73. Pentru că ești tot ce e bun în lumea mea",
        "74. Pentru că ești cea mai frumoasă melodie",
        "75. Pentru că ești cea mai frumoasă culoare",
        "76. Pentru că ești cea mai frumoasă amintire în devenire",
        "77. Pentru că ești cea mai frumoasă zi de mâine",
        "78. Pentru că ești cea mai frumoasă alegere pe care am făcut-o",
        "79. Pentru că ești cea mai frumoasă certitudine",
        "80. Pentru că ești cea mai frumoasă întrebare și răspuns",
        "81. Pentru că ești cea mai frumoasă liniște",
        "82. Pentru că ești cea mai frumoasă furtună",
        "83. Pentru că ești cea mai frumoasă casă",
        "84. Pentru că ești cea mai frumoasă călătorie",
        "85. Pentru că ești cea mai frumoasă destinație",
        "86. Pentru că ești cea mai frumoasă surpriză a vieții mele",
        "87. Pentru că ești cea mai frumoasă dovadă că magia există",
        "88. Pentru că ești cea mai frumoasă versiune a iubirii",
        "89. Pentru că ești cea mai frumoasă parte din mine",
        "90. Pentru că ești cea mai frumoasă persoană pe care o cunosc",
        "91. Pentru că ești cea mai frumoasă întâmplare care mi s-a întâmplat",
        "92. Pentru că ești cea mai frumoasă motivație",
        "93. Pentru că ești cel mai frumos peisaj",
        "94. Pentru că ești cea mai frumoasă seară",
        "95. Pentru că ești cea mai frumoasă dimineață",
        "96. Pentru că ești cea mai frumoasă clipă",
        "97. Pentru că ești cea mai frumoasă veșnicie",
        "98. Pentru că ești cea mai frumoasă poveste de spus",
        "99. Pentru că ești cea mai frumoasă inimă",
        "100. Pentru că te iubesc. Simplu. Complet. Pentru totdeauna. ❤️"
    ]

    for motiv in motive:
        st.markdown(f'<div class="reason-card">{motiv}</div>', unsafe_allow_html=True)

# ========== DREAPTA ==========
with col_right:
    st.markdown('<h1 class="main-title">Happy Birthday, Rebeca</h1>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">O zi la fel de rară precum un rubin</p>', unsafe_allow_html=True)

    # Melodie SoundCloud
    st.markdown('<div class="music-box">', unsafe_allow_html=True)
    st.markdown("### 🎵 Melodia noastră")
    
    st.components.v1.html("""
        <iframe width="100%" height="120" scrolling="no" frameborder="no" allow="autoplay"
            src="https://w.soundcloud.com/player/?url=https%3A//soundcloud.com/alex-coretes/pupsies-misery-slowed&color=%23ff2e63&auto_play=true&hide_related=false&show_comments=false&show_user=true&show_reposts=false&show_teaser=false&visual=false">
        </iframe>
    """, height=130)
    st.markdown('</div>', unsafe_allow_html=True)

    # Buton surpriză
    if st.button("✨ Deschide surpriza mea pentru tine ✨", use_container_width=True):
        
        # Animație
        st.components.v1.html("""
        <div id="animation-container" style="position:fixed; top:0; left:0; width:100%; height:100%; pointer-events:none; z-index:9999; overflow:hidden;"></div>
        <script>
            const container = document.getElementById('animation-container');
            const symbols = ['❤️', '💕', '💗', '💖', '✨', '🌸', '💞', '💓'];
            for (let i = 0; i < 60; i++) {
                const el = document.createElement('div');
                el.innerHTML = symbols[Math.floor(Math.random() * symbols.length)];
                el.style.position = 'absolute';
                el.style.left = Math.random() * 100 + 'vw';
                el.style.top = '110vh';
                el.style.fontSize = (Math.random() * 28 + 14) + 'px';
                el.style.opacity = '0';
                el.style.animation = `fly ${3 + Math.random() * 4}s ease-out forwards`;
                el.style.animationDelay = (Math.random() * 0.8) + 's';
                container.appendChild(el);
            }
            const style = document.createElement('style');
            style.innerHTML = `
                @keyframes fly {
                    0% { transform: translateY(0) scale(0.3) rotate(0deg); opacity: 0; }
                    10% { opacity: 1; }
                    100% { transform: translateY(-120vh) scale(1.2) rotate(360deg); opacity: 0; }
                }
            `;
            document.head.appendChild(style);
            setTimeout(() => { container.remove(); }, 7000);
        </script>
        """, height=0)

        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        
        st.markdown('<div class="love-text">I love you Rebeca</div>', unsafe_allow_html=True)
        
        # GIF Hello Kitty
        st.markdown("""
        <div style="display: flex; justify-content: center; margin: 1.2rem 0;">
            <img src="https://media3.giphy.com/media/v1.Y2lkPTZjMDliOTUycngwdWRiN3Jocm9uMHJqY3pieHZtODR4cTg1a3ZpOGU0ZXZqYTQ4cyZlcD12MV9naWZzX3NlYXJjaCZjdD1n/kZqbBT64ECtjy/200w.gif" 
                 alt="Hello Kitty" 
                 style="width: 270px; border-radius: 22px; box-shadow: 0 12px 35px rgba(255,46,99,0.5);">
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("### ❤️ La mulți ani, iubirea mea!")
        
        messages = [
            "Astăzi universul sărbătorește existența ta.",
            "Să ai parte de zâmbete adevărate, de liniște și de momente care îți umplu sufletul.",
            "Să-ți împlinești toate visele frumoase în acest nou an de viață.",
            "Ești cea mai prețioasă persoană și meriți absolut tot ce e mai bun.",
            "Să fii sănătoasă, iubită și mereu înconjurată de lumină.",
            "Te iubesc mai mult cu fiecare răsărit."
        ]
        
        for msg in messages:
            st.markdown(f'<p class="message">❤️ {msg}</p>', unsafe_allow_html=True)

        # ========== MESAJ DE ÎMPĂCARE ==========
        st.markdown("""
        <div class="apology-box">
            <b>Rebeca,</b><br><br>
            Știu că am greșit și că te-am rănit.<br>
            Nu există nicio scuză care să șteargă ce s-a întâmplat, dar vreau să știi că îmi pare sincer rău.<br><br>
            Te iubesc în continuare.<br>
            Îmi lipsesc zâmbetul tău, vocea ta și pur și simplu prezența ta.<br>
            Vreau să fiu din nou alături de tine, dacă mai există vreo șansă.<br><br>
            Dacă ești dispusă să vorbim, sunt aici.<br><br>
            <b>Cu toată inima</b>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        st.markdown("##### La mulți ani, Rebeca ❤️")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    st.markdown("""
    <div class="glass-card" style="text-align:center; margin-top:1rem;">
        <p style="font-size:1.2rem; color:#ffb3c1; margin:0; line-height:1.6;">
            Ești motivul pentru care inima mea a învățat să bată diferit.<br>
            Mulțumesc că exiști.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<p class="footer">MADE WITH ENDLESS LOVE FOR REBECA ❤️</p>', unsafe_allow_html=True)
