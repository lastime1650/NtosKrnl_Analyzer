# DifRtlUpcaseUnicodeStringWrapper

- RVA: `0x0063CED0`–`0x0063D047` (길이 `375` bytes)
- VA: `0x000000014063CED0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000A9A64`
- 디코드: `108`개 명령, `375/375` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **9**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0063CF0E` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063CF34` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063CF68` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063CF8E` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063CFA7` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063CFB5` → [RtlUpcaseUnicodeString](../../page/96/RtlUpcaseUnicodeString_function_00960780.md) (function, `0x00960780`)
- `0x0063CFE1` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063D007` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063D020` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063CF44` → RVA `0x00F048B8` (`.data`; read)
- `0x0063CF55` → RVA `0x00F04980` (`.data`; read)
- `0x0063CF61` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063CFB5` → [RtlUpcaseUnicodeString](../../page/96/RtlUpcaseUnicodeString_function_00960780.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063CED0  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
0063CED5  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
0063CEDA  48 89 7C 24 18                  mov qword ptr [rsp + 0x18], rdi
0063CEDF  55                              push rbp
0063CEE0  41 54                           push r12
0063CEE2  41 55                           push r13
0063CEE4  41 56                           push r14
0063CEE6  41 57                           push r15
0063CEE8  48 8B EC                        mov rbp, rsp
0063CEEB  48 83 EC 50                     sub rsp, 0x50
0063CEEF  0F 57 C0                        xorps xmm0, xmm0
0063CEF2  33 C0                           xor eax, eax
0063CEF4  4C 8B E9                        mov r13, rcx
0063CEF7  48 89 45 F0                     mov qword ptr [rbp - 0x10], rax
0063CEFB  B9 99 00 00 00                  mov ecx, 0x99
0063CF00  45 8A F8                        mov r15b, r8b
0063CF03  0F 11 45 D0                     movups xmmword ptr [rbp - 0x30], xmm0
0063CF07  4C 8B E2                        mov r12, rdx
0063CF0A  0F 11 45 E0                     movups xmmword ptr [rbp - 0x20], xmm0
0063CF0E  E8 21 8B E5 FF                  call 0x140495a34
0063CF13  48 8B F0                        mov rsi, rax
0063CF16  48 85 C0                        test rax, rax
0063CF19  0F 84 8D 00 00 00               je 0x14063cfac
0063CF1F  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063CF22  A8 18                           test al, 0x18
0063CF24  74 0A                           je 0x14063cf30
0063CF26  48 8B 4D 28                     mov rcx, qword ptr [rbp + 0x28]
0063CF2A  48 89 4D D0                     mov qword ptr [rbp - 0x30], rcx
0063CF2E  EB 0D                           jmp 0x14063cf3d
0063CF30  A8 04                           test al, 4
0063CF32  74 09                           je 0x14063cf3d
0063CF34  E8 CF 6C E9 FF                  call 0x1404d3c08
0063CF39  48 89 45 D0                     mov qword ptr [rbp - 0x30], rax
0063CF3D  45 32 F6                        xor r14b, r14b
0063CF40  4C 89 6D E8                     mov qword ptr [rbp - 0x18], r13
0063CF44  44 38 35 6D 79 8C 00            cmp byte ptr [rip + 0x8c796d], r14b
0063CF4B  4C 89 65 E0                     mov qword ptr [rbp - 0x20], r12
0063CF4F  44 88 7D D8                     mov byte ptr [rbp - 0x28], r15b
0063CF53  75 0C                           jne 0x14063cf61
0063CF55  F7 05 21 7A 8C 00 00 08 00 00   test dword ptr [rip + 0x8c7a21], 0x800
0063CF5F  74 13                           je 0x14063cf74
0063CF61  48 8D 0D 18 6F 8C 00            lea rcx, [rip + 0x8c6f18]
0063CF68  E8 B3 96 BD FF                  call 0x140216620
0063CF6D  44 8A F0                        mov r14b, al
0063CF70  84 C0                           test al, al
0063CF72  74 38                           je 0x14063cfac
0063CF74  48 8D 7E 20                     lea rdi, [rsi + 0x20]
0063CF78  48 8B 1F                        mov rbx, qword ptr [rdi]
0063CF7B  EB 19                           jmp 0x14063cf96
0063CF7D  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063CF81  48 85 C0                        test rax, rax
0063CF84  74 0D                           je 0x14063cf93
0063CF86  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063CF8A  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063CF8E  E8 3D DB 07 00                  call 0x1406baad0
0063CF93  48 8B 1B                        mov rbx, qword ptr [rbx]
0063CF96  48 3B DF                        cmp rbx, rdi
0063CF99  75 E2                           jne 0x14063cf7d
0063CF9B  45 84 F6                        test r14b, r14b
0063CF9E  74 0C                           je 0x14063cfac
0063CFA0  48 8D 0D D9 6E 8C 00            lea rcx, [rip + 0x8c6ed9]
0063CFA7  E8 D4 CE D0 FF                  call 0x140349e80
0063CFAC  45 8A C7                        mov r8b, r15b
0063CFAF  49 8B D4                        mov rdx, r12
0063CFB2  49 8B CD                        mov rcx, r13
0063CFB5  E8 C6 37 32 00                  call 0x140960780
0063CFBA  89 45 F0                        mov dword ptr [rbp - 0x10], eax
0063CFBD  48 85 F6                        test rsi, rsi
0063CFC0  74 63                           je 0x14063d025
0063CFC2  40 32 FF                        xor dil, dil
0063CFC5  40 38 3D EC 78 8C 00            cmp byte ptr [rip + 0x8c78ec], dil
0063CFCC  75 0C                           jne 0x14063cfda
0063CFCE  F7 05 A8 79 8C 00 00 08 00 00   test dword ptr [rip + 0x8c79a8], 0x800
0063CFD8  74 13                           je 0x14063cfed
0063CFDA  48 8D 0D 9F 6E 8C 00            lea rcx, [rip + 0x8c6e9f]
0063CFE1  E8 3A 96 BD FF                  call 0x140216620
0063CFE6  40 8A F8                        mov dil, al
0063CFE9  84 C0                           test al, al
0063CFEB  74 38                           je 0x14063d025
0063CFED  48 83 C6 30                     add rsi, 0x30
0063CFF1  48 8B 1E                        mov rbx, qword ptr [rsi]
0063CFF4  EB 19                           jmp 0x14063d00f
0063CFF6  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063CFFA  48 85 C0                        test rax, rax
0063CFFD  74 0D                           je 0x14063d00c
0063CFFF  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063D003  48 8D 4D D0                     lea rcx, [rbp - 0x30]
0063D007  E8 C4 DA 07 00                  call 0x1406baad0
0063D00C  48 8B 1B                        mov rbx, qword ptr [rbx]
0063D00F  48 3B DE                        cmp rbx, rsi
0063D012  75 E2                           jne 0x14063cff6
0063D014  40 84 FF                        test dil, dil
0063D017  74 0C                           je 0x14063d025
0063D019  48 8D 0D 60 6E 8C 00            lea rcx, [rip + 0x8c6e60]
0063D020  E8 5B CE D0 FF                  call 0x140349e80
0063D025  8B 45 F0                        mov eax, dword ptr [rbp - 0x10]
0063D028  4C 8D 5C 24 50                  lea r11, [rsp + 0x50]
0063D02D  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0063D031  49 8B 73 38                     mov rsi, qword ptr [r11 + 0x38]
0063D035  49 8B 7B 40                     mov rdi, qword ptr [r11 + 0x40]
0063D039  49 8B E3                        mov rsp, r11
0063D03C  41 5F                           pop r15
0063D03E  41 5E                           pop r14
0063D040  41 5D                           pop r13
0063D042  41 5C                           pop r12
0063D044  5D                              pop rbp
0063D045  C3                              ret
0063D046  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifRtlUpcaseUnicodeStringWrapper(__int64 a1, __int64 a2, unsigned __int8 a3)
{
    __int64 result;
    __int64 v_r14;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m28;
    unsigned __int64 v_stack_m38;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m48;
    unsigned __int8 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_p0;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_stack_p18 = v_rdi;
    v_rsp = (v_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(153, a2, a3, a4);
    if (result == 0) goto loc_0063CFAC;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063CF30;
    v_stack_m58 = v_stack_p0;
    goto loc_0063CF3D;
loc_0063CF30:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m58 = result;
    }
    v_r14 = 0;
    v_stack_m40 = a1;
    v_stack_m48 = a2;
    v_stack_m50 = a3;
    if ((*(unsigned __int8 *)(v_rip + 9206125)) != 0) goto loc_0063CF61;
    if (((*(unsigned int *)(v_rip + 9206305)) & (0x800ULL)) == 0) goto loc_0063CF74;
loc_0063CF61:
    result = ExAcquireRundownProtection(v_rip + 9203480, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063CFAC;
loc_0063CF74:
    goto loc_0063CF96;
loc_0063CF7D:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063CF96:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063CF7D;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9203417;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = RtlUpcaseUnicodeString(a1, a2, a3, a4);
    v_stack_m38 = (unsigned int)(result);
    if (result == 0) goto loc_0063D025;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9205996)) != 0) goto loc_0063CFDA;
    if (((*(unsigned int *)(v_rip + 9206184)) & (0x800ULL)) == 0) goto loc_0063CFED;
