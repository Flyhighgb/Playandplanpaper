(function(){
  var d=document.getElementById('days');
  if(d){var n=new Date(),y=(n.getMonth()===11&&n.getDate()>25)?n.getFullYear()+1:n.getFullYear();
    d.textContent=Math.ceil((new Date(y,11,25)-new Date(n.getFullYear(),n.getMonth(),n.getDate()))/864e5);}
  document.querySelectorAll('.chips button').forEach(function(b){b.addEventListener('click',function(){
    document.querySelectorAll('.chips button').forEach(function(o){o.setAttribute('aria-pressed',o===b);});
    var f=b.dataset.f;document.querySelectorAll('#hub-grid .card').forEach(function(c){c.hidden=!(f==='all'||c.dataset.f.split(' ').indexOf(f)>-1);});
  });});
  document.querySelectorAll('.thumbs button').forEach(function(b){b.addEventListener('click',function(){
    document.querySelectorAll('.thumbs button').forEach(function(o){o.setAttribute('aria-pressed',o===b);});
    document.getElementById('pdp-main').src=b.dataset.src;
  });});
})();
