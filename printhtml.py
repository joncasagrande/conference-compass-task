class PrintHtml:
      # I am only using this class because I dont know if it was possible to work with dominate
      def __init__(self):
            self.htmlfile = "<html><head>"
            self.htmlfile = self.htmlfile + "<meta charset=\"utf-8\">"
            self.htmlfile = self.htmlfile + "<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">"
            self.htmlfile = self.htmlfile + "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">"
            self.htmlfile = self.htmlfile + " <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\">"
            self.htmlfile = self.htmlfile + "</head><body>" 
            self.htmlfile = self.htmlfile +"<div class=\"row\">"
  
      def closeHtml(self):
            self.htmlfile = self.htmlfile +"</div>"
            self.htmlfile = self.htmlfile+ " <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js\"></script>"
            self.htmlfile = self.htmlfile+ " <script src=\"js/bootstrap.min.js\"></script>"
            self.htmlfile = self.htmlfile+ " </body></html>"

      def addRow(self):
            self.htmlfile = self.htmlfile +"</div><br/>"
            self.htmlfile = self.htmlfile +"<div class=\"row\">"

      def printLink(self,planned_works):
            self.htmlfile = self.htmlfile + "<div class=\"col-md-3\">"
            self.htmlfile = self.htmlfile +"<h5>"+getattr(planned_works, 'reference_number')+" -- Road "+getattr(planned_works, 'road')+"</h5>"
            self.htmlfile = self.htmlfile +"<spam style=\"font-size:11px\">Location:</spam>"
            self.htmlfile = self.htmlfile +"<p style=\"font-size:14px\">"+getattr(planned_works, 'location')+"</p>"
            #htmlfile= htmlfile +"<spam style=\"font-size:11px\">Local authority:</spam>"
            #htmlfile= htmlfile +"<p style=\"font-size:14px\">"+getattr(planned_works, 'local_authority')+"</p>"
            #todo check trouble with /
            self.htmlfile = self.htmlfile +"<spam style=\"font-size:11px\">Description:</spam>"
            self.htmlfile = self.htmlfile +"<p style=\"font-size:12px\">"+getattr(planned_works, 'description')+"</p>"
            self.htmlfile = self.htmlfile +"<spam style=\"font-size:11px\">Start at:</spam>"
            self.htmlfile = self.htmlfile +"<p style=\"font-size:12px\">"+getattr(planned_works, 'start_date')+"</p>"
            self.htmlfile = self.htmlfile +"<spam style=\"font-size:11px\">End at:</spam>"
            self.htmlfile = self.htmlfile +"<p style=\"font-size:12px\">"+getattr(planned_works, 'end_date')+"</p>"
            self.htmlfile = self.htmlfile +"<spam style=\"font-size:9px\">Published "+getattr(planned_works, 'published_date')+"</spam></div>"
            self.htmlfile = self.htmlfile +"</div>"  

      def printHtml(self):
            return self.htmlfile