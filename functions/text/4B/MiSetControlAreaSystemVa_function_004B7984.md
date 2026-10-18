# MiSetControlAreaSystemVa

- RVA: `0x004B7984`–`0x004B79DE` (길이 `90` bytes)
- VA: `0x00000001404B7984`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x00060BC4`
- 디코드: `25`개 명령, `90/90` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **2**; 고유 호출 대상: **2**
- 직접 호출자로 확인된 함수: **1**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x004B799C` → [ExAcquireSpinLockExclusive](../24/ExAcquireSpinLockExclusive_function_00248690.md) (function, `0x00248690`)
- `0x004B79C8` → [MiReleaseSpinLockExclusive](../24/MiReleaseSpinLockExclusive_function_002482C0.md) (function, `0x002482C0`)

### Direct callers
- [sub_00B2B51A](../../page/B2/Unknown_function_00B2B51A.md) at `0x00B2B53E`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
004B7984  48 89 5C 24 08                  mov qword ptr [rsp + 8], rbx
004B7989  48 89 74 24 10                  mov qword ptr [rsp + 0x10], rsi
004B798E  57                              push rdi
004B798F  48 83 EC 20                     sub rsp, 0x20
004B7993  48 8B F9                        mov rdi, rcx
004B7996  8B DA                           mov ebx, edx
004B7998  48 83 C1 48                     add rcx, 0x48
004B799C  E8 EF 0C D9 FF                  call 0x140248690
004B79A1  44 8B 4F 5C                     mov r9d, dword ptr [rdi + 0x5c]
004B79A5  48 8D 4F 48                     lea rcx, [rdi + 0x48]
004B79A9  0F BA 6F 38 1D                  bts dword ptr [rdi + 0x38], 0x1d
004B79AE  45 8B C1                        mov r8d, r9d
004B79B1  41 0F BA F0 10                  btr r8d, 0x10
004B79B6  41 0F BA E9 10                  bts r9d, 0x10
004B79BB  83 FB 01                        cmp ebx, 1
004B79BE  8A D0                           mov dl, al
004B79C0  45 0F 4C C8                     cmovl r9d, r8d
004B79C4  44 89 4F 5C                     mov dword ptr [rdi + 0x5c], r9d
004B79C8  E8 F3 08 D9 FF                  call 0x1402482c0
004B79CD  48 8B 5C 24 30                  mov rbx, qword ptr [rsp + 0x30]
004B79D2  48 8B 74 24 38                  mov rsi, qword ptr [rsp + 0x38]
004B79D7  48 83 C4 20                     add rsp, 0x20
004B79DB  5F                              pop rdi
004B79DC  C3                              ret
004B79DD  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall MiSetControlAreaSystemVa(__int64 a1, int a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_p10;
    unsigned __int64 v_stack_p8;

    v_stack_p8 = v_rbx;
    v_stack_p10 = v_rsi;
    v_rsp = (v_rsp) - (32);
    a1 = (a1) + (72);
    result = ExAcquireSpinLockExclusive(a1, a2, a3, a4);
    a4 = (unsigned int)(*(unsigned int *)(a1 + 92));
    if (((unsigned int)((unsigned int)(a2))) < 1) { a4 = (unsigned int)((unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 92))))); }
    *(unsigned int *)(a1 + 92) = (unsigned int)(a4);
    result = MiReleaseSpinLockExclusive(a1 + 72, (unsigned __int8)(result), (unsigned int)((unsigned int)((unsigned int)(*(unsigned int *)(a1 + 92)))), a4);
    v_rsp = (v_rsp) + (32);
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t MiSetControlAreaSystemVa(void *Arg1, int32_t Arg2)
{
    uint8_t *arg1 = (uint8_t *)Arg1;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_p10;
    uint64_t v_stack_p8;

    v_stack_p8 = local_rbx;
    v_stack_p10 = local_rsi;
    local_rsp = (local_rsp) - (32);
    Arg1 = (Arg1) + (72);
    result = ExAcquireSpinLockExclusive(Arg1, Arg2, a3, a4);
    a4 = (uint32_t)(*(uint32_t *)(arg1 + 0x5C));
    if (((uint32_t)((uint32_t)(Arg2))) < 1) { a4 = (uint32_t)((uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5C))))); }
    *(uint32_t *)(arg1 + 0x5C) = (uint32_t)(a4);
    result = MiReleaseSpinLockExclusive(Arg1 + 72, (uint8_t)(result), (uint32_t)((uint32_t)((uint32_t)(*(uint32_t *)(arg1 + 0x5C)))), a4);
    local_rsp = (local_rsp) + (32);
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg1` | `+ 0x38` | `32` | `R/W` |
| `Arg1` | `+ 0x48` | `64` | `R` |
| `Arg1` | `+ 0x5C` | `32` | `R` |
| `Arg1` | `+ 0x5C` | `32` | `W` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x004B7984&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_004B7984[BB_004B7984]
  bb_004B79DD[BB_004B79DD]
```
