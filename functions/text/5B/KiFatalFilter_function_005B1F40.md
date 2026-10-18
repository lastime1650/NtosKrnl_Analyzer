# KiFatalFilter

- RVA: `0x005B1F40`–`0x005B1F60` (길이 `32` bytes)
- VA: `0x00000001405B1F40`
- 실행 섹션: `.text`
- PDB 이름 있음: `예`; PDB Function 태그: `아니요`
- unwind 정보 RVA: `0x000622F0`
- 디코드: `9`개 명령, `32/32` bytes 표시
- 미해석 바이트: `0` (있으면 어셈블리에 `.byte`로 보존)

> 이 문서는 커널 이미지의 기계어와 PDB 기호를 분석해 생성했습니다. 4번과 5번은 함수 원형과 자료형을 바이너리 사용 방식에서 추정한 C 해석이며 원본 소스 복구 결과는 아닙니다.

## 1. Dependencies

- 직접 호출 지점: **1**; 고유 호출 대상: **1**
- 직접 호출자로 확인된 함수: **2**
- RIP 상대 이미지 참조: **0**

### Outgoing calls
- `0x005B1F5A` → [KeBugCheckEx](../4F/KeBugCheckEx_function_004FD660.md) (function, `0x004FD660`)

### Direct callers
- [KeExpandKernelStackAndCalloutInternal$filt$0](../6D/KeExpandKernelStackAndCalloutInternal_filt_0_function_006D1F50.md) at `0x006D1F61`
- [KiInitializeKernel$filt$0](../../pagelk/B8/KiInitializeKernel_filt_0_function_00B802D9.md) at `0x00B802EA`

### Static image references
- 디코드된 RIP-relative 메모리 참조가 없습니다.

## 2. Other-region calls and transfers

- 다른 실행 섹션으로 향하는 call: **0**
- 별도 외부 분기/꼬리 이동을 확인하지 못했습니다.

## 3. Assembly (complete function range)

```asm
005B1F40  48 83 EC 38                     sub rsp, 0x38
005B1F44  4C 8B 02                        mov r8, qword ptr [rdx]
005B1F47  48 8B 42 08                     mov rax, qword ptr [rdx + 8]
005B1F4B  4D 8B C8                        mov r9, r8
005B1F4E  48 89 44 24 20                  mov qword ptr [rsp + 0x20], rax
005B1F53  49 63 10                        movsxd rdx, dword ptr [r8]
005B1F56  4D 8B 40 10                     mov r8, qword ptr [r8 + 0x10]
005B1F5A  E8 01 B7 F4 FF                  call 0x1404fd660
005B1F5F  CC                              int3
```

## 4. C-style interpretation (structured pseudocode)

```c
__int64 __fastcall KiFatalFilter(__int64 a1, __int64 a2)
{
    __int64 result;
    __int64 v_rsp;
    unsigned __int64 v_stack_m18;

    v_rsp = (v_rsp) - (56);
    v_stack_m18 = *(unsigned __int64 *)(a2 + 8);
    result = KeBugCheckEx(a1, (int)(*(unsigned int *)(*(unsigned __int64 *)(a2))), *(unsigned __int64 *)(*(unsigned __int64 *)(a2) + 16), *(unsigned __int64 *)(a2));
    return result;
}
```

## 5. (Beta) C Style

```c
int64_t KiFatalFilter(int64_t Arg1, void *Arg2)
{
    uint8_t *arg2 = (uint8_t *)Arg2;

    int64_t result;
    int64_t local_rsp;
    uint64_t v_stack_m18;

    local_rsp = (local_rsp) - (56);
    v_stack_m18 = *(uint64_t *)(arg2 + 0x8);
    result = KeBugCheckEx(Arg1, (int32_t)(*(uint32_t *)(*(uint64_t *)(arg2))), *(uint64_t *)(*(uint64_t *)(arg2) + 0x10), *(uint64_t *)(arg2));
    return result;
}
```

### 관측된 메모리 오프셋

구조체 형식이 확인되지 않은 접근은 인자 기준의 오프셋으로만 기록했습니다.

| 기준 인자 | 오프셋 표현 | 폭 (bit) | 접근 |
|---|---:|---:|---|
| `Arg2` | `+ 0x0` | `64` | `R` |
| `Arg2` | `+ 0x8` | `64` | `R` |

## 6. Execution-region graph

[열기: 2D/3D 그래프와 함수 탐색 컨트롤 패널](../../../control-panel.html?section=text&rva=0x005B1F40&view=graph)

- 2D 그래프는 위에서 아래로 흐르고, 3D 그래프는 빈 공간을 드래그해 회전합니다. Shift+드래그는 이동, 휠은 확대·축소, 함수 노드 선택은 대상 보고서 이동입니다.

### Static fallback

```mermaid
flowchart TD
  bb_005B1F40[BB_005B1F40]
```
