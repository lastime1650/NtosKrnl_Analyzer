# ApiSetCompose_ProcessV7Extension_Phase1

- RVA: `0x006641BC`–`0x006648A2` (길이 `1,766` bytes)
- VA: `0x00000001406641BC`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A0D74`
- 디코드: `473`개 명령, `1,766/1,766` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **18**; 고유 호출 대상: **9**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x0066422F` → [ApiSetpSearchForSectionIndex_V7](ApiSetpSearchForSectionIndex_V7_function_00665218.md) (function, `0x00665218`)
- `0x0066424B` → [ApiSetSchemaExpander_InsertExtensionNameEntry](ApiSetSchemaExpander_InsertExtensionNameEntry_function_006656B0.md) (function, `0x006656B0`)
- `0x006642A4` → [ApiSetpGetContractKeyInfo](ApiSetpGetContractKeyInfo_function_00664B44.md) (function, `0x00664B44`)
- `0x006642F5` → [ApiSetpGetSearchKeyHash](ApiSetpGetSearchKeyHash_function_00664F9C.md) (function, `0x00664F9C`)
- `0x00664312` → [ApiSetpGetSearchKeyHash](ApiSetpGetSearchKeyHash_function_00664F9C.md) (function, `0x00664F9C`)
- `0x00664328` → [ApiSetpSearchForSectionIndex_V7](ApiSetpSearchForSectionIndex_V7_function_00665218.md) (function, `0x00665218`)
- `0x00664379` → [ApiSetSchemaExpander_InsertContractEntry](ApiSetSchemaExpander_InsertContractEntry_function_0066565C.md) (function, `0x0066565C`)
- `0x00664405` → [ApiSetpGetSearchKeyHash](ApiSetpGetSearchKeyHash_function_00664F9C.md) (function, `0x00664F9C`)
- `0x00664421` → [ApiSetpGetSearchKeyHash](ApiSetpGetSearchKeyHash_function_00664F9C.md) (function, `0x00664F9C`)
- `0x00664437` → [ApiSetpSearchForSectionIndex_V7](ApiSetpSearchForSectionIndex_V7_function_00665218.md) (function, `0x00665218`)
- `0x0066445B` → [ApiSetSchemaExpander_InsertGroupContractEntry](ApiSetSchemaExpander_InsertGroupContractEntry_function_00665704.md) (function, `0x00665704`)
- `0x006644EE` → [ApiSetpGetSearchKeyHash](ApiSetpGetSearchKeyHash_function_00664F9C.md) (function, `0x00664F9C`)
- `0x0066450A` → [ApiSetpGetSearchKeyHash](ApiSetpGetSearchKeyHash_function_00664F9C.md) (function, `0x00664F9C`)
- `0x00664520` → [ApiSetpSearchForSectionIndex_V7](ApiSetpSearchForSectionIndex_V7_function_00665218.md) (function, `0x00665218`)
- `0x00664544` → [ApiSetSchemaExpander_InsertSemverContractEntry](ApiSetSchemaExpander_InsertSemverContractEntry_function_00665850.md) (function, `0x00665850`)
- `0x00664647` → [ApiSetpSearchForApiSetA](ApiSetpSearchForApiSetA_function_006624A8.md) (function, `0x006624A8`)
- `0x006646BF` → [ApiSetpSearchForSectionIndex_V7](ApiSetpSearchForSectionIndex_V7_function_00665218.md) (function, `0x00665218`)
- `0x006646E2` → [ApiSetSchemaExpander_InsertHostEntry](ApiSetSchemaExpander_InsertHostEntry_function_00665758.md) (function, `0x00665758`)

