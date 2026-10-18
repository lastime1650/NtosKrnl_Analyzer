# MiCaptureImageCfgContext

- RVA: `0x009414E0`–`0x009418E3` (길이 `1,027` bytes)
- VA: `0x00000001409414E0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009027C`
- 디코드: `246`개 명령, `1,027/1,027` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0094166F` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (function, `0x0035B540`)
- `0x00941694` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x009416EE` → [MiLogRelocationRva](MiLogRelocationRva_function_009420DC.md) (function, `0x009420DC`)
- `0x00941861` → [MiFreeImageCfgContext](../../text/49/MiFreeImageCfgContext_function_0049BEA4.md) (function, `0x0049BEA4`)

### Direct callers
- [MiParseImageLoadConfig](MiParseImageLoadConfig_function_00940D18.md) at `0x00941023`

### Static image references
- `0x009415F5` → RVA `0x00E2D828` (`.data`; write)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **3**
  - `0x0094166F` → [MiAllocatePool](../../text/35/MiAllocatePool_function_0035B540.md) (`PAGE` → `.text`)
  - `0x00941694` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x00941861` → [MiFreeImageCfgContext](../../text/49/MiFreeImageCfgContext_function_0049BEA4.md) (`PAGE` → `.text`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
009414E0  48 8B C4                        mov rax, rsp
009414E3  4C 89 48 20                     mov qword ptr [rax + 0x20], r9
009414E7  4C 89 40 18                     mov qword ptr [rax + 0x18], r8
009414EB  48 89 50 10                     mov qword ptr [rax + 0x10], rdx
009414EF  48 89 48 08                     mov qword ptr [rax + 8], rcx
009414F3  53                              push rbx
009414F4  56                              push rsi
009414F5  57                              push rdi
009414F6  41 54                           push r12
009414F8  41 55                           push r13
009414FA  41 56                           push r14
009414FC  41 57                           push r15
009414FE  48 83 EC 60                     sub rsp, 0x60
00941502  4D 8B D9                        mov r11, r9
00941505  33 DB                           xor ebx, ebx
00941507  48 8B 84 24 E0 00 00 00         mov rax, qword ptr [rsp + 0xe0]
0094150F  21 18                           and dword ptr [rax], ebx
00941511  0F 57 C0                        xorps xmm0, xmm0
00941514  4C 8B A4 24 E8 00 00 00         mov r12, qword ptr [rsp + 0xe8]
0094151C  41 0F 11 04 24                  movups xmmword ptr [r12], xmm0
00941521  41 0F 11 44 24 10               movups xmmword ptr [r12 + 0x10], xmm0
00941527  45 33 C9                        xor r9d, r9d
0094152A  45 33 C0                        xor r8d, r8d
0094152D  B9 0B 02 00 00                  mov ecx, 0x20b
00941532  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
0094153A  66 39 48 30                     cmp word ptr [rax + 0x30], cx
0094153E  48 8B 84 24 D0 00 00 00         mov rax, qword ptr [rsp + 0xd0]
00941546  B9 00 40 00 00                  mov ecx, 0x4000
0094154B  0F 85 83 02 00 00               jne 0x1409417d4
00941551  4C 8B B8 80 00 00 00            mov r15, qword ptr [rax + 0x80]
00941558  44 8B A8 88 00 00 00            mov r13d, dword ptr [rax + 0x88]
0094155F  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
00941564  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
00941569  8B B8 90 00 00 00               mov edi, dword ptr [rax + 0x90]
0094156F  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
00941573  85 F9                           test ecx, edi
00941575  74 1B                           je 0x140941592
00941577  81 BC 24 D8 00 00 00 B0 00 00 00  cmp dword ptr [rsp + 0xd8], 0xb0
00941582  72 0E                           jb 0x140941592
00941584  4C 8B 88 A0 00 00 00            mov r9, qword ptr [rax + 0xa0]
0094158B  44 8B 80 A8 00 00 00            mov r8d, dword ptr [rax + 0xa8]
00941592  4C 8B 70 78                     mov r14, qword ptr [rax + 0x78]
00941596  4C 89 74 24 40                  mov qword ptr [rsp + 0x40], r14
0094159B  0F BA E7 0A                     bt edi, 0xa
0094159F  73 63                           jae 0x140941604
009415A1  4D 85 FF                        test r15, r15
009415A4  74 5E                           je 0x140941604
009415A6  44 8B D7                        mov r10d, edi
009415A9  41 C1 EA 1C                     shr r10d, 0x1c
009415AD  41 83 C2 04                     add r10d, 4
009415B1  44 89 54 24 2C                  mov dword ptr [rsp + 0x2c], r10d
009415B6  4D 3B FB                        cmp r15, r11
009415B9  0F 82 15 03 00 00               jb 0x1409418d4
009415BF  45 85 ED                        test r13d, r13d
009415C2  0F 84 0C 03 00 00               je 0x1409418d4
009415C8  33 D2                           xor edx, edx
009415CA  83 C8 FF                        or eax, 0xffffffff
009415CD  41 F7 F2                        div r10d
009415D0  44 3B E8                        cmp r13d, eax
009415D3  0F 83 FB 02 00 00               jae 0x1409418d4
009415D9  8B D7                           mov edx, edi
009415DB  23 D1                           and edx, ecx
009415DD  89 54 24 30                     mov dword ptr [rsp + 0x30], edx
009415E1  89 54 24 38                     mov dword ptr [rsp + 0x38], edx
009415E5  74 38                           je 0x14094161f
009415E7  4D 85 C9                        test r9, r9
009415EA  74 33                           je 0x14094161f
009415EC  4D 3B CB                        cmp r9, r11
009415EF  0F 83 05 02 00 00               jae 0x1409417fa
009415F5  C7 05 29 C2 4E 00 0A 00 00 00   mov dword ptr [rip + 0x4ec229], 0xa
009415FF  BB 05 00 00 C0                  mov ebx, 0xc0000005
00941604  85 DB                           test ebx, ebx
00941606  0F 88 52 02 00 00               js 0x14094185e
0094160C  8B C3                           mov eax, ebx
0094160E  48 83 C4 60                     add rsp, 0x60
00941612  41 5F                           pop r15
00941614  41 5E                           pop r14
00941616  41 5D                           pop r13
00941618  41 5C                           pop r12
0094161A  5F                              pop rdi
0094161B  5E                              pop rsi
0094161C  5B                              pop rbx
0094161D  C3                              ret
0094161E  CC                              int3
0094161F  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
00941627  4D 2B FB                        sub r15, r11
0094162A  4C 89 7C 24 48                  mov qword ptr [rsp + 0x48], r15
0094162F  41 8B F2                        mov esi, r10d
00941632  41 0F AF F5                     imul esi, r13d
00941636  89 74 24 34                     mov dword ptr [rsp + 0x34], esi
0094163A  44 8B EE                        mov r13d, esi
0094163D  49 8D 0C 37                     lea rcx, [r15 + rsi]
00941641  49 3B CF                        cmp rcx, r15
00941644  0F 86 7B 02 00 00               jbe 0x1409418c5
0094164A  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
0094164D  48 3B C8                        cmp rcx, rax
00941650  0F 87 6F 02 00 00               ja 0x1409418c5
00941656  8D 46 04                        lea eax, [rsi + 4]
00941659  3B C6                           cmp eax, esi
0094165B  0F 82 64 02 00 00               jb 0x1409418c5
00941661  41 B8 4D 69 43 54               mov r8d, 0x5443694d
00941667  41 8B D5                        mov edx, r13d
0094166A  B9 00 01 00 00                  mov ecx, 0x100
0094166F  E8 CC 9E A1 FF                  call 0x14035b540
00941674  48 89 44 24 50                  mov qword ptr [rsp + 0x50], rax
00941679  48 85 C0                        test rax, rax
0094167C  0F 84 F8 01 00 00               je 0x14094187a
00941682  48 8B 94 24 B0 00 00 00         mov rdx, qword ptr [rsp + 0xb0]
0094168A  49 8D 14 17                     lea rdx, [r15 + rdx]
0094168E  45 8B C5                        mov r8d, r13d
00941691  48 8B C8                        mov rcx, rax
00941694  E8 A7 51 D8 FF                  call 0x1406c6840
00941699  44 8B 6C 24 2C                  mov r13d, dword ptr [rsp + 0x2c]
0094169E  EB 31                           jmp 0x1409416d1
009416A0  8B D8                           mov ebx, eax
009416A2  4C 8B A4 24 E8 00 00 00         mov r12, qword ptr [rsp + 0xe8]
009416AA  8B 74 24 34                     mov esi, dword ptr [rsp + 0x34]
009416AE  4C 8B 7C 24 48                  mov r15, qword ptr [rsp + 0x48]
009416B3  8B 44 24 24                     mov eax, dword ptr [rsp + 0x24]
009416B7  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
009416BB  8B 7C 24 28                     mov edi, dword ptr [rsp + 0x28]
009416BF  44 8B 6C 24 2C                  mov r13d, dword ptr [rsp + 0x2c]
009416C4  4C 8B 74 24 40                  mov r14, qword ptr [rsp + 0x40]
009416C9  8B 44 24 38                     mov eax, dword ptr [rsp + 0x38]
009416CD  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
009416D1  85 DB                           test ebx, ebx
009416D3  0F 88 B5 01 00 00               js 0x14094188e
009416D9  4C 8B 8C 24 A0 00 00 00         mov r9, qword ptr [rsp + 0xa0]
009416E1  4C 8B 84 24 A8 00 00 00         mov r8, qword ptr [rsp + 0xa8]
009416E9  8B D6                           mov edx, esi
009416EB  41 8B CF                        mov ecx, r15d
009416EE  E8 E9 09 00 00                  call 0x1409420dc
009416F3  45 33 C0                        xor r8d, r8d
009416F6  33 C9                           xor ecx, ecx
009416F8  4C 8B 8C 24 C0 00 00 00         mov r9, qword ptr [rsp + 0xc0]
00941700  4C 8B 54 24 50                  mov r10, qword ptr [rsp + 0x50]
00941705  3B CE                           cmp ecx, esi
00941707  73 2D                           jae 0x140941736
00941709  42 8B 14 11                     mov edx, dword ptr [rcx + r10]
0094170D  49 3B D1                        cmp rdx, r9
00941710  73 15                           jae 0x140941727
00941712  85 C9                           test ecx, ecx
00941714  74 09                           je 0x14094171f
00941716  41 3B D0                        cmp edx, r8d
00941719  0F 82 4C 01 00 00               jb 0x14094186b
0094171F  44 8B C2                        mov r8d, edx
00941722  41 03 CD                        add ecx, r13d
00941725  EB DE                           jmp 0x140941705
00941727  C7 05 F7 C0 4E 00 08 00 00 00   mov dword ptr [rip + 0x4ec0f7], 8
00941731  BB 7B 00 00 C0                  mov ebx, 0xc000007b
00941736  85 DB                           test ebx, ebx
00941738  0F 88 20 01 00 00               js 0x14094185e
0094173E  4D 85 F6                        test r14, r14
00941741  74 26                           je 0x140941769
00941743  48 8B 8C 24 B8 00 00 00         mov rcx, qword ptr [rsp + 0xb8]
0094174B  4C 3B F1                        cmp r14, rcx
0094174E  0F 82 49 01 00 00               jb 0x14094189d
00941754  4A 8D 04 09                     lea rax, [rcx + r9]
00941758  4C 3B F0                        cmp r14, rax
0094175B  0F 83 3C 01 00 00               jae 0x14094189d
00941761  44 2B F1                        sub r14d, ecx
00941764  45 89 74 24 18                  mov dword ptr [r12 + 0x18], r14d
00941769  48 8B 94 24 E0 00 00 00         mov rdx, qword ptr [rsp + 0xe0]
00941771  8B 0A                           mov ecx, dword ptr [rdx]
00941773  83 C9 01                        or ecx, 1
00941776  89 0A                           mov dword ptr [rdx], ecx
00941778  48 8B 84 24 C8 00 00 00         mov rax, qword ptr [rsp + 0xc8]
00941780  66 0F BA 60 3C 0E               bt word ptr [rax + 0x3c], 0xe
00941786  73 05                           jae 0x14094178d
00941788  83 C9 02                        or ecx, 2
0094178B  89 0A                           mov dword ptr [rdx], ecx
0094178D  0F BA E7 0F                     bt edi, 0xf
00941791  0F 82 1A 01 00 00               jb 0x1409418b1
00941797  83 7C 24 30 00                  cmp dword ptr [rsp + 0x30], 0
0094179C  74 05                           je 0x1409417a3
0094179E  83 C9 08                        or ecx, 8
009417A1  89 0A                           mov dword ptr [rdx], ecx
009417A3  0F BA E7 14                     bt edi, 0x14
009417A7  0F 82 0E 01 00 00               jb 0x1409418bb
009417AD  0F BA E7 16                     bt edi, 0x16
009417B1  73 05                           jae 0x1409417b8
009417B3  83 C9 40                        or ecx, 0x40
009417B6  89 0A                           mov dword ptr [rdx], ecx
009417B8  41 89 3C 24                     mov dword ptr [r12], edi
009417BC  4D 89 54 24 08                  mov qword ptr [r12 + 8], r10
009417C1  8B 44 24 20                     mov eax, dword ptr [rsp + 0x20]
009417C5  41 89 44 24 10                  mov dword ptr [r12 + 0x10], eax
009417CA  45 89 6C 24 14                  mov dword ptr [r12 + 0x14], r13d
009417CF  E9 30 FE FF FF                  jmp 0x140941604
009417D4  44 8B 78 50                     mov r15d, dword ptr [rax + 0x50]
009417D8  44 8B 68 54                     mov r13d, dword ptr [rax + 0x54]
009417DC  44 89 6C 24 20                  mov dword ptr [rsp + 0x20], r13d
009417E1  44 89 6C 24 24                  mov dword ptr [rsp + 0x24], r13d
009417E6  8B 78 58                        mov edi, dword ptr [rax + 0x58]
009417E9  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
009417ED  85 F9                           test ecx, edi
009417EF  75 59                           jne 0x14094184a
009417F1  44 8B 70 4C                     mov r14d, dword ptr [rax + 0x4c]
009417F5  E9 9C FD FF FF                  jmp 0x140941596
009417FA  45 85 C0                        test r8d, r8d
009417FD  0F 84 F2 FD FF FF               je 0x1409415f5
00941803  44 3B C0                        cmp r8d, eax
00941806  0F 83 E9 FD FF FF               jae 0x1409415f5
0094180C  4D 2B CB                        sub r9, r11
0094180F  45 0F AF C2                     imul r8d, r10d
00941813  41 8B C8                        mov ecx, r8d
00941816  49 03 C9                        add rcx, r9
00941819  49 3B C9                        cmp rcx, r9
0094181C  76 1D                           jbe 0x14094183b
0094181E  48 8B 94 24 C8 00 00 00         mov rdx, qword ptr [rsp + 0xc8]
00941826  8B 42 10                        mov eax, dword ptr [rdx + 0x10]
00941829  48 3B C8                        cmp rcx, rax
0094182C  77 0D                           ja 0x14094183b
0094182E  41 8D 40 04                     lea eax, [r8 + 4]
00941832  41 3B C0                        cmp eax, r8d
00941835  0F 83 EC FD FF FF               jae 0x140941627
0094183B  C7 05 E3 BF 4E 00 0B 00 00 00   mov dword ptr [rip + 0x4ebfe3], 0xb
00941845  E9 B5 FD FF FF                  jmp 0x1409415ff
0094184A  83 BC 24 D8 00 00 00 70         cmp dword ptr [rsp + 0xd8], 0x70
00941852  72 9D                           jb 0x1409417f1
00941854  44 8B 48 68                     mov r9d, dword ptr [rax + 0x68]
00941858  44 8B 40 6C                     mov r8d, dword ptr [rax + 0x6c]
0094185C  EB 93                           jmp 0x1409417f1
0094185E  49 8B CC                        mov rcx, r12
00941861  E8 3E A6 B5 FF                  call 0x14049bea4
00941866  E9 A1 FD FF FF                  jmp 0x14094160c
0094186B  C7 05 B3 BF 4E 00 09 00 00 00   mov dword ptr [rip + 0x4ebfb3], 9
00941875  E9 B7 FE FF FF                  jmp 0x140941731
0094187A  BB 9A 00 00 C0                  mov ebx, 0xc000009a
0094187F  C7 05 9F BF 4E 00 06 00 00 00   mov dword ptr [rip + 0x4ebf9f], 6
00941889  E9 76 FD FF FF                  jmp 0x140941604
0094188E  C7 05 90 BF 4E 00 07 00 00 00   mov dword ptr [rip + 0x4ebf90], 7
00941898  E9 67 FD FF FF                  jmp 0x140941604
0094189D  BB 7B 00 00 C0                  mov ebx, 0xc000007b
009418A2  C7 05 7C BF 4E 00 0A 00 00 00   mov dword ptr [rip + 0x4ebf7c], 0xa
009418AC  E9 53 FD FF FF                  jmp 0x140941604
009418B1  83 C9 10                        or ecx, 0x10
009418B4  89 0A                           mov dword ptr [rdx], ecx
009418B6  E9 DC FE FF FF                  jmp 0x140941797
009418BB  83 C9 20                        or ecx, 0x20
009418BE  89 0A                           mov dword ptr [rdx], ecx
009418C0  E9 E8 FE FF FF                  jmp 0x1409417ad
009418C5  C7 05 59 BF 4E 00 05 00 00 00   mov dword ptr [rip + 0x4ebf59], 5
009418CF  E9 2B FD FF FF                  jmp 0x1409415ff
009418D4  C7 05 4A BF 4E 00 04 00 00 00   mov dword ptr [rip + 0x4ebf4a], 4
009418DE  E9 1C FD FF FF                  jmp 0x1409415ff
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiCaptureImageCfgContext(__int64 a1, __int64 a2, __int64 a3, __int64 a4, __int64 a5, __int64 a6, __int64 a7, unsigned int a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m60;
    unsigned int v_stack_m68;
    unsigned int v_stack_m6C;
    unsigned int v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned int v_stack_p20;
    unsigned int v_stack_p24;
    unsigned int v_stack_p28;
    unsigned int v_stack_p2C;
    unsigned int v_stack_p30;
    unsigned int v_stack_p34;
    unsigned int v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned __int64 v_stack_p48;
    unsigned __int64 v_stack_p50;
    unsigned __int64 v_stack_pA0;
    unsigned __int64 v_stack_pA8;
    unsigned __int64 v_stack_pB0;
    unsigned __int64 v_stack_pB8;
    unsigned __int64 v_stack_pE8;

    *(unsigned __int64 *)(v_rsp + 32) = a4;
    *(unsigned __int64 *)(v_rsp + 24) = a3;
    *(unsigned __int64 *)(v_rsp + 16) = a2;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_rbx = 0;
    *(unsigned __int64 *)(a10) = v_xmm0;
    *(unsigned __int64 *)(a10 + 16) = v_xmm0;
    a4 = 0;
    a3 = 0;
    if ((*(unsigned __int16 *)(a6 + 48)) != 523) goto loc_009417D4;
    v_stack_m78 = (unsigned int)((unsigned int)(*(unsigned int *)(a7 + 136)));
    v_stack_m74 = (unsigned int)((unsigned int)(*(unsigned int *)(a7 + 136)));
    v_stack_m70 = (unsigned int)((unsigned int)(*(unsigned int *)(a7 + 144)));
    if ((((unsigned int)((unsigned int)(0x4000ULL))) & ((unsigned int)((unsigned int)(*(unsigned int *)(a7 + 144))))) == 0) goto loc_00941592;
    if (a8 >= 176) {
        a4 = *(unsigned __int64 *)(a7 + 160);
        a3 = *(unsigned int *)(a7 + 168);
    }
loc_00941596:
    v_stack_m58 = *(unsigned __int64 *)(a7 + 120);
    if (a8 >= 176) goto loc_00941604;
    if (*(unsigned __int64 *)(a7 + 128) == 0) goto loc_00941604;
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a7 + 144))))) >> (28));
    v_r10 = (unsigned int)((v_r10) + (4));
    v_stack_m6C = (unsigned int)(v_r10);
    if ((*(unsigned __int64 *)(a7 + 128)) < a4) goto loc_009418D4;
    if ((unsigned int)((unsigned int)(*(unsigned int *)(a7 + 136))) == 0) goto loc_009418D4;
    a2 = 0;
    result = (unsigned int)((a7) | (0xFFFFFFFFULL));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a7 + 136)))) >= ((unsigned int)(result))) goto loc_009418D4;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a7 + 144))))) & ((unsigned int)((unsigned int)(0x4000ULL))));
    v_stack_m68 = (unsigned int)(a2);
    v_stack_m60 = (unsigned int)(a2);
    if (condition_is_equal) goto loc_0094161F;
    if (a4 == 0) goto loc_0094161F;
    if (a4 >= a4) goto loc_009417FA;
loc_009415F5:
    *(unsigned int *)(v_rip + 5161513) = 10;
loc_009415FF:
loc_00941604:
    if (sign_flag) goto loc_0094185E;
loc_0094160C:
    v_rsp = (v_rsp) + (96);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000005ULL)));
loc_0094161F:
loc_00941627:
    v_r15 = (*(unsigned __int64 *)(a7 + 128)) - (a4);
    v_stack_p48 = v_r15;
    v_rsi = (unsigned int)(((unsigned int)((unsigned int)(v_r10))) * ((unsigned int)((unsigned int)(*(unsigned int *)(a7 + 136)))));
    v_stack_p34 = (unsigned int)(v_rsi);
    if ((v_r15 + v_rsi * 1) <= v_r15) goto loc_009418C5;
    if ((v_r15 + v_rsi * 1) > ((unsigned int)(*(unsigned int *)(a6 + 16)))) goto loc_009418C5;
    if (((unsigned int)(v_rsi + 4)) < ((unsigned int)(v_rsi))) goto loc_009418C5;
    result = MiAllocatePool(256, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))), (unsigned int)(0x5443694DULL), a4);
    v_stack_p50 = result;
    if (result == 0) goto loc_0094187A;
    result = memcpy(result, v_r15 + v_stack_pB0 * 1, (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))), a4);
    goto loc_009416D1;
loc_009416D1:
    if (sign_flag) goto loc_0094188E;
    result = MiLogRelocationRva((unsigned int)((unsigned int)(v_r15)), (unsigned int)((unsigned int)(v_rsi)), v_stack_pA8, v_stack_pA0);
    a3 = 0;
    a1 = 0;
loc_00941705:
    if (0 >= ((unsigned int)(v_rsi))) goto loc_00941736;
    if (((unsigned int)(*(unsigned int *)(a1 + v_stack_p50 * 1))) >= a5) goto loc_00941727;
    if (0 == 0) goto loc_0094171F;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + v_stack_p50 * 1)))) < 0) goto loc_0094186B;
loc_0094171F:
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned int)(v_stack_p2C))));
    goto loc_00941705;
loc_00941727:
    *(unsigned int *)(v_rip + 5161207) = 8;
loc_00941731:
loc_00941736:
    if (sign_flag) goto loc_0094185E;
    if (*(unsigned __int64 *)(a7 + 120) == 0) goto loc_00941769;
    if ((*(unsigned __int64 *)(a7 + 120)) < v_stack_pB8) goto loc_0094189D;
    if ((*(unsigned __int64 *)(a7 + 120)) >= (v_stack_pB8 + a5 * 1)) goto loc_0094189D;
    v_r14 = (unsigned int)((*(unsigned __int64 *)(a7 + 120)) - ((unsigned int)(v_stack_pB8)));
    *(unsigned int *)(a10 + 24) = (unsigned int)(v_r14);
loc_00941769:
    a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(a9))) | (1));
    *(unsigned int *)(a9) = (unsigned int)(a1);
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (2));
        *(unsigned int *)(a9) = (unsigned int)(a1);
    }
    if (condition_is_below) goto loc_009418B1;
loc_00941797:
    if (v_stack_p30 != 0) {
        a1 = (unsigned int)((a1) | (8));
        *(unsigned int *)(a9) = (unsigned int)(a1);
    }
    if (condition_is_below) goto loc_009418BB;
loc_009417AD:
    if (!(condition_is_above_or_equal)) {
        a1 = (unsigned int)((a1) | (64));
        *(unsigned int *)(a9) = (unsigned int)(a1);
    }
    *(unsigned int *)(a10) = (unsigned int)((unsigned int)(*(unsigned int *)(a7 + 144)));
    *(unsigned __int64 *)(a10 + 8) = v_stack_p50;
    *(unsigned int *)(a10 + 16) = (unsigned int)((unsigned int)(v_stack_p20));
    *(unsigned int *)(a10 + 20) = (unsigned int)((unsigned int)(v_stack_p2C));
    goto loc_00941604;
loc_009417D4:
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p20) + 84)));
    v_stack_p24 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p20) + 84)));
    v_stack_p28 = (unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p20) + 88)));
    if ((((unsigned int)(a1)) & ((unsigned int)((unsigned int)(*(unsigned int *)((unsigned int)(v_stack_p20) + 88))))) != 0) goto loc_0094184A;
loc_009417F1:
    goto loc_00941596;
loc_009417FA:
    if ((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + v_stack_p50 * 1))))) == 0) goto loc_009415F5;
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + v_stack_p50 * 1)))))) >= ((unsigned int)((unsigned int)(v_stack_p20)))) goto loc_009415F5;
    a4 = (a5) - (a4);
    a3 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + v_stack_p50 * 1))))) * ((unsigned int)(v_stack_p50)));
    a1 = ((unsigned int)((unsigned int)(a3))) + (a4);
    if (a1 <= a4) goto loc_0094183B;
    if (a1 > ((unsigned int)(*(unsigned int *)(a6 + 16)))) goto loc_0094183B;
    if (((unsigned int)(a3 + 4)) >= ((unsigned int)(a3))) goto loc_00941627;
loc_0094183B:
    *(unsigned int *)(v_rip + 5160931) = 11;
    goto loc_009415FF;
loc_0094184A:
    if (a8 < 112) goto loc_009417F1;
    goto loc_009417F1;
loc_0094185E:
    result = MiFreeImageCfgContext(a10, a6, (unsigned int)(*(unsigned int *)(a3 + 4 + 108)), (unsigned int)(*(unsigned int *)(a3 + 4 + 104)));
    goto loc_0094160C;
loc_0094186B:
    *(unsigned int *)(v_rip + 5160883) = 9;
    goto loc_00941731;
loc_0094187A:
    *(unsigned int *)(v_rip + 5160863) = 6;
    goto loc_00941604;
loc_0094188E:
    *(unsigned int *)(v_rip + 5160848) = 7;
    goto loc_00941604;
loc_0094189D:
    *(unsigned int *)(v_rip + 5160828) = 10;
    goto loc_00941604;
loc_009418B1:
    a1 = (unsigned int)((a10) | (16));
    *(unsigned int *)(a6) = (unsigned int)(a1);
    goto loc_00941797;
loc_009418BB:
    a1 = (unsigned int)((a1) | (32));
    *(unsigned int *)(a6) = (unsigned int)(a1);
    goto loc_009417AD;
loc_009418C5:
    *(unsigned int *)(v_rip + 5160793) = 5;
    goto loc_009415FF;
loc_009418D4:
    *(unsigned int *)(v_rip + 5160778) = 4;
    goto loc_009415FF;
}
```

