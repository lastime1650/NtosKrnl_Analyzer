# RtlDecompressBufferXpressLz

- RVA: `0x00450330`–`0x0045074D` (길이 `1,053` bytes)
- VA: `0x0000000140450330`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A71B4`
- 디코드: `296`개 명령, `1,053/1,053` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **0**; 고유 호출 대상: **0**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- 직접 디코드된 call 명령이 없습니다.

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00450330  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
00450335  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0045033A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0045033F  48 89 7C 24 20                  mov qword ptr [rsp + 0x20], rdi
00450344  41 54                           push r12
00450346  41 56                           push r14
00450348  41 57                           push r15
0045034A  4D 8B D0                        mov r10, r8
0045034D  4C 8B D9                        mov r11, rcx
00450350  41 83 F9 05                     cmp r9d, 5
00450354  0F 82 31 03 00 00               jb 0x14045068b
0045035A  41 8B D9                        mov ebx, r9d
0045035D  48 8B F9                        mov rdi, rcx
00450360  49 03 D8                        add rbx, r8
00450363  44 8B FA                        mov r15d, edx
00450366  4C 03 F9                        add r15, rcx
00450369  45 33 E4                        xor r12d, r12d
0045036C  4C 8D 73 AA                     lea r14, [rbx - 0x56]
00450370  49 8D AF 90 FE FF FF            lea rbp, [r15 - 0x170]
00450377  66 0F 1F 84 00 00 00 00 00      nop word ptr [rax + rax]
00450380  41 8B 0A                        mov ecx, dword ptr [r10]
00450383  49 83 C2 04                     add r10, 4
00450387  4D 3B D6                        cmp r10, r14
0045038A  0F 83 B7 02 00 00               jae 0x140450647
00450390  48 3B FD                        cmp rdi, rbp
00450393  0F 83 AE 02 00 00               jae 0x140450647
00450399  8D 04 4D 01 00 00 00            lea eax, [rcx*2 + 1]
004503A0  85 C9                           test ecx, ecx
004503A2  78 12                           js 0x1404503b6
004503A4  EB 65                           jmp 0x14045040b
004503A6  41 0F B6 0A                     movzx ecx, byte ptr [r10]
004503AA  88 0F                           mov byte ptr [rdi], cl
004503AC  48 FF C7                        inc rdi
004503AF  49 FF C2                        inc r10
004503B2  03 C0                           add eax, eax
004503B4  74 CA                           je 0x140450380
004503B6  41 0F B7 32                     movzx esi, word ptr [r10]
004503BA  49 83 C2 02                     add r10, 2
004503BE  8B D6                           mov edx, esi
004503C0  48 C1 EE 03                     shr rsi, 3
004503C4  48 FF C6                        inc rsi
004503C7  83 E2 07                        and edx, 7
004503CA  48 83 FA 07                     cmp rdx, 7
004503CE  74 5E                           je 0x14045042e
004503D0  4C 8B C7                        mov r8, rdi
004503D3  4C 8B CA                        mov r9, rdx
004503D6  4C 2B C6                        sub r8, rsi
004503D9  48 83 C2 03                     add rdx, 3
004503DD  4D 3B C3                        cmp r8, r11
004503E0  0F 82 A5 02 00 00               jb 0x14045068b
004503E6  48 83 FE 04                     cmp rsi, 4
004503EA  0F 82 F9 00 00 00               jb 0x1404504e9
004503F0  41 8B 08                        mov ecx, dword ptr [r8]
004503F3  89 0F                           mov dword ptr [rdi], ecx
004503F5  41 8B 48 04                     mov ecx, dword ptr [r8 + 4]
004503F9  89 4F 04                        mov dword ptr [rdi + 4], ecx
004503FC  48 83 FA 09                     cmp rdx, 9
00450400  7D 49                           jge 0x14045044b
00450402  48 03 FA                        add rdi, rdx
00450405  85 C0                           test eax, eax
00450407  78 A9                           js 0x1404503b2
00450409  03 C0                           add eax, eax
0045040B  85 C0                           test eax, eax
0045040D  78 97                           js 0x1404503a6
0045040F  03 C0                           add eax, eax
00450411  78 7B                           js 0x14045048e
00450413  03 C0                           add eax, eax
00450415  41 8B 0A                        mov ecx, dword ptr [r10]
00450418  89 0F                           mov dword ptr [rdi], ecx
0045041A  0F 88 82 00 00 00               js 0x1404504a2
00450420  48 83 C7 04                     add rdi, 4
00450424  49 83 C2 04                     add r10, 4
00450428  03 C0                           add eax, eax
0045042A  78 86                           js 0x1404503b2
0045042C  EB DB                           jmp 0x140450409
0045042E  4D 85 E4                        test r12, r12
00450431  74 7C                           je 0x1404504af
00450433  41 0F B6 14 24                  movzx edx, byte ptr [r12]
00450438  48 C1 EA 04                     shr rdx, 4
0045043C  45 33 E4                        xor r12d, r12d
0045043F  48 83 FA 0F                     cmp rdx, 0xf
00450443  74 7A                           je 0x1404504bf
00450445  48 83 C2 07                     add rdx, 7
00450449  EB 85                           jmp 0x1404503d0
0045044B  48 83 C7 08                     add rdi, 8
0045044F  49 83 C0 08                     add r8, 8
00450453  48 83 EA 08                     sub rdx, 8
00450457  48 3B FD                        cmp rdi, rbp
0045045A  0F 83 D2 00 00 00               jae 0x140450532
00450460  41 8B 08                        mov ecx, dword ptr [r8]
00450463  89 0F                           mov dword ptr [rdi], ecx
00450465  41 8B 48 04                     mov ecx, dword ptr [r8 + 4]
00450469  89 4F 04                        mov dword ptr [rdi + 4], ecx
0045046C  41 8B 48 08                     mov ecx, dword ptr [r8 + 8]
00450470  89 4F 08                        mov dword ptr [rdi + 8], ecx
00450473  41 8B 48 0C                     mov ecx, dword ptr [r8 + 0xc]
00450477  89 4F 0C                        mov dword ptr [rdi + 0xc], ecx
0045047A  48 83 FA 11                     cmp rdx, 0x11
0045047E  7C 82                           jl 0x140450402
00450480  48 83 C7 10                     add rdi, 0x10
00450484  49 83 C0 10                     add r8, 0x10
00450488  48 83 EA 10                     sub rdx, 0x10
0045048C  EB C9                           jmp 0x140450457
0045048E  41 0F B7 0A                     movzx ecx, word ptr [r10]
00450492  66 89 0F                        mov word ptr [rdi], cx
00450495  48 83 C7 02                     add rdi, 2
00450499  49 83 C2 02                     add r10, 2
0045049D  E9 10 FF FF FF                  jmp 0x1404503b2
004504A2  48 83 C7 03                     add rdi, 3
004504A6  49 83 C2 03                     add r10, 3
004504AA  E9 03 FF FF FF                  jmp 0x1404503b2
004504AF  4D 8B E2                        mov r12, r10
004504B2  49 FF C2                        inc r10
004504B5  41 0F B6 14 24                  movzx edx, byte ptr [r12]
004504BA  83 E2 0F                        and edx, 0xf
004504BD  EB 80                           jmp 0x14045043f
004504BF  49 8D 4A 07                     lea rcx, [r10 + 7]
004504C3  49 3B CE                        cmp rcx, r14
004504C6  0F 83 A4 01 00 00               jae 0x140450670
004504CC  41 0F B6 12                     movzx edx, byte ptr [r10]
004504D0  49 FF C2                        inc r10
004504D3  48 81 FA FF 00 00 00            cmp rdx, 0xff
004504DA  0F 84 12 02 00 00               je 0x1404506f2
004504E0  48 83 C2 0F                     add rdx, 0xf
004504E4  E9 5C FF FF FF                  jmp 0x140450445
004504E9  41 0F B6 08                     movzx ecx, byte ptr [r8]
004504ED  88 0F                           mov byte ptr [rdi], cl
004504EF  48 83 FE 01                     cmp rsi, 1
004504F3  74 1A                           je 0x14045050f
004504F5  41 0F B6 48 01                  movzx ecx, byte ptr [r8 + 1]
004504FA  88 4F 01                        mov byte ptr [rdi + 1], cl
004504FD  48 83 FE 02                     cmp rsi, 2
00450501  0F 85 E1 01 00 00               jne 0x1404506e8
00450507  48 2B D6                        sub rdx, rsi
0045050A  48 03 FE                        add rdi, rsi
0045050D  EB 15                           jmp 0x140450524
0045050F  41 0F B6 08                     movzx ecx, byte ptr [r8]
00450513  88 4F 01                        mov byte ptr [rdi + 1], cl
00450516  41 0F B6 08                     movzx ecx, byte ptr [r8]
0045051A  88 4F 02                        mov byte ptr [rdi + 2], cl
0045051D  49 8B D1                        mov rdx, r9
00450520  48 83 C7 03                     add rdi, 3
00450524  48 85 D2                        test rdx, rdx
00450527  0F 84 D8 FE FF FF               je 0x140450405
0045052D  E9 BE FE FF FF                  jmp 0x1404503f0
00450532  4C 8D 0C 3A                     lea r9, [rdx + rdi]
00450536  4D 3B CF                        cmp r9, r15
00450539  0F 87 4C 01 00 00               ja 0x14045068b
0045053F  49 8B F0                        mov rsi, r8
00450542  48 8B CA                        mov rcx, rdx
00450545  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
00450547  49 8B F9                        mov rdi, r9
0045054A  85 C0                           test eax, eax
0045054C  0F 89 9E 00 00 00               jns 0x1404505f0
00450552  03 C0                           add eax, eax
00450554  0F 84 DD 00 00 00               je 0x140450637
0045055A  4C 3B D3                        cmp r10, rbx
0045055D  0F 84 49 01 00 00               je 0x1404506ac
00450563  49 8D 4A 01                     lea rcx, [r10 + 1]
00450567  48 3B CB                        cmp rcx, rbx
0045056A  0F 83 CF 01 00 00               jae 0x14045073f
00450570  41 0F B7 32                     movzx esi, word ptr [r10]
00450574  49 83 C2 02                     add r10, 2
00450578  8B D6                           mov edx, esi
0045057A  48 C1 EE 03                     shr rsi, 3
0045057E  48 FF C6                        inc rsi
00450581  83 E2 07                        and edx, 7
00450584  48 83 FA 07                     cmp rdx, 7
00450588  0F 84 89 00 00 00               je 0x140450617
0045058E  48 8B CF                        mov rcx, rdi
00450591  48 83 C2 03                     add rdx, 3
00450595  48 2B CE                        sub rcx, rsi
00450598  49 3B CB                        cmp rcx, r11
0045059B  0F 82 EA 00 00 00               jb 0x14045068b
004505A1  4C 8D 04 3A                     lea r8, [rdx + rdi]
004505A5  4D 3B C7                        cmp r8, r15
004505A8  0F 87 DD 00 00 00               ja 0x14045068b
004505AE  48 8B F1                        mov rsi, rcx
004505B1  48 8B CA                        mov rcx, rdx
004505B4  F3 A4                           rep movsb byte ptr [rdi], byte ptr [rsi]
004505B6  49 8B F8                        mov rdi, r8
004505B9  EB 8F                           jmp 0x14045054a
004505BB  85 C0                           test eax, eax
004505BD  78 35                           js 0x1404505f4
004505BF  03 C0                           add eax, eax
004505C1  49 8D 72 02                     lea rsi, [r10 + 2]
004505C5  48 3B F3                        cmp rsi, rbx
004505C8  0F 87 BD 00 00 00               ja 0x14045068b
004505CE  48 8D 57 02                     lea rdx, [rdi + 2]
004505D2  49 3B D7                        cmp rdx, r15
004505D5  0F 87 B0 00 00 00               ja 0x14045068b
004505DB  41 0F B7 0A                     movzx ecx, word ptr [r10]
004505DF  4C 8B D6                        mov r10, rsi
004505E2  66 89 0F                        mov word ptr [rdi], cx
004505E5  48 8B FA                        mov rdi, rdx
004505E8  85 C0                           test eax, eax
004505EA  0F 88 62 FF FF FF               js 0x140450552
004505F0  03 C0                           add eax, eax
004505F2  EB C7                           jmp 0x1404505bb
004505F4  4C 3B D3                        cmp r10, rbx
004505F7  0F 83 8E 00 00 00               jae 0x14045068b
004505FD  49 3B FF                        cmp rdi, r15
00450600  0F 83 85 00 00 00               jae 0x14045068b
00450606  41 0F B6 0A                     movzx ecx, byte ptr [r10]
0045060A  88 0F                           mov byte ptr [rdi], cl
0045060C  48 FF C7                        inc rdi
0045060F  49 FF C2                        inc r10
00450612  E9 3B FF FF FF                  jmp 0x140450552
00450617  4D 85 E4                        test r12, r12
0045061A  74 3F                           je 0x14045065b
0045061C  41 0F B6 14 24                  movzx edx, byte ptr [r12]
00450621  48 C1 EA 04                     shr rdx, 4
00450625  45 33 E4                        xor r12d, r12d
00450628  48 83 FA 0F                     cmp rdx, 0xf
0045062C  74 42                           je 0x140450670
0045062E  48 83 C2 07                     add rdx, 7
00450632  E9 57 FF FF FF                  jmp 0x14045058e
00450637  49 8D 42 03                     lea rax, [r10 + 3]
0045063B  48 3B C3                        cmp rax, rbx
0045063E  73 4B                           jae 0x14045068b
00450640  41 8B 0A                        mov ecx, dword ptr [r10]
00450643  49 83 C2 04                     add r10, 4
00450647  8D 04 4D 01 00 00 00            lea eax, [rcx*2 + 1]
0045064E  85 C9                           test ecx, ecx
00450650  0F 88 04 FF FF FF               js 0x14045055a
00450656  E9 60 FF FF FF                  jmp 0x1404505bb
0045065B  4C 3B D3                        cmp r10, rbx
0045065E  73 2B                           jae 0x14045068b
00450660  4D 8B E2                        mov r12, r10
00450663  49 FF C2                        inc r10
00450666  41 0F B6 14 24                  movzx edx, byte ptr [r12]
0045066B  83 E2 0F                        and edx, 0xf
0045066E  EB B8                           jmp 0x140450628
00450670  4C 3B D3                        cmp r10, rbx
00450673  73 16                           jae 0x14045068b
00450675  41 0F B6 12                     movzx edx, byte ptr [r10]
00450679  49 FF C2                        inc r10
0045067C  48 81 FA FF 00 00 00            cmp rdx, 0xff
00450683  74 35                           je 0x1404506ba
00450685  48 83 C2 0F                     add rdx, 0xf
00450689  EB A3                           jmp 0x14045062e
0045068B  B8 42 02 00 C0                  mov eax, 0xc0000242
00450690  48 8B 5C 24 20                  mov rbx, qword ptr [rsp + 0x20]
00450695  48 8B 6C 24 28                  mov rbp, qword ptr [rsp + 0x28]
0045069A  48 8B 74 24 30                  mov rsi, qword ptr [rsp + 0x30]
0045069F  48 8B 7C 24 38                  mov rdi, qword ptr [rsp + 0x38]
004506A4  41 5F                           pop r15
004506A6  41 5E                           pop r14
004506A8  41 5C                           pop r12
004506AA  C3                              ret
004506AB  CC                              int3
004506AC  48 8B 44 24 48                  mov rax, qword ptr [rsp + 0x48]
004506B1  41 2B FB                        sub edi, r11d
004506B4  89 38                           mov dword ptr [rax], edi
004506B6  33 C0                           xor eax, eax
004506B8  EB D6                           jmp 0x140450690
004506BA  49 8D 4A 01                     lea rcx, [r10 + 1]
004506BE  48 3B CB                        cmp rcx, rbx
004506C1  73 C8                           jae 0x14045068b
004506C3  41 0F B7 12                     movzx edx, word ptr [r10]
004506C7  49 83 C2 02                     add r10, 2
004506CB  48 85 D2                        test rdx, rdx
004506CE  74 59                           je 0x140450729
004506D0  48 83 FA 16                     cmp rdx, 0x16
004506D4  72 B5                           jb 0x14045068b
004506D6  48 8D 4F 03                     lea rcx, [rdi + 3]
004506DA  48 03 CA                        add rcx, rdx
004506DD  48 3B CF                        cmp rcx, rdi
004506E0  72 A9                           jb 0x14045068b
004506E2  48 83 EA 16                     sub rdx, 0x16
004506E6  EB 9D                           jmp 0x140450685
004506E8  41 0F B6 48 02                  movzx ecx, byte ptr [r8 + 2]
004506ED  E9 28 FE FF FF                  jmp 0x14045051a
004506F2  41 0F B7 12                     movzx edx, word ptr [r10]
004506F6  49 83 C2 02                     add r10, 2
004506FA  48 85 D2                        test rdx, rdx
004506FD  75 07                           jne 0x140450706
004506FF  41 8B 12                        mov edx, dword ptr [r10]
00450702  49 83 C2 04                     add r10, 4
00450706  48 83 FA 16                     cmp rdx, 0x16
0045070A  0F 82 7B FF FF FF               jb 0x14045068b
00450710  48 8D 4F 03                     lea rcx, [rdi + 3]
00450714  48 03 CA                        add rcx, rdx
00450717  48 3B CF                        cmp rcx, rdi
0045071A  0F 82 6B FF FF FF               jb 0x14045068b
00450720  48 83 EA 16                     sub rdx, 0x16
00450724  E9 B7 FD FF FF                  jmp 0x1404504e0
00450729  49 8D 4A 03                     lea rcx, [r10 + 3]
0045072D  48 3B CB                        cmp rcx, rbx
00450730  0F 83 55 FF FF FF               jae 0x14045068b
00450736  41 8B 12                        mov edx, dword ptr [r10]
00450739  49 83 C2 04                     add r10, 4
0045073D  EB 91                           jmp 0x1404506d0
0045073F  49 3B FF                        cmp rdi, r15
00450742  0F 82 43 FF FF FF               jb 0x14045068b
00450748  E9 5F FF FF FF                  jmp 0x1404506ac
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlDecompressBufferXpressLz(__int64 a1, int a2, __int64 a3, int a4, __int64 a5, __int64 a6)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_stack_p20 = v_rdi;
    if (a4 < 5) goto loc_0045068B;
    v_rbx = ((unsigned int)(a4)) + (a3);
    v_r15 = ((unsigned int)(a2)) + (a1);
    v_r12 = 0;
loc_00450380:
    v_r10 = (a3) + (4);
    if (v_r10 >= (v_rbx - 86)) goto loc_00450647;
    if (a1 >= (v_r15 - 368)) goto loc_00450647;
    if (sign_flag) goto loc_004503B6;
    goto loc_0045040B;
loc_004503A6:
    *(unsigned __int8 *)(a1) = (unsigned __int8)(*(unsigned __int8 *)(v_r10));
    v_rdi = (a1) + 1;
    v_r10 = (v_r10) + 1;
loc_004503B2:
    result = (unsigned int)(((unsigned int)(*(unsigned int *)(a3)) * 2 + 1) + ((unsigned int)((unsigned int)(*(unsigned int *)(a3)) * 2 + 1)));
    if (condition_is_equal) goto loc_00450380;
loc_004503B6:
    v_r10 = (v_r10) + (2);
    v_rsi = (*(unsigned __int16 *)(v_r10)) >> (3);
    v_rsi = (v_rsi) + 1;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r10)))) & (7));
    if (a2 == 7) goto loc_0045042E;
loc_004503D0:
    a3 = (v_rdi) - (v_rsi);
    a2 = (a2) + (3);
    if (a3 < a1) goto loc_0045068B;
    if (v_rsi < 4) goto loc_004504E9;
loc_004503F0:
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)));
    if (a2 >= 9) goto loc_0045044B;
loc_00450402:
    v_rdi = (v_rdi) + (a2);
loc_00450405:
    if (sign_flag) goto loc_004503B2;
loc_00450409:
    result = (unsigned int)((result) + ((unsigned int)(result)));
loc_0045040B:
    if (sign_flag) goto loc_004503A6;
    result = (unsigned int)((result) + ((unsigned int)(result)));
    if (sign_flag) goto loc_0045048E;
    result = (unsigned int)((result) + ((unsigned int)(result)));
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(v_r10)));
    if (sign_flag) goto loc_004504A2;
    v_rdi = (v_rdi) + (4);
    v_r10 = (v_r10) + (4);
    result = (unsigned int)((result) + ((unsigned int)(result)));
    if (sign_flag) goto loc_004503B2;
    goto loc_00450409;
loc_0045042E:
    if (0 == 0) goto loc_004504AF;
    a2 = (*(unsigned __int8 *)(v_r12)) >> (4);
    v_r12 = 0;
loc_0045043F:
    if (a2 == 15) goto loc_004504BF;
loc_00450445:
    a2 = (a2) + (7);
    goto loc_004503D0;
loc_0045044B:
    v_rdi = (v_rdi) + (8);
    a3 = (a3) + (8);
    a2 = (a2) - (8);
loc_00450457:
    if (v_rdi >= (v_r15 - 368)) goto loc_00450532;
    *(unsigned int *)(v_rdi) = (unsigned int)((unsigned int)(*(unsigned int *)(a3)));
    *(unsigned int *)(v_rdi + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 4)));
    *(unsigned int *)(v_rdi + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 8)));
    *(unsigned int *)(v_rdi + 12) = (unsigned int)((unsigned int)(*(unsigned int *)(a3 + 12)));
    if (a2 < 17) goto loc_00450402;
    v_rdi = (v_rdi) + (16);
    a3 = (a3) + (16);
    a2 = (a2) - (16);
    goto loc_00450457;
loc_0045048E:
    *(unsigned __int16 *)(v_rdi) = (unsigned __int16)(*(unsigned __int16 *)(v_r10));
    v_rdi = (v_rdi) + (2);
    v_r10 = (v_r10) + (2);
    goto loc_004503B2;
loc_004504A2:
    v_rdi = (v_rdi) + (3);
    v_r10 = (v_r10) + (3);
    goto loc_004503B2;
loc_004504AF:
    v_r10 = (v_r10) + 1;
    a2 = (unsigned int)((*(unsigned __int8 *)(v_r10)) & (15));
    goto loc_0045043F;
loc_004504BF:
    if ((v_r10 + 7) >= (v_rbx - 86)) goto loc_00450670;
    v_r10 = (v_r10) + 1;
    if ((*(unsigned __int8 *)(v_r10)) == 255) goto loc_004506F2;
loc_004504E0:
    a2 = (*(unsigned __int8 *)(v_r10)) + (15);
    goto loc_00450445;
loc_004504E9:
    *(unsigned __int8 *)(v_rdi) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    if (v_rsi == 1) goto loc_0045050F;
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(a3 + 1));
    if (v_rsi != 2) goto loc_004506E8;
    a2 = (a2) - (v_rsi);
    v_rdi = (v_rdi) + (v_rsi);
    goto loc_00450524;
loc_0045050F:
    *(unsigned __int8 *)(v_rdi + 1) = (unsigned __int8)(*(unsigned __int8 *)(a3));
loc_0045051A:
    *(unsigned __int8 *)(v_rdi + 2) = (unsigned __int8)(*(unsigned __int8 *)(a3));
    v_rdi = (v_rdi) + (3);
loc_00450524:
    if (a2 == 0) goto loc_00450405;
    goto loc_004503F0;
loc_00450532:
    if ((a2 + v_rdi * 1) > v_r15) goto loc_0045068B;
loc_0045054A:
    if (!sign_flag) goto loc_004505F0;
loc_00450552:
    result = (unsigned int)((result) + ((unsigned int)(result)));
    if (condition_is_equal) goto loc_00450637;
loc_0045055A:
    if (v_r10 == v_rbx) goto loc_004506AC;
    if ((v_r10 + 1) >= v_rbx) goto loc_0045073F;
    v_r10 = (v_r10) + (2);
    v_rsi = (*(unsigned __int16 *)(v_r10)) >> (3);
    v_rsi = (v_rsi) + 1;
    a2 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int16 *)(v_r10)))) & (7));
    if (a2 == 7) goto loc_00450617;
loc_0045058E:
    a2 = (a2) + (3);
    a1 = (a2 + v_rdi * 1) - (v_rsi);
    if (a1 < a1) goto loc_0045068B;
    if ((a2 + a2 + v_rdi * 1 * 1) > v_r15) goto loc_0045068B;
    goto loc_0045054A;
loc_004505BB:
    if (sign_flag) goto loc_004505F4;
    result = (unsigned int)((result) + ((unsigned int)(result)));
    if ((v_r10 + 2) > v_rbx) goto loc_0045068B;
    if ((a2 + a2 + v_rdi * 1 * 1 + 2) > v_r15) goto loc_0045068B;
    *(unsigned __int16 *)(a2 + a2 + v_rdi * 1 * 1) = (unsigned __int16)(*(unsigned __int16 *)(v_r10));
    if (sign_flag) goto loc_00450552;
loc_004505F0:
    result = (unsigned int)((result) + ((unsigned int)(result)));
    goto loc_004505BB;
loc_004505F4:
    if ((v_r10 + 2) >= v_rbx) goto loc_0045068B;
    if ((a2 + a2 + v_rdi * 1 * 1 + 2) >= v_r15) goto loc_0045068B;
    *(unsigned __int8 *)(a2 + a2 + v_rdi * 1 * 1 + 2) = (unsigned __int8)(*(unsigned __int8 *)(v_r10 + 2));
    v_rdi = (a2 + a2 + v_rdi * 1 * 1 + 2) + 1;
    v_r10 = (v_r10 + 2) + 1;
    goto loc_00450552;
loc_00450617:
    if (v_r10 == 0) goto loc_0045065B;
    a2 = (*(unsigned __int8 *)(v_r10)) >> (4);
    v_r12 = 0;
loc_00450628:
    if (a2 == 15) goto loc_00450670;
loc_0045062E:
    a2 = (a2) + (7);
    goto loc_0045058E;
loc_00450637:
    if ((v_r10 + 3) >= v_rbx) goto loc_0045068B;
    v_r10 = (v_r10) + (4);
loc_00450647:
    if (sign_flag) goto loc_0045055A;
    goto loc_004505BB;
loc_0045065B:
    if (v_r10 >= v_rbx) goto loc_0045068B;
    v_r10 = (v_r10) + 1;
    a2 = (unsigned int)((*(unsigned __int8 *)(v_r10)) & (15));
    goto loc_00450628;
loc_00450670:
    if (v_r10 >= v_rbx) goto loc_0045068B;
    v_r10 = (v_r10) + 1;
    if ((*(unsigned __int8 *)(v_r10)) == 255) goto loc_004506BA;
loc_00450685:
    a2 = (*(unsigned __int8 *)(v_r10)) + (15);
    goto loc_0045062E;
loc_0045068B:
loc_00450690:
    return (unsigned int)(0xC0000242ULL);
loc_004506AC:
    v_rdi = (unsigned int)((v_stack_p20) - ((unsigned int)(a1)));
    *(unsigned int *)(a6) = (unsigned int)(v_rdi);
    result = 0;
    goto loc_00450690;
loc_004506BA:
    if ((v_r10 + 1) >= v_stack_p8) goto loc_0045068B;
    v_r10 = (v_r10) + (2);
    if (*(unsigned __int16 *)(v_r10) == 0) goto loc_00450729;
loc_004506D0:
    if ((*(unsigned __int16 *)(v_r10)) < 22) goto loc_0045068B;
    a1 = (v_rdi + 3) + (*(unsigned __int16 *)(v_r10));
    if (a1 < v_rdi) goto loc_0045068B;
    a2 = (*(unsigned __int16 *)(v_r10)) - (22);
    goto loc_00450685;
loc_004506E8:
    goto loc_0045051A;
loc_004506F2:
    v_r10 = (v_r10) + (2);
    if (*(unsigned __int16 *)(v_r10) == 0) {
        a2 = *(unsigned int *)(v_r10);
        v_r10 = (v_r10) + (4);
    }
    if (a2 < 22) goto loc_0045068B;
    a1 = (v_rdi + 3) + (a2);
    if (a1 < v_rdi) goto loc_0045068B;
    a2 = (a2) - (22);
    goto loc_004504E0;
loc_00450729:
    if ((v_r10 + 3) >= v_stack_p8) goto loc_0045068B;
    v_r10 = (v_r10) + (4);
    goto loc_004506D0;
loc_0045073F:
    if (v_rdi < v_r15) goto loc_0045068B;
    goto loc_004506AC;
}
```