### Direct callers
- [ApiSetComposeSchema_V7](ApiSetComposeSchema_V7_function_00663CCC.md) at `0x00663E84`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
006641BC  48 89 5C 24 10                  mov qword ptr [rsp + 0x10], rbx
006641C1  55                              push rbp
006641C2  56                              push rsi
006641C3  57                              push rdi
006641C4  41 54                           push r12
006641C6  41 55                           push r13
006641C8  41 56                           push r14
006641CA  41 57                           push r15
006641CC  48 8B EC                        mov rbp, rsp
006641CF  48 83 EC 70                     sub rsp, 0x70
006641D3  33 FF                           xor edi, edi
006641D5  4C 8B E1                        mov r12, rcx
006641D8  0F B7 49 10                     movzx ecx, word ptr [rcx + 0x10]
006641DC  48 8B F2                        mov rsi, rdx
006641DF  8B DF                           mov ebx, edi
006641E1  41 BE FF FF 00 00               mov r14d, 0xffff
006641E7  44 8D 6F 01                     lea r13d, [rdi + 1]
006641EB  66 85 C9                        test cx, cx
006641EE  74 6A                           je 0x14066425a
006641F0  33 C0                           xor eax, eax
006641F2  4C 8D 45 D8                     lea r8, [rbp - 0x28]
006641F6  48 89 45 F8                     mov qword ptr [rbp - 8], rax
006641FA  0F 57 C0                        xorps xmm0, xmm0
006641FD  41 8B 44 24 08                  mov eax, dword ptr [r12 + 8]
00664202  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00664206  66 89 4D E0                     mov word ptr [rbp - 0x20], cx
0066420A  49 03 C4                        add rax, r12
0066420D  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00664211  66 89 4D EA                     mov word ptr [rbp - 0x16], cx
00664215  48 8B 4A 20                     mov rcx, qword ptr [rdx + 0x20]
00664219  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
0066421D  40 88 7D E2                     mov byte ptr [rbp - 0x1e], dil
00664221  44 8A 49 59                     mov r9b, byte ptr [rcx + 0x59]
00664225  48 8D 51 50                     lea rdx, [rcx + 0x50]
00664229  41 D0 E9                        shr r9b, 1
0066422C  45 22 CD                        and r9b, r13b
0066422F  E8 E4 0F 00 00                  call 0x140665218
00664234  66 41 3B C6                     cmp ax, r14w
00664238  74 0A                           je 0x140664244
0066423A  BB 35 00 00 C0                  mov ebx, 0xc0000035
0066423F  E9 43 06 00 00                  jmp 0x140664887
00664244  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00664248  48 8B CE                        mov rcx, rsi
0066424B  E8 60 14 00 00                  call 0x1406656b0
00664250  8B D8                           mov ebx, eax
00664252  85 C0                           test eax, eax
00664254  0F 88 2D 06 00 00               js 0x140664887
0066425A  8B CF                           mov ecx, edi
0066425C  89 4D C4                        mov dword ptr [rbp - 0x3c], ecx
0066425F  66 41 3B 7C 24 12               cmp di, word ptr [r12 + 0x12]
00664265  0F 83 1C 06 00 00               jae 0x140664887
0066426B  8B C1                           mov eax, ecx
0066426D  4C 8D 4D D8                     lea r9, [rbp - 0x28]
00664271  33 C9                           xor ecx, ecx
00664273  0F 57 C0                        xorps xmm0, xmm0
00664276  48 89 4D F8                     mov qword ptr [rbp - 8], rcx
0066427A  45 33 C0                        xor r8d, r8d
0066427D  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
00664281  48 8D 14 80                     lea rdx, [rax + rax*4]
00664285  41 8B 44 24 0C                  mov eax, dword ptr [r12 + 0xc]
0066428A  49 03 C4                        add rax, r12
0066428D  48 89 55 C8                     mov qword ptr [rbp - 0x38], rdx
00664291  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00664295  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00664299  8B 0C 90                        mov ecx, dword ptr [rax + rdx*4]
0066429C  0F B7 54 90 08                  movzx edx, word ptr [rax + rdx*4 + 8]
006642A1  49 03 CC                        add rcx, r12
006642A4  E8 9B 08 00 00                  call 0x140664b44
006642A9  84 C0                           test al, al
006642AB  0F 84 D1 05 00 00               je 0x140664882
006642B1  44 8B 75 E4                     mov r14d, dword ptr [rbp - 0x1c]
006642B5  41 8D 46 FF                     lea eax, [r14 - 1]
006642B9  83 F8 02                        cmp eax, 2
006642BC  0F 87 C0 05 00 00               ja 0x140664882
006642C2  4C 8B 7E 20                     mov r15, qword ptr [rsi + 0x20]
006642C6  41 8A 4F 02                     mov cl, byte ptr [r15 + 2]
006642CA  45 8A 57 37                     mov r10b, byte ptr [r15 + 0x37]
006642CE  8A D1                           mov dl, cl
006642D0  80 E2 10                        and dl, 0x10
006642D3  44 88 54 24 20                  mov byte ptr [rsp + 0x20], r10b
006642D8  80 E1 08                        and cl, 8
006642DB  41 F6 47 35 04                  test byte ptr [r15 + 0x35], 4
006642E0  74 1D                           je 0x1406642ff
006642E2  84 D2                           test dl, dl
006642E4  41 8A D5                        mov dl, r13b
006642E7  41 0F 95 C1                     setne r9b
006642EB  84 C9                           test cl, cl
006642ED  48 8D 4D D8                     lea rcx, [rbp - 0x28]
006642F1  41 0F 95 C0                     setne r8b
006642F5  E8 A2 0C 00 00                  call 0x140664f9c
006642FA  0F B6 C0                        movzx eax, al
006642FD  EB 18                           jmp 0x140664317
006642FF  84 D2                           test dl, dl
00664301  41 8A D5                        mov dl, r13b
00664304  41 0F 95 C1                     setne r9b
00664308  84 C9                           test cl, cl
0066430A  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0066430E  41 0F 95 C0                     setne r8b
00664312  E8 85 0C 00 00                  call 0x140664f9c
00664317  49 8D 57 2C                     lea rdx, [r15 + 0x2c]
0066431B  89 45 50                        mov dword ptr [rbp + 0x50], eax
0066431E  45 8A CD                        mov r9b, r13b
00664321  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00664325  49 8B CF                        mov rcx, r15
00664328  E8 EB 0E 00 00                  call 0x140665218
0066432D  44 0F B7 E8                     movzx r13d, ax
00664331  B8 FF FF 00 00                  mov eax, 0xffff
00664336  66 44 89 6D 40                  mov word ptr [rbp + 0x40], r13w
0066433B  66 44 3B E8                     cmp r13w, ax
0066433F  74 2D                           je 0x14066436e
00664341  41 0F B7 4F 12                  movzx ecx, word ptr [r15 + 0x12]
00664346  41 0F B6 57 34                  movzx edx, byte ptr [r15 + 0x34]
0066434B  41 8B 7F 2C                     mov edi, dword ptr [r15 + 0x2c]
0066434F  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00664352  49 0F AF D5                     imul rdx, r13
00664356  48 2B D1                        sub rdx, rcx
00664359  49 8D 0C 17                     lea rcx, [r15 + rdx]
0066435D  48 03 F9                        add rdi, rcx
00664360  39 07                           cmp dword ptr [rdi], eax
00664362  74 2D                           je 0x140664391
00664364  BB 29 02 00 C0                  mov ebx, 0xc0000229
00664369  E9 19 05 00 00                  jmp 0x140664887
0066436E  4C 8D 45 40                     lea r8, [rbp + 0x40]
00664372  48 8B CE                        mov rcx, rsi
00664375  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00664379  E8 DE 12 00 00                  call 0x14066565c
0066437E  8B D8                           mov ebx, eax
00664380  85 C0                           test eax, eax
00664382  0F 88 FF 04 00 00               js 0x140664887
00664388  44 8B 75 E4                     mov r14d, dword ptr [rbp - 0x1c]
0066438C  44 0F B7 6D 40                  movzx r13d, word ptr [rbp + 0x40]
00664391  B8 FF FF 00 00                  mov eax, 0xffff
00664396  66 89 45 50                     mov word ptr [rbp + 0x50], ax
0066439A  44 0F B7 C8                     movzx r9d, ax
0066439E  66 89 45 58                     mov word ptr [rbp + 0x58], ax
006643A2  41 83 FE 01                     cmp r14d, 1
006643A6  75 23                           jne 0x1406643cb
006643A8  48 85 FF                        test rdi, rdi
006643AB  0F 84 74 02 00 00               je 0x140664625
006643B1  44 0F B7 47 04                  movzx r8d, word ptr [rdi + 4]
006643B6  0F B7 4F 06                     movzx ecx, word ptr [rdi + 6]
006643BA  8A 47 0A                        mov al, byte ptr [rdi + 0xa]
006643BD  66 44 89 45 50                  mov word ptr [rbp + 0x50], r8w
006643C2  66 89 4D 58                     mov word ptr [rbp + 0x58], cx
006643C6  E9 D1 01 00 00                  jmp 0x14066459c
006643CB  48 8B 7E 20                     mov rdi, qword ptr [rsi + 0x20]
006643CF  8A 4F 02                        mov cl, byte ptr [rdi + 2]
006643D2  8A D1                           mov dl, cl
006643D4  80 E1 08                        and cl, 8
006643D7  80 E2 10                        and dl, 0x10
006643DA  41 83 FE 02                     cmp r14d, 2
006643DE  0F 85 E9 00 00 00               jne 0x1406644cd
006643E4  F6 47 41 04                     test byte ptr [rdi + 0x41], 4
006643E8  44 8A 57 43                     mov r10b, byte ptr [rdi + 0x43]
006643EC  44 88 54 24 20                  mov byte ptr [rsp + 0x20], r10b
006643F1  74 1C                           je 0x14066440f
006643F3  84 D2                           test dl, dl
006643F5  41 0F 95 C1                     setne r9b
006643F9  84 C9                           test cl, cl
006643FB  48 8D 4D D8                     lea rcx, [rbp - 0x28]
006643FF  41 0F 95 C0                     setne r8b
00664403  33 D2                           xor edx, edx
00664405  E8 92 0B 00 00                  call 0x140664f9c
0066440A  0F B6 C0                        movzx eax, al
0066440D  EB 17                           jmp 0x140664426
0066440F  84 D2                           test dl, dl
00664411  41 0F 95 C1                     setne r9b
00664415  84 C9                           test cl, cl
00664417  48 8D 4D D8                     lea rcx, [rbp - 0x28]
0066441B  41 0F 95 C0                     setne r8b
0066441F  33 D2                           xor edx, edx
00664421  E8 76 0B 00 00                  call 0x140664f9c
00664426  45 33 C9                        xor r9d, r9d
00664429  89 45 C0                        mov dword ptr [rbp - 0x40], eax
0066442C  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00664430  48 8B CF                        mov rcx, rdi
00664433  48 8D 57 38                     lea rdx, [rdi + 0x38]
00664437  E8 DC 0D 00 00                  call 0x140665218
0066443C  44 0F B7 C8                     movzx r9d, ax
00664440  B8 FF FF 00 00                  mov eax, 0xffff
00664445  66 44 89 4D 40                  mov word ptr [rbp + 0x40], r9w
0066444A  66 44 3B C8                     cmp r9w, ax
0066444E  75 28                           jne 0x140664478
00664450  4C 8D 45 40                     lea r8, [rbp + 0x40]
00664454  48 8B CE                        mov rcx, rsi
00664457  48 8D 55 D8                     lea rdx, [rbp - 0x28]
0066445B  E8 A4 12 00 00                  call 0x140665704
00664460  8B D8                           mov ebx, eax
00664462  85 C0                           test eax, eax
00664464  0F 88 1D 04 00 00               js 0x140664887
0066446A  44 8B 75 E4                     mov r14d, dword ptr [rbp - 0x1c]
0066446E  44 0F B7 4D 40                  movzx r9d, word ptr [rbp + 0x40]
00664473  E9 2C 01 00 00                  jmp 0x1406645a4
00664478  8B 47 38                        mov eax, dword ptr [rdi + 0x38]
0066447B  0F B6 57 40                     movzx edx, byte ptr [rdi + 0x40]
0066447F  44 0F B7 47 12                  movzx r8d, word ptr [rdi + 0x12]
00664484  49 0F AF D1                     imul rdx, r9
00664488  48 03 D0                        add rdx, rax
0066448B  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
0066448E  49 2B D0                        sub rdx, r8
00664491  39 04 3A                        cmp dword ptr [rdx + rdi], eax
00664494  0F 85 CA FE FF FF               jne 0x140664364
0066449A  0F B7 44 3A 04                  movzx eax, word ptr [rdx + rdi + 4]
0066449F  0F B6 4F 34                     movzx ecx, byte ptr [rdi + 0x34]
006644A3  48 0F AF C8                     imul rcx, rax
006644A7  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
006644AA  48 03 C8                        add rcx, rax
006644AD  8A 44 3A 06                     mov al, byte ptr [rdx + rdi + 6]
006644B1  49 2B C8                        sub rcx, r8
006644B4  44 0F B7 44 39 04               movzx r8d, word ptr [rcx + rdi + 4]
006644BA  0F B7 4C 39 06                  movzx ecx, word ptr [rcx + rdi + 6]
006644BF  66 89 4D 58                     mov word ptr [rbp + 0x58], cx
006644C3  66 44 89 45 50                  mov word ptr [rbp + 0x50], r8w
006644C8  E9 CF 00 00 00                  jmp 0x14066459c
006644CD  F6 47 4D 04                     test byte ptr [rdi + 0x4d], 4
006644D1  44 8A 57 4F                     mov r10b, byte ptr [rdi + 0x4f]
006644D5  44 88 54 24 20                  mov byte ptr [rsp + 0x20], r10b
006644DA  74 1C                           je 0x1406644f8
006644DC  84 D2                           test dl, dl
006644DE  41 0F 95 C1                     setne r9b
006644E2  84 C9                           test cl, cl
006644E4  48 8D 4D D8                     lea rcx, [rbp - 0x28]
006644E8  41 0F 95 C0                     setne r8b
006644EC  33 D2                           xor edx, edx
006644EE  E8 A9 0A 00 00                  call 0x140664f9c
006644F3  0F B6 C0                        movzx eax, al
006644F6  EB 17                           jmp 0x14066450f
006644F8  84 D2                           test dl, dl
006644FA  41 0F 95 C1                     setne r9b
006644FE  84 C9                           test cl, cl
00664500  48 8D 4D D8                     lea rcx, [rbp - 0x28]
00664504  41 0F 95 C0                     setne r8b
00664508  33 D2                           xor edx, edx
0066450A  E8 8D 0A 00 00                  call 0x140664f9c
0066450F  45 33 C9                        xor r9d, r9d
00664512  89 45 C0                        mov dword ptr [rbp - 0x40], eax
00664515  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00664519  48 8B CF                        mov rcx, rdi
0066451C  48 8D 57 44                     lea rdx, [rdi + 0x44]
00664520  E8 F3 0C 00 00                  call 0x140665218
00664525  44 0F B7 C8                     movzx r9d, ax
00664529  B8 FF FF 00 00                  mov eax, 0xffff
0066452E  66 44 89 4D 40                  mov word ptr [rbp + 0x40], r9w
00664533  66 44 3B C8                     cmp r9w, ax
00664537  75 15                           jne 0x14066454e
00664539  4C 8D 45 40                     lea r8, [rbp + 0x40]
0066453D  48 8B CE                        mov rcx, rsi
00664540  48 8D 55 D8                     lea rdx, [rbp - 0x28]
00664544  E8 07 13 00 00                  call 0x140665850
00664549  E9 12 FF FF FF                  jmp 0x140664460
0066454E  8B 47 44                        mov eax, dword ptr [rdi + 0x44]
00664551  0F B6 57 4C                     movzx edx, byte ptr [rdi + 0x4c]
00664555  44 0F B7 47 12                  movzx r8d, word ptr [rdi + 0x12]
0066455A  49 0F AF D1                     imul rdx, r9
0066455E  48 03 D0                        add rdx, rax
00664561  8B 45 C0                        mov eax, dword ptr [rbp - 0x40]
00664564  49 2B D0                        sub rdx, r8
00664567  39 04 3A                        cmp dword ptr [rdx + rdi], eax
0066456A  0F 85 F4 FD FF FF               jne 0x140664364
00664570  0F B7 44 3A 04                  movzx eax, word ptr [rdx + rdi + 4]
00664575  0F B6 4F 34                     movzx ecx, byte ptr [rdi + 0x34]
00664579  48 0F AF C8                     imul rcx, rax
0066457D  8B 47 2C                        mov eax, dword ptr [rdi + 0x2c]
00664580  48 03 C8                        add rcx, rax
00664583  49 2B C8                        sub rcx, r8
00664586  0F B7 44 39 04                  movzx eax, word ptr [rcx + rdi + 4]
0066458B  66 89 45 50                     mov word ptr [rbp + 0x50], ax
0066458F  0F B7 44 39 06                  movzx eax, word ptr [rcx + rdi + 6]
00664594  66 89 45 58                     mov word ptr [rbp + 0x58], ax
00664598  8A 44 3A 0A                     mov al, byte ptr [rdx + rdi + 0xa]
0066459C  A8 01                           test al, 1
0066459E  0F 85 BE 02 00 00               jne 0x140664862
006645A4  4C 8B 7D C8                     mov r15, qword ptr [rbp - 0x38]
006645A8  41 83 FE 02                     cmp r14d, 2
006645AC  75 37                           jne 0x1406645e5
006645AE  4C 8B 46 20                     mov r8, qword ptr [rsi + 0x20]
006645B2  41 0F B7 C1                     movzx eax, r9w
006645B6  41 0F B6 50 40                  movzx edx, byte ptr [r8 + 0x40]
006645BB  41 8B 48 38                     mov ecx, dword ptr [r8 + 0x38]
006645BF  48 0F AF D0                     imul rdx, rax
006645C3  41 0F B7 40 12                  movzx eax, word ptr [r8 + 0x12]
006645C8  48 2B D0                        sub rdx, rax
006645CB  49 8D 04 10                     lea rax, [r8 + rdx]
006645CF  48 03 C8                        add rcx, rax
006645D2  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
006645D6  66 44 89 69 04                  mov word ptr [rcx + 4], r13w
006645DB  42 8B 44 B8 0C                  mov eax, dword ptr [rax + r15*4 + 0xc]
006645E0  89 41 08                        mov dword ptr [rcx + 8], eax
006645E3  EB 44                           jmp 0x140664629
006645E5  41 83 FE 03                     cmp r14d, 3
006645E9  75 3E                           jne 0x140664629
006645EB  48 8B 56 20                     mov rdx, qword ptr [rsi + 0x20]
006645EF  41 0F B7 C1                     movzx eax, r9w
006645F3  0F B6 4A 4C                     movzx ecx, byte ptr [rdx + 0x4c]
006645F7  44 8B 42 44                     mov r8d, dword ptr [rdx + 0x44]
006645FB  48 0F AF C8                     imul rcx, rax
006645FF  0F B7 42 12                     movzx eax, word ptr [rdx + 0x12]
00664603  48 2B C8                        sub rcx, rax
00664606  48 8D 04 0A                     lea rax, [rdx + rcx]
0066460A  4C 03 C0                        add r8, rax
0066460D  48 8B 45 D0                     mov rax, qword ptr [rbp - 0x30]
00664611  66 45 89 68 04                  mov word ptr [r8 + 4], r13w
00664616  42 F6 44 B8 11 04               test byte ptr [rax + r15*4 + 0x11], 4
0066461C  74 0B                           je 0x140664629
0066461E  41 80 48 0A 04                  or byte ptr [r8 + 0xa], 4
00664623  EB 04                           jmp 0x140664629
00664625  4C 8B 7D C8                     mov r15, qword ptr [rbp - 0x38]
00664629  33 C0                           xor eax, eax
0066462B  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
0066462F  38 46 10                        cmp byte ptr [rsi + 0x10], al
00664632  74 1E                           je 0x140664652
00664634  41 83 FE 03                     cmp r14d, 3
00664638  75 18                           jne 0x140664652
0066463A  44 0F B7 45 EA                  movzx r8d, word ptr [rbp - 0x16]
0066463F  48 8B 55 D8                     mov rdx, qword ptr [rbp - 0x28]
00664643  48 8B 4E 28                     mov rcx, qword ptr [rsi + 0x28]
00664647  E8 5C DE FF FF                  call 0x1406624a8
0066464C  48 89 45 C8                     mov qword ptr [rbp - 0x38], rax
00664650  33 C0                           xor eax, eax
00664652  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00664656  0F B7 F8                        movzx edi, ax
00664659  66 42 3B 44 B9 0A               cmp ax, word ptr [rcx + r15*4 + 0xa]
0066465F  0F 83 FD 01 00 00               jae 0x140664862
00664665  41 BB 01 00 00 00               mov r11d, 1
0066466B  46 8B 74 B9 04                  mov r14d, dword ptr [rcx + r15*4 + 4]
00664670  4C 8D 45 D8                     lea r8, [rbp - 0x28]
00664674  0F 57 C0                        xorps xmm0, xmm0
00664677  0F B7 C7                        movzx eax, di
0066467A  48 C1 E0 04                     shl rax, 4
0066467E  49 03 C4                        add rax, r12
00664681  4C 03 F0                        add r14, rax
00664684  33 C0                           xor eax, eax
00664686  0F 11 45 D8                     movups xmmword ptr [rbp - 0x28], xmm0
0066468A  48 89 45 F8                     mov qword ptr [rbp - 8], rax
0066468E  0F 11 45 E8                     movups xmmword ptr [rbp - 0x18], xmm0
00664692  41 0F B7 4E 08                  movzx ecx, word ptr [r14 + 8]
00664697  41 8B 06                        mov eax, dword ptr [r14]
0066469A  66 89 4D E0                     mov word ptr [rbp - 0x20], cx
0066469E  49 03 C4                        add rax, r12
006646A1  66 89 4D EA                     mov word ptr [rbp - 0x16], cx
006646A5  48 8B 4E 20                     mov rcx, qword ptr [rsi + 0x20]
006646A9  48 89 45 D8                     mov qword ptr [rbp - 0x28], rax
006646AD  44 88 5D E2                     mov byte ptr [rbp - 0x1e], r11b
006646B1  44 8A 49 65                     mov r9b, byte ptr [rcx + 0x65]
006646B5  48 8D 51 5C                     lea rdx, [rcx + 0x5c]
006646B9  41 D0 E9                        shr r9b, 1
006646BC  45 22 CB                        and r9b, r11b
006646BF  E8 54 0B 00 00                  call 0x140665218
006646C4  44 0F B7 D0                     movzx r10d, ax
006646C8  66 89 45 40                     mov word ptr [rbp + 0x40], ax
006646CC  B8 FF FF 00 00                  mov eax, 0xffff
006646D1  66 44 3B D0                     cmp r10w, ax
006646D5  75 29                           jne 0x140664700
006646D7  4C 8D 45 40                     lea r8, [rbp + 0x40]
006646DB  48 8B CE                        mov rcx, rsi
006646DE  48 8D 55 D8                     lea rdx, [rbp - 0x28]
006646E2  E8 71 10 00 00                  call 0x140665758
006646E7  45 33 C9                        xor r9d, r9d
006646EA  8B D8                           mov ebx, eax
006646EC  85 C0                           test eax, eax
006646EE  0F 88 93 01 00 00               js 0x140664887
006646F4  44 0F B7 55 40                  movzx r10d, word ptr [rbp + 0x40]
006646F9  B8 FF FF 00 00                  mov eax, 0xffff
006646FE  EB 03                           jmp 0x140664703
00664700  45 33 C9                        xor r9d, r9d
00664703  66 45 39 4E 0A                  cmp word ptr [r14 + 0xa], r9w
00664708  0F 84 AE 00 00 00               je 0x1406647bc
0066470E  41 B3 01                        mov r11b, 1
00664711  66 39 45 50                     cmp word ptr [rbp + 0x50], ax
00664715  0F 84 49 FC FF FF               je 0x140664364
0066471B  44 8B B6 9C 00 00 00            mov r14d, dword ptr [rsi + 0x9c]
00664722  41 8D 46 10                     lea eax, [r14 + 0x10]
00664726  41 C1 EE 04                     shr r14d, 4
0066472A  89 86 9C 00 00 00               mov dword ptr [rsi + 0x9c], eax
00664730  4C 8B 46 20                     mov r8, qword ptr [rsi + 0x20]
00664734  41 0F B7 C6                     movzx eax, r14w
00664738  41 0F B7 50 12                  movzx edx, word ptr [r8 + 0x12]
0066473D  45 0F B7 48 72                  movzx r9d, word ptr [r8 + 0x72]
00664742  41 0F B6 48 64                  movzx ecx, byte ptr [r8 + 0x64]
00664747  4C 0F AF C8                     imul r9, rax
0066474B  41 8B 40 68                     mov eax, dword ptr [r8 + 0x68]
0066474F  4C 03 C8                        add r9, rax
00664752  0F B7 45 50                     movzx eax, word ptr [rbp + 0x50]
00664756  48 0F AF C8                     imul rcx, rax
0066475A  41 8B 40 5C                     mov eax, dword ptr [r8 + 0x5c]
0066475E  4C 2B CA                        sub r9, rdx
00664761  48 03 C8                        add rcx, rax
00664764  4D 03 C8                        add r9, r8
00664767  48 2B CA                        sub rcx, rdx
0066476A  42 8B 44 01 04                  mov eax, dword ptr [rcx + r8 + 4]
0066476F  41 89 41 08                     mov dword ptr [r9 + 8], eax
00664773  42 0F B7 44 01 08               movzx eax, word ptr [rcx + r8 + 8]
00664779  66 41 89 41 0E                  mov word ptr [r9 + 0xe], ax
0066477E  4C 8B 46 20                     mov r8, qword ptr [rsi + 0x20]
00664782  41 0F B7 C2                     movzx eax, r10w
00664786  41 0F B6 50 64                  movzx edx, byte ptr [r8 + 0x64]
0066478B  41 8B 48 5C                     mov ecx, dword ptr [r8 + 0x5c]
0066478F  48 0F AF D0                     imul rdx, rax
00664793  41 0F B7 40 12                  movzx eax, word ptr [r8 + 0x12]
00664798  48 2B D0                        sub rdx, rax
0066479B  49 8D 04 10                     lea rax, [r8 + rdx]
0066479F  48 03 C8                        add rcx, rax
006647A2  8B 41 04                        mov eax, dword ptr [rcx + 4]
006647A5  41 89 41 04                     mov dword ptr [r9 + 4], eax
006647A9  0F B7 41 08                     movzx eax, word ptr [rcx + 8]
006647AD  66 41 89 41 0C                  mov word ptr [r9 + 0xc], ax
006647B2  0F B7 45 58                     movzx eax, word ptr [rbp + 0x58]
006647B6  66 41 89 01                     mov word ptr [r9], ax
006647BA  EB 07                           jmp 0x1406647c3
006647BC  45 8A D9                        mov r11b, r9b
006647BF  44 0F B7 F0                     movzx r14d, ax
006647C3  48 8B 56 20                     mov rdx, qword ptr [rsi + 0x20]
006647C7  41 0F B7 C5                     movzx eax, r13w
006647CB  0F B6 4A 34                     movzx ecx, byte ptr [rdx + 0x34]
006647CF  44 8B 42 2C                     mov r8d, dword ptr [rdx + 0x2c]
006647D3  48 0F AF C8                     imul rcx, rax
006647D7  0F B7 42 12                     movzx eax, word ptr [rdx + 0x12]
006647DB  48 2B C8                        sub rcx, rax
006647DE  48 8D 04 0A                     lea rax, [rdx + rcx]
006647E2  4C 03 C0                        add r8, rax
006647E5  41 80 48 0A 02                  or byte ptr [r8 + 0xa], 2
006647EA  45 84 DB                        test r11b, r11b
006647ED  66 45 89 50 04                  mov word ptr [r8 + 4], r10w
006647F2  41 BB 01 00 00 00               mov r11d, 1
006647F8  74 0A                           je 0x140664804
006647FA  66 45 01 58 08                  add word ptr [r8 + 8], r11w
006647FF  66 45 89 70 06                  mov word ptr [r8 + 6], r14w
00664804  48 8B 45 C8                     mov rax, qword ptr [rbp - 0x38]
00664808  48 85 C0                        test rax, rax
0066480B  74 41                           je 0x14066484e
0066480D  44 8B 48 10                     mov r9d, dword ptr [rax + 0x10]
00664811  4C 8B 46 20                     mov r8, qword ptr [rsi + 0x20]
00664815  4C 03 4E 28                     add r9, qword ptr [rsi + 0x28]
00664819  41 0F B7 C2                     movzx eax, r10w
0066481D  41 0F B6 48 64                  movzx ecx, byte ptr [r8 + 0x64]
00664822  41 8B 50 5C                     mov edx, dword ptr [r8 + 0x5c]
00664826  48 0F AF C8                     imul rcx, rax
0066482A  41 0F B7 40 12                  movzx eax, word ptr [r8 + 0x12]
0066482F  48 2B C8                        sub rcx, rax
00664832  49 8D 04 08                     lea rax, [r8 + rcx]
00664836  48 03 D0                        add rdx, rax
00664839  41 8B 40 24                     mov eax, dword ptr [r8 + 0x24]
0066483D  03 42 04                        add eax, dword ptr [rdx + 4]
00664840  41 89 41 0C                     mov dword ptr [r9 + 0xc], eax
00664844  0F B7 42 08                     movzx eax, word ptr [rdx + 8]
00664848  03 C0                           add eax, eax
0066484A  41 89 41 10                     mov dword ptr [r9 + 0x10], eax
0066484E  48 8B 4D D0                     mov rcx, qword ptr [rbp - 0x30]
00664852  66 41 03 FB                     add di, r11w
00664856  66 42 3B 7C B9 0A               cmp di, word ptr [rcx + r15*4 + 0xa]
0066485C  0F 82 09 FE FF FF               jb 0x14066466b
00664862  8B 4D C4                        mov ecx, dword ptr [rbp - 0x3c]
00664865  41 BD 01 00 00 00               mov r13d, 1
0066486B  41 0F B7 44 24 12               movzx eax, word ptr [r12 + 0x12]
00664871  41 03 CD                        add ecx, r13d
00664874  89 4D C4                        mov dword ptr [rbp - 0x3c], ecx
00664877  3B C8                           cmp ecx, eax
00664879  73 0C                           jae 0x140664887
0066487B  33 FF                           xor edi, edi
0066487D  E9 E9 F9 FF FF                  jmp 0x14066426b
00664882  BB 33 00 00 C0                  mov ebx, 0xc0000033
00664887  8B C3                           mov eax, ebx
00664889  48 8B 9C 24 B8 00 00 00         mov rbx, qword ptr [rsp + 0xb8]
00664891  48 83 C4 70                     add rsp, 0x70
00664895  41 5F                           pop r15
00664897  41 5E                           pop r14
00664899  41 5D                           pop r13
0066489B  41 5C                           pop r12
0066489D  5F                              pop rdi
0066489E  5E                              pop rsi
0066489F  5D                              pop rbp
006648A0  C3                              ret
006648A1  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall ApiSetCompose_ProcessV7Extension_Phase1(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m40;
    unsigned __int16 v_stack_m4E;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m54;
    unsigned __int8 v_stack_m56;
    unsigned __int16 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned int v_stack_m74;
    unsigned int v_stack_m78;
    unsigned __int8 v_stack_m88;
    unsigned __int64 v_stack_p10;
    unsigned int v_stack_p18;
    unsigned __int16 v_stack_p20;
    unsigned __int16 v_stack_p8;

    v_stack_p10 = v_rbx;
    v_rsp = (v_rsp) - (112);
    v_rdi = 0;
    if ((unsigned __int16)(*(unsigned __int16 *)(a1 + 16)) == 0) goto loc_0066425A;
    result = 0;
    v_stack_m40 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m58 = (unsigned __int16)(*(unsigned __int16 *)(a1 + 16));
    result = ((unsigned int)(*(unsigned int *)(a1 + 8))) + (a1);
    v_stack_m50 = v_xmm0;
    v_stack_m4E = (unsigned __int16)(*(unsigned __int16 *)(a1 + 16));
    v_stack_m60 = result;
    v_stack_m56 = 0;
    a4 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 89)) >> (1));
    a4 = (unsigned __int8)((a4) & ((unsigned __int8)(v_rdi + 1)));
    result = ApiSetpSearchForSectionIndex_V7(*(unsigned __int64 *)(a2 + 32), *(unsigned __int64 *)(a2 + 32) + 80, v_stack_m60, a4);
    if (((unsigned __int16)(result)) == ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_00664244;
    goto loc_00664887;
loc_00664244:
    result = ApiSetSchemaExpander_InsertExtensionNameEntry(a2, v_stack_m60, v_stack_m60, a4);
    if (sign_flag) goto loc_00664887;
loc_0066425A:
    v_stack_m74 = 0;
    if (0 >= (*(unsigned __int16 *)(a1 + 18))) goto loc_00664887;
loc_0066426B:
    a1 = 0;
    v_stack_m40 = 0;
    a3 = 0;
    v_stack_m60 = v_xmm0;
    result = ((unsigned int)(*(unsigned int *)(a1 + 12))) + (0);
    v_stack_m70 = 0 + 0 * 4;
    v_stack_m68 = result;
    v_stack_m50 = v_xmm0;
    a1 = ((unsigned int)(*(unsigned int *)(result + 0 + 0 * 4 * 4))) + (0);
    result = ApiSetpGetContractKeyInfo(a1, *(unsigned __int16 *)(result + 0 + 0 * 4 * 4 + 8), a3, v_stack_m60);
    if ((unsigned __int8)(result) == 0) goto loc_00664882;
    if (((unsigned int)((unsigned int)(v_stack_m54) - 1)) > 2) goto loc_00664882;
    a2 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 2))) & (16));
    v_stack_m88 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 55));
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 2)) & (8));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 53)) & (4)) == 0) goto loc_006642FF;
    a4 = ((unsigned __int8)(a2) != 0) ? 1 : 0;
    a3 = ((unsigned __int8)(a1) != 0) ? 1 : 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, (unsigned __int8)(v_rdi + 1), a3, a4);
    goto loc_00664317;
