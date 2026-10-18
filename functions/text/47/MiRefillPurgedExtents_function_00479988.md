# MiRefillPurgedExtents

- RVA: `0x00479988`–`0x00479A19` (길이 `145` bytes)
- VA: `0x0000000140479988`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x0005D7BC`
- 디코드: `39`개 명령, `145/145` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004799B1` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x004799C4` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)
- `0x004799EC` → [MiAllocateFileExtents](../../page/AB/MiAllocateFileExtents_function_00ABDF54.md) (function, `0x00ABDF54`)
- `0x004799F6` → [MiDereferenceControlArea](MiDereferenceControlArea_function_00479A20.md) (function, `0x00479A20`)

### Direct callers
- [MiPfPutPagesInTransition](../36/MiPfPutPagesInTransition_function_003640EC.md) at `0x00364AF6`
- [MiPfPrepareReadList](../../page/93/MiPfPrepareReadList_function_0093CD5C.md) at `0x0093D2A5`
- [MiPfPrepareSequentialReadList](../../page/93/MiPfPrepareSequentialReadList_function_0093D8E8.md) at `0x0093DF4D`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **1**
  - `0x004799EC` → [MiAllocateFileExtents](../../page/AB/MiAllocateFileExtents_function_00ABDF54.md) (`.text` → `PAGE`)
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
00479988  48 8B C4                        mov rax, rsp
0047998B  48 89 58 08                     mov qword ptr [rax + 8], rbx
0047998F  48 89 68 10                     mov qword ptr [rax + 0x10], rbp
00479993  48 89 70 18                     mov qword ptr [rax + 0x18], rsi
00479997  48 89 78 20                     mov qword ptr [rax + 0x20], rdi
0047999B  41 56                           push r14
0047999D  48 83 EC 30                     sub rsp, 0x30
004799A1  48 8B 29                        mov rbp, qword ptr [rcx]
004799A4  4C 8B F1                        mov r14, rcx
004799A7  41 8B F8                        mov edi, r8d
004799AA  48 8B F2                        mov rsi, rdx
004799AD  48 8D 4D 48                     lea rcx, [rbp + 0x48]
004799B1  E8 DA EC DC FF                  call 0x140248690
004799B6  48 FF 45 28                     inc qword ptr [rbp + 0x28]
004799BA  48 8D 4D 48                     lea rcx, [rbp + 0x48]
004799BE  48 FF 45 30                     inc qword ptr [rbp + 0x30]
004799C2  8A D0                           mov dl, al
004799C4  E8 F7 E8 DC FF                  call 0x1402482c0
004799C9  48 8B D6                        mov rdx, rsi
004799CC  89 7C 24 28                     mov dword ptr [rsp + 0x28], edi
004799D0  49 2B 56 08                     sub rdx, qword ptr [r14 + 8]
004799D4  41 B9 01 00 00 00               mov r9d, 1
004799DA  48 C1 FA 03                     sar rdx, 3
004799DE  4C 8B C6                        mov r8, rsi
004799E1  49 8B CE                        mov rcx, r14
004799E4  C7 44 24 20 02 00 00 00         mov dword ptr [rsp + 0x20], 2
004799EC  E8 63 45 64 00                  call 0x140abdf54
004799F1  48 8B CD                        mov rcx, rbp
004799F4  8B D8                           mov ebx, eax
004799F6  E8 25 00 00 00                  call 0x140479a20
004799FB  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
00479A00  8B C3                           mov eax, ebx
00479A02  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
00479A07  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
00479A0C  48 8B 7C 24 58                  mov rdi, qword ptr [rsp + 0x58]
00479A11  48 83 C4 30                     add rsp, 0x30
00479A15  41 5E                           pop r14
00479A17  C3                              ret
00479A18  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiRefillPurgedExtents(__int64 a1, __int64 a2, int a3)
{
    __int64 result;
    __int64 v_rsp;
    unsigned int v_stack_m10;
    unsigned int v_stack_m18;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p20;
    unsigned __int64 v_stack_p8;

    *(unsigned __int64 *)(v_rsp + 8) = v_rbx;
    *(unsigned __int64 *)(v_rsp + 16) = v_rbp;
    *(unsigned __int64 *)(v_rsp + 24) = v_rsi;
    *(unsigned __int64 *)(v_rsp + 32) = v_rdi;
    v_rsp = (v_rsp) - (48);
    result = ExAcquireSpinLockExclusive(*(unsigned __int64 *)(a1) + 72, a2, a3, a4);
    result = MiReleaseSpinLockExclusive(*(unsigned __int64 *)(a1) + 72, (unsigned __int8)(result), a3, a4);
    v_stack_m10 = (unsigned int)((unsigned int)(a3));
    a2 = (a2) - (*(unsigned __int64 *)(a1 + 8));
    a2 = (a2) >> (3);
    v_stack_m18 = 2;
    result = MiAllocateFileExtents(a1, a2, a2, 1);
    result = MiDereferenceControlArea(*(unsigned __int64 *)(a1), a2, a2, 1);
    v_rsp = (v_rsp) + (48);
    return (unsigned int)((unsigned int)((unsigned int)((unsigned int)(result))));
}
```

## 5. (Beta) C Style

```c
int64_t MiRefillPurgedExtents(void *Arg1, int64_t Arg2, int32_t Arg3)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint32_t v_stack_m10;
    uint32_t v_stack_m18;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p20;
    uint64_t v_stack_p8;

    *(uint64_t *)(local_rsp + 0x8) = local_rbx;
    *(uint64_t *)(local_rsp + 0x10) = local_rbp;
    *(uint64_t *)(local_rsp + 0x18) = local_rsi;
    *(uint64_t *)(local_rsp + 0x20) = local_rdi;
    local_rsp = (local_rsp) - (48);
    result = ExAcquireSpinLockExclusive(*(uint64_t *)(arg1) + 72, Arg2, Arg3, a4);
    result = MiReleaseSpinLockExclusive(*(uint64_t *)(arg1) + 72, (uint8_t)(result), Arg3, a4);
    v_stack_m10 = (uint32_t)((uint32_t)(Arg3));
    Arg2 = (Arg2) - (*(uint64_t *)(arg1 + 0x8));
    Arg2 = (Arg2) >> (3);
    v_stack_m18 = 2;
    result = MiAllocateFileExtents(Arg1, Arg2, Arg2, 1);
    result = MiDereferenceControlArea(*(uint64_t *)(arg1), Arg2, Arg2, 1);
    local_rsp = (local_rsp) + (48);
    return (uint32_t)((uint32_t)((uint32_t)((uint32_t)(result))));
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x0` | `64` | `R` |
| `Arg1` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x00479988&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_00479988[BB_00479988]
  bb_00479A18[BB_00479A18]
```
