# LdrResSearchResource

- RVA: `0x0098F7A0`–`0x0098FB18` (길이 `888` bytes)
- VA: `0x000000014098F7A0`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x00098A8C`
- 디코드: `227`개 명령, `888/888` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **10**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0098F8AD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x0098F8F4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (function, `0x006C6840`)
- `0x0098F954` → [LdrpResGetMappingSize](../99/LdrpResGetMappingSize_function_00991614.md) (function, `0x00991614`)
- `0x0098F98F` → [LdrpResSearchResourceMappedFile](../../text/45/LdrpResSearchResourceMappedFile_function_00454C98.md) (function, `0x00454C98`)
- `0x0098FA18` → [DownLevelLangIDToLanguageName](../../text/4B/DownLevelLangIDToLanguageName_function_004BBAA8.md) (function, `0x004BBAA8`)
- `0x0098FAF3` → [DownLevelLanguageNameToLangID](../../text/4C/DownLevelLanguageNameToLangID_function_004C3748.md) (function, `0x004C3748`)

### Direct callers
- [PfSnGetAppVersion](../../text/48/PfSnGetAppVersion_function_0048AD84.md) at `0x0048ADF3`
- [PopValidateWinresume](../75/PopValidateWinresume_function_0075DFF4.md) at `0x0075E1F6`
- [PopValidateWinresume](../75/PopValidateWinresume_function_0075DFF4.md) at `0x0075E2B9`
- [RtlLoadString](../78/RtlLoadString_function_0078C570.md) at `0x0078C6C1`
- [LdrResFindResourceDirectory](../78/LdrResFindResourceDirectory_function_0078C990.md) at `0x0078CA0B`
- [SeRegisterElamCertResources](../79/SeRegisterElamCertResources_function_0079B8C8.md) at `0x0079B934`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FB83`
- [AslpFileGetVersionBlock](../81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FCEE`
- [LdrResFindResource](LdrResFindResource_function_0098E850.md) at `0x0098E8B1`
- [PspLocateInPEManifest](PspLocateInPEManifest_function_0098F568.md) at `0x0098F5D8`
- [PopEtGetProcessVersionInfo](PopEtGetProcessVersionInfo_function_0098F68C.md) at `0x0098F718`
- [KeHwPolicyLocateResource](../../init/C3/KeHwPolicyLocateResource_function_00C38A80.md) at `0x00C38B5A`

### Static image references
- `0x0098F7B3` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **5**
  - `0x0098F8AD` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x0098F8F4` → [memcpy](../../text/6C/memcpy_function_006C6840.md) (`PAGE` → `.text`)
  - `0x0098F98F` → [LdrpResSearchResourceMappedFile](../../text/45/LdrpResSearchResourceMappedFile_function_00454C98.md) (`PAGE` → `.text`)
  - `0x0098FA18` → [DownLevelLangIDToLanguageName](../../text/4B/DownLevelLangIDToLanguageName_function_004BBAA8.md) (`PAGE` → `.text`)
  - `0x0098FAF3` → [DownLevelLanguageNameToLangID](../../text/4C/DownLevelLanguageNameToLangID_function_004C3748.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **1**
  - `0x0098F9B7` → [sub_00B2B9CE](../B2/Unknown_function_00B2B9CE.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
0098F7A0  40 53                           push rbx
0098F7A2  56                              push rsi
0098F7A3  57                              push rdi
0098F7A4  41 54                           push r12
0098F7A6  41 55                           push r13
0098F7A8  41 56                           push r14
0098F7AA  41 57                           push r15
0098F7AC  48 81 EC A0 00 00 00            sub rsp, 0xa0
0098F7B3  48 8B 05 86 AF 47 00            mov rax, qword ptr [rip + 0x47af86]
0098F7BA  48 33 C4                        xor rax, rsp
0098F7BD  48 89 84 24 98 00 00 00         mov qword ptr [rsp + 0x98], rax
0098F7C5  41 8B D8                        mov ebx, r8d
0098F7C8  4C 8B E1                        mov r12, rcx
0098F7CB  48 8B 84 24 00 01 00 00         mov rax, qword ptr [rsp + 0x100]
0098F7D3  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0098F7D8  4C 8B BC 24 08 01 00 00         mov r15, qword ptr [rsp + 0x108]
0098F7E0  4C 8B AC 24 10 01 00 00         mov r13, qword ptr [rsp + 0x110]
0098F7E8  48 8B 84 24 18 01 00 00         mov rax, qword ptr [rsp + 0x118]
0098F7F0  48 89 44 24 70                  mov qword ptr [rsp + 0x70], rax
0098F7F5  45 33 C0                        xor r8d, r8d
0098F7F8  45 8B F0                        mov r14d, r8d
0098F7FB  48 85 C9                        test rcx, rcx
0098F7FE  0F 84 21 02 00 00               je 0x14098fa25
0098F804  48 85 D2                        test rdx, rdx
0098F807  0F 84 18 02 00 00               je 0x14098fa25
0098F80D  4D 85 ED                        test r13, r13
0098F810  0F 85 3C 02 00 00               jne 0x14098fa52
0098F816  41 BA 00 0C 00 00               mov r10d, 0xc00
0098F81C  45 85 CA                        test r10d, r9d
0098F81F  75 7A                           jne 0x14098f89b
0098F821  41 8B C9                        mov ecx, r9d
0098F824  41 BB 00 01 00 00               mov r11d, 0x100
0098F82A  41 0B CB                        or ecx, r11d
0098F82D  41 F7 C1 00 0F 00 00            test r9d, 0xf00
0098F834  41 0F 45 C9                     cmovne ecx, r9d
0098F838  8B F9                           mov edi, ecx
0098F83A  0F BA EF 0C                     bts edi, 0xc
0098F83E  0F BA E1 0D                     bt ecx, 0xd
0098F842  0F 42 F9                        cmovb edi, ecx
0098F845  F7 C7 00 00 F0 FF               test edi, 0xfff00000
0098F84B  75 4E                           jne 0x14098f89b
0098F84D  83 FB 03                        cmp ebx, 3
0098F850  0F 82 06 02 00 00               jb 0x14098fa5c
0098F856  83 FB 04                        cmp ebx, 4
0098F859  0F 87 07 02 00 00               ja 0x14098fa66
0098F85F  8B C7                           mov eax, edi
0098F861  83 E0 41                        and eax, 0x41
0098F864  0F 85 06 02 00 00               jne 0x14098fa70
0098F86A  83 FB 04                        cmp ebx, 4
0098F86D  0F 84 0C 02 00 00               je 0x14098fa7f
0098F873  41 85 FB                        test r11d, edi
0098F876  0F 84 C4 01 00 00               je 0x14098fa40
0098F87C  F7 C7 00 0E 00 00               test edi, 0xe00
0098F882  75 17                           jne 0x14098f89b
0098F884  0F BA E7 0F                     bt edi, 0xf
0098F888  0F 82 11 02 00 00               jb 0x14098fa9f
0098F88E  8B C7                           mov eax, edi
0098F890  B9 00 30 00 00                  mov ecx, 0x3000
0098F895  23 C1                           and eax, ecx
0098F897  3B C1                           cmp eax, ecx
0098F899  75 2B                           jne 0x14098f8c6
0098F89B  BB F2 00 00 C0                  mov ebx, 0xc00000f2
0098F8A0  8B C3                           mov eax, ebx
0098F8A2  48 8B 8C 24 98 00 00 00         mov rcx, qword ptr [rsp + 0x98]
0098F8AA  48 33 CC                        xor rcx, rsp
0098F8AD  E8 8E CD D1 FF                  call 0x1406ac640
0098F8B2  48 81 C4 A0 00 00 00            add rsp, 0xa0
0098F8B9  41 5F                           pop r15
0098F8BB  41 5E                           pop r14
0098F8BD  41 5D                           pop r13
0098F8BF  41 5C                           pop r12
0098F8C1  5F                              pop rdi
0098F8C2  5E                              pop rsi
0098F8C3  5B                              pop rbx
0098F8C4  C3                              ret
0098F8C5  CC                              int3
0098F8C6  8B C7                           mov eax, edi
0098F8C8  83 E0 18                        and eax, 0x18
0098F8CB  3C 18                           cmp al, 0x18
0098F8CD  74 CC                           je 0x14098f89b
0098F8CF  4C 89 44 24 58                  mov qword ptr [rsp + 0x58], r8
0098F8D4  0F BA E7 11                     bt edi, 0x11
0098F8D8  0F 82 D5 01 00 00               jb 0x14098fab3
0098F8DE  0F BA E7 13                     bt edi, 0x13
0098F8E2  0F 82 DD 00 00 00               jb 0x14098f9c5
0098F8E8  4C 8B C3                        mov r8, rbx
0098F8EB  49 C1 E0 03                     shl r8, 3
0098F8EF  48 8D 4C 24 78                  lea rcx, [rsp + 0x78]
0098F8F4  E8 47 6F D3 FF                  call 0x1406c6840
0098F8F9  EB 04                           jmp 0x14098f8ff
0098F8FB  8B D8                           mov ebx, eax
0098F8FD  EB A1                           jmp 0x14098f8a0
0098F8FF  BE 03 00 00 00                  mov esi, 3
0098F904  3B DE                           cmp ebx, esi
0098F906  0F 46 F3                        cmovbe esi, ebx
0098F909  83 FE 03                        cmp esi, 3
0098F90C  75 1E                           jne 0x14098f92c
0098F90E  48 8B 8C 24 88 00 00 00         mov rcx, qword ptr [rsp + 0x88]
0098F916  48 81 F9 00 00 01 00            cmp rcx, 0x10000
0098F91D  0F 83 C6 01 00 00               jae 0x14098fae9
0098F923  48 85 C9                        test rcx, rcx
0098F926  0F 85 D1 00 00 00               jne 0x14098f9fd
0098F92C  8B DF                           mov ebx, edi
0098F92E  81 E3 00 10 00 00               and ebx, 0x1000
0098F934  F7 C7 00 03 00 00               test edi, 0x300
0098F93A  74 21                           je 0x14098f95d
0098F93C  4D 8B F4                        mov r14, r12
0098F93F  0F BA E7 09                     bt edi, 9
0098F943  0F 82 E6 00 00 00               jb 0x14098fa2f
0098F949  44 8B C7                        mov r8d, edi
0098F94C  48 8D 54 24 58                  lea rdx, [rsp + 0x58]
0098F951  49 8B CE                        mov rcx, r14
0098F954  E8 BB 1C 00 00                  call 0x140991614
0098F959  85 C0                           test eax, eax
0098F95B  78 5F                           js 0x14098f9bc
0098F95D  4C 8B 64 24 70                  mov r12, qword ptr [rsp + 0x70]
0098F962  4C 89 64 24 40                  mov qword ptr [rsp + 0x40], r12
0098F967  4C 89 6C 24 38                  mov qword ptr [rsp + 0x38], r13
0098F96C  4C 89 7C 24 30                  mov qword ptr [rsp + 0x30], r15
0098F971  48 8B 44 24 68                  mov rax, qword ptr [rsp + 0x68]
0098F976  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0098F97B  89 74 24 20                     mov dword ptr [rsp + 0x20], esi
0098F97F  4C 8D 4C 24 78                  lea r9, [rsp + 0x78]
0098F984  44 8B C7                        mov r8d, edi
0098F987  48 8B 54 24 58                  mov rdx, qword ptr [rsp + 0x58]
0098F98C  49 8B CE                        mov rcx, r14
0098F98F  E8 04 53 AC FF                  call 0x140454c98
0098F994  8B D8                           mov ebx, eax
0098F996  3D 8A 00 00 C0                  cmp eax, 0xc000008a
0098F99B  0F 85 FF FE FF FF               jne 0x14098f8a0
0098F9A1  48 8B 54 24 78                  mov rdx, qword ptr [rsp + 0x78]
0098F9A6  48 83 C2 F0                     add rdx, -0x10
0098F9AA  48 F7 C2 F7 FF FF FF            test rdx, -9
0098F9B1  0F 84 E9 FE FF FF               je 0x14098f8a0
0098F9B7  E9 12 C0 19 00                  jmp 0x140b2b9ce
0098F9BC  85 DB                           test ebx, ebx
0098F9BE  74 9D                           je 0x14098f95d
0098F9C0  E9 DD FE FF FF                  jmp 0x14098f8a2
0098F9C5  F7 C7 00 03 00 00               test edi, 0x300
0098F9CB  74 17                           je 0x14098f9e4
0098F9CD  4D 85 FF                        test r15, r15
0098F9D0  74 12                           je 0x14098f9e4
0098F9D2  49 8B 07                        mov rax, qword ptr [r15]
0098F9D5  48 85 C0                        test rax, rax
0098F9D8  74 0A                           je 0x14098f9e4
0098F9DA  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0098F9DF  E9 04 FF FF FF                  jmp 0x14098f8e8
0098F9E4  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0098F9E9  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
0098F9ED  E9 AE FE FF FF                  jmp 0x14098f8a0
0098F9F2  8B D8                           mov ebx, eax
0098F9F4  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0098F9F8  E9 A3 FE FF FF                  jmp 0x14098f8a0
0098F9FD  B8 FF 03 00 00                  mov eax, 0x3ff
0098FA02  66 85 C8                        test ax, cx
0098FA05  74 1E                           je 0x14098fa25
0098FA07  48 83 F9 7F                     cmp rcx, 0x7f
0098FA0B  74 18                           je 0x14098fa25
0098FA0D  41 B9 02 00 00 00               mov r9d, 2
0098FA13  45 33 C0                        xor r8d, r8d
0098FA16  33 D2                           xor edx, edx
0098FA18  E8 8B C0 B2 FF                  call 0x1404bbaa8
0098FA1D  85 C0                           test eax, eax
0098FA1F  0F 85 07 FF FF FF               jne 0x14098f92c
0098FA25  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0098FA2A  E9 71 FE FF FF                  jmp 0x14098f8a0
0098FA2F  49 83 CE 01                     or r14, 1
0098FA33  41 F6 C4 01                     test r12b, 1
0098FA37  4D 0F 45 F4                     cmovne r14, r12
0098FA3B  E9 09 FF FF FF                  jmp 0x14098f949
0098FA40  8B C7                           mov eax, edi
0098FA42  41 23 C2                        and eax, r10d
0098FA45  0F BA E7 09                     bt edi, 9
0098FA49  73 46                           jae 0x14098fa91
0098FA4B  85 C0                           test eax, eax
0098FA4D  E9 30 FE FF FF                  jmp 0x14098f882
0098FA52  48 85 C0                        test rax, rax
0098FA55  74 CE                           je 0x14098fa25
0098FA57  E9 BA FD FF FF                  jmp 0x14098f816
0098FA5C  40 F6 C7 02                     test dil, 2
0098FA60  0F 85 F0 FD FF FF               jne 0x14098f856
0098FA66  BB F1 00 00 C0                  mov ebx, 0xc00000f1
0098FA6B  E9 30 FE FF FF                  jmp 0x14098f8a0
0098FA70  83 FB 04                        cmp ebx, 4
0098FA73  74 0A                           je 0x14098fa7f
0098FA75  B8 F1 00 00 C0                  mov eax, 0xc00000f1
0098FA7A  E9 23 FE FF FF                  jmp 0x14098f8a2
0098FA7F  85 C0                           test eax, eax
0098FA81  0F 85 EC FD FF FF               jne 0x14098f873
0098FA87  B8 F2 00 00 C0                  mov eax, 0xc00000f2
0098FA8C  E9 11 FE FF FF                  jmp 0x14098f8a2
0098FA91  41 3B C2                        cmp eax, r10d
0098FA94  0F 84 01 FE FF FF               je 0x14098f89b
0098FA9A  E9 E5 FD FF FF                  jmp 0x14098f884
0098FA9F  8B C7                           mov eax, edi
0098FAA1  F7 D0                           not eax
0098FAA3  A9 10 08 00 00                  test eax, 0x810
0098FAA8  0F 85 ED FD FF FF               jne 0x14098f89b
0098FAAE  E9 DB FD FF FF                  jmp 0x14098f88e
0098FAB3  0F BA E7 0A                     bt edi, 0xa
0098FAB7  73 17                           jae 0x14098fad0
0098FAB9  4D 85 FF                        test r15, r15
0098FABC  74 12                           je 0x14098fad0
0098FABE  49 8B 07                        mov rax, qword ptr [r15]
0098FAC1  48 85 C0                        test rax, rax
0098FAC4  74 0A                           je 0x14098fad0
0098FAC6  48 89 44 24 58                  mov qword ptr [rsp + 0x58], rax
0098FACB  E9 0E FE FF FF                  jmp 0x14098f8de
0098FAD0  BB 0D 00 00 C0                  mov ebx, 0xc000000d
0098FAD5  89 5C 24 50                     mov dword ptr [rsp + 0x50], ebx
0098FAD9  E9 C2 FD FF FF                  jmp 0x14098f8a0
0098FADE  8B D8                           mov ebx, eax
0098FAE0  89 44 24 50                     mov dword ptr [rsp + 0x50], eax
0098FAE4  E9 B7 FD FF FF                  jmp 0x14098f8a0
0098FAE9  33 C0                           xor eax, eax
0098FAEB  66 39 01                        cmp word ptr [rcx], ax
0098FAEE  74 0B                           je 0x14098fafb
0098FAF0  8D 50 02                        lea edx, [rax + 2]
0098FAF3  E8 50 3C B3 FF                  call 0x1404c3748
0098FAF8  0F B7 C0                        movzx eax, ax
0098FAFB  89 44 24 60                     mov dword ptr [rsp + 0x60], eax
0098FAFF  EB 07                           jmp 0x14098fb08
0098FB01  8B D8                           mov ebx, eax
0098FB03  E9 98 FD FF FF                  jmp 0x14098f8a0
0098FB08  0F B7 C0                        movzx eax, ax
0098FB0B  48 89 84 24 88 00 00 00         mov qword ptr [rsp + 0x88], rax
0098FB13  E9 14 FE FF FF                  jmp 0x14098f92c
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall LdrResSearchResource(__int64 a1, __int64 a2, int a3, int a4, __int64 a5, __int64 a6, __int64 a7, __int64 a8)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;
    unsigned __int64 v_stack_p38;
    unsigned __int64 v_stack_p40;
    unsigned int v_stack_p50;
    unsigned __int64 v_stack_p58;
    unsigned int v_stack_p60;
    unsigned __int64 v_stack_p68;
    unsigned __int64 v_stack_p70;
    unsigned __int64 v_stack_p78;
    unsigned __int64 v_stack_p88;

    v_rsp = (v_rsp) - (160);
    result = (*(unsigned __int64 *)(v_rip + 4697990)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m70 = a5;
    v_stack_m68 = a8;
    a3 = 0;
    if (a1 == 0) goto loc_0098FA25;
    if (a2 == 0) goto loc_0098FA25;
    if (a7 != 0) goto loc_0098FA52;
loc_0098F816:
    if ((((unsigned int)((unsigned int)(0xC00ULL))) & (a4)) != 0) goto loc_0098F89B;
    a1 = (unsigned int)(((unsigned int)(a4)) | (256));
    if (((a4) & (0xF00ULL)) != 0) { a1 = a4; }
    v_rdi = (unsigned int)((unsigned int)(a1));
    if (condition_is_below) { v_rdi = (unsigned int)(a1); }
    if ((((unsigned int)(v_rdi)) & (0xFFF00000ULL)) != 0) goto loc_0098F89B;
    if (((unsigned int)((unsigned int)(a3))) < 3) goto loc_0098FA5C;
loc_0098F856:
    if (((unsigned int)((unsigned int)(a3))) > 4) goto loc_0098FA66;
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (65));
    if (condition_is_not_equal) goto loc_0098FA70;
    if (((unsigned int)((unsigned int)(a3))) == 4) goto loc_0098FA7F;
loc_0098F873:
    if (((256) & ((unsigned int)(v_rdi))) == 0) goto loc_0098FA40;
loc_0098F882:
    if ((((unsigned int)(v_rdi)) & (0xE00ULL)) != 0) goto loc_0098F89B;
loc_0098F884:
    if (condition_is_below) goto loc_0098FA9F;
loc_0098F88E:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & ((unsigned int)((unsigned int)(0x3000ULL))));
    if (((unsigned int)(result)) != ((unsigned int)((unsigned int)(0x3000ULL)))) goto loc_0098F8C6;
loc_0098F89B:
loc_0098F8A0:
loc_0098F8A2:
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, a4);
    v_rsp = (v_rsp) + (160);
    return result;
loc_0098F8C6:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (24));
    if (((unsigned __int8)(result)) == 24) goto loc_0098F89B;
    v_stack_p58 = 0;
    if (((unsigned __int8)(result)) < 24) goto loc_0098FAB3;
