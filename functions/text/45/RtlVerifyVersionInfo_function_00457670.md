# RtlVerifyVersionInfo

- RVA: `0x00457670`–`0x00457A53` (길이 `995` bytes)
- VA: `0x0000000140457670`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000A81D0`
- 디코드: `266`개 명령, `995/995` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **7**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x004576BF` → [memset](../6C/memset_function_006C6C40.md) (function, `0x006C6C40`)
- `0x004576D1` → [RtlGetVersion](../../page/A1/RtlGetVersion_function_00A19110.md) (function, `0x00A19110`)
- `0x004577B0` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x004578CC` → [RtlpVerCompare](RtlpVerCompare_function_00457A5C.md) (function, `0x00457A5C`)
- `0x0045793A` → [RtlpVerGetConditionMask](RtlpVerGetConditionMask_function_00457B38.md) (function, `0x00457B38`)
- `0x0045795E` → [RtlpVerGetConditionMask](RtlpVerGetConditionMask_function_00457B38.md) (function, `0x00457B38`)
- `0x00457994` → [RtlpVerCompare](RtlpVerCompare_function_00457A5C.md) (function, `0x00457A5C`)

### Direct callers
- [WdipSemLoadScenarioTable](../../page/7B/WdipSemLoadScenarioTable_function_007B02D8.md) at `0x007B0592`
- [AslpFileGetVersionBlock](../../page/81/AslpFileGetVersionBlock_function_0081FA50.md) at `0x0081FC2E`

### Static image references
- `0x0045768E` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004576D1` → [RtlGetVersion](../../page/A1/RtlGetVersion_function_00A19110.md) (`.text` → `PAGE`)
- call이 아닌 외부 분기/꼬리 이동: **10**
  - `0x00457818` → [sub_006F1A86 + 0x64](../6F/Unknown_function_006F1A86.md) (`tail-transfer`)
  - `0x00457821` → [sub_006F1A86 + 0x55](../6F/Unknown_function_006F1A86.md) (`tail-transfer`)
  - `0x00457829` → [sub_006F1A86 + 0x62](../6F/Unknown_function_006F1A86.md) (`tail-transfer`)
  - `0x004579F1` → [sub_006F1A86](../6F/Unknown_function_006F1A86.md) (`tail-transfer`)
  - `0x00457A01` → [sub_006F1A86 + 0xB](../6F/Unknown_function_006F1A86.md) (`tail-transfer`)
  - `0x00457A09` → [sub_006F1A86 + 0x1C](../6F/Unknown_function_006F1A86.md) (`tail-transfer`)
  - `0x00457A12` → [sub_006F1A86 + 0x12](../6F/Unknown_function_006F1A86.md) (`tail-transfer`)
  - `0x00457A1A` → [sub_006F1A86 + 0x1A](../6F/Unknown_function_006F1A86.md) (`tail-transfer`)
  - `0x00457A32` → [sub_006F1A86 + 0x8F](../6F/Unknown_function_006F1A86.md) (`tail-transfer`)
  - `0x00457A3A` → [sub_006F1A86 + 0x97](../6F/Unknown_function_006F1A86.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00457670  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
00457675  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0045767A  55                              push rbp
0045767B  57                              push rdi
0045767C  41 54                           push r12
0045767E  41 56                           push r14
00457680  41 57                           push r15
00457682  48 8D 6C 24 90                  lea rbp, [rsp - 0x70]
00457687  48 81 EC 70 01 00 00            sub rsp, 0x170
0045768E  48 8B 05 AB 30 9B 00            mov rax, qword ptr [rip + 0x9b30ab]
00457695  48 33 C4                        xor rax, rsp
00457698  48 89 45 60                     mov qword ptr [rbp + 0x60], rax
0045769C  33 DB                           xor ebx, ebx
0045769E  49 8B F8                        mov rdi, r8
004576A1  44 8B F2                        mov r14d, edx
004576A4  4C 8B F9                        mov r15, rcx
004576A7  40 8A F3                        mov sil, bl
004576AA  85 D2                           test edx, edx
004576AC  0F 84 48 02 00 00               je 0x1404578fa
004576B2  33 D2                           xor edx, edx
004576B4  48 8D 4C 24 44                  lea rcx, [rsp + 0x44]
004576B9  41 B8 18 01 00 00               mov r8d, 0x118
004576BF  E8 7C F5 26 00                  call 0x1406c6c40
004576C4  48 8D 4C 24 40                  lea rcx, [rsp + 0x40]
004576C9  C7 44 24 40 1C 01 00 00         mov dword ptr [rsp + 0x40], 0x11c
004576D1  E8 3A 1A 5C 00                  call 0x140a19110
004576D6  85 C0                           test eax, eax
004576D8  0F 85 CB 00 00 00               jne 0x1404577a9
004576DE  44 8D 63 01                     lea r12d, [rbx + 1]
004576E2  41 F6 C6 40                     test r14b, 0x40
004576E6  0F 85 18 02 00 00               jne 0x140457904
004576EC  B8 02 00 00 00                  mov eax, 2
004576F1  41 8A CC                        mov cl, r12b
004576F4  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
004576F8  41 8B F4                        mov esi, r12d
004576FB  44 84 F0                        test al, r14b
004576FE  0F 84 E0 00 00 00               je 0x1404577e4
00457704  48 85 FF                        test rdi, rdi
00457707  0F 89 BC 02 00 00               jns 0x1404579c9
0045770D  8B CB                           mov ecx, ebx
0045770F  41 03 CC                        add ecx, r12d
00457712  D1 E8                           shr eax, 1
00457714  75 F9                           jne 0x14045770f
00457716  8D 0C 49                        lea ecx, [rcx + rcx*2]
00457719  48 8B F7                        mov rsi, rdi
0045771C  83 C1 FD                        add ecx, -3
0045771F  48 D3 EE                        shr rsi, cl
00457722  83 E6 07                        and esi, 7
00457725  45 8B 47 04                     mov r8d, dword ptr [r15 + 4]
00457729  8B D6                           mov edx, esi
0045772B  44 8B 4C 24 44                  mov r9d, dword ptr [rsp + 0x44]
00457730  45 3B C1                        cmp r8d, r9d
00457733  0F 94 C1                        sete cl
00457736  88 4C 24 30                     mov byte ptr [rsp + 0x30], cl
0045773A  41 2B D4                        sub edx, r12d
0045773D  0F 85 EB 00 00 00               jne 0x14045782e
00457743  45 3B C8                        cmp r9d, r8d
00457746  0F 85 94 00 00 00               jne 0x1404577e0
0045774C  84 C9                           test cl, cl
0045774E  0F 85 90 00 00 00               jne 0x1404577e4
00457754  B8 04 00 00 00                  mov eax, 4
00457759  44 84 F0                        test al, r14b
0045775C  0F 85 33 01 00 00               jne 0x140457895
00457762  BA 08 00 00 00                  mov edx, 8
00457767  44 84 F2                        test dl, r14b
0045776A  0F 85 BF 02 00 00               jne 0x140457a2f
00457770  B8 80 00 00 00                  mov eax, 0x80
00457775  44 84 F0                        test al, r14b
00457778  0F 84 60 01 00 00               je 0x1404578de
0045777E  48 85 FF                        test rdi, rdi
00457781  0F 88 CB 00 00 00               js 0x140457852
00457787  0F B6 4D 5A                     movzx ecx, byte ptr [rbp + 0x5a]
0045778B  41 0F B6 97 1A 01 00 00         movzx edx, byte ptr [r15 + 0x11a]
00457793  41 2B DC                        sub ebx, r12d
00457796  0F 85 D2 00 00 00               jne 0x14045786e
0045779C  3B CA                           cmp ecx, edx
0045779E  0F 84 3A 01 00 00               je 0x1404578de
004577A4  B8 59 00 00 C0                  mov eax, 0xc0000059
004577A9  48 8B 4D 60                     mov rcx, qword ptr [rbp + 0x60]
004577AD  48 33 CC                        xor rcx, rsp
004577B0  E8 8B 4E 25 00                  call 0x1406ac640
004577B5  4C 8D 9C 24 70 01 00 00         lea r11, [rsp + 0x170]
004577BD  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
004577C1  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
004577C5  49 8B E3                        mov rsp, r11
004577C8  41 5F                           pop r15
004577CA  41 5E                           pop r14
004577CC  41 5C                           pop r12
004577CE  5F                              pop rdi
004577CF  5D                              pop rbp
004577D0  C3                              ret
004577D1  CC                              int3
004577D2  45 3B C8                        cmp r9d, r8d
004577D5  0F 9D C0                        setge al
004577D8  84 C0                           test al, al
004577DA  0F 85 6C FF FF FF               jne 0x14045774c
004577E0  84 C9                           test cl, cl
004577E2  74 C0                           je 0x1404577a4
004577E4  45 84 F4                        test r12b, r14b
004577E7  0F 85 8D 01 00 00               jne 0x14045797a
004577ED  84 C9                           test cl, cl
004577EF  0F 84 5F FF FF FF               je 0x140457754
004577F5  BA 20 00 00 00                  mov edx, 0x20
004577FA  44 84 F2                        test dl, r14b
004577FD  0F 85 03 02 00 00               jne 0x140457a06
00457803  84 C9                           test cl, cl
00457805  0F 84 49 FF FF FF               je 0x140457754
0045780B  41 F6 C6 10                     test r14b, 0x10
0045780F  0F 84 3F FF FF FF               je 0x140457754
00457815  41 3B F4                        cmp esi, r12d
00457818  0F 85 CC A2 29 00               jne 0x1406f1aea
0045781E  48 85 FF                        test rdi, rdi
00457821  0F 88 B4 A2 29 00               js 0x1406f1adb
00457827  8B C3                           mov eax, ebx
00457829  E9 BA A2 29 00                  jmp 0x1406f1ae8
0045782E  41 2B D4                        sub edx, r12d
00457831  0F 84 AC 01 00 00               je 0x1404579e3
00457837  41 2B D4                        sub edx, r12d
0045783A  74 96                           je 0x1404577d2
0045783C  41 2B D4                        sub edx, r12d
0045783F  0F 84 93 01 00 00               je 0x1404579d8
00457845  41 3B D4                        cmp edx, r12d
00457848  75 96                           jne 0x1404577e0
0045784A  45 3B C8                        cmp r9d, r8d
0045784D  0F 9E C0                        setle al
00457850  EB 86                           jmp 0x1404577d8
00457852  8B CB                           mov ecx, ebx
00457854  41 03 CC                        add ecx, r12d
00457857  D1 E8                           shr eax, 1
00457859  75 F9                           jne 0x140457854
0045785B  8D 0C 49                        lea ecx, [rcx + rcx*2]
0045785E  83 C1 FD                        add ecx, -3
00457861  48 D3 EF                        shr rdi, cl
00457864  83 E7 07                        and edi, 7
00457867  8B DF                           mov ebx, edi
00457869  E9 19 FF FF FF                  jmp 0x140457787
0045786E  41 2B DC                        sub ebx, r12d
00457871  0F 84 D2 01 00 00               je 0x140457a49
00457877  41 2B DC                        sub ebx, r12d
0045787A  74 69                           je 0x1404578e5
0045787C  41 2B DC                        sub ebx, r12d
0045787F  0F 84 BA 01 00 00               je 0x140457a3f
00457885  41 3B DC                        cmp ebx, r12d
00457888  0F 85 16 FF FF FF               jne 0x1404577a4
0045788E  3B CA                           cmp ecx, edx
00457890  0F 96 C0                        setbe al
00457893  EB 55                           jmp 0x1404578ea
00457895  48 85 FF                        test rdi, rdi
00457898  0F 89 81 01 00 00               jns 0x140457a1f
0045789E  8B CB                           mov ecx, ebx
004578A0  41 03 CC                        add ecx, r12d
004578A3  D1 E8                           shr eax, 1
004578A5  75 F9                           jne 0x1404578a0
004578A7  8D 0C 49                        lea ecx, [rcx + rcx*2]
004578AA  4C 8B D7                        mov r10, rdi
004578AD  83 C1 FD                        add ecx, -3
004578B0  49 D3 EA                        shr r10, cl
004578B3  41 83 E2 07                     and r10d, 7
004578B7  44 8B 44 24 4C                  mov r8d, dword ptr [rsp + 0x4c]
004578BC  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
004578C1  41 8B 57 0C                     mov edx, dword ptr [r15 + 0xc]
004578C5  41 8B CA                        mov ecx, r10d
004578C8  89 5C 24 20                     mov dword ptr [rsp + 0x20], ebx
004578CC  E8 8B 01 00 00                  call 0x140457a5c
004578D1  84 C0                           test al, al
004578D3  0F 85 89 FE FF FF               jne 0x140457762
004578D9  E9 C6 FE FF FF                  jmp 0x1404577a4
004578DE  33 C0                           xor eax, eax
004578E0  E9 C4 FE FF FF                  jmp 0x1404577a9
004578E5  3B CA                           cmp ecx, edx
004578E7  0F 93 C0                        setae al
004578EA  F6 D8                           neg al
004578EC  1B C0                           sbb eax, eax
004578EE  F7 D0                           not eax
004578F0  25 59 00 00 C0                  and eax, 0xc0000059
004578F5  E9 AF FE FF FF                  jmp 0x1404577a9
004578FA  B8 0D 00 00 C0                  mov eax, 0xc000000d
004578FF  E9 A5 FE FF FF                  jmp 0x1404577a9
00457904  45 0F B7 9F 18 01 00 00         movzx r11d, word ptr [r15 + 0x118]
0045790C  66 45 85 DB                     test r11w, r11w
00457910  0F 84 D6 FD FF FF               je 0x1404576ec
00457916  44 8B D3                        mov r10d, ebx
00457919  41 83 FA 10                     cmp r10d, 0x10
0045791D  73 37                           jae 0x140457956
0045791F  41 8B CA                        mov ecx, r10d
00457922  45 8B CC                        mov r9d, r12d
00457925  41 D3 E1                        shl r9d, cl
00457928  45 85 D9                        test r9d, r11d
0045792B  74 24                           je 0x140457951
0045792D  48 85 FF                        test rdi, rdi
00457930  79 C8                           jns 0x1404578fa
00457932  BA 40 00 00 00                  mov edx, 0x40
00457937  48 8B CF                        mov rcx, rdi
0045793A  E8 F9 01 00 00                  call 0x140457b38
0045793F  83 E8 06                        sub eax, 6
00457942  75 6E                           jne 0x1404579b2
00457944  0F B7 45 58                     movzx eax, word ptr [rbp + 0x58]
00457948  41 85 C1                        test r9d, eax
0045794B  0F 84 53 FE FF FF               je 0x1404577a4
00457951  45 03 D4                        add r10d, r12d
00457954  EB C3                           jmp 0x140457919
00457956  BA 40 00 00 00                  mov edx, 0x40
0045795B  48 8B CF                        mov rcx, rdi
0045795E  E8 D5 01 00 00                  call 0x140457b38
00457963  83 F8 07                        cmp eax, 7
00457966  0F 85 80 FD FF FF               jne 0x1404576ec
0045796C  40 84 F6                        test sil, sil
0045796F  0F 85 77 FD FF FF               jne 0x1404576ec
00457975  E9 2A FE FF FF                  jmp 0x1404577a4
0045797A  41 3B F4                        cmp esi, r12d
0045797D  74 6F                           je 0x1404579ee
0045797F  44 8B 44 24 48                  mov r8d, dword ptr [rsp + 0x48]
00457984  4C 8D 4C 24 30                  lea r9, [rsp + 0x30]
00457989  41 8B 57 08                     mov edx, dword ptr [r15 + 8]
0045798D  8B CE                           mov ecx, esi
0045798F  44 89 64 24 20                  mov dword ptr [rsp + 0x20], r12d
00457994  E8 C3 00 00 00                  call 0x140457a5c
00457999  8A 4C 24 30                     mov cl, byte ptr [rsp + 0x30]
0045799D  84 C0                           test al, al
0045799F  0F 85 48 FE FF FF               jne 0x1404577ed
004579A5  84 C9                           test cl, cl
004579A7  0F 85 48 FE FF FF               jne 0x1404577f5
004579AD  E9 F2 FD FF FF                  jmp 0x1404577a4
004579B2  41 3B C4                        cmp eax, r12d
004579B5  0F 85 3F FF FF FF               jne 0x1404578fa
004579BB  0F B7 45 58                     movzx eax, word ptr [rbp + 0x58]
004579BF  41 85 C1                        test r9d, eax
004579C2  74 8D                           je 0x140457951
004579C4  41 8A F4                        mov sil, r12b
004579C7  EB 88                           jmp 0x140457951
004579C9  48 8B C7                        mov rax, rdi
004579CC  48 C1 E8 04                     shr rax, 4
004579D0  0F B6 F0                        movzx esi, al
004579D3  E9 4D FD FF FF                  jmp 0x140457725
004579D8  45 3B C8                        cmp r9d, r8d
004579DB  0F 9C C0                        setl al
004579DE  E9 F5 FD FF FF                  jmp 0x1404577d8
004579E3  45 3B C8                        cmp r9d, r8d
004579E6  0F 9F C0                        setg al
004579E9  E9 EA FD FF FF                  jmp 0x1404577d8
004579EE  48 85 FF                        test rdi, rdi
004579F1  0F 88 8F A0 29 00               js 0x1406f1a86
004579F7  48 8B C7                        mov rax, rdi
004579FA  48 C1 E8 02                     shr rax, 2
004579FE  0F B6 C0                        movzx eax, al
00457A01  E9 8B A0 29 00                  jmp 0x1406f1a91
00457A06  41 3B F4                        cmp esi, r12d
00457A09  0F 85 93 A0 29 00               jne 0x1406f1aa2
00457A0F  48 85 FF                        test rdi, rdi
00457A12  0F 88 80 A0 29 00               js 0x1406f1a98
00457A18  8B C3                           mov eax, ebx
00457A1A  E9 81 A0 29 00                  jmp 0x1406f1aa0
00457A1F  48 8B C7                        mov rax, rdi
00457A22  48 C1 E8 10                     shr rax, 0x10
00457A26  44 0F B6 D0                     movzx r10d, al
00457A2A  E9 88 FE FF FF                  jmp 0x1404578b7
00457A2F  48 85 FF                        test rdi, rdi
00457A32  0F 88 DD A0 29 00               js 0x1406f1b15
00457A38  8B C3                           mov eax, ebx
00457A3A  E9 DE A0 29 00                  jmp 0x1406f1b1d
00457A3F  3B CA                           cmp ecx, edx
00457A41  0F 92 C0                        setb al
00457A44  E9 A1 FE FF FF                  jmp 0x1404578ea
00457A49  3B CA                           cmp ecx, edx
00457A4B  0F 97 C0                        seta al
00457A4E  E9 97 FE FF FF                  jmp 0x1404578ea
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlVerifyVersionInfo(__int64 a1, int a2, __int64 a3)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m124;
    unsigned int v_stack_m128;
    unsigned __int64 v_stack_m140;
    unsigned int v_stack_m150;
    unsigned __int64 v_stack_m154;
    unsigned __int64 v_stack_m158;
    unsigned __int8 v_stack_m168;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int8 v_stack_m3E;
    unsigned __int16 v_stack_m40;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;

    v_stack_p10 = v_rbx;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (368);
    result = (*(unsigned __int64 *)(v_rip + 10170539)) ^ (v_rsp);
    v_stack_m38 = result;
    v_rbx = 0;
    if (a2 == 0) goto loc_004578FA;
    a2 = 0;
    result = memset(v_stack_m154, a2, 280, a4);
    v_stack_m158 = 284;
    result = RtlGetVersion(v_stack_m158, a2, 280, a4);
    if ((unsigned int)(result) != 0) goto loc_004577A9;
    if ((((unsigned __int8)((unsigned int)(a2))) & (64)) != 0) goto loc_00457904;
loc_004576EC:
    v_stack_m168 = (unsigned __int8)((unsigned __int8)(v_rbx + 1));
    if (((2) & ((unsigned __int8)((unsigned int)(a2)))) == 0) goto loc_004577E4;
    if (!sign_flag) goto loc_004579C9;
loc_0045770F:
    a1 = (unsigned int)((0) + ((unsigned int)(v_rbx + 1)));
    result = (unsigned int)((2) >> (1));
    if (condition_is_not_equal) goto loc_0045770F;
    a1 = (unsigned int)((a1 + a1 * 2) + (-3));
    v_rsi = (a3) >> ((unsigned __int8)(a1));
    v_rsi = (unsigned int)((v_rsi) & (7));
loc_00457725:
    a1 = (((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)))) == ((unsigned int)((unsigned int)(v_stack_m154)))) ? 1 : 0;
    v_stack_m168 = (unsigned __int8)(a1);
    a2 = (unsigned int)(((unsigned int)((unsigned int)(v_rsi))) - ((unsigned int)(v_rbx + 1)));
    if (condition_is_not_equal) goto loc_0045782E;
    if (((unsigned int)((unsigned int)(v_stack_m154))) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) goto loc_004577E0;
