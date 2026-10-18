# PiDqActionDataGetChangedProperties

- RVA: `0x00A61F10`–`0x00A62382` (길이 `1,138` bytes)
- VA: `0x0000000140A61F10`
- 실행 섹션: `PAGE`
- PDB 이름 있음: `예`; PDB Function 태그: `예`
- unwind 정보 RVA: `0x000B32F4`
- 디코드: `306`개 명령, `1,138/1,138` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **15**; 고유 호출 대상: **10**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x00A61F92` → [PiPnpRtlBeginOperation](../8E/PiPnpRtlBeginOperation_function_008E033C.md) (function, `0x008E033C`)
- `0x00A61FFE` → [PiDqGrowPropertyArray](../99/PiDqGrowPropertyArray_function_00991920.md) (function, `0x00991920`)
- `0x00A62044` → [PiDqPnPGetObjectProperty](../8D/PiDqPnPGetObjectProperty_function_008DFD90.md) (function, `0x008DFD90`)
- `0x00A620A3` → [PiDqGrowPropertyArray](../99/PiDqGrowPropertyArray_function_00991920.md) (function, `0x00991920`)
- `0x00A620C0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A620D3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A620F3` → [PiPnpRtlEndOperation](../8E/PiPnpRtlEndOperation_function_008E0518.md) (function, `0x008E0518`)
- `0x00A62102` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)
- `0x00A62148` → [PiDqPnPGetObjectPropertyInBestLocale](../8D/PiDqPnPGetObjectPropertyInBestLocale_function_008DEE10.md) (function, `0x008DEE10`)
- `0x00A6220F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A62226` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (function, `0x00B82870`)
- `0x00A62266` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (function, `0x006AD2B0`)
- `0x00A622B8` → [PiDqOpenObjectRegKey](../98/PiDqOpenObjectRegKey_function_0098FF30.md) (function, `0x0098FF30`)
- `0x00A622DD` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)
- `0x00A622FE` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (function, `0x00500080`)

### Direct callers
- [PiDqActionDataCreate](../8D/PiDqActionDataCreate_function_008DE1F0.md) at `0x008DE408`

### Static image references
- `0x00A61F2C` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **8**
  - `0x00A620C0` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A620D3` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A62102` → [_security_check_cookie](../../text/6A/_security_check_cookie_function_006AC640.md) (`PAGE` → `.text`)
  - `0x00A6220F` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A62226` → [ExFreePoolWithTag](../../poolcode/B8/ExFreePoolWithTag_function_00B82870.md) (`PAGE` → `POOLCODE`)
  - `0x00A62266` → [ZwClose](../../text/6A/ZwClose_function_006AD2B0.md) (`PAGE` → `.text`)
  - `0x00A622DD` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
  - `0x00A622FE` → [wcsicmp](../../text/50/wcsicmp_function_00500080.md) (`PAGE` → `.text`)
- call이 아닌 외부 분기/꼬리 이동: **3**
  - `0x00A62323` → [sub_00B3E2B4 + 0x13](../B3/Unknown_function_00B3E2B4.md) (`tail-transfer`)
  - `0x00A62331` → [sub_00B3E2B4](../B3/Unknown_function_00B3E2B4.md) (`tail-transfer`)
  - `0x00A62340` → [sub_00B3E2B4](../B3/Unknown_function_00B3E2B4.md) (`tail-transfer`)

## 3. Assembly (complete function range)