loc_0098F8DE:
    if (((unsigned __int8)(result)) < 24) goto loc_0098F9C5;
loc_0098F8E8:
    a3 = ((unsigned int)(0xC00000F2ULL)) << (3);
    result = memcpy(v_stack_p78, a2, a3, a4);
    goto loc_0098F8FF;
loc_0098F8FF:
    v_rsi = 3;
    if (((unsigned int)((unsigned int)(0xC00000F2ULL))) <= 3) { v_rsi = (unsigned int)((unsigned int)(0xC00000F2ULL)); }
    if (((unsigned int)(v_rsi)) != 3) goto loc_0098F92C;
    if (v_stack_p88 >= 0x10000ULL) goto loc_0098FAE9;
    if (v_stack_p88 != 0) goto loc_0098F9FD;
loc_0098F92C:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & (0x1000ULL));
    if ((((unsigned int)(v_rdi)) & (768)) == 0) goto loc_0098F95D;
    if (condition_is_below) goto loc_0098FA2F;
loc_0098F949:
    result = LdrpResGetMappingSize(a1, v_stack_p58, (unsigned int)((unsigned int)(v_rdi)), a4);
    if (sign_flag) goto loc_0098F9BC;
loc_0098F95D:
    v_stack_p40 = v_stack_p70;
    v_stack_p38 = a7;
    v_stack_p30 = a6;
    v_stack_p28 = v_stack_p68;
    v_stack_p20 = (unsigned int)(v_rsi);
    result = LdrpResSearchResourceMappedFile(a1, v_stack_p58, (unsigned int)((unsigned int)(v_rdi)), v_stack_p78);
    if (((unsigned int)(result)) != 0xC000008AULL) goto loc_0098F8A0;
    a2 = (v_stack_p78) + (-16);
    if (((a2) & (-9)) == 0) goto loc_0098F8A0;
