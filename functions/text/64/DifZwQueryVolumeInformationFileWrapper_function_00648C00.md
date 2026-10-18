# DifZwQueryVolumeInformationFileWrapper

- RVA: `0x00648C00`–`0x00648D92` (길이 `402` bytes)
- VA: `0x0000000140648C00`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000D2BBC`
- 디코드: `116`개 명령, `402/402` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00648C40` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00648C66` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00648CA8` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00648CCE` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00648CE7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00648D00` → [ZwQueryVolumeInformationFile](../6A/ZwQueryVolumeInformationFile_function_006AD9F0.md) (function, `0x006AD9F0`)
- `0x00648D2C` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00648D52` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00648D6B` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00648C76` → RVA `0x00F048B8` (`.data`; read)
- `0x00648C95` → RVA `0x00F04980` (`.data`; read)
- `0x00648CA1` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00648C00  48 8B C4                        mov rax, rsp
00648C03  48 89 58 10                     mov qword ptr [rax + 0x10], rbx
00648C07  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00648C0B  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
00648C0F  48 89 48 08                     mov qword ptr [rax + 8], rcx
00648C13  55                              push rbp
00648C14  41 54                           push r12
00648C16  41 55                           push r13
00648C18  41 56                           push r14
00648C1A  41 57                           push r15
00648C1C  48 8B EC                        mov rbp, rsp
00648C1F  48 83 EC 60                     sub rsp, 0x60
00648C23  0F 57 C0                        xorps xmm0, xmm0
00648C26  B9 21 00 00 00                  mov ecx, 0x21
00648C2B  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
00648C2F  45 8B F9                        mov r15d, r9d
00648C32  4D 8B E0                        mov r12, r8
00648C35  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
00648C39  4C 8B EA                        mov r13, rdx
00648C3C  0F 11 45 F0                     movups xmmword ptr [rbp - 0x10], xmm0
00648C40  E8 EF CD E4 FF                  call 0x140495a34
00648C45  48 8B F0                        mov rsi, rax
00648C48  48 85 C0                        test rax, rax
00648C4B  0F 84 9B 00 00 00               je 0x140648cec
00648C51  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00648C54  A8 18                           test al, 0x18
00648C56  74 0A                           je 0x140648c62
00648C58  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
00648C5C  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
00648C60  EB 0D                           jmp 0x140648c6f
00648C62  A8 04                           test al, 4
00648C64  74 09                           je 0x140648c6f
00648C66  E8 9D AF E8 FF                  call 0x1404d3c08
00648C6B  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
00648C6F  48 8B 45 30                     mov rax, qword ptr [rbp + 0x30]
00648C73  45 32 F6                        xor r14b, r14b
00648C76  44 38 35 3B BC 8B 00            cmp byte ptr [rip + 0x8bbc3b], r14b
00648C7D  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
00648C81  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00648C84  89 45 D8                        mov dword ptr [rbp - 0x28], eax
00648C87  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
00648C8B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
00648C8F  44 89 7D DC                     mov dword ptr [rbp - 0x24], r15d
00648C93  75 0C                           jne 0x140648ca1
00648C95  F7 05 E1 BC 8B 00 00 08 00 00   test dword ptr [rip + 0x8bbce1], 0x800
00648C9F  74 13                           je 0x140648cb4
00648CA1  48 8D 0D D8 B1 8B 00            lea rcx, [rip + 0x8bb1d8]
00648CA8  E8 73 D9 BC FF                  call 0x140216620
00648CAD  44 8A F0                        mov r14b, al
00648CB0  84 C0                           test al, al
00648CB2  74 38                           je 0x140648cec
00648CB4  48 8D 7E 20                     lea rdi, [rsi + 0x20]
00648CB8  48 8B 1F                        mov rbx, qword ptr [rdi]
00648CBB  EB 19                           jmp 0x140648cd6
00648CBD  48 8D 43 F0                     lea rax, [rbx - 0x10]
00648CC1  48 85 C0                        test rax, rax
00648CC4  74 0D                           je 0x140648cd3
00648CC6  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00648CCA  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00648CCE  E8 FD 1D 07 00                  call 0x1406baad0
00648CD3  48 8B 1B                        mov rbx, qword ptr [rbx]
00648CD6  48 3B DF                        cmp rbx, rdi
00648CD9  75 E2                           jne 0x140648cbd
00648CDB  45 84 F6                        test r14b, r14b
00648CDE  74 0C                           je 0x140648cec
00648CE0  48 8D 0D 99 B1 8B 00            lea rcx, [rip + 0x8bb199]
00648CE7  E8 94 11 D0 FF                  call 0x140349e80
00648CEC  8B 45 50                        mov eax, dword ptr [rbp + 0x50]
00648CEF  45 8B CF                        mov r9d, r15d
00648CF2  48 8B 4D 30                     mov rcx, qword ptr [rbp + 0x30]
00648CF6  4D 8B C4                        mov r8, r12
00648CF9  49 8B D5                        mov rdx, r13
00648CFC  89 44 24 20                     mov dword ptr [rsp + 0x20], eax
00648D00  E8 EB 4C 06 00                  call 0x1406ad9f0
00648D05  89 45 F8                        mov dword ptr [rbp - 8], eax
00648D08  48 85 F6                        test rsi, rsi
00648D0B  74 63                           je 0x140648d70
00648D0D  40 32 FF                        xor dil, dil
00648D10  40 38 3D A1 BB 8B 00            cmp byte ptr [rip + 0x8bbba1], dil
00648D17  75 0C                           jne 0x140648d25
00648D19  F7 05 5D BC 8B 00 00 08 00 00   test dword ptr [rip + 0x8bbc5d], 0x800
00648D23  74 13                           je 0x140648d38
00648D25  48 8D 0D 54 B1 8B 00            lea rcx, [rip + 0x8bb154]
00648D2C  E8 EF D8 BC FF                  call 0x140216620
00648D31  40 8A F8                        mov dil, al
00648D34  84 C0                           test al, al
00648D36  74 38                           je 0x140648d70
00648D38  48 83 C6 30                     add rsi, 0x30
00648D3C  48 8B 1E                        mov rbx, qword ptr [rsi]
00648D3F  EB 19                           jmp 0x140648d5a
00648D41  48 8D 43 F0                     lea rax, [rbx - 0x10]
00648D45  48 85 C0                        test rax, rax
00648D48  74 0D                           je 0x140648d57
00648D4A  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00648D4E  48 8D 4D D0                     lea rcx, [rbp - 0x30]
00648D52  E8 79 1D 07 00                  call 0x1406baad0
00648D57  48 8B 1B                        mov rbx, qword ptr [rbx]
00648D5A  48 3B DE                        cmp rbx, rsi
00648D5D  75 E2                           jne 0x140648d41
00648D5F  40 84 FF                        test dil, dil
00648D62  74 0C                           je 0x140648d70
00648D64  48 8D 0D 15 B1 8B 00            lea rcx, [rip + 0x8bb115]
00648D6B  E8 10 11 D0 FF                  call 0x140349e80
00648D70  8B 45 F8                        mov eax, dword ptr [rbp - 8]
00648D73  4C 8D 5C 24 60                  lea r11, [rsp + 0x60]
00648D78  49 8B 5B 38                     mov rbx, qword ptr [r11 + 0x38]
00648D7C  49 8B 73 40                     mov rsi, qword ptr [r11 + 0x40]
00648D80  49 8B 7B 48                     mov rdi, qword ptr [r11 + 0x48]
00648D84  49 8B E3                        mov rsp, r11
00648D87  41 5F                           pop r15
00648D89  41 5E                           pop r14
00648D8B  41 5D                           pop r13
00648D8D  41 5C                           pop r12
00648D8F  5D                              pop rbp
00648D90  C3                              ret
00648D91  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifZwQueryVolumeInformationFileWrapper(__int64 a1, __int64 a2, __int64 a3, int a4, unsigned int a5)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned int v_stack_m30;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned int v_stack_m4C;
    unsigned int v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 16) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    *(unsigned __int64 *)(v_rsp + 8) = a1;
    v_rsp = (v_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(33, a2, a3, a4);
    if (result == 0) goto loc_00648CEC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00648C62;
    v_stack_m58 = v_stack_p0;
    goto loc_00648C6F;
loc_00648C62:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = (unsigned int)((unsigned int)(a5));
    v_stack_m40 = a2;
    v_stack_m48 = a3;
    v_stack_m4C = (unsigned int)((unsigned int)(a4));
    if ((*(unsigned __int8 *)(v_rip + 9157691)) != 0) goto loc_00648CA1;
    if (((*(unsigned int *)(v_rip + 9157857)) & (0x800ULL)) == 0) goto loc_00648CB4;
loc_00648CA1:
    result = ExAcquireRundownProtection(v_rip + 9155032, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00648CEC;
loc_00648CB4:
    goto loc_00648CD6;
loc_00648CBD:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00648CD6:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00648CBD;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9154969;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m68 = (unsigned int)((unsigned int)(a5));
    result = ZwQueryVolumeInformationFile(v_stack_p8, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    v_stack_m30 = (unsigned int)(result);
    if (result == 0) goto loc_00648D70;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9157537)) != 0) goto loc_00648D25;
    if (((*(unsigned int *)(v_rip + 9157725)) & (0x800ULL)) == 0) goto loc_00648D38;
loc_00648D25:
    result = ExAcquireRundownProtection(v_rip + 9154900, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    if ((unsigned __int8)(result) == 0) goto loc_00648D70;
loc_00648D38:
    v_rsi = (result) + (48);
    goto loc_00648D5A;
loc_00648D41:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
loc_00648D5A:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00648D41;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9154837;
        result = ExReleaseRundownProtection(a1, a2, a3, (unsigned int)((unsigned int)((unsigned int)(a4))));
    }
    return (unsigned int)(v_stack_m30);
}
```

