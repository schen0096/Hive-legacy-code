tinymce.init({
    selector: 'div.editor',
    height: 500,
    menubar: false,
    plugins: [
      ' autolink lists link charmap anchor textcolor',
      'insertdatetime table paste wordcount'
    ],
    toolbar: 'formatselect | bold italic backcolor | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent | removeformat ',
    content_css: [
      '//fonts.googleapis.com/css?family=Lato:300,300i,400,400i',
      '//www.tiny.cloud/css/codepen.min.css'
    ]
  });