loc_0045774C:
    if ((unsigned __int8)(a1) != 0) goto loc_004577E4;
loc_00457754:
    if (((4) & ((unsigned __int8)((unsigned int)(a2)))) != 0) goto loc_00457895;
loc_00457762:
    if (((8) & ((unsigned __int8)((unsigned int)(a2)))) != 0) goto loc_00457A2F;
    if (((128) & ((unsigned __int8)((unsigned int)(a2)))) == 0) goto loc_004578DE;
    if (sign_flag) goto loc_00457852;
loc_00457787:
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_rbx + 1)));
    if (condition_is_not_equal) goto loc_0045786E;
    if (((unsigned int)(v_stack_m3E)) == ((unsigned int)(*(unsigned __int8 *)(a1 + 282)))) goto loc_004578DE;
loc_004577A4:
loc_004577A9:
    a1 = (v_stack_m38) ^ (v_rsp);
    result = _security_check_cookie(a1, *(unsigned __int8 *)(a1 + 282), (unsigned int)(*(unsigned int *)(a1 + 4)), (unsigned int)(v_stack_m154));
    return result;
loc_004577D2:
    result = (((unsigned int)((unsigned int)(v_stack_m154))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) ? 1 : 0;
loc_004577D8:
    if ((unsigned __int8)(result) != 0) goto loc_0045774C;
loc_004577E0:
    if ((unsigned __int8)(a1) == 0) goto loc_004577A4;
loc_004577E4:
    if ((((unsigned __int8)(v_rbx + 1)) & ((unsigned __int8)((unsigned int)(a2)))) != 0) goto loc_0045797A;
loc_004577ED:
    if ((unsigned __int8)(a1) == 0) goto loc_00457754;
loc_004577F5:
    if (((32) & ((unsigned __int8)((unsigned int)(a2)))) != 0) goto loc_00457A06;
    if ((unsigned __int8)(a1) == 0) goto loc_00457754;
    if ((((unsigned __int8)((unsigned int)(a2))) & (16)) == 0) goto loc_00457754;
loc_0045782E:
    a2 = (unsigned int)((32) - ((unsigned int)(v_rbx + 1)));
    if (condition_is_equal) goto loc_004579E3;
    a2 = (unsigned int)((a2) - ((unsigned int)(v_rbx + 1)));
    if (condition_is_equal) goto loc_004577D2;
    a2 = (unsigned int)((a2) - ((unsigned int)(v_rbx + 1)));
    if (condition_is_equal) goto loc_004579D8;
    if (a2 != ((unsigned int)(v_rbx + 1))) goto loc_004577E0;
    result = (((unsigned int)((unsigned int)(v_stack_m154))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4))))) ? 1 : 0;
    goto loc_004577D8;
