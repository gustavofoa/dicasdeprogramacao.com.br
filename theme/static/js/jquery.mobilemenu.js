!function(a){a.fn.mobileMenu=function(b){var c={defaultText:"Navigate to...",className:"select-menu",subMenuClass:"sub-menu",subMenuDash:"&ndash;"},d=a.extend(c,b),e=a(this);return this.each(function(){e.find("ul").addClass(d.subMenuClass),a("<select />",{class:d.className}).insertAfter(e),a("<option />",{value:"#",text:d.defaultText}).appendTo("."+d.className),e.find("a").each(function(){var g,b=a(this),c="&nbsp;"+b.text(),e=b.parents("."+d.subMenuClass),f=e.length;b.parents("ul").hasClass(d.subMenuClass)&&(g=Array(f+1).join(d.subMenuDash),c=g+c),a("<option />",{value:this.href,html:c,selected:this.href==window.location.href}).appendTo("."+d.className)}),a("."+d.className).change(function(){var b=a(this).val();"#"!==b&&(window.location.href=a(this).val())})}),this}}(jQuery);