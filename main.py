import pandas as pd
import numpy as np
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import Frame

chatters = [
    {"username": "Soumyajit Pal", "message": "Soumyajit sent an attachment."},
    {"username": "Sagnik De", "message": "You sent an attachment."},
    {"username": "Aniket Safui", "message": "Active 13h\n13 hours ago\nago"},
    {"username": "Satwik", "message": "Active 10m\n10 minutes ago\nago"},
    {
        "username": "𝐘𝐨𝐮𝐫 𝐁𝐨𝐧𝐠𝐛𝐨𝐲",
        "message": "You: Esob nibbi Der k reply Dao , amader k to khuleo Dekho na",
    },
    {"username": "𝐒𝐚𝐟𝐚𝐥𝐲𝐚", "message": "Ikr"},
    {"username": "Ayan Das", "message": "You: Hm"},
    {"username": "Sayandip Sarkar", "message": "Emni"},
    {"username": "Tahsin Anan", "message": "Accha👍"},
    {"username": "Ｓｗａｒｎａｙｕ", "message": "You: 👍"},
    {"username": "Avirup Pal", "message": "🤣"},
    {"username": "Debanka Haldar", "message": "Aww"},
    {"username": "Snehasish Mondal", "message": "Khub baje"},
    {"username": "minereva", "message": "Apadoto na"},
    {"username": "Sagnik Biswas", "message": "Reacted 😂 to your message"},
    {"username": "Shreya Bez", "message": "🥰"},
    {
        "username": "TECHZONED\nPhone & Tech News",
        "message": "Reacted 😂 to your message",
    },
    {"username": "Anik Panja", "message": "You: 🤣"},
    {"username": "adhya_pandya", "message": "Ha pta h😀"},
    {"username": "Arghadeep Ghosh", "message": "Arghadeep sent an attachment."},
    {"username": "Akshat Jiwrajka", "message": "You sent an attachment."},
    {
        "username": "Shivam Arora",
        "message": "You: Brother pls review HP VICTUS ryzen 7 7840hs with rtx3050 (6gb) 95w tgp available at 79k for 16 gb (ddr5 5200mhz)variant ..",
    },
    {"username": "সৌম্য শুভ্র", "message": "ওহ্"},
    {"username": "Aryaan Sinha", "message": "Aryaan sent an attachment."},
    {"username": "Soham Kabir", "message": "bhalo👍"},
    {"username": "Soumyadeb Barman", "message": "You: Hmm"},
    {"username": "vedaant gupta", "message": "Not everyone can message this account."},
    {"username": "Debajyoti Roy", "message": "You: 🫠"},
    {"username": "Badguy_247", "message": "You: https://www.reddit.com/r/GOONED/"},
    {"username": "☆ Shreya ☆", "message": "Hmm"},
    {"username": "Debanjan Naskar", "message": "Follow back kot"},
    {"username": "_sristi chatterjee_", "message": "Yes yes thnx"},
    {"username": "", "message": "You: Ami vlo I achi"},
    {"username": "s", "message": "Mp r por Atul Krishna te chole ga6i"},
    {"username": "Soumyadip Mistry", "message": "Soumyadip sent an attachment."},
    {"username": "Swagata Maiti", "message": "Happy new year 🥳"},
    {"username": "vivi", "message": "💀😭"},
    {"username": "Arka Ghosh", "message": "Active 4h\n4 hours ago\nago"},
    {"username": '!" Mercy_xD', "message": "You: Sei"},
    {"username": "Deeksha Chatterjee", "message": "Deeksha sent an attachment."},
    {"username": "Sσυʋιƙ Mαɳɳα", "message": "You: 😂😂😂"},
    {"username": "Spring Fest", "message": "You sent an attachment."},
    {"username": "Tanmoy Gayen", "message": "😂"},
    {"username": "Rupan Kar", "message": "You sent an attachment."},
    {"username": "Agnibha Pal", "message": "You: 😐"},
    {"username": "5 Idiots", "message": "Deeksha sent an attachment."},
    {"username": "Arghyajyoti Biswas", "message": "You: 🤣thnx"},
    {"username": "IPL memes", "message": "Reacted 💋 to your message"},
    {"username": "Priyanshi Mukherjee", "message": "Acha 😂"},
    {"username": "", "message": "Hi 3d"},
    {"username": "Payel Bhandari", "message": "Oo"},
    {"username": "itzzme_bhattacharya_paromita", "message": "Amar jonno"},
    {"username": "Arkajyoti Modak", "message": "Arkajyoti sent an attachment."},
    {"username": "Raktim Datta", "message": "Raktim sent an attachment."},
    {"username": "Arghya Saha", "message": "🙃"},
    {"username": "Souvik Majhi", "message": "Souvik sent an attachment."},
    {"username": "Sanchita Saha", "message": "Reacted ❤️ to your message"},
    {"username": "arpita", "message": "Hmmm"},
    {"username": "MASK k Chutiye", "message": "Viswasarathi sent an attachment."},
    {"username": "Debarchan Mistry", "message": "Debarchan sent an attachment."},
    {"username": "Ishan Rai", "message": "Active 5h\n5 hours ago\nago"},
    {"username": "Sumon Sardar", "message": "Sumon sent an attachment."},
    {"username": "Adda Marar jaiga", "message": "Ki boss ki khobor"},
    {"username": "Debanshu Ghosh", "message": "You sent an attachment."},
    {"username": "Rupam Bora", "message": "Oh😂❤️"},
    {"username": "Captain Sayan Bhowmik", "message": "Hm hm"},
    {"username": "Shaurya IIT Kharagpur", "message": "You shared a story."},
    {"username": "Srijoni Sarkar", "message": "You: Hmm"},
    {"username": "Dalli Manideep", "message": "💯"},
    {"username": "𝕊𝕒𝕪𝕒𝕟 𝔾𝕙𝕠𝕤𝕙", "message": "𝕊𝕒𝕪𝕒𝕟 sent an attachment."},
    {"username": "𝚂𝚛𝚎𝚎𝚓𝚊𝚗 𝙿𝚊𝚗𝚓𝚊", "message": "𝚂𝚛𝚎𝚎𝚓𝚊𝚗 sent an attachment."},
    {"username": "Anubhab Bhattacharjee", "message": "😂"},
    {"username": "Baishakhi Bhunia", "message": "🙂🙂"},
    {"username": "AnimeFlex", "message": "Active 14m\n14 minutes ago\nago"},
    {"username": "Shubhayu Maji", "message": "🔥"},
    {"username": "borguinho", "message": "borguinho sent an attachment."},
    {"username": "Laxmikant Jorwal", "message": "REAL 🥹🥹"},
    {"username": "Tridibesh Sarkar", "message": "You sent an attachment."},
    {"username": "dumb", "message": "You: baka"},
    {"username": "LWEEBS", "message": "You sent an attachment."},
    {"username": "anish", "message": "😒"},
    {"username": "kirit", "message": "You: Sobai dekhe prai"},
    {"username": "Sauparna Das", "message": "Sauparna sent an attachment."},
    {"username": "MASK k Chutiye", "message": "swarajdian05 is active"},
    {"username": "Suprit Banerjee", "message": "You: 😂"},
    {
        "username": "JULIA BLISS ® DJ | Travel | Lifestyle",
        "message": "You sent an attachment.",
    },
    {"username": "Pratik", "message": "Pratik sent an attachment."},
    {"username": "Arnab Das", "message": "You: Bolll"},
    {"username": "محمد سعيد", "message": "Liked a message"},
    {"username": "Jayanta Sarkar", "message": "You: chinta koro na"},
    {"username": "", "message": "Thle oi bgm ta dilei vlo hoto 😶\u200d🌫️"},
    {"username": "Sneha Ghosh", "message": "Ebr chesta krchi dekhi ki hoy"},
    {"username": "Anshika Pandey", "message": "Anshika sent an attachment."},
    {"username": "Sannaddha Ray", "message": "Reacted ❤️ to your message"},
    {"username": "Sourajoy Jana", "message": "Sourajoy sent an attachment."},
    {"username": "Anik Panja", "message": "Anik sent an attachment."},
    {"username": "Anirban Chandra", "message": "You: Hi"},
    {
        "username": "aparajita verma",
        "message": "https://acrobat.adobe.com/link/track?uri=urn:aaid:scds:US:3c14c51c-8de1-41bd-9059-57f50cd928dd",
    },
    {
        "username": "Mukul Sharma",
        "message": "Greetings from stufflistings🌟 Now you can experience Gemini Advanced for just ₹2! 🌟 1. 🔗 Sideload the Gemini AI app on your phone. 2. 🌐 In your phone settings, change the assistant language to English USA. 3. 🚀 Enjoy Gemini as your new assistant! 🔗 play store link https://play.google.com/store/apps/details?id=com.google.android.apps.bard&utm_source=keyword_blog&utm_medium=owned&utm_campaign=blog_gem_24q1 🔗 Apk link https://www.apkmirror.com/apk/google-inc/google-gemini/google-gemini-1-0-603736800-release/google-gemini-1-0-603736800-android-apk-download/ 📌 Don't miss out on exclusive updates! Make sure to follow us for the latest tech trends. 👉 WhatsApp channel https://whatsapp.com/channel/0029Va9pDXAEgGfEseB5AX3A 👉 Telegram channel https://telegram.me/gizmoalerts Happy exploring! 🌐✨",
    },
]
df = pd.DataFrame(chatters)
df


