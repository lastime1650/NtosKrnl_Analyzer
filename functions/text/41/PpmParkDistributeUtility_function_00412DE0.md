# PpmParkDistributeUtility

- RVA: `0x00412DE0`–`0x0041338E` (길이 `1,454` bytes)
- VA: `0x0000000140412DE0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0009BF60`
- 디코드: `371`개 명령, `1,454/1,454` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00412F3F` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004131F2` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004132C1` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)
- `0x004132E1` → [PpmHeteroUtilityToNormalizedUtility](PpmHeteroUtilityToNormalizedUtility_function_00413394.md) (function, `0x00413394`)
- `0x0041331B` → [KeGetPrcb](../2D/KeGetPrcb_function_002D85D0.md) (function, `0x002D85D0`)

### Direct callers
- [PpmParkDistributeAllUtility](PpmParkDistributeAllUtility_function_00412D10.md) at `0x00412D99`
- [sub_006FAB60](../6F/Unknown_function_006FAB60.md) at `0x006FAB9E`
- [sub_006FAB60](../6F/Unknown_function_006FAB60.md) at `0x006FAC55`
- [sub_006FAB60](../6F/Unknown_function_006FAB60.md) at `0x006FACB4`
- [sub_006FAB60](../6F/Unknown_function_006FAB60.md) at `0x006FAD05`
- [sub_006FAB60](../6F/Unknown_function_006FAB60.md) at `0x006FAD3D`

### Static image references
- `0x00412E02` → RVA `0x00FC8C40` (`ALMOSTRO`; read)
- `0x00412E69` → RVA `0x00F231B8` (`.data`; read)
- `0x00412E74` → RVA `0x00FC6A80` (`ALMOSTRO`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00412DE0  66 44 89 44 24 18               mov word ptr [rsp + 0x18], r8w
00412DE6  48 89 54 24 10                  mov qword ptr [rsp + 0x10], rdx
00412DEB  53                              push rbx
00412DEC  55                              push rbp
00412DED  56                              push rsi
00412DEE  57                              push rdi
00412DEF  41 54                           push r12
00412DF1  41 55                           push r13
00412DF3  41 56                           push r14
00412DF5  41 57                           push r15
00412DF7  48 83 EC 38                     sub rsp, 0x38
00412DFB  8B B4 24 A8 00 00 00            mov esi, dword ptr [rsp + 0xa8]
00412E02  4C 8D 35 37 5E BB 00            lea r14, [rip + 0xbb5e37]
00412E09  45 33 E4                        xor r12d, r12d
00412E0C  45 0F B6 E9                     movzx r13d, r9b
00412E10  48 8B C1                        mov rax, rcx
00412E13  40 32 ED                        xor bpl, bpl
00412E16  45 32 FF                        xor r15b, r15b
00412E19  45 32 DB                        xor r11b, r11b
00412E1C  48 33 C2                        xor rax, rdx
00412E1F  41 8B FC                        mov edi, r12d
00412E22  41 0F B7 D0                     movzx edx, r8w
00412E26  48 8B D8                        mov rbx, rax
00412E29  89 94 24 A8 00 00 00            mov dword ptr [rsp + 0xa8], edx
00412E30  44 8B CA                        mov r9d, edx
00412E33  48 89 84 24 80 00 00 00         mov qword ptr [rsp + 0x80], rax
00412E3B  45 0F B7 D0                     movzx r10d, r8w
00412E3F  90                              nop
00412E40  44 89 A4 24 98 00 00 00         mov dword ptr [rsp + 0x98], r12d
00412E48  41 8D 49 01                     lea ecx, [r9 + 1]
00412E4C  48 85 C0                        test rax, rax
00412E4F  74 62                           je 0x140412eb3
00412E51  4C 0F BC C0                     bsf r8, rax
00412E55  41 8B D1                        mov edx, r9d
00412E58  41 0F B6 C8                     movzx ecx, r8b
00412E5C  48 0F B3 C8                     btr rax, rcx
00412E60  C1 E2 06                        shl edx, 6
00412E63  41 0F B6 C8                     movzx ecx, r8b
00412E67  03 D1                           add edx, ecx
00412E69  48 8B 0D 48 03 B1 00            mov rcx, qword ptr [rip + 0xb10348]
00412E70  44 8B 04 91                     mov r8d, dword ptr [rcx + rdx*4]
00412E74  8B 0D 06 3C BB 00               mov ecx, dword ptr [rip + 0xbb3c06]
00412E7A  44 3B C1                        cmp r8d, ecx
00412E7D  0F 83 AF 04 00 00               jae 0x140413332
00412E83  0F AE E8                        lfence
00412E86  4B 8B 14 C6                     mov rdx, qword ptr [r14 + r8*8]
00412E8A  44 38 A2 08 8A 00 00            cmp byte ptr [rdx + 0x8a08], r12b
00412E91  75 3E                           jne 0x140412ed1
00412E93  41 FE C7                        inc r15b
00412E96  8B 8A D8 89 00 00               mov ecx, dword ptr [rdx + 0x89d8]
00412E9C  8B 92 F0 89 00 00               mov edx, dword ptr [rdx + 0x89f0]
00412EA2  85 D2                           test edx, edx
00412EA4  74 06                           je 0x140412eac
00412EA6  0F AF CA                        imul ecx, edx
00412EA9  C1 E9 10                        shr ecx, 0x10
00412EAC  03 F1                           add esi, ecx
00412EAE  40 FE C5                        inc bpl
00412EB1  EB 8D                           jmp 0x140412e40
00412EB3  66 41 FF C2                     inc r10w
00412EB7  45 0F B7 CA                     movzx r9d, r10w
00412EBB  44 3B C9                        cmp r9d, ecx
00412EBE  73 1D                           jae 0x140412edd
00412EC0  41 0F B7 C2                     movzx eax, r10w
00412EC4  48 8B 04 C5 08 00 00 00         mov rax, qword ptr [rax*8 + 8]
00412ECC  E9 7B FF FF FF                  jmp 0x140412e4c
00412ED1  41 FE C3                        inc r11b
00412ED4  48 0B BA C8 00 00 00            or rdi, qword ptr [rdx + 0xc8]
00412EDB  EB B9                           jmp 0x140412e96
00412EDD  44 0F B7 A4 24 90 00 00 00      movzx r12d, word ptr [rsp + 0x90]
00412EE6  4C 8B B4 24 88 00 00 00         mov r14, qword ptr [rsp + 0x88]
00412EEE  48 89 7C 24 28                  mov qword ptr [rsp + 0x28], rdi
00412EF3  8B BC 24 A8 00 00 00            mov edi, dword ptr [rsp + 0xa8]
00412EFA  44 88 9C 24 98 00 00 00         mov byte ptr [rsp + 0x98], r11b
00412F02  0F 1F 40 00                     nop dword ptr [rax]
00412F06  66 66 0F 1F 84 00 00 00 00 00   nop word ptr [rax + rax]
00412F10  C7 44 24 20 00 00 00 00         mov dword ptr [rsp + 0x20], 0
00412F18  8D 4F 01                        lea ecx, [rdi + 1]
00412F1B  4D 85 F6                        test r14, r14
00412F1E  74 44                           je 0x140412f64
00412F20  49 0F BC D6                     bsf rdx, r14
00412F24  8B CF                           mov ecx, edi
00412F26  0F B6 C2                        movzx eax, dl
00412F29  49 0F B3 C6                     btr r14, rax
00412F2D  C1 E1 06                        shl ecx, 6
00412F30  0F B6 C2                        movzx eax, dl
00412F33  03 C8                           add ecx, eax
00412F35  48 8B 05 7C 02 B1 00            mov rax, qword ptr [rip + 0xb1027c]
00412F3C  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
00412F3F  E8 8C 56 EC FF                  call 0x1402d85d0
00412F44  8B 90 D8 89 00 00               mov edx, dword ptr [rax + 0x89d8]
00412F4A  2B 90 DC 89 00 00               sub edx, dword ptr [rax + 0x89dc]
00412F50  8B 80 F0 89 00 00               mov eax, dword ptr [rax + 0x89f0]
00412F56  85 C0                           test eax, eax
00412F58  74 06                           je 0x140412f60
00412F5A  0F AF D0                        imul edx, eax
00412F5D  C1 EA 10                        shr edx, 0x10
00412F60  03 F2                           add esi, edx
00412F62  EB AC                           jmp 0x140412f10
00412F64  66 41 FF C4                     inc r12w
00412F68  41 0F B7 FC                     movzx edi, r12w
00412F6C  3B F9                           cmp edi, ecx
00412F6E  73 0E                           jae 0x140412f7e
00412F70  41 0F B7 C4                     movzx eax, r12w
00412F74  4C 8B 34 C5 08 00 00 00         mov r14, qword ptr [rax*8 + 8]
00412F7C  EB 9D                           jmp 0x140412f1b
00412F7E  B8 01 00 00 00                  mov eax, 1
00412F83  44 0F B6 C5                     movzx r8d, bpl
00412F87  40 3A E8                        cmp bpl, al
00412F8A  41 8B D5                        mov edx, r13d
00412F8D  44 0F 46 C0                     cmovbe r8d, eax
00412F91  45 3A E8                        cmp r13b, r8b
00412F94  41 0F B6 C8                     movzx ecx, r8b
00412F98  44 0F B6 AC 24 A0 00 00 00      movzx r13d, byte ptr [rsp + 0xa0]
00412FA1  0F 43 D1                        cmovae edx, ecx
00412FA4  41 0F B6 C8                     movzx ecx, r8b
00412FA8  3A D0                           cmp dl, al
00412FAA  0F B6 EA                        movzx ebp, dl
00412FAD  0F 46 E8                        cmovbe ebp, eax
00412FB0  33 D2                           xor edx, edx
00412FB2  8B C6                           mov eax, esi
00412FB4  F7 F1                           div ecx
00412FB6  33 D2                           xor edx, edx
00412FB8  40 0F B6 CD                     movzx ecx, bpl
00412FBC  8B F8                           mov edi, eax
00412FBE  8B C6                           mov eax, esi
00412FC0  F7 F1                           div ecx
00412FC2  44 8B E0                        mov r12d, eax
00412FC5  45 84 FF                        test r15b, r15b
00412FC8  74 0E                           je 0x140412fd8
00412FCA  80 BC 24 98 00 00 00 00         cmp byte ptr [rsp + 0x98], 0
00412FD2  0F 87 CD 01 00 00               ja 0x1404131a5
00412FD8  0F B7 B4 24 90 00 00 00         movzx esi, word ptr [rsp + 0x90]
00412FE0  4C 8B C3                        mov r8, rbx
00412FE3  44 8B 94 24 A8 00 00 00         mov r10d, dword ptr [rsp + 0xa8]
00412FEB  0F 1F 44 00 00                  nop dword ptr [rax + rax]
00412FF0  C7 84 24 98 00 00 00 00 00 00 00  mov dword ptr [rsp + 0x98], 0
00412FFB  41 8D 4A 01                     lea ecx, [r10 + 1]
00412FFF  4D 85 C0                        test r8, r8
00413002  0F 84 8A 00 00 00               je 0x140413092
00413008  49 0F BC D0                     bsf rdx, r8
0041300C  41 8B CA                        mov ecx, r10d
0041300F  0F B6 C2                        movzx eax, dl
00413012  49 0F B3 C0                     btr r8, rax
00413016  C1 E1 06                        shl ecx, 6
00413019  0F B6 C2                        movzx eax, dl
0041301C  03 C8                           add ecx, eax
0041301E  48 8B 05 93 01 B1 00            mov rax, qword ptr [rip + 0xb10193]
00413025  8B 14 88                        mov edx, dword ptr [rax + rcx*4]
00413028  8B 05 52 3A BB 00               mov eax, dword ptr [rip + 0xbb3a52]
0041302E  3B D0                           cmp edx, eax
00413030  0F 83 23 03 00 00               jae 0x140413359
00413036  0F AE E8                        lfence
00413039  48 8D 0D 00 5C BB 00            lea rcx, [rip + 0xbb5c00]
00413040  48 8B 0C D1                     mov rcx, qword ptr [rcx + rdx*8]
00413044  44 8B 89 F0 89 00 00            mov r9d, dword ptr [rcx + 0x89f0]
0041304B  44 8B 99 D8 89 00 00            mov r11d, dword ptr [rcx + 0x89d8]
00413052  45 85 C9                        test r9d, r9d
00413055  0F 84 0D 01 00 00               je 0x140413168
0041305B  41 8B C1                        mov eax, r9d
0041305E  41 0F AF C3                     imul eax, r11d
00413062  C1 E8 10                        shr eax, 0x10
00413065  3B F8                           cmp edi, eax
00413067  77 87                           ja 0x140412ff0
00413069  48 33 99 C8 00 00 00            xor rbx, qword ptr [rcx + 0xc8]
00413070  45 85 C9                        test r9d, r9d
00413073  74 58                           je 0x1404130cd
00413075  33 D2                           xor edx, edx
00413077  41 8B C4                        mov eax, r12d
0041307A  C1 E0 10                        shl eax, 0x10
0041307D  41 F7 F1                        div r9d
00413080  8B D0                           mov edx, eax
00413082  41 3B D3                        cmp edx, r11d
00413085  76 27                           jbe 0x1404130ae
00413087  89 91 D8 89 00 00               mov dword ptr [rcx + 0x89d8], edx
0041308D  E9 5E FF FF FF                  jmp 0x140412ff0
00413092  66 FF C6                        inc si
00413095  44 0F B7 D6                     movzx r10d, si
00413099  44 3B D1                        cmp r10d, ecx
0041309C  73 34                           jae 0x1404130d2
0041309E  0F B7 C6                        movzx eax, si
004130A1  4C 8B 04 C5 08 00 00 00         mov r8, qword ptr [rax*8 + 8]
004130A9  E9 51 FF FF FF                  jmp 0x140412fff
004130AE  45 84 ED                        test r13b, r13b
004130B1  0F 84 39 FF FF FF               je 0x140412ff0
004130B7  8B 81 DC 89 00 00               mov eax, dword ptr [rcx + 0x89dc]
004130BD  3B C2                           cmp eax, edx
004130BF  0F 47 D0                        cmova edx, eax
004130C2  89 91 D8 89 00 00               mov dword ptr [rcx + 0x89d8], edx
004130C8  E9 23 FF FF FF                  jmp 0x140412ff0
004130CD  41 8B D4                        mov edx, r12d
004130D0  EB B0                           jmp 0x140413082
004130D2  44 0F B7 B4 24 90 00 00 00      movzx r14d, word ptr [rsp + 0x90]
004130DB  4C 8D 2D 5E 5B BB 00            lea r13, [rip + 0xbb5b5e]
004130E2  45 0F B7 D6                     movzx r10d, r14w
004130E6  45 8B DE                        mov r11d, r14d
004130E9  45 8B CE                        mov r9d, r14d
004130EC  33 ED                           xor ebp, ebp
004130EE  66 90                           nop
004130F0  41 8D 49 01                     lea ecx, [r9 + 1]
004130F4  48 85 DB                        test rbx, rbx
004130F7  74 54                           je 0x14041314d
004130F9  48 0F BC D3                     bsf rdx, rbx
004130FD  41 8B C9                        mov ecx, r9d
00413100  0F B6 C2                        movzx eax, dl
00413103  48 0F B3 C3                     btr rbx, rax
00413107  C1 E1 06                        shl ecx, 6
0041310A  0F B6 C2                        movzx eax, dl
0041310D  03 C8                           add ecx, eax
0041310F  48 8B 05 A2 00 B1 00            mov rax, qword ptr [rip + 0xb100a2]
00413116  8B 14 88                        mov edx, dword ptr [rax + rcx*4]
00413119  8B 05 61 39 BB 00               mov eax, dword ptr [rip + 0xbb3961]
0041311F  3B D0                           cmp edx, eax
00413121  0F 83 55 02 00 00               jae 0x14041337c
00413127  0F AE E8                        lfence
0041312A  49 8B 4C D5 00                  mov rcx, qword ptr [r13 + rdx*8]
0041312F  44 8B 81 F0 89 00 00            mov r8d, dword ptr [rcx + 0x89f0]
00413136  8B C7                           mov eax, edi
00413138  45 85 C0                        test r8d, r8d
0041313B  74 08                           je 0x140413145
0041313D  C1 E0 10                        shl eax, 0x10
00413140  33 D2                           xor edx, edx
00413142  41 F7 F0                        div r8d
00413145  89 81 D8 89 00 00               mov dword ptr [rcx + 0x89d8], eax
0041314B  EB A3                           jmp 0x1404130f0
0041314D  66 41 FF C2                     inc r10w
00413151  45 0F B7 CA                     movzx r9d, r10w
00413155  44 3B C9                        cmp r9d, ecx
00413158  73 16                           jae 0x140413170
0041315A  41 0F B7 C2                     movzx eax, r10w
0041315E  48 8B 1C C5 08 00 00 00         mov rbx, qword ptr [rax*8 + 8]
00413166  EB 8C                           jmp 0x1404130f4
00413168  41 8B C3                        mov eax, r11d
0041316B  E9 F5 FE FF FF                  jmp 0x140413065
00413170  48 8B 9C 24 B0 00 00 00         mov rbx, qword ptr [rsp + 0xb0]
00413178  44 0F B6 AC 24 A0 00 00 00      movzx r13d, byte ptr [rsp + 0xa0]
00413181  48 85 DB                        test rbx, rbx
00413184  0F 85 F2 00 00 00               jne 0x14041327c
0041318A  45 84 ED                        test r13b, r13b
0041318D  0F 85 57 01 00 00               jne 0x1404132ea
00413193  48 83 C4 38                     add rsp, 0x38
00413197  41 5F                           pop r15
00413199  41 5E                           pop r14
0041319B  41 5D                           pop r13
0041319D  41 5C                           pop r12
0041319F  5F                              pop rdi
004131A0  5E                              pop rsi
004131A1  5D                              pop rbp
004131A2  5B                              pop rbx
004131A3  C3                              ret
004131A4  CC                              int3
004131A5  44 0F B7 B4 24 90 00 00 00      movzx r14d, word ptr [rsp + 0x90]
004131AE  8B B4 24 A8 00 00 00            mov esi, dword ptr [rsp + 0xa8]
004131B5  4C 8B 7C 24 28                  mov r15, qword ptr [rsp + 0x28]
004131BA  66 0F 1F 44 00 00               nop word ptr [rax + rax]
004131C0  C7 84 24 98 00 00 00 00 00 00 00  mov dword ptr [rsp + 0x98], 0
004131CB  8D 4E 01                        lea ecx, [rsi + 1]
004131CE  4D 85 FF                        test r15, r15
004131D1  74 69                           je 0x14041323c
004131D3  49 0F BC D7                     bsf rdx, r15
004131D7  8B CE                           mov ecx, esi
004131D9  0F B6 C2                        movzx eax, dl
004131DC  49 0F B3 C7                     btr r15, rax
004131E0  C1 E1 06                        shl ecx, 6
004131E3  0F B6 C2                        movzx eax, dl
004131E6  03 C8                           add ecx, eax
004131E8  48 8B 05 C9 FF B0 00            mov rax, qword ptr [rip + 0xb0ffc9]
004131EF  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
004131F2  E8 D9 53 EC FF                  call 0x1402d85d0
004131F7  4C 8B C0                        mov r8, rax
004131FA  48 33 98 C8 00 00 00            xor rbx, qword ptr [rax + 0xc8]
00413201  8B 88 F0 89 00 00               mov ecx, dword ptr [rax + 0x89f0]
00413207  85 C9                           test ecx, ecx
00413209  74 6C                           je 0x140413277
0041320B  41 8B C4                        mov eax, r12d
0041320E  33 D2                           xor edx, edx
00413210  C1 E0 10                        shl eax, 0x10
00413213  F7 F1                           div ecx
00413215  8B C8                           mov ecx, eax
00413217  41 3B 88 D8 89 00 00            cmp ecx, dword ptr [r8 + 0x89d8]
0041321E  76 3D                           jbe 0x14041325d
00413220  41 89 88 D8 89 00 00            mov dword ptr [r8 + 0x89d8], ecx
00413227  8D 45 FF                        lea eax, [rbp - 1]
0041322A  40 84 ED                        test bpl, bpl
0041322D  0F B6 C8                        movzx ecx, al
00413230  40 0F B6 C5                     movzx eax, bpl
00413234  0F 44 C8                        cmove ecx, eax
00413237  0F B6 E9                        movzx ebp, cl
0041323A  EB 84                           jmp 0x1404131c0
0041323C  66 41 FF C6                     inc r14w
00413240  41 0F B7 F6                     movzx esi, r14w
00413244  3B F1                           cmp esi, ecx
00413246  0F 83 8C FD FF FF               jae 0x140412fd8
0041324C  41 0F B7 C6                     movzx eax, r14w
00413250  4C 8B 3C C5 08 00 00 00         mov r15, qword ptr [rax*8 + 8]
00413258  E9 71 FF FF FF                  jmp 0x1404131ce
0041325D  45 84 ED                        test r13b, r13b
00413260  74 C5                           je 0x140413227
00413262  41 8B 80 DC 89 00 00            mov eax, dword ptr [r8 + 0x89dc]
00413269  3B C1                           cmp eax, ecx
0041326B  0F 46 C1                        cmovbe eax, ecx
0041326E  41 89 80 D8 89 00 00            mov dword ptr [r8 + 0x89d8], eax
00413275  EB B0                           jmp 0x140413227
00413277  41 8B CC                        mov ecx, r12d
0041327A  EB 9B                           jmp 0x140413217
0041327C  4C 8B BC 24 80 00 00 00         mov r15, qword ptr [rsp + 0x80]
00413284  41 0F B7 FE                     movzx edi, r14w
00413288  41 8B F6                        mov esi, r14d
0041328B  C7 84 24 A0 00 00 00 00 00 00 00  mov dword ptr [rsp + 0xa0], 0
00413296  8D 4E 01                        lea ecx, [rsi + 1]
00413299  4D 85 FF                        test r15, r15
0041329C  0F 84 C0 00 00 00               je 0x140413362
004132A2  49 0F BC D7                     bsf rdx, r15
004132A6  8B CE                           mov ecx, esi
004132A8  0F B6 C2                        movzx eax, dl
004132AB  49 0F B3 C7                     btr r15, rax
004132AF  C1 E1 06                        shl ecx, 6
004132B2  0F B6 C2                        movzx eax, dl
004132B5  03 C8                           add ecx, eax
004132B7  48 8B 05 FA FE B0 00            mov rax, qword ptr [rip + 0xb0fefa]
004132BE  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
004132C1  E8 0A 53 EC FF                  call 0x1402d85d0
004132C6  8B 90 D8 89 00 00               mov edx, dword ptr [rax + 0x89d8]
004132CC  81 FA 10 27 00 00               cmp edx, 0x2710
004132D2  76 B7                           jbe 0x14041328b
004132D4  81 C2 F0 D8 FF FF               add edx, 0xffffd8f0
004132DA  48 8D 88 B0 89 00 00            lea rcx, [rax + 0x89b0]
004132E1  E8 AE 00 00 00                  call 0x140413394
004132E6  03 E8                           add ebp, eax
004132E8  EB A1                           jmp 0x14041328b
004132EA  48 8B 9C 24 88 00 00 00         mov rbx, qword ptr [rsp + 0x88]
004132F2  41 8D 4B 01                     lea ecx, [r11 + 1]
004132F6  48 85 DB                        test rbx, rbx
004132F9  74 3F                           je 0x14041333a
004132FB  48 0F BC D3                     bsf rdx, rbx
004132FF  41 8B CB                        mov ecx, r11d
00413302  0F B6 C2                        movzx eax, dl
00413305  48 0F B3 C3                     btr rbx, rax
00413309  C1 E1 06                        shl ecx, 6
0041330C  0F B6 C2                        movzx eax, dl
0041330F  03 C8                           add ecx, eax
00413311  48 8B 05 A0 FE B0 00            mov rax, qword ptr [rip + 0xb0fea0]
00413318  8B 0C 88                        mov ecx, dword ptr [rax + rcx*4]
0041331B  E8 B0 52 EC FF                  call 0x1402d85d0
00413320  45 0F B7 DE                     movzx r11d, r14w
00413324  8B 88 DC 89 00 00               mov ecx, dword ptr [rax + 0x89dc]
0041332A  89 88 D8 89 00 00               mov dword ptr [rax + 0x89d8], ecx
00413330  EB C0                           jmp 0x1404132f2
00413332  49 8B D4                        mov rdx, r12
00413335  E9 50 FB FF FF                  jmp 0x140412e8a
0041333A  66 41 FF C6                     inc r14w
0041333E  45 0F B7 DE                     movzx r11d, r14w
00413342  44 3B D9                        cmp r11d, ecx
00413345  0F 83 48 FE FF FF               jae 0x140413193
0041334B  41 0F B7 C6                     movzx eax, r14w
0041334F  48 8B 1C C5 08 00 00 00         mov rbx, qword ptr [rax*8 + 8]
00413357  EB 9D                           jmp 0x1404132f6
00413359  33 ED                           xor ebp, ebp
0041335B  8B CD                           mov ecx, ebp
0041335D  E9 E2 FC FF FF                  jmp 0x140413044
00413362  66 FF C7                        inc di
00413365  0F B7 F7                        movzx esi, di
00413368  3B F1                           cmp esi, ecx
0041336A  73 18                           jae 0x140413384
0041336C  0F B7 C7                        movzx eax, di
0041336F  4C 8B 3C C5 08 00 00 00         mov r15, qword ptr [rax*8 + 8]
00413377  E9 1D FF FF FF                  jmp 0x140413299
0041337C  48 8B CD                        mov rcx, rbp
0041337F  E9 AB FD FF FF                  jmp 0x14041312f
00413384  89 2B                           mov dword ptr [rbx], ebp
00413386  45 8B DE                        mov r11d, r14d
00413389  E9 FC FD FF FF                  jmp 0x14041318a
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PpmParkDistributeUtility(__int64 a1, __int64 a2, unsigned __int16 a3, unsigned __int8 a4, unsigned __int8 a5, unsigned int a6, __int64 a7)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_r11;
    __int64 v_r12;
    __int64 v_r14;
    __int64 v_r15;
    __int64 v_rbp;
    __int64 v_rbx;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m50;
    unsigned int v_stack_m58;
    unsigned __int64 v_stack_p10;
    unsigned __int16 v_stack_p18;
    unsigned int v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned int v_stack_p30;
    unsigned __int64 v_stack_p8;
    unsigned __int64 v_stack_p80;
    unsigned __int64 v_stack_p88;
    unsigned __int16 v_stack_p90;
    unsigned int v_stack_p98;
    unsigned int v_stack_pA0;

    v_stack_p18 = a3;
    v_stack_p10 = a2;
    v_rsp = (v_rsp) - (56);
    v_r12 = 0;
    v_rbp = 0;
    v_r15 = 0;
    v_r11 = 0;
    result = (a1) ^ (a2);
    v_stack_p30 = a3;
    v_stack_p8 = result;
loc_00412E40:
    v_stack_p20 = 0;
loc_00412E4C:
    if (result == 0) goto loc_00412EB3;
    a2 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a3)))) << (6));
    a2 = (unsigned int)((a2) + ((unsigned int)((unsigned __int8)(a3))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600712) + a2 * 4)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12270598))))) goto loc_00413332;
loc_00412E8A:
    if ((*(unsigned __int8 *)(*(unsigned __int64 *)(v_rip + 12279351 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600712) + a2 * 4)) * 8) + 35336)) != 0) goto loc_00412ED1;
    v_r15 = (unsigned __int8)((v_r15) + 1);
loc_00412E96:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12279351 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600712) + a2 * 4)) * 8) + 35312))) != 0) {
        a1 = (unsigned int)(((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12279351 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600712) + a2 * 4)) * 8) + 35288))) * ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12279351 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600712) + a2 * 4)) * 8) + 35312)))));
        a1 = (unsigned int)((a1) >> (16));
    }
    v_rsi = (unsigned int)(((unsigned int)(a6)) + ((unsigned int)(a1)));
    v_rbp = (unsigned __int8)((v_rbp) + 1);
    goto loc_00412E40;
loc_00412EB3:
    v_r10 = (unsigned __int16)((a3) + 1);
    if (((unsigned int)((unsigned __int16)(v_r10))) >= ((unsigned int)(a1))) goto loc_00412EDD;
    goto loc_00412E4C;
loc_00412ED1:
    v_r11 = (unsigned __int8)((v_r11) + 1);
    v_rdi = (0) | (*(unsigned __int64 *)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12279351 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600712) + a2 * 4)) * 8) + 35312)) + 200));
    goto loc_00412E96;
loc_00412EDD:
    v_stack_m50 = v_rdi;
    v_stack_p20 = (unsigned __int8)(v_r11);
loc_00412F10:
    v_stack_m58 = 0;
loc_00412F1B:
    if (v_stack_p10 == 0) goto loc_00412F64;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12279351 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600712) + a2 * 4)) * 8) + 35312))))));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600508) + a1 * 4)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12279351 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600712) + a2 * 4)) * 8) + 35312)), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600712) + a2 * 4)), (unsigned __int16)(v_r10));
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 35288))) - (*(unsigned int *)(result + 35292)));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 35312))) != 0) {
        a2 = (unsigned int)((a2) * ((unsigned int)((unsigned int)(*(unsigned int *)(result + 35312)))));
        a2 = (unsigned int)((a2) >> (16));
    }
    v_rsi = (unsigned int)((v_rsi) + ((unsigned int)(a2)));
    goto loc_00412F10;
loc_00412F64:
    v_r12 = (unsigned __int16)((v_stack_p18) + 1);
    if (((unsigned int)((unsigned __int16)(v_r12))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600508) + a1 * 4))))) goto loc_00412F7E;
    goto loc_00412F1B;
loc_00412F7E:
    a3 = (unsigned __int8)(v_rbp);
    if (((unsigned __int8)(v_rbp)) <= 1) { a3 = 1; }
    a2 = (unsigned int)(a4);
    if (a4 >= ((unsigned __int8)(a3))) { a2 = (unsigned int)((unsigned __int8)(a3)); }
    v_rbp = (unsigned __int8)(a2);
    if (((unsigned __int8)(a2)) <= 1) { v_rbp = 1; }
    a2 = 0;
    a2 = 0;
    if ((unsigned __int8)(v_r15) == 0) goto loc_00412FD8;
    if (v_stack_p20 > 0) goto loc_004131A5;
loc_00412FD8:
loc_00412FF0:
    v_stack_p20 = 0;
loc_00412FFF:
    if (result == 0) goto loc_00413092;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) << (6));
    a1 = (unsigned int)((a1) + (0));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12270162))))) goto loc_00413359;
loc_00413044:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8) + 35312))) == 0) goto loc_00413168;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8) + 35312))))) * ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8) + 35288)))));
    result = (unsigned int)((result) >> (16));
loc_00413065:
    if (((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi)))))) > ((unsigned int)(result))) goto loc_00412FF0;
    v_rbx = (result) ^ (*(unsigned __int64 *)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8) + 200));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8) + 35312))) == 0) goto loc_004130CD;
    a2 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi))))))) << (16));
loc_00413082:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) <= ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8) + 35288))))) goto loc_004130AE;
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8) + 35288) = (unsigned int)((unsigned int)((unsigned int)(result)));
    goto loc_00412FF0;
loc_00413092:
    v_rsi = (unsigned __int16)((v_stack_p18) + 1);
    if (((unsigned int)((unsigned __int16)(v_rsi))) >= ((unsigned int)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8)))) goto loc_004130D2;
    goto loc_00412FFF;
loc_004130AE:
    if (a5 == 0) goto loc_00412FF0;
    a2 = (unsigned int)((unsigned int)(result));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8) + 35292)))) > ((unsigned int)((unsigned int)((unsigned int)(result))))) { a2 = (unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8) + 35292))); }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278784 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600275) + a1 * 4)) * 8) + 35288) = (unsigned int)(a2);
    goto loc_00412FF0;
loc_004130CD:
    goto loc_00413082;
loc_004130D2:
    v_rbp = 0;
loc_004130F0:
loc_004130F4:
    if (v_rbx == 0) goto loc_0041314D;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi))))))))));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600034) + a1 * 4)))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip + 12269921))))) goto loc_0041337C;
loc_0041312F:
    result = (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi))))));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278622 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600034) + a1 * 4)) * 8) + 35312))) != 0) {
        result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi))))))) << (16));
        a2 = 0;
    }
    *(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278622 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600034) + a1 * 4)) * 8) + 35288) = (unsigned int)(result);
    goto loc_004130F0;
loc_0041314D:
    v_r10 = (unsigned __int16)(((unsigned __int16)(v_stack_p18)) + 1);
    if (((unsigned int)((unsigned __int16)(v_r10))) >= ((unsigned int)(*(unsigned __int64 *)(v_rip + 12278622 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600034) + a1 * 4)) * 8)))) goto loc_00413170;
    goto loc_004130F4;
loc_00413168:
    goto loc_00413065;
loc_00413170:
    if (a7 != 0) goto loc_0041327C;
loc_0041318A:
    if (a5 != 0) goto loc_004132EA;
loc_00413193:
    v_rsp = (v_rsp) + (56);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))));
loc_004131A5:
loc_004131C0:
    v_stack_p98 = 0;
loc_004131CE:
    if (v_stack_p28 == 0) goto loc_0041323C;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a6)))) << (6));
    a1 = (unsigned int)((a1) + (0));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11599817) + a1 * 4)), a2, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 12278622 + (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11600034) + a1 * 4)) * 8) + 35312)), (unsigned __int16)(v_r10));
    v_rbx = (a7) ^ (*(unsigned __int64 *)(result + 200));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + 35312))) == 0) goto loc_00413277;
    a2 = 0;
    result = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_rsi))))))) << (16));
loc_00413217:
    if (((unsigned int)((unsigned int)((unsigned int)(result)))) <= (*(unsigned int *)(result + 35288))) goto loc_0041325D;
    *(unsigned int *)(result + 35288) = (unsigned int)((unsigned int)((unsigned int)(result)));
loc_00413227:
    a1 = (unsigned __int8)(v_rbp - 1);
    if (0 == 0) { a1 = 0; }
    goto loc_004131C0;
loc_0041323C:
    v_r14 = (unsigned __int16)((v_stack_p90) + 1);
    if (((unsigned int)((unsigned __int16)(v_r14))) >= ((unsigned int)(a1))) goto loc_00412FD8;
    goto loc_004131CE;
loc_0041325D:
    if (a5 == 0) goto loc_00413227;
    result = (unsigned int)(*(unsigned int *)(result + 35292));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 35292)))) <= ((unsigned int)(a1))) { result = (unsigned int)(a1); }
    *(unsigned int *)(result + 35288) = (unsigned int)(result);
    goto loc_00413227;
loc_00413277:
    goto loc_00413217;
loc_0041327C:
loc_0041328B:
    v_stack_pA0 = 0;
loc_00413299:
    if (v_stack_p80 == 0) goto loc_00413362;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_r14))))) << (6));
    a1 = (unsigned int)((a1) + (0));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11599610) + a1 * 4)), a2, result, (unsigned __int16)(v_r10));
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + 35288)))) <= 0x2710ULL) goto loc_0041328B;
    a2 = (unsigned int)(((unsigned int)(*(unsigned int *)(result + 35288))) + (0xFFFFD8F0ULL));
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, a2, result, (unsigned __int16)(v_r10));
    v_rbp = (unsigned int)(((unsigned __int8)(a1)) + ((unsigned int)(result)));
    goto loc_0041328B;
loc_004132EA:
loc_004132F2:
loc_004132F6:
    if (v_stack_p88 == 0) goto loc_0041333A;
    a1 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)((unsigned int)(v_stack_p18))))) << (6));
    a1 = (unsigned int)((a1) + ((unsigned int)((unsigned __int8)(a2))));
    result = KeGetPrcb((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_rip + 11599520) + a1 * 4)), a2, result, (unsigned __int16)(v_r10));
    *(unsigned int *)(result + 35288) = (unsigned int)((unsigned int)(*(unsigned int *)(result + 35292)));
    goto loc_004132F2;
loc_00413332:
    goto loc_00412E8A;
loc_0041333A:
    v_r14 = (unsigned __int16)((v_r14) + 1);
    if (((unsigned int)((unsigned __int16)(v_r14))) >= ((unsigned int)((unsigned int)(*(unsigned int *)(result + 35292))))) goto loc_00413193;
    goto loc_004132F6;
loc_00413359:
    v_rbp = 0;
    goto loc_00413044;
loc_00413362:
    v_rdi = (unsigned __int16)(((unsigned __int16)(v_r14)) + 1);
    if (((unsigned int)((unsigned __int16)(v_rdi))) >= 0) goto loc_00413384;
    goto loc_00413299;
loc_0041337C:
    goto loc_0041312F;
loc_00413384:
    *(unsigned int *)(*(unsigned __int64 *)((unsigned __int16)(v_r14) * 8 + 8)) = 0;
    goto loc_0041318A;
}
```