## 5. (Beta) C Style

```c
int64_t RtlDecompressBufferXpressLz(int64_t Arg1, void *Arg2, int64_t Arg3, int32_t Arg4, uint64_t Arg5, void *Arg6)
{
    uint8_t *arg2 = (uint8_t *)Arg2;
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    v_stack_p20 = local_rdi;
    if (Arg4 < 5) goto loc_0045068B;
    local_rbx = ((uint32_t)(Arg4)) + (Arg3);
    local_r15 = ((uint32_t)(Arg2)) + (Arg1);
    local_r12 = 0;
loc_00450380:
    local_r10 = (Arg3) + (4);
    if (local_r10 >= (local_rbx - 86)) goto loc_00450647;
    if (Arg1 >= (local_r15 - 368)) goto loc_00450647;
    if (sign_flag) goto loc_004503B6;
    goto loc_0045040B;
loc_004503A6:
    *(uint8_t *)(Arg1) = (uint8_t)(*(uint8_t *)(local_r10));
    local_rdi = (Arg1) + 1;
    local_r10 = (local_r10) + 1;
loc_004503B2:
    result = (uint32_t)(((uint32_t)(*(uint32_t *)(Arg3)) * 2 + 1) + ((uint32_t)((uint32_t)(*(uint32_t *)(Arg3)) * 2 + 1)));
    if (condition_is_equal) goto loc_00450380;
loc_004503B6:
    local_r10 = (local_r10) + (2);
    local_rsi = (*(uint16_t *)(local_r10)) >> (3);
    local_rsi = (local_rsi) + 1;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_r10)))) & (7));
    if (Arg2 == 7) goto loc_0045042E;
loc_004503D0:
    Arg3 = (local_rdi) - (local_rsi);
    Arg2 = (Arg2) + (3);
    if (Arg3 < Arg1) goto loc_0045068B;
    if (local_rsi < 4) goto loc_004504E9;
loc_004503F0:
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3)));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4)));
    if (Arg2 >= 9) goto loc_0045044B;
loc_00450402:
    local_rdi = (local_rdi) + (Arg2);
loc_00450405:
    if (sign_flag) goto loc_004503B2;
loc_00450409:
    result = (uint32_t)((result) + ((uint32_t)(result)));
loc_0045040B:
    if (sign_flag) goto loc_004503A6;
    result = (uint32_t)((result) + ((uint32_t)(result)));
    if (sign_flag) goto loc_0045048E;
    result = (uint32_t)((result) + ((uint32_t)(result)));
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(local_r10)));
    if (sign_flag) goto loc_004504A2;
    local_rdi = (local_rdi) + (4);
    local_r10 = (local_r10) + (4);
    result = (uint32_t)((result) + ((uint32_t)(result)));
    if (sign_flag) goto loc_004503B2;
    goto loc_00450409;
loc_0045042E:
    if (0 == 0) goto loc_004504AF;
    Arg2 = (*(uint8_t *)(local_r12)) >> (4);
    local_r12 = 0;
loc_0045043F:
    if (Arg2 == 15) goto loc_004504BF;
loc_00450445:
    Arg2 = (Arg2) + (7);
    goto loc_004503D0;
loc_0045044B:
    local_rdi = (local_rdi) + (8);
    Arg3 = (Arg3) + (8);
    Arg2 = (Arg2) - (8);
loc_00450457:
    if (local_rdi >= (local_r15 - 368)) goto loc_00450532;
    *(uint32_t *)(local_rdi) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3)));
    *(uint32_t *)(local_rdi + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x4)));
    *(uint32_t *)(local_rdi + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0x8)));
    *(uint32_t *)(local_rdi + 0xC) = (uint32_t)((uint32_t)(*(uint32_t *)(Arg3 + 0xC)));
    if (Arg2 < 17) goto loc_00450402;
    local_rdi = (local_rdi) + (16);
    Arg3 = (Arg3) + (16);
    Arg2 = (Arg2) - (16);
    goto loc_00450457;
loc_0045048E:
    *(uint16_t *)(local_rdi) = (uint16_t)(*(uint16_t *)(local_r10));
    local_rdi = (local_rdi) + (2);
    local_r10 = (local_r10) + (2);
    goto loc_004503B2;
loc_004504A2:
    local_rdi = (local_rdi) + (3);
    local_r10 = (local_r10) + (3);
    goto loc_004503B2;
loc_004504AF:
    local_r10 = (local_r10) + 1;
    Arg2 = (uint32_t)((*(uint8_t *)(local_r10)) & (15));
    goto loc_0045043F;
loc_004504BF:
    if ((local_r10 + 7) >= (local_rbx - 86)) goto loc_00450670;
    local_r10 = (local_r10) + 1;
    if ((*(uint8_t *)(local_r10)) == 255) goto loc_004506F2;
loc_004504E0:
    Arg2 = (*(uint8_t *)(local_r10)) + (15);
    goto loc_00450445;
loc_004504E9:
    *(uint8_t *)(local_rdi) = (uint8_t)(*(uint8_t *)(Arg3));
    if (local_rsi == 1) goto loc_0045050F;
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(Arg3 + 0x1));
    if (local_rsi != 2) goto loc_004506E8;
    Arg2 = (Arg2) - (local_rsi);
    local_rdi = (local_rdi) + (local_rsi);
    goto loc_00450524;
loc_0045050F:
    *(uint8_t *)(local_rdi + 0x1) = (uint8_t)(*(uint8_t *)(Arg3));
loc_0045051A:
    *(uint8_t *)(local_rdi + 0x2) = (uint8_t)(*(uint8_t *)(Arg3));
    local_rdi = (local_rdi) + (3);
loc_00450524:
    if (Arg2 == NULL) goto loc_00450405;
    goto loc_004503F0;
loc_00450532:
    if ((Arg2 + local_rdi * 1) > local_r15) goto loc_0045068B;
loc_0045054A:
    if (!sign_flag) goto loc_004505F0;
loc_00450552:
    result = (uint32_t)((result) + ((uint32_t)(result)));
    if (condition_is_equal) goto loc_00450637;
loc_0045055A:
    if (local_r10 == local_rbx) goto loc_004506AC;
    if ((local_r10 + 1) >= local_rbx) goto loc_0045073F;
    local_r10 = (local_r10) + (2);
    local_rsi = (*(uint16_t *)(local_r10)) >> (3);
    local_rsi = (local_rsi) + 1;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(*(uint16_t *)(local_r10)))) & (7));
    if (Arg2 == 7) goto loc_00450617;
loc_0045058E:
    Arg2 = (Arg2) + (3);
    Arg1 = (Arg2 + local_rdi * 1) - (local_rsi);
    if (Arg1 < Arg1) goto loc_0045068B;
    if ((Arg2 + Arg2 + local_rdi * 1 * 1) > local_r15) goto loc_0045068B;
    goto loc_0045054A;
loc_004505BB:
    if (sign_flag) goto loc_004505F4;
    result = (uint32_t)((result) + ((uint32_t)(result)));
    if ((local_r10 + 2) > local_rbx) goto loc_0045068B;
    if ((Arg2 + Arg2 + local_rdi * 1 * 1 + 2) > local_r15) goto loc_0045068B;
    *(uint16_t *)(arg2 + arg2 + local_rdi * 1 * 1) = (uint16_t)(*(uint16_t *)(local_r10));
    if (sign_flag) goto loc_00450552;
loc_004505F0:
    result = (uint32_t)((result) + ((uint32_t)(result)));
    goto loc_004505BB;
loc_004505F4:
    if ((local_r10 + 2) >= local_rbx) goto loc_0045068B;
    if ((Arg2 + Arg2 + local_rdi * 1 * 1 + 2) >= local_r15) goto loc_0045068B;
    *(uint8_t *)(arg2 + arg2 + local_rdi * 1 * 1 + 0x2) = (uint8_t)(*(uint8_t *)(local_r10 + 0x2));
    local_rdi = (Arg2 + Arg2 + local_rdi * 1 * 1 + 2) + 1;
    local_r10 = (local_r10 + 2) + 1;
    goto loc_00450552;
loc_00450617:
    if (local_r10 == 0) goto loc_0045065B;
    Arg2 = (*(uint8_t *)(local_r10)) >> (4);
    local_r12 = 0;
loc_00450628:
    if (Arg2 == 15) goto loc_00450670;
loc_0045062E:
    Arg2 = (Arg2) + (7);
    goto loc_0045058E;
loc_00450637:
    if ((local_r10 + 3) >= local_rbx) goto loc_0045068B;
    local_r10 = (local_r10) + (4);
loc_00450647:
    if (sign_flag) goto loc_0045055A;
    goto loc_004505BB;
loc_0045065B:
    if (local_r10 >= local_rbx) goto loc_0045068B;
    local_r10 = (local_r10) + 1;
    Arg2 = (uint32_t)((*(uint8_t *)(local_r10)) & (15));
    goto loc_00450628;
loc_00450670:
    if (local_r10 >= local_rbx) goto loc_0045068B;
    local_r10 = (local_r10) + 1;
    if ((*(uint8_t *)(local_r10)) == 255) goto loc_004506BA;
loc_00450685:
    Arg2 = (*(uint8_t *)(local_r10)) + (15);
    goto loc_0045062E;
loc_0045068B:
loc_00450690:
    return (uint32_t)(0xC0000242ULL);
loc_004506AC:
    local_rdi = (uint32_t)((v_stack_p20) - ((uint32_t)(Arg1)));
    *(uint32_t *)(arg6) = (uint32_t)(local_rdi);
    result = 0;
    goto loc_00450690;
loc_004506BA:
    if ((local_r10 + 1) >= v_stack_p8) goto loc_0045068B;
    local_r10 = (local_r10) + (2);
    if (*(uint16_t *)(local_r10) == 0) goto loc_00450729;
loc_004506D0:
    if ((*(uint16_t *)(local_r10)) < 22) goto loc_0045068B;
    Arg1 = (local_rdi + 3) + (*(uint16_t *)(local_r10));
    if (Arg1 < local_rdi) goto loc_0045068B;
    Arg2 = (*(uint16_t *)(local_r10)) - (22);
    goto loc_00450685;
loc_004506E8:
    goto loc_0045051A;
loc_004506F2:
    local_r10 = (local_r10) + (2);
    if (*(uint16_t *)(local_r10) == 0) {
        Arg2 = *(uint32_t *)(local_r10);
        local_r10 = (local_r10) + (4);
    }
    if (Arg2 < 22) goto loc_0045068B;
    Arg1 = (local_rdi + 3) + (Arg2);
    if (Arg1 < local_rdi) goto loc_0045068B;
    Arg2 = (Arg2) - (22);
    goto loc_004504E0;
loc_00450729:
    if ((local_r10 + 3) >= v_stack_p8) goto loc_0045068B;
    local_r10 = (local_r10) + (4);
    goto loc_004506D0;
loc_0045073F:
    if (local_rdi < local_r15) goto loc_0045068B;
    goto loc_004506AC;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `- 0x170` | `64` | `R` |
| `Arg6` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00450330&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
