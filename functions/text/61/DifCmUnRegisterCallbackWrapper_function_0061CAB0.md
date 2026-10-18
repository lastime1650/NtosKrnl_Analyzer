# DifCmUnRegisterCallbackWrapper

- RVA: `0x0061CAB0`–`0x0061CC0F` (길이 `351` bytes)
- VA: `0x000000014061CAB0`
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
- `0x0061CADF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0061CB07` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0061CB35` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061CB5C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061CB75` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0061CB7D` → [CmUnRegisterCallback](../../page/7E/CmUnRegisterCallback_function_007E1510.md) (function, `0x007E1510`)
- `0x0061CBAA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0061CBD1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0061CBEA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0061CB19` → RVA `0x00F048B8` (`.data`; read)
- `0x0061CB22` → RVA `0x00F04980` (`.data`; read)
- `0x0061CB2E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0061CB7D` → [CmUnRegisterCallback](../../page/7E/CmUnRegisterCallback_function_007E1510.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0061CAB0  4C 8B DC                        mov r11, rsp
0061CAB3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0061CAB7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0061CABB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0061CABF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0061CAC3  41 56                           push r14
0061CAC5  48 83 EC 40                     sub rsp, 0x40
0061CAC9  33 C0                           xor eax, eax
0061CACB  0F 57 C0                        xorps xmm0, xmm0
0061CACE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0061CAD3  48 8B D9                        mov rbx, rcx
0061CAD6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0061CADA  B9 AC 01 00 00                  mov ecx, 0x1ac
0061CADF  E8 50 8F E7 FF                  call 0x140495a34
0061CAE4  48 8B F0                        mov rsi, rax
0061CAE7  48 85 C0                        test rax, rax
0061CAEA  0F 84 8A 00 00 00               je 0x14061cb7a
0061CAF0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0061CAF3  A8 18                           test al, 0x18
0061CAF5  74 0C                           je 0x14061cb03
0061CAF7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0061CAFC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0061CB01  EB 0E                           jmp 0x14061cb11
0061CB03  A8 04                           test al, 4
0061CB05  74 0A                           je 0x14061cb11
0061CB07  E8 FC 70 EB FF                  call 0x1404d3c08
0061CB0C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0061CB11  40 32 ED                        xor bpl, bpl
0061CB14  48 89 5C 24 28                  mov qword ptr [rsp + 0x28], rbx
0061CB19  40 38 2D 98 7D 8E 00            cmp byte ptr [rip + 0x8e7d98], bpl
0061CB20  75 0C                           jne 0x14061cb2e
0061CB22  F7 05 54 7E 8E 00 00 08 00 00   test dword ptr [rip + 0x8e7e54], 0x800
0061CB2C  74 13                           je 0x14061cb41
0061CB2E  48 8D 0D 4B 73 8E 00            lea rcx, [rip + 0x8e734b]
0061CB35  E8 E6 9A BF FF                  call 0x140216620
0061CB3A  40 8A E8                        mov bpl, al
0061CB3D  84 C0                           test al, al
0061CB3F  74 39                           je 0x14061cb7a
0061CB41  4C 8D 76 20                     lea r14, [rsi + 0x20]
0061CB45  49 8B 3E                        mov rdi, qword ptr [r14]
0061CB48  EB 1A                           jmp 0x14061cb64
0061CB4A  48 8D 47 F0                     lea rax, [rdi - 0x10]
0061CB4E  48 85 C0                        test rax, rax
0061CB51  74 0E                           je 0x14061cb61
0061CB53  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061CB57  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061CB5C  E8 6F DF 09 00                  call 0x1406baad0
0061CB61  48 8B 3F                        mov rdi, qword ptr [rdi]
0061CB64  49 3B FE                        cmp rdi, r14
0061CB67  75 E1                           jne 0x14061cb4a
0061CB69  40 84 ED                        test bpl, bpl
0061CB6C  74 0C                           je 0x14061cb7a
0061CB6E  48 8D 0D 0B 73 8E 00            lea rcx, [rip + 0x8e730b]
0061CB75  E8 06 D3 D2 FF                  call 0x140349e80
0061CB7A  48 8B CB                        mov rcx, rbx
0061CB7D  E8 8E 49 1C 00                  call 0x1407e1510
0061CB82  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0061CB86  48 85 F6                        test rsi, rsi
0061CB89  74 64                           je 0x14061cbef
0061CB8B  40 32 FF                        xor dil, dil
0061CB8E  40 38 3D 23 7D 8E 00            cmp byte ptr [rip + 0x8e7d23], dil
0061CB95  75 0C                           jne 0x14061cba3
0061CB97  F7 05 DF 7D 8E 00 00 08 00 00   test dword ptr [rip + 0x8e7ddf], 0x800
0061CBA1  74 13                           je 0x14061cbb6
0061CBA3  48 8D 0D D6 72 8E 00            lea rcx, [rip + 0x8e72d6]
0061CBAA  E8 71 9A BF FF                  call 0x140216620
0061CBAF  40 8A F8                        mov dil, al
0061CBB2  84 C0                           test al, al
0061CBB4  74 39                           je 0x14061cbef
0061CBB6  48 83 C6 30                     add rsi, 0x30
0061CBBA  48 8B 1E                        mov rbx, qword ptr [rsi]
0061CBBD  EB 1A                           jmp 0x14061cbd9
0061CBBF  48 8D 43 F0                     lea rax, [rbx - 0x10]
0061CBC3  48 85 C0                        test rax, rax
0061CBC6  74 0E                           je 0x14061cbd6
0061CBC8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0061CBCC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0061CBD1  E8 FA DE 09 00                  call 0x1406baad0
0061CBD6  48 8B 1B                        mov rbx, qword ptr [rbx]
0061CBD9  48 3B DE                        cmp rbx, rsi
0061CBDC  75 E1                           jne 0x14061cbbf
0061CBDE  40 84 FF                        test dil, dil
0061CBE1  74 0C                           je 0x14061cbef
0061CBE3  48 8D 0D 96 72 8E 00            lea rcx, [rip + 0x8e7296]
0061CBEA  E8 91 D2 D2 FF                  call 0x140349e80
0061CBEF  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0061CBF3  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0061CBF8  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0061CBFD  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0061CC02  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0061CC07  48 83 C4 40                     add rsp, 0x40
0061CC0B  41 5E                           pop r14
0061CC0D  C3                              ret
0061CC0E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifCmUnRegisterCallbackWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rbp;
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
    result = DifGetAPIThunkContextById(428, a2, a3, a4);
    if (result == 0) goto loc_0061CB7A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0061CB03;
    v_stack_m28 = v_stack_p0;
    goto loc_0061CB11;
loc_0061CB03:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rbp = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9338264)) != 0) goto loc_0061CB2E;
    if (((*(unsigned int *)(v_rip + 9338452)) & (0x800ULL)) == 0) goto loc_0061CB41;
loc_0061CB2E:
    result = ExAcquireRundownProtection(v_rip + 9335627, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061CB7A;
loc_0061CB41:
    goto loc_0061CB64;
loc_0061CB4A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061CB64:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0061CB4A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9335563;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = CmUnRegisterCallback(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0061CBEF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9338147)) != 0) goto loc_0061CBA3;
    if (((*(unsigned int *)(v_rip + 9338335)) & (0x800ULL)) == 0) goto loc_0061CBB6;
loc_0061CBA3:
    result = ExAcquireRundownProtection(v_rip + 9335510, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0061CBEF;
loc_0061CBB6:
    v_rsi = (result) + (48);
    goto loc_0061CBD9;
loc_0061CBBF:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0061CBD9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0061CBBF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9335446;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifCmUnRegisterCallbackWrapper(int64_t Arg1)
{
    int64_t result;
    int64_t local_rbp;
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
    result = DifGetAPIThunkContextById(428, a2, a3, a4);
    if (result == 0) goto loc_0061CB7A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0061CB03;
    v_stack_m28 = v_stack_p0;
    goto loc_0061CB11;
loc_0061CB03:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rbp = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8E7D98)) != 0) goto loc_0061CB2E;
    if (((*(uint32_t *)(v_rip + 0x8E7E54)) & (0x800ULL)) == 0) goto loc_0061CB41;
loc_0061CB2E:
    result = ExAcquireRundownProtection(v_rip + 9335627, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061CB7A;
loc_0061CB41:
    goto loc_0061CB64;
loc_0061CB4A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061CB64:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0061CB4A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9335563;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = CmUnRegisterCallback(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0061CBEF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8E7D23)) != 0) goto loc_0061CBA3;
    if (((*(uint32_t *)(v_rip + 0x8E7DDF)) & (0x800ULL)) == 0) goto loc_0061CBB6;
loc_0061CBA3:
    result = ExAcquireRundownProtection(v_rip + 9335510, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0061CBEF;
loc_0061CBB6:
    local_rsi = (result) + (48);
    goto loc_0061CBD9;
loc_0061CBBF:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0061CBD9:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0061CBBF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9335446;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0061CAB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0061CAB0[BB_0061CAB0]
  bb_0061CAF0[BB_0061CAF0]
  bb_0061CAF7[BB_0061CAF7]
  bb_0061CB03[BB_0061CB03]
  bb_0061CB07[BB_0061CB07]
  bb_0061CB11[BB_0061CB11]
  bb_0061CB22[BB_0061CB22]
  bb_0061CB2E[BB_0061CB2E]
  bb_0061CB41[BB_0061CB41]
  bb_0061CB4A[BB_0061CB4A]
  bb_0061CB53[BB_0061CB53]
  bb_0061CB61[BB_0061CB61]
  bb_0061CB64[BB_0061CB64]
  bb_0061CB69[BB_0061CB69]
  bb_0061CB6E[BB_0061CB6E]
  bb_0061CB7A[BB_0061CB7A]
  bb_0061CB8B[BB_0061CB8B]
  bb_0061CB97[BB_0061CB97]
  bb_0061CBA3[BB_0061CBA3]
  bb_0061CBB6[BB_0061CBB6]
  bb_0061CBBF[BB_0061CBBF]
  bb_0061CBC8[BB_0061CBC8]
  bb_0061CBD6[BB_0061CBD6]
  bb_0061CBD9[BB_0061CBD9]
  bb_0061CBDE[BB_0061CBDE]
  bb_0061CBE3[BB_0061CBE3]
  bb_0061CBEF[BB_0061CBEF]
  bb_0061CC0E[BB_0061CC0E]
  bb_0061CAB0 -->|branch| bb_0061CB7A
  bb_0061CAB0 -->|fallthrough| bb_0061CAF0
  bb_0061CAF0 -->|branch| bb_0061CB03
  bb_0061CAF0 -->|fallthrough| bb_0061CAF7
  bb_0061CAF7 -->|branch| bb_0061CB11
  bb_0061CB03 -->|branch| bb_0061CB11
  bb_0061CB03 -->|fallthrough| bb_0061CB07
  bb_0061CB07 -->|flow| bb_0061CB11
  bb_0061CB11 -->|branch| bb_0061CB2E
  bb_0061CB11 -->|fallthrough| bb_0061CB22
  bb_0061CB22 -->|branch| bb_0061CB41
  bb_0061CB22 -->|fallthrough| bb_0061CB2E
  bb_0061CB2E -->|branch| bb_0061CB7A
  bb_0061CB2E -->|fallthrough| bb_0061CB41
  bb_0061CB41 -->|branch| bb_0061CB64
  bb_0061CB4A -->|branch| bb_0061CB61
  bb_0061CB4A -->|fallthrough| bb_0061CB53
  bb_0061CB53 -->|flow| bb_0061CB61
  bb_0061CB61 -->|flow| bb_0061CB64
  bb_0061CB64 -->|branch| bb_0061CB4A
  bb_0061CB64 -->|fallthrough| bb_0061CB69
  bb_0061CB69 -->|branch| bb_0061CB7A
  bb_0061CB69 -->|fallthrough| bb_0061CB6E
  bb_0061CB6E -->|flow| bb_0061CB7A
  bb_0061CB7A -->|branch| bb_0061CBEF
  bb_0061CB7A -->|fallthrough| bb_0061CB8B
  bb_0061CB8B -->|branch| bb_0061CBA3
  bb_0061CB8B -->|fallthrough| bb_0061CB97
  bb_0061CB97 -->|branch| bb_0061CBB6
  bb_0061CB97 -->|fallthrough| bb_0061CBA3
  bb_0061CBA3 -->|branch| bb_0061CBEF
  bb_0061CBA3 -->|fallthrough| bb_0061CBB6
  bb_0061CBB6 -->|branch| bb_0061CBD9
  bb_0061CBBF -->|branch| bb_0061CBD6
  bb_0061CBBF -->|fallthrough| bb_0061CBC8
  bb_0061CBC8 -->|flow| bb_0061CBD6
  bb_0061CBD6 -->|flow| bb_0061CBD9
  bb_0061CBD9 -->|branch| bb_0061CBBF
  bb_0061CBD9 -->|fallthrough| bb_0061CBDE
  bb_0061CBDE -->|branch| bb_0061CBEF
  bb_0061CBDE -->|fallthrough| bb_0061CBE3
  bb_0061CBE3 -->|flow| bb_0061CBEF
```
