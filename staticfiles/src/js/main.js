document.addEventListener("DOMContentLoaded", function () {
    const toggles = document.querySelectorAll('[data-collapse-toggle]');
    toggles.forEach(toggle => {
        toggle.addEventListener('click', () => {
            const targetId = toggle.getAttribute('data-collapse-toggle');
            const target = document.getElementById(targetId);
            target.classList.toggle('hidden');
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('navbar-toggle');
    const menu = document.getElementById('navbar-dropdown');
  
    const dropdown = document.getElementById('dropdownNavbarLink');
    const dropdownMenu = document.getElementById('dropdownNavbar');
  
    const doubleDropdownButton = document.getElementById('doubleDropdownButton');
    const doubleDropdown = document.getElementById('doubleDropdown');

    const dropdownCantos = document.querySelector('#dropdownNavbarLinkCantos');
dropdownCantos.addEventListener('click', () => {
    const menu = document.querySelector('#dropdownNavbarCantos');
    menu.classList.toggle('hidden');
});

const dropdownCreadores = document.querySelector('#dropdownNavbarLinkCreadores');
dropdownCantos.addEventListener('click', () => {
    const menu = document.querySelector('#dropdownNavbarCreadores');
    menu.classList.toggle('hidden');
});
})

document.addEventListener('DOMContentLoaded', function () {
    const button = document.getElementById('navbar-toggle');
    const menu = document.getElementById('navbar-dropdown');
  
    const dropdownButton = document.getElementById('dropdownNavbarLink');
    const dropdownMenu = document.getElementById('dropdownNavbar');
  
    const doubleDropdownButton = document.getElementById('doubleDropdownButton');
    const doubleDropdown = document.getElementById('doubleDropdown');
  
    dropdownButton.addEventListener('click', () => {
      dropdownMenu.classList.toggle('hidden');
    });
  
    doubleDropdownButton.addEventListener('click', () => {
      doubleDropdown.classList.toggle('hidden');
    });
  
    button.addEventListener('click', function () {
      menu.classList.toggle('hidden');
    });
  });