# DifPsSetCreateThreadNotifyRoutineWrapper

- RVA: `0x0063ADC0`–`0x0063AF1F` (길이 `351` bytes)
- VA: `0x000000014063ADC0`
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
- `0x0063ADEF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0063AE17` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0063AE45` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063AE6C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063AE85` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0063AE8D` → [PsSetCreateThreadNotifyRoutine](../../page/78/PsSetCreateThreadNotifyRoutine_function_007877D0.md) (function, `0x007877D0`)
- `0x0063AEBA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0063AEE1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0063AEFA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0063AE29` → RVA `0x00F048B8` (`.data`; read)
- `0x0063AE32` → RVA `0x00F04980` (`.data`; read)
- `0x0063AE3E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x0063AE8D` → [PsSetCreateThreadNotifyRoutine](../../page/78/PsSetCreateThreadNotifyRoutine_function_007877D0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0063ADC0  4C 8B DC                        mov r11, rsp
0063ADC3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0063ADC7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0063ADCB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0063ADCF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0063ADD3  41 56                           push r14
0063ADD5  48 83 EC 40                     sub rsp, 0x40
0063ADD9  33 C0                           xor eax, eax
0063ADDB  0F 57 C0                        xorps xmm0, xmm0
0063ADDE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0063ADE3  48 8B E9                        mov rbp, rcx
0063ADE6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0063ADEA  B9 AC 00 00 00                  mov ecx, 0xac
0063ADEF  E8 40 AC E5 FF                  call 0x140495a34
0063ADF4  48 8B F0                        mov rsi, rax
0063ADF7  48 85 C0                        test rax, rax
0063ADFA  0F 84 8A 00 00 00               je 0x14063ae8a
0063AE00  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0063AE03  A8 18                           test al, 0x18
0063AE05  74 0C                           je 0x14063ae13
0063AE07  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0063AE0C  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0063AE11  EB 0E                           jmp 0x14063ae21
0063AE13  A8 04                           test al, 4
0063AE15  74 0A                           je 0x14063ae21
0063AE17  E8 EC 8D E9 FF                  call 0x1404d3c08
0063AE1C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0063AE21  40 32 FF                        xor dil, dil
0063AE24  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0063AE29  40 38 3D 88 9A 8C 00            cmp byte ptr [rip + 0x8c9a88], dil
0063AE30  75 0C                           jne 0x14063ae3e
0063AE32  F7 05 44 9B 8C 00 00 08 00 00   test dword ptr [rip + 0x8c9b44], 0x800
0063AE3C  74 13                           je 0x14063ae51
0063AE3E  48 8D 0D 3B 90 8C 00            lea rcx, [rip + 0x8c903b]
0063AE45  E8 D6 B7 BD FF                  call 0x140216620
0063AE4A  40 8A F8                        mov dil, al
0063AE4D  84 C0                           test al, al
0063AE4F  74 39                           je 0x14063ae8a
0063AE51  4C 8D 76 20                     lea r14, [rsi + 0x20]
0063AE55  49 8B 1E                        mov rbx, qword ptr [r14]
0063AE58  EB 1A                           jmp 0x14063ae74
0063AE5A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063AE5E  48 85 C0                        test rax, rax
0063AE61  74 0E                           je 0x14063ae71
0063AE63  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063AE67  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063AE6C  E8 5F FC 07 00                  call 0x1406baad0
0063AE71  48 8B 1B                        mov rbx, qword ptr [rbx]
0063AE74  49 3B DE                        cmp rbx, r14
0063AE77  75 E1                           jne 0x14063ae5a
0063AE79  40 84 FF                        test dil, dil
0063AE7C  74 0C                           je 0x14063ae8a
0063AE7E  48 8D 0D FB 8F 8C 00            lea rcx, [rip + 0x8c8ffb]
0063AE85  E8 F6 EF D0 FF                  call 0x140349e80
0063AE8A  48 8B CD                        mov rcx, rbp
0063AE8D  E8 3E C9 14 00                  call 0x1407877d0
0063AE92  89 44 24 30                     mov dword ptr [rsp + 0x30], eax
0063AE96  48 85 F6                        test rsi, rsi
0063AE99  74 64                           je 0x14063aeff
0063AE9B  40 32 FF                        xor dil, dil
0063AE9E  40 38 3D 13 9A 8C 00            cmp byte ptr [rip + 0x8c9a13], dil
0063AEA5  75 0C                           jne 0x14063aeb3
0063AEA7  F7 05 CF 9A 8C 00 00 08 00 00   test dword ptr [rip + 0x8c9acf], 0x800
0063AEB1  74 13                           je 0x14063aec6
0063AEB3  48 8D 0D C6 8F 8C 00            lea rcx, [rip + 0x8c8fc6]
0063AEBA  E8 61 B7 BD FF                  call 0x140216620
0063AEBF  40 8A F8                        mov dil, al
0063AEC2  84 C0                           test al, al
0063AEC4  74 39                           je 0x14063aeff
0063AEC6  48 83 C6 30                     add rsi, 0x30
0063AECA  48 8B 1E                        mov rbx, qword ptr [rsi]
0063AECD  EB 1A                           jmp 0x14063aee9
0063AECF  48 8D 43 F0                     lea rax, [rbx - 0x10]
0063AED3  48 85 C0                        test rax, rax
0063AED6  74 0E                           je 0x14063aee6
0063AED8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0063AEDC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0063AEE1  E8 EA FB 07 00                  call 0x1406baad0
0063AEE6  48 8B 1B                        mov rbx, qword ptr [rbx]
0063AEE9  48 3B DE                        cmp rbx, rsi
0063AEEC  75 E1                           jne 0x14063aecf
0063AEEE  40 84 FF                        test dil, dil
0063AEF1  74 0C                           je 0x14063aeff
0063AEF3  48 8D 0D 86 8F 8C 00            lea rcx, [rip + 0x8c8f86]
0063AEFA  E8 81 EF D0 FF                  call 0x140349e80
0063AEFF  8B 44 24 30                     mov eax, dword ptr [rsp + 0x30]
0063AF03  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0063AF08  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0063AF0D  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0063AF12  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0063AF17  48 83 C4 40                     add rsp, 0x40
0063AF1B  41 5E                           pop r14
0063AF1D  C3                              ret
0063AF1E  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifPsSetCreateThreadNotifyRoutineWrapper(__int64 a1)
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
    result = DifGetAPIThunkContextById(172, a2, a3, a4);
    if (result == 0) goto loc_0063AE8A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0063AE13;
    v_stack_m28 = v_stack_p0;
    goto loc_0063AE21;
loc_0063AE13:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9214600)) != 0) goto loc_0063AE3E;
    if (((*(unsigned int *)(v_rip + 9214788)) & (0x800ULL)) == 0) goto loc_0063AE51;
loc_0063AE3E:
    result = ExAcquireRundownProtection(v_rip + 9211963, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063AE8A;
loc_0063AE51:
    goto loc_0063AE74;
loc_0063AE5A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063AE74:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0063AE5A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9211899;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    result = PsSetCreateThreadNotifyRoutine(a1, a2, a3, a4);
    v_stack_m18 = (unsigned int)(result);
    if (result == 0) goto loc_0063AEFF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9214483)) != 0) goto loc_0063AEB3;
    if (((*(unsigned int *)(v_rip + 9214671)) & (0x800ULL)) == 0) goto loc_0063AEC6;
loc_0063AEB3:
    result = ExAcquireRundownProtection(v_rip + 9211846, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0063AEFF;
loc_0063AEC6:
    v_rsi = (result) + (48);
    goto loc_0063AEE9;
loc_0063AECF:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0063AEE9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0063AECF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9211782;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return (unsigned int)(v_stack_m18);
}
```