# Helper function to wrap text in large columns
def wrap_text(text, max_len=50):
    words = text.split(" ")
    lines = []
    current_line = []
    current_length = 0
    for word in words:
        if current_length + len(word) + 1 <= max_len:
            current_line.append(word)
            current_length += len(word) + 1
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_length = len(word)
    if current_line:
        lines.append(" ".join(current_line))
    return "\n".join(lines)


# Create a PDF file from the DataFrame
def dataframe_to_pdf(df, output_filename):
    pdf = SimpleDocTemplate(output_filename, pagesize=letter)
    elements = []

    # Styles for the table
    style = TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
            ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
            ("ALIGN", (0, 0), (-1, -1), "LEFT"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("FONTSIZE", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
            ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
            ("GRID", (0, 0), (-1, -1), 1, colors.black),
        ]
    )

    # Wrap text in large columns and prepare data for the table
    data = []
    column_widths = []
    max_col_width = 5 * inch  # Set maximum width for large columns
    min_col_width = 1.5 * inch  # Minimum width for small columns

    for i, col in enumerate(df.columns):
        max_len = 50 if df[col].dtype == object else 20
        df[col] = df[col].apply(
            lambda x: wrap_text(str(x), max_len) if isinstance(x, str) else x
        )
        column_width = max_col_width if df[col].str.len().max() > 50 else min_col_width
        column_widths.append(column_width)

    # Convert dataframe rows into table format
    data.append(list(df.columns))  # Header
    for row in df.itertuples(index=False):
        data.append(list(row))

    # Create a table with the processed data
    table = Table(data, colWidths=column_widths)
    table.setStyle(style)

    elements.append(table)
    pdf.build(elements)