loc_006642FF:
    a4 = ((unsigned __int8)((unsigned __int8)(v_rdi + 1)) != 0) ? 1 : 0;
    a3 = ((unsigned __int8)(v_stack_m60) != 0) ? 1 : 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, (unsigned __int8)(v_rdi + 1), a3, a4);
loc_00664317:
    v_stack_p18 = (unsigned int)(result);
    result = ApiSetpSearchForSectionIndex_V7(*(unsigned __int64 *)(a2 + 32), *(unsigned __int64 *)(a2 + 32) + 44, v_stack_m60, (unsigned __int8)(v_rdi + 1));
    v_stack_p8 = (unsigned __int16)((unsigned __int16)(result));
    if (((unsigned __int16)((unsigned __int16)(result))) == ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_0066436E;
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 52)) * ((unsigned __int16)(result));
    a2 = (a2) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    v_rdi = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 44))) + (*(unsigned __int64 *)(a2 + 32) + a2 * 1);
    if ((*(unsigned int *)(v_rdi)) == ((unsigned int)((unsigned int)(v_stack_p18)))) goto loc_00664391;
loc_00664364:
    goto loc_00664887;
loc_0066436E:
    result = ApiSetSchemaExpander_InsertContractEntry(a2, v_stack_m60, v_stack_p8, (unsigned __int8)(v_rdi + 1));
    if (sign_flag) goto loc_00664887;
