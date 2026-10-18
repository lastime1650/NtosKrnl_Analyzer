# PopPepTriggerActivity

- RVA: `0x0024CDB0`–`0x0024D0C4` (길이 `788` bytes)
- VA: `0x000000014024CDB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00062CCC`
- 디코드: `209`개 명령, `788/788` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **5**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **8**
- RIP 상대 이미지 참조: **4**

### Outgoing calls
- `0x0024CEB5` → [PopPepTriggerComponentActiveActivity](PopPepTriggerComponentActiveActivity_function_0024D860.md) (function, `0x0024D860`)
- `0x0024CEBF` → [PopPepTriggerComponentActivatingActivity](PopPepTriggerComponentActivatingActivity_function_0024D790.md) (function, `0x0024D790`)
- `0x0024D088` → [PopPepTriggerComponentIdleStateChangeActivity](../46/PopPepTriggerComponentIdleStateChangeActivity_function_00463D90.md) (function, `0x00463D90`)
- `0x0024D0A6` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0024D0BE` → [PopFxBugCheck](../2B/PopFxBugCheck_function_002BFC6C.md) (function, `0x002BFC6C`)

### Direct callers
- [PopPepProcessEvent](PopPepProcessEvent_function_0024B930.md) at `0x0024C1C3`
- [PopPepCompleteComponentActiveActivity](PopPepCompleteComponentActiveActivity_function_0024D5F0.md) at `0x0024D6CE`
- [PopPepTriggerComponentActivatingActivity](PopPepTriggerComponentActivatingActivity_function_0024D790.md) at `0x0024D82B`
- [PopPepTriggerComponentActivatingActivity](PopPepTriggerComponentActivatingActivity_function_0024D790.md) at `0x0024D845`
- [PopPepSurprisePowerOn](../26/PopPepSurprisePowerOn_function_0026E480.md) at `0x0026E4FB`
- [PopPepCompleteComponentIdleStateChangeActivity](../2B/PopPepCompleteComponentIdleStateChangeActivity_function_002BF1B0.md) at `0x002BF2ED`
- [PopPepComponentSetLatency](../2B/PopPepComponentSetLatency_function_002BF3D8.md) at `0x002BF574`
- [PopPepUpdateIdleState](../2B/PopPepUpdateIdleState_function_002BF794.md) at `0x002BF7E8`
- [PopPepTriggerComponentIdleStateChangeActivity](../46/PopPepTriggerComponentIdleStateChangeActivity_function_00463D90.md) at `0x00463E0A`

### Static image references
- `0x0024CDC7` → RVA `0x00001030` (`.rdata`; read)
- `0x0024CE80` → RVA `0x0024D790` (`PopPepTriggerComponentActivatingActivity`; read)
- `0x0024CEA2` → RVA `0x0024D860` (`PopPepTriggerComponentActiveActivity`; read)
- `0x0024D079` → RVA `0x00463D90` (`PopPepTriggerComponentIdleStateChangeActivity`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0024CDB0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0024CDB5  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
0024CDBA  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
0024CDBF  57                              push rdi
0024CDC0  48 83 EC 20                     sub rsp, 0x20
0024CDC4  49 63 D8                        movsxd rbx, r8d
0024CDC7  48 8D 2D 62 42 DB FF            lea rbp, [rip - 0x24bd9e]
0024CDCE  48 69 C3 88 00 00 00            imul rax, rbx, 0x88
0024CDD5  48 8B F2                        mov rsi, rdx
0024CDD8  48 8B F9                        mov rdi, rcx
0024CDDB  4C 8B DB                        mov r11, rbx
0024CDDE  44 8B 54 28 04                  mov r10d, dword ptr [rax + rbp + 4]
0024CDE3  45 85 D2                        test r10d, r10d
0024CDE6  74 32                           je 0x14024ce1a
0024CDE8  41 83 FA 01                     cmp r10d, 1
0024CDEC  0F 85 57 01 00 00               jne 0x14024cf49
0024CDF2  49 6B D3 22                     imul rdx, r11, 0x22
0024CDF6  8B 4C 95 28                     mov ecx, dword ptr [rbp + rdx*4 + 0x28]
0024CDFA  85 C9                           test ecx, ecx
0024CDFC  0F 85 D8 00 00 00               jne 0x14024ceda
0024CE02  8B 4C 95 38                     mov ecx, dword ptr [rbp + rdx*4 + 0x38]
0024CE06  85 C9                           test ecx, ecx
0024CE08  0F 85 F2 00 00 00               jne 0x14024cf00
0024CE0E  8B 4C 95 3C                     mov ecx, dword ptr [rbp + rdx*4 + 0x3c]
0024CE12  85 C9                           test ecx, ecx
0024CE14  0F 85 0C 01 00 00               jne 0x14024cf26
0024CE1A  33 D2                           xor edx, edx
0024CE1C  83 FB 05                        cmp ebx, 5
0024CE1F  77 11                           ja 0x14024ce32
0024CE21  49 69 C3 88 00 00 00            imul rax, r11, 0x88
0024CE28  80 3C 28 01                     cmp byte ptr [rax + rbp], 1
0024CE2C  0F 84 60 02 00 00               je 0x14024d092
0024CE32  8B CA                           mov ecx, edx
0024CE34  48 8D 46 38                     lea rax, [rsi + 0x38]
0024CE38  83 F9 01                        cmp ecx, 1
0024CE3B  4C 8D 57 48                     lea r10, [rdi + 0x48]
0024CE3F  4C 0F 45 D0                     cmovne r10, rax
0024CE43  48 8B C2                        mov rax, rdx
0024CE46  83 FA 06                        cmp edx, 6
0024CE49  7D 24                           jge 0x14024ce6f
0024CE4B  4D 8B 04 C2                     mov r8, qword ptr [r10 + rax*8]
0024CE4F  4D 85 C0                        test r8, r8
0024CE52  74 14                           je 0x14024ce68
0024CE54  49 6B CB 22                     imul rcx, r11, 0x22
0024CE58  48 03 C8                        add rcx, rax
0024CE5B  8B 4C 8D 10                     mov ecx, dword ptr [rbp + rcx*4 + 0x10]
0024CE5F  41 85 08                        test dword ptr [r8], ecx
0024CE62  0F 85 48 02 00 00               jne 0x14024d0b0
0024CE68  FF C2                           inc edx
0024CE6A  48 FF C0                        inc rax
0024CE6D  EB D7                           jmp 0x14024ce46
0024CE6F  48 85 F6                        test rsi, rsi
0024CE72  0F 84 24 02 00 00               je 0x14024d09c
0024CE78  48 8B 44 DE 38                  mov rax, qword ptr [rsi + rbx*8 + 0x38]
0024CE7D  83 08 01                        or dword ptr [rax], 1
0024CE80  48 8D 0D 09 09 00 00            lea rcx, [rip + 0x909]
0024CE87  44 89 48 04                     mov dword ptr [rax + 4], r9d
0024CE8B  45 8B C1                        mov r8d, r9d
0024CE8E  49 69 C3 88 00 00 00            imul rax, r11, 0x88
0024CE95  48 8B D6                        mov rdx, rsi
0024CE98  48 8B 44 28 70                  mov rax, qword ptr [rax + rbp + 0x70]
0024CE9D  48 3B C1                        cmp rax, rcx
0024CEA0  74 1A                           je 0x14024cebc
0024CEA2  48 8D 0D B7 09 00 00            lea rcx, [rip + 0x9b7]
0024CEA9  48 3B C1                        cmp rax, rcx
0024CEAC  0F 85 C7 01 00 00               jne 0x14024d079
0024CEB2  48 8B CF                        mov rcx, rdi
0024CEB5  E8 A6 09 00 00                  call 0x14024d860
0024CEBA  EB 08                           jmp 0x14024cec4
0024CEBC  48 8B CF                        mov rcx, rdi
0024CEBF  E8 CC 08 00 00                  call 0x14024d790
0024CEC4  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
0024CEC9  48 8B 6C 24 38                  mov rbp, qword ptr [rsp + 0x38]
0024CECE  48 8B 74 24 40                  mov rsi, qword ptr [rsp + 0x40]
0024CED3  48 83 C4 20                     add rsp, 0x20
0024CED7  5F                              pop rdi
0024CED8  C3                              ret
0024CED9  CC                              int3
0024CEDA  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
0024CEDE  44 8B 00                        mov r8d, dword ptr [rax]
0024CEE1  44 85 C1                        test ecx, r8d
0024CEE4  0F 84 18 FF FF FF               je 0x14024ce02
0024CEEA  41 F6 C0 02                     test r8b, 2
0024CEEE  74 04                           je 0x14024cef4
0024CEF0  F0 FF 4F 78                     lock dec dword ptr [rdi + 0x78]
0024CEF4  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
0024CEF8  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024CEFB  E9 02 FF FF FF                  jmp 0x14024ce02
0024CF00  48 8B 47 68                     mov rax, qword ptr [rdi + 0x68]
0024CF04  44 8B 00                        mov r8d, dword ptr [rax]
0024CF07  44 85 C1                        test ecx, r8d
0024CF0A  0F 84 FE FE FF FF               je 0x14024ce0e
0024CF10  41 F6 C0 02                     test r8b, 2
0024CF14  74 04                           je 0x14024cf1a
0024CF16  F0 FF 4F 78                     lock dec dword ptr [rdi + 0x78]
0024CF1A  48 8B 47 68                     mov rax, qword ptr [rdi + 0x68]
0024CF1E  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024CF21  E9 E8 FE FF FF                  jmp 0x14024ce0e
0024CF26  48 8B 47 70                     mov rax, qword ptr [rdi + 0x70]
0024CF2A  8B 10                           mov edx, dword ptr [rax]
0024CF2C  85 CA                           test edx, ecx
0024CF2E  0F 84 E6 FE FF FF               je 0x14024ce1a
0024CF34  F6 C2 02                        test dl, 2
0024CF37  74 04                           je 0x14024cf3d
0024CF39  F0 FF 4F 78                     lock dec dword ptr [rdi + 0x78]
0024CF3D  48 8B 47 70                     mov rax, qword ptr [rdi + 0x70]
0024CF41  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024CF44  E9 D1 FE FF FF                  jmp 0x14024ce1a
0024CF49  41 83 FA 02                     cmp r10d, 2
0024CF4D  0F 85 C7 FE FF FF               jne 0x14024ce1a
0024CF53  80 79 7D 00                     cmp byte ptr [rcx + 0x7d], 0
0024CF57  74 13                           je 0x14024cf6c
0024CF59  49 69 C3 88 00 00 00            imul rax, r11, 0x88
0024CF60  8B 4C 28 28                     mov ecx, dword ptr [rax + rbp + 0x28]
0024CF64  85 C9                           test ecx, ecx
0024CF66  0F 85 EA 00 00 00               jne 0x14024d056
0024CF6C  49 6B D3 22                     imul rdx, r11, 0x22
0024CF70  8B 4C 95 2C                     mov ecx, dword ptr [rbp + rdx*4 + 0x2c]
0024CF74  85 C9                           test ecx, ecx
0024CF76  75 57                           jne 0x14024cfcf
0024CF78  8B 4C 95 30                     mov ecx, dword ptr [rbp + rdx*4 + 0x30]
0024CF7C  85 C9                           test ecx, ecx
0024CF7E  75 6E                           jne 0x14024cfee
0024CF80  8B 4C 95 34                     mov ecx, dword ptr [rbp + rdx*4 + 0x34]
0024CF84  85 C9                           test ecx, ecx
0024CF86  0F 85 84 00 00 00               jne 0x14024d010
0024CF8C  80 7F 7D 00                     cmp byte ptr [rdi + 0x7d], 0
0024CF90  0F 84 84 FE FF FF               je 0x14024ce1a
0024CF96  49 69 C3 88 00 00 00            imul rax, r11, 0x88
0024CF9D  8B 4C 28 38                     mov ecx, dword ptr [rax + rbp + 0x38]
0024CFA1  85 C9                           test ecx, ecx
0024CFA3  0F 85 8A 00 00 00               jne 0x14024d033
0024CFA9  49 69 C3 88 00 00 00            imul rax, r11, 0x88
0024CFB0  8B 4C 28 3C                     mov ecx, dword ptr [rax + rbp + 0x3c]
0024CFB4  85 C9                           test ecx, ecx
0024CFB6  0F 84 5E FE FF FF               je 0x14024ce1a
0024CFBC  48 8B 47 70                     mov rax, qword ptr [rdi + 0x70]
0024CFC0  8B 10                           mov edx, dword ptr [rax]
0024CFC2  85 CA                           test edx, ecx
0024CFC4  0F 84 50 FE FF FF               je 0x14024ce1a
0024CFCA  E9 65 FF FF FF                  jmp 0x14024cf34
0024CFCF  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
0024CFD3  44 8B 00                        mov r8d, dword ptr [rax]
0024CFD6  44 85 C1                        test ecx, r8d
0024CFD9  74 9D                           je 0x14024cf78
0024CFDB  41 F6 C0 02                     test r8b, 2
0024CFDF  74 04                           je 0x14024cfe5
0024CFE1  F0 FF 4E 68                     lock dec dword ptr [rsi + 0x68]
0024CFE5  48 8B 46 40                     mov rax, qword ptr [rsi + 0x40]
0024CFE9  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024CFEC  EB 8A                           jmp 0x14024cf78
0024CFEE  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
0024CFF2  44 8B 00                        mov r8d, dword ptr [rax]
0024CFF5  44 85 C1                        test ecx, r8d
0024CFF8  74 86                           je 0x14024cf80
0024CFFA  41 F6 C0 02                     test r8b, 2
0024CFFE  74 04                           je 0x14024d004
0024D000  F0 FF 4E 68                     lock dec dword ptr [rsi + 0x68]
0024D004  48 8B 46 48                     mov rax, qword ptr [rsi + 0x48]
0024D008  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024D00B  E9 70 FF FF FF                  jmp 0x14024cf80
0024D010  48 8B 46 50                     mov rax, qword ptr [rsi + 0x50]
0024D014  8B 10                           mov edx, dword ptr [rax]
0024D016  85 D1                           test ecx, edx
0024D018  0F 84 6E FF FF FF               je 0x14024cf8c
0024D01E  F6 C2 02                        test dl, 2
0024D021  74 04                           je 0x14024d027
0024D023  F0 FF 4E 68                     lock dec dword ptr [rsi + 0x68]
0024D027  48 8B 46 50                     mov rax, qword ptr [rsi + 0x50]
0024D02B  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024D02E  E9 59 FF FF FF                  jmp 0x14024cf8c
0024D033  48 8B 47 68                     mov rax, qword ptr [rdi + 0x68]
0024D037  8B 10                           mov edx, dword ptr [rax]
0024D039  85 CA                           test edx, ecx
0024D03B  0F 84 68 FF FF FF               je 0x14024cfa9
0024D041  F6 C2 02                        test dl, 2
0024D044  74 04                           je 0x14024d04a
0024D046  F0 FF 4F 78                     lock dec dword ptr [rdi + 0x78]
0024D04A  48 8B 47 68                     mov rax, qword ptr [rdi + 0x68]
0024D04E  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024D051  E9 53 FF FF FF                  jmp 0x14024cfa9
0024D056  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
0024D05A  8B 10                           mov edx, dword ptr [rax]
0024D05C  85 CA                           test edx, ecx
0024D05E  0F 84 08 FF FF FF               je 0x14024cf6c
0024D064  F6 C2 02                        test dl, 2
0024D067  74 04                           je 0x14024d06d
0024D069  F0 FF 4F 78                     lock dec dword ptr [rdi + 0x78]
0024D06D  48 8B 47 48                     mov rax, qword ptr [rdi + 0x48]
0024D071  83 20 FC                        and dword ptr [rax], 0xfffffffc
0024D074  E9 F3 FE FF FF                  jmp 0x14024cf6c
0024D079  48 8D 0D 10 6D 21 00            lea rcx, [rip + 0x216d10]
0024D080  48 3B C1                        cmp rax, rcx
0024D083  48 8B CF                        mov rcx, rdi
0024D086  75 1E                           jne 0x14024d0a6
0024D088  E8 03 6D 21 00                  call 0x140463d90
0024D08D  E9 32 FE FF FF                  jmp 0x14024cec4
0024D092  B9 01 00 00 00                  mov ecx, 1
0024D097  E9 98 FD FF FF                  jmp 0x14024ce34
0024D09C  48 8B 44 DF 48                  mov rax, qword ptr [rdi + rbx*8 + 0x48]
0024D0A1  E9 D7 FD FF FF                  jmp 0x14024ce7d
0024D0A6  E8 25 DA 46 00                  call 0x1406baad0
0024D0AB  E9 14 FE FF FF                  jmp 0x14024cec4
0024D0B0  4C 63 CA                        movsxd r9, edx
0024D0B3  4D 8B C3                        mov r8, r11
0024D0B6  49 8B D2                        mov rdx, r10
0024D0B9  B9 66 06 00 00                  mov ecx, 0x666
0024D0BE  E8 A9 2B 07 00                  call 0x1402bfc6c
0024D0C3  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall PopPepTriggerActivity(__int64 a1, __int64 a2, int a3, int a4)
{
    __int64 result;
    __int64 v_r10;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    result = (result) * ((int)(a3));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + v_rip - 2407838 * 1 + 4))) == 0) goto loc_0024CE1A;
    if (((unsigned int)((unsigned int)(*(unsigned int *)(result + v_rip - 2407838 * 1 + 4)))) != 1) goto loc_0024CF49;
    a2 = (a2) * ((int)(a3));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2407838 + a2 * 4 + 40))) != 0) goto loc_0024CEDA;
loc_0024CE02:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2407838 + a2 * 4 + 56))) != 0) goto loc_0024CF00;
loc_0024CE0E:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2407838 + a2 * 4 + 60))) != 0) goto loc_0024CF26;
loc_0024CE1A:
    a2 = 0;
    if (((unsigned int)((int)(a3))) > 5) goto loc_0024CE32;
    result = (result) * ((int)(a3));
    if ((*(unsigned __int8 *)(result + v_rip - 2407838 * 1)) == 1) goto loc_0024D092;
loc_0024CE32:
loc_0024CE34:
    v_r10 = a1 + 72;
    if (0 != 1) { v_r10 = a2 + 56; }
loc_0024CE46:
    if (0 >= 6) goto loc_0024CE6F;
    if (*(unsigned __int64 *)(v_r10 + 0 * 8) == 0) goto loc_0024CE68;
    a1 = (0) * ((int)(a3));
    a1 = (a1) + (0);
    if (((*(unsigned int *)(*(unsigned __int64 *)(v_r10 + 0 * 8))) & ((unsigned int)((unsigned int)(*(unsigned int *)(v_rip - 2407838 + a1 * 4 + 16))))) != 0) goto loc_0024D0B0;
loc_0024CE68:
    a2 = (unsigned int)((a2) + 1);
    result = (0) + 1;
    goto loc_0024CE46;
loc_0024CE6F:
    if (a2 == 0) goto loc_0024D09C;
loc_0024CE7D:
    *(unsigned int *)(*(unsigned __int64 *)(a2 + (int)(a3) * 8 + 56) + 4) = a4;
    result = (*(unsigned __int64 *)(a2 + (int)(a3) * 8 + 56)) * ((int)(a3));
    if ((*(unsigned __int64 *)(result + v_rip - 2407838 * 1 + 112)) == (v_rip + 2313)) goto loc_0024CEBC;
    if ((*(unsigned __int64 *)(result + v_rip - 2407838 * 1 + 112)) != (v_rip + 2487)) goto loc_0024D079;
    result = PopPepTriggerComponentActiveActivity(a1, a2, (unsigned int)(a4), a4);
    goto loc_0024CEC4;
loc_0024CEBC:
    result = PopPepTriggerComponentActivatingActivity(a1, a2, (unsigned int)(a4), a4);
loc_0024CEC4:
    v_rsp = (v_rsp) + (32);
    return result;
loc_0024CEDA:
    if ((((unsigned int)(a1)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72)))))) == 0) goto loc_0024CE02;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72))))) & (2)) != 0) {
    }
    goto loc_0024CE02;
loc_0024CF00:
    if ((((unsigned int)(a1)) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 104)))))) == 0) goto loc_0024CE0E;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 104))))) & (2)) != 0) {
    }
    goto loc_0024CE0E;
loc_0024CF26:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 112))))) & ((unsigned int)(a1))) == 0) goto loc_0024CE1A;
loc_0024CF34:
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 112))))) & (2)) != 0) {
    }
    goto loc_0024CE1A;
loc_0024CF49:
    if (((unsigned int)(v_r10)) != 2) goto loc_0024CE1A;
    if ((*(unsigned __int8 *)(a1 + 125)) == 0) goto loc_0024CF6C;
    result = (*(unsigned __int64 *)(a1 + 112)) * ((int)(a3));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_p10 * 1 + 40))) != 0) goto loc_0024D056;
loc_0024CF6C:
    a2 = ((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 112)))) * ((int)(a3));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + a2 * 4 + 44))) != 0) goto loc_0024CFCF;
loc_0024CF78:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + a2 * 4 + 48))) != 0) goto loc_0024CFEE;
loc_0024CF80:
    if ((unsigned int)((unsigned int)(*(unsigned int *)(v_stack_p10 + a2 * 4 + 52))) != 0) goto loc_0024D010;
loc_0024CF8C:
    if ((*(unsigned __int8 *)(a1 + 125)) == 0) goto loc_0024CE1A;
    result = (result) * ((int)(a3));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_p10 * 1 + 56))) != 0) goto loc_0024D033;
loc_0024CFA9:
    result = (result) * ((int)(a3));
    if ((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_p10 * 1 + 60))) == 0) goto loc_0024CE1A;
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 112))))) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_p10 * 1 + 60))))) == 0) goto loc_0024CE1A;
    goto loc_0024CF34;
loc_0024CFCF:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_p10 * 1 + 60)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 64)))))) == 0) goto loc_0024CF78;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 64))))) & (2)) != 0) {
    }
    goto loc_0024CF78;
loc_0024CFEE:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_p10 * 1 + 60)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 72)))))) == 0) goto loc_0024CF80;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 72))))) & (2)) != 0) {
    }
    goto loc_0024CF80;
loc_0024D010:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_p10 * 1 + 60)))) & ((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 80)))))) == 0) goto loc_0024CF8C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 80))))) & (2)) != 0) {
    }
    goto loc_0024CF8C;
loc_0024D033:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 104))))) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_p10 * 1 + 60))))) == 0) goto loc_0024CFA9;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 104))))) & (2)) != 0) {
    }
    goto loc_0024CFA9;
loc_0024D056:
    if ((((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72))))) & ((unsigned int)((unsigned int)(*(unsigned int *)(result + v_stack_p10 * 1 + 60))))) == 0) goto loc_0024CF6C;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72))))) & (2)) != 0) {
    }
    goto loc_0024CF6C;
loc_0024D079:
    if ((*(unsigned __int64 *)(a1 + 72)) != (v_rip + 2190608)) goto loc_0024D0A6;
    result = PopPepTriggerComponentIdleStateChangeActivity(a1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72))), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 72))), a4);
    goto loc_0024CEC4;
loc_0024D092:
    goto loc_0024CE34;
loc_0024D09C:
    goto loc_0024CE7D;
loc_0024D0A6:
    result = guard_dispatch_icall(1, (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72))), (unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(v_stack_p18 + 72))), a4);
    goto loc_0024CEC4;
loc_0024D0B0:
    result = PopFxBugCheck((unsigned int)(0x666ULL), v_r10, (int)(a3), (int)((unsigned int)((unsigned int)(*(unsigned int *)(*(unsigned __int64 *)(a1 + 72))))));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t PopPepTriggerActivity(void *Arg1, void *Arg2, int32_t Arg3, int32_t Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_r10;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    result = (result) * ((int32_t)(Arg3));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + v_rip - 0x24BD9E * 1 + 0x4))) == 0) goto loc_0024CE1A;
    if (((uint32_t)((uint32_t)(*(uint32_t *)(result + v_rip - 0x24BD9E * 1 + 0x4)))) != 1) goto loc_0024CF49;
    Arg2 = (Arg2) * ((int32_t)(Arg3));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x24BD9E + arg2 * 4 + 0x28))) != 0) goto loc_0024CEDA;
loc_0024CE02:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x24BD9E + arg2 * 4 + 0x38))) != 0) goto loc_0024CF00;
loc_0024CE0E:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x24BD9E + arg2 * 4 + 0x3C))) != 0) goto loc_0024CF26;
loc_0024CE1A:
    Arg2 = 0;
    if (((uint32_t)((int32_t)(Arg3))) > 5) goto loc_0024CE32;
    result = (result) * ((int32_t)(Arg3));
    if ((*(uint8_t *)(result + v_rip - 0x24BD9E * 1)) == 1) goto loc_0024D092;
loc_0024CE32:
loc_0024CE34:
    local_r10 = Arg1 + 72;
    if (0 != 1) { local_r10 = Arg2 + 56; }
loc_0024CE46:
    if (0 >= 6) goto loc_0024CE6F;
    if (*(uint64_t *)(local_r10 + 0x0 * 8) == 0) goto loc_0024CE68;
    Arg1 = (0) * ((int32_t)(Arg3));
    Arg1 = (Arg1) + (0);
    if (((*(uint32_t *)(*(uint64_t *)(local_r10 + 0x0 * 8))) & ((uint32_t)((uint32_t)(*(uint32_t *)(v_rip - 0x24BD9E + arg1 * 4 + 0x10))))) != 0) goto loc_0024D0B0;
loc_0024CE68:
    Arg2 = (uint32_t)((Arg2) + 1);
    result = (0) + 1;
    goto loc_0024CE46;
loc_0024CE6F:
    if (Arg2 == NULL) goto loc_0024D09C;
loc_0024CE7D:
    *(uint32_t *)(*(uint64_t *)(arg2 + (int32_t)(Arg3) * 8 + 0x38) + 0x4) = Arg4;
    result = (*(uint64_t *)(arg2 + (int32_t)(Arg3) * 8 + 0x38)) * ((int32_t)(Arg3));
    if ((*(uint64_t *)(result + v_rip - 0x24BD9E * 1 + 0x70)) == (v_rip + 2313)) goto loc_0024CEBC;
    if ((*(uint64_t *)(result + v_rip - 0x24BD9E * 1 + 0x70)) != (v_rip + 2487)) goto loc_0024D079;
    result = PopPepTriggerComponentActiveActivity(Arg1, Arg2, (uint32_t)(Arg4), Arg4);
    goto loc_0024CEC4;
loc_0024CEBC:
    result = PopPepTriggerComponentActivatingActivity(Arg1, Arg2, (uint32_t)(Arg4), Arg4);
loc_0024CEC4:
    local_rsp = (local_rsp) + (32);
    return result;
loc_0024CEDA:
    if ((((uint32_t)(Arg1)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48)))))) == 0) goto loc_0024CE02;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48))))) & (2)) != 0) {
    }
    goto loc_0024CE02;
loc_0024CF00:
    if ((((uint32_t)(Arg1)) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x68)))))) == 0) goto loc_0024CE0E;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x68))))) & (2)) != 0) {
    }
    goto loc_0024CE0E;
loc_0024CF26:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x70))))) & ((uint32_t)(Arg1))) == 0) goto loc_0024CE1A;
loc_0024CF34:
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x70))))) & (2)) != 0) {
    }
    goto loc_0024CE1A;
loc_0024CF49:
    if (((uint32_t)(local_r10)) != 2) goto loc_0024CE1A;
    if ((*(uint8_t *)(arg1 + 0x7D)) == 0) goto loc_0024CF6C;
    result = (*(uint64_t *)(arg1 + 0x70)) * ((int32_t)(Arg3));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_p10 * 1 + 0x28))) != 0) goto loc_0024D056;
loc_0024CF6C:
    Arg2 = ((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x70)))) * ((int32_t)(Arg3));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + arg2 * 4 + 0x2C))) != 0) goto loc_0024CFCF;
loc_0024CF78:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + arg2 * 4 + 0x30))) != 0) goto loc_0024CFEE;
loc_0024CF80:
    if ((uint32_t)((uint32_t)(*(uint32_t *)(v_stack_p10 + arg2 * 4 + 0x34))) != 0) goto loc_0024D010;
loc_0024CF8C:
    if ((*(uint8_t *)(arg1 + 0x7D)) == 0) goto loc_0024CE1A;
    result = (result) * ((int32_t)(Arg3));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_p10 * 1 + 0x38))) != 0) goto loc_0024D033;
loc_0024CFA9:
    result = (result) * ((int32_t)(Arg3));
    if ((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_p10 * 1 + 0x3C))) == 0) goto loc_0024CE1A;
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x70))))) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_p10 * 1 + 0x3C))))) == 0) goto loc_0024CE1A;
    goto loc_0024CF34;
loc_0024CFCF:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_p10 * 1 + 0x3C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x40)))))) == 0) goto loc_0024CF78;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x40))))) & (2)) != 0) {
    }
    goto loc_0024CF78;
loc_0024CFEE:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_p10 * 1 + 0x3C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x48)))))) == 0) goto loc_0024CF80;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x48))))) & (2)) != 0) {
    }
    goto loc_0024CF80;
loc_0024D010:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_p10 * 1 + 0x3C)))) & ((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x50)))))) == 0) goto loc_0024CF8C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x50))))) & (2)) != 0) {
    }
    goto loc_0024CF8C;
loc_0024D033:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x68))))) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_p10 * 1 + 0x3C))))) == 0) goto loc_0024CFA9;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x68))))) & (2)) != 0) {
    }
    goto loc_0024CFA9;
loc_0024D056:
    if ((((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48))))) & ((uint32_t)((uint32_t)(*(uint32_t *)(result + v_stack_p10 * 1 + 0x3C))))) == 0) goto loc_0024CF6C;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48))))) & (2)) != 0) {
    }
    goto loc_0024CF6C;
loc_0024D079:
    if ((*(uint64_t *)(arg1 + 0x48)) != (v_rip + 2190608)) goto loc_0024D0A6;
    result = PopPepTriggerComponentIdleStateChangeActivity(Arg1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48))), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x48))), Arg4);
    goto loc_0024CEC4;
loc_0024D092:
    goto loc_0024CE34;
loc_0024D09C:
    goto loc_0024CE7D;
loc_0024D0A6:
    result = guard_dispatch_icall(1, (uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48))), (uint32_t)(*(uint32_t *)(*(uint64_t *)(v_stack_p18 + 0x48))), Arg4);
    goto loc_0024CEC4;
loc_0024D0B0:
    result = PopFxBugCheck((uint32_t)(0x666ULL), local_r10, (int32_t)(Arg3), (int32_t)((uint32_t)((uint32_t)(*(uint32_t *)(*(uint64_t *)(arg1 + 0x48))))));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x48 + rbx*8` | `64` | `R` |
| `Arg1` | `+ 0x68` | `64` | `R` |
| `Arg1` | `+ 0x70` | `64` | `R` |
| `Arg1` | `+ 0x78` | `32` | `R/W` |
| `Arg1` | `+ 0x7D` | `8` | `R` |
| `Arg2` | `+ 0x38` | `64` | `R` |
| `Arg2` | `+ 0x40` | `64` | `R` |
| `Arg2` | `+ 0x48` | `64` | `R` |
| `Arg2` | `+ 0x50` | `64` | `R` |
| `Arg2` | `+ 0x68` | `32` | `R/W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0024CDB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.
