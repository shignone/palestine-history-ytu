import logging
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,    
)



logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

keyboard = [
        [
            InlineKeyboardButton("1996", callback_data="1"),
            InlineKeyboardButton("1997", callback_data="2"),
        ],
        [
            InlineKeyboardButton("1998", callback_data="3"),
            InlineKeyboardButton("1999", callback_data="4"),
        ],
        [
            InlineKeyboardButton("2000", callback_data="5"),
            InlineKeyboardButton("2001", callback_data="6"),
        ],
        [
            InlineKeyboardButton("2002", callback_data="7"),
            InlineKeyboardButton("2003", callback_data="8"),
        ],
        [
            InlineKeyboardButton("2004", callback_data="9"),
            InlineKeyboardButton("2005", callback_data="10"),
        ],
        [
            InlineKeyboardButton("2006", callback_data="11"),
            InlineKeyboardButton("2007", callback_data="12"),
        ],
        

    ]
reply_markup = InlineKeyboardMarkup(keyboard)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
   
 await update.message.reply_text("اهلا بيك في بوت تاريخ فلسطين، تقدر تشوف ملخص اللي حصل في كل سنة من 1996 الى 2007", reply_markup=reply_markup)

async def button(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:

    query = update.callback_query
   
    

    await query.answer()
    if query.data == "1":
        await query.edit_message_text(text=' أقيمت إنتخابات رئاسية فاز بها ياسر عرفات على منافسته الوحيدة سميحة خليل ', reply_markup=reply_markup)
    elif query.data == "2":
        await query.edit_message_text(text='تم الإتفاق بين منظمة التحرير الفلسطينية وإسرائيل على ما عرف بإسم إتفاق الخليل الذي ترتب عليه إنسحاب القوات الإسرائيلية من مناطق مأهولة بالفلسطينيين وبقاء مناطق تحت السيطرة الإسرائيلية في البلدة القديمة والطرق المؤدية إليها .', reply_markup=reply_markup)
    elif query.data == "3":
        await query.edit_message_text(text='نصت اتفاقية واي ريفر التي وقعت عام 1998 على الانسحاب الإسرائيلي من بعض مناطق الضفة، وعلى اتخاذ تدابير أمنية لمكافحة الإرهاب، وتوطيد العلاقات الاقتصادية بين السلطة الفلسطينية وإسرائيل. وإعادة الانتشار الثاني للقوات الإسرائيلية في الضفة الغربية على أن تتم إعادة الانتشار على ثلاث مراحل', reply_markup=reply_markup)
    elif query.data == "4":
        await query.edit_message_text(text=' إسرائيل والفلسطينيون وافقوا على فتح ممر أمن يصل بين الضفة الغربية وقطاع غزة. رئيس الوزراء إيهود باراك والزعيم الفلسطيني ياسر عرفات وافقا على الأتفاق، الذي سمح للفلسطينيين لأول مرّة بالتحرّك بحرية بشكل نسبي بين المناطق.', reply_markup=reply_markup)
    elif query.data == "5":
        await query.edit_message_text(text='الانتفاضة الفلسطينية 2000 (انتفاضة الاقصى)\nكانت بداية انتفاضة الاقصى في تاريخ 28/9/2000 ردة فعل شعبية على دخول ارئيل شارون أحد باحات المسجد الاقصى المبارك.', reply_markup=reply_markup)
    elif query.data == "6":
        await query.edit_message_text(text='كانت مستوطنة "سديروت"، جنوبي إسرائيل، على موعد مع تلقي أول صاروخ فلسطيني محلي الصنع، أطلقته كتائب القسام، بعد عام من انطلاق انتفاضة الأقصى يوم 26 أكتوبر/تشرين الأول 2001، لتطور الكتائب بعد ذلك وعلى نحو متسارع من قدراتها في تصنيع الصواريخ.', reply_markup=reply_markup)
    elif query.data == "7":
        await query.edit_message_text(text='في يونيو حزيران 2002 بدأت الحكومة الإسرائيلية ببناء جدار فاصل داخل الضفة الغربية، قائلة بأن الهدف من بناء الجدار هو حماية مواطنيها من "الهجمات الإرهابية" والحفاظ على أمنها، وأدى بناء الجدار إلى تحديد الحركة بين مناطق الضفة الغربية، كما حدّ من الحركة إلى إسرائيل بالإضافة إلى خلق مناطق مغلقة وجيوب محصورة خلف الجدار لا يستطيع السكان الفلسطينيون الوصول إليها إلا بتصاريح خاصة، وكذلك إلى حصر ما يقدر ب 5000 فلسطيني خلف الجدار.', reply_markup=reply_markup)
    elif query.data == "8":
        await query.edit_message_text(text='في السنة الثالثة من إنتفاضة الأقصى قتلت إسرائيل 503 فلسطيني وقد كانت خطة خارطة الطريق والتي اعلنت في القمة العربية الخامسة عشرة التي عقدت في شرم الشيخ بالإضافة إلى اغتيال إسماعيل أبو شنب ابرز احداث العام.', reply_markup=reply_markup)
    elif query.data == "9":
        await query.edit_message_text(text='شهد عام 2004 في فلسطين احداثا كثيرة أبرزها وفاة ياسر عرفات رئيس السلطة الوطنية الفلسطينية واغتيال إسرائيل لمؤسس حماس أحمد ياسين وعبد العزيز الرنتيسي والبدء في بناء الجدار العازل في الضفة الغربية.', reply_markup=reply_markup)
    elif query.data == "10":
        await query.edit_message_text(text='في 9 يناير 2005 إستلم السيد محمود عباس لمنصب الرئاسة للسلطة الوطنية الفلسطينية بعيد وفاة الرئيس الراحل السيد ياسر عرفات الذي يظل يشغل هذا المنصب حتى وفاته وإقامة إنتخابات رئاسية. ', reply_markup=reply_markup)
    elif query.data == "11":
        await query.edit_message_text(text='عام 2006 إقيمت الإنتخابات التشريعة الثانية في الضفة الغربية وقطاع غزة، أسفرت عن نجاح حركة حماس بالأغلبية النيابية في المجلس التشريعي الفلسطيني، وهو ما اعتبر تغيير كبير على الخارطة السياسية الفلسطينية، وتعرض الفلسطينيون بعدها لضغوط دولية تمثلت في تغيير سياسة الدول المانحة في تحويلها للأموال للسلطة الوطنية الفلسطينية أو إيقافها تماما مما أدى إلى ضائقة مالية خانقة تعرضت لها مؤسسات السلطة .', reply_markup=reply_markup)
    elif query.data == "12":
        await query.edit_message_text(text='معركة غزة، يشار إليها أيضًا انقلاب حركة حماس في قطاع غزة، كان صراع عسكري بين حركتي فتح وحماس، جرت أحداثه في قطاع غزة بين 10 و15 يونيو 2007. شكل الانقلاب ذروة الصراع بين فتح وحماس، وتركزت على النضال من أجل السلطة، بعد أن فقدتها حركة فتح في الانتخابات البرلمانية لعام 2006. نجح مقاتلو حماس في السيطرة على قطاع غزة والإطاحة بمسؤولي فتح. وأسفرت المعركة عن حل حكومة الوحدة وتقسيم الأراضي الفلسطينية إلى كيانين بحكم الأمر الواقع، الضفة الغربية التي تخضع للسلطة الوطنية الفلسطينية، وغزة التي تحكمها حماس.', reply_markup=reply_markup)
    
    



def main() -> None:
   
    application = Application.builder().token("6504534469:AAHy3LIrAeJv5qwo4RHqoxSEz0Up-iMfvks").build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CallbackQueryHandler(button))
    application.add_handler(CommandHandler("help", help_command))
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()    