# CmSiAcquireProcessLockedPagesCharge

- RVA: `0x0047D714`–`0x0047D7DB` (길이 `199` bytes)
- VA: `0x000000014047D714`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000ADAF8`
- 디코드: `55`개 명령, `199/199` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **6**; 고유 호출 대상: **6**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **1**

### Outgoing calls
- `0x0047D756` → [KeStackAttachProcess](../21/KeStackAttachProcess_function_00216800.md) (function, `0x00216800`)
- `0x0047D75F` → [CmSiRWLockAcquireExclusive](../../page/A1/CmSiRWLockAcquireExclusive_function_00A1679C.md) (function, `0x00A1679C`)
- `0x0047D78C` → [MmAdjustWorkingSetSizeEx](MmAdjustWorkingSetSizeEx_function_0047D8D4.md) (function, `0x0047D8D4`)
- `0x0047D7A5` → [CmSiRWLockReleaseExclusive](../../page/A0/CmSiRWLockReleaseExclusive_function_00A0DAB0.md) (function, `0x00A0DAB0`)
- `0x0047D7B1` → [KiUnstackDetachProcess](../21/KiUnstackDetachProcess_function_00217D30.md) (function, `0x00217D30`)
- `0x0047D7C0` → [_security_check_cookie](../6A/_security_check_cookie_function_006AC640.md) (function, `0x006AC640`)

### Direct callers
- [HvpViewMapAcquireChargesAndLockViewPages](../../page/9B/HvpViewMapAcquireChargesAndLockViewPages_function_009B6480.md) at `0x009B64A3`

### Static image references
- `0x0047D726` → RVA `0x00E0A740` (`.data`; read)

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **2**
  - `0x0047D75F` → [CmSiRWLockAcquireExclusive](../../page/A1/CmSiRWLockAcquireExclusive_function_00A1679C.md) (`.text` → `PAGE`)
  - `0x0047D7A5` → [CmSiRWLockReleaseExclusive](../../page/A0/CmSiRWLockReleaseExclusive_function_00A0DAB0.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
0047D714  48 89 5C 24 18                  mov qword ptr [rsp + 0x18], rbx
0047D719  48 89 6C 24 20                  mov qword ptr [rsp + 0x20], rbp
0047D71E  56                              push rsi
0047D71F  57                              push rdi
0047D720  41 56                           push r14
0047D722  48 83 EC 70                     sub rsp, 0x70
0047D726  48 8B 05 13 D0 98 00            mov rax, qword ptr [rip + 0x98d013]
0047D72D  48 33 C4                        xor rax, rsp
0047D730  48 89 44 24 68                  mov qword ptr [rsp + 0x68], rax
0047D735  0F 57 C0                        xorps xmm0, xmm0
0047D738  4C 8B F2                        mov r14, rdx
0047D73B  48 8B D9                        mov rbx, rcx
0047D73E  48 8D 54 24 38                  lea rdx, [rsp + 0x38]
0047D743  48 8B 49 08                     mov rcx, qword ptr [rcx + 8]
0047D747  0F 11 44 24 38                  movups xmmword ptr [rsp + 0x38], xmm0
0047D74C  0F 11 44 24 48                  movups xmmword ptr [rsp + 0x48], xmm0
0047D751  0F 11 44 24 58                  movups xmmword ptr [rsp + 0x58], xmm0
0047D756  E8 A5 90 D9 FF                  call 0x140216800
0047D75B  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0047D75F  E8 38 90 59 00                  call 0x140a1679c
0047D764  48 8B 6B 20                     mov rbp, qword ptr [rbx + 0x20]
0047D768  48 8D 44 24 30                  lea rax, [rsp + 0x30]
0047D76D  48 8B 53 28                     mov rdx, qword ptr [rbx + 0x28]
0047D771  49 03 EE                        add rbp, r14
0047D774  48 89 44 24 28                  mov qword ptr [rsp + 0x28], rax
0047D779  48 8B CD                        mov rcx, rbp
0047D77C  83 64 24 20 00                  and dword ptr [rsp + 0x20], 0
0047D781  41 B1 01                        mov r9b, 1
0047D784  45 33 C0                        xor r8d, r8d
0047D787  C6 44 24 30 00                  mov byte ptr [rsp + 0x30], 0
0047D78C  E8 43 01 00 00                  call 0x14047d8d4
0047D791  8B F8                           mov edi, eax
0047D793  85 C0                           test eax, eax
0047D795  78 0A                           js 0x14047d7a1
0047D797  4C 01 73 18                     add qword ptr [rbx + 0x18], r14
0047D79B  33 FF                           xor edi, edi
0047D79D  48 89 6B 20                     mov qword ptr [rbx + 0x20], rbp
0047D7A1  48 8D 4B 10                     lea rcx, [rbx + 0x10]
0047D7A5  E8 06 03 59 00                  call 0x140a0dab0
0047D7AA  33 D2                           xor edx, edx
0047D7AC  48 8D 4C 24 38                  lea rcx, [rsp + 0x38]
0047D7B1  E8 7A A5 D9 FF                  call 0x140217d30
0047D7B6  8B C7                           mov eax, edi
0047D7B8  48 8B 4C 24 68                  mov rcx, qword ptr [rsp + 0x68]
0047D7BD  48 33 CC                        xor rcx, rsp
0047D7C0  E8 7B EE 22 00                  call 0x1406ac640
0047D7C5  4C 8D 5C 24 70                  lea r11, [rsp + 0x70]
0047D7CA  49 8B 5B 30                     mov rbx, qword ptr [r11 + 0x30]
0047D7CE  49 8B 6B 38                     mov rbp, qword ptr [r11 + 0x38]
0047D7D2  49 8B E3                        mov rsp, r11
0047D7D5  41 5E                           pop r14
0047D7D7  5F                              pop rdi
0047D7D8  5E                              pop rsi
0047D7D9  C3                              ret
0047D7DA  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall CmSiAcquireProcessLockedPagesCharge(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rbp;
    __int64 v_rdi;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;
    unsigned __int64 v_stack_m20;
    unsigned __int64 v_stack_m30;
    unsigned __int64 v_stack_m40;
    unsigned __int64 v_stack_m50;
    unsigned __int64 v_stack_m58;
    unsigned __int64 v_stack_m60;
    unsigned int v_stack_m68;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;

    v_stack_p18 = v_rbx;
    v_stack_p20 = v_rbp;
    v_rsp = (v_rsp) - (112);
    result = (*(unsigned __int64 *)(v_rip + 10014739)) ^ (v_rsp);
    v_stack_m20 = result;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = v_xmm0;
    v_stack_m30 = v_xmm0;
    result = KeStackAttachProcess(*(unsigned __int64 *)(a1 + 8), v_stack_m50, a3, a4);
    result = CmSiRWLockAcquireExclusive(a1 + 16, v_stack_m50, a3, a4);
    v_rbp = (*(unsigned __int64 *)(a1 + 32)) + (a2);
    v_stack_m60 = v_stack_m58;
    a3 = 0;
    v_stack_m58 = 0;
    result = MmAdjustWorkingSetSizeEx(v_rbp, *(unsigned __int64 *)(a1 + 40), a3, 1);
    v_rdi = (unsigned int)((unsigned int)(result));
    if (!(sign_flag)) {
        v_rdi = 0;
        *(unsigned __int64 *)(a1 + 32) = v_rbp;
    }
    result = CmSiRWLockReleaseExclusive(a1 + 16, *(unsigned __int64 *)(a1 + 40), a3, 1);
    a2 = 0;
    result = KiUnstackDetachProcess(v_stack_m50, a2, a3, 1);
    a1 = (v_stack_m20) ^ (v_rsp);
    result = _security_check_cookie(a1, a2, a3, 1);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t CmSiAcquireProcessLockedPagesCharge(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rbp;
    int64_t local_rdi;
    int64_t local_rsp;
    uint64_t v_stack_m18;
    uint64_t v_stack_m20;
    uint64_t v_stack_m30;
    uint64_t v_stack_m40;
    uint64_t v_stack_m50;
    uint64_t v_stack_m58;
    uint64_t v_stack_m60;
    uint32_t v_stack_m68;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;

    v_stack_p18 = local_rbx;
    v_stack_p20 = local_rbp;
    local_rsp = (local_rsp) - (112);
    result = (*(uint64_t *)(v_rip + 0x98D013)) ^ (local_rsp);
    v_stack_m20 = result;
    v_stack_m50 = v_xmm0;
    v_stack_m40 = v_xmm0;
    v_stack_m30 = v_xmm0;
    result = KeStackAttachProcess(*(uint64_t *)(arg1 + 0x8), v_stack_m50, Arg3, a4);
    result = CmSiRWLockAcquireExclusive(Arg1 + 16, v_stack_m50, Arg3, a4);
    local_rbp = (*(uint64_t *)(arg1 + 0x20)) + (Arg2);
    v_stack_m60 = v_stack_m58;
    Arg3 = 0;
    v_stack_m58 = 0;
    result = MmAdjustWorkingSetSizeEx(local_rbp, *(uint64_t *)(arg1 + 0x28), Arg3, 1);
    local_rdi = (uint32_t)((uint32_t)(result));
    if (!(sign_flag)) {
        local_rdi = 0;
        *(uint64_t *)(arg1 + 0x20) = local_rbp;
    }
    result = CmSiRWLockReleaseExclusive(Arg1 + 16, *(uint64_t *)(arg1 + 0x28), Arg3, 1);
    Arg2 = 0;
    result = KiUnstackDetachProcess(v_stack_m50, Arg2, Arg3, 1);
    Arg1 = (v_stack_m20) ^ (local_rsp);
    result = _security_check_cookie(Arg1, Arg2, Arg3, 1);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x8` | `64` | `R` |
| `Arg1` | `+ 0x10` | `64` | `R` |
| `Arg1` | `+ 0x18` | `64` | `R/W` |
| `Arg1` | `+ 0x20` | `64` | `R` |
| `Arg1` | `+ 0x20` | `64` | `W` |
| `Arg1` | `+ 0x28` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x0047D714&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_0047D714[BB_0047D714]
  bb_0047D797[BB_0047D797]
  bb_0047D7A1[BB_0047D7A1]
  bb_0047D7DA[BB_0047D7DA]
  bb_0047D714 -->|branch| bb_0047D7A1
  bb_0047D714 -->|fallthrough| bb_0047D797
  bb_0047D797 -->|flow| bb_0047D7A1
```