## 5. (Beta) C Style

```c
int64_t DifPsSetCreateThreadNotifyRoutineWrapper(int64_t Arg1)
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
    result = DifGetAPIThunkContextById(172, a2, a3, a4);
    if (result == 0) goto loc_0063AE8A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0063AE13;
    v_stack_m28 = v_stack_p0;
    goto loc_0063AE21;
loc_0063AE13:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8C9A88)) != 0) goto loc_0063AE3E;
    if (((*(uint32_t *)(v_rip + 0x8C9B44)) & (0x800ULL)) == 0) goto loc_0063AE51;
loc_0063AE3E:
    result = ExAcquireRundownProtection(v_rip + 9211963, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063AE8A;
loc_0063AE51:
    goto loc_0063AE74;
loc_0063AE5A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063AE74:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0063AE5A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9211899;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    result = PsSetCreateThreadNotifyRoutine(Arg1, a2, a3, a4);
    v_stack_m18 = (uint32_t)(result);
    if (result == 0) goto loc_0063AEFF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8C9A13)) != 0) goto loc_0063AEB3;
    if (((*(uint32_t *)(v_rip + 0x8C9ACF)) & (0x800ULL)) == 0) goto loc_0063AEC6;
loc_0063AEB3:
    result = ExAcquireRundownProtection(v_rip + 9211846, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0063AEFF;
loc_0063AEC6:
    local_rsi = (result) + (48);
    goto loc_0063AEE9;
loc_0063AECF:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0063AEE9:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0063AECF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9211782;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return (uint32_t)(v_stack_m18);
}
```

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0063ADC0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0063ADC0[BB_0063ADC0]
  bb_0063AE00[BB_0063AE00]
  bb_0063AE07[BB_0063AE07]
  bb_0063AE13[BB_0063AE13]
  bb_0063AE17[BB_0063AE17]
  bb_0063AE21[BB_0063AE21]
  bb_0063AE32[BB_0063AE32]
  bb_0063AE3E[BB_0063AE3E]
  bb_0063AE51[BB_0063AE51]
  bb_0063AE5A[BB_0063AE5A]
  bb_0063AE63[BB_0063AE63]
  bb_0063AE71[BB_0063AE71]
  bb_0063AE74[BB_0063AE74]
  bb_0063AE79[BB_0063AE79]
  bb_0063AE7E[BB_0063AE7E]
  bb_0063AE8A[BB_0063AE8A]
  bb_0063AE9B[BB_0063AE9B]
  bb_0063AEA7[BB_0063AEA7]
  bb_0063AEB3[BB_0063AEB3]
  bb_0063AEC6[BB_0063AEC6]
  bb_0063AECF[BB_0063AECF]
  bb_0063AED8[BB_0063AED8]
  bb_0063AEE6[BB_0063AEE6]
  bb_0063AEE9[BB_0063AEE9]
  bb_0063AEEE[BB_0063AEEE]
  bb_0063AEF3[BB_0063AEF3]
  bb_0063AEFF[BB_0063AEFF]
  bb_0063AF1E[BB_0063AF1E]
  bb_0063ADC0 -->|branch| bb_0063AE8A
  bb_0063ADC0 -->|fallthrough| bb_0063AE00
  bb_0063AE00 -->|branch| bb_0063AE13
  bb_0063AE00 -->|fallthrough| bb_0063AE07
  bb_0063AE07 -->|branch| bb_0063AE21
  bb_0063AE13 -->|branch| bb_0063AE21
  bb_0063AE13 -->|fallthrough| bb_0063AE17
  bb_0063AE17 -->|flow| bb_0063AE21
  bb_0063AE21 -->|branch| bb_0063AE3E
  bb_0063AE21 -->|fallthrough| bb_0063AE32
  bb_0063AE32 -->|branch| bb_0063AE51
  bb_0063AE32 -->|fallthrough| bb_0063AE3E
  bb_0063AE3E -->|branch| bb_0063AE8A
  bb_0063AE3E -->|fallthrough| bb_0063AE51
  bb_0063AE51 -->|branch| bb_0063AE74
  bb_0063AE5A -->|branch| bb_0063AE71
  bb_0063AE5A -->|fallthrough| bb_0063AE63
  bb_0063AE63 -->|flow| bb_0063AE71
  bb_0063AE71 -->|flow| bb_0063AE74
  bb_0063AE74 -->|branch| bb_0063AE5A
  bb_0063AE74 -->|fallthrough| bb_0063AE79
  bb_0063AE79 -->|branch| bb_0063AE8A
  bb_0063AE79 -->|fallthrough| bb_0063AE7E
  bb_0063AE7E -->|flow| bb_0063AE8A
  bb_0063AE8A -->|branch| bb_0063AEFF
  bb_0063AE8A -->|fallthrough| bb_0063AE9B
  bb_0063AE9B -->|branch| bb_0063AEB3
  bb_0063AE9B -->|fallthrough| bb_0063AEA7
  bb_0063AEA7 -->|branch| bb_0063AEC6
  bb_0063AEA7 -->|fallthrough| bb_0063AEB3
  bb_0063AEB3 -->|branch| bb_0063AEFF
  bb_0063AEB3 -->|fallthrough| bb_0063AEC6
  bb_0063AEC6 -->|branch| bb_0063AEE9
  bb_0063AECF -->|branch| bb_0063AEE6
  bb_0063AECF -->|fallthrough| bb_0063AED8
  bb_0063AED8 -->|flow| bb_0063AEE6
  bb_0063AEE6 -->|flow| bb_0063AEE9
  bb_0063AEE9 -->|branch| bb_0063AECF
  bb_0063AEE9 -->|fallthrough| bb_0063AEEE
  bb_0063AEEE -->|branch| bb_0063AEFF
  bb_0063AEEE -->|fallthrough| bb_0063AEF3
  bb_0063AEF3 -->|flow| bb_0063AEFF
```