loc_00664391:
    v_stack_p18 = (unsigned __int16)((unsigned int)(0xFFFFULL));
    v_stack_p20 = (unsigned __int16)((unsigned int)(0xFFFFULL));
    if (((unsigned int)((unsigned int)(v_stack_m54))) != 1) goto loc_006643CB;
    if (v_rdi == 0) goto loc_00664625;
    v_stack_p18 = (unsigned __int16)(*(unsigned __int16 *)(v_rdi + 4));
    v_stack_p20 = (unsigned __int16)(*(unsigned __int16 *)(v_rdi + 6));
    goto loc_0066459C;
loc_006643CB:
    a1 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 2)) & (8));
    a2 = (unsigned __int8)(((unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 2))) & (16));
    if (((unsigned int)((unsigned int)(v_stack_m54))) != 2) goto loc_006644CD;
    v_stack_m88 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 67));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 65)) & (4)) == 0) goto loc_0066440F;
    a4 = ((unsigned __int8)(a2) != 0) ? 1 : 0;
    a3 = ((unsigned __int8)(a1) != 0) ? 1 : 0;
    a2 = 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, a2, a3, a4);
    goto loc_00664426;
loc_0066440F:
    a4 = (0 != 0) ? 1 : 0;
    a3 = ((unsigned __int8)(v_stack_m60) != 0) ? 1 : 0;
    a2 = 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, a2, a3, a4);