loc_00457852:
loc_00457854:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 56)))) + ((unsigned int)(v_rbx + 1)));
    result = (unsigned int)((result) >> (1));
    if (condition_is_not_equal) goto loc_00457854;
    a1 = (unsigned int)((a1 + a1 * 2) + (-3));
    v_rdi = (a3) >> ((unsigned __int8)(a1));
    v_rdi = (unsigned int)((v_rdi) & (7));
    goto loc_00457787;
loc_0045786E:
    v_rbx = (unsigned int)(((unsigned int)((unsigned int)(v_rdi))) - ((unsigned int)(v_rbx + 1)));
    if (condition_is_equal) goto loc_00457A49;
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_rbx + 1)));
    if (condition_is_equal) goto loc_004578E5;
    v_rbx = (unsigned int)((v_rbx) - ((unsigned int)(v_rbx + 1)));
    if (condition_is_equal) goto loc_00457A3F;
    if (((unsigned int)(v_rbx)) != ((unsigned int)(v_rbx + 1))) goto loc_004577A4;
    result = (((unsigned int)(a1)) <= a2) ? 1 : 0;
    goto loc_004578EA;
loc_00457895:
    if (!sign_flag) goto loc_00457A1F;
loc_004578A0:
    a1 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) + ((unsigned int)(v_rbx + 1)));
    result = (unsigned int)((result) >> (1));
    if (condition_is_not_equal) goto loc_004578A0;
    a1 = (unsigned int)((a1 + a1 * 2) + (-3));
    v_r10 = (v_rdi) >> ((unsigned __int8)(a1));
    v_r10 = (unsigned int)((v_r10) & (7));
