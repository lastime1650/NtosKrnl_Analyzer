# DifIoGetDeviceToVerifyWrapper

- RVA: `0x0062ABB0`–`0x0062AD10` (길이 `352` bytes)
- VA: `0x000000014062ABB0`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060130`
- 디코드: `93`개 명령, `352/352` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **8**; 고유 호출 대상: **5**
- 직접 호출자로 확인된 함수: **0**
- RIP 상대 이미지 참조: **3**

### Outgoing calls
- `0x0062ABDF` → [DifGetAPIThunkContextById](../49/DifGetAPIThunkContextById_function_00495A34.md) (function, `0x00495A34`)
- `0x0062AC07` → [DifGetReturnAddressForWrappers](../4D/DifGetReturnAddressForWrappers_function_004D3C08.md) (function, `0x004D3C08`)
- `0x0062AC35` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062AC5C` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062AC75` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)
- `0x0062ACAA` → [ExAcquireRundownProtection](../21/ExAcquireRundownProtection_function_00216620.md) (function, `0x00216620`)
- `0x0062ACD1` → [guard_dispatch_icall](../6B/guard_dispatch_icall_function_006BAAD0.md) (function, `0x006BAAD0`)
- `0x0062ACEA` → [ExReleaseRundownProtection](../34/ExReleaseRundownProtection_function_00349E80.md) (function, `0x00349E80`)

### Direct callers
- 이 함수 시작 RVA로 연결되는 직접 call은 확인되지 않았습니다. 간접 호출은 완전히 역산할 수 없습니다.

### Static image references
- `0x0062AC19` → RVA `0x00F048B8` (`.data`; read)
- `0x0062AC22` → RVA `0x00F04980` (`.data`; read)
- `0x0062AC2E` → RVA `0x00F03E80` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0062ABB0  4C 8B DC                        mov r11, rsp
0062ABB3  49 89 5B 08                     mov qword ptr [r11 + 8], rbx
0062ABB7  49 89 6B 10                     mov qword ptr [r11 + 0x10], rbp
0062ABBB  49 89 73 18                     mov qword ptr [r11 + 0x18], rsi
0062ABBF  49 89 7B 20                     mov qword ptr [r11 + 0x20], rdi
0062ABC3  41 56                           push r14
0062ABC5  48 83 EC 40                     sub rsp, 0x40
0062ABC9  33 C0                           xor eax, eax
0062ABCB  0F 57 C0                        xorps xmm0, xmm0
0062ABCE  0F 11 44 24 20                  movups xmmword ptr [rsp + 0x20], xmm0
0062ABD3  48 8B E9                        mov rbp, rcx
0062ABD6  49 89 43 E8                     mov qword ptr [r11 - 0x18], rax
0062ABDA  B9 4F 01 00 00                  mov ecx, 0x14f
0062ABDF  E8 50 AE E6 FF                  call 0x140495a34
0062ABE4  48 8B F0                        mov rsi, rax
0062ABE7  48 85 C0                        test rax, rax
0062ABEA  0F 84 8A 00 00 00               je 0x14062ac7a
0062ABF0  8B 40 0C                        mov eax, dword ptr [rax + 0xc]
0062ABF3  A8 18                           test al, 0x18
0062ABF5  74 0C                           je 0x14062ac03
0062ABF7  48 8B 4C 24 48                  mov rcx, qword ptr [rsp + 0x48]
0062ABFC  48 89 4C 24 20                  mov qword ptr [rsp + 0x20], rcx
0062AC01  EB 0E                           jmp 0x14062ac11
0062AC03  A8 04                           test al, 4
0062AC05  74 0A                           je 0x14062ac11
0062AC07  E8 FC 8F EA FF                  call 0x1404d3c08
0062AC0C  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
0062AC11  40 32 FF                        xor dil, dil
0062AC14  48 89 6C 24 28                  mov qword ptr [rsp + 0x28], rbp
0062AC19  40 38 3D 98 9C 8D 00            cmp byte ptr [rip + 0x8d9c98], dil
0062AC20  75 0C                           jne 0x14062ac2e
0062AC22  F7 05 54 9D 8D 00 00 08 00 00   test dword ptr [rip + 0x8d9d54], 0x800
0062AC2C  74 13                           je 0x14062ac41
0062AC2E  48 8D 0D 4B 92 8D 00            lea rcx, [rip + 0x8d924b]
0062AC35  E8 E6 B9 BE FF                  call 0x140216620
0062AC3A  40 8A F8                        mov dil, al
0062AC3D  84 C0                           test al, al
0062AC3F  74 39                           je 0x14062ac7a
0062AC41  4C 8D 76 20                     lea r14, [rsi + 0x20]
0062AC45  49 8B 1E                        mov rbx, qword ptr [r14]
0062AC48  EB 1A                           jmp 0x14062ac64
0062AC4A  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062AC4E  48 85 C0                        test rax, rax
0062AC51  74 0E                           je 0x14062ac61
0062AC53  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062AC57  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062AC5C  E8 6F FE 08 00                  call 0x1406baad0
0062AC61  48 8B 1B                        mov rbx, qword ptr [rbx]
0062AC64  49 3B DE                        cmp rbx, r14
0062AC67  75 E1                           jne 0x14062ac4a
0062AC69  40 84 FF                        test dil, dil
0062AC6C  74 0C                           je 0x14062ac7a
0062AC6E  48 8D 0D 0B 92 8D 00            lea rcx, [rip + 0x8d920b]
0062AC75  E8 06 F2 D1 FF                  call 0x140349e80
0062AC7A  48 8B 85 58 05 00 00            mov rax, qword ptr [rbp + 0x558]
0062AC81  48 89 44 24 30                  mov qword ptr [rsp + 0x30], rax
0062AC86  48 85 F6                        test rsi, rsi
0062AC89  74 64                           je 0x14062acef
0062AC8B  40 32 FF                        xor dil, dil
0062AC8E  40 38 3D 23 9C 8D 00            cmp byte ptr [rip + 0x8d9c23], dil
0062AC95  75 0C                           jne 0x14062aca3
0062AC97  F7 05 DF 9C 8D 00 00 08 00 00   test dword ptr [rip + 0x8d9cdf], 0x800
0062ACA1  74 13                           je 0x14062acb6
0062ACA3  48 8D 0D D6 91 8D 00            lea rcx, [rip + 0x8d91d6]
0062ACAA  E8 71 B9 BE FF                  call 0x140216620
0062ACAF  40 8A F8                        mov dil, al
0062ACB2  84 C0                           test al, al
0062ACB4  74 39                           je 0x14062acef
0062ACB6  48 83 C6 30                     add rsi, 0x30
0062ACBA  48 8B 1E                        mov rbx, qword ptr [rsi]
0062ACBD  EB 1A                           jmp 0x14062acd9
0062ACBF  48 8D 43 F0                     lea rax, [rbx - 0x10]
0062ACC3  48 85 C0                        test rax, rax
0062ACC6  74 0E                           je 0x14062acd6
0062ACC8  48 8B 40 08                     mov rax, qword ptr [rax + 8]
0062ACCC  48 8D 4C 24 20                  lea rcx, [rsp + 0x20]
0062ACD1  E8 FA FD 08 00                  call 0x1406baad0
0062ACD6  48 8B 1B                        mov rbx, qword ptr [rbx]
0062ACD9  48 3B DE                        cmp rbx, rsi
0062ACDC  75 E1                           jne 0x14062acbf
0062ACDE  40 84 FF                        test dil, dil
0062ACE1  74 0C                           je 0x14062acef
0062ACE3  48 8D 0D 96 91 8D 00            lea rcx, [rip + 0x8d9196]
0062ACEA  E8 91 F1 D1 FF                  call 0x140349e80
0062ACEF  48 8B 44 24 30                  mov rax, qword ptr [rsp + 0x30]
0062ACF4  48 8B 5C 24 50                  mov rbx, qword ptr [rsp + 0x50]
0062ACF9  48 8B 6C 24 58                  mov rbp, qword ptr [rsp + 0x58]
0062ACFE  48 8B 74 24 60                  mov rsi, qword ptr [rsp + 0x60]
0062AD03  48 8B 7C 24 68                  mov rdi, qword ptr [rsp + 0x68]
0062AD08  48 83 C4 40                     add rsp, 0x40
0062AD0C  41 5E                           pop r14
0062AD0E  C3                              ret
0062AD0F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall DifIoGetDeviceToVerifyWrapper(__int64 a1)
{
    __int64 result;
    __int64 v_rdi;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
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
    result = DifGetAPIThunkContextById(335, a2, a3, a4);
    if (result == 0) goto loc_0062AC7A;
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (24)) == 0) goto loc_0062AC03;
    v_stack_m28 = v_stack_p0;
    goto loc_0062AC11;
loc_0062AC03:
    result = (unsigned int)(*(unsigned int *)(result + 12));
    if ((((unsigned __int8)((unsigned int)(*(unsigned int *)(result + 12)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    v_rdi = 0;
    v_stack_m20 = a1;
    if ((*(unsigned __int8 *)(v_rip + 9280664)) != 0) goto loc_0062AC2E;
    if (((*(unsigned int *)(v_rip + 9280852)) & (0x800ULL)) == 0) goto loc_0062AC41;
loc_0062AC2E:
    result = ExAcquireRundownProtection(v_rip + 9278027, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062AC7A;
loc_0062AC41:
    goto loc_0062AC64;
loc_0062AC4A:
    result = *(unsigned __int64 *)(result + 32) - 16;
    if (*(unsigned __int64 *)(result + 32) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(result + 32) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062AC64:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(result + 32))) != (result + 32)) goto loc_0062AC4A;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9277963;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_stack_m18 = *(unsigned __int64 *)(a1 + 1368);
    if (result == 0) goto loc_0062ACEF;
    v_rdi = 0;
    if ((*(unsigned __int8 *)(v_rip + 9280547)) != 0) goto loc_0062ACA3;
    if (((*(unsigned int *)(v_rip + 9280735)) & (0x800ULL)) == 0) goto loc_0062ACB6;
loc_0062ACA3:
    result = ExAcquireRundownProtection(v_rip + 9277910, a2, a3, a4);
    if ((unsigned __int8)(result) == 0) goto loc_0062ACEF;
loc_0062ACB6:
    v_rsi = (result) + (48);
    goto loc_0062ACD9;
loc_0062ACBF:
    result = *(unsigned __int64 *)(v_rsi) - 16;
    if (*(unsigned __int64 *)(v_rsi) - 16 != 0) {
        result = *(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi) - 16 + 8);
        a1 = v_stack_m28;
        result = guard_dispatch_icall(a1, a2, a3, a4);
    }
loc_0062ACD9:
    if ((*(unsigned __int64 *)(*(unsigned __int64 *)(v_rsi))) != v_rsi) goto loc_0062ACBF;
    if ((unsigned __int8)((unsigned __int8)(result)) != 0) {
        a1 = v_rip + 9277846;
        result = ExReleaseRundownProtection(a1, a2, a3, a4);
    }
    v_rsp = (v_rsp) + (64);
    return v_stack_m18;
}
```