loc_0098F9BC:
    if ((unsigned int)((unsigned int)((unsigned int)(result))) == 0) goto loc_0098F95D;
    goto loc_0098F8A2;
loc_0098F9C5:
    if ((((unsigned int)(v_rdi)) & (768)) == 0) goto loc_0098F9E4;
    if (a6 == 0) goto loc_0098F9E4;
    if (*(unsigned __int64 *)(a6) == 0) goto loc_0098F9E4;
    v_stack_p58 = *(unsigned __int64 *)(a6);
    goto loc_0098F8E8;
loc_0098F9E4:
    v_stack_p50 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0098F8A0;
loc_0098F9FD:
    if ((((unsigned __int16)((unsigned int)(0x3FFULL))) & ((unsigned __int16)(a1))) == 0) goto loc_0098FA25;
    if (a1 == 127) goto loc_0098FA25;
    a3 = 0;
    a2 = 0;
    result = DownLevelLangIDToLanguageName(a1, a2, a3, 2);
    if ((unsigned int)(result) != 0) goto loc_0098F92C;
loc_0098FA25:
    goto loc_0098F8A0;
loc_0098FA2F:
    v_r14 = (a1) | (1);
    if ((((unsigned __int8)(v_stack_p70)) & (1)) != 0) { v_r14 = v_stack_p70; }
    goto loc_0098F949;