loc_004578B7:
    v_stack_m150 = (unsigned int)(v_rbx);
    result = RtlpVerCompare((unsigned int)((unsigned int)(v_r10)), (unsigned int)(*(unsigned int *)(a1 + 12)), (unsigned int)(v_stack_m124), v_stack_m140);
    if ((unsigned __int8)(result) != 0) goto loc_00457762;
    goto loc_004577A4;
loc_004578DE:
    result = 0;
    goto loc_004577A9;
loc_004578E5:
    result = (((unsigned int)((unsigned int)((unsigned int)(v_r10)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 12))))) ? 1 : 0;
loc_004578EA:
    result = (unsigned __int8)(-(result));
    result = (unsigned int)(~(result));
    result = (unsigned int)((result) & (0xC0000059ULL));
    goto loc_004577A9;
loc_004578FA:
    goto loc_004577A9;
loc_00457904:
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 280)) == 0) goto loc_004576EC;
loc_00457919:
    if (((unsigned int)((unsigned int)((unsigned int)(v_rbx)))) >= 16) goto loc_00457956;
    a4 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx + 1))) << ((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rbx)))))));
    if ((((unsigned int)(a4)) & ((unsigned int)(*(unsigned __int16 *)(a1 + 280)))) == 0) goto loc_00457951;
    if (!sign_flag) goto loc_004578FA;
    result = RtlpVerGetConditionMask(v_rdi, 64, (unsigned int)(v_stack_m124), a4);
    result = (unsigned int)((result) - (6));
    if (condition_is_not_equal) goto loc_004579B2;
    if ((((unsigned int)(a4)) & ((unsigned int)(v_stack_m40))) == 0) goto loc_004577A4;
