import pandas as pd
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch


class Processing:
    def __init__(self, following, follower, chat):
        self.following = following
        self.follower = follower
        self.chatters = chat

    # Helper function to wrap text in large columns
    def wrap_text(self, text, max_len=50):
        words = text.split(' ')
        lines = []
        current_line = []
        current_length = 0
        for word in words:
            if current_length + len(word) + 1 <= max_len:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)
        if current_line:
            lines.append(' '.join(current_line))
        return "\n".join(lines)

    def chats(self):
        df = pd.DataFrame(self.chatters)
        self.chatters = df

    def follow(self):
        df2 = pd.DataFrame(self.follower)
        df3 = pd.DataFrame(self.following)
        df2 = df2[df2[0] != ""]
        df3 = df3[df3[0] != ""]
        df2.rename(columns={0: 'Followers'}, inplace=True)
        df3.rename(columns={0: 'Following'}, inplace=True)
        diff = len(df3) - len(df2)
        fill_value = "  "
        if diff > 0:  # df1 is larger, so we need to pad df2
            padding = pd.DataFrame([[fill_value] * df2.shape[1]] * diff, columns=df2.columns)
            df2 = pd.concat([df2, padding])
        elif diff < 0:
            padding = pd.DataFrame([[fill_value] * df3.shape[1]] * abs(diff), columns=df3.columns)
            df3 = pd.concat([df3, padding], )
        df2 = df2.reset_index(drop=True)
        df3 = df3.reset_index(drop=True)
        self.follower = df2
        self.following = df3
        df4 = pd.concat([df2, df3], axis=1)

        self.comb = df4

    def dataframe_to_pdf(self, df, output_filename):
        pdf = SimpleDocTemplate(output_filename, pagesize=letter)
        elements = []

        # Styles for the table
        style = TableStyle([
            ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
            ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
            ('ALIGN', (0, 0), (-1, -1), 'LEFT'),
            ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
            ('FONTSIZE', (0, 0), (-1, -1), 10),
            ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
            ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
            ('GRID', (0, 0), (-1, -1), 1, colors.black),
        ])
        data = []
        column_widths = []
        max_col_width = 5 * inch
        min_col_width = 1.5 * inch

        for i, col in enumerate(df.columns):
            max_len = 50 if df[col].dtype == object else 20
            df[col] = df[col].apply(lambda x: self.wrap_text(str(x), max_len) if isinstance(x, str) else x)
            column_width = max_col_width if df[col].str.len().max() > 50 else min_col_width
            column_widths.append(column_width)

        data.append(list(df.columns))
        for row in df.itertuples(index=False):
            data.append(list(row))

        table = Table(data, colWidths=column_widths)
        table.setStyle(style)

        elements.append(table)
        pdf.build(elements)

    def process(self, n1, n2):
        self.chats()
        self.follow()
        self.dataframe_to_pdf(self.chatters, n1)
        self.dataframe_to_pdf(self.comb, n2)
        print("Successfully saved")