## 5. (Beta) C Style

```c
int64_t MiCaptureImageCfgContext(int64_t Arg1, int64_t Arg2, int64_t Arg3, int64_t Arg4, int64_t Arg5, void *Arg6, void *Arg7, uint32_t Arg8, void *Arg9, void *Arg10)
{
    uint8_t *arg6 = (uint8_t *)Arg6;
    uint8_t *arg7 = (uint8_t *)Arg7;
    uint8_t *arg9 = (uint8_t *)Arg9;
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r10;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m58;
    uint32_t v_stack_m60;
    uint32_t v_stack_m68;
    uint32_t v_stack_m6C;
    uint32_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint32_t v_stack_p20;
    uint32_t v_stack_p24;
    uint32_t v_stack_p28;
    uint32_t v_stack_p2C;
    uint32_t v_stack_p30;
    uint32_t v_stack_p34;
    uint32_t v_stack_p38;
    uint64_t v_stack_p40;
    uint64_t v_stack_p48;
    uint64_t v_stack_p50;
    uint64_t v_stack_pA0;
    uint64_t v_stack_pA8;
    uint64_t v_stack_pB0;
    uint64_t v_stack_pB8;
    uint64_t v_stack_pE8;

    *(uint64_t *)(local_rsp + 0x20) = Arg4;
    *(uint64_t *)(local_rsp + 0x18) = Arg3;
    *(uint64_t *)(local_rsp + 0x10) = Arg2;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    local_rbx = 0;
    *(uint64_t *)(arg10) = v_xmm0;
    *(uint64_t *)(arg10 + 0x10) = v_xmm0;
    Arg4 = 0;
    Arg3 = 0;
    if ((*(uint16_t *)(arg6 + 0x30)) != 523) goto loc_009417D4;
    v_stack_m78 = (uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x88)));
    v_stack_m74 = (uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x88)));
    v_stack_m70 = (uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x90)));
    if ((((uint32_t)((uint32_t)(0x4000ULL))) & ((uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x90))))) == 0) goto loc_00941592;
    if (Arg8 >= 176) {
        Arg4 = *(uint64_t *)(arg7 + 0xA0);
        Arg3 = *(uint32_t *)(arg7 + 0xA8);
    }
loc_00941596:
    v_stack_m58 = *(uint64_t *)(arg7 + 0x78);
    if (Arg8 >= 176) goto loc_00941604;
    if (*(uint64_t *)(arg7 + 0x80) == 0) goto loc_00941604;
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x90))))) >> (28));
    local_r10 = (uint32_t)((local_r10) + (4));
    v_stack_m6C = (uint32_t)(local_r10);
    if ((*(uint64_t *)(arg7 + 0x80)) < Arg4) goto loc_009418D4;
    if ((uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x88))) == 0) goto loc_009418D4;
    Arg2 = 0;
    result = (uint32_t)((Arg7) | (0xFFFFFFFFULL));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x88)))) >= ((uint32_t)(result))) goto loc_009418D4;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x90))))) & ((uint32_t)((uint32_t)(0x4000ULL))));
    v_stack_m68 = (uint32_t)(Arg2);
    v_stack_m60 = (uint32_t)(Arg2);
    if (condition_is_equal) goto loc_0094161F;
    if (Arg4 == 0) goto loc_0094161F;
    if (Arg4 >= Arg4) goto loc_009417FA;
loc_009415F5:
    *(uint32_t *)(v_rip + 0x4EC229) = 10;
loc_009415FF:
loc_00941604:
    if (sign_flag) goto loc_0094185E;
loc_0094160C:
    local_rsp = (local_rsp) + (96);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000005ULL)));
loc_0094161F:
loc_00941627:
    local_r15 = (*(uint64_t *)(arg7 + 0x80)) - (Arg4);
    v_stack_p48 = local_r15;
    local_rsi = (uint32_t)(((uint32_t)((uint32_t)(local_r10))) * ((uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x88)))));
    v_stack_p34 = (uint32_t)(local_rsi);
    if ((local_r15 + local_rsi * 1) <= local_r15) goto loc_009418C5;
    if ((local_r15 + local_rsi * 1) > ((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) goto loc_009418C5;
    if (((uint32_t)(local_rsi + 4)) < ((uint32_t)(local_rsi))) goto loc_009418C5;
    result = MiAllocatePool(256, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))), (uint32_t)(0x5443694DULL), Arg4);
    v_stack_p50 = result;
    if (result == 0) goto loc_0094187A;
    result = memcpy(result, local_r15 + v_stack_pB0 * 1, (uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))), Arg4);
    goto loc_009416D1;
loc_009416D1:
    if (sign_flag) goto loc_0094188E;
    result = MiLogRelocationRva((uint32_t)((uint32_t)(local_r15)), (uint32_t)((uint32_t)(local_rsi)), v_stack_pA8, v_stack_pA0);
    Arg3 = 0;
    Arg1 = 0;
loc_00941705:
    if (0 >= ((uint32_t)(local_rsi))) goto loc_00941736;
    if (((uint32_t)(*(uint32_t *)(Arg1 + v_stack_p50 * 1))) >= Arg5) goto loc_00941727;
    if (0 == 0) goto loc_0094171F;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + v_stack_p50 * 1)))) < 0) goto loc_0094186B;
loc_0094171F:
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint32_t)(v_stack_p2C))));
    goto loc_00941705;
loc_00941727:
    *(uint32_t *)(v_rip + 0x4EC0F7) = 8;
loc_00941731:
loc_00941736:
    if (sign_flag) goto loc_0094185E;
    if (*(uint64_t *)(arg7 + 0x78) == 0) goto loc_00941769;
    if ((*(uint64_t *)(arg7 + 0x78)) < v_stack_pB8) goto loc_0094189D;
    if ((*(uint64_t *)(arg7 + 0x78)) >= (v_stack_pB8 + Arg5 * 1)) goto loc_0094189D;
    local_r14 = (uint32_t)((*(uint64_t *)(arg7 + 0x78)) - ((uint32_t)(v_stack_pB8)));
    *(uint32_t *)(arg10 + 0x18) = (uint32_t)(local_r14);
loc_00941769:
    Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg9))) | (1));
    *(uint32_t *)(arg9) = (uint32_t)(Arg1);
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (2));
        *(uint32_t *)(arg9) = (uint32_t)(Arg1);
    }
    if (condition_is_below) goto loc_009418B1;
loc_00941797:
    if (v_stack_p30 != 0) {
        Arg1 = (uint32_t)((Arg1) | (8));
        *(uint32_t *)(arg9) = (uint32_t)(Arg1);
    }
    if (condition_is_below) goto loc_009418BB;
loc_009417AD:
    if (!(condition_is_above_or_equal)) {
        Arg1 = (uint32_t)((Arg1) | (64));
        *(uint32_t *)(arg9) = (uint32_t)(Arg1);
    }
    *(uint32_t *)(arg10) = (uint32_t)((uint32_t)(*(uint32_t *)(arg7 + 0x90)));
    *(uint64_t *)(arg10 + 0x8) = v_stack_p50;
    *(uint32_t *)(arg10 + 0x10) = (uint32_t)((uint32_t)(v_stack_p20));
    *(uint32_t *)(arg10 + 0x14) = (uint32_t)((uint32_t)(v_stack_p2C));
    goto loc_00941604;
loc_009417D4:
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p20) + 0x54)));
    v_stack_p24 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p20) + 0x54)));
    v_stack_p28 = (uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p20) + 0x58)));
    if ((((uint32_t)(Arg1)) & ((uint32_t)((uint32_t)(*(uint32_t *)((uint32_t)(v_stack_p20) + 0x58))))) != 0) goto loc_0094184A;
loc_009417F1:
    goto loc_00941596;
loc_009417FA:
    if ((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + v_stack_p50 * 1))))) == 0) goto loc_009415F5;
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + v_stack_p50 * 1)))))) >= ((uint32_t)((uint32_t)(v_stack_p20)))) goto loc_009415F5;
    Arg4 = (Arg5) - (Arg4);
    Arg3 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + v_stack_p50 * 1))))) * ((uint32_t)(v_stack_p50)));
    Arg1 = ((uint32_t)((uint32_t)(Arg3))) + (Arg4);
    if (Arg1 <= Arg4) goto loc_0094183B;
    if (Arg1 > ((uint32_t)(*(uint32_t *)(arg6 + 0x10)))) goto loc_0094183B;
    if (((uint32_t)(Arg3 + 4)) >= ((uint32_t)(Arg3))) goto loc_00941627;
loc_0094183B:
    *(uint32_t *)(v_rip + 0x4EBFE3) = 11;
    goto loc_009415FF;
loc_0094184A:
    if (Arg8 < 112) goto loc_009417F1;
    goto loc_009417F1;
loc_0094185E:
    result = MiFreeImageCfgContext(Arg10, Arg6, (uint32_t)(*(uint32_t *)(Arg3 + 0x4 + 0x6C)), (uint32_t)(*(uint32_t *)(Arg3 + 0x4 + 0x68)));
    goto loc_0094160C;
loc_0094186B:
    *(uint32_t *)(v_rip + 0x4EBFB3) = 9;
    goto loc_00941731;
loc_0094187A:
    *(uint32_t *)(v_rip + 0x4EBF9F) = 6;
    goto loc_00941604;
loc_0094188E:
    *(uint32_t *)(v_rip + 0x4EBF90) = 7;
    goto loc_00941604;
loc_0094189D:
    *(uint32_t *)(v_rip + 0x4EBF7C) = 10;
    goto loc_00941604;
loc_009418B1:
    Arg1 = (uint32_t)((Arg10) | (16));
    *(uint32_t *)(arg6) = (uint32_t)(Arg1);
    goto loc_00941797;
loc_009418BB:
    Arg1 = (uint32_t)((Arg1) | (32));
    *(uint32_t *)(arg6) = (uint32_t)(Arg1);
    goto loc_009417AD;
loc_009418C5:
    *(uint32_t *)(v_rip + 0x4EBF59) = 5;
    goto loc_009415FF;
loc_009418D4:
    *(uint32_t *)(v_rip + 0x4EBF4A) = 4;
    goto loc_009415FF;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x10` | `32` | `R` |
