<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0">

<xsl:template match="/">
  <html>
    <head>
      <title>Boat audio</title>
    </head>
    <body>
      <h2>Employee information</h2>
      <table>
        <tr><th>Employee name</th><th>Role</th><th>Salary</th></tr>
        <xsl:for-each select="Business/company/Employee">
          <tr>
            <td><xsl:value-of select="name"/></td>
            <td><xsl:value-of select="role"/></td>
            <td><xsl:value-of select="salary"/></td>
          </tr>
        </xsl:for-each>
      </table>
    </body>
  </html>
</xsl:template>

</xsl:stylesheet>