loc_00457951:
    v_r10 = (unsigned int)(((unsigned int)((unsigned int)(v_rbx))) + ((unsigned int)(v_rbx + 1)));
    goto loc_00457919;
loc_00457956:
    result = RtlpVerGetConditionMask(v_rdi, 64, (unsigned int)(v_stack_m124), a4);
    if (((unsigned int)(result)) != 7) goto loc_004576EC;
    if ((unsigned __int8)(*(unsigned __int64 *)(v_stack_m28 + 64)) != 0) goto loc_004576EC;
    goto loc_004577A4;
loc_0045797A:
    if (((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))) == ((unsigned int)(v_rbx + 1))) goto loc_004579EE;
    v_stack_m150 = (unsigned int)(v_rbx + 1);
    result = RtlpVerCompare((unsigned int)((unsigned int)(*(unsigned __int64 *)(v_stack_m28 + 64))), (unsigned int)(*(unsigned int *)(a1 + 8)), (unsigned int)(v_stack_m128), v_stack_m140);
    if ((unsigned __int8)(result) != 0) goto loc_004577ED;
    if ((unsigned __int8)(v_stack_m140) != 0) goto loc_004577F5;
    goto loc_004577A4;
loc_004579B2:
    if (((unsigned int)(result)) != ((unsigned int)(v_rbx + 1))) goto loc_004578FA;
    if ((((unsigned int)(v_stack_m140)) & ((unsigned int)(v_stack_m40))) == 0) goto loc_00457951;
    goto loc_00457951;