loc_0098FA40:
    result = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) & ((unsigned int)((unsigned int)(0xC00ULL))));
    if (condition_is_above_or_equal) goto loc_0098FA91;
    goto loc_0098F882;
loc_0098FA52:
    if (result == 0) goto loc_0098FA25;
    goto loc_0098F816;
loc_0098FA5C:
    if ((((unsigned __int8)(v_rdi)) & (2)) != 0) goto loc_0098F856;
loc_0098FA66:
    goto loc_0098F8A0;
loc_0098FA70:
    if (((unsigned int)((unsigned int)(0xC00000F1ULL))) == 4) goto loc_0098FA7F;
    goto loc_0098F8A2;
loc_0098FA7F:
    if ((unsigned int)((unsigned int)(0xC00000F1ULL)) != 0) goto loc_0098F873;
    goto loc_0098F8A2;
loc_0098FA91:
    if (((unsigned int)((unsigned int)(0xC00000F2ULL))) == ((unsigned int)((unsigned int)(0xC00ULL)))) goto loc_0098F89B;
    goto loc_0098F884;
loc_0098FA9F:
    result = (unsigned int)(~((unsigned int)((unsigned int)(v_rdi))));
    if ((((unsigned int)(result)) & (0x810ULL)) != 0) goto loc_0098F89B;
    goto loc_0098F88E;