loc_00664426:
    a4 = 0;
    v_stack_m78 = (unsigned int)(result);
    result = ApiSetpSearchForSectionIndex_V7(*(unsigned __int64 *)(a2 + 32), *(unsigned __int64 *)(a2 + 32) + 56, v_stack_m60, a4);
    v_stack_p8 = (unsigned __int16)((unsigned __int16)(result));
    if (((unsigned __int16)((unsigned __int16)(result))) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_00664478;
    result = ApiSetSchemaExpander_InsertGroupContractEntry(0, v_stack_m60, v_stack_p8, (unsigned __int16)(result));
loc_00664460:
    if (sign_flag) goto loc_00664887;
    goto loc_006645A4;
loc_00664478:
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 64)) * (v_stack_p8);
    a2 = (a2) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 56)));
    a2 = (a2) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    if ((*(unsigned int *)(a2 + *(unsigned __int64 *)(a2 + 32) * 1)) != ((unsigned int)((unsigned int)(v_stack_m78)))) goto loc_00664364;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 52)) * (*(unsigned __int16 *)(a2 + *(unsigned __int64 *)(a2 + 32) * 1 + 4));
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 44)));
    a1 = (a1) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    v_stack_p20 = (unsigned __int16)(*(unsigned __int16 *)(a1 + *(unsigned __int64 *)(a2 + 32) * 1 + 6));
    v_stack_p18 = (unsigned __int16)(*(unsigned __int16 *)(a1 + *(unsigned __int64 *)(a2 + 32) * 1 + 4));
    goto loc_0066459C;
loc_006644CD:
    v_stack_m88 = (unsigned __int8)(*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 79));
    if (((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 77)) & (4)) == 0) goto loc_006644F8;
    a4 = ((unsigned __int8)(a2) != 0) ? 1 : 0;
    a3 = ((unsigned __int8)(*(unsigned __int16 *)(a1 + *(unsigned __int64 *)(a2 + 32) * 1 + 6)) != 0) ? 1 : 0;
    a2 = 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, a2, a3, a4);
    goto loc_0066450F;
loc_006644F8:
    a4 = (0 != 0) ? 1 : 0;
    a3 = ((unsigned __int8)(v_stack_m60) != 0) ? 1 : 0;
    a2 = 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, a2, a3, a4);
loc_0066450F:
    a4 = 0;
    v_stack_m78 = (unsigned int)(result);
    result = ApiSetpSearchForSectionIndex_V7(*(unsigned __int64 *)(a2 + 32), *(unsigned __int64 *)(a2 + 32) + 68, v_stack_m60, a4);
    v_stack_p8 = (unsigned __int16)((unsigned __int16)(result));
    if (((unsigned __int16)((unsigned __int16)(result))) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_0066454E;
    result = ApiSetSchemaExpander_InsertSemverContractEntry(0, v_stack_m60, v_stack_p8, (unsigned __int16)(result));
    goto loc_00664460;
loc_0066454E:
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 76)) * ((unsigned __int16)(result));
    a2 = (a2) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 68)));
    a2 = (a2) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    if ((*(unsigned int *)(a2 + *(unsigned __int64 *)(a2 + 32) * 1)) != ((unsigned int)((unsigned int)(v_stack_m78)))) goto loc_00664364;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 52)) * (*(unsigned __int16 *)(a2 + *(unsigned __int64 *)(a2 + 32) * 1 + 4));
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 44)));
    a1 = (a1) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    v_stack_p18 = (unsigned __int16)(*(unsigned __int16 *)(a1 + *(unsigned __int64 *)(a2 + 32) * 1 + 4));
    v_stack_p20 = (unsigned __int16)(*(unsigned __int16 *)(a1 + *(unsigned __int64 *)(a2 + 32) * 1 + 6));
