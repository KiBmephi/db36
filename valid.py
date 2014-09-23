#!/usr/bin/python
#-*- coding: UTF-8 -*-

import optparse, libxml2, sys

def validate(xml_file, dtd_file):
  doc = libxml2.parseFile(xml_file)
  dtd = libxml2.parseDTD(None, dtd_file)
  ctxt = libxml2.newValidCtxt()
  ret = doc.validateDtd(ctxt, dtd)
  dtd.freeDtd()
  doc.freeDoc()
  return ret

raw_input
def main():
  op = optparse.OptionParser(description = U"�������� �� ������������ DTD", prog="dtd", version="0.1", usage=U"%prog")
  op.add_option("-x", "--xml", dest="xml", help=U"XML ��������", metavar="XML_FILE")
  op.add_option("-d", "--dtd", dest="dtd", help=U"DTD ��������", metavar="DTD_FILE")

  options, arguments = op.parse_args()
  if options.xml and options.dtd:
    if validate(options.xml, options.dtd):
      print "Successful!"
    else:
      print "Not Successful!"
  else:
    op.print_help()
if __name__=='__main__':
  main()