loc_0063CFDA:
    result = ExAcquireRundownProtection(v_rip + 9203359, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063D025;
loc_0063CFED:
    v_rsi = (result) + (48);
    goto loc_0063D00F;
loc_0063CFF6:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m58;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063D00F:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063CFF6;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9203296;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    return (unsigned int)(v_stack_m38);
}
```

## 5. (Beta) C Style

```c
int64_t DifRtlUpcaseUnicodeStringWrapper(int64_t Arg1, int64_t Arg2, uint8_t Arg3)
{
    int64_t result;
    int64_t local_r14;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m28;
    uint64_t v_stack_m38;
    uint64_t v_stack_m40;
    uint64_t v_stack_m48;
    uint8_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_p0;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    v_stack_p18 = local_rdi;
    local_rsp = (local_rsp) - (80);
    result = 0;
    v_stack_m38 = 0;
    v_stack_m58 = v_xmm0;
    v_stack_m48 = v_xmm0;
    result = DifGetAPIThunkContextById(153, Arg2, Arg3, a4);
    if (result == 0) goto loc_0063CFAC;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063CF30;
    v_stack_m58 = v_stack_p0;
    goto loc_0063CF3D;
loc_0063CF30:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, Arg2, Arg3, a4);
        v_stack_m58 = result;
    }
    local_r14 = 0;
    v_stack_m40 = Arg1;
    v_stack_m48 = Arg2;
    v_stack_m50 = Arg3;
    if ((*(uint8_t *)(v_rip + 0x8C796D)) != 0) goto loc_0063CF61;
    if (((*(uint32_t *)(v_rip + 0x8C7A21)) & (0x800ULL)) == 0) goto loc_0063CF74;