loc_0098FAB3:
    if (condition_is_above_or_equal) goto loc_0098FAD0;
    if (a6 == 0) goto loc_0098FAD0;
    if (*(unsigned __int64 *)(a6) == 0) goto loc_0098FAD0;
    v_stack_p58 = *(unsigned __int64 *)(a6);
    goto loc_0098F8DE;
loc_0098FAD0:
    v_stack_p50 = (unsigned int)((unsigned int)(0xC000000DULL));
    goto loc_0098F8A0;
loc_0098FAE9:
    result = 0;
    if ((*(unsigned __int16 *)(a1)) != 0) {
        a2 = result + 2;
        result = DownLevelLanguageNameToLangID(a1, a2, a3, 2);
        result = (unsigned __int16)(result);
    }
    v_stack_p60 = (unsigned int)(result);
    goto loc_0098FB08;
loc_0098FB08:
    v_stack_p88 = (unsigned __int16)(result);
    goto loc_0098F92C;
}
```

## 5. (Beta) C Style

```c
int64_t LdrResSearchResource(int64_t Arg1, int64_t Arg2, int32_t Arg3, int32_t Arg4, int64_t Arg5, int64_t Arg6, int64_t Arg7, int64_t Arg8)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;
    uint64_t v_stack_p38;
    uint64_t v_stack_p40;
    uint32_t v_stack_p50;
    uint64_t v_stack_p58;
    uint32_t v_stack_p60;
    uint64_t v_stack_p68;
    uint64_t v_stack_p70;
    uint64_t v_stack_p78;
    uint64_t v_stack_p88;

    local_rsp = (local_rsp) - (160);
    result = (*(uint64_t *)(v_rip + 0x47AF86)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m70 = Arg5;
    v_stack_m68 = Arg8;
    Arg3 = 0;
    if (Arg1 == 0) goto loc_0098FA25;
    if (Arg2 == 0) goto loc_0098FA25;
    if (Arg7 != 0) goto loc_0098FA52;
loc_0098F816:
    if ((((uint32_t)((uint32_t)(0xC00ULL))) & (Arg4)) != 0) goto loc_0098F89B;
    Arg1 = (uint32_t)(((uint32_t)(Arg4)) | (256));
    if (((Arg4) & (0xF00ULL)) != 0) { Arg1 = Arg4; }
    local_rdi = (uint32_t)((uint32_t)(Arg1));
    if (condition_is_below) { local_rdi = (uint32_t)(Arg1); }
    if ((((uint32_t)(local_rdi)) & (0xFFF00000ULL)) != 0) goto loc_0098F89B;
    if (((uint32_t)((uint32_t)(Arg3))) < 3) goto loc_0098FA5C;
loc_0098F856:
    if (((uint32_t)((uint32_t)(Arg3))) > 4) goto loc_0098FA66;
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (65));
    if (condition_is_not_equal) goto loc_0098FA70;
    if (((uint32_t)((uint32_t)(Arg3))) == 4) goto loc_0098FA7F;