loc_004579C9:
    result = (v_rdi) >> (4);
    goto loc_00457725;
loc_004579D8:
    result = (((unsigned int)(v_stack_m140)) < ((unsigned int)((unsigned int)(v_stack_m128)))) ? 1 : 0;
    goto loc_004577D8;
loc_004579E3:
    result = (((unsigned int)(v_stack_m140)) > ((unsigned int)((unsigned int)(v_stack_m128)))) ? 1 : 0;
    goto loc_004577D8;
loc_004579EE:
    result = (v_rdi) >> (2);
loc_00457A06:
loc_00457A1F:
    result = (v_rdi) >> (16);
    goto loc_004578B7;
loc_00457A2F:
loc_00457A3F:
    result = (((unsigned int)(v_stack_m140)) < ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))))) ? 1 : 0;
    goto loc_004578EA;
loc_00457A49:
    result = (((unsigned int)(v_stack_m140)) > ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 8))))) ? 1 : 0;
    goto loc_004578EA;
}
```

## 5. (Beta) C Style

```c
int64_t RtlVerifyVersionInfo(void *Arg1, int32_t Arg2, int64_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_r10;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m124;
    uint32_t v_stack_m128;
    uint64_t v_stack_m140;
    uint32_t v_stack_m150;
    uint64_t v_stack_m154;
    uint64_t v_stack_m158;
    uint8_t v_stack_m168;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint8_t v_stack_m3E;
    uint16_t v_stack_m40;
    uint64_t v_stack_m98;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;

    v_stack_p10 = local_rbx;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (368);
    result = (*(uint64_t *)(v_rip + 0x9B30AB)) ^ (local_rsp);
    v_stack_m38 = result;
    local_rbx = 0;
    if (Arg2 == 0) goto loc_004578FA;
    Arg2 = 0;
    result = memset(v_stack_m154, Arg2, 280, a4);
    v_stack_m158 = 284;
    result = RtlGetVersion(v_stack_m158, Arg2, 280, a4);
    if ((uint32_t)(result) != 0) goto loc_004577A9;
    if ((((uint8_t)((uint32_t)(Arg2))) & (64)) != 0) goto loc_00457904;
loc_004576EC:
    v_stack_m168 = (uint8_t)((uint8_t)(local_rbx + 1));
    if (((2) & ((uint8_t)((uint32_t)(Arg2)))) == 0) goto loc_004577E4;
    if (!sign_flag) goto loc_004579C9;
loc_0045770F:
    Arg1 = (uint32_t)((0) + ((uint32_t)(local_rbx + 1)));
    result = (uint32_t)((2) >> (1));
    if (condition_is_not_equal) goto loc_0045770F;
    Arg1 = (uint32_t)((Arg1 + Arg1 * 2) + (-3));
    local_rsi = (Arg3) >> ((uint8_t)(Arg1));
    local_rsi = (uint32_t)((local_rsi) & (7));
loc_00457725:
    Arg1 = (((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)))) == ((uint32_t)((uint32_t)(v_stack_m154)))) ? 1 : 0;
    v_stack_m168 = (uint8_t)(Arg1);
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)(local_rsi))) - ((uint32_t)(local_rbx + 1)));
    if (condition_is_not_equal) goto loc_0045782E;
    if (((uint32_t)((uint32_t)(v_stack_m154))) != ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) goto loc_004577E0;