## 5. (Beta) C Style

```c
int64_t DifIoGetDeviceToVerifyWrapper(void *Arg1)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rdi;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
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
    result = DifGetAPIThunkContextById(335, a2, a3, a4);
    if (result == 0) goto loc_0062AC7A;
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (24)) == 0) goto loc_0062AC03;
    v_stack_m28 = v_stack_p0;
    goto loc_0062AC11;
loc_0062AC03:
    result = (uint32_t)(*(uint32_t *)(result + 0xC));
    if ((((uint8_t)((uint32_t)(*(uint32_t *)(result + 0xC)))) & (4)) != 0) {
        result = DifGetReturnAddressForWrappers(v_stack_p0, a2, a3, a4);
        v_stack_m28 = result;
    }
    local_rdi = 0;
    v_stack_m20 = Arg1;
    if ((*(uint8_t *)(v_rip + 0x8D9C98)) != 0) goto loc_0062AC2E;
    if (((*(uint32_t *)(v_rip + 0x8D9D54)) & (0x800ULL)) == 0) goto loc_0062AC41;
loc_0062AC2E:
    result = ExAcquireRundownProtection(v_rip + 9278027, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062AC7A;
loc_0062AC41:
    goto loc_0062AC64;
loc_0062AC4A:
    result = *(uint64_t *)(result + 0x20) - 16;
    if (*(uint64_t *)(result + 0x20) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(result + 0x20) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062AC64:
    if ((*(uint64_t *)(*(uint64_t *)(result + 0x20))) != (result + 32)) goto loc_0062AC4A;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9277963;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    v_stack_m18 = *(uint64_t *)(arg1 + 0x558);
    if (result == 0) goto loc_0062ACEF;
    local_rdi = 0;
    if ((*(uint8_t *)(v_rip + 0x8D9C23)) != 0) goto loc_0062ACA3;
    if (((*(uint32_t *)(v_rip + 0x8D9CDF)) & (0x800ULL)) == 0) goto loc_0062ACB6;
loc_0062ACA3:
    result = ExAcquireRundownProtection(v_rip + 9277910, a2, a3, a4);
    if ((uint8_t)(result) == 0) goto loc_0062ACEF;
loc_0062ACB6:
    local_rsi = (result) + (48);
    goto loc_0062ACD9;
loc_0062ACBF:
    result = *(uint64_t *)(local_rsi) - 16;
    if (*(uint64_t *)(local_rsi) - 16 != 0) {
        result = *(uint64_t *)(*(uint64_t *)(local_rsi) - 0x10 + 0x8);
        Arg1 = v_stack_m28;
        result = guard_dispatch_icall(Arg1, a2, a3, a4);
    }
loc_0062ACD9:
    if ((*(uint64_t *)(*(uint64_t *)(local_rsi))) != local_rsi) goto loc_0062ACBF;
    if ((uint8_t)((uint8_t)(result)) != 0) {
        Arg1 = v_rip + 9277846;
        result = ExReleaseRundownProtection(Arg1, a2, a3, a4);
    }
    local_rsp = (local_rsp) + (64);
    return v_stack_m18;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x558` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0062ABB0&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0062ABB0[BB_0062ABB0]
  bb_0062ABF0[BB_0062ABF0]
  bb_0062ABF7[BB_0062ABF7]
  bb_0062AC03[BB_0062AC03]
  bb_0062AC07[BB_0062AC07]
  bb_0062AC11[BB_0062AC11]
  bb_0062AC22[BB_0062AC22]
  bb_0062AC2E[BB_0062AC2E]
  bb_0062AC41[BB_0062AC41]
  bb_0062AC4A[BB_0062AC4A]
  bb_0062AC53[BB_0062AC53]
  bb_0062AC61[BB_0062AC61]
  bb_0062AC64[BB_0062AC64]
  bb_0062AC69[BB_0062AC69]
  bb_0062AC6E[BB_0062AC6E]
  bb_0062AC7A[BB_0062AC7A]
  bb_0062AC8B[BB_0062AC8B]
  bb_0062AC97[BB_0062AC97]
  bb_0062ACA3[BB_0062ACA3]
  bb_0062ACB6[BB_0062ACB6]
  bb_0062ACBF[BB_0062ACBF]
  bb_0062ACC8[BB_0062ACC8]
  bb_0062ACD6[BB_0062ACD6]
  bb_0062ACD9[BB_0062ACD9]
  bb_0062ACDE[BB_0062ACDE]
  bb_0062ACE3[BB_0062ACE3]
  bb_0062ACEF[BB_0062ACEF]
  bb_0062AD0F[BB_0062AD0F]
  bb_0062ABB0 -->|branch| bb_0062AC7A
  bb_0062ABB0 -->|fallthrough| bb_0062ABF0
  bb_0062ABF0 -->|branch| bb_0062AC03
  bb_0062ABF0 -->|fallthrough| bb_0062ABF7
  bb_0062ABF7 -->|branch| bb_0062AC11
  bb_0062AC03 -->|branch| bb_0062AC11
  bb_0062AC03 -->|fallthrough| bb_0062AC07
  bb_0062AC07 -->|flow| bb_0062AC11
  bb_0062AC11 -->|branch| bb_0062AC2E
  bb_0062AC11 -->|fallthrough| bb_0062AC22
  bb_0062AC22 -->|branch| bb_0062AC41
  bb_0062AC22 -->|fallthrough| bb_0062AC2E
  bb_0062AC2E -->|branch| bb_0062AC7A
  bb_0062AC2E -->|fallthrough| bb_0062AC41
  bb_0062AC41 -->|branch| bb_0062AC64
  bb_0062AC4A -->|branch| bb_0062AC61
  bb_0062AC4A -->|fallthrough| bb_0062AC53
  bb_0062AC53 -->|flow| bb_0062AC61
  bb_0062AC61 -->|flow| bb_0062AC64
  bb_0062AC64 -->|branch| bb_0062AC4A
  bb_0062AC64 -->|fallthrough| bb_0062AC69
  bb_0062AC69 -->|branch| bb_0062AC7A
  bb_0062AC69 -->|fallthrough| bb_0062AC6E
  bb_0062AC6E -->|flow| bb_0062AC7A
  bb_0062AC7A -->|branch| bb_0062ACEF
  bb_0062AC7A -->|fallthrough| bb_0062AC8B
  bb_0062AC8B -->|branch| bb_0062ACA3
  bb_0062AC8B -->|fallthrough| bb_0062AC97
  bb_0062AC97 -->|branch| bb_0062ACB6
  bb_0062AC97 -->|fallthrough| bb_0062ACA3
  bb_0062ACA3 -->|branch| bb_0062ACEF
  bb_0062ACA3 -->|fallthrough| bb_0062ACB6
  bb_0062ACB6 -->|branch| bb_0062ACD9
  bb_0062ACBF -->|branch| bb_0062ACD6
  bb_0062ACBF -->|fallthrough| bb_0062ACC8
  bb_0062ACC8 -->|flow| bb_0062ACD6
  bb_0062ACD6 -->|flow| bb_0062ACD9
  bb_0062ACD9 -->|branch| bb_0062ACBF
  bb_0062ACD9 -->|fallthrough| bb_0062ACDE
  bb_0062ACDE -->|branch| bb_0062ACEF
  bb_0062ACDE -->|fallthrough| bb_0062ACE3
  bb_0062ACE3 -->|flow| bb_0062ACEF
```
