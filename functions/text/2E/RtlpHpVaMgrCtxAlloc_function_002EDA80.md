# RtlpHpVaMgrCtxAlloc

- RVA: `0x002EDA80`–`0x002EDB14` (길이 `148` bytes)
- VA: `0x00000001402EDA80`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00071920`
- 디코드: `45`개 명령, `148/148` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **4**; 고유 호출 대상: **4**
- 직접 호출자로 확인된 함수: **3**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x002EDAC4` → [RtlpHpVaMgrAlloc](RtlpHpVaMgrAlloc_function_002EDB1C.md) (function, `0x002EDB1C`)
- `0x002EDAED` → [ExAcquireSpinLockShared](../24/ExAcquireSpinLockShared_function_0024DCE0.md) (function, `0x0024DCE0`)
- `0x002EDB00` → [RtlpHpVaMgrCtxAllocatorFind](../4F/RtlpHpVaMgrCtxAllocatorFind_function_004FA484.md) (function, `0x004FA484`)
- `0x002EDB0D` → [ExReleaseSpinLockShared](../2F/ExReleaseSpinLockShared_function_002F0EF0.md) (function, `0x002F0EF0`)

### Direct callers
- [RtlpHpLargeAlloc](RtlpHpLargeAlloc_function_002EBD5C.md) at `0x002EBECF`
- [RtlpHpSegMgrReserve](RtlpHpSegMgrReserve_function_002ED1F0.md) at `0x002ED2D1`
- [RtlpHpAllocVA](../32/RtlpHpAllocVA_function_003276A0.md) at `0x003277C8`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
002EDA80  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
002EDA85  48 89 6C 24 10                  mov qword ptr [rsp + 0x10], rbp
002EDA8A  48 89 74 24 18                  mov qword ptr [rsp + 0x18], rsi
002EDA8F  57                              push rdi
002EDA90  41 56                           push r14
002EDA92  41 57                           push r15
002EDA94  48 83 EC 20                     sub rsp, 0x20
002EDA98  41 8B 01                        mov eax, dword ptr [r9]
002EDA9B  49 8B F1                        mov rsi, r9
002EDA9E  4D 8B F0                        mov r14, r8
002EDAA1  4C 8B FA                        mov r15, rdx
002EDAA4  48 8B E9                        mov rbp, rcx
002EDAA7  83 F8 FF                        cmp eax, -1
002EDAAA  74 37                           je 0x1402edae3
002EDAAC  48 83 C0 2D                     add rax, 0x2d
002EDAB0  48 8D 34 40                     lea rsi, [rax + rax*2]
002EDAB4  48 C1 E6 04                     shl rsi, 4
002EDAB8  48 03 F1                        add rsi, rcx
002EDABB  4D 8B C6                        mov r8, r14
002EDABE  49 8B D7                        mov rdx, r15
002EDAC1  48 8B CE                        mov rcx, rsi
002EDAC4  E8 53 00 00 00                  call 0x1402edb1c
002EDAC9  48 8B 5C 24 40                  mov rbx, qword ptr [rsp + 0x40]
002EDACE  48 8B 6C 24 48                  mov rbp, qword ptr [rsp + 0x48]
002EDAD3  48 8B 74 24 50                  mov rsi, qword ptr [rsp + 0x50]
002EDAD8  48 83 C4 20                     add rsp, 0x20
002EDADC  41 5F                           pop r15
002EDADE  41 5E                           pop r14
002EDAE0  5F                              pop rdi
002EDAE1  C3                              ret
002EDAE2  CC                              int3
002EDAE3  48 8D B9 60 08 00 00            lea rdi, [rcx + 0x860]
002EDAEA  48 8B CF                        mov rcx, rdi
002EDAED  E8 EE 01 F6 FF                  call 0x14024dce0
002EDAF2  45 33 C9                        xor r9d, r9d
002EDAF5  45 33 C0                        xor r8d, r8d
002EDAF8  48 8B D6                        mov rdx, rsi
002EDAFB  48 8B CD                        mov rcx, rbp
002EDAFE  8A D8                           mov bl, al
002EDB00  E8 7F C9 20 00                  call 0x1404fa484
002EDB05  48 8B CF                        mov rcx, rdi
002EDB08  8A D3                           mov dl, bl
002EDB0A  48 8B F0                        mov rsi, rax
002EDB0D  E8 DE 33 00 00                  call 0x1402f0ef0
002EDB12  EB A7                           jmp 0x1402edabb
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall RtlpHpVaMgrCtxAlloc(__int64 a1, __int64 a2, __int64 a3, __int64 a4)
{
    __int64 result;
    __int64 v_rsi;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p18;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rbp;
    v_stack_p18 = v_rsi;
    v_rsp = (v_rsp) - (32);
    if (((unsigned int)((unsigned int)(*(unsigned int *)(a4)))) == -1) goto loc_002EDAE3;
    result = ((unsigned int)(*(unsigned int *)(a4))) + (45);
    v_rsi = (result + result * 2) << (4);
    v_rsi = (v_rsi) + (a1);
loc_002EDABB:
    result = RtlpHpVaMgrAlloc(v_rsi, a2, a3, a4);
    v_rsp = (v_rsp) + (32);
    return result;
loc_002EDAE3:
    result = ExAcquireSpinLockShared(v_rsi + 2144, a2, a3, a4);
    a4 = 0;
    a3 = 0;
    result = RtlpHpVaMgrCtxAllocatorFind(v_stack_p10, v_stack_p18, a3, a4);
    result = ExReleaseSpinLockShared(v_rsi + 2144, (unsigned __int8)((unsigned __int8)(result)), a3, a4);
    goto loc_002EDABB;
}
```

## 5. (Beta) C Style

```c
int64_t RtlpHpVaMgrCtxAlloc(void *Arg1, int64_t Arg2, int64_t Arg3, void *Arg4)
{
    uint8_t *arg1 = (uint8_t *)Arg1;
    uint8_t *arg4 = (uint8_t *)Arg4;

    int64_t result;
    int64_t local_rsi;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p18;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rbp;
    v_stack_p18 = local_rsi;
    local_rsp = (local_rsp) - (32);
    if (((uint32_t)((uint32_t)(*(uint32_t *)(arg4)))) == -1) goto loc_002EDAE3;
    result = ((uint32_t)(*(uint32_t *)(arg4))) + (45);
    local_rsi = (result + result * 2) << (4);
    local_rsi = (local_rsi) + (Arg1);
loc_002EDABB:
    result = RtlpHpVaMgrAlloc(local_rsi, Arg2, Arg3, Arg4);
    local_rsp = (local_rsp) + (32);
    return result;
loc_002EDAE3:
    result = ExAcquireSpinLockShared(local_rsi + 2144, Arg2, Arg3, Arg4);
    Arg4 = 0;
    Arg3 = 0;
    result = RtlpHpVaMgrCtxAllocatorFind(v_stack_p10, v_stack_p18, Arg3, Arg4);
    result = ExReleaseSpinLockShared(local_rsi + 2144, (uint8_t)((uint8_t)(result)), Arg3, Arg4);
    goto loc_002EDABB;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x860` | `64` | `R` |
| `Arg4` | `+ 0x0` | `32` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x002EDA80&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_002EDA80[BB_002EDA80]
  bb_002EDAAC[BB_002EDAAC]
  bb_002EDABB[BB_002EDABB]
  bb_002EDAE2[BB_002EDAE2]
  bb_002EDAE3[BB_002EDAE3]
  bb_002EDA80 -->|branch| bb_002EDAE3
  bb_002EDA80 -->|fallthrough| bb_002EDAAC
  bb_002EDAAC -->|flow| bb_002EDABB
  bb_002EDAE2 -->|flow| bb_002EDAE3
  bb_002EDAE3 -->|branch| bb_002EDABB
```