loc_0066459C:
    if ((((unsigned __int8)(*(unsigned __int8 *)(a2 + *(unsigned __int64 *)(a2 + 32) * 1 + 10))) & (1)) != 0) goto loc_00664862;
loc_006645A4:
    if (((unsigned int)((unsigned int)(v_stack_m54))) != 2) goto loc_006645E5;
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 64)) * ((unsigned __int16)((unsigned __int16)(result)));
    a2 = (a2) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 56))) + (*(unsigned __int64 *)(a2 + 32) + a2 * 1);
    *(unsigned __int16 *)(a1 + 4) = (unsigned __int16)(v_stack_p8);
    *(unsigned int *)(a1 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m68 + v_stack_m70 * 4 + 12)));
    goto loc_00664629;
loc_006645E5:
    if (((unsigned int)((unsigned int)(v_stack_m54))) != 3) goto loc_00664629;
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 76)) * ((unsigned __int16)((unsigned __int16)(result)));
    a1 = (a1) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    a3 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 68))) + (*(unsigned __int64 *)(a2 + 32) + a1 * 1);
    *(unsigned __int16 *)(a3 + 4) = (unsigned __int16)(v_stack_p8);
    if (((*(unsigned __int8 *)(v_stack_m68 + v_stack_m70 * 4 + 17)) & (4)) == 0) goto loc_00664629;
    goto loc_00664629;
loc_00664625:
loc_00664629:
    result = 0;
    v_stack_m70 = 0;
    if ((*(unsigned __int8 *)(a2 + 16)) == 0) goto loc_00664652;
    if (((unsigned int)((unsigned int)(v_stack_m54))) == 3) {
        a3 = v_stack_m4E;
        a2 = v_stack_m60;
        a1 = *(unsigned __int64 *)(a2 + 40);
        result = ApiSetpSearchForApiSetA(a1, a2, a3, (unsigned __int16)(result));
        v_stack_m70 = result;
        result = 0;
    }
    if (0 >= (*(unsigned __int16 *)(v_stack_m68 + v_stack_m70 * 4 + 10))) goto loc_00664862;
loc_0066466B:
    result = (0) << (4);
    result = (result) + (a1);
    v_r14 = ((unsigned int)(*(unsigned int *)(v_stack_m68 + v_stack_m70 * 4 + 4))) + (result);
    result = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m40 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m58 = (unsigned __int16)(*(unsigned __int16 *)(v_r14 + 8));
    result = ((unsigned int)(*(unsigned int *)(v_r14))) + (a1);
    v_stack_m4E = (unsigned __int16)(*(unsigned __int16 *)(v_r14 + 8));
    v_stack_m60 = result;
    v_stack_m56 = 1;
    a4 = (unsigned __int8)((*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 101)) >> (1));
    a4 = (unsigned __int8)((a4) & (1));
    result = ApiSetpSearchForSectionIndex_V7(*(unsigned __int64 *)(a2 + 32), *(unsigned __int64 *)(a2 + 32) + 92, v_stack_m60, a4);
    v_stack_p8 = (unsigned __int16)(result);
    if (((unsigned __int16)((unsigned __int16)(result))) != ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_00664700;
    result = ApiSetSchemaExpander_InsertHostEntry(a2, v_stack_m60, v_stack_p8, a4);
    a4 = 0;
    if (sign_flag) goto loc_00664887;
    goto loc_00664703;
loc_00664700:
    a4 = 0;
loc_00664703:
    if ((*(unsigned __int16 *)(v_r14 + 10)) == 0) goto loc_006647BC;
    if (v_stack_p18 == ((unsigned __int16)((unsigned int)(0xFFFFULL)))) goto loc_00664364;
    v_r14 = (unsigned int)(((unsigned int)(*(unsigned int *)(a2 + 156))) >> (4));
    *(unsigned int *)(a2 + 156) = (unsigned int)((unsigned int)(*(unsigned int *)(a2 + 156)) + 16);
    a4 = (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 114)) * ((unsigned __int16)(v_r14));
    a4 = (a4) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 104)));
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 100)) * (v_stack_p18);
    a4 = (a4) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    a1 = (a1) + ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 92)));
    a4 = (a4) + (*(unsigned __int64 *)(a2 + 32));
    a1 = (a1) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    *(unsigned int *)(a4 + 8) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + *(unsigned __int64 *)(a2 + 32) * 1 + 4)));
    *(unsigned __int16 *)(a4 + 14) = (unsigned __int16)(*(unsigned __int16 *)(a1 + *(unsigned __int64 *)(a2 + 32) * 1 + 8));
    a2 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 100)) * ((unsigned __int16)(v_stack_p8));
    a2 = (a2) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    a1 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 92))) + (*(unsigned __int64 *)(a2 + 32) + a2 * 1);
    *(unsigned int *)(a4 + 4) = (unsigned int)((unsigned int)(*(unsigned int *)(a1 + 4)));
    *(unsigned __int16 *)(a4 + 12) = (unsigned __int16)(*(unsigned __int16 *)(a1 + 8));
    *(unsigned __int16 *)(a4) = (unsigned __int16)(v_stack_p20);
    goto loc_006647C3;
loc_006647BC:
loc_006647C3:
    a1 = (*(unsigned __int8 *)(*(unsigned __int64 *)(a2 + 32) + 52)) * ((unsigned __int16)(v_stack_p8));
    a1 = (a1) - (*(unsigned __int16 *)(*(unsigned __int64 *)(a2 + 32) + 18));
    a3 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a2 + 32) + 44))) + (*(unsigned __int64 *)(a2 + 32) + a1 * 1);
    *(unsigned __int16 *)(a3 + 4) = (unsigned __int16)(v_stack_p8);
    if ((unsigned __int8)((unsigned __int8)(a4)) != 0) {
        *(unsigned __int16 *)(a3 + 6) = (unsigned __int16)((unsigned __int16)(v_stack_p20));
    }
    result = v_stack_m70;
    if (v_stack_m70 != 0) {
        a4 = *(unsigned int *)(v_stack_m70 + 16);
        a3 = *(unsigned __int64 *)(a2 + 32);
        a4 = (a4) + (*(unsigned __int64 *)(a2 + 40));
        result = (unsigned __int16)(v_stack_p8);
        a1 = *(unsigned __int8 *)(a3 + 100);
        a2 = *(unsigned int *)(a3 + 92);
        a1 = (a1) * (result);
        result = *(unsigned __int16 *)(a3 + 18);
        a1 = (a1) - (result);
        result = a3 + a1 * 1;
        a2 = (a2) + (result);
        result = *(unsigned int *)(a3 + 36);
        result = (unsigned int)((result) + (*(unsigned int *)(a2 + 4)));
        *(unsigned int *)(a4 + 12) = (unsigned int)(result);
        result = *(unsigned __int16 *)(a2 + 8);
        result = (unsigned int)((result) + ((unsigned int)(result)));
        *(unsigned int *)(a4 + 16) = (unsigned int)(result);
    }
    v_rdi = (unsigned __int16)((0) + (1));
    if (((unsigned __int16)(v_rdi)) < (*(unsigned __int16 *)(v_stack_m68 + v_stack_m70 * 4 + 10))) goto loc_0066466B;
loc_00664862:
    a1 = (unsigned int)(((unsigned int)(v_stack_m74)) + (1));
    v_stack_m74 = (unsigned int)(a1);
    if (((unsigned int)(a1)) >= ((unsigned int)(*(unsigned __int16 *)(a1 + 18)))) goto loc_00664887;
    v_rdi = 0;
    goto loc_0066426B;