class Processing:
    def __init__(self, following, follower, chat):
        self.following = following
        self.follower = follower
        self.chatters = chat

    # Helper function to wrap text in large columns
    def wrap_text(self, text, max_len=50):
        words = text.split(" ")
        lines = []
        current_line = []
        current_length = 0
        for word in words:
            if current_length + len(word) + 1 <= max_len:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                lines.append(" ".join(current_line))
                current_line = [word]
                current_length = len(word)
        if current_line:
            lines.append(" ".join(current_line))
        return "\n".join(lines)

    def chats(self):
        df = pd.DataFrame(self.chatters)
        self.chatters = df

    def follow(self):
        df2 = pd.DataFrame(self.follower)
        df3 = pd.DataFrame(self.following)
        df2 = df2[df2[0] != ""]
        df3 = df3[df3[0] != ""]
        df2.rename(columns={0: "Followers"}, inplace=True)
        df3.rename(columns={0: "Following"}, inplace=True)
        diff = len(df3) - len(df2)
        fill_value = "  "
        if diff > 0:  # df1 is larger, so we need to pad df2
            padding = pd.DataFrame(
                [[fill_value] * df2.shape[1]] * diff, columns=df2.columns
            )
            df2 = pd.concat([df2, padding])
        elif diff < 0:
            padding = pd.DataFrame(
                [[fill_value] * df3.shape[1]] * abs(diff), columns=df3.columns
            )
            df3 = pd.concat(
                [df3, padding],
            )
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
        style = TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.grey),
                ("TEXTCOLOR", (0, 0), (-1, 0), colors.whitesmoke),
                ("ALIGN", (0, 0), (-1, -1), "LEFT"),
                ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
                ("FONTSIZE", (0, 0), (-1, -1), 10),
                ("BOTTOMPADDING", (0, 0), (-1, 0), 12),
                ("BACKGROUND", (0, 1), (-1, -1), colors.beige),
                ("GRID", (0, 0), (-1, -1), 1, colors.black),
            ]
        )
        data = []
        column_widths = []
        max_col_width = 5 * inch
        min_col_width = 1.5 * inch

        for i, col in enumerate(df.columns):
            max_len = 50 if df[col].dtype == object else 20
            df[col] = df[col].apply(
                lambda x: self.wrap_text(str(x), max_len) if isinstance(x, str) else x
            )
            column_width = (
                max_col_width if df[col].str.len().max() > 50 else min_col_width
            )
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