loc_0098F873:
    if (((256) & ((uint32_t)(local_rdi))) == 0) goto loc_0098FA40;
loc_0098F882:
    if ((((uint32_t)(local_rdi)) & (0xE00ULL)) != 0) goto loc_0098F89B;
loc_0098F884:
    if (condition_is_below) goto loc_0098FA9F;
loc_0098F88E:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & ((uint32_t)((uint32_t)(0x3000ULL))));
    if (((uint32_t)(result)) != ((uint32_t)((uint32_t)(0x3000ULL)))) goto loc_0098F8C6;
loc_0098F89B:
loc_0098F8A0:
loc_0098F8A2:
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (160);
    return result;
loc_0098F8C6:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (24));
    if (((uint8_t)(result)) == 24) goto loc_0098F89B;
    v_stack_p58 = 0;
    if (((uint8_t)(result)) < 24) goto loc_0098FAB3;
loc_0098F8DE:
    if (((uint8_t)(result)) < 24) goto loc_0098F9C5;
loc_0098F8E8:
    Arg3 = ((uint32_t)(0xC00000F2ULL)) << (3);
    result = memcpy(v_stack_p78, Arg2, Arg3, Arg4);
    goto loc_0098F8FF;
loc_0098F8FF:
    local_rsi = 3;
    if (((uint32_t)((uint32_t)(0xC00000F2ULL))) <= 3) { local_rsi = (uint32_t)((uint32_t)(0xC00000F2ULL)); }
    if (((uint32_t)(local_rsi)) != 3) goto loc_0098F92C;
    if (v_stack_p88 >= 0x10000ULL) goto loc_0098FAE9;
    if (v_stack_p88 != 0) goto loc_0098F9FD;
