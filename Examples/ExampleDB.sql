PGDMP     
                	    z            simpleHTTPMicroservice    14.5    14.5     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    40963    simpleHTTPMicroservice    DATABASE     x   CREATE DATABASE "simpleHTTPMicroservice" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'Ukrainian_Ukraine.1251';
 (   DROP DATABASE "simpleHTTPMicroservice";
                postgres    false            ?            1259    40971    Users    TABLE     o   CREATE TABLE public."Users" (
    user_name character varying NOT NULL,
    user_password character varying
);
    DROP TABLE public."Users";
       public         heap    postgres    false            ?          0    40971    Users 
   TABLE DATA           ;   COPY public."Users" (user_name, user_password) FROM stdin;
    public          postgres    false    209   g       \           2606    40977    Users Users_pkey 
   CONSTRAINT     Y   ALTER TABLE ONLY public."Users"
    ADD CONSTRAINT "Users_pkey" PRIMARY KEY (user_name);
 >   ALTER TABLE ONLY public."Users" DROP CONSTRAINT "Users_pkey";
       public            postgres    false    209            ?   '   x?-N-244?442?
????8?H8?"???? ?     