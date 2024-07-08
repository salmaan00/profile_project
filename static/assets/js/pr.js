function saveProfile() {
    // Here you can implement JavaScript to send the profile data to the server or perform other actions
    // For demonstration purposes, we'll just log the profile data to the console
    let bio = document.getElementById('bio').innerText.trim();
    let skills = document.getElementById('skills').innerText.trim();
    let contactDetails = document.getElementById('contact-details').innerText.trim();
    let projectShowcases = document.getElementById('project-showcases').innerText.trim();
    let workExperience = document.getElementById('work-experience').innerText.trim();
    let education = document.getElementById('education').innerText.trim();
    let certifications = document.getElementById('certifications').innerText.trim();
    
    console.log('Bio:', bio);
    console.log('Skills:', skills);
    console.log('Contact details:', contactDetails);
    console.log('Project showcases:', projectShowcases);
    console.log('Work experience:', workExperience);
    console.log('Education:', education);
    console.log('Certifications:', certifications);
}