loc_00664882:
loc_00664887:
    v_rsp = (v_rsp) + (112);
    return (unsigned int)((unsigned int)((unsigned int)(0xC0000033ULL)));
}
```

## 5. (Beta) C Style

```c
int64_t ApiSetCompose_ProcessV7Extension_Phase1(void *Arg1, void *Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m40;
    uint16_t v_stack_m4E;
    uint64_t v_stack_m50;
    uint32_t v_stack_m54;
    uint8_t v_stack_m56;
    uint16_t v_stack_m58;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint32_t v_stack_m74;
    uint32_t v_stack_m78;
    uint8_t v_stack_m88;
    uint64_t v_stack_p10;
    uint32_t v_stack_p18;
    uint16_t v_stack_p20;
    uint16_t v_stack_p8;

    v_stack_p10 = local_rbx;
    local_rsp = (local_rsp) - (112);
    local_rdi = 0;
    if ((uint16_t)(*(uint16_t *)(arg1 + 0x10)) == 0) goto loc_0066425A;
    result = 0;
    v_stack_m40 = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m58 = (uint16_t)(*(uint16_t *)(arg1 + 0x10));
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0x8))) + (Arg1);
    v_stack_m50 = v_xmm0;
    v_stack_m4E = (uint16_t)(*(uint16_t *)(arg1 + 0x10));
    v_stack_m60 = result;
    v_stack_m56 = 0;
    a4 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x59)) >> (1));
    a4 = (uint8_t)((a4) & ((uint8_t)(local_rdi + 1)));
    result = ApiSetpSearchForSectionIndex_V7(*(uint64_t *)(arg2 + 0x20), *(uint64_t *)(arg2 + 0x20) + 80, v_stack_m60, a4);
    if (((uint16_t)(result)) == ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_00664244;
    goto loc_00664887;
loc_00664244:
    result = ApiSetSchemaExpander_InsertExtensionNameEntry(Arg2, v_stack_m60, v_stack_m60, a4);
    if (sign_flag) goto loc_00664887;
loc_0066425A:
    v_stack_m74 = 0;
    if (0 >= (*(uint16_t *)(arg1 + 0x12))) goto loc_00664887;
loc_0066426B:
    Arg1 = 0;
    v_stack_m40 = 0;
    a3 = 0;
    v_stack_m60 = v_xmm0;
    result = ((uint32_t)(*(uint32_t *)(arg1 + 0xC))) + (0);
    v_stack_m70 = 0 + 0 * 4;
    v_stack_m68 = result;
    v_stack_m50 = v_xmm0;
    Arg1 = ((uint32_t)(*(uint32_t *)(result + 0x0 + 0x0 * 4 * 4))) + (0);
    result = ApiSetpGetContractKeyInfo(Arg1, *(uint16_t *)(result + 0x0 + 0x0 * 4 * 4 + 0x8), a3, v_stack_m60);
    if ((uint8_t)(result) == 0) goto loc_00664882;
    if (((uint32_t)((uint32_t)(v_stack_m54) - 1)) > 2) goto loc_00664882;
    Arg2 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x2))) & (16));
    v_stack_m88 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x37));
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x2)) & (8));
    if (((*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x35)) & (4)) == 0) goto loc_006642FF;
    a4 = ((uint8_t)(Arg2) != 0) ? 1 : 0;
    a3 = ((uint8_t)(Arg1) != 0) ? 1 : 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, (uint8_t)(local_rdi + 1), a3, a4);
    goto loc_00664317;
loc_006642FF:
    a4 = ((uint8_t)((uint8_t)(local_rdi + 1)) != 0) ? 1 : 0;
    a3 = ((uint8_t)(v_stack_m60) != 0) ? 1 : 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, (uint8_t)(local_rdi + 1), a3, a4);
loc_00664317:
    v_stack_p18 = (uint32_t)(result);
    result = ApiSetpSearchForSectionIndex_V7(*(uint64_t *)(arg2 + 0x20), *(uint64_t *)(arg2 + 0x20) + 44, v_stack_m60, (uint8_t)(local_rdi + 1));
    v_stack_p8 = (uint16_t)((uint16_t)(result));
    if (((uint16_t)((uint16_t)(result))) == ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_0066436E;
    Arg2 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x34)) * ((uint16_t)(result));
    Arg2 = (Arg2) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    local_rdi = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x2C))) + (*(uint64_t *)(arg2 + 0x20) + Arg2 * 1);
    if ((*(uint32_t *)(local_rdi)) == ((uint32_t)((uint32_t)(v_stack_p18)))) goto loc_00664391;
loc_00664364:
    goto loc_00664887;
loc_0066436E:
    result = ApiSetSchemaExpander_InsertContractEntry(Arg2, v_stack_m60, v_stack_p8, (uint8_t)(local_rdi + 1));
    if (sign_flag) goto loc_00664887;
loc_00664391:
    v_stack_p18 = (uint16_t)((uint32_t)(0xFFFFULL));
    v_stack_p20 = (uint16_t)((uint32_t)(0xFFFFULL));
    if (((uint32_t)((uint32_t)(v_stack_m54))) != 1) goto loc_006643CB;
    if (local_rdi == 0) goto loc_00664625;
    v_stack_p18 = (uint16_t)(*(uint16_t *)(local_rdi + 0x4));
    v_stack_p20 = (uint16_t)(*(uint16_t *)(local_rdi + 0x6));
    goto loc_0066459C;
loc_006643CB:
    Arg1 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x2)) & (8));
    Arg2 = (uint8_t)(((uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x2))) & (16));
    if (((uint32_t)((uint32_t)(v_stack_m54))) != 2) goto loc_006644CD;
    v_stack_m88 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x43));
    if (((*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x41)) & (4)) == 0) goto loc_0066440F;
    a4 = ((uint8_t)(Arg2) != 0) ? 1 : 0;
    a3 = ((uint8_t)(Arg1) != 0) ? 1 : 0;
    Arg2 = 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, Arg2, a3, a4);
    goto loc_00664426;
loc_0066440F:
    a4 = (0 != 0) ? 1 : 0;
    a3 = ((uint8_t)(v_stack_m60) != 0) ? 1 : 0;
    Arg2 = 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, Arg2, a3, a4);
loc_00664426:
    a4 = 0;
    v_stack_m78 = (uint32_t)(result);
    result = ApiSetpSearchForSectionIndex_V7(*(uint64_t *)(arg2 + 0x20), *(uint64_t *)(arg2 + 0x20) + 56, v_stack_m60, a4);
    v_stack_p8 = (uint16_t)((uint16_t)(result));
    if (((uint16_t)((uint16_t)(result))) != ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_00664478;
    result = ApiSetSchemaExpander_InsertGroupContractEntry(0, v_stack_m60, v_stack_p8, (uint16_t)(result));
loc_00664460:
    if (sign_flag) goto loc_00664887;
    goto loc_006645A4;
loc_00664478:
    Arg2 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x40)) * (v_stack_p8);
    Arg2 = (Arg2) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x38)));
    Arg2 = (Arg2) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    if ((*(uint32_t *)(arg2 + *(uint64_t *)(arg2 + 0x20) * 1)) != ((uint32_t)((uint32_t)(v_stack_m78)))) goto loc_00664364;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x34)) * (*(uint16_t *)(arg2 + *(uint64_t *)(arg2 + 0x20) * 1 + 0x4));
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x2C)));
    Arg1 = (Arg1) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    v_stack_p20 = (uint16_t)(*(uint16_t *)(arg1 + *(uint64_t *)(arg2 + 0x20) * 1 + 0x6));
    v_stack_p18 = (uint16_t)(*(uint16_t *)(arg1 + *(uint64_t *)(arg2 + 0x20) * 1 + 0x4));
    goto loc_0066459C;
loc_006644CD:
    v_stack_m88 = (uint8_t)(*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x4F));
    if (((*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x4D)) & (4)) == 0) goto loc_006644F8;
    a4 = ((uint8_t)(Arg2) != 0) ? 1 : 0;
    a3 = ((uint8_t)(*(uint16_t *)(arg1 + *(uint64_t *)(arg2 + 0x20) * 1 + 0x6)) != 0) ? 1 : 0;
    Arg2 = 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, Arg2, a3, a4);
    goto loc_0066450F;
loc_006644F8:
    a4 = (0 != 0) ? 1 : 0;
    a3 = ((uint8_t)(v_stack_m60) != 0) ? 1 : 0;
    Arg2 = 0;
    result = ApiSetpGetSearchKeyHash(v_stack_m60, Arg2, a3, a4);
loc_0066450F:
    a4 = 0;
    v_stack_m78 = (uint32_t)(result);
    result = ApiSetpSearchForSectionIndex_V7(*(uint64_t *)(arg2 + 0x20), *(uint64_t *)(arg2 + 0x20) + 68, v_stack_m60, a4);
    v_stack_p8 = (uint16_t)((uint16_t)(result));
    if (((uint16_t)((uint16_t)(result))) != ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_0066454E;
    result = ApiSetSchemaExpander_InsertSemverContractEntry(0, v_stack_m60, v_stack_p8, (uint16_t)(result));
    goto loc_00664460;
loc_0066454E:
    Arg2 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x4C)) * ((uint16_t)(result));
    Arg2 = (Arg2) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x44)));
    Arg2 = (Arg2) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    if ((*(uint32_t *)(arg2 + *(uint64_t *)(arg2 + 0x20) * 1)) != ((uint32_t)((uint32_t)(v_stack_m78)))) goto loc_00664364;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x34)) * (*(uint16_t *)(arg2 + *(uint64_t *)(arg2 + 0x20) * 1 + 0x4));
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x2C)));
    Arg1 = (Arg1) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    v_stack_p18 = (uint16_t)(*(uint16_t *)(arg1 + *(uint64_t *)(arg2 + 0x20) * 1 + 0x4));
    v_stack_p20 = (uint16_t)(*(uint16_t *)(arg1 + *(uint64_t *)(arg2 + 0x20) * 1 + 0x6));