loc_0045774C:
    if ((uint8_t)(Arg1) != 0) goto loc_004577E4;
loc_00457754:
    if (((4) & ((uint8_t)((uint32_t)(Arg2)))) != 0) goto loc_00457895;
loc_00457762:
    if (((8) & ((uint8_t)((uint32_t)(Arg2)))) != 0) goto loc_00457A2F;
    if (((128) & ((uint8_t)((uint32_t)(Arg2)))) == 0) goto loc_004578DE;
    if (sign_flag) goto loc_00457852;
loc_00457787:
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(local_rbx + 1)));
    if (condition_is_not_equal) goto loc_0045786E;
    if (((uint32_t)(v_stack_m3E)) == ((uint32_t)(*(uint8_t *)(arg1 + 0x11A)))) goto loc_004578DE;
loc_004577A4:
loc_004577A9:
    Arg1 = (v_stack_m38) ^ (local_rsp);
    result = _security_check_cookie(Arg1, *(uint8_t *)(arg1 + 0x11A), (uint32_t)(*(uint32_t *)(arg1 + 0x4)), (uint32_t)(v_stack_m154));
    return result;
loc_004577D2:
    result = (((uint32_t)((uint32_t)(v_stack_m154))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) ? 1 : 0;
loc_004577D8:
    if ((uint8_t)(result) != 0) goto loc_0045774C;
loc_004577E0:
    if ((uint8_t)(Arg1) == 0) goto loc_004577A4;
loc_004577E4:
    if ((((uint8_t)(local_rbx + 1)) & ((uint8_t)((uint32_t)(Arg2)))) != 0) goto loc_0045797A;
loc_004577ED:
    if ((uint8_t)(Arg1) == 0) goto loc_00457754;
loc_004577F5:
    if (((32) & ((uint8_t)((uint32_t)(Arg2)))) != 0) goto loc_00457A06;
    if ((uint8_t)(Arg1) == 0) goto loc_00457754;
    if ((((uint8_t)((uint32_t)(Arg2))) & (16)) == 0) goto loc_00457754;
loc_0045782E:
    Arg2 = (uint32_t)((32) - ((uint32_t)(local_rbx + 1)));
    if (condition_is_equal) goto loc_004579E3;
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(local_rbx + 1)));
    if (condition_is_equal) goto loc_004577D2;
    Arg2 = (uint32_t)((Arg2) - ((uint32_t)(local_rbx + 1)));
    if (condition_is_equal) goto loc_004579D8;
    if (Arg2 != ((uint32_t)(local_rbx + 1))) goto loc_004577E0;
    result = (((uint32_t)((uint32_t)(v_stack_m154))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4))))) ? 1 : 0;
    goto loc_004577D8;
loc_00457852:
loc_00457854:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x38)))) + ((uint32_t)(local_rbx + 1)));
    result = (uint32_t)((result) >> (1));
    if (condition_is_not_equal) goto loc_00457854;
    Arg1 = (uint32_t)((Arg1 + Arg1 * 2) + (-3));
    local_rdi = (Arg3) >> ((uint8_t)(Arg1));
    local_rdi = (uint32_t)((local_rdi) & (7));
    goto loc_00457787;
loc_0045786E:
    local_rbx = (uint32_t)(((uint32_t)((uint32_t)(local_rdi))) - ((uint32_t)(local_rbx + 1)));
    if (condition_is_equal) goto loc_00457A49;
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(local_rbx + 1)));
    if (condition_is_equal) goto loc_004578E5;
    local_rbx = (uint32_t)((local_rbx) - ((uint32_t)(local_rbx + 1)));
    if (condition_is_equal) goto loc_00457A3F;
    if (((uint32_t)(local_rbx)) != ((uint32_t)(local_rbx + 1))) goto loc_004577A4;
    result = (((uint32_t)(Arg1)) <= Arg2) ? 1 : 0;
    goto loc_004578EA;