loc_0098F92C:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & (0x1000ULL));
    if ((((uint32_t)(local_rdi)) & (768)) == 0) goto loc_0098F95D;
    if (condition_is_below) goto loc_0098FA2F;
loc_0098F949:
    result = LdrpResGetMappingSize(Arg1, v_stack_p58, (uint32_t)((uint32_t)(local_rdi)), Arg4);
    if (sign_flag) goto loc_0098F9BC;
loc_0098F95D:
    v_stack_p40 = v_stack_p70;
    v_stack_p38 = Arg7;
    v_stack_p30 = Arg6;
    v_stack_p28 = v_stack_p68;
    v_stack_p20 = (uint32_t)(local_rsi);
    result = LdrpResSearchResourceMappedFile(Arg1, v_stack_p58, (uint32_t)((uint32_t)(local_rdi)), v_stack_p78);
    if (((uint32_t)(result)) != 0xC000008AULL) goto loc_0098F8A0;
    Arg2 = (v_stack_p78) + (-16);
    if (((Arg2) & (-9)) == 0) goto loc_0098F8A0;
loc_0098F9BC:
    if ((uint32_t)((uint32_t)((uint32_t)(result))) == 0) goto loc_0098F95D;
    goto loc_0098F8A2;
loc_0098F9C5:
    if ((((uint32_t)(local_rdi)) & (768)) == 0) goto loc_0098F9E4;
    if (Arg6 == 0) goto loc_0098F9E4;
    if (*(uint64_t *)(Arg6) == 0) goto loc_0098F9E4;
    v_stack_p58 = *(uint64_t *)(Arg6);
    goto loc_0098F8E8;