## 5. (Beta) C Style

```c
int64_t PpmParkDistributeUtility(int64_t Arg1, int64_t Arg2, uint16_t Arg3, uint8_t Arg4, uint8_t Arg5, void *Arg6, int64_t Arg7)
{
    uint8_t *arg6 = (uint8_t *)Arg6;

    int64_t result;
    int64_t local_r10;
    int64_t local_r11;
    int64_t local_r12;
    int64_t local_r14;
    int64_t local_r15;
    int64_t local_rbp;
    int64_t local_rbx;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m50;
    uint32_t v_stack_m58;
    uint64_t v_stack_p10;
    uint16_t v_stack_p18;
    uint32_t v_stack_p20;
    uint64_t v_stack_p28;
    uint32_t v_stack_p30;
    uint64_t v_stack_p8;
    uint64_t v_stack_p80;
    uint64_t v_stack_p88;
    uint16_t v_stack_p90;
    uint32_t v_stack_p98;
    uint32_t v_stack_pA0;

    v_stack_p18 = Arg3;
    v_stack_p10 = Arg2;
    local_rsp = (local_rsp) - (56);
    local_r12 = 0;
    local_rbp = 0;
    local_r15 = 0;
    local_r11 = 0;
    result = (Arg1) ^ (Arg2);
    v_stack_p30 = Arg3;
    v_stack_p8 = result;
loc_00412E40:
    v_stack_p20 = 0;
loc_00412E4C:
    if (result == 0) goto loc_00412EB3;
    Arg2 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg3)))) << (6));
    Arg2 = (uint32_t)((Arg2) + ((uint32_t)((uint8_t)(Arg3))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10348) + Arg2 * 4)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB3C06))))) goto loc_00413332;
loc_00412E8A:
    if ((*(uint8_t *)(*(uint64_t *)(v_rip + 0xBB5E37 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10348) + Arg2 * 4)) * 8) + 0x8A08)) != 0) goto loc_00412ED1;
    local_r15 = (uint8_t)((local_r15) + 1);
loc_00412E96:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5E37 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10348) + Arg2 * 4)) * 8) + 0x89F0))) != 0) {
        Arg1 = (uint32_t)(((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5E37 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10348) + Arg2 * 4)) * 8) + 0x89D8))) * ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5E37 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10348) + Arg2 * 4)) * 8) + 0x89F0)))));
        Arg1 = (uint32_t)((Arg1) >> (16));
    }
    local_rsi = (uint32_t)(((uint32_t)(Arg6)) + ((uint32_t)(Arg1)));
    local_rbp = (uint8_t)((local_rbp) + 1);
    goto loc_00412E40;
loc_00412EB3:
    local_r10 = (uint16_t)((Arg3) + 1);
    if (((uint32_t)((uint16_t)(local_r10))) >= ((uint32_t)(Arg1))) goto loc_00412EDD;
    goto loc_00412E4C;
loc_00412ED1:
    local_r11 = (uint8_t)((local_r11) + 1);
    local_rdi = (0) | (*(uint64_t *)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5E37 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10348) + Arg2 * 4)) * 8) + 0x89F0)) + 0xC8));
    goto loc_00412E96;
loc_00412EDD:
    v_stack_m50 = local_rdi;
    v_stack_p20 = (uint8_t)(local_r11);
loc_00412F10:
    v_stack_m58 = 0;
loc_00412F1B:
    if (v_stack_p10 == 0) goto loc_00412F64;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5E37 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10348) + Arg2 * 4)) * 8) + 0x89F0))))));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB1027C) + Arg1 * 4)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5E37 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10348) + Arg2 * 4)) * 8) + 0x89F0)), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10348) + Arg2 * 4)), (uint16_t)(local_r10));
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x89D8))) - (*(uint32_t *)(result + 0x89DC)));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89F0))) != 0) {
        Arg2 = (uint32_t)((Arg2) * ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89F0)))));
        Arg2 = (uint32_t)((Arg2) >> (16));
    }
    local_rsi = (uint32_t)((local_rsi) + ((uint32_t)(Arg2)));
    goto loc_00412F10;
loc_00412F64:
    local_r12 = (uint16_t)((v_stack_p18) + 1);
    if (((uint32_t)((uint16_t)(local_r12))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB1027C) + Arg1 * 4))))) goto loc_00412F7E;
    goto loc_00412F1B;
loc_00412F7E:
    Arg3 = (uint8_t)(local_rbp);
    if (((uint8_t)(local_rbp)) <= 1) { Arg3 = 1; }
    Arg2 = (uint32_t)(Arg4);
    if (Arg4 >= ((uint8_t)(Arg3))) { Arg2 = (uint32_t)((uint8_t)(Arg3)); }
    local_rbp = (uint8_t)(Arg2);
    if (((uint8_t)(Arg2)) <= 1) { local_rbp = 1; }
    Arg2 = 0;
    Arg2 = 0;
    if ((uint8_t)(local_r15) == 0) goto loc_00412FD8;
    if (v_stack_p20 > 0) goto loc_004131A5;
loc_00412FD8:
loc_00412FF0:
    v_stack_p20 = 0;
loc_00412FFF:
    if (result == 0) goto loc_00413092;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB3A52))))) goto loc_00413359;
loc_00413044:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8) + 0x89F0))) == 0) goto loc_00413168;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8) + 0x89F0))))) * ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8) + 0x89D8)))));
    result = (uint32_t)((result) >> (16));
loc_00413065:
    if (((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi)))))) > ((uint32_t)(result))) goto loc_00412FF0;
    local_rbx = (result) ^ (*(uint64_t *)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8) + 0xC8));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8) + 0x89F0))) == 0) goto loc_004130CD;
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi))))))) << (16));
loc_00413082:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) <= ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8) + 0x89D8))))) goto loc_004130AE;
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8) + 0x89D8) = (uint32_t)((uint32_t)((uint32_t)(result)));
    goto loc_00412FF0;
loc_00413092:
    local_rsi = (uint16_t)((v_stack_p18) + 1);
    if (((uint32_t)((uint16_t)(local_rsi))) >= ((uint32_t)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8)))) goto loc_004130D2;
    goto loc_00412FFF;
loc_004130AE:
    if (Arg5 == 0) goto loc_00412FF0;
    Arg2 = (uint32_t)((uint32_t)(result));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8) + 0x89DC)))) > ((uint32_t)((uint32_t)((uint32_t)(result))))) { Arg2 = (uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8) + 0x89DC))); }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5C00 + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB10193) + Arg1 * 4)) * 8) + 0x89D8) = (uint32_t)(Arg2);
    goto loc_00412FF0;
loc_004130CD:
    goto loc_00413082;
loc_004130D2:
    local_rbp = 0;
loc_004130F0:
loc_004130F4:
    if (local_rbx == 0) goto loc_0041314D;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi))))))))));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB100A2) + Arg1 * 4)))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip + 0xBB3961))))) goto loc_0041337C;
loc_0041312F:
    result = (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi))))));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5B5E + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB100A2) + Arg1 * 4)) * 8) + 0x89F0))) != 0) {
        result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi))))))) << (16));
        Arg2 = 0;
    }
    *(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5B5E + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB100A2) + Arg1 * 4)) * 8) + 0x89D8) = (uint32_t)(result);
    goto loc_004130F0;
loc_0041314D:
    local_r10 = (uint16_t)(((uint16_t)(v_stack_p18)) + 1);
    if (((uint32_t)((uint16_t)(local_r10))) >= ((uint32_t)(*(uint64_t *)(v_rip + 0xBB5B5E + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB100A2) + Arg1 * 4)) * 8)))) goto loc_00413170;
    goto loc_004130F4;
loc_00413168:
    goto loc_00413065;
loc_00413170:
    if (Arg7 != 0) goto loc_0041327C;
loc_0041318A:
    if (Arg5 != 0) goto loc_004132EA;
loc_00413193:
    local_rsp = (local_rsp) + (56);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))));
loc_004131A5:
loc_004131C0:
    v_stack_p98 = 0;
loc_004131CE:
    if (v_stack_p28 == 0) goto loc_0041323C;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg6)))) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB0FFC9) + Arg1 * 4)), Arg2, (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xBB5B5E + (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB100A2) + Arg1 * 4)) * 8) + 0x89F0)), (uint16_t)(local_r10));
    local_rbx = (Arg7) ^ (*(uint64_t *)(result + 0xC8));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89F0))) == 0) goto loc_00413277;
    Arg2 = 0;
    result = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_rsi))))))) << (16));
loc_00413217:
    if (((uint32_t)((uint32_t)((uint32_t)(result)))) <= (*(uint32_t *)(result + 0x89D8))) goto loc_0041325D;
    *(uint32_t *)(result + 0x89D8) = (uint32_t)((uint32_t)((uint32_t)(result)));
loc_00413227:
    Arg1 = (uint8_t)(local_rbp - 1);
    if (0 == 0) { Arg1 = 0; }
    goto loc_004131C0;
loc_0041323C:
    local_r14 = (uint16_t)((v_stack_p90) + 1);
    if (((uint32_t)((uint16_t)(local_r14))) >= ((uint32_t)(Arg1))) goto loc_00412FD8;
    goto loc_004131CE;
loc_0041325D:
    if (Arg5 == 0) goto loc_00413227;
    result = (uint32_t)(*(uint32_t *)(result + 0x89DC));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89DC)))) <= ((uint32_t)(Arg1))) { result = (uint32_t)(Arg1); }
    *(uint32_t *)(result + 0x89D8) = (uint32_t)(result);
    goto loc_00413227;
loc_00413277:
    goto loc_00413217;
loc_0041327C:
loc_0041328B:
    v_stack_pA0 = 0;
loc_00413299:
    if (v_stack_p80 == 0) goto loc_00413362;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(local_r14))))) << (6));
    Arg1 = (uint32_t)((Arg1) + (0));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB0FEFA) + Arg1 * 4)), Arg2, result, (uint16_t)(local_r10));
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89D8)))) <= 0x2710ULL) goto loc_0041328B;
    Arg2 = (uint32_t)(((uint32_t)(*(uint32_t *)(result + 0x89D8))) + (0xFFFFD8F0ULL));
    result = PpmHeteroUtilityToNormalizedUtility(result + 35248, Arg2, result, (uint16_t)(local_r10));
    local_rbp = (uint32_t)(((uint8_t)(Arg1)) + ((uint32_t)(result)));
    goto loc_0041328B;
loc_004132EA:
loc_004132F2:
loc_004132F6:
    if (v_stack_p88 == 0) goto loc_0041333A;
    Arg1 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)((uint32_t)(v_stack_p18))))) << (6));
    Arg1 = (uint32_t)((Arg1) + ((uint32_t)((uint8_t)(Arg2))));
    result = KeGetPrcb((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_rip + 0xB0FEA0) + Arg1 * 4)), Arg2, result, (uint16_t)(local_r10));
    *(uint32_t *)(result + 0x89D8) = (uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89DC)));
    goto loc_004132F2;
loc_00413332:
    goto loc_00412E8A;
loc_0041333A:
    local_r14 = (uint16_t)((local_r14) + 1);
    if (((uint32_t)((uint16_t)(local_r14))) >= ((uint32_t)((uint32_t)(*(uint32_t *)(result + 0x89DC))))) goto loc_00413193;
    goto loc_004132F6;
loc_00413359:
    local_rbp = 0;
    goto loc_00413044;
loc_00413362:
    local_rdi = (uint16_t)(((uint16_t)(local_r14)) + 1);
    if (((uint32_t)((uint16_t)(local_rdi))) >= 0) goto loc_00413384;
    goto loc_00413299;
loc_0041337C:
    goto loc_0041312F;
loc_00413384:
    *(uint32_t *)(*(uint64_t *)((uint16_t)(local_r14) * 8 + 0x8)) = 0;
    goto loc_0041318A;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg6` | `+ 0x0 + rax*1` | `16` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00412DE0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