loc_00457895:
    if (!sign_flag) goto loc_00457A1F;
loc_004578A0:
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) + ((uint32_t)(local_rbx + 1)));
    result = (uint32_t)((result) >> (1));
    if (condition_is_not_equal) goto loc_004578A0;
    Arg1 = (uint32_t)((Arg1 + Arg1 * 2) + (-3));
    local_r10 = (local_rdi) >> ((uint8_t)(Arg1));
    local_r10 = (uint32_t)((local_r10) & (7));
loc_004578B7:
    v_stack_m150 = (uint32_t)(local_rbx);
    result = RtlpVerCompare((uint32_t)((uint32_t)(local_r10)), (uint32_t)(*(uint32_t *)(arg1 + 0xC)), (uint32_t)(v_stack_m124), v_stack_m140);
    if ((uint8_t)(result) != 0) goto loc_00457762;
    goto loc_004577A4;
loc_004578DE:
    result = 0;
    goto loc_004577A9;
loc_004578E5:
    result = (((uint32_t)((uint32_t)((uint32_t)(local_r10)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0xC))))) ? 1 : 0;
loc_004578EA:
    result = (uint8_t)(-(result));
    result = (uint32_t)(~(result));
    result = (uint32_t)((result) & (0xC0000059ULL));
    goto loc_004577A9;
loc_004578FA:
    goto loc_004577A9;
loc_00457904:
    if ((uint16_t)(*(uint16_t *)(arg1 + 0x118)) == 0) goto loc_004576EC;
loc_00457919:
    if (((uint32_t)((uint32_t)((uint32_t)(local_rbx)))) >= 16) goto loc_00457956;
    a4 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx + 1))) << ((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rbx)))))));
    if ((((uint32_t)(a4)) & ((uint32_t)(*(uint16_t *)(arg1 + 0x118)))) == 0) goto loc_00457951;
    if (!sign_flag) goto loc_004578FA;
    result = RtlpVerGetConditionMask(local_rdi, 64, (uint32_t)(v_stack_m124), a4);
    result = (uint32_t)((result) - (6));
    if (condition_is_not_equal) goto loc_004579B2;
    if ((((uint32_t)(a4)) & ((uint32_t)(v_stack_m40))) == 0) goto loc_004577A4;
loc_00457951:
    local_r10 = (uint32_t)(((uint32_t)((uint32_t)(local_rbx))) + ((uint32_t)(local_rbx + 1)));
    goto loc_00457919;
loc_00457956:
    result = RtlpVerGetConditionMask(local_rdi, 64, (uint32_t)(v_stack_m124), a4);
    if (((uint32_t)(result)) != 7) goto loc_004576EC;
    if ((uint8_t)(*(uint64_t *)(v_stack_m28 + 0x40)) != 0) goto loc_004576EC;
    goto loc_004577A4;
loc_0045797A:
    if (((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))) == ((uint32_t)(local_rbx + 1))) goto loc_004579EE;
    v_stack_m150 = (uint32_t)(local_rbx + 1);
    result = RtlpVerCompare((uint32_t)((uint32_t)(*(uint64_t *)(v_stack_m28 + 0x40))), (uint32_t)(*(uint32_t *)(arg1 + 0x8)), (uint32_t)(v_stack_m128), v_stack_m140);
    if ((uint8_t)(result) != 0) goto loc_004577ED;
    if ((uint8_t)(v_stack_m140) != 0) goto loc_004577F5;
    goto loc_004577A4;
loc_004579B2:
    if (((uint32_t)(result)) != ((uint32_t)(local_rbx + 1))) goto loc_004578FA;
    if ((((uint32_t)(v_stack_m140)) & ((uint32_t)(v_stack_m40))) == 0) goto loc_00457951;
    goto loc_00457951;
loc_004579C9:
    result = (local_rdi) >> (4);
    goto loc_00457725;
loc_004579D8:
    result = (((uint32_t)(v_stack_m140)) < ((uint32_t)((uint32_t)(v_stack_m128)))) ? 1 : 0;
    goto loc_004577D8;
loc_004579E3:
    result = (((uint32_t)(v_stack_m140)) > ((uint32_t)((uint32_t)(v_stack_m128)))) ? 1 : 0;
    goto loc_004577D8;
loc_004579EE:
    result = (local_rdi) >> (2);
loc_00457A06:
loc_00457A1F:
    result = (local_rdi) >> (16);
    goto loc_004578B7;
loc_00457A2F:
loc_00457A3F:
    result = (((uint32_t)(v_stack_m140)) < ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))))) ? 1 : 0;
    goto loc_004578EA;
loc_00457A49:
    result = (((uint32_t)(v_stack_m140)) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x8))))) ? 1 : 0;
    goto loc_004578EA;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x4` | `32` | `R` |
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x118` | `16` | `R` |
| `Arg1` | `+ 0x11A` | `8` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00457670&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
