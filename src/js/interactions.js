 // Micro-interactions for the analysis button
    const analyzeBtn = document.getElementById('analyzeBtn');
    const resultsSection = document.getElementById('resultSection');
    const dropZone = document.getElementById('drop-zone');
    const intentarNuevoBtn = document.getElementById('intentarNuevoBtn');
    const analyzeSection = document.getElementById('analysisSection');

    analyzeBtn.addEventListener('click', () => {
        // Simulated loading state
        const originalHtml = analyzeBtn.innerHTML;
        analyzeBtn.innerHTML = '<span class="material-symbols-outlined animate-spin text-sm">progress_activity</span> PROCESANDO...';
        analyzeBtn.classList.add('opacity-75');
        
        setTimeout(() => {
            analyzeBtn.innerHTML = originalHtml;
            analyzeBtn.classList.remove('opacity-75');
            
            // Scroll to results and pulse
            resultsSection.scrollIntoView({ behavior: 'smooth' });
            resultsSection.classList.add('ring-2', 'ring-teal-accent/40');
            setTimeout(() => resultsSection.classList.remove('ring-2', 'ring-teal-accent/40'), 1200);
            resultsSection.style.display = 'block'; // Show results section
            analyzeSection.style.display = 'none'; // Hide analysis section
        }, 1200);
    });//onclick="document.getElementById('file-input').click()"

    // Drop zone highlight
    dropZone.addEventListener('dragover', (e) => {
        e.preventDefault();
        dropZone.classList.add('bg-teal-soft/20', 'border-teal-accent');
    });

    dropZone.addEventListener('dragleave', () => {
        dropZone.classList.remove('bg-teal-soft/20', 'border-teal-accent');
    });

    dropZone.addEventListener('click', () => {
        document.getElementById('file-input').click();
    });

    intentarNuevoBtn.addEventListener('click', () => {
        resultsSection.style.display = 'none'; // Show results section
        analyzeSection.style.display = 'block'; // Hide analysis section
    });