loc_0063CF61:
    result = ExAcquireRundownProtection(v_rip + 9203480, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063CFAC;
loc_0063CF74:
    goto loc_0063CF96;
loc_0063CF7D:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063CF96:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063CF7D;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9203417;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    result = RtlUpcaseUnicodeString(Arg1, Arg2, Arg3, a4);
    v_stack_m38 = (uint32_t)(result);
    if (result == 0) goto loc_0063D025;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C78EC)) != 0) goto loc_0063CFDA;
    if (((*(uint32_t *)(v_rip + 0x8C79A8)) & (0x800ULL)) == 0) goto loc_0063CFED;
loc_0063CFDA:
    result = ExAcquireRundownProtection(v_rip + 9203359, Arg2, Arg3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063D025;
loc_0063CFED:
    local_rsi = (result) + (48);
    goto loc_0063D00F;
loc_0063CFF6:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m58;
        result = guard_dispatch_icall(Arg1, Arg2, Arg3, a4);
    }
loc_0063D00F:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063CFF6;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9203296;
        result = ExReleaseRundownProtection(Arg1, Arg2, Arg3, a4);
    }
    return (uint32_t)(v_stack_m38);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063CED0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063CED0[BB_0063CED0]
  bb_0063CF1F[BB_0063CF1F]
  bb_0063CF26[BB_0063CF26]
  bb_0063CF30[BB_0063CF30]
  bb_0063CF34[BB_0063CF34]
  bb_0063CF3D[BB_0063CF3D]
  bb_0063CF55[BB_0063CF55]
  bb_0063CF61[BB_0063CF61]
  bb_0063CF74[BB_0063CF74]
  bb_0063CF7D[BB_0063CF7D]
  bb_0063CF86[BB_0063CF86]
  bb_0063CF93[BB_0063CF93]
  bb_0063CF96[BB_0063CF96]
  bb_0063CF9B[BB_0063CF9B]
  bb_0063CFA0[BB_0063CFA0]
  bb_0063CFAC[BB_0063CFAC]
  bb_0063CFC2[BB_0063CFC2]
  bb_0063CFCE[BB_0063CFCE]
  bb_0063CFDA[BB_0063CFDA]
  bb_0063CFED[BB_0063CFED]
  bb_0063CFF6[BB_0063CFF6]
  bb_0063CFFF[BB_0063CFFF]
  bb_0063D00C[BB_0063D00C]
  bb_0063D00F[BB_0063D00F]
  bb_0063D014[BB_0063D014]
  bb_0063D019[BB_0063D019]
  bb_0063D025[BB_0063D025]
  bb_0063D046[BB_0063D046]
  bb_0063CED0 -->|branch| bb_0063CFAC
  bb_0063CED0 -->|fallthrough| bb_0063CF1F
  bb_0063CF1F -->|branch| bb_0063CF30
  bb_0063CF1F -->|fallthrough| bb_0063CF26
  bb_0063CF26 -->|branch| bb_0063CF3D
  bb_0063CF30 -->|branch| bb_0063CF3D
  bb_0063CF30 -->|fallthrough| bb_0063CF34
  bb_0063CF34 -->|flow| bb_0063CF3D
  bb_0063CF3D -->|branch| bb_0063CF61
  bb_0063CF3D -->|fallthrough| bb_0063CF55
  bb_0063CF55 -->|branch| bb_0063CF74
  bb_0063CF55 -->|fallthrough| bb_0063CF61
  bb_0063CF61 -->|branch| bb_0063CFAC
  bb_0063CF61 -->|fallthrough| bb_0063CF74
  bb_0063CF74 -->|branch| bb_0063CF96
  bb_0063CF7D -->|branch| bb_0063CF93
  bb_0063CF7D -->|fallthrough| bb_0063CF86
  bb_0063CF86 -->|flow| bb_0063CF93
  bb_0063CF93 -->|flow| bb_0063CF96
  bb_0063CF96 -->|branch| bb_0063CF7D
  bb_0063CF96 -->|fallthrough| bb_0063CF9B
  bb_0063CF9B -->|branch| bb_0063CFAC
  bb_0063CF9B -->|fallthrough| bb_0063CFA0
  bb_0063CFA0 -->|flow| bb_0063CFAC
  bb_0063CFAC -->|branch| bb_0063D025
  bb_0063CFAC -->|fallthrough| bb_0063CFC2
  bb_0063CFC2 -->|branch| bb_0063CFDA
  bb_0063CFC2 -->|fallthrough| bb_0063CFCE
  bb_0063CFCE -->|branch| bb_0063CFED
  bb_0063CFCE -->|fallthrough| bb_0063CFDA
  bb_0063CFDA -->|branch| bb_0063D025
  bb_0063CFDA -->|fallthrough| bb_0063CFED
  bb_0063CFED -->|branch| bb_0063D00F
  bb_0063CFF6 -->|branch| bb_0063D00C
  bb_0063CFF6 -->|fallthrough| bb_0063CFFF
  bb_0063CFFF -->|flow| bb_0063D00C
  bb_0063D00C -->|flow| bb_0063D00F
  bb_0063D00F -->|branch| bb_0063CFF6
  bb_0063D00F -->|fallthrough| bb_0063D014
  bb_0063D014 -->|branch| bb_0063D025
  bb_0063D014 -->|fallthrough| bb_0063D019
  bb_0063D019 -->|flow| bb_0063D025
```