## 5. (Beta) C Style

```c
int64_t DifZwQueryVolumeInformationFileWrapper(int64_t Arg1, int64_t Arg2, int64_t Arg3, int32_t Arg4, uint32_t Arg5)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint32_t v_stack_m30;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint32_t v_stack_m4C;
    uint32_t v_stack_m50;
    uint64_t v_stack_m58;
    uint32_t v_stack_m68;
    uint64_t v_stack_p0;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x10) = local_rbx;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    *(uint64_t *)(local_rsp + 0x8) = Arg1;
    local_rsp = (local_rsp) - (96);
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    v_stack_m38 = v_xmm0;
    result = DifGetAPIThunkContextById(33, Arg2, Arg3, Arg4);
    if (result == 0) goto loc_00648CEC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00648C62;
    v_stack_m58 = v_stack_p0;
    goto loc_00648C6F;
loc_00648C62:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, Arg4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m38 = v_stack_p8;
    v_stack_m50 = (uint32_t)((uint32_t)(Arg5));
    v_stack_m40 = Arg2;
    v_stack_m48 = Arg3;
    v_stack_m4C = (uint32_t)((uint32_t)(Arg4));
    if ((*(uint8_t *)(v_rip + 0x8BBC3B)) != 0) goto loc_00648CA1;
    if (((*(uint32_t *)(v_rip + 0x8BBCE1)) & (0x800ULL)) == 0) goto loc_00648CB4;
loc_00648CA1:
    result = ExAcquireRundownProtection(v_rip + 9155032, Arg2, Arg3, Arg4);
    if ((uint8_t)(result) == 0) goto loc_00648CEC;
loc_00648CB4:
    goto loc_00648CD6;
loc_00648CBD:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, Arg4);
    }
loc_00648CD6:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00648CBD;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9154969;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, Arg4);
    }
    v_stack_m68 = (uint32_t)((uint32_t)(Arg5));
    result = ZwQueryVolumeInformationFile(v_stack_p8, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    v_stack_m30 = (uint32_t)(result);
    if (result == 0) goto loc_00648D70;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8BBBA1)) != 0) goto loc_00648D25;
    if (((*(uint32_t *)(v_rip + 0x8BBC5D)) & (0x800ULL)) == 0) goto loc_00648D38;
loc_00648D25:
    result = ExAcquireRundownProtection(v_rip + 9154900, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    if ((uint8_t)(result) == 0) goto loc_00648D70;
loc_00648D38:
    local_rsi = (result) + (48);
    goto loc_00648D5A;
loc_00648D41:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
loc_00648D5A:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00648D41;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9154837;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, (uint32_t)((uint32_t)((uint32_t)(Arg4))));
    }
    return (uint32_t)(v_stack_m30);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00648C00&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00648C00[BB_00648C00]
  bb_00648C51[BB_00648C51]
  bb_00648C58[BB_00648C58]
  bb_00648C62[BB_00648C62]
  bb_00648C66[BB_00648C66]
  bb_00648C6F[BB_00648C6F]
  bb_00648C95[BB_00648C95]
  bb_00648CA1[BB_00648CA1]
  bb_00648CB4[BB_00648CB4]
  bb_00648CBD[BB_00648CBD]
  bb_00648CC6[BB_00648CC6]
  bb_00648CD3[BB_00648CD3]
  bb_00648CD6[BB_00648CD6]
  bb_00648CDB[BB_00648CDB]
  bb_00648CE0[BB_00648CE0]
  bb_00648CEC[BB_00648CEC]
  bb_00648D0D[BB_00648D0D]
  bb_00648D19[BB_00648D19]
  bb_00648D25[BB_00648D25]
  bb_00648D38[BB_00648D38]
  bb_00648D41[BB_00648D41]
  bb_00648D4A[BB_00648D4A]
  bb_00648D57[BB_00648D57]
  bb_00648D5A[BB_00648D5A]
  bb_00648D5F[BB_00648D5F]
  bb_00648D64[BB_00648D64]
  bb_00648D70[BB_00648D70]
  bb_00648D91[BB_00648D91]
  bb_00648C00 -->|branch| bb_00648CEC
  bb_00648C00 -->|fallthrough| bb_00648C51
  bb_00648C51 -->|branch| bb_00648C62
  bb_00648C51 -->|fallthrough| bb_00648C58
  bb_00648C58 -->|branch| bb_00648C6F
  bb_00648C62 -->|branch| bb_00648C6F
  bb_00648C62 -->|fallthrough| bb_00648C66
  bb_00648C66 -->|flow| bb_00648C6F
  bb_00648C6F -->|branch| bb_00648CA1
  bb_00648C6F -->|fallthrough| bb_00648C95
  bb_00648C95 -->|branch| bb_00648CB4
  bb_00648C95 -->|fallthrough| bb_00648CA1
  bb_00648CA1 -->|branch| bb_00648CEC
  bb_00648CA1 -->|fallthrough| bb_00648CB4
  bb_00648CB4 -->|branch| bb_00648CD6
  bb_00648CBD -->|branch| bb_00648CD3
  bb_00648CBD -->|fallthrough| bb_00648CC6
  bb_00648CC6 -->|flow| bb_00648CD3
  bb_00648CD3 -->|flow| bb_00648CD6
  bb_00648CD6 -->|branch| bb_00648CBD
  bb_00648CD6 -->|fallthrough| bb_00648CDB
  bb_00648CDB -->|branch| bb_00648CEC
  bb_00648CDB -->|fallthrough| bb_00648CE0
  bb_00648CE0 -->|flow| bb_00648CEC
  bb_00648CEC -->|branch| bb_00648D70
  bb_00648CEC -->|fallthrough| bb_00648D0D
  bb_00648D0D -->|branch| bb_00648D25
  bb_00648D0D -->|fallthrough| bb_00648D19
  bb_00648D19 -->|branch| bb_00648D38
  bb_00648D19 -->|fallthrough| bb_00648D25
  bb_00648D25 -->|branch| bb_00648D70
  bb_00648D25 -->|fallthrough| bb_00648D38
  bb_00648D38 -->|branch| bb_00648D5A
  bb_00648D41 -->|branch| bb_00648D57
  bb_00648D41 -->|fallthrough| bb_00648D4A
  bb_00648D4A -->|flow| bb_00648D57
  bb_00648D57 -->|flow| bb_00648D5A
  bb_00648D5A -->|branch| bb_00648D41
  bb_00648D5A -->|fallthrough| bb_00648D5F
  bb_00648D5F -->|branch| bb_00648D70
  bb_00648D5F -->|fallthrough| bb_00648D64
  bb_00648D64 -->|flow| bb_00648D70
```
