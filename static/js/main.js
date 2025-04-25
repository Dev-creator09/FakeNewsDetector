// Wait for the DOM to fully load
document.addEventListener('DOMContentLoaded', function() {
    // Form validation
    const newsForm = document.querySelector('form');
    
    if (newsForm) {
        newsForm.addEventListener('submit', function(e) {
            const textArea = document.getElementById('news_text');
            
            if (!textArea.value.trim()) {
                e.preventDefault();
                alert('Please enter some text to analyze.');
                return false;
            }
            
            if (textArea.value.trim().length < 50) {
                if (!confirm('The text entered is quite short. For better results, consider using a longer article. Proceed anyway?')) {
                    e.preventDefault();
                    return false;
                }
            }
            
            // Add a loading state
            const submitBtn = this.querySelector('button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.textContent = 'Analyzing...';
            }
            
            return true;
        });
    }
    
    // Animate confidence meter on results page
    const meterSpan = document.querySelector('.meter span');
    if (meterSpan) {
        // Force re-render to trigger the transition
        setTimeout(() => {
            const widthValue = meterSpan.style.width;
            meterSpan.style.width = '0';
            
            setTimeout(() => {
                meterSpan.style.width = widthValue;
            }, 50);
        }, 100);
    }
    
    // Enable example article
    const exampleBtn = document.getElementById('load-example');
    if (exampleBtn) {
        exampleBtn.addEventListener('click', function() {
            const textArea = document.getElementById('news_text');
            
            // Load fake news example
            textArea.value = `BREAKING: Scientists Discover New Planet Inhabited by Advanced Civilization
            
In what might be the most significant discovery in human history, astronomers at a secret research facility claim to have found definitive evidence of an advanced alien civilization on a recently discovered Earth-like planet only 4.2 light years away.
            
The scientists, who wish to remain anonymous due to government restrictions, say they have been in direct communication with the alien species for several months. "They are far more advanced than us, both technologically and spiritually," said one researcher who spoke on condition of anonymity.
            
The government has allegedly been covering up this discovery, fearing mass panic or religious upheaval. Our source claims that world leaders have already met in secret to discuss establishing official first contact.
            
The implications of this discovery are shocking and will fundamentally change our understanding of humanity's place in the universe. More details to come as this exclusive story develops.`;
        });
    }
});