loc_0066459C:
    if ((((uint8_t)(*(uint8_t *)(arg2 + *(uint64_t *)(arg2 + 0x20) * 1 + 0xA))) & (1)) != 0) goto loc_00664862;
loc_006645A4:
    if (((uint32_t)((uint32_t)(v_stack_m54))) != 2) goto loc_006645E5;
    Arg2 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x40)) * ((uint16_t)((uint16_t)(result)));
    Arg2 = (Arg2) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x38))) + (*(uint64_t *)(arg2 + 0x20) + Arg2 * 1);
    *(uint16_t *)(arg1 + 0x4) = (uint16_t)(v_stack_p8);
    *(uint32_t *)(arg1 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m68 + v_stack_m70 * 4 + 0xC)));
    goto loc_00664629;
loc_006645E5:
    if (((uint32_t)((uint32_t)(v_stack_m54))) != 3) goto loc_00664629;
    Arg1 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x4C)) * ((uint16_t)((uint16_t)(result)));
    Arg1 = (Arg1) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    a3 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x44))) + (*(uint64_t *)(arg2 + 0x20) + Arg1 * 1);
    *(uint16_t *)(a3 + 0x4) = (uint16_t)(v_stack_p8);
    if (((*(uint8_t *)(v_stack_m68 + v_stack_m70 * 4 + 0x11)) & (4)) == 0) goto loc_00664629;
    goto loc_00664629;
loc_00664625:
loc_00664629:
    result = 0;
    v_stack_m70 = 0;
    if ((*(uint8_t *)(arg2 + 0x10)) == 0) goto loc_00664652;
    if (((uint32_t)((uint32_t)(v_stack_m54))) == 3) {
        a3 = v_stack_m4E;
        Arg2 = v_stack_m60;
        Arg1 = *(uint64_t *)(arg2 + 0x28);
        result = ApiSetpSearchForApiSetA(Arg1, Arg2, a3, (uint16_t)(result));
        v_stack_m70 = result;
        result = 0;
    }
    if (0 >= (*(uint16_t *)(v_stack_m68 + v_stack_m70 * 4 + 0xA))) goto loc_00664862;
loc_0066466B:
    result = (0) << (4);
    result = (result) + (Arg1);
    local_r14 = ((uint32_t)(*(uint32_t *)(v_stack_m68 + v_stack_m70 * 4 + 0x4))) + (result);
    result = 0;
    v_stack_m60 = v_xmm0;
    v_stack_m40 = 0;
    v_stack_m50 = v_xmm0;
    v_stack_m58 = (uint16_t)(*(uint16_t *)(local_r14 + 0x8));
    result = ((uint32_t)(*(uint32_t *)(local_r14))) + (Arg1);
    v_stack_m4E = (uint16_t)(*(uint16_t *)(local_r14 + 0x8));
    v_stack_m60 = result;
    v_stack_m56 = 1;
    a4 = (uint8_t)((*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x65)) >> (1));
    a4 = (uint8_t)((a4) & (1));
    result = ApiSetpSearchForSectionIndex_V7(*(uint64_t *)(arg2 + 0x20), *(uint64_t *)(arg2 + 0x20) + 92, v_stack_m60, a4);
    v_stack_p8 = (uint16_t)(result);
    if (((uint16_t)((uint16_t)(result))) != ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_00664700;
    result = ApiSetSchemaExpander_InsertHostEntry(Arg2, v_stack_m60, v_stack_p8, a4);
    a4 = 0;
    if (sign_flag) goto loc_00664887;
    goto loc_00664703;
loc_00664700:
    a4 = 0;
loc_00664703:
    if ((*(uint16_t *)(local_r14 + 0xA)) == 0) goto loc_006647BC;
    if (v_stack_p18 == ((uint16_t)((uint32_t)(0xFFFFULL)))) goto loc_00664364;
    local_r14 = (uint32_t)(((uint32_t)(*(uint32_t *)(arg2 + 0x9C))) >> (4));
    *(uint32_t *)(arg2 + 0x9C) = (uint32_t)((uint32_t)(*(uint32_t *)(arg2 + 0x9C)) + 16);
    a4 = (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x72)) * ((uint16_t)(local_r14));
    a4 = (a4) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x68)));
    Arg1 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x64)) * (v_stack_p18);
    a4 = (a4) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    Arg1 = (Arg1) + ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x5C)));
    a4 = (a4) + (*(uint64_t *)(arg2 + 0x20));
    Arg1 = (Arg1) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    *(uint32_t *)(a4 + 0x8) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + *(uint64_t *)(arg2 + 0x20) * 1 + 0x4)));
    *(uint16_t *)(a4 + 0xE) = (uint16_t)(*(uint16_t *)(arg1 + *(uint64_t *)(arg2 + 0x20) * 1 + 0x8));
    Arg2 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x64)) * ((uint16_t)(v_stack_p8));
    Arg2 = (Arg2) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    Arg1 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x5C))) + (*(uint64_t *)(arg2 + 0x20) + Arg2 * 1);
    *(uint32_t *)(a4 + 0x4) = (uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x4)));
    *(uint16_t *)(a4 + 0xC) = (uint16_t)(*(uint16_t *)(arg1 + 0x8));
    *(uint16_t *)(a4) = (uint16_t)(v_stack_p20);
    goto loc_006647C3;
loc_006647BC:
loc_006647C3:
    Arg1 = (*(uint8_t *)(*(uint64_t *)(arg2 + 0x20) + 0x34)) * ((uint16_t)(v_stack_p8));
    Arg1 = (Arg1) - (*(uint16_t *)(*(uint64_t *)(arg2 + 0x20) + 0x12));
    a3 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg2 + 0x20) + 0x2C))) + (*(uint64_t *)(arg2 + 0x20) + Arg1 * 1);
    *(uint16_t *)(a3 + 0x4) = (uint16_t)(v_stack_p8);
    if ((uint8_t)((uint8_t)(a4)) != 0) {
        *(uint16_t *)(a3 + 0x6) = (uint16_t)((uint16_t)(v_stack_p20));
    }
    result = v_stack_m70;
    if (v_stack_m70 != 0) {
        a4 = *(uint32_t *)(v_stack_m70 + 0x10);
        a3 = *(uint64_t *)(arg2 + 0x20);
        a4 = (a4) + (*(uint64_t *)(arg2 + 0x28));
        result = (uint16_t)(v_stack_p8);
        Arg1 = *(uint8_t *)(a3 + 0x64);
        Arg2 = *(uint32_t *)(a3 + 0x5C);
        Arg1 = (Arg1) * (result);
        result = *(uint16_t *)(a3 + 0x12);
        Arg1 = (Arg1) - (result);
        result = a3 + Arg1 * 1;
        Arg2 = (Arg2) + (result);
        result = *(uint32_t *)(a3 + 0x24);
        result = (uint32_t)((result) + (*(uint32_t *)(arg2 + 0x4)));
        *(uint32_t *)(a4 + 0xC) = (uint32_t)(result);
        result = *(uint16_t *)(arg2 + 0x8);
        result = (uint32_t)((result) + ((uint32_t)(result)));
        *(uint32_t *)(a4 + 0x10) = (uint32_t)(result);
    }
    local_rdi = (uint16_t)((0) + (1));
    if (((uint16_t)(local_rdi)) < (*(uint16_t *)(v_stack_m68 + v_stack_m70 * 4 + 0xA))) goto loc_0066466B;
loc_00664862:
    Arg1 = (uint32_t)(((uint32_t)(v_stack_m74)) + (1));
    v_stack_m74 = (uint32_t)(Arg1);
    if (((uint32_t)(Arg1)) >= ((uint32_t)(*(uint16_t *)(arg1 + 0x12)))) goto loc_00664887;
    local_rdi = 0;
    goto loc_0066426B;
loc_00664882:
loc_00664887:
    local_rsp = (local_rsp) + (112);
    return (uint32_t)((uint32_t)((uint32_t)(0xC0000033ULL)));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `32` | `R` |
| `Arg1` | `+ 0xC` | `32` | `R` |
| `Arg1` | `+ 0x10` | `16` | `R` |
| `Arg1` | `+ 0x12` | `16` | `R` |
| `Arg2` | `+ 0x10` | `8` | `R` |
| `Arg2` | `+ 0x20` | `64` | `R` |
| `Arg2` | `+ 0x28` | `64` | `R` |
| `Arg2` | `+ 0x9C` | `32` | `R` |
| `Arg2` | `+ 0x9C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x006641BC&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
