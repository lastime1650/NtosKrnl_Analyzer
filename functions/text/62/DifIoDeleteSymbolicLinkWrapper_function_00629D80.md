# DifIoDeleteSymbolicLinkWrapper

- RVA: `0x00629D80`–`0x00629EDF` (길이 `351` bytes)
- VA: `0x0000000140629D80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `94`개 명령, `351/351` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x00629DAF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x00629DD7` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x00629E05` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00629E2C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00629E45` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x00629E4D` → [IoDeleteSymbolicLink](../../page/AA/IoDeleteSymbolicLink_function_00AA7510.md) (function, `0x00AA7510`)
- `0x00629E7A` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x00629EA1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x00629EBA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x00629DE9` → RVA `0x00F048B8` (`.data`; read)
- `0x00629DF2` → RVA `0x00F04980` (`.data`; read)
- `0x00629DFE` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x00629E4D` → [IoDeleteSymbolicLink](../../page/AA/IoDeleteSymbolicLink_function_00AA7510.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00629D80  4C 8B DC                        mov r11, rsp
00629D83  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
00629D87  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
00629D8B  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
00629D8F  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
00629D93  41 56                           push r14
00629D95  48 83 EC 40                     sub rsp, 0x40
00629D99  33 C0                           xor eax, eax
00629D9B  0F 57 C0                        xorps xmm0, xmm0
00629D9E  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
00629DA3  48 8B E9                        mov rbp, rcx
00629DA6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
00629DAA  B9 59 01 00 00                  mov ecx, 0x159
00629DAF  E8 80 BC E6 FF                  call 0x140495a34
00629DB4  48 8B F0                        mov rsi, rax
00629DB7  48 85 C0                        test rax, rax
00629DBA  0F 84 8A 00 00 00               je 0x140629e4a
00629DC0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
00629DC3  A8 18                           test al, 0x18
00629DC5  74 0C                           je 0x140629dd3
00629DC7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
00629DCC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
00629DD1  EB 0E                           jmp 0x140629de1
00629DD3  A8 04                           test al, 4
00629DD5  74 0A                           je 0x140629de1
00629DD7  E8 2C 9E EA FF                  call 0x1404d3c08
00629DDC  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
00629DE1  40 32 FF                        xor dil, dil
00629DE4  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
00629DE9  40 38 3D C8 AA 8D 00            cmp byte ptr [rip + 0x8daac8], dil
00629DF0  75 0C                           jne 0x140629dfe
00629DF2  F7 05 84 AB 8D 00 00 08 00 00   test dword ptr [rip + 0x8dab84], 0x800
00629DFC  74 13                           je 0x140629e11
00629DFE  48 8D 0D 7B A0 8D 00            lea rcx, [rip + 0x8da07b]
00629E05  E8 16 C8 BE FF                  call 0x140216620
00629E0A  40 8A F8                        mov dil, al
00629E0D  84 C0                           test al, al
00629E0F  74 39                           je 0x140629e4a
00629E11  4C 8D 76 20                     lea r14, [rsi + 0x20]
00629E15  49 8B 1E                        mov rbx, qword ptr [r14]
00629E18  EB 1A                           jmp 0x140629e34
00629E1A  48 8D 43 F0                     lea rax, [rbx - 0x10]
00629E1E  48 85 C0                        test rax, rax
00629E21  74 0E                           je 0x140629e31
00629E23  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00629E27  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00629E2C  E8 9F 0C 09 00                  call 0x1406baad0
00629E31  48 8B 1B                        mov rbx, qword ptr [rbx]
00629E34  49 3B DE                        cmp rbx, r14
00629E37  75 E1                           jne 0x140629e1a
00629E39  40 84 FF                        test dil, dil
00629E3C  74 0C                           je 0x140629e4a
00629E3E  48 8D 0D 3B A0 8D 00            lea rcx, [rip + 0x8da03b]
00629E45  E8 36 00 D2 FF                  call 0x140349e80
00629E4A  48 8B CD                        mov rcx, rbp
00629E4D  E8 BE D6 47 00                  call 0x140aa7510
00629E52  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
00629E56  48 85 F6                        test rsi, rsi
00629E59  74 64                           je 0x140629ebf
00629E5B  40 32 FF                        xor dil, dil
00629E5E  40 38 3D 53 AA 8D 00            cmp byte ptr [rip + 0x8daa53], dil
00629E65  75 0C                           jne 0x140629e73
00629E67  F7 05 0F AB 8D 00 00 08 00 00   test dword ptr [rip + 0x8dab0f], 0x800
00629E71  74 13                           je 0x140629e86
00629E73  48 8D 0D 06 A0 8D 00            lea rcx, [rip + 0x8da006]
00629E7A  E8 A1 C7 BE FF                  call 0x140216620
00629E7F  40 8A F8                        mov dil, al
00629E82  84 C0                           test al, al
00629E84  74 39                           je 0x140629ebf
00629E86  48 83 C6 30                     add rsi, 0x30
00629E8A  48 8B 1E                        mov rbx, qword ptr [rsi]
00629E8D  EB 1A                           jmp 0x140629ea9
00629E8F  48 8D 43 F0                     lea rax, [rbx - 0x10]
00629E93  48 85 C0                        test rax, rax
00629E96  74 0E                           je 0x140629ea6
00629E98  48 8B 40 08                     mov rax, qword ptr [rax + 8]
00629E9C  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
00629EA1  E8 2A 0C 09 00                  call 0x1406baad0
00629EA6  48 8B 1B                        mov rbx, qword ptr [rbx]
00629EA9  48 3B DE                        cmp rbx, rsi
00629EAC  75 E1                           jne 0x140629e8f
00629EAE  40 84 FF                        test dil, dil
00629EB1  74 0C                           je 0x140629ebf
00629EB3  48 8D 0D C6 9F 8D 00            lea rcx, [rip + 0x8d9fc6]
00629EBA  E8 C1 FF D1 FF                  call 0x140349e80
00629EBF  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
00629EC3  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
00629EC8  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
00629ECD  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
00629ED2  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
00629ED7  48 83 C4 40                     add rsp, 0x40
00629EDB  41 5E                           pop r14
00629EDD  C3                              ret
00629EDE  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoDeleteSymbolicLinkWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(unsigned __int64 *)(v_rsp - 24) = 0;
    result = DifGetAPIThunkContextById(345, a2, a3, a4);
    if (result == 0) goto loc_00629E4A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_00629DD3;
    v_stack_m28 = v_stack_p0;
    goto loc_00629DE1;
loc_00629DD3:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9284296)) != 0) goto loc_00629DFE;
    if (((*(unsigned int *)(v_rip + 9284484)) & (0x800ULL)) == 0) goto loc_00629E11;
loc_00629DFE:
    result = ExAcquireRundownProtection(v_rip + 9281659, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00629E4A;
loc_00629E11:
    goto loc_00629E34;
loc_00629E1A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00629E34:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_00629E1A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9281595;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = IoDeleteSymbolicLink(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_00629EBF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9284179)) != 0) goto loc_00629E73;
    if (((*(unsigned int *)(v_rip + 9284367)) & (0x800ULL)) == 0) goto loc_00629E86;
loc_00629E73:
    result = ExAcquireRundownProtection(v_rip + 9281542, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_00629EBF;
loc_00629E86:
    v_rsi = (result) + (48);
    goto loc_00629EA9;
loc_00629E8F:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_00629EA9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_00629E8F;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9281478;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifIoDeleteSymbolicLinkWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint32_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m28;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (64);
    result = 0;
    v_stack_m28 = v_xmm0;
    *(uint64_t *)(local_rsp - 0x18) = 0;
    result = DifGetAPIThunkContextById(345, a2, a3, a4);
    if (result == 0) goto loc_00629E4A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_00629DD3;
    v_stack_m28 = v_stack_p0;
    goto loc_00629DE1;
loc_00629DD3:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8DAAC8)) != 0) goto loc_00629DFE;
    if (((*(uint32_t *)(v_rip + 0x8DAB84)) & (0x800ULL)) == 0) goto loc_00629E11;
loc_00629DFE:
    result = ExAcquireRundownProtection(v_rip + 9281659, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00629E4A;
loc_00629E11:
    goto loc_00629E34;
loc_00629E1A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00629E34:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_00629E1A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9281595;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = IoDeleteSymbolicLink(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_00629EBF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8DAA53)) != 0) goto loc_00629E73;
    if (((*(uint32_t *)(v_rip + 0x8DAB0F)) & (0x800ULL)) == 0) goto loc_00629E86;
loc_00629E73:
    result = ExAcquireRundownProtection(v_rip + 9281542, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_00629EBF;
loc_00629E86:
    local_rsi = (result) + (48);
    goto loc_00629EA9;
loc_00629E8F:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_00629EA9:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_00629E8F;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9281478;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00629D80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00629D80[BB_00629D80]
  bb_00629DC0[BB_00629DC0]
  bb_00629DC7[BB_00629DC7]
  bb_00629DD3[BB_00629DD3]
  bb_00629DD7[BB_00629DD7]
  bb_00629DE1[BB_00629DE1]
  bb_00629DF2[BB_00629DF2]
  bb_00629DFE[BB_00629DFE]
  bb_00629E11[BB_00629E11]
  bb_00629E1A[BB_00629E1A]
  bb_00629E23[BB_00629E23]
  bb_00629E31[BB_00629E31]
  bb_00629E34[BB_00629E34]
  bb_00629E39[BB_00629E39]
  bb_00629E3E[BB_00629E3E]
  bb_00629E4A[BB_00629E4A]
  bb_00629E5B[BB_00629E5B]
  bb_00629E67[BB_00629E67]
  bb_00629E73[BB_00629E73]
  bb_00629E86[BB_00629E86]
  bb_00629E8F[BB_00629E8F]
  bb_00629E98[BB_00629E98]
  bb_00629EA6[BB_00629EA6]
  bb_00629EA9[BB_00629EA9]
  bb_00629EAE[BB_00629EAE]
  bb_00629EB3[BB_00629EB3]
  bb_00629EBF[BB_00629EBF]
  bb_00629EDE[BB_00629EDE]
  bb_00629D80 -->|branch| bb_00629E4A
  bb_00629D80 -->|fallthrough| bb_00629DC0
  bb_00629DC0 -->|branch| bb_00629DD3
  bb_00629DC0 -->|fallthrough| bb_00629DC7
  bb_00629DC7 -->|branch| bb_00629DE1
  bb_00629DD3 -->|branch| bb_00629DE1
  bb_00629DD3 -->|fallthrough| bb_00629DD7
  bb_00629DD7 -->|flow| bb_00629DE1
  bb_00629DE1 -->|branch| bb_00629DFE
  bb_00629DE1 -->|fallthrough| bb_00629DF2
  bb_00629DF2 -->|branch| bb_00629E11
  bb_00629DF2 -->|fallthrough| bb_00629DFE
  bb_00629DFE -->|branch| bb_00629E4A
  bb_00629DFE -->|fallthrough| bb_00629E11
  bb_00629E11 -->|branch| bb_00629E34
  bb_00629E1A -->|branch| bb_00629E31
  bb_00629E1A -->|fallthrough| bb_00629E23
  bb_00629E23 -->|flow| bb_00629E31
  bb_00629E31 -->|flow| bb_00629E34
  bb_00629E34 -->|branch| bb_00629E1A
  bb_00629E34 -->|fallthrough| bb_00629E39
  bb_00629E39 -->|branch| bb_00629E4A
  bb_00629E39 -->|fallthrough| bb_00629E3E
  bb_00629E3E -->|flow| bb_00629E4A
  bb_00629E4A -->|branch| bb_00629EBF
  bb_00629E4A -->|fallthrough| bb_00629E5B
  bb_00629E5B -->|branch| bb_00629E73
  bb_00629E5B -->|fallthrough| bb_00629E67
  bb_00629E67 -->|branch| bb_00629E86
  bb_00629E67 -->|fallthrough| bb_00629E73
  bb_00629E73 -->|branch| bb_00629EBF
  bb_00629E73 -->|fallthrough| bb_00629E86
  bb_00629E86 -->|branch| bb_00629EA9
  bb_00629E8F -->|branch| bb_00629EA6
  bb_00629E8F -->|fallthrough| bb_00629E98
  bb_00629E98 -->|flow| bb_00629EA6
  bb_00629EA6 -->|flow| bb_00629EA9
  bb_00629EA9 -->|branch| bb_00629E8F
  bb_00629EA9 -->|fallthrough| bb_00629EAE
  bb_00629EAE -->|branch| bb_00629EBF
  bb_00629EAE -->|fallthrough| bb_00629EB3
  bb_00629EB3 -->|flow| bb_00629EBF
```