```asm
00A61F10  48 89 5C 24 20                  mov qword ptr [rsp + 0x20], rbx
00A61F15  55                              push rbp
00A61F16  56                              push rsi
00A61F17  57                              push rdi
00A61F18  41 54                           push r12
00A61F1A  41 55                           push r13
00A61F1C  41 56                           push r14
00A61F1E  41 57                           push r15
00A61F20  48 8D 6C 24 F9                  lea rbp, [rsp - 7]
00A61F25  48 81 EC D0 00 00 00            sub rsp, 0xd0
00A61F2C  48 8B 05 0D 88 3A 00            mov rax, qword ptr [rip + 0x3a880d]
00A61F33  48 33 C4                        xor rax, rsp
00A61F36  48 89 45 FF                     mov qword ptr [rbp - 1], rax
00A61F3A  48 8B B5 87 00 00 00            mov rsi, qword ptr [rbp + 0x87]
00A61F41  0F 57 C0                        xorps xmm0, xmm0
00A61F44  48 8B 45 67                     mov rax, qword ptr [rbp + 0x67]
00A61F48  4C 8B AD 8F 00 00 00            mov r13, qword ptr [rbp + 0x8f]
00A61F4F  48 8B 7D 7F                     mov rdi, qword ptr [rbp + 0x7f]
00A61F53  48 89 4D C7                     mov qword ptr [rbp - 0x39], rcx
00A61F57  48 8D 4D BF                     lea rcx, [rbp - 0x41]
00A61F5B  48 89 75 9F                     mov qword ptr [rbp - 0x61], rsi
00A61F5F  33 F6                           xor esi, esi
00A61F61  44 8B F6                        mov r14d, esi
00A61F64  48 89 75 97                     mov qword ptr [rbp - 0x69], rsi
00A61F68  44 8B E6                        mov r12d, esi
00A61F6B  48 89 75 BF                     mov qword ptr [rbp - 0x41], rsi
00A61F6F  41 89 75 00                     mov dword ptr [r13], esi
00A61F73  44 88 4D 87                     mov byte ptr [rbp - 0x79], r9b
00A61F77  4C 89 45 A7                     mov qword ptr [rbp - 0x59], r8
00A61F7B  89 55 8B                        mov dword ptr [rbp - 0x75], edx
00A61F7E  48 89 45 B7                     mov qword ptr [rbp - 0x49], rax
00A61F82  48 89 7D AF                     mov qword ptr [rbp - 0x51], rdi
00A61F86  0F 11 45 CF                     movups xmmword ptr [rbp - 0x31], xmm0
00A61F8A  0F 11 45 DF                     movups xmmword ptr [rbp - 0x21], xmm0
00A61F8E  0F 11 45 EF                     movups xmmword ptr [rbp - 0x11], xmm0
00A61F92  E8 A5 E3 E7 FF                  call 0x1408e033c
00A61F97  8B C6                           mov eax, esi
00A61F99  89 45 8F                        mov dword ptr [rbp - 0x71], eax
00A61F9C  3B 47 4C                        cmp eax, dword ptr [rdi + 0x4c]
00A61F9F  0F 83 33 01 00 00               jae 0x140a620d8
00A61FA5  44 8B F8                        mov r15d, eax
00A61FA8  48 8B DE                        mov rbx, rsi
00A61FAB  49 C1 E7 05                     shl r15, 5
00A61FAF  4C 03 FF                        add r15, rdi
00A61FB2  49 8D 7F 64                     lea rdi, [r15 + 0x64]
00A61FB6  48 39 75 6F                     cmp qword ptr [rbp + 0x6f], rsi
00A61FBA  0F 85 EA 01 00 00               jne 0x140a621aa
00A61FC0  8B 0F                           mov ecx, dword ptr [rdi]
00A61FC2  85 C9                           test ecx, ecx
00A61FC4  0F 85 A6 02 00 00               jne 0x140a62270
00A61FCA  8B 75 8B                        mov esi, dword ptr [rbp - 0x75]
00A61FCD  33 C0                           xor eax, eax
00A61FCF  45 85 F6                        test r14d, r14d
00A61FD2  0F 88 00 01 00 00               js 0x140a620d8
00A61FD8  38 45 87                        cmp byte ptr [rbp - 0x79], al
00A61FDB  0F 85 42 01 00 00               jne 0x140a62123
00A61FE1  41 8B 55 00                     mov edx, dword ptr [r13]
00A61FE5  44 3B E2                        cmp r12d, edx
00A61FE8  77 24                           ja 0x140a6200e
00A61FEA  39 45 77                        cmp dword ptr [rbp + 0x77], eax
00A61FED  0F 86 6B 03 00 00               jbe 0x140a6235e
00A61FF3  44 8B 65 77                     mov r12d, dword ptr [rbp + 0x77]
00A61FF7  48 8B 4D 9F                     mov rcx, qword ptr [rbp - 0x61]
00A61FFB  45 8B C4                        mov r8d, r12d
00A61FFE  E8 1D F9 F2 FF                  call 0x140991920
00A62003  44 8B F0                        mov r14d, eax
00A62006  85 C0                           test eax, eax
00A62008  0F 88 CA 00 00 00               js 0x140a620d8
00A6200E  41 8B 45 00                     mov eax, dword ptr [r13]
00A62012  4D 8D 4F 50                     lea r9, [r15 + 0x50]
00A62016  4C 8B C3                        mov r8, rbx
00A62019  8B D6                           mov edx, esi
00A6201B  48 8D 0C 40                     lea rcx, [rax + rax*2]
00A6201F  48 8B 45 9F                     mov rax, qword ptr [rbp - 0x61]
00A62023  48 C1 E1 04                     shl rcx, 4
00A62027  48 03 08                        add rcx, qword ptr [rax]
00A6202A  49 8B 47 68                     mov rax, qword ptr [r15 + 0x68]
00A6202E  48 89 4C 24 30                  mov qword ptr [rsp + 0x30], rcx
00A62033  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00A62037  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A6203C  41 8B 47 64                     mov eax, dword ptr [r15 + 0x64]
00A62040  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A62044  E8 47 DD E7 FF                  call 0x1408dfd90
00A62049  33 F6                           xor esi, esi
00A6204B  44 8B F0                        mov r14d, eax
00A6204E  85 C0                           test eax, eax
00A62050  0F 88 82 00 00 00               js 0x140a620d8
00A62056  41 FF 45 00                     inc dword ptr [r13]
00A6205A  8B 45 8F                        mov eax, dword ptr [rbp - 0x71]
00A6205D  48 8B 7D AF                     mov rdi, qword ptr [rbp - 0x51]
00A62061  FF C0                           inc eax
00A62063  E9 31 FF FF FF                  jmp 0x140a61f99
00A62068  45 8B 55 00                     mov r10d, dword ptr [r13]
00A6206C  44 8B C6                        mov r8d, esi
00A6206F  48 8B 75 9F                     mov rsi, qword ptr [rbp - 0x61]
00A62073  44 8B 5D E3                     mov r11d, dword ptr [rbp - 0x1d]
00A62077  8B 5D DF                        mov ebx, dword ptr [rbp - 0x21]
00A6207A  45 3B C2                        cmp r8d, r10d
00A6207D  0F 82 8D 02 00 00               jb 0x140a62310
00A62083  45 3B E2                        cmp r12d, r10d
00A62086  0F 87 A4 01 00 00               ja 0x140a62230
00A6208C  8B 45 77                        mov eax, dword ptr [rbp + 0x77]
00A6208F  85 C0                           test eax, eax
00A62091  0F 84 AE 02 00 00               je 0x140a62345
00A62097  44 8B E0                        mov r12d, eax
00A6209A  45 8B C4                        mov r8d, r12d
00A6209D  41 8B D2                        mov edx, r10d
00A620A0  48 8B CE                        mov rcx, rsi
00A620A3  E8 78 F8 F2 FF                  call 0x140991920
00A620A8  44 8B F0                        mov r14d, eax
00A620AB  85 C0                           test eax, eax
00A620AD  0F 89 7D 01 00 00               jns 0x140a62230
00A620B3  48 85 FF                        test rdi, rdi
00A620B6  74 0D                           je 0x140a620c5
00A620B8  BA 50 6E 70 58                  mov edx, 0x58706e50
00A620BD  48 8B CF                        mov rcx, rdi
00A620C0  E8 AB 07 12 00                  call 0x140b82870
00A620C5  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00A620C9  48 85 C9                        test rcx, rcx
00A620CC  74 0A                           je 0x140a620d8
00A620CE  BA 50 6E 70 58                  mov edx, 0x58706e50
00A620D3  E8 98 07 12 00                  call 0x140b82870
00A620D8  48 8B 5D 97                     mov rbx, qword ptr [rbp - 0x69]
00A620DC  48 8D 43 FF                     lea rax, [rbx - 1]
00A620E0  48 83 F8 FD                     cmp rax, -3
00A620E4  0F 86 79 01 00 00               jbe 0x140a62263
00A620EA  48 8B 4D BF                     mov rcx, qword ptr [rbp - 0x41]
00A620EE  48 85 C9                        test rcx, rcx
00A620F1  74 05                           je 0x140a620f8
00A620F3  E8 20 E4 E7 FF                  call 0x1408e0518
00A620F8  41 8B C6                        mov eax, r14d
00A620FB  48 8B 4D FF                     mov rcx, qword ptr [rbp - 1]
00A620FF  48 33 CC                        xor rcx, rsp
00A62102  E8 39 A5 C4 FF                  call 0x1406ac640
00A62107  48 8B 9C 24 28 01 00 00         mov rbx, qword ptr [rsp + 0x128]
00A6210F  48 81 C4 D0 00 00 00            add rsp, 0xd0
00A62116  41 5F                           pop r15
00A62118  41 5E                           pop r14
00A6211A  41 5D                           pop r13
00A6211C  41 5C                           pop r12
00A6211E  5F                              pop rdi
00A6211F  5E                              pop rsi
00A62120  5D                              pop rbp
00A62121  C3                              ret
00A62122  CC                              int3
00A62123  48 8B 4D A7                     mov rcx, qword ptr [rbp - 0x59]
00A62127  48 8D 45 CF                     lea rax, [rbp - 0x31]
00A6212B  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A62130  4D 8D 4F 50                     lea r9, [r15 + 0x50]
00A62134  48 8B 45 B7                     mov rax, qword ptr [rbp - 0x49]
00A62138  4C 8B C3                        mov r8, rbx
00A6213B  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A62140  8B D6                           mov edx, esi
00A62142  8B 07                           mov eax, dword ptr [rdi]
00A62144  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00A62148  E8 C3 CC E7 FF                  call 0x1408dee10
00A6214D  33 F6                           xor esi, esi
00A6214F  44 8B F0                        mov r14d, eax
00A62152  85 C0                           test eax, eax
00A62154  78 82                           js 0x140a620d8
00A62156  48 8B 4D B7                     mov rcx, qword ptr [rbp - 0x49]
00A6215A  48 8B 7D E7                     mov rdi, qword ptr [rbp - 0x19]
00A6215E  0F B7 01                        movzx eax, word ptr [rcx]
00A62161  66 F7 D8                        neg ax
00A62164  48 1B DB                        sbb rbx, rbx
00A62167  48 23 D9                        and rbx, rcx
00A6216A  49 8B 4F 68                     mov rcx, qword ptr [r15 + 0x68]
00A6216E  48 3B CB                        cmp rcx, rbx
00A62171  0F 84 F1 FE FF FF               je 0x140a62068
00A62177  48 85 C9                        test rcx, rcx
00A6217A  0F 85 51 01 00 00               jne 0x140a622d1
00A62180  48 3B FB                        cmp rdi, rbx
00A62183  74 7D                           je 0x140a62202
00A62185  48 85 FF                        test rdi, rdi
00A62188  0F 85 61 01 00 00               jne 0x140a622ef
00A6218E  48 85 DB                        test rbx, rbx
00A62191  74 6F                           je 0x140a62202
00A62193  48 83 C8 FF                     or rax, 0xffffffffffffffff
00A62197  48 FF C0                        inc rax
00A6219A  66 39 34 43                     cmp word ptr [rbx + rax*2], si
00A6219E  75 F7                           jne 0x140a62197
00A621A0  48 8D 48 01                     lea rcx, [rax + 1]
00A621A4  48 8D 0C 4B                     lea rcx, [rbx + rcx*2]
00A621A8  EB B4                           jmp 0x140a6215e
00A621AA  44 8B C6                        mov r8d, esi
00A621AD  44 3B 45 77                     cmp r8d, dword ptr [rbp + 0x77]
00A621B1  0F 83 A3 FE FF FF               jae 0x140a6205a
00A621B7  41 8B C8                        mov ecx, r8d
00A621BA  48 C1 E1 05                     shl rcx, 5
00A621BE  48 03 4D 6F                     add rcx, qword ptr [rbp + 0x6f]
00A621C2  8B 41 10                        mov eax, dword ptr [rcx + 0x10]
00A621C5  41 39 47 60                     cmp dword ptr [r15 + 0x60], eax
00A621C9  74 05                           je 0x140a621d0
00A621CB  41 FF C0                        inc r8d
00A621CE  EB DD                           jmp 0x140a621ad
00A621D0  49 8B 57 50                     mov rdx, qword ptr [r15 + 0x50]
00A621D4  48 2B 11                        sub rdx, qword ptr [rcx]
00A621D7  75 08                           jne 0x140a621e1
00A621D9  49 8B 57 58                     mov rdx, qword ptr [r15 + 0x58]
00A621DD  48 2B 51 08                     sub rdx, qword ptr [rcx + 8]
00A621E1  48 85 D2                        test rdx, rdx
00A621E4  75 E5                           jne 0x140a621cb
00A621E6  8B 41 14                        mov eax, dword ptr [rcx + 0x14]
00A621E9  39 07                           cmp dword ptr [rdi], eax
00A621EB  75 DE                           jne 0x140a621cb
00A621ED  49 39 77 68                     cmp qword ptr [r15 + 0x68], rsi
00A621F1  0F 84 C9 FD FF FF               je 0x140a61fc0
00A621F7  40 38 75 87                     cmp byte ptr [rbp - 0x79], sil
00A621FB  74 CE                           je 0x140a621cb
00A621FD  E9 BE FD FF FF                  jmp 0x140a61fc0
00A62202  48 85 FF                        test rdi, rdi
00A62205  74 0D                           je 0x140a62214
00A62207  BA 50 6E 70 58                  mov edx, 0x58706e50
00A6220C  48 8B CF                        mov rcx, rdi
00A6220F  E8 5C 06 12 00                  call 0x140b82870
00A62214  48 8B 4D F7                     mov rcx, qword ptr [rbp - 9]
00A62218  48 85 C9                        test rcx, rcx
00A6221B  0F 84 39 FE FF FF               je 0x140a6205a
00A62221  BA 50 6E 70 58                  mov edx, 0x58706e50
00A62226  E8 45 06 12 00                  call 0x140b82870
00A6222B  E9 2A FE FF FF                  jmp 0x140a6205a
00A62230  41 8B 45 00                     mov eax, dword ptr [r13]
00A62234  0F 10 45 CF                     movups xmm0, xmmword ptr [rbp - 0x31]
00A62238  0F 10 4D DF                     movups xmm1, xmmword ptr [rbp - 0x21]
00A6223C  48 8D 0C 40                     lea rcx, [rax + rax*2]
00A62240  48 8B 06                        mov rax, qword ptr [rsi]
00A62243  48 03 C9                        add rcx, rcx
00A62246  0F 11 04 C8                     movups xmmword ptr [rax + rcx*8], xmm0
00A6224A  0F 10 45 EF                     movups xmm0, xmmword ptr [rbp - 0x11]
00A6224E  0F 11 4C C8 10                  movups xmmword ptr [rax + rcx*8 + 0x10], xmm1
00A62253  0F 11 44 C8 20                  movups xmmword ptr [rax + rcx*8 + 0x20], xmm0
00A62258  41 FF 45 00                     inc dword ptr [r13]
00A6225C  33 F6                           xor esi, esi
00A6225E  E9 F7 FD FF FF                  jmp 0x140a6205a
00A62263  48 8B CB                        mov rcx, rbx
00A62266  E8 45 B0 C4 FF                  call 0x1406ad2b0
00A6226B  E9 7A FE FF FF                  jmp 0x140a620ea
00A62270  83 F9 01                        cmp ecx, 1
00A62273  0F 85 FE 00 00 00               jne 0x140a62377
00A62279  33 DB                           xor ebx, ebx
00A6227B  48 39 5D 97                     cmp qword ptr [rbp - 0x69], rbx
00A6227F  74 0F                           je 0x140a62290
00A62281  48 8B 5D 97                     mov rbx, qword ptr [rbp - 0x69]
00A62285  48 83 FB FF                     cmp rbx, -1
00A62289  74 D1                           je 0x140a6225c
00A6228B  E9 3D FD FF FF                  jmp 0x140a61fcd
00A62290  44 8B 45 8B                     mov r8d, dword ptr [rbp - 0x75]
00A62294  48 8D 45 97                     lea rax, [rbp - 0x69]
00A62298  48 8B 55 A7                     mov rdx, qword ptr [rbp - 0x59]
00A6229C  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
00A622A1  48 8B 45 C7                     mov rax, qword ptr [rbp - 0x39]
00A622A5  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
00A622AA  B8 01 00 00 00                  mov eax, 1
00A622AF  44 8B C8                        mov r9d, eax
00A622B2  88 5C 24 20                     mov byte ptr [rsp + 0x20], bl
00A622B6  8B C8                           mov ecx, eax
00A622B8  E8 73 DC F2 FF                  call 0x14098ff30
00A622BD  44 8B F0                        mov r14d, eax
00A622C0  3D 34 00 00 C0                  cmp eax, 0xc0000034
00A622C5  75 BA                           jne 0x140a62281
00A622C7  48 83 4D 97 FF                  or qword ptr [rbp - 0x69], 0xffffffffffffffff
00A622CC  44 8B F3                        mov r14d, ebx
00A622CF  EB B0                           jmp 0x140a62281
00A622D1  48 85 DB                        test rbx, rbx
00A622D4  0F 84 A6 FE FF FF               je 0x140a62180
00A622DA  48 8B D3                        mov rdx, rbx
00A622DD  E8 9E DD A9 FF                  call 0x140500080
00A622E2  85 C0                           test eax, eax
00A622E4  0F 84 7E FD FF FF               je 0x140a62068
00A622EA  E9 91 FE FF FF                  jmp 0x140a62180
00A622EF  48 85 DB                        test rbx, rbx
00A622F2  0F 84 0A FF FF FF               je 0x140a62202
00A622F8  48 8B D3                        mov rdx, rbx
00A622FB  48 8B CF                        mov rcx, rdi
00A622FE  E8 7D DD A9 FF                  call 0x140500080
00A62303  85 C0                           test eax, eax
00A62305  0F 84 F7 FE FF FF               je 0x140a62202
00A6230B  E9 7E FE FF FF                  jmp 0x140a6218e
00A62310  4C 8B 0E                        mov r9, qword ptr [rsi]
00A62313  41 8B C0                        mov eax, r8d
00A62316  48 8D 14 40                     lea rdx, [rax + rax*2]
00A6231A  48 C1 E2 04                     shl rdx, 4
00A6231E  42 3B 5C 0A 10                  cmp ebx, dword ptr [rdx + r9 + 0x10]
00A62323  0F 85 9E BF 0D 00               jne 0x140b3e2c7
00A62329  48 8B 4D CF                     mov rcx, qword ptr [rbp - 0x31]
00A6232D  4A 2B 0C 0A                     sub rcx, qword ptr [rdx + r9]
00A62331  0F 85 7D BF 0D 00               jne 0x140b3e2b4
00A62337  48 8B 4D D7                     mov rcx, qword ptr [rbp - 0x29]
00A6233B  4A 2B 4C 0A 08                  sub rcx, qword ptr [rdx + r9 + 8]
00A62340  E9 6F BF 0D 00                  jmp 0x140b3e2b4
00A62345  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00A62349  B9 05 00 00 00                  mov ecx, 5
00A6234E  8B 40 4C                        mov eax, dword ptr [rax + 0x4c]
00A62351  3B C1                           cmp eax, ecx
00A62353  0F 47 C8                        cmova ecx, eax
00A62356  44 03 E1                        add r12d, ecx
00A62359  E9 3C FD FF FF                  jmp 0x140a6209a
00A6235E  48 8B 45 AF                     mov rax, qword ptr [rbp - 0x51]
00A62362  B9 05 00 00 00                  mov ecx, 5
00A62367  8B 40 4C                        mov eax, dword ptr [rax + 0x4c]
00A6236A  3B C1                           cmp eax, ecx
00A6236C  0F 47 C8                        cmova ecx, eax
00A6236F  44 03 E1                        add r12d, ecx
00A62372  E9 80 FC FF FF                  jmp 0x140a61ff7
00A62377  41 BE 0D 00 00 C0               mov r14d, 0xc000000d
00A6237D  E9 56 FD FF FF                  jmp 0x140a620d8
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PiDqActionDataGetChangedProperties(__int64 a1, int a2, __int64 a3, unsigned __int8 a4, __int64 a5, __int64 a6, unsigned int a7, __int64 a8, __int64 a9, __int64 a10)
{
    __int64 result;
    __int64 v_r12;
    __int64 v_r15;
    __int64 v_rbx;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m3F;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m5C;
    unsigned __int64 v_stack_m60;
    unsigned __int64 v_stack_m68;
    unsigned __int64 v_stack_m70;
    unsigned __int64 v_stack_m78;
    unsigned __int64 v_stack_m80;
    unsigned __int64 v_stack_m88;
    unsigned __int64 v_stack_m90;
    unsigned __int64 v_stack_m98;
    unsigned __int64 v_stack_mA0;
    unsigned __int64 v_stack_mA8;
    unsigned int v_stack_mB0;
    unsigned int v_stack_mB4;
    unsigned __int8 v_stack_mB8;
    unsigned __int64 v_stack_mD8;
    unsigned __int64 v_stack_mE0;
    unsigned int v_stack_mE8;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p28;
    unsigned __int64 v_stack_p30;

    v_stack_p20 = v_rbx;
    v_rsp = (v_rsp) - (208);
    result = (*(unsigned __int64 *)(v_rip + 3835917)) ^ (v_rsp);
    v_stack_m40 = result;
    v_stack_m78 = a1;
    v_stack_mA0 = a9;
    v_rsi = 0;
    v_stack_mA8 = 0;
    v_stack_m80 = 0;
    *(unsigned int *)(a10) = 0;
    v_stack_mB8 = a4;
    v_stack_m98 = a3;
    v_stack_mB4 = a2;
    v_stack_m88 = a5;
    v_stack_m90 = a8;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    result = PiPnpRtlBeginOperation(v_stack_m80, a2, a3, a4);
loc_00A61F99:
    v_stack_mB0 = 0;
    if (0 >= (*(unsigned int *)(a8 + 76))) goto loc_00A620D8;
    v_r15 = (0) << (5);
    v_r15 = (v_r15) + (a8);
    if (a6 != 0) goto loc_00A621AA;
loc_00A61FC0:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 100))) != 0) goto loc_00A62270;
loc_00A61FCD:
    result = 0;
    if (sign_flag) goto loc_00A620D8;
    if (v_stack_mB8 != 0) goto loc_00A62123;
    if (0 > ((unsigned int)((unsigned int)(*(unsigned int *)(a10))))) goto loc_00A6200E;
    if (a7 <= 0) goto loc_00A6235E;
loc_00A61FF7:
    result = PiDqGrowPropertyArray(v_stack_mA0, (unsigned int)(*(unsigned int *)(a10)), (unsigned int)((unsigned int)((unsigned int)(a7))), a4);
    if (sign_flag) goto loc_00A620D8;
loc_00A6200E:
    a1 = ((unsigned int)(*(unsigned int *)(a10)) + (unsigned int)(*(unsigned int *)(a10)) * 2) << (4);
    a1 = (a1) + (*(unsigned __int64 *)(v_stack_mA0));
    v_stack_mD8 = a1;
    v_stack_mE0 = *(unsigned __int64 *)(v_r15 + 104);
    v_stack_mE8 = (unsigned int)((unsigned int)(*(unsigned int *)(v_r15 + 100)));
    result = PiDqPnPGetObjectProperty(v_stack_m98, (unsigned int)((unsigned int)((unsigned int)(v_stack_mB4))), 0, v_r15 + 80);
    v_rsi = 0;
    if (sign_flag) goto loc_00A620D8;
loc_00A6205A:
    result = (unsigned int)(((unsigned int)(v_stack_mB0)) + 1);
    goto loc_00A61F99;
loc_00A62068:
    if (0 < ((unsigned int)((unsigned int)(*(unsigned int *)(a10))))) goto loc_00A62310;
    if (((unsigned int)((unsigned int)(a7))) > ((unsigned int)((unsigned int)(*(unsigned int *)(a10))))) goto loc_00A62230;
    if ((unsigned int)((unsigned int)(a7)) == 0) goto loc_00A62345;
loc_00A6209A:
    result = PiDqGrowPropertyArray(v_stack_mA0, (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a10)))), (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a7))))), v_r15 + 80);
    if (!sign_flag) goto loc_00A62230;
    if (v_stack_m90 != 0) {
        a2 = 0x58706E50ULL;
        a1 = v_stack_m90;
        result = ExFreePoolWithTag(a1, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a7))))), v_r15 + 80);
    }
    if (v_stack_m48 != 0) {
        a2 = 0x58706E50ULL;
        result = ExFreePoolWithTag(v_stack_m48, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a7))))), v_r15 + 80);
    }
    if ((v_stack_mA8 - 1) <= -3) goto loc_00A62263;
loc_00A620EA:
    result = v_stack_mA8 - 1;
    if (v_stack_m80 != 0) {
        result = PiPnpRtlEndOperation(v_stack_m80, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a7))))), v_r15 + 80);
    }
    a1 = (v_stack_m40) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, (unsigned int)((unsigned int)((unsigned int)((unsigned int)((unsigned int)(a7))))), v_r15 + 80);
    v_rsp = (v_rsp) + (208);
    return result;
loc_00A62123:
    v_stack_p30 = v_stack_m70;
    v_stack_p28 = v_stack_m88;
    v_stack_p20 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90)));
    result = PiDqPnPGetObjectPropertyInBestLocale(v_stack_m98, (unsigned int)((unsigned int)(v_stack_mA0)), v_stack_p20, v_r15 + 80);
    v_rsi = 0;
    if (sign_flag) goto loc_00A620D8;
loc_00A6215E:
    result = (unsigned __int16)(-(*(unsigned __int16 *)(v_stack_m88)));
    v_rbx = (v_stack_p20) & (v_stack_m88);
    if ((*(unsigned __int64 *)(v_r15 + 104)) == v_rbx) goto loc_00A62068;
    if (*(unsigned __int64 *)(v_r15 + 104) != 0) goto loc_00A622D1;
loc_00A62180:
    if (v_stack_m58 == v_rbx) goto loc_00A62202;
    if (v_stack_m58 != 0) goto loc_00A622EF;
loc_00A6218E:
    if (v_rbx == 0) goto loc_00A62202;
    result = (result) | (-1);
loc_00A62197:
    result = (result) + 1;
    if ((*(unsigned __int16 *)(v_rbx + result * 2)) != 0) goto loc_00A62197;
    goto loc_00A6215E;
loc_00A621AA:
loc_00A621AD:
    if (0 >= a7) goto loc_00A6205A;
    a1 = (0) << (5);
    a1 = (a1) + (a6);
    if ((*(unsigned int *)(v_r15 + 96)) == ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 16))))) goto loc_00A621D0;
loc_00A621CB:
    a3 = (unsigned int)((0) + 1);
    goto loc_00A621AD;
loc_00A621D0:
    a2 = (*(unsigned __int64 *)(v_r15 + 80)) - (*(unsigned __int64 *)(a1));
    if (!(condition_is_not_equal)) {
        a2 = *(unsigned __int64 *)(v_r15 + 88);
        a2 = (a2) - (*(unsigned __int64 *)(a1 + 8));
    }
    if (a2 != 0) goto loc_00A621CB;
    if ((*(unsigned int *)(v_stack_m58)) != ((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 20))))) goto loc_00A621CB;
    if ((*(unsigned __int64 *)(v_r15 + 104)) == 0) goto loc_00A61FC0;
    if (v_stack_mB8 == 0) goto loc_00A621CB;
    goto loc_00A61FC0;
loc_00A62202:
    result = (unsigned int)(*(unsigned int *)(a1 + 20));
    if (v_stack_m58 != 0) {
        a2 = 0x58706E50ULL;
        a1 = v_stack_m58;
        result = ExFreePoolWithTag(a1, a2, a3, v_r15 + 80);
    }
    if (v_stack_m48 == 0) goto loc_00A6205A;
    result = ExFreePoolWithTag(v_stack_m48, (unsigned int)(0x58706E50ULL), a3, v_r15 + 80);
    goto loc_00A6205A;
loc_00A62230:
    a1 = ((unsigned int)(*(unsigned int *)(a10)) + (unsigned int)(*(unsigned int *)(a10)) * 2) + ((unsigned int)(*(unsigned int *)(a10)) + (unsigned int)(*(unsigned int *)(a10)) * 2);
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + a1 * 8) = v_xmm0;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + a1 * 8 + 16) = v_xmm1;
    *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) + a1 * 8 + 32) = v_xmm0;
loc_00A6225C:
    v_rsi = 0;
    goto loc_00A6205A;
loc_00A62263:
    result = ZwClose(v_rbx, (unsigned int)(0x58706E50ULL), a3, v_r15 + 80);
    goto loc_00A620EA;
loc_00A62270:
    if (((unsigned int)(v_rbx)) != 1) goto loc_00A62377;
    v_rbx = 0;
    if (v_stack_mA8 == 0) goto loc_00A62290;
loc_00A62281:
    if (v_stack_mA8 == -1) goto loc_00A6225C;
    goto loc_00A61FCD;
loc_00A62290:
    v_stack_p30 = v_stack_mA8;
    v_stack_p28 = v_stack_m78;
    v_stack_p20 = (unsigned __int8)(v_stack_mA8);
    result = PiDqOpenObjectRegKey(1, v_stack_m98, (unsigned int)(v_stack_mB4), 1);
    if (((unsigned int)(result)) != 0xC0000034ULL) goto loc_00A62281;
    goto loc_00A62281;
loc_00A622D1:
    if (v_stack_mA8 == 0) goto loc_00A62180;
    result = wcsicmp(1, v_stack_mA8, (unsigned int)(v_stack_mB4), 1);
    if ((unsigned int)(result) == 0) goto loc_00A62068;
    goto loc_00A62180;
loc_00A622EF:
    if (v_stack_mA8 == 0) goto loc_00A62202;
    result = wcsicmp(v_stack_m58, v_stack_mA8, (unsigned int)(v_stack_mB4), 1);
    if ((unsigned int)(result) == 0) goto loc_00A62202;
    goto loc_00A6218E;
loc_00A62310:
    a2 = ((unsigned int)((unsigned int)((unsigned int)(v_stack_mB4))) + (unsigned int)((unsigned int)((unsigned int)(v_stack_mB4))) * 2) << (4);
    a1 = (v_stack_m70) - (*(unsigned __int64 *)(a2 + *(unsigned __int64 *)(v_rsi) * 1));
    a1 = (v_stack_m68) - (*(unsigned __int64 *)(a2 + *(unsigned __int64 *)(v_rsi) * 1 + 8));
loc_00A62345:
    a1 = 5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90 + 76)))) > 5) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90 + 76))); }
    v_r12 = (unsigned int)(((unsigned int)((unsigned int)((unsigned int)(a7)))) + ((unsigned int)(a1)));
    goto loc_00A6209A;
loc_00A6235E:
    a1 = 5;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90 + 76)))) > 5) { a1 = (unsigned int)((unsigned int)(*(unsigned int *)(v_stack_m90 + 76))); }
    v_r12 = (unsigned int)((v_r12) + ((unsigned int)(a1)));
    goto loc_00A61FF7;
loc_00A62377:
    goto loc_00A620D8;
}
```