| `Arg6` | `+ 0x30` | `16` | `R` |
| `Arg6` | `+ 0x3C` | `16` | `R` |
| `Arg7` | `+ 0x4C` | `32` | `R` |
| `Arg7` | `+ 0x50` | `32` | `R` |
| `Arg7` | `+ 0x54` | `32` | `R` |
| `Arg7` | `+ 0x58` | `32` | `R` |
| `Arg7` | `+ 0x68` | `32` | `R` |
| `Arg7` | `+ 0x6C` | `32` | `R` |
| `Arg7` | `+ 0x78` | `64` | `R` |
| `Arg7` | `+ 0x80` | `64` | `R` |
| `Arg7` | `+ 0x88` | `32` | `R` |
| `Arg7` | `+ 0x90` | `32` | `R` |
| `Arg7` | `+ 0xA0` | `64` | `R` |
| `Arg7` | `+ 0xA8` | `32` | `R` |
| `Arg9` | `+ 0x0` | `32` | `R` |
| `Arg9` | `+ 0x0` | `32` | `R/W` |
| `Arg9` | `+ 0x0` | `32` | `W` |
| `Arg10` | `+ 0x0` | `32` | `W` |
| `Arg10` | `+ 0x0` | `128` | `R` |
| `Arg10` | `+ 0x8` | `64` | `W` |
| `Arg10` | `+ 0x10` | `32` | `W` |
| `Arg10` | `+ 0x10` | `128` | `R` |
| `Arg10` | `+ 0x14` | `32` | `W` |
| `Arg10` | `+ 0x18` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x009414E0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
