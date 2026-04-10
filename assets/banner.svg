<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 280" width="900" height="280">
  <defs>
    <!-- Background gradient -->
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#050d1a"/>
      <stop offset="50%" style="stop-color:#0a1628"/>
      <stop offset="100%" style="stop-color:#0d0d1f"/>
    </linearGradient>

    <!-- Cyan glow gradient -->
    <radialGradient id="glowCenter" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#00b4d8;stop-opacity:0.15"/>
      <stop offset="100%" style="stop-color:#00b4d8;stop-opacity:0"/>
    </radialGradient>

    <!-- Robot body gradient -->
    <linearGradient id="robotBody" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1a2a3a"/>
      <stop offset="100%" style="stop-color:#0d1520"/>
    </linearGradient>

    <!-- Robot head gradient -->
    <linearGradient id="robotHead" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" style="stop-color:#1e3448"/>
      <stop offset="100%" style="stop-color:#0d1e2e"/>
    </linearGradient>

    <!-- Eye glow -->
    <radialGradient id="eyeGlow" cx="50%" cy="50%" r="50%">
      <stop offset="0%" style="stop-color:#00f5ff"/>
      <stop offset="60%" style="stop-color:#00b4d8"/>
      <stop offset="100%" style="stop-color:#004466;stop-opacity:0"/>
    </radialGradient>

    <!-- Brain circuit gradient -->
    <linearGradient id="circuitGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#00b4d8;stop-opacity:0"/>
      <stop offset="50%" style="stop-color:#00b4d8"/>
      <stop offset="100%" style="stop-color:#00b4d8;stop-opacity:0"/>
    </linearGradient>

    <!-- Title text gradient -->
    <linearGradient id="titleGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" style="stop-color:#ffffff"/>
      <stop offset="50%" style="stop-color:#00e5ff"/>
      <stop offset="100%" style="stop-color:#ffffff"/>
    </linearGradient>

    <!-- Filter: cyan glow -->
    <filter id="cyanGlow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <!-- Filter: strong glow -->
    <filter id="strongGlow" x="-100%" y="-100%" width="300%" height="300%">
      <feGaussianBlur stdDeviation="6" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <!-- Filter: soft glow -->
    <filter id="softGlow" x="-30%" y="-30%" width="160%" height="160%">
      <feGaussianBlur stdDeviation="2" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>

    <!-- Clip for robot screen -->
    <clipPath id="screenClip">
      <rect x="72" y="105" width="46" height="28" rx="3"/>
    </clipPath>
  </defs>

  <!-- ═══════════════════════════════════════ -->
  <!--  BACKGROUND                            -->
  <!-- ═══════════════════════════════════════ -->
  <rect width="900" height="280" fill="url(#bgGrad)"/>

  <!-- Ambient center glow -->
  <ellipse cx="450" cy="140" rx="350" ry="180" fill="url(#glowCenter)"/>

  <!-- ═══════════════════════════════════════ -->
  <!--  ANIMATED GRID FLOOR                   -->
  <!-- ═══════════════════════════════════════ -->
  <g opacity="0.25">
    <!-- Horizontal grid lines (perspective) -->
    <line x1="0" y1="230" x2="900" y2="230" stroke="#00b4d8" stroke-width="0.5"/>
    <line x1="50" y1="215" x2="850" y2="215" stroke="#00b4d8" stroke-width="0.4"/>
    <line x1="100" y1="200" x2="800" y2="200" stroke="#00b4d8" stroke-width="0.3"/>
    <line x1="140" y1="188" x2="760" y2="188" stroke="#00b4d8" stroke-width="0.25"/>
    <line x1="175" y1="178" x2="725" y2="178" stroke="#00b4d8" stroke-width="0.2"/>
    <!-- Vertical perspective lines -->
    <line x1="450" y1="170" x2="0" y2="280" stroke="#00b4d8" stroke-width="0.4"/>
    <line x1="450" y1="170" x2="150" y2="280" stroke="#00b4d8" stroke-width="0.3"/>
    <line x1="450" y1="170" x2="300" y2="280" stroke="#00b4d8" stroke-width="0.25"/>
    <line x1="450" y1="170" x2="450" y2="280" stroke="#00b4d8" stroke-width="0.4"/>
    <line x1="450" y1="170" x2="600" y2="280" stroke="#00b4d8" stroke-width="0.25"/>
    <line x1="450" y1="170" x2="750" y2="280" stroke="#00b4d8" stroke-width="0.3"/>
    <line x1="450" y1="170" x2="900" y2="280" stroke="#00b4d8" stroke-width="0.4"/>
  </g>

  <!-- Grid scan line animation -->
  <rect x="0" y="170" width="900" height="2" fill="#00b4d8" opacity="0.15">
    <animate attributeName="y" from="170" to="280" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0;0.3;0" dur="3s" repeatCount="indefinite"/>
  </rect>

  <!-- ═══════════════════════════════════════ -->
  <!--  FLOATING CIRCUIT PARTICLES (left)     -->
  <!-- ═══════════════════════════════════════ -->
  <!-- Particle 1 -->
  <circle cx="180" cy="80" r="2" fill="#00b4d8" filter="url(#softGlow)">
    <animate attributeName="cy" values="80;60;80" dur="4s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.8;0.2;0.8" dur="4s" repeatCount="indefinite"/>
  </circle>
  <!-- Particle 2 -->
  <circle cx="150" cy="140" r="1.5" fill="#00d4a8" filter="url(#softGlow)">
    <animate attributeName="cy" values="140;120;140" dur="5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.6;0.1;0.6" dur="5s" repeatCount="indefinite"/>
  </circle>
  <!-- Particle 3 -->
  <circle cx="200" cy="160" r="2.5" fill="#00b4d8" filter="url(#softGlow)">
    <animate attributeName="cy" values="160;135;160" dur="3.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="1;0.3;1" dur="3.5s" repeatCount="indefinite"/>
  </circle>
  <!-- Particle 4 (right side) -->
  <circle cx="720" cy="90" r="2" fill="#00b4d8" filter="url(#softGlow)">
    <animate attributeName="cy" values="90;70;90" dur="4.5s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.7;0.2;0.7" dur="4.5s" repeatCount="indefinite"/>
  </circle>
  <!-- Particle 5 -->
  <circle cx="760" cy="150" r="1.5" fill="#00f5ff" filter="url(#softGlow)">
    <animate attributeName="cy" values="150;130;150" dur="3.8s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.9;0.2;0.9" dur="3.8s" repeatCount="indefinite"/>
  </circle>
  <!-- Particle 6 -->
  <circle cx="740" cy="60" r="3" fill="#00d4a8" filter="url(#softGlow)">
    <animate attributeName="cy" values="60;40;60" dur="6s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.5;0.1;0.5" dur="6s" repeatCount="indefinite"/>
  </circle>

  <!-- ═══════════════════════════════════════ -->
  <!--  FLOATING DATA NODES                   -->
  <!-- ═══════════════════════════════════════ -->
  <!-- Left data node -->
  <g filter="url(#softGlow)">
    <rect x="40" y="55" width="90" height="40" rx="5" fill="#0a1e30" stroke="#00b4d8" stroke-width="0.8" opacity="0.9">
      <animate attributeName="y" values="55;48;55" dur="5s" repeatCount="indefinite"/>
    </rect>
    <text x="85" y="71" font-family="'Courier New',monospace" font-size="8" fill="#00b4d8" text-anchor="middle" opacity="0.9">
      <animate attributeName="y" values="71;64;71" dur="5s" repeatCount="indefinite"/>
      DROPOUT RISK
    </text>
    <text x="85" y="85" font-family="'Courier New',monospace" font-size="11" font-weight="bold" fill="#ff3b3b" text-anchor="middle">
      <animate attributeName="y" values="85;78;85" dur="5s" repeatCount="indefinite"/>
      87.3%
    </text>
  </g>

  <!-- Right data node -->
  <g filter="url(#softGlow)">
    <rect x="770" y="45" width="90" height="40" rx="5" fill="#0a1e30" stroke="#00d4a8" stroke-width="0.8" opacity="0.9">
      <animate attributeName="y" values="45;38;45" dur="4.5s" repeatCount="indefinite"/>
    </rect>
    <text x="815" y="61" font-family="'Courier New',monospace" font-size="8" fill="#00d4a8" text-anchor="middle" opacity="0.9">
      <animate attributeName="y" values="61;54;61" dur="4.5s" repeatCount="indefinite"/>
      ACCURACY
    </text>
    <text x="815" y="75" font-family="'Courier New',monospace" font-size="11" font-weight="bold" fill="#00f5ff" text-anchor="middle">
      <animate attributeName="y" values="75;68;75" dur="4.5s" repeatCount="indefinite"/>
      94.1%
    </text>
  </g>

  <!-- Bottom left data node -->
  <g filter="url(#softGlow)">
    <rect x="30" y="160" width="100" height="36" rx="5" fill="#0a1e30" stroke="#ffb703" stroke-width="0.8" opacity="0.85">
      <animate attributeName="y" values="160;154;160" dur="6s" repeatCount="indefinite"/>
    </rect>
    <text x="80" y="174" font-family="'Courier New',monospace" font-size="7.5" fill="#ffb703" text-anchor="middle">
      <animate attributeName="y" values="174;168;174" dur="6s" repeatCount="indefinite"/>
      SHAP SCORE
    </text>
    <text x="80" y="188" font-family="'Courier New',monospace" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">
      <animate attributeName="y" values="188;182;188" dur="6s" repeatCount="indefinite"/>
      +0.421
    </text>
  </g>

  <!-- Bottom right data node -->
  <g filter="url(#softGlow)">
    <rect x="770" y="155" width="100" height="36" rx="5" fill="#0a1e30" stroke="#6c5ce7" stroke-width="0.8" opacity="0.85">
      <animate attributeName="y" values="155;149;155" dur="5.5s" repeatCount="indefinite"/>
    </rect>
    <text x="820" y="169" font-family="'Courier New',monospace" font-size="7.5" fill="#a29bfe" text-anchor="middle">
      <animate attributeName="y" values="169;163;169" dur="5.5s" repeatCount="indefinite"/>
      PATIENTS
    </text>
    <text x="820" y="183" font-family="'Courier New',monospace" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">
      <animate attributeName="y" values="183;177;183" dur="5.5s" repeatCount="indefinite"/>
      400
    </text>
  </g>

  <!-- ═══════════════════════════════════════ -->
  <!--  ROBOT — body                          -->
  <!-- ═══════════════════════════════════════ -->
  <g transform="translate(426, 28)">
    <!-- Floating animation on whole robot -->
    <animateTransform attributeName="transform" type="translate"
      values="426,28; 426,20; 426,28" dur="4s" repeatCount="indefinite"/>

    <!-- Shadow below robot -->
    <ellipse cx="24" cy="202" rx="28" ry="6" fill="#00b4d8" opacity="0.12">
      <animate attributeName="rx" values="28;22;28" dur="4s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.12;0.06;0.12" dur="4s" repeatCount="indefinite"/>
    </ellipse>

    <!-- Legs -->
    <rect x="9" y="172" width="12" height="26" rx="4" fill="url(#robotBody)" stroke="#1a3a50" stroke-width="1"/>
    <rect x="27" y="172" width="12" height="26" rx="4" fill="url(#robotBody)" stroke="#1a3a50" stroke-width="1"/>
    <!-- Feet -->
    <rect x="6" y="194" width="16" height="8" rx="3" fill="#0d1e30" stroke="#00b4d8" stroke-width="0.6"/>
    <rect x="26" y="194" width="16" height="8" rx="3" fill="#0d1e30" stroke="#00b4d8" stroke-width="0.6"/>

    <!-- Torso -->
    <rect x="4" y="108" width="40" height="68" rx="6" fill="url(#robotBody)" stroke="#1e3a52" stroke-width="1.2"/>

    <!-- Chest panel / screen -->
    <rect x="10" y="118" width="28" height="38" rx="3" fill="#060f1a" stroke="#00b4d8" stroke-width="0.8"/>
    <!-- Chest screen scanline -->
    <rect x="10" y="118" width="28" height="3" fill="#00b4d8" opacity="0.4">
      <animate attributeName="y" values="118;153;118" dur="2s" repeatCount="indefinite"/>
    </rect>
    <!-- Chest data lines -->
    <line x1="13" y1="126" x2="35" y2="126" stroke="#00b4d8" stroke-width="0.6" opacity="0.5"/>
    <line x1="13" y1="131" x2="30" y2="131" stroke="#00b4d8" stroke-width="0.6" opacity="0.5"/>
    <line x1="13" y1="136" x2="33" y2="136" stroke="#00b4d8" stroke-width="0.6" opacity="0.5"/>
    <line x1="13" y1="141" x2="28" y2="141" stroke="#00b4d8" stroke-width="0.6" opacity="0.5"/>
    <!-- Chest pulsing dot -->
    <circle cx="24" cy="150" r="3" fill="#ff3b3b" filter="url(#softGlow)">
      <animate attributeName="r" values="3;5;3" dur="1.2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="1;0.4;1" dur="1.2s" repeatCount="indefinite"/>
    </circle>

    <!-- Shoulder joints -->
    <circle cx="3" cy="118" r="5" fill="#0d1e30" stroke="#00b4d8" stroke-width="1"/>
    <circle cx="45" cy="118" r="5" fill="#0d1e30" stroke="#00b4d8" stroke-width="1"/>

    <!-- Left arm -->
    <rect x="-14" y="112" width="10" height="44" rx="4" fill="url(#robotBody)" stroke="#1a3a50" stroke-width="1">
      <animateTransform attributeName="transform" type="rotate"
        values="0,-4,134; 8,-4,134; 0,-4,134" dur="4s" repeatCount="indefinite"/>
    </rect>
    <!-- Left hand -->
    <circle cx="-9" cy="160" r="5" fill="#0d1e30" stroke="#00b4d8" stroke-width="0.8">
      <animateTransform attributeName="transform" type="rotate"
        values="0,-9,160; 8,-9,160; 0,-9,160" dur="4s" repeatCount="indefinite"/>
    </circle>

    <!-- Right arm -->
    <rect x="52" y="112" width="10" height="44" rx="4" fill="url(#robotBody)" stroke="#1a3a50" stroke-width="1">
      <animateTransform attributeName="transform" type="rotate"
        values="0,57,134; -8,57,134; 0,57,134" dur="4s" repeatCount="indefinite"/>
    </rect>
    <!-- Right hand -->
    <circle cx="57" cy="160" r="5" fill="#0d1e30" stroke="#00b4d8" stroke-width="0.8">
      <animateTransform attributeName="transform" type="rotate"
        values="0,57,160; -8,57,160; 0,57,160" dur="4s" repeatCount="indefinite"/>
    </circle>

    <!-- Neck -->
    <rect x="17" y="96" width="14" height="14" rx="3" fill="#0d1e30" stroke="#1a3a50" stroke-width="1"/>
    <!-- Neck bolts -->
    <circle cx="19" cy="100" r="1.5" fill="#00b4d8" opacity="0.7"/>
    <circle cx="29" cy="100" r="1.5" fill="#00b4d8" opacity="0.7"/>

    <!-- HEAD -->
    <rect x="2" y="44" width="44" height="54" rx="8" fill="url(#robotHead)" stroke="#00b4d8" stroke-width="1.5" filter="url(#softGlow)"/>

    <!-- Antenna -->
    <line x1="24" y1="44" x2="24" y2="22" stroke="#00b4d8" stroke-width="1.5"/>
    <circle cx="24" cy="18" r="5" fill="#060f1a" stroke="#00b4d8" stroke-width="1.2" filter="url(#strongGlow)">
      <animate attributeName="fill" values="#060f1a;#00b4d8;#060f1a" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="r" values="5;7;5" dur="2s" repeatCount="indefinite"/>
    </circle>
    <!-- Antenna signal rings -->
    <circle cx="24" cy="18" r="9" fill="none" stroke="#00b4d8" stroke-width="0.5">
      <animate attributeName="r" values="5;14;5" dur="2s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.8;0;0.8" dur="2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="24" cy="18" r="9" fill="none" stroke="#00b4d8" stroke-width="0.3">
      <animate attributeName="r" values="5;20;5" dur="2s" begin="0.3s" repeatCount="indefinite"/>
      <animate attributeName="opacity" values="0.5;0;0.5" dur="2s" begin="0.3s" repeatCount="indefinite"/>
    </circle>

    <!-- EYES -->
    <!-- Left eye socket -->
    <ellipse cx="13" cy="64" rx="7" ry="7" fill="#060a12" stroke="#00b4d8" stroke-width="0.8"/>
    <!-- Left eye glow -->
    <ellipse cx="13" cy="64" rx="5" ry="5" fill="url(#eyeGlow)" filter="url(#strongGlow)">
      <animate attributeName="rx" values="5;6;5" dur="1.8s" repeatCount="indefinite"/>
      <animate attributeName="ry" values="5;6;5" dur="1.8s" repeatCount="indefinite"/>
    </ellipse>
    <!-- Left pupil -->
    <circle cx="13" cy="64" r="2.5" fill="#00f5ff">
      <animate attributeName="cx" values="13;14;13;12;13" dur="4s" repeatCount="indefinite"/>
    </circle>

    <!-- Right eye socket -->
    <ellipse cx="35" cy="64" rx="7" ry="7" fill="#060a12" stroke="#00b4d8" stroke-width="0.8"/>
    <!-- Right eye glow -->
    <ellipse cx="35" cy="64" rx="5" ry="5" fill="url(#eyeGlow)" filter="url(#strongGlow)">
      <animate attributeName="rx" values="5;6;5" dur="1.8s" repeatCount="indefinite"/>
      <animate attributeName="ry" values="5;6;5" dur="1.8s" repeatCount="indefinite"/>
    </ellipse>
    <!-- Right pupil -->
    <circle cx="35" cy="64" r="2.5" fill="#00f5ff">
      <animate attributeName="cx" values="35;36;35;34;35" dur="4s" repeatCount="indefinite"/>
    </circle>

    <!-- Eye blink -->
    <rect x="6" y="59" width="14" height="0" rx="2" fill="#0d1e30">
      <animate attributeName="height" values="0;10;0" dur="4s" keyTimes="0;0.1;0.2" repeatCount="indefinite"/>
    </rect>
    <rect x="28" y="59" width="14" height="0" rx="2" fill="#0d1e30">
      <animate attributeName="height" values="0;10;0" dur="4s" keyTimes="0;0.1;0.2" repeatCount="indefinite"/>
    </rect>

    <!-- Mouth / speaker grille -->
    <rect x="8" y="82" width="32" height="10" rx="3" fill="#060a12" stroke="#1a3a50" stroke-width="0.8"/>
    <line x1="11" y1="87" x2="15" y2="87" stroke="#00b4d8" stroke-width="1.2" opacity="0.8"/>
    <line x1="18" y1="87" x2="22" y2="87" stroke="#00b4d8" stroke-width="1.2" opacity="0.8"/>
    <line x1="25" y1="87" x2="29" y2="87" stroke="#00b4d8" stroke-width="1.2" opacity="0.8"/>
    <line x1="32" y1="87" x2="36" y2="87" stroke="#00b4d8" stroke-width="1.2" opacity="0.8"/>
    <!-- Speaker wave animation -->
    <line x1="11" y1="87" x2="15" y2="87" stroke="#00f5ff" stroke-width="1.2">
      <animate attributeName="y1" values="87;84;87;90;87" dur="0.5s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="87;84;87;90;87" dur="0.5s" repeatCount="indefinite"/>
    </line>
    <line x1="18" y1="87" x2="22" y2="87" stroke="#00f5ff" stroke-width="1.2">
      <animate attributeName="y1" values="87;90;87;84;87" dur="0.5s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="87;90;87;84;87" dur="0.5s" repeatCount="indefinite"/>
    </line>
    <line x1="25" y1="87" x2="29" y2="87" stroke="#00f5ff" stroke-width="1.2">
      <animate attributeName="y1" values="87;84;87;90;87" dur="0.4s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="87;84;87;90;87" dur="0.4s" repeatCount="indefinite"/>
    </line>
    <line x1="32" y1="87" x2="36" y2="87" stroke="#00f5ff" stroke-width="1.2">
      <animate attributeName="y1" values="87;90;87;84;87" dur="0.4s" repeatCount="indefinite"/>
      <animate attributeName="y2" values="87;90;87;84;87" dur="0.4s" repeatCount="indefinite"/>
    </line>

    <!-- Head bolts / rivets -->
    <circle cx="5" cy="50" r="2" fill="#1a3a52" stroke="#00b4d8" stroke-width="0.5"/>
    <circle cx="43" cy="50" r="2" fill="#1a3a52" stroke="#00b4d8" stroke-width="0.5"/>
    <circle cx="5" cy="88" r="2" fill="#1a3a52" stroke="#00b4d8" stroke-width="0.5"/>
    <circle cx="43" cy="88" r="2" fill="#1a3a52" stroke="#00b4d8" stroke-width="0.5"/>

  </g>

  <!-- ═══════════════════════════════════════ -->
  <!--  CONNECTION LINES robot → data nodes   -->
  <!-- ═══════════════════════════════════════ -->
  <!-- To left dropout node -->
  <line x1="426" y1="75" x2="135" y2="75" stroke="#00b4d8" stroke-width="0.6" stroke-dasharray="4,4" opacity="0.5">
    <animate attributeName="stroke-dashoffset" values="0;-16" dur="1s" repeatCount="indefinite"/>
  </line>
  <!-- To right accuracy node -->
  <line x1="476" y1="65" x2="770" y2="65" stroke="#00d4a8" stroke-width="0.6" stroke-dasharray="4,4" opacity="0.5">
    <animate attributeName="stroke-dashoffset" values="0;-16" dur="1s" repeatCount="indefinite"/>
  </line>
  <!-- To bottom left shap node -->
  <line x1="426" y1="155" x2="135" y2="178" stroke="#ffb703" stroke-width="0.6" stroke-dasharray="4,4" opacity="0.4">
    <animate attributeName="stroke-dashoffset" values="0;-16" dur="1.2s" repeatCount="indefinite"/>
  </line>
  <!-- To bottom right patients node -->
  <line x1="476" y1="155" x2="770" y2="173" stroke="#a29bfe" stroke-width="0.6" stroke-dasharray="4,4" opacity="0.4">
    <animate attributeName="stroke-dashoffset" values="0;-16" dur="1.2s" repeatCount="indefinite"/>
  </line>

  <!-- ═══════════════════════════════════════ -->
  <!--  TITLE TEXT                            -->
  <!-- ═══════════════════════════════════════ -->
  <text x="450" y="228" font-family="'Courier New',monospace" font-size="34" font-weight="bold"
    fill="url(#titleGrad)" text-anchor="middle" letter-spacing="3" filter="url(#softGlow)">
    PharmaTrialGuard
  </text>

  <!-- Animated underline -->
  <rect x="280" y="234" width="0" height="2" rx="1" fill="#00b4d8">
    <animate attributeName="width" values="0;340;0" dur="3s" repeatCount="indefinite"/>
    <animate attributeName="x" values="450;280;450" dur="3s" repeatCount="indefinite"/>
  </rect>

  <!-- Subtitle -->
  <text x="450" y="256" font-family="'Courier New',monospace" font-size="11" fill="#00b4d8"
    text-anchor="middle" letter-spacing="2" opacity="0.85">
    AI-POWERED CLINICAL TRIAL DROPOUT PREDICTION &amp; EXPLAINABILITY
  </text>

  <!-- Corner brackets -->
  <path d="M12,8 L12,2 L22,2" stroke="#00b4d8" stroke-width="1.5" fill="none" opacity="0.6"/>
  <path d="M888,8 L888,2 L878,2" stroke="#00b4d8" stroke-width="1.5" fill="none" opacity="0.6"/>
  <path d="M12,272 L12,278 L22,278" stroke="#00b4d8" stroke-width="1.5" fill="none" opacity="0.6"/>
  <path d="M888,272 L888,278 L878,278" stroke="#00b4d8" stroke-width="1.5" fill="none" opacity="0.6"/>

  <!-- Version tag -->
  <rect x="10" y="10" width="52" height="14" rx="3" fill="#0a1e30" stroke="#00b4d8" stroke-width="0.5" opacity="0.8"/>
  <text x="36" y="20" font-family="'Courier New',monospace" font-size="8" fill="#00b4d8" text-anchor="middle" opacity="0.9">v1.0.0</text>

  <!-- Status tag top right -->
  <rect x="838" y="10" width="52" height="14" rx="3" fill="#0a1e30" stroke="#00d4a8" stroke-width="0.5" opacity="0.8"/>
  <circle cx="844" cy="17" r="2.5" fill="#00d4a8">
    <animate attributeName="opacity" values="1;0.2;1" dur="1.5s" repeatCount="indefinite"/>
  </circle>
  <text x="868" y="20" font-family="'Courier New',monospace" font-size="8" fill="#00d4a8" text-anchor="middle" opacity="0.9">LIVE</text>

</svg>
