from datetime import date

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import String, ForeignKey


class Base(DeclarativeBase):
    DEFAULT_STR_LENGTH = 2048


class BaseWithId(Base):
    __abstract__ = True
    id: Mapped[int] = mapped_column(primary_key=True)


class Media(BaseWithId):
    __tablename__ = 'media'

    name: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    type_id: Mapped[int]
    link: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    description: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))


class MediaType(BaseWithId):
    __tablename__ = 'media_type'

    name: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))


class News(BaseWithId):
    __tablename__ = 'news'

    description: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    text: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    created_at: Mapped[date]
    is_posted: Mapped[bool] = mapped_column(default=True)
    bot_post_setting_id: Mapped[int] = mapped_column(ForeignKey('bot_post_setting.id', ondelete='CASCADE'))
    preview_photo: Mapped[int] = mapped_column(ForeignKey('media.id', ondelete='CASCADE'))


class BotPostSetting(BaseWithId):
    __tablename__ = 'bot_post_setting'

    is_posted: Mapped[bool] = mapped_column(default=True)


class ProjectCategory(BaseWithId):
    __tablename__ = 'project_category'

    name: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))


class Project(BaseWithId):
    __tablename__ = 'project'

    title: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    description: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    text: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    project_category_id: Mapped[int] = mapped_column(ForeignKey('project_category.id', ondelete='CASCADE'))
    created_at: Mapped[date]
    is_posted: Mapped[bool] = mapped_column(default=True)
    preview_photo: Mapped[int] = mapped_column(ForeignKey('media.id', ondelete='CASCADE'))


class Press(BaseWithId):
    __tablename__ = 'press'

    title: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    description: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    created_at: Mapped[date]
    is_posted: Mapped[bool] = mapped_column(default=True)
    preview_photo: Mapped[int] = mapped_column(ForeignKey('media.id', ondelete='CASCADE'))
    external_link: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))


class Electron(BaseWithId):
    __tablename__ = 'electron'

    name: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    description: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    photo_id: Mapped[int] = mapped_column(ForeignKey('media.id', ondelete='CASCADE'))


class Painting(BaseWithId):
    __tablename__ = 'painting'

    title: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    author: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    description: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    materials: Mapped[str] = mapped_column(String(length=Base.DEFAULT_STR_LENGTH))
    created_at: Mapped[date]
    is_posted: Mapped[bool] = mapped_column(default=True)
    preview_photo: Mapped[int] = mapped_column(ForeignKey('media.id', ondelete='CASCADE'))


class MediaPainting(Base):
    __tablename__ = 'media_painting'

    media_id: Mapped[int] = mapped_column(ForeignKey('media.id', ondelete='CASCADE'), primary_key=True)
    painting_id: Mapped[int] = mapped_column(ForeignKey('painting.id', ondelete='CASCADE'))