loc_0098F9E4:
    v_stack_p50 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0098F8A0;
loc_0098F9FD:
    if ((((uint16_t)((uint32_t)(0x3FFULL))) & ((uint16_t)(Arg1))) == 0) goto loc_0098FA25;
    if (Arg1 == 127) goto loc_0098FA25;
    Arg3 = 0;
    Arg2 = 0;
    result = DownLevelLangIDToLanguageName(Arg1, Arg2, Arg3, 2);
    if ((uint32_t)(result) != 0) goto loc_0098F92C;
loc_0098FA25:
    goto loc_0098F8A0;
loc_0098FA2F:
    local_r14 = (Arg1) | (1);
    if ((((uint8_t)(v_stack_p70)) & (1)) != 0) { local_r14 = v_stack_p70; }
    goto loc_0098F949;
loc_0098FA40:
    result = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) & ((uint32_t)((uint32_t)(0xC00ULL))));
    if (condition_is_above_or_equal) goto loc_0098FA91;
    goto loc_0098F882;
loc_0098FA52:
    if (result == 0) goto loc_0098FA25;
    goto loc_0098F816;
loc_0098FA5C:
    if ((((uint8_t)(local_rdi)) & (2)) != 0) goto loc_0098F856;
loc_0098FA66:
    goto loc_0098F8A0;
loc_0098FA70:
    if (((uint32_t)((uint32_t)(0xC00000F1ULL))) == 4) goto loc_0098FA7F;
    goto loc_0098F8A2;
loc_0098FA7F:
    if ((uint32_t)((uint32_t)(0xC00000F1ULL)) != 0) goto loc_0098F873;
    goto loc_0098F8A2;
loc_0098FA91:
    if (((uint32_t)((uint32_t)(0xC00000F2ULL))) == ((uint32_t)((uint32_t)(0xC00ULL)))) goto loc_0098F89B;
    goto loc_0098F884;
loc_0098FA9F:
    result = (uint32_t)(~((uint32_t)((uint32_t)(local_rdi))));
    if ((((uint32_t)(result)) & (0x810ULL)) != 0) goto loc_0098F89B;
    goto loc_0098F88E;
loc_0098FAB3:
    if (condition_is_above_or_equal) goto loc_0098FAD0;
    if (Arg6 == 0) goto loc_0098FAD0;
    if (*(uint64_t *)(Arg6) == 0) goto loc_0098FAD0;
    v_stack_p58 = *(uint64_t *)(Arg6);
    goto loc_0098F8DE;
loc_0098FAD0:
    v_stack_p50 = (uint32_t)((uint32_t)(0xC000000DULL));
    goto loc_0098F8A0;
loc_0098FAE9:
    result = 0;
    if ((*(uint16_t *)(Arg1)) != 0) {
        Arg2 = result + 2;
        result = DownLevelLanguageNameToLangID(Arg1, Arg2, Arg3, 2);
        result = (uint16_t)(result);
    }
    v_stack_p60 = (uint32_t)(result);
    goto loc_0098FB08;
loc_0098FB08:
    v_stack_p88 = (uint16_t)(result);
    goto loc_0098F92C;
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x0098F7A0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