## 5. (Beta) C Style

```c
int64_t PiDqActionDataGetChangedProperties(int64_t Arg1, int32_t Arg2, int64_t Arg3, uint8_t Arg4, int64_t Arg5, int64_t Arg6, uint32_t Arg7, int64_t Arg8, int64_t Arg9, void *Arg10)
{
    uint8_t *arg10 = (uint8_t *)Arg10;

    int64_t result;
    int64_t local_r12;
    int64_t local_r15;
    int64_t local_rbx;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m3F;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m5C;
    uint64_t v_stack_m60;
    uint64_t v_stack_m68;
    uint64_t v_stack_m70;
    uint64_t v_stack_m78;
    uint64_t v_stack_m80;
    uint64_t v_stack_m88;
    uint64_t v_stack_m90;
    uint64_t v_stack_m98;
    uint64_t v_stack_mA0;
    uint64_t v_stack_mA8;
    uint32_t v_stack_mB0;
    uint32_t v_stack_mB4;
    uint8_t v_stack_mB8;
    uint64_t v_stack_mD8;
    uint64_t v_stack_mE0;
    uint32_t v_stack_mE8;
    uint64_t v_stack_p20;
    uint64_t v_stack_p28;
    uint64_t v_stack_p30;

    v_stack_p20 = local_rbx;
    local_rsp = (local_rsp) - (208);
    result = (*(uint64_t *)(v_rip + 0x3A880D)) ^ (local_rsp);
    v_stack_m40 = result;
    v_stack_m78 = Arg1;
    v_stack_mA0 = Arg9;
    local_rsi = 0;
    v_stack_mA8 = 0;
    v_stack_m80 = 0;
    *(uint32_t *)(arg10) = 0;
    v_stack_mB8 = Arg4;
    v_stack_m98 = Arg3;
    v_stack_mB4 = Arg2;
    v_stack_m88 = Arg5;
    v_stack_m90 = Arg8;
    v_stack_m70 = v_xmm0;
    v_stack_m60 = v_xmm0;
    v_stack_m50 = v_xmm0;
    result = PiPnpRtlBeginOperation(v_stack_m80, Arg2, Arg3, Arg4);
loc_00A61F99:
    v_stack_mB0 = 0;
    if (0 >= (*(uint32_t *)(Arg8 + 0x4C))) goto loc_00A620D8;
    local_r15 = (0) << (5);
    local_r15 = (local_r15) + (Arg8);
    if (Arg6 != 0) goto loc_00A621AA;
loc_00A61FC0:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x64))) != 0) goto loc_00A62270;
loc_00A61FCD:
    result = 0;
    if (sign_flag) goto loc_00A620D8;
    if (v_stack_mB8 != 0) goto loc_00A62123;
    if (0 > ((uint32_t)((uint32_t)(*(uint32_t *)(arg10))))) goto loc_00A6200E;
    if (Arg7 <= 0) goto loc_00A6235E;
loc_00A61FF7:
    result = PiDqGrowPropertyArray(v_stack_mA0, (uint32_t)(*(uint32_t *)(arg10)), (uint32_t)((uint32_t)((uint32_t)(Arg7))), Arg4);
    if (sign_flag) goto loc_00A620D8;
loc_00A6200E:
    Arg1 = ((uint32_t)(*(uint32_t *)(arg10)) + (uint32_t)(*(uint32_t *)(arg10)) * 2) << (4);
    Arg1 = (Arg1) + (*(uint64_t *)(v_stack_mA0));
    v_stack_mD8 = Arg1;
    v_stack_mE0 = *(uint64_t *)(local_r15 + 0x68);
    v_stack_mE8 = (uint32_t)((uint32_t)(*(uint32_t *)(local_r15 + 0x64)));
    result = PiDqPnPGetObjectProperty(v_stack_m98, (uint32_t)((uint32_t)((uint32_t)(v_stack_mB4))), 0, local_r15 + 80);
    local_rsi = 0;
    if (sign_flag) goto loc_00A620D8;
loc_00A6205A:
    result = (uint32_t)(((uint32_t)(v_stack_mB0)) + 1);
    goto loc_00A61F99;
loc_00A62068:
    if (0 < ((uint32_t)((uint32_t)(*(uint32_t *)(arg10))))) goto loc_00A62310;
    if (((uint32_t)((uint32_t)(Arg7))) > ((uint32_t)((uint32_t)(*(uint32_t *)(arg10))))) goto loc_00A62230;
    if ((uint32_t)((uint32_t)(Arg7)) == 0) goto loc_00A62345;
loc_00A6209A:
    result = PiDqGrowPropertyArray(v_stack_mA0, (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg10)))), (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg7))))), local_r15 + 80);
    if (!sign_flag) goto loc_00A62230;
    if (v_stack_m90 != 0) {
        Arg2 = 0x58706E50ULL;
        Arg1 = v_stack_m90;
        result = ExFreePoolWithTag(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg7))))), local_r15 + 80);
    }
    if (v_stack_m48 != 0) {
        Arg2 = 0x58706E50ULL;
        result = ExFreePoolWithTag(v_stack_m48, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg7))))), local_r15 + 80);
    }
    if ((v_stack_mA8 - 1) <= -3) goto loc_00A62263;
loc_00A620EA:
    result = v_stack_mA8 - 1;
    if (v_stack_m80 != 0) {
        result = PiPnpRtlEndOperation(v_stack_m80, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg7))))), local_r15 + 80);
    }
    Arg1 = (v_stack_m40) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, (uint32_t)((uint32_t)((uint32_t)((uint32_t)((uint32_t)(Arg7))))), local_r15 + 80);
    local_rsp = (local_rsp) + (208);
    return result;
loc_00A62123:
    v_stack_p30 = v_stack_m70;
    v_stack_p28 = v_stack_m88;
    v_stack_p20 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90)));
    result = PiDqPnPGetObjectPropertyInBestLocale(v_stack_m98, (uint32_t)((uint32_t)(v_stack_mA0)), v_stack_p20, local_r15 + 80);
    local_rsi = 0;
    if (sign_flag) goto loc_00A620D8;
loc_00A6215E:
    result = (uint16_t)(-(*(uint16_t *)(v_stack_m88)));
    local_rbx = (v_stack_p20) & (v_stack_m88);
    if ((*(uint64_t *)(local_r15 + 0x68)) == local_rbx) goto loc_00A62068;
    if (*(uint64_t *)(local_r15 + 0x68) != 0) goto loc_00A622D1;
loc_00A62180:
    if (v_stack_m58 == local_rbx) goto loc_00A62202;
    if (v_stack_m58 != 0) goto loc_00A622EF;
loc_00A6218E:
    if (local_rbx == 0) goto loc_00A62202;
    result = (result) | (-1);
loc_00A62197:
    result = (result) + 1;
    if ((*(uint16_t *)(local_rbx + result * 2)) != 0) goto loc_00A62197;
    goto loc_00A6215E;
loc_00A621AA:
loc_00A621AD:
    if (0 >= Arg7) goto loc_00A6205A;
    Arg1 = (0) << (5);
    Arg1 = (Arg1) + (Arg6);
    if ((*(uint32_t *)(local_r15 + 0x60)) == ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x10))))) goto loc_00A621D0;
loc_00A621CB:
    Arg3 = (uint32_t)((0) + 1);
    goto loc_00A621AD;
loc_00A621D0:
    Arg2 = (*(uint64_t *)(local_r15 + 0x50)) - (*(uint64_t *)(Arg1));
    if (!(condition_is_not_equal)) {
        Arg2 = *(uint64_t *)(local_r15 + 0x58);
        Arg2 = (Arg2) - (*(uint64_t *)(Arg1 + 0x8));
    }
    if (Arg2 != 0) goto loc_00A621CB;
    if ((*(uint32_t *)(v_stack_m58)) != ((uint32_t)((uint32_t)(*(uint32_t *)(Arg1 + 0x14))))) goto loc_00A621CB;
    if ((*(uint64_t *)(local_r15 + 0x68)) == 0) goto loc_00A61FC0;
    if (v_stack_mB8 == 0) goto loc_00A621CB;
    goto loc_00A61FC0;
loc_00A62202:
    result = (uint32_t)(*(uint32_t *)(Arg1 + 0x14));
    if (v_stack_m58 != 0) {
        Arg2 = 0x58706E50ULL;
        Arg1 = v_stack_m58;
        result = ExFreePoolWithTag(Arg1, Arg2, Arg3, local_r15 + 80);
    }
    if (v_stack_m48 == 0) goto loc_00A6205A;
    result = ExFreePoolWithTag(v_stack_m48, (uint32_t)(0x58706E50ULL), Arg3, local_r15 + 80);
    goto loc_00A6205A;
loc_00A62230:
    Arg1 = ((uint32_t)(*(uint32_t *)(arg10)) + (uint32_t)(*(uint32_t *)(arg10)) * 2) + ((uint32_t)(*(uint32_t *)(arg10)) + (uint32_t)(*(uint32_t *)(arg10)) * 2);
    *(uint64_t *)(*(uint64_t *)(local_rsi) + Arg1 * 8) = v_xmm0;
    *(uint64_t *)(*(uint64_t *)(local_rsi) + Arg1 * 8 + 0x10) = v_xmm1;
    *(uint64_t *)(*(uint64_t *)(local_rsi) + Arg1 * 8 + 0x20) = v_xmm0;
loc_00A6225C:
    local_rsi = 0;
    goto loc_00A6205A;
loc_00A62263:
    result = ZwClose(local_rbx, (uint32_t)(0x58706E50ULL), Arg3, local_r15 + 80);
    goto loc_00A620EA;
loc_00A62270:
    if (((uint32_t)(local_rbx)) != 1) goto loc_00A62377;
    local_rbx = 0;
    if (v_stack_mA8 == 0) goto loc_00A62290;
loc_00A62281:
    if (v_stack_mA8 == -1) goto loc_00A6225C;
    goto loc_00A61FCD;
loc_00A62290:
    v_stack_p30 = v_stack_mA8;
    v_stack_p28 = v_stack_m78;
    v_stack_p20 = (uint8_t)(v_stack_mA8);
    result = PiDqOpenObjectRegKey(1, v_stack_m98, (uint32_t)(v_stack_mB4), 1);
    if (((uint32_t)(result)) != 0xC0000034ULL) goto loc_00A62281;
    goto loc_00A62281;
loc_00A622D1:
    if (v_stack_mA8 == 0) goto loc_00A62180;
    result = wcsicmp(1, v_stack_mA8, (uint32_t)(v_stack_mB4), 1);
    if ((uint32_t)(result) == 0) goto loc_00A62068;
    goto loc_00A62180;
loc_00A622EF:
    if (v_stack_mA8 == 0) goto loc_00A62202;
    result = wcsicmp(v_stack_m58, v_stack_mA8, (uint32_t)(v_stack_mB4), 1);
    if ((uint32_t)(result) == 0) goto loc_00A62202;
    goto loc_00A6218E;
loc_00A62310:
    Arg2 = ((uint32_t)((uint32_t)((uint32_t)(v_stack_mB4))) + (uint32_t)((uint32_t)((uint32_t)(v_stack_mB4))) * 2) << (4);
    Arg1 = (v_stack_m70) - (*(uint64_t *)(Arg2 + *(uint64_t *)(local_rsi) * 1));
    Arg1 = (v_stack_m68) - (*(uint64_t *)(Arg2 + *(uint64_t *)(local_rsi) * 1 + 0x8));
loc_00A62345:
    Arg1 = 5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x4C)))) > 5) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x4C))); }
    local_r12 = (uint32_t)(((uint32_t)((uint32_t)((uint32_t)(Arg7)))) + ((uint32_t)(Arg1)));
    goto loc_00A6209A;
loc_00A6235E:
    Arg1 = 5;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x4C)))) > 5) { Arg1 = (uint32_t)((uint32_t)(*(uint32_t *)(v_stack_m90 + 0x4C))); }
    local_r12 = (uint32_t)((local_r12) + ((uint32_t)(Arg1)));
    goto loc_00A61FF7;
loc_00A62377:
    goto loc_00A620D8;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg10` | `+ 0x0` | `32` | `R` |
| `Arg10` | `+ 0x0` | `32` | `R/W` |
| `Arg10` | `+ 0x0` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=page&rva=0x00A61F